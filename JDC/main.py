from JDC import Switches
from JDC import JdCloud
import time
"""
64g运行状态:{"feed_id":"248161614328763030","command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"get_router_status_detail\"\n}"}]}
32g设备连接情况:{"feed_id":"703071609586163712","command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"get_device_list\"\n}"}]}

"""

if __name__ =="__main__":
    pin = "" 
    appkey = "996"
    tgt = ""
    accesskey = ""
    wskey = ""
    jdmt_sign = ""
    jdmt_appkey = ""
    Authorization= "smart xxxxxxxxxxxxx"
    UserAgent = "JBOXAppModule_Example/2.7.1 (iPhone; iOS 14.4; Scale/3.00)(JDCLOUD-APP; iOS/2.7.1/2)"

    switches = Switches(pin=pin,appkey=appkey,tgt=tgt,accesskey=accesskey,wskey=wskey,jdmt_sign=jdmt_sign,jdmt_appkey=jdmt_appkey,UserAgent=UserAgent)

    getAccountInfo = switches.getAccountInfo()
    
    
    deviceDict = {
        “”“
        64g运行状态:{"feed_id":"xxxxxx","command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"get_router_status_detail\"\n}"}]}
        32g设备连接情况:{"feed_id":"xxxxxx","command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"get_device_list\"\n}"}]}
        deviceDict 里面存的是对应版本的feed_id,和authorization以及对应的操作，现在做如下讲解：
            {
                feed_id : 这个id要自己抓取，feedID在app数据包中对应的名称叫做device_id
                command : command 字面理解就是命令，没错，对比一下32与64的command很容易发现只有最后key=cmd中字符串不同,不同的字符串代表执行对应的不同的命令。
            }
        "Jdc32" : ["feed_id", "authorization"],
        最好是抓两个不同的备用，我也不知道为什么，现在还在逆向app中。
        也就是分开且对应抓取
        ”“”
        "Jdc32" : ["xxxxxxxxxx", "smart xxxx"],
        "Jdc64" : ["xxxxxxxxxx", "smart xxxx"]
    }
    for key in deviceDict.keys():

        feed_id = deviceDict[key][0]
        au = deviceDict[key][1]
        getUsersInfo = switches.getUsersInfo(feed_id=feed_id, au=au)
        deviceInfo = switches.getDeviceInfo(feed_id=feed_id, au=au)
        print(deviceInfo)




#     while True:
#         """
#         对cpu，网速情况的监控，
# 
#         这里不是很完善，可以自己改一下
#         """
#         print("CPU: "+deviceInfo["Cpu"]+"  上传："+deviceInfo["UPload"]+'\t\t'+"下载："+deviceInfo["Download"])
#         time.sleep(0.5)
