
# Collects bugs everyday for 7 days. Should display the total number of bugs collected after the 7 days.
# 26 February 2019
# CTI-110 P4T2 - Bug Collector
# Jordan Harper
#
# Set total = 0
# for each of 7 days
# Input bugs collected for a day
# Add bugs collected to total
# Display total



# initialize the accumulator.
total = 0
def main():
	# Get the bugs collected for each day.
	for day in range(1,8):

		# Promt the user.
		print('Enter the bugs collected on day', day)

		# Input the number of bugs.
		bugs = int(input())

		# Add bugs to total.
		total = total + bugs


	# Display the total bugs
	print('You collected a total of', total, 'bugs.')
main()


    
