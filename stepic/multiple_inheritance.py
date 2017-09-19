import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, p_object):
        super(LoggableList, self).append(p_object)
        self.log(p_object)

mine = LoggableList()
mine.append(10)