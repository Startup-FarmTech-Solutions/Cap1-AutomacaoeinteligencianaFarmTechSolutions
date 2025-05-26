# Levantamento de Requisitos – FarmTech Solutions – Fase 4

## 1. Requisitos Funcionais (RF)  
Funcionalidades que o sistema **deve realizar**.

| Código | Descrição |
|--------|-----------|
| **RF01** | O sistema deve coletar dados de umidade do solo e nutrientes usando sensores conectados ao ESP32. |
| **RF02** | O ESP32 deve exibir as leituras em tempo real no display LCD (via I2C). |
| **RF03** | O sistema deve enviar os dados coletados para um banco de dados externo. |
| **RF04** | O backend Python deve processar esses dados e armazená-los corretamente. |
| **RF05** | O sistema deve utilizar um modelo de Machine Learning (via Scikit-learn) para prever a necessidade de irrigação com base no histórico de dados. |
| **RF06** | Deve haver uma interface gráfica interativa em Streamlit, que exiba:<br>– Gráficos da umidade e nutrientes<br>– Status atual do sistema<br>– Previsões do modelo de ML |
| **RF07** | O ESP32 deve utilizar o Serial Plotter para gerar gráficos em tempo real das variáveis monitoradas. |
| **RF08** | O sistema deve enviar alertas no display LCD sobre a necessidade de irrigação ou status crítico. |
| **RF09** | O sistema deve otimizar o uso de memória no ESP32, utilizando tipos de dados adequados. |
| **RF10** | Todo o código deve estar versionado e documentado no GitHub, com README atualizado. |

## 2. Requisitos Não Funcionais (RNF)  
Restrições, padrões de qualidade e desempenho.

| Código | Descrição |
|--------|-----------|
| **RNF01** | O código no ESP32 deve ser otimizado, reduzindo o uso de memória RAM e flash. |
| **RNF02** | A interface em Streamlit deve ser responsiva, clara e de fácil navegação. |
| **RNF03** | O sistema deve garantir atualização em tempo real dos dados (mínimo delay possível). |
| **RNF04** | O banco de dados deve ser seguro e escalável, suportando aumento na quantidade de registros. |
| **RNF05** | O repositório no GitHub deve seguir padrões profissionais de documentação. |
| **RNF06** | O vídeo de apresentação deve ter no máximo 5 minutos, bem editado e explicativo. |
| **RNF07** | O uso do Serial Plotter deve ser demonstrado com prints explicados no README. |
| **RNF08** | O sistema precisa rodar de forma eficiente na simulação do Wokwi, sem travamentos. |

## 3. Requisitos de Hardware  

| Item | Descrição |
|------|-----------|
| **ESP32** | Microcontrolador principal. |
| **Sensor de Umidade do Solo** | Para medir a umidade da terra. |
| **Sensor de Nutrientes (Simulado)** | Para indicar a qualidade do solo, como níveis de nitrogênio, fósforo e potássio. |
| **Sensor de Temperatura** | Para monitorar a temperatura do ambiente, importante para decisão da irrigação. |
| **Display LCD 16x2 (I2C)** | Mostrar informações críticas em tempo real. |
| **Conexão Wi-Fi** | Envio dos dados para backend/banco de dados. |


## 4. Requisitos de Software  

| Ferramenta/ Biblioteca | Descrição                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------|
| **Python 3.x**        | Linguagem principal para desenvolvimento do backend, machine learning e interface web.               |
| **Scikit-learn**      | Biblioteca de Machine Learning para criação e treinamento de modelos preditivos baseados nos dados coletados dos sensores. |
| **Streamlit**         | Framework para criação de dashboards interativos, onde serão exibidos gráficos, status e previsões do sistema de irrigação em tempo real. |
| **Banco de Dados (MySQL, PostgreSQL ou SQLite)** | Sistema para armazenar os dados históricos coletados pelos sensores e gerar consultas para análise e visualização. |
| **Arduino IDE / Wokwi** | Ambiente para desenvolvimento do firmware em C/C++ para o ESP32, controle dos sensores e do display LCD. |
| **Git/GitHub**        | Controle de versão, hospedagem do código-fonte, documentação e integração contínua do projeto.        |
| **Serial Plotter (Arduino IDE/Wokwi)** | Ferramenta para monitoramento gráfico em tempo real dos dados enviados pelo ESP32, facilitando a análise visual durante o desenvolvimento. |


## 5. Requisitos de Integração  

| Código | Descrição |
|--------|-----------|
| **RI01** | Integração do ESP32 com o display LCD (via I2C). |
| **RI02** | Integração do ESP32 com o banco de dados através do backend Python. |
| **RI03** | Integração entre o modelo de Machine Learning (Scikit-learn) e o dashboard Streamlit. |
| **RI04** | O backend deve consumir os dados dos sensores e alimentar tanto o banco quanto o ML. |
| **RI05** | O Streamlit deve consumir o banco e apresentar dados e previsões. |

## 6. Objetivos da Fase 4  

- ✔️ Melhorar a inteligência do sistema usando Machine Learning (Scikit-learn).  
- ✔️ Implementar uma interface gráfica funcional e interativa (Streamlit).  
- ✔️ Mostrar informações em tempo real no hardware (display LCD).  
- ✔️ Monitorar os dados visualmente via Serial Plotter.  
- ✔️ Otimizar o uso de memória no ESP32.  
- ✔️ Entregar código funcional, bem documentado e hospedado no GitHub.  
- ✔️ Criar um vídeo didático e bem editado para a apresentação final.

## 7. Variáveis Principais

| Variável       | Tipo      | Descrição                                                                 |
|----------------|-----------|---------------------------------------------------------------------------|
| `umidade`      | float     | Valor da umidade do solo coletado pelo sensor, em percentual (%)           |
| `nutrientes`   | float     | Índice ou nível dos nutrientes do solo (NPK), valor simulado ou real       |
| `temperatura`  | float     | Temperatura ambiente medida pelo sensor, em graus Celsius (°C)             |
| `hora`         | datetime  | Registro do horário da coleta dos dados                                    |
| `status_irrigacao` | boolean | Estado atual da irrigação (ligado/desligado)                              |
| `previsao_irrigacao` | boolean | Saída do modelo preditivo indicando se é necessária irrigação futura      |
| `nivel_bateria`| float     | Nível da bateria do dispositivo ESP32, em percentual (%)                   |
| `memoria_esp32`| int       | Uso atual de memória RAM do ESP32, em bytes                                |
| `sinal_wifi`   | int       | Força do sinal Wi-Fi conectado ao ESP32, em dBm                            |

## 8. Hardware Adicional

| Componente       | Descrição                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------|
| **ESP32**        | Microcontrolador principal do projeto, responsável por coletar dados dos sensores, processar informações e comunicar com o backend via Wi-Fi. |
| **Display LCD 16x2 (I2C)** | Tela para exibir em tempo real as principais métricas do sistema, como umidade do solo, níveis de nutrientes, temperatura e status da irrigação. Utiliza protocolo I2C para conexão com o ESP32. |
| **Módulo Wi-Fi integrado no ESP32** | Permite a comunicação sem fio para envio de dados ao backend e banco de dados.                  |
| **Placa de prototipagem (Breadboard)** | Facilita a montagem e conexão dos sensores e display durante o desenvolvimento e testes.       |
| **Fonte de alimentação** | Fonte adequada para alimentar o ESP32 e sensores com voltagem e corrente estáveis.              |
| **Cabos e conectores** | Fios para conexão elétrica dos sensores, display e ESP32, garantindo a integridade do circuito.     |


