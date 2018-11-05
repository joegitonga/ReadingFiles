'''
Created on Oct 19, 2018

@author: Chomba
'''
import csv

class Loans:
    
    def __intit__(self, network, product,month):
        self.network = network
        self.product = product
        self.month = month
        

with open('Loans.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    #for row in csvReader:
        #print(row)
        
    def findNetwork(csvReader):
        network_row = []
        for row in csvReader:
            if row[1] == "'Network 1'":
                network_row.append(row[4])
        return [[sum(map(int, network_row))], [len(network_row)]]
    
    print(findNetwork(csvReader))
                
            
        