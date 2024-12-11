import subprocess
import os

file_path = os.path.join(r"C:\Users\jonas\Downloads\crypto_bg_miner\run_command.py")

# Execute the Python script
process = subprocess.Popen(["python", "run_command.py"])

process()