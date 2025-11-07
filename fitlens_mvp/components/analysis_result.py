import random

import streamlit as st
from PIL import Image

def show_analysis_result(analysis_data: dict):
    st.header('📊 Análise dos resultados')
    st.write('Aqui está uma análise baseado no vídeo fornecido:')

    col1, col2 = st.columns(2)
    with col1:
        st.metric('Detecção de movimento', analysis_data['movements_detected'])
        st.metric("Acurácia:", f'{analysis_data['accuracy']}%')
        st.metric('Quantidade de repetição:', analysis_data['repetitions'])
    with col2:
        st.write('### Movimento:')
        st.write(f'##### {analysis_data['movement_type']}')
        st.write('### Erro detectado:')
        st.write(f'##### {analysis_data['issues_detected']}')
        st.write('### Músculo em risco:')
        st.write(f'##### {analysis_data['muscle_risk']}')

    st.markdown('### 💡 Feedbacks')
    st.write(analysis_data['feedback'])

    st.markdown("---")

    st.subheader("🎥 Execução Correta")
    
    st.video("https://www.youtube.com/watch?v=SCVCLChPQFY")

#     show_type = random.choice(["video", "image"])

#     if show_type == "video":
#     else:
#         show_correct_form_image()

# def show_correct_form_image():
#     """
#     Exibe uma imagem ilustrando o movimento correto do supino.
#     """
#     try:
#         image = Image.open("fitlens_mvp/assets/supino_correto.jpg")
#         st.image(
#             image,
#             caption="Exemplo de execução correta do supino reto com barra.",
#             use_container_width=True,
#         )
#     except FileNotFoundError:
#         st.warning(
#             "Imagem ilustrativa não encontrada — adicione um arquivo em `fitlens_mvp/assets/supino_correto.jpg`."
#         )
