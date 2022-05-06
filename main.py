import json
from api_request import *
from functions import *
import ast

if __name__ == '__main__':

    information = FlightAndPassengerInformation()
    print(information.flightNumber)

    transaction_num = generate_transaction_number()
    customer_id = generate_customer_ID()
    response = ast.literal_eval(information.response)
    for k, v in response.items():
        if k == "destinations":
            dest = (v)
    for k, v in dest[0].items():
        if k == "medianDelay":
            delay = v

    if "-" not in delay.split("-")[0]:
        if int(delay.split(":")[0]) >= 1:
            hoursToMin = int(delay.split(":")[0]) * 60
        try:
            hoursToMin
        except NameError:
            var_exists = False
        else:
            var_exists = True
        hoursToMin = hoursToMin if var_exists else 0
        calcDelay = hoursToMin + int(delay.split(":")[1])
    else:
        calcDelay = 0

    try:
        calcDelay
    except NameError:
        var_exists = False
    else:
        var_exists = True

    calcDelay = calcDelay if var_exists else 0
    write_customer(transaction_num, information.customerFirstName, information.customerLastName,
                   get_wallet_amount(), information.flightNumber,
                   calcDelay,
                   calculate_payout(calcDelay), customer_id)

    print("passenger delayed (min): ", calcDelay, " passenger_owed: $", calculate_payout(calcDelay))

    update_insurance_wallet(get_wallet_change(calcDelay), transaction_num)
