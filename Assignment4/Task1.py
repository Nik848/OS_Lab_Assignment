import subprocess
# List of scripts to execute in sequence
scripts = ['script1.py', 'script2.py', 'script3.py']
# Run each script one by one (batch processing)
for script in scripts:
    print(f"Executing {script}...")
    # subprocess.call runs the script as a separate process
    subprocess.call(['python3', script])
