import os
import csv
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "runtime_results.csv")
output_path = os.path.join(BASE_DIR, "runtime_graph.png")

sizes = []
times = []

with open(csv_path, "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sizes.append(int(row["input_size"]))
        times.append(float(row["runtime_seconds"]))

plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker="o")
plt.xlabel("Input Size (n)")
plt.ylabel("Runtime (seconds)")
plt.title("HVLCS Runtime")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_path, dpi=200)
plt.show()

print(f"Graph saved to: {output_path}")