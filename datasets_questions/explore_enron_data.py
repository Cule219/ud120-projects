#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# num = 0
# for key, value in enumerate(enron_data):
#     if enron_data[value]['poi'] == 1:
#         num += 1
# print num

def get_name(name):
    new_name = name.upper().split(' ')
    new_name.insert(0, new_name.pop())
    return ' '.join(new_name)

pois = ['Jeffrey K Skilling', 'Wesley Colwell', 'James Prentice']

# for name in pois:
#     print get_name(name)
#     print enron_data[get_name(name)]['total_payments']

# email_address = 0
# salary = 0
# for name in enron_data:
#     if enron_data[name]['email_address'] != 'NaN':
#         email_address += 1
#     if enron_data[name]['salary'] != 'NaN':
#         salary += 1
# print (email_address, salary)

total_payments = 0
total = 0
for name in enron_data:
    if enron_data[name]['poi'] == True:
        if enron_data[name]['total_payments'] == 'NaN':
            total_payments += 1
        total += 1
print (total_payments, total, total_payments * 100 / total)