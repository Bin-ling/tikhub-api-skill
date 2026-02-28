# swagger_client.XiguaAppV2APIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get**](XiguaAppV2APIApi.md#fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get) | **GET** /api/v1/xigua/app/v2/fetch_one_video | 获取单个作品数据/Get single video data
[**fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get**](XiguaAppV2APIApi.md#fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get) | **GET** /api/v1/xigua/app/v2/fetch_one_video_play_url | 获取单个作品的播放链接/Get single video play URL
[**fetch_one_video_v2_api_v1_xigua_app_v2_fetch_one_video_v2_get**](XiguaAppV2APIApi.md#fetch_one_video_v2_api_v1_xigua_app_v2_fetch_one_video_v2_get) | **GET** /api/v1/xigua/app/v2/fetch_one_video_v2 | 获取单个作品数据 V2/Get single video data V2
[**fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get**](XiguaAppV2APIApi.md#fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get) | **GET** /api/v1/xigua/app/v2/fetch_user_info | 个人信息/Personal information
[**fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get**](XiguaAppV2APIApi.md#fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get) | **GET** /api/v1/xigua/app/v2/fetch_user_post_list | 获取个人作品列表/Get user post list
[**fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get**](XiguaAppV2APIApi.md#fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get) | **GET** /api/v1/xigua/app/v2/fetch_video_comment_list | 视频评论列表/Video comment list
[**search_video_api_v1_xigua_app_v2_search_video_get**](XiguaAppV2APIApi.md#search_video_api_v1_xigua_app_v2_search_video_get) | **GET** /api/v1/xigua/app/v2/search_video | 搜索视频/Search video


# **fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get**
> fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get(item_id)

获取单个作品数据/Get single video data

# [中文] ### 用途: - 获取单个作品数据（信息较少，不包含标题等信息，但是包含相关视频的信息） ### 参数: - item_id: 作品id ### 返回: - 作品数据，其中包含视频链接的Base64编码播放地址，需要前端解码后使用，或者使用 /fetch_one_video_play_url 获取播放链接。  # [English] ### Purpose: - Get single video data (less information, does not include title and other information, but includes information about related videos) ### Parameters: - item_id: Video id ### Return: - Video data, which contains the Base64 encoded playback address of the video link, which needs to be decoded and used by the front end, or use /fetch_one_video_play_url to get the playback link.  # [示例/Example] item_id: \"7354954305222377999\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiguaAppV2APIApi()
item_id = NULL # object | 作品id/Video id

try:
    # 获取单个作品数据/Get single video data
    api_instance.fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get(item_id)
except ApiException as e:
    print("Exception when calling XiguaAppV2APIApi->fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**object**](.md)| 作品id/Video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get**
> fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get(item_id)

获取单个作品的播放链接/Get single video play URL

# [中文] ### 用途: - 获取单个作品的播放链接，此接口返回的是已经解码后的播放链接，可以直接使用。 ### 参数: - item_id: 作品id ### 返回: - 作品的播放链接的明文链接。  # [English] ### Purpose: - Get single video play URL, the interface returns the decoded play URL, which can be used directly. ### Parameters: - item_id: Video id ### Return: - Play URL of the video, plaintext link.  # [示例/Example] item_id: \"7354954305222377999\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiguaAppV2APIApi()
item_id = NULL # object | 作品id/Video id

try:
    # 获取单个作品的播放链接/Get single video play URL
    api_instance.fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get(item_id)
except ApiException as e:
    print("Exception when calling XiguaAppV2APIApi->fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**object**](.md)| 作品id/Video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_v2_api_v1_xigua_app_v2_fetch_one_video_v2_get**
> fetch_one_video_v2_api_v1_xigua_app_v2_fetch_one_video_v2_get(item_id)

获取单个作品数据 V2/Get single video data V2

# [中文] ### 用途: - 获取单个作品数据（信息全面，包含标题等信息，但是不包含相关视频推荐信息） ### 参数: - item_id: 作品id ### 返回: - 作品数据，其中包含视频链接的Base64编码播放地址，需要前端解码后使用，或者使用 /fetch_one_video_play_url 获取播放链接。  # [English] ### Purpose: - Get single video data (more comprehensive information, including title and other information, but not including information about related video recommendations) ### Parameters: - item_id: Video id ### Return: - Video data, which contains the Base64 encoded playback address of the video link, which needs to be decoded and used by the front end, or use /fetch_one_video_play_url to get the playback link.  # [示例/Example] item_id: \"7354954305222377999\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiguaAppV2APIApi()
item_id = NULL # object | 作品id/Video id

try:
    # 获取单个作品数据 V2/Get single video data V2
    api_instance.fetch_one_video_v2_api_v1_xigua_app_v2_fetch_one_video_v2_get(item_id)
except ApiException as e:
    print("Exception when calling XiguaAppV2APIApi->fetch_one_video_v2_api_v1_xigua_app_v2_fetch_one_video_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**object**](.md)| 作品id/Video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get**
> fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get(user_id)

个人信息/Personal information

# [中文] ### 用途: - 个人信息 ### 参数: - user_id: 用户id ### 返回: - 个人信息  # [English] ### Purpose: - Personal information ### Parameters: - user_id: User id ### Return: - Personal information  # [示例/Example] user_id: \"52712347586\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiguaAppV2APIApi()
user_id = NULL # object | 用户id/User id

try:
    # 个人信息/Personal information
    api_instance.fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get(user_id)
except ApiException as e:
    print("Exception when calling XiguaAppV2APIApi->fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户id/User id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get**
> fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get(user_id, max_behot_time=max_behot_time)

获取个人作品列表/Get user post list

# [中文] ### 用途: - 获取个人作品列表 ### 参数: - user_id: 用户id - max_behot_time: 最大行为时间，默认空，第一次请求传空，后续请求传上一次请求返回数据中的JSON中的值。 - max_behot_time的值可以是JSON路径为：$.data.data.[-1].behot_time - 也就是data中的最后一个元素的cursor值 ### 返回: - 作品列表  # [English] ### Purpose: - Get user post list ### Parameters: - user_id: User id - max_behot_time: Maximum behavior time, default empty, pass empty for the first request, pass the max_behot_time returned by the previous request for subsequent requests - The value of max_behot_time can be the JSON path: $.data.data.[-1].behot_time - That is, the cursor value of the last element in data ### Return: - Post list  # [示例/Example] user_id = \"1922379661976311\" max_behot_time = \"\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiguaAppV2APIApi()
user_id = NULL # object | 用户id/User id
max_behot_time = NULL # object | 最大行为时间/Maximum behavior time (optional)

try:
    # 获取个人作品列表/Get user post list
    api_instance.fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get(user_id, max_behot_time=max_behot_time)
except ApiException as e:
    print("Exception when calling XiguaAppV2APIApi->fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户id/User id | 
 **max_behot_time** | [**object**](.md)| 最大行为时间/Maximum behavior time | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get**
> fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get(item_id, offset=offset, count=count)

视频评论列表/Video comment list

# [中文] ### 用途: - 视频评论列表 ### 参数: - item_id: 作品id - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset - count: 数量，默认20，建议保持默认。 ### 返回: - 评论列表  # [English] ### Purpose: - Video comment list ### Parameters: - item_id: Video id - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests - count: Quantity, default 20, it is recommended to keep the default. ### Return: - Comment list  # [示例/Example] item_id: \"7354954305222377999\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiguaAppV2APIApi()
item_id = NULL # object | 作品id/Video id
offset = NULL # object | 偏移量/Offset (optional)
count = NULL # object | 数量/Count (optional)

try:
    # 视频评论列表/Video comment list
    api_instance.fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get(item_id, offset=offset, count=count)
except ApiException as e:
    print("Exception when calling XiguaAppV2APIApi->fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**object**](.md)| 作品id/Video id | 
 **offset** | [**object**](.md)| 偏移量/Offset | [optional] 
 **count** | [**object**](.md)| 数量/Count | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_video_api_v1_xigua_app_v2_search_video_get**
> search_video_api_v1_xigua_app_v2_search_video_get(keyword, offset=offset, order_type=order_type, min_duration=min_duration, max_duration=max_duration)

搜索视频/Search video

# [中文] ### 用途: - 搜索视频 ### 参数: - keyword: 关键词 - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset - order_type: 排序方式，为空时按照默认排序，以下为可选排序方式。     - 最新: publish_time     - 最热: play_count - min_duration: 最小时长，默认空，单位秒。 - max_duration: 最大时长，默认空，单位秒。 ### 返回: - 视频列表  # [English] ### Purpose: - Search video ### Parameters: - keyword: Keyword - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests - order_type: Order type, empty for default sorting, the following are optional sorting methods.     - Newest: publish_time     - Hottest: play_count - min_duration: Minimum duration, default empty, in seconds. - max_duration: Maximum duration, default empty, in seconds. ### Return: - Video list  # [示例/Example] > 搜索关键字为“抖音”的视频，按照播放量排序，时长1-180秒(1-3分钟) > Search for videos with the keyword \"抖音\", sorted by play count, duration 1-180 seconds (1-3 minutes) keyword: \"抖音\" order_type: \"play_count\" min_duration: 1 max_duration: 180

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiguaAppV2APIApi()
keyword = NULL # object | 关键词/Keyword
offset = NULL # object | 偏移量/Offset (optional)
order_type = NULL # object | 排序方式/Order type (optional)
min_duration = NULL # object | 最小时长/Minimum duration (optional)
max_duration = NULL # object | 最大时长/Maximum duration (optional)

try:
    # 搜索视频/Search video
    api_instance.search_video_api_v1_xigua_app_v2_search_video_get(keyword, offset=offset, order_type=order_type, min_duration=min_duration, max_duration=max_duration)
except ApiException as e:
    print("Exception when calling XiguaAppV2APIApi->search_video_api_v1_xigua_app_v2_search_video_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 关键词/Keyword | 
 **offset** | [**object**](.md)| 偏移量/Offset | [optional] 
 **order_type** | [**object**](.md)| 排序方式/Order type | [optional] 
 **min_duration** | [**object**](.md)| 最小时长/Minimum duration | [optional] 
 **max_duration** | [**object**](.md)| 最大时长/Maximum duration | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

