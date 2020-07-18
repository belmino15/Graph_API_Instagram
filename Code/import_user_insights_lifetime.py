from insights import getUserInsights
from defines import getCreds
import pandas as pd
import datetime
import time

params = getCreds()
metric = 'audience_city, audience_country, audience_gender_age, audience_locale, online_followers'
columns = ['audience_city', 'audience_country', 'audience_gender_age', 'audience_locale', 'online_followers']
dic_columns = {'audience_city':0, 'audience_country':1, 'audience_gender_age':2, 'audience_locale':3, 'online_followers':4}

response = getUserInsights( params= params, period= 'lifetime', metric= metric )

for col in columns:
    df_linha = dict()
    df_linha.update( response['json_data']['data'][dic_columns[col]]['values'][0]['value'] )
    df_data = pd.DataFrame(df_linha.items(), columns= [col, 'value'])
    df_data['end_time'] = response['json_data']['data'][0]['values'][0]['end_time']
    file_name = 'user_media_lifetime_' + col + '.xlsx'
    df_data.to_excel( file_name, index=False )

print('\n                       Import Complete')