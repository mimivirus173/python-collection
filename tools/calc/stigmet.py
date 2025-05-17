# function checks if input is float
def to_float(n):
    try:
        return float(n)
    except ValueError:
        return None

def alf_stigmet(max, stig):
    # Brúkar stigmetið hjá alisfrøði
    if max <= 0 or stig < 0:
        print("\nÓgildað svar!")
        return

    virði = float(stig / max) * 100
    meting = [
        (6, "-3"), (33, "00"), (39, "02"), 
        (55, "4"), (75, "7"), (92, "10"), 
        (100, "12")
    ]
    for mark, karakter in meting:
        if virði <= mark:
            print(f"\n{karakter}")
            return
    print("\nÓgildað svar!")

def evf_stigmet(max, stig):
    # Brúkar stigmetið hjá evnafrøði
    if max <= 0 or stig < 0:
        print("\nÓgildað svar!")
        return

    virði = float(stig / max) * 100
    meting = [
        (9, "-3"), (44, "00"), (57, "02"), 
        (67, "4"), (79, "7"), (95, "10"), 
        (100, "12")
    ]
    for mark, karakter in meting:
        if virði <= mark:
            print(f"\n{karakter}")
            return
    print("\nÓgildað svar!")

def stø_stigmet(max, stig):
    # Brúkar stigmetið hjá støddfrøði
    if max <= 0 or stig < 0:
        print("\nÓgildað svar!")
        return

    virði = float(stig / max) * 100
    meting = [
        (8, "-3"), (33, "00"), (40, "02"), 
        (56, "4"), (77, "7"), (91, "10"), 
        (100, "12")
    ]
    for mark, karakter in meting:
        if virði <= mark:
            print(f"\n{karakter}")
            return
    print("\nÓgildað svar!")

def main():
    fak_val = input("alf, evf ella stø?: ").strip().lower()
    if fak_val == "alf":
        if ((max := to_float(input("Maks stig: "))) is not None and
            (stig := to_float(input("Tíni stig: "))) is not None):
            alf_stigmet(max, stig)
        else:
            print("Invalid input!")
            exit(0)
    elif fak_val == "evf":
        if ((max := to_float(input("Maks stig: "))) is not None and
            (stig := to_float(input("Tíni stig: "))) is not None):
            evf_stigmet(max, stig)
        else:
            print("Invalid input!")
            exit(0)
    elif fak_val == "stø":
        if ((max := to_float(input("Maks stig: "))) is not None and
            (stig := to_float(input("Tíni stig: "))) is not None):
            stø_stigmet(max, stig)
        else:
            print("Invalid input!")
            exit(0)
    else:
        print("Ógildað val!")
        exit(0)

if __name__ == '__main__':
    main()