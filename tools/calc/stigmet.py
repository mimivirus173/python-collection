def alf_stigmet(max, stig):
    # Brúkar stigmetið hjá alisfrøði

    value = float(stig / max) * 100

    # Roknar karakter
    if 0 <= value <= 6:
        print("")
        print("-3")  
    elif 6 < value <= 33:
        print("")
        print("00")
    elif 33 < value <= 39:
        print("")
        print("02")    
    elif 39 < value <= 55:
        print("")
        print("4")
    elif 55 < value <= 75:
        print("")
        print("7")
    elif 75 < value <= 92:
        print("")
        print("10")
    elif 92 < value <= 100:
        print("")
        print("12")
    else:
        print("")
        print("Ógildað svar!")

def evf_stigmet(max, stig):
    # Brúkar stigmetið hjá evnafrøði

    value = float(stig / max) * 100

    # Roknar karakter
    if 0 <= value <= 9:
        print("")
        print("-3")
    elif 9 < value <= 44:
        print("")
        print("00")
    elif 44 < value <= 57:
        print("")
        print("02")
    elif 57 < value <= 67:
        print("")
        print("4")
    elif 67 < value <= 79:
        print("")
        print("7")
    elif 79 < value <= 95:
        print("")
        print("10")
    elif 95 < value <= 100:
        print("")
        print("12")
    else:
        print("")
        print("Ógildað svar!")     

def stø_stigmet(max, stig):
    # Brúkar stigmetið hjá støddfrøði

    value = float(stig / max) * 100

    # Roknar karakter
    if 0 <= value <= 8:
        print("")
        print("-3")
    elif 8 < value <= 33:
        print("")
        print("00")
    elif 33 < value <= 40:
        print("")
        print("02")
    elif 40 < value <= 56:
        print("")
        print("4")
    elif 56 < value <= 77:
        print("")
        print("7")
    elif 77 < value <= 91:
        print("")
        print("10")
    elif 91 < value <= 100:
        print("")
        print("12")
    else:
        print("")
        print("Ógildað svar!")     

def main():
    fak_val = input("alf, evf ella stø?: ").strip().lower()
    if fak_val == "alf":
        try:
            max = int(input("Maks stig: "))
            stig = int(input("Tíni stig: "))
        except ValueError:
            print("Ógildað tal!")
             
        else:
            alf_stigmet(max, stig)
    elif fak_val == "evf":
        try:
            max = int(input("Maks stig: "))
            stig = int(input("Tíni stig: "))
        except ValueError:
            print("Ógildað tal!")
             
        else:
            evf_stigmet(max, stig)
    elif fak_val == "stø":
        try:
            max = int(input("Maks stig: "))
            stig = int(input("Tíni stig: "))
        except ValueError:
            print("Ógildað tal!")
             
        else:
            stø_stigmet(max, stig)
    else:
        print("Ógildað val!")
        exit(0)

if __name__ == '__main__':
    main()