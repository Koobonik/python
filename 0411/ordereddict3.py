def sort_by_key(t):
    return t[0]


from collections import OrderedDict

d = dict()
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

for k, v in OrderedDict(sorted(d.items(), key = sort_by_key)).items():
    print(k, v)