# 🌾 FarmTech Solutions - Automação Agrícola Inteligente 🚀

## 💡 Descrição do Projeto

Este projeto visa revolucionar a agricultura através de um sistema de automação inteligente, monitorando variáveis cruciais do solo e do ambiente com **sensores integrados a um ESP32**. Os dados coletados são exibidos em tempo real em um **display LCD** e persistidos em um **banco de dados** para análise histórica. A inteligência do sistema é ampliada com um **modelo preditivo de Machine Learning (Scikit-learn)**, capaz de otimizar a tomada de decisões, como a necessidade de irrigação. Toda a interação e visualização dos dados são facilitadas por um **dashboard interativo construído com Streamlit**.

-----

## 🎯 Objetivos

Os principais objetivos da **FarmTech Solutions** são:

  * **Monitoramento Preciso:** Coletar dados em tempo real sobre umidade, temperatura do ar e do solo, e níveis de nutrientes.
  * **Visualização Clara:** Apresentar as informações dos sensores tanto em um display LCD local quanto em um dashboard web interativo.
  * **Otimização Inteligente:** Utilizar Machine Learning para prever e otimizar ações como a irrigação, garantindo o uso eficiente dos recursos.
  * **Gerenciamento de Dados:** Armazenar os dados coletados de forma organizada em um banco de dados para análise histórica e treinamento de modelos.
  * **Eficiência de Hardware:** Otimizar o uso de memória e processamento no microcontrolador ESP32 para garantir desempenho e estabilidade.

-----

## 🏗️ Circuito Eletrônico

O sistema de monitoramento é construído em torno do microcontrolador **ESP32**, que interage com diversos sensores e um display para a apresentação local dos dados. O circuito foi projetado e simulado na plataforma **Wokwi**.

### 🔌 Componentes Principais

  * **Microcontrolador ESP32:** O cérebro do sistema, responsável pela leitura dos sensores, processamento e comunicação.
  * **Sensor de Umidade do Solo:** Monitora o teor de água no solo, crucial para a decisão de irrigação.
  * **Sensor de Nutrientes (NPK):** Avalia os níveis de Nitrogênio, Fósforo e Potássio no solo, indicando a necessidade de fertilização.
  * **Sensor de Temperatura (DHT22/DS18B20):** Mede a temperatura do ar e/ou do solo.
  * **Display LCD 16x2 (via I2C):** Exibe as leituras dos sensores em tempo real diretamente no dispositivo.
  * **Fotorresistor (LDR):** Detecta a intensidade luminosa ambiente.
  * **Relé/Controle GPIO:** Permite o acionamento de atuadores (ex: bomba de irrigação).

### 🖥️ Diagrama do Circuito

O esquema detalhado do circuito pode ser visualizado abaixo, demonstrando a interconexão entre os componentes e o ESP32.

### 📊 Tabela de Variáveis e Sensores

| Variável Monitorada            | Sensor Utilizado no Wokwi | Interface de Conexão |
| :----------------------------- | :------------------------ | :------------------- |
| Temperatura (ar)               | DHT22, DS18B20            | Digital              |
| Umidade (ar)                   | DHT22                     | Digital              |
| Luminosidade                   | Photoresistor (LDR)       | Analógico (`analogRead`) |
| Irrigação Ativa                | Relé / Controle GPIO      | Digital              |
| Nitrogênio, Fósforo, Potássio  | NPK-sensor                | Analógico ou UART    |

-----

## 👨‍💻 Código do ESP32

O firmware do ESP32 é escrito em **C++** e foi desenvolvido para ser eficiente e modular.

### 📝 Principais Funcionalidades

  * **Leitura de Sensores:** Rotinas otimizadas para adquirir dados dos diferentes sensores.
  * **Exibição no LCD:** Gerenciamento do display I2C para mostrar informações em tempo real.
  * **Comunicação Serial:** Envio dos dados dos sensores via porta serial para monitoramento e ingestão por outros sistemas (ex: banco de dados).
  * **Otimização de Memória:** Implementação de técnicas para garantir o uso eficiente dos recursos limitados do microcontrolador.
  * **Monitoramento:** Geração de dados compatíveis com o Serial Plotter da IDE Arduino para visualização gráfica instantânea.

### 📜 Exemplo de Código (ESP32)

