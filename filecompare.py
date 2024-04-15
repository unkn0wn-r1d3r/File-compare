def compare_files(file_a_path, file_b_path):
    # Read all lines from both files
    with open(file_a_path, 'r') as file_a:
        lines_a = file_a.readlines()
    with open(file_b_path, 'r') as file_b:
        lines_b = file_b.readlines()

    # Create a dictionary to store lines from file B with line numbers
    lines_b_dict = {line.strip(): idx for idx, line in enumerate(lines_b, 1)}

    # List to store results
    results = []

    # Check each line in file A if it exists in file B
    for idx_a, line_a in enumerate(lines_a, 1):
        line_a = line_a.strip()  # Remove trailing newline
        if line_a in lines_b_dict:
            results.append({
                'line_content': line_a,
                'line_number_a': idx_a,
                'line_number_b': lines_b_dict[line_a]
            })

    # Return the results
    return results


# Example usage
file_a_path = 'file_a.txt'
file_b_path = 'file_b.txt'
matches = compare_files(file_a_path, file_b_path)

# Print the results
for match in matches:
    print(f"Match found: '{match['line_content']}'")
    print(f"  File A Line: {match['line_number_a']}")
    print(f"  File B Line: {match['line_number_b']}\n")
