from datetime import datetime
import schedule
from scheduler import attendanceschedule
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    # schedule.every().day.at('11:52').do(attendanceschedule.attendance).run()
    # schedule.every().day.at('11:51').do(attendanceschedule.fee).run()
    pass

