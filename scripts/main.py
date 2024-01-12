#!/usr/bin/env python

from pprint import PrettyPrinter
from timetable import Timetable
from db import Db
from dataclasses import dataclass

pprint = PrettyPrinter(indent=4).pprint

@dataclass
class Holiday:
    name: str
    date_start: str
    date_end: str

# 2023./2024.
DATE_START = "2024-01-08"
DATE_END = "2024-06-21"

holidays = [
        Holiday("Zimski praznici 2/2", "2024-02-19", "2024-02-23"),
        Holiday("Proljetni praznici", "2024-03-28", "2024-04-08"),
        Holiday("Uskrs", "2024-03-31", "2024-03-31"),
        Holiday("Uskrsni ponedjeljak", "2024-04-01", "2024-04-01"),
        Holiday("Praznik rada", "2024-05-01", "2024-05-01"),
        Holiday("Dan državnosti, Tijelovo", "2024-05-30", "2024-05-30"),
        Holiday("Dan antifašističke borbe", "2024-06-22", "2024-06-22"),
        ]


def sync_periods(timetable, db):
    db.clear_periods()
    for period in timetable.get_periods():
        db.add_period(period.name, period.starttime, period.endtime)

def sync_rooms(timetable, db):
    db.clear_rooms()
    for room in timetable.get_classrooms():
        db.add_room(room.name, room.short)

def sync_session_schedules(db):
    db.clear_session_schedules()
    db.add_session_schedules_default()

def sync_sessions_weeks_dates(db):
    date_start = DATE_START
    date_end = DATE_END
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

def sync_holidays(db):
    for holiday in holidays:
        db.add_holiday(holiday.name, holiday.date_start, holiday.date_end)

def sync_bookings(timetable, db):
    teachings = timetable.get_teachings()
    for teaching in teachings:
        room_id = db.get_room_id_by_name(teaching.classroom_name)
        period_id = db.get_period_id_by_name(teaching.period_name)
        db.add_booking_in_range(room_id, period_id, teaching.notes, DATE_START, DATE_END, teaching.weekday)

def sync_private_bookings(db):
    db.import_private_bookings("private.json")

def sync_all(timetable, db):
    db.clear_all()
    sync_sessions_weeks_dates(db)
    sync_session_schedules(db)
    sync_periods(timetable, db)
    sync_rooms(timetable, db)
    sync_departments(db)
    sync_holidays(db)
    sync_bookings(timetable, db)

if __name__== "__main__":
    timetable = Timetable()
    db = Db()
