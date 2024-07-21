MILENIUM_DIGITS = '20'

year = input('Introduzca los dos últimos dígitos de un año: ')
month = input('Introduzca un mes: ')
day = input('Introduzca un día: ')

date = f'{month}/{day}/{year}'
date_list = date.split('/')

new_year_format = MILENIUM_DIGITS + date_list.pop()
date_list.append(new_year_format)

better_date = '-'.join(date_list)
print(f'{date} --> {better_date}')
