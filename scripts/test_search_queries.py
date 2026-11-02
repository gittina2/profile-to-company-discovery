from app.schemas import Profile
from app.llm import generate_search_query

profile_test = Profile(
    profile_summary="Software Engineer with experience in Python and Data Analysis.",
    expertise_areas=["Software Engineering", "Data Analysis"],
    technical_methods=["Python", "SQL", "Machine Learning"],
    work_activities=["Developing software applications", "Analyzing data sets"],
    interests=["Open Source Software", "Artificial Intelligence"],
    preferred_activities=["Working on innovative projects", "Collaborating with cross-functional teams"],
    constraints=[],
    domains_to_explore=[])

queries = generate_search_query(profile_test)

for i, q in enumerate(queries, start=1):
    print(f"Query {i}: {q}")
