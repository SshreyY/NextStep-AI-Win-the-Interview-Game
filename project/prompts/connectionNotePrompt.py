from langchain.prompts import PromptTemplate
CONNECTION_NOTE_PROMPT = PromptTemplate.from_template(
    """
    ### Matched Details:
    {matchedDetails}

    ### Instruction:
    Write a maximum of 200-character LinkedIn personalized connection note using the name in the resume and skills in the resume to a {recipient_type}. 
    Mention a key skill or experience and express a desire to connect.
    """
)


