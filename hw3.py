a = ("шалаш", "шамаш", "оно", "она", "они")
b = tuple(filter(lambda x: x == x[::-1], a))
print(b)