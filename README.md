# Festival UNIFEI: Sistema de Gerenciamento de Filas

### Projeto para a Professora Bárbara

---

## Resumo do Projeto
Este projeto é um **sistema em Python** desenvolvido para fins **educativos e demonstrativos**, simulando um festival com recursos de organização de filas e controle de acesso.

Ele implementa as seguintes funcionalidades, acessíveis via **Interface de Linha de Comando (CLI)** através do arquivo `terminal.py`:

* **Gerenciamento de Ingressos:** Criação, registro e estatísticas de ingressos.
* **Gerenciamento de Filas:** Atendimento em modo **padrão (FIFO)** ou **prioridade (para VIPs)**.
* **Histórico de Ações:** Suporte a comandos **desfazer/refazer** (Undo/Redo) via estrutura de Pilha.
* **Roteiro/Mapa de Navegação:** Simulação de localização e movimentação pelo mapa do festival.

---

## Requisitos
* **Python 3.8+** (testado com Python 3.12).
* Apenas **bibliotecas padrão** do Python (como `collections`).
* **Recomendado:** Rodar via PowerShell, cmd ou terminal do VS Code para melhor compatibilidade.

---

## Estrutura do Projeto
O sistema é modular, com cada arquivo `.py` responsável por uma funcionalidade específica:

| Arquivo | Função |
| :--- | :--- |
| `terminal.py` | Interface principal (CLI). Recebe comandos e coordena os módulos. |
| `ingressos.py` | Criação, registro e estatísticas dos ingressos. |
| `fila.py` | Estrutura da fila (modo **PADRÃO** e **PRIORIDADE**). Enfileirar, desenfileirar, listar e remover. |
| `pilha.py` | Histórico de ações (**desfazer/refazer**) com “fotos” do estado atual. |
| `roteiro.py` | Manipulação de mapa/roteiro e posição (comandos de navegação). |

> **Atenção:** Certifique-se de que todos os arquivos listados estão na mesma pasta para o funcionamento correto do sistema, especialmente o `roteiro.py` para os comandos de mapa.

---

## Como Executar

1.  Abra o **terminal** (PowerShell, cmd, ou terminal do VS Code).
2.  Navegue até a pasta do projeto:
    ```bash
    cd "C:\caminho\para\sua\pasta\do\projeto"
    ```
3.  Inicie o sistema com o interpretador Python:
    ```bash
    python terminal.py
    ```
4.  O sistema aguardará comandos no prompt interno:
    ```
    festival>
    ```

> **Observação:** Não tente digitar comandos como `ajuda` diretamente no terminal do sistema operacional (PowerShell). Eles só funcionarão após iniciar o script `terminal.py` e aparecer o prompt `festival>`.

---

## Comandos Suportados

### Ingressos e Filas

| Comando | Descrição |
| :--- | :--- |
| `comprar <nome> <tipo>` | Cria um ingresso e adiciona à fila. Tipos: `VIP`, `INTEIRA`, `MEIA`. |
| `entrar` | Processa (atende) o próximo da fila. |
| `espiar` | Mostra o próximo da fila sem removê-lo. |
| `cancelar <id>` | Remove um ingresso pendente da fila, usando seu ID. |
| `listar` | Exibe todos na fila atual. |
| `estatisticas` | Mostra totais, atendidos, pendentes, por tipo e média de espera. |
| `modo <padrao/prioridade>` | Altera a política de atendimento da fila. |

### Mapa e Roteiro

| Comando | Descrição |
| :--- | :--- |
| `ir <destino>` | Vai para um novo local no mapa. |
| `voltar` | Retorna à posição anterior. |
| `avancar` | Avança no roteiro de navegação. |
| `onde` | Mostra a posição atual no festival. |
| `mapa` | Exibe o mapa completo de locais. |

### Histórico de Ações

| Comando | Descrição |
| :--- | :--- |
| `desfazer` | Desfaz a última ação do usuário. |
| `refazer` | Refaz uma ação que foi desfeita. |

### Geral

| Comando | Descrição |
| :--- | :--- |
| `ajuda` | Mostra a lista de comandos disponíveis. |
| `sair` | Encerra o programa. |

---

## Exemplos Práticos

### 1. Criar, listar e atender ingressos

```bash
festival> comprar joao VIP
festival> comprar maria MEIA
festival> listar
# Fila (modo PADRÃO):
# 1) João — VIP
# 2) Maria — MEIA
festival> entrar
# Atendido: João (VIP)
````

### 2\. Navegação e Estatísticas

```bash
festival> ir palco
# Você está em: Palco Principal
festival> estatisticas
# Total: 2 | Pendentes: 1 | Atendidos: 1
# VIP: 1 | INTEIRA: 0 | MEIA: 1
# Média de espera: 3.5s
```

### 3\. Desfazer uma ação

```bash
festival> desfazer
# Última ação desfeita/refeita com sucesso.
festival> listar
# Fila (modo PADRÃO):
# 1) João — VIP
# 2) Maria — MEIA
```

-----

## Dicas Úteis

  * O recurso de histórico permite que **todos os comandos** de gerenciamento de filas e navegação sejam desfeitos e refeitos.
  * O código foi estruturado para ser **modular**, facilitando o estudo das estruturas de dados (fila, pilha) e o controle de estado.

-----

## Dicas de Depuração

  * **Erro de comando não reconhecido** (`ajuda : The term 'ajuda' is not recognized...`): Confirme que você iniciou o script corretamente com `python terminal.py` e está digitando o comando dentro do prompt `festival>`.
  * **`ModuleNotFoundError`:** Verifique se todos os arquivos (`terminal.py`, `ingressos.py`, `fila.py`, `pilha.py`, `roteiro.py`) estão na **mesma pasta**.
  * **Inicialização:** Certifique-se de que o final do seu arquivo `terminal.py` contém o bloco de execução principal:
    ```python
    if __name__ == "__main__":
        main()
    ```

-----

## Licença e Notas

Este projeto é de caráter **educativo e demonstrativo**, desenvolvido como um exercício prático de programação e aplicação de estruturas de dados. O código é simples, modular e intencionalmente fácil de estender para novos recursos.

-----

Desenvolvido pela Equipe de Engenharia de Controle e Automação — UNIFEI.

```
