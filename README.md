# Cap1-AutomacaoeinteligencianaFarmTechSolutions
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

* Biblioteca: Scikit-learn
* Algoritmo: Random Forest Classifier
* Objetivo: Previsão da necessidade de irrigação.

![Gráfico Predição](./imagens/grafico_predicao.png)

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
