import requests
import sys


rl = 'todos'
rl2 = 'users'
url = 'https://jsonplaceholder.typicode.com/'

response = requests.get(url + rl2)

if response.status_code == 200:
    json_data = response.json()
    for k in json_data:
        if k['id'] == int(sys.argv[1]):
            name = k['name']
    response2 = requests.get(url + rl)
    if response2.status_code == 200:
        json_data = response2.json()
        all = 0
        done = 0
        donelist = []
        for i in json_data:
          if i['userId'] == int(sys.argv[1]):
            all += 1
            if i['completed'] == True:
                donelist.append(i['title'])
                done += 1
    print("Employee {} is done with tasks({}/{}):".format(name, done, all))
    for i in donelist:
        print('\t' + i)
    


else:
    print(f"Error: {response.status_code}")