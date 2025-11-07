import streamlit as st
from fitlens_mvp.components.header import show_header
from fitlens_mvp.components.video_uploader import video_uploader
from fitlens_mvp.components.analysis_result import show_analysis_result
from fitlens_mvp.services.fake_analyzer import analyze_video


def run_app():
    show_header()

    st.info('🎥 Faça o upload do seu vídeo para que possamos analisar seu treino!')

    uploaded_file = video_uploader()

    if uploaded_file is not None:
        st.success('✅ Upload do vídeo realizado com sucesso!')
        with st.spinner('Análisando vídeo...'):
            analysis_data = analyze_video(uploaded_file)
        show_analysis_result(analysis_data)
    else:
        st.warning('Por favor, suba um arquivo de vídeo para prosseguir.')