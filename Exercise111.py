#فایل نمرات
class Grade:
    def __init__(self, stu_id: int, crc_code: int, score: float) -> None:
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:
    def set_file(self, address: str) -> None:
        self.address = address

    def load(self, line_number: int) -> Grade:
        with open(self.address,'r') as files:
            get_info = files.readlines()
            if line_number > len(get_info):
                return None
            else:
                list_info = get_info[line_number -1].split()
                stu_id = list_info[0]
                src_code = list_info[1]
                score = list_info[2]
                grade = Grade(int(stu_id),int(src_code),float(score))
                return grade
                
        
    def calc_student_average(self, student_id: int) -> float:
        with open(self.address,'r') as files:
            list_files = files.readlines()
            final_list = [file.split() for file in list_files]
            sum_number = [float(line[2]) for line in final_list if int(line[0]) == student_id]
            return sum(sum_number) / len(sum_number)

    def calc_course_average(self, course_code: int) -> float:
        with open(self.address,'r') as files:
            list_files = files.readlines()
            final_list = [file.split() for file in list_files]
            sum_number = [float(line[2]) for line in final_list if int(line[1]) == course_code]
            return sum(sum_number) / len(sum_number)

    def count(self) -> int:
        with open(self.address,'r') as files:
            list_files = files.readlines()
            return len(list_files)

    def save(self, grade: Grade) -> None:
        new_line = f"\n{grade.student_id} {grade.course_code} {grade.score}"
        with open(self.address,'r') as files:
            list_files = files.readlines()
            final_list = [file.split() for file in list_files]
            check_student = [1 for file in final_list if int(file[0]) == grade.student_id and float(file[2]) == grade.score]
            if not check_student:
                with open(self.address,'+a') as file:
                    file.write(new_line)


path = './sample_scores.txt'
course = CourseUtil()
course.set_file(path)
grade = Grade(987987987,124,18.5)
course.save(grade)

