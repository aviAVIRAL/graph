#  Flood Fill Algorithm


# concpet 

# Example usage
# arr = [
#     [1, 1, 1],
#     [1, 1, 0],
#     [1, 0, 1]
# ]

arr = [ [1, 1, 1], [1, 1, 0], [1, 0, 1] ]

sol = [row for row in arr]  
print(sol)

#                   op 
#  [ [1, 1, 1], 
#    [1, 1, 0], 
#    [1, 0, 1]  ] 


print()
print()

sol = [row[:] for row in arr]  
# sol = [ x[:] for  x in arr]  

print(sol)

#                   op 
#  [ [1, 1, 1], 
#    [1, 1, 0], 
#    [1, 0, 1]  ] 


print()
print()
for x in arr : 
    print(*x)
print()

#                  op 
# 1 1 1
# 1 1 0
# 1 0 1