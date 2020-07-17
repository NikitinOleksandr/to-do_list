def final_deposit_amount(*interest, amount=1000):
    for arg in interest:
        amount *= arg / 100 + 1
    return round(amount, 2)
