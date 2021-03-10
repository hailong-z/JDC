from .jdc import JdCloud
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot import on_command,CommandSession




pin = "jd_5800b69c9ac12"
appkey = "996"
tgt = "AAJf8FujAEAbgpcBHqEYJ93OSEdgi4XSMo2ZIVwIgw4-C9a1P_-Q4P_7rzClZbPy595GCN2VS8qto8I3JjV6K54JdtFKLQbF"
accesskey = "b8f9c108c190a39760e1b4e373208af5cd75feb4"
wskey = "AAJf8FujAEAbgpcBHqEYJ93OSEdgi4XSMo2ZIVwIgw4-C9a1P_-Q4P_7rzClZbPy595GCN2VS8qto8I3JjV6K54JdtFKLQbF"
jdmt_sign = "122158c5d3d55f8b2339854403528984"
jdmt_appkey = "fe2c20725c261e49a80d707a6ab299e1"
jd_cloud = JdCloud(pin, appkey, tgt, accesskey, Authorization, wskey, jdmt_sign, jdmt_appkey)

@nonebot.scheduler.scheduled_job('cron', hour='6', minute='10')
async def _():
    bot = nonebot.get_bot()
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
    await bot.send_private_msg(user_id=1226619354,
                               message=msg)

@on_command('收益', aliases=('京东云', '无线宝', '积分'),only_to_me=False)
async def weather(session:CommandSession):
    bot = nonebot.get_bot()
    res = jd_cloud.run()
    msg = '------<<JDC财务报表>>------\n' \
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
    await bot.send_msg(message=msg, group_id=971506048)
    await bot.send_private_msg(user_id=1226619354,
                                   message=msg)


