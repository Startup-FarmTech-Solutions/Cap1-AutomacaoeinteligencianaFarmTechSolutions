# Cap1-Automacao e Inteligencia na Farm Tech Solutions
Projeto de automação agrícola inteligente, com sensores integrados no ESP32, display LCD, banco de dados e um modelo preditivo de Machine Learning utilizando Scikit-learn. A visualização dos dados é feita através de um dashboard interativo com Streamlit.

Perfeito! Aqui está o modelo completo e personalizado no mesmo padrão que você pediu, já adaptado para a **FASE 4 – Data Science em Ação** do seu projeto **FarmTech Solutions**.

---

# ✅ **ESTRUTURA DO PROJETO (GitHub)**

```
farmtech-fase4/
├── 📁 circuito/
│   ├── circuito.png            # Print do circuito no Wokwi com display LCD
│   ├── lcd_wokwi.png           # (Print focado no LCD funcionando)
│   └── esquema.pdf             # (Opcional) Esquemático elétrico
├── 📁 codigo_esp32/
│   ├── main.ino                # Código otimizado do ESP32
│   ├── lcd_display.cpp         # (Se modularizar) Função de exibição no LCD
│   ├── sensores.cpp            # (Se modularizar) Leitura dos sensores
│   ├── platformio.ini          # (Se usar PlatformIO)
│   └── README.md               # Instruções sobre o código ESP32
├── 📁 dados/
│   ├── dados_coletados.csv     # Dados históricos dos sensores
│   └── dataset_modelo.csv      # Dataset tratado para Machine Learning
├── 📁 analise_ml/
│   ├── treinamento_modelo.ipynb# Notebook com treino do modelo (Scikit-learn)
│   ├── model.pkl               # Modelo salvo
│   ├── analise_dados.png       # Gráficos de análise exploratória
│   └── README.md               # Descrição da análise de dados
├── 📁 dashboard_streamlit/
│   ├── app.py                  # Aplicação do dashboard interativo
│   ├── requirements.txt        # Bibliotecas necessárias
│   ├── imagens/                # Prints do dashboard funcionando
│   └── README.md               # Guia de uso do Streamlit
├── 📁 banco_dados/
│   ├── modelo_banco.sql        # Script SQL com a estrutura do BD
│   ├── ERD.png                 # (Opcional) Diagrama entidade-relacionamento
│   └── README.md               # Descrição do banco e acesso
├── 📁 imagens/
│   ├── serial_plotter.png      # Print do monitoramento no Serial Plotter
│   ├── grafico_umidade.png     # Gráficos para README
│   └── grafico_predicao.png    # Gráficos do modelo ML
├── 📁 documentacao/
│   ├── vídeo.mp4               # (ou link do YouTube no README)
│   └── prints_etapas/          # Prints das etapas concluídas
├── README.md                   # Arquivo principal com resumo do projeto
└── LICENSE                     # (Opcional) Licença do projeto
```

---

# 🗂️ **ESTRUTURA DO README (Modelo)**


# 🌾 FarmTech Solutions - Fase 4 🚀

## 💡 Descrição
Projeto de automação agrícola inteligente, com sensores integrados no ESP32, display LCD, banco de dados e um modelo preditivo de Machine Learning utilizando Scikit-learn. A visualização dos dados é feita através de um dashboard interativo com Streamlit.

## 🎯 Objetivos
- 🔌 Monitorar umidade, temperatura e nutrientes do solo.
- 📊 Exibir os dados em tempo real no display LCD e no dashboard.
- 🤖 Prever necessidades de irrigação com Machine Learning.
- 💾 Armazenar os dados em um banco de dados.
- 🧠 Otimizar o uso de memória no ESP32.

---

## 🏗️ Circuito
- **Plataforma:** Wokwi
- **Componentes:**
  - Sensor de Umidade 🌱
  - Sensor de Nutrientes ⚗️
  - Sensor de Temperatura 🌡️
  - Display LCD 16x2 via I2C 🖥️
  - Microcontrolador ESP32 ⚙️

### 🔌 Esquema do Circuito
![Esquema do Circuito](./circuito/circuito.png)

| Variável                      | Sensor no Wokwi     | Interface                |
| ----------------------------- | ------------------- | ------------------------ |
| temperatura (ar)              | DHT22, DS18B20      | digital                  |
| umidade (ar)                  | DHT22               | digital                  |
| luminosidade                  | Photoresistor (LDR) | analógico (`analogRead`) |
| irrigação\_ativa              | relé/control GPIO   | digital                  |
| nitrogenio, fosforo, potassio | npk-sensor          | analógico ou UART        |

