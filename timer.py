import subprocess
import time
import os

class Triplet:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
def string_for_csv(triplet):
        return str(triplet.a) + "," + str(triplet.b) + "," + str(triplet.c)

def python_time():
    """Calcul time execution of the python program."""
    if os.path.exists("primaryNumber.txt"):
        os.remove("primaryNumber.txt")
    start = time.perf_counter()
    subprocess.run(["python", "main.py"], cwd="Python", stdout=open("primaryNumber.txt", "a"))
    end = time.perf_counter()
    return (end - start)

def c_time():
    """Calcul time execution of the C program."""
    if os.path.exists("primaryNumber.txt"):
        os.remove("primaryNumber.txt")
    start = time.perf_counter()
    subprocess.run(r"C\main.exe", shell=True, stdout=open("primaryNumber.txt", "a"))
    end = time.perf_counter()
    return (end - start)

def java_time():
    """Calcul time execution of the C program."""
    if os.path.exists("primaryNumber.txt"):
        os.remove("primaryNumber.txt")
    start = time.perf_counter()
    subprocess.run("java -cp Java Main", shell=True, stdout=open("primaryNumber.txt", "a"))
    end = time.perf_counter()
    return (end - start)

def create_csv(filename):
    with open("result.csv", "w") as file:
        file.write(",Python,C,Java" + "\n")

def write_data(index, data):
    """Write on csv for the line with data"""
    with open("result.csv", "a") as file:
        file.write(f"ATTEMPT #{index}, {data}" + "\n")
        
def write_line(string):
    """writing the string in the csv"""
    with open("result.csv", "a") as file:
        file.write(string + "\n")

def average(numeric_list):
    sum = 0
    for number in numeric_list:
        sum+=number
    return sum/len(numeric_list)


if __name__ == "__main__":
    python_tab = []
    for _ in range(10):
        python_tab.append(python_time())
        
    c_tab = []
    for _ in range(10):
        c_tab.append(c_time())   

    java_tab = []
    for _ in range(10):
        java_tab.append(java_time())

    create_csv("result.csv")
    for i in range(10):
        write_data(i, string_for_csv(Triplet(python_tab[i], c_tab[i], java_tab[i])))

    write_line(",,,")
    write_line(f"AVERAGE:, {average(python_tab)}, {average(c_tab)}, {average(java_tab)}")
