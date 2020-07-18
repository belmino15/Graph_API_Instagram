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

```python
print('teste')
```
# Reference

This code was based on the excellent code proposed by github.com/jstolpe and the great video at https://youtu.be/dEDKOcPuXlU
