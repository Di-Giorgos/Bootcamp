print()
"""
    *
   ***
  *****
 *******
*********
"""
N = 5 

for i in range(0, N):
	for j in range(0, N-i-1): print(" ", end="")
	for j in range(0, 2*i+1): print("*", end="")	

	print() 
		
	
	
"""
for i in range(N):
	print("  " * (N-i-1), end="")
	print("* " * (2*i+1), end="")
	print()
"""