from JDC import Switches
if __name__ =="__main__":
    args = {
        "pin" :"jd_5800b69c9a",
        "appkey" : "996",
        "tgt" : "AAJf8FujAEAbgpcBHqEYJ9",
        "accesskey" : "b8f9c108c190a39760e1b4e373208af5cd75fe",
        "wskey" : "AAJf8FujAEAbgpcBHqEYJ93OSEdgi4XSMo2ZIVwIgw4-C9a1P_-Q4P_7rzClZbPy595GCN2VS8qto8I3JjV6K54JdtFKL",
        "jdmt_sign" : "122158c5d3d58b23398544035289",
        "jdmt_appkey" : "fe2c20725c261e49a80d707a6ab299",
        "UserAgent" : "JBOXAppModule_Example/2.7.1 (iPhone; iOS 14.4; Scale/3.00)(JDCLOUD-APP; iOS/2.7.1/2)",
        "feed_id" : "2481616143763030",
        "authorization" :
            [
                {
                    "statusDetailAU" : "smart b8f9c108c190a39760e1b4e373208af75feb4:::sU0wHDzLTtXLl9gUWExGlFQINTQ=:::2021-03-11T16:13:53.091Z",
                    "deviceListAU" : "smart b8f9c108c190a39760e1b4e373208af57feb4:::BfO8/seQnyHJ3cmA3hJsuOFkaA=:::2021-03-11T16:13:50.873Z",
                    "jdcpluginOpt&GetPcdnStatus" : "smart b8f9c108c190a39760e1b4e373208af575feb4:::hx684/QauCZtoIOIAjRs3hkKAnY=:::2021-03-11T16:13:53.093Z"
                }
            ]
    }

    switches = Switches(
                        pin=args["pin"],
                        appkey=args["appkey"],
                        tgt=args["tgt"],
                        accesskey=args["accesskey"],
                        wskey=args["wskey"],
                        jdmt_sign=args["jdmt_sign"],
                        jdmt_appkey=args["jdmt_appkey"],
                        UserAgent=args["UserAgent"]
                        )


    routerStatus = switches.getRouterStatusInfo(feed_id=args["feed_id"], au=args["authorization"][0]["jdcpluginOpt&GetPcdnStatus"])

    getAccountInfo = switches.getAccountInfo()

    getUsersInfo = switches.getUsersInfo(feed_id=args["feed_id"], au=args["authorization"][0]['deviceListAU'])

    deviceInfo = switches.getDeviceInfo(feed_id=args["feed_id"], au=args["authorization"][0]["statusDetailAU"])
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"账户数据：{getAccountInfo}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"路由数据：{deviceInfo}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"设备情况：{getUsersInfo[2]}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"插件情况：{routerStatus}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")

    # while True:
    #
    #     print("CPU: "+deviceInfo["Cpu"]+"  上传："+deviceInfo["UPload"]+'\t\t'+"下载："+deviceInfo["Download"])
    #     time.sleep(0.5)
