from pathlib import Path

p1 = Path("new-demo-file.txt")
print(type(p1))

if not p1.exists():
    with open(p1, 'w') as file:
        file.write("I am a new file")
        file.write("Not anymore :-(")

print(p1.name)
print(p1.stem)
print(p1.suffix)

p2 = Path("new-test-dir")
print(list(p2.iterdir()))
