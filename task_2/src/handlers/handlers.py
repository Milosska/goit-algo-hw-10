import random
import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np


def get_integral_value(value: float) -> float:
    """Base function for integral calculation."""
    return value**2


def get_integral_value_np(x: np.ndarray) -> np.ndarray:
    """Base function for integral calculation graph."""
    return x**2


def check_integral_calculation(
    lower_bound: float,
    upper_bound: float,
) -> list[float]:
    """Makes analytic intergal calculation using scipy library."""
    result, error = spi.quad(get_integral_value, lower_bound, upper_bound)

    print(
        f"Analytic integral result from {lower_bound} to {upper_bound}"
        f"is {result} with error {error}."
    )
    return [result, error]


def is_under_curve(lower_bound: float, upper_bound: float, x: float, y: float) -> bool:
    """Checks if thr point (x, y) is under the curve y = x^2."""
    return lower_bound <= x <= upper_bound and 0 <= y <= get_integral_value(x)


def monte_carlo_simulation(
    lower_bound: float,
    upper_bound: float,
    num_experiments: int,
) -> float:
    """Monte-Carlo simulation for integral calculation."""
    points = [
        (
            random.uniform(lower_bound, upper_bound),
            random.uniform(0, get_integral_value(upper_bound)),
        )
        for _ in range(num_experiments)
    ]

    under_points = [
        point
        for point in points
        if is_under_curve(lower_bound, upper_bound, point[0], point[1])
    ]

    points_under_curve = len(under_points)
    points_total = len(points)
    rectangle_area = (upper_bound - lower_bound) * get_integral_value(upper_bound)

    integral_area = points_under_curve / points_total * rectangle_area

    print(
        f"Monte-Carlo integral result from {lower_bound} to {upper_bound} is {integral_area}."
    )

    return integral_area


def get_visual_implementation(lower_bound: float, upper_bound: float, num_points: int):
    """Visual implementation of the integral calculation."""
    # Генеруємо випадкові точки
    xs = np.random.uniform(lower_bound, upper_bound, num_points)
    ys = np.random.uniform(0, get_integral_value(upper_bound), num_points)

    # Розділяємо точки
    under_x = []
    under_y = []
    over_x = []
    over_y = []

    for x, y in zip(xs, ys):
        if is_under_curve(lower_bound, upper_bound, x, y):
            under_x.append(x)
            under_y.append(y)
        else:
            over_x.append(x)
            over_y.append(y)

    # Будуємо криву
    x_curve = np.linspace(lower_bound, upper_bound, 400)
    y_curve = get_integral_value_np(x_curve)

    fig, ax = plt.subplots(figsize=(8, 6))

    # Крива
    ax.plot(x_curve, y_curve, color="red", linewidth=3, label="y = x²")

    # Точки
    ax.scatter(
        under_x, under_y, color="green", s=10, alpha=0.6, label="Under the curve"
    )
    ax.scatter(over_x, over_y, color="blue", s=10, alpha=0.6, label="Over the curve")

    # Межі інтегрування
    ax.axvline(x=lower_bound, color="gray", linestyle="--")
    ax.axvline(x=upper_bound, color="gray", linestyle="--")

    # Прямокутник інтегрування
    ax.set_xlim(lower_bound - 0.2, upper_bound + 0.2)
    ax.set_ylim(0, get_integral_value(upper_bound) + 0.5)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Monte-Carlo simulation for integral calculation y = x²")
    ax.legend()
    ax.grid(True)

    plt.show()
