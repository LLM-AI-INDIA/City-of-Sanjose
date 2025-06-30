import streamlit as st
from streamlit_chat import message
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd
from src.chat_ui import text_based
import time

# Load environment variables
load_dotenv()

# Streamlit app main function
def main():
    col1,col2,col3,col4 = st.columns((2,2.5,3.5,2))
    with col2:
        st.write("## ")
        # st.write("### ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Usecase</span></p>", unsafe_allow_html=True)
    
    with col3:
        usecase_option = st.selectbox("", ["Select", "Policy Analysis", "Financial Data Analysis", "Customer Experience"], key="usecase_select")
        st.write("## ")
        st.write("## ")
    if usecase_option == "Policy Analysis":
        text_based(usecase_option)
    elif usecase_option == "Customer Experience":
        text_based(usecase_option)
    elif usecase_option == "Financial Data Analysis":
        text_based(usecase_option)

