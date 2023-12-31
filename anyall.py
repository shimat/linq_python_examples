values = [1, 2, 3]

print(any(x >= 3 for x in values))
print(any(x > 3 for x in values))

print(all(x <= 3 for x in values))
print(all(x <= 2 for x in values))

print()

print(any(True for x in []))
print(any(False for x in []))
print(all(True for x in []))
print(all(False for x in []))
