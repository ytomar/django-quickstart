import sys, os, yaml

def readConfig(name=None):
    HERE = HOME = os.path.dirname(os.path.abspath(__file__))
    CONFIG = yaml.load(open(os.path.join(HERE,'conf','config.main.yml')))
    CONFIG['DATA'] = os.path.join(HERE,'data')
    CONFIG['LOGS'] = os.path.join(HERE,'logs')
    CONFIG["HOME"] = HERE
    if HOME not in sys.path:
        sys.path.append(HOME)
    return CONFIG
