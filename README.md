# MSA English Test

**Shalahuddin Al-Ayyuby Schools**  
**Created by Mr. Ady Firman**

A computer-based English testing system. This starter version provides the initial FastAPI application and a health-check endpoint.

## Run locally on Windows

1. Install Python 3.11 or newer from https://www.python.org/downloads/ and enable **Add Python to PATH** during installation.
2. Open Command Prompt in this project folder.
3. Create and activate a virtual environment:

   ```bat
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:

   ```bat
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bat
   uvicorn main:app --reload
   ```

6. Open http://127.0.0.1:8000 in your browser.
7. API health check: http://127.0.0.1:8000/health

## Current status

This is only the starter foundation. Teacher authentication, database-backed exam/question management, importing, QR entry, grading, and live monitoring will be added in later stages. Do not use this starter version for real student data or live exams yet.
