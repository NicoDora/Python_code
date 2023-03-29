# Using Ohm's law to calculate voltage, current, and resistance

try:
    choice = int(input("What value would you like to calculate? (1: Voltage(V), 2: Current(I), 3: Resistance(R): "))


    if choice == 1: # Calculate voltage
        current = float(input("Enter the current (I) in [mA]: "))
        resistance = float(input("Enter the resistance (R) in [Ω]: "))
        voltage = current * resistance
        print(f"The voltage (V) is {round(voltage/1000000000, 2)}[MV], {round(voltage/1000000, 2)}[kV], {round(voltage/1000, 2)}[V], {round(voltage, 2)}[mV], {round(voltage*1000, 2)}[µV].")

    elif choice == 2: # Calculate current
        voltage = float(input("Enter the voltage (V) in [V]: "))
        resistance = float(input("Enter the resistance (R) in [Ω]: "))
        current = voltage / resistance
        print(f"The current (I) is {round(current/1000000, 2)}[MA], {round(current/1000, 2)}[kA], {round(current, 2)}[A], {round(current*1000, 2)}[mA], {round(current*1000000, 2)}[µA].")

    elif choice == 3: # Calculate resistance
        voltage = float(input("Enter the voltage (V) in [V]: "))
        current = float(input("Enter the current (I) in [mA]: "))
        resistance = voltage / current
        print(f"The resistance (R) is {round(resistance/1000, 2)}[MΩ], {round(resistance, 2)}[kΩ], {round(resistance*1000, 2)}[Ω], {round(resistance*1000000, 2)}[mΩ], {round(resistance*1000000000, 2)}[µΩ].")

except ValueError: # Handle non-numeric inputs
    print("ValueError: Please enter a valid number.")
