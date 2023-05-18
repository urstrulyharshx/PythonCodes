import subprocess
data=subprocess.check_output(['netsh','wlan','show','profile']).decode('utf-8').split('\n')
