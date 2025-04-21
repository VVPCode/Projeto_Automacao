import pandas as pd
import pyautogui
import time
from openpyxl import Workbook
import json

def carregar_posicoes():
    try:
        with open('posicoes.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def executar_tarefa(tarefa, tipo, dado, posicoes):
    status = 'Sucesso'
    inicio = time.time()
    try:
        if tipo == 'click':
            if dado in posicoes:
                x, y = posicoes[dado]
                pyautogui.click(x, y)
            else:
                print(f"Elemento '{dado}' não encontrado nas posições.")
                status = 'Falha'
        elif tipo == 'texto':
            pyautogui.write(dado, interval=0.05)
        elif tipo == 'tecla':
            pyautogui.press(dado)
        elif tipo == 'espera':
            time.sleep(int(dado))
        elif tipo == 'atalho':
            teclas = dado.split('+')
            pyautogui.hotkey(*teclas)
        elif tipo == "db_click":
            if dado in posicoes:
                x, y = posicoes[dado]
                pyautogui.doubleClick(x, y)
        else:
            print(f"Tipo de tarefa desconhecido: {tipo}")
            status = 'Falha'
    except Exception as e:
        print(f"Erro ao executar tarefa '{tarefa}': {e}")
        status = 'Erro'
    tempo_total = round(time.time() - inicio, 2)
    return status, tempo_total

def gerar_relatorio(relatorio):
    wb = Workbook()
    ws = wb.active
    ws.append(["Tarefa", "Status", "Tempo (s)"])
    for item in relatorio:
        ws.append(item)
    wb.save("relatorio.xlsx")

def main():
    tarefas = pd.read_csv('tarefas.csv')
    posicoes = carregar_posicoes()
    relatorio = []

    print("Iniciando automação em 5 segundos...")
    time.sleep(5)

    for _, linha in tarefas.iterrows():
        tarefa = linha['Tarefa']
        tipo = linha['Tipo']
        dado = linha['Dado']
        print(f"Executando: {tarefa}")
        status, tempo = executar_tarefa(tarefa, tipo, dado, posicoes)
        relatorio.append([tarefa, status, tempo])

    gerar_relatorio(relatorio)
    print("Automação finalizada. Relatório gerado.")

if __name__ == "__main__":
    main()
