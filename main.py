import win32com.client
import time


from gen import *



# for i in range(len(q)):
  # q[i]=int(np.random.randint(maxpitch)+1)

speed=0.5

print("waiting 3")

time.sleep(3)
print("doing it")
shell = win32com.client.Dispatch("WScript.Shell")

# shell.AppActivate("Outlook")
# shell.SendKeys("^o", 0) # 1 für Pause = true 0 für nein
# shell.SendKeys("^a", 0)
# shell.SendKeys("^c", 0)

for qq in q:
  shell.SendKeys(posn[qq[0]], 0)
  time.sleep(qq[1]*speed)

print("done")