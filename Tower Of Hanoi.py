# Code by - Rajesh Kumar
def TowerOfHanoi(n, A, B, C):
	if n == 0:
		return
	TowerOfHanoi(n-1, A, C, B)
	print("Move disk", n, "from rod", A,"to rod", B)
	TowerOfHanoi(n-1, C, B, A)

N = int(input("Enter number of plate : "))
# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')
