import logging
logging.basicConfig(level=logging.INFO)  # log to console
logging.info('This will get logged')  # INFO:root:This will get logged
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')  # log to file
logging.warning('This will get logged to a file')  # root - WARNING - This will get logged to a file
logging.basicConfig(format='%(process)d-%(levelname)s-%(asctime)s-%(message)s', level=logging.INFO)
logging.info('Admin logged in')  # 124404-INFO-2024-10-23 18:39:22,623-Admin logged in

logging.basicConfig(format='[%(asctime)s]-%(levelname)s-%(filename)s-[LINE:%(lineno)s]-%(message)s', level=logging.INFO)
logging.info('Admin logged in')  # [2024-10-23 19:44:34,104]-INFO-7logs.py-[LINE:14]-Admin logged in


a = 5; b = 0
try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
    print(e)

