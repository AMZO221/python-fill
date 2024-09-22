#creer un fichier
import os
for i in range(3):
    print(os.getcwd())
    os.rmdir(f"new directory {i}")


