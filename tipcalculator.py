print("Welcome to the Tip Calculator")
bill =float(input("What was the total Bill? $"))
number_people =int(input("How many people to split the bill?\n"))
tip_percent =int(input("What percentage Tip would you like to give ? 10 , 12 or 15?\n"))
tip_amount =bill * (tip_percent/100)
total_amount =bill +tip_amount
bill_per_person = total_amount/number_people
final_amount =round(bill_per_person,2)
print(f"Each person should pay :${final_amount}")