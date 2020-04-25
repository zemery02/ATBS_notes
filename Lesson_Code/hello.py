# This program says hello and asks for my name

print('Hello World!')

print('What is your name?') #ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

print('What is your age?') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

if myAge == '15':
    print('You\'re going to be driving in no time!')
elif myAge == '17':
    print('You\'re going to be legal next year!')
elif myAge == '20':
    print('You can drink next year! Bottoms up!')
else:
    print('Time sure does fly doesn\'t it?')
