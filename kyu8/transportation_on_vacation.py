def rental_car_cost(d):
    total_amount = d * 40
    if d >= 7:
        total_amount -= 50
    elif d > 3:
        total_amount -= 20
    return total_amount
