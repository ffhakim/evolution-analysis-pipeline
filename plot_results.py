import sys
import matplotlib.pyplot as plt

# Check for filename
if len(sys.argv) < 2:
    print("Usage: python3 plot_results.py <results_file>")
    sys.exit(1)

filename = sys.argv[1]

# Counters
count_success = 0 # Contains Z
count_stop = 0    # Truncated by *
count_total = 0

print(f"Reading {filename}...")

with open(filename, "r") as f:
    for line in f:
        # We look for the ">>>" lines we printed in the analysis script
        if ">>> SUCCESS" in line:
            count_success += 1
        elif ">>> NOTE" in line:
            count_stop += 1

count_total = count_success + count_stop

print(f"Total sequences analyzed: {count_total}")
print(f"Success (Z): {count_success}")
print(f"Stopped (*): {count_stop}")

# --- PLOTTING ---
labels = ['Incorporated (Z)', 'Truncated (*)']
counts = [count_success, count_stop]
colors = ['green', 'red']

plt.figure(figsize=(8, 6))
plt.bar(labels, counts, color=colors)
plt.title(f'Non-Natural Amino Acid Incorporation\n({filename})')
plt.ylabel('Number of Sequences')

# Save the plot as an image
output_img = filename.replace(".txt", ".png")
plt.savefig(output_img)
print(f"Graph saved to {output_img}")