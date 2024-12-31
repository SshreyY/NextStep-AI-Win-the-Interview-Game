from langchain_community.document_loaders import WebBaseLoader

"""
    Scrape job posting content from a given URL.

    Args:
        job_url (str): The URL of the job posting.
    
    Returns:
        str: The content of the job posting.
"""
def scarpeJobPosting(job_url: str) -> str:

    #load the webpage content
    loader = WebBaseLoader(job_url)
    
    #Extract and return the job posting content
    job_data = loader.load().pop().page_content
    return job_data

