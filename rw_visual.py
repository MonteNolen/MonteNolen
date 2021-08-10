import matplotlib.pyplot as plt
from RandomWalk import RandomWalk
from die import Die

while True:
    die_1 = Die()
    die_2 = Die()

    results = []
    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+2):
        frequency = results.count(value)
        frequencies.append(frequency)

    x_value = list(range(2, max_result+2))


    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(die_1.num_sides + die_2.num_sides)
    ax.scatter(x_value, frequencies, c='red', s=100) #, edgecolor='none'
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("make another walk? (y/n): ")
    if keep_running == 'n':
        break