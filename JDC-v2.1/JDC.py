import requests
import time
import jsonpath
import urllib3
import json
import datetime

#关掉用Charles抓包调试时的警告
urllib3.disable_warnings()

class JdCloud():
    def __init__(self, pin, appkey, tgt, accesskey, wskey, jdmt_sign, jdmt_appkey,UserAgent):
        self.pin = pin
        self.appkey = appkey
        self.tgt =tgt
        self.accesskey = accesskey
        self.wskey = wskey
        self.jdmt_sign = jdmt_sign
        self.jdmt_appkey = jdmt_appkey
        self.UserAgent = UserAgent

    def accountHeaders(self):
        """
        获取用户金币信息

        :return: headers
        """
        headers = {
            "content-type": "application/json",
            "jdmt-rx-appkey": self.jdmt_appkey,
            "jdmt-rx-sign": self.jdmt_sign,
            "wskey": self.wskey,
            "Referer": "http://guanli.luyou.360.cn/new_index.htm",
            "User-Agent": self.UserAgent
        }
        return headers

    def routertHeaders(self, au):
        """
        获取路由器状态

        :return: headers
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": au,
            "accesskey": self.accesskey,
            "tgt": self.tgt,
            "appkey": self.appkey,
            "pin": self.pin,
            "User-Agent": self.UserAgent
        }
        return headers

    def usersInfoJs(self, feed_id):
        """
        好像是所有的链接用户设备的js吧

        :return: json
        """
        jsText = {"feed_id":feed_id,"command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"get_device_list\"\n}"}]}
        return json.dumps(jsText, separators=(',', ':'))

    def routerInfoJs(self, feed_id):
        """
        路由器运行状态信息

        :return: json
        """
        jsText = {"feed_id":feed_id,"command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"get_router_status_detail\"\n}"}]}
        return json.dumps(jsText, separators=(',', ':'))

    def routerStatusInfoJs(self, feed_id):
        """
        路由器的配置信息

        :param feed_id:str
        :return: json
        """
        jsText = {"feed_id":feed_id,"command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"jdcplugin_opt.get_pcdn_status\"\n}"}]}
        return json.dumps(jsText, separators=(',', ':'))

    def todayPointAll(self):
        """
        今日设备总积分

        :return:
            {'code': 200,
             'requestId': 'c0ui5t77t6fisgtbj7fo3w3mia1q93am',
             'error': None,
             'result':
                {'todayDate': '2021-02-28',
                 'pointInfos':
                    [
                        {'mac': 'DCD87C0B99B1',
                        'todayPointIncome': 59,
                         'allPointIncome': 7637},

                        {'mac': 'DCD87C1234EA',
                        'todayPointIncome': 10,
                         'allPointIncome': 20}
                    ],
                    'pageInfo':
                    {'currentPage': 1,
                     'pageSize': 15,
                     'totalRecord': 2,
                     'totalPage': 1
                     }
                }
            }
        """
        todayPointAll_url = "https://router-app-api.jdcloud.com/v1/regions/cn-north-1/todayPointDetail?sortField=today_point&sortDirection=DESC&currentPage=1&pageSize=15"
        headers = self.accountHeaders()
        res = requests.get(todayPointAll_url, headers=headers,verify=False)
        return res.json()

    def pinTotalAvailPoint(self):
        """
        可用总积分

        :return:
        """
        pinTotalAvailPoint_url = "https://router-app-api.jdcloud.com/v1/regions/cn-north-1/pinTotalAvailPoint?"
        headers = self.accountHeaders()
        res = requests.get(pinTotalAvailPoint_url, headers=headers,verify=False)
        return res.json()

    # 待开发项目
    def listAllUserDevices(self, feed_id, au):
        """
                获取设备名称

        尚无多台设备，待有多台设备之后再进行研究
        :return: -1
        """
        listAllUserDevices_url = "https://gw.smart.jd.com/f/service/controlDevice?plat=ios&hard_platform=iPhone11,2&app_version=6.5.5&plat_version=14.4&device_id=a3f5c988dda4cddf1c0cbdd47d336c9c99054854&channel=jd HTTP/1.1"
        js = self.usersInfoJs(feed_id=feed_id)
        headers = self.routertHeaders(au=au)
        res = requests.post(listAllUserDevices_url, headers=headers,data=js,verify=False)

        return res.json()

    def deviceInfo(self, feed_id, au):
        """
        设备运行状态--查看cpu，mac，upload，download，等信息

        :return:json
        """
        deviceInfoUrl = "https://gw.smart.jd.com/f/service/controlDevice?plat=ios&hard_platform=iPhone11,2&app_version=6.5.5&plat_version=14.4&device_id=a3f5c988dda4cddf1c0cbdd47d336c9c99054854&channel=jd HTTP/1.1"
        js = self.routerInfoJs(feed_id=feed_id)
        headers = self.routertHeaders(au=au)
        res = requests.post(deviceInfoUrl, headers=headers, data=js, verify=False)
        return res.json()

    def routerStatusInfo(self, feed_id, au):
        """
        插件信息查询

        :param feed_id:str
        :return: json
        """
        routerStatusInfoUrl = "https://gw.smart.jd.com/f/service/controlDevice?plat=ios&hard_platform=iPhone11,2&app_version=6.5.5&plat_version=14.4&device_id=a3f5c988dda4cddf1c0cbdd47d336c9c99054854&channel=jd HTTP/1.1"
        js = self.routerStatusInfoJs(feed_id=feed_id)
        headers = self.routertHeaders(au=au)
        res = requests.post(routerStatusInfoUrl, headers=headers, data=js, verify=False)
        return res.json()



class Switches(JdCloud):

    def result_search(self, jsonResult, key_name):
        """
        从返回结果中的json文本中查找想要的文本结果

        :param jsonResult: json
        :param key_name: key
        :return: result
        """
        return jsonpath.jsonpath(jsonResult, key_name)[0]

    def result_searches(self, jsonResult, key_name):
        return jsonpath.jsonpath(jsonResult, key_name)

    def getAccountInfo(self):
        """
        每日财务报告

        这里只写了只有一台的情况，多台的情况需要重写，我没有多台设备不知道多台是怎么样的情况

        :return:
        """
        todayPointAllResult = self.todayPointAll()
        todayPointAllList64 = {}
        for key in "mac", "todayDate", "todayPointIncome", "allPointIncome" :
            result = self.result_searches(todayPointAllResult,f"$..{key}")
            todayPointAllList64[key] = result[0]
        pinTotalAvailPointResult = self.pinTotalAvailPoint()
        resultDic = {
            "todayDate": todayPointAllList64['todayDate'],  # 当前日期
            "todayPointIncome": todayPointAllList64['todayPointIncome'],  # 当天收入
            "allPointIncome": todayPointAllList64['allPointIncome'],  # 历史总收入
            "totalAvailPoint": self.result_search(pinTotalAvailPointResult, "$..totalAvailPoint"), # 当前剩余
        }
        return resultDic

    def infoDataParser(self, deviceInfo):
        """
        解析返回值

        :param deviceInfo:
        :return: str
        """
        try:
            deviceInfoDic = deviceInfo["result"]
            deviceInfoDic = eval(deviceInfoDic)["streams"][0]["current_value"]
            return deviceInfoDic
        except Exception:
            return "-1"

    def getDeviceInfo(self, feed_id, au):
        """
        获得路由器的运行信息

        :return: resultDic
        """
        def _time(seconds):
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            return "%d小时%02d分钟%02d秒" % (h, m, s)
        deviceInfo = self.deviceInfo(feed_id=feed_id, au=au)
        deviceInfoDic = self.infoDataParser(deviceInfo=deviceInfo)
        if deviceInfoDic != -1:
            deviceInfo_js = json.loads(deviceInfoDic)
            resultDic = {
                "Mac": self.result_search(deviceInfo_js, "$..mac"),
                "Rom": self.result_search(deviceInfo_js, "$..rom"),
                "Cpu": self.result_search(deviceInfo_js, "$..cpu"),
                "mem": self.result_search(deviceInfo_js, "$..mem"),
                "UPload": self.result_search(deviceInfo_js, "$..upload"),
                "Download": self.result_search(deviceInfo_js, "$..download"),
                "OnlineTime": _time(seconds=int(self.result_search(deviceInfo_js, "$..onlineTime")))
            }
            return resultDic
        else:
            return -1

    def getUsersInfo(self, feed_id, au):
        """
        获取所有连接到路由器的设备
            1，熟悉设备上线通知，下线通知。
            2，新设备上线通知，下线通知
            在线状态
            ['A44519ED3EC5', '0', '妈',          '2.4G', '2021-02-28 20:29', '0', '1', '-89', 'Redmi8A-Redmi', '1', '0', '0'],
            ['A483E752688E', '0', 'MacBook-Pro', '2.4G', '2021-02-28 14:26', '0', '1', '-92', 'MacBook-Pro', '1', '0', '0'],
            ['00E04C78F2E7', '14', 'MacBook-Pro', 'wire', '2021-02-28 12:26', '0', '1', '0', 'MacBook-Pro', '1', '0', '0'],
            ['7EBC8BCF57AF', '0', 'ipadpro', '5G', '2021-02-28 12:19', '0', '1', '-86', '', '1', '0', '0'],
            离线状态
             ['D462EA121B51', '0', 'HONOR_9X-1278feffe1de9b4c', '2.4G', '2021-02-19 18:41', '2021-02-19 18:41', '1', '0', 'HONOR_9X-1278feffe1de9b4c', '1', '0', '0'],
            ['EE7BB675BCF6', '0', 'nova_6_SE-d25ab8c4b2333ff', '2.4G', '2021-02-19 17:58', '2021-02-19 17:58', '1', '0', 'nova_6_SE-d25ab8c4b2333ff', '1', '0', '0'],
            ['ACE3421BECD3', '0', 'STK-AL00-e99c15f153999948', '2.4G', '2021-02-19 15:55', '2021-02-19 15:55', '1', '0', 'STK-AL00-e99c15f153999948', '1', '0', '0'],
            1，记录mac地址，设备备注，联网方式，联网时间
            2，判断第五位是否为0 ，0 在线

        :return:list
        """
        userInfo = self.listAllUserDevices(feed_id=feed_id, au=au)
        deviceInfoDic = self.infoDataParser(userInfo)
        if deviceInfoDic != -1:
            deviceInfoDic = eval(deviceInfoDic)["data"]["device_list"]
            return deviceInfoDic
        else:
            return -1

    def getRouterStatusInfo(self, feed_id, au):
        routerStatusInfo = self.routerStatusInfo(feed_id=feed_id, au=au)
        routerStatusInfoDic = self.infoDataParser(routerStatusInfo)
        if routerStatusInfoDic != -1:
            routerStatusInfoJs = json.loads(routerStatusInfoDic)
            pcdnList = {
                "插件状态" : self.result_search(routerStatusInfoJs, "$..status"),
                "插件别称" : self.result_search(routerStatusInfoJs, "$..nickname"),
                "插件名称" : self.result_search(routerStatusInfoJs, "$..name"),
                "缓存大小" : self.result_search(routerStatusInfoJs, "$..cache_size")
                #{'插件状态': '正常', '插件别称': '插件A', '插件名称': 'pcdniqiyi', '缓存大小': '7858212'}9点13
            }
            return pcdnList
        else:
            return -1







