from io import StringIO
import csv

a = 'abc,"de,f","hij"'

f = StringIO(a)
reader = csv.reader(f, delimiter=',')
for row in reader:
    print (row[2])