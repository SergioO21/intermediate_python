from data_of_data_filter import DATA

def run():

    # With list and dicts comprehension
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    # With high order functions
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    # ------------------------------------------------------------------------------------
    # If you have a python 3.9, you can write:
    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))

    # ---------- Challenge -----------
    # With list and dicts comprehension
    adults2 = [worker["name"] for worker in DATA if worker["age"] > 18]
    # ------------------------------------------------------------------------
    # If you have a python 3.9, you can write:
    # old_people2 = [worker | {"old": worker["age"] > 70} for worker in DATA]
    old_people2 = [{**worker, **{"old": worker["age"] > 70}} for worker in DATA]

    # With high order functions
    all_python_devs2 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs2 = list(map(lambda worker: worker["name"], all_python_devs2))
    # -----------------------------------------------------------------------------------------
    all_platzi_workers2 = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers2 = list(map(lambda worker: worker["name"], all_platzi_workers2))

    for worker in old_people2:
        print(worker)


if __name__ == '__main__':
    run()
