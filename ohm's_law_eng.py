# Using Ohm's law to calculate voltage, current, and resistance
try:
    choice = int(input("What value would you like to calculate? (1: Voltage_V, 2: Current_I, 3: Resistance_R): "))


    if choice == 1: # Calculate voltage
        current = float(input("Enter the current (I) in [mA]: "))
        resistance = float(input("Enter the resistance (R) in [Ω]: "))
        voltage = current * resistance
        print(f"The voltage (V) is {round(voltage/1000, 2)}[V], {round(voltage, 2)}[mV].")

    elif choice == 2: # Calculate current
        voltage = float(input("Enter the voltage (V) in [V]: "))
        resistance = float(input("Enter the resistance (R) in [Ω]: "))
        current = voltage / resistance
        print(f"The current (I) is {round(current, 2)}[A], {round(current*1000, 2)}[mA].")

    elif choice == 3: # Calculate resistance
        voltage = float(input("Enter the voltage (V) in [V]: "))
        current = float(input("Enter the current (I) in [mA]: "))
        resistance = voltage / current
        print(f"The resistance (R) is {round(resistance, 2)}[kΩ], {round(resistance*1000, 2)}[Ω].")
        
except ValueError: # Handle non-numeric inputs
    print("ValueError: Please enter a valid number.")
