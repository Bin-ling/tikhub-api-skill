# swagger_client.KuaishouWebAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get**](KuaishouWebAPIApi.md#fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get) | **GET** /api/v1/kuaishou/web/fetch_get_user_id | 获取用户ID/Fetch user ID
[**fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get**](KuaishouWebAPIApi.md#fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get) | **GET** /api/v1/kuaishou/web/fetch_kuaishou_hot_list_v1 | 获取快手热榜 V1/Fetch Kuaishou Hot List V1
[**fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get**](KuaishouWebAPIApi.md#fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get) | **GET** /api/v1/kuaishou/web/fetch_kuaishou_hot_list_v2 | 获取快手热榜 V2/Fetch Kuaishou Hot List V2
[**fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get**](KuaishouWebAPIApi.md#fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get) | **GET** /api/v1/kuaishou/web/fetch_one_video | 获取单个作品数据 V1/Get single video data V1
[**fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get**](KuaishouWebAPIApi.md#fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get) | **GET** /api/v1/kuaishou/web/fetch_one_video_by_url | 链接获取作品数据/Fetch single video by URL
[**fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get**](KuaishouWebAPIApi.md#fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get) | **GET** /api/v1/kuaishou/web/fetch_one_video_comment | 获取作品一级评论/Fetch video comments
[**fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get**](KuaishouWebAPIApi.md#fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get) | **GET** /api/v1/kuaishou/web/fetch_one_video_sub_comment | 获取作品二级评论/Fetch video sub comments
[**fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get**](KuaishouWebAPIApi.md#fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get) | **GET** /api/v1/kuaishou/web/fetch_one_video_v2 | 获取单个作品数据 V2/Get single video data V2
[**fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get**](KuaishouWebAPIApi.md#fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get) | **GET** /api/v1/kuaishou/web/fetch_user_collect | 获取用户收藏作品/Fetch user collect
[**fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get**](KuaishouWebAPIApi.md#fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get) | **GET** /api/v1/kuaishou/web/fetch_user_info | 获取用户信息/Fetch user info
[**fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get**](KuaishouWebAPIApi.md#fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get) | **GET** /api/v1/kuaishou/web/fetch_user_live_replay | 获取用户直播回放/Fetch user live replay
[**fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get**](KuaishouWebAPIApi.md#fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get) | **GET** /api/v1/kuaishou/web/fetch_user_post | 获取用户发布作品/Fetch user posts
[**generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get**](KuaishouWebAPIApi.md#generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get) | **GET** /api/v1/kuaishou/web/generate_share_short_url | 生成分享短连接/Generate share short URL


# **fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get**
> fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get(share_link)

获取用户ID/Fetch user ID

# [中文] ### 用途: - 通过用户分享链接获取用户ID ### 参数: - share_link: 用户分享链接 ### 返回: - 用户ID  # [English] ### Purpose: - Fetch user ID via user share link ### Parameters: - share_link: User share link ### Returns: - User ID  # [示例/Example] share_link = \"https://v.kuaishou.com/KcdKDwFp\"  share_link = \"https://c.kuaishou.com/fw/user/3xcuu5habgc8z29\"  share_link = \"https://live.kuaishou.com/profile/3xcuu5habgc8z29?fid=2357689552&cc=share_copylink\"  # [返回示例/Example Response] ```json ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
share_link = NULL # object | 

try:
    # 获取用户ID/Fetch user ID
    api_instance.fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get(share_link)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_link** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get**
> fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get()

获取快手热榜 V1/Fetch Kuaishou Hot List V1

# [中文] ### 用途: - 获取快手热榜 V1 ### 参数: - 无 ### 返回: - 快手热榜 V1 列表  # [English] ### Purpose: - Fetch Kuaishou Hot List V1 ### Parameters: - None ### Returns: - Kuaishou Hot List V1  # [示例/Example]  # [返回示例/Example Response] ```json  ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()

try:
    # 获取快手热榜 V1/Fetch Kuaishou Hot List V1
    api_instance.fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get()
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get: %s\n" % e)
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

# **fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get**
> fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get(board_type=board_type)

获取快手热榜 V2/Fetch Kuaishou Hot List V2

# [中文] ### 用途: - 获取快手热榜 V2 ### 参数: - board_type 榜单类型，默认值为 1:     1 - 热榜     2 - 文娱     3 - 社会     4 - 有用     5 - 挑战     6 - 搜索 ### 返回: - 快手热榜 V2 列表  # [English] ### Purpose: - Fetch Kuaishou Hot List V2 ### Parameters: - board_type: Board Type, default is 1:     1 - Hot List     2 - Entertainment     3 - Society     4 - Useful     5 - Challenge     6 - Search ### Returns: - Kuaishou Hot List V2  # [示例/Example]  # [返回示例/Example Response] ```json  ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
board_type = NULL # object |  (optional)

try:
    # 获取快手热榜 V2/Fetch Kuaishou Hot List V2
    api_instance.fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get(board_type=board_type)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_type** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get**
> fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get(share_text)

获取单个作品数据 V1/Get single video data V1

# [中文] ### 用途: - 获取单个作品数据，此接口不支持图文作品。 ### 参数: - share_text: 作品分享链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video data, this interface does not support photo only posts. ### Parameters: - share_text: Photo share link ### Returns: - Video data  # [示例/Example] share_text = \"https://www.kuaishou.com/f/X-f2k5KJpiXN1SY\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
share_text = NULL # object | 

try:
    # 获取单个作品数据 V1/Get single video data V1
    api_instance.fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get(share_text)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_text** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get**
> fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get(url)

链接获取作品数据/Fetch single video by URL

# [中文] ### 用途: - 根据链接获取单个作品数据 ### 参数: - url: 作品链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video by URL ### Parameters: - url: Photo URL ### Returns: - Video data  # [示例/Example] url = \"https://v.kuaishou.com/GKTpYm\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
url = NULL # object | 

try:
    # 链接获取作品数据/Fetch single video by URL
    api_instance.fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get(url)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get**
> fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get(photo_id, pcursor=pcursor)

获取作品一级评论/Fetch video comments

# [中文] ### 用途: - 获取单个作品评论数据 ### 参数: - photo_id: 作品ID - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 评论数据  # [English] ### Purpose: - Fetch single video comment data ### Parameters: - photo_id: Photo ID - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Comments data  # [示例/Example] photo_id = \"3x7gxp2zhgjv832\" pcursor = None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
photo_id = NULL # object | 
pcursor = NULL # object |  (optional)

try:
    # 获取作品一级评论/Fetch video comments
    api_instance.fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get(photo_id, pcursor=pcursor)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photo_id** | [**object**](.md)|  | 
 **pcursor** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get**
> fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get(photo_id, root_comment_id, pcursor=pcursor)

获取作品二级评论/Fetch video sub comments

# [中文] ### 用途: - 获取单个作品二级评论数据 ### 参数: - photo_id: 作品ID - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 - root_comment_id: 根评论ID ### 返回: - 评论数据  # [English] ### Purpose: - Fetch single video comment data ### Parameters: - photo_id: Photo ID - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. - root_comment_id: Root comment ID ### Returns: - Comments data  # [示例/Example] photo_id = \"3xgarycnydawq3g\" pcursor = \"909377053156\" root_comment_id = \"908850553827\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
photo_id = NULL # object | 
root_comment_id = NULL # object | 
pcursor = NULL # object |  (optional)

try:
    # 获取作品二级评论/Fetch video sub comments
    api_instance.fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get(photo_id, root_comment_id, pcursor=pcursor)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photo_id** | [**object**](.md)|  | 
 **root_comment_id** | [**object**](.md)|  | 
 **pcursor** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get**
> fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get(photo_id)

获取单个作品数据 V2/Get single video data V2

# [中文] ### 用途: - 快手单一视频查询接口V2 ### 参数: - photo_id: 作品ID，作品ID可以从作品链接中提取 ### 返回: - 视频数据  # [English] ### Purpose: - Kuaishou single video query API V2 ### Parameters: - photo_id: Photo ID, the photo ID can be extracted from the photo link ### Returns: - Video data  # [示例/Example] photo_id = \"3xtdqvdnqd3psuc\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
photo_id = NULL # object | 

try:
    # 获取单个作品数据 V2/Get single video data V2
    api_instance.fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get(photo_id)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photo_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get**
> fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get(user_id, pcursor=pcursor)

获取用户收藏作品/Fetch user collect

# [中文] ### 用途: - 获取用户收藏作品 ### 参数: - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取 - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid - 备注：不支持使用uid也就是纯数字的用户ID查询 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 用户收藏作品列表  # [English] ### Purpose: - Fetch user favorite - Note: This API requires the user's eid, which can be extracted from the user's profile URL. - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq. - Note: Querying with uid (pure numeric user ID) is not supported. ### Parameters: - user_id: User ID - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - User favorite list  # [示例/Example] user_id = \"3xz63mn6fngqtiq\" pcursor = None  # [返回示例/Example Response] ```json  ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
user_id = NULL # object | 
pcursor = NULL # object |  (optional)

try:
    # 获取用户收藏作品/Fetch user collect
    api_instance.fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get(user_id, pcursor=pcursor)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 
 **pcursor** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get**
> fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get(user_id)

获取用户信息/Fetch user info

# [中文]     ### 用途:     - 获取用户信息     - 备注：     - 此接口在请求时请将超时时间设置为30秒以上，否则可能会导致客户端未及时收到请求响应并且导致计费。     - 此接口由于风控的特殊性，我们尽可能保持稳定，但仍然无法保证100%稳定，如果遇到请求失败，请稍后重试。     - 推荐一直重复请求，直到成功为止，并且超时时间设置为30秒以上。     ### 参数:     - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取     - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid     - 备注：不支持使用uid也就是纯数字的用户ID查询     ### 返回:     - 用户信息，包括昵称、头像、粉丝数、关注数、获赞数、性别等      # [English]     ### Purpose:     - Fetch user info     - Note: This API requires the user's eid, which can be extracted from the user's profile URL.     - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq.     - Note: Querying with uid (pure numeric user ID) is not supported.     - Note: Please set the timeout to more than 30 seconds when making requests to this API, otherwise it may cause the client to not receive the response in time and result in billing.     - Due to the special nature of risk control for this API, we try to keep it stable, but we still cannot guarantee 100% stability. If you encounter a request failure, please try again later.     - It is recommended to keep retrying until successful, and set the timeout to more than 30 seconds.     ### Parameters:     - user_id: User ID     ### Returns:     - User info, including nickname, avatar, number of followers, number of followings, number      # [示例/Example]     user_id = \"3xz63mn6fngqtiq\"      # [返回示例/Example Response]     ```json     {         \"code\": 200,         \"request_id\": \"782e6fa2-4c8e-4fac-b151-78db03c10b8d\",         \"router\": \"/api/v1/kuaishou/web/fetch_user_info\",         \"params\": {             \"user_id\": \"3xz63mn6fngqtiq\"         },         \"data\": {             \"result\": 1,             \"userProfile\": {                 \"profile\": {                     \"user_profile_bg_url\": \"//s2-10623.kwimgs.com/kos/nlav10623/vision_images/profile_background.5bc08b1bf4fba1f4.svg\",                     \"user_id\": \"3xz63mn6fngqtiq\",                     \"user_name\": \"权少爱吃小汉堡🍔\",                     \"headurl\": \"https://p66-pro.a.yximgs.com/uhead/AB/2025/08/11/21/BMjAyNTA4MTEyMTEyNDlfMjI4OTA1ODAyXzFfaGQ5ODdfODg4_s.jpg\",                     \"user_text\": \"感谢你的关注木木哒 我玩得游戏叫:Gmod  禁止冒充搬运视频 违者必究\"                 },                 \"gender\": \"M\",                 \"showCollectTab\": false,                 \"livingInfo\": {                     \"living\": false,                     \"livingId\": null,                     \"iconType\": 0                 },                 \"ownerCount\": {                     \"fan\": 4300985,                     \"like\": 37676016,                     \"follow\": 198,                     \"photo_public\": 237                 },                 \"userDefineId\": \"quanshaogmod\",                 \"isFollowing\": false,                 \"isUserIsolated\": false             },             \"host-name\": \"public-bjzey-c3-kce-node67.idchb1az3.hb1.kwaidc.com\"         }     }     ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
user_id = NULL # object | 

try:
    # 获取用户信息/Fetch user info
    api_instance.fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get(user_id)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get**
> fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get(user_id, pcursor=pcursor)

获取用户直播回放/Fetch user live replay

# [中文] ### 用途: - 获取用户直播回放列表 ### 参数: - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取 - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid - 备注：不支持使用uid也就是纯数字的用户ID查询 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 用户直播回放列表  # [English] ### Purpose: - Fetch user live replay - Note: This API requires the user's eid, which can be extracted from the user's profile URL. - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq. - Note: Querying with uid (pure numeric user ID) is not supported. ### Parameters: - user_id: User ID - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - User live replay list  # [示例/Example] user_id = \"3xz63mn6fngqtiq\" pcursor = None  # [返回示例/Example Response] ```json  ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
user_id = NULL # object | 
pcursor = NULL # object |  (optional)

try:
    # 获取用户直播回放/Fetch user live replay
    api_instance.fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get(user_id, pcursor=pcursor)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 
 **pcursor** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get**
> fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get(user_id, pcursor=pcursor)

获取用户发布作品/Fetch user posts

# [中文] ### 用途: - 获取用户作品列表 ### 参数: - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取 - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid - 备注： - 不支持使用uid也就是纯数字的用户ID查询 - 此接口在请求时请将超时时间设置为30秒以上，否则可能会导致客户端未及时收到请求响应并且导致计费。 - 此接口由于风控的特殊性，我们尽可能保持稳定，但仍然无法保证100%稳定，如果遇到请求失败，请稍后重试。 - 推荐一直重复请求，直到成功为止，并且超时时间设置为30秒以上。 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 用户作品列表  # [English] ### Purpose: - Fetch user posts - Note: This API requires the user's eid, which can be extracted from the user's profile URL. - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq. - Note: - Querying with uid (pure numeric user ID) is not supported. - Note: Please set the timeout to more than 30 seconds when making requests to this API, otherwise it may cause the client to not receive the response in time and result in billing. - Due to the special nature of risk control for this API, we try to keep it - stable, but we still cannot guarantee 100% stability. If you encounter a request failure, please try again later. - It is recommended to keep retrying until successful, and set the timeout to more than 30 seconds. ### Parameters: - user_id: User ID - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - User posts list  # [示例/Example] user_id = \"3xz63mn6fngqtiq\" pcursor = None  # [部分返回示例/Part Example Response] ```json {     \"code\": 200,     \"request_id\": \"de055431-bf7d-4a24-a332-9cc1654ab247\",     \"router\": \"/api/v1/kuaishou/web/fetch_user_post\",     \"params\": {         \"user_id\": \"3xz63mn6fngqtiq\",         \"pcursor\": \"1.698748219278E12\"     },     \"data\": {         \"result\": 1,         \"pcursor\": \"1.692702206373E12\",         \"feeds\": [             {                 \"type\": 1,                 \"photo\": {                     \"manifestH265\": {                         \"version\": \"1.0.0\",                         \"businessType\": 2,                         \"mediaType\": 2,                         \"videoId\": \"b1a31deb8e75e7be\",                         \"hideAuto\": false,                         \"manualDefaultSelect\": false,                         \"stereoType\": 0,                         \"adaptationSet\": [                             {                                 \"id\": 1,                                 \"duration\": 84937,                                 \"representation\": [                                     {                                         \"id\": 1,                                         \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_hd15_Bfb2327ef432b8e22bee0565c052210d0.mp4?tag=1-1756664181-unknown-0-4pez7u9yx4-11bcd04505e80c93&provider=self&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=hd15&ss=vpm\",                                         \"backupUrl\": [                                             \"https://v1.kwaicdn.com/ksc2/WsLapasbDJwa_d5-gSoI2EwR1RYcYI6MpzWrlOzqoBPJ1eG7TRpv8UtWiNxv2xy-tsiAXr2VvmiqAJQmxNCMawMQCe7orKomsXk6v-GJKt55XiiE9GdcOTmXM0Uj_MN1np_i8ffWmDHyxrrCfhiIKRMXGETtR5BcJTIxz5hg3BgWZAEVV8VxRcZ2PwP4phUM.mp4?pkey=AAWWdaRz9xwLglSkzE1QAdM0NoasskNdA0fRCgDJSWyTPo4tra_0jYCqgP_ieXHG4ky9vMQafXhiVaetL-iijtgENHHeQG2YMY8NxTVz_PjB8T1hTNmOXW8mQTnf2NHOa0k&tag=1-1756664181-unknown-1-0vq1m73bcl-d99c4fa7dba7dbf0&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=hd15&ss=vpm\"                                         ],                                         \"maxBitrate\": 3000,                                         \"avgBitrate\": 1622,                                         \"width\": 1280,                                         \"height\": 720,                                         \"frameRate\": 60.0,                                         \"quality\": 1.5,                                         \"kvqScore\": {                                             \"FR\": -1.0,                                             \"NR\": 3.4632160663604736,                                             \"FRPost\": -1.0,                                             \"NRPost\": -1.0,                                             \"sharpness\": 0.4285,                                             \"blur\": 0.2377                                         },                                         \"qualityType\": \"720p\",                                         \"qualityLabel\": \"高清\",                                         \"featureP2sp\": false,                                         \"p2spCode\": \"{\"fRsn\":0,\"fixOpt\":-1,\"schTask\":\"\",\"schCode\":-1,\"schRes\":\"\",\"pushTask\":\"v=0&p=0&s=0&d=0\",\"pushCode\":-1}\",                                         \"hidden\": false,                                         \"disableAdaptive\": false,                                         \"defaultSelect\": false,                                         \"comment\": \"videoId=b1a31deb8e75e7be/ttExplain=HEVC_Turbo2_720P_高码率/tt=hd15\",                                         \"hdrType\": 0,                                         \"fileSize\": 17227811,                                         \"agc\": false,                                         \"mute\": false,                                         \"oriLoudness\": 0.0,                                         \"makeupGain\": 0.0,                                         \"realLoudness\": -9.532,                                         \"realNormalizeGain\": 1.0,                                         \"normalizeGain\": 0.0                                     }                                 ]                             }                         ],                         \"playInfo\": {                             \"bizType\": 0,                             \"cdnTimeRangeLevel\": 0                         },                         \"videoFeature\": {                             \"blurProbability\": 0.02436523512005806,                             \"blockyProbability\": 0.5486664772033691,                             \"avgEntropy\": 11.74826078414917,                             \"mosScore\": 0.6893717646598816                         }                     },                     \"photoUrls\": [                         {                             \"cdn\": \"k0u2ayecy7bycz.djvod.ndcimgs.com\",                             \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_b_Baea19a439f265123a9b5c73a99b387c9.mp4?tag=1-1756664181-unknown-0-ngtc9b5fkw-400249aac756fa3c&provider=self&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=b&ss=vps\"                         },                         {                             \"cdn\": \"v2.kwaicdn.com\",                             \"url\": \"https://v2.kwaicdn.com/ksc2/PtGMNZW1atApoKjZtdZAeYBv_Hk3rukAMsduvp-BRuBp66aB3ZFXpDnlTON3Xy5ehrz5fc5c4ys3g0Nays7EXtftXSi7JkRjPKFMN-vbPXVZ68800hSKYaFZejJUW1GKp2ttjc9vIgAKHkCkn1E8e709mnQxJz6nzJRRixcAEvJ6PxVraa3OqiGkiA12zLt0.mp4?pkey=AAVID_YMrWOJ06oySpzkfx8i-z7z8Iyx34JyeXW13PQLMfVfPDvy1b0cEQh_2ri0Bs7F_GvTuADCNUK0SR0f0zes8DixR10HM6lJQkpQ64nHhqlVoxHkP9DQGPvgr1nZ-l4&tag=1-1756664181-unknown-1-cpfxvlhxnd-8304a252b8387036&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=b&ss=vps\"                         }                     ],                     \"manifest\": {                         \"version\": \"1.0.0\",                         \"businessType\": 2,                         \"mediaType\": 2,                         \"videoId\": \"b1a31deb8e75e7be\",                         \"hideAuto\": false,                         \"manualDefaultSelect\": false,                         \"stereoType\": 0,                         \"adaptationSet\": [                             {                                 \"id\": 1,                                 \"duration\": 84937,                                 \"representation\": [                                     {                                         \"id\": 1,                                         \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_b_Baea19a439f265123a9b5c73a99b387c9.mp4?tag=1-1756664181-unknown-0-raca8mq3p7-df6cf126f2ba1979&provider=self&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=b&ss=vpm\",                                         \"backupUrl\": [                                             \"https://v2.kwaicdn.com/ksc2/PtGMNZW1atApoKjZtdZAeYBv_Hk3rukAMsduvp-BRuBp66aB3ZFXpDnlTON3Xy5ehrz5fc5c4ys3g0Nays7EXtftXSi7JkRjPKFMN-vbPXVZ68800hSKYaFZejJUW1GKp2ttjc9vIgAKHkCkn1E8e709mnQxJz6nzJRRixcAEvJ6PxVraa3OqiGkiA12zLt0.mp4?pkey=AAUkTComC4sD_jFDy6Q8DZvnU7bttEcUKZYUyPGThMFjvLORo0aHnSv2Y7qhYldRnSBe9H1NRLi9yC1zprgWULvlD6mm7Q8pWup3vG3BabToQqpNmpHI2hwzk6m0UE-8j38&tag=1-1756664181-unknown-1-frwqzvnubq-3aeb9dc39d8958ed&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=b&ss=vpm\"                                         ],                                         \"maxBitrate\": 4900,                                         \"avgBitrate\": 3482,                                         \"width\": 1280,                                         \"height\": 720,                                         \"frameRate\": 60.0,                                         \"quality\": 1.5,                                         \"kvqScore\": {                                             \"FR\": -1.0,                                             \"NR\": 3.5491535663604736,                                             \"FRPost\": -1.0,                                             \"NRPost\": -1.0,                                             \"sharpness\": 0.3316,                                             \"blur\": 0.2374                                         },                                         \"qualityType\": \"720p\",                                         \"qualityLabel\": \"高清\",                                         \"featureP2sp\": false,                                         \"p2spCode\": \"{\"fRsn\":0,\"fixOpt\":-1,\"schTask\":\"\",\"schCode\":-1,\"schRes\":\"\",\"pushTask\":\"v=0&p=0&s=0&d=0\",\"pushCode\":-1}\",                                         \"hidden\": false,                                         \"disableAdaptive\": false,                                         \"defaultSelect\": false,                                         \"comment\": \"videoId=b1a31deb8e75e7be/ttExplain=AVC_VeryFast_720P_高码率_Basic/tt=b\",                                         \"hdrType\": 0,                                         \"fileSize\": 36976273,                                         \"bitratePattern\": [                                             5000,                                             3471,                                             6733,                                             481,                                             1569                                         ],                                         \"agc\": false,                                         \"mute\": false,                                         \"oriLoudness\": 0.0,                                         \"makeupGain\": 0.0,                                         \"realLoudness\": -9.532,                                         \"realNormalizeGain\": 1.0,                                         \"normalizeGain\": 0.0                                     }                                 ]                             }                         ],                         \"playInfo\": {                             \"bizType\": 0,                             \"cdnTimeRangeLevel\": 0                         },                         \"videoFeature\": {                             \"blurProbability\": 0.02436523512005806,                             \"blockyProbability\": 0.5486664772033691,                             \"avgEntropy\": 11.74826078414917,                             \"mosScore\": 0.6893717646598816                         }                     },                     \"photoH265Urls\": [                         {                             \"cdn\": \"k0u2ayecy7bycz.djvod.ndcimgs.com\",                             \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_hd15_Bfb2327ef432b8e22bee0565c052210d0.mp4?tag=1-1756664181-unknown-0-ra3mc5pqwz-b5d377ade7d0a512&provider=self&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=hd15&ss=vps\"                         },                         {                             \"cdn\": \"v1.kwaicdn.com\",                             \"url\": \"https://v1.kwaicdn.com/ksc2/WsLapasbDJwa_d5-gSoI2EwR1RYcYI6MpzWrlOzqoBPJ1eG7TRpv8UtWiNxv2xy-tsiAXr2VvmiqAJQmxNCMawMQCe7orKomsXk6v-GJKt55XiiE9GdcOTmXM0Uj_MN1np_i8ffWmDHyxrrCfhiIKRMXGETtR5BcJTIxz5hg3BgWZAEVV8VxRcZ2PwP4phUM.mp4?pkey=AAVktrin9oeeededNfrZf8LaIR1CvEQJ8FlSEH5iw-Azi03uiv1Eh297Xfd7f6yLLkZNDEyqFg4KqNphKlDhQmAw3TKsBqJYmLfLtR3cRWzJ5VY6FadrIRrGZvuCwgCob4A&tag=1-1756664181-unknown-1-tx8vx8qkhx-44a6a7306fccf2ff&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=hd15&ss=vps\"                         }                     ],                     \"viewCount\": 1594389,                     \"width\": 1280,                     \"id\": \"3xezqrk27gdc5a4\",                     \"animatedCoverUrl\": \"https://p1.a.yximgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_animatedV5_Beaaaeb032c640d38decbda1f52bc209e.webp?tag=1-1756664181-xpcwebprofile-0-tdiakvxcxz-98dff964a1098863&clientCacheKey=3xezqrk27gdc5a4_animatedV5.webp&di=3da39dcf&bp=14734\",                     \"overrideCoverUrl\": \"https://p1.a.yximgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_ccc_B39cbb17aaf65e0a76080064fd78dfc64.jpg?tag=1-1756664181-xpcwebprofile-0-gg941gqowe-afd116662be96449&clientCacheKey=3xezqrk27gdc5a4_ccc.jpg&di=3da39dcf&bp=14734\",                     \"collectCount\": 22057,                     \"riskTagContent\": null,                     \"expTag\": \"1_a/2008712974016392641_xpcwebprofilexxnull0\",                     \"riskTagUrl\": null,                     \"timestamp\": 1698748219278,                     \"stereoType\": 0,                     \"likeCount\": 75604,                     \"collected\": false,                     \"duration\": 84816,                     \"liked\": false,                     \"coverUrl\": \"https://p1.a.yximgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_ccc_B39cbb17aaf65e0a76080064fd78dfc64.jpg?tag=1-1756664181-xpcwebprofile-0-lznq3kgead-b3f7c6ea108bb5d1&clientCacheKey=3xezqrk27gdc5a4_ccc.jpg&di=3da39dcf&bp=14734\",                     \"caption\": \"健 身 鸭 脖\",                     \"height\": 720                 },                 \"author\": {                     \"id\": \"3xz63mn6fngqtiq\",                     \"headerUrl\": \"https://p66-pro.a.yximgs.com/uhead/AB/2025/08/11/21/BMjAyNTA4MTEyMTEyNDlfMjI4OTA1ODAyXzFfaGQ5ODdfODg4_s.jpg\",                     \"livingInfo\": {                         \"living\": false,                         \"livingId\": null,                         \"iconType\": 0                     },                     \"name\": \"权少爱吃小汉堡🍔\",                     \"following\": false                 },                 \"comment\": {                     \"us_c\": 0                 },                 \"danmakuSwitch\": true             }             },         ],         \"llsid\": \"2008712974016392641\",         \"host-name\": \"public-bjx-c26-kce-node642.idchb1az1.hb1.kwaidc.com\",         \"webPageArea\": \"profilexxnull\"     } } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
user_id = NULL # object | 
pcursor = NULL # object |  (optional)

try:
    # 获取用户发布作品/Fetch user posts
    api_instance.fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get(user_id, pcursor=pcursor)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 
 **pcursor** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get**
> generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get(photo_id)

生成分享短连接/Generate share short URL

# [中文] ### 用途: - 生成分享短连接 ### 参数: - photo_id: 作品ID ### 返回: - 短连接  # [English] ### Purpose: - Generate share short URL ### Parameters: - photo_id: Photo ID ### Returns: - Short URL  # [示例/Example] body = {     \"photo_id\": \"3xtdqvdnqd3psuc\" }  # [返回示例/Example Response] ```json {   \"code\": 200,   \"request_id\": \"3fe5f6dc-e88c-4915-a6fa-2a63a2743342\",   \"router\": \"/api/v1/kuaishou/web/generate_share_short_url\",   \"params\": {     \"photo_id\": \"3xtdqvdnqd3psuc\"   },   \"data\": {     \"result\": 1,     \"hostName\": \"public-bjzey-rs6-kce-node1155.idchb1az3.hb1.kwaidc.com\",     \"cache-scope\": \"nocache\",     \"error_msg\": null,     \"max-age\": 0,     \"share\": {       \"shareMethod\": \"TOKEN\",       \"shareMethodType\": null,       \"shareChannel\": \"COPY_LINK\",       \"shareMode\": \"APP\",       \"kpn\": \"KUAISHOU\",       \"subBiz\": \"BROWSE_SLIDE_PHOTO\",       \"appName\": \"as\",       \"appIconUrl\": \"https://static.yximgs.com/udata/pkg/ks-share-sdk/cardlogonew.png\",       \"shareObject\": {         \"copylinkSuccessTips\": \"链接复制成功，快去分享给朋友吧\",         \"shareMessage\": \"https://v.kuaishou.com/KDh1s1j1 上一秒他是市民，下一秒他是市长 大哥突如其来的专业，让人笑不活了。\"搞笑 \"非物质文化遗产 \"...更多\",         \"kwaiToken\": \"X8hIM7myjQen2bi\",         \"shareId\": \"18546252276277\",         \"shareObjectId\": \"3xtdqvdnqd3psuc\",         \"shareResourceType\": \"PHOTO_OTHER\",         \"shortLink\": \"https://v.kuaishou.com/KDh1s1j1\"       },       \"extParams\": {         \"shareMode\": \"app\",         \"tokenExtParams\": \"{}\",         \"expTag\": \"1_i/0_unknown0\",         \"shareMethod\": \"token\",         \"useMmuTitle\": false,         \"logExt\": \"{\"expTag\":\"1_i/0_unknown0\",\"trendingType\":\"\"}\",         \"templateStyle\": \"\",         \"shareInfoWrap\": \"{\"shareTitleInfo\":{\"title\":\"分享一个作品给你\",\"subTitle\":\"推荐你看这个视频\"},\"shareId\":\"18546252276277\",\"docId\":9,\"groupName\":\"\",\"shareType\":\"PHOTO_OTHER\",\"coverUrlKey\":null,\"coverUrl\":null,\"tagType\":null,\"webShareVerifyData\":null}\",         \"battleTemplateId\": \"\",         \"templateGenerationType\": \"\"       }     },     \"host-name\": \"public-bjzey-rs6-kce-node1155.idchb1az3.hb1.kwaidc.com\"   } } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuaishouWebAPIApi()
photo_id = NULL # object | 

try:
    # 生成分享短连接/Generate share short URL
    api_instance.generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get(photo_id)
except ApiException as e:
    print("Exception when calling KuaishouWebAPIApi->generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photo_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

