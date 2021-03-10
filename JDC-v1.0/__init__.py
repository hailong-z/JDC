from jdc import JdCloud
if __name__ =="__main__":
    """
    实际上，这里只需要pin参数和wskey参数即可完成访问，不需要其他的参数，但是为了构建相对完整的headers，我在此还是写下了多个参数。
    """
    pin = ""
    appkey = "996"
    tgt = ""
    accesskey = ""
    wskey = ""
    jdmt_sign = ""
    jdmt_appkey = ""
    jd_cloud = JdCloud(pin, appkey, tgt, accesskey, Authorization, wskey, jdmt_sign, jdmt_appkey)
    res = jd_cloud.run()
    msg = '--------<<JDC早报>>--------\n' \
          f'当前日期：{res["todayDate"]}\n' \
          '------------------------------\n' \
          f'今日收益：{res["todayPointIncome"]}\n' \
          '------------------------------\n' \
          f'历史收益：{res["allPointIncome"]}\n' \
          '------------------------------\n' \
          f'现有收益：{res["amount"]}\n' \
          f'其中将有{res["recentExpireAmount"]}积分在\n' \
          f'{res["recentExpireTime"]}过期\n' \
          '------------------------------\n'


