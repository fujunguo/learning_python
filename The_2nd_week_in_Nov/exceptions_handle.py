try:
    text = input('Enter something -->')
except EOFError:
    print('Why did you do an E0F on me?')
except KeyboardInterrupt:
    print('You cancelled the operation')
else:
    print('You entered {}'.format(text))
