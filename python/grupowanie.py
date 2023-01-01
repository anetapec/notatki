import re


def run_example():
    matching_example = ["00-000", "27-600", "33-100"]
    examples_without_match = ["00-00", "12567", "a3-798", "dd-tre"]

    pattern = re.compile(r"(\d{2})-(\d{3})")

    for example in matching_example:
        print(pattern.findall(example))

    for example in examples_without_match:
        print(pattern.findall(example))

if __name__ == '__main__':
    run_example()