from src.create_measurements import main

def create_files():
    initial_size = 1000
    multiplications_value = 10
    max_size = 1_000_000_000

    actual_size = initial_size

    while actual_size <= max_size:
        main(actual_size)
        actual_size = actual_size * multiplications_value

if __name__ == '__main__':
    create_files()