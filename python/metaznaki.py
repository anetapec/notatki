import re

text = "Ala ma kota, kot jest wesoły "
patern = re.compile(r"kot")

print(patern.findall(text))

text1 = "Ala ma kota, nazywa się Mruczek i jest bardzo wesołym zwierzakiem"
pattern = re.compile(r"[abc]")
pattern2 = re.compile(r"[abc.]")
pattern3 = re.compile(r"[^a]")
pattern4 = re.compile(r"[a-c]")
pattern5 = re.compile(r"[a-zA-Z]")
print(pattern5.findall(text1))
print(pattern4.findall(text1))

def run_example():
    matching_example = ["00-000", "27-600", "33-100"]
    examples_without_match = ["00-00", "12567", "a3-798", "dd-tre"]

    pattern6 = re.compile(r"\d\d-\d\d\d")

    for example in matching_example:
        print(pattern6.findall(example))

    for example in examples_without_match:
        print(pattern6.findall(example))
    print("*" * 10)

#za pomocą liczby powtórzeń

    matching_example1 = ["00-000", "27-600", "33-100"]
    examples_without_match1 = ["00-00", "12567", "a3-798", "dd-tre"]

    pattern7 = re.compile(r"\d{2}-\d{3}")

    for example in matching_example1:
        print(pattern7.findall(example))

    for example in examples_without_match1:
        print(pattern7.findall(example))

if __name__ == '__main__':
    run_example()



