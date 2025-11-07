import streamlit as st

def show_analysis_result(analysis_data: dict):
    st.header('📊 Análise dos resultados')
    st.write('Aqui está uma análise baseado no vídeo fornecido:')

    col1, col2 = st.columns(2)
    with col1:
        st.metric('Detecção de movimento', analysis_data['movements_detected'])
        st.metric("Acurácia:", f'{analysis_data['accuracy']}%')
    with col2:
        st.metric('Quantidade de repetição:', analysis_data['repetitions'])
        st.metric('Potenciais falhas:', analysis_data['issues_detected'])

    st.markdown('### 💡 Feedbacks')
    st.write(analysis_data['feedback'])
