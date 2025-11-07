import streamlit as st

def show_header():
    st.title('🏋️‍♀️ FitLens')
    st.subheader('Análise em tempo real de movimentos -- powered by Gabrena')
    if st.button('Treinando sozinho? Utilize o FitStand!'):
        # st.warning('💲 O seu 1º FitStand é gratuito! 💲')
        st.toast('💲 O seu 1º FitStand é gratuito!')
    st.markdown('---')