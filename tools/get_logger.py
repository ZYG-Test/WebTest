import logging.handlers

class GetLogger:

    logger =None

    #获取logger
    @classmethod
    def get_logger(cls):
        #如果Logger为空
        if cls.logger is None:
            #获取日志器
            cls.logger=logging.getLogger()
            #设置日志器默认格式
            cls.logger.setLevel(logging.INFO)
            # 获取处理器 控制台
            sh = logging.StreamHandler()
            #获取处理器文件时间
            th= logging.handlers.TimedRotatingFileHandler(filename='../log/runcase.log',
                                                          when='midnight',
                                                          interval=1,
                                                          backupCount=30,
                                                          encoding='utf-8')
            #获取格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s)"
            fmt = logging.Formatter(fm)
            #将格式器设置处理器中
            sh.setFormatter(fmt)
            th.setFormatter(fmt)
            #将处理器 添加到日志器中
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        #返回日志器
        return cls.logger
