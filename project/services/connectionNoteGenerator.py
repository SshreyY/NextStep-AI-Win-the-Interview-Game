import os
from langchain_groq import ChatGroq
from prompts.connectionNotePrompt import CONNECTION_NOTE_PROMPT 
from dotenv import load_dotenv

#load the env variables from the .env file
load_dotenv()

#init the LLM with GroqCloud API using the specified model and temperature settings
llm = ChatGroq(temperature=0.7, 
               groq_api_key=os.getenv("GROQ_API_KEY"), 
               model_name="llama-3.1-70b-versatile")


"""
    Generate a personalized connection note based on matched details and recipient type.

    Args:
        matchedDetails (dict): A dictionary of details matched between a resume and job posting.
        recipient_type (str): The type of recipient for the connection note.
    
    Returns:
        str: A formatted connection note with subject and body.
"""
def generateConnectionNote(matchedDetails: dict, recipient_type: str) -> str:

    #format matched details to include reciepient type in each detail
    matchedDetails = [{'recipient_type': recipient_type, 'data': detail} for detail in matchedDetails]
    
    #create a pipeline with the prompt and LLM
    chain_extract =  CONNECTION_NOTE_PROMPT | llm

    #invoking the chain pipeline by passing these parameters 
    res = chain_extract.invoke(input={'matchedDetails': matchedDetails, 'recipient_type': recipient_type})
    
    #now we are going to breakdown the AI response into subject and body format
    subject = res.content.split("\n\n")[0]
    body = "\n\n".join(res.content.split("\n\n")[1:])

    #formating the response for the UI
    connectionNote = f"Subject: {subject}\n\n{body}"
    return connectionNote