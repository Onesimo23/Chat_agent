import tkinter as tk
from tkinter import scrolledtext
from search_agent import MozCultureSearchAgent

class MozCultureChat:
    def __init__(self, master):
        self.master = master
        master.title("Chat sobre Cultura Moçambicana")

        # Mensagem de boas-vindas
        self.welcome_message = "Bem-vindo ao motor de busca da cultura moçambicana! Faça sua pergunta abaixo:"
        
        # Criação do frame principal
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)  # Margens ao redor do frame

        # Campo de texto para exibir a conversa
        self.conversation = scrolledtext.ScrolledText(self.frame, width=60, height=20, state='disabled', wrap=tk.WORD)
        self.conversation.grid(row=0, column=0, columnspan=2)

        # Adiciona mensagem de boas-vindas
        self.conversation.config(state='normal')
        self.conversation.insert(tk.END, f"Bot: {self.welcome_message}\n", 'welcome')  # Insere mensagem de boas-vindas
        self.conversation.config(state='disabled')

        # Campo de entrada de texto para perguntas
        self.entry = tk.Entry(self.frame, width=50)
        self.entry.grid(row=1, column=0, padx=(0, 10))  # Espaçamento à direita

        # Botão para enviar a pergunta
        self.send_button = tk.Button(self.frame, text="Enviar", command=self.send_question)
        self.send_button.grid(row=1, column=1)

        # Inicializa o agente de busca
        self.agent = MozCultureSearchAgent()

        # Adiciona tags para diferentes cores de fundo
        self.conversation.tag_config('question', background='#d0e8ff', justify='right')  # Cor de fundo para perguntas
        self.conversation.tag_config('answer', background='#e8ffd0', justify='left')    # Cor de fundo para respostas
        self.conversation.tag_config('welcome', background='#f0f0f0')  # Cor de fundo para mensagem de boas-vindas

    def send_question(self):
        question = self.entry.get()
        self.conversation.config(state='normal')
        self.conversation.insert(tk.END, f"Você: {question}\n", 'question')  # Insere pergunta com tag
        self.entry.delete(0, tk.END)  # Limpa o campo de entrada

        # Chama a função do agente de busca e garante resposta em português
        answer = self.agent.ask_question(question)

        # Adiciona a resposta à conversa
        self.conversation.insert(tk.END, f"Agente: {answer}\n", 'answer')  # Insere resposta com tag
        self.conversation.config(state='disabled')
        self.conversation.see(tk.END)  # Rola para o final da conversa

if __name__ == "__main__":
    root = tk.Tk()
    chat_app = MozCultureChat(root)
    root.mainloop()
