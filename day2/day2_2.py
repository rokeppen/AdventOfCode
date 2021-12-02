def get_product():
    aim, depth, distance = 0, 0, 0
    for x in open("input.txt", "r"):
        key, value = x.split(" ")
        if key == "forward":
            distance += int(value)
            depth += aim*int(value)
        else:
            aim += -int(value) if key == "up" else int(value)
    return depth*distance


if __name__ == '__main__':
    print(get_product())
