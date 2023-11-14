"""Practice with dictonaries"""

# Creating a new dictionary

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}


#Adding a key, value pair
ice_cream["mint"] = 3
ice_cream.pop("mint")

#Accessing the values
print(f"There are {ice_cream['chocolate']} orders of chocolate")

# updating a value
ice_cream["vanilla"] = 10
# ice_cream["vanilla"] += 2
# print(ice_cream)
# print(f"there are {len(ice_cream)} key value terms")


# # Checking to see if a pair is in the dict
# print("Chocolate in ice cream?")
# print("chocolate" in ice_cream)
# print("mint in ice cream?")
# print("mint" in ice_cream)

# if "mint" in ice_cream:
#     print(f"there are {ice_cream['mint']} orders of mint")
# else:
#     print("no orders of mint")


for flavor in ice_cream:
    print(f"{flavor} has {ice_cream[flavor]} orders")
