<<<<<<< HEAD
colors = {"Baby_Blue": "#89cff0", "Banana_Mania": "#fae7b5", "Black_Coffee": "#3b2f2f", "Bronze": "#cd7f32", "Burlywood4": "#8b7355", "Chamoisee": "#a0785a", "Charcoal": "#36454f", "LimeGreen": "	#32cd32", "Cheese": "#ffbd88", "Mango": "#fdbe02"}

color_name = input("Enter Name: ")

while color_name != "":
    try:
        print(f"{colors[color_name]}")
    except KeyError:
        print("Invalid color")
    color_name = input("Enter Name: ")
=======
colors = {"Baby Blue": "#89cff0", "Banana Mania": "#fae7b5", "Black Coffee": "#3b2f2f", "Bronze": "#cd7f32",
          "Burlywood4": "#8b7355", "Chamoisee": "#a0785a", "Charcoal": "#36454f", "LimeGreen": "	#32cd32",
          "Cheese": "#ffbd88", "Mango": "#fdbe02"}

color_name = input("Enter a colour name: ")

while color_name != "":
    try:
        print(f"This code for \"{color_name}\" is {colors[color_name]}")
    except KeyError:
        print("Invalid color")
    color_name = input("Enter a colour name: ")
>>>>>>> origin/master
