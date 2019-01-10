import pymysql, os, json, time
file = "C:/Users\A738775\Documents\Calculator\data_aws.json"
json_data=open(file).read()
json_obj = json.loads(json_data)
lista_sku = list(json_obj['products'])
con = pymysql.connect(host = 'localhost',user = 'root',passwd = 'root',db = 'test')
cursor = con.cursor()
cursor.execute("DROP TABLE aws2")
cursor.execute("CREATE TABLE aws2 (sku VARCHAR(255),CPU VARCHAR(255),RAM VARCHAR(255),LOC VARCHAR(255),PRECO VARCHAR(255))")

for x in lista_sku:
    if json_obj['products'][x]['productFamily'] == 'Compute Instance' :
        vcpu = json_obj['products'][x]['attributes']['vcpu']
        ram = json_obj['products'][x]['attributes']['memory']
        loc = json_obj['products'][x]['attributes']['location']
        cursor.execute("INSERT INTO aws2 (sku,CPU,RAM,LOC) VALUES (%s,%s,%s,%s)", (x,vcpu,ram,loc))
con.commit()
con.close()