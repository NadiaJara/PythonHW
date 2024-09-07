def voter():
    age = input("Age: ")
    eighteen = 18

    if age == eighteen:
        print("I am a Voter")
    elif age > eighteen:
        print("I am not a Voter")
    elif age < eighteen:
        print("I am a Voter from age 18")
    else:
        print("Please add a valid age")        

voter()       