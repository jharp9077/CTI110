# This program calculates  different tip percentages based on the input form the user.
# 14 Feb. 2019
# CTI-110 P3HW2 - Meal Tip Tax
# Jordan Harper
#
# Input the total value of the meal
# Do total meal value * 7% then display.
# multiply the tip and tax total by the tip percentage inputed then display
# If not using one of the defined percentages display a error.
# Display the results for the total bill after taxes tip included.


for i in range (0,100):
    def main():
# Get the total value of the meal.

        total_bill = float(input('\n\n\nEnter total bill: $'))

# Determines Tax of the meal
        tax = total_bill * .07

# Totals meal total with the tax
        total_sale = tax + total_bill

# Display the total sale before tax
        print('Total before tax', total_bill)

# Display the total sale with tax
        print('Total after tax',' $',total_sale)

# Shows a comment to the user about tipping well.
        print('Tip your server the following for outstanding service.')

# Gets the tip for  percent of the bill and displays.

        total_tip = int(input('Please tip 15, 18, or 20 Percent %'))

# Decides which equation to use based off user input for percentages.

        if total_tip == 15:
            print('15 percent tip and total sale after tax: $', tax * .15 + total_sale)

        elif total_tip == 18:
            print('18 percent tip and total sale after tax: $', total_bill * .18 + total_sale)

        elif total_tip ==20:
            print('20 percent tip and total sale after tax: $', total_bill * .20 + total_sale)

        else:
            print('Please use a mentioned tip from above')

main()



