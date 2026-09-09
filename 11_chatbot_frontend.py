import streamlit as st

from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage


CONFIG = {'configurable': {'thread_id': 'thread-1'}}


# st.session_state -> dict
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# Loading the conversation history
for message in st.session_state['message_history']:

    with st.chat_message(message['role']):
        st.text(message['content'])


# Get user input
user_input = st.chat_input('Type here')


if user_input:

    # Add user message to history
    st.session_state['message_history'].append({
        'role': 'user',
        'content': user_input
    })

    # Display user message
    with st.chat_message('user'):
        st.text(user_input)


    # Generate AI response
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {
                    'messages': [
                        HumanMessage(content=user_input)
                    ]
                },
                config=CONFIG,
                stream_mode='messages'
            )
        )


    # Add AI response to history
    st.session_state['message_history'].append({
        'role': 'assistant',
        'content': ai_message
    })