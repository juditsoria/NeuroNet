import requests
from xml.etree import ElementTree

def obtener_datos():
    search_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=ansiedad&retmode=xml'
    params = {
        'db': 'pmc',
        'term': 'ansiedad',
        'retmode': 'xml', 
        'retmax': '10'
    }

    response = requests.get(search_url, params=params)
    print("Response:", response.content)  # Verifica si la respuesta es válida

    tree = ElementTree.fromstring(response.content)
    id_list = tree.find('.//IdList').findall('Id')
    ids = [id_elem.text for id_elem in id_list]
    print("IDs encontrados:", ids)  # Verifica los IDs obtenidos

    if not ids:
        return []  # Retorna una lista vacía si no se encuentran artículos

    fetch_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    fetch_params = {
        'db': 'pmc',
        'id': ','.join(ids),
        'retmode': 'xml'
    }

    fetch_response = requests.get(fetch_url, params=fetch_params)
    print("Fetch response:", fetch_response.content)  # Verifica si la respuesta de fetch es válida

    fetch_tree = ElementTree.fromstring(fetch_response.content)
    articles = []

    for article in fetch_tree.findall('.//PubmedArticle'):
        title = article.find('.//ArticleTitle').text
        authors = article.findall('.//Author')
        author_names = [f"{author.find('.//LastName').text} {author.find('.//ForeName').text}" for author in authors]
        articles.append({
            'title': title,
            'authors': ', '.join(author_names),
            'journal': article.find('.//Journal/Title').text,
            'year': article.find('.//PubDate/Year').text
        })
    
    print("Artículos encontrados:", articles)  # Verifica los artículos obtenidos
    return articles

