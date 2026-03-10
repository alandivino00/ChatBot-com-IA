
menssagem1 = {"role": "assistant", "content": "Bora aprender python." }
menssagem2 = {"role": "user", "content": "O que é python?" } 
menssagem3 = {"role": "assistant", "content": "Python é uma linguagem." }

lista_menssagens = [menssagem1, menssagem2, menssagem3] 

nova_menssagem = {"role": "user", "content": "Quais as vantagens de python?" }  
lista_menssagens.append(nova_menssagem) 

print(lista_menssagens)
