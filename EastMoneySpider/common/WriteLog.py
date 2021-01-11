import logging  # 引入logging模块
import os.path
import time

class MyLogger(object):
    def __init__(self, fileName):
        # 第一步，创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)  # Log等级总开关
        # 第二步，创建一个handler，用于写入日志文件
        rq = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/Logs/' + fileName + '/'
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name, mode='w')
        fh.setLevel(logging.INFO)  # 输出到file的log等级的开关
        # 第三步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        # 第四步，将logger添加到handler里面
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    log = MyLogger("test")
    log.debug('this is a logger debug message')
    log.info('this is a logger info message')
    log.warning('this is a logger warning message')
    log.error('this is a logger error message')
    log.critical('this is a logger critical message')
