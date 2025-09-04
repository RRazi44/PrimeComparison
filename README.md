# 📊 PrimeComparison

## Description

This project contains 3 programs to generate the primary number less than 1,000,000 each one write in differents programming langage : **Python**, **C** and **Java**.

The Python script `timer.py` measures the execution time for each program and saves the result on a CSV file called ``result.csv`` 


**Important :** This project does not aim to determine which programming langage is the fastest in general. The benchmark only measures how long this specific algorithm takes to run on a single computer.



## 🚀 Installation

Clone the repository: ``git clone git@github.com:RRazi44/PrimeComparison.git``

Make sure you have:

- **Python 3**

- **gcc** (for compiling the C program)

- **Java (JDK)** 



## 🛠️ Usage

Once you've installed the JDK, python and GCC, you can compile the Java and C programs:

```bash
cd Java
javac Main.java
cd ..
gcc Main.c -o Main.exe
cd ..
```

And to run the benchmark : 

```bash
python timer.py
```

This will execute each prime generators, measure their execution time and save the result into ``result.csv``



## 📈 Example



|            | Python             | C                  | Java               |
| ---------- | ------------------ | ------------------ | ------------------ |
| ATTEMPT #0 | 31.169610199998715 | 3.407364899998356  | 2.471721999998408  |
| ATTEMPT #1 | 31.039752299999236 | 3.400814699998591  | 2.4700040999996418 |
| ATTEMPT #2 | 30.793680199996743 | 3.410284800000227  | 2.4829213000011805 |
| ATTEMPT #3 | 32.03145790000053  | 3.4910879000017303 | 2.5165514000000258 |
| ATTEMPT #4 | 30.87469599999895  | 3.4244922999969276 | 2.545394500000839  |
| ATTEMPT #5 | 30.898460100001103 | 3.4003772999967623 | 2.4979984999990847 |
| ATTEMPT #6 | 31.50986379999813  | 3.4027415000018664 | 2.4692340000001423 |
| ATTEMPT #7 | 31.08279080000284  | 3.4086365999974078 | 2.4511353999987477 |
| ATTEMPT #8 | 31.356230500001402 | 3.403519600000436  | 2.4682782999989286 |
| ATTEMPT #9 | 30.684617200000503 | 3.401648999999452  | 2.467576299997745  |
|            |                    |                    |                    |
| AVERAGE:   | 31.144115899999814 | 3.4150968599991756 | 2.4840815799994744 |
