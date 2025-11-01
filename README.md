# 🧪 Projeto de Cobertura de Testes (Qualidade e Testes de Software)

Este repositório contém um conjunto de módulos e testes automatizados desenvolvidos como parte da disciplina **Qualidade e Testes de Software** da FATEC.  
O objetivo principal é praticar **testes unitários**, **cobertura de código** e **boas práticas de TDD (Test Driven Development)** em Python com `pytest`.

---

## 🧰 Tecnologias e Ferramentas

- **Linguagem:** Python 3.12+
- **Framework de Teste:** [pytest](https://docs.pytest.org/)
- **Cobertura de Código:** [pytest-cov](https://pytest-cov.readthedocs.io/)
- **Ambiente Virtual:** venv
- **Editor recomendado:** Visual Studio Code

---

## 📁 Estrutura do Projeto

projeto_teste_cobertura/
│
├── projeto/
│ ├── src/
│ │ ├── init.py
│ │ ├── estoque.py # Implementação da Tarefa 3
│ │ └── (... demais tarefas podem ser adicionadas aqui)
│ │
│ └── tests/
│ ├── test_estoque.py # Testes do módulo de estoque
│ └── (... demais testes)
│
├── .gitignore
├── requirements.txt
├── pytest.ini
└── README.md

  
## ⚙️ Como Executar o Projeto  
  
### 1. Criar e ativar o ambiente virtual  
```bash  
python -m venv .venv  
# Ativar (Windows PowerShell)  
.venv\Scripts\Activate.ps1  
# Ativar (Linux/Mac)  
source .venv/bin/activate

### 2. Instalar dependências

```bash

pip install -r requirements.txt  

### 3. Rodar os testes

```bash

pytest