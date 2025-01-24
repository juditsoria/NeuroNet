import requests
from xml.etree import ElementTree

def obtener_datos():
    '''
    Esta función realiza una búsqueda en la base de datos PubMed sobre artículos relacionados con el término "ansiedad" 
    y luego obtiene detalles sobre estos artículos.

    Paso 1: Realiza una búsqueda en PubMed utilizando el término "ansiedad" y obtiene los IDs de los artículos encontrados.
    Paso 2: Utiliza los IDs obtenidos para realizar una solicitud y obtener detalles sobre los artículos, como el título, 
    autores, nombre de la revista y el año de publicación.

    Retorna:
        - Una lista de diccionarios, cada uno representando un artículo con su título, autores, revista y año de publicación.
    
    Excepciones:
        - Si la búsqueda o la obtención de detalles falla, se lanzará una excepción con un mensaje descriptivo.
    '''
    # Paso 1: Obtener IDs de artículos relacionados con "ansiedad"
    search_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    search_params = {
        'db': 'pubmed',         # Base de datos PubMed
        'term': 'ansiedad',     # Término de búsqueda
        'retmode': 'xml',       # Formato de respuesta
        'retmax': '10'          # Número máximo de IDs a devolver
    }

    response = requests.get(search_url, params=search_params)
    if response.status_code != 200 or not response.content.strip():
        raise Exception(f"Error en la búsqueda: {response.status_code}, {response.content}")
    
    # Parsear el XML de búsqueda para obtener los IDs
    try:
        tree = ElementTree.fromstring(response.content)
        id_list = tree.find('.//IdList').findall('Id')
        ids = [id_elem.text for id_elem in id_list]
    except Exception as e:
        raise Exception(f"Error al procesar el XML de búsqueda: {e}, contenido: {response.content}")

    if not ids:
        print("No se encontraron artículos relacionados con el término 'ansiedad'.")
        return []

    # Paso 2: Obtener detalles de los artículos usando los IDs
    fetch_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    fetch_params = {
        'db': 'pubmed',
        'id': ','.join(ids),  
        'retmode': 'xml'      
    }

    fetch_response = requests.get(fetch_url, params=fetch_params)
    if fetch_response.status_code != 200 or not fetch_response.content.strip():
        raise Exception(f"Error al obtener detalles: {fetch_response.status_code}, {fetch_response.content}")

    # Parsear el XML de detalles para extraer información de los artículos
    try:
        fetch_tree = ElementTree.fromstring(fetch_response.content)
        articles = []

        for article in fetch_tree.findall('.//PubmedArticle'):
            title_elem = article.find('.//ArticleTitle')
            title = title_elem.text if title_elem is not None else "Título no disponible"

            # Autores
            authors = article.findall('.//Author')
            author_names = []
            for author in authors:
                last_name = author.find('.//LastName')
                fore_name = author.find('.//ForeName')
                if last_name is not None and fore_name is not None:
                    author_names.append(f"{last_name.text} {fore_name.text}")

            # Revista
            journal_elem = article.find('.//Journal/Title')
            journal = journal_elem.text if journal_elem is not None else "Revista no disponible"

            # Año de publicación
            year_elem = article.find('.//PubDate/Year')
            year = year_elem.text if year_elem is not None else "Año no disponible"

            # Agregar artículo
            articles.append({
                'title': title,
                'authors': ', '.join(author_names) if author_names else "Autores no disponibles",
                'journal': journal,
                'year': year
            })
    except Exception as e:
        raise Exception(f"Error al procesar el XML de detalles: {e}, contenido: {fetch_response.content}")

    return articles


try:
    datos = obtener_datos()
    for articulo in datos:
        print(f"Título: {articulo['title']}")
        print(f"Autores: {articulo['authors']}")
        print(f"Revista: {articulo['journal']}")
        print(f"Año: {articulo['year']}")
        print("-" * 40)
except Exception as e:
    print("Error:", e)
