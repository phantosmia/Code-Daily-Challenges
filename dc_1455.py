def maximum_path_sum(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row+1][col+1])
    return triangle[0][0]
triangle = [[1], [2, 3], [1, 5, 1]]
print(maximum_path_sum(triangle)) 

triangle = [[2], [4, 3], [3, 1, 5], [2, 3, 1, 4]]
print(maximum_path_sum(triangle))

tri = [  [1],[4, 8],[1, 5, 3] ] 
print(maximum_path_sum(tri))

triangle = [[10], [5, 14], [1, 11, 15], [8, 6, 9, 5]]

print(maximum_path_sum(triangle))