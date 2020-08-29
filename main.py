import random
import math
import pprint


# fitness function(s)
def check_fit(solution_test):
    this_fit = 0

    #1	The Toyota Camry was hired at 6:00am by a British couple.


    #2	The car in the middle had a black colour.



    #3	The Hyundai Accent left the depot at 9:00am.


    # #4	The Holden Barina with a blue colour was to the left of the car that carries the British couple.


    #5	To the right of the car hired by a French lady was the car going to Gold Coast.


    # #6	The Nissan X-Trail was heading for Sydney.


    # #7	To the right of the car carrying a Chinese businessman was the car with a green colour.

    #8	The car going to Newcastle left at 5:00am.


    #9	The Honda Civic left at 7:00am and was on the right of the car heading for Gold Coast.

    #10	The car with a red colour was going to Tamworth.


    #11	To the left of the car that left at 7:00am was the car with a white colour.

    #12	The last car was hired by an Indian man.


    #13	The car with a black colour left at 8:00am.


    #14	The car carrying an Indian man was to the right of the car hired by a Chinese businessman.


    #15	The car heading for Tamworth left at 6:00am.


    return this_fit


# variables
position = [0, 1, 2, 3, 4]
color = ['black', 'blue', 'green', 'red', 'white']
make = ['Holden Barina', 'Honda Civic', 'Hyundai Accent', 'Nissan X-Trail', 'Toyota Camry']
time = ['5am', '6am', '7am', '8am', '9am']
person = ['British', 'Canadian', 'Chinese', 'French', 'Indian']
destination = ['Gold Coast', 'Newcastle', 'Port Macquarie', 'Sydney', 'Tamworth']


# seed for starter solution
random.shuffle(position)
random.shuffle(color)
random.shuffle(make)
random.shuffle(time)
random.shuffle(person)
random.shuffle(destination)

# random starter solution
solution = []
for i in range(0, 5):
    solution.append(
        {'position': position[i], 'color': color[i], 'make': make[i], 'time': time[i], 'person': person[i], 'destination': destination[i]}
    )

# SIM ANNEALING

temp = 10
cooling = 0.9995
fit = 100
iterations = 0

while temp > 0.000000001 and fit > 0:
    iterations += 1
    print(f"Fitness is {fit}")

    # the actual solution (for testing reasons)
    solutionTest = [
        {'position': 0, 'color': 'blue', 'make': 'Holden Barina', 'time': '6am', 'person': 'Canadian', 'destination': 'Newcastle'},
        {'position': 1, 'color': 'red', 'make': 'Toyota Camry', 'time': '5am', 'person': 'British', 'destination': 'Tamworth'},
        {'position': 2, 'color': 'black', 'make': 'Nissan X-Trail', 'time': '8am', 'person': 'French', 'destination': 'Sydney'},
        {'position': 3, 'color': 'white', 'make': 'Hyundai Accent', 'time': '9am', 'person': 'Chinese', 'destination': 'Gold Coast'},
        {'position': 4, 'color': 'green', 'make': 'Honda Civic', 'time': '7am', 'person': 'Indian', 'destination': 'Port Macquarie'},
    ]

    # to find the solutionTest, randomly pick an attribute and swap 2 random cars
    # solutionTest = solution
    attributes = ['position', 'color', 'make', 'time', 'person', 'destination']
    rand_attribute = random.choice(attributes)
    car1 = random.randint(0, 4)
    car2 = random.randint(0, 4)
    while car2 == car1:
        position2 = random.randint(0, 4)
    solutionTest[car1][rand_attribute], solutionTest[car2][rand_attribute] = solutionTest[car2][rand_attribute], solutionTest[car1][rand_attribute]

    fitTest = check_fit(solutionTest)
    if fitTest < fit:
        solution = solutionTest
        fit = fitTest
    else:
        try:
            swap = math.exp((fit - fitTest) / temp)
        except ZeroDivisionError:
            swap = 1
        if swap > random.choice([0, 1]):
            fit = fitTest
            solution = solutionTest
            temp = temp * cooling

print(f"Solved using {iterations} iterations at {fit} fitness.")
pprint.pprint(solution)