import time
import random

ret_code = [0, 2, 4]



print("sleep 2s")
time.sleep(2)
print('wake up')
print('print numbers:')
for i in range(10):
    print(i)
    time.sleep(0.1)

exit(2)
# exit(random.choice(ret_code))
