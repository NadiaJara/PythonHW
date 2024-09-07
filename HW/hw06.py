print("Todays Temperature")

def todaysTemperature():
    if todaysTemperature < 32:
        print("Freezing")
    elif todaysTemperature < 55:
        print("Pleasant")    
    elif todaysTemperature < 73:
        print("Getting Warmer")
    elif todaysTemperature > 101:
        print("Very Hot")
    else:
        print("Please put a valid temperature")   
todaysTemperature()     

