def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {"fistname": "Facundo", "lasname": "Garcia"}

    suer_list = [
        {"fistname": "Facundo", "lasname": "Garcia"},
        {"fistname": "Miguel", "lasname": "Torres"},
        {"fistname": "Pepe", "lasname": "Rodelo"},
        {"fistname": "Susana", "lasname": "Martinez"},
        {"fistname": "Jose", "lasname": "Garcia"}
    ]

    super_dict = {
        "naturals_nums": [1, 2, 3],
        "integers_nums": [-1, -2, -3, 0, 1, 2, 3],
        "flootings_nums": [1.1, 2.5, 3.5, 2.1]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()
