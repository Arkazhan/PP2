import re

# ex1
s = str(input())
p = re.compile('a[b]*') 
m = p.search(s)
print(m)

# ex2
s = str(input())
p = re.compile('ab{3}|ab{2}')
m = p.search(s)
print(m)

# ex3
s = str(input())
p = re.compile('^[a-z]+_[a-z]+$')
m = p.search(s)
print(m)

# ex4
s = str(input())
p = re.compile('[A-Z][a-z]+')
m = p.search(s)
print(m)

# ex5
s = str(input())
p = re.compile('a.*?b$')
m = p.search(s)
print(m)

# ex6
s = str(input())
p = re.sub("[ ,.]", ":", s)
print(p)

# ex7
s = str(input())
words = s.split('_')
camel = words[0] + ''.join(word.capitalize() for word in words[1:])
print(camel)

# ex8
s = str(input())
p = re.findall("[A-Z][^A-Z]*", s)
print(p)

# ex9
s = str(input())
p = re.findall("[A-Z][^A-Z]*", s)
print(*p)

# ex10
s = str(input())
p = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
m = re.sub('([a-z0-9])([A-Z])', r'\1_\2', p).lower()
print(m)