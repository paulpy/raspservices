import logging
logging.basicConfig(filename='testlog.log',level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
