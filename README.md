# osis-assessments-sdk
A set of API endpoints that allow you to get score sheet

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.00
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.5

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import osis_assessments_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osis_assessments_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import osis_assessments_sdk
from pprint import pprint
from osis_assessments_sdk.api import score_encoding_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.error import Error
from osis_assessments_sdk.model.score_responsible_person import ScoreResponsiblePerson
from osis_assessments_sdk.model.session_exam import SessionExam
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/assessments
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_assessments_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/assessments"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'


# Enter a context with an instance of the API client
with osis_assessments_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = score_encoding_api.ScoreEncodingApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
x_user_first_name = "X-User-FirstName_example" # str |  (optional)
x_user_last_name = "X-User-LastName_example" # str |  (optional)
x_user_email = "X-User-Email_example" # str |  (optional)
x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    try:
        api_response = api_instance.get_current_session(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->get_current_session: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/assessments*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ScoreEncodingApi* | [**get_current_session**](docs/ScoreEncodingApi.md#get_current_session) | **GET** /sessions/current/ | 
*ScoreEncodingApi* | [**get_next_session**](docs/ScoreEncodingApi.md#get_next_session) | **GET** /sessions/next/ | 
*ScoreEncodingApi* | [**get_previous_session**](docs/ScoreEncodingApi.md#get_previous_session) | **GET** /sessions/previous/ | 
*ScoreEncodingApi* | [**get_score_responsible_list**](docs/ScoreEncodingApi.md#get_score_responsible_list) | **GET** /score_responsibles/ | 
*ScoreEncodingApi* | [**score_sheet_xls_export**](docs/ScoreEncodingApi.md#score_sheet_xls_export) | **GET** /{code}/xls_export | 
*ScoreEncodingApi* | [**score_sheets_pdf_export**](docs/ScoreEncodingApi.md#score_sheets_pdf_export) | **GET** /pdf_export | 


## Documentation For Models

 - [AcceptedLanguageEnum](docs/AcceptedLanguageEnum.md)
 - [Error](docs/Error.md)
 - [ScoreResponsiblePerson](docs/ScoreResponsiblePerson.md)
 - [SessionExam](docs/SessionExam.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in osis_assessments_sdk.apis and osis_assessments_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from osis_assessments_sdk.api.default_api import DefaultApi`
- `from osis_assessments_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import osis_assessments_sdk
from osis_assessments_sdk.apis import *
from osis_assessments_sdk.models import *
```

