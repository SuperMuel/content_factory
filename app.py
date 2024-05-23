import streamlit as st
from content.linkedin_crew import LinkedinCrew
import os

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = st.secrets["openai_api_key"]

if not os.environ.get("SERPER_API_KEY"):
    os.environ["SERPER_API_KEY"] = st.secrets["serper_api_key"]

if not os.environ.get("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = st.secrets["anthropic_api_key"]

st.title("Content Factory")


topic = st.text_input("Enter the topic of the post")

if clicked := st.button("Generate a Linkedin Post"):
    with st.spinner("Generating content..."):
        linkedin_crew = LinkedinCrew(subject=topic)
        result = linkedin_crew.run()

    st.subheader("Generated LinkedIn Post")
    st.write(result)
