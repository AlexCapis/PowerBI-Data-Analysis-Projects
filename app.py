import streamlit as st
import base64
import os


st.set_page_config(page_title="POWER BI", page_icon=" :chart_with_upwards_trend:", layout="wide")

# Ponemos un titulo a nuestra aplicación
st.title("🚀 Descubre eL Poder de POWER BI 📊")




# Texto de explicación
texto = """

"""
st.write(texto)

menu = st.sidebar.selectbox("Selecciona la Página", ['HOME', 'VENTA VIDEOJUEGOS', 'INDICADORES MUNDIALES', 'RECURSOS HUMANOS'])

# Variable de control para ocultar o mostrar el contenido de HOME
mostrar_home = True

# Contenido de la versión 1.0
if menu == 'VENTA VIDEOJUEGOS':
    mostrar_home = False
    st.header("🎮 Un Viaje a Través de las Ventas de Videojuegos")

    imagen = "docs/images/portada_venta_videojuegos.png"
    imagen_cargada = st.image(imagen)




    texto_version_1 = '''
  En esta presentación, exploraremos profundamente el vasto universo de datos relacionados con las ventas de videojuegos, desglosando tendencias, preferencias y patrones de consumo.

    ## 🎯 **Objetivo del Análisis**
    Nuestro objetivo es descubrir información valiosa que pueda impulsar estrategias comerciales inteligentes en la industria de los videojuegos. Utilizando Power BI, hemos transformado datos crudos en visualizaciones interactivas que cuentan historias impactantes sobre las ventas de videojuegos a nivel mundial.

   ## **¿Qué Vas a Descubrir?**
    - **Total de Copias Vendidas**: Un vistazo al alcance global de las ventas en millones de copias.
    - **Distribución Geográfica**: Descubre cómo se distribuyen las ventas por región.
    - **Plataformas Populares**: Analiza las ventas por plataforma y región para identificar tendencias.
    - **Preferencias de Género**: Explora las ventas según el género del juego y la región.
    - **Tendencias Temporales**: Visualiza cómo las ventas han evolucionado a lo largo de los años en diferentes regiones.
    - **Restablecer los datos**: Con este botón interactivo podrás volver al inicio del dashboard restableciendo todos los valores.

    
    ## 🎥 **Visualiza Nuestro Dashboard en Función**

    A continuación, les vamos a mostrar un vídeo a través del cuál podrán ver de una manera más dinámica las interacciones con las que cuenta este dashboard. ¡No parpadeen que se lo pierden!
    '''
    st.markdown(texto_version_1)

   
    st.video("docs/clips/ventas_videojuegos_largo.mp4") 

    st.markdown(" A continuación, podrás descargar el archivo que se ha utilizado para el dashboard en formato Excel para que puedas explorarlo y replicar el proyecto. ¡Anímate a explorar los datos por ti mismo y descubrir más sobre la industria de los videojuegos!"     )

# Ruta al archivo Excel en tu repositorio
    excel_file_path = "data/Ventas_Videojuegos.xlsx"

# Leer el archivo Excel en bytes
    with open(excel_file_path, "rb") as file:
        bytes_data = file.read()

# Codificar el archivo en base64 para la descarga
    b64_data = base64.b64encode(bytes_data).decode('utf-8')

# Crear un enlace para la descarga usando st.download_button
    st.download_button(
        label="Descargar Ventas de Videojuegos en Excel",
        data=bytes_data,
        file_name="Ventas_Videojuegos.xlsx",
        mime="application/octet-stream"
)






# Contenido de la versión 1.0
if menu == 'INDICADORES MUNDIALES': 
    mostrar_home = False
    st.header(" 🌍 Explorando el Mundo a Través de Datos ")

    imagen = "docs/images/portada_indicadores_mundiales.png"
    imagen_cargada = st.image(imagen)

    texto_version_2= '''

    ¡Bienvenido a nuestro análisis profundo de la población donde realizaremos un análisis exhaustivo para una mejor comprensión de los datos. 


    ## 🎯 Objetivo del Análisis

    El objetivo principal es obtener una comprensión profunda de la distribución de la población en diferentes regiones del mundo y su relación con la mortalidad infantil y la esperanza de vida.
     
    ## ¿Qué descubrirás?

    El análisis se presenta a través de dos secciones: 
    
    1. **Población por Área**: En esta sección, exploramos la distribución de la población por continente y país mediante varias visualizaciones, como un treemap, un mapa, una matriz y diversas segmentaciones de datos. También proporcionamos un botón para restablecer las selecciones y facilitar la interacción del usuario.

    2. **Indicadores Mundiales**: En esta sección, analizamos la mortalidad infantil y la esperanza de vida por regiones. Utilizamos diversas visualizaciones, incluyendo matrices, un gráfico de dispersión, un gráfico de barras agrupadas y un mapa. Además, integramos segmentaciones de datos y botones de navegación (atrás y restablecer) para mejorar la experiencia del usuario.

    
    ## 🎥 Explora Nuestro Dashboard en Acción

    Para ofrecerte una experiencia más dinámica y cautivadora, te presentamos un vídeo que muestra las interacciones y funcionalidades de nuestro dashboard. ¡Atento!




    '''
    st.markdown(texto_version_2)

    st.video("docs/clips/indicadores_mundiales_largo.mp4") 



