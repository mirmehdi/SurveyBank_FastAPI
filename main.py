from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from typing import List, Optional
import pandas as pd
import os
import random

app = FastAPI()

security = HTTPBasic()

# Dummy user database
USER_DB = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine"
}

ADMIN_PASSWORD = "4dm1N"

# Ensure the file path is correct relative to the script's location
DATA_FILE = 'questions.csv'

def load_data(file_path: str):
    df = pd.read_csv(file_path)
    df.fillna('', inplace=True)
    return df.to_dict(orient='records')

def save_data(file_path: str, data):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

questions = load_data(DATA_FILE)

def authenticate(credentials: HTTPBasicCredentials):
    if credentials.username not in USER_DB or USER_DB[credentials.username] != credentials.password:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return credentials.username

def authenticate_admin(credentials: HTTPBasicCredentials):
    if credentials.username != "admin" or credentials.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="Forbidden")

@app.get("/healthcheck")
def healthcheck():
    return {"status": "API is functional"}

@app.get("/questions", response_model=List[dict])
def get_questions(
    use: Optional[str] = None,
    subjects: Optional[str] = Query(None),
    count: int = 5,
    credentials: HTTPBasicCredentials = Depends(security)
):
    user = authenticate(credentials)
    filtered_questions = questions
    
    if use:
        filtered_questions = [q for q in filtered_questions if q['use'] == use]

    if subjects:
        subjects_list = subjects.split(',')
        filtered_questions = [q for q in filtered_questions if q['subject'] in subjects_list]

    if len(filtered_questions) < count:
        raise HTTPException(status_code=400, detail="Not enough questions available")
    
    random.shuffle(filtered_questions)
    return filtered_questions[:count]

@app.post("/questions", status_code=201)
def add_question(new_question: dict, credentials: HTTPBasicCredentials = Depends(security)):
    authenticate_admin(credentials)
    questions.append(new_question)
    save_data(DATA_FILE, questions)
    return {"message": "Question added successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
