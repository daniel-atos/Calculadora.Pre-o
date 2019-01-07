
import json
import sqlite3


with open('data_aws.json') as f:
    data = json.loads(f.read())

nodes = data['products']
str_data = json.dumps({"nodes": nodes})
# get data string from DB column and load into json
db_data = json.loads(db_col_data)
# get new/latest 'nodes' data from api as explained above
# append this data to 'db_data' json as
latest_data = db_data["nodes"] + new_api_nodes
# now add this data back to column after json.dumps()
db_col_data = json.dumps(latest_data)
# add to DB col and DB commit