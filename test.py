class Student:
    def __init__(self, maSV, tenSV, mToan, mLy, mHoa):
        self.maSV = maSV
        self.tenSV = tenSV
        self.mToan = mToan
        self.mLy = mLy
        self.mHoa = mHoa

    def mTrungBinh(self):
        return (self.mToan + self.mLy + self.mHoa)/3


s1 = Student(1, "Nguyen Van A", 8, 7, 3)
s2 = Student(2, "Nguyen Van B", 9, 2, 7)
s3 = Student(3, "Nguyen Van C", 7, 1, 8)
s4 = Student(4, "Nguyen Van D", 8, 7, 5)
s5 = Student(5, "Nguyen Van E", 0, 2, 7)
s6 = Student(6, "Nguyen Van F", 7, 4, 8)
s7 = Student(7, "Nguyen Van G", 8, 7, 9)
s8 = Student(8, "Nguyen Van H", 9, 5, 1)
s9 = Student(9, "Nguyen Van I", 7, 5, 4)
s10 = Student(10, "Nguyen Van J", 8, 7, 8)

listStudent = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

# sắp xếp mảng trên theo thứ tự tăng dần của điểm trung bình
# sử dụng thuật toán sắp xếp chọn trực tiếp

# range(start, stop, step)
# len: độ dài của mảng
# i:  = start
for i in range(len(listStudent)):
    min = i
    for j in range(i+1, len(listStudent)):
        if listStudent[min].mTrungBinh() > listStudent[j].mTrungBinh():
            min = j
    listStudent[i], listStudent[min] = listStudent[min], listStudent[i]

# in ra mang sau khi sap xep
for i in range(len(listStudent)):
    print(listStudent[i].maSV, listStudent[i].tenSV,
          listStudent[i].mTrungBinh())
