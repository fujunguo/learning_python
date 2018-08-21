number=23
guess=int(input('Enter an integer:'))

if guess==number:
    #新块在这里开始
    print('Congratulations,you guessed it.')
    print('(but you do not win any prizes!)')
    #新块在这里结束
elif guess<number:
    #另一代码块
    print('No,it is a little higher than that')
    #你可以在此处做任何你希望在该代码块内进行的事情
else:
    print('No,it is a little lower than that')
print('Done')
