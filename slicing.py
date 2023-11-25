planet1 = 'Closest of sun'
print(planet1)
print(planet1[0])
print(planet1[1])
print(planet1[2])
print()
print(planet1[-1])
print(planet1[-2])
print(planet1[-3])
print()

# Slicing a string
print(planet1[-1])
print(planet1[1:4])
print(planet1[11:])
print(planet1[-3:])

# Slicing tuple
print('################Slicing tuple##############')
devops = ('Linux', 'Vagrant', 'Bash Scripting', 'AWS', 'Jenkins', 'Python', 'Ansible', 'Docker')
print(devops[0])
print(devops[4])
print(devops[-1])
print(devops[2:5])
print(devops[2:5][0])

print(devops[2:5][0][0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])

# Dictionary example

Skills = {'Devops': ('AWS', 'Docker', 'Python', 'Jenkins'), 'Development': ['Java', 'NodeJS', '.net']}
print(Skills)
print(Skills['Devops'])
print(Skills['Development'])
print(Skills['Devops'][-1])
print(Skills['Devops'][-1][:3])