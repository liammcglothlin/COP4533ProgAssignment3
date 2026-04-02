import random
import time
import subprocess
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOLVE_PATH = os.path.join(BASE_DIR, "src", "solve.py")
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_FILE = os.path.join(BASE_DIR, "runtime_results.csv")

NUM_TESTS = 10
STEP = 25
alphabet = ['a', 'b', 'c', 'd', 'e']


def generate_test(filename, n):
    with open(filename, "w") as f:
        f.write("5\n")
        for ch in alphabet:
            f.write(f"{ch} {random.randint(1, 10)}\n")

        A = ''.join(random.choice(alphabet) for _ in range(n))
        B = ''.join(random.choice(alphabet) for _ in range(n))

        f.write(A + "\n")
        f.write(B + "\n")


def run_tests():
    os.makedirs(DATA_DIR, exist_ok=True)

    results = []

    for i in range(1, NUM_TESTS + 1):
        n = i * STEP
        filename = os.path.join(DATA_DIR, f"test{i}.in")

        generate_test(filename, n)

        start = time.perf_counter()

        with open(filename, "r") as infile:
            subprocess.run(
                [sys.executable, SOLVE_PATH],
                stdin=infile,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )

        end = time.perf_counter()
        runtime = end - start

        print(f"n={n}, time={runtime:.6f} sec")
        results.append((n, runtime))

    return results


def save_results(results):
    with open(RESULTS_FILE, "w") as f:
        f.write("input_size,runtime_seconds\n")
        for n, runtime in results:
            f.write(f"{n},{runtime:.6f}\n")

    print(f"\nSaved results to: {RESULTS_FILE}")


if __name__ == "__main__":
    results = run_tests()
    save_results(results)