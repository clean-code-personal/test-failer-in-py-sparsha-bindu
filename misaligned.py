
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return color_map


def test_print_color_map():
    color_map = print_color_map()
    assert(len(color_map) == 25)
    for i, color in enumerate(color_map):
        parts = color.split(" | ")
        assert(parts[0] == str(i))
        assert(parts[1] in ["White", "Red", "Black", "Yellow", "Violet"])
        assert(parts[2] in ["Blue", "Orange", "Green", "Brown", "Slate"])
color_map=print_color_map()
test_print_color_map()
print("All is well (maybe!)\n")
