'''
# Question 1
### Task:

Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site.
Output the total distance traveled to two decimal places given the following miles per employee commute to the job site.
Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:
- Employee A: 15.62 miles
- Employee B: 41.85 miles
- Employee C: 32.67 miles

The solution output should be in the format
```
Distance: total_miles_traveled miles
```

---

### Sample Input/Output:

If the input is

```
1
2
3
```

then the expected output is

Distance: 197.33 miles
'''
'''
--------------------------------------------------------------
# THIS IS THE RESULT OF QUESTION 1 # 
employee_distance_a = int(input()) * 15.62
employee_distance_b = int(input()) * 41.85
employee_distance_c = int(input()) * 32.67
distance_total = employee_distance_b + employee_distance_c + employee_distance_a
print(f"Distance: {distance_total:.2f} miles")
--------------------------------------------------------------
'''

'''
# Question 2

### Task:

Create a solution that accepts an integer input representing any number of ounces.
Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value.
There are 16 ounces in a pound and 2,000 pounds in a ton.
The solution output should be in the format.
```
Tons: value_1
Pounds: value_2
Ounces: value_3
```
---
### Sample Input/Output:
If the input is
```
32035
```
then the expected output is
```
Tons: 1
Pounds: 2
Ounces: 3
```
```
#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

```
'''
'''
--------------------------------------------------------------
# THIS IS THE RESULT OF QUESTION 2 # 
ounces_total = int(input())
tons = ounces_total // 32000
rest = ounces_total % 32000
pounds = rest // 16
ounces = rest % 16

print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces}")
--------------------------------------------------------------

'''