# House project

def getHousePrice():
	price = int(input("Price of the house: "))
	return price

def downPaymentChoice():
	dp = input("Do you need Down Payment? [yes/no]").upper()
	result = False

	if dp == "YES":
		result = True

	return result

def getDownPayment():
	dp = int(input("Get Down Payment: "))
	return dp


def getCreditScore():
	creditScore = int(input("What is your credit score? "))
	return creditScore

def getInterestRate(creditScore):
	interestRate = 0.0

	if creditScore < 501:
		interestRate = 0.05
	elif creditScore > 501 and creditScore < 701:
		interestRate = 0.02
	else:
		interestRate = 0.01

	return interestRate


def calculateMonthlyPayment(housePrice, downPayment, interestRate, years):
	monthlyPayment = ((housePrice - downPayment) * ((1 + interestRate) ** years)) / (12 * years)
	return monthlyPayment



def calculateTotalInterest(monthlyPayment, years, housePrice, downPayment):
	totalInterest = (monthlyPayment * years * 12) - (housePrice - downPayment)
	return totalInterest


print("## HOUSE PRICE EXERCICE")
housePrice = getHousePrice()

if downPaymentChoice() == False:
	# Work on this later
	print("Not yet implemented.")
	exit(1)

# Downpayment needed
downPayment = getDownPayment()
creditScore = getCreditScore()
interestRate = getInterestRate(creditScore)

print("The interest rate is: ", interestRate)

# Calculate for 10 to 25 years
for years in range(10, 26):
	monthlyPayment = calculateMonthlyPayment(housePrice, downPayment, interestRate, years)
	totalInterest = calculateTotalInterest(monthlyPayment, years, housePrice, downPayment)

	print("Pay in ", years, " with monthly payment of ", monthlyPayment, " and total interest is ", totalInterest)





