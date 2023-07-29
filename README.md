DESCRIPTION:

This was a coding assessment I did for a job application a while back. I figured I may as well upload it.
All indications of the company have been removed, for the sake of privacy.


USAGE:

This program will generate two output .csv files based on given input .csv files.

The required input files are as follows: 

a "teams" file in the following format.

TeamId,Name
1,Team One
2,Team Two

a "sales" file in the following format. It should not have a header, but the columns, from left to right, represent the following:
SaleId, ProductId, TeamId, Quantity, Discount. Discount should be represented as a floating point percentage as seen below.

1,1,2,10,0.00
2,1,1,1,0.00
3,2,1,5,5.00
4,3,4,1,2.50

a "products" file in the following format. It should not have a header, but the columns, from left to right, represent the following:
ProductId, Name, Price, LotSize. Price is by unit, not by lot.

1,Minor Widget,0.25,250
2,Critical Widget,5.00,10
3,Complete System (Basic),500,1
4,Complete System (Deluxe),625,1

To run the program, you can use the following command line arguments:

--teammap, -t: Designates the "teams" file
--productmaster, -p: Designates the "product" file
--sales, -s: Designates the "sales" file
--team-report: Designates the name you want to give to the file the program creates with the team report.
--product-report: Designates the name you want to give to the file the program creates with the product report.
