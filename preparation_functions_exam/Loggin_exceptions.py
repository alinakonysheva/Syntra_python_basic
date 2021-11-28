import logging
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
logging.basicConfig(filename='lod_log_exc.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

a = []
try:
    a[1]
except Exception as e:
    # print(e.__class__)
    logging.error(f"{e.__class__}", exc_info=True)
