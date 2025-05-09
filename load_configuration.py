import json

class LoadConfiguration:
    def __init__(self, config_path):
        self.load_config(config_path)

    def load_config(self, config_path):
        with open(config_path) as f:
            config = json.load(f)

        self.source_bucket = config["source_bucket"]
        self.target_bucket = config["target_bucket"]
        self.prefix = config.get("prefix")
        self.max_workers = config.get("max_workers", 10)
        self.batch_size = config.get("batch_size", 100)
        self.google_creds = config["google_credentials"]
        self.magalu_config = config["magalu_cloud"]
