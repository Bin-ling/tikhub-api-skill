# swagger_client.ToutiaoWebAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_article_info_api_v1_toutiao_web_get_article_info_get**](ToutiaoWebAPIApi.md#get_article_info_api_v1_toutiao_web_get_article_info_get) | **GET** /api/v1/toutiao/web/get_article_info | 获取指定文章的信息/Get information of specified article
[**get_video_info_api_v1_toutiao_web_get_video_info_get**](ToutiaoWebAPIApi.md#get_video_info_api_v1_toutiao_web_get_video_info_get) | **GET** /api/v1/toutiao/web/get_video_info | 获取指定视频的信息/Get information of specified video


# **get_article_info_api_v1_toutiao_web_get_article_info_get**
> get_article_info_api_v1_toutiao_web_get_article_info_get(aweme_id)

获取指定文章的信息/Get information of specified article

# [中文] ### 用途: - 获取指定文章的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/article/7450114952884503059/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/article/7450114952884503059/ ### Return: - Post information  # [示例/Example] aweme_id = \"7450114952884503059\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToutiaoWebAPIApi()
aweme_id = NULL # object | 作品ID/Post ID

try:
    # 获取指定文章的信息/Get information of specified article
    api_instance.get_article_info_api_v1_toutiao_web_get_article_info_get(aweme_id)
except ApiException as e:
    print("Exception when calling ToutiaoWebAPIApi->get_article_info_api_v1_toutiao_web_get_article_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | [**object**](.md)| 作品ID/Post ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_info_api_v1_toutiao_web_get_video_info_get**
> get_video_info_api_v1_toutiao_web_get_video_info_get(aweme_id)

获取指定视频的信息/Get information of specified video

# [中文] ### 用途: - 获取指定视频的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/video/7431543350882206242/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified video ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/video/7431543350882206242/ ### Return: - Post information  # [示例/Example] aweme_id = \"7431543350882206242\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToutiaoWebAPIApi()
aweme_id = NULL # object | 作品ID/Post ID

try:
    # 获取指定视频的信息/Get information of specified video
    api_instance.get_video_info_api_v1_toutiao_web_get_video_info_get(aweme_id)
except ApiException as e:
    print("Exception when calling ToutiaoWebAPIApi->get_video_info_api_v1_toutiao_web_get_video_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | [**object**](.md)| 作品ID/Post ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

