#!/usr/bin/env python

from pathlib import Path
from asctt2012.timetable import Timetable as Tt
from xsdata.formats.dataclass.parsers import XmlParser
from pprint import PrettyPrinter
from dataclasses import dataclass

pprint = PrettyPrinter(indent=4).pprint

@dataclass
class Teaching:
    classroom_name: str
    period_name: str
    weekday: int
    notes: str

class Timetable:
    def __init__(self):
        xml_string = Path("asctt2012.xml").read_text()
        parser = XmlParser()
        self.timetable = parser.from_string(xml_string, Tt)

    def get_periods(self):
        return self.timetable.periods.period

    def get_classrooms(self):
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

    def get_item_by_field(self, items, field, field_value):
        for i in items:
            i_field = getattr(i, field)
            if i_field is not None:
                if i_field == field_value:
                    return i
        else:
            return None

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

    def convert_days_to_weekday(self, days):
        if days == 1:
            return 5
        elif days == 10:
            return 4
        elif days == 100:
            return 3
        elif days == 1000:
            return 2
        elif days == 10000:
            return 1
        else:
            #TODO: if multiple days?
            raise Exception(f"Missing day {days} in match case")

    def get_teachings(self):
        teachings = []
        cards = list(self.get_cards())
        for card in cards:
            lesson = self.get_item_by_id(self.get_lessons(), card.lessonid)
            classrooms = self.get_items_by_ids(self.get_classrooms(), card.classroomids)
            weekday = self.convert_days_to_weekday(card.days)
            classnames = self.get_items_by_ids(self.get_classes(), lesson.classids)
            teachers = self.get_items_by_ids(self.get_teachers(), lesson.teacherids)
            subject = self.get_item_by_id(self.get_subjects(), lesson.subjectid)
            match len(classrooms):
                case 1:
                    classroom_name = classrooms[0].name
                    period = self.get_item_by_field(self.get_periods(), "period", card.period)
                    period_name = period.name
                    teachers = ", ".join(x.name for x in teachers)
                    subject_name = subject.name
                    classnames = ", ".join(x.name for x in classnames)
                    notes = f"{classnames}, {subject_name}, {teachers}"

                    teachings.append(Teaching(classroom_name, period_name, weekday, notes))
                case 0:
                    pass
                case _:
                    raise Exception(f"More then one classrooms in {card}")
        return teachings
