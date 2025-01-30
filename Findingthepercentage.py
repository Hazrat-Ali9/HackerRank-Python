# Finding The Percentage

if __name__ == '__main__':
    n = int(input())  
    student_record = {}  


    for _ in range(n):
        line = input().split()
        name, marks = line[0], list(map(float, line[1:]))
        student_record[name] = marks
    query_name = input()  
    average_score = sum(student_record[query_name]) / len(student_record[query_name])
    print("{:.2f}".format(average_score))

