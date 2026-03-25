# ✈️ Predição e Análise de Atrasos de Voos

Tech Challenge – FIAP
Machine Learning Engineering

---

# 📌 Visão Geral do Projeto

Atrasos de voos são um desafio comum na aviação, impactando passageiros, companhias aéreas e a operação dos aeroportos.

Este projeto analisa dados históricos de voos para identificar padrões relacionados a atrasos e desenvolve modelos de Machine Learning capazes de:

* prever se um voo irá atrasar (classificação)
* prever quanto tempo o atraso irá durar (regressão)

Além disso, o projeto aplica técnicas de aprendizado não supervisionado para identificar padrões operacionais entre aeroportos e apresenta os resultados em um dashboard interativo no Power BI.

---

# 🎯 Objetivos do Projeto

* Realizar Análise Exploratória de Dados (EDA)
* Identificar fatores associados a atrasos
* Desenvolver modelos de classificação e regressão
* Aplicar clusterização para segmentar aeroportos
* Criar dashboard interativo
* Demonstrar pipeline completo de Data Science

---

# 🧰 Tecnologias Utilizadas

Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Power BI
GitHub

---

# 📁 Estrutura do Projeto

FLIGHTS-ML

dashboard/
  flight_delay_dashboard.pbix

data/
  raw/
  processed/

models/
  logistic_model.pkl
  random_forest.pkl

notebooks/
  flight_delay_analysis.ipynb

outputs/
  figures/
  tables/

src/
  data_processing.py
  feature_engineering.py
  model_training.py

---

# 📂 Dataset

Os dados são baixados automaticamente via script utilizando Google Drive.

### ▶️ Download automático

---

# 🔎 Metodologia

O projeto segue as etapas:

1. Leitura e integração dos dados
2. Tratamento de valores ausentes
3. Análise exploratória (EDA)
4. Engenharia de features
5. Modelagem supervisionada
6. Modelagem não supervisionada
7. Avaliação

---

# 📈 Análise Exploratória (EDA)

Principais insights:

* Distribuição de atrasos é assimétrica (cauda longa)
* Diferenças relevantes entre companhias aéreas
* Atrasos aumentam ao longo do dia (pior à noite)
* Clima impacta casos extremos
* Rotas e aeroportos concentram atrasos

---

# 🧠 Engenharia de Features

Principais features criadas:

* `IS_DELAYED` (atraso > 15 min)
* Período do dia
* Hora do voo
* Cidade de origem/destino (redução de cardinalidade)
* Rota (origem + destino)

Foi evitado data leakage (uso apenas de variáveis disponíveis antes do voo).

---

# 🤖 Modelagem Supervisionada

## Classificação

Objetivo: prever se o voo irá atrasar

Modelos:

* Logistic Regression
* Random Forest

Resultado:

* Logistic Regression teve melhor desempenho
* Random Forest apresentou colapso na classe minoritária

---

## Regressão

Objetivo: prever duração do atraso

Modelos:

* Linear Regression
* Random Forest Regressor

Resultado:

* Linear Regression apresentou melhor desempenho
* Alto R² (~0.96)

---

# 🔬 Modelagem Não Supervisionada

Aplicação de clusterização de aeroportos com:

* KMeans
* PCA (visualização)

Variáveis utilizadas:

* ARRIVAL_DELAY
* DEPARTURE_DELAY
* DELAY_RATE
* DISTANCE
* AIR_TIME
* WEATHER_DELAY
* N_FLIGHTS

Resultado:

* Identificação de aeroportos mais eficientes vs mais críticos
* Segmentação operacional clara

---

# 📊 Resultados

* Atrasos dependem de múltiplos fatores operacionais
* Modelos conseguem prever atraso e duração
* Clusterização identifica padrões estruturais entre aeroportos

---

# ⚠️ Limitações

* Falta de dados climáticos detalhados
* Não considera variáveis em tempo real
* Desbalanceamento da variável alvo

---

# 🚀 Próximos Passos

* Incluir dados climáticos reais
* Melhorar classificação (balanceamento)
* Deploy de modelo
* API de previsão
* Dashboard em tempo real

---

# ▶️ Como Executar

```bash
git clone https://github.com/gicatelli/flights-ml.git
cd flights-ml
pip install -r requirements.txt
```
Executar script python:

```bash
python src/download_data.py
```

Executar notebook:

```bash
jupyter notebook notebooks/flight_delay_analysis.ipynb
```

---

# 📌 Conclusão

Este projeto demonstra uma pipeline completa de Data Science:

* EDA → entendimento do problema
* Modelagem supervisionada → previsão
* Modelagem não supervisionada → descoberta de padrões

Gerando insights interpretáveis e aplicáveis ao problema de atrasos em voos.

---

# 👤 Autor

Projeto desenvolvido por Giovanna Catelli
Tech Challenge – FIAP