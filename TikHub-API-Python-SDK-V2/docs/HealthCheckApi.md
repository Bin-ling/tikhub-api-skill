# swagger_client.HealthCheckApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_api_v1_health_check_get**](HealthCheckApi.md#health_check_api_v1_health_check_get) | **GET** /api/v1/health/check | 检查服务器是否正确响应请求 / Check if the server responds to requests correctly


# **health_check_api_v1_health_check_get**
> health_check_api_v1_health_check_get()

检查服务器是否正确响应请求 / Check if the server responds to requests correctly

# [中文]  ### 用途说明:  - 检查服务器是否正确响应请求。  ### 参数说明:  - 无参数。  ### 返回结果:  - `status`: 服务器状态，正常为 `ok`。  # [English]  ### Purpose:  - Check if the server responds to requests correctly.  ### Parameter Description:  - No parameters.  ### Return Result:  - `status`: Server status, normal is `ok`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthCheckApi()

try:
    # 检查服务器是否正确响应请求 / Check if the server responds to requests correctly
    api_instance.health_check_api_v1_health_check_get()
except ApiException as e:
    print("Exception when calling HealthCheckApi->health_check_api_v1_health_check_get: %s\n" % e)
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

