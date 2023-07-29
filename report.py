
import csv
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--teammap', '-t')
parser.add_argument('--productmaster', '-p')
parser.add_argument('--sales', '-s')
#note: FIX THIS TO MATCH ORIGINAL ARGS
parser.add_argument('--team-report', dest = 'trep')
parser.add_argument('--product-report', dest = 'prep')

args = parser.parse_args()

t = args.teammap
p = args.productmaster
s = args.sales

tr = args.trep
pr = args.prep




def main(teammap, prod, sales, treport, preport):

    #create dicts for the given csv's
    with open(teammap, mode= 'r') as tmap:
        with open (prod, mode= 'r') as pmas:
            with open(sales, mode= 'r') as smap:
                #productmaster and sales don't have headers. This fixes that.
                prodfields = ['ProductId', 'Name', 'Price', 'LotSize']
                salefields = ['SaleId', 'ProductId', 'TeamId', 'Quantity', 'Discount']


                teamreader = csv.DictReader(tmap)
                prodreader = csv.DictReader(pmas, fieldnames= prodfields)
                salereader = csv.DictReader(smap, fieldnames= salefields)

                teamFile = []
                prodFile = []
                saleFile = []

                for i in teamreader:
                    teamFile.append(i)

                for i in prodreader:
                    prodFile.append(i)

                for i in salereader:
                    saleFile.append(i)

                with open (treport, 'w', newline= '') as teamreport:
                    fields = ['Team', 'GrossRevenue']
                    writer = csv.DictWriter(teamreport, fieldnames = fields)

                    writer.writeheader()
                    for team in teamFile:
                        gross = 0
                        id = team['TeamId']
                        name = team['Name']
                        for sale in saleFile:
                            if sale['TeamId'] == id:
                                pid = sale['ProductId']
                                quantity = int(sale['Quantity'])
                                discount = float(sale['Discount'])
                                multiplier = (100-discount)/100
                                for item in prodFile:
                                    if item['ProductId'] == pid:
                                        price = float(item['Price'])
                                        lotSize = int(item['LotSize'])
                                        gross = gross + (quantity * lotSize * price * multiplier)
                        writer.writerow({'Team': name, 'GrossRevenue': gross})

                with open (preport, 'w', newline='') as prodreport:
                    fields = ['Name', 'GrossRevenue', 'TotalUnits', 'DiscountCost']
                    writer = csv.DictWriter(prodreport, fieldnames = fields)

                    writer.writeheader()
                    for item in prodFile:
                        gross = 0
                        totaldiscount = 0
                        units = 0
                        pid = item['ProductId']
                        name = item['Name']
                        price = float(item['Price'])
                        lotSize = int(item['LotSize'])
                        for sale in saleFile:
                            if sale['ProductId'] == pid:
                                quantity = int(sale['Quantity'])
                                discount = float(sale['Discount'])
                                multiplier = (100-discount)/100
                                baseprice = quantity * lotSize * price
                                totaldiscount = totaldiscount + (baseprice - (baseprice * multiplier))
                                gross = gross + (baseprice * multiplier)
                                units = units + (lotSize * quantity)

                        writer.writerow({'Name': name, 'GrossRevenue': gross, 'TotalUnits': units, 'DiscountCost': totaldiscount})

                            
    return 0

main (t, p, s, tr, pr )