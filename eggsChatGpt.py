def check_egg(floor, floors):
    # A function that simulates breaking the egg and returns True if it breaks, False otherwise
    if floor >= floors:
        return True
    return False

egg1_floor = 14
egg2_floor = 27
egg3_floor = 39
egg4_floor = 50
egg5_floor = 60
egg6_floor = 69
egg7_floor = 76
egg_floors = [egg1_floor, egg2_floor, egg3_floor, egg4_floor, egg5_floor, egg6_floor, egg7_floor]

floors = 102 # number of floors in the building

for i in range(7):
    if egg_floors[i] >= floors:
        low = egg_floors[i-1]
        high = egg_floors[i]
        eggs = i
        break
else:
    low = egg_floors[6]
    high = floors
    eggs = 7

while low + 1 < high:
    mid = (low + high) // 2
    if mid >= floors or check_egg(mid, floors):
        high = mid
    else:
        low = mid

print(f"The highest floor the egg can be dropped from without breaking is: {low}")

