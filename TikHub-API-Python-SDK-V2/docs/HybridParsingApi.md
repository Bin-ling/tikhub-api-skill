# swagger_client.HybridParsingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hybrid_parsing_single_video_api_v1_hybrid_video_data_get**](HybridParsingApi.md#hybrid_parsing_single_video_api_v1_hybrid_video_data_get) | **GET** /api/v1/hybrid/video_data | 混合解析单一视频接口/Hybrid parsing single video endpoint
[**hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0**](HybridParsingApi.md#hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0) | **GET** /api/v1/hybrid/video_data | 混合解析单一视频接口/Hybrid parsing single video endpoint


# **hybrid_parsing_single_video_api_v1_hybrid_video_data_get**
> hybrid_parsing_single_video_api_v1_hybrid_video_data_get(url, minimal=minimal, base64_url=base64_url)

混合解析单一视频接口/Hybrid parsing single video endpoint

# [中文] ### 用途: - 该接口用于解析抖音/TikTok单一视频的数据。 ### 参数: - `url`: 视频链接、分享链接、分享文本。 ### 返回: - `data`: 视频数据。  # [English] ### Purpose: - This endpoint is used to parse data of a single Douyin/TikTok video. ### Parameters: - `url`: Video link, share link, or share text. ### Returns: - `data`: Video data.  # [Example] url = \"https://v.douyin.com/L4FJNR3/\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HybridParsingApi()
url = NULL # object | 
minimal = NULL # object | 是否返回最小数据/Whether to return minimal data (optional)
base64_url = NULL # object | 是否Base64编码提交URL/Base64 encoding URL (optional)

try:
    # 混合解析单一视频接口/Hybrid parsing single video endpoint
    api_instance.hybrid_parsing_single_video_api_v1_hybrid_video_data_get(url, minimal=minimal, base64_url=base64_url)
except ApiException as e:
    print("Exception when calling HybridParsingApi->hybrid_parsing_single_video_api_v1_hybrid_video_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)|  | 
 **minimal** | [**object**](.md)| 是否返回最小数据/Whether to return minimal data | [optional] 
 **base64_url** | [**object**](.md)| 是否Base64编码提交URL/Base64 encoding URL | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0**
> hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0(url, minimal=minimal, base64_url=base64_url)

混合解析单一视频接口/Hybrid parsing single video endpoint

# [中文] ### 用途: - 该接口用于解析抖音/TikTok单一视频的数据。 ### 参数: - `url`: 视频链接、分享链接、分享文本。 ### 返回: - `data`: 视频数据。  # [English] ### Purpose: - This endpoint is used to parse data of a single Douyin/TikTok video. ### Parameters: - `url`: Video link, share link, or share text. ### Returns: - `data`: Video data.  # [Example] url = \"https://v.douyin.com/L4FJNR3/\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HybridParsingApi()
url = NULL # object | 
minimal = NULL # object | 是否返回最小数据/Whether to return minimal data (optional)
base64_url = NULL # object | 是否Base64编码提交URL/Base64 encoding URL (optional)

try:
    # 混合解析单一视频接口/Hybrid parsing single video endpoint
    api_instance.hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0(url, minimal=minimal, base64_url=base64_url)
except ApiException as e:
    print("Exception when calling HybridParsingApi->hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)|  | 
 **minimal** | [**object**](.md)| 是否返回最小数据/Whether to return minimal data | [optional] 
 **base64_url** | [**object**](.md)| 是否Base64编码提交URL/Base64 encoding URL | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

