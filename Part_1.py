'''   
        Guru99 live python projects
        Data Analysis Application
'''
'''
    Part 1: Read File and store data in file without importing libraries 
'''

#Dict to store data from file
Emission = {}

# Reading files and getting data in dict
with open ("Emissions.csv","r") as f:
    file = f.read()
    for row in file.split('\n'):
       Emission.update({str(row.split(',')[0]):[float(i) for i in row.split(',')[1:]]})

# Showing content of Dict
for x,y in Emission.items():   
    print (x, end=' - ')
    print (y)

print("Congrats! Data extraction successful!!!")