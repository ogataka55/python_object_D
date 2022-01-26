import math


class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        r_area = self.height * self.width
        return format(r_area, '.2f')  # 小数点第2位まで表示

    def diagonal(self):
        r_dia = math.sqrt((self.height ** 2) + (self.width ** 2))  # mathモジュールの平方根.sqrt()
        return format(r_dia, '.2f')  # 小数点第2位まで表示


# Rectangleクラスのインスタンス化
rectangle1 = Rectangle(height=5, width=6)
rectangle2 = Rectangle(height=3, width=3)

# 高さ5,幅6の長方形
print(f"高さ{rectangle1.height},幅{rectangle1.width}の長方形")
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

# 高さ3,幅3の長方形
print(f"高さ{rectangle2.height},幅{rectangle2.width}の長方形")
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
