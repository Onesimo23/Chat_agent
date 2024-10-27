import openai

# Defina sua chave de API do OpenAI
openai.api_key = 'Minha chave API'

def ask_chatgpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=100,
            n=1,
            stop=None
        )
        answer = response['choices'][0]['message']['content']
        return answer.strip()
    except Exception as e:
        return "Erro ao comunicar com o ChatGPT."
