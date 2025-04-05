# config.ini: [Data] H=host P=1-> c.py: c=configparser.ConfigParser()->c.read('config.ini')->h=c['Data']['H'] p=c['Data'].getint('P')-> print(h,p)
import configparser

# Создаем объект configparser
config = configparser.ConfigParser()

# Читаем файл конфигурации
config.read('config.ini')

db_host = config['Database']['Host']
db_port = config['Database'].getint('Port')

print("Database Host:", db_host)
print("Database Port:", db_port)

# config.ini: [Data] H=host P=1-> c=configparser.ConfigParser()->c.read('config.ini')->h=c['Data']['H'] p=c['Data'].getint('P')-> print(h,p)