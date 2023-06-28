def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# count_up_to(5)
cuonter=count_up_to(3)
# print(next(cuonter))
# print(next(cuonter))

for nun in cuonter:
    print(nun)