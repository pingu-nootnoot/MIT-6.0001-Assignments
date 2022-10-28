#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:33:13 2020

@author: pingu
"""

############ Part B: Saving, with a raise ############
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

num_of_month = 0
while current_savings <= total_cost*portion_down_payment:
#    semi = False this has no use!
    if num_of_month%6 == 0 and num_of_month > 0:
        #num of month must > 0 because 0%6 == 0 too
#        semi = True this again has no use!
        current_savings = current_savings*(1+r/12) + annual_salary/12*portion_saved*(1+r/12)
        annual_salary += annual_salary*semi_annual_raise
        #did not work in the beginning because misspelled annual!!!!!
    else:
        current_savings = current_savings*(1+r/12) + annual_salary/12*portion_saved*(1+r/12)
    num_of_month += 1
    #add number after so that it starts with 0
    #the raise will happen when num is 6, which is 7th month
print("Number of months:", num_of_month)