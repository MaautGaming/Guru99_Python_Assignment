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

#Getting the value from user and verifying
#Loop till country name is valid
countries = input("Enter two comma-separated country names to visualize comparisions:\n")
country_1, country_2 = countries.split(',')[0], countries.split(',')[1]
country_1 = country_1.title().strip()
country_2 = country_2.title().strip()
while(country_1 not in list(Emission.keys()) or  country_2 not in list(Emission.keys())):
    print("Sorry! Information about 1 or more desired Country is not available....\nTry again...")
    countries = input("Enter two comma-separated country names to visualize comparisions:\n")
    country_1, country_2 = countries.split(',')[0], countries.split(',')[1]
    country_1 = country_1.title().strip()
    country_2 = country_2.title().strip()

#Setting X-axis value to countries' stats
x = Emission[list(Emission.keys())[0]]
y1 = Emission[country_1]
#Setting Y-axis value to Years
y2 = Emission[country_2]

#Importing library and plotting graph
import matplotlib.pyplot as plt
plt.xlabel("Years")
plt.ylabel("Emissions in " + country_1)
plt.plot(x,y1, label=country_1)
plt.plot(x,y2, label=country_2)
plt.legend()
plt.show()