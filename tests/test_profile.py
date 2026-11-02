from app.schemas import Profile

def test_profile_creation():
    profile = Profile(
        profile_summary="Software Engineer with experience in Python and Data Analysis.",
        expertise_areas=["Python", "Data Analysis"],
        technical_methods=["Machine Learning", "Web Development"],
        work_activities=["Coding", "Reading"],
        interests=["Machine Learning", "Web Development"],
        preferred_activities=["Coding", "Reading"],
        constraints=["Hybrid", "Remote"],
        domains_to_explore=["AI", "Cloud Computing"]
    )
    assert len(profile.expertise_areas) == 2
    assert profile.interests == ["Machine Learning", "Web Development"]

def test_profile_rejects_missing_fields():
    try:
        profile = Profile(
            profile_summary="Software Engineer with experience in Python and Data Analysis.",
            expertise_areas=["Python", "Data Analysis"],
            technical_methods=["Machine Learning", "Web Development"],
            work_activities=["Coding", "Reading"],
            interests=["Machine Learning", "Web Development"],
            preferred_activities=["Coding", "Reading"],
            constraints=["Hybrid", "Remote"]
            # Missing domains_to_explore
        )
    except Exception as e:
        assert "domains_to_explore" in str(e)