IP = str(input("Enter an IP Address")).split(".")
while len(IP) < 4 or len(IP) > 4:
    print("Enter a valid IP Address")
    IP = str(input("Enter an IP Address")).split(".")

first_octate = int(IP[0])
if first_octate < 0:
    print("Invalid IP")
elif first_octate >= 1 and first_octate <= 126:
    print("It's a class A IP Address")
elif first_octate == 127:
    print("It's a loopback address and belongs to Class A")
elif first_octate >= 128 and first_octate <= 191:
    print("It's a class B IP Address")
elif first_octate >= 192 and first_octate <= 223:
    print("It's a class C IP Address")
elif first_octate >= 224 and first_octate <= 239:
    print("It's a class D IP Address")
elif first_octate >= 240 and first_octate <= 254:
    print("It's a class E IP Address")
elif first_octate == 255:
    print("It's a broadcast address")
else:
    print("Invalid IP Address")
