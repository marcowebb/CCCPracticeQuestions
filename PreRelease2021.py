from datetime import date,timedelta

# Task 1
today = date.today()
latest = today + timedelta(days=7)
latestDate = latest.strftime("%d-%m-%Y")
today = today.strftime("%d-%m-%Y")

constOneDayCost = [20.00, 12.00, 16.00, 60.00, 15.00]
constTwoDayCost = [30.00, 18.00, 24.00, 90.00, 22.50]
constExtraAttractions = [2.50, 2.00, 5.00]

print("You make book any day from", today, "until", latestDate)

print("Prices all in $")
print("1 Day Prices:")
print("1 Adult:", constOneDayCost[0])
print("1 Child (an adult may bring up to 2 children):", constOneDayCost[1])
print("1 Senior:", constOneDayCost[2])
print("Family Ticket (up to 2 adults / seniors, and 3 children):", constOneDayCost[3])
print("Groups of 6 or more, price per person:", constOneDayCost[4])

print("2 Day Prices:")
print("1 Adult:", constTwoDayCost[0])
print("1 Child (an adult may bring up to 2 children):", constTwoDayCost[1])
print("1 Senior:", constTwoDayCost[2])
print("Family Ticket (up to 2 adults / seniors, and 3 children):", constTwoDayCost[3])
print("Groups of 6 or more, price per person:", constTwoDayCost[4])

print("Extra Attractions (price per person)")
print("Lion Feeding:", constExtraAttractions[0])
print("Penguin Feeding:", constExtraAttractions[1])
print("Evening Barbecue (2-day tickets only):", constExtraAttractions[2])

# Task 2
bookingNum = 0
twoDay = False
adultNum = 0
childNum = 0
seniorNum = 0
ticketUseDate = ""
lionFeed = False
penguinFeed = False
eveningBBQ = False
totalCost = 0.0

today = date.today()
check = False
while check != True:
	print("You may book on:")
	print("1:",today.strftime("%d-%m-%Y"))
	print("2:",(today + timedelta(days=1)).strftime("%d-%m-%Y"))
	print("3:",(today + timedelta(days=2)).strftime("%d-%m-%Y"))
	print("4:",(today + timedelta(days=3)).strftime("%d-%m-%Y"))
	print("5:",(today + timedelta(days=4)).strftime("%d-%m-%Y"))
	print("6:",(today + timedelta(days=5)).strftime("%d-%m-%Y"))
	print("7:",(today + timedelta(days=6)).strftime("%d-%m-%Y"))
	print("8:",(today + timedelta(days=7)).strftime("%d-%m-%Y"))
	ticketDateCheck = input("Which option will you choose for the date of your ticket? : ")
	if ticketDateCheck == "1":
		ticketUseDate = today
		check = True
	elif ticketDateCheck == "2":
		ticketUseDate = today + timedelta(days=1)
		check = True
	elif ticketDateCheck == "3":
		ticketUseDate = today + timedelta(days=2)
		check = True
	elif ticketDateCheck == "4":
		ticketUseDate = today + timedelta(days=3)
		check = True
	elif ticketDateCheck == "5":
		ticketUseDate = today + timedelta(days=4)
		check = True
	elif ticketDateCheck == "6":
		ticketUseDate = today + timedelta(days=5)
		check = True
	elif ticketDateCheck == "7":
		ticketUseDate = today + timedelta(days=6)
		check = True
	elif ticketDateCheck == "8":
		ticketUseDate = today + timedelta(days=7)
		check = True
	else:
		print("Please input a number from 1 to 8.")

check = False
while check != True:
	twoDayConfirm = input("Would you like to book for two days? Y/N: ")
	if twoDayConfirm == "Y":
		twoDay = True
		check = True
	elif twoDayConfirm == "N":
		twoDay = False
		check = True
	else:
		print("Please input either Y/N.")

check = False
while check != True:
	adultNumCheck = int(input("How many adult tickets would you like to book? : "))
	if adultNumCheck < 0:
		print("Please enter number larger than 0")
	else:
		adultNum = adultNumCheck
		check = True
		if twoDay == True:
			totalCost += (adultNum * 30.0)
		else:
			totalCost += (adultNum * 20.0)
	
check = False
while check != True:
	seniorNumCheck = int(input("How many senior tickets would you like to book? : "))
	if seniorNumCheck < 0:
		print("Please enter number larger than 0")
	else:
		seniorNum = seniorNumCheck
		check = True
		if twoDay == True:
			totalCost += (seniorNum * 24.0)
		else:
			totalCost += (seniorNum * 16.0)

check = False
while check != True:
	childNumCheck = int(input("How many child tickets would you like to book? : "))
	if childNumCheck < 0:
		print("Please enter number larger than 0")
	else:
		accompanyMinors = adultNum + seniorNum
		if accompanyMinors / childNumCheck >= 0.5:
			childNum = childNumCheck
			check = True
			if twoDay == True:
				totalCost += (childNum * 18.0)
			else:
				totalCost += (childNum * 12.0)
		else:
			print("A minimum of one adult must accompany every two children")		

print("total cost:", totalCost)
print("number of adults", adultNum)
print("number of seniors", seniorNum)
print("number of children", childNum)
print("to be used on", ticketUseDate.strftime("%d-%m-%Y"))

# Task 3
childNumTemp = childNum

familyTicketCount = 0
groupTicketCount = 0

famTicketGuard = []
for i in range(0, adultNum):
	famTicketGuard.append("a")
for i in range(0, seniorNum):
	famTicketGuard.append("s")

if len(famTicketGuard) == 1:
	print("Family ticket not possible.")
elif len(famTicketGuard) % 2 == 0:
	accompanyMinorsPairs = len(famTicketGuard)
	accompanyMinorsPairs = accompanyMinorsPairs / 2
	while True:
		if childNumTemp >= 3 and accompanyMinors >= 1:
			childNumTemp -= 3
			accompanyMinors -= 1
			familyTicketCount += 1
		else:
			break
	if familyTicketCount >= 1:
		for i in range(0, familyTicketCount):
			famTicketGuard.pop(0)
			famTicketGuard.pop(0)
elif len(famTicketGuard) % 2 != 0:
	famTicketGuardLeftover = famTicketGuard[-1]
	famTicketGuard.pop(-1)

	accompanyMinorsPairs = len(famTicketGuard)
	accompanyMinorsPairs = accompanyMinorsPairs / 2
	while True:
		if childNumTemp >= 3 and accompanyMinors >= 1:
			childNumTemp -= 3
			accompanyMinors -= 1
			familyTicketCount += 1
		else:
			break
	if familyTicketCount >= 1:
		for i in range(0, familyTicketCount):
			famTicketGuard.pop(0)
			famTicketGuard.pop(0)

	famTicketGuard.append(famTicketGuardLeftover)

# FAMILY TICKET CALCULATOR WORKS!
# Now, just calculate possibilities of group tickets
# with the leftover people from this

# famTicketGuard = remaining guardians
# childNumTemp = remaining children
childNum = childNumTemp

