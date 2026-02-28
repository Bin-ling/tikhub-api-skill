# swagger_client.XiaohongshuWebV2APIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get**](XiaohongshuWebV2APIApi.md#fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_feed_notes | 获取单一笔记和推荐笔记 V1 (已弃用)/Fetch one note and feed notes V1 (deprecated)
[**fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get**](XiaohongshuWebV2APIApi.md#fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_feed_notes_v2 | 获取单一笔记和推荐笔记 V2/Fetch one note and feed notes V2(v2稳定, 推荐使用此接口)
[**fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get**](XiaohongshuWebV2APIApi.md#fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_feed_notes_v3 | 获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)
[**fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get**](XiaohongshuWebV2APIApi.md#fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_feed_notes_v4 | 获取单一笔记和推荐笔记 V4 (互动量有延迟)/Fetch one note and feed notes V4 (interaction volume has a delay)
[**fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get**](XiaohongshuWebV2APIApi.md#fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_feed_notes_v5 | 获取单一笔记和推荐笔记 V5 (互动量有缺失)/Fetch one note and feed notes V5 (interaction volume has a missing)
[**fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get**](XiaohongshuWebV2APIApi.md#fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_follower_list | 获取用户粉丝列表/Fetch follower list
[**fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get**](XiaohongshuWebV2APIApi.md#fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_following_list | 获取用户关注列表/Fetch following list
[**fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get**](XiaohongshuWebV2APIApi.md#fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_home_notes | 获取Web用户主页笔记/Fetch web user profile notes
[**fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get**](XiaohongshuWebV2APIApi.md#fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_home_notes_app | 获取App用户主页笔记/Fetch App user home notes
[**fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get**](XiaohongshuWebV2APIApi.md#fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_hot_list | 获取小红书热榜/Fetch Xiaohongshu hot list
[**fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get**](XiaohongshuWebV2APIApi.md#fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_note_comments | 获取笔记评论/Fetch note comments
[**fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get**](XiaohongshuWebV2APIApi.md#fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_note_image | 获取小红书笔记图片/Fetch Xiaohongshu note image
[**fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get**](XiaohongshuWebV2APIApi.md#fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_product_list | 获取小红书商品列表/Fetch Xiaohongshu product list
[**fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get**](XiaohongshuWebV2APIApi.md#fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_search_notes | 获取搜索笔记/Fetch search notes
[**fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get**](XiaohongshuWebV2APIApi.md#fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_search_users | 获取搜索用户/Fetch search users
[**fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get**](XiaohongshuWebV2APIApi.md#fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_sub_comments | 获取子评论/Fetch sub comments
[**fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get**](XiaohongshuWebV2APIApi.md#fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_user_info_app | 获取App用户信息/Fetch App user info
[**fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get**](XiaohongshuWebV2APIApi.md#fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get) | **GET** /api/v1/xiaohongshu/web_v2/fetch_user_info | 获取用户信息/Fetch user info


# **fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get**
> fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get(note_id)

获取单一笔记和推荐笔记 V1 (已弃用)/Fetch one note and feed notes V1 (deprecated)

# [中文] ### 用途: - 获取单一笔记和推荐笔记 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
note_id = NULL # object | 笔记ID/Note ID

try:
    # 获取单一笔记和推荐笔记 V1 (已弃用)/Fetch one note and feed notes V1 (deprecated)
    api_instance.fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get(note_id)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | [**object**](.md)| 笔记ID/Note ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get**
> fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get(note_id)

获取单一笔记和推荐笔记 V2/Fetch one note and feed notes V2(v2稳定, 推荐使用此接口)

# [中文] ### 用途: - 获取单一笔记和推荐笔记 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
note_id = NULL # object | 笔记ID/Note ID

try:
    # 获取单一笔记和推荐笔记 V2/Fetch one note and feed notes V2(v2稳定, 推荐使用此接口)
    api_instance.fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get(note_id)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | [**object**](.md)| 笔记ID/Note ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get**
> fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get(short_url)

获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)

# [中文] ### 用途: - 获取单一笔记和推荐笔记 ### 参数: - short_url: 短链，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes ### Parameters: - short_url: Short URL, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] short_url = \"http://xhslink.com/a/tyoREa3ciaAeb\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
short_url = NULL # object | 短链/Short URL

try:
    # 获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)
    api_instance.fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get(short_url)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_url** | [**object**](.md)| 短链/Short URL | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get**
> fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get(note_id)

获取单一笔记和推荐笔记 V4 (互动量有延迟)/Fetch one note and feed notes V4 (interaction volume has a delay)

# [中文] ### 用途: - 获取单一笔记和推荐笔记，结构不同互动量有延时 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes, the structure is different and the interaction volume has a delay ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
note_id = NULL # object | 笔记ID/Note ID

try:
    # 获取单一笔记和推荐笔记 V4 (互动量有延迟)/Fetch one note and feed notes V4 (interaction volume has a delay)
    api_instance.fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get(note_id)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | [**object**](.md)| 笔记ID/Note ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get**
> fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get(note_id)

获取单一笔记和推荐笔记 V5 (互动量有缺失)/Fetch one note and feed notes V5 (interaction volume has a missing)

# [中文] ### 用途: - 获取单一笔记和推荐笔记，结构不同互动量有缺失 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记 ### 备注: - 互动数据仅有点赞数，没有评论数与收藏数  # [English] ### Purpose: - Get one note and feed notes, the structure is different and the interaction volume has a missing ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes ### Notes: - Interaction data only includes likes, without comments and favorites.  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
note_id = NULL # object | 笔记ID/Note ID

try:
    # 获取单一笔记和推荐笔记 V5 (互动量有缺失)/Fetch one note and feed notes V5 (interaction volume has a missing)
    api_instance.fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get(note_id)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | [**object**](.md)| 笔记ID/Note ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get**
> fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get(user_id, cursor=cursor)

获取用户粉丝列表/Fetch follower list

# [中文] ### 用途: - 获取用户粉丝列表 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 用户粉丝列表  # [English] ### Purpose: - Get follower list ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Follower list  # [示例/Example] user_id = \"604a28420000000001005211\" cursor = \"\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
user_id = NULL # object | 用户ID/User ID
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取用户粉丝列表/Fetch follower list
    api_instance.fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get(user_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get**
> fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get(user_id, cursor=cursor)

获取用户关注列表/Fetch following list

# [中文] ### 用途: - 获取用户关注列表 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 用户关注列表  # [English] ### Purpose: - Get following list ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Following list  # [示例/Example] user_id = \"604a28420000000001005211\" cursor = \"\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
user_id = NULL # object | 用户ID/User ID
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取用户关注列表/Fetch following list
    api_instance.fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get(user_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get**
> fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get(user_id, cursor=cursor)

获取Web用户主页笔记/Fetch web user profile notes

# [中文] ### 用途: - 获取主页笔记 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 主页笔记  # [English] ### Purpose: - Get home notes ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Home notes  # [示例/Example] user_id = \"5f3e0d00000000001f03a4bc\" cursor = \"\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
user_id = NULL # object | 用户ID/User ID
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取Web用户主页笔记/Fetch web user profile notes
    api_instance.fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get(user_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get**
> fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get(user_id, cursor=cursor)

获取App用户主页笔记/Fetch App user home notes

# [中文] ### 用途: - 获取App主页笔记 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 主页笔记  # [English] ### Purpose: - Get home notes ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Home notes  # [示例/Example] user_id = \"5f3e0d00000000001f03a4bc\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
user_id = NULL # object | 用户ID/User ID
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取App用户主页笔记/Fetch App user home notes
    api_instance.fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get(user_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get**
> fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get()

获取小红书热榜/Fetch Xiaohongshu hot list

# [中文] ### 用途: - 获取小红书热榜 ### 返回: - 小红书热榜  # [English] ### Purpose: - Get Xiaohongshu hot list ### Return: - Xiaohongshu hot list  # [示例/Example]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()

try:
    # 获取小红书热榜/Fetch Xiaohongshu hot list
    api_instance.fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get()
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get: %s\n" % e)
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

# **fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get**
> fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get(note_id, cursor=cursor)

获取笔记评论/Fetch note comments

# [中文] ### 用途: - 获取笔记评论 ### 参数: - note_id: 笔记ID - cursor: 游标 ### 返回: - 笔记评论  # [English] ### Purpose: - Get note comments ### Parameters: - note_id: Note ID - cursor: Cursor ### Return: - Note comments  # [示例/Example] note_id = \"651ccaa9000000001f03d7f7\" cursor = \"\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
note_id = NULL # object | 笔记ID/Note ID
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取笔记评论/Fetch note comments
    api_instance.fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get(note_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | [**object**](.md)| 笔记ID/Note ID | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get**
> fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get(note_id)

获取小红书笔记图片/Fetch Xiaohongshu note image

# [中文] ### 用途: - 获取小红书笔记图片 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 小红书笔记图片  # [English] ### Purpose: - Get Xiaohongshu note image ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - Xiaohongshu note image  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
note_id = NULL # object | 笔记ID/Note ID

try:
    # 获取小红书笔记图片/Fetch Xiaohongshu note image
    api_instance.fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get(note_id)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | [**object**](.md)| 笔记ID/Note ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get**
> fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get(user_id, page=page)

获取小红书商品列表/Fetch Xiaohongshu product list

# [中文] ### 用途: - 获取小红书商品列表 ### 参数: - user_id: 用户ID - page: 页码 ### 返回: - 小红书商品列表  # [English] ### Purpose: - Get Xiaohongshu product list ### Parameters: - user_id: User ID - page: Page number ### Return: - Xiaohongshu product list  # [示例/Example] user_id = \"627e35aa00000000210275ae\" page = \"1\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
user_id = NULL # object | 用户ID/User ID
page = NULL # object | 页码/Page number (optional)

try:
    # 获取小红书商品列表/Fetch Xiaohongshu product list
    api_instance.fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get(user_id, page=page)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **page** | [**object**](.md)| 页码/Page number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get**
> fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get(keywords, page=page, sort_type=sort_type, note_type=note_type)

获取搜索笔记/Fetch search notes

# [中文] ### 用途: - 获取搜索笔记 ### 参数: - keywords：搜索关键词 - sort_type：排序方式     - general：综合     - time_descending：最新     - popularity_descending：最热 - note_type: 笔记类型     - 0：全部     - 1：视频     - 2：图文 ### 返回: - 搜索笔记  # [English] ### Purpose: - Get search notes ### Parameters: - keywords: Search keywords - sort_type: Sort type     - general: General     - time_descending: Latest     - popularity_descending: Popular - note_type: Note type     - 0: All     - 1: Video     - 2: Note ### Return: - Search notes  # [示例/Example] keywords = \"口红\" page = 1 sort_type = \"general\" note_type = \"1\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
keywords = NULL # object | 搜索关键词/Search keywords
page = NULL # object | 页码/Page number (optional)
sort_type = NULL # object | 排序方式/Sort type (optional)
note_type = NULL # object | 笔记类型/Note type (optional)

try:
    # 获取搜索笔记/Fetch search notes
    api_instance.fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get(keywords, page=page, sort_type=sort_type, note_type=note_type)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | [**object**](.md)| 搜索关键词/Search keywords | 
 **page** | [**object**](.md)| 页码/Page number | [optional] 
 **sort_type** | [**object**](.md)| 排序方式/Sort type | [optional] 
 **note_type** | [**object**](.md)| 笔记类型/Note type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get**
> fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get(keywords, page=page)

获取搜索用户/Fetch search users

# [中文] ### 用途: - 获取搜索用户 ### 参数: - keywords：搜索关键词 - page：页码 ### 返回: - 搜索用户  # [English] ### Purpose: - Get search users ### Parameters: - keywords: Search keywords - page: Page number ### Return: - Search users  # [示例/Example] keywords = \"口红\" page = 1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
keywords = NULL # object | 搜索关键词/Search keywords
page = NULL # object | 页码/Page number (optional)

try:
    # 获取搜索用户/Fetch search users
    api_instance.fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get(keywords, page=page)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | [**object**](.md)| 搜索关键词/Search keywords | 
 **page** | [**object**](.md)| 页码/Page number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get**
> fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get(note_id, comment_id, cursor=cursor)

获取子评论/Fetch sub comments

# [中文] ### 用途: - 获取子评论 ### 参数: - note_id: 笔记ID - comment_id: 评论ID - cursor: 游标 ### 返回: - 子评论  # [English] ### Purpose: - Get sub comments ### Parameters: - note_id: Note ID - comment_id: Comment ID - cursor: Cursor ### Return: - Sub comments  # [示例/Example] note_id = \"673c894c0000000007033f92\" comment_id = \"673ecdfc000000001503bf8b\" cursor = \"\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
note_id = NULL # object | 笔记ID/Note ID
comment_id = NULL # object | 评论ID/Comment ID
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取子评论/Fetch sub comments
    api_instance.fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get(note_id, comment_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | [**object**](.md)| 笔记ID/Note ID | 
 **comment_id** | [**object**](.md)| 评论ID/Comment ID | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get**
> fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get(user_id)

获取App用户信息/Fetch App user info

# [中文] ### 用途: - 获取用户信息 ### 参数: - user_id: 用户ID ### 返回: - 用户信息  # [English] ### Purpose: - Get user info ### Parameters: - user_id: User ID ### Return: - User info  # [示例/Example] user_id = \"5e3a8ee700000000010070c6\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
user_id = NULL # object | 用户ID/User ID

try:
    # 获取App用户信息/Fetch App user info
    api_instance.fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get(user_id)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get: %s\n" % e)
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

# **fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get**
> fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get(user_id)

获取用户信息/Fetch user info

# [中文] ### 用途: - 获取用户信息 ### 参数: - user_id: 用户ID ### 返回: - 用户信息  # [English] ### Purpose: - Get user info ### Parameters: - user_id: User ID ### Return: - User info  # [示例/Example] user_id = \"5e3a8ee700000000010070c6\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.XiaohongshuWebV2APIApi()
user_id = NULL # object | 用户ID/User ID

try:
    # 获取用户信息/Fetch user info
    api_instance.fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get(user_id)
except ApiException as e:
    print("Exception when calling XiaohongshuWebV2APIApi->fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get: %s\n" % e)
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

