class Point:
    def __init__(self, tuple, id):
        self.id = id
        self.x = int(tuple[0])
        self.y = int(tuple[1])

class Matrice:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = self.gen_matrix()
        self.map = self.gen_map()

    def gen_matrix(self):
        matrix = []
        for y in range(self.height):
            for x in range(self.width):
                matrix.append((x, y))
        return matrix

    def gen_map(self):
        map = {}
        for item in self.matrix:
            map[item] = "Empty"
        return map

    def place_input_point(self, point):
        self.map[(point.x, point.y)] = point.id

    def manhanthan(self, square, list_of_point):
        """
        Manhantan distance between two points
        """
        distances = {}
        for point in list_of_point:
            distances[point.id] = abs(int((square[0] - int(point.x)))) + abs((square[1] - int(point.y)))
        return distances

    def find_distance(self, square, list_of_point):
        # Manhathan distance
        distances = self.manhanthan(square, list_of_point)
        min = 10000
        answer = None
        # Get the min distance in dictionary
        for key, values in distances.items():
            if values < min:
                min = values
                answer = key
        # Check if two points or more are equidistant
        count = 0
        for key, values in distances.items():
            if values == min:
                count += 1
            if count > 1:
                answer = '.'
                return answer
        return answer

    def fill_map(self, list_of_points):
        """
        Fill map with points or .
        """
        for square in self.matrix:
            if self.map[square] == 'Empty':
                self.map[square] = self.find_distance(square, list_of_points)

    def count_areas(self, list_of_points):
        """
        Count areas for a given point
        """
        answer = {}
        for point in list_of_points:
            answer[point.id] = sum(value == point.id for value in self.map.values())

        return answer

# Part 2 function
    def find_region(self, square, list_of_points, threshold):
        """
        Find if a location is below a threshold of distances
        """
        distances = self.manhanthan(square, list_of_points)
        total_sum = sum(value for value in distances.values())
        if total_sum <= threshold:
            return '#'
        return '.'

# Part 2 function
    def fill_region(self, list_of_points,threshold):
        """
        Fill a region with either . or #
        """
        for square in self.matrix:
            self.map[square] = self.find_region(square, list_of_points, threshold)

def get_input(filename):
    file = open(filename, "r")
    point_list = []
    for counter, line in enumerate(file):
        line = line.replace(",", "")
        line = line.replace("\n", "").split(" ")
        point_list.append(Point(line, counter))
    file.close()
    return point_list

# Get the inputs
point_list = get_input('Day_6_input')
test_list = get_input('Day_6_test')

# Solve Part 1
def solve(point_list, size):
    """
    I compare two matrices with moving the point by one
    If an area is finite, it should be the same between the two matrices
    I pick the highest at the end.
    """
    matrix = Matrice(size, size)
    for point in point_list:
        matrix.place_input_point(point)
    matrix.fill_map(point_list)
    a = matrix.count_areas(point_list)

    matrix = Matrice(size, size)
    for point in point_list:
        point.x += 1
        point.y += 1
        matrix.place_input_point(point)
    matrix.fill_map(point_list)
    b = matrix.count_areas(point_list)

    answer = []
    for keys, values in a.items():
        if values == b[keys]:
            answer.append(values)

    return max(answer)

print(solve(test_list, 10))
print(solve(point_list, 500))

def part2_solve(input, size, threshold):
    """
    Find the size of the region for a given threshold.
    """
    matrix = Matrice(size, size)
    matrix.fill_region(input, threshold)
    count = 0
    for keys, values in matrix.map.items():
        if values == '#': count +=1
    return count

print(part2_solve(test_list, 10, 30))
print(part2_solve(point_list, 500, 10000))