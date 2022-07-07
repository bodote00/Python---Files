user_input = input("Please enter points: ").split(";")

points_list = []

for point in user_input:
    x, y = point.split(",") 
    points_list.append({"x": float(x)**2, "y": float(y)**2})

print (points_list)