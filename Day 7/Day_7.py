def breadth_first(self, matrix):
    visited, queue = set(), [(self.x, self.y)]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for x2, y2 in ((self.x + 1, self.y), (self.x + 1, self.y + 1),
                           (self.x, self.y + 1), (self.x + 1, self.y - 1),
                           (self.x, self.y - 1), (self.x - 1, self.y - 1),
                           (self.x - 1, self.y), (self.x - 1, self.y + 1)
                           ):
                if 0 <= x2 <= matrix.width and 0 <= y2 <= matrix.height:
                    queue.append(tuple((x2, y2)))
    return visited
