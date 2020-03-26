import configparser
config = configparser.ConfigParser()

def get_database_value(key):
    config.read('config.ini')
    databases = config['databases'][key]
    return databases

def get_sql_type(key):
    config.read('config.ini')
    sql = config['application']['database']
    return sql

def get_value(section_name,key):
    config.read('config.ini')
    try:
        value = config[section_name][key]
    except KeyError as ex:
        value = 'Database not avaiable'
    return value



if __name__ == '__main__':
    print (get_database_value('WC'))