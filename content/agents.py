from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI


class Agents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)  # type: ignore
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.search_tool = SerperDevTool(
            search_url="https://google.serper.dev/news",
            n_results=5,
            # TODO : localize the search
        )

    def news_researcher(self):
        return Agent(
            role="News Researcher",
            backstory="You are a diligent news researcher, always on the lookout for the most recent and relevant news.",
            goal="Find the latest news on {subject}",
            tools=[self.search_tool],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=self.OpenAIGPT35,
        )

    def content_evaluator(self):
        return Agent(
            role="Content Evaluator",
            backstory="As a content evaluator, you have a keen eye for detail and can identify the most valuable articles.",
            goal="Evaluate and select the top 3 news articles on {subject}",
            tools=[],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=self.OpenAIGPT35,
        )

    def summarizer(self):
        return Agent(
            role="Summarizer",
            backstory="You are skilled at summarizing complex information into concise and understandable summaries.",
            goal="Summarize the top 3 news articles on {subject}",
            tools=[],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=self.OpenAIGPT35,
        )

    def social_media_writer(self):
        return Agent(
            role="Social Media Writer",
            backstory="You craft engaging and professional LinkedIn posts that resonate with the audience.",
            goal="Generate a LinkedIn post based on the summarized news articles",
            tools=[],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=self.OpenAIGPT35,
        )

    def content_verifier(self):
        return Agent(
            role="Content Verifier",
            backstory="You are meticulous and have a keen eye for detail, ensuring that the content adheres to specified guidelines.",
            goal="Ensure the LinkedIn post does not contain forbidden terms and rewrite it if necessary",
            tools=[],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=self.OpenAIGPT35,
        )
