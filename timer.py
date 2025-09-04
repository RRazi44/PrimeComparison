import subprocess
import time
import os

def java_time():
    if os.path.exists("primaryNumber.txt"):
        os.remove("primaryNumber.txt")
    start = time.perf_counter()
    subprocess.run("java -cp Java Main", shell=True, stdout=open("primaryNumber.txt", "a"))
    end = time.perf_counter()
    print(end - start)

def c_time():
    if os.path.exists("primaryNumber.txt"):
        os.remove("primaryNumber.txt")
    start = time.perf_counter()
    subprocess.run(r"C\main.exe", shell=True, stdout=open("primaryNumber.txt", "a"))
    end = time.perf_counter()
    print(end - start)

def python_time():
    if os.path.exists("primaryNumber.txt"):
        os.remove("primaryNumber.txt")
    start = time.perf_counter()
    subprocess.run(["python", "main.py"], cwd="Python", stdout=open("primaryNumber.txt", "a"))
    end = time.perf_counter()
    print(end - start)

print("Java:")
for _ in range(10):
    java_time()

print("C:")
for _ in range(10):
    c_time()

print("Python:")
for _ in range(10):
    python_time()
