# Collect the registration information
participantName = input('Enter your name: ')
participantType = input('Enter your type of participant (s = student, e = employee or g = guests):')
registrationDay = int(input('Enter your registration day from 1 through 7: '))
workshopSelection = input('Attend the optional workshop, (Y for yes or N for no) : ')
eveningSession = input('Attend the evening session (Y for yes or N for no) : ')

# Determine the base registration fee
if participantType == 's':
    baseRegistrationFee = 45.00
elif participantType == 'e':
    baseRegistrationFee = 70.00
else:
    baseRegistrationFee = 95.00

# Determine the Early - Registration Discount
if participantType == 's' and (registrationDay == 1 or registrationDay == 2):
    discount = baseRegistrationFee * .20
elif participantType == 'e' and (registrationDay == 1 or registrationDay == 2 or registrationDay == 3):
    discount = baseRegistrationFee * .10
else:
    discount = 0

if workshopSelection == 'Y':
    workshopFee =  30.00
else:
    workshopFee = 0.00

#determine the evening parking fee
if eveningSession == 'Y' and workshopSelection == 'Y' and (participantType == 's' or participantType == 'e'):
    parkingFee = 0
elif eveningSession == 'Y':
    parkingFee = 12.00
else:
    parkingFee = 0

#Calculate Final registration Cost
finalRegistrationCost = baseRegistrationFee - discount + workshopFee + parkingFee

#Determine the registration category
if finalRegistrationCost <= 60.00:
    finalRegistrationCategory = 'Budget Registration'
elif  60.00 < finalRegistrationCost <= 100.00:
    finalRegistrationCategory = 'Standard Registration'
else:
    finalRegistrationCategory = 'Premium Registration'

#display the registration information
print('Participant Name:  ', participantName)
print('Participant Type: ', participantType)
print('Base Registration Fee:$', baseRegistrationFee)
print('Early-registration Discount:$',format(discount,'.2f'))
print('Workshop Fee:$', format(workshopFee,'.2f'))
print('Evening Parking Fee:$ ', format(parkingFee,'.2f'))
print('Final Registration Cost:$ ', format(finalRegistrationCost,'.2f'))
print('Final Registration Category: ', finalRegistrationCategory)
