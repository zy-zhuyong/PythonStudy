# coding = utf-8
# 实现自动化工装控制上下电
from pykits.shell.tooling import ATooling
import time

if __name__ == '__main__':
    tool = ATooling
    while True:
        tool.set_wakeup_signal_en('on', True)
        time.sleep(20)
        tool.set_wakeup_signal_en('on', False)
        time.sleep(3)
