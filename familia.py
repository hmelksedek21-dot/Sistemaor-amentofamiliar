import streamlit as st
import pandas as pd
import plotly.express as px

tabela_orcamento = pd.read_csv("orcamentofamiliar.csv")

st.write("# Orçamento Familiar")

st.sidebar.write("## Cadastro de Produtos")
Data = st.sidebar.date_input("Data")
produto = st.sidebar.text_input("Produto")
categoria = st.sidebar.text_input("Categoria")
consumo = st.sidebar.number_input("Valor")
botao_cadastro = st.sidebar.button("Cadastrar produto")

if botao_cadastro:
    novo_produto = [Data, produto, categoria, consumo]
    tabela_orcamento.loc[len(tabela_orcamento)] = novo_produto
    tabela_orcamento.to_csv("orcamentofamiliar.csv", index=False)
    st.success("Produto Cadastrado")

st.write("## Produtos Cadastrados")
st.dataframe(tabela_orcamento)

st.write("## Dashboard")
soma = tabela_orcamento["consumo"].sum()
st.metric("Total", f"R${soma}")

coluna = px.bar(tabela_orcamento, x="produto", y="consumo")
st.plotly_chart(coluna)

pizza = px.pie(tabela_orcamento, names="categoria", values="consumo", hole=0.5)
st.plotly_chart(pizza)