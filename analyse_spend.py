import csv #import csv module

with open('December-journey.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file) #DictReader method to make field name keys for each value

    tot = 0
    for line in csv_reader:
        #print(line)
        tot += -(float(line["Daily Charge (GBP)"])) #Sum fare values

    print(f"Total PAYG spend: £{tot:.2f}")#print sum

    monthly_cost = 172.50
    print(f"Monthly travelcard cost: £{monthly_cost:.2f}")

    diff = monthly_cost - tot

    if tot < monthly_cost:#compare with monthly and give recommendation
        print(f"Recommendation: PAYG is cheaper by £{diff:.2f}")
    elif tot > monthly_cost:
        print(f"Recommendation: Travelcard is cheaper by £{abs(diff):.2f}")
    else:
        print("Recommendation: Both options cost the same.")


