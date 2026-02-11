import csv #import csv module

with open('journeys.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file) #DictReader method to make field name keys for each value
    tot = 0
    for line in csv_reader:
        tot += float(line["fare"]) #Sum fare values
    print(f"Total PAYG spend: £{tot:.2f}")#print sum
    monthly_cost = 160
    print(f"Monthly travelcard cost: £{monthly_cost:.2f}")
    diff = monthly_cost - tot
    print(f"Recommendation: PAYG is cheaper by £{diff:.2f}")#compare with monthly and give recommendation


