import streamlit as st

from page_sidebar import sidebar
from page_task import task
from page_download_model import download_model
from page_context import context
from page_questions import questions
from page_results import results



def main():

    pages_mapper = {

                        '1. ¿Qué vamos a hacer?': task,
                        '2. Descargar un modelo': download_model,
                        '3. Contexto': context,
                        '4. Preguntas': questions,
                        '5. Resultados': results,  
                    }

    ls_page_name = pages_mapper.keys()
    page_name = sidebar(ls_page_name)

    pages_mapper[page_name]()


if __name__ == '__main__':
    main()
