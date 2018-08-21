def move(n,X,Y,Z):
	if n==1:
		print(X,'->',Z)
	else:
		move(n-1,X,Z,Y)
		move(1,X,Y,Z)
		move(n-1,Y,X,Z)
move(5,"A","B","C")
