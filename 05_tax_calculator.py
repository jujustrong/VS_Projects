
GROSS_SALARY = input("enter gross pay: ")
STATE = input("enter state abbreviation (ex. NY, CA, TX, etc.): ")

def USA(salary, state):

    federal_tax = 0
    state_tax = 0
    fica = 0

    STANDARD_DEDUCTION_FEDERAL = 12950
    STANDARD_DEDUCTION_NY = 8000
    STANDARD_DEDUCTION_CA = 4601

    salary = int(salary)
    taxable_income = salary - STANDARD_DEDUCTION_FEDERAL

    if taxable_income < 0:
        federal_tax = 0
    elif taxable_income <= 10275:
        federal_tax = .10*taxable_income
    elif 10275 < taxable_income <= 41775:
        federal_tax = 1027.5+.12*(taxable_income-10275)
    elif 41775 < taxable_income <= 89075:
        federal_tax = 4807.5 +.22*(taxable_income-41775)
    elif 89075 < taxable_income <= 170050:
        federal_tax = 15213.5+.24*(taxable_income-89075)
    elif 170050 < taxable_income <= 215950:
        federal_tax = 34647.5+.32*(taxable_income-170050)
    elif 215950 < taxable_income <= 539900:
        federal_tax = 49335.5+.35*(taxable_income-215950)
    elif taxable_income > 539900:
        federal_tax = 162718+.37*(taxable_income-539900)


    #FICA deducted from *Gross*

    if salary <= 160200:
        fica = 0.0765 * salary
    elif 160200 < salary <= 200000:
        fica = 0.062 * 147000 + 0.0145 * salary
    elif salary > 200000:
        fica = 0.062 * 147000 + 0.0145 * 200000 + 0.0235 * (salary - 200000)


    #STATE TAXES

    def NY():
        ny_taxable = salary - 8000
        if ny_taxable <= 8500:
            state_tax = .04*ny_taxable
        elif 8500 < ny_taxable <= 11700:
            state_tax = 340+.045*(ny_taxable - 8500)
        elif 11700 < ny_taxable <= 13900:
            state_tax = 484+.0525*(ny_taxable - 11700)
        elif 13900 < ny_taxable <= 80650:
            state_tax = 600+.0585*(ny_taxable - 13900)
        elif 80650 < ny_taxable <= 215400:
            state_tax = 4504+.0625*(ny_taxable - 80650)
        elif 215400 < ny_taxable <= 1077550:
            state_tax = 12926+.0685*(ny_taxable - 215400)
        elif 1077550 < ny_taxable <= 5000000:
            state_tax = 71984+.0965*(ny_taxable - 1077550)
        elif 5000000 < ny_taxable <= 25000000:
            state_tax = 450500+.103*(ny_taxable - 5000000)
        elif ny_taxable > 25000000:
            state_tax = 2510500+.109*(ny_taxable - 25000000)

        return state_tax

    def CA():
        ca_taxable = salary - 4601
        if ca_taxable <= 10099:
            state_tax = .01*ca_taxable
        elif 10099 < ca_taxable <= 23942:
            state_tax = 100.99+.02*(ca_taxable - 10099)
        elif 23942 < ca_taxable <= 37788:
            state_tax = 377.85+.04*(ca_taxable - 23942)
        elif 37788 < ca_taxable <= 52455:
            state_tax = 931.69+.06*(ca_taxable - 37788)
        elif 52455 < ca_taxable <= 66295:
            state_tax = 1811.71+.08*(ca_taxable - 52455)
        elif 66295 < ca_taxable <= 338639:
            state_tax = 2918.91+.093*(ca_taxable - 66295)
        elif 338639 < ca_taxable <= 406364:
            state_tax = 28246.9+.103*(ca_taxable - 338639)
        elif 406364 < ca_taxable <= 677275:
            state_tax = 35222.58+.113*(ca_taxable - 406364)
        elif ca_taxable > 677275:
            state_tax = 65835+.123*(ca_taxable - 677275)

        return state_tax
    

    if state == "NY":
        total_tax = federal_tax + NY()
        
    elif state == "CA":
        total_tax = federal_tax + CA()

    taxrate = ((total_tax + fica) / salary) * 100
    netpay = salary - (total_tax + fica)
    
    return f'Your net pay is ${netpay} with a tax rate of {int(taxrate)}%'


    

result = USA(GROSS_SALARY, STATE)
print(result)