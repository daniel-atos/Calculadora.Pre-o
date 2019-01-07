import json
import sqlite3
import requests
def get_account_info():

    api_url = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/sa-east-1/index.json'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        with open('data_aws.json', 'w') as f:
            json.dump(data, f, indent=1)    #json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)#
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



    
#arq_json = ()
#traffic = json.load(open(''))
#db = sqlite3.connect("base_aws.db")
#query = "insert values (?,?,?,?,?,?,?)"
#columns = ['local',]
#for timestamp, data in traffic.iteritems():
#    keys = (timestamp,) + tuple(data[c] for c in columns)
#    c = db.cursor()
#    c.execute(query, keys)
#    c.close()