import csv #import csv module
from datetime import datetime

def csv_tot(filepath):#turned into func
    monthly_tot = {}
    for file in filepath:
        with open(file, 'r', newline='', encoding='utf-8') as csv_file:#'r' means read, newline makes sure there isn't extra spacing, encoding handles special characters
            csv_reader = csv.DictReader(csv_file) #DictReader method to make field name keys for each value


            for line in csv_reader:
                date = line["Date"]
                charge = -(float(line["Daily Charge (GBP)"])) #Sum fare values

                date_obj = datetime.strptime(date, "%d/%m/%Y")#(strptime)string parse time turns string into date
                month_name = date_obj.strftime("%B %Y")#(strftime)string formate time turns date into text

                if month_name not in monthly_tot:
                    monthly_tot[month_name] = 0

                monthly_tot[month_name] += charge

    return monthly_tot #print sum

#print(csv_tot(['November-journey.csv','December-journey.csv','January-journey.csv']))
tot_dict = csv_tot(['November-journey.csv','December-journey.csv','January-journey.csv'])

def comparison(tot):
    monthly_cost = 66.50
    print(f"Monthly Bus & Tram Pass cost: £{monthly_cost:.2f}")
    for date,charge in tot.items():

        diff = monthly_cost - charge
        print(f"For {date}: ")
        if charge < monthly_cost:  # compare with monthly and give recommendation
            print(f"Recommendation: PAYG is cheaper by £{diff:.2f}")
        elif charge > monthly_cost:
            print(f"Recommendation: Bus & Tram Pass is cheaper by £{abs(diff):.2f}")
        else:
            print("Recommendation: Both options cost the same.")

comparison(tot_dict)

