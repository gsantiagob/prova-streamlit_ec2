# 📊 Dashboard Financeiro com Streamlit

Este projeto é um dashboard interativo criado com [Streamlit](https://streamlit.io/) para visualização e análise de dados financeiros com base em um arquivo CSV. Ele roda em uma instância **EC2 (Ubuntu)** da AWS.

---

## 🚀 Funcionalidades

- Limpeza e tratamento de dados financeiros (com símbolos e valores ausentes)
- Visualização de:
  - Produtos mais vendidos
  - Lucro médio por faixa de desconto
  - Comparativo de preços de venda vs. fabricação
- Exibição interativa dos dados brutos com filtros

---

## 🧹 Função de Limpeza

Os valores monetários e de quantidade são tratados com a função abaixo para garantir que possam ser usados em operações numéricas:

```python
def clean_currency(x):
    if isinstance(x, str):
        x = x.strip()
        if x in ["-", "", "NA"]:
            return None
        return float(x.replace("$", "").replace(".", "").replace(",", "."))
    return x

---

## 🌍 Como acessar o Streamlit rodando na EC2 a partir do seu navegador local

### ✅ 1. Instalar as dependências 
sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install git curl unzip tar make sudo vim wget -y

---

### ✅ 2. Clone o repositório

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

---

✅ 3. Instalar o pythone e criar o ambiente virtual

sudo apt install python3-pip
sudo apt install python3-full python3-venv
python3 -m venv meuambiente
source meuambiente/bin/activate

---
✅ 4. Instalar as bibliotecas

pip install streamlit pandas matplotlib

---
✅ 5. Rodar o streamlit com acesso externo

streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false --server.port 8501 --server.address 0.0.0.0

---

🌍 Como acessar o Streamlit rodando na EC2 a partir do seu navegador local

✅ 6. Acesse o app pelo navegador

http://<IP-PÚBLICO-DA-SUA-EC2>:8501

⚠️ Importante: liberar a porta no grupo de segurança da EC2

---

✅ 7. Encerrar o app
Pressione Ctrl + C no terminal para interromper a execução do Streamlit.

