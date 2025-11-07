import streamlit as st
from fitlens_mvp.main_app import run_app

if __name__ == '__main__':
    st.set_page_config(page_title='FitLens MVP', layout='wide')
    run_app()