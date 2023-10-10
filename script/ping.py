import subprocess  
import time  

setime = input("间隔时间:")
setime = float(setime)
ip = input("ip地址:")

def ping(host):  
    """连续ping指定的目标IP或域名"""  
    while True:  
        result = subprocess.run(["ping", "-c", "1", host], stdout=subprocess.PIPE)  
        if b"unreachable" in result.stdout:  # 如果目标主机无法访问  
            print(host, "is offline.")  
        else:  # 如果目标主机可以访问  
            print(host, "is online.")  
        time.sleep(setime)  # 休眠1秒再继续ping  
  
# 测试上面的函数  
ping(ip)