#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:05:09 2020

@author: pingu
"""

############ Part A: House Hunting ############
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

num_of_month = 0
while current_savings <= total_cost*portion_down_payment:
    current_savings = (current_savings + annual_salary/12*portion_saved)*(1+r/12)
    num_of_month += 1
print("Number of months:", num_of_month)