import os

print("Enter your folder name to add to documents: ")
newDir = input()
print("Enter the number of chapters + 1 (16 chapters would be 17): ")
ch_Num = input()
ch_Num = int(y)


dirs = range(1, ch_Num)
parent_dir = f"/Documents/{newDir}"

for dir in dirs:
    new_dir = ('Chapter' + str(dir))
    path = os.path.join(parent_dir, new_dir)
    os.makedirs(path)
    print(f"Directory {new_dir} created successfully")
