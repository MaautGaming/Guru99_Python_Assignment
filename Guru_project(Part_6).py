'''   
        Guru99 live python projects
        Data Analysis Application (complete)
'''
try:
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


    # Taking desired year from user
    year = input("Enter the year to find statistics(1997 to 2010)")
    while(not year.isdigit() or int(year) > 2010 or int(year)<1997):
        print("Sorry! Information about desired Year is not available....\nTry again...")
        year = input("Enter the year to find statistics(1997 to 2010)")

    index=0
    #To finf average, minimum and maximum
    min_value, max_value, sum_all, country_count= 100.0, -1.0, 0.0, -1
    #to store country names
    min_country,max_country = "",""
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


except FileNotFoundError:
    print("File not found....")
except IOError:
    print("Output file can’t be saved")