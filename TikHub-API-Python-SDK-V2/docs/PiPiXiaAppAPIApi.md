# swagger_client.PiPiXiaAppAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get**](PiPiXiaAppAPIApi.md#fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get) | **GET** /api/v1/pipixia/app/fetch_hashtag_detail | 获取话题详情/Get hashtag detail
[**fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get**](PiPiXiaAppAPIApi.md#fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get) | **GET** /api/v1/pipixia/app/fetch_hashtag_post_list | 获取话题作品列表/Get hashtag post list
[**fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get**](PiPiXiaAppAPIApi.md#fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get) | **GET** /api/v1/pipixia/app/fetch_home_feed | 获取首页推荐/Get home feed
[**fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get**](PiPiXiaAppAPIApi.md#fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get) | **GET** /api/v1/pipixia/app/fetch_home_short_drama_feed | 获取首页短剧推荐/Get home short drama feed
[**fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get**](PiPiXiaAppAPIApi.md#fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get) | **GET** /api/v1/pipixia/app/fetch_hot_search_board_detail | 获取热搜榜单详情/Get hot search board detail
[**fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get**](PiPiXiaAppAPIApi.md#fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get) | **GET** /api/v1/pipixia/app/fetch_hot_search_board_list | 获取热搜榜单列表/Get hot search board list
[**fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get**](PiPiXiaAppAPIApi.md#fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get) | **GET** /api/v1/pipixia/app/fetch_hot_search_words | 获取热搜词条/Get hot search words
[**fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get**](PiPiXiaAppAPIApi.md#fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get) | **GET** /api/v1/pipixia/app/fetch_increase_post_view_count | 增加作品浏览数/Increase post view count
[**fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get**](PiPiXiaAppAPIApi.md#fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get) | **GET** /api/v1/pipixia/app/fetch_post_comment_list | 获取作品评论列表/Get post comment list
[**fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get**](PiPiXiaAppAPIApi.md#fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get) | **GET** /api/v1/pipixia/app/fetch_post_detail | 获取单个作品数据/Get single video data
[**fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get**](PiPiXiaAppAPIApi.md#fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get) | **GET** /api/v1/pipixia/app/fetch_post_statistics | 获取作品统计数据/Get post statistics
[**fetch_search_api_v1_pipixia_app_fetch_search_get**](PiPiXiaAppAPIApi.md#fetch_search_api_v1_pipixia_app_fetch_search_get) | **GET** /api/v1/pipixia/app/fetch_search | 搜索接口/Search API
[**fetch_short_url_api_v1_pipixia_app_fetch_short_url_get**](PiPiXiaAppAPIApi.md#fetch_short_url_api_v1_pipixia_app_fetch_short_url_get) | **GET** /api/v1/pipixia/app/fetch_short_url | 生成短连接/Generate short URL
[**fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get**](PiPiXiaAppAPIApi.md#fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get) | **GET** /api/v1/pipixia/app/fetch_user_follower_list | 获取用户粉丝列表/Get user follower list
[**fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get**](PiPiXiaAppAPIApi.md#fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get) | **GET** /api/v1/pipixia/app/fetch_user_following_list | 获取用户关注列表/Get user following list
[**fetch_user_info_api_v1_pipixia_app_fetch_user_info_get**](PiPiXiaAppAPIApi.md#fetch_user_info_api_v1_pipixia_app_fetch_user_info_get) | **GET** /api/v1/pipixia/app/fetch_user_info | 获取用户信息/Get user information
[**fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get**](PiPiXiaAppAPIApi.md#fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get) | **GET** /api/v1/pipixia/app/fetch_user_post_list | 获取用户作品列表/Get user post list


# **fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get**
> fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get(hashtag_id)

获取话题详情/Get hashtag detail

# [中文] ### 用途: - 获取话题详情数据。 ### 参数: - hashtag_id: 话题id，可以从分享链接中获取。 ### 返回: - 话题详情数据  # [English] ### Purpose: - Get hashtag detail data. ### Parameters: - hashtag_id: AKA hashtag id, can be obtained from the share link. ### Return: - Hashtag detail data # [示例/Example] hashtag_id = \"129559\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
hashtag_id = NULL # object | 话题id/Hashtag id

try:
    # 获取话题详情/Get hashtag detail
    api_instance.fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get(hashtag_id)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashtag_id** | [**object**](.md)| 话题id/Hashtag id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get**
> fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get(hashtag_id, cursor=cursor, feed_count=feed_count, hashtag_request_type=hashtag_request_type, hashtag_sort_type=hashtag_sort_type)

获取话题作品列表/Get hashtag post list

# [中文] ### 用途: - 获取话题作品列表数据。 ### 参数: - hashtag_id: 话题id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 - feed_count: 翻页数量，默认为0，后续每次翻页加1，比如第一页为0，第二页为1，第三页为2，以此类推。 - hashtag_request_type: 话题请求类型，默认为0，可用值如下：     - 0: 热门     - 1: 最新     - 2: 精华 - hashtag_sort_type: 话题排序类型，默认为3，可用值如下：     - 3: 按热度     - 2: 按时间，从新到旧     - 1: 精华 ### 返回: - 话题作品列表数据  # [English] ### Purpose: - Get hashtag post list data. ### Parameters: - hashtag_id: AKA hashtag id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. - feed_count: Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. ### Return: - Hashtag post list data  # [示例/Example] hashtag_id = \"129559\" cursor = \"0\" feed_count = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
hashtag_id = NULL # object | 话题id/Hashtag id
cursor = NULL # object | 翻页游标/Page cursor (optional)
feed_count = NULL # object | 翻页数量/Page count (optional)
hashtag_request_type = NULL # object | 话题请求类型/Hashtag request type (optional)
hashtag_sort_type = NULL # object | 话题排序类型/Hashtag sort type (optional)

try:
    # 获取话题作品列表/Get hashtag post list
    api_instance.fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get(hashtag_id, cursor=cursor, feed_count=feed_count, hashtag_request_type=hashtag_request_type, hashtag_sort_type=hashtag_sort_type)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashtag_id** | [**object**](.md)| 话题id/Hashtag id | 
 **cursor** | [**object**](.md)| 翻页游标/Page cursor | [optional] 
 **feed_count** | [**object**](.md)| 翻页数量/Page count | [optional] 
 **hashtag_request_type** | [**object**](.md)| 话题请求类型/Hashtag request type | [optional] 
 **hashtag_sort_type** | [**object**](.md)| 话题排序类型/Hashtag sort type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get**
> fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get(cursor=cursor)

获取首页推荐/Get home feed

# [中文] ### 用途: - 获取首页推荐数据。 ### 参数: - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 ### 返回: - 首页推荐数据  # [English] ### Purpose: - Get home feed data. ### Parameters: - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. ### Return: - Home feed data  # [示例/Example] cursor = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
cursor = NULL # object | 翻页游标/Page cursor (optional)

try:
    # 获取首页推荐/Get home feed
    api_instance.fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get(cursor=cursor)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | [**object**](.md)| 翻页游标/Page cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get**
> fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get(page=page)

获取首页短剧推荐/Get home short drama feed

# [中文] ### 用途: - 获取首页短剧推荐数据。 ### 参数: - page: 页码，默认为1，每次翻页加1。 ### 返回: - 首页短剧推荐数据  # [English] ### Purpose: - Get home short drama feed data. ### Parameters: - page: Page number, default is 1, add 1 for each page. ### Return: - Home short drama feed data  # [示例/Example] page = 1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
page = NULL # object | 页码/Page number (optional)

try:
    # 获取首页短剧推荐/Get home short drama feed
    api_instance.fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get(page=page)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| 页码/Page number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get**
> fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get(block_type)

获取热搜榜单详情/Get hot search board detail

# [中文] ### 用途: - 获取热搜榜单详情数据。 ### 参数: - block_type: 榜单类型，可以从`/fetch_hot_search_board_list`接口中获取。 ### 返回: - 热搜榜单详情数据  # [English] ### Purpose: - Get hot search board detail data. ### Parameters: - block_type: Board type, can be obtained from the `/fetch_hot_search_board_list` interface. ### Return: - Hot search board detail data  # [示例/Example] block_type = 12

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
block_type = NULL # object | 榜单类型/Board type

try:
    # 获取热搜榜单详情/Get hot search board detail
    api_instance.fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get(block_type)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_type** | [**object**](.md)| 榜单类型/Board type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get**
> fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get()

获取热搜榜单列表/Get hot search board list

# [中文] ### 用途: - 获取热搜榜单列表数据。 ### 返回: - 热搜榜单列表数据  # [English] ### Purpose: - Get hot search board list data. ### Return: - Hot search board list data  # [示例/Example] 无/None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()

try:
    # 获取热搜榜单列表/Get hot search board list
    api_instance.fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get()
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get: %s\n" % e)
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

# **fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get**
> fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get()

获取热搜词条/Get hot search words

# [中文] ### 用途: - 获取热搜词条数据。 ### 返回: - 热搜词条数据  # [English] ### Purpose: - Get hot search words data. ### Return: - Hot search words data  # [示例/Example] 无/None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()

try:
    # 获取热搜词条/Get hot search words
    api_instance.fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get()
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get: %s\n" % e)
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

# **fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get**
> fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get(cell_id, cell_type=cell_type)

增加作品浏览数/Increase post view count

# [中文] ### 用途: - 增加作品浏览数。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 - cell_type: 作品类型，1为视频，多大数保持默认值即可。 ### 返回: - 执行结果  # [English] ### Purpose: - Increase post view count. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. - cell_type: Video type, 1 for video, keep the default value for other types. ### Return: - Execution result  # [示例/Example] cell_id = \"7411193113223371043\" cell_type = 1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
cell_id = NULL # object | 作品id/Video id
cell_type = NULL # object | 作品类型/Video type (optional)

try:
    # 增加作品浏览数/Increase post view count
    api_instance.fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get(cell_id, cell_type=cell_type)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cell_id** | [**object**](.md)| 作品id/Video id | 
 **cell_type** | [**object**](.md)| 作品类型/Video type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get**
> fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get(cell_id, cell_type=cell_type, offset=offset)

获取作品评论列表/Get post comment list

# [中文] ### 用途: - 获取作品的评论列表。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 - cell_type: 作品类型，1为视频，多大数保持默认值即可。 - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。 ### 返回: - 作品评论列表  # [English] ### Purpose: - Get the comment list of a post. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. - cell_type: Video type, 1 for video, keep the default value for other types. - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. ### Return: - Post comment list  # [示例/Example] cell_id = \"7411193113223371043\" cell_type = 1 offset = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
cell_id = NULL # object | 作品id/Video id
cell_type = NULL # object | 作品类型/Video type (optional)
offset = NULL # object | 翻页游标/Page cursor (optional)

try:
    # 获取作品评论列表/Get post comment list
    api_instance.fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get(cell_id, cell_type=cell_type, offset=offset)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cell_id** | [**object**](.md)| 作品id/Video id | 
 **cell_type** | [**object**](.md)| 作品类型/Video type | [optional] 
 **offset** | [**object**](.md)| 翻页游标/Page cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get**
> fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get(cell_id, cell_type=cell_type)

获取单个作品数据/Get single video data

# [中文] ### 用途: - 获取单个作品数据，支持图文、视频等。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 - cell_type: 作品类型，1为视频，多大数保持默认值即可。 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data, support photo, video, etc. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. - cell_type: Video type, 1 for video, keep the default value for other types. ### Return: - Video data  # [示例/Example] cell_id = \"7411193113223371043\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
cell_id = NULL # object | 作品id/Video id
cell_type = NULL # object | 作品类型/Video type (optional)

try:
    # 获取单个作品数据/Get single video data
    api_instance.fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get(cell_id, cell_type=cell_type)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cell_id** | [**object**](.md)| 作品id/Video id | 
 **cell_type** | [**object**](.md)| 作品类型/Video type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get**
> fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get(cell_id)

获取作品统计数据/Get post statistics

# [中文] ### 用途: - 获取单个作品的统计数据，如点赞数、评论数、转发数等。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 ### 返回: - 作品统计数据  # [English] ### Purpose: - Get the statistics of a single post, such as the number of likes, comments, reposts, etc. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. ### Return: - Post statistics  # [示例/Example] cell_id = \"7411193113223371043\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
cell_id = NULL # object | 作品id/Video id

try:
    # 获取作品统计数据/Get post statistics
    api_instance.fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get(cell_id)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cell_id** | [**object**](.md)| 作品id/Video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_search_api_v1_pipixia_app_fetch_search_get**
> fetch_search_api_v1_pipixia_app_fetch_search_get(keyword, offset=offset, search_type=search_type)

搜索接口/Search API

# [中文] ### 用途: - 搜索接口，支持搜索用户、作品等。 ### 参数: - keyword: 搜索关键词。 - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。 - search_type: 搜索类型，可用值如下：     - 1: 综合     - 8: 热门     - 9: 新鲜     - 2：视频     - 3：图文     - 4：用户     - 5：话题 ### 返回: - 搜索结果  # [English] ### Purpose: - Search API, support search user, post, etc. ### Parameters: - keyword: Search keyword. - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. - search_type: Search type, available values are as follows:     - 1: Comprehensive     - 8: Hot     - 9: Fresh     - 2: Video     - 3: Photo     - 4: User     - 5: Hashtag ### Return: - Search result  # [示例/Example] keyword = \"皮皮虾\" offset = \"0\" search_type = \"1\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
keyword = NULL # object | 搜索关键词/Search keyword
offset = NULL # object | 翻页游标/Page cursor (optional)
search_type = NULL # object | 搜索类型/Search type (optional)

try:
    # 搜索接口/Search API
    api_instance.fetch_search_api_v1_pipixia_app_fetch_search_get(keyword, offset=offset, search_type=search_type)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_search_api_v1_pipixia_app_fetch_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 搜索关键词/Search keyword | 
 **offset** | [**object**](.md)| 翻页游标/Page cursor | [optional] 
 **search_type** | [**object**](.md)| 搜索类型/Search type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_short_url_api_v1_pipixia_app_fetch_short_url_get**
> fetch_short_url_api_v1_pipixia_app_fetch_short_url_get(original_url)

生成短连接/Generate short URL

# [中文] ### 用途: - 生成短连接。 ### 参数: - original_url: 原始链接，可以是任意链接。 ### 返回: - 短连接  # [English] ### Purpose: - Generate short URL. ### Parameters: - original_url: Original URL, can be any link. ### Return: - Short URL  # [示例/Example] original_url = \"https://h5.pipix.com/item/7385813877985909043\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
original_url = NULL # object | 原始链接/Original URL

try:
    # 生成短连接/Generate short URL
    api_instance.fetch_short_url_api_v1_pipixia_app_fetch_short_url_get(original_url)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_short_url_api_v1_pipixia_app_fetch_short_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_url** | [**object**](.md)| 原始链接/Original URL | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get**
> fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get(user_id, cursor=cursor)

获取用户粉丝列表/Get user follower list

# [中文] ### 用途: - 获取用户的粉丝列表。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 ### 返回: - 用户粉丝列表  # [English] ### Purpose: - Get user's follower list. ### Parameters: - user_id: AKA user id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. ### Return: - User follower list  # [示例/Example] user_id = \"1310254082831248\" cursor = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
user_id = NULL # object | 用户id/User id
cursor = NULL # object | 翻页游标/Page cursor (optional)

try:
    # 获取用户粉丝列表/Get user follower list
    api_instance.fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get(user_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户id/User id | 
 **cursor** | [**object**](.md)| 翻页游标/Page cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get**
> fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get(user_id, cursor=cursor)

获取用户关注列表/Get user following list

# [中文] ### 用途: - 获取用户的关注列表。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 ### 返回: - 用户关注列表  # [English] ### Purpose: - Get user's following list. ### Parameters: - user_id: AKA user id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. ### Return: - User following list  # [示例/Example] user_id = \"1310254082831248\" cursor = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
user_id = NULL # object | 用户id/User id
cursor = NULL # object | 翻页游标/Page cursor (optional)

try:
    # 获取用户关注列表/Get user following list
    api_instance.fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get(user_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户id/User id | 
 **cursor** | [**object**](.md)| 翻页游标/Page cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_info_api_v1_pipixia_app_fetch_user_info_get**
> fetch_user_info_api_v1_pipixia_app_fetch_user_info_get(user_id)

获取用户信息/Get user information

# [中文] ### 用途: - 获取用户信息，如昵称、性别、头像等。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 ### 返回: - 用户信息  # [English] ### Purpose: - Get user information, such as nickname and avatar. ### Parameters: - user_id: AKA user id, can be obtained from the share link. ### Return: - User information  # [示例/Example] user_id = \"1310254082831248\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
user_id = NULL # object | 用户id/User id

try:
    # 获取用户信息/Get user information
    api_instance.fetch_user_info_api_v1_pipixia_app_fetch_user_info_get(user_id)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_user_info_api_v1_pipixia_app_fetch_user_info_get: %s\n" % e)
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

# **fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get**
> fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get(user_id, cursor=cursor, feed_count=feed_count)

获取用户作品列表/Get user post list

# [中文] ### 用途: - 获取用户作品列表，如视频、图文等。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 - feed_count: 翻页数量，默认为0，后续每次翻页加1，比如第一页为0，第二页为1，第三页为2，以此类推。 ### 返回: - 用户作品列表  # [English] ### Purpose: - Get user post list, such as videos, photos, etc. ### Parameters: - user_id: AKA user id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. - feed_count: Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. ### Return: - User post list  # [示例/Example] user_id = \"1310254082831248\" cursor = \"0\" feed_count = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PiPiXiaAppAPIApi()
user_id = NULL # object | 用户id/User id
cursor = NULL # object | 翻页游标/Page cursor (optional)
feed_count = NULL # object | 翻页数量/Page count (optional)

try:
    # 获取用户作品列表/Get user post list
    api_instance.fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get(user_id, cursor=cursor, feed_count=feed_count)
except ApiException as e:
    print("Exception when calling PiPiXiaAppAPIApi->fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户id/User id | 
 **cursor** | [**object**](.md)| 翻页游标/Page cursor | [optional] 
 **feed_count** | [**object**](.md)| 翻页数量/Page count | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

