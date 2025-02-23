from app.solution import (
    find_best_sequence,
    print_sequence,
    read_numbers_from_file,
    save_numbers_to_file,
)


input_file = "file.txt"
output_file = "output.txt"

numbers = read_numbers_from_file(input_file)

if __name__ == "__main__":
    best_sequence = find_best_sequence(numbers)
    print_sequence(best_sequence)
    save_numbers_to_file(output_file, best_sequence)
