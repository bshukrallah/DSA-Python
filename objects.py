class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie_one = Cookie("Green")
cookie_two = Cookie("Red")

print(cookie_one.get_color())
print(cookie_two.get_color())
cookie_two.set_color("Orange")
print(cookie_two.get_color())

x = 2
y = 2


print(str(id(x)) + " " + str(x))
print(str(id(y)) + " " + str(y))

y = 4
print(str(id(y)) + " " + str(y))