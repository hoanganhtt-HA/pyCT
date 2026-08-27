class Student:
    def __init__(self, student_id, name, age, score):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.score = score

    def display(self):
        print(
            f"ID: {self.student_id} | "
            f"Tên: {self.name} | "
            f"Tuổi: {self.age} | "
            f"Điểm: {self.score}"
        )


students = []


def add_student():
    student_id = input("Nhập ID: ")
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm: "))

    student = Student(student_id, name, age, score)
    students.append(student)

    print("Đã thêm sinh viên.")


def show_students():
    if not students:
        print("Danh sách sinh viên trống.")
        return

    print("\n--- DANH SÁCH SINH VIÊN ---")
    for student in students:
        student.display()


def search_student():
    student_id = input("Nhập ID cần tìm: ")

    for student in students:
        if student.student_id == student_id:
            student.display()
            return

    print("Không tìm thấy sinh viên.")


def delete_student():
    student_id = input("Nhập ID cần xóa: ")

    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Đã xóa sinh viên.")
            return

    print("Không tìm thấy sinh viên.")


def main():
    while True:
        print("\n===== QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Hiển thị sinh viên")
        print("3. Tìm sinh viên")
        print("4. Xóa sinh viên")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "0":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")


main()