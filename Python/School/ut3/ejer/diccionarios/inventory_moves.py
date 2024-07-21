# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    inventory = {}
    inventory_items = imoves.split(',')
    for item in inventory_items:
        ikey = item[0]
        ival = int(item[1:])
        if ikey in inventory:
            inventory[ikey] += ival
        else:
            inventory[ikey] = ival

    return inventory


if __name__ == '__main__':
    run('A1,B4,A-2,A7,B1,C4')
