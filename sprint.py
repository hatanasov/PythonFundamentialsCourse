timeRacing = int(input()) # length of the racing in hours
numParticipant = int(input()) # Number of participant want to run
avgLaps = int(input()) # Average laps per participant
routeLength = int(input()) # length of the route
routeCapacity = int(input()) # Capacity of the route
pay = float(input()) # the amount of money paid per kilometer

limitOfParticipant = routeCapacity * timeRacing
realParticipant = 0

if numParticipant > limitOfParticipant:
    realParticipant = limitOfParticipant
else:
    realParticipant = numParticipant

totalKilometers = (realParticipant * avgLaps * routeLength) / 1000 # in kilometers
totalPay = totalKilometers * pay

print( "Money raised: {0:.2f}".format(totalPay))