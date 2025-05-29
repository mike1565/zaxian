
import os

returns = os.system('shutdown /s /t 0')

if returns != 0:
    print('报错参数', returns)
