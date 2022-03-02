# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_assessments_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.attendance_mark_calendar import AttendanceMarkCalendar
from osis_assessments_sdk.model.attendance_mark_requested import AttendanceMarkRequested
from osis_assessments_sdk.model.error import Error
from osis_assessments_sdk.model.learning_unit_progress import LearningUnitProgress
from osis_assessments_sdk.model.progress_overview import ProgressOverview
from osis_assessments_sdk.model.request_attendance_mark_command import RequestAttendanceMarkCommand
from osis_assessments_sdk.model.score_responsible_person import ScoreResponsiblePerson
from osis_assessments_sdk.model.session_exam import SessionExam
