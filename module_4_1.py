from fake_math import divide as false
from true_math import divide as true

result1 = false(69, 3)
result2 = false(3, 0)
result3 = true(49, 7)
result4 = true(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)