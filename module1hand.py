
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades0 = [5, 3, 3, 5, 4]
grades1 = [2, 2, 2, 3]
grades2 = [4, 5, 5, 2]
grades3 = [4, 4, 3]
grades4 = [5, 5, 5, 4, 5]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
res = sorted(students)
print(res)
students0 = 'Aaron'
students1 = 'Bilbo'
students2 = 'Johnny'
students3 = 'Khendrik'
students4 = 'Steve'
result = {}
result[students0] = sum(grades[0]) / len(grades[0])
result[students1] = sum(grades[1]) / len(grades[1])
result[students2] = sum(grades[2]) / len(grades[2])
result[students3] = sum(grades[3]) / len(grades[3])
result[students4] = sum(grades[4]) / len(grades[4])
print(result)








