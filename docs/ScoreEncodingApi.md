# osis_assessments_sdk.ScoreEncodingApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/assessments*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assessment_email**](ScoreEncodingApi.md#assessment_email) | **GET** /{cohort_name}/email | 
[**get_current_session**](ScoreEncodingApi.md#get_current_session) | **GET** /sessions/current/ | 
[**get_next_session**](ScoreEncodingApi.md#get_next_session) | **GET** /sessions/next/ | 
[**get_overview**](ScoreEncodingApi.md#get_overview) | **GET** /overview/ | 
[**get_previous_session**](ScoreEncodingApi.md#get_previous_session) | **GET** /sessions/previous/ | 
[**get_score_responsible_list**](ScoreEncodingApi.md#get_score_responsible_list) | **GET** /score_responsibles/ | 
[**score_sheet_xls_export**](ScoreEncodingApi.md#score_sheet_xls_export) | **GET** /{code}/xls_export | 
[**score_sheets_pdf_export**](ScoreEncodingApi.md#score_sheets_pdf_export) | **GET** /pdf_export | 


# **assessment_email**
> AssessmentMail assessment_email(cohort_name)



Return the email of score encoding on a specified cohort

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import score_encoding_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.error import Error
from osis_assessments_sdk.model.assessment_mail import AssessmentMail
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
    api_instance = score_encoding_api.ScoreEncodingApi(api_client)
    cohort_name = "cohort_name_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.assessment_email(cohort_name)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->assessment_email: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.assessment_email(cohort_name, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->assessment_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cohort_name** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**AssessmentMail**](AssessmentMail.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_session**
> SessionExam get_current_session()



Return current session

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import score_encoding_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.error import Error
from osis_assessments_sdk.model.session_exam import SessionExam
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
    api_instance = score_encoding_api.ScoreEncodingApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_current_session(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->get_current_session: %s\n" % e)
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

[**SessionExam**](SessionExam.md)

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

# **get_next_session**
> SessionExam get_next_session()



Return next session exam

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import score_encoding_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.error import Error
from osis_assessments_sdk.model.session_exam import SessionExam
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
    api_instance = score_encoding_api.ScoreEncodingApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_next_session(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->get_next_session: %s\n" % e)
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

[**SessionExam**](SessionExam.md)

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

# **get_overview**
> ProgressOverview get_overview()



Return score encoding progress overview for a tutor

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import score_encoding_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.progress_overview import ProgressOverview
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
    api_instance = score_encoding_api.ScoreEncodingApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_overview(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->get_overview: %s\n" % e)
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

[**ProgressOverview**](ProgressOverview.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_previous_session**
> SessionExam get_previous_session()



Return previous session exam

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import score_encoding_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.error import Error
from osis_assessments_sdk.model.session_exam import SessionExam
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
    api_instance = score_encoding_api.ScoreEncodingApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_previous_session(accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->get_previous_session: %s\n" % e)
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

[**SessionExam**](SessionExam.md)

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

# **get_score_responsible_list**
> [ScoreResponsiblePerson] get_score_responsible_list()



Return a list of score responsibles for several learning units.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import score_encoding_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_assessments_sdk.model.error import Error
from osis_assessments_sdk.model.score_responsible_person import ScoreResponsiblePerson
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
    api_instance = score_encoding_api.ScoreEncodingApi(api_client)
    learning_unit_codes = [
        "learning_unit_codes_example",
    ] # [str] |  (optional)
    year = 1 # int |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_score_responsible_list(learning_unit_codes=learning_unit_codes, year=year, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->get_score_responsible_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learning_unit_codes** | **[str]**|  | [optional]
 **year** | **int**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[ScoreResponsiblePerson]**](ScoreResponsiblePerson.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **score_sheet_xls_export**
> file_type score_sheet_xls_export(code)



Return XLS file of score sheet

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import score_encoding_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
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
    api_instance = score_encoding_api.ScoreEncodingApi(api_client)
    code = "code_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.score_sheet_xls_export(code)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->score_sheet_xls_export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.score_sheet_xls_export(code, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->score_sheet_xls_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

**file_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **score_sheets_pdf_export**
> file_type score_sheets_pdf_export()



Return PDF file of score sheet

### Example

* Api Key Authentication (Token):
```python
import time
import osis_assessments_sdk
from osis_assessments_sdk.api import score_encoding_api
from osis_assessments_sdk.model.accepted_language_enum import AcceptedLanguageEnum
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
    api_instance = score_encoding_api.ScoreEncodingApi(api_client)
    codes = [
        "codes_example",
    ] # [str] |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.score_sheets_pdf_export(codes=codes, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_assessments_sdk.ApiException as e:
        print("Exception when calling ScoreEncodingApi->score_sheets_pdf_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codes** | **[str]**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

**file_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

