import configparser 

config = configparser.ConfigParser()
config['email'] = {'EMAIL_HOST_USER': '',
                   'EMAIL_HOST_PASSWORD': '',
                   'DEFAULT_FROM_EMAIL': ''}

config['database'] = {'name': '',
                   'user': '',
                   'password': ''}

# write configuration file 
with open('config.ini', 'w') as configfile:
    config.write(configfile)
