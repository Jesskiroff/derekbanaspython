#have the user enter his or her investment amount and expected interest 
#each year their investment will increase by their investment + ther investment * interrest rate
# print out the earnings after 10 years 


# #ask 4 money invested + interest rate
# investment_amount = input("What sum are you investing? ")
# interest_rate = input("What is the interest rate you expect to get back on your investment? ")

# #convert value to float 
# investment_amount = float(investment_amount)

# #convert val to float and round the % rate by 2 digits
# #to convert any number to a percentage, just multiply by .01
# interest_rate = float(interest_rate) * .01

# #cycle through 10 yrs using a for loop and range from 0-9
# for i in range(10):
#     investment_amount = investment_amount +(investment_amount * interest_rate)
#     print (investment_amount)
# #Output the results
# print("Investment after 10 yrs is : {:.2f}".format(investment_amount))


#have the user enter his or her investment amount and expected interest 
#each year their investment will increase by their investment + ther investment * interrest rate
# print out the earnings after 10 years 


investment_amount = input("What amount of money are you investing? ")
interest_rate = input("What interest rate are you expecting to get back on your investment? ")

investment_amount = float(investment_amount)
interest_rate = float(interest_rate) * .01

for i in range (10):
    investment_amount = investment_amount + (investment_amount * interest_rate)

print("Your investment will compound to {:.2f}".format(investment_amount))