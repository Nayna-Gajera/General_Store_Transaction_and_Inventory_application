import xlrd


class Student:
    def __init__(self, id, name, math, science, hindi, marathi, english, ss, computer, evs, eco, gk, result, counter):
        self.id = id
        self.name = name
        self.math = math
        self.science = science
        self.hindi = hindi
        self.marathi = marathi
        self.english = english
        self.ss = ss
        self.computer = computer
        self.evs = evs
        self.eco = eco
        self.gk = gk
        self.result = result
        self.counter = counter


location = xlrd.open_workbook(r'C:\Users\018810569\Students.xlsx')
sheet_1 = location.sheet_by_index(0)
sheet_2 = location.sheet_by_index(1)
student_list = []
qualified = []
disqualified = []
for i in range(1, sheet_1.nrows):
    cnt = 0
    for j in range(2, 12):
        if sheet_1.cell_value(i, j) == "Y":
            cnt += 1

    record = Student(str(sheet_1.cell_value(i, 0)), str(sheet_1.cell_value(i, 1)), str(sheet_1.cell_value(i, 2)),
                     str(sheet_1.cell_value(i, 3)), str(sheet_1.cell_value(i, 4)), str(sheet_1.cell_value(i, 5)),
                     str(sheet_1.cell_value(i, 6)), str(sheet_1.cell_value(i, 7)), str(sheet_1.cell_value(i, 8)),
                     str(sheet_1.cell_value(i, 9)), str(sheet_1.cell_value(i, 10)), str(sheet_1.cell_value(i, 11)),
                     0, cnt)
    if cnt < 8:
        disqualified.append(record)
    else:
        totalMarks = 0
        for k in range(1, sheet_2.nrows):
            if int(sheet_1.cell_value(i, 0)) == int(sheet_2.cell_value(k, 0)):
                if record.math == "Y":
                    totalMarks = totalMarks + int(sheet_2.cell_value(k, 2))
                if record.science == "Y":
                    totalMarks = totalMarks + int(sheet_2.cell_value(k, 3))
                if record.hindi == "Y":
                    totalMarks = totalMarks + int(sheet_2.cell_value(k, 4))
                if record.marathi == "Y":
                    totalMarks = totalMarks + int(sheet_2.cell_value(k, 5))
                if record.english == "Y":
                    totalMarks = totalMarks + int(sheet_2.cell_value(k, 6))
                if record.ss == "Y":
                    totalMarks = totalMarks + int(sheet_2.cell_value(k, 7))
                if record.computer == "Y":
                    totalMarks = totalMarks + int(sheet_2.cell_value(k, 8))
                if record.evs == "Y":
                    totalMarks = totalMarks + int(sheet_2.cell_value(k, 9))
                if record.eco == "Y":
                    totalMarks = totalMarks + int(sheet_2.cell_value(k, 10))
                if record.gk == "Y":
                    totalMarks = totalMarks + int(sheet_2.cell_value(k, 11))

                result = int(totalMarks/record.counter)
                record.result = result
                if result > 75:
                    qualified.append(record)
                else:
                    disqualified.append(record)

for i in qualified:
    print(str(i.name), i.result)

for j in disqualified:
    print(j.name)


