import pandas as pd
import os, os.path

DIR = '../data/requests'

def save_customer_request(email, date, time):

    customer_request = {'Email': [], 'Date': [], 'Departure': [],}

    for t in time:

        customer_request['Email'].append(email)
        customer_request['Date'].append(date)
        customer_request['Departure'].append(t)

    df = pd.DataFrame.from_dict(customer_request)
    num = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) - 1
    df.to_csv(f'../data/requests/request_{num}.csv', index=False)