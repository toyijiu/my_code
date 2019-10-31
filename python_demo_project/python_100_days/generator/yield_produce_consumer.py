def consumer():
    while True:
        d = yield
        if not d:
            break
        print("consumer:",d)

#创建并启动消费者
c = consumer()
c.send(None)
#生产一个数据给消费者
c.send(1)
#生产结束，通知消费者结束
c.send(None)