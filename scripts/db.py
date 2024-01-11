import mariadb
from credentials import *
import datetime

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
        keys = ', '.join(x for x in data.keys())
        values = str(list(data.values()))[1:-1]
        values = values.replace("None", "NULL")
        query = f"INSERT INTO {table} ({keys}) VALUES ({values});"
        print("TUSAM:", query)
        self.cur.execute(query)
        self.conn.commit()

    def truncate(self, table):
        self.cur.execute("SET FOREIGN_KEY_CHECKS=0;")
        self.cur.execute(f"truncate table {table};")
        self.cur.execute("SET FOREIGN_KEY_CHECKS=1;")
        self.conn.commit()

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

    def add_booking(self, room_id, period_id, classname, date):
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
            'notes': classname,
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

    def add_booking_in_range(self, room_id, period_id, classname, date_start, date_end, weekday):
        date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d').date()
        date_end = datetime.datetime.strptime(date_end, '%Y-%m-%d').date()
        delta = date_end - date_start
        for i in range(delta.days + 1):
            day = date_start + datetime.timedelta(days=i)
            if weekday == day.weekday() + 1:
                self.add_booking(room_id, period_id, classname, str(day))

    def export(self):
        data = {}
        tables = self.execute("show tables;")
        for table in tables:
            table_name = table["Tables_in_crbs_db"]
            data[table_name] = self.execute(f"SELECT * FROM {table_name}")
        print(data)
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



# dodaj session
# dodaj timetable week
# applyan_tjedan_na_polugodiste
# dodaj sobe
# dodaj periods
        
