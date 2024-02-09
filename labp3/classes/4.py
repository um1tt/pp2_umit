import math

class Point:
    def __init__(self, x=0, y=0):
       
        self.x = x
        self.y = y

    def show(self):

        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):

        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance
        
# Creating three Point objects
point_a = Point(0, 0)
point_b = Point(3, 4)
point_c = Point(-1, -1)

# Displaying coordinates
point_a.show()
point_b.show()
point_c.show()

# Calculating and displaying distances between points
distance_ab = point_a.dist(point_b)
distance_bc = point_b.dist(point_c)
distance_ca = point_c.dist(point_a)

print(f"Distance between point_a and point_b: {distance_ab}")
print(f"Distance between point_b and point_c: {distance_bc}")
print(f"Distance between point_c and point_a: {distance_ca}")
