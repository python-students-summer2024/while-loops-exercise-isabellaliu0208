def get_starting_number():
    while True:
        num = input("How many bottles of beer on the wall? ")
        if num.isdigit():
            num = int(num)
            if num >= 1:
                return num
            else:
                print("Please enter a number 1 or greater.")
        else:
            print("Please enter a valid integer.")

def sing(starting_bottles):
    bottles = starting_bottles
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles-1} {'bottles' if bottles-1 > 1 else 'bottle'} of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print(f"Take it down, pass it around, no more bottles of beer on the wall!\n")
        bottles -= 1
