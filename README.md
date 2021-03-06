# Graph_API_Instagram

This project aims to present a way to access the Instagram API using python. Although it is a prototype designed to study the use of API and data extraction, this repository will present each of the actions performed so that everyone can use them to extract their own data. The purpose of data extraction is to allow analysis using machine learning from the data.

# Switch to Professional Account

If you plan to use your personal account to learn how to use the Graph API. The first step is to change your account to a professional account.

Please note that for accessing various information (visit the documentation at https://developers.facebook.com/docs/instagram for more information) your account must be professional for at least seven days and have more than 100 followers.

Professional instagram accounts need a Facebook account to link, this Facebook account will be required for your access.The accesses I used were through an Instagram account linked to a personal Facebook account and an Instagram account linked to a Facebook page. In the second case, it was necessary that the Facebook developer account was elevated to the position of administrator of the page.

# Generate Token

After associating the instagram account with the desired facebook account. Visit https://developers.facebook.com/ and create a App. In Tools access the Graph API Explorer tool and generate your User Token.

The required permissions are:
- instagram_basic
- instagram_manage_comments
- instagram_manage_insights
- pages_read_user_content
- pages_show_list

# Definition of Credentials

You must add the information below in the **defines.py** file.
- ACCESS-TOKEN;
- FB-APP-CLIENT-ID;
- FB-APP-CLIENT-SECRET.

In the following fields:

```python
creds['access_token'] = 'ACCESS-TOKEN'
creds['client_id'] = 'FB-APP-CLIENT-ID'
creds['client_secret'] = 'FB-APP-CLIENT-SECRET'
```

The information from the last two fields is obtained in your app in Settings > Basic.

# What's next?

The README will still be implemented to add further details to the explanation.

For now please note that to check if your Token is ok, you must use **debug_access_token.py**. Afterwards, you must redo your Token with an expiration date higher with **get_long_lived_access_token.py**.

Use **get_user_pages.py** and **get_instagram_account.py** to get the ID to complete the **define.py** informations that you don't have yet.

Than you can use the **import_id_media.py**, **import_user_insights.py**, **import_user_insights_lifetime.py** to import the data from the Instagram account.

# Reference

This code was based on the excellent code proposed by github.com/jstolpe and the great video at https://youtu.be/dEDKOcPuXlU
