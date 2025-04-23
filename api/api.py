import os
from fastapi import FastAPI
from pydantic import BaseModel, PositiveInt, EmailStr
from dotenv import load_dotenv

app = FastAPI()

class Data(BaseModel):
    name: str
    contact: str
    linkedin_link: str
    github_link: str
    professional_experience: str
    academic_background: str
    skills: str
    objectives: str
    position: str
    vacancy_description: str

@app.post('/api/generate')
def generate_cv(data: Data):
    return {'message': 'Dados recebidos com sucesso!',
            'name': data.name,
            'contact': data.contact,
            'linkedin_link': data.linkedin_link,
            'github_link': data.github_link,
            'professional_experience': data.professional_experience,
            'academic_background': data.academic_background,
            'skills': data.skills,
            'objectives': data.objectives,
            'position': data.position,
            'vacancy_description': data.vacancy_description
            }