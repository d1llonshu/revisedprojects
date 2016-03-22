#I used 1 centimeter = .4 inches to avoid rounding crazy numbers
yourName = input("What is your Name?")

yourHeight = input("What is your height in centimeters?")
yourHeight = int(yourHeight) * 4
yourHeight = yourHeight / 10
inches = yourHeight % 12
yourHeight = yourHeight / 12

feet = yourHeight

print("Nice to meet you {}, you are {} feet {} inches tall.".format(yourName, feet, inches)

