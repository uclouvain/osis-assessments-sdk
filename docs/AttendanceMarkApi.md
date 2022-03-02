# osis_assessments_sdk.AttendanceMarkApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/assessments*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attendancemarkrequested_list**](AttendanceMarkApi.md#attendancemarkrequested_list) | **GET** /attendance_mark/request/ | 
[**attendancemarkscalendars_list**](AttendanceMarkApi.md#attendancemarkscalendars_list) | **GET** /attendance_mark/calendars/ | 
[**requestattendancemark**](AttendanceMarkApi.md#requestattendancemark) | **POST** /attendance_mark/request/ | 


# **attendancemarkrequested_list**
> [AttendanceMarkRequested] attendancemarkrequested_list()



Return all attendance marks requested during the current session

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import attendance_mark_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.error import Error
from osis_assessments_sdk.model.attendance_mark_requested import AttendanceMarkRequested
from pprint import pprint
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
    api_instance = attendance_mark_api.AttendanceMarkApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attendancemarkrequested_list(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling AttendanceMarkApi->attendancemarkrequested_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[AttendanceMarkRequested]**](AttendanceMarkRequested.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attendancemarkscalendars_list**
> [AttendanceMarkCalendar] attendancemarkscalendars_list()



Return all calendars related to attendance marks.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import attendance_mark_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.error import Error
from osis_assessments_sdk.model.attendance_mark_calendar import AttendanceMarkCalendar
from pprint import pprint
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
    api_instance = attendance_mark_api.AttendanceMarkApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attendancemarkscalendars_list(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling AttendanceMarkApi->attendancemarkscalendars_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[AttendanceMarkCalendar]**](AttendanceMarkCalendar.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requestattendancemark**
> RequestAttendanceMarkCommand requestattendancemark(request_attendance_mark_command)



Request an attendance mark for the current session

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import attendance_mark_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.request_attendance_mark_command import RequestAttendanceMarkCommand
from osis_assessments_sdk.model.error import Error
from pprint import pprint
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
    api_instance = attendance_mark_api.AttendanceMarkApi(api_client)
    request_attendance_mark_command = RequestAttendanceMarkCommand(
        code="Informatique 1",
    ) # RequestAttendanceMarkCommand | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.requestattendancemark(request_attendance_mark_command)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling AttendanceMarkApi->requestattendancemark: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.requestattendancemark(request_attendance_mark_command, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling AttendanceMarkApi->requestattendancemark: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_attendance_mark_command** | [**RequestAttendanceMarkCommand**](RequestAttendanceMarkCommand.md)|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**RequestAttendanceMarkCommand**](RequestAttendanceMarkCommand.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Requested |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

