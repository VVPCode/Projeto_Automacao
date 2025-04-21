# 🖱️ Projeto de Automação com PyAutoGUI

Este projeto tem como objetivo automatizar tarefas repetitivas no Windows usando Python e a biblioteca PyAutoGUI. As ações automatizadas são definidas em um arquivo CSV e executadas conforme a sequência programada, permitindo desde cliques e digitação até atalhos de teclado e geração de relatórios.

## 📁 Estrutura do Projeto

- `mapear_posicoes.py`: script para mapear e salvar posições de elementos na tela.
- `main.py`: script principal que executa as tarefas automatizadas com base em um CSV.
- `tarefas.csv`: define as tarefas a serem executadas.
- `posicoes.json`: arquivo gerado pelo script de mapeamento com as coordenadas dos elementos.
- `relatorio.xlsx`: arquivo gerado após a execução, contendo o status e o tempo de cada tarefa.

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [pandas](https://pypi.org/project/pandas/)
- [openpyxl](https://pypi.org/project/openpyxl/)
- json
- time

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/VVPCode/Projeto_Automacao.git
   cd seu-repo
   ```

2. Instale as dependências:
   ```bash
   pip install pyautogui pandas openpyxl
   ```

3. Mapeie os elementos necessários:
   ```bash
   python mapear_posicoes.py
   ```
   Isso vai gerar o arquivo `posicoes.json`.

4. Configure as tarefas em `tarefas.csv` (modelo já incluído).

5. Execute a automação:
   ```bash
   python main.py
   ```

6. Ao final, será gerado um relatório `relatorio.xlsx` com os resultados das tarefas.

## 🧪 Exemplo de Execução da Automação

Abaixo está um exemplo real de automação que pode ser feita com este projeto. A sequência de ações está definida no arquivo `tarefas.csv`:

### 🔄 Fluxo Automatizado:

1. Abre o menu iniciar
2. Pesquisa por "explorador de arquivos"
3. Abre o explorador
4. Navega até a área de trabalho, onde o usuário deve colocar a pasta do projeto para que o exemplo funcione
5. Entra em uma pasta chamada "Projeto_automacao"
6. Cria um novo documento de texto
7. Nomeia o arquivo como `exemplo.txt`
8. Abre o arquivo e digita um texto explicativo
9. Fecha o arquivo
10. Exclui o arquivo criado

Essa automação mostra como é possível reproduzir interações reais de um usuário com o sistema operacional usando PyAutoGUI e um CSV com instruções.

---

📂 Exemplo de tarefas do CSV:
```csv
Tarefa,Tipo,Dado
Abrir menu iniciar,click,iniciar
Pesquisar explorador de arquivos,texto,explorador de arquivos
Abrir explorador de arquivos,tecla,enter
Pesquisar área de trabalho,texto,Desktop
Abrir pasta do projeto,db_click,icone_pasta_projeto
Documento de texto,click,novo_txt
Nomeando arquivo,texto,exemplo
Abrir arquivo criado,db_click,arquivo_exemplo
Digitar texto,texto,"Oi, este eh um exemplo do funcionamento do projeto."
Fechar arquivo,atalho,alt+f4
Seleciona arquivo criado,click,arquivo_exemplo
Deleta arquivo criado,tecla,delete
```

## ✅ Tipos de Tarefas Suportados

| Tipo     | Ação                                             |
|----------|--------------------------------------------------|
| click    | Clica na posição nomeada                         |
| db_click | Clique duplo na posição nomeada                  |
| texto    | Digita o texto informado                         |
| tecla    | Pressiona uma tecla (ex: `enter`, `delete`)      |
| espera   | Espera o número de segundos informados           |
| atalho   | Executa um atalho de teclado (ex: `alt+f4`)      |

## 👨‍💻 Autor

Desenvolvido por Vitor Vieira Piroti (https://github.com/VVPCode)

## 🛡️ Licença

Este projeto está licenciado sob a Licença MIT.
