import pulp


def calculate_max_products():
    model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

    A = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
    B = pulp.LpVariable("Fruit Juice", lowBound=0, cat="Integer")

    model += A + B, "Quantity"  # Objective

    model += 2 * A + B <= 100  # Water constraint
    model += A <= 50  # Sugar constraint
    model += A <= 30  # Lemon juice constraint
    model += 2 * B <= 40  # Mashed fruits constraint

    model.solve()
    print("Status:", pulp.LpStatus[model.status])

    print(f"Number of {A.name}:", int(A.varValue))
    print(f"Number of {B.name}:", int(B.varValue))

    total_products_num = int(A.varValue + B.varValue)
    print("Total max number of products:", total_products_num)

    return total_products_num