# Contenido de la versión 3.0
if menu == 'RECURSOS HUMANOS':
    mostrar_home = False
    st.header(" 🧑‍💼 Desglosando Nuestra Fuerza Laboral")

    imagen = "docs/images/portada_recursos_humanos.png"
    imagen_cargada = st.image(imagen)

    texto_version_3 = '''

    ¡Bienvenido a nuestro análisis profundo del departamento de Recursos Humanos de una organización destacada! En este viaje de datos, desentrañaremos aspectos cruciales a través de visualizaciones interactivas.

    ## 🎯 Objetivo del Análisis 

    Nuestro objetivo es obtener insights esenciales para estrategias de Recursos Humanos efectivas. Utilizando Power BI, hemos traducido datos complejos en visualizaciones impactantes, revelando historias cruciales sobre nuestra fuerza laboral.

    ## Descubre Perspectivas Clave

    1. **Perfil Demográfico**: Explora la distribución de empleados por género, edad promedio y otros aspectos clave, proporcionando una visión global de nuestra fuerza laboral.
    
    
    2. **Estructura Salarial**: Analiza la distribución salarial, identificando tendencias y patrones en sueldos y proporcionando insights vitales para políticas de compensación.
    
    
    3. **Evaluación de Desempeño**: Adéntrate en la evaluación de nuestros empleados.
    

    ## 🎥 Un Vistazo a Nuestro Dashboard

    A continuación, les vamos a presentar un vídeo que ofrece una experiencia dinámica y cautivadora, permitiéndote sumergirte en las interacciones que ofrece nuestro dashboard. ¡Prepárate para una visualización impactante, no te distraigas para no perderte ningún detalle!




    '''
    
    st.markdown(texto_version_3)



    st.video("docs/clips/recursos_humanos_largo.mp4") 

    st.markdown(" A continuación, podrás descargar el archivo que se ha utilizado para el dashboard en formato Excel para que puedas explorarlo y replicar el proyecto. ¡Anímate a explorar los datos por ti mismo!"     )

# Ruta al archivo Excel en tu repositorio
    excel_file_path = "data/Datos_Empleados.xlsx"

# Leer el archivo Excel en bytes
    with open(excel_file_path, "rb") as file:
        bytes_data = file.read()

# Codificar el archivo en base64 para la descarga
    b64_data = base64.b64encode(bytes_data).decode('utf-8')

# Crear un enlace para la descarga usando st.download_button
    st.download_button(
        label="Descargar Datos de Empleados en Excel",
        data=bytes_data,
        file_name=" Datos_Empleados.xlsx",
        mime="application/octet-stream"
)
    

    


# Contenido de HOME
if mostrar_home:
    # Ponemos una imagen
    imagen = "docs/images/portada_powerbi.png"
    imagen_cargada = st.image(imagen)

    texto_home = '''
    

    ¡Bienvenido a la sección principal de nuestra aplicación dedicada a POWER BI! Aquí podrás explorar diversas funcionalidades, proyectos y recursos relacionados con esta poderosa herramienta de visualización de datos.

    ## ¿Qué Puedes Encontrar Aquí?

    - **Ventas de Videojuegos**: Explora análisis interactivos sobre las ventas de videojuegos, descubre tendencias y patrones de la industria del gaming.

    - **Indicadores Mundiales**: Accede a visualizaciones de indicadores clave a nivel mundial y obtén información valiosa sobre diversos aspectos globales.

    - **Recursos Humanos**: Explora análisis y visualizaciones relacionadas con recursos humanos, como gestión de talento y eficiencia en equipos.

    Selecciona una de las opciones en el menú lateral para comenzar tu exploración y descubrir el poder de POWER BI.

    ---

    ¡No dudes en explorar y disfrutar de nuestra aplicación interactiva! Si tienes preguntas o necesitas ayuda, estaremos encantados de resolver las dudas.









    '''
    st.write(texto_home)

