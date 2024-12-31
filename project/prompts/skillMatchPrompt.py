from langchain.prompts import PromptTemplate


SKILL_MATCH_PROMPT = PromptTemplate.from_template(
    """
    ### Job Posting:

    {jobPosting}

    ### Resume:

    {resume}

    ### Instruction:

    I want you to analyze the job posting and my resume to find the strongest overlaps between my skills and experiences and the job requirements. Highlight the specific technical and soft skills I have that match what the job is looking for. Then, explain why I would be a great fit for this role based on my background and strengths. Please format the response in JSON like this:

    {{
        "matched_skills": ["list of my most relevant skills that align with the job"],
        "matched_experience": ["summary of my most relevant experiences and accomplishments"],
        "fit_reasoning": "a clear explanation of why I am a strong candidate for this role"
    }}
    """
)