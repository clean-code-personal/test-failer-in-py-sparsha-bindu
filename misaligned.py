
def print_color_map(): #returns a list of strings, each representing a single mapping from number to color
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return color_map

def test_print_color_map(): #performs these checks and asserts that the length of the list is 25, which is the number of mappings that should be present
    color_map = print_color_map()
    assert len(color_map) == 25
    for i, color in enumerate(color_map):
        parts = color.split(" | ")
        assert int(parts[0]) == i + 1 # Check that the first value starts from 1, not 0
        assert parts[1] in ["White", "Red", "Black", "Yellow", "Violet"]
        assert parts[2] in ["Blue", "Orange", "Green", "Brown", "Slate"]

test_print_color_map()
print("All tests passed!")

