"""
FIRST ASSIGNMENT 

Having aptech as your starting point, you are to direct a user to either of two locations: Abakpa or Emene


get your users name and the place they want to go

if they choose to go with the abakpa location, then direct them on how they can get there from aptech

if they choose to go with the emene location, then direct them on how they can also get there from aptech
"""

# first assignment answer 
name = input("hello what is your name")

#Ask where they ant to go to
destination = input(f"welcome {name}! where would you like to go (Abakpa or Emene)?").lower()

#Direct the user based on their choice
if destination == "abakpa":
  print(f"Alright {name}, here's how you can get to Abakpa from Aptech:")
  print("Take a bus from abakpa juntion towards new heaven.")
  print("from there join a bus going directly to abakpa")
  print("drop at abakpa main junction")

elif destination == "emene":
    print(f"Alright {name}, here's h0w you can get to eemene from aptech.")
    print("from aptech junction take a bus heading towards abakaliki road.")
    print("continue straight until you reach emene junction")
    print("from there you can stop at emene main bustop")
    

else:
    print(f"sorry {name}, that destination is not available. please choose either Abakpa or Emene!")
