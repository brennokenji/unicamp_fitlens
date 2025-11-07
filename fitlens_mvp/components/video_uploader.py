import streamlit as st

def video_uploader():
    uploaded_file = st.file_uploader(
        'Suba seu vídeo de exercício aqui',
        type=['mp4', 'mov', 'avi'],
        help='Formatos aceitos: mp4, mov, avi',
    )

    if uploaded_file:
        st.video(uploaded_file)
    return uploaded_file
