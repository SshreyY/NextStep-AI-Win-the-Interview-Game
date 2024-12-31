from langchain.prompts import PromptTemplate

EMAIL_PROMPT = PromptTemplate.from_template(
    """
    ### Matched Details:
    {matchedDetails}

    ### Instruction:
    cold emails should be 5-15 lines of text or 50-150 words. 
    Craft a {recipient_type} for this person using this:  structure, explanantion, and use the example:
    1) Use Short Openers, Open with a basic phrase, for cordialities. If possiblem try to make the message personable. Example: "Hello [name]", "Hello recuriter or hiring manager", "Hello [name], I hope you have been well" 
    2) Start with a quick intro, Present your school and/or major. Bonus points for a unique experince or value proposition. Example: "I am a current junior majoring in finance who's interacted with business owners utilizing tech solutions"
    3) Provide a reason(s) to listen (credibility), Express strengths or experinces relating to the field. IT should include some personal strengths and answer a readers "why should I respond to you. Example: "I love a challenge and as a growth oriented individual, your company's reputation for a strong work environmental interests me."
    4) Close with a purpose, end the message with what you are looking to do. Example: "I'd love to learn a little more about your experince!"

    """
)