import simplejson as json

data = {}  # dict
data['people'] = []

data['people'].append({
    'name': 'kim',
    'website': 'naver.com',
    'from': 'Seoul',
})

data['people'].append({
    'name': 'park',
    'website': 'google.com',
    'from': 'Busan',
})

data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon',
})

# print(type(data))
# print(data)

# Dict => str (직렬화)
e = json.dumps(data, indent=4)
# print(type(e))
# print(e)

# print('------------------------------------------')
# str => Dict
d = json.loads(e)
# print(type(d))
# print(d)

# Json 파일 쓰기
with open('data/member.json', "w") as outfile:
    outfile.write(e)

# Json 파일 읽기
with open('data/member.json', "r") as infile:
    r = json.loads(infile.read())
    for p in r['people']:
        print('Name : ' + p['name'])
        print('Website : ' + p['website'])
        print('From : ' + p['from'])
        print('')
