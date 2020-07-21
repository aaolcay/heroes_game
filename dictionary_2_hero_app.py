#           War of Heroes
################ HERO 1 ########################
name = input("Hey, player 1 enter the name of your hero:\n")
weapon =input("Enter the your hero's weapon:\n")
p = float(input("Enter the your hero's power:\n"))
h = float(input("Enter the your hero's health:\n"))
################ HERO 2 ########################
name_2 = input("Hey, player 2 enter the name of your hero:\n")
weapon_2 =input("Enter the your hero's weapon:\n")
p_2 = float(input("Enter the your hero's power:\n"))
h_2 = float(input("Enter the your hero's health:\n"))
################################################
Hero_1 = {"name":"{:s}".format(str(name)),
          "power":float(p),
          "health":float(h),
          "weapon":"{:s}".format(str(weapon))}

Hero_2  = {"name":"{:s}".format(str(name_2)),
          "power":float(p_2),
          "health":float(h_2),
          "weapon":"{:s}".format(str(weapon_2))}
#################################################
def shoot(Hero_1,Hero_2):
    Hero_2["health"] = Hero_2["health"] - Hero_1["power"]
    Hero_1["health"] = Hero_1["health"] - Hero_2["power"]
    print("{} and {} are matched and ---->\n".format(Hero_2["name"],Hero_1["name"]))
    if Hero_1["health"] < Hero_2["health"]:
        print("The winner is : {}".format(Hero_2["name"]))
    elif Hero_1["health"] == Hero_2["health"]:
        print("End in a draw")
    else:
        print("The winner is : {}".format(Hero_1["name"]))
shoot(Hero_1,Hero_2)