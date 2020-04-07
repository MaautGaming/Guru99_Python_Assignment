'''   
        Guru99 live python projects
        Data Analysis Application
'''
'''
    Part 3:  Plot the emissions data from a user-selected country. You should use Python plotting library matplotlib for drawing the plots. 
'''
#Dict to store data from file
Emission = {}

# Reading files and getting data in dict
with open ("Emissions.csv","r") as f:
    file = f.read()
    for row in file.split('\n'):
       Emission.update({str(row.split(',')[0]):[float(i) for i in row.split(',')[1:]]})

#Getting the value from user and verifying
country = input("Enter the country name to visualize its stats")
country = country.title().strip()

#Loop till country name is valid
while(country not in list(Emission.keys())):
    print("Sorry! Information about desired Country is not available....\nTry again...")
    country = input("Enter the country name to visualize its stats")

#Setting X-axis value to country's stats
x = Emission[list(Emission.keys())[0]]
#Setting Y-axis value to Years
y = Emission[country]

#Importing library and plotting graph
import matplotlib.pyplot as plt
plt.xlabel("Years")
plt.ylabel("Emissions in " + country)
plt.plot(x,y)
plt.show()