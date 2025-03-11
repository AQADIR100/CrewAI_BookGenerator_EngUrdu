from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
import google.generativeai as genai  # Changed import
import os

from write_a_book_with_flows.types import BookOutline

@CrewBase
class OutlineCrew:
    """Book Outline Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # Changed to use Google AI SDK directly
    llm = genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    generation_config = {
        "temperature": 0.5,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    
    model = genai.GenerativeModel(model_name="gemini-pro",
                                generation_config=generation_config)

    @agent
    def researcher(self) -> Agent:
        search_tool = SerperDevTool()
        return Agent(
            config=self.agents_config["researcher"],
            tools=[search_tool],
            llm=self.llm,
            verbose=True,
            # Optional: Add safety settings for Gemini
            safety_settings={
                "HARASSMENT": "BLOCK_NONE",
                "HATE_SPEECH": "BLOCK_NONE",
                "SEXUAL": "BLOCK_NONE",
                "DANGEROUS": "BLOCK_NONE"
            }
        )

    @agent
    def outliner(self) -> Agent:
        return Agent(
            config=self.agents_config["outliner"],
            llm=self.llm,
            verbose=True,
        )

    @task
    def research_topic(self) -> Task:
        return Task(
            config=self.tasks_config["research_topic"],
        )

    @task
    def generate_outline(self) -> Task:
        return Task(
            config=self.tasks_config["generate_outline"], 
            output_pydantic=BookOutline
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Book Outline Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

