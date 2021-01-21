import random


class Printer:
    def __init__(self, pagesPerMinutes):
        self._rate = pagesPerMinutes  # 打印机每分钟能打印的页数
        self._currentTask = None  # 当前任务
        self._timeRemaining = 0  # 当前需要的时间

    def tick(self):  # 一次tick执行
        if self._currentTask:
            self._timeRemaining -= 1
            if self._timeRemaining <= 0:  # 任务执行结束，将当前任务置为None, 等待新任务
                self._currentTask = None

    def busy(self):  # 返回当前打印机状态是否busy
        return True if self._currentTask else False

    def startNext(self, newTask):  # 打印机执行新任务
        self._currentTask = newTask
        self._timeRemaining = newTask.getPages() * 60 / self._rate  # 计算任务需要的秒数


class Task:
    def __init__(self, generateTime):
        self._timestamp = generateTime  # 任务产生的时间戳
        self._pages = random.randint(1, 21)  # 任务随机页数，范围1-20

    def getStamp(self):
        return self._timestamp

    def getPages(self):
        return self._pages

    def waitTime(self, current_time):  # 计算任务的等待时间
        return current_time - self._timestamp

def simulation(numSeconds, pagesPerMinutes):
    labPrinter = Printer(pagesPerMinutes)
    printQueue, waitingTimes = [], []

    for currentSecond in range(numSeconds):
        if newPrinterTask():  # 检查是否产生新任务
            task = Task(currentSecond)
            printQueue.append(task)  # 将新任务加入到队列中

        if not labPrinter.busy() and printQueue:
            nextTask = printQueue.pop(0)
            waitingTimes.append(nextTask.waitTime(currentSecond))  # 计算任务在队列中的等待时间
            labPrinter.startNext(nextTask)

        labPrinter.tick()

    averageWait = sum(waitingTimes) / len(waitingTimes)
    print(f"Average Wait {averageWait: 8.4f} seconds {len(printQueue): 3d} tasks remaining not done.")


def newPrinterTask():  # 随机产生任务，平均每180秒产生一个
    num = random.randint(1, 181)
    return True if num == 180 else False


if __name__ == '__main__':
    for i in range(10):
        simulation(360000, 10)
