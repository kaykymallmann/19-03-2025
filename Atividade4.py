import requests

def consultar_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            if "resultado" in dados and isinstance(dados["resultado"], list) and len(dados["resultado"]) > 0:
                return dados["resultado"]
            else:
                return "Nenhum resultado encontrado."
    except (requests.exceptions.RequestException, ValueError, json.JSONDecodeError) as e:
        print(f"Erro: {str(e)}")
        return "Erro ao processar a requisição ou JSON."
    
    return "Erro na requisição"

print(consultar_api("https://api.exemplo.com/dados"))

