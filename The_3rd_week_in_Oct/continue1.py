while True:
    s=input('Enter something:')
    if s=='quit':
        break
    if len(s)<3:
        print('Too small')
        continue
    else:
        print('Input is of sufficient length')
