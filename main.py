import os


if __name__ == '__main__':
    for i in range(1, 26):
        os.makedirs(f"Day {i}", exist_ok=True)
        with open(f"Day {i}/README.md", "w") as f:
            f.write(f"# This is the what we learned in Day {i}\n")
    print("Done")
