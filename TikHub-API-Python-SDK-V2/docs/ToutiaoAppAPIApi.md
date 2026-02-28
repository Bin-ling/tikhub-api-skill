# swagger_client.ToutiaoAppAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_article_info_api_v1_toutiao_app_get_article_info_get**](ToutiaoAppAPIApi.md#get_article_info_api_v1_toutiao_app_get_article_info_get) | **GET** /api/v1/toutiao/app/get_article_info | 获取指定文章的信息/Get information of specified article
[**get_comments_api_v1_toutiao_app_get_comments_get**](ToutiaoAppAPIApi.md#get_comments_api_v1_toutiao_app_get_comments_get) | **GET** /api/v1/toutiao/app/get_comments | 获取指定作品的评论/Get comments of specified post
[**get_user_id_api_v1_toutiao_app_get_user_id_get**](ToutiaoAppAPIApi.md#get_user_id_api_v1_toutiao_app_get_user_id_get) | **GET** /api/v1/toutiao/app/get_user_id | 从头条用户主页获取用户user_id/Get user_id from user profile
[**get_user_info_api_v1_toutiao_app_get_user_info_get**](ToutiaoAppAPIApi.md#get_user_info_api_v1_toutiao_app_get_user_info_get) | **GET** /api/v1/toutiao/app/get_user_info | 获取指定用户的信息/Get information of specified user
[**get_video_info_api_v1_toutiao_app_get_video_info_get**](ToutiaoAppAPIApi.md#get_video_info_api_v1_toutiao_app_get_video_info_get) | **GET** /api/v1/toutiao/app/get_video_info | 获取指定视频的信息/Get information of specified video


# **get_article_info_api_v1_toutiao_app_get_article_info_get**
> get_article_info_api_v1_toutiao_app_get_article_info_get(group_id)

获取指定文章的信息/Get information of specified article

# [中文] ### 用途: - 获取指定文章的信息 ### 参数: - group_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/article/7450114952884503059/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - group_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/article/7450114952884503059/ ### Return: - Post information  # [示例/Example] group_id = \"7450114952884503059\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToutiaoAppAPIApi()
group_id = NULL # object | 作品ID/Post ID

try:
    # 获取指定文章的信息/Get information of specified article
    api_instance.get_article_info_api_v1_toutiao_app_get_article_info_get(group_id)
except ApiException as e:
    print("Exception when calling ToutiaoAppAPIApi->get_article_info_api_v1_toutiao_app_get_article_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| 作品ID/Post ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments_api_v1_toutiao_app_get_comments_get**
> get_comments_api_v1_toutiao_app_get_comments_get(group_id, offset)

获取指定作品的评论/Get comments of specified post

# [中文] ### 用途: - 获取指定作品的评论 ### 参数: - group_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/i7453372680222523931/ - offset: 偏移量，用于分页，默认为0，然后每次加20 ### 返回: - 评论列表  # [English] ### Purpose: - Get comments of specified post ### Parameters: - group_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/i7453372680222523931/ - offset: Offset, used for pagination, default is 0, then add 20 each time ### Return: - Comment list  # [示例/Example] group_id = \"7453372680222523931\" offset = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToutiaoAppAPIApi()
group_id = NULL # object | 作品ID/Post ID
offset = NULL # object | 偏移量/Offset

try:
    # 获取指定作品的评论/Get comments of specified post
    api_instance.get_comments_api_v1_toutiao_app_get_comments_get(group_id, offset)
except ApiException as e:
    print("Exception when calling ToutiaoAppAPIApi->get_comments_api_v1_toutiao_app_get_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| 作品ID/Post ID | 
 **offset** | [**object**](.md)| 偏移量/Offset | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_id_api_v1_toutiao_app_get_user_id_get**
> get_user_id_api_v1_toutiao_app_get_user_id_get(user_profile_url)

从头条用户主页获取用户user_id/Get user_id from user profile

# [中文] ### 用途: - 从头条用户主页获取用户user_id ### 参数: - user_profile_url: 用户主页链接     - 例如: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/ ### 返回: - 用户ID  # [English] ### Purpose: - Get user_id from user profile ### Parameters: - user_profile_url: User profile URL     - For example: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/ ### Return: - User ID  # [示例/Example] user_profile_url = \"https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToutiaoAppAPIApi()
user_profile_url = NULL # object | 用户主页链接/User profile URL

try:
    # 从头条用户主页获取用户user_id/Get user_id from user profile
    api_instance.get_user_id_api_v1_toutiao_app_get_user_id_get(user_profile_url)
except ApiException as e:
    print("Exception when calling ToutiaoAppAPIApi->get_user_id_api_v1_toutiao_app_get_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile_url** | [**object**](.md)| 用户主页链接/User profile URL | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_info_api_v1_toutiao_app_get_user_info_get**
> get_user_info_api_v1_toutiao_app_get_user_info_get(user_id)

获取指定用户的信息/Get information of specified user

# [中文] ### 用途: - 获取指定用户的信息 ### 参数: - user_id: 用户ID，可以从以下接口获取：     - `/api/v1/toutiao/app/get_user_id` ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - user_id: User ID, can be obtained from the following API:     - `/api/v1/toutiao/app/get_user_id` ### Return: - User information  # [示例/Example] user_id = \"1352838578180211\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToutiaoAppAPIApi()
user_id = NULL # object | 用户ID/User ID

try:
    # 获取指定用户的信息/Get information of specified user
    api_instance.get_user_info_api_v1_toutiao_app_get_user_info_get(user_id)
except ApiException as e:
    print("Exception when calling ToutiaoAppAPIApi->get_user_info_api_v1_toutiao_app_get_user_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_info_api_v1_toutiao_app_get_video_info_get**
> get_video_info_api_v1_toutiao_app_get_video_info_get(group_id)

获取指定视频的信息/Get information of specified video

# [中文] ### 用途: - 获取指定视频的信息 ### 参数: - group_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/video/7431543350882206242/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified video ### Parameters: - group_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/video/7431543350882206242/ ### Return: - Post information  # [示例/Example] group_id = \"7431543350882206242\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToutiaoAppAPIApi()
group_id = NULL # object | 作品ID/Post ID

try:
    # 获取指定视频的信息/Get information of specified video
    api_instance.get_video_info_api_v1_toutiao_app_get_video_info_get(group_id)
except ApiException as e:
    print("Exception when calling ToutiaoAppAPIApi->get_video_info_api_v1_toutiao_app_get_video_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| 作品ID/Post ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

