# Nested List
if __name__ == '__main__':
    n = int(input().strip())
    students = []
    for _ in range(n):
        name = input().strip()
        score = float(input().strip())
        students.append([name, score])

    lowest_grade = sorted(set([score for name, score in students]))[1]
    names_with_second_lowest_grade = sorted([name for name, score in students if score == lowest_grade])  

    for name in names_with_second_lowest_grade:
        print(name)