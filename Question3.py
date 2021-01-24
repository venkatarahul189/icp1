a = input('enter string');
result = ''
for i in a:
    if i == 'n':
        i = 'ns'
    result += i
print(result)