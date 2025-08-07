def get_vat_rate(task: str):
    reduced_vat_tasks = ["wall_painting", "tiles_removal"]
    return 0.055 if task in reduced_vat_tasks else 0.20
