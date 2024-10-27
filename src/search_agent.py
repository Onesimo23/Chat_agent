from data_loader import load_data
from search_engine import search
from google_search import google_search
from chatgpt_integration import ask_chatgpt

class MozCultureSearchAgent:
    def __init__(self, data_filepath='data/moz_culture_data.json'):
        self.data = load_data(data_filepath)

    def ask_question(self, question):
        # Primeiro, procura na base de dados local
        answer = search(question, self.data)

        if answer == "Desculpe, não encontrei uma resposta para a pergunta.":
            # Tenta perguntar ao ChatGPT
            answer = ask_chatgpt(question)

            # Se o ChatGPT falhar, tenta o Google
            if "Erro ao comunicar com o ChatGPT" in answer:
                google_answers = google_search(question)
                
                if isinstance(google_answers, list) and google_answers:
                    return google_answers[0]  # Retorna a primeira resposta da pesquisa
                else:
                    return "O agente está offline e só pode responder a perguntas específicas."

        return answer
