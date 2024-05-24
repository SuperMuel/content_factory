import streamlit as st
import os

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = st.secrets["openai_api_key"]

if not os.environ.get("SERPER_API_KEY"):
    os.environ["SERPER_API_KEY"] = st.secrets["serper_api_key"]

if not os.environ.get("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = st.secrets["anthropic_api_key"]

from content.linkedin_crew import LinkedinCrew

st.title("Content Factory")

# Language selector
language = st.selectbox(
    "Select the language for the post",
    ["EN","FR"],
)

topic = st.text_input("Enter the topic of the post")

if clicked := st.button("Generate a Linkedin Post"):
    with st.spinner("Generating content..."):
        linkedin_crew = LinkedinCrew(subject=topic, language=language)
        result = linkedin_crew.run()

    st.subheader("Generated LinkedIn Post")
    st.write(result)
