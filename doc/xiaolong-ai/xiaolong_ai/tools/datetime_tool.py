# -*- coding: utf-8 -*-

# 小龙智脑 (XiaoLong Brain) - 全新原创项目

# 作者 / 版权人: 小龙 (XiaoLong)

# License: MIT。本项目所有代码均为原创，保留署名即可自由使用。



from datetime import datetime

from xiaolong_ai.core.tool import tool





@tool(name="now", description="返回当前日期时间，如 now()")

def now():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

