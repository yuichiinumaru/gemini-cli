import os
import sys

def get_conflict_files():
    output = os.popen("jj status --no-pager").read()
    files = []
    for line in output.split('\n'):
        if '2-sided conflict' in line:
            parts = line.split()
            # usually: path/to/file 2-sided conflict
            f = parts[0]
            if '__snapshots__' not in f:
                files.append(f)
    return files

for f in get_conflict_files():
    if not os.path.exists(f): continue
    print(f"\n--- {f} ---")
    in_conflict = False
    with open(f, 'r') as file:
        for i, line in enumerate(file.readlines()):
            if line.startswith('<<<<<<<'):
                in_conflict = True
                print(f"L{i+1}: {line.strip()}")
            elif in_conflict:
                print(f"L{i+1}: {line.strip()}")
                if line.startswith('>>>>>>>'):
                    in_conflict = False
                    print("-" * 20)
