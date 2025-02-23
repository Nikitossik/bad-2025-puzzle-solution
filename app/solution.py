import heapq
from typing import List, Dict, Tuple


def read_numbers_from_file(filename: str) -> List[str]:
    """Returns a list of numbers from file"""

    numbers = []
    try:
        with open(filename, "r") as file:
            for line in file:
                number = line.strip()
                if number.isdigit():
                    numbers.append(number)
    except FileNotFoundError:
        print(f"Please check existance of {filename}")

    return numbers


def save_numbers_to_file(filename: str, numbers: List[str]) -> None:
    """Writes a list of numbers to the file"""
    with open(filename, "w+") as file:
        for number in numbers:
            file.write(number + "\n")


def check_connection(a: str, b: str) -> bool:
    """
    Checks if a and b can be connected
    Examples:
        a = "337989", b = "890062" -> True
        a = "337990", b = "890062" -> False
    """
    return len(a) >= 2 and len(b) >= 2 and a[-2:] == b[:2]


def graphify(numbers: List[str]) -> Dict[str, List[str]]:
    """
    Returns a graph object - dict as { <number>: <list of numbers the 'number' has connections with> }

    Example:
        numbers = ['112233', '332212', '332211']
        result = {
            '112233': ['332212', '332211'],
            '332212': [],
            '332211': ['112233']
        }
    """
    graph: Dict[str, List[str]] = {num: [] for num in numbers}

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and check_connection(numbers[i], numbers[j]):
                graph[numbers[i]].append(numbers[j])

    return graph


def greedy_sequence_from_start(
    graph: Dict[str, List[str]], start_number: str
) -> List[str]:
    """
    Greedy algorithm that finds a sequence of connected numbers starting from <start_number>
    """
    sequence_list: List[str] = [start_number]
    used: set[str] = {start_number}  # Track used numbers to prevent duplicates

    heap: List[Tuple[int, str]] = []
    # Add neighbors to the priority queue (sorted by number of connections)
    for neighbor in graph[start_number]:
        heapq.heappush(
            heap, (-len(graph[neighbor]), neighbor)
        )  # Max heap based on connections

    while heap:
        _, next_number = heapq.heappop(
            heap
        )  # Get the best next number (most connections)

        if next_number in used:
            continue  # Skip already used numbers

        # Checking the connection between numbers
        if check_connection(sequence_list[-1], next_number):
            sequence_list.append(next_number)  # Add number to the sequence
            used.add(next_number)  # Note number as used

            # Add new possible connections
            for neighbor in graph[next_number]:
                if neighbor not in used:
                    heapq.heappush(heap, (-len(graph[neighbor]), neighbor))

    return sequence_list


def find_best_sequence(numbers: List[str]) -> List[str]:
    """
    Finds the longest sequence of connected numbers checking every number as a start
    """
    graph = graphify(numbers)  # connection graph
    best_sequence: List[str] = []

    # Try every number as the starting point and select the best result
    for start in numbers:
        sequence = greedy_sequence_from_start(graph, start)

        if len(sequence) > len(best_sequence):
            best_sequence = sequence

    return best_sequence


def print_sequence(sequence: List[str]) -> None:
    """Prints out a detailed sequence information"""

    if not sequence:
        print("No sequence found!")
        return

    colored_sequence = [
        number
        if idx == len(sequence) - 1
        else number[:-2] + f"\033[44m{number[-2:]}\033[0m"
        for idx, number in enumerate(sequence)
    ]

    sequence_string = colored_sequence.pop(0)

    for number in colored_sequence:
        sequence_string += number[2:]

    print(f"\nHighlighted string sequence: {sequence_string}")
    print(
        f"\nFull sequence elements: {' -> '.join(sequence)}",
    )
