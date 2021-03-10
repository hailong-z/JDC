import requests
import time
import jsonpath

class JdCloud():
    def __init__(self, pin, appkey, tgt, accesskey, Authorization, wskey, jdmt_sign, jdmt_appkey):
        self.pin = pin
        self.appkey = appkey
        self.tgt =tgt
        self.accesskey = accesskey
        self.Authorization = Authorization
        self.wskey = wskey
        self.jdmt_sign = jdmt_sign
        self.jdmt_appkey = jdmt_appkey

    def listAllUserDevicestotal(self):
        """
        今日设备总积分

        response：
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
        headers = {
            "content-type": "application/json",
            "jdmt-rx-appkey": self.jdmt_appkey,
            "jdmt-rx-sign": self.jdmt_sign,
            "wskey": self.wskey,
            "jdmt-rx-time": str(time.time() * 1000),
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 (JBOX-APP; Android/2.0.4/8)",
        }
        res1 = requests.get(listAllUserDevicestotal_url, headers=headers)
        return res1.json()

    def routerAccountInfo(self):
        """
        显示未兑换积分

        查询所有账户信息和积分
        response：
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
        routerAccountInfo_url = "https://router-app-api.jdcloud.com/v1/regions/cn-north-1/routerAccountInfo?mac=DCD87C0B99B1"
        headers = {
            "content-type": "application/json",
            "jdmt-rx-appkey": self.jdmt_appkey,
            "jdmt-rx-sign": self.jdmt_sign,
            "wskey": self.wskey,
            "Referer": "http://guanli.luyou.360.cn/new_index.htm",
        }
        res = requests.get(routerAccountInfo_url, headers=headers)
        return res.json()

    # 待开发项目
    def _(self):
        """
        获取设备名称

        尚无多台设备，待有多台设备之后再进行研究
        """
        listAllUserDevices_url = "https://gw.smart.jd.com/f/service/listAllUserDevices?plat=ios&hard_platform=iPhone11,2" \
                                 "&app_version=6.5.5&plat_version=14.4&device_id=a3f5c988dda4cddf1c0cbdd47d336c9c99054854&channel=jd"

        headers_2 = {
            "pin": self.pin,
            "appkey": self.appkey,
            "tgt": self.tgt,
            "accesskey": self.accesskey,
            "Authorization": self.Authorization,
        }

        res2 = requests.post(listAllUserDevices_url, headers=headers_2)

    def result_search(self, json_result, key_name):
        """从返回结果中的json文本中查找想要的文本结果"""
        return jsonpath.jsonpath(json_result, key_name)[0]

    def run(self):
        routerAccountInfo_result = self.routerAccountInfo()
        listAllUserDevicestotal_result = self.listAllUserDevicestotal()
        result_dic = {
            "time":time.time(),
            "todayDate": self.result_search(listAllUserDevicestotal_result, "$..todayDate"),  # 当前日期
            "todayPointIncome": self.result_search(listAllUserDevicestotal_result, "$..todayPointIncome"),  # 当天收入
            "allPointIncome": self.result_search(listAllUserDevicestotal_result, "$..allPointIncome"),  # 历史总收入
            "amount": self.result_search(routerAccountInfo_result, "$..amount"),  # 当前总剩余
            "recentExpireAmount": self.result_search(routerAccountInfo_result, "$..recentExpireAmount"),  # 即将过期
            "recentExpireTime": time.strftime("%Y-%m-%d",
                                              time.localtime(self.result_search(routerAccountInfo_result, "$..recentExpireTime") / 1000))#到期时间
            # 最近过期时间
        }
        return result_dic











