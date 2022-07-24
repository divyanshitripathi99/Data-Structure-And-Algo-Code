def towerofhanoi(n , A ,B ,C):
	if (n ==1 ):
		print("Move disk 1 from rod ", A ,"to rod",B)
		return
	
	towerofhanoi(n-1 , A ,C ,B)
	print("Move disk", n ,"from rod ", A ,"to rod",B )
	towerofhanoi(n-1 , C,B ,A)
n= 4
towerofhanoi(n , 'A' ,'C' ,'B')
		
	
