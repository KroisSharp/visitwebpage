import time
import subprocess

while True:
    my_p = subprocess.Popen(["Firefox", "https://dk.linkedin.com"])
    time.sleep(30)
    my_p.kill()
    #åben de ønskde afslut med:
    time.sleep(7200) #3600 sek er en time
