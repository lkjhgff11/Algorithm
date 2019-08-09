import operator
product = {"TV": 2000000,
           "냉장고": 1500000,
           "책상": 350000,
           "노트북": 1200000,
           "가스레인지": 200000,
           "세탁기": 1000000,}


# value 값을 기준으로 정렬하는데 reverse = True해서 내림차순 정렬한다.
ps = dict(sorted(product.items(),key = operator.itemgetter(1),reverse = True))

for key,value in ps.items():
    print("{}: {}".format(key,value))
