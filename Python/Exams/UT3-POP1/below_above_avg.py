# ***********************************
# POR ENCIMA Y POR DEBAJO DE LA MEDIA
# ***********************************


def run(marks: list) -> tuple:
    copy_marks = marks.copy()
    avg = sum(copy_marks) / len(copy_marks)
    below_avg = [mark for mark in marks if mark <= avg]
    above_avg = [mark for mark in marks if mark > avg]

    return below_avg, above_avg


if __name__ == '__main__':
    run([3.7, 1.2, 9.5, 4.7, 6.3, 7.2, 3.8, 1.1, 1.4])
