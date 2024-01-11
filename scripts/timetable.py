#!/usr/bin/env python

from pathlib import Path
from asctt2012.timetable import Timetable as Tt
from xsdata.formats.dataclass.parsers import XmlParser

class Timetable:
    def __init__(self):
        xml_string = Path("asctt2012.xml").read_text()
        parser = XmlParser()
        self.timetable = parser.from_string(xml_string, Tt)

    def get_periods(self):
        return self.timetable.periods.period

    def get_rooms(self):
        return self.timetable.classrooms.classroom

    def get_classes(self):
        return self.timetable.classes.class_value

    def get_teachers(self):
        return self.timetable.teachers.teacher

    def get_subjects(self):
        return self.timetable.subjects.subject

    def get_groups(self):
        return self.timetable.groups.group

    def get_lessons(self):
        return self.timetable.lessons.lesson

    def get_cards(self):
        return self.timetable.cards.card

    def get_item_by_id(self, items, id):
        for i in items:
            if id == i.id:
                return i
        else:
            return None

    def get_items_by_ids(self, items, ids):
        data = []
        for id in ids.split(","):
            for i in items:
                if id == i.id:
                    data.append(i)
        return data

    def convert_days(self, days):
        match days:
            case 1:
                return 5
            case 10:
                return 4
            case 100:
                return 3
            case 1000:
                return 2
            case 10000:
                return 1
            case _:
                #TODO: if multiple days?
                raise Exception(f"Missing day {days} in match case")

    def parse_cards(self):
        cards = self.get_cards()
        for card in cards[:10]:
            card.days = self.convert_days(card.days)
            card.classroomids = self.get_items_by_ids(self.get_rooms(), card.classroomids)
            print(card)
