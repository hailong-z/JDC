2021年3月11日更新
=

JDC-v2.1<br>
(JDC-v1.0留个纪念吧）<br>
>JDC-v2.1在JDC-v2.0的基础上完成了所有的代码构建并且格式化了上下行接口对象：<br>
>>①authorization算法逆向<br>
>>②监控路由器数据，并将数据存入数据库<br>
>>③对记录的路由器数据进行分析建表<br>
>>④监控路由器子设备的情况（上线提醒，下线提醒等)<br>
>>⑤对接QQ机器人<br>
>>在QQ机器人上运行JDC-v2.1展示收益：<br>
>>![IMG_1E434D366175-1](https://user-images.githubusercontent.com/61647893/110804034-c379cf00-82ba-11eb-8e8f-6edc170469c2.jpeg)



JDC-v2.0
>JDC-v2.0通过多个结合两个主机返回的信息，直接获取最佳的返回值，可以更好地整合结果。监控路由器运行状态，建立数据分析表<br>
>项目过程：<br>
>>①~~基本完善JDC中代码结构,代码完善程度90~~<br>
>>②host= router-app-api.jdcloud.com/正常抓取，headers不会过期，host=gw.smart.jd.com的headers中有个参数叫做authorization，其认证方式大概几天一换，就很烦，导致监控路由器网速等信息不能正常返回<br>
>>③~~目前在等京东云无线宝app的破壳逆向~~<br>
>>④~~qq机器人的连接~~

~~JDC-v1.0~~
>~~JDC-v1.0通过主机router-app-api.jdcloud.com/正常抓取数据~~<br>
>~~项目过程：~~<br>
>>~~①代码完成度100~~<br>
>>~~②能长期的，正常的返回数据,但是仅仅只能返回每日收益，历史总收益，当前未兑换。不能对路由器的运行信息进行监控~~<br>
>>~~③JDC-v1.0配合qq机器人运行结果展示:~~<br>
>>![IMG_BDD37FAA6EF9-1](https://user-images.githubusercontent.com/61647893/110797655-44819800-82b4-11eb-9770-5f57c664c16c.jpeg)
***
**京东云无线宝app逆向工程进度**
>已经完成逆向找到了解密后的.dex文件,也大概了解了加密的位置，app login的文件位置，无奈不会java，加上最近要忙复试，于是一拖再拖，希望有经验的大佬能帮忙一起做<br>邮箱：haswell_z#foxmail.com(#换成@）希望各位大佬给点帮助，逆向什么的太难了
