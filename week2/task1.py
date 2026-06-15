class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def vector(self):
        return (self.p2.x - self.p1.x, self.p2.y - self.p1.y)
    
    def is_parallel(self, other):
        v1 = self.vector()
        v2 = other.vector()
        return v1[0] * v2[1] == v1[1] * v2[0]
    
    def is_perpendicular(self, other):
        v1 = self.vector()
        v2 = other.vector()
        return v1[0] * v2[0] + v1[1] * v2[1] == 0

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def is_intersecting(self, other):
        distance_squared = (self.center.x - other.center.x) ** 2 + (self.center.y - other.center.y) ** 2
        radius_sum_squared = (self.radius + other.radius) ** 2
        return distance_squared <= radius_sum_squared

class Polygon:
    def __init__(self, points):
        self.points = points
    
    def perimeter(self):
        perimeter = 0
        n = len(self.points)

        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]
            perimeter += ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

        return perimeter

line_a = Line(Point(-6, 1), Point(2, 4))
line_b = Line(Point(-6, -1), Point(2, 2))

# Are Line A and Line B parallel?
print(line_a.is_parallel(line_b))

# Are Line C and Line A perpendicular?
line_c = Line(Point(-4, -4), Point(-1, 6))
print(line_c.is_perpendicular(line_a))

# Print the area of Circle A.
circle_a = Circle(Point(6, 3), 2)
print(circle_a.area())

# Do Circle A and Circle B intersect?
circle_b = Circle(Point(8, 1), 1)
print(circle_a.is_intersecting(circle_b))

# Print the perimeter of Polygon A.
polygon_a = Polygon([Point(2, 0), Point(5, -1), Point(4, -4), Point(-1, -2)])
print(polygon_a.perimeter())
