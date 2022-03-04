import streamlit as st

def context():


    text =  """
            # Obra
          Aquí describimos el texto fuente de la obra
            """
    st.write(text)

    label = "MASP Lina Bo Bardi"
    context_text = st.text_area(label, "")

    if context_text:
        text = "*¡Contexto listo!*"
        st.write(text)

    text = "---"
    st.write(text)

    text = """
        El MASP, Museo de Arte Contemporáneo de Sao Paulo, fue diseñado por la importante arquitecta Lina Bo Bardi el año 1958, constituyendo un proyecto emblemático de la arquitectura moderna de Brasil, al ser parte de uno de los edificios más importantes de la renovación de la ciudad. Construido gracias a genial idea de Pietro María Bardi, marido de Lina, quien, junto a Assis Chateaubriand, decidieron crear un nuevo museo de arte en Sao Paulo, 12 años antes de su construcción, generando una sede propia para el MASP. A 8 metros del suelo, y con 74 metros de luz entre los pilares, esta obra se convirtió en la planta libre más grande del mundo.
Desde el 2003 este importante edificio de Sao Paulo está protegido por el Instituto do Patrimônio Histórico e Artístico Nacional. la idea de estos dos personajes, era generar una sede para albergar exposiciones periódicas, con el fin de promover la cultura y los aspectos didácticos del arte, a través de concursos, conferencias y talleres, como grabado, pintura, diseño industrial, entre muchos otros.
Este moderno edificio, de líneas simples y sus característicos y grandes marcos rojos, se construyó sobre el terreno ocupado por el antiguo Belvedere de Trianon, en la Avenida Paulista, en 1968. Este asombroso lugar, en el medio del cruce de dos ejes viarios, tiene hacia un lado la calle, y hacia el otro el Parque Trianon, desde donde se tiene vistas hacia la ciudad y la Sierra de Cantareira.
Como un gran volumen suspendido y colgado de marcos rojos, dejando así el nivel de la calle de libre circulación, el MASP fue pensado con una arquitectura simple, que lograra reflejar un carácter monumental, con el fin de expandir la cultura en la ciudad.
Estos 4 grandes pilares entrelazados por dos enormes e impresionantes vigas, funcionan como un exoesqueleto, que sostiene el edificio para permitir que sus visitantes y ciudadanos mantengan un recorrido fluido, sin interrupciones, y que el edificio genere un impacto negativo en el paisaje urbano.
Con 10,000 metros cuadrados, la cubierta que genera su suspensión genera una gran plaza que funciona como un hall cívico, una sombra en la ciudad, donde las personas se encuentran. Esta plaza además constituye el hall del museo, articulando los dos paisajes que se unen a través de este edificio: los edificios de la Av. Paulista, y el Parque. Este vacío, se relaciona con la manera de exposición al interior del museo, donde el usuario pasa a ser el protagonista quien decide su propio recorrido y movimiento, tanto al interior como en el exterior.
En cuanto a la distribución del MASP, dentro del basamento se encuentra un extenso hall cívico, el cual es sede de reuniones públicas y políticas, un teatro–auditorio y otro más pequeño con sala de proyecciones, por su parte el volumen flotante alberga la pinacoteca con escritorios, salas de exposiciones, una fototeca, filmoteca y videoteca.
Las circulaciones verticales del proyecto, se conforman por una escalera en el exterior y un ascensor en acero y vidrio, donde la escalera es la que representa el paso del pasado al futuro, articulando el espacio a través de un lugar de encuentro entre el interior y el exterior, invitando a los transeúntes a subir por ella, ascendiendo lentamente, por debajo de un gran volumen de escala monumental.
Los marcos no siempre fueron rojos. Con la reforma del año 2001, se efectuó una impermeabilización y restauración general, que incluyó la pintura de esta magnífica estructura, la cual adoptó una mayor importancia, al destacarse desde muchos puntos de la ciudad.
Arquitecto: Lina Bo Bardi


           """
    st.write(text)

    st.session_state['context_text'] = context_text
