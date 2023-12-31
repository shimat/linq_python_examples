values = [7, 3, 1, 5, 2, 6, 4]

print(sorted(values))  # [1, 2, 3, 4, 5, 6, 7]
print(sorted(values, reverse=True))  # [7, 6, 5, 4, 3, 2, 1]


names = ["Alice", "Bob", "Caroline"]

print(sorted(names, key=len))  # ['Bob', 'Alice', 'Caroline']
print(sorted(names, key=len, reverse=True))  # ['Caroline', 'Alice', 'Bob']

print(sorted(names, key=lambda s: len(s)))  # ['Bob', 'Alice', 'Caroline']
