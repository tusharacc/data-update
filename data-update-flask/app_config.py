import config

def get_configurations():
    #Get Applications
    applications = config.get_value('application','applications')
    configurations = []
    for item in applications.split(','):
        d = {}
        databases = config.get_value('databases',item).split(',')
        d['name'] = item
        d['databases'] = databases
        configurations.append(d)
    
    return {'data':configurations}

if __name__ == '__main__':
    print (get_configurations())