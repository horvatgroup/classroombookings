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
