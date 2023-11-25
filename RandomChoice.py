import random

VACCINES = ['Moderna', 'Pfizer', 'Sputnik v', 'Covaxin', 'AstraZeneca']
random.shuffle(VACCINES)
print(VACCINES)
print('############################################################')
LUCKY = random.choice(VACCINES)
print(LUCKY)
print('############################################################')
for vac in VACCINES:
    print(f'*********TESTING VACCINE {vac}')
    if vac == LUCKY:
        print('##################################')
        print(f'{LUCKY} vaccine, test SUCCESSFUL')
        print('##################################')
        break
