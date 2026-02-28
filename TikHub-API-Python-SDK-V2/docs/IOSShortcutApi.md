# swagger_client.IOSShortcutApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shortcut_api_v1_ios_shortcut_shortcut_get**](IOSShortcutApi.md#get_shortcut_api_v1_ios_shortcut_shortcut_get) | **GET** /api/v1/ios_shortcut/shortcut | 用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts


# **get_shortcut_api_v1_ios_shortcut_shortcut_get**
> get_shortcut_api_v1_ios_shortcut_shortcut_get()

用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IOSShortcutApi()

try:
    # 用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts
    api_instance.get_shortcut_api_v1_ios_shortcut_shortcut_get()
except ApiException as e:
    print("Exception when calling IOSShortcutApi->get_shortcut_api_v1_ios_shortcut_shortcut_get: %s\n" % e)
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

