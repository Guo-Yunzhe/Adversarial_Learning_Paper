f = open('README.md')
count = 0
txt = f.readlines()
f.close

for i in txt:
    if i[0] == '*':
        count += 1
        pass
    pass
pass

print(count)