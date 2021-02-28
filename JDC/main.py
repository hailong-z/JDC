





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
    Authorization= ""
    UserAgent = "JBOXAppModule_Example/2.7.1 (iPhone; iOS 14.4; Scale/3.00)(JDCLOUD-APP; iOS/2.7.1/2)"

    switches = Switches(pin=pin,appkey=appkey,tgt=tgt,accesskey=accesskey,Authorization=Authorization,wskey=wskey,jdmt_sign=jdmt_sign,jdmt_appkey=jdmt_appkey,UserAgent=UserAgent)

    getUsersInfo = switches.getUsersInfo()

    getAccountInfo = switches.getAccountInfo()

    accountInfo = switches.getAccountInfo()

    deviceInfo = switches.getDeviceInfo()




    # while True:
    #
    #     print("CPU: "+deviceInfo["Cpu"]+"  上传："+deviceInfo["UPload"]+'\t\t'+"下载："+deviceInfo["Download"])
    #     time.sleep(0.5)