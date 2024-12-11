import random

running = False

def mcdonalds_code_bruteforcer():
    """
    This function generates a random typing speed between 100 and 200 words per minute.
    """
    running = True
    while running:
        code = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        print(code)


if __name__ == "__main__":
    mcdonalds_code_bruteforcer()
