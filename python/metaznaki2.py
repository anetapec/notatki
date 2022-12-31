import re

def run_example():
    matching_example = ["AA-0jB", "AG-klI", "JT-K3f"]
    examples_without_match = ["jK-00", "12567", "a3-798", "dd-tre"]

    pattern6 = re.compile(r"[A-Z][A-Z]-\w\w\w")

    for example in matching_example:
        print(pattern6.findall(example))

    for example in examples_without_match:
        print(pattern6.findall(example))
    print("^" * 20)
    pattern7 = re.compile(r"[A-Z]{2}-\w{3}")

    for example in matching_example:
        print(pattern7.findall(example))

    for example in examples_without_match:
        print(pattern7.findall(example))






if __name__ == '__main__':
    run_example()
