import streamlit as st

def context():


    text =  """
            # Contexto
            Aquí escribimos el contexto, que es el fragmento de texto de la intranet sobre el cual queremos hacer preguntas.
            Como el modelo funciona en inglés, no queda otra que tirar de Google Translator o similar.
            """
    st.write(text)

    label = "Pega aquí el texto de la intranet"
    context_text = st.text_area(label, "")

    if context_text:
        text = "*¡Contexto listo!*"
        st.write(text)

    text = "---"
    st.write(text)

    text = """
           # Texto de ejemplo:

          Allende inició sus estudios primarios en la sección preparatoria del Liceo de Tacna, 
          dirigido por el profesor Julio Angulo. Se mostraba como un niño travieso y energético según cuenta Zoila Rosa Ovalle, 
          la mamá Rosa, la niñera que cuidó de Allende en la niñez y adolescencia y que alcanzó a verlo convertido en presidente. 
          Ella lo apodaría Chichito, pues el pequeño Allende no podía pronunciar su diminutivo correspondiente, 
          Salvadorcito, de ahí el origen del apodo Chicho Allende.
           """
    st.write(text)

    st.session_state['context_text'] = context_text
