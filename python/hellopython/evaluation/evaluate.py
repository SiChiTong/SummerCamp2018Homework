# -*- coding: utf-8 -*- 
import os
import sys
import importlib
import random
import signal
import time
 
 
def set_timeout(num, callback):
    def wrap(func):
        def handle(signum, frame):  # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame.
            raise RuntimeError
 
        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handle)  # 设置信号和回调函数
                signal.alarm(num)  # 设置 num 秒的闹钟
                #print 'start alarm signal.'
                r = func(*args, **kwargs)
                #print 'close alarm signal.'
                signal.alarm(0)  # 关闭闹钟
                return r
            except RuntimeError as e:
                callback()
 
        return to_do
 
    return wrap

#print("args is ",sys.argv);# ["evaluate.py", "python/hellopython", "赵勇","python/hellopython/赵勇/Score.txt"] 

#sys.argv=["",".","zy","score.txt"]
herepath=os.path.split(sys.argv[0])[0]
topicFolder=os.path.join(herepath,"..")

if len(sys.argv)<4:
    exit(0)

if not os.access('{}/{}/sort.py'.format(topicFolder,sys.argv[2]),os.R_OK):
    os.system('echo "[D]({}/evaluation/none.md)" > {}'.format(sys.argv[1],sys.argv[3]))
    exit(0)

sys.path.append('{}/{}'.format(topicFolder,sys.argv[2]))

try:
    import sort
except ImportError:
    os.system('echo "[C]({}/evaluation/import.md)" > {}'.format(sys.argv[1],sys.argv[3]))
    exit(0)

nums=[]
for i in range(1000):
    nums.append(random.randint(0, 1000))

def after_timeout():  # 超时后的处理函数
    os.system('echo "[B]({}/evaluation/timeout.md)" > {}'.format(sys.argv[1],sys.argv[3]))
    exit(0)

@set_timeout(2, after_timeout)  # 限时 2 秒
def call_sort(nums):
    if(sorted(nums)==sort.sort(nums)):
        os.system('echo "[S]({}/{}/sort.py)" > {}'.format(sys.argv[1],sys.argv[2],sys.argv[3]))
    else:
        os.system('echo "[B]({}/evaluation/sort.md)" > {}'.format(sys.argv[1],sys.argv[3]))

try:
    call_sort(nums)
except AttributeError:
    os.system('echo "[B]({}/evaluation/no_sort.md)" > {}'.format(sys.argv[1],sys.argv[3]))
    exit(0)




