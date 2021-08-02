import yaml

_config = None

def config():
    
    global _config
    
    if not _config:
        with open('config.yaml', mode='r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            
        return config