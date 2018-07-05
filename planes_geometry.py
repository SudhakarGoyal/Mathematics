#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 23:46:59 2018

@author: sudhakar
"""
import math 
from linear_algebra import Vector
class planes(object):
    def __init__(self, normal_vector, constant):
# =============================================================================
#         self.coordinates = tuple(coordinates)
#         self.dimension = len(coordinates)
# =============================================================================
         self.normal_vector = normal_vector
         self.constant = constant
    def if_parallel_planes(self,v):
        x1, y1, z1 = self.normal_vector.coordinates
        d1 = self.constant
        x2, y2, z2 = v.normal_vector.coordinates
        d2 = v.constant
        if(round(x1/x2,2) == round(y1/y2,2) and round(x1/x2,2) == round(z1/z2,2) and not round(x1/x2,2) == round(d1/d2,2)):
            return True
        else:
            return False

        
    def if_same_planes(self,v):
        x1, y1, z1 = self.normal_vector.coordinates
        d1 = self.constant
        x2, y2, z2 = v.normal_vector.coordinates
        d2 = v.constant
        print(x1/x2)
        print(y1/y2)
        print (round(z1/z2,2))
        print(d1/d2)
        
        if(round(x1/x2,2) == round(y1/y2,2) and round(x1/x2,2) == round(z1/z2,2) and round(x1/x2,2) == round(d1/d2,2)):
            return True
        else:
            return False
        
    def angle_with(self,v, degrees):
         x1, y1, z1 = self.normal_vector.coordinates
         d1 = self.constant
         x2, y2, z2 = v.normal_vector.coordinates
         d2 = v.constant          
         
         mag1 = round(self.normal_vector.magnitude(),3)
         mag2 = round(v.normal_vector.magnitude(),3)
         den = (round(mag1*mag2, 3))         
         num = round((self.normal_vector.dot(v.normal_vector)),3)
# =============================================================================
#          print(num/den)
# =============================================================================
         
         if(degrees):
             return math.acos(round(num/den,3))*180/math.pi
         else:
             return math.acos(round(num/den,3))
         
# =============================================================================
#         def swap_rows(self,row1,row2):
# =============================================================================
            
     
v1 = planes(normal_vector = Vector([-7.926,8.625,-7.217]), constant = -7.952)
v2 = planes(normal_vector = Vector([-2.642,2.875,-2.404]), constant = -2.443)
print(v1.angle_with(v2,1))        
print(v1.if_same_planes(v2))
print(v1.if_parallel_planes(v2))

        
        