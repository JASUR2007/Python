def rates(based_price,monthes,monthly_payment, monthly_fine):
    full = monthes * monthly_payment
    result = full - based_price
    fund = int((monthly_payment*monthly_fine/100)+monthly_payment)
    precentage = (full*100/based_price)-100
    if monthly_fine == 0:
        return f'You will pay: {full} \nOver paying: {result} \nPrecentage: {int(precentage)}% \nYour have not fines'
    else:
        changed_full = full + fund
        changed_over_pay = result + fund
        precentage = (changed_full/(based_price/100))-100
        return f'You will pay: {changed_full} \nOver paying: {changed_over_pay} \nPrecentage: {int(precentage)}% \nYour fine: {fund}'

print(rates(5000000,12,600000,0))


