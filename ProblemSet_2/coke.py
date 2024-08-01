Amount_due = 50
print(f"Amount Due: {Amount_due}")

while Amount_due > 0:
    coin_inserted = int(input("Insert coin: "))
    Amount_due -= coin_inserted
    if Amount_due > 0:
        print(f"Amount Due: {Amount_due}")

#if amount due is negative ie more coins than the amount due has entered then print out the change
#abs() means absolute. Since when change is owed, we're printing out the negative so convert it into pos
#either multiply by neg or take absolute.

if Amount_due < 0:
    print(f"Change owed: {abs(Amount_due)}")
else:
    print("Change owed: 0")