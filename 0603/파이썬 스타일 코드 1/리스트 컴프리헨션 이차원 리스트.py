words = "The quick brown fox jumps over the lazy dog".split()
print(words)
print(type(words))
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)
print(type(stuff))