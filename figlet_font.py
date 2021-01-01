import pyfiglet

Name = input('enter your name: ')

print(''''select which font you want: 
1.cursive
2.3-d
3.standard''')

font = input('')
if font == 'cursive':
	result = pyfiglet.figlet_format(Name, font='cursive')
	print(result)
elif font == '3-d':
	result = pyfiglet.figlet_format(Name, font='3-d')
	print(result)
else:
	result = pyfiglet.figlet_format(Name, font='standard')
	print(result)