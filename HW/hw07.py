def diabeticCondition(hbA1c):
    if hbA1c > 6.4:
        print("I am a diabetic patient.")
    if hbA1c >= 5.7:
        print("I am a pre-diabetic patient.")
    elif hbA1c < 5.7:
        print("I am a healthy person.")  
    else:
        print("Please add a valid hbA1c value.") 

diabeticCondition(2.6)                 