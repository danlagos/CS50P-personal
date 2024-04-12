"""
Test for 75% Fuel Level
simulate "input of 3/4" expect "75%" failure message "Expected 75% when input is 3/4"

Test for 25% Fuel Level
simulate "input of 1/4" expect "25%" failure message "Expected 25% when input is 1/4"

Test for Full Tank
simulate "input of 4/4" expect "F" failure message "Expected F for full tank when input is 4/4"

Test for Empty Tank
simulate "input of 0/4" expect "E" failure message "Expected E for empty tank when input is 0/4"

Test for Zero Division Error Handling
simulate "input of 4/0" expect "to re-prompt user" failure message "Expected to re-prompt user on zero denominator"

Test for Non-Integer Input Handling
simulate "input of three/four" expect "to re-prompt user" failure message "Expected to re-prompt user on non-integer input"

Test for Decimal Input Handling
simulate "input of 1.5/3" expect "to re-prompt user" failure message "Expected to re-prompt user on decimal input"

Test for Invalid Fraction Input
simulate "input of 5/4" expect "to re-prompt user" failure message "Expected to re-prompt user when numerator is larger than denominator"
"""