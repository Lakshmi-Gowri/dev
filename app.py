import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(
        page_title="Lakshmi Gowri's Portfolio",
        page_icon="🚀",
        layout="wide"
    )

    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
