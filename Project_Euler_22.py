from sys import argv

script, from_file = argv

alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27}

data = open(from_file, 'r').read()

split_data = data.split()
sorted_data = split_data.sort()
print(sorted_data)