Este trecho demonstra a inicialização do LCD e a simulação da leitura de sensores para exibição e envio serial.

```cpp
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Configuração do LCD
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    Serial.begin(9600); // Inicializa a comunicação serial
    lcd.init();         // Inicializa o display LCD
    lcd.backlight();    // Acende a luz de fundo do LCD
}

void loop() {
    // Simulação de leitura de sensores (em um cenário real, estas seriam leituras físicas)
    float umidade = random(30, 70);    // Umidade simulada entre 30% e 70%
    float temperatura = random(20, 35); // Temperatura simulada entre 20°C e 35°C

    // Exibe os dados no display LCD
    lcd.setCursor(0,0); // Define o cursor na coluna 0, linha 0
    lcd.print("Umidade: ");
    lcd.print(umidade);
    lcd.print("%"); // Adiciona unidade para clareza

    lcd.setCursor(0,1); // Define o cursor na coluna 0, linha 1
    lcd.print("Temp: ");
    lcd.print(temperatura);
    lcd.print(" C"); // Adiciona unidade para clareza

    // Envia os dados para a porta serial para monitoramento ou persistência
    Serial.print("Umidade:");
    Serial.print(umidade);
    Serial.print(","); // Separador para facilitar a leitura por softwares externos
    Serial.print("Temperatura:");
    Serial.println(temperatura); // println para quebrar a linha após cada conjunto de dados

    delay(5000); // Aguarda 5 segundos antes da próxima leitura (ajustável)
}
```

-----

## 📊 Análise de Dados e Machine Learning

A inteligência da **FarmTech Solutions** reside em seu componente de Machine Learning, que processa dados históricos para tomar decisões preditivas, como a necessidade de irrigação.

### 📚 Escolha e Avaliação de Algoritmos

Para garantir a melhor performance do sistema, realizamos uma avaliação rigorosa de múltiplos algoritmos de Machine Learning. O problema foi modelado como uma **classificação binária**: o modelo prediz se a irrigação é necessária (`1`) ou não (`0`), com base em variáveis ambientais e do solo (umidade, nutrientes, temperatura e hora do dia).

### 🤖 Algoritmos Avaliados

A tabela abaixo resume os algoritmos considerados, suas vantagens e desvantagens para este projeto:

| Algoritmo                                  | Vantagens                                                              | Desvantagens                                              |
| :------------------------------------------ | :---------------------------------------------------------------------- | :-------------------------------------------------------- |
| **Regressão Logística**                     | Simples, rápido, bom para estabelecer um baseline                      | Assume relação linear entre variáveis                   |
| **Árvore de Decisão**                       | Fácil interpretação, lida com variáveis categóricas                     | Pode sofrer de overfitting e ser sensível a ruído         |
| **Random Forest**                           | Reduz overfitting, alta acurácia, robusto                               | Mais lento e menos interpretável que uma única árvore     |
| **K-Nearest Neighbors (KNN)**               | Simples, não-paramétrico, intuitivo                                    | Custo computacional elevado para grandes datasets         |
| **Support Vector Machine (SVM)**           | Eficaz em espaços de alta dimensão, bom para problemas complexos       | Mais lento e exige ajuste cuidadoso de parâmetros         |
| **Gradient Boosting (LightGBM, CatBoost)** | Alta performance, lida bem com não-linearidades e dados desbalanceados | Maior complexidade e menor interpretabilidade             |

### 🔬 Metodologia de Treinamento

Todos os algoritmos foram treinados utilizando a biblioteca **Scikit-learn** (com exceção do LightGBM e CatBoost, que utilizam suas próprias bibliotecas otimizadas).

  * **Divisão de Dados:** O dataset foi dividido em **80% para treino** e **20% para teste**, aplicando **estratificação** para manter a proporção das classes (irrigar/não irrigar) em ambos os conjuntos.
  * **Pré-processamento:** As etapas de pré-processamento incluíram:
      * **Normalização** de variáveis numéricas, crucial para algoritmos sensíveis à escala (ex: KNN, SVM).
      * **Tratamento de dados ausentes**, se aplicável.
      * **Conversão de variáveis categóricas** (ex: One-Hot Encoding), se necessário.

### 📈 Métricas de Avaliação

Para uma comparação robusta dos modelos, utilizamos as seguintes métricas:

