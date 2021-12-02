import logging



logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)


logger.debug('this is a debug message')
logger.info('this is info')
logger.warning('this is a warning')
logger.error('this is error')
logger.critical('this is a warning')


def my_func():
    try:
        pass
    except Exception as e:
        logging.error('my_func: {}'.format(e))

def my_other_func():
    myl = ['banaan', 'appel', 'kers']
     
    for item in myl:
        logging.debug(item)



























