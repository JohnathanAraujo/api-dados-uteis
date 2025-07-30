import requests

def buscar_cep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url, timeout=5)  # timeout de segurança
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            return {"erro": "CEP não encontrado na base do ViaCEP."}

        return dados

    except requests.exceptions.Timeout:
        return {"erro": "A consulta ao ViaCEP demorou demais e foi cancelada (timeout)."}

    except requests.exceptions.HTTPError as e:
        return {"erro": f"Erro HTTP ao consultar o ViaCEP: {e.response.status_code}"}

    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro geral de requisição: {str(e)}"}

    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}
