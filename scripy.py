# Program to convert decimal to biner

st_count = 0
biner = 0
base = 1
bil = input("Decimal: ")

while bil > 0:
    remainder = bil % 2
    if (remainder):
        st_count = st_count + 1
    biner = biner + remainder * base
    bil = bil /2
    base = base * 10

print "Biner: ", biner

# code by Khoirul
