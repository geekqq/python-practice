# Break statement

for i in 'DevOps':
    print(i)
    if i == 'O':
        print('Found my data.')
        break
print('Out of the loop')
print('##########################')
for i in 'DevOps':
    print(i)
    if i == 'O':
        print('Found my data.')
        continue
    print(f'Value of i is {i}')