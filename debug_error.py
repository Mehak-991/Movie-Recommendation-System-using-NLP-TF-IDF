import subprocess
try:
    result = subprocess.run(
        [r'.\venv\Scripts\python.exe', 'manage.py', 'check'],
        capture_output=True, text=True
    )
    with open('debug_out.txt', 'w', encoding='utf-8') as f:
        f.write(result.stdout)
        f.write('\n---STDERR---\n')
        f.write(result.stderr)
except Exception as e:
    with open('debug_out.txt', 'w', encoding='utf-8') as f:
        f.write(str(e))
print("Done. Check debug_out.txt")
