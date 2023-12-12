import machine
import utime
import _thread

# 初始化 PIO
pios = {
    0: machine.Pin(5, machine.Pin.OUT),
    1: machine.Pin(0, machine.Pin.OUT)
    # 可以根据需要添加更多的脚位
}

# 控制函数
def control_pio(pin_number, state):
    if pin_number in pios:
        pios[pin_number].value(state)

# 任务列表
tasks = []

# 定时器线程函数
def timer_thread():
    while True:
        current_time = utime.localtime()
        for task in list(tasks):  # 使用列表副本进行迭代，以避免修改迭代器
            pin_number, start_time, stop_time, pio_active = task

            # 构建当前时间和启动/停止时间的比较元组
            current_tuple = (current_time[6], current_time[3], current_time[4], current_time[5])
            start_tuple = start_time[:-1]
            stop_tuple = stop_time[:-1]

            # 检查是否到达启动时间
            if not pio_active and current_tuple >= start_tuple:
                control_pio(pin_number, 1)  # 启动 PIO
                task[3] = True

            # 检查是否到达停止时间
            if pio_active and current_tuple >= stop_tuple:
                control_pio(pin_number, 0)  # 停止 PIO
                tasks.remove(task)  # 从任务列表中移除任务

        utime.sleep(1)  # 每秒检查一次

# 启动和管理定时器的函数
def start_timer(pin_number, start_weekday, start_hour, start_minute, start_second, stop_weekday, stop_hour, stop_minute, stop_second):
    global tasks
    start_time = (start_weekday, start_hour, start_minute, start_second, True)
    stop_time = (stop_weekday, stop_hour, stop_minute, stop_second, False)
    tasks.append([pin_number, start_time, stop_time, False])

# 启动定时器线程
_thread.start_new_thread(timer_thread, ())

# 使用示例
# 启动定时器，控制脚位 0，星期一 20:54:00 启动，20:54:30 停止
start_timer(0, 0, 22, 41, 0, 0, 22, 41, 30)

# 启动定时器，控制脚位 1，星期一 20:54:10 启动，20:54:50 停止
start_timer(1, 0, 22, 41, 10, 0, 22, 41, 50)