| Métrica                | Justificativa para o Projeto                                             |
| :--------------------- | :------------------------------------------------------------ |
| **Acurácia**           | Percentual de predições corretas gerais.                       |
| **Precisão**           | Relevante para evitar **falsos positivos** (irrigar desnecessariamente, desperdiçando água). |
| **Recall**             | Crucial para evitar **falsos negativos** (não irrigar quando a planta precisa, prejudicando a colheita). |
| **F1-Score**           | Métrica de equilíbrio entre Precisão e Recall, ideal para datasets desbalanceados. |
| **Matriz de Confusão** | Análise visual detalhada dos tipos de erros cometidos por cada modelo. |

**Observação:** Em casos de **desbalanceamento** entre as classes (`precisa_irrigar`), o **F1-Score** e o **Recall** são as métricas mais importantes para a decisão final, pois refletem melhor a capacidade do modelo em identificar a classe minoritária.

### ⚙️ Processo de Treinamento e Avaliação (Código Exemplo)

O script a seguir ilustra o pipeline de treinamento e avaliação para todos os modelos:

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
import pandas as pd # Importar pandas para criar um DataFrame de exemplo

# --- Criação de um DataFrame de exemplo (para fins de demonstração) ---
# Em um cenário real, você carregaria seu dados_coletados.csv aqui
data = {
    'umidade': [30, 45, 60, 25, 70, 35, 50, 40, 55, 65],
    'nutrientes': [5, 7, 3, 8, 2, 6, 4, 9, 1, 10],
    'temperatura': [22, 25, 20, 28, 23, 26, 21, 24, 27, 19],
    'hora_dia': [8, 14, 18, 10, 22, 16, 12, 9, 20, 7],
    'precisa_irrigar': [1, 0, 0, 1, 0, 1, 0, 1, 0, 0] # 1 = precisa irrigar, 0 = não precisa
}
df = pd.DataFrame(data)
# ---------------------------------------------------------------------

# Separação de features (X) e target (y)
X = df[['umidade', 'nutrientes', 'temperatura', 'hora_dia']]
y = df['precisa_irrigar']

# Divisão dos dados em treino e teste (com estratificação)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Normalização das features (apenas para algoritmos sensíveis à escala)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Dicionário de modelos a serem avaliados
models = {
    'Regressão Logística': LogisticRegression(random_state=42),
    'Árvore de Decisão': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'KNN': KNeighborsClassifier(),
    'SVM': SVC(probability=True, random_state=42),
    'LightGBM': lgb.LGBMClassifier(random_state=42),
    'CatBoost': CatBoostClassifier(verbose=0, random_state=42) # verbose=0 para não printar o treinamento
}

