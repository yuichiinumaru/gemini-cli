import os
import subprocess

def get_conflict_files():
    output = os.popen("jj status --no-pager").read()
    files = []
    for line in output.split('\n'):
        if '2-sided conflict' in line:
            parts = line.split()
            f = parts[0]
            files.append(f)
    return files

conflicts = get_conflict_files()

auto_resolve_upstream = [
    '__snapshots__', '.snap', '.svg', '.eval.ts', 'integration-tests', 
    'test.', '.test.', 'schemas/'
]

for f in conflicts:
    if f == 'packages/core/src/services/contextManager.ts':
        continue
    
    # Check if file should be auto-resolved to upstream (side 2)
    if any(m in f for m in auto_resolve_upstream):
        print(f"Auto-resolving {f} using upstream")
        subprocess.run(["jj", "restore", "--from", "vntqzqso", f])
        
