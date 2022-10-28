#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:21:14 2020

@author: pingu
"""

############ Part C: Finding the right amount to save away ############
annual_salary = float(input("Enter the starting salary: "))

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
current_savings = 0
num_of_month = 0
steps = 0
epsilon = 100
low = 0
high = 10000
best_savings_rate = (low + high)/2

while num_of_month < 36:
    if num_of_month%6 == 0 and num_of_month > 0:
        current_savings = current_savings*(1+r/12) + annual_salary/12*(1+r/12)
        annual_salary += annual_salary*semi_annual_raise
    else:
        current_savings = current_savings*(1+r/12) + annual_salary/12**(1+r/12)
    num_of_month += 1
#print("Total amount if saved 100% salary:", current_savings)
if current_savings < total_cost*portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    while abs(current_savings*best_savings_rate/10000 - total_cost*portion_down_payment) > epsilon:
        if current_savings*best_savings_rate/10000 > total_cost*portion_down_payment:
            high = best_savings_rate
        else:
            low = best_savings_rate
        best_savings_rate = (low + high)/2
        steps += 1
    print("Best savings rate:", int(best_savings_rate)/10000)
    print("Steps in bisection search:", steps)

