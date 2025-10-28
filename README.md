# Festival UNIFEI  
### Sistema de Gerenciamento de Filas — Projeto para a Professora Bárbara

## Resumo
Pequeno sistema em **Python** para gerenciar **ingressos**, **filas** (modo padrão e prioridade), **histórico de ações** e um **roteiro/mapa**.  
A interface é feita por **linha de comando (CLI)** através do arquivo `terminal.py`.

---

## Requisitos
- **Python 3.8+** (testado com **Python 3.12**)
- Apenas **biblioteca padrão** (`collections`)

---

## Estrutura de Arquivos
| Arquivo | Função |
|----------|--------|
| `terminal.py` | Interface principal (CLI). Recebe comandos e coordena os módulos. |
| `ingressos.py` | Criação, registro e estatísticas dos ingressos. |
| `fila.py` | Estrutura da fila (modo **PADRÃO** e **PRIORIDADE**): enfileirar, desenfileirar, listar e remover. |
| `pilha.py` | Histórico de ações (**desfazer/refazer**) com “fotos” do estado atual. |
| `roteiro.py` | Manipulação de mapa/roteiro e posição. Necessário para comandos de navegação. |

> ⚠️ Caso o arquivo `roteiro.py` falte, verifique o repositório — ele é necessário para os comandos de **mapa/rota**.

---

## Como Executar

1. Abra o **PowerShell** ou o **terminal do VS Code**  
2. Navegue até a pasta do projeto:
   ```bash
   cd "C:\Users\Home\Documents\pyton"
3. Execute o programa:
  '''bash
  python terminal.py


5.   
