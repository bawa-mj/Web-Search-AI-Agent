# 🌐 Web Search AI Agent

A simple Streamlit chatbot that can search the web in real time to answer your questions. Built using LangChain's agent framework with the Tavily search tool and Groq's LLaMA 3.3 model.

## Features

- Chat-style interface built with Streamlit
- Real-time web search using Tavily
- Powered by Groq's `llama-3.3-70b-versatile` model
- Conversation memory using LangGraph's `MemorySaver`

## Tech Stack

- [Streamlit](https://streamlit.io/) — frontend/UI
- [LangChain](https://www.langchain.com/) — agent framework
- [LangGraph](https://www.langchain.com/langgraph) — memory/checkpointing
- [Groq](https://groq.com/) — LLM inference
- [Tavily](https://tavily.com/) — web search API

## Prerequisites

- Python 3.9+
- A [Groq API key](https://console.groq.com/keys)
- A [Tavily API key](https://tavily.com/)

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/web-search-ai-agent.git
cd web-search-ai-agent
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your API keys

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## Usage

Run the app with:

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal and start asking questions. The agent will search the web when needed and reply with an answer.

## Project Structure

```
web-search-ai-agent/
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── screenshots/
│   └── demo.png         # App screenshot used in this README
├── .env                  # API keys (not committed)
└── README.md
```

## requirements.txt

```
streamlit
python-dotenv
langchain
langchain-groq
langchain-tavily
langgraph
```
## Screenshot

![Web Search AI Agent demo][
(https://github.com/bawa-mj/Web-Search-AI-Agent/blob/main/Web%20Search%20AI%20Agent.png)]
## Notes

- The API keys are required for the app to work — without them, the LLM and search tool calls will fail.
- Conversation memory is currently tied to a single fixed `thread_id`, so it resets when the app restarts.

## License

This project is open source and available under the [MIT License](LICENSE).
