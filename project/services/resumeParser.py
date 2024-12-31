from langchain.text_splitter import RecursiveCharacterTextSplitter
import pdfplumber

"""
    Parse and process the text from an uploaded resume file.

    Args:
        uploaded_file: A file-like object representing the uploaded PDF file.
    
    Returns:
        str: Extracted and processed text from the resume.
    
    Raises:
        ValueError: If the uploaded file is not a valid PDF or if there are errors during parsing.
"""
def parseResume(uploaded_file) -> str:
    try:
        #validate the uploaded file extenstion and make sure its a pdf
        if not uploaded_file.name.endswith('.pdf'):
            raise ValueError("Invalid file type. Please upload a PDF resume.")

        #open and read the uploaded pdf file using pdfPlumber
        with pdfplumber.open(uploaded_file) as pdf:
            #extract the text from all pages that have text
            text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
            return text
    except Exception as e:
        raise ValueError(f"Error loading resume: {str(e)}")
    
    document = loader.load()
    text = " ".join(doc.page_content for doc in document)

    #use langchain's recursiveCharacterTextSplitter for chunking the extracted text
    text_splitter = RecursiveCharacterTextSplitter(
        #maximum size of each chunk
        chunk_size = 1000,
        #overlap between chunks for context preservation
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)

    #combine the split chunks back into a single str for further processing.
    return " ".join(chunks)