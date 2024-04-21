# Capstone Project

Follow these steps to set up the project:

1. Clone this repository

   ```bash
        git clone https://github.com/Alami64/Capstone_resume_project.git
   ```
## Install LLM Ollama
1. Download and Install Ollama on your computer from website: https://ollama.com

2. Using command line made custom prompt for model Resume :  Ollama create resume -f ./resume
3. Run Ollama on the backend
   ```bash
   ollama list
   ```

## Backend
1. Create a new virtual environment:
 ```bash
   python -m venv venv
   ```
2. Active the new virtual environment:
   - Linux:
    ```bash
      . venv/bin/activate
     ```
   - Windows:
   ```bash
   .\venv\Scripts\Activate
    ```
3. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```
4. Run application
   ```bash
      uvicorn main:app --reload
   ```
You should be able to access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000/)!

## Frontend
Follow these steps to set up the front-end project:

1. Navigate into the project directory
    ```bash
        cd frontend
    ```

2. Install npm dependences
    ```bash
        npm install
    ```

3. Run the frontend project
    ```bash
        npm run dev
    ```

You should be able to access the app at [http://localhost:5173/](http://localhost:5173/)!


# Job Recommendation System
