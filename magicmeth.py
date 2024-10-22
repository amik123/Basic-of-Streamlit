## way 1
# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __add__(self,others):
#         temp_x=self.x+others.x
#         temp_y=self.y+others.y
#         return temp_x,temp_y

    
# v1=Vector(4,5)
# v2=Vector(5,6)
# print(v1+v2)

##way 2
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,others):
        temp_x=self.x+others.x
        temp_y=self.y+others.y
        return Vector(temp_x,temp_y)

    def __str__(self):
        return f"Vector=({self.x},{self.y})"
    
v1=Vector(4,5)
v2=Vector(5,6)
print(v1+v2)