print('Enter input file number (e.g. for "10.in" enter: 10):')
fileNum = str(input())

# Read from .in file if exists
try:
    inputFileName = './InputFiles/' + fileNum + '.in'
    inputFile = open(inputFileName, "r")
    print("Thanks, working...")
except FileNotFoundError:
    print("This file does not exist: make sure the correct file number was provided.")
    exit()

# Parse first line for N number of shifts
N = int(inputFile.readline())

# Parse for rows
rows = inputFile.readlines()
print("Parsing completed...")

# Parse rows for shifts
shifts = {}
personCtr = 1

for r in rows:
    # Parse for shifts
    shiftStart = int(r.split(" ")[0])
    shiftEnd = int(r.split(" ")[1].split("\n")[0])
    currShift = [shiftStart, shiftEnd]
    shifts[personCtr] = currShift
    personCtr += 1
print("Shifts recorded...")


# Record all covered hours without duplicates
allHoursCovered = set({})
hoursCoveredShifts = []

for person in shifts:
    shift = shifts[person]

    # Get all available hours to update all at once
    actualHours = [t for t in range(shifts[person][0], shifts[person][1])]
    allHoursCovered.update(actualHours)

    allHoursCoveredLen = len(allHoursCovered)
    
    # Calculate new covered hours after each new shift
    if person > 1:
        CoverageHoursContribution = allHoursCoveredLen - coveredHoursBefore

        # Reinitialize previous element with current element
        coveredHoursBefore = allHoursCoveredLen

    # Calculate covered hours after first shift and intialize previous element to calculate current element later
    else:
        CoverageHoursContribution = coveredHoursBefore = allHoursCoveredLen

    # Append contribution of each shift to actual coverage
    hoursCoveredShifts.append(CoverageHoursContribution)

# Reduct the minimum contribution to find max amount of hours without safeguard to fire
maxAmount = str(len(allHoursCovered) - min(hoursCoveredShifts))
print("Calculations done...")

# Write the max amount into respective output files
outputFileName = './OutputFiles/' + fileNum + '.out'
with open(str(outputFileName), "w") as f:
    f.write(maxAmount)
    f.close() 

print(fileNum + ".out was succesfully created: \n" + str(maxAmount))
