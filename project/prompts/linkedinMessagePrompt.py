from langchain.prompts import PromptTemplate

LINKEDIN_MESSAGE_PROMPT = PromptTemplate.from_template(
    """
    ### Matched Details:
    {matchedDetails}

    ### Instruction:

    Use this information below is quotes to help you craft my message after the quotes:
    What would a better cold DM look like?

    "1 Show Value
    Here’s a much better version
    Subject: 👋 Data Infra at Flexport?
    Hi Jim,
    I know your company’s in a later-growth stage business. From your JD, your data team seems to be at a critical stage of growth.
    I’ve spent the last year understanding modern data stacks (Spark + Kubernetes) in-depth in an academic setting. Beyond that, I’ve had over 5 years of technical experience. I would jump at the chance to see the early stages of implementation at a hyper-growth startup.
    Here’s my resume, I’d love to chat further.
    This DM catches my eye. It’s specific to the job description, and shows the candidate has done their research. More importantly, it shows you understand where the business is and where it’s headed; business acumen is valuable regardless of level.

    2 Make it a relationship
    Relational > Transactional. Whether it’s marketing or a job search, building relationships trumps transactions.
    “Do you have job opportunities” is direct, but it’s a transaction, and not a great return on investments for the hiring manager.
    Instead, ask to start a conversation about navigating your career. Senior-level professionals and hiring managers are increasingly putting their thoughts and personalities online, whether its’ LinkedIn, Twitter, Medium/Substack, or their own personal blogs. You can find what they’re thoughts are by doing a quick Google Search.
    For example, my blog shows nextgen data architectures are top-of-mind for me.
    Daliana’s blog and Twitter shows she’s helping folks break into Data Science from other fields.
    Do the work, and build a relationship. It may seem like a lot, but putting in this effort yields tremendous benefits. I have mentors I’ve reached out to and been reached out to in this way that I still chat and get career perspective from!"

    Now do this below using the above example:    
    Write a professional but conversational LinkedIn message to a {recipient_type}. 
    Mention the matched skills and experiences and express interest in the job. Keep it short and engaging.
    """
)
