from typing import Optional

from crewai import Crew
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

from content.agents import Agents
from content.tasks import Tasks

gpt3_5 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)  # type: ignore
gpt4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

claude_haiku = ChatAnthropic(model_name="claude-3-haiku-20240307")
claude_sonnet = ChatAnthropic(model_name="claude-3-sonnet-20240229")


class LinkedinCrew:
    def __init__(self, subject: str, language: str = "EN", example_linkedin_posts: Optional[str] = None):
        self.subject = subject
        self.language = language
        self.example_linkedin_posts = example_linkedin_posts

    def run(self):
        # Initialize custom agents and tasks
        agents = Agents(llm=claude_haiku)
        tasks = Tasks(
            search_tool=agents.search_tool,
            news_researcher=agents.news_researcher(),
            content_evaluator=agents.content_evaluator(),
            summarizer=agents.summarizer(),
            content_verifier=agents.content_verifier(),
            social_media_writer=agents.social_media_writer(),
            example_linkedin_posts=self.example_linkedin_posts,
        )

        # Define tasks with relevant agents
        search_task = tasks.search_task(self.subject)
        compare_task = tasks.compare_task()
        summarize_task = tasks.summarize_task()
        write_task = tasks.write_task()
        verify_task = tasks.verify_task()

        # Form the crew with the defined agents and tasks
        crew = Crew(
            agents=[
                agents.news_researcher(),
                agents.content_evaluator(),
                agents.summarizer(),
                agents.social_media_writer(llm=claude_sonnet),
                agents.content_verifier(),
            ],
            tasks=[search_task, compare_task, summarize_task, write_task, verify_task],
            verbose=True,
        )

        # Kick off the crew with the specified subject
        return crew.kickoff(inputs={"subject": self.subject, "language": self.language})


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Linkedin Crew! ##")
    print("-------------------------------")
    subject = input("Enter the subject: ")

    custom_crew = LinkedinCrew(subject)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is the Linkedin post :")
    print("########################\n")
    print(result)
