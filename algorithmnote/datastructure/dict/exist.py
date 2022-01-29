# dict 구조에서 해당 요소가 존재하는지 확인하기
anydict = {"name": "BMW", "practice": "7000"}

if "name" in anydict:
    print('Key exist!')
else:
    print('Key does not exist!')


if anydict.get("name"):
    print('Key exist')
else:
    print('Key does not exist!')
