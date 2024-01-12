# The exercises are from the codebasics io
        # Problem Source: https://github.com/codebasics/py/tree/master/Basics/Exercise



#5 list
heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print("1. The length of the list: ", len(heroes))

heroes.append('black panther')
print("2. Added black panther: ", heroes)

heroes.remove('black panther')
heroes.insert(3, 'black panther')
print("3. Added black panther after hulk: ", heroes)


heroes[1:3] = ["doctor strange"]
print("4. Replaced using one line: ", heroes)

print("Sorted list: ", sorted(heroes))



print("\n\n")


#8 condition

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter a city\n").strip()

if city in india:
    country = "india"
elif city in pakistan:
    country = "pakistan"
elif city in bangladesh:
    country = "bangladesh"
else:
    city = False

if city:
    print("1.i. Your city belongs from", country)
else:
    print("1.i. You are from out of the world.")

#------------------------
city1 = input("Enter a city\n").strip()
city2 = input("Enter another city\n").strip()

if city1 in india and city2 in india:
    print("1.ii. Both belong to the same country")
elif city1 in bangladesh and city2 in bangladesh:
    print("1.ii. Both belong to the same country")
elif city1 in pakistan and city2 in pakistan:
    print("1.ii. Both belong to the same country")
else:
    print("1.ii. They belong in different countries")

#--------------------------




#9 for loop
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

heads = [_ for _ in result if _ == "heads" ]
print("1. The heads was in the result: ", len(heads), "times")


#--

for num in range(1, 11):
    if num % 2 != 0:
        print("2. ", num, "*", num, "=", pow(num, 2))


#--
expense_list = [2340, 2500, 2100, 3100, 2980]
month = ["january", "february", "March", "April", "May"]

expense = int(input("Enter expense:"))

if expense in expense_list:
    print("3. The expense is from ", month[expense_list.index(expense)])
else:
    print("3. The expense in not in the list")


#---
print("5.")
for i in range(1, 6):
    print("*"*i)










    