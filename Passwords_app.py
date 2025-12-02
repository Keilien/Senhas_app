import string as st 
import numpy as np
import streamlit as sl

sl.title("Gerador de Senha Online")

letras = st.ascii_letters
numeros= st.digits
especial= st.punctuation
algarismos=(letras + numeros + especial)

# Adiciona um botão na interface
if sl.button("Gerar Nova Senha"):
    # Logica para gerar a senha
    Gerador_senha = np.random.choice(list(algarismos), 10)
    senha_final = ''.join(Gerador_senha)
    
    # Exibe o resultado na interface
    sl.success(f"Sua senha gerada é: **{senha_final}**")
