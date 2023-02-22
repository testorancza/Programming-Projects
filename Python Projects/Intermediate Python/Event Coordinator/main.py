guests = {}


def read_guestlist(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        val = yield name, age
        if val is not None:
            val = val.split(",")
            name = val[0]
            age = int(val[1])
            guests[name] = age
            yield name, age


guestlist = read_guestlist('guest_list.txt')

# task 3;
# Adding Jane,35
for i in range(10):
    print(next(guestlist))
guestlist.send("Jane, 35")
print(next(guestlist))
print(next(guestlist))
print(next(guestlist))
print(next(guestlist))

# question
for i in guests:
    print(i)
# task 4
over_21 = (key for key, val in guests.items() if val > 21)

for guest_name in over_21:
    print(guest_name)


# task 5
def chicken():
    food = 'Chicken'
    table = 1
    for i in range(5):
        seat = i + 1
        yield f'menu: {food}', f'table: {table}', f'seat: {seat}'


def beef():
    food = 'Beef'
    table = 2
    for i in range(5):
        seat = i + 1
        yield f'menu: {food}', f'table: {table}', f'seat: {seat}'


def fish():
    food = 'Fish'
    table = 3
    for i in range(5):
        seat = i + 1
        yield f'menu: {food}', f'table: {table}', f'seat: {seat}'


# task 6
def meal_assigner(guests, generator1, generator2, generator3):
    names = list(guests.keys())
    for i in range(5):
        yield (names[i], next(generator1))
    for i in range(5):
        i += 5
        yield (names[i], next(generator2))
    for i in range(5):
        i += 10
        yield (names[i], next(generator3))


meal_plans = meal_assigner(guests, chicken(), fish(), beef())

for i in meal_plans:
    print(i)