from django.apps import AppConfig


class CoreConfig(AppConfig):
    '''
    Configuración de la aplicación 'core' dentro del proyecto Django.

    Esta clase configura la aplicación 'core', incluyendo:
    - La configuración del campo automático para los identificadores (ID) en los modelos.
    - El nombre de la aplicación dentro del proyecto Django.

    Atributos:
        default_auto_field (str): Especifica el tipo de campo automático para los identificadores. En este caso, se establece como 'BigAutoField' para utilizar un identificador entero grande.
        name (str): El nombre de la aplicación. En este caso, 'core', que debe coincidir con el nombre de la carpeta de la aplicación en el proyecto.

    La clase CoreConfig hereda de AppConfig, que es la clase base para la configuración de cualquier aplicación en Django.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