---

## 👨‍💻 Código ESP32
- Linguagem: C++
- Funções principais:
  - Leitura dos sensores
  - Envio de dados via Serial
  - Exibição no LCD
  - Monitoramento via Serial Plotter
  - Otimização de variáveis para economia de memória

```cpp
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Configuração do LCD
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
}

void loop() {
  float umidade = random(30, 70); // Simulação
  float temperatura = random(20, 35);
  
  lcd.setCursor(0,0);
  lcd.print("Umidade: ");
  lcd.print(umidade);

  lcd.setCursor(0,1);
  lcd.print("Temp: ");
  lcd.print(temperatura);
  lcd.print(" C");

  Serial.print("Umidade:");
  Serial.print(umidade);
  Serial.print(",");
  Serial.print("Temperatura:");
  Serial.println(temperatura);

  delay(2000);
}
````

---

## 🔍 Dados

* Dados coletados simulando sensores.
* Dataset preparado para Machine Learning.

---

## 📈 Machine Learning

###  Escolha e Avaliação de Algoritmos

Para esta fase do projeto, decidimos realizar o **treinamento e avaliação com múltiplos algoritmos** de Machine Learning, com o objetivo de identificar aquele que oferece o melhor desempenho para o problema de **prever a necessidade de irrigação**.

O problema foi modelado como uma **classificação binária**, onde o modelo deve prever se a irrigação é necessária (`1`) ou não (`0`), com base em variáveis como umidade do solo, níveis de nutrientes, temperatura e hora do dia.

---

### Algoritmos Avaliados

| Algoritmo                                  | Vantagens                                                              | Desvantagens                                              |
| ------------------------------------------ | ---------------------------------------------------------------------- | --------------------------------------------------------- |
| **Logistic Regression**                    | Simples, rápido, bom para baseline                                     | Supõe relação linear entre as variáveis                   |
| **Decision Tree**                          | Fácil de interpretar, lida com variáveis categóricas                   | Pode sofrer de overfitting e ser sensível a ruído         |
| **Random Forest**                          | Reduz overfitting, boa acurácia, robusto                               | Mais lento e menos interpretável que uma árvore única     |
| **K-Nearest Neighbors (KNN)**              | Simples, não-paramétrico, intuitivo                                    | Custo computacional elevado em grandes conjuntos de dados |
| **Support Vector Machine (SVM)**           | Eficaz em espaços de alta dimensão, bom para problemas complexos       | Mais lento e exige ajuste cuidadoso de parâmetros         |
| **Gradient Boosting (LightGBM, CatBoost)** | Alta performance, lida bem com não-linearidades e dados desbalanceados | Complexidade maior e menos interpretável                  |

---

### Metodologia

Todos os algoritmos foram treinados utilizando a biblioteca **Scikit-learn** (com exceção do **LightGBM** e **CatBoost**, implementados com suas respectivas bibliotecas).

O dataset foi dividido em **80% para treino** e **20% para teste** utilizando **stratified split** para manter a proporção das classes.

O pré-processamento incluiu:

* Normalização das variáveis numéricas para algoritmos sensíveis a escala (KNN, SVM).
* Conversão de variáveis categóricas, se houver.
* Tratamento de dados ausentes.

---

### Métricas de Avaliação

Para comparar os modelos, utilizamos as seguintes métricas:

| Métrica                | Justificativa                                                |
| ---------------------- | ------------------------------------------------------------ |
| **Acurácia**           | Percentual de acertos gerais                                 |
| **Precisão**           | Evitar falsos positivos: irrigar desnecessariamente          |
| **Recall**             | Evitar falsos negativos: falhar em irrigar quando necessário |
| **F1-Score**           | Métrica principal para balancear precisão e recall           |
| **Matriz de Confusão** | Análise visual dos erros de cada modelo                      |

**Obs.:** Se o dataset apresentar **desbalanceamento** entre classes, as métricas como **F1-Score** e **Recall** terão maior peso na decisão final.

---

### Processo de Treinamento

Para cada modelo, seguimos o mesmo pipeline:

1. Separação de **features** e **target**.
2. Divisão em **treino** e **teste**.
3. Ajuste de **parâmetros padrão** (sem hiperparâmetros complexos, para avaliação justa).
4. Treinamento do modelo.
5. Avaliação com as métricas definidas.

---

### Exemplo de Código para Avaliação de Todos os Modelos

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import lightgbm as lgb
from catboost import CatBoostClassifier

# Separação
X = df[['umidade', 'nutrientes', 'temperatura', 'hora_dia']]
y = df['precisa_irrigar']

# Divisão
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Normalização
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modelos
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'KNN': KNeighborsClassifier(),
    'SVM': SVC(probability=True),
    'LightGBM': lgb.LGBMClassifier(),
    'CatBoost': CatBoostClassifier(verbose=0)
}

# Treinamento e avaliação
for name, model in models.items():
    if name in ['KNN', 'SVM', 'Logistic Regression']:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    print(f"\nModelo: {name}")
    print(classification_report(y_test, y_pred))
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
```

