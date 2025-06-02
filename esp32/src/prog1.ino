import ujson
import network
import time

# Conectar-se à rede Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    time.sleep(0.1)

# Dados a serem gravados no arquivo
dados = {
    "temperatura": 25.5,
    "umidade": 60
}

# Simulando a criação de um arquivo .txt
conteudo = ujson.dumps(dados)
print("Conteúdo do arquivo:", conteudo)
