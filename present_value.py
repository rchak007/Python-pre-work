#!/usr/bin/python3 

import sys

def main():
    # present_value future_value interest no_comp years - 4 arguments
    # PV = FV / [1+(i/n)]^(n*t)
    # Where FV is the future value, PV is the past value, i is the interest rate, 
    # n is the number of compounding periods within a year, and t is the number of years
    # python present_value.py 10000 10 1 5

    print (sys.argv)
    if len(sys.argv) == 5:    
        future_value = int( sys.argv[1] )
        interest = int( sys.argv[2]  )
        no_comp = int( sys.argv[3] )
        years = int( sys.argv[4] )
        print ('Future Value = ', future_value, 'Interest % = ', interest, 'Number of Compounding periods in a year = ', no_comp, 'Years  = ', years)
        second_part = 1 + ( ( interest / 100 ) / no_comp ) 
        print('second part', second_part)
        third_part = no_comp * years
        print('3rd part =  ', third_part)
        exp =  second_part ** third_part
        print('exp = ',  exp)
        present_value = future_value / ( exp)
        print('Present value = ', present_value)
    else:
        print('incorrect usage - present_value.py future_value interest no_comp years - 5 arguments')
       




# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()