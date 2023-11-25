# For loops

PLANET = "Earth"
for i in PLANET:
    print(i)

print('Rest of the code!')

VACCINES = ('Moderna', 'Pfizer', 'Sputnik v', 'Covaxin', 'AstraZeneca')

for vac in VACCINES:
    print(f'{vac} vaccine provides immunization against covid19.')

# While loop
x = 0
while x <= 10:
    print("Value of x is: ", x)
    print('Looping')
    x += 1
print("Rest of the code!")