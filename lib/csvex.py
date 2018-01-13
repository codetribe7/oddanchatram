import csv
with open('../data/oddanchatram/2013/oddanchatram-market-vegetable-price-details-1122013.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(', '.join(row))
