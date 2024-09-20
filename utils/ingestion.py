import requests
import json
import os
import datetime

class Collector:
    '''
    Classe principal, para coletar e salvar os dados.
    
    Args:
        url: URL do endpoint que será requisitado
        prefix: Prefixo para salvar o arquivo no diretório correto.
    '''
    def __init__(self, url, prefix):
        self.url = url
        self.prefix = prefix

    def get_file(self):
        resp = requests.get(self.url)
        if resp.status_code == 200:  # se retornar com sucesso, extrai
            print("Success.")
            return resp.json().get('data')  # acessa 'data' da resposta JSON
        else:
            print(f"Failed. Status code: {resp.status_code}")  # se der erro, exibe o status code
            return None

    def save_file(self, data, file_path):
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")  # hora/minuto/segundo/milisegundo para o nome do arquivo
        os.makedirs(file_path, exist_ok=True)  # se não existir o diretório, cria
        full_path = os.path.join(file_path, f"{now}.json")

        with open(full_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"File saved to path {full_path}")

    def get_and_save(self):
        file_path = f"/home/leandro/dev/yugioh/yugioh/data/{self.prefix}/"
        data = self.get_file()
        if data:
            print("Saving data.")
            self.save_file(data, file_path)
        else:
            print("Failed to get data! Try again.")
