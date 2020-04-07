'''   
        Guru99 live python projects
        Data Analysis Application
'''
'''
    Part 2: It's time to start the data analysis. The simple assignment today is to 
                1. Take input from the user 
                2. Calculate worldwide statistics (min, max, average) for a user-entered year 
'''
"""
Variable to work on entire program
Dict to store data from file
"""
Emission = {}
#To store index of desired year to find relevant information 
index=0
#To finf average, minimum and maximum
min_value, max_value, sum_all, country_count= 100.0, -1.0, 0.0, -1
#to store country names
min_country,max_country = "",""




# Reading files and getting data in dict
with open ("Emissions.csv","r") as f:
    file = f.read()
    for row in file.split('\n'):
       Emission.update({str(row.split(',')[0]):[float(i) for i in row.split(',')[1:]]})


# Taking desired year from user
year = input("Enter the year to find statistics(1997 to 2010)")
while(not year.isdigit() or int(year) > 2010 or int(year)<1997):
    print("Sorry! Information about desired Year is not available....\nTry again...")
    year = input("Enter the year to find statistics(1997 to 2010)")


#Getting the statistics about the year
#First getting the index of the year
for x in Emission['CO2 per capita']:
    if x == year:
        index = Emission['CO2 per capita'].index(x)
        
# Getting minimum, maximum and average
for x,y in Emission.items():
    if country_count != -1 :
            if min_value > y[index]:
                min_value = y[index]
                min_country = x
            if max_value < y[index]:
                max_value = y[index]
                max_country = x
            sum_all+=y[index]
    country_count+=1
avg = sum_all/country_count

#Declaring result
print ("Stats about the "+year+" :")
print ("Country with minimum CO2 Emission :" + min_country)
print ("Country with maximum CO2 Emission :" + max_country)
print ("Average CO2 Emission :" + str(avg))
