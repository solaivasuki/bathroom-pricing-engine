def get_labor_cost(task: str, area: float):
    labor_rates = {
        "tiles_removal": (1, 25),
        "plumbing_shower": (3, 30),
        "toilet_replacement": (2, 28),
        "vanity_installation": (2, 30),
        "wall_painting": (1, 20),
        "floor_tiling": (2, 25),
    }
    hours, rate = labor_rates.get(task, (1, 20))
    return hours * rate, hours
