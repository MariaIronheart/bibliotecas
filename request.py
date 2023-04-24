import requests
#1
res = requests.get('https://scotch.io')

print(res)
#2
if res:
    print('Response OK')
else:
    print('Response Failed')
#3    
print(res.status_code)