import streamlit as st
import os

# st.logo('images/sociaty-logo2.svg') # needs streamlit==1.35.0

if not os.environ.get("OPENAI_API_KEY"):
	os.environ["OPENAI_API_KEY"] = st.secrets["openai_api_key"]

if not os.environ.get("SERPER_API_KEY"):
	os.environ["SERPER_API_KEY"] = st.secrets["serper_api_key"]

if not os.environ.get("ANTHROPIC_API_KEY"):
	os.environ["ANTHROPIC_API_KEY"] = st.secrets["anthropic_api_key"]

from content.linkedin_crew import LinkedinCrew

st.title("Content Factory")

with st.expander("Put the linkedin posts you like here"):
	example_linkedin_posts = st.text_area("", height=200, key="example_linkedin_posts")

	st.caption(
		"Give us one or more linkedin posts you like, and we will generate similar posts for you. Separate them by ------")

# Language selector
language = st.selectbox(
	"Select the language for the post",
	["FR", "EN"],
)

topic = st.text_input("Enter the topic of the post", placeholder="GPT4o")

if clicked := st.button("Generate a Linkedin Post"):
	with st.spinner("Generating content..."):
		linkedin_crew = LinkedinCrew(subject=topic,
									 language=language,
									 example_linkedin_posts=example_linkedin_posts,
									 )
		result = linkedin_crew.run()  # TODO handle error

	st.subheader("Generated LinkedIn Post")

	st.code(result, language="markdown")

# To show output in an expander : https://github.com/amadad/civic-agentcy/blob/main/src/civic_agentcy/crew.py
