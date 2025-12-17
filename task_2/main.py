from src.decorators import handle_errors
from src.handlers import (
    monte_carlo_simulation,
    check_integral_calculation,
    get_visual_implementation,
)


@handle_errors
def main():
    lower_integral_bound = 0
    upper_intergal_bound = 2
    num_experiments = 25000

    print("Start integral calculation.")

    print("Calculating integral value with Monte-Carlo method...")
    monte_carlo_simulation(
        lower_integral_bound,
        upper_intergal_bound,
        num_experiments,
    )

    print("Calculating integral value with analytic method...")
    check_integral_calculation(lower_integral_bound, upper_intergal_bound)

    print("Drowing the graph.")
    get_visual_implementation(
        lower_integral_bound, upper_intergal_bound, num_experiments
    )

    print("Calculation completed.")


if __name__ == "__main__":
    main()
