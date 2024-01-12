from os import walk
import mariadb
from credentials import *
import datetime
from dataclasses import dataclass

@dataclass
class Booking:
    room_name: str
    period_name: str
    notes: str
    date: str

class Db:
    def __init__(self):
        self.conn = mariadb.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_database)
        self.cur = self.conn.cursor(dictionary=True)

    def execute(self, cmd):
        self.cur.execute(cmd)
        self.conn.commit()
        return self.cur.fetchall()

    def insert(self, table, data):
        keys = ', '.join([x for x in data.keys()])
        values = ', '.join([repr(x) for x in data.values()])
        values = values.replace("None", "NULL")
        query = f"INSERT INTO {table} ({keys}) VALUES ({values});"
        self.cur.execute(query)
        self.conn.commit()

    def update(self, table, field, field_value, data):
        keys_values = ", ".join([f"{key}={repr(value)}" for key, value in data.items()])
        query = f'UPDATE {table} SET {keys_values} WHERE {field}={repr(field_value)};'
        self.cur.execute(query)
        self.conn.commit()

    def truncate(self, table):
        self.cur.execute("SET FOREIGN_KEY_CHECKS=0;")
        self.cur.execute(f"truncate table {table};")
        self.cur.execute("SET FOREIGN_KEY_CHECKS=1;")
        self.conn.commit()

    def convert_date_to_str(self, date):
        return date.strftime('%Y-%m-%d')

    def convert_date_str_to_date(self, date_str):
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    def get_periods(self):
        result = self.execute("SELECT * FROM periods;")
        for r in result:
            r["time_start"] = str(r["time_start"])
            r["time_end"] = str(r["time_end"])
        return result

    def add_period(self, name, time_start, time_end):
        data = {
            'time_start': time_start,
            'time_end': time_end,
            'name': name,
            'days': 0,
            'bookable': 1,
            'day_1': 1,
            'day_2': 1,
            'day_3': 1,
            'day_4': 1,
            'day_5': 1,
            'day_6': 0,
            'day_7': 0
            }
        return self.insert("periods", data)

    def clear_periods(self):
        self.truncate("periods")

    def get_period_id_by_name(self, name):
        periods = self.get_periods()
        for period in periods:
            if period["name"] == name:
                return period["period_id"]
        return None

    def get_rooms(self):
        return self.execute("SELECT * FROM rooms;")

    def add_room(self, name, short_name):
        data = {
            'user_id': 0,
            'name': short_name,
            'location': name,
            'bookable': 1,
            'icon': None,
            'notes': None,
            'photo': None
            }
        return self.insert("rooms", data)

    def clear_rooms(self):
        self.truncate("rooms")

    def get_room_id_by_name(self, name):
        rooms = self.get_rooms()
        for room in rooms:
            if room["location"] == name:
                return room["room_id"]
        return None

    def get_weeks(self):
        return self.execute("SELECT * FROM weeks;")

    def add_week(self, name):
        data = {
            'name': name,
            'fgcol': '',
            'bgcol': '80FF00',
            'icon': None
            }
        self.insert("weeks", data)

    def clear_weeks(self):
        self.truncate("weeks")

    def get_departments(self):
        return self.execute("SELECT * FROM departments;")

    def add_department(self, name):
        data = {
            'name': name,
            'description': '',
            'icon': ''
            }
        self.insert("departments", data)

    def clear_departments(self):
        self.truncate("departments")

    def get_sessions(self):
        return self.execute("SELECT * FROM sessions;")

    def add_session(self, name, date_start, date_end):
        data = {
            'name': name,
            'date_start': date_start,
            'date_end': date_end,
            'is_current': 1,
            'is_selectable': 1
            }
        self.insert("sessions", data)
        
    def clear_sessions(self):
        self.truncate("sessions")

    def get_dates(self):
        return self.execute("SELECT * FROM dates;")

    def add_date(self, date, weekday):
        data = {
            "date": date,
            "holiday_id": None,
            "session_id": 1,
            "week_id": 1,
            "weekday": weekday
            }
        self.insert("dates", data)

    def add_dates(self, date_start, date_end):
        date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d').date()
        date_end = datetime.datetime.strptime(date_end, '%Y-%m-%d').date()
        delta = date_end - date_start
        for i in range(delta.days + 1):
            day = date_start + datetime.timedelta(days=i)
            self.add_date(str(day), day.weekday() + 1)

    def clear_dates(self):
        self.truncate("dates")

    def get_bookings(self):
        return self.execute("SELECT * FROM bookings;")

    def add_booking(self, room_id, period_id, notes, date):
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            'repeat_id': None,
            'session_id': 1,
            'period_id': period_id,
            'room_id': room_id,
            'user_id': 1,
            'department_id': 1,
            'date': date,
            'status': 10,
            'notes': notes,
            'cancel_reason': None,
            'cancelled_at': None,
            'cancelled_by': None,
            'created_at': created_at,
            'created_by': 1,
            'updated_at': None,
            'updated_by': None
            }
        self.insert("bookings", data)

    def clear_bookings(self):
        self.truncate("bookings")

    def get_date(self, date):
        dates = self.get_dates()
        for d in dates:
            if d["date"] == date:
                return d
        return None

    def add_booking_in_range(self, room_id, period_id, notes, date_start, date_end, weekday):
        date_start = self.convert_date_str_to_date(date_start)
        date_end = self.convert_date_str_to_date(date_end)
        delta = date_end - date_start
        for i in range(delta.days + 1):
            day = date_start + datetime.timedelta(days=i)
            date = self.get_date(day)
            if weekday == day.weekday() + 1:
                if date["holiday_id"] is None:
                    self.add_booking(room_id, period_id, notes, str(day))

    def export(self):
        data = {}
        tables = self.execute("show tables;")
        for table in tables:
            table_name = table["Tables_in_crbs_db"]
            data[table_name] = self.execute(f"SELECT * FROM {table_name}")
        filename = input("Enter filename: ")
        with open(filename + ".json", "w") as outfile: 
            import json
            json.dump(data, outfile, indent = 4, sort_keys=True, default=str)

    def clear_all(self):
        tables = self.execute("show tables;")
        for table in tables:
            table_name = table["Tables_in_crbs_db"]
            if table_name not in ("migrations", "settings", "users"):
                self.truncate(table_name)

    def get_holidays(self):
        return self.execute("SELECT * FROM holidays;")

    def add_holiday(self, name, date_start, date_end):
        data = {
            'session_id': 1,
            'name': name,
            'date_start': date_start,
            'date_end': date_end
            }
        self.insert("holidays", data)
        self.sync_dates_by_holiday_name(name, date_start, date_end)

    def clear_holidays(self):
        self.truncate("holidays")

    def get_holiday_id_by_name(self, name):
        holidays = self.get_holidays()
        for holiday in holidays:
            if holiday["name"] == name:
                return holiday["holiday_id"]
        return None

    def sync_dates_by_holiday_name(self, name, date_start, date_end):
        holiday_id = self.get_holiday_id_by_name(name)
        date_start = self.convert_date_str_to_date(date_start)
        date_end = self.convert_date_str_to_date(date_end)
        delta = date_end - date_start
        for i in range(delta.days + 1):
            day = date_start + datetime.timedelta(days=i)
            dates = self.get_dates()
            for date in dates:
                if day == date["date"]:
                    data = {
                        "holiday_id": holiday_id
                    }
                    self.update("dates", "date", self.convert_date_to_str(date["date"]), data) 

    def get_dict_from_list_of_dict_by_field_and_field_value(self, list_of_dicts, field, field_value):
        for d in list_of_dicts:
            if d[field] == field_value:
                return d
        return None

    def export_private_bookings(self):
        private_bookings = []
        bookings = self.get_bookings()
        for booking in bookings:
            if booking["department_id"] != 1:
                room_name = self.get_dict_from_list_of_dict_by_field_and_field_value(self.get_rooms(), "room_id", booking["room_id"])["location"]
                period_name = self.get_dict_from_list_of_dict_by_field_and_field_value(self.get_periods(), "period_id", booking["period_id"])["name"]
                notes = booking["notes"]
                date = self.convert_date_to_str(booking["date"])
                private_bookings.append(Booking(room_name, period_name, notes, date).__dict__)
        filename = input("Enter filename: ")
        with open(filename + ".json", "w") as outfile: 
            import json
            json.dump(private_bookings, outfile, indent = 4, sort_keys=True, default=str)

    def get_booking_by_date_room_id_period_id(self, date, room_id, period_id):
        bookings = self.get_bookings()
        for b in bookings:
            if b["date"] == date and b["room_id"] == room_id and b["period_id"] == period_id:
                return b
        return None

    def import_private_bookings(self, filename):
        with open(filename) as json_file:
            import json
            private_bookings = json.load(json_file)
            for booking in private_bookings:
                date = self.convert_date_str_to_date(booking["date"])
                room_id = self.get_room_id_by_name(booking["room_name"])
                period_id = self.get_period_id_by_name(booking["period_name"])
                notes = booking["notes"]
                current_booking = self.get_booking_by_date_room_id_period_id(date, room_id, period_id)
                if current_booking is None:
                    self.add_booking(room_id, period_id, notes, self.convert_date_to_str(date))
                else:
                    print(f"Conflict booking {booking}")
