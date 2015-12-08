import csv

combined = []
bulls = []
cattle = []
with open('bulls.csv', 'r') as f:
    for bull in csv.reader(f):
        if bull[2] != '':
            bulls.append(bull)

with open('cattle.csv', 'r') as f:
    for cow in csv.reader(f):
        if cow[1] != '':
            cattle.append(cow)


bull_header = bulls.pop(0)[3:]
cattle_header = cattle.pop(0)[2:]
bull_header = ["bull_" + column_name for column_name in bull_header]
cattle_header = ["cow_" + column_name for column_name in cattle_header]
combined_header = bull_header + cattle_header

offspring_data = {}

for bull in bulls:
    bull_asa = bull[2]
    for cow in cattle:
        cow_asa = cow[1]
        offspring_name = "{}-{}".format(bull_asa, cow_asa)
        combined_data = bull[3:] + cow[2:]
        offspring_data[offspring_name] = dict(zip(combined_header, combined_data))

for offspring in offspring_data:
    for column_name in offspring_data[offspring]:        
        try:
            new_value = float(offspring_data[offspring][column_name])
            offspring_data[offspring][column_name] = new_value
        except:
            pass

##print("DATA PREPARED")

for offspring in offspring_data:
    for data in ['REA']:
        predicted = (offspring_data[offspring]['bull_{}'.format(data)] +  offspring_data[offspring]['cow_{}'.format(data)]) / 2.0
        offspring_data[offspring]['predicted_REA'] = predicted

##print("FINISHED REA")

##for offspring in offspring_data:
##    print(offspring_data[offspring]['bull_REA'],
##          offspring_data[offspring]['cow_REA'],
##          offspring_data[offspring]['predicted_REA'])

for offspring in offspring_data:
    for data in ['API']:
        predicted = (offspring_data[offspring]['bull_{}'.format(data)] +  offspring_data[offspring]['cow_{}'.format(data)]) / 2.0
        offspring_data[offspring]['predicted_API'] = predicted

##print("FINISHED API")

for offspring in offspring_data:
    print(offspring_data[offspring]['bull_API'],
          offspring_data[offspring]['cow_API'],
          offspring_data[offspring]['predicted_API'])

for offspring in offspring_data:
    for data in ['TI']:
        predicted = (offspring_data[offspring]['bull_{}'.format(data)] +  offspring_data[offspring]['cow_{}'.format(data)]) / 2.0
        offspring_data[offspring]['predicted_TI'] = predicted

##print("FINISHED TI")

for offspring in offspring_data:
    print(offspring_data[offspring]['bull_TI'],
          offspring_data[offspring]['cow_TI'],
          offspring_data[offspring]['predicted_TI'])

for offspring in offspring_data:
    for data in ['BW']:
        try:
            predicted = (offspring_data[offspring]['bull_{}'.format(data)] +  offspring_data[offspring]['cow_{}'.format(data)]) / 2.0
        except:
            predicted = 0
        offspring_data[offspring]['predicted_BW'] = predicted

##print("FINISHED BW")

##for offspring in offspring_data:
##    print(offspring_data[offspring]['bull_BW'],
##          offspring_data[offspring]['cow_BW'],
##          offspring_data[offspring]['predicted_BW'])

for offspring in offspring_data:
    for data in ['MILK']:
        try:
            predicted = (offspring_data[offspring]['bull_{}'.format(data)] +  offspring_data[offspring]['cow_{}'.format(data)]) / 2.0
        except:
            predicted = 0
        offspring_data[offspring]['predicted_MILK'] = predicted

##print("FINISHED MILK")

##for offspring in offspring_data:
##    print(offspring_data[offspring]['bull_MILK'],
##          offspring_data[offspring]['cow_MILK'],
##        offspring_data[offspring]['predicted_MILK'])

for offspring in offspring_data:
    for data in ['WW']:
        predicted = (offspring_data[offspring]['bull_{}'.format(data)] +  offspring_data[offspring]['cow_{}'.format(data)]) / 2.0
        offspring_data[offspring]['predicted_WW'] = predicted

##for offspring in offspring_data:
##    print(offspring_data[offspring]['bull_WW'],
##          offspring_data[offspring]['cow_WW'],
##          offspring_data[offspring]['predicted_WW'])

for offspring in offspring_data:
    for data in ['YW']:
       predicted = (offspring_data[offspring]['bull_{}'.format(data)] +  offspring_data[offspring]['cow_{}'.format(data)]) / 2.0
       offspring_data[offspring]['predicted_YW'] = predicted
        
##for offspring in offspring_data:
##    print(offspring_data[offspring]['bull_YW'],
##          offspring_data[offspring]['cow_YW'],
##          offspring_data[offspring]['predicted_YW'])

for offspring in offspring_data:
    for data in ['MARB']:
        predicted = (offspring_data[offspring]['bull_{}'.format(data)] +  offspring_data[offspring]['cow_{}'.format(data)]) / 2.0
        offspring_data[offspring]['predicted_MARB'] = predicted

for offspring in offspring_data:
    for data in ['MARB']:
        try:
            predicted = (offspring_data[offspring]['bull_{}'.format(data)] +  offspring_data[offspring]['cow_{}'.format(data)]) / 2.0
        except:
            predicted = 0
        offspring_data[offspring]['predicted_MARB'] = predicted




