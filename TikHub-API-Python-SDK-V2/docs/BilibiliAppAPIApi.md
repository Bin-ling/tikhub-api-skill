# swagger_client.BilibiliAppAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get**](BilibiliAppAPIApi.md#fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get) | **GET** /api/v1/bilibili/app/fetch_bangumi_tab | 获取番剧推荐/Get bangumi tab
[**fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get**](BilibiliAppAPIApi.md#fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get) | **GET** /api/v1/bilibili/app/fetch_cinema_tab | 获取影视推荐/Get cinema tab
[**fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get**](BilibiliAppAPIApi.md#fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get) | **GET** /api/v1/bilibili/app/fetch_home_feed | 获取主页推荐视频流/Get home feed
[**fetch_one_video_api_v1_bilibili_app_fetch_one_video_get**](BilibiliAppAPIApi.md#fetch_one_video_api_v1_bilibili_app_fetch_one_video_get) | **GET** /api/v1/bilibili/app/fetch_one_video | 获取单个视频详情信息/Get single video data
[**fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get**](BilibiliAppAPIApi.md#fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get) | **GET** /api/v1/bilibili/app/fetch_popular_feed | 获取热门推荐/Get popular feed
[**fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get**](BilibiliAppAPIApi.md#fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get) | **GET** /api/v1/bilibili/app/fetch_reply_detail | 获取二级评论回复/Get reply detail
[**fetch_search_all_api_v1_bilibili_app_fetch_search_all_get**](BilibiliAppAPIApi.md#fetch_search_all_api_v1_bilibili_app_fetch_search_all_get) | **GET** /api/v1/bilibili/app/fetch_search_all | 综合搜索/search all
[**fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get**](BilibiliAppAPIApi.md#fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get) | **GET** /api/v1/bilibili/app/fetch_search_by_type | 分类搜索/ search by type
[**fetch_user_info_api_v1_bilibili_app_fetch_user_info_get**](BilibiliAppAPIApi.md#fetch_user_info_api_v1_bilibili_app_fetch_user_info_get) | **GET** /api/v1/bilibili/app/fetch_user_info | 获取用户信息/Get user info
[**fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get**](BilibiliAppAPIApi.md#fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get) | **GET** /api/v1/bilibili/app/fetch_user_videos | 获取用户投稿视频/Get user videos
[**fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get**](BilibiliAppAPIApi.md#fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get) | **GET** /api/v1/bilibili/app/fetch_video_comments | 获取视频评论列表/Get video comments


# **fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get**
> fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get()

获取番剧推荐/Get bangumi tab

# [中文] ### 用途: - 获取主页番剧推荐 ### 返回: - 番剧推荐数据  # [English] ### Purpose: - Get bangumi tab (anime recommendations) ### Return: - Bangumi tab data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()

try:
    # 获取番剧推荐/Get bangumi tab
    api_instance.fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get()
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get: %s\n" % e)
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

# **fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get**
> fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get()

获取影视推荐/Get cinema tab

# [中文] ### 用途: - 获取主页影视推荐 ### 返回: - 影视推荐数据  # [English] ### Purpose: - Get cinema tab (movies/TV recommendations) ### Return: - Cinema tab data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()

try:
    # 获取影视推荐/Get cinema tab
    api_instance.fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get()
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get: %s\n" % e)
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

# **fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get**
> fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get(idx=idx, flush=flush, pull=pull)

获取主页推荐视频流/Get home feed

# [中文] ### 用途: - 获取主页推荐视频流 ### 参数: - idx: 页面索引，默认使用当前时间戳 - flush: 刷新标记（0=普通加载, 1=刷新） - pull: 是否下拉刷新 ### 返回: - 推荐视频流数据  # [English] ### Purpose: - Get home feed (recommended videos) ### Parameters: - idx: Page index, defaults to current timestamp - flush: Flush flag (0=normal load, 1=refresh) - pull: Pull to refresh ### Return: - Home feed data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()
idx = NULL # object | 页面索引/Page index (optional)
flush = NULL # object | 刷新标记/Flush flag (0=普通加载, 1=刷新) (optional)
pull = NULL # object | 是否下拉刷新/Pull to refresh (optional)

try:
    # 获取主页推荐视频流/Get home feed
    api_instance.fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get(idx=idx, flush=flush, pull=pull)
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idx** | [**object**](.md)| 页面索引/Page index | [optional] 
 **flush** | [**object**](.md)| 刷新标记/Flush flag (0&#x3D;普通加载, 1&#x3D;刷新) | [optional] 
 **pull** | [**object**](.md)| 是否下拉刷新/Pull to refresh | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_api_v1_bilibili_app_fetch_one_video_get**
> fetch_one_video_api_v1_bilibili_app_fetch_one_video_get(av_id=av_id, bv_id=bv_id)

获取单个视频详情信息/Get single video data

# [中文] ### 用途: - 获取单个视频详情信息（APP接口） ### 参数: - av_id: AV号（与bv_id二选一） - bv_id: BV号（与av_id二选一） ### 返回: - 视频详情信息  # [English] ### Purpose: - Get single video data (APP API) ### Parameters: - av_id: AV ID (choose one of av_id or bv_id) - bv_id: BV ID (choose one of av_id or bv_id) ### Return: - Video data  # [示例/Example] av_id = \"115568241811221\" bv_id = \"BV18SCrBGE9E\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()
av_id = NULL # object | AV号/AV ID (optional)
bv_id = NULL # object | BV号/BV ID (optional)

try:
    # 获取单个视频详情信息/Get single video data
    api_instance.fetch_one_video_api_v1_bilibili_app_fetch_one_video_get(av_id=av_id, bv_id=bv_id)
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_one_video_api_v1_bilibili_app_fetch_one_video_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **av_id** | [**object**](.md)| AV号/AV ID | [optional] 
 **bv_id** | [**object**](.md)| BV号/BV ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get**
> fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get(idx=idx, last_param=last_param)

获取热门推荐/Get popular feed

# [中文] ### 用途: - 获取热门推荐视频 ### 参数: - idx: 页面索引（从1开始） - last_param: 上一页最后一个视频的ID（用于分页） ### 返回: - 热门推荐视频数据  # [English] ### Purpose: - Get popular feed ### Parameters: - idx: Page index (starting from 1) - last_param: Last video ID from previous page (for pagination) ### Return: - Popular feed data  # [示例/Example] idx = 1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()
idx = NULL # object | 页面索引/Page index (optional)
last_param = NULL # object | 上一页最后一个视频ID/Last video ID (optional)

try:
    # 获取热门推荐/Get popular feed
    api_instance.fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get(idx=idx, last_param=last_param)
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idx** | [**object**](.md)| 页面索引/Page index | [optional] 
 **last_param** | [**object**](.md)| 上一页最后一个视频ID/Last video ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get**
> fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get(root, av_id=av_id, bv_id=bv_id, next_offset=next_offset, ps=ps)

获取二级评论回复/Get reply detail

# [中文] ### 用途: - 获取二级评论回复 ### 参数: - root: 一级评论ID（必填） - av_id: AV号（与bv_id二选一） - bv_id: BV号（与av_id二选一） - next_offset: 下一页游标 - ps: 每页数量 ### 返回: - 二级评论列表数据  # [English] ### Purpose: - Get reply detail (second level comments) ### Parameters: - root: Root comment ID (required) - av_id: AV ID (choose one of av_id or bv_id) - bv_id: BV ID (choose one of av_id or bv_id) - next_offset: Next page cursor - ps: Page size ### Return: - Reply data  # [示例/Example] root = \"241743663521\" av_id = \"113100682434775\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()
root = NULL # object | 一级评论ID/Root comment ID
av_id = NULL # object | AV号/AV ID (optional)
bv_id = NULL # object | BV号/BV ID (optional)
next_offset = NULL # object | 下一页游标/Next page cursor (optional)
ps = NULL # object | 每页数量/Page size (optional)

try:
    # 获取二级评论回复/Get reply detail
    api_instance.fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get(root, av_id=av_id, bv_id=bv_id, next_offset=next_offset, ps=ps)
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | [**object**](.md)| 一级评论ID/Root comment ID | 
 **av_id** | [**object**](.md)| AV号/AV ID | [optional] 
 **bv_id** | [**object**](.md)| BV号/BV ID | [optional] 
 **next_offset** | [**object**](.md)| 下一页游标/Next page cursor | [optional] 
 **ps** | [**object**](.md)| 每页数量/Page size | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_search_all_api_v1_bilibili_app_fetch_search_all_get**
> fetch_search_all_api_v1_bilibili_app_fetch_search_all_get(keyword, page=page, page_size=page_size, order=order)

综合搜索/search all

# [中文] ### 用途: - 综合搜索（返回所有类型的搜索结果） ### 参数: - keyword: 搜索关键词（必填） - page: 页码，从1开始 - page_size: 每页结果数量 - order: 排序方式（0=综合排序） ### 返回: - 搜索结果，包含nav（分类导航）、item（搜索结果）、pagination（分页信息）等  # [English] ### Purpose: -  search all (returns all types of search results) ### Parameters: - keyword: Search keyword (required) - page: Page number, starting from 1 - page_size: Results per page - order: Sort order (0=comprehensive) ### Return: - Search results including nav (category navigation), item (results), pagination, etc.  # [示例/Example] keyword = \"原神\" page = 1 page_size = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()
keyword = NULL # object | 搜索关键词/Search keyword
page = NULL # object | 页码/Page number (optional)
page_size = NULL # object | 每页数量/Page size (optional)
order = NULL # object | 排序方式/Sort order (0=综合排序) (optional)

try:
    # 综合搜索/search all
    api_instance.fetch_search_all_api_v1_bilibili_app_fetch_search_all_get(keyword, page=page, page_size=page_size, order=order)
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_search_all_api_v1_bilibili_app_fetch_search_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 搜索关键词/Search keyword | 
 **page** | [**object**](.md)| 页码/Page number | [optional] 
 **page_size** | [**object**](.md)| 每页数量/Page size | [optional] 
 **order** | [**object**](.md)| 排序方式/Sort order (0&#x3D;综合排序) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get**
> fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get(keyword, search_type=search_type, page=page, page_size=page_size, order=order)

分类搜索/ search by type

# [中文] ### 用途: - 分类搜索（按类型搜索） ### 参数: - keyword: 搜索关键词（必填） - search_type: 搜索类型     - video: 视频     - bangumi: 番剧     - pgc: 影视     - live: 直播     - article: 专栏     - user: 用户 - page: 页码，从1开始 - page_size: 每页结果数量 - order: 排序方式     - 0: 综合排序     - 1: 最新发布     - 2: 播放量     - 3: 弹幕数 ### 返回: - 搜索结果  # [English] ### Purpose: -  search by type ### Parameters: - keyword: Search keyword (required) - search_type: Search type     - video: Videos     - bangumi: Anime     - pgc: Movies/TV     - live: Live streams     - article: Articles     - user: Users - page: Page number, starting from 1 - page_size: Results per page - order: Sort order     - 0: Comprehensive     - 1: Latest     - 2: Play count     - 3: Danmaku count ### Return: - Search results  # [示例/Example] keyword = \"原神\" search_type = \"video\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()
keyword = NULL # object | 搜索关键词/Search keyword
search_type = NULL # object | 搜索类型/Search type (video/bangumi/pgc/live/article/user) (optional)
page = NULL # object | 页码/Page number (optional)
page_size = NULL # object | 每页数量/Page size (optional)
order = NULL # object | 排序方式/Sort order (0=综合, 1=最新, 2=播放量, 3=弹幕数) (optional)

try:
    # 分类搜索/ search by type
    api_instance.fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get(keyword, search_type=search_type, page=page, page_size=page_size, order=order)
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 搜索关键词/Search keyword | 
 **search_type** | [**object**](.md)| 搜索类型/Search type (video/bangumi/pgc/live/article/user) | [optional] 
 **page** | [**object**](.md)| 页码/Page number | [optional] 
 **page_size** | [**object**](.md)| 每页数量/Page size | [optional] 
 **order** | [**object**](.md)| 排序方式/Sort order (0&#x3D;综合, 1&#x3D;最新, 2&#x3D;播放量, 3&#x3D;弹幕数) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_info_api_v1_bilibili_app_fetch_user_info_get**
> fetch_user_info_api_v1_bilibili_app_fetch_user_info_get(user_id)

获取用户信息/Get user info

# [中文] ### 用途: - 获取用户信息 ### 参数: - user_id: 用户ID（必填） ### 返回: - 用户信息（包含粉丝数、关注数、投稿数等）  # [English] ### Purpose: - Get user info ### Parameters: - user_id: User ID (required) ### Return: - User info (including followers, following, videos count, etc.)  # [示例/Example] user_id = \"203680252\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()
user_id = NULL # object | 用户ID/User ID

try:
    # 获取用户信息/Get user info
    api_instance.fetch_user_info_api_v1_bilibili_app_fetch_user_info_get(user_id)
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_user_info_api_v1_bilibili_app_fetch_user_info_get: %s\n" % e)
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

# **fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get**
> fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get(user_id, post_filter=post_filter, page=page, ps=ps)

获取用户投稿视频/Get user videos

# [中文] ### 用途: - 获取用户投稿视频列表 ### 参数: - user_id: 用户ID（必填） - post_filter: 过滤类型（archive=投稿, season=合集, contribute=贡献） - page: 页码 - ps: 每页数量 ### 返回: - 用户投稿视频列表  # [English] ### Purpose: - Get user uploaded videos ### Parameters: - user_id: User ID (required) - post_filter: Filter type (archive/season/contribute) - page: Page number - ps: Page size ### Return: - User videos data  # [示例/Example] user_id = \"203680252\" post_filter = \"archive\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()
user_id = NULL # object | 用户ID/User ID
post_filter = NULL # object | 过滤类型/Filter type (archive/season/contribute) (optional)
page = NULL # object | 页码/Page number (optional)
ps = NULL # object | 每页数量/Page size (optional)

try:
    # 获取用户投稿视频/Get user videos
    api_instance.fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get(user_id, post_filter=post_filter, page=page, ps=ps)
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **post_filter** | [**object**](.md)| 过滤类型/Filter type (archive/season/contribute) | [optional] 
 **page** | [**object**](.md)| 页码/Page number | [optional] 
 **ps** | [**object**](.md)| 每页数量/Page size | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get**
> fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get(av_id=av_id, bv_id=bv_id, mode=mode, next_offset=next_offset)

获取视频评论列表/Get video comments

# [中文] ### 用途: - 获取视频评论列表 ### 参数: - av_id: AV号（与bv_id二选一） - bv_id: BV号（与av_id二选一） - mode: 排序模式（3=热门, 2=时间） - next_offset: 分页游标 ### 返回: - 评论列表数据  # [English] ### Purpose: - Get video comments ### Parameters: - av_id: AV ID (choose one of av_id or bv_id) - bv_id: BV ID (choose one of av_id or bv_id) - mode: Sort mode (3=hot, 2=time) - next_offset: Pagination cursor ### Return: - Comments data  # [示例/Example] bv_id = \"BV18SCrBGE9E\" mode = 3 next_offset = 1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BilibiliAppAPIApi()
av_id = NULL # object | AV号/AV ID (optional)
bv_id = NULL # object | BV号/BV ID (optional)
mode = NULL # object | 排序模式/Sort mode (3=热门/hot, 2=时间/time) (optional)
next_offset = NULL # object | 分页游标/Pagination cursor (optional)

try:
    # 获取视频评论列表/Get video comments
    api_instance.fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get(av_id=av_id, bv_id=bv_id, mode=mode, next_offset=next_offset)
except ApiException as e:
    print("Exception when calling BilibiliAppAPIApi->fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **av_id** | [**object**](.md)| AV号/AV ID | [optional] 
 **bv_id** | [**object**](.md)| BV号/BV ID | [optional] 
 **mode** | [**object**](.md)| 排序模式/Sort mode (3&#x3D;热门/hot, 2&#x3D;时间/time) | [optional] 
 **next_offset** | [**object**](.md)| 分页游标/Pagination cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

