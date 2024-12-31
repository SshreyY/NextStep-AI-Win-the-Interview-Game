import os
from langchain_groq import ChatGroq
from prompts.skillMatchPrompt import SKILL_MATCH_PROMPT
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

#Load environment variables from a .env file.
load_dotenv()

#init the LLM with GroqCloud API using the specified model and temperature settings
llm = ChatGroq(temperature=0, 
               groq_api_key=os.getenv("GROQ_API_KEY"), 
               model_name="llama-3.1-70b-versatile")

"""
    Match skills between a job posting and a resume.

    Args:
        jobPosting (str): The job posting content.
        resume (str): The resume content.
    
    Returns:
        dict: A dictionary of matched skills and relevant details.
"""
def matchSkills(jobPosting: str, resume: str) -> dict:

    #create a pipeline with the prompt and LLM
    chain_extract = SKILL_MATCH_PROMPT | llm

    #invoking the chain pipeline by passing these parameters
    result = chain_extract.invoke(input={"jobPosting": jobPosting, "resume": resume})

    #Parse the response into JSON format.
    try:
        json_parser = JsonOutputParser()
        result = json_parser.parse(result.content)
    except OutputParserException:
        #Raise an error if the response can't be parse
        raise OutputParserException("Context too big. Unable to parse jobs.")
    #return the resut as a list of dictionaries
    return result if isinstance(result, list) else [result]