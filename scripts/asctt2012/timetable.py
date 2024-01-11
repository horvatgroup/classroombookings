from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Buildings:
    class Meta:
        name = "buildings"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Card:
    class Meta:
        name = "card"

    lessonid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    classroomids: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    period: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    weeks: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    terms: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    days: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Class:
    class Meta:
        name = "class"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    short: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    teacherid: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    classroomids: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    grade: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    partner_id: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Classroom:
    class Meta:
        name = "classroom"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    short: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    buildingid: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    partner_id: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Daysdef:
    class Meta:
        name = "daysdef"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    short: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    days: Optional[Union[int, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Grade:
    class Meta:
        name = "grade"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    short: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    grade: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Group:
    class Meta:
        name = "group"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    classid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    studentids: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    entireclass: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    divisiontag: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Lesson:
    class Meta:
        name = "lesson"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    classids: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    subjectid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    periodspercard: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    periodsperweek: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    teacherids: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    classroomids: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    groupids: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    seminargroup: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    termsdefid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    weeksdefid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    daysdefid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    capacity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    partner_id: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Period:
    class Meta:
        name = "period"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    short: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    period: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    starttime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    endtime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Students:
    class Meta:
        name = "students"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Studentsubjects:
    class Meta:
        name = "studentsubjects"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Subject:
    class Meta:
        name = "subject"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    short: Optional[Union[str, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    partner_id: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Teacher:
    class Meta:
        name = "teacher"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    firstname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    lastname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    short: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    gender: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    email: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mobile: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    partner_id: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Termsdef:
    class Meta:
        name = "termsdef"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    short: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    terms: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Weeksdef:
    class Meta:
        name = "weeksdef"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    short: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    weeks: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Cards:
    class Meta:
        name = "cards"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    card: List[Card] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Classes:
    class Meta:
        name = "classes"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    class_value: List[Class] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Classrooms:
    class Meta:
        name = "classrooms"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    classroom: List[Classroom] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Daysdefs:
    class Meta:
        name = "daysdefs"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    daysdef: List[Daysdef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Grades:
    class Meta:
        name = "grades"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    grade: List[Grade] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Groups:
    class Meta:
        name = "groups"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    group: List[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Lessons:
    class Meta:
        name = "lessons"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    lesson: List[Lesson] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Periods:
    class Meta:
        name = "periods"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    period: List[Period] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Subjects:
    class Meta:
        name = "subjects"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    subject: List[Subject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Teachers:
    class Meta:
        name = "teachers"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    teacher: List[Teacher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Termsdefs:
    class Meta:
        name = "termsdefs"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    termsdef: Optional[Termsdef] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Weeksdefs:
    class Meta:
        name = "weeksdefs"

    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    weeksdef: Optional[Weeksdef] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Timetable:
    class Meta:
        name = "timetable"

    importtype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    options: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    defaultexport: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    displayname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    displaycountries: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    periods: Optional[Periods] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    daysdefs: Optional[Daysdefs] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    weeksdefs: Optional[Weeksdefs] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    termsdefs: Optional[Termsdefs] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    subjects: Optional[Subjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    teachers: Optional[Teachers] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    buildings: Optional[Buildings] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    classrooms: Optional[Classrooms] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    grades: Optional[Grades] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    classes: Optional[Classes] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    groups: Optional[Groups] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    students: Optional[Students] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    studentsubjects: Optional[Studentsubjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    lessons: Optional[Lessons] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    cards: Optional[Cards] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
