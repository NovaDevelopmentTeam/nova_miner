import subprocess
import os

# Change the working directory
os.chdir(r'C:\Users\jonas\Downloads\crypto_bg_miner\xmrig-6.22.2')

# Define the command to run xmrig with the appropriate arguments
command = ['xmrig.exe', '-o', 'pool.supportxmr.com:443', '-u', '47SoHaddieiTiuTvczsrbvLdMMLYbk3wKjBbtag8xqErLsPwHABwCtHJiawhC7sS97WJd52KrL1cxTENHS4foTu98rHm1Gs', '-k', '--tls']

# Execute the command using subprocess.Popen
subprocess.Popen(command)
