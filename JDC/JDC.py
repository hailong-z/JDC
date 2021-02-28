import requests
import time
import jsonpath
import urllib3
import json
import datetime

#关掉用Charles抓包调试时的警告
urllib3.disable_warnings()

class JdCloud():
    def __init__(self, pin, appkey, tgt, accesskey, Authorization, wskey, jdmt_sign, jdmt_appkey,UserAgent):
        self.pin = pin
        self.appkey = appkey
        self.tgt =tgt
        self.accesskey = accesskey
        self.Authorization = Authorization
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

    def usersHeadersInfo(self):
        """
        获取路由器在线设备信息

        :return: headers
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.Authorization,
            "accesskey": self.accesskey,
            "tgt": self.tgt,
            "appkey": self.appkey,
            "pin": self.pin,
            "User-Agent": self.UserAgent
        }
        return headers

    def routertHeaders(self):
        """
        获取路由器状态,不要问我为什么有两个headers
        有时候用同一个Authorization进行认证会出问题，最好是抓两个，虽然本质上都一样。

        :return: headers
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.Authorization,
            "accesskey": self.accesskey,
            "tgt": self.tgt,
            "appkey": self.appkey,
            "pin": self.pin,
            "User-Agent": self.UserAgent
        }
        return headers

    def usersInfoJs(self):
        """
        好像是所有的链接用户设备的js吧
        js_text 这个变量非常重要，记得变量内不该空格的地方别空格

        :return: json
        """
        js_text = {"feed_id":"70307160958616371","command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"get_device_list\"\n}"}]}
        return json.dumps(js_text, separators=(',', ':'))

    def routerInfoJs(self):
        """
        路由器运行状态信息

        :return: json
        """
        js_text = {"feed_id":"70307160958616371","command":[{"stream_id":"SetParams","current_value":"{\n  \"cmd\" : \"get_router_status_detail\"\n}"}]}
        return json.dumps(js_text, separators=(',', ':'))

    def routerInfoAU(self):
        """
        路由器运行状态信息的AU
        没错，这又是一个Authorization，主要是在做的过程中不敢删代码，怕删到最后自己都不知道怎么回事了，后面再优化吧

        :return:AU
        """
        AU = ""
        return AU

    def listAllUserDevicestotal(self) -> 1:
        """
        今日设备总积分

        :return:
               {"code":200,
               "requestId":"c0som6242fv1fjmfr2badap8hk0c7gkp",
               "error":null,
               "result":
                      {"todayDate":"2021-02-25",
                      "pointInfos":[
                             {"mac":"DCD87C0B99B1",
                             "todayPointIncome":202,
                             "allPointIncome":7154
                             }
                             ],
                             "pageInfo":{
                                    "currentPage":1,
                                    "pageSize":15,
                                    "totalRecord":1,
                                    "totalPage":1
                                    }
                      }
               }
        """
        listAllUserDevicestotal_url = f"https://router-app-api.jdcloud.com/v1/regions/cn-north-1/todayPointDetail?sortField=today_point&sortDirection=DESC&pageSize=15&currentPage=1&time=${time.time() * 1000}"
        headers = self.accountHeaders()
        res1 = requests.get(listAllUserDevicestotal_url, headers=headers,verify=False)
        return res1.json()

    def routerAccountInfo(self) -> 1:
        """
        显示未兑换积分

        查询所有账户信息和积分
        :return:
               {"code":200,
               "requestId":"c0so9hhoi1ob652fcupit1so9rvfw6ui",
               "error":null,
               "result":
                      {"accountInfo":
                             {"mac":"DCD87C0B99B1",
                             "amount":1203, #总积分
                             "bindAccount":"jd_5800b69c9ac12",
                             "recentExpireAmount":77, #将有77积分会过期
                             "recentExpireTime":1645221835000 #过期的时间
                             }
                      }
               }
        """
        routerAccountInfo_url = "https://router-app-api.jdcloud.com/v1/regions/cn-north-1/routerAccountInfo?mac=XXXXXXX"#这里mac需要抓自己设备的
        headers = self.accountHeaders()
        res = requests.get(routerAccountInfo_url, headers=headers,verify=False)
        return res.json()

    def todayPointAll(self) -> 1:
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
    def listAllUserDevices(self) -> 1:
        """
                获取设备名称

        尚无多台设备，待有多台设备之后再进行研究
        :return: -1
        """
        listAllUserDevices_url = "https://gw.smart.jd.com/f/service/controlDevice?plat=ios&hard_platform=iPhone11,2&app_version=6.5.5&plat_version=14.4&device_id=xxxx&channel=jd HTTP/1.1"#这个也需要自己抓自己的

        js = self.usersInfoJs()
        headers = self.usersHeadersInfo()
        res = requests.post(listAllUserDevices_url, headers=headers,data=js,verify=False)
        return res.json()

    def deviceInfo(self) -> 1:
        """
        设备运行状态
        查看cpu，mac，upload，download，等信息

        :return:-1
        """
        deviceInfo_url = "https://gw.smart.jd.com/f/service/controlDevice?plat=ios&hard_platform=iPhone11,2&app_version=6.5.5&plat_version=14.4&device_id=xxxx&channel=jd HTTP/1.1"#对这个也要自己抓
        js = self.routerInfoJs()
        headers = self.routertHeaders()
        res = requests.post(deviceInfo_url, headers=headers, data=js, verify=False)
        return res.json()




