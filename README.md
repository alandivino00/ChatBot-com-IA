# Chatbot com Inteligência Artificial utilizando Python

## 📌 Sobre o Projeto
Este projeto consiste no desenvolvimento de um **chatbot com Inteligência Artificial utilizando Python**, capaz de responder perguntas e manter o contexto de uma conversa.

A aplicação foi construída utilizando o framework **Streamlit**, permitindo criar uma interface web simples diretamente em Python, integrando **front-end e back-end em um único código**.

O chatbot se conecta à API da OpenAI para gerar respostas inteligentes com base no histórico da conversa.

---

## 🎯 Objetivo
O objetivo do projeto é demonstrar como desenvolver um **sistema de chat com IA**, entendendo conceitos importantes como:

- Criação de aplicações web com Python
- Integração com APIs de Inteligência Artificial
- Estruturação de mensagens em sistemas conversacionais
- Armazenamento de histórico de conversa

---

## ⚙️ Tecnologias Utilizadas

- Python
- Streamlit
- OpenAI API
- VS Code

---

## 🧠 Como o Chatbot Funciona

O funcionamento do sistema segue o fluxo abaixo:

1. O usuário envia uma mensagem pelo campo de chat.
2. A mensagem é armazenada no histórico da conversa.
3. O histórico completo é enviado para a API da OpenAI.
4. O modelo de IA processa a mensagem e gera uma resposta.
5. A resposta é exibida no chat e adicionada ao histórico.

Esse processo se repete a cada nova mensagem enviada.

---

## 💬 Estrutura das Mensagens

As mensagens do chat são armazenadas em uma **lista de dicionários**, formato padrão utilizado por APIs de IA conversacional:

```python
[
 {"role": "user", "content": "Pergunta do usuário"},
 {"role": "assistant", "content": "Resposta da IA"}
]