def minimum_required_boats(population, boat_limit_weight):
    population.sort()
    left = 0 
    right = len(population) - 1
    boats = 0
    while left <= right:
        if population[left] + population[right] <= boat_limit_weight:
            left += 1
        right -= 1
        boats += 1
    return boats
print(minimum_required_boats([100, 200, 150, 80, 90], 200))

