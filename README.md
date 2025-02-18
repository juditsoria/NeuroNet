# Proyecto de Psicología

Este proyecto es una plataforma web desarrollada con Django para la gestión de recursos psicológicos, reservas y evaluaciones en línea.
Además, cuenta con una API para integrar artículos relacionados con temas psicológicos, como la ansiedad, y otros recursos que
pueden ser consultados por los usuarios.

## Capturas de pantalla
- Landing page:
  ![image](https://github.com/user-attachments/assets/dace1d39-1330-40e3-ac9d-45d52861ff4b)
- Registro:
   ![image](https://github.com/user-attachments/assets/127788c2-a11b-4263-99b2-5b76c9c5e40e)
- Login:
     ![image](https://github.com/user-attachments/assets/33c1bf07-f421-4f0b-98dd-d111d9444c17)
- Home:
- ![image](https://github.com/user-attachments/assets/596c4cdb-4632-4648-bbf1-fb28c49db0ef)
- Si el usuario es psicólogo no puede reservar cita:
 ![image](https://github.com/user-attachments/assets/b75da92c-301f-4dcd-a004-10945d9c0da5)
- Lisa de reservas:
   <img width="928" alt="Captura de pantalla 2025-01-22 223659" src="https://github.com/user-attachments/assets/a61597e6-416b-452d-b788-f45a58a8df3b" />
- Formulario para reserva:
  <img width="953" alt="image" src="https://github.com/user-attachments/assets/6ddb7ee4-bff4-44e9-b36e-6e58875dddb3" />
- Fuentes:
   <img width="943" alt="image" src="https://github.com/user-attachments/assets/f6b29cd6-bb9f-455f-be34-6dc4467c0c96" />
- Recursos:
   <img width="927" alt="image" src="https://github.com/user-attachments/assets/e8bb1757-db81-4f69-95c0-89b29109fced" />
- Artículos interesantes sobre ansiedad obtenidos de una api externa:
  ![image](https://github.com/user-attachments/assets/50103712-2917-462a-b5ea-78eaecd58181)


## Requisitos

Para ejecutar este proyecto, necesitas tener instalado lo siguiente:

- Python 3.12 o superior
- Django 5.1.5 o superior
- Otros paquetes listados en `requirements.txt`

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/juditsoria/NeuroNet.git
2. Crea un entorno virtual y activa el entorno:
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
3. Instala las dependencias:
  pip install -r requirements.txt
4. Ejecuta las migraciones para configurar la base de datos:
   python manage.py makemigrations
   python manage.py migrate
5. Inicia el servidor de desarrollo:
   python manage.py runserver
6. Accede a la aplicación en tu navegador: http://127.0.0.1:8000/

## Funcionalidades

- **Recursos Psicológicos**:
     - Registro de usuarios: El usuario se registra y se designa a si mismo como psicólogo o cliente.
     - Login
     - Creación de reservas, y modificación y eliminación de las mismas.
    - Visualización de artículos sobre la ansiedad obtenidos mediante una API externa (PubMed). La plataforma recupera información sobre artículos científicos relacionados con la ansiedad, incluyendo título, autores, revista y año de publicación.
    - Consulta de videos sobre los diferentes tipos de terapias psicológicas disponibles. Los usuarios pueden acceder a contenido educativo en video para aprender más sobre terapias como la cognitivo-conductual, la terapia de exposición, entre otras.
    - Acceso a fuentes externas con artículos relevantes sobre psicología. La plataforma proporciona enlaces a artículos de diversas fuentes confiables en línea, permitiendo a los usuarios profundizar más sobre temas de interés en el área de la psicología.

- **Gestión de Recursos**:
    - Los administradores pueden agregar, editar y eliminar recursos como artículos, videos y enlaces externos a través del backend de Django. Esto permite mantener la base de datos de recursos actualizada y relevante para los usuarios.

- **Interfaz Simple y Funcional**:
    - La interfaz de usuario es sencilla y está diseñada para que los usuarios puedan encontrar fácilmente los recursos de interés sin distracciones. Se hace uso de HTML básico y de Django para ofrecer una experiencia fluida.





