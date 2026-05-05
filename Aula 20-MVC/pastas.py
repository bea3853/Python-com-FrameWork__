import os

p = input("Projeto: ")

for d in ["controllers", "services", "repositories", "models"]:
    os.makedirs(f"{p}/app/{d}", exist_ok=True)
    open(f"{p}/app/{d}/__init__.py", "w").close()

open(f"{p}/app/__init__.py", "w").close()
