import pyautogui
import json
import time

posicoes = {}

print("=== Mapeamento de Posições ===")
print("Esse script vai capturar posições do mouse na tela.")
print("Digite 'sair' quando terminar.\n")

while True:
    nome = input("Nome do elemento (ou 'sair' para finalizar): ").strip()
    if nome.lower() == 'sair':
        break
    print("Posicione o mouse sobre o elemento em 5 segundos...")
    time.sleep(5)
    x, y = pyautogui.position()
    posicoes[nome] = (x, y)
    print(f"Posição registrada para '{nome}': ({x}, {y})\n")

with open("posicoes.json", "w") as f:
    json.dump(posicoes, f)

print("\nMapeamento concluído! Arquivo 'posicoes.json' salvo com sucesso.")
