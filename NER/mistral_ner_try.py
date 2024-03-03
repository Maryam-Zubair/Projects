import fitz
import spacy
import re
import subprocess
import json
import requests

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        # converting each page into text 
        text += page.get_text()
    return text

def preprocess_text(raw_text):
    text = raw_text.strip()
    processed_text = ' '.join(text.split())
    return processed_text

def generate_response(prompt):
    curl_command = f"""curl -s http://localhost:11434/api/generate -d '{{"model": "ner", "prompt":"{prompt}"}}'"""
    process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    full_response = ""

    while True:
        output_line = process.stdout.readline()
        if not output_line and process.poll() is not None:
            break
        if output_line:
            try:
                response_data = json.loads(output_line.strip())
                full_response += response_data.get("response", "")
            except json.JSONDecodeError:
                return "Invalid response format", 500
    return full_response

def ner(text):
    # Regular Expressions:
    phone_number_pattern = re.compile(r'\b(?:\+?\d{1,2}\s?)?(?:\()?(\d{3}(?:\))?)?\s?[-.\s]?(\d{3})[-.\s]?((?!20\d{2}|21[0-2]\d|22[0-1]\d|2220)[0-9]{4})\b')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    # Regular expression for education section to extract the last year
    education_year_pattern = re.compile(r'(Master’s|Bachelor’s)[^\d]*(\d{4}(?:-(\d{4}))?)', re.IGNORECASE)
    # Using Customized model
    nlp = spacy.load(r"/Users/maryamz/Desktop/PROJECTS/Resume/output/model-best")
    doc = nlp(text)

    # Find and print phone numbers using regular expression if not found by the model
    if not any(ent.label_ == 'Phone' for ent in doc.ents):
        phone_numbers = phone_number_pattern.findall(text)
        for match in phone_numbers:
            formatted_number = '-'.join(part for part in match if part)
            print(formatted_number, ": Phone Number")

    # Find and print email addresses using regular expression if not found by the model
    if not any(ent.label_ == 'Email Address' for ent in doc.ents):
        email_addresses = email_pattern.findall(text)
        for email in email_addresses:
            print(email, ": Email Address")
        
    graduation_years = []
    matches = education_year_pattern.finditer(text)
    for match in matches:
        start, end = match.span()
        line = text[start:end]
        years_match = re.findall(r'\b(\d{4}(?:-(\d{4}))?)\b', line)
        if years_match:
            graduation_years.append(years_match[-1][1] if years_match[-1][1] else years_match[-1][0])
    # Print the extracted graduation years
    for year in graduation_years:
        print(year, ": Graduation Year")

    # Entities :
    for ent in doc.ents:
        # To print skills only
        if ent.label_ == 'Skills':
            lower_text = ent.text.lower()
            target_words = ['projects', 'work experience']
            for target_word in target_words:
                index = lower_text.find(target_word)
                if index != -1:
                    skills = ent.text[:index].strip()
                    print(skills, ":", ent.label_)
                    break
        else:
            print(ent.text, ": ",ent.label_)


def get_answer():
    pdf_path = "/Users/maryamz/Desktop/PROJECTS/Resume/Maryam_Zubair.pdf"
    resume_text = extract_text_from_pdf(pdf_path)
    plain_data = preprocess_text(resume_text)
    response = generate_response(plain_data)
    output = ner(plain_data)
    print(response)

if __name__ == '__main__':
    get_answer()