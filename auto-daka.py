# ref: 
# https://blog.csdn.net/HDFQQ188816190/article/details/98599940  adb 命令大全（简洁明了）adb命令启动应用
# https://blog.csdn.net/freedom_fd/article/details/94553284 python编写 钉钉自动 打卡脚本



import time
import os

print(os.system('adb shell input keyevent 224 ')) 
time.sleep(2)
print(os.system('adb shell input tap 850 2033 ')) 
time.sleep(2)
# start dingding
print(os.system('adb shell am start -n com.alibaba.android.rimet/.biz.LaunchHomeActivity')) 
time.sleep(8)
print(os.system('adb shell input tap 540 2050 ')) 
time.sleep(8)
print(os.system('adb shell input tap 450 1000 ')) 
time.sleep(8)
print(os.system('adb shell input tap 550 1300 ')) 
time.sleep(8)
# back to home
print(os.system('adb shell input keyevent 3')) 
time.sleep(2)
# kill dingding
print(os.system('adb shell am force-stop com.alibaba.android.rimet')) 
time.sleep(2)
print(os.system('adb shell input keyevent 223 ')) 
