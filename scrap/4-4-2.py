import simplejson as json

data = {}  # dict
data['people'] = []

data['people'].append({
    'name': 'kim',
    'website': 'naver.com',
    'from': 'Seoul',
    'grade': [95, 77, 89, 91]
})

data['people'].append({
    'name': 'park',
    'website': 'google.com',
    'from': 'Busan',
    'grade': [85, 88, 79, 81]
})

data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon',
    'grade': [80, 85, 90, 96]
})

# Json 파일 쓰기
with open('data/member2.json', "w") as outfile:
    json.dump(data, outfile)

# Json 파일 읽기
with open('data/member2.json', "r") as infile:
    r = json.load(infile)
    for p in r['people']:
        print('Name : ' + p['name'])
        print('Website : ' + p['website'])
        print('From : ' + p['from'])
        t = p['grade']
        grade = ''
        for g in t:
            grade = grade + ' ' + str(g)
            print('Grade : ', grade.lstrip())
            print('')
