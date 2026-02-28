# swagger_client.WeChatChannelsAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_comments_api_v1_wechat_channels_fetch_comments_get**](WeChatChannelsAPIApi.md#fetch_comments_api_v1_wechat_channels_fetch_comments_get) | **GET** /api/v1/wechat_channels/fetch_comments | 微信视频号评论/WeChat Channels Comments
[**fetch_default_search_api_v1_wechat_channels_fetch_default_search_get**](WeChatChannelsAPIApi.md#fetch_default_search_api_v1_wechat_channels_fetch_default_search_get) | **GET** /api/v1/wechat_channels/fetch_default_search | 微信视频号默认搜索/WeChat Channels Default Search
[**fetch_home_page_api_v1_wechat_channels_fetch_home_page_get**](WeChatChannelsAPIApi.md#fetch_home_page_api_v1_wechat_channels_fetch_home_page_get) | **GET** /api/v1/wechat_channels/fetch_home_page | 微信视频号主页/WeChat Channels Home Page
[**fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get**](WeChatChannelsAPIApi.md#fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get) | **GET** /api/v1/wechat_channels/fetch_hot_words | 微信视频号热门话题/WeChat Channels Hot Topics
[**fetch_live_history_api_v1_wechat_channels_fetch_live_history_get**](WeChatChannelsAPIApi.md#fetch_live_history_api_v1_wechat_channels_fetch_live_history_get) | **GET** /api/v1/wechat_channels/fetch_live_history | 微信视频号直播回放/WeChat Channels Live History
[**fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get**](WeChatChannelsAPIApi.md#fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get) | **GET** /api/v1/wechat_channels/fetch_search_latest | 微信视频号搜索最新视频/WeChat Channels Search Latest Videos
[**fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get**](WeChatChannelsAPIApi.md#fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get) | **GET** /api/v1/wechat_channels/fetch_search_ordinary | 微信视频号综合搜索/WeChat Channels Comprehensive Search
[**fetch_user_search_api_v1_wechat_channels_fetch_user_search_get**](WeChatChannelsAPIApi.md#fetch_user_search_api_v1_wechat_channels_fetch_user_search_get) | **GET** /api/v1/wechat_channels/fetch_user_search | 微信视频号用户搜索/WeChat Channels User Search
[**fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get**](WeChatChannelsAPIApi.md#fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get) | **GET** /api/v1/wechat_channels/fetch_video_detail | 微信视频号视频详情/WeChat Channels Video Detail


# **fetch_comments_api_v1_wechat_channels_fetch_comments_get**
> fetch_comments_api_v1_wechat_channels_fetch_comments_get(id, last_buffer=last_buffer, comment_id=comment_id)

微信视频号评论/WeChat Channels Comments

# [中文] ### 用途: - 获取微信视频号视频评论 - 支持分页获取更多评论 - 价格：0.01$/次 ### 参数: - id: 视频ID - lastBuffer: 分页参数，首次请求可为空 - comment_id: 评论ID，默认不传，传入则获取该评论下的子评论 ### 返回: - 视频评论列表  # [English] ### Purpose: - Get WeChat Channels video comments - Support pagination for more comments - Price: $0.01 per request ### Parameters: - id: Video ID - lastBuffer: Pagination parameter, can be empty for first request - comment_id: Comment ID, if provided, fetches replies to that comment ### Return: - Video comment list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatChannelsAPIApi()
id = NULL # object | 视频ID/Video ID
last_buffer = NULL # object | 分页参数/Pagination parameter (optional)
comment_id = NULL # object | 评论ID，默认不传，传入则获取该评论下的子评论/Comment ID, if provided, fetches replies to that comment (optional)

try:
    # 微信视频号评论/WeChat Channels Comments
    api_instance.fetch_comments_api_v1_wechat_channels_fetch_comments_get(id, last_buffer=last_buffer, comment_id=comment_id)
except ApiException as e:
    print("Exception when calling WeChatChannelsAPIApi->fetch_comments_api_v1_wechat_channels_fetch_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| 视频ID/Video ID | 
 **last_buffer** | [**object**](.md)| 分页参数/Pagination parameter | [optional] 
 **comment_id** | [**object**](.md)| 评论ID，默认不传，传入则获取该评论下的子评论/Comment ID, if provided, fetches replies to that comment | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_default_search_api_v1_wechat_channels_fetch_default_search_get**
> fetch_default_search_api_v1_wechat_channels_fetch_default_search_get(keywords, session_buffer=session_buffer)

微信视频号默认搜索/WeChat Channels Default Search

# [中文] ### 用途: - 获取微信视频号默认搜索结果 - 支持分页获取更多结果 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 - session_buffer:     - 分页参数，首次请求可为空，后续使用响应中的 `last_buff` 进行分页请求     - JSON Path： `$.data.last_buff` ### 返回: - 搜索结果列表，包含视频信息  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取翻页参数 `last_buff`: `$.data.last_buff`     - 获取视频列表: `$.data.media_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.media_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.media_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.media_list[*].object_desc.media[0].url + $.data.media_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.media_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels default search results - Support pagination for more results - Price: $0.01 per request ### Parameters: - keywords: Search keywords - session_buffer: Pagination parameter, can be empty for first request     - For subsequent requests, use `last_buff` from the response for pagination     - JSON Path: `$.data.last_buff`  ### Return: - Search result list with video information ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the pagination parameter `last_buff`: `$.data.last_buff`     - To get the video list: `$.data.media_list[*]`     - To get the video CDN link (without Token): `$.data.media_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.media_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.media_list[*].object_desc.media[0].url + $.data.media_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.media_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatChannelsAPIApi()
keywords = NULL # object | 搜索关键词/Search keywords
session_buffer = NULL # object | 分页参数/Pagination parameter (optional)

try:
    # 微信视频号默认搜索/WeChat Channels Default Search
    api_instance.fetch_default_search_api_v1_wechat_channels_fetch_default_search_get(keywords, session_buffer=session_buffer)
except ApiException as e:
    print("Exception when calling WeChatChannelsAPIApi->fetch_default_search_api_v1_wechat_channels_fetch_default_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | [**object**](.md)| 搜索关键词/Search keywords | 
 **session_buffer** | [**object**](.md)| 分页参数/Pagination parameter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_home_page_api_v1_wechat_channels_fetch_home_page_get**
> fetch_home_page_api_v1_wechat_channels_fetch_home_page_get(username, last_buffer=last_buffer)

微信视频号主页/WeChat Channels Home Page

# [中文] ### 用途: - 获取微信视频号用户主页信息 - 包含用户发布的视频列表 - 支持分页获取更多视频 - 价格：0.01$/次 ### 参数: - username: 用户名 - last_buffer:     - 分页参数，首次请求可为空，后续使用 `object_list` 最后一个 item 的 `last_buffer` 进行分页请求     - JSON Path: `$.data.object_list[-1].last_buffer` ### 返回: - 用户主页信息和视频列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取翻页参数 `last_buffer`: `$.data.object_list[-1].last_buffer`     - 获取视频列表: `$.data.object_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.object_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels user homepage information - Including list of videos published by user - Support pagination for more videos - Price: $0.01 per request ### Parameters: - username: Username - last_buffer:     - Pagination parameter, can be empty for first request     - For subsequent requests, use the `last_buffer` of the last item in `object_list`     - JSON Path: `$.data.object_list[-1].last_buffer` ### Return: - User homepage information and video list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the pagination parameter `last_buffer`: `$.data.object_list[-1].last_buffer`     - To get the video list: `$.data.object_list[*]`     - To get the video CDN link (without Token): `$.data.object_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatChannelsAPIApi()
username = NULL # object | 用户名/Username
last_buffer = NULL # object | 分页参数/Pagination parameter (optional)

try:
    # 微信视频号主页/WeChat Channels Home Page
    api_instance.fetch_home_page_api_v1_wechat_channels_fetch_home_page_get(username, last_buffer=last_buffer)
except ApiException as e:
    print("Exception when calling WeChatChannelsAPIApi->fetch_home_page_api_v1_wechat_channels_fetch_home_page_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)| 用户名/Username | 
 **last_buffer** | [**object**](.md)| 分页参数/Pagination parameter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get**
> fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get()

微信视频号热门话题/WeChat Channels Hot Topics

# [中文] ### 用途: - 获取微信视频号当前热门话题 - 可用于发现热门内容和趋势 - 价格：0.01$/次 ### 参数: - 无需额外参数 ### 返回: - 热门话题列表  # [English] ### Purpose: - Get current hot topics in WeChat Channels - Can be used to discover popular content and trends - Price: $0.01 per request ### Parameters: - No additional parameters required ### Return: - Hot topic list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatChannelsAPIApi()

try:
    # 微信视频号热门话题/WeChat Channels Hot Topics
    api_instance.fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get()
except ApiException as e:
    print("Exception when calling WeChatChannelsAPIApi->fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get: %s\n" % e)
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

# **fetch_live_history_api_v1_wechat_channels_fetch_live_history_get**
> fetch_live_history_api_v1_wechat_channels_fetch_live_history_get(username)

微信视频号直播回放/WeChat Channels Live History

# [中文] ### 用途: - 获取微信视频号用户的直播回放列表 - 价格：0.01$/次 ### 参数: - username: 用户名 ### 返回: - 直播回放列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取直播回放列表: `$.data.live_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.live_list[*].media.url`     - 获取视频 CDN 链接的 Token: `$.data.live_list[*].media.url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.live_list[*].media.url + $.data.live_list[*].media.url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.live_list[*].media.decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels user's live replay list - Price: $0.01 per request ### Parameters: - username: Username ### Return: - Live replay list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the live replay list: `$.data.live_list[*]`     - To get the video CDN link (without Token): `$.data.live_list[*].media.url`     - To get the Token for the video CDN link: `$.data.live_list[*].media.url_token`     - How to concatenate the complete URL of the video CDN: `$.data.live_list[*].media.url + $.data.live_list[*].media.url_token`     - To get the video decryption key (different for each request): `$.data.live_list[*].media.decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatChannelsAPIApi()
username = NULL # object | 用户名/Username

try:
    # 微信视频号直播回放/WeChat Channels Live History
    api_instance.fetch_live_history_api_v1_wechat_channels_fetch_live_history_get(username)
except ApiException as e:
    print("Exception when calling WeChatChannelsAPIApi->fetch_live_history_api_v1_wechat_channels_fetch_live_history_get: %s\n" % e)
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

# **fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get**
> fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get(keywords)

微信视频号搜索最新视频/WeChat Channels Search Latest Videos

# [中文] ### 用途: - 获取微信视频号最新视频搜索结果 - 按时间倒序排列 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 ### 返回: - 最新视频搜索结果列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取视频列表: `$.data.object_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.object_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels latest video search results - Sorted by time in descending order - Price: $0.01 per request ### Parameters: - keywords: Search keywords ### Return: - Latest video search result list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the video list: `$.data.object_list[*]`     - To get the video CDN link (without Token): `$.data.object_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatChannelsAPIApi()
keywords = NULL # object | 搜索关键词/Search keywords

try:
    # 微信视频号搜索最新视频/WeChat Channels Search Latest Videos
    api_instance.fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get(keywords)
except ApiException as e:
    print("Exception when calling WeChatChannelsAPIApi->fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | [**object**](.md)| 搜索关键词/Search keywords | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get**
> fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get(keywords)

微信视频号综合搜索/WeChat Channels Comprehensive Search

# [中文] ### 用途: - 获取微信视频号综合搜索结果 - 按相关性排序 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 ### 返回: - 综合搜索结果列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取视频列表: `$.data.object_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.object_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels comprehensive search results - Sorted by relevance - Price: $0.01 per request ### Parameters: - keywords: Search keywords ### Return: - Comprehensive search result list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the video list: `$.data.object_list[*]`     - To get the video CDN link (without Token): `$.data.object_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatChannelsAPIApi()
keywords = NULL # object | 搜索关键词/Search keywords

try:
    # 微信视频号综合搜索/WeChat Channels Comprehensive Search
    api_instance.fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get(keywords)
except ApiException as e:
    print("Exception when calling WeChatChannelsAPIApi->fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | [**object**](.md)| 搜索关键词/Search keywords | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_search_api_v1_wechat_channels_fetch_user_search_get**
> fetch_user_search_api_v1_wechat_channels_fetch_user_search_get(keywords, page=page)

微信视频号用户搜索/WeChat Channels User Search

# [中文] ### 用途: - 搜索微信视频号用户 - 按关键词查找相关用户 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 - page: 页码，从1开始 ### 返回: - 用户搜索结果列表  # [English] ### Purpose: - Search WeChat Channels users - Find related users by keywords - Price: $0.01 per request ### Parameters: - keywords: Search keywords - page: Page number, starting from 1 ### Return: - User search result list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatChannelsAPIApi()
keywords = NULL # object | 搜索关键词/Search keywords
page = NULL # object | 页码/Page number (optional)

try:
    # 微信视频号用户搜索/WeChat Channels User Search
    api_instance.fetch_user_search_api_v1_wechat_channels_fetch_user_search_get(keywords, page=page)
except ApiException as e:
    print("Exception when calling WeChatChannelsAPIApi->fetch_user_search_api_v1_wechat_channels_fetch_user_search_get: %s\n" % e)
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

# **fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get**
> fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get(id=id, export_id=export_id)

微信视频号视频详情/WeChat Channels Video Detail

# [中文] ### 用途: - 获取微信视频号视频详细信息 - 可通过视频ID或导出ID获取 - 价格：0.01$/次 ### 参数: - id: 视频ID（二选一） - exportId: 导出ID（会过期，二选一，使用时可不传id） ### 返回: - 视频详细信息  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取视频 CDN 链接（不带Token）: `$.data.object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_desc.media[0].url + $.data.object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels video detailed information - Can be obtained through video ID or export ID - Price: $0.01 per request ### Parameters: - id: Video ID (choose one) - exportId: Export ID (may expire, choose one, can be used without id) ### Return: - Video detailed information ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the video CDN link (without Token): `$.data.object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_desc.media[0].url + $.data.object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatChannelsAPIApi()
id = NULL # object | 视频ID/Video ID (optional)
export_id = NULL # object | 导出ID会过期，优先用视频ID，使用时可不传id/Export ID may expire, prefer to use Video ID, can be used without id (optional)

try:
    # 微信视频号视频详情/WeChat Channels Video Detail
    api_instance.fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get(id=id, export_id=export_id)
except ApiException as e:
    print("Exception when calling WeChatChannelsAPIApi->fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| 视频ID/Video ID | [optional] 
 **export_id** | [**object**](.md)| 导出ID会过期，优先用视频ID，使用时可不传id/Export ID may expire, prefer to use Video ID, can be used without id | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

