from plants.moisture import *
from plants.models import MoistureLog


def get_moisture_cron():
    MoistureLog.objects.create(moisture_level=get_moisture(0, 140, 1023))
