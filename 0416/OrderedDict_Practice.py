from collections import OrderedDict

dt1 = {}
dt1['aaa'] = 'NewYork'
dt1['bbb'] = 'London'
dt1['ccc'] = 'Chicago'
dt1['ddd'] = 'Manchester'
dt1['eee'] = 'Tokyo'

dt2 = OrderedDict()
dt2['aaa'] = 'NewYork'
dt2['bbb'] = 'London'
dt2['ccc'] = 'Chicago'
dt2['ddd'] = 'Manchester'
dt2['eee'] = 'Tokyo'

dt3 = OrderedDict()
dt3['aaa'] = 'NewYork'
dt3['bbb'] = 'London'
dt3['ccc'] = 'Chicago'
dt3['ddd'] = 'Manchester'
dt3['eee'] = 'Tokyo'

print('Dictionary\n', dt1.keys())
print('Dictionary(Sort)\n', sorted(dt1.keys()))
print('OrderedDict\n', dt2.keys())
print('OrderedDict(Out of order)\n', dt3.keys())

print("딕셔너리", dt1)
print(dt2.values())
print(dt3)