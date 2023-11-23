# GS Artificial Care

## Descrição

Este projeto consiste em um serviço web Flask que fornece previsões de calorias queimadas e passos dados com base no tipo de treino, tempo (e distância, no caso de passos) fornecidos como parâmetros. Os modelos usados para previsões foram treinados previamente e armazenados nos arquivos 'calorias.pkl' e 'passos.pkl'.

## Estrutura do Projeto

``` Plain Text
|-- calorias.pkl
|-- GS_Artificial_Care.ipynb
|-- main.py
|-- passos.pkl
|-- README.md
|-- requirements.txt
```

- **calorias.pkl**: Modelo de regressão linear treinado para prever calorias queimadas.
- **GS_Artificial_Care.ipynb**: Notebook Jupyter utilizado para o desenvolvimento e treinamento dos modelos.
- **main.py**: Arquivo principal contendo o código Flask para a API de previsões.
- **passos.pkl**: Modelo de regressão linear treinado para prever passos dados.
- **README.md**: Documentação do projeto.
- **requirements.txt**: Lista de dependências do projeto.

## Instalação

Certifique-se de ter o Python instalado em sua máquina. Utilize o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Para iniciar o serviço web, execute o seguinte comando:

```bash
python main.py
```

Isso iniciará o servidor Flask em modo de depuração.

### API Endpoints

#### Previsão de Calorias

- **Endpoint:** `/calorias`
- **Método:** GET
- **Parâmetros:**
  - `workout_type`: Número de 1 a 11 representando o tipo de treino.
  - `time`: Tempo de duração do treino em minutos.
- **Exemplo de Uso:**

  ``` Plain Text
  GET http://localhost:5000/calorias?workout_type=1&time=30
  ```

#### Previsão de Passos

- **Endpoint:** `/passos`
- **Método:** GET
- **Parâmetros:**
  - `workout_type`: Número de 1 a 11 representando o tipo de treino.
  - `time`: Tempo de duração do treino em minutos.
  - `distance`: Distância percorrida durante o treino em kilômetros (apenas para tipos de treino que exigem essa informação).
- **Exemplo de Uso:**

  ``` Plain Text
  GET http://localhost:5000/passos?workout_type=1&time=30&distance=5
  ```

## Mapa de Tipo de Treino

- 'Treino livre': 1
- 'Bicicleta Ergométrica': 2
- 'Caminhada': 3
- 'Surfar': 4
- 'Ciclismo': 5
- 'Corrida ao ar livre': 6
- 'Corrida de Trilha': 7
- 'Natação': 8
- 'Trilha': 9
- 'Esteira': 10
- 'Críquete': 11

Certifique-se de fornecer os parâmetros corretos ao fazer chamadas à API.

---
Este projeto foi desenvolvido pela equipe 'Artificial Care Plus' e faz parte da GS da FIAP.
