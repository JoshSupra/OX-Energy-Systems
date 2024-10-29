# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:19:20 2024

@author: jjmcc
"""
#Create a class for solar panels
    #Allow for calculation of area of solar panel
    #Attributes - length, width, kWp
#Create a class for buildings and roofs
    #Allow for calculation of area of roof
    #Attributes - length, width, roof angle
#Calculate amount of panels per side and multiply by two
import math

class Building():
    def __init__(self, name, length, width, angle):
        self.name = name
        self.length = length
        self.width = width
        self.angle = angle
        self.roof_width = (self.width/2)/math.cos(self.angle*(math.pi/180))   
        
class Panel():
    def __init__(self, model_name, pv_length, pv_width, pv_power):
        self.model_name = model_name
        self.length = pv_length
        self.width = pv_width
        self.power = pv_power

def panel_calculate(roof_length, panel_length, roof_width, panel_width, power):
    length_ratio = int(roof_length/panel_length)
    width_ratio = int (roof_width/panel_width)
    panel_number = length_ratio*width_ratio*2
    total_capacity = panel_number * power
    return(panel_number, total_capacity)

      
building_name = input("Please provide the name of the building. ")
building_length = int(input("Please provide a value for the length of the building in metres."))               
building_width = int(input("Please provide a value for the width of the building in metres."))
building_angle = int(input("Please input the angle of the roof in degrees. "))
Building1 = Building(building_name, building_length, building_width, building_angle) 

pv_name = input("Please provide the model name of the panel.") 
panel_length = int(input("Please provide the length of the panel in mm."))/1000
panel_width = int(input("Please provide the width of the panel in mm."))/1000
panel_power = int(input("Please provide the peak power rating of the panel in W."))/1000
Panel1 = Panel(pv_name, panel_length, panel_width, panel_power)

panel_number, total_capacity = panel_calculate(Building1.length, Panel1.length, Building1.roof_width, Panel1.width, Panel1.power)

print("The maximum number of panels is {} and the peak power capacity is {} kWp".format(panel_number,total_capacity))
