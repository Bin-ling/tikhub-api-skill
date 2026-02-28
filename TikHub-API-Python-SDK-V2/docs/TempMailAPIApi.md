# swagger_client.TempMailAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get**](TempMailAPIApi.md#get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get) | **GET** /api/v1/temp_mail/v1/get_email_by_id | Get Email By Id
[**get_emails_api_v1_temp_mail_v1_get_emails_inbox_get**](TempMailAPIApi.md#get_emails_api_v1_temp_mail_v1_get_emails_inbox_get) | **GET** /api/v1/temp_mail/v1/get_emails_inbox | Get Emails
[**get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get**](TempMailAPIApi.md#get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get) | **GET** /api/v1/temp_mail/v1/get_temp_email_address | Get Temp Email


# **get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get**
> get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get(token, message_id)

Get Email By Id

# [中文] ### 用途: - 通过邮件ID获取邮件数据 ### 参数: - token: 邮箱Bearer Token - message_id: 邮件ID ### 返回: - 邮件数据  # [English] ### Purpose: - Get email data by email ID ### Parameters: - token: Email Bearer Token - message_id: Email ID ### Returns: - Email data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TempMailAPIApi()
token = NULL # object | Bearer Token
message_id = NULL # object | Message ID

try:
    # Get Email By Id
    api_instance.get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get(token, message_id)
except ApiException as e:
    print("Exception when calling TempMailAPIApi->get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**object**](.md)| Bearer Token | 
 **message_id** | [**object**](.md)| Message ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emails_api_v1_temp_mail_v1_get_emails_inbox_get**
> get_emails_api_v1_temp_mail_v1_get_emails_inbox_get(token)

Get Emails

# [中文] ### 用途: - 获取邮件列表 ### 参数: - token: 邮箱Bearer Token ### 返回: - emails: 邮件列表  # [English] ### Purpose: - Get a list of emails ### Parameters: - token: Email Bearer Token ### Returns: - emails: List of emails

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TempMailAPIApi()
token = NULL # object | Bearer Token

try:
    # Get Emails
    api_instance.get_emails_api_v1_temp_mail_v1_get_emails_inbox_get(token)
except ApiException as e:
    print("Exception when calling TempMailAPIApi->get_emails_api_v1_temp_mail_v1_get_emails_inbox_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**object**](.md)| Bearer Token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get**
> get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get()

Get Temp Email

# [中文] ### 用途: - 获取一个临时邮箱地址 - 用于注册或者接收邮件，该邮箱地址不会被删除，也不会被其他人使用。 - 该邮箱无法发送邮件，只能接收邮件。 - 请自行保存邮箱地址、用户名、密码、Bearer Token，我们无法帮助您找回这些关键信息。 ### 参数: - 无 ### 返回: - domain: 邮箱域名 - name: 邮箱用户名 - password: 邮箱密码 - email_address: 邮箱地址 - token: 邮箱Bearer Token  # [English] ### Purpose: - Get a temporary email address - Used for registration or receiving emails, this email address will not be deleted or used by others. - This email cannot send emails, only receive emails. - Please save the email address, username, password, and Bearer Token yourself, we cannot help you retrieve this critical information. ### Parameters: - None ### Returns: - domain: Email domain - name: Email username - password: Email password - email_address: Email address - token: Email Bearer Token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TempMailAPIApi()

try:
    # Get Temp Email
    api_instance.get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get()
except ApiException as e:
    print("Exception when calling TempMailAPIApi->get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

