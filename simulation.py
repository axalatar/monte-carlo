import random
import math

# a monte carlo simulation!
# the math goes like this:
#
# imagine you have a unit circle (r=1) centered inside the smallest possible square (s=2)
# the area of the circle is (pi * r^2) = (pi * 1^2) = pi, and the square is (s^2) = (2^2) = 4
# given any random point inside the square, the chance it's inside the circle is pi/4
#
# therefore, given enough random points inside the square, if you can measure how many are
# inside the circle, you can estimate pi by doing
# pi = 4 * ((points inside circle) / (total points))


num_points = 100000000
num_circle = 0

progress_interval = 0.1
# in percentage; 0.1 = 10% complete



per_interval = progress_interval * num_points
for i in range(num_points):
    x = random.random()
    y = random.random()
    # even though the circle is centered at (0, 0), so the real range should be [-1, 1],
    # adding [-1, 0] does not change the probabilities because all the numbers get squared
    # and made positive anyway

    dist = math.sqrt(x ** 2 + y ** 2)
    if(1 >= dist):
        num_circle += 1
    
    if(i % per_interval == 0):
        if i == 0: 
            continue

        print(f"{i/per_interval} interval(s) completed; {i} points placed. Estimate = {4*(num_circle)/i}")

print(4 * (num_circle/num_points))