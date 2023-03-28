# 옴의 법칙 이용해서 전압, 전류, 저항 구하기
try:
    choice = int(input("어떤 값을 구하려고 하나요? (1: 전압(V), 2: 전류(I), 3: 저항(R): "))


    if choice == 1: # 전압 구하기
        current = float(input("전류(I)를 [mA]단위로 입력하세요: "))
        resistance = float(input("저항(R)을 [Ω]단위로 입력하세요: "))
        voltage = current * resistance
        print(f"전압(V)은 {round(voltage/1000, 2)}[V], {round(voltage, 2)}[mV] 입니다.")

    elif choice == 2: # 전류 구하기
        voltage = float(input("전압(V)을 [V]단위로 입력하세요: "))
        resistance = float(input("저항(R)을 [Ω]단위로 입력하세요: "))
        current = voltage / resistance
        print(f"전류(I)는 {round(current, 2)}[A], {round(current*1000, 2)}[mA] 입니다.")

    elif choice == 3: # 저항 구하기
        voltage = float(input("전압(V)을 [V]단위로 입력하세요: "))
        current = float(input("전류(I)를 [mA]단위로 입력하세요: "))
        resistance = voltage / current
        print(f"저항(R)은 {round(resistance, 2)}[kΩ], {round(resistance*1000, 2)}[Ω] 입니다.")
    
except ValueError: # 숫자가 아닌 다른 값이 입력되었을 때
    print("ValueError: 올바른 숫자를 입력해주세요.")