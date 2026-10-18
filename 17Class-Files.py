file = open("order.txt", "w") # this will create the file
try:
    file.write("Hi Siddiq") # To write something in the file
finally:
    file.close()

# another simplest way

with open("secondFile.txt", "w") as secondFile:
    secondFile.write("HI Aisha Siddiqha")