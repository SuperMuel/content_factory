from crewai import Task
from content.constants import FORBIDDEN_TERMS


class Tasks:
    def __init__(
        self,
        search_tool,
        news_researcher,
        content_evaluator,
        summarizer,
        content_verifier,
        social_media_writer,
    ):
        self.search_tool = search_tool
        self.news_researcher = news_researcher
        self.content_evaluator = content_evaluator
        self.summarizer = summarizer
        self.content_verifier = content_verifier
        self.social_media_writer = social_media_writer

    def search_task(self, subject):
        return Task(
            description=(
                f"Use the search tool to find the latest news articles on {subject}. "
                "Return a list of relevant articles."
            ),
            expected_output="A list of relevant news articles with links and summaries.",
            tools=[self.search_tool],
            agent=self.news_researcher,
        )

    def compare_task(self):
        return Task(
            description=(
                "Evaluate the list of news articles and select the top 3 based on relevance and quality."
            ),
            expected_output="A list of the top 3 selected news articles.",
            tools=[],
            agent=self.content_evaluator,
        )

    def summarize_task(self):
        return Task(
            description=(
                "Summarize the top 3 selected news articles. "
                "Each summary should be concise and capture the key points of the article, as well as interesting insights, quotes or facts."
            ),
            expected_output="Summaries of the top 3 news articles.",
            tools=[],
            agent=self.summarizer,
        )

    def verify_task(self):
        return Task(
            description=(
                "Verify that the LinkedIn post does not contain any forbidden terms. "
                "If forbidden terms are found, rewrite the post to adhere to the guidelines. "
                f"Here are the forbidden terms: \n {FORBIDDEN_TERMS}"
            ),
            expected_output="A verified and possibly revised LinkedIn post.",
            tools=[],
            agent=self.content_verifier,
        )

    def write_task(self):
        return Task(
            description=(
                "Generate a LinkedIn post based on the summarized news articles. "
                "The post should be professional, engaging, and suitable for a LinkedIn audience."
            ),
            expected_output="A LinkedIn post ready for publishing.",
            tools=[],
            agent=self.social_media_writer,
        )
