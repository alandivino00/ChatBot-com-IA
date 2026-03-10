# Passo a passo

# Passo 1: escrever chatBOT natela

# Passo 2: adicionar campo de input

# Passo 3: salvar resposta e perguntas e mostrar na tela

# Passo 4: responder perguntar usando openIA


import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="adicione sua chave aqui")

st.write("# Chatbot com IA")  

if not "lista_menssagens" in st.session_state:  
    st.session_state["lista_menssagens"] = []

texto_usuario = st.chat_input("Digite sua pergunta aqui")   

for menssagem in st.session_state["lista_menssagens"]:  
    role = menssagem["role"]
    content = menssagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:   
    st.chat_message("user").write(texto_usuario)
    menssagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_menssagens"].append(menssagem_usuario) 
    
    resposta_ia = modelo_ia.chat.completions.create(messages=st.session_state["lista_menssagens"],model="gpt-4o")   
    
    print(resposta_ia)
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    menssagem_ia = {"role": "assistant", "content": texto_resposta_ia}   
    st.session_state["lista_menssagens"].append(menssagem_ia)
    
    print(st.session_state["lista_menssagens"])

