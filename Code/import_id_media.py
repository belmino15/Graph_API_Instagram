from insights import getUserMedia
from defines import getCreds
import pandas as pd
import json
import os
import contextlib
import requests
import time
import numpy as np

params = getCreds() # get creds
response = getUserMedia( params ) # get users media from the api
list_df = []
columns = ['id', 'caption', 'media_type', 'media_url', 'permalink','thumbnail_url', 'timestamp', 'username']
for i in range(0,128):

    with open('result.json', 'w') as fp:
        json.dump(response['json_data'], fp)

    data = json.load(open('result.json'))
    try:
        df_data = pd.DataFrame(data["data"])
    except KeyError as e:
        print("An error has occurred in loop {}. The error message is {}.".format(i,e))
        df_data = pd.DataFrame(columns = columns)
        

    data = json.load(open('result.json'))
    df_pag = pd.DataFrame(data["paging"])
    
    if df_data.shape[1] == 7:
        df_data['thumbnail_url'] = np.nan
        df_data = df_data[columns]

    list_df.append(df_data) 


    url = df_pag.loc['after','next']
    time.sleep(40)

    data = requests.get( url ) # make get request

    response = dict() # hold response info
    response['json_data'] = json.loads( data.content ) # response data from the api

df = pd.concat([f for f in list_df])
df.to_excel('id_media.xlsx',index=False )