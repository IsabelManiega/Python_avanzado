# 1) int
x = 10
print(type(x))

# 2) str
x = 'Hello'
print(type(x))

# 3) list
x = [10, 20, 30, 40]
print(type(x))

# 4) tuple
x = (10, 20, 30, 40)
print(type(x))

# 5) Dict
x = {'1': 'Paris', '2': 'Londres', '3': 'Madrid',}
print(type(x))
print(x.values)
print(x.values())
print(x.keys())
print(x.get('1'))
x['1'] = 'Berlin'
print(x.get('1'))
print(x.items())


