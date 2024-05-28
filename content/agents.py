from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_anthropic import ChatAnthropic

claude3Sonnet = ChatAnthropic(model_name="claude-3-sonnet-20240229")

class Agents:
    def __init__(self, llm):
        self.llm = llm

        self.search_tool = SerperDevTool(
            search_url="https://google.serper.dev/news",
            # TODO : Do multiple searches with selected location(s)
        )

    def news_researcher(self, llm=None):
        return Agent(
            role="News Researcher",
            backstory="You are a diligent news researcher, always on the lookout for the most recent and relevant news.",
            goal="Find the latest news on {subject}",
            tools=[self.search_tool],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=llm or self.llm,
        )

    def content_evaluator(self, llm=None):
        return Agent(
            role="Content Evaluator",
            backstory="As a content evaluator, you have a keen eye for detail and can identify the most valuable articles.",
            goal="Evaluate and select the top 3 news articles on {subject}", # TODO : Add more details
            tools=[],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=llm or self.llm,
        )

    def summarizer(self, llm=None):
        return Agent(
            role="Summarizer",
            backstory="You are skilled at summarizing complex information into concise and understandable summaries.",
            goal="Summarize the top 3 news articles on {subject}",
            tools=[],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=llm or self.llm,

        )

    def social_media_writer(self, llm=None):
        return Agent(
            role="Social Media Writer",
            backstory="You are the world's best LinkedIn copywriter, writing for top CEOs. You conduct research on "
                      "current events and wants to share it with your audience."
                      "You excel at crafting LinkedIn posts using the most suitable copywriting framework. "
                      "Your tone is natural, direct, educational and informal. "
                      "You focus on the content. "
                      "You excel at imitating the style of others linkedin posts and can generate similar posts. "
                      "You are a native speaker of the {language} language. You write linkedin posts in that language.",

            goal="Generate a perfect LinkedIn post based on the news on {subject} in the {language} "
                 "language",
            tools=[],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=llm or self.llm,
        )

    def content_verifier(self, llm=None):
        return Agent(
            role="Content Verifier",
            backstory="You are meticulous and have a keen eye for detail, ensuring that the content adheres to "
                      "specified guidelines.",
            goal="Ensure the LinkedIn post does not contain forbidden terms and rewrite it if necessary, using the "
                 "same language.",
            tools=[],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=llm or self.llm,
        )
