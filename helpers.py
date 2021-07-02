def get_delivery_charge(distance):
    if 0 < distance < 10000:
        return 5000
    elif 10000 <= distance < 20000:
        return 10000
    elif 20000 <= distance < 50000:
        return 50000
    elif distance >= 50000:
        return 100000