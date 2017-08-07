px = 2
py = 1
while True:
    for y in range(4):
        for x in range(4):
            if x == px and y == py:
                print("P", end=" ")
            else:
                print("-", end= " ")
                
        print() 
    command = input("Your move? ")
    if command.upper() == "D":
        px += 1
        