# Loop para treinar e avaliar cada modelo
for name, model in models.items():
    print(f"\n--- Modelo: {name} ---")
    if name in ['KNN', 'SVM', 'Regressão Logística']:
        # Para modelos sensíveis à escala, usamos os dados normalizados
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        # Para os demais, usamos os dados originais
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    # Impressão das métricas de avaliação
    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred))
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
```

### 🏆 Definição do Algoritmo Final

Após a execução dos testes e a comparação das métricas de todos os modelos, o algoritmo escolhido como solução final para a predição da necessidade de irrigação foi o **Random Forest Classifier**.

**Justificativa:**

  * **F1-Score:** [Adicionar o F1-Score do Random Forest aqui]
  * **Precisão:** [Adicionar a Precisão do Random Forest aqui]
  * **Recall:** [Adicionar o Recall do Random Forest aqui]

O **Random Forest** foi selecionado por apresentar o **melhor equilíbrio entre precisão e recall**, crucial para minimizar tanto o desperdício de água (falsos positivos) quanto a falta de irrigação (falsos negativos). Além disso, sua robustez contra overfitting e a capacidade de fornecer a importância das features o tornam uma escolha sólida e interpretável para o nosso sistema.

-----

## 📊 Dashboard Interativo com Streamlit

Para uma visualização amigável e interativa dos dados e previsões, desenvolvemos um dashboard utilizando o **Streamlit**.

### 🌟 Funcionalidades

  * **Visualização em Tempo Real:** Exibe as últimas leituras dos sensores.
  * **Gráficos Históricos:** Apresenta tendências de umidade, temperatura e nutrientes ao longo do tempo.
  * **Previsões do Modelo ML:** Mostra as predições do modelo de Machine Learning (ex: "Necessidade de Irrigar: SIM/NÃO").
  * **Interface Intuitiva:** Design responsivo e fácil de usar para monitoramento rápido.

### 🖼️ Exemplo do Dashboard

A imagem abaixo ilustra a interface do dashboard em funcionamento:

-----

## 🗄️ Banco de Dados

Os dados coletados pelos sensores são armazenados em um banco de dados para garantir a persistência, permitir análises históricas e fornecer a base para o treinamento contínuo dos modelos de Machine Learning.

  * **Estrutura SQL:** O arquivo `modelo_banco.sql` contém o script para criar a estrutura do banco de dados (tabelas e campos) para armazenar as leituras dos sensores.
  * **Flexibilidade:** A arquitetura permite integrar diferentes sistemas de banco de dados (ex: SQLite para protótipo, PostgreSQL para produção).

-----

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente:

1.  **Clone o Repositório:**

    ```bash
    git clone https://github.com/usuario/farmtech-fase4.git
    cd farmtech-fase4
    ```

2.  **Execute o Código do ESP32:**

      * Abra o arquivo `codigo_esp32/main.ino` na IDE do Arduino ou no PlatformIO.
      * Conecte seu ESP32 e faça o upload do código.
      * Você também pode simular o circuito e o código diretamente no **Wokwi** (link para o projeto Wokwi pode ser adicionado aqui, se houver).

3.  **Configure e Rode o Dashboard Streamlit:**

      * Navegue até o diretório do dashboard:
        ```bash
        cd dashboard_streamlit
        ```
      * Instale as dependências necessárias:
        ```bash
        pip install -r requirements.txt
        ```
      * Execute a aplicação Streamlit:
        ```bash
        streamlit run app.py
        ```
      * O dashboard será aberto automaticamente em seu navegador web.

4.  **Explore o Banco de Dados:**

      * Utilize o script `banco_dados/modelo_banco.sql` para criar o esquema do banco de dados em sua ferramenta SQL preferida (ex: DBeaver, pgAdmin).
      * Conecte seu sistema de ingestão de dados para popular o banco com as leituras do ESP32.

-----

## 👥 Equipe do Projeto

  * **Francismar Alves Martins Júnior**
  * **Antonio Ancelmo Neto Barros**
  * **Vitor Eiji Fernandes Teruia**
  * **Beatriz Pilecarte de Melo**
  * **Matheus Soares Bento da Silva**

-----

## 📜 Licença

[Inserir tipo de licença aqui, por exemplo: MIT License]

-----

# 📅 Kanban de Desenvolvimento (Fase 4)

Este Kanban visualiza o progresso das tarefas da Fase 4 do projeto, destacando os itens concluídos e as próximas etapas.

| 🔧 Planejamento             | 🔌 Montagem do Circuito           | 👨‍💻 Programação ESP32           | 📈 Dados & Machine Learning       | 📄 Documentação & Entrega           |
| :-------------------------- | :-------------------------------- | :------------------------------- | :-------------------------------- | :-------------------------------- |
| ✔ Definir escopo e sensores | ✔ Montar circuito no Wokwi       | ✔ Implementar leitura de sensores | ✔ Coletar/simular dados históricos| ✔ Preencher README detalhadamente |
| ✔ Distribuir tarefas        | ✔ Integrar display LCD (I2C)     | ✔ Exibir dados no LCD            | ✔ Realizar análise exploratória   | ✔ Organizar arquivos e imagens    |
| ✔ Criar repositório GitHub  | ✔ Gerar prints do circuito       | ✔ Configurar Serial Plotter      | ✔ Treinar e avaliar múltiplos modelos ML | ✔ Gravar vídeo de demonstração     |
|                             |                                  | ✔ Otimizar código ESP32          | ✔ Selecionar e justificar modelo final | ✔ Revisão final do projeto        |
|                             |                                  |                                 | ✔ Salvar modelo treinado (.pkl)   | ✔ Publicar no GitHub              |
|                             |                                  |                                 | ✔ Criar dashboard Streamlit       |                                   |
|                             |                                  |                                 | ✔ Modelar banco de dados          |                                   |
