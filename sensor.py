class sensor:
    uuid = None
    sensor_type = None

    def __init__(self, uuid, sensor_type):
        self.uuid = uuid
        self.sensor_type = sensor_type
