import re

def search(query, data):
    query = query.lower()
    for entry in data:
        if re.search(query, entry['question'].lower()):
            return entry['answer']
    return "Desculpe, não encontrei uma resposta para a pergunta."
