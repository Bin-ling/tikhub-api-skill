# swagger_client.ThreadsWebAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_post_comments_api_v1_threads_web_fetch_post_comments_get**](ThreadsWebAPIApi.md#fetch_post_comments_api_v1_threads_web_fetch_post_comments_get) | **GET** /api/v1/threads/web/fetch_post_comments | 获取帖子评论/Get post comments
[**fetch_post_detail_api_v1_threads_web_fetch_post_detail_get**](ThreadsWebAPIApi.md#fetch_post_detail_api_v1_threads_web_fetch_post_detail_get) | **GET** /api/v1/threads/web/fetch_post_detail | 获取帖子详情/Get post detail
[**fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get**](ThreadsWebAPIApi.md#fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get) | **GET** /api/v1/threads/web/fetch_post_detail_v2 | 获取帖子详情 V2(支持链接)/Get post detail V2(supports URL)
[**fetch_user_info_api_v1_threads_web_fetch_user_info_get**](ThreadsWebAPIApi.md#fetch_user_info_api_v1_threads_web_fetch_user_info_get) | **GET** /api/v1/threads/web/fetch_user_info | 获取用户信息/Get user info
[**fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get**](ThreadsWebAPIApi.md#fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get) | **GET** /api/v1/threads/web/fetch_user_info_by_id | 根据用户ID获取用户信息/Get user info by ID
[**fetch_user_posts_api_v1_threads_web_fetch_user_posts_get**](ThreadsWebAPIApi.md#fetch_user_posts_api_v1_threads_web_fetch_user_posts_get) | **GET** /api/v1/threads/web/fetch_user_posts | 获取用户帖子列表/Get user posts
[**fetch_user_replies_api_v1_threads_web_fetch_user_replies_get**](ThreadsWebAPIApi.md#fetch_user_replies_api_v1_threads_web_fetch_user_replies_get) | **GET** /api/v1/threads/web/fetch_user_replies | 获取用户回复列表/Get user replies
[**fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get**](ThreadsWebAPIApi.md#fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get) | **GET** /api/v1/threads/web/fetch_user_reposts | 获取用户转发列表/Get user reposts
[**search_profiles_api_v1_threads_web_search_profiles_get**](ThreadsWebAPIApi.md#search_profiles_api_v1_threads_web_search_profiles_get) | **GET** /api/v1/threads/web/search_profiles | 搜索用户档案/Search profiles
[**search_recent_api_v1_threads_web_search_recent_get**](ThreadsWebAPIApi.md#search_recent_api_v1_threads_web_search_recent_get) | **GET** /api/v1/threads/web/search_recent | 搜索最新内容/Search recent content
[**search_top_api_v1_threads_web_search_top_get**](ThreadsWebAPIApi.md#search_top_api_v1_threads_web_search_top_get) | **GET** /api/v1/threads/web/search_top | 搜索热门内容/Search top content


# **fetch_post_comments_api_v1_threads_web_fetch_post_comments_get**
> fetch_post_comments_api_v1_threads_web_fetch_post_comments_get(post_id, end_cursor=end_cursor)

获取帖子评论/Get post comments

# [中文] ### 用途: - 获取Threads帖子评论列表 - 价格：0.002$ / 次 ### 参数: - post_id: 帖子ID，例如：3390920896561588969 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 帖子评论列表数据，包含:     - comments: 评论列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Get Threads post comments list - Price: 0.002$ / time ### Parameters: - post_id: Post ID, for example: 3390920896561588969 - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - Post comments list data, including:     - comments: Comment list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] post_id = \"3390920896561588969\" end_cursor = None  # or a cursor string from previous response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
post_id = NULL # object | 帖子ID/Post ID
end_cursor = NULL # object | 分页游标/Pagination cursor (optional) (optional)

try:
    # 获取帖子评论/Get post comments
    api_instance.fetch_post_comments_api_v1_threads_web_fetch_post_comments_get(post_id, end_cursor=end_cursor)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->fetch_post_comments_api_v1_threads_web_fetch_post_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | [**object**](.md)| 帖子ID/Post ID | 
 **end_cursor** | [**object**](.md)| 分页游标/Pagination cursor (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_post_detail_api_v1_threads_web_fetch_post_detail_get**
> fetch_post_detail_api_v1_threads_web_fetch_post_detail_get(post_id)

获取帖子详情/Get post detail

# [中文] ### 用途: - 获取Threads帖子详情 - 价格：0.002$ / 次 ### 参数: - post_id: 帖子ID（纯数字），例如：3349029093483693129，可以从其他接口获取，如果是使用URL获取，去调用 /fetch_post_detail_v2 接口。 ### 返回: - 帖子详情数据，包含:     - id: 帖子ID     - text: 帖子文本内容     - user: 发布者信息     - image_versions2: 图片信息     - video_versions: 视频信息     - like_count: 点赞数     - text_post_app_info: 帖子应用信息     - 等等...  # [English] ### Purpose: - Get Threads post detail - Price: 0.002$ / time ### Parameters: - post_id: Post ID (numeric only), for example: 3349029093483693129, can be obtained from other APIs. If using URL to get, call /fetch_post_detail_v2 API. ### Return: - Post detail data, including:     - id: Post ID     - text: Post text content     - user: Publisher information     - image_versions2: Image information     - video_versions: Video information     - like_count: Like count     - text_post_app_info: Post app information     - etc...  # [示例/Example] post_id = \"3349029093483693129\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
post_id = NULL # object | 帖子ID/Post ID

try:
    # 获取帖子详情/Get post detail
    api_instance.fetch_post_detail_api_v1_threads_web_fetch_post_detail_get(post_id)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->fetch_post_detail_api_v1_threads_web_fetch_post_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | [**object**](.md)| 帖子ID/Post ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get**
> fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get(post_id=post_id, url=url)

获取帖子详情 V2(支持链接)/Get post detail V2(supports URL)

# [中文] ### 用途: - 获取Threads帖子详情（支持短代码和完整URL） - 价格：0.002$ / 次 ### 参数: - post_id: 帖子短代码（可选），例如：DPVUglOjOUu，可以从帖子URL中提取，例如：https://www.threads.com/@taylorswift/post/DPVUglOjOUu 中的 DPVUglOjOUu - url: 完整的帖子URL（可选），例如：https://www.threads.com/@taylorswift/post/DPVUglOjOUu - 注意：post_id 和 url 至少提供一个参数 ### 返回: - 帖子详情数据，包含:     - post_id: 帖子ID     - text: 帖子文本内容     - user: 发布者信息     - media: 媒体信息（图片、视频）     - like_count: 点赞数     - reply_count: 回复数     - repost_count: 转发数     - timestamp: 发布时间     - 等等...  # [English] ### Purpose: - Get Threads post detail (supports short code and full URL) - Price: 0.002$ / time ### Parameters: - post_id: Post short code (optional), for example: DPVUglOjOUu, can be extracted from post URL, e.g., DPVUglOjOUu in https://www.threads.com/@taylorswift/post/DPVUglOjOUu - url: Full post URL (optional), for example: https://www.threads.com/@taylorswift/post/DPVUglOjOUu - Note: At least one of post_id or url must be provided ### Return: - Post detail data, including:     - post_id: Post ID     - text: Post text content     - user: Publisher information     - media: Media information (images, videos)     - like_count: Like count     - reply_count: Reply count     - repost_count: Repost count     - timestamp: Publish timestamp     - etc...  # [示例/Example] post_id = \"DPVUglOjOUu\" # or url = \"https://www.threads.com/@taylorswift/post/DPVUglOjOUu\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
post_id = NULL # object | 帖子短代码/Post short code (optional)
url = NULL # object | 完整帖子URL/Full post URL (optional)

try:
    # 获取帖子详情 V2(支持链接)/Get post detail V2(supports URL)
    api_instance.fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get(post_id=post_id, url=url)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | [**object**](.md)| 帖子短代码/Post short code | [optional] 
 **url** | [**object**](.md)| 完整帖子URL/Full post URL | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_info_api_v1_threads_web_fetch_user_info_get**
> fetch_user_info_api_v1_threads_web_fetch_user_info_get(username)

获取用户信息/Get user info

# [中文] ### 用途: - 获取Threads用户信息 - 价格：0.002$ / 次 ### 参数: - username: 用户名，例如：lilbieber，可以从用户主页链接中获取，例如：https://www.threads.net/@lilbieber 中的 lilbieber。 ### 返回: - 用户信息数据，包含:     - pk: 用户ID     - username: 用户名     - full_name: 全名     - biography: 个人简介     - profile_pic_url: 头像URL     - follower_count: 粉丝数     - is_verified: 是否认证     - 等等...  # [English] ### Purpose: - Get Threads user information - Price: 0.002$ / time ### Parameters: - username: Username, for example: lilbieber, can be obtained from the user's homepage link, for example: lilbieber in https://www.threads.net/@lilbieber ### Return: - User information data, including:     - pk: User ID     - username: Username     - full_name: Full name     - biography: Biography     - profile_pic_url: Profile picture URL     - follower_count: Follower count     - is_verified: Is verified     - etc...  # [示例/Example] username = \"lilbieber\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
username = NULL # object | 用户名/Username

try:
    # 获取用户信息/Get user info
    api_instance.fetch_user_info_api_v1_threads_web_fetch_user_info_get(username)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->fetch_user_info_api_v1_threads_web_fetch_user_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)| 用户名/Username | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get**
> fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get(user_id)

根据用户ID获取用户信息/Get user info by ID

# [中文] ### 用途: - 根据用户ID获取Threads用户信息 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：67027868801，可以从用户主页API或帖子数据中获取。 ### 返回: - 用户信息数据，包含:     - pk: 用户ID     - username: 用户名     - full_name: 全名     - biography: 个人简介     - profile_pic_url: 头像URL     - follower_count: 粉丝数     - is_verified: 是否认证     - 等等...  # [English] ### Purpose: - Get Threads user information by user ID - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 67027868801, can be obtained from user profile API or post data ### Return: - User information data, including:     - pk: User ID     - username: Username     - full_name: Full name     - biography: Biography     - profile_pic_url: Profile picture URL     - follower_count: Follower count     - is_verified: Is verified     - etc...  # [示例/Example] user_id = \"67027868801\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
user_id = NULL # object | 用户ID/User ID

try:
    # 根据用户ID获取用户信息/Get user info by ID
    api_instance.fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get(user_id)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get: %s\n" % e)
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

# **fetch_user_posts_api_v1_threads_web_fetch_user_posts_get**
> fetch_user_posts_api_v1_threads_web_fetch_user_posts_get(user_id, end_cursor=end_cursor)

获取用户帖子列表/Get user posts

# [中文] ### 用途: - 获取Threads用户的帖子列表 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：63625256886，可以从用户主页API获取。 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 用户帖子列表数据，包含:     - threads: 帖子列表数组     - next_cursor: 下一页游标     - has_more: 是否有更多数据     - 每个帖子包含:         - id: 帖子ID         - text: 帖子文本内容         - user: 发布者信息         - image_versions2: 图片信息         - video_versions: 视频信息         - like_count: 点赞数         - text_post_app_info: 帖子应用信息         - 等等...  # [English] ### Purpose: - Get Threads user's post list - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 63625256886, can be obtained from user profile API - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - User post list data, including:     - threads: Post list array     - next_cursor: Next page cursor     - has_more: Has more data     - Each post contains:         - id: Post ID         - text: Post text content         - user: Publisher information         - image_versions2: Image information         - video_versions: Video information         - like_count: Like count         - text_post_app_info: Post app information         - etc...  # [示例/Example] user_id = \"63625256886\" end_cursor = None  # or a cursor string from previous response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
user_id = NULL # object | 用户ID/User ID
end_cursor = NULL # object | 分页游标/Pagination cursor (optional) (optional)

try:
    # 获取用户帖子列表/Get user posts
    api_instance.fetch_user_posts_api_v1_threads_web_fetch_user_posts_get(user_id, end_cursor=end_cursor)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->fetch_user_posts_api_v1_threads_web_fetch_user_posts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **end_cursor** | [**object**](.md)| 分页游标/Pagination cursor (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_replies_api_v1_threads_web_fetch_user_replies_get**
> fetch_user_replies_api_v1_threads_web_fetch_user_replies_get(user_id, end_cursor=end_cursor)

获取用户回复列表/Get user replies

# [中文] ### 用途: - 获取Threads用户的回复列表 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：63625256886 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 用户回复列表数据，包含:     - threads: 回复列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Get Threads user's reply list - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 63625256886 - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - User reply list data, including:     - threads: Reply list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] user_id = \"63625256886\" end_cursor = None  # or a cursor string from previous response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
user_id = NULL # object | 用户ID/User ID
end_cursor = NULL # object | 分页游标/Pagination cursor (optional) (optional)

try:
    # 获取用户回复列表/Get user replies
    api_instance.fetch_user_replies_api_v1_threads_web_fetch_user_replies_get(user_id, end_cursor=end_cursor)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->fetch_user_replies_api_v1_threads_web_fetch_user_replies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **end_cursor** | [**object**](.md)| 分页游标/Pagination cursor (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get**
> fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get(user_id, end_cursor=end_cursor)

获取用户转发列表/Get user reposts

# [中文] ### 用途: - 获取Threads用户的转发列表 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：63625256886 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 用户转发列表数据，包含:     - threads: 转发列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Get Threads user's repost list - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 63625256886 - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - User repost list data, including:     - threads: Repost list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] user_id = \"63625256886\" end_cursor = None  # or a cursor string from previous response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
user_id = NULL # object | 用户ID/User ID
end_cursor = NULL # object | 分页游标/Pagination cursor (optional) (optional)

try:
    # 获取用户转发列表/Get user reposts
    api_instance.fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get(user_id, end_cursor=end_cursor)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **end_cursor** | [**object**](.md)| 分页游标/Pagination cursor (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_profiles_api_v1_threads_web_search_profiles_get**
> search_profiles_api_v1_threads_web_search_profiles_get(query)

搜索用户档案/Search profiles

# [中文] ### 用途: - 搜索Threads用户档案 - 价格：0.002$ / 次 ### 参数: - query: 搜索关键词，例如：mark ### 返回: - 搜索结果数据，包含:     - users: 用户列表     - 每个用户包含:         - pk: 用户ID         - username: 用户名         - full_name: 全名         - profile_pic_url: 头像URL         - is_verified: 是否认证         - follower_count: 粉丝数         - 等等...  # [English] ### Purpose: - Search Threads user profiles - Price: 0.002$ / time ### Parameters: - query: Search query, for example: mark ### Return: - Search result data, including:     - users: User list     - Each user contains:         - pk: User ID         - username: Username         - full_name: Full name         - profile_pic_url: Profile picture URL         - is_verified: Is verified         - follower_count: Follower count         - etc...  # [示例/Example] query = \"mark\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
query = NULL # object | 搜索关键词/Search query

try:
    # 搜索用户档案/Search profiles
    api_instance.search_profiles_api_v1_threads_web_search_profiles_get(query)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->search_profiles_api_v1_threads_web_search_profiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**object**](.md)| 搜索关键词/Search query | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_recent_api_v1_threads_web_search_recent_get**
> search_recent_api_v1_threads_web_search_recent_get(query, end_cursor=end_cursor)

搜索最新内容/Search recent content

# [中文] ### 用途: - 搜索Threads最新内容 - 价格：0.002$ / 次 ### 参数: - query: 搜索关键词，例如：bitcoin - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 搜索结果数据，包含:     - threads: 帖子列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Search Threads recent content - Price: 0.002$ / time ### Parameters: - query: Search query, for example: bitcoin - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - Search result data, including:     - threads: Post list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] query = \"bitcoin\" end_cursor = None  # or a cursor string from previous response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
query = NULL # object | 搜索关键词/Search query
end_cursor = NULL # object | 分页游标/Pagination cursor (optional) (optional)

try:
    # 搜索最新内容/Search recent content
    api_instance.search_recent_api_v1_threads_web_search_recent_get(query, end_cursor=end_cursor)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->search_recent_api_v1_threads_web_search_recent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**object**](.md)| 搜索关键词/Search query | 
 **end_cursor** | [**object**](.md)| 分页游标/Pagination cursor (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_top_api_v1_threads_web_search_top_get**
> search_top_api_v1_threads_web_search_top_get(query, end_cursor=end_cursor)

搜索热门内容/Search top content

# [中文] ### 用途: - 搜索Threads热门内容 - 价格：0.002$ / 次 ### 参数: - query: 搜索关键词，例如：bitcoin - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 搜索结果数据，包含:     - threads: 帖子列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Search Threads top content - Price: 0.002$ / time ### Parameters: - query: Search query, for example: bitcoin - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - Search result data, including:     - threads: Post list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] query = \"bitcoin\" end_cursor = None  # or a cursor string from previous response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThreadsWebAPIApi()
query = NULL # object | 搜索关键词/Search query
end_cursor = NULL # object | 分页游标/Pagination cursor (optional) (optional)

try:
    # 搜索热门内容/Search top content
    api_instance.search_top_api_v1_threads_web_search_top_get(query, end_cursor=end_cursor)
except ApiException as e:
    print("Exception when calling ThreadsWebAPIApi->search_top_api_v1_threads_web_search_top_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**object**](.md)| 搜索关键词/Search query | 
 **end_cursor** | [**object**](.md)| 分页游标/Pagination cursor (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

