print("Input MR Size in inches")
mrsize = float(input())

print("Input slit roll size in millimeters")
slitsize = float(input()) / 25.4 # converts to inches

print("Input number of slits across")
across = int(input())

trimsize = mrsize - (slitsize * across) # hopefully does the math for the trim size
print("You have a trim size of", trimsize)

print("What is your label roll weight")
rollweight = float(input())

trimweight = (rollweight / slitsize) * trimsize
print("Your trim weight is", trimweight)
