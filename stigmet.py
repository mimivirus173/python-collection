while True:
    # Check if input is an integer
    try:
        max = int(input("Max stig: "))
        stig = int(input("Tíni stig: "))
    except ValueError:
        print("Invalid input!")
        print("--------------------")
    else:
        # Divide your points with the max
        value = float(stig / max) * 100

        # Calculate grades
        if value <= 6:
            print("-3")

            print("--------------------")
        
        elif 6 < value <= 34:
            print("00")
            
            print("--------------------")
        
        elif 34 < value <= 40:
            print("4")
            
            print("--------------------")
        
        elif 40 < value <= 56:
            print("7")
            
            print("--------------------")
        
        elif 56 < value <= 76:
            print("10")
            
            print("--------------------")
        
        elif 76 < value:
            print("12")
            
            print("--------------------")