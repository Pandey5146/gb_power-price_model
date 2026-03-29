import subprocess
import sys

SCRIPTS = [
    "src/extract_recent_price.py",
    "src/extract_historical_wind.py",
    "src/extract_prices.py",
    "src/extract_historical_demand.py",
]

for script in SCRIPTS:
    print(f"\n=== Running {script} ===")
    result = subprocess.run([sys.executable, script], check=False)
    if result.returncode != 0:
        print(f"FAILED: {script} (exit code {result.returncode})")
        sys.exit(result.returncode)

print("\nAll daily extract scripts completed successfully.")