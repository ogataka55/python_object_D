import math


class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        s_area = self.side ** 2
        return format(s_area, '.2f')  # 小数点第2位まで表示

    def diagonal(self):
        s_dia = math.sqrt((self.side ** 2) + (self.side ** 2))  # mathモジュールの平方根.sqrt()
        return format(s_dia, '.2f')  # 小数点第2位まで表示


# Squareクラスのインスタンス化
square1 = Square(side=1.5)
square2 = Square(side=15)

# 一辺1.5の正方形
print(f"一辺{square1.side}の正方形")
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

# 高さ3,幅3の長方形
print(f"一辺{square1.side}の正方形")
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
