def todaysTemperature(temperature):
    temperature = input("Today's Temperature: ")

    if temperature < 32:
        print("Freezing")
    elif temperature < 55:
        print("Pleasant")    
    elif temperature < 73:
        print("Getting Warmer")
    elif temperature > 101:
        print("Hot")
    if temperature >= 101:
        print("Very")     
    else:
        print("Please put a valid temperature")   

todaysTemperature(75)     

