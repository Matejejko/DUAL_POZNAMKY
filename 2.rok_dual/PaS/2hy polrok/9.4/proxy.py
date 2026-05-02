import requests
proxy_url = "http://10.168.62.171:8080"
proxiny = {"https": proxy_url, "http": proxy_url}
response = requests.get("https://github.com", proxies=proxiny)
print(response.status_code)
