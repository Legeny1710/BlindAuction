from replit import clear

print("Welcome to the blind auction program")
###########################


#list to store users name and bid
Users_bid_list = []

#inputs for name, bid and option to continue or not
name = input("What is your name?: ")
bid = int(input("What is your bid?: "))

More_people = input("Are there any more people who wants to bid? (Type 'yes' or 'no'): ")

#Adding those information on a list in dictionary format
new_user = {}

new_user["name"] = name
new_user["bid"] = bid

Users_bid_list.append(new_user)



#While loop

while More_people == "yes":
  clear()
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: "))
  
  #Adding those information on a list in dictionary format
  new_user = {}
  
  new_user["name"] = name
  new_user["bid"] = bid
  
  Users_bid_list.append(new_user)

  More_people = input("Are there any more people who wants to bid? (Type 'yes' or 'no'): ")





#Finding which user has the highest bid
maxName = ""
max = Users_bid_list[0]["bid"]
for i in Users_bid_list:
  if i["bid"] > max:
    max = i["bid"]
    maxName = str(i["name"])



#Printing who got the highest bid
clear()
print(f"The winner of this auction is {maxName}")
