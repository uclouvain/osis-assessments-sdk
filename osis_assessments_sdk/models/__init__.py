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
from osis_assessments_sdk.model.array_of_score_responsible_person import ArrayOfScoreResponsiblePerson
from osis_assessments_sdk.model.current_session import CurrentSession
from osis_assessments_sdk.model.error import Error
from osis_assessments_sdk.model.score_responsible_person import ScoreResponsiblePerson
