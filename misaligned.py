def generate_color_map(major_colors,minor_colors):
    color_map = []
    for i,major in enumerate(major_colors):
        for j,major in enumerate(minor_colors):
            color_map.append((i*5+j,majore,major))
    return color_map

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")
