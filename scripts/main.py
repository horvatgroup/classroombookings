#!/usr/bin/env python

from pprint import PrettyPrinter
from timetable import Timetable
from db import Db

pprint = PrettyPrinter(indent=4).pprint

def sync_periods(timetable, db):
    db.clear_periods()
    for period in timetable.get_periods():
        db.add_period(period.name, period.starttime, period.endtime)

def sync_rooms(timetable, db):
    db.clear_rooms()
    for room in timetable.get_rooms():
        db.add_room(room.name, room.short)

def sync_sessions_weeks_dates(db):
    date_start = "2024-01-01"
    date_end = "2024-07-01"
    db.clear_sessions()
    db.clear_weeks()
    db.clear_dates()
    db.add_session("Polugodište", date_start, date_end)
    db.add_week("Tjedan")
    db.add_dates(date_start, date_end)

def sync_departments(db):
    db.clear_departments()
    db.add_department("Nastava")
    db.add_department("Privatno")

def sync_all(timetable, db):
    db.clear_all()
    sync_sessions_weeks_dates(db)
    sync_periods(timetable, db)
    sync_rooms(timetable, db)
    sync_departments(db)

if __name__== "__main__":
    timetable = Timetable()
    db = Db()
