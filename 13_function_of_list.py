name = [10,34,56,76,54,34,56,43,23]

print(name)

name.append(10)
print("1 >",name)

name.sort()
print("2 >",name)

name.sort(reverse=True)
print("3 >",name)

name.reverse()
print("4 >",name)

name.insert(0,5)
print("5 >",name)

print(type(name))