# ******************
# POBLACIÓN PROMEDIO
# ******************


def run(pdata: dict) -> dict:
    avg_data = pdata.copy()
    world_pop = sum(avg_data.values())
    for city in avg_data:
        avg_data[city] = round(pdata[city] / world_pop * 100, 3)

    return avg_data


if __name__ == '__main__':
    run({'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000})
