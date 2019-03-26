# This program takes positive integers from the user until a negative integer has been inputed.
# It then totals all positive integers
# 5 March 2019
# CTI-110 P4HW3 - Sum of Numbers
# Jordan Harper
#
# User inputs numbers they like
# Then total all positive integers that had been input.
# Stop calculating the negative integer
# Display the result of positive integer



max = 10
total = 0.0
positive_num = 0
def main():
	# Create the for loop to stop if it goes past max
	for counter in range (max):
		
	   
	# This will show positive numbers only and
	# Then total it with all entered positive numbers
		while positive_num > -1: 
			total = total + positive_num
			positive_num = int(input('Enter a positive number: '))
		  
	# Displays total of positive numbers
	print('Total of the positive numbers is:', total)
       
  main()  

       

    
