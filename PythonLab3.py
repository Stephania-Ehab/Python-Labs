# Example

import fileoperation as fo

fo.write('example.txt', 'This is a new content.')
fo.append('example.txt', ' This is appended content.')
print(fo.read('example.txt', 'all'))
print(fo.read('example.txt', 5))
print(fo.read('example.txt', 'line'))
print(fo.read('example.txt', 'lines'))
