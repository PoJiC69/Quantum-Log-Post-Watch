import time
import hashlib
import json

class LogEntry:
    def __init__(self, timestamp, mode, sensor_values):
        self.timestamp = timestamp
        self.mode = mode
        self.sensor_values = sensor_values
        self.terra_hash = self.calculate_terra_hash()

    def calculate_terra_hash(self):
        log_str = f'{self.timestamp}{self.mode}{json.dumps(self.sensor_values)}'
        return hashlib.sha256(log_str.encode()).hexdigest()

    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'mode': self.mode,
            'sensor_values': self.sensor_values,
            'terra_hash': self.terra_hash
        }

class LogDatabase:
    def __init__(self, filename='log_db.json'):
        self.filename = filename
        self.entries = []
        self.load_database()

    def load_database(self):
        try:
            with open(self.filename, 'r') as file:
                self.entries = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.entries = []

    def append_entry(self, mode, sensor_values):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        entry = LogEntry(timestamp, mode, sensor_values)
        self.entries.append(entry.to_dict())
        self.save_database()

    def save_database(self):
        with open(self.filename, 'w') as file:
            json.dump(self.entries, file, indent=4)

    def display_entries(self):
        for entry in self.entries:
            print(entry)

# Example Usage
if __name__ == '__main__':
    db = LogDatabase()
    db.append_entry('reading', {'temperature': 22.5, 'humidity': 55})
    db.display_entries()