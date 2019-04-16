from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():  # keys 랑 values 만 이용할 수도 있음
    print(k, v)