cube_list = [
    [2 , 3 , 3] ,
    [4 , 8 , 2] , 
    [3 , 5 , 4]
]

cube_number = 1

for i in cube_list:
    result = 1
    for j in i:
        result = result * j
    print(f"volume of cube number{cube_number} = {result}")
