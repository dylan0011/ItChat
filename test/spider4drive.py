import requests, html5lib
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
}

# cookies = dict(SESSIONID='3E74906E4C93A6992B7F86DAECB9EB57')

login_url = 'http://hz.5u5u5u5u.com/hzlogin.action'
login_param = {'name': '342901199107051710', 'password': 'enjoyLIFE', 'validateCode': ''}

class_url = 'http://hz.5u5u5u5u.com/learning_json/queryCentralizedBusOrgsAndLessons.action'
class_param = {'lcode': 605623836}

submit_url = 'http://hz.5u5u5u5u.com/learning_json/doBespeak.action'
submit_param = {'lid': '796074621', 'ltype': 605623836}

ad = 'http://hz.5u5u5u5u.com/learning_json/doBespeak.action'
ads = {'lid': "796074620,", 'ltype': "605623836"}

# r = requests.post(login_url, data=login_param, headers=headers)
# print(r)
# print(r.cookies)
# print(r.text)
# print()
#
# r = requests.post(class_url, data=class_param, headers=r.headers)
# print(r)
# print(r.cookies)
# print(r.text)
# print()
#
# r = requests.post(submit_url, data=submit_param, headers=r.headers)
# print(r)
# print(r.cookies)
# print(r.text)

cn_bing_url = 'http://cn.bing.com/'
wb_data = requests.get(cn_bing_url, headers=headers)

soup = BeautifulSoup(wb_data.text, "html5lib", from_encoding='utf-8')

print(soup.prettify())
