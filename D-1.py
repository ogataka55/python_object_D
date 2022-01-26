import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        c_area = (self.radius ** 2) * math.pi  # mathモジュールの円周率π
        return format(c_area, '.2f')  # 小数点第2位まで表示

    def perimeter(self):
        c_peri = (self.radius * 2) * math.pi  # mathモジュールの円周率π
        return format(c_peri, '.2f')  # 小数点第2位まで表示


# Circleクラスのインスタンス化
circle1 = Circle(radius=1)
circle3 = Circle(radius=3)

# 半径1の円
print(f"半径{circle1.radius}の円")
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
print(f"半径{circle3.radius}の円")
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
