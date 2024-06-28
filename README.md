# Projeto de Automação: Conversão de XML para Planilha

Este projeto consiste em um script Python que automatiza a extração de informações de um arquivo XML e as transforma em dados organizados em uma planilha Excel (.xlsx).

## Funcionalidades

- **Leitura de XML**: O script lê um arquivo XML específico (`arquivo.xml`).
- **Extração de Dados**: Extraímos informações como ID, Nome, Posição, Departamento e Salário de cada empregado listado no XML.
- **Criação da Planilha**: Os dados extraídos são organizados em uma planilha Excel usando a biblioteca `openpyxl`.
- **Salvamento da Planilha**: A planilha resultante é salva como `xml_empregados.xlsx`.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para o desenvolvimento.
- **Bibliotecas Python**:
  - `xml.etree.cElementTree`: Para análise e processamento do XML.
  - `openpyxl`: Para criar e manipular planilhas Excel.