---

###  Definição do Algoritmo Final

Após realizar a avaliação com todos os modelos e comparar os resultados com base nas métricas definidas, selecionaremos como **algoritmo final** aquele que apresentar o **melhor equilíbrio entre F1-Score, precisão e recall**, priorizando a capacidade do modelo em evitar **erros críticos** para o sistema de irrigação.

---

### Justificativa a ser adicionada após os testes

**Após a execução dos testes, o algoritmo com melhor desempenho foi o:**

 **Random Forest Classifier** com F1-Score: 
 **Precision**: 
 **Recall**: 

O Random Forest foi escolhido como modelo final pois apresentou o melhor equilíbrio entre precisão e recall, além de ser robusto contra overfitting e fornecer uma boa explicabilidade através das importâncias das features.

---

### Considerações Finais

Essa abordagem de testar múltiplos algoritmos garante uma escolha **baseada em dados**, e não apenas em suposições teóricas. Além disso, o pipeline criado é facilmente reutilizável e extensível para novas versões do sistema.


---

## 📊 Dashboard Streamlit

* Visualização dos dados em tempo real.
* Gráficos de umidade, temperatura e previsão.

![Dashboard](./dashboard_streamlit/imagens/dashboard.png)

---

## 🗄️ Banco de Dados

* Modelo SQL armazenando leituras dos sensores.

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/usuario/farmtech-fase4.git
```

2. Execute o código ESP32 no Wokwi ou na IDE Arduino.

3. Rode o dashboard:

```bash
cd dashboard_streamlit
pip install -r requirements.txt
streamlit run app.py
```

4. Consulte o banco de dados com o script SQL.

---

## 👥 Equipe

* Francismar Alves Martins Júnior
* Antonio Ancelmo Neto Barros
* Vitor Eiji Fernandes Teruia
* Beatriz Pilecarte de Melo
* Matheus Soares Bento da Silva

---

## 📜 Licença


---

# 📅 **KANBAN (CARTÕES DE TAREFAS)**

| 🔧 Planejamento             | 🔌 Montagem do Circuito           | 👨‍💻 Programação                 | 📈 Dados/Análise                  | 📄 Documentação/Entrega           |
|-----------------------------|-----------------------------------|----------------------------------|-----------------------------------|-----------------------------------|
| ✔ Definir sensores          | ✔ Montar circuito no Wokwi       | ✔ Ler sensores no ESP32         | ✔ Coletar dados simulados        | ✔ Preencher README               |
| ✔ Distribuir tarefas        | ✔ Implementar display LCD        | ✔ Exibir dados no LCD           | ✔ Analisar dados no Python       | ✔ Organizar imagens e dados      |
| ✔ Criar repositório GitHub  | ✔ Gerar print do circuito        | ✔ Serial Plotter funcionando    | ✔ Treinar modelo ML              | ✔ Gravar vídeo explicativo       |
|                             |                                   | ✔ Otimizar código ESP32         | ✔ Salvar modelo (.pkl)           | ✔ Fazer revisão final            |
|                             |                                   |                                  | ✔ Criar dashboard Streamlit      | ✔ Publicar no GitHub             |

---

Se desejar, posso gerar os seguintes arquivos prontos para você começar agora:

✅ README.md  
✅ main.ino (código ESP32 com LCD funcionando)  
✅ treinamento_modelo.ipynb (modelo Scikit-learn básico)  
✅ app.py (dashboard Streamlit básico)  
✅ modelo_banco.sql (banco de dados exemplo)  
