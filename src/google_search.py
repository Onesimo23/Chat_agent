import requests

# Chave da API do Google Custom Search e ID do mecanismo de pesquisa personalizado (CSE)
API_KEY = 'Api'
CSE_ID = 'ID'  

def google_search(query, cse_id=CSE_ID, api_key=API_KEY):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cse_id}&key={api_key}&hl=pt"  # Adicionado &hl=pt
    response = requests.get(url)
    
    # Verifica se a resposta foi bem-sucedida
    if response.status_code == 200:
        results = response.json()
        
        # Filtra os 3 primeiros resultados mais relevantes para simplificar
        answers = []
        for item in results.get("items", [])[:3]:
            answers.append(f"{item['title']}: {item['snippet']} - {item['link']}")
        
        return answers if answers else ["Nenhuma resposta relevante foi encontrada."]
    else:
        return ["Erro ao buscar informações na web."]
