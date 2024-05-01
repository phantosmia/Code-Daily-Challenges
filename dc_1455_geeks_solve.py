# Python program for 
# Recursive implementation of 
# Max sum problem in a triangle  

N = 3

  
#  Function for finding maximum sum 

def maxPathSum(tri, i, j, row, col): 

     if(j == col ): 

         return 0

    

     if(i == row-1 ): 

         return tri[i][j]  

    

     return tri[i][j] + max(maxPathSum(tri, i+1, j, row, col), 

                            maxPathSum(tri, i+1, j+1, row, col)) 

  
# Driver program to test above functions 

tri = [  [1, 0, 0],[4, 8, 0],[1, 5, 3] ] 

print(maxPathSum(tri, 0, 0, 3, 3)) 

triangle = [[2, 0, 0, 0], [4, 3, 0, 0], [3, 1, 5, 0], [2, 3, 1, 4]]

print(maxPathSum(triangle, 0, 0, 4, 4))