'''   
        Guru99 live python projects
        Data Analysis Application
'''
'''
    Part 5: In today's assignment: 
            1. You will extract data for up to three user-selected countries and
               save it to a new file Emissions_subset.csv. 
            2. The new file should have the exact same format as the source 
               file, i.e. first line of headers and then up to 3 lines for selected countries.  
'''
#Dict to store data from file
Emission = {}

# Reading files and getting data in dict
with open ("Emissions.csv","r") as f:
    file = f.read()
    for row in file.split('\n'):
       Emission.update({str(row.split(',')[0]):[float(i) for i in row.split(',')[1:]]})

while(True):
    countries = input("Enter at most three comma-separated country names for which you want to extract data:\n")
    country = countries.split(',')

    for i in range (len(country)):
        country[i] = country[i].title().strip()

    if len(country) > 3:
        print("Err: At most 3 countries are allowed")
        continue
    
    for x in country: 
        if x not in Emission.keys():
            print(f"ERR: Sorry “{x}” is not a valid country\n")
            continue

    else:
        file = open('Emissions_subset.csv','w')
        file.write(list(Emission.keys())[0] + "," + ",".join(str(i) for i in list(Emission.values())[0]) + "\n")
        for x in country:
            file.write(x + "," + ",".join(str(i) for i in Emission[x]) + "\n")
        file.close()

        print(f"Data successfully extracted for countries " + ", ".join(country) + " saved into file Emissions_subset.csv")
        break