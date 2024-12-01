# cdv_analytics

Data Analytics case for Casa dos Ventos

## Como rodar

Após clonar o repositório, e configurar o virtual environment, instale as dependências do projeto executando:

```powershell
pip install .
```

ou usando poetry:

```powershell
poetry install
```

O arquivo principal referente ao projeto é o notebook "data_etl.ipynb", na pasta cdv_analytics, o qual contém as explicações e passo a passo desde a obtenção dos dados, processamento e limpeza dos dados até finalmente exportá-los no formato ".csv" para visualização no Tableau.

Os arquivos baixados ou gerados durante a execução do notebook encontram-se na pasta outputs e as visualizações no Tableau podem ser acessadas a partir dessa [Dashboard](https://public.tableau.com/app/profile/nuno.alvares.de.paula.monteiro/viz/Aerogeradores/Painel1).

Esta [apresentação](https://docs.google.com/presentation/d/1mnBtyNZZFU28fkppKuJJ22__dGRVrPM5cr2VYXTeZy4/edit?usp=sharing) contém um resumo dos principais insights e análise dos dados.
