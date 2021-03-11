from JDC import Switches
from JDC import JdCloud
import time


if __name__ =="__main__":
    pin = "" 
    appkey = "996"
    tgt = ""
    accesskey = ""
    wskey = ""
    jdmt_sign = ""
    jdmt_appkey = ""
    UserAgent = "JBOXAppModule_Example/2.7.1 (iPhone; iOS 14.4; Scale/3.00)(JDCLOUD-APP; iOS/2.7.1/2)"

    switches = Switches(pin=pin,appkey=appkey,tgt=tgt,accesskey=accesskey,wskey=wskey,jdmt_sign=jdmt_sign,jdmt_appkey=jdmt_appkey,UserAgent=UserAgent)
    getAccountInfo = switches.getAccountInfo()
    feed_id = ""
    Authorization= {
    """
    64g运行状态:{"feed_id":"2481616143283030","command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"get_router_status_detail\"\n}"}]}
    32g设备连接情况:{"feed_id":"7030716095861712","command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"get_device_list\"\n}"}]}
    ------------------------------------------
    这里需要单独解释一下这个字典的含义。

    由于在获取路由器信息的时候，所有的数据都通过一条相同的url请求数据，所以采用了json来区分参数。例如：get_device_list就是获取列表
    对于json参数，需要在其对应的https封包内找到authorization
    """
        "statusDetailAU" : "smart xxxxx",
        
        "deviceListAU" : "smart xxxxx"
                    }
    getUsersInfo = switches.getUsersInfo(feed_id=feed_id, au=Authorization['deviceListAU'])
    deviceInfo = switches.getDeviceInfo(feed_id=feed_id, au = Authorization['statusDetailAU'])

#     while True:
#         """
#         对cpu，网速情况的监控，
# 
#         这里不是很完善，可以自己改一下
#         """
#         print("CPU: "+deviceInfo["Cpu"]+"  上传："+deviceInfo["UPload"]+'\t\t'+"下载："+deviceInfo["Download"])
#         time.sleep(0.5)
