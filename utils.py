import time


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 把 unix time 转换为普通人类可以看懂的格式
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)
