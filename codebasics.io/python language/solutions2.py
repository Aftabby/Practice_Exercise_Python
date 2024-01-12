# The exercises are from the codebasics io
        # Problem Source: https://github.com/codebasics/py/tree/master/Basics/Exercise

# 13 read write files
# 13.1
word_stats = dict()
print(word_stats)

with open("E:\\Programming\\Practice_Exercise_Python\\codebasics.io\\python language\\poem.txt") as poem:
    for verse in poem:
        words = verse.split(" ")
        for word in words:
            if word in word_stats:
                word_stats[word] += 1
            else:
                word_stats[word] = 1
        
    word_stats_values = list(word_stats.values())
    max_word_count = max(word_stats_values)

    print("This/these are the max repeated words:")
    for key, value in word_stats.items():
            if value == max_word_count:
                 print(f"'{key}' was found for {value} times.")
                
    


# 13.2

with open("E:\\Programming\\Practice_Exercise_Python\\codebasics.io\\python language\\stocks.csv") as file, open("E:\\Programming\\Practice_Exercise_Python\\codebasics.io\\python language\\output.csv", "w") as out:
    out.write("Company Name, PE Ratio, PB Ratio\n")
    next(file)  #IMPORTANT : This will skip the first line of stocks.csv, which is a header

    for line in file:
        words = line.split(",")
        stock = words[0]
        price = float(words[1])
        eps = float(words[2])
        book_value = float(words[3])
        pe_ratio = round(price/eps, 2)
        p2b_ratio = round(price/book_value, 2)

        out.write(f"{stock}, {pe_ratio}, {p2b_ratio}\n")



class Employee:
     def __init__(self, id, name):
        self.id = id
        self.name = name


emp1 = Employee(1, "coder")

print(emp1.name, emp1.id)
del emp1.id
#print(emp1.id) #Does not exist so it will show an error
del emp1
#print(emp1.name)    #does not exist, so it will show an error
