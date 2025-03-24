import os 


for i in range(1, 26):
    os.makedirs(f"Day {i}", exist_ok=True)
    with open(f"Day {i}/README.md", "w") as f:
        f.write(f"# Day {i}\n\nThis is the README for Day {i}.")
print("Done")
