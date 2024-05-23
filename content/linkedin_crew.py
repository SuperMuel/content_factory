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
    def __init__(self, subject):
        self.subject = subject

    def run(self):
        # Initialize custom agents and tasks
        agents = Agents(llm=claude_haiku)
        tasks = Tasks(
            agents.search_tool,
            agents.news_researcher(),
            agents.content_evaluator(),
            agents.summarizer(),
            agents.content_verifier(),
            agents.social_media_writer(),
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
                agents.social_media_writer(),
                agents.content_verifier(),
            ],
            tasks=[search_task, compare_task, summarize_task, write_task, verify_task],
            verbose=True,
        )

        # Kick off the crew with the specified subject
        return crew.kickoff(inputs={"subject": self.subject})


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
