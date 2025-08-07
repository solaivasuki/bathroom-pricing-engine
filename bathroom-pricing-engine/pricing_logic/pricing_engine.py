from labor_calc import get_labor_cost
from material_db import get_material_cost
from vat_rules import get_vat_rate

def calculate_total_cost(task, area, city="default"):
    material_cost = get_material_cost(task, city)
    labor_cost, hours = get_labor_cost(task, area)
    subtotal = material_cost + labor_cost
    vat_rate = get_vat_rate(task)
    vat_amount = subtotal * vat_rate
    total = subtotal + vat_amount

    return {
        "task": task,
        "city": city,
        "area": area,
        "hours": hours,
        "labor_cost": labor_cost,
        "material_cost": material_cost,
        "vat_rate": vat_rate,
        "vat_amount": vat_amount,
        "total_cost": total
    }

# Example usage
if __name__ == "__main__":
    result = calculate_total_cost("wall_painting", area=15, city="Paris")
    for k, v in result.items():
        print(f"{k}: {v}")
