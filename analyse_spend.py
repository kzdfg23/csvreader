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


tot_dict = csv_tot(['November-journey.csv','December-journey.csv','January-journey.csv'])
print(tot_dict)

def comparison(tot):
    monthly_cost = 66.50
    print(f"Monthly Bus & Tram Pass cost: £{monthly_cost:.2f}")
    for month,charge in tot.items():

        diff = monthly_cost - charge
        per_diff = (diff/charge) * 100
        payg_per_diff = (diff/monthly_cost) * 100
        print(f"For {month}: ")
        print(f"You spent: £{charge:.2f}")
        if charge < monthly_cost:  # compare with monthly and give recommendation
            print(f"Recommendation: PAYG is {payg_per_diff:.0f}% cheaper")
        elif charge > monthly_cost:
            print(f"Recommendation: Bus & Tram Pass is {abs(per_diff):.0f}% cheaper")
        else:
            print("Recommendation: Both options cost the same.")

comparison(tot_dict)

def ave_monthly(data):
    if data == {}:
        return 0
    total = 0
    for charge in data.values():
        total += charge
    return total/len(data)
print(ave_monthly(tot_dict))

def highest_spend_month(data):
    month, spend = next(iter(data.items()))
    for date, charge in data.items():
        if charge > spend:
            spend = charge
            month = date

    return [month,spend]
print(highest_spend_month(tot_dict))

def lowest_spend_month(data):
    month, spend = next(iter(data.items()))
    for date, charge in data.items():
        if charge < spend:
            spend = charge
            month = date

    return [month,spend]
print(lowest_spend_month(tot_dict))

def trend_detect(data):
    it = iter(data.items())
    month, spend = next(it)

    for next_month, next_spend in it:
        if next_spend > spend:
            diff = next_spend - spend
            print(f"increase by £{diff:.2f} from {month} to {next_month}")
        elif spend > next_spend:
            print(f"decrease by {(spend - next_spend):.2f} from {month} to {next_month}")
        else:
            print(f"no change from {month} to {next_month}")

        month, spend = next_month, next_spend

trend_detect(tot_dict)