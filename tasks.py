
'''
-------------------------------------------------------------------------------
# THIS IS THE RESULT OF QUESTION 1 # 
employee_distance_a = int(input()) * 15.62
employee_distance_b = int(input()) * 41.85
employee_distance_c = int(input()) * 32.67
distance_total = employee_distance_b + employee_distance_c + employee_distance_a
print(f"Distance: {distance_total:.2f} miles")
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
# THIS IS THE RESULT OF QUESTION 2 # 
ounces_total = int(input())
tons = ounces_total // 32000
rest = ounces_total % 32000
pounds = rest // 16
ounces = rest % 16

print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces}")
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
# THIS IS THE RESULT OF QUESTION 3 #
various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

index_value = int(input())
element = various_data_types[index_value]
data_type = type(element).__name__
print(f"Element {index_value}: {data_type}")
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
'''
'''
-------------------------------------------------------------------------------
# THIS IS THE RESULT OF QUESTION 4 #
b1 = int(input())
b2 = int(input())
h = int(input())
area_total = ((b1 + b2) / 2) * h


print(f"Trapezoid area: {area_total:.2f} square meters")
-------------------------------------------------------------------------------
'''
'''
# THIS IS THE RESULT OF QUESTION 5 #
in1 = int(input())
in2 = int(input())
in3 = int(input())
in4 = int(input())
in5 = int(input())

print(f"Integer: {in1 + in2 + in3 + in4 + in5}")
print(f"Float: {float(in1) + float(in2) + float(in3) + float(in4) + float(in5)}")
print(f"String: {str(in1) + str(in2) + str(in3) + str(in4) + str(in5)}")
-------------------------------------------------------------------------------
'''
'''
-------------------------------------------------------------------------------

# THIS IS THE RESULT OF QUESTION 6 #
student_id = int(input())
student_id = str(student_id)
print(f"{student_id[0:3]}-{student_id[3:5]}-{student_id[5:9]}")

-------------------------------------------------------------------------------
'''
'''
-------------------------------------------------------------------------------

# THIS IS THE RESULT OF QUESTION 7 #
predef_list = [4,-27,15,33,-10]

input_value = int(input())
max_value = max(predef_list)
result = input_value > max_value
print(f"Greater Than Max? {result}")
-------------------------------------------------------------------------------
'''

