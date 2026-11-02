from app.llm import evaluate_results, extract_profile_with_llm, generate_search_query
from app.schemas import CompanyEvaluationRequest, ProfileText, Profile
from fastapi import FastAPI

app = FastAPI(title="profile-to-company-discoverer",
              description="A service that discovers companies from your professional profiles",
              version="0.1.0")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/profile/extract", response_model=Profile)
def extract_profile(profile_text: ProfileText):
    #print(f"Received profile text: {profile_text.text[:200]}")
    return extract_profile_with_llm(profile_text.text)

@app.post("/profile/search")
def search_companies(profile: Profile):
    queries = generate_search_query(profile)
    return {"queries": queries}

@app.post("/profile/evaluate")
def evaluate_company(payload: CompanyEvaluationRequest):

    return evaluate_results(payload.profile, 
                            payload.title, 
                            payload.content, 
                            payload.url)
