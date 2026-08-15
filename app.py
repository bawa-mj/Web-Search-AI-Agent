from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver


st.set_page_config(
    page_title="Web Search AI Agent",
    page_icon="🌐"
)

st.markdown("""
<style>
.stChatInput textarea {
    min-height: 80px !important;
}

.stChatInput {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)


st.title("Web Search AI Agent")


model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

search = TavilySearch()
memory = MemorySaver()


agent = create_agent(
    model=model,
    tools=[search],
    system_prompt="you are a agent can search the web and answer questions",
    checkpointer=memory
)


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input("User query...")


if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching..."):

            response = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                },
                {
                    "configurable": {
                        "thread_id": "1"
                    }
                }
            )

            answer = response["messages"][-1].content

            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })