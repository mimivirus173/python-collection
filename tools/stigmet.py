# Brúkar stigmetið hjá alisfrøði

while True:
    # Kannar um eitt tal var skrivað
    try:
        max = int(input("Maks stig: "))
        stig = int(input("Tíni stig: "))
    except ValueError:
        print("Ógildað tal!")
        print("--------------------")
    else:
        # Býtir tíni stig við max. stig
        value = float(stig / max) * 100

        # Roknar karakter
        if 0 <= value <= 6:
            print("")
            print("-3")

            print("--------------------")
        
        elif 6 < value <= 33:
            print("")
            print("00")
            
            print("--------------------")

        elif 33 < value <= 39:
            print("")
            print("02")
            
            print("--------------------")
        
        elif 39 < value <= 55:
            print("")
            print("4")
            
            print("--------------------")
        
        elif 55 < value <= 75:
            print("")
            print("7")
            
            print("--------------------")
        
        elif 75 < value <= 92:
            print("")
            print("10")
            
            print("--------------------")
        
        elif 92 < value <= 100:
            print("")
            print("12")
            
            print("--------------------")
        else:
            print("")
            print("Ógildað svar!")

            print("--------------------")