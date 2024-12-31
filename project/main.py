import streamlit as st
from services.resumeParser import parseResume
from services.chromaDBinit import storeResume, chromaReset
from services.matcher import matchSkills
from services.emailGenerator import generateEmail
from services.linkedinMessageGenerator import generatelinkedInMessage
from services.connectionNoteGenerator import generateConnectionNote
from services.jobScraper import scarpeJobPosting
from prompts.skillMatchPrompt import SKILL_MATCH_PROMPT
from prompts.emailPrompt import EMAIL_PROMPT
from prompts.linkedinMessagePrompt import LINKEDIN_MESSAGE_PROMPT
from prompts.connectionNotePrompt import CONNECTION_NOTE_PROMPT

#sidebar navigation
st.sidebar.title("Let's Generate...")
page = st.sidebar.radio("Pick the type", ["Cold Email", "LinkedIn Message", "Connection Note"])

#Sidebar Inputs
st.sidebar.subheader("Common Inputs")
uploaded_file = st.sidebar.file_uploader("Upload your resume (PDF/Docx)", type=["pdf", "docx"])
job_url = st.sidebar.text_input("Enter Job Posting URL")
recipient_type = st.sidebar.selectbox("Who are you sending the message to?", ["Hiring Manager", "Recruiter"])

#Check if required inputs are present
if uploaded_file and job_url:
    resumeText = parseResume(uploaded_file)
    jobPosting = scarpeJobPosting(job_url)
    st.sidebar.success("Inputs ready!")

#Main Page Content based on the selected page
if page == "Cold Email":
    st.title("AI Message Generator - Cold Email")

    if st.button("Generate Cold Email"):
        if uploaded_file and job_url:
            #reset ChromaDB and store resume
            chromaReset()
            metadata = {"filename": uploaded_file.name}
            storeResume(resumeText, metadata)
            
            #match skills and generate the email
            matchedDetails = matchSkills(jobPosting, resumeText)
            email = generateEmail(matchedDetails, recipient_type)

            #display the generated email
            st.subheader("Generated Cold Email")
            st.write(email)
        else:
            st.error("Please upload a resume and provide a job posting URL.")

elif page == "LinkedIn Message":
    st.title("AI Message Generator - LinkedIn Message")

    if st.button("Generate LinkedIn Message"):
        st.cache_data.clear()
        if uploaded_file and job_url:
            #reset chromaDB and store resume
            chromaReset()
            metadata = {"filename": uploaded_file.name}
            storeResume(resumeText, metadata)

            #match skills and generate the linkedinmessage
            matchedDetails = matchSkills(jobPosting, resumeText)
            linkedin_message = generatelinkedInMessage(matchedDetails, recipient_type)

            #Display the generated linkedinMessage
            st.subheader("Generated LinkedIn Message")
            st.write(linkedin_message)
        else:
            st.error("Please upload a resume and provide a job posting URL.")

elif page == "Connection Note":
    st.title("AI Message Generator - Connection Note")

    if st.button("Generate Connection Note"):
        if uploaded_file and job_url:
            #reset ChromaDB and store resume 
            chromaReset()
            metadata = {"filename": uploaded_file.name}
            storeResume(resumeText, metadata)

            #match skills and generat ethe linkedIn connection Note
            matchedDetails = matchSkills(jobPosting, resumeText)
            connection_note = generateConnectionNote(matchedDetails, recipient_type)

            #display the generated connection note 
            st.subheader("Generated Connection Note")
            st.write(connection_note)
        else:
            st.error("Please upload a resume and provide a job posting URL.")