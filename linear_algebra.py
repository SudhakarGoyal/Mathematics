# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math 

class Vector(object):
    def __init__(self, coordinates):
        self.coordinates = tuple(coordinates)
        self.dimension = len(coordinates)
            
    def ifequal(self,v):
        return self.coordinates == v.coordinates
    
    def is_zero(self):
        tolerance = 1e-5
        if(self.magnitude() < tolerance ):
            return True
        else:
            return False
        
    
    def add(self, v):
        new_coordinates = []
        for i in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[i] + v.coordinates[i] )
        return new_coordinates
    
    def subtract(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return new_coordinates
    
    def multiply_scalar(self,v):
        new_coordinates = [v*x for x in self.coordinates]            
        return new_coordinates
        
    def magnitude(self):
        mag = 0
        for i in range(len(self.coordinates)):
            mag+= (self.coordinates[i]**2)
        return mag**0.5
    
    def normalize(self):
        try:
            new_coordinates = [self.multiply_scalar(1/self.magnitude())]
            return new_coordinates
        except ZeroDivisionError:
            raise Exception('Cannot normalize zero vector')
            
    def dot(self,v):
        mag =0
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])  
# =============================================================================
#         for i in range(len(v.coordinates)):
#             mag+=(self.coordinates[i]*v.coordinates[i])
#         return (mag)
# =============================================================================
        
    def angle(self,v, deg):
        if(deg == True):
            return math.acos(self.dot(v)/(self.magnitude()*v.magnitude()))*(180/math.pi)
        else:
            return math.acos(self.dot(v)/(self.magnitude()*v.magnitude()))
        
    def ifparallel(self,v):
        if(self.is_zero() == 1 or v.is_zero()==1 or self.angle(v,1) == 0 or self.angle(v,1) == 180):
            return 1
        else:
            return 0
        
    def iforthogonal(self,v):
        if(self.is_zero() == 1 or v.is_zero()==1 or self.angle(v,1) == 90 or self.angle(v,1) == 270 ):
            return 1
        else:
            return 0
        
    def cross_product(self,v):
        new_coordinates = []
        new_coordinates =[self.coordinates[1]*v.coordinates[2] - self.coordinates[2]*v.coordinates[1],
                          -1*(self.coordinates[0]*v.coordinates[2] - self.coordinates[2]*v.coordinates[0]),
                          self.coordinates[0]*v.coordinates[1] -self.coordinates[1]*v.coordinates[0]]
        return Vector(new_coordinates) 
    
    def area_parallelogram(self,v):
        new_coordinates = self.cross_product(v)
        return new_coordinates.magnitude()
    
    def area_triangle(self,v):
        return 0.5*self.area_parallelogram(v)
                   
                        
    
vec = Vector([1.5,9.547,3.691])    
vec2 = Vector([-6.007,0.124,5.772])


print(vec.ifparallel(vec2))  
print(vec.iforthogonal(vec2))
print(vec.cross_product(vec2))
print(vec.ifequal(vec2))