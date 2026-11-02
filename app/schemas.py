
from pydantic import BaseModel


class Profile(BaseModel):
    profile_summary: str
    expertise_areas: list[str]
    technical_methods: list[str]
    work_activities: list[str]
    interests: list[str]
    preferred_activities: list[str]
    constraints: list[str]
    domains_to_explore: list[str]

class ProfileText(BaseModel):
    text: str


class CompanyEvaluation(BaseModel):
    company_name: str
    company_description: str
    profile_fit_reasons: list[str]
    evidence_url: str
    confidence: str

class CompanyEvaluationRequest(BaseModel):
    profile: Profile
    title: str
    url: str
    content: str


    
