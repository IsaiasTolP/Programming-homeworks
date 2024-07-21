# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/avg_temps/avg_temps.dat'
    f_input = open(input_path)

    monthly_avg_temp = []
    for line in f_input:
        monthly_temps = [int(temp) for temp in line.strip().split(',')]
        month_days = len(monthly_temps)
        avg_temp = round(sum(monthly_temps) / month_days, 2)
        monthly_avg_temp.append(str(avg_temp))
    f_input.close

    with open(output_path, 'w') as f_output:
        for temp in monthly_avg_temp:
            f_output.write(temp + '\n')

    return filecmp.cmp(output_path, 'data/avg_temps/.expected', shallow=False)


if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')
