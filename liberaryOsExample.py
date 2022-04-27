import os

webpage = input()

if 'https://' in webpage:
    os.system('start ' + webpage)
    print('if')

elif 'www.' in webpage:
    webpage = 'https://' + webpage
    os.system('start ' + webpage)
    print('elif')

else:
    webpage = 'https://www.' + webpage
    os.system('start ' + webpage)
    print('else')