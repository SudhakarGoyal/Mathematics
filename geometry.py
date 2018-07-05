#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 19:18:18 2018

@author: sudhakar
"""

from linear_algebra import Vector
import math
class Line(object):
# =============================================================================
#     def __init__(self, normal_vector = None, constant_term = None):   # taking normal vector to the line and constant term of the line's equation
# =============================================================================
# =============================================================================
#         self.dimension = 2
#         
#         if not normal_vector:
#             all_zeros = [0]*self.dimension
#             normal_vector = Vector(all_zeros)
#             self.normal_vector = normal_vector  
#             
#         if not constant_term:
#             constant_term = 0
#             self.constant_term = constant_term
# =============================================================================
            
    def __init__(self, coordinates):
        self.coordinates = tuple(coordinates)
        self.dimension = len(coordinates)
        
    def if_same_lines(self,v):
        x1,y1,c1 = self.coordinates
        x2,y2,c2 = v.coordinates
        print(round((y1/y2),2))
        
        if (round((x1/x2),2) == round((y1/y2),2) and round((x1/x2),2) == round((c1/c2),2)):
            return True
        else:
            return False
    
    def intersection(self,v):
        try:
            x1, y1,c1  = self.coordinates
            x2, y2 ,c2= v.coordinates      
            pt_intersection =  [(y2*c1 - y1*c2)/(x1*y2 - y1*x2), (x1*c2 - x2*c1)/((x1*y2 - y1*x2))]
            return pt_intersection
        
        except ZeroDivisionError:
            if(self.if_same_lines(v)):
                return self
            else:
                return None    
   

    def if_parallel_lines(self,v):
        x1,y1,c1 = self.coordinates
        x2,y2,c2 = v.coordinates
        if (-1*x1/y1 == -1*x2/y2 ):
            return True
        else:
            return False
        
    def if_perpendicular_lines(self,v):
        x1,y1,c1 = self.coordinates
        x2,y2,c2 = v.coordinates
        if (-1*x1/y1 == y2/x2 ):
            return True
        else:
            return False      
        
    def angle_with(self,v, degrees):
        x1,y1,c1 = self.coordinates
        x2,y2,c2 = v.coordinates
        m1 = -y1/x1
        m2 = -y2/x2
        if(degrees):
            return round((math.atan2((m1-m2),1+m1*m2))*180/math.pi,3)
        else:
            return round(math.atan2((m1-m2),1+m1*m2),3)
    
v1 = Line([1,1,0])
v2 = Line([-2,2,0])
print(v1.intersection(v2))
print(v1.if_same_lines(v2))
print(v1.angle_with(v2,1))
print(v1.if_perpendicular_lines(v2))
