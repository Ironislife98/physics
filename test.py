x = [100, 100]
y = [100, 200]

# Distance between two points should be 100
distance = max(x[1], y[1]) - min(x[1], y[1])
run = True
while run:
    print(distance)
    force = ((6.67 * (10 ** -11)) * (6 * 10 ** 24) * 1) / distance
    x[1] -= force
    if distance <= 0:
        break