# from zipfile import ZipFile
import time
from pathlib import Path

start = time.perf_counter()
# Simple open file
base_dir = Path(__file__).parent
path = base_dir / "fear.txt"

# Example 1
fh = open(path, "rt")  # r: чтение, t: текстовый режим
for line in fh.readlines():
    print(line.strip())  # удалить пробельные символы и вывести
fh.close()

# Read Example 2
fh = open(path, "rt")
try:
    for line in fh.readlines():
        print(line.strip())
finally:
    fh.close()

# Read Example 3
fh = open(path)
# rt — режим по умолчанию
try:
    for line in fh:
        # можно итерироваться напрямую по fh
        print(line.strip())
finally:
    fh.close()

# Read Example 4
with open(path) as fh:
    for line in fh:
        print(line.strip())

# Write Example 1
path = base_dir / "print_example.txt"
with open(path, "w") as fw:
    print("Hey I am printing into a file!!!", file=fw)

# Read Write
path_read = base_dir / "fear.txt"
with open(path_read) as f:
    lines = [line.rstrip() for line in f]

path_write = base_dir / "fear_copy.txt"
with open(path_write, "w") as fw:
    fw.write("\n".join(lines))

# Write to Binary file
path_bin = base_dir / "example.bin"
with open(path_bin, "wb") as fw:
    fw.write(b"This is binary data...")

with open(path_bin, "rb") as f:
    print(f.read())  # prints: b'This is binary data...'

# Write only if file not exist
# path_x = base_dir / "write_x.txt"
# with open(path_x, "x") as fw:  # this succeeds
#     fw.write("Writing line 1")

# Error file exit
# with open(path_x, "x") as fw:  # this fails
#     fw.write("Writing line 2")

# Use Path

p = base_dir / "fear.txt"
print(f"p.is_file(): {p.is_file()}")
# True
path = p.parent.absolute()
print(path)
print(f"path.is_dir(): {path.is_dir()}")

# Show directory content
p = base_dir
for entry in p.glob("*"):
    print("File:" if entry.is_file() else "Folder:", entry)

end = time.perf_counter()
print(f"Elapsed time: {end - start} seconds")

# File Three walking
# p = Path(".")
# for root, dirs, files in p.walk():
#     print(f"{root=}")

#     if dirs:
#         print("Directories:")
#         for dir_ in dirs:
#             print(dir_)
#         print()

#     if files:
#         print("Files:")
#         for filename in files:
#             print(filename)
#         print()


# Zipfile
# with ZipFile("example.zip", "w") as zp:
#     zp.write("content1.txt")
#     zp.write("content2.txt")
#     zp.write("subfolder/content3.txt")
#     zp.write("subfolder/content4.txt")


# with ZipFile("example.zip") as zp:
#     zp.extract("content1.txt", "extract_zip")
#     zp.extract("subfolder/content3.txt", "extract_zip")
