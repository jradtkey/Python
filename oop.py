# import math
#
# class Pizza:
#     def __init__(self, radius, ingredients):
#         self.ingredients = ingredients
#         self.radius = radius
#
#     def __repr__(self):
#         return self.ingredients
#
#     def area(self):
#         return self._circle_area(self.radius)
#
#     @staticmethod
#     def _circle_area(r):
#         return r ** 2 * math.pi
#
#     @classmethod
#     def margherita(cls):
#         return cls(['cheese', 'tomatoes'])
#
#     @classmethod
#     def pepperoni(cls):
#         return cls(['cheese', 'pepperoni'])
#
#
# p = Pizza(4.5, ['cheese', 'balls'])
# print p.__repr__()

dic = {
    'helo': 1,
    'poop': 2
}

for value in dic:
    if dic[value] > 1:
        print value
