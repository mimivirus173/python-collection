def main():
    # Explanatory text
    print("This program can convert temperatures between degrees Celsius (°C), Kelvin (K), and degrees Amun (°A).")
    print("")
    print("When choosing mode, enter '1' to convert from Celsius to Amun, '2' to convert from Amun to Celsius, '3' to convert from Kelvin to Amun, or '4' to convert from Amun to Kelvin: ")
    print("(TLDR: 1 = C -> A | 2 = A -> C | 3 = K -> A | 4 = A -> K)")
    print("Choose mode 0 for info on the program.")
    print("")

    # The program
    while True:
        # Check for valid input
        try:
            choice = input("Mode: ")
            choice = int(choice)
        except ValueError:
            print("Invalid input!")
            print("--------------------")
        else:
            if choice == 0:
                print("")

                print("Amun is a scale based on the freezing and boiling temperature of ammonia (-77.73 °C and -33.34 °C respectively).")
                print("The scale between 0 °A and 1 °A is equal to 0.44 °C.")
                print("The scale between 0 °C and 1 °C is equal to 2.27 °A.")

                print("--------------------")
            elif choice == 1:
                # Celsius to Amun conversion
                print("")
                try:
                    celsius = float(input("Input a temperature in °C: "))
                except ValueError:
                    print("Invalid input!")
                    print("--------------------")
                else:
                    if celsius >= -273.15:
                        print("Converting...")
                        print("")

                        amun = "%.2f" % float((celsius + 77.73) * (100 / (-33.34 + 77.33)))
                        # "%.2f" makes it so that every decimal after the 2nd one is ignored

                        print("Result: " + str(amun) + " °A")
                        print("--------------------")
                    else:
                        print("Cannot have temperatures below absolute zero!")
                        print("--------------------")
            elif choice == 2:
                # Amun to Celsius conversion
                print("")
                try:
                    amun = float(input("Input a temperature in °A: "))
                except ValueError:
                    print("Invalid input!")
                    print("--------------------")
                else:
                    if amun >= -444.24:
                        print("Converting...")
                        print("")

                        celsius = "%.2f" % float((amun * (-33.34 + 77.33) / 100) - 77.73)

                        print("Result: " + str(celsius) + " °C")
                        print("--------------------")
                    else:
                        print("Cannot have temperatures below absolute zero!")
                        print("--------------------")
            elif choice == 3:
                # Kelvin to Amun conversion
                print("")
                try:
                    kelvin = float(input("Input a temperature in K: "))
                except ValueError:
                    print("Invalid input!")
                    print("--------------------")
                else:
                    if kelvin >= 0:
                        print("Converting...")
                        print("")

                        amun = "%.2f" % float(((kelvin - 273.15) + 77.73) * (100 / (-33.34 + 77.33)))

                        print("Result: " + str(amun) + " °A")
                        print("--------------------")
                    else:
                        print("Cannot have temperatures below absolute zero!")
                        print("--------------------")
            elif choice == 4:
                # Amun to Kelvin conversion
                print("")
                try:
                    amun = float(input("Input a temperature in °A: "))
                except ValueError:
                    print("Invalid input!")
                    print("--------------------")
                else:
                    if amun >= -444.24:
                        print("Converting...")
                        print("")

                        kelvin = "%.2f" % float(((amun * (-33.34 + 77.73) / 100)) + 273.15 - 77.73)

                        print("Result: " + str(kelvin) + " K")
                        print("--------------------")
                    else:
                        print("Cannot have temperatures below absolute zero!")
                        print("--------------------")
            else:
                print("Invalid choice!")
                print("--------------------")

if __name__ == '__main__':
    main()