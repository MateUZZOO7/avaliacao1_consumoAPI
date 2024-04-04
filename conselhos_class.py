
import requests
import csv

class AdviceAPI:
    def __init__(self, url):
        self.url = url

    def get_advice(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json()
                return data['slip']['advice']
            else:
                print(f"Erro na requisição. Código de status: {response.status_code}")
                return None
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return None

class AdviceLogger:
    def __init__(self, filename):
        self.filename = filename

    def log_advice(self, advice):
        try:
            with open(self.filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([advice])
            print("Conselho salvo com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao salvar o conselho: {e}")

URL_API = "https://api.adviceslip.com/advice"

CSV_FILENAME = "conselhos.csv"


api = AdviceAPI(URL_API)

logger = AdviceLogger(CSV_FILENAME)

conselho = api.get_advice()

if conselho:
    logger.log_advice(conselho)
else:
    print("Falha ao obter o conselho.")