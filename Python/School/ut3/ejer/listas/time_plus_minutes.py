# *****************
# FICHO CUANDO TOCA
# *****************


def run(time: str, offset: int) -> str:
    time_list = [int(num) for num in time.split(':')]

    hours_in_mins = time_list[0] * 60
    mins = time_list[1]
    start_time_mins = hours_in_mins + mins
    final_time_mins = start_time_mins + offset

    if (final_hours := final_time_mins // 60) > 24:
        final_hours = final_hours - 24
    final_mins = final_time_mins % 60

    final_time = f'{final_hours}:{final_mins}'

    return final_time


if __name__ == '__main__':
    run('17:15', 240)
