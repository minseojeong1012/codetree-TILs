class Student:
    num = 1 #\ 클래스\ 변수

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.num = Student.num #\ 클래스\ 변수 num의 값을 인스턴스 변수 num에 대입

        Student.num += 1 #\ 클래스\ 변수 num의 값을 1 증가

n = int(input())

students = [Student(*tuple(map(int, input().split()))) for _ in range(n)]

students.sort(key=lambda x: (-x.height, -x.weight, x.num))

for student in students:
    print(student.height, student.weight, student.num)