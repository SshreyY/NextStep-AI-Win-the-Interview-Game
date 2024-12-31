import uuid
import chromadb
from chromadb.config import Settings
from langchain_community.vectorstores import Chroma

#initialize ChromaDB client with settings allowing to reset.
client = chromadb.Client(Settings(allow_reset = True))
collection_name = "resumeSession"

def chromaReset():
    """Reset ChromaDB for a fresh session"""
    #Clears all data in ChromaDB to ensure no data overlap between sessions
    client.reset()

def storeResume(resumeText: str, metadata: dict):
    """Store the resume details in ChromaDB to help us with semantic mataching."""
    #making sure that the vector based db is fresh for each session and each resume upload, so that it doesn't overlap with anyone else resume
    chromaReset()

    #create a collection if it doesn't exist
    collections = client.get_or_create_collection(name= collection_name)

    #Generate UUID if no id is provided in metadata
    resume_id = str(metadata.get("id", uuid.uuid4()))

    #adding the resume text and metadata to the collection
    collections.add(
        documents=[resumeText],
        metadatas=[metadata],
        ids=[resume_id],
    )
    