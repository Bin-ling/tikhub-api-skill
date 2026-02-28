# swagger_client.Lemon8AppAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get**](Lemon8AppAPIApi.md#fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get) | **GET** /api/v1/lemon8/app/fetch_discover_banners | 获取发现页Banner/Get banners of discover page
[**fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get**](Lemon8AppAPIApi.md#fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get) | **GET** /api/v1/lemon8/app/fetch_discover_tab | 获取发现页主体内容/Get main content of discover page
[**fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get**](Lemon8AppAPIApi.md#fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get) | **GET** /api/v1/lemon8/app/fetch_discover_tab_information_tabs | 获取发现页的 Editor&#39;s Picks/Get Editor&#39;s Picks of discover page
[**fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get**](Lemon8AppAPIApi.md#fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get) | **GET** /api/v1/lemon8/app/fetch_hot_search_keywords | 获取热搜关键词/Get hot search keywords
[**fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get**](Lemon8AppAPIApi.md#fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get) | **GET** /api/v1/lemon8/app/fetch_post_comment_list | 获取指定作品的评论列表/Get comments list of specified post
[**fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get**](Lemon8AppAPIApi.md#fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get) | **GET** /api/v1/lemon8/app/fetch_post_detail | 获取指定作品的信息/Get information of specified post
[**fetch_search_api_v1_lemon8_app_fetch_search_get**](Lemon8AppAPIApi.md#fetch_search_api_v1_lemon8_app_fetch_search_get) | **GET** /api/v1/lemon8/app/fetch_search | 搜索接口/Search API
[**fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get**](Lemon8AppAPIApi.md#fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get) | **GET** /api/v1/lemon8/app/fetch_topic_info | 获取话题信息/Get topic information
[**fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get**](Lemon8AppAPIApi.md#fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get) | **GET** /api/v1/lemon8/app/fetch_topic_post_list | 获取话题作品列表/Get topic post list
[**fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get**](Lemon8AppAPIApi.md#fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get) | **GET** /api/v1/lemon8/app/fetch_user_follower_list | 获取指定用户的粉丝列表/Get fans list of specified user
[**fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get**](Lemon8AppAPIApi.md#fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get) | **GET** /api/v1/lemon8/app/fetch_user_following_list | 获取指定用户的关注列表/Get following list of specified user
[**get_item_id_api_v1_lemon8_app_get_item_id_get**](Lemon8AppAPIApi.md#get_item_id_api_v1_lemon8_app_get_item_id_get) | **GET** /api/v1/lemon8/app/get_item_id | 通过分享链接获取作品ID/Get post ID through sharing link
[**get_item_ids_api_v1_lemon8_app_get_item_ids_post**](Lemon8AppAPIApi.md#get_item_ids_api_v1_lemon8_app_get_item_ids_post) | **POST** /api/v1/lemon8/app/get_item_ids | 通过分享链接批量获取作品ID/Get post IDs in batch through sharing links
[**get_user_id_api_v1_lemon8_app_get_user_id_get**](Lemon8AppAPIApi.md#get_user_id_api_v1_lemon8_app_get_user_id_get) | **GET** /api/v1/lemon8/app/get_user_id | 通过分享链接获取用户ID/Get user ID through sharing link
[**get_user_ids_api_v1_lemon8_app_get_user_ids_post**](Lemon8AppAPIApi.md#get_user_ids_api_v1_lemon8_app_get_user_ids_post) | **POST** /api/v1/lemon8/app/get_user_ids | 通过分享链接批量获取用户ID/Get user IDs in batch through sharing links
[**handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get**](Lemon8AppAPIApi.md#handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get) | **GET** /api/v1/lemon8/app/fetch_user_profile | 获取指定用户的信息/Get information of specified user


# **fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get**
> fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get()

获取发现页Banner/Get banners of discover page

# [中文] ### 用途: - 获取发现页Banner（搜索页上方的滚动内容） ### 返回: - Banner列表  # [English] ### Purpose: - Get banners of discover page ### Return: - Banners list  # [示例/Example]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()

try:
    # 获取发现页Banner/Get banners of discover page
    api_instance.fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get()
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get: %s\n" % e)
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

# **fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get**
> fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get()

获取发现页主体内容/Get main content of discover page

# [中文] ### 用途: - 获取发现页（搜索页主体内容） ### 返回: - 主体内容  # [English] ### Purpose: - Get main content of discover page ### Return: - Main content  # [示例/Example]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()

try:
    # 获取发现页主体内容/Get main content of discover page
    api_instance.fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get()
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get: %s\n" % e)
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

# **fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get**
> fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get()

获取发现页的 Editor's Picks/Get Editor's Picks of discover page

# [中文] ### 用途: - 获取发现页（搜索页下方的推荐内容 - Editor's Picks） ### 返回: - 推荐内容  # [English] ### Purpose: - Get Editor's Picks of discover page ### Return: - Editor's Picks  # [示例/Example]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()

try:
    # 获取发现页的 Editor's Picks/Get Editor's Picks of discover page
    api_instance.fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get()
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get: %s\n" % e)
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

# **fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get**
> fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get()

获取热搜关键词/Get hot search keywords

# [中文] ### 用途: - 获取热搜关键词 ### 返回: - 热搜关键词列表  # [English] ### Purpose: - Get hot search keywords ### Return: - Hot search keywords list  # [示例/Example]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()

try:
    # 获取热搜关键词/Get hot search keywords
    api_instance.fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get()
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get: %s\n" % e)
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

# **fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get**
> fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get(group_id, item_id, media_id, offset=offset)

获取指定作品的评论列表/Get comments list of specified post

# [中文] ### 用途: - 获取指定作品的评论列表 ### 参数: - group_id: 作品的group_id，可以从接口`/lemon8/app/fetch_post_detail`获取 - item_id: 作品的item_id，可以从接口`/lemon8/app/fetch_post_detail` 或 `/lemon8/app/get_item_id`获取 - media_id: 作品的media_id，可以从接口`/lemon8/app/fetch_post_detail`获取 - offset: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的offset进行翻页。 ### 返回: - 评论列表  # [English] ### Purpose: - Get comments list of specified post ### Parameters: - group_id: Post's group_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` - item_id: Post's item_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` or `/lemon8/app/get_item_id` - media_id: Post's media_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` - offset: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the offset returned by the last request is used for subsequent requests. ### Return: - Comments list  # [示例/Example] group_id = \"7361926875709129222\" item_id = \"7361926875709129222\" media_id = \"7428056850216862763\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()
group_id = NULL # object | 作品的group_id/Post's group_id
item_id = NULL # object | 作品的item_id/Post's item_id
media_id = NULL # object | 作品的media_id/Post's media_id
offset = NULL # object | 翻页参数/Pagination parameter (optional)

try:
    # 获取指定作品的评论列表/Get comments list of specified post
    api_instance.fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get(group_id, item_id, media_id, offset=offset)
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| 作品的group_id/Post&#39;s group_id | 
 **item_id** | [**object**](.md)| 作品的item_id/Post&#39;s item_id | 
 **media_id** | [**object**](.md)| 作品的media_id/Post&#39;s media_id | 
 **offset** | [**object**](.md)| 翻页参数/Pagination parameter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get**
> fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get(item_id)

获取指定作品的信息/Get information of specified post

# [中文] ### 用途: - 获取指定作品的信息 ### 参数: - item_id: 作品ID，可以从接口`/lemon8/app/get_item_id`获取 ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - item_id: Post ID, can be obtained from the interface `/lemon8/app/get_item_id` ### Return: - Post information  # [示例/Example] item_id = \"7361926875709129222\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()
item_id = NULL # object | 作品ID/Post ID

try:
    # 获取指定作品的信息/Get information of specified post
    api_instance.fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get(item_id)
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**object**](.md)| 作品ID/Post ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_search_api_v1_lemon8_app_fetch_search_get**
> fetch_search_api_v1_lemon8_app_fetch_search_get(query, max_cursor=max_cursor, filter_type=filter_type, order_by=order_by, search_tab=search_tab)

搜索接口/Search API

# [中文] ### 用途: - 搜索接口 ### 参数: - query: 搜索关键词 - max_cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的`max_cursor`进行翻页，可以通过返回结果的`has_more`字段判断是否还有更多数据。 - filter_type: 搜索过滤类型，默认为空字符串，可选值如下：     - 空字符串：All（全部，默认使用此参数搜索）     - video：只搜索视频作品     - posts：只搜索文章作品 - order_by: 搜索排序方式，默认为空字符串，可选值如下：     - 空字符串：Relevance（相关度，默认使用此参数排序）     - popular：流行度排序     - recent：从新到旧排序 - search_tab: 搜索类型，默认为`main`，可选值如下：     - main：APP中显示为 `Top`（综合搜索，默认使用此参数搜索）     - user：APP中显示为 `Accounts` （搜索用户账号）     - hashtag：APP中显示为 `Hashtags`（搜索话题）     - article：APP中显示为 `Posts`（搜索文章） ### 返回: - 搜索结果  # [English] ### Purpose: - Search API ### Parameters: - query: Search keyword - max_cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the `max_cursor` returned by the last request is used for subsequent requests. You can judge whether there is more data by the `has_more` field in the return result. - filter_type: Search filter type, default is an empty string, optional values are as follows:     - Empty string: All (default using this parameter to search)     - video: Search only video     - posts: Search only posts - order_by: Search sort type, default is an empty string, optional values are as follows:     - Empty string: Relevance (default using this parameter to sort)     - popular: Sort by popularity     - recent: Sort from new to old - search_tab: Search type, default is `main`, optional values are as follows:     - main: Display as `Top` in the APP (comprehensive search, default using this parameter to search)     - user: Display as `Accounts` in the APP (search user accounts)     - hashtag: Display as `Hashtags` in the APP (search hashtags)     - article: Display as `Posts` in the APP (search articles) ### Return: - Search results  # [示例/Example] query = \"lemon8\" max_cursor = \"\" filter_type = \"\" order_by = \"\" search_tab = \"main\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()
query = NULL # object | 搜索关键词/Search keyword
max_cursor = NULL # object | 翻页参数/Pagination parameter (optional)
filter_type = NULL # object | 搜索过滤类型/Search filter type (optional)
order_by = NULL # object | 搜索排序方式/Search sort type (optional)
search_tab = NULL # object | 搜索类型/Search type (optional)

try:
    # 搜索接口/Search API
    api_instance.fetch_search_api_v1_lemon8_app_fetch_search_get(query, max_cursor=max_cursor, filter_type=filter_type, order_by=order_by, search_tab=search_tab)
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_search_api_v1_lemon8_app_fetch_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**object**](.md)| 搜索关键词/Search keyword | 
 **max_cursor** | [**object**](.md)| 翻页参数/Pagination parameter | [optional] 
 **filter_type** | [**object**](.md)| 搜索过滤类型/Search filter type | [optional] 
 **order_by** | [**object**](.md)| 搜索排序方式/Search sort type | [optional] 
 **search_tab** | [**object**](.md)| 搜索类型/Search type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get**
> fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get(forum_id)

获取话题信息/Get topic information

# [中文] ### 用途: - 获取话题信息 ### 参数: - forum_id: 话题ID，可以从下面的接口获取     - 获取指定作品的信息：`/lemon8/app/fetch_post_detail`     - 获取发现页的 Editor's Picks：`/lemon8/app/fetch_discover_tab_information_tabs`     - 通过接口搜索 Hashtag：`/lemon8/app/fetch_search?search_tab=hashtag&keyword=lemon8` ### 返回: - 话题信息  # [English] ### Purpose: - Get topic information ### Parameters: - forum_id: Topic ID, can be obtained from the following interfaces     - Get information of specified post: `/lemon8/app/fetch_post_detail`     - Get Editor's Picks of discover page: `/lemon8/app/fetch_discover_tab_information_tabs`     - Search Hashtag through interface: `/lemon8/app/fetch_search?search_tab=hashtag&keyword=lemon8` ### Return: - Topic information  # [示例/Example] forum_id = \"7174447913778593798\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()
forum_id = NULL # object | 话题ID/Topic ID

try:
    # 获取话题信息/Get topic information
    api_instance.fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get(forum_id)
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forum_id** | [**object**](.md)| 话题ID/Topic ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get**
> fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get(category, category_parameter, hashtag_name, max_behot_time=max_behot_time, sort_type=sort_type)

获取话题作品列表/Get topic post list

# [中文] ### 用途: - 获取话题作品列表 ### 参数: - category: 话题分类 ID，可以从接口`/lemon8/app/fetch_topic_info`获取 - max_behot_time: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的max_behot_time进行翻页。 - category_parameter: 分类参数ID，可以从接口`/lemon8/app/fetch_topic_info`获取 - hashtag_name: Hashtag名称，可以从接口`/lemon8/app/fetch_topic_info`获取 - sort_type: 排序方式，0为默认排序，当前只支持使用默认排序，请不要传入其他值。 ### 返回: - 作品列表  # [English] ### Purpose: - Get topic post list ### Parameters: - category: Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info` - max_behot_time: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the max_behot_time returned by the last request is used for subsequent requests. - category_parameter: Category parameter ID, can be obtained from the interface `/lemon8/app/fetch_topic_info` - hashtag_name: Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info` - sort_type: Sort type, 0 for default sort, currently only support default sort, please do not pass other values. ### Return: - Post list  # [示例/Example] category = \"590\" max_behot_time = \"\" category_parameter = \"7174447913778593798\" hashtag_name = \"lemon8christmas\" sort_type = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()
category = NULL # object | 话题分类 ID/Topic category ID
category_parameter = NULL # object | 分类参数/Category parameter
hashtag_name = NULL # object | Hashtag名称/Hashtag name
max_behot_time = NULL # object | 翻页参数/Pagination parameter (optional)
sort_type = NULL # object | 排序方式/Sort type (optional)

try:
    # 获取话题作品列表/Get topic post list
    api_instance.fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get(category, category_parameter, hashtag_name, max_behot_time=max_behot_time, sort_type=sort_type)
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | [**object**](.md)| 话题分类 ID/Topic category ID | 
 **category_parameter** | [**object**](.md)| 分类参数/Category parameter | 
 **hashtag_name** | [**object**](.md)| Hashtag名称/Hashtag name | 
 **max_behot_time** | [**object**](.md)| 翻页参数/Pagination parameter | [optional] 
 **sort_type** | [**object**](.md)| 排序方式/Sort type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get**
> fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get(user_id, cursor=cursor)

获取指定用户的粉丝列表/Get fans list of specified user

# [中文] ### 用途: - 获取指定用户的粉丝列表 ### 参数: - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取 - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。 ### 返回: - 粉丝列表  # [English] ### Purpose: - Get fans list of specified user ### Parameters: - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id` - cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests. ### Return: - Fans list  # [示例/Example] user_id = \"7428056850216862763\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()
user_id = NULL # object | 用户ID/User ID
cursor = NULL # object | 翻页参数/Pagination parameter (optional)

try:
    # 获取指定用户的粉丝列表/Get fans list of specified user
    api_instance.fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get(user_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **cursor** | [**object**](.md)| 翻页参数/Pagination parameter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get**
> fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get(user_id, cursor=cursor)

获取指定用户的关注列表/Get following list of specified user

# [中文] ### 用途: - 获取指定用户的关注列表 ### 参数: - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取 - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。 ### 返回: - 关注列表  # [English] ### Purpose: - Get following list of specified user ### Parameters: - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id` - cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests. ### Return: - Following list  # [示例/Example] user_id = \"7428056850216862763\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()
user_id = NULL # object | 用户ID/User ID
cursor = NULL # object | 翻页参数/Pagination parameter (optional)

try:
    # 获取指定用户的关注列表/Get following list of specified user
    api_instance.fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get(user_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **cursor** | [**object**](.md)| 翻页参数/Pagination parameter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_id_api_v1_lemon8_app_get_item_id_get**
> get_item_id_api_v1_lemon8_app_get_item_id_get(share_text)

通过分享链接获取作品ID/Get post ID through sharing link

# [中文] ### 用途: - 通过分享链接获取作品ID ### 参数: - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 作品ID  # [English] ### Purpose: - Get post ID through sharing link ### Parameters: - share_text: Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - Post ID  # [示例/Example] share_text = \"https://www.lemon8-app.com/@deathlabs_/7445613324903006766\" share_text = \"https://v.lemon8-app.com/al/OghwFTppx\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()
share_text = NULL # object | 分享链接/Share link

try:
    # 通过分享链接获取作品ID/Get post ID through sharing link
    api_instance.get_item_id_api_v1_lemon8_app_get_item_id_get(share_text)
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->get_item_id_api_v1_lemon8_app_get_item_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_text** | [**object**](.md)| 分享链接/Share link | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_ids_api_v1_lemon8_app_get_item_ids_post**
> get_item_ids_api_v1_lemon8_app_get_item_ids_post()

通过分享链接批量获取作品ID/Get post IDs in batch through sharing links

# [中文] ### 用途: - 通过分享链接批量获取作品ID，一次最多获取10个 ### 参数: - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 作品ID列表  # [English] ### Purpose: - Get post IDs in batch through sharing links, up to 10 at a time ### Parameters: - share_texts: Share links list, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - Post IDs list  # [示例/Example] share_texts = [     \"https://www.lemon8-app.com/@deathlabs_/7445613324903006766\",     \"https://v.lemon8-app.com/al/OghwFTppx\" ]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()

try:
    # 通过分享链接批量获取作品ID/Get post IDs in batch through sharing links
    api_instance.get_item_ids_api_v1_lemon8_app_get_item_ids_post()
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->get_item_ids_api_v1_lemon8_app_get_item_ids_post: %s\n" % e)
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

# **get_user_id_api_v1_lemon8_app_get_user_id_get**
> get_user_id_api_v1_lemon8_app_get_user_id_get(share_text)

通过分享链接获取用户ID/Get user ID through sharing link

# [中文] ### 用途: - 通过分享链接获取用户ID ### 参数: - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 用户ID  # [English] ### Purpose: - Get user ID through sharing link ### Parameters: - share_text: Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - User ID  # [示例/Example] share_text = \"https://www.lemon8-app.com/lemon8cars?region=us\" share_text = \"https://v.lemon8-app.com/al/OgZrsUppx\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()
share_text = NULL # object | 分享链接/Share link

try:
    # 通过分享链接获取用户ID/Get user ID through sharing link
    api_instance.get_user_id_api_v1_lemon8_app_get_user_id_get(share_text)
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->get_user_id_api_v1_lemon8_app_get_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_text** | [**object**](.md)| 分享链接/Share link | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ids_api_v1_lemon8_app_get_user_ids_post**
> get_user_ids_api_v1_lemon8_app_get_user_ids_post()

通过分享链接批量获取用户ID/Get user IDs in batch through sharing links

# [中文] ### 用途: - 通过分享链接批量获取用户ID，一次最多获取10个 ### 参数: - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 用户ID列表  # [English] ### Purpose: - Get user IDs in batch through sharing links, up to 10 at a time ### Parameters: - share_texts: Share links list, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - User IDs list  # [示例/Example] share_texts = [     \"https://www.lemon8-app.com/lemon8cars?region=us\",     \"https://v.lemon8-app.com/al/OgZrsUppx\" ]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()

try:
    # 通过分享链接批量获取用户ID/Get user IDs in batch through sharing links
    api_instance.get_user_ids_api_v1_lemon8_app_get_user_ids_post()
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->get_user_ids_api_v1_lemon8_app_get_user_ids_post: %s\n" % e)
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

# **handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get**
> handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get(user_id)

获取指定用户的信息/Get information of specified user

# [中文] ### 用途: - 获取指定用户的信息 ### 参数: - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取 ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id` ### Return: - User information  # [示例/Example] user_id = \"7217844966059656197\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Lemon8AppAPIApi()
user_id = NULL # object | 用户ID/User ID

try:
    # 获取指定用户的信息/Get information of specified user
    api_instance.handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get(user_id)
except ApiException as e:
    print("Exception when calling Lemon8AppAPIApi->handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get: %s\n" % e)
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

