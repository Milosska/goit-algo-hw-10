from src.decorators import handle_errors
from src.handlers import calculate_max_products


@handle_errors
def main():
    calculate_max_products()


if __name__ == "__main__":
    main()
