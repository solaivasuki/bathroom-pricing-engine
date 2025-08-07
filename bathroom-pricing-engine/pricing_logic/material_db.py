def get_material_cost(task: str, city: str = "default"):
    base_prices = {
        "tiles_removal": 10,
        "plumbing_shower": 100,
        "toilet_replacement": 150,
        "vanity_installation": 200,
        "wall_painting": 50,
        "floor_tiling": 80,
    }
    city_multiplier = 1.0
    if city.lower() == "marseille":
        city_multiplier = 0.95
    elif city.lower() == "paris":
        city_multiplier = 1.2
    return base_prices.get(task, 0) * city_multiplier
