# Flow to create a book in ENGLISH or URDU
Welcome to the Book Writing Flow that create a book in word format in English Or Urdu depending on input you give. It is powered by [CrewAI](https://crewai.com) & [Streamlit](https://streamlit.io). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. My goal is to enable agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.


## Installation
Ensure you have Python >=3.10 <=3.13 installed on your system. First, activate the virtual environment: and the install the required dependencies:

```bash
uv venv
```
```bash
.venv\Scripts\activate
```
Install the required dependencies:

```bash
uv sync
```

### Customizing API Key

**Add your `GEMINI_API_KEY` into the `.env` file**  


## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
uv run kickoff
```
When you kickstart the flow, it will direct to streamlit interface, where you can enter a topic and goal of the book in either english or urdu. The flow is smart enough to detect the language and create book in the given language on the topic entered. It orchestrate multiple crews to perform the tasks. The flow will first generate a book outline, then create and run a crew for each chapter, and finally join all the chapters into a single markdown file.The book is ready to download in word format available for further editing if required.


