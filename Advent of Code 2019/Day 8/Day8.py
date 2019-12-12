def read_input():
    image = []
    with open('Day_8_input.txt', "r") as file:
        for x in file:
            for digit in x:
                image.append(int(digit))
    return image


def get_product(image):

    min0 = float('inf')
    mindict = {}
    counter = 0
    count = {0: 0, 1: 0, 2: 0}

    for pixel in image:
        counter += 1
        if counter % (HEIGHT*WIDTH) == 0:
            if count[0] < min0:
                min0 = count[0]
                mindict = count
            count = {0: 0, 1: 0, 2: 0}
        if pixel in count:
            count[pixel] += 1
    return mindict[1]*mindict[2]


def get_layer_dict():
    layer_dict = {}
    for position in range(0, HEIGHT*WIDTH+1):
        layer_dict[position] = ""
    return layer_dict

def get_all_layers(image):
    counter = 0
    dict_list = []
    layer = get_layer_dict()
    for pixel in image:
        layer[counter % (HEIGHT * WIDTH)] = pixel
        counter += 1
        if counter % (HEIGHT*WIDTH) == 0:
            dict_list.append(layer)
            layer = get_layer_dict()
    return dict_list


def process_message(image):
    last_layer = get_layer_dict()
    pixel_done = set()
    for layer in get_all_layers(image):
        for position in range(0,HEIGHT*WIDTH+1):
            if layer[position] == 0 and position not in pixel_done:
                last_layer[position] = "  "
                pixel_done.add(position)
            elif layer[position] == 1 and position not in pixel_done:
                last_layer[position] = " X"
                pixel_done.add(position)
    return last_layer


def print_message(last_layer):
    line = "Code Below Beep Boop:\n"
    for pixel in range(0,HEIGHT*WIDTH+1):
        if pixel % (WIDTH) == 0:
            print(line)
            line = ""
        line += str(last_layer[pixel])


HEIGHT = 6
WIDTH = 25
image = read_input()

print("Product is:", get_product(image))
print_message(process_message(image))