class Switches(JdCloud):

    def result_search(self, json_result, key_name):
        """
        从返回结果中的json文本中查找想要的文本结果

        :param json_result: json
        :param key_name: key
        :return: result
        """
        return jsonpath.jsonpath(json_result, key_name)[0]

    def result_searches(self, json_result, key_name):
        return jsonpath.jsonpath(json_result, key_name)

    def getAccountInfo(self):
        """
        每日财务报告

        :return:
        """
        routerAccountInfo_result = self.routerAccountInfo()
        listAllUserDevicestotal_result = self.listAllUserDevicestotal()

        todayPointAll_result = self.todayPointAll()
        todayPointAll_list64 =[]
        todayPointAll_list32 = []
        date = ''
        for key in "mac", "todayDate", "todayPointIncome", "allPointIncome" :
            result = self.result_searches(todayPointAll_result,f"$..{key}")
            if len(result) > 1 :
                todayPointAll_list32.append(result[1])
                todayPointAll_list64.append(result[0])
            else:
                date = result[0]

        pinTotalAvailPoint_result = self.pinTotalAvailPoint()

        result_dic = {
            "todayDate": date,  # 当前日期
            "todayPointIncome": todayPointAll_list64[1]+todayPointAll_list32[1],  # 当天收入
            "allPointIncome": todayPointAll_list64[2]+ todayPointAll_list32[2],  # 历史总收入
            "totalAvailPoint": self.result_search(pinTotalAvailPoint_result, "$..totalAvailPoint"), # 当前总剩余
            "32g_today": todayPointAll_list32[1],
            "32g_total": todayPointAll_list32[2],
            "64g_today": todayPointAll_list64[1],
            "64g_total": todayPointAll_list64[2],
        }
        for i in result_dic:
            print(i+":"+str(result_dic[i]))
        return result_dic


    def getDeviceInfo(self):
        """
        获得路由器的运行信息

        :return: result_dic
        """
        deviceInfo = self.deviceInfo()
        deviceInfo_dic = deviceInfo["result"]
        deviceInfo_dic = eval(deviceInfo_dic)["streams"][0]["current_value"]
        deviceInfo_js = json.loads(deviceInfo_dic)

        result_dic = {
            "Mac": self.result_search(deviceInfo_js, "$..mac"),
            "Rom": self.result_search(deviceInfo_js, "$..rom"),
            "Cpu": self.result_search(deviceInfo_js, "$..cpu"),
            "mem": self.result_search(deviceInfo_js, "$..mem"),
            "UPload": self.result_search(deviceInfo_js, "$..upload"),
            "Download": self.result_search(deviceInfo_js, "$..download"),
            "OnlineTime": datetime.timedelta(seconds=self.result_search(deviceInfo_js, "$..onlineTime"))
        }

        return result_dic

    def getUsersInfo(self):
        """
        获取所有连接到路由器的设备
            1，熟悉设备上线通知，下线通知。
            2，新设备上线通知，下线通知
            在线状态
            ['A44519ED3EC5', '0', '妈',          '2.4G', '2021-02-28 20:29', '0', '1', '-89', 'Redmi8A-Redmi', '1', '0', '0'],
            ['A483E752688E', '0', 'MacBook-Pro', '2.4G', '2021-02-28 14:26', '0', '1', '-92', 'MacBook-Pro', '1', '0', '0'],
            ['00E04C78F2E7', '14', 'MacBook-Pro', 'wire', '2021-02-28 12:26', '0', '1', '0', 'MacBook-Pro', '1', '0', '0'],
            ['7EBC8BCF57AF', '0', '钟海龙的ipadpro', '5G', '2021-02-28 12:19', '0', '1', '-86', '', '1', '0', '0'],
            离线状态
             ['D462EA121B51', '0', 'HONOR_9X-1278feffe1de9b4c', '2.4G', '2021-02-19 18:41', '2021-02-19 18:41', '1', '0', 'HONOR_9X-1278feffe1de9b4c', '1', '0', '0'],
            ['EE7BB675BCF6', '0', 'nova_6_SE-d25ab8c4b2333ff', '2.4G', '2021-02-19 17:58', '2021-02-19 17:58', '1', '0', 'nova_6_SE-d25ab8c4b2333ff', '1', '0', '0'],
            ['ACE3421BECD3', '0', 'STK-AL00-e99c15f153999948', '2.4G', '2021-02-19 15:55', '2021-02-19 15:55', '1', '0', 'STK-AL00-e99c15f153999948', '1', '0', '0'],
            1，记录mac地址，设备备注，联网方式，联网时间
            2，判断第五位是否为0 ，0 在线

        :return:
        """
        userInfo = self.listAllUserDevices()
        deviceInfo_dic = userInfo["result"]
        deviceInfo_dic = eval(deviceInfo_dic)["streams"][0]["current_value"]
        deviceInfo_dic = eval(deviceInfo_dic)["data"]["device_list"]
        for device in deviceInfo_dic:
            pass











