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
   git clone https://github.com/seu-usuario/seu-repo.git
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

## 📝 Exemplo de tarefas.csv

```csv
Tarefa,Tipo,Dado
Abrir menu iniciar,click,iniciar
Esperar,espera,2
Pesquisar explorador,texto,explorador de arquivos
...
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
