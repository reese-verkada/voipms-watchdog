from voipms_watchdog import db
from voipms_watchdog.models import *

db.create_all()

from voipms_watchdog.tests import options
