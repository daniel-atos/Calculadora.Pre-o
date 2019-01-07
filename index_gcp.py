import json
import sqlite3
import requests
def get_account_info():

    api_url = 'https://cloudbilling.googleapis.com/v1/services/6F81-5844-456A/skus?key=AIzaSyANB5RXQ0AqSgzZXPdodTm7JojHusTvIOk'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        with open('data_gcp.json', 'w') as f:
            json.dump(data, f)
        #return json.loads(response.content.decode('utf-8'))
    else:
        return None

account_info = get_account_info()
#if account_info is not None:
    #print("Aqui estão suas informações: ")
    #for k, v in account_info.items():
        #print('{0}:{1}'.format(k, v))

#else:
    #print('[!] Solicitação inválida')

