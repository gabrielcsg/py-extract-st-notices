# Extração de Dados de Editais da Prefeitura de Serra Talhada

Este projeto realiza a extração de dados de editais publicados pela Prefeitura de Serra Talhada utilizando as bibliotecas Python `requests`, `pandas`, `beautifulsoup4` e `openpyxl`.

## Sumário

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Descrição

Este projeto visa automatizar a extração de dados de editais disponibilizados pela Prefeitura de Serra Talhada. Através de web scraping, os dados são coletados e organizados em um formato estruturado para fácil análise e utilização.

## Funcionalidades

- Extração de dados de editais diretamente do site da Prefeitura de Serra Talhada utilizando as bibliotecas `requests` e `beautifulsoup4`.
- Processamento, limpeza dos dados, Armazenamento dos dados extraídos em planilhas Excel através utilizando a biblioteca `pandas`.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - `requests`
  - `pandas`
  - `beautifulsoup4`
  - `openpyxl`

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/gabrielcsg/py-extract-st-notices.git
   cd py-extract-st-notices
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para executar o script de extração de dados, utilize o seguinte comando:

```bash
python main.py
```

Os dados extraídos serão salvos em um arquivo Excel na pasta raiz do projeto.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests. Para grandes mudanças, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Licença

Este projeto está licenciado sob a Licença MIT.
