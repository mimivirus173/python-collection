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
        if 0 <= value <= 6:
            print("-3")

            print("--------------------")
        
        elif 6 < value <= 33:
            print("00")
            
            print("--------------------")

        elif 33 < value <= 39:
            print("02")
            
            print("--------------------")
        
        elif 39 < value <= 55:
            print("4")
            
            print("--------------------")
        
        elif 55 < value <= 75:
            print("7")
            
            print("--------------------")
        
        elif 75 < value <= 92:
            print("10")
            
            print("--------------------")
        
        elif 92 < value <= max:
            print("12")
            
            print("--------------------")
        else:
            print("Invalid result!")

            print("--------------------")