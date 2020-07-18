from insights import getUserInsights
from defines import getCreds
import pandas as pd
import datetime
import time

params = getCreds()
metric = 'email_contacts, follower_count, get_directions_clicks, impressions, phone_call_clicks, profile_views, reach, text_message_clicks, website_clicks'
columns = ['email_contacts', 'follower_count', 'get_directions_clicks', 'impressions', 'phone_call_clicks', 'profile_views', 'reach', 'text_message_clicks', 'website_clicks']
dic_columns = {'email_contacts':0, 'follower_count':1, 'get_directions_clicks':2, 'impressions':3, 'phone_call_clicks':4, 'profile_views':5, 'reach':6, 'text_message_clicks':7, 'website_clicks':8}
df_data = pd.DataFrame(columns = columns)
df_linha = dict()

data_start = datetime.datetime.now()

response = getUserInsights( params= params, metric= metric, datetime_end= data_start )

months = 25

for j in range(0,months):
    for data in range(29,-1,-1):
        df_linha['end_time'] = response['json_data']['data'][0]['values'][data]['end_time']
        for col in columns:
            df_linha[col] = response['json_data']['data'][dic_columns[col]]['values'][data]['value']
        df_int = pd.DataFrame(df_linha,index= [0])
        df_data = pd.concat([df_data, df_int], ignore_index= True, sort= True)
    data_start = data_start + datetime.timedelta(days= -30)
    response = getUserInsights( params= params, metric= metric, datetime_end= data_start)
    print('Month Completed {}'.format(j+1))

df_data.to_excel('user_media.xlsx',index=False )
print('\n                       Import Complete')