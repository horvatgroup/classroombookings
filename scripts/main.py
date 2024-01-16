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
PASTORALNI_CENTAR = "Pastoralni centar"
SKOLSKA_ZGRADA = "Školska zgrada"
BOLNICA = "Bolnica"
SESSION = "Polugodište"
WEEK = "Tjedan"
SCHEDULE = "Periods"

holidays = [
        Holiday("Zimski praznici 2/2", "2024-02-19", "2024-02-23"),
        Holiday("Proljetni praznici", "2024-03-28", "2024-04-08"),
        Holiday("Uskrs", "2024-03-31", "2024-03-31"),
        Holiday("Uskrsni ponedjeljak", "2024-04-01", "2024-04-01"),
        Holiday("Praznik rada", "2024-05-01", "2024-05-01"),
        Holiday("Dan državnosti, Tijelovo", "2024-05-30", "2024-05-30"),
        Holiday("Dan antifašističke borbe", "2024-06-22", "2024-06-22"),
        ]

def sync_room_groups(db):
    db.clear_room_groups()
    db.add_room_group(PASTORALNI_CENTAR)
    db.add_room_group(SKOLSKA_ZGRADA)
    db.add_room_group(BOLNICA)

def sync_rooms(timetable, db):
    db.clear_rooms()
    room_group_id_pastoralni_centar = db.get_room_group_id_by_name(PASTORALNI_CENTAR)
    room_group_id_skolska_zgrada = db.get_room_group_id_by_name(SKOLSKA_ZGRADA)
    room_group_id_bolnica = db.get_room_group_id_by_name(BOLNICA)
    for room in timetable.get_classrooms():
        if "nova škola" in room.name.lower():
            db.add_room(room.name, room.short, room_group_id_skolska_zgrada)
        elif "bolnica" in room.name.lower():
            db.add_room(room.name, room.short, room_group_id_bolnica)
        else:
            db.add_room(room.name, room.short, room_group_id_pastoralni_centar)

def sync_access_control(db):
    db.clear_access_control()
    db.add_access_control_for_all_rooms()

def sync_departments(db):
    db.clear_departments()
    db.add_department("Nastava")
    db.add_department("Vannastavno")

def sync_sessions_weeks_dates(db):
    date_start = DATE_START
    date_end = DATE_END
    db.clear_sessions()
    db.clear_weeks()
    db.clear_dates()
    db.add_session(SESSION, date_start, date_end)
    db.add_week(WEEK)
    db.add_dates(date_start, date_end)

def sync_session_schedules(db):
    db.clear_session_schedules()
    session_id = db.get_session_id_by_name(SESSION)
    group_room_ip_pastoralni_centar = db.get_room_group_id_by_name(PASTORALNI_CENTAR)
    group_room_ip_skolska_zgrada = db.get_room_group_id_by_name(SKOLSKA_ZGRADA)
    schedule_id = db.get_schedule_id_by_name(SCHEDULE)
    db.add_session_schedule(session_id, group_room_ip_skolska_zgrada, schedule_id)
    db.add_session_schedule(session_id, group_room_ip_pastoralni_centar, schedule_id)

def sync_periods(timetable, db):
    db.clear_periods()
    for period in timetable.get_periods():
        db.add_period(period.name, period.starttime, period.endtime)

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
    sync_room_groups(db)
    sync_rooms(timetable, db)
    sync_access_control(db)
    sync_departments(db)
    sync_sessions_weeks_dates(db)
    sync_session_schedules(db)
    sync_periods(timetable, db)
    sync_holidays(db)
    #sync_bookings(timetable, db)

if __name__== "__main__":
    timetable = Timetable()
    db = Db()
