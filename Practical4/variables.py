a = 5.08  # Population in 2004
b = 5.33  # Population in 2014
c = 5.55  # Population in 2024

d = b - a # Change between 2004 and 2014
e = c - b # Change between 2014 and 2024

# Compare d to e:
# d = 0.25 million, e = 0.22 million. 
# Since e is smaller than d,
# the population growth is decelerating in Scotland.

# Create variables X and Y
X = True
Y = False

W = X or Y

# Truth table for W:
# X = True,  Y = True  -> W = True
# X = True,  Y = False -> W = True
# X = False, Y = True  -> W = True
# X = False, Y = False -> W = False