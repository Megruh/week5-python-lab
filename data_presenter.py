
open_file = open('CupcakeInvoices.csv')

# for row in open_file:
#     print(row)

# for cupcake in open_file:
#     cupcake = cupcake.split(',')
#     print(cupcake[2])

grand_total = 0
for row in open_file:
    row = row.split(',')
    quantity = int(row[3])
    price = float(row[4].rstrip('/r/n'))
    total = quantity * price
    decimal_limit = "{:.2f}".format(total)
    print(row[0] + "'s total is " + str(decimal_limit))
    grand_total += total
grand_total = "{:.2f}".format(grand_total)
print(grand_total)

open_file.close()