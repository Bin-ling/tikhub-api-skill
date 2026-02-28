# swagger_client.WeiboWebAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get**](WeiboWebAPIApi.md#fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get) | **GET** /api/v1/weibo/web/fetch_channel_feed | 根据频道名称获取热门内容/Get channel feed by name
[**fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get**](WeiboWebAPIApi.md#fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get) | **GET** /api/v1/weibo/web/fetch_comment_replies | 获取评论子评论/Get comment replies
[**fetch_config_list_api_v1_weibo_web_fetch_config_list_get**](WeiboWebAPIApi.md#fetch_config_list_api_v1_weibo_web_fetch_config_list_get) | **GET** /api/v1/weibo/web/fetch_config_list | 获取频道配置列表/Get channel config list
[**fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get**](WeiboWebAPIApi.md#fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get) | **GET** /api/v1/weibo/web/fetch_hot_search | 获取热搜榜/Get hot search ranking
[**fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get**](WeiboWebAPIApi.md#fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get) | **GET** /api/v1/weibo/web/fetch_post_comments | 获取微博评论/Get post comments
[**fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get**](WeiboWebAPIApi.md#fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get) | **GET** /api/v1/weibo/web/fetch_post_detail | 获取微博详情/Get post detail
[**fetch_search_api_v1_weibo_web_fetch_search_get**](WeiboWebAPIApi.md#fetch_search_api_v1_weibo_web_fetch_search_get) | **GET** /api/v1/weibo/web/fetch_search | 搜索微博/Search Weibo
[**fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get**](WeiboWebAPIApi.md#fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get) | **GET** /api/v1/weibo/web/fetch_search_topics | 获取搜索页热搜词/Get search page hot topics
[**fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get**](WeiboWebAPIApi.md#fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get) | **GET** /api/v1/weibo/web/fetch_trend_top | 获取频道热门趋势/Get channel trend top
[**fetch_user_info_api_v1_weibo_web_fetch_user_info_get**](WeiboWebAPIApi.md#fetch_user_info_api_v1_weibo_web_fetch_user_info_get) | **GET** /api/v1/weibo/web/fetch_user_info | 获取用户信息/Get user information
[**fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get**](WeiboWebAPIApi.md#fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get) | **GET** /api/v1/weibo/web/fetch_user_posts | 获取用户微博列表/Get user posts


# **fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get**
> fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get(channel_name=channel_name, page=page)

根据频道名称获取热门内容/Get channel feed by name

# [中文] ### 用途: - 根据频道名称获取热门内容（便捷接口） ### 参数: - channel_name: 频道名称，如 \"热门\"、\"榜单\"、\"社会\" 等，不传则使用默认频道 - page: 页码，默认1 ### 返回: - 热门微博列表 ### 说明: - 此接口会自动调用 fetch_config_list 获取频道配置，然后获取对应频道的热门内容 - 如果指定的频道名称不存在，会返回错误信息 - 可用频道：热门、榜单、同城、社会、科技、明星、电影、音乐、数码、汽车、游戏  # [English] ### Purpose: - Get trending content by channel name (convenience endpoint) ### Parameters: - channel_name: Channel name, such as \"热门\", \"榜单\", \"社会\", etc. Use default if not provided - page: Page number, default 1 ### Return: - Trending Weibo list ### Note: - This endpoint will automatically call fetch_config_list to get channel config, then fetch trending content - Returns error if the specified channel name does not exist - Available channels: 热门, 榜单, 同城, 社会, 科技, 明星, 电影, 音乐, 数码, 汽车, 游戏  # [示例/Example] channel_name = \"热门\" page = 1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()
channel_name = NULL # object | 频道名称，不传则使用默认频道/Channel name, use default if not provided (optional)
page = NULL # object | 页码/Page number (optional)

try:
    # 根据频道名称获取热门内容/Get channel feed by name
    api_instance.fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get(channel_name=channel_name, page=page)
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | [**object**](.md)| 频道名称，不传则使用默认频道/Channel name, use default if not provided | [optional] 
 **page** | [**object**](.md)| 页码/Page number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get**
> fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get(cid, max_id=max_id)

获取评论子评论/Get comment replies

# [中文] ### 用途: - 获取评论的子评论（回复） ### 参数: - cid: 根评论ID（从 fetch_post_comments 返回的评论中获取） - max_id: 翻页用的ID，默认0为第一页，从上一页返回结果中获取下一页的max_id ### 返回: - 子评论列表  # [English] ### Purpose: - Get comment replies (sub-comments) ### Parameters: - cid: Root comment ID (from fetch_post_comments response) - max_id: Pagination ID, default 0 for first page, get next page max_id from previous response ### Return: - Sub-comments list  # [示例/Example] cid = \"5100663573318494\" max_id = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()
cid = NULL # object | 根评论ID/Root comment ID
max_id = NULL # object | 翻页ID，默认0为第一页/Pagination ID, default 0 for first page (optional)

try:
    # 获取评论子评论/Get comment replies
    api_instance.fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get(cid, max_id=max_id)
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | [**object**](.md)| 根评论ID/Root comment ID | 
 **max_id** | [**object**](.md)| 翻页ID，默认0为第一页/Pagination ID, default 0 for first page | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_config_list_api_v1_weibo_web_fetch_config_list_get**
> fetch_config_list_api_v1_weibo_web_fetch_config_list_get()

获取频道配置列表/Get channel config list

# [中文] ### 用途: - 获取微博移动端所有频道的配置信息 ### 返回: - 频道列表，包含频道名称和 containerid ### 说明: - 返回的 containerid 可用于 fetch_trend_top 接口获取对应频道的热门内容  # [English] ### Purpose: - Get all channel configuration information from Weibo mobile ### Return: - Channel list, including channel name and containerid ### Note: - The returned containerid can be used in fetch_trend_top endpoint to get trending content of the corresponding channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()

try:
    # 获取频道配置列表/Get channel config list
    api_instance.fetch_config_list_api_v1_weibo_web_fetch_config_list_get()
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_config_list_api_v1_weibo_web_fetch_config_list_get: %s\n" % e)
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

# **fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get**
> fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get()

获取热搜榜/Get hot search ranking

# [中文] ### 用途: - 获取微博实时热搜榜（Top 50）和实时上升热点 ### 返回: - 热搜榜列表，包含：     - **实时热搜榜**: 当前最热门的50个话题，按热度排序     - **实时上升热点**: 正在快速上升的热门话题 ### 说明: - 这是微博官方热搜榜数据 - 每个热搜包含：排名、话题名、热度值、标签（如：新、热、沸）等 - 与 `fetch_search_topics` 不同，此接口返回的是完整的热搜排行榜  # [English] ### Purpose: - Get Weibo real-time hot search ranking (Top 50) and rising trends ### Return: - Hot search list, including:     - **Real-time Hot Search**: Top 50 hottest topics, sorted by popularity     - **Rising Trends**: Topics that are rapidly gaining attention ### Note: - This is official Weibo hot search data - Each entry includes: rank, topic name, heat value, tags (new, hot, trending), etc. - Different from `fetch_search_topics`, this returns the complete hot search ranking

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()

try:
    # 获取热搜榜/Get hot search ranking
    api_instance.fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get()
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get: %s\n" % e)
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

# **fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get**
> fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get(post_id, mid, max_id=max_id, max_id_type=max_id_type)

获取微博评论/Get post comments

# [中文] ### 用途: - 获取微博的评论列表（热门评论流） ### 参数: - post_id: 微博ID - mid: 微博MID - max_id: 翻页用的ID，从上一页返回结果中获取 - max_id_type: max_id类型，默认0 ### 返回: - 评论列表  # [English] ### Purpose: - Get Weibo post comments (hot comments flow) ### Parameters: - post_id: Post ID - mid: Post MID - max_id: Pagination ID from previous page result - max_id_type: max_id type, default 0 ### Return: - Comments list  # [示例/Example] post_id = \"5100663548412324\" mid = \"5100663548412324\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()
post_id = NULL # object | 微博ID/Post ID
mid = NULL # object | 微博MID/Post MID
max_id = NULL # object | 翻页ID/Pagination ID (optional)
max_id_type = NULL # object | 翻页ID类型/Pagination ID type (optional)

try:
    # 获取微博评论/Get post comments
    api_instance.fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get(post_id, mid, max_id=max_id, max_id_type=max_id_type)
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | [**object**](.md)| 微博ID/Post ID | 
 **mid** | [**object**](.md)| 微博MID/Post MID | 
 **max_id** | [**object**](.md)| 翻页ID/Pagination ID | [optional] 
 **max_id_type** | [**object**](.md)| 翻页ID类型/Pagination ID type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get**
> fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get(post_id)

获取微博详情/Get post detail

# [中文] ### 用途: - 获取单条微博的详情 ### 参数: - post_id: 微博ID ### 返回: - 微博详情  # [English] ### Purpose: - Get single Weibo post detail ### Parameters: - post_id: Post ID ### Return: - Post detail  # [示例/Example] post_id = \"5092682368025584\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()
post_id = NULL # object | 微博ID/Post ID

try:
    # 获取微博详情/Get post detail
    api_instance.fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get(post_id)
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | [**object**](.md)| 微博ID/Post ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_search_api_v1_weibo_web_fetch_search_get**
> fetch_search_api_v1_weibo_web_fetch_search_get(keyword, page=page, search_type=search_type, time_scope=time_scope)

搜索微博/Search Weibo

# [中文] ### 用途: - 搜索微博内容 ### 参数: - **keyword**: 搜索关键词     - 普通搜索: `游戏`、`新闻`     - 话题搜索: `#话题名#`（如 `#大冰建议女生不要找老登#`） - **page**: 页码     - 从 **1** 开始递增: 1, 2, 3, 4...     - 每页约返回 10-20 条结果     - **不是** 1, 10, 20 这种偏移量模式 - **search_type**: 搜索类型     - **1**: 综合（默认，按相关性排序）     - **61**: 实时（按时间排序，最新优先）     - **3**: 用户（搜索用户账号）     - **60**: 热门（按热度排序）     - **64**: 视频（仅视频内容）     - **63**: 图片（仅图片内容）     - **21**: 文章（仅长文章） - **time_scope**: 时间范围筛选     - **null/不传**: 不限时间（默认）     - **hour**: 一小时内     - **day**: 一天内（24小时）     - **week**: 一周内     - **month**: 一个月内 ### 返回: - 搜索结果列表 ### 注意: - 此接口会自动生成游客Cookie，无需登录即可使用 - 如遇到 432 错误，系统会自动重试  # [English] ### Purpose: - Search Weibo content ### Parameters: - **keyword**: Search keyword     - Normal search: `game`, `news`     - Hashtag search: `#topic#` (e.g., `#TopicName#`) - **page**: Page number     - Starts from **1** and increments: 1, 2, 3, 4...     - Returns ~10-20 results per page     - **NOT** offset mode like 1, 10, 20 - **search_type**: Search type     - **1**: Comprehensive (default, sorted by relevance)     - **61**: Real-time (sorted by time, newest first)     - **3**: Users (search user accounts)     - **60**: Hot (sorted by popularity)     - **64**: Video (video content only)     - **63**: Pictures (image content only)     - **21**: Articles (long articles only) - **time_scope**: Time range filter     - **null/empty**: No time limit (default)     - **hour**: Within one hour     - **day**: Within one day (24 hours)     - **week**: Within one week     - **month**: Within one month ### Return: - Search results list ### Note: - This endpoint auto-generates visitor cookies, no login required - Auto-retry on 432 error  # [示例/Example] keyword = \"游戏\" page = 1 search_type = \"1\" time_scope = null

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()
keyword = NULL # object | 搜索关键词，支持话题搜索如 #话题名#/Search keyword, supports hashtag like #topic#
page = NULL # object | 页码，从1开始递增(1,2,3...)，每页约10-20条/Page number, starts from 1 (1,2,3...), ~10-20 results per page (optional)
search_type = NULL # object | 搜索类型/Search type: 1=综合, 61=实时, 3=用户, 60=热门, 64=视频, 63=图片, 21=文章 (optional)
time_scope = NULL # object | 时间范围/Time scope: hour=一小时内, day=一天内, week=一周内, month=一个月内, null=不限 (optional)

try:
    # 搜索微博/Search Weibo
    api_instance.fetch_search_api_v1_weibo_web_fetch_search_get(keyword, page=page, search_type=search_type, time_scope=time_scope)
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_search_api_v1_weibo_web_fetch_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 搜索关键词，支持话题搜索如 #话题名#/Search keyword, supports hashtag like #topic# | 
 **page** | [**object**](.md)| 页码，从1开始递增(1,2,3...)，每页约10-20条/Page number, starts from 1 (1,2,3...), ~10-20 results per page | [optional] 
 **search_type** | [**object**](.md)| 搜索类型/Search type: 1&#x3D;综合, 61&#x3D;实时, 3&#x3D;用户, 60&#x3D;热门, 64&#x3D;视频, 63&#x3D;图片, 21&#x3D;文章 | [optional] 
 **time_scope** | [**object**](.md)| 时间范围/Time scope: hour&#x3D;一小时内, day&#x3D;一天内, week&#x3D;一周内, month&#x3D;一个月内, null&#x3D;不限 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get**
> fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get()

获取搜索页热搜词/Get search page hot topics

# [中文] ### 用途: - 获取搜索页的热搜词列表（搜索建议/热门话题） ### 返回: - 搜索热词列表 ### 说明: - 这是搜索页面展示的热门搜索词 - 通常用于搜索框下方的热门推荐 - 与 `fetch_hot_search` 不同，此接口返回的是搜索建议词  # [English] ### Purpose: - Get search page hot topics list (search suggestions/trending topics) ### Return: - Search hot topics list ### Note: - These are hot search terms displayed on the search page - Usually used for trending recommendations below the search box - Different from `fetch_hot_search`, this returns search suggestion terms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()

try:
    # 获取搜索页热搜词/Get search page hot topics
    api_instance.fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get()
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get: %s\n" % e)
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

# **fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get**
> fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get(containerid, page=page)

获取频道热门趋势/Get channel trend top

# [中文] ### 用途: - 获取指定频道的热门趋势内容 ### 参数: - containerid: 频道容器ID，可从 fetch_config_list 接口获取 - page: 页码，默认1 ### 返回: - 热门微博列表 ### 说明: - containerid 示例: 102803_ctg1_8999_-_ctg1_8999_home - 可通过 fetch_config_list 获取所有可用的 containerid  # [English] ### Purpose: - Get trending content of the specified channel ### Parameters: - containerid: Channel container ID, can be obtained from fetch_config_list endpoint - page: Page number, default 1 ### Return: - Trending Weibo list ### Note: - containerid example: 102803_ctg1_8999_-_ctg1_8999_home - You can get all available containerids from fetch_config_list  # [示例/Example] containerid = \"102803_ctg1_8999_-_ctg1_8999_home\" page = 1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()
containerid = NULL # object | 频道容器ID/Channel container ID
page = NULL # object | 页码/Page number (optional)

try:
    # 获取频道热门趋势/Get channel trend top
    api_instance.fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get(containerid, page=page)
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **containerid** | [**object**](.md)| 频道容器ID/Channel container ID | 
 **page** | [**object**](.md)| 页码/Page number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_info_api_v1_weibo_web_fetch_user_info_get**
> fetch_user_info_api_v1_weibo_web_fetch_user_info_get(uid)

获取用户信息/Get user information

# [中文] ### 用途: - 获取微博用户信息 ### 参数: - uid: 用户ID ### 返回: - 用户信息  # [English] ### Purpose: - Get Weibo user information ### Parameters: - uid: User ID ### Return: - User information  # [示例/Example] uid = \"2992978081\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()
uid = NULL # object | 用户ID/User ID

try:
    # 获取用户信息/Get user information
    api_instance.fetch_user_info_api_v1_weibo_web_fetch_user_info_get(uid)
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_user_info_api_v1_weibo_web_fetch_user_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | [**object**](.md)| 用户ID/User ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get**
> fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get(uid, page=page, since_id=since_id)

获取用户微博列表/Get user posts

# [中文] ### 用途: - 获取微博用户的微博列表 ### 参数: - uid: 用户ID - page: 页码，默认1 - since_id: 翻页用的ID，从上一页返回结果中获取 ### 返回: - 用户微博列表  # [English] ### Purpose: - Get Weibo user's posts list ### Parameters: - uid: User ID - page: Page number, default 1 - since_id: Pagination ID from previous page result ### Return: - User posts list  # [示例/Example] uid = \"7277477906\" page = 1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeiboWebAPIApi()
uid = NULL # object | 用户ID/User ID
page = NULL # object | 页码/Page number (optional)
since_id = NULL # object | 翻页ID，从上一页结果获取/Pagination ID from previous page (optional)

try:
    # 获取用户微博列表/Get user posts
    api_instance.fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get(uid, page=page, since_id=since_id)
except ApiException as e:
    print("Exception when calling WeiboWebAPIApi->fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | [**object**](.md)| 用户ID/User ID | 
 **page** | [**object**](.md)| 页码/Page number | [optional] 
 **since_id** | [**object**](.md)| 翻页ID，从上一页结果获取/Pagination ID from previous page | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

