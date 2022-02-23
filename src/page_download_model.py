import streamlit as st

def user_interface():

    text =  """
            # Nos descargamos un modelo de Machine Learning que pueda hacer frente a esta tarea
            """
    st.write(text)
    
    text = "Escoge el modelo que quieres usar"
    st.write(text)

    defaul_model_name = ""
    model_name = "Modelo seleccionado"
    user_input = st.text_input(model_name, defaul_model_name)
    
    pressed = False

    if user_input:
        text = "Descargar modelo"
        pressed = st.button(text)

    return pressed, user_input


def user_interface_2():

    text = "---"
    st.write(text)

    text = """
           # Te recomendamos este modelo: 
           
           nlp-en-es/roberta-base-bne-finetuned-sqac

           Más información aquí: https://huggingface.co/nlp-en-es/roberta-base-bne-finetuned-sqac
           """
    st.write(text)


def logic(user_input):

    from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
    
    try:
        nlp = pipeline("question-answering", model=user_input, tokenizer=user_input)
        text = "*¡Modelo correctamente descargado!*"
        st.session_state['nlp_model'] = nlp
        return text

    except OSError:
            text = "Modelo no encontrado"
            return text


def download_model():

    pressed, user_input = user_interface()

    if pressed:
        result = logic(user_input)
        st.write(result)

    user_interface_2()
