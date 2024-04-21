import json
from fastapi import FastAPI, File, UploadFile, Request, Form, HTTPException
from typing import Union, Optional, List, Dict
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import fitz
import tempfile
from extractor import ParseResume
from jobsearch import JobExtractor
from typing import Optional 
from llm_response import get_completion_from_llm
from llm_response import chatbot
from geolocation import get_city_name


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # List of allowed origins (React app URL)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Location(BaseModel):
    latitude: float
    longitude: float

class ChatbotRequest(BaseModel):
    job_description: str
    user_query: str
    user_resume : bytes
    chat_history: List[Dict[str, str]] = []

def read_single_pdf(upload_file):
    text = ""  # Initialize text variable with an empty string
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            # Save uploaded file to a temporary file
            content = upload_file.read()  
            temp_file.write(content)
            temp_file_path = temp_file.name  
            doc = fitz.open(temp_file_path)
            for page_num in range(doc.page_count):
                page = doc[page_num]
                # converting each page into text 
                text += page.get_text()

    except Exception as e:
        print("Error reading file")

    return text  # Move the return statement outside the try-except block

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/query")
async def handle_query(
    message: str = Form(...),
    chatHistory: str = Form(...),
    jobDescription: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)):
    
    # Deserialize the JSON strings into Python objects
    message_data = json.loads(message)
    chat_history_data = json.loads(chatHistory)

    # Optionally handle the file
    resume_text = ""
    if file:
        file_content = await file.read()
        print(f"Received File: {file.filename}")
        
        # Convert PDF to text
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file_content)
            temp_file_path = temp_file.name

        doc = fitz.open(temp_file_path)
        for page_num in range(doc.page_count):
            page = doc[page_num]
            resume_text += page.get_text()

    # Extract the user_query from the message_data dictionary
    user_query = message_data.get("content", "")

    # Call the chatbot function
    response = chatbot(jobDescription, user_query, resume_text, chat_history_data)

    return {"response": response}

    
@app.post("/resume_process/")
async def resume_pdf_to_text(file: UploadFile = File(...)):
    data = read_single_pdf(file.file)
    json_txt = get_completion_from_llm(data)
    start_index = json_txt.find("{")
    json_txt = json_txt[start_index:]
    json_data = json.loads(json_txt)
    parser = ParseResume(json_data)
    formatted_resume = parser.get_formatted_resume()
    return {"parsed_keywords": formatted_resume,
            "keywords": json_data}

@app.post("/extract_jobs/")
async def extract_jobs(
        keywords: str = Form(...), 
        location: str = Form(...),
        datePosted: Optional[int] = Form(None),
        results: Optional[int] = Form(None),
        resume_file: Optional[UploadFile] = File(None)
    ):

    # Basic validation
    if not 0 < len(location) <= 100:  # Example length check for 'location'
        raise HTTPException(status_code=422, detail="Invalid 'location' length.")
        
    if datePosted not in [None, 24, 48, 168]:  # Example allowed values for 'datePosted'
        raise HTTPException(status_code=422, detail="Invalid 'datePosted' value.")
        
    if results is not None and (results < 1 or results > 100):  # Results range check
        raise HTTPException(status_code=422, detail="Invalid 'results' range.")
    
    try:  
        
        resume_data = read_single_pdf(resume_file.file)  
        job_extractor = JobExtractor(resume_data, location, datePosted, int(results))
        job_data = job_extractor.get_job()
        # print(job_data)
        return {"job_data": job_data}
    except Exception as e:  
        print(f"Error during job extraction: {e}") 
        raise HTTPException(status_code=500, detail="An error occurred while extracting jobs.")

# @app.post("/extract_jobs/")
# async def extract_jobs(file: UploadFile = File(...)):
#     data = read_single_pdf(file.file)
#     json_txt = get_completion_from_llm(data)
#     json_data = json.loads(json_txt)
#     parser = ParseResume(json_data)
#     job_extractor = JobExtractor(json_data)
#     job_data = job_extractor.get_job()
#     print(job_data)
#     return {"job_data": job_data}

@app.post("/get-city/")
async def get_city(location: Location):
    print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    try:

        city_name = await get_city_name(location.latitude, location.longitude)
        if city_name in ["API key not found", "Could not retrieve the city name", "City name not found"]:
            raise HTTPException(status_code=404, detail=city_name)
        return {"city": city_name}
    except Exception as e:
        print(f"Error during city extraction: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while extracting city name.")
    

# @app.post("/chatbot")
# async def chatbot_endpoint(request: ChatbotRequest):
#     job_description = request.job_description
#     user_query = request.user_query
#     user_resume = request.user_resume
#     chat_history = request.chat_history

#     # naming the pdf
#     if user_resume:
#         with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#             temp_file.write(user_resume)
#             temp_file_path = temp_file.name

#         # Convert PDF to text
#         doc = fitz.open(temp_file_path)
#         resume_text = ""
#         for page_num in range(doc.page_count):
#             page = doc[page_num]
#             resume_text += page.get_text()

#     # Pass the resume_text to the chatbot function
#     response = chatbot(job_description, user_query, resume_text)
#     return {"response": response}
