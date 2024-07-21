country = input('Introduzca el nombre de un país: ').lower()

match country:
    case 'españa':
        print('🇪🇸')
    case 'italia':
        print('🇮🇹')
    case 'inglaterra':
        print('🏴󠁧󠁢󠁥󠁮󠁧󠁿')
    case 'alemania':
        print('🇩🇪')
    case 'francia':
        print('🇫🇷')
    case 'rusia':
        print('🇷🇺')
    case _:
        print('Todavía no tenemos esa.')
