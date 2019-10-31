def coroutine():
    print("coroutine start")
    result = None
    while True:
        s = yield result
        result = s.split(",")

#函数返回协程对象
c = coroutine()
#启动协程
c.send(None)
#向协程发送消息，让其恢复执行
print(c.send("a,b"))
#关闭协程
c.close()
