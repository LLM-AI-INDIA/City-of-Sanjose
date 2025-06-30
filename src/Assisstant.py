import streamlit as st
from openai import OpenAI
import os
import time
from dotenv import load_dotenv
load_dotenv()


# Data Driven (Q&A)
def policy_agent(user_input):
    if 'client' not in st.session_state:
        st.session_state.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        st.session_state.thread = st.session_state.client.beta.threads.create()
    message = st.session_state.client.beta.threads.messages.create(thread_id=st.session_state.thread.id,role="user",content=user_input)
    run = st.session_state.client.beta.threads.runs.create_and_poll(thread_id=st.session_state.thread.id,assistant_id=os.environ["ASSISSTANT_ID"])
    # run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,run_id=run.id)
    a = 0
    while True:
        run = st.session_state.client.beta.threads.runs.retrieve(thread_id=st.session_state.thread.id, run_id=run.id)
        time.sleep(2)
        print(run.status)
        a = a+1
        print(a)
        if run.status=="completed":
            messages = st.session_state.client.beta.threads.messages.list(thread_id=st.session_state.thread.id)
            latest_message = messages.data[0]
            text = latest_message.content[0].text.value
            return text
        

def CustomerExp(user_input):
    if 'client' not in st.session_state:
        st.session_state.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        st.session_state.thread = st.session_state.client.beta.threads.create()
    message = st.session_state.client.beta.threads.messages.create(thread_id=st.session_state.thread.id,role="user",content=user_input)
    run = st.session_state.client.beta.threads.runs.create_and_poll(thread_id=st.session_state.thread.id,assistant_id=os.environ["ASSISSTANT_ID_2"])
    # run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,run_id=run.id)
    a = 0
    while True:
        run = st.session_state.client.beta.threads.runs.retrieve(thread_id=st.session_state.thread.id, run_id=run.id)
        time.sleep(2)
        print(run.status)
        a = a+1
        print(a)
        if run.status=="completed":
            messages = st.session_state.client.beta.threads.messages.list(thread_id=st.session_state.thread.id)
            latest_message = messages.data[0]
            text = latest_message.content[0].text.value
            return text