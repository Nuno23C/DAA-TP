import json
import requests

def obter_dados_meteorologicos(cidade, data_inicio, data_fim, latitude, longitude):
    api_key = "b5397d87f6eb40318ebcc4288726e736"
    base_url = "https://api.weatherbit.io/v2.0/history/hourly"

    params = {
        'city': cidade,
        'start_date': data_inicio,
        'end_date': data_fim,
        'lat': latitude,
        'lon': longitude,
        'key': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        dados_meteorologicos = response.json()
        return dados_meteorologicos
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

# Substitua 'SUA_WEATHERBIT_API_KEY' pela sua chave de API do Weatherbit
cidade = 'Braga'
data_inicio = '2022-01-01'
data_fim = '2023-01-01'
latitude = '41.5518'
longitude = '-8.4229'

dados = obter_dados_meteorologicos(cidade, data_inicio, data_fim, latitude, longitude)

if dados:
    print(f"Dados meteorológicos para {cidade} entre {data_inicio} e {data_fim}:\n")
    # Salvar dados em um arquivo JSON
    with open('dadosWB22.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=2)
    print("Dados salvos com sucesso no arquivo 'dadosWB21.json'")
else:
    print("Não foi possível obter os dados meteorológicos.")
