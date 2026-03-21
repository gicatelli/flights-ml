# ✈️ Predição e Análise de Atrasos de Voos

Tech Challenge – FIAP  
Machine Learning Engineering

---

# 📌 Visão Geral do Projeto

Atrasos de voos são um desafio comum na aviação, impactando passageiros, companhias aéreas e a operação dos aeroportos. Compreender os fatores que contribuem para esses atrasos é essencial para melhorar a eficiência operacional e a experiência do cliente.

Este projeto analisa dados históricos de voos para identificar padrões relacionados a atrasos e desenvolve modelos de Machine Learning capazes de prever se um voo terá atraso significativo.

Além disso, o projeto aplica técnicas de aprendizado não supervisionado para identificar padrões operacionais entre aeroportos e rotas, e apresenta os resultados em um dashboard interativo no Power BI.

---

# 🎯 Objetivos do Projeto

Os principais objetivos são:

- Realizar **Análise Exploratória de Dados (EDA)** para entender padrões de atraso  
- Identificar fatores operacionais associados a atrasos e cancelamentos  
- Desenvolver **modelos de Machine Learning** para prever atrasos  
- Aplicar **técnicas de aprendizado não supervisionado** para identificar padrões entre aeroportos  
- Criar um **dashboard interativo no Power BI**  
- Estruturar o projeto seguindo boas práticas de **Data Science e ML Engineering**

---

# 🧰 Tecnologias Utilizadas

Python  
Pandas  
NumPy  
Matplotlib  
Seaborn  
Scikit-learn  
XGBoost  
Google Colab  
Power BI  
GitHub  

---

# 📁 Estrutura do Projeto


FLIGHTS-ML

dashboard/
    flight_delay_dashboard.pbix

data/
    raw
    processed

models/
    logistic_model.pkl
    random_forest.pkl

notebooks/
    flight_delay_analysis.ipynb

outputs/
    figures
    tables

src/
    data_processing.py
    feature_engineering.py
    model_training.py

.gitignore
LICENSE
README.md
requirements.txt


---

# 📂 Descrição das Pastas

**data/raw**  
Armazena o dataset original.

**data/processed**  
Armazena os dados tratados e prontos para modelagem.

**notebooks**  
Contém o notebook principal com toda a análise (desenvolvido no Google Colab).

**src**  
Scripts reutilizáveis de processamento, engenharia de features e modelagem.

**models**  
Modelos treinados de Machine Learning.

**outputs/figures**  
Gráficos gerados durante a análise.

**outputs/tables**  
Tabelas agregadas utilizadas no dashboard.

**dashboard**  
Arquivo do Power BI com visualizações interativas.

---

# 📊 Dataset

O dataset contém informações históricas de voos, incluindo dados operacionais como horários, aeroportos, companhias aéreas, atrasos e cancelamentos.

Principais variáveis:

| Variável | Descrição |
|--------|-------------|
| YEAR | Ano do voo |
| MONTH | Mês |
| DAY | Dia |
| DAY_OF_WEEK | Dia da semana |
| AIRLINE | Companhia aérea |
| ORIGIN_AIRPORT | Aeroporto de origem |
| DESTINATION_AIRPORT | Aeroporto de destino |
| SCHEDULED_DEPARTURE | Horário previsto de saída |
| DEPARTURE_DELAY | Atraso na saída (minutos) |
| ARRIVAL_DELAY | Atraso na chegada (minutos) |
| DISTANCE | Distância do voo |
| CANCELLED | Indica cancelamento |
| DIVERTED | Indica desvio de rota |

---

# 🔎 Metodologia

O projeto segue um pipeline padrão de Machine Learning:

1️⃣ Carregamento dos dados  
2️⃣ Entendimento da base  
3️⃣ Limpeza e tratamento  
4️⃣ Análise exploratória (EDA)  
5️⃣ Engenharia de features  
6️⃣ Modelagem supervisionada  
7️⃣ Modelagem não supervisionada  
8️⃣ Avaliação dos modelos  
9️⃣ Construção do dashboard  

---

# 📈 Análise Exploratória (EDA)

A EDA foi realizada para identificar padrões e comportamentos dos atrasos.

Principais análises:

- Distribuição de atrasos na chegada  
- Atraso médio por companhia aérea  
- Atraso por aeroporto  
- Atraso por dia da semana  
- Atraso por horário  
- Taxa de cancelamento  
- Rotas com maior atraso  

Os gráficos estão disponíveis em:


outputs/figures


---

# 🧠 Engenharia de Features

Foram criadas variáveis adicionais para melhorar a performance dos modelos:

- Período do dia (manhã, tarde, noite, madrugada)  
- Indicador de fim de semana  
- Identificação de rota (origem + destino)  
- Faixas de distância  
- Duração prevista do voo  

Foi tomado cuidado para evitar **data leakage**, ou seja, não foram utilizadas variáveis que só existem após a execução do voo.

---

# 🤖 Modelagem Supervisionada

O objetivo do modelo é prever se um voo terá atraso significativo.

Variável alvo:
is_delayed

Definição:
ARRIVAL_DELAY > 15 minutos

Modelos utilizados:
- Regressão Logística (baseline)  
- Random Forest  

Métricas de avaliação:
- Acurácia  
- Precisão  
- Recall  
- F1-Score  
- ROC AUC  

---

# 🔬 Modelagem Não Supervisionada

Foi utilizada clusterização para identificar padrões entre aeroportos.

Variáveis utilizadas:

- Atraso médio  
- Taxa de atraso  
- Taxa de cancelamento  
- Volume de voos  
- Distância média  

Algoritmos:

- K-Means  
- PCA (para visualização dos clusters)

---

# 📊 Dashboard no Power BI

Foi desenvolvido um dashboard interativo para análise dos dados.

Principais visões:

- Visão geral de atrasos  
- Atraso por companhia aérea  
- Atraso por aeroporto  
- Análise de rotas  
- Comportamento temporal  

Arquivo:


dashboard/flight_delay_dashboard.pbix


---

# 📊 Resultados

O projeto identificou fatores importantes associados aos atrasos, como:

- Companhias com maior taxa de atraso  
- Aeroportos com maior congestionamento  
- Impacto do horário nos atrasos  
- Rotas mais problemáticas  

Os modelos de Machine Learning mostraram capacidade de prever atrasos com base em variáveis operacionais.

---

# ⚠️ Limitações

- Ausência de dados climáticos detalhados  
- Falta de variáveis operacionais em tempo real  
- Possível viés nos dados históricos  

---

# 🚀 Próximos Passos

- Incluir dados climáticos  
- Criar modelo para prever cancelamentos  
- Implementar API para previsão em tempo real  
- Evoluir o dashboard com previsões  

---

# ▶️ Como Executar o Projeto

Clonar o repositório:
git clone https://github.com/seu-repositorio/flights-ml.git

Instalar dependências:
pip install -r requirements.txt

Abrir o notebook:
notebooks/flight_delay_analysis.ipynb

Executar todas as células para reproduzir a análise.

---

# 📌 Autor

Projeto desenvolvido por Giovanna Catelli para o Tech Challenge da FIAP – Machine Learning Engineering.