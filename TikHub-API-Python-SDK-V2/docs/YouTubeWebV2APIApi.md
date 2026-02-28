# swagger_client.YouTubeWebV2APIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_channel_description_api_v1_youtube_web_v2_get_channel_description_get**](YouTubeWebV2APIApi.md#get_channel_description_api_v1_youtube_web_v2_get_channel_description_get) | **GET** /api/v1/youtube/web_v2/get_channel_description | 获取频道描述信息/Get channel description
[**get_channel_id_api_v1_youtube_web_v2_get_channel_id_get**](YouTubeWebV2APIApi.md#get_channel_id_api_v1_youtube_web_v2_get_channel_id_get) | **GET** /api/v1/youtube/web_v2/get_channel_id | 从频道URL获取频道ID /Get channel ID from URL
[**get_channel_shorts_api_v1_youtube_web_v2_get_channel_shorts_get**](YouTubeWebV2APIApi.md#get_channel_shorts_api_v1_youtube_web_v2_get_channel_shorts_get) | **GET** /api/v1/youtube/web_v2/get_channel_shorts | 获取频道短视频列表/Get channel shorts
[**get_channel_url_api_v1_youtube_web_v2_get_channel_url_get**](YouTubeWebV2APIApi.md#get_channel_url_api_v1_youtube_web_v2_get_channel_url_get) | **GET** /api/v1/youtube/web_v2/get_channel_url | 从频道ID获取频道URL/Get channel URL from channel ID
[**get_channel_videos_api_v1_youtube_web_v2_get_channel_videos_get**](YouTubeWebV2APIApi.md#get_channel_videos_api_v1_youtube_web_v2_get_channel_videos_get) | **GET** /api/v1/youtube/web_v2/get_channel_videos | 获取频道视频 /Get channel videos
[**get_general_search_api_v1_youtube_web_v2_get_general_search_get**](YouTubeWebV2APIApi.md#get_general_search_api_v1_youtube_web_v2_get_general_search_get) | **GET** /api/v1/youtube/web_v2/get_general_search | 综合搜索（支持过滤条件）/General search with filters
[**get_related_videos_api_v1_youtube_web_v2_get_related_videos_get**](YouTubeWebV2APIApi.md#get_related_videos_api_v1_youtube_web_v2_get_related_videos_get) | **GET** /api/v1/youtube/web_v2/get_related_videos | 获取视频相似内容/Get related videos
[**get_search_suggestions_api_v1_youtube_web_v2_get_search_suggestions_get**](YouTubeWebV2APIApi.md#get_search_suggestions_api_v1_youtube_web_v2_get_search_suggestions_get) | **GET** /api/v1/youtube/web_v2/get_search_suggestions | 获取搜索推荐词/Get search suggestions
[**get_shorts_search_api_v1_youtube_web_v2_get_shorts_search_get**](YouTubeWebV2APIApi.md#get_shorts_search_api_v1_youtube_web_v2_get_shorts_search_get) | **GET** /api/v1/youtube/web_v2/get_shorts_search | YouTube Shorts短视频搜索/YouTube Shorts search
[**get_signed_stream_url_api_v1_youtube_web_v2_get_signed_stream_url_get**](YouTubeWebV2APIApi.md#get_signed_stream_url_api_v1_youtube_web_v2_get_signed_stream_url_get) | **GET** /api/v1/youtube/web_v2/get_signed_stream_url | 获取已签名的视频流URL/Get signed video stream URL
[**get_video_comment_replies_api_v1_youtube_web_v2_get_video_comment_replies_get**](YouTubeWebV2APIApi.md#get_video_comment_replies_api_v1_youtube_web_v2_get_video_comment_replies_get) | **GET** /api/v1/youtube/web_v2/get_video_comment_replies | 获取视频二级评论/Get video sub comments
[**get_video_comments_api_v1_youtube_web_v2_get_video_comments_get**](YouTubeWebV2APIApi.md#get_video_comments_api_v1_youtube_web_v2_get_video_comments_get) | **GET** /api/v1/youtube/web_v2/get_video_comments | 获取视频评论/Get video comments
[**get_video_info_api_v1_youtube_web_v2_get_video_info_get**](YouTubeWebV2APIApi.md#get_video_info_api_v1_youtube_web_v2_get_video_info_get) | **GET** /api/v1/youtube/web_v2/get_video_info | 获取视频详情 /Get video information
[**get_video_streams_api_v1_youtube_web_v2_get_video_streams_get**](YouTubeWebV2APIApi.md#get_video_streams_api_v1_youtube_web_v2_get_video_streams_get) | **GET** /api/v1/youtube/web_v2/get_video_streams | 获取视频流信息/Get video streams info
[**get_video_streams_v2_api_v1_youtube_web_v2_get_video_streams_v2_get**](YouTubeWebV2APIApi.md#get_video_streams_v2_api_v1_youtube_web_v2_get_video_streams_v2_get) | **GET** /api/v1/youtube/web_v2/get_video_streams_v2 | 获取视频流信息 V2/Get video streams info V2
[**search_channels_api_v1_youtube_web_v2_search_channels_get**](YouTubeWebV2APIApi.md#search_channels_api_v1_youtube_web_v2_search_channels_get) | **GET** /api/v1/youtube/web_v2/search_channels | 搜索频道/Search channels


# **get_channel_description_api_v1_youtube_web_v2_get_channel_description_get**
> get_channel_description_api_v1_youtube_web_v2_get_channel_description_get(channel_id=channel_id, continuation_token=continuation_token, language_code=language_code, country_code=country_code, need_format=need_format)

获取频道描述信息/Get channel description

# [中文] ### 用途: - 获取YouTube频道的介绍信息（订阅数、视频数、观看次数、注册时间、社交链接等）  ### 重要提示 - 需要两次请求获取完整数据: - **第一次请求**（使用channel_id）: 返回基本信息（频道名称、描述、订阅数、视频数、头像、横幅等） - **第二次请求**（使用continuation_token）: 返回高级信息（**注册时间、社交媒体链接、国家、观看次数**等）  ### 如何获取channel_id: - 如果你只有频道URL（如 `https://www.youtube.com/@CozyCraftYT`），请先调用 **get_channel_id** 接口获取channel_id - 该接口会返回类似 `UCeu6U67OzJhV1KwBansH3Dg` 的频道ID  ### 参数详解:  #### 📌 必选参数（二选一）: **channel_id** (string) - **作用**: 频道ID，用于第一次请求获取频道基本信息 - **格式**: 通常以 `UC` 开头的24位字符串 - **示例**: `\"UCeu6U67OzJhV1KwBansH3Dg\"` - **获取方式**: 调用 **get_channel_id** 接口，传入频道URL即可获取  **continuation_token** (string) - **作用**: 翻页标志，用于第二次请求获取频道的高级信息 - **获取方式**: 从第一次请求的响应中获取 `continuation_token` 字段 - **注意**: `channel_id` 和 `continuation_token` 必须提供其中一个  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置显示语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 使用流程（三步获取完整数据）: 1. **获取channel_id**: 如果只有频道URL，先调用 `get_channel_id?channel_url=https://www.youtube.com/@CozyCraftYT` 2. **第一次请求**: 使用 `channel_id` 参数获取频道基本信息，同时获取 `continuation_token` 3. **第二次请求**: 使用 `continuation_token` 获取高级信息（注册时间、社交链接等）  ### 返回数据结构 (need_format=true):  #### 第一次请求返回（使用channel_id）: ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": \"CozyCraft\",   \"handle\": \"CozyCraftYT\",   \"description\": \"频道介绍...\",   \"subscriber_count\": \"9.84万位订阅者\",   \"video_count\": \"181 个视频\",   \"view_count\": null,   \"country\": null,   \"creation_date\": null,   \"links\": [],   \"avatar\": [{\"url\": \"...\", \"width\": 900, \"height\": 900}],   \"banner\": [{\"url\": \"...\", \"width\": 2560, \"height\": 424}],   \"keywords\": \"Minecraft Ambience...\",   \"channel_url\": \"https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg\",   \"vanity_url\": \"http://www.youtube.com/@CozyCraftYT\",   \"rss_url\": \"https://www.youtube.com/feeds/videos.xml?channel_id=UCeu6U67OzJhV1KwBansH3Dg\",   \"is_family_safe\": true,   \"verified\": false,   \"has_business_email\": false,   \"has_membership\": true,   \"continuation_token\": \"4qmFsgJg...\" } ```  #### 第二次请求返回（使用continuation_token）: ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": null,   \"handle\": \"CozyCraftYT\",   \"description\": \"完整频道介绍...\",   \"subscriber_count\": \"98.4K subscribers\",   \"video_count\": \"181 videos\",   \"view_count\": \"53,218,926 views\",   \"country\": \"United States\",   \"creation_date\": \"Oct 28, 2022\",   \"links\": [     {\"name\": \"Discord\", \"url\": \"https://discord.gg/tvuxxcsgSS\"},     {\"name\": \"Twitter\", \"url\": \"https://twitter.com/...\"}   ],   \"avatar\": [],   \"banner\": [],   \"verified\": false,   \"has_business_email\": true,   \"continuation_token\": null } ```  ### 注意事项: - **必须进行两次请求才能获取完整的频道信息** - 第一次请求: 获取基本信息（title、avatar、banner、keywords、rss_url等）和 continuation_token - 第二次请求: 获取高级信息（creation_date、links、view_count、country等） - 建议两次请求都设置 `need_format=true` 获取清洗后的数据 - 可以合并两次请求的结果来获得完整的频道信息  # [English] ### Purpose: - Get YouTube channel description information (subscribers, videos, views, creation date, social links, etc.)  ### Important - Two requests required for complete data: - **First request** (with channel_id): Returns basic info (title, description, subscribers, videos, avatar, banner, etc.) - **Second request** (with continuation_token): Returns advanced info (**creation date, social media links, country, view count**, etc.)  ### How to get channel_id: - If you only have channel URL (e.g., `https://www.youtube.com/@CozyCraftYT`), call **get_channel_id** endpoint first - It will return channel_id like `UCeu6U67OzJhV1KwBansH3Dg`  ### Parameters:  #### 📌 Required (choose one): **channel_id** (string) - **Purpose**: Channel ID for first request to get basic channel info - **Format**: Usually starts with `UC`, 24 characters - **Example**: `\"UCeu6U67OzJhV1KwBansH3Dg\"` - **How to get**: Call **get_channel_id** endpoint with channel URL  **continuation_token** (string) - **Purpose**: Pagination token for second request to get advanced info - **How to get**: Get `continuation_token` field from first request response - **Note**: Must provide either `channel_id` or `continuation_token`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  **country_code** (string, optional) - **Purpose**: Set region code - **Default**: `\"US\"` - **Values**: `\"US\"`, `\"JP\"`, `\"GB\"`, etc.  **need_format** (boolean, optional) - **Purpose**: Whether to return cleaned simplified data - **Default**: `false` - **Values**:   - `false` - Return raw complete data   - `true` - Return cleaned simplified data (recommended)  ### Usage Flow (3 steps for complete data): 1. **Get channel_id**: If you only have URL, call `get_channel_id?channel_url=https://www.youtube.com/@CozyCraftYT` 2. **First request**: Use `channel_id` parameter to get basic info and `continuation_token` 3. **Second request**: Use `continuation_token` to get advanced info (creation date, social links, etc.)  ### Response Structure (need_format=true):  #### First request response (with channel_id): ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": \"CozyCraft\",   \"handle\": \"CozyCraftYT\",   \"description\": \"Channel description...\",   \"subscriber_count\": \"98.4K subscribers\",   \"video_count\": \"181 videos\",   \"view_count\": null,   \"country\": null,   \"creation_date\": null,   \"links\": [],   \"avatar\": [{\"url\": \"...\", \"width\": 900, \"height\": 900}],   \"banner\": [{\"url\": \"...\", \"width\": 2560, \"height\": 424}],   \"keywords\": \"Minecraft Ambience...\",   \"channel_url\": \"https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg\",   \"vanity_url\": \"http://www.youtube.com/@CozyCraftYT\",   \"rss_url\": \"https://www.youtube.com/feeds/videos.xml?channel_id=UCeu6U67OzJhV1KwBansH3Dg\",   \"is_family_safe\": true,   \"verified\": false,   \"has_business_email\": false,   \"has_membership\": true,   \"continuation_token\": \"4qmFsgJg...\" } ```  #### Second request response (with continuation_token): ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": null,   \"handle\": \"CozyCraftYT\",   \"description\": \"Full channel description...\",   \"subscriber_count\": \"98.4K subscribers\",   \"video_count\": \"181 videos\",   \"view_count\": \"53,218,926 views\",   \"country\": \"United States\",   \"creation_date\": \"Oct 28, 2022\",   \"links\": [     {\"name\": \"Discord\", \"url\": \"https://discord.gg/tvuxxcsgSS\"},     {\"name\": \"Twitter\", \"url\": \"https://twitter.com/...\"}   ],   \"avatar\": [],   \"banner\": [],   \"verified\": false,   \"has_business_email\": true,   \"continuation_token\": null } ```  ### Notes: - **Two requests are required to get complete channel information** - First request: Get basic info (title, avatar, banner, keywords, rss_url, etc.) and continuation_token - Second request: Get advanced info (creation_date, links, view_count, country, etc.) - Recommend setting `need_format=true` for both requests - You can merge results from both requests for complete channel info  # [示例/Examples] ## 步骤1 - 获取channel_id（如果只有URL） GET /youtube_web/get_channel_id?channel_url=https://www.youtube.com/@CozyCraftYT  ## 步骤2 - 第一次请求获取基本信息和continuation_token GET /youtube_web/get_channel_description?channel_id=UCeu6U67OzJhV1KwBansH3Dg&need_format=true  ## 步骤3 - 第二次请求获取高级信息（使用返回的continuation_token） GET /youtube_web/get_channel_description?continuation_token=xxx&need_format=true

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
channel_id = NULL # object | 频道ID（格式如：UCeu6U67OzJhV1KwBansH3Dg），可通过get_channel_id接口从频道URL获取/Channel ID, can be obtained from channel URL via get_channel_id endpoint (optional)
continuation_token = NULL # object | 翻页标志（用于获取频道注册时间等高级信息）/Continuation token for getting advanced info like channel creation date (optional)
language_code = NULL # object | 语言代码（如zh-CN, en-US等）/Language code (optional)
country_code = NULL # object | 国家代码（如US, JP等）/Country code (optional)
need_format = NULL # object | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data (optional)

try:
    # 获取频道描述信息/Get channel description
    api_instance.get_channel_description_api_v1_youtube_web_v2_get_channel_description_get(channel_id=channel_id, continuation_token=continuation_token, language_code=language_code, country_code=country_code, need_format=need_format)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_channel_description_api_v1_youtube_web_v2_get_channel_description_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)| 频道ID（格式如：UCeu6U67OzJhV1KwBansH3Dg），可通过get_channel_id接口从频道URL获取/Channel ID, can be obtained from channel URL via get_channel_id endpoint | [optional] 
 **continuation_token** | [**object**](.md)| 翻页标志（用于获取频道注册时间等高级信息）/Continuation token for getting advanced info like channel creation date | [optional] 
 **language_code** | [**object**](.md)| 语言代码（如zh-CN, en-US等）/Language code | [optional] 
 **country_code** | [**object**](.md)| 国家代码（如US, JP等）/Country code | [optional] 
 **need_format** | [**object**](.md)| 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_id_api_v1_youtube_web_v2_get_channel_id_get**
> get_channel_id_api_v1_youtube_web_v2_get_channel_id_get(channel_url)

从频道URL获取频道ID /Get channel ID from URL

# [中文] ### 用途: - 从YouTube频道URL转换获取频道ID（channel_id）。 - 支持多种URL格式，包括@用户名格式、/channel/格式、/c/格式、/user/格式。 ### 参数: - channel_url: 频道URL。 ### 返回: - channel_id: 频道ID（如：UCeu6U67OzJhV1KwBansH3Dg） - channel_url: 标准化的频道URL - source: 数据来源（url_parse表示直接从URL解析，page_parse表示从页面解析）  # [English] ### Purpose: - Convert YouTube channel URL to channel ID. - Supports multiple URL formats including @username, /channel/, /c/, /user/ formats. ### Parameters: - channel_url: Channel URL. ### Returns: - channel_id: Channel ID (e.g., UCeu6U67OzJhV1KwBansH3Dg) - channel_url: Normalized channel URL - source: Data source (url_parse means parsed from URL directly, page_parse means parsed from page)  # [示例/Example] channel_url = \"https://www.youtube.com/@CozyCraftYT\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
channel_url = NULL # object | 频道URL/Channel URL，支持多种格式如：https://www.youtube.com/@username, https://www.youtube.com/channel/UCxxxxxx, https://www.youtube.com/c/channelname

try:
    # 从频道URL获取频道ID /Get channel ID from URL
    api_instance.get_channel_id_api_v1_youtube_web_v2_get_channel_id_get(channel_url)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_channel_id_api_v1_youtube_web_v2_get_channel_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_url** | [**object**](.md)| 频道URL/Channel URL，支持多种格式如：https://www.youtube.com/@username, https://www.youtube.com/channel/UCxxxxxx, https://www.youtube.com/c/channelname | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_shorts_api_v1_youtube_web_v2_get_channel_shorts_get**
> get_channel_shorts_api_v1_youtube_web_v2_get_channel_shorts_get(channel_id=channel_id, channel_url=channel_url, continuation_token=continuation_token, need_format=need_format)

获取频道短视频列表/Get channel shorts

# [中文] ### 用途: - 获取YouTube频道的短视频(Shorts)列表 - 支持分页获取更多短视频  ### 参数: - channel_id: 频道ID（推荐，如 UCuAXFkgsw1L7xaCfnd5JJOw） - channel_url: 频道URL（可选，如果提供channel_id则忽略） - continuation_token: 分页token（可选，用于获取下一页） - need_format: 是否格式化数据（默认 true）   - true: 返回格式化的结构化数据（推荐）   - false: 返回原始的 YouTube API 结构（用于调试）  ### 返回数据包含: #### 当 need_format=true 时: - channel_id: 频道ID - shorts: 短视频列表   - video_id: 短视频的ID   - title: 标题   - view_count_text: 观看次数文本（如 \"1.2M views\"）   - thumbnails: 缩略图列表   - accessibility_text: 无障碍文本描述   - video_url: 短视频链接 - continuation_token: 下一页的分页token - has_more: 是否还有更多短视频 - total_count: 当前页短视频数量  #### 当 need_format=false 时: - channel_id: 频道ID - shorts: 原始的 reelItemRenderer 对象列表 - continuation_token: 下一页的分页token - has_more: 是否还有更多短视频 - total_count: 当前页短视频数量  ### 使用流程: 1. 首次请求：只传 channel_id 参数 2. 获取响应中的 continuation_token 3. 下次请求：传入 channel_id 和 continuation_token 4. 重复步骤 2-3 直到 has_more 为 false  ### 注意事项: - 每页通常返回 30 个左右的短视频 - ⚠️ 目前暂不支持 @username 格式，请使用频道ID（UCxxxx 格式）  ### 价格: - $0.001 USD / 请求  # [English] ### Purpose: - Get YouTube channel's Shorts (short videos) list - Supports pagination to get more shorts  ### Parameters: - channel_id: Channel ID (recommended, e.g., UCuAXFkgsw1L7xaCfnd5JJOw) - channel_url: Channel URL (optional, ignored if channel_id is provided) - continuation_token: Pagination token (optional, for next page) - need_format: Whether to format data (default true)   - true: Return formatted structured data (recommended)   - false: Return raw YouTube API structure (for debugging)  ### Returns: #### When need_format=true: - channel_id: Channel ID - shorts: Shorts list   - video_id: Short video ID   - title: Title   - view_count_text: View count text (e.g., \"1.2M views\")   - thumbnails: Thumbnail list   - accessibility_text: Accessibility description text   - video_url: Short video URL - continuation_token: Next page pagination token - has_more: Whether there are more shorts - total_count: Current page shorts count  #### When need_format=false: - channel_id: Channel ID - shorts: Raw reelItemRenderer object list - continuation_token: Next page pagination token - has_more: Whether there are more shorts - total_count: Current page shorts count  ### Usage Flow: 1. First request: Only pass channel_id parameter 2. Get continuation_token from response 3. Next request: Pass channel_id and continuation_token 4. Repeat steps 2-3 until has_more is false  ### Notes: - Each page typically returns around 30 shorts - ⚠️ Currently does not support @username format, please use channel ID (UCxxxx format)  ### Price: - $0.001 USD / request  ### [示例/Example] #### 获取短视频列表: channel_id = \"UCuAXFkgsw1L7xaCfnd5JJOw\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
channel_id = NULL # object | 频道ID/Channel ID (e.g., UCuAXFkgsw1L7xaCfnd5JJOw) (optional)
channel_url = NULL # object | 频道URL/Channel URL (如果提供channel_id则忽略/Ignored if channel_id is provided) (optional)
continuation_token = NULL # object | 分页token/Pagination token (optional)
need_format = NULL # object | 是否格式化数据/Whether to format data (optional)

try:
    # 获取频道短视频列表/Get channel shorts
    api_instance.get_channel_shorts_api_v1_youtube_web_v2_get_channel_shorts_get(channel_id=channel_id, channel_url=channel_url, continuation_token=continuation_token, need_format=need_format)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_channel_shorts_api_v1_youtube_web_v2_get_channel_shorts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)| 频道ID/Channel ID (e.g., UCuAXFkgsw1L7xaCfnd5JJOw) | [optional] 
 **channel_url** | [**object**](.md)| 频道URL/Channel URL (如果提供channel_id则忽略/Ignored if channel_id is provided) | [optional] 
 **continuation_token** | [**object**](.md)| 分页token/Pagination token | [optional] 
 **need_format** | [**object**](.md)| 是否格式化数据/Whether to format data | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_url_api_v1_youtube_web_v2_get_channel_url_get**
> get_channel_url_api_v1_youtube_web_v2_get_channel_url_get(channel_id)

从频道ID获取频道URL/Get channel URL from channel ID

# [中文] ### 用途: - 从YouTube频道ID转换获取频道Handle (@用户名) - 与 get_channel_id 接口互为反向操作  ### 参数: - channel_id: 频道ID（如：UCeu6U67OzJhV1KwBansH3Dg）  ### 返回: - channel_id: 频道ID - handle: 频道Handle（如：CozyCraftYT） - title: 频道名称 - channel_url: 标准频道URL（/channel/格式） - vanity_url: 个性化URL（/@用户名格式）  ### 使用场景: - 当你有频道ID但需要获取@用户名格式的URL时 - 需要展示用户友好的频道链接时  # [English] ### Purpose: - Convert YouTube channel ID to channel handle (@username) - Reverse operation of get_channel_id endpoint  ### Parameters: - channel_id: Channel ID (e.g., UCeu6U67OzJhV1KwBansH3Dg)  ### Returns: - channel_id: Channel ID - handle: Channel handle (e.g., CozyCraftYT) - title: Channel name - channel_url: Standard channel URL (/channel/ format) - vanity_url: Vanity URL (/@username format)  ### Use Cases: - When you have channel ID but need @username format URL - When you need to display user-friendly channel links  # [示例/Example] channel_id = \"UCeu6U67OzJhV1KwBansH3Dg\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
channel_id = NULL # object | 频道ID/Channel ID (格式如：UCeu6U67OzJhV1KwBansH3Dg)

try:
    # 从频道ID获取频道URL/Get channel URL from channel ID
    api_instance.get_channel_url_api_v1_youtube_web_v2_get_channel_url_get(channel_id)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_channel_url_api_v1_youtube_web_v2_get_channel_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)| 频道ID/Channel ID (格式如：UCeu6U67OzJhV1KwBansH3Dg) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_videos_api_v1_youtube_web_v2_get_channel_videos_get**
> get_channel_videos_api_v1_youtube_web_v2_get_channel_videos_get(channel_id, language_code=language_code, country_code=country_code, continuation_token=continuation_token, need_format=need_format)

获取频道视频 /Get channel videos

# [中文] ### 用途: - 获取YouTube频道的视频列表 - 支持分页获取，可通过 continuation_token 获取更多视频  ### 参数详解:  #### 📌 必选参数: **channel_id** (string) - **作用**: 频道ID - **获取方式**:   - 从频道URL中提取，例如 `https://www.youtube.com/channel/UCJHBJ7F-nAIlMGolm0Hu4vg`   - 或从 `@用户名` 格式的URL中，先访问频道页面获取真实的频道ID - **示例**: `\"UCJHBJ7F-nAIlMGolm0Hu4vg\"`  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **continuation_token** (string, 可选) - **作用**: 分页token，用于获取下一页视频 - **获取方式**: 从上一次请求的响应中提取 - **首次请求**: 不传此参数或传 `null`  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 返回数据结构 (need_format=true): ```json {   \"videos\": [     {       \"video_id\": \"zd3yCa1bJCM\",       \"title\": \"Minecraft: DREAM! - Asleep Custom Map\",       \"thumbnail\": \"https://i.ytimg.com/vi/zd3yCa1bJCM/hqdefault.jpg\",       \"thumbnails\": [         {\"url\": \"...\", \"width\": 168, \"height\": 94},         {\"url\": \"...\", \"width\": 336, \"height\": 188}       ],       \"moving_thumbnail\": \"https://i.ytimg.com/an_webp/zd3yCa1bJCM/mqdefault_6s.webp?...\",       \"duration\": \"16:57\",       \"duration_accessibility\": \"16分钟57秒钟\",       \"view_count\": \"343,369次观看\",       \"short_view_count\": \"34万次观看\",       \"published_time\": \"18小时前\",       \"description\": \"Today, we're trapped in a super weird dream...\",       \"is_live\": false,       \"is_verified\": true,       \"url\": \"https://www.youtube.com/watch?v=zd3yCa1bJCM\",       \"playback_url\": \"https://rr5---sn-ogueln67.googlevideo.com/initplayback?...\"     }   ],   \"continuation_token\": \"下一页token\" } ```  ### 清洗后的字段说明: - `video_id`: 视频ID - `title`: 视频标题 - `thumbnail`: 最高清晰度缩略图URL - `thumbnails`: 所有分辨率的缩略图列表 - `moving_thumbnail`: 动态缩略图URL（webp格式，鼠标悬停预览） - `duration`: 视频时长（如\"16:57\"） - `duration_accessibility`: 时长无障碍文本（如\"16分钟57秒钟\"） - `view_count`: 完整观看次数（如\"343,369次观看\"） - `short_view_count`: 简短观看次数（如\"34万次观看\"） - `published_time`: 发布时间（如\"18小时前\"） - `description`: 视频描述片段 - `is_live`: 是否为直播 - `is_verified`: 频道是否已认证 - `url`: 视频播放页URL - `playback_url`: 视频播放初始化URL（googlevideo.com，可能为空） - `continuation_token`: 下一页的分页token  # [English] ### Purpose: - Get YouTube channel video list - Supports pagination via continuation_token  ### Parameters:  #### 📌 Required: **channel_id** (string) - **Purpose**: Channel ID - **How to get**:   - Extract from channel URL, e.g., `https://www.youtube.com/channel/UCJHBJ7F-nAIlMGolm0Hu4vg`   - Or visit the channel page to get the real channel ID from `@username` format URLs - **Example**: `\"UCJHBJ7F-nAIlMGolm0Hu4vg\"`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  **country_code** (string, optional) - **Purpose**: Set region code - **Default**: `\"US\"` - **Values**: `\"US\"`, `\"JP\"`, `\"GB\"`, etc.  **continuation_token** (string, optional) - **Purpose**: Pagination token for next page - **How to get**: Extract from previous response - **First request**: Omit or set to `null`  **need_format** (boolean, optional) - **Purpose**: Whether to return cleaned simplified data - **Default**: `false` - **Values**:   - `false` - Return raw complete data   - `true` - Return cleaned simplified data (recommended)  ### Response Structure (need_format=true): ```json {   \"videos\": [     {       \"video_id\": \"zd3yCa1bJCM\",       \"title\": \"Minecraft: DREAM! - Asleep Custom Map\",       \"thumbnail\": \"https://i.ytimg.com/vi/zd3yCa1bJCM/hqdefault.jpg\",       \"thumbnails\": [         {\"url\": \"...\", \"width\": 168, \"height\": 94},         {\"url\": \"...\", \"width\": 336, \"height\": 188}       ],       \"moving_thumbnail\": \"https://i.ytimg.com/an_webp/zd3yCa1bJCM/mqdefault_6s.webp?...\",       \"duration\": \"16:57\",       \"duration_accessibility\": \"16 minutes, 57 seconds\",       \"view_count\": \"343,369 views\",       \"short_view_count\": \"343K views\",       \"published_time\": \"18 hours ago\",       \"description\": \"Today, we're trapped in a super weird dream...\",       \"is_live\": false,       \"is_verified\": true,       \"url\": \"https://www.youtube.com/watch?v=zd3yCa1bJCM\",       \"playback_url\": \"https://rr5---sn-ogueln67.googlevideo.com/initplayback?...\"     }   ],   \"continuation_token\": \"next page token\" } ```  ### Cleaned Data Field Descriptions: - `video_id`: Video ID - `title`: Video title - `thumbnail`: Highest resolution thumbnail URL - `thumbnails`: List of all resolution thumbnails - `moving_thumbnail`: Moving thumbnail URL (webp format, hover preview) - `duration`: Video duration (e.g., \"16:57\") - `duration_accessibility`: Duration accessibility text (e.g., \"16 minutes, 57 seconds\") - `view_count`: Full view count (e.g., \"343,369 views\") - `short_view_count`: Short view count (e.g., \"343K views\") - `published_time`: Published time (e.g., \"18 hours ago\") - `description`: Video description snippet - `is_live`: Whether it's a live stream - `is_verified`: Whether the channel is verified - `url`: Video playback page URL - `playback_url`: Video playback initialization URL (googlevideo.com, may be empty) - `continuation_token`: Pagination token for next page  # [示例/Examples] ## 获取频道首页视频 / Get first page of channel videos GET /youtube_web/get_channel_videos?channel_id=UCJHBJ7F-nAIlMGolm0Hu4vg  ## 获取清洗后的数据（推荐）/ Get cleaned data (recommended) GET /youtube_web/get_channel_videos?channel_id=UCJHBJ7F-nAIlMGolm0Hu4vg&need_format=true  ## 获取下一页 / Get next page GET /youtube_web/get_channel_videos?channel_id=UCJHBJ7F-nAIlMGolm0Hu4vg&continuation_token=xxxxx&need_format=true

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
channel_id = NULL # object | 频道ID/Channel ID
language_code = NULL # object | 语言代码（如zh-CN, en-US等）/Language code (optional)
country_code = NULL # object | 国家代码（如US, JP等）/Country code (optional)
continuation_token = NULL # object | 分页token，用于获取下一页/Pagination token for next page (optional)
need_format = NULL # object | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data (optional)

try:
    # 获取频道视频 /Get channel videos
    api_instance.get_channel_videos_api_v1_youtube_web_v2_get_channel_videos_get(channel_id, language_code=language_code, country_code=country_code, continuation_token=continuation_token, need_format=need_format)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_channel_videos_api_v1_youtube_web_v2_get_channel_videos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | [**object**](.md)| 频道ID/Channel ID | 
 **language_code** | [**object**](.md)| 语言代码（如zh-CN, en-US等）/Language code | [optional] 
 **country_code** | [**object**](.md)| 国家代码（如US, JP等）/Country code | [optional] 
 **continuation_token** | [**object**](.md)| 分页token，用于获取下一页/Pagination token for next page | [optional] 
 **need_format** | [**object**](.md)| 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_general_search_api_v1_youtube_web_v2_get_general_search_get**
> get_general_search_api_v1_youtube_web_v2_get_general_search_get(search_query, language_code=language_code, country_code=country_code, time_zone=time_zone, upload_time=upload_time, duration=duration, content_type=content_type, feature=feature, sort_by=sort_by, continuation_token=continuation_token)

综合搜索（支持过滤条件）/General search with filters

# [中文] ### 用途: - YouTube综合搜索，支持多种过滤条件，可以精确筛选搜索结果  ### 参数详解: - **search_query**: 搜索关键字 - **language_code**: 语言代码，推荐使用zh-CN（中文）或en-US（英文） - **country_code**: 国家代码，影响搜索结果的地区相关性 - **time_zone**: 时区设置  ### 过滤条件 (选择一个值即可): #### 上传时间 (upload_time): - `hour`: 过去1小时内上传 - `today`: 今天上传 - `week`: 本周上传 - `month`: 本月上传 - `year`: 今年上传  #### 视频时长 (duration): - `short`: 短视频（少于4分钟） - `medium`: 中等时长（4-20分钟） - `long`: 长视频（超过20分钟）  #### 内容类型 (content_type): - `video`: 视频 - `channel`: 频道 - `playlist`: 播放列表 - `movie`: 电影  #### 特征 (feature): - `hd`: 高清视频 - `4k`: 4K视频 - `subtitles`: 包含字幕 - `live`: 直播 - `creative_commons`: 知识共享许可 - `360`: 360度视频 - `vr180`: VR180视频 - `3d`: 3D视频 - `hdr`: HDR视频 - `location`: 包含位置信息 - `purchased`: 已购买内容  #### 排序方式 (sort_by): - `relevance`: 相关性（默认） - `upload_date`: 上传日期 - `view_count`: 观看次数 - `rating`: 评分  ### 返回: - 包含过滤条件的搜索结果  # [English] ### Purpose: - YouTube comprehensive search with multiple filter options for precise result filtering  ### Parameters: - **search_query**: Search keyword - **language_code**: Language code (zh-CN for Chinese, en-US for English) - **country_code**: Country code affecting regional relevance - **time_zone**: Time zone setting  ### Filter Options (select one value for each): #### Upload Time (upload_time): - `hour`: Uploaded in the past hour - `today`: Uploaded today - `week`: Uploaded this week - `month`: Uploaded this month - `year`: Uploaded this year  #### Duration (duration): - `short`: Short videos (under 4 minutes) - `medium`: Medium length (4-20 minutes) - `long`: Long videos (over 20 minutes)  #### Content Type (content_type): - `video`: Videos - `channel`: Channels - `playlist`: Playlists - `movie`: Movies  #### Features (feature): - `hd`: High definition - `4k`: 4K videos - `subtitles`: With subtitles - `live`: Live streams - `creative_commons`: Creative Commons licensed - `360`: 360-degree videos - `vr180`: VR180 videos - `3d`: 3D videos - `hdr`: HDR videos - `location`: With location info - `purchased`: Purchased content  #### Sort By (sort_by): - `relevance`: Relevance (default) - `upload_date`: Upload date - `view_count`: View count - `rating`: Rating  ### Returns: - Filtered search results  # [示例/Examples] ## 基础搜索 GET /youtube_web/get_general_search?search_query=Python编程  ## 搜索本周上传的Python编程短视频 GET /youtube_web/get_general_search?search_query=Python编程&upload_time=week&duration=short  ## 搜索高清的Python教程视频，按观看次数排序 GET /youtube_web/get_general_search?search_query=Python tutorial&feature=hd&sort_by=view_count  ## 搜索今天上传的4K编程直播 GET /youtube_web/get_general_search?search_query=programming&upload_time=today&feature=4k&content_type=video

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
search_query = NULL # object | 搜索关键字/Search keyword
language_code = NULL # object | 语言代码（如zh-CN, en-US等）/Language code (optional)
country_code = NULL # object | 国家代码（如US, CN等）/Country code (optional)
time_zone = NULL # object | 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone (optional)
upload_time = NULL # object | 上传时间过滤 | Upload time filter (optional)
duration = NULL # object | 视频时长过滤 | Duration filter (optional)
content_type = NULL # object | 内容类型过滤 | Content type filter (optional)
feature = NULL # object | 特征过滤 | Feature filter (optional)
sort_by = NULL # object | 排序方式 | Sort by (optional)
continuation_token = NULL # object | 翻页令牌/Pagination token (optional)

try:
    # 综合搜索（支持过滤条件）/General search with filters
    api_instance.get_general_search_api_v1_youtube_web_v2_get_general_search_get(search_query, language_code=language_code, country_code=country_code, time_zone=time_zone, upload_time=upload_time, duration=duration, content_type=content_type, feature=feature, sort_by=sort_by, continuation_token=continuation_token)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_general_search_api_v1_youtube_web_v2_get_general_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | [**object**](.md)| 搜索关键字/Search keyword | 
 **language_code** | [**object**](.md)| 语言代码（如zh-CN, en-US等）/Language code | [optional] 
 **country_code** | [**object**](.md)| 国家代码（如US, CN等）/Country code | [optional] 
 **time_zone** | [**object**](.md)| 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone | [optional] 
 **upload_time** | [**object**](.md)| 上传时间过滤 | Upload time filter | [optional] 
 **duration** | [**object**](.md)| 视频时长过滤 | Duration filter | [optional] 
 **content_type** | [**object**](.md)| 内容类型过滤 | Content type filter | [optional] 
 **feature** | [**object**](.md)| 特征过滤 | Feature filter | [optional] 
 **sort_by** | [**object**](.md)| 排序方式 | Sort by | [optional] 
 **continuation_token** | [**object**](.md)| 翻页令牌/Pagination token | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_videos_api_v1_youtube_web_v2_get_related_videos_get**
> get_related_videos_api_v1_youtube_web_v2_get_related_videos_get(video_id=video_id, video_url=video_url, need_format=need_format)

获取视频相似内容/Get related videos

# [中文] ### 用途: - 获取YouTube视频的相似内容推荐（推荐视频列表） - 类似于视频播放页面右侧的相关视频 - 一次性返回所有推荐视频（通常20-30个）  ### 参数: - video_id: 视频ID（推荐） - video_url: 完整的视频URL（可选，如果提供video_id则忽略） - need_format: 是否格式化数据（默认 true）   - true: 返回格式化的结构化数据（推荐）   - false: 返回原始的 YouTube API 结构（用于调试或自定义解析）  ### 返回数据包含: #### 当 need_format=true 时: - video_id: 当前视频ID - related_videos: 相关视频列表（格式化后的数据）   - video_id: 相关视频的ID   - title: 视频标题   - author: 作者名称   - author_id: 作者频道ID   - author_url: 作者频道链接   - length_text: 视频时长文本（如 \"3:45\"）   - length_seconds: 视频时长（秒数）   - view_count_text: 观看次数文本（如 \"1.2M views\"）   - short_view_count_text: 简短观看次数文本（如 \"1.2M\"）   - published_time_text: 发布时间文本（如 \"2 days ago\"）   - thumbnails: 所有分辨率的缩略图列表   - rich_thumbnail: 动态缩略图（如果有）   - badges: 视频徽章（如 NEW、LIVE 等）   - owner_badges: 作者徽章（如验证标识）   - video_url: 视频链接   - navigation_endpoint: 导航端点 - total_count: 推荐视频总数  #### 当 need_format=false 时: - video_id: 当前视频ID - related_videos: 原始的 lockupViewModel 对象列表 - total_count: 推荐视频总数  ### 注意事项: - 每个视频的推荐内容由 YouTube 算法生成，可能会变化 - 推荐列表通常包含 20-30 个视频 - ⚠️ **此接口不支持分页**，一次性返回所有推荐视频  ### 价格: - $0.001 USD / 请求  # [English] ### Purpose: - Get YouTube video's related content recommendations (recommended videos list) - Similar to the related videos shown on the right side of video playback page - Returns all recommended videos at once (typically 20-30 videos)  ### Parameters: - video_id: Video ID (recommended) - video_url: Full video URL (optional, ignored if video_id is provided) - need_format: Whether to format data (default true)   - true: Return formatted structured data (recommended)   - false: Return raw YouTube API structure (for debugging or custom parsing)  ### Returns: #### When need_format=true: - video_id: Current video ID - related_videos: Related videos list   - video_id: Related video's ID   - title: Video title   - author: Author name   - author_id: Author channel ID   - author_url: Author channel URL   - length_text: Video duration text (e.g., \"3:45\")   - length_seconds: Video duration in seconds   - view_count_text: View count text (e.g., \"1.2M views\")   - short_view_count_text: Short view count text (e.g., \"1.2M\")   - published_time_text: Published time text (e.g., \"2 days ago\")   - thumbnails: All resolution thumbnails   - rich_thumbnail: Moving thumbnail (if available)   - badges: Video badges (e.g., NEW, LIVE)   - owner_badges: Channel verification badges   - video_url: Video URL   - navigation_endpoint: Navigation endpoint - total_count: Total number of recommended videos  #### When need_format=false: - video_id: Current video ID - related_videos: Raw lockupViewModel object list - total_count: Total number of recommended videos  ### Notes: - Each video's recommendations are generated by YouTube's algorithm and may change - Recommendation list typically contains 20-30 videos - ⚠️ **This API does not support pagination**, returns all recommendations at once  ### Price: - $0.001 USD / request  ### [示例/Example] #### 获取推荐视频: video_id = \"dQw4w9WgXcQ\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
video_id = NULL # object | 视频ID/Video ID (optional)
video_url = NULL # object | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) (optional)
need_format = NULL # object | 是否格式化数据。true: 返回格式化的结构化数据，false: 返回原始API结构/Whether to format data. true: return formatted structured data, false: return raw API structure (optional)

try:
    # 获取视频相似内容/Get related videos
    api_instance.get_related_videos_api_v1_youtube_web_v2_get_related_videos_get(video_id=video_id, video_url=video_url, need_format=need_format)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_related_videos_api_v1_youtube_web_v2_get_related_videos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | [**object**](.md)| 视频ID/Video ID | [optional] 
 **video_url** | [**object**](.md)| 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) | [optional] 
 **need_format** | [**object**](.md)| 是否格式化数据。true: 返回格式化的结构化数据，false: 返回原始API结构/Whether to format data. true: return formatted structured data, false: return raw API structure | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_suggestions_api_v1_youtube_web_v2_get_search_suggestions_get**
> get_search_suggestions_api_v1_youtube_web_v2_get_search_suggestions_get(keyword, language=language, region=region)

获取搜索推荐词/Get search suggestions

# [中文] ### 用途: - 获取YouTube搜索推荐词（自动补全） - 类似于在YouTube搜索框输入时显示的推荐词  ### 参数: - keyword: 搜索关键词（必填） - language: 语言代码（可选，默认 en）   - en: 英语   - zh-cn: 简体中文   - ja: 日语   - ko: 韩语 - region: 地区代码（可选，默认 US）   - US: 美国   - SG: 新加坡   - CN: 中国   - JP: 日本   - KR: 韩国  ### 返回数据包含: - keyword: 搜索关键词 - suggestions: 推荐词列表（字符串数组） - total_count: 推荐词数量  ### 注意事项: - 推荐词会根据语言和地区有所不同 - 通常返回 10-20 个推荐词 - 响应速度非常快（< 1秒）  ### 价格: - $0.0001 USD / 请求  # [English] ### Purpose: - Get YouTube search suggestions (autocomplete) - Similar to suggestions shown when typing in YouTube search box  ### Parameters: - keyword: Search keyword (required) - language: Language code (optional, default en)   - en: English   - zh-cn: Simplified Chinese   - ja: Japanese   - ko: Korean - region: Region code (optional, default US)   - US: United States   - SG: Singapore   - CN: China   - JP: Japan   - KR: Korea  ### Returns: - keyword: Search keyword - suggestions: Suggestions list (array of strings) - total_count: Number of suggestions  ### Notes: - Suggestions vary by language and region - Typically returns 10-20 suggestions - Very fast response (< 1 second)  ### Price: - $0.0001 USD / request  ### [示例/Example] #### 获取推荐词: keyword = \"Rick Astley\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
keyword = NULL # object | 搜索关键词/Search keyword
language = NULL # object | 语言代码/Language code (e.g., en, zh-cn, ja) (optional)
region = NULL # object | 地区代码/Region code (e.g., US, SG, CN, JP) (optional)

try:
    # 获取搜索推荐词/Get search suggestions
    api_instance.get_search_suggestions_api_v1_youtube_web_v2_get_search_suggestions_get(keyword, language=language, region=region)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_search_suggestions_api_v1_youtube_web_v2_get_search_suggestions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 搜索关键词/Search keyword | 
 **language** | [**object**](.md)| 语言代码/Language code (e.g., en, zh-cn, ja) | [optional] 
 **region** | [**object**](.md)| 地区代码/Region code (e.g., US, SG, CN, JP) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shorts_search_api_v1_youtube_web_v2_get_shorts_search_get**
> get_shorts_search_api_v1_youtube_web_v2_get_shorts_search_get(search_query, language_code=language_code, country_code=country_code, time_zone=time_zone, upload_time=upload_time, sort_by=sort_by, continuation_token=continuation_token, filter_mixed_content=filter_mixed_content)

YouTube Shorts短视频搜索/YouTube Shorts search

# [中文] ### 用途: - YouTube Shorts短视频专门搜索，使用原生YouTube API接口  ### 特点: - 🎬 专门搜索YouTube Shorts短视频（<60秒） - 🔍 支持多种过滤条件和排序方式 - 📱 优化的移动端短视频内容 - ⚡ 智能过滤：首次请求可能返回混合内容（长视频+短视频），默认自动过滤长视频  ### 重要说明 - YouTube Shorts搜索机制: 根据YouTube的搜索逻辑，Shorts搜索有以下特性： 1. **首次请求**（无continuation_token）：可能返回混合内容（部分长视频 + 部分短视频） 2. **后续请求**（有continuation_token）：仅返回纯短视频内容 3. **解决方案**：    - 方案A：使用 `filter_mixed_content=true`（默认），自动过滤掉长视频    - 方案B：使用第一次返回的 continuation_token 进行第二次请求，获取纯Shorts内容    - 方案C：设置 `filter_mixed_content=false`，获取原始混合内容  ### 参数详解:  #### 📌 必选参数 (Required Parameters):  **search_query** (string) - **作用**: 搜索关键字，用于匹配Shorts视频的标题、描述等内容 - **格式**: 任意字符串 - **示例**: `\"Python编程\"`, `\"gaming\"`, `\"cooking tutorial\"` - **注意**: 支持中英文及其他语言，空格会被自动处理  #### ⚙️ 可选参数 - 基础设置 (Optional Parameters - Basic Settings):  **language_code** (string, 可选) - **作用**: 设置搜索结果的显示语言，影响返回内容的语言偏好 - **默认值**: `\"en-US\"` - **可用值**:   - `\"zh-CN\"` - 简体中文   - `\"zh-TW\"` - 繁体中文   - `\"en-US\"` - 英语（美国）   - `\"en-GB\"` - 英语（英国）   - `\"ja-JP\"` - 日语   - `\"ko-KR\"` - 韩语   - `\"es-ES\"` - 西班牙语   - `\"fr-FR\"` - 法语   - `\"de-DE\"` - 德语   - 其他符合IETF BCP 47标准的语言代码 - **示例**: `language_code=zh-CN` - **影响**: 会影响搜索算法的语言匹配和结果排序  **country_code** (string, 可选) - **作用**: 设置地区/国家代码，影响搜索结果的地域相关性和内容可用性 - **默认值**: `\"US\"` - **可用值**:   - `\"US\"` - 美国   - `\"CN\"` - 中国   - `\"JP\"` - 日本   - `\"KR\"` - 韩国   - `\"GB\"` - 英国   - `\"DE\"` - 德国   - `\"FR\"` - 法国   - `\"CA\"` - 加拿大   - 其他符合ISO 3166-1 alpha-2标准的国家代码 - **示例**: `country_code=JP` - **影响**: 某些Shorts可能因地区限制而不可见  **time_zone** (string, 可选) - **作用**: 设置时区，影响时间相关过滤器（如\"今天\"、\"本周\"）的计算 - **默认值**: `\"America/Los_Angeles\"` - **可用值**: 符合IANA时区数据库的时区标识符   - `\"America/Los_Angeles\"` - 美国太平洋时区   - `\"America/New_York\"` - 美国东部时区   - `\"Asia/Shanghai\"` - 中国时区   - `\"Asia/Tokyo\"` - 日本时区   - `\"Europe/London\"` - 英国时区   - `\"Europe/Paris\"` - 法国时区 - **示例**: `time_zone=Asia/Shanghai` - **影响**: 结合upload_time参数使用时，决定\"今天\"等时间段的具体范围  **filter_mixed_content** (boolean, 可选) - **作用**: 控制是否自动过滤掉响应中的长视频（非Shorts内容） - **默认值**: `true` - **可用值**:   - `true` - 自动过滤长视频，只返回Shorts（推荐）   - `false` - 返回原始内容，可能包含长视频 - **示例**: `filter_mixed_content=true` - **使用场景**:   - `true`: 当你只需要纯Shorts内容时使用（推荐首次请求使用）   - `false`: 当你需要分析YouTube原始返回的混合内容时使用（调试用） - **注意**: 只影响首次请求，使用continuation_token的请求本身就只返回Shorts  #### 🎯 可选参数 - Shorts过滤条件 (Optional Parameters - Shorts Filters):  **upload_time** (string, 可选) - **作用**: 按上传时间过滤Shorts，只返回指定时间段内上传的视频 - **默认值**: `null` (不过滤) - **可用值**:   - `\"hour\"` - 过去1小时内上传   - `\"today\"` - 今天上传（基于time_zone参数）   - `\"week\"` - 本周上传（最近7天）   - `\"month\"` - 本月上传（最近30天）   - `\"year\"` - 今年上传（最近365天） - **示例**: `upload_time=week` - **使用场景**: 寻找最新、热门的Shorts内容 - **注意**: 与time_zone参数配合使用，时间计算基于设定的时区  **sort_by** (string, 可选) - **作用**: 设置搜索结果的排序方式 - **默认值**: `null` (YouTube默认相关性排序) - **可用值**:   - `\"relevance\"` - 按相关性排序（YouTube默认算法）   - `\"upload_date\"` - 按上传日期排序（最新优先）   - `\"view_count\"` - 按观看次数排序（最多观看优先）   - `\"rating\"` - 按评分排序（最高评分优先） - **示例**: `sort_by=view_count` - **使用场景**:   - `relevance`: 寻找最相关的内容   - `upload_date`: 寻找最新发布的Shorts   - `view_count`: 寻找最受欢迎的Shorts   - `rating`: 寻找质量最高的Shorts - **优先级**: sort_by的优先级高于upload_time，两者同时使用时以sort_by为准  #### 📄 可选参数 - 翻页控制 (Optional Parameters - Pagination):  **continuation_token** (string, 可选) - **作用**: 用于获取下一页搜索结果的翻页令牌 - **默认值**: `null` (获取第一页) - **格式**: YouTube返回的加密字符串 - **示例**: `continuation_token=EqcBEgPkuKzor4YybhmgGk...` - **获取方式**: 从上一次请求的响应中提取（见\"翻页机制详解\"部分） - **使用场景**:   - 首次搜索：不传此参数，获取第一页结果   - 后续翻页：传入上次返回的token，获取下一页结果 - **注意**:   - Token有时效性，通常在数小时内有效   - 使用continuation_token时，必须保持search_query等其他参数一致   - 使用token的请求会自动返回纯Shorts内容（无需过滤）  ### 翻页机制详解: #### 如何获取 continuation_token： 从响应JSON中提取，路径通常为以下之一： ```python # 路径1：在 onResponseReceivedCommands 中 response[\"data\"][\"onResponseReceivedCommands\"][0][\"appendContinuationItemsAction\"][\"continuationItems\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"]  # 路径2：在 contents 中 response[\"data\"][\"contents\"][\"twoColumnSearchResultsRenderer\"][\"primaryContents\"][\"sectionListRenderer\"][\"contents\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"] ```  #### 使用流程： 1. **首次请求**: 不传 continuation_token    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python    ``` 2. **提取token**: 从响应中找到 continuation_token 3. **后续请求**: 传入 continuation_token 获取下一页    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python&continuation_token=xxx    ```  ### 响应数据结构: ```json {   \"code\": 200,   \"data\": {     \"contents\": {       \"twoColumnSearchResultsRenderer\": {         \"primaryContents\": {           \"sectionListRenderer\": {             \"contents\": [               {                 \"itemSectionRenderer\": {                   \"contents\": [                     {                       \"gridShelfViewModel\": {                         // Shorts视频列表                         \"items\": [...]                       }                     }                   ]                 }               },               {                 \"continuationItemRenderer\": {                   \"continuationEndpoint\": {                     \"continuationCommand\": {                       \"token\": \"xxx\"  // 下一页的token                     }                   }                 }               }             ]           }         }       }     }   } } ```  ### 返回: - 专门针对Shorts的搜索结果，包含视频列表和翻页token  # [English] ### Purpose: - YouTube Shorts specialized search using native YouTube API  ### Features: - 🎬 Specialized search for YouTube Shorts (<60 seconds) - 🔍 Support for multiple filter conditions and sorting options - 📱 Optimized for mobile short-form content - ⚡ Smart filtering: First request may return mixed content (long+short videos), automatically filters long videos by default  ### Important - YouTube Shorts Search Mechanism: According to YouTube's search logic, Shorts search has these characteristics: 1. **First request** (no continuation_token): May return mixed content (some long videos + some short videos) 2. **Subsequent requests** (with continuation_token): Returns only pure Shorts content 3. **Solutions**:    - Solution A: Use `filter_mixed_content=true` (default) to automatically filter long videos    - Solution B: Use continuation_token from first response for second request to get pure Shorts    - Solution C: Set `filter_mixed_content=false` to get original mixed content  ### Parameters: - **search_query**: Search keyword - **language_code**: Language code (zh-CN for Chinese, en-US for English) - **country_code**: Country code affecting regional relevance - **time_zone**: Time zone (e.g., America/Los_Angeles, Asia/Shanghai) - **filter_mixed_content**: Whether to filter long videos from mixed content (default true)  ### Shorts-specific Filters: #### Upload Time (upload_time): - `hour`: Shorts uploaded in the past hour - `today`: Shorts uploaded today - `week`: Shorts uploaded this week - `month`: Shorts uploaded this month - `year`: Shorts uploaded this year  #### Sort By (sort_by): - `relevance`: Relevance (default) - `upload_date`: Upload date - `view_count`: View count - `rating`: Rating  ### Pagination Mechanism Explained: #### How to get continuation_token: Extract from response JSON, typically at one of these paths: ```python # Path 1: In onResponseReceivedCommands response[\"onResponseReceivedCommands\"][0][\"appendContinuationItemsAction\"][\"continuationItems\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"]  # Path 2: In contents response[\"contents\"][\"twoColumnSearchResultsRenderer\"][\"primaryContents\"][\"sectionListRenderer\"][\"contents\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"] ```  #### Usage Flow: 1. **First request**: Don't pass continuation_token    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python    ``` 2. **Extract token**: Find continuation_token in response 3. **Next requests**: Pass continuation_token to get next page    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python&continuation_token=xxx    ```  ### Response Data Structure: ```json {   \"code\": 200,   \"data\": {     \"contents\": {       \"twoColumnSearchResultsRenderer\": {         \"primaryContents\": {           \"sectionListRenderer\": {             \"contents\": [               {                 \"itemSectionRenderer\": {                   \"contents\": [                     {                       \"gridShelfViewModel\": {                         // Shorts video list                         \"items\": [...]                       }                     }                   ]                 }               },               {                 \"continuationItemRenderer\": {                   \"continuationEndpoint\": {                     \"continuationCommand\": {                       \"token\": \"xxx\"  // Token for next page                     }                   }                 }               }             ]           }         }       }     }   } } ```  ### Returns: - Shorts-specific search results with video list and pagination token  # [示例/Examples] ## 基础Shorts搜索（自动过滤长视频） GET /youtube_web/get_shorts_search?search_query=Python编程  ## 获取原始混合内容（包含长视频） GET /youtube_web/get_shorts_search?search_query=Python编程&filter_mixed_content=false  ## 搜索本周上传的Python相关Shorts GET /youtube_web/get_shorts_search?search_query=python&upload_time=week  ## 搜索观看次数最多的技术Shorts GET /youtube_web/get_shorts_search?search_query=技术&sort_by=view_count  ## 翻页获取更多Shorts GET /youtube_web/get_shorts_search?search_query=编程&continuation_token=EqcBEgPkuKzor4YybhmgGk...

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
search_query = NULL # object | 搜索关键字/Search keyword
language_code = NULL # object | 语言代码（如zh-CN, en-US等）/Language code (optional)
country_code = NULL # object | 国家代码（如US, CN等）/Country code (optional)
time_zone = NULL # object | 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone (optional)
upload_time = NULL # object | 上传时间过滤 | Upload time filter for Shorts (optional)
sort_by = NULL # object | 排序方式 | Sort by for Shorts (optional)
continuation_token = NULL # object | 翻页令牌/Pagination token (optional)
filter_mixed_content = NULL # object | 是否过滤混合内容（长视频），默认True / Filter mixed content (long videos), default True (optional)

try:
    # YouTube Shorts短视频搜索/YouTube Shorts search
    api_instance.get_shorts_search_api_v1_youtube_web_v2_get_shorts_search_get(search_query, language_code=language_code, country_code=country_code, time_zone=time_zone, upload_time=upload_time, sort_by=sort_by, continuation_token=continuation_token, filter_mixed_content=filter_mixed_content)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_shorts_search_api_v1_youtube_web_v2_get_shorts_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | [**object**](.md)| 搜索关键字/Search keyword | 
 **language_code** | [**object**](.md)| 语言代码（如zh-CN, en-US等）/Language code | [optional] 
 **country_code** | [**object**](.md)| 国家代码（如US, CN等）/Country code | [optional] 
 **time_zone** | [**object**](.md)| 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone | [optional] 
 **upload_time** | [**object**](.md)| 上传时间过滤 | Upload time filter for Shorts | [optional] 
 **sort_by** | [**object**](.md)| 排序方式 | Sort by for Shorts | [optional] 
 **continuation_token** | [**object**](.md)| 翻页令牌/Pagination token | [optional] 
 **filter_mixed_content** | [**object**](.md)| 是否过滤混合内容（长视频），默认True / Filter mixed content (long videos), default True | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signed_stream_url_api_v1_youtube_web_v2_get_signed_stream_url_get**
> get_signed_stream_url_api_v1_youtube_web_v2_get_signed_stream_url_get(itag, video_id=video_id, video_url=video_url)

获取已签名的视频流URL/Get signed video stream URL

# [中文] ### 用途: - 获取指定 itag 的已签名播放地址（可直接播放） - 配合 get_video_streams 接口使用，先获取所有格式，再选择 itag 获取播放地址  ### 参数: - video_id: 视频ID（推荐） - video_url: 完整的视频URL（可选） - itag: 格式标识符，从 get_video_streams 接口返回的格式列表中选择  ### 返回数据: - itag: 格式标识符 - url: 已签名的播放地址（可直接使用） - expires_in_seconds: URL有效期（通常为6小时 = 21600秒）  ### 注意事项: - 播放地址有时效性（约6小时），过期后需重新获取 - URL 长度较长（约1000-2000字符） - 某些视频可能受地区限制  # [English] ### Purpose: - Get signed playback URL for specific itag (ready to play) - Use with get_video_streams endpoint: first get all formats, then select itag to get playback URL  ### Parameters: - video_id: Video ID (recommended) - video_url: Full video URL (optional) - itag: Format identifier, selected from formats list returned by get_video_streams  ### Returns: - itag: Format identifier - url: Signed playback URL (ready to use) - expires_in_seconds: URL validity period (typically 6 hours = 21600 seconds)  ### Notes: - Playback URLs expire after approximately 6 hours, need to regenerate after expiration - URL length is long (approximately 1000-2000 characters) - Some videos may have regional restrictions  # [示例/Example] video_id = \"dQw4w9WgXcQ\" itag = 18  # 360p mp4 with audio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
itag = NULL # object | 格式标识符 itag (从 get_video_streams 接口获取)/Format identifier itag (obtained from get_video_streams endpoint)
video_id = NULL # object | 视频ID/Video ID (optional)
video_url = NULL # object | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) (optional)

try:
    # 获取已签名的视频流URL/Get signed video stream URL
    api_instance.get_signed_stream_url_api_v1_youtube_web_v2_get_signed_stream_url_get(itag, video_id=video_id, video_url=video_url)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_signed_stream_url_api_v1_youtube_web_v2_get_signed_stream_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itag** | [**object**](.md)| 格式标识符 itag (从 get_video_streams 接口获取)/Format identifier itag (obtained from get_video_streams endpoint) | 
 **video_id** | [**object**](.md)| 视频ID/Video ID | [optional] 
 **video_url** | [**object**](.md)| 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_comment_replies_api_v1_youtube_web_v2_get_video_comment_replies_get**
> get_video_comment_replies_api_v1_youtube_web_v2_get_video_comment_replies_get(continuation_token, language_code=language_code, country_code=country_code, need_format=need_format)

获取视频二级评论/Get video sub comments

# [中文] ### 用途: - 获取视频二级评论  ### 参数详解:  #### 📌 必选参数: **continuation_token** (string) - **作用**: 回复的continuation token - **获取方式**: 从一级评论的响应数据中获取 `reply_continuation_token` 字段 - **示例**: `\"Eg0SC29hU05CejRxTVFZGAYygwEaUBIaVWd3WmhjUXVGUmJZTlhkUV85VjRBYUFCQWciAggAKhhVQ0pIQko3Ri1uQUlsTUdvbG0wSHU0dmcyC29hU05CejRxTVFZQAFICoIBAggBQi9jb21tZW50LXJlcGxpZXMtaXRlbS1VZ3daaGNRdUZSYllOWGRRXzlWNEFhQUJBZw%3D%3D\"`  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置回复显示的语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 使用流程: 1. 先调用 `/get_video_comments` 接口获取一级评论 2. 从一级评论的响应中找到 `reply_continuation_token` 字段 3. 使用该 token 调用本接口获取该评论的所有回复  ### 返回数据结构 (need_format=true): ```json {   \"comments\": [     {       \"comment_id\": \"UgwZhcQuFRbYNXdQ_9V4AaABAg.A2B3C4D5E6F7G8H9I0J1\",       \"content\": \"回复内容文本\",       \"published_time\": \"2天前\",       \"reply_level\": 1,       \"like_count\": \"5\",       \"like_count_a11y\": \"5 次赞\",       \"reply_count\": \"0\",       \"author\": {         \"channel_id\": \"UCxxxxxx\",         \"display_name\": \"@username\",         \"channel_url\": \"https://www.youtube.com/@username\",         \"avatar_url\": \"https://yt3.ggpht.com/...\",         \"is_verified\": false,         \"is_creator\": true,         \"is_artist\": false       }     }   ],   \"continuation_token\": \"下一页token（如果有更多回复）\" } ```  ### 字段说明: - `reply_level`: 回复层级（1表示二级评论/回复） - `is_creator`: 是否为视频创作者（如果是创作者回复会标记为true） - 其他字段与一级评论相同  # [English] ### Purpose: - Get video second-level comments  ### Parameters: - id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc. - continuation_token: Token to continue fetching comments. Default is None. ### Returns: - Video comments.  # [示例/Example] id = \"LuIL5JATZsc\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
continuation_token = NULL # object | 回复的continuation token（从一级评论的reply_continuation_token字段获取）/Reply continuation token from first-level comment
language_code = NULL # object | 语言代码（如zh-CN, en-US等）/Language code (optional)
country_code = NULL # object | 国家代码（如US, JP等）/Country code (optional)
need_format = NULL # object | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data (optional)

try:
    # 获取视频二级评论/Get video sub comments
    api_instance.get_video_comment_replies_api_v1_youtube_web_v2_get_video_comment_replies_get(continuation_token, language_code=language_code, country_code=country_code, need_format=need_format)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_video_comment_replies_api_v1_youtube_web_v2_get_video_comment_replies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **continuation_token** | [**object**](.md)| 回复的continuation token（从一级评论的reply_continuation_token字段获取）/Reply continuation token from first-level comment | 
 **language_code** | [**object**](.md)| 语言代码（如zh-CN, en-US等）/Language code | [optional] 
 **country_code** | [**object**](.md)| 国家代码（如US, JP等）/Country code | [optional] 
 **need_format** | [**object**](.md)| 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_comments_api_v1_youtube_web_v2_get_video_comments_get**
> get_video_comments_api_v1_youtube_web_v2_get_video_comments_get(video_id, language_code=language_code, country_code=country_code, sort_by=sort_by, continuation_token=continuation_token, need_format=need_format)

获取视频评论/Get video comments

# [中文] ### 用途: - 获取YouTube视频的一级评论  ### 参数详解:  #### 📌 必选参数: **video_id** (string) - **作用**: 视频ID - **格式**: YouTube视频ID字符串 - **示例**: `\"oaSNBz4qMQY\"` - **获取方式**: 从URL `https://www.youtube.com/watch?v=oaSNBz4qMQY` 中提取  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置评论显示的语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **sort_by** (string, 可选) - **作用**: 评论排序方式 - **默认值**: `\"top\"` - **可用值**:   - `\"top\"` - 热门评论（按点赞数排序）   - `\"newest\"` - 最新评论（按时间排序）  **continuation_token** (string, 可选) - **作用**: 翻页令牌，用于获取下一页评论 - **默认值**: `null` - **获取方式**: 从上一次请求的响应中提取  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 返回数据结构 (need_format=true): ```json {   \"comments\": [     {       \"comment_id\": \"UgzRDoUJAvDNn5_8i8p4AaABAg\",       \"content\": \"评论内容文本\",       \"published_time\": \"1天前\",       \"reply_level\": 0,       \"like_count\": \"2\",       \"like_count_a11y\": \"2 次赞\",       \"reply_count\": \"0\",       \"reply_count_a11y\": \"0 条回复\",       \"reply_count_text\": \"1 条回复\",       \"reply_continuation_token\": \"...\",       \"author\": {         \"channel_id\": \"UCzRzHrLFuH0lHZYnrI84I8Q\",         \"display_name\": \"@username\",         \"channel_url\": \"https://www.youtube.com/@username\",         \"avatar_url\": \"https://yt3.ggpht.com/...\",         \"avatar_thumbnails\": [           {\"url\": \"...\", \"width\": 88, \"height\": 88}         ],         \"is_verified\": false,         \"is_creator\": false,         \"is_artist\": false       },       \"creator_thumbnail_url\": \"https://yt3.ggpht.com/...\"     }   ],   \"continuation_token\": \"下一页token\" } ```  ### 字段说明: - `comment_id`: 评论唯一ID - `content`: 评论文本内容 - `published_time`: 发布时间（相对时间，如\"1天前\"） - `reply_level`: 回复层级（0表示一级评论） - `like_count`: 点赞数 - `reply_count`: 回复数 - `reply_count_text`: 回复数文本（如\"1 条回复\"） - `reply_continuation_token`: 获取该评论回复的token - `author`: 评论作者信息   - `channel_id`: 作者频道ID   - `display_name`: 显示名称   - `channel_url`: 频道URL   - `avatar_url`: 头像URL   - `is_verified`: 是否已认证   - `is_creator`: 是否为视频创作者   - `is_artist`: 是否为音乐人 - `creator_thumbnail_url`: 视频创作者头像URL  # [English] ### Purpose: - Get YouTube video first-level comments  ### Parameters:  #### 📌 Required: **video_id** (string) - **Purpose**: Video ID - **Format**: YouTube video ID string - **Example**: `\"oaSNBz4qMQY\"` - **How to get**: Extract from URL `https://www.youtube.com/watch?v=oaSNBz4qMQY`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference for comments - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  **country_code** (string, optional) - **Purpose**: Set region code - **Default**: `\"US\"` - **Values**: `\"US\"`, `\"JP\"`, `\"GB\"`, etc.  **sort_by** (string, optional) - **Purpose**: Comment sorting method - **Default**: `\"top\"` - **Values**:   - `\"top\"` - Top comments (sorted by likes)   - `\"newest\"` - Newest comments (sorted by time)  **continuation_token** (string, optional) - **Purpose**: Pagination token for next page - **Default**: `null` - **How to get**: Extract from previous response  **need_format** (boolean, optional) - **Purpose**: Whether to return cleaned simplified data - **Default**: `false` - **Values**:   - `false` - Return raw complete data   - `true` - Return cleaned simplified data (recommended)  ### Response Structure (need_format=true): ```json {   \"comments\": [     {       \"comment_id\": \"UgzRDoUJAvDNn5_8i8p4AaABAg\",       \"content\": \"Comment text content\",       \"published_time\": \"1 day ago\",       \"reply_level\": 0,       \"like_count\": \"2\",       \"like_count_a11y\": \"2 likes\",       \"reply_count\": \"0\",       \"reply_count_a11y\": \"0 replies\",       \"reply_count_text\": \"1 reply\",       \"reply_continuation_token\": \"...\",       \"author\": {         \"channel_id\": \"UCzRzHrLFuH0lHZYnrI84I8Q\",         \"display_name\": \"@username\",         \"channel_url\": \"https://www.youtube.com/@username\",         \"avatar_url\": \"https://yt3.ggpht.com/...\",         \"avatar_thumbnails\": [           {\"url\": \"...\", \"width\": 88, \"height\": 88}         ],         \"is_verified\": false,         \"is_creator\": false,         \"is_artist\": false       },       \"creator_thumbnail_url\": \"https://yt3.ggpht.com/...\"     }   ],   \"continuation_token\": \"next page token\" } ```  ### Field Descriptions: - `comment_id`: Unique comment ID - `content`: Comment text content - `published_time`: Published time (relative, e.g., \"1 day ago\") - `reply_level`: Reply level (0 for first-level comments) - `like_count`: Number of likes - `reply_count`: Number of replies - `reply_count_text`: Reply count text (e.g., \"1 reply\") - `reply_continuation_token`: Token to get replies for this comment - `author`: Comment author info   - `channel_id`: Author's channel ID   - `display_name`: Display name   - `channel_url`: Channel URL   - `avatar_url`: Avatar URL   - `is_verified`: Whether verified   - `is_creator`: Whether video creator   - `is_artist`: Whether artist - `creator_thumbnail_url`: Video creator's avatar URL  # [示例/Examples] ## 获取热门评论 GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&sort_by=top  ## 获取最新评论 GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&sort_by=newest  ## 获取清洗后的评论数据（推荐） GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&need_format=true  ## 翻页获取更多评论 GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&continuation_token=xxx&need_format=true

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
video_id = NULL # object | 视频ID/Video ID
language_code = NULL # object | 语言代码（如zh-CN, en-US等）/Language code (optional)
country_code = NULL # object | 国家代码（如US, JP等）/Country code (optional)
sort_by = NULL # object | 排序方式 | Sort by (optional)
continuation_token = NULL # object | 翻页令牌/Pagination token (optional)
need_format = NULL # object | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data (optional)

try:
    # 获取视频评论/Get video comments
    api_instance.get_video_comments_api_v1_youtube_web_v2_get_video_comments_get(video_id, language_code=language_code, country_code=country_code, sort_by=sort_by, continuation_token=continuation_token, need_format=need_format)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_video_comments_api_v1_youtube_web_v2_get_video_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | [**object**](.md)| 视频ID/Video ID | 
 **language_code** | [**object**](.md)| 语言代码（如zh-CN, en-US等）/Language code | [optional] 
 **country_code** | [**object**](.md)| 国家代码（如US, JP等）/Country code | [optional] 
 **sort_by** | [**object**](.md)| 排序方式 | Sort by | [optional] 
 **continuation_token** | [**object**](.md)| 翻页令牌/Pagination token | [optional] 
 **need_format** | [**object**](.md)| 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_info_api_v1_youtube_web_v2_get_video_info_get**
> get_video_info_api_v1_youtube_web_v2_get_video_info_get(video_id, language_code=language_code, need_format=need_format)

获取视频详情 /Get video information

# [中文] ### 用途: - 获取YouTube视频详情信息 - 返回原始完整数据（包含 playerResponse 和 initialData）  ### 参数详解:  #### 📌 必选参数: **video_id** (string) - **作用**: 视频ID - **获取方式**: 从视频URL中提取，例如 `https://www.youtube.com/watch?v=oaSNBz4qMQY`，video_id 就是 `oaSNBz4qMQY` - **示例**: `\"oaSNBz4qMQY\"`  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  ### 返回数据结构: ```json {   \"playerResponse\": {     \"videoDetails\": {},     \"streamingData\": {       \"formats\": [],       \"adaptiveFormats\": []     },     \"microformat\": {},     ...   },   \"initialData\": {     \"contents\": {       \"twoColumnWatchNextResults\": {         \"results\": {           \"results\": {             \"contents\": [               {                 \"videoPrimaryInfoRenderer\": {...},                 \"videoSecondaryInfoRenderer\": {...}               }             ]           }         }       }     },     ...   } } ```  ### 主要字段说明: - `playerResponse`: YouTube 播放器响应数据   - `videoDetails`: 视频基本信息（可能为空，取决于YouTube的返回）   - `streamingData`: 视频流数据（包含 formats 和 adaptiveFormats，包含 googlevideo.com 的URL）   - `microformat`: 元数据信息 - `initialData`: YouTube 页面初始化数据   - `videoPrimaryInfoRenderer`: 主要信息（标题、观看次数、点赞数等）   - `videoSecondaryInfoRenderer`: 次要信息（频道信息、描述等）  # [English] ### Purpose: - Get YouTube video details - Returns raw complete data (includes playerResponse and initialData)  ### Parameters:  #### 📌 Required: **video_id** (string) - **Purpose**: Video ID - **How to get**: Extract from video URL, e.g., `https://www.youtube.com/watch?v=oaSNBz4qMQY`, video_id is `oaSNBz4qMQY` - **Example**: `\"oaSNBz4qMQY\"`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  ### Response Structure: ```json {   \"playerResponse\": {     \"videoDetails\": {},     \"streamingData\": {       \"formats\": [],       \"adaptiveFormats\": []     },     \"microformat\": {},     ...   },   \"initialData\": {     \"contents\": {       \"twoColumnWatchNextResults\": {         \"results\": {           \"results\": {             \"contents\": [               {                 \"videoPrimaryInfoRenderer\": {...},                 \"videoSecondaryInfoRenderer\": {...}               }             ]           }         }       }     },     ...   } } ```  ### Key Fields: - `playerResponse`: YouTube player response data   - `videoDetails`: Basic video info (may be empty depending on YouTube's response)   - `streamingData`: Video stream data (includes formats and adaptiveFormats with googlevideo.com URLs)   - `microformat`: Metadata information - `initialData`: YouTube page initialization data   - `videoPrimaryInfoRenderer`: Primary info (title, view count, like count, etc.)   - `videoSecondaryInfoRenderer`: Secondary info (channel info, description, etc.)  # [示例/Examples] ## 获取视频详情数据 / Get video details GET /youtube_web/get_video_info?video_id=oaSNBz4qMQY  ## 指定语言 / Specify language GET /youtube_web/get_video_info?video_id=oaSNBz4qMQY&language_code=en-US

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
video_id = NULL # object | 视频ID/Video ID
language_code = NULL # object | 语言代码（如zh-CN, en-US等）/Language code (optional)
need_format = NULL # object | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data (optional)

try:
    # 获取视频详情 /Get video information
    api_instance.get_video_info_api_v1_youtube_web_v2_get_video_info_get(video_id, language_code=language_code, need_format=need_format)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_video_info_api_v1_youtube_web_v2_get_video_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | [**object**](.md)| 视频ID/Video ID | 
 **language_code** | [**object**](.md)| 语言代码（如zh-CN, en-US等）/Language code | [optional] 
 **need_format** | [**object**](.md)| 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_streams_api_v1_youtube_web_v2_get_video_streams_get**
> get_video_streams_api_v1_youtube_web_v2_get_video_streams_get(video_id=video_id, video_url=video_url)

获取视频流信息/Get video streams info

# [中文] ### ⚠️ 重要说明: - **此接口仅返回格式信息，URL 字段为 null** - **必须搭配 get_signed_stream_url 接口获取播放地址** - 如需一次性获取所有 URL，请使用 get_video_streams_v2 接口  ### 用途: - 获取YouTube视频所有清晰度的格式信息 - 返回标准格式（音视频合并）和自适应格式（音视频分离）  ### 参数: - video_id: 视频ID（推荐） - video_url: 完整的视频URL（可选，如果提供video_id则忽略）  ### 返回数据包含: - 视频基本信息（标题、作者、时长、观看次数等） - formats: 标准格式流（包含音频和视频） - adaptive_formats: 自适应格式流（仅视频或仅音频）   - 每个格式包含: itag、mime_type、质量标签、分辨率、比特率等   - ⚠️ **url 字段为 null**（YouTube 需要签名解密才能获取真实播放地址）   - has_signature 为 true 表示需要使用 get_signed_stream_url 接口 - hls_manifest_url: HLS流地址（如果有） - dash_manifest_url: DASH流地址（如果有） - available_qualities: 所有可用的清晰度列表  ### 使用流程（两步法）: 1. **第一步**: 调用此接口获取所有可用格式信息（URL 为 null） 2. **第二步**: 从返回的 formats 或 adaptive_formats 中选择需要的 itag 3. **第三步**: 调用 get_signed_stream_url 接口，传入 video_id 和 itag，获取真实播放地址  ### 注意事项: - YouTube 视频播放地址需要签名解密，原始 API 返回的 URL 字段为 null 是正常现象 - 播放地址必须通过 get_signed_stream_url 接口单独获取 - 高清视频（720p+）通常需要分别下载音视频流并合并  ### 价格: - $0.001 USD/请求  # [English] ### ⚠️ Important Notice: - **This endpoint ONLY returns format information, URL fields are null** - **MUST use get_signed_stream_url endpoint to get playback URLs** - For getting all URLs at once, use get_video_streams_v2 endpoint  ### Purpose: - Get all quality format information for YouTube video - Returns standard formats (merged audio/video) and adaptive formats (separate audio/video)  ### Parameters: - video_id: Video ID (recommended) - video_url: Full video URL (optional, ignored if video_id is provided)  ### Returns: - Basic video info (title, author, duration, view count, etc.) - formats: Standard format streams (audio and video combined) - adaptive_formats: Adaptive format streams (video-only or audio-only)   - Each format contains: itag, mime_type, quality label, resolution, bitrate, etc.   - ⚠️ **url field is null** (YouTube requires signature decryption to get actual playback URL)   - has_signature=true means need to use get_signed_stream_url endpoint - hls_manifest_url: HLS manifest URL (if available) - dash_manifest_url: DASH manifest URL (if available) - available_qualities: List of all available quality levels  ### Usage Flow (Two-Step Method): 1. **Step 1**: Call this endpoint to get all available format information (URLs are null) 2. **Step 2**: Select the desired itag from returned formats or adaptive_formats 3. **Step 3**: Call get_signed_stream_url endpoint with video_id and itag to get actual playback URL  ### Notes: - YouTube video playback URLs require signature decryption, null URL fields in raw API response is normal - Playback URLs must be obtained separately via get_signed_stream_url endpoint - High-quality videos (720p+) usually require separate download and merge of audio/video streams  ### Price: - $0.001 USD/request  ### [示例/Example] #### Step 1 - 获取格式信息: video_id = \"dQw4w9WgXcQ\" #### Step 2 - 获取播放地址: use get_signed_stream_url with selected itag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
video_id = NULL # object | 视频ID/Video ID (optional)
video_url = NULL # object | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) (optional)

try:
    # 获取视频流信息/Get video streams info
    api_instance.get_video_streams_api_v1_youtube_web_v2_get_video_streams_get(video_id=video_id, video_url=video_url)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_video_streams_api_v1_youtube_web_v2_get_video_streams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | [**object**](.md)| 视频ID/Video ID | [optional] 
 **video_url** | [**object**](.md)| 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_streams_v2_api_v1_youtube_web_v2_get_video_streams_v2_get**
> get_video_streams_v2_api_v1_youtube_web_v2_get_video_streams_v2_get(video_id=video_id, video_url=video_url)

获取视频流信息 V2/Get video streams info V2

# [中文] ### ✅ 特性: - **自动返回所有格式的已解密播放地址** - 无需额外调用 get_signed_stream_url 接口 - 一次性获取所有清晰度的可用链接  ### 用途: - 获取YouTube视频所有清晰度的格式信息和播放地址 - 返回标准格式（音视频合并）和自适应格式（音视频分离） - 适合需要展示所有清晰度选项的场景  ### 参数: - video_id: 视频ID（推荐） - video_url: 完整的视频URL（可选，如果提供video_id则忽略）  ### 返回数据包含: - 视频基本信息（标题、作者、时长、观看次数等） - formats: 标准格式流（包含音频和视频） - adaptive_formats: 自适应格式流（仅视频或仅音频）   - 每个格式包含: itag、mime_type、质量标签、分辨率、比特率等   - ✅ **url 字段包含已解密的播放地址，可直接使用**   - has_signature 为 false 表示 URL 已解密，可直接播放 - hls_manifest_url: HLS流地址（如果有） - dash_manifest_url: DASH流地址（如果有） - available_qualities: 所有可用的清晰度列表 - expires_in_seconds: URL 过期时间（约 6 小时 = 21600 秒）  ### 与 get_video_streams 的区别: - **get_video_streams**: URL 为 null，需要搭配 get_signed_stream_url 使用（两步法） - **get_video_streams_v2 (本接口)**: 自动返回所有已解密的 URL（一步到位）  ### 注意事项: - 播放地址有时效性（约6小时），建议获取后尽快使用 - 高清视频（720p+）通常需要分别下载音视频流并合并 - 响应时间较长（约10秒），因为需要为所有格式解密 URL  ### 价格: - $0.003 USD/请求  # [English] ### ✅ Features: - **Automatically returns decrypted playback URLs for all formats** - No need to call get_signed_stream_url endpoint separately - Get all quality URLs in one request  ### Purpose: - Get all quality format information and playback URLs for YouTube video - Returns standard formats (merged audio/video) and adaptive formats (separate audio/video) - Suitable for scenarios that need to display all quality options  ### Parameters: - video_id: Video ID (recommended) - video_url: Full video URL (optional, ignored if video_id is provided)  ### Returns: - Basic video info (title, author, duration, view count, etc.) - formats: Standard format streams (audio and video combined) - adaptive_formats: Adaptive format streams (video-only or audio-only)   - Each format contains: itag, mime_type, quality label, resolution, bitrate, etc.   - ✅ **url field contains decrypted playback URL, ready to use**   - has_signature=false means URL is decrypted and ready to play - hls_manifest_url: HLS manifest URL (if available) - dash_manifest_url: DASH manifest URL (if available) - available_qualities: List of all available quality levels - expires_in_seconds: URL expiration time (about 6 hours = 21600 seconds)  ### Difference from get_video_streams: - **get_video_streams**: URLs are null, need to use get_signed_stream_url (two-step method) - **get_video_streams_v2 (this endpoint)**: Automatically returns all decrypted URLs (one-step solution)  ### Notes: - Playback URLs expire after ~6 hours, use them promptly - High-quality videos (720p+) usually require separate download and merge of audio/video streams - Longer response time (~10 seconds) as it needs to decrypt URLs for all formats  ### Price: - $0.003 USD/request  ### [示例/Example] #### 获取所有格式和URL: video_id = \"dQw4w9WgXcQ\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
video_id = NULL # object | 视频ID/Video ID (optional)
video_url = NULL # object | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) (optional)

try:
    # 获取视频流信息 V2/Get video streams info V2
    api_instance.get_video_streams_v2_api_v1_youtube_web_v2_get_video_streams_v2_get(video_id=video_id, video_url=video_url)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->get_video_streams_v2_api_v1_youtube_web_v2_get_video_streams_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | [**object**](.md)| 视频ID/Video ID | [optional] 
 **video_url** | [**object**](.md)| 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_channels_api_v1_youtube_web_v2_search_channels_get**
> search_channels_api_v1_youtube_web_v2_search_channels_get(keyword=keyword, continuation_token=continuation_token, need_format=need_format)

搜索频道/Search channels

# [中文] ### 用途: - 搜索YouTube频道 - 只返回频道类型的搜索结果（过滤掉视频、播放列表等） - 支持分页获取更多频道  ### 参数: - keyword: 搜索关键词（首次请求必填） - continuation_token: 分页token（可选，用于获取下一页） - need_format: 是否格式化数据（默认 true）   - true: 返回格式化的结构化数据（推荐）   - false: 返回原始的 YouTube API 结构（用于调试）  ### 返回数据包含: #### 当 need_format=true 时: - keyword: 搜索关键词 - channels: 频道列表   - channel_id: 频道ID（如 \"UCjuNibFJ21MiSNpu8LZyV4w\"）   - title: 频道名称   - handle: 频道自定义handle（如 \"@chaijing2023\"）   - subscriber_count_text: 订阅者数量文本（如 \"1.11M subscribers\"）   - description: 频道描述片段   - thumbnails: 缩略图列表（包含不同尺寸）   - is_subscribed: 当前用户是否已订阅该频道（布尔值）   - canonical_url: 频道规范URL路径（如 \"/@chaijing2023\"）   - channel_url: 频道完整URL（优先使用自定义URL） - continuation_token: 下一页的分页token - has_more: 是否还有更多频道 - total_count: 当前页频道数量  #### 当 need_format=false 时: - keyword: 搜索关键词 - channels: 原始的 channelRenderer 对象列表 - continuation_token: 下一页的分页token - has_more: 是否还有更多频道 - total_count: 当前页频道数量  ### 使用流程: 1. 首次请求：只传 keyword 参数 2. 获取响应中的 continuation_token 3. 下次请求：传入 continuation_token（keyword 可选） 4. 重复步骤 2-3 直到 has_more 为 false  ### 注意事项: - 每页通常返回 10-20 个频道 - 搜索结果只包含频道，不包含视频、播放列表等 - 搜索结果的顺序和数量由 YouTube 算法决定  ### 价格: - $0.001 USD / 请求  # [English] ### Purpose: - Search YouTube channels - Only returns channel-type search results (filters out videos, playlists, etc.) - Supports pagination to get more channels  ### Parameters: - keyword: Search keyword (required for first request) - continuation_token: Pagination token (optional, for next page) - need_format: Whether to format data (default true)   - true: Return formatted structured data (recommended)   - false: Return raw YouTube API structure (for debugging)  ### Returns: #### When need_format=true: - keyword: Search keyword - channels: Channels list   - channel_id: Channel ID (e.g., \"UCjuNibFJ21MiSNpu8LZyV4w\")   - title: Channel name   - handle: Channel custom handle (e.g., \"@chaijing2023\")   - subscriber_count_text: Subscriber count text (e.g., \"1.11M subscribers\")   - description: Channel description snippet   - thumbnails: Thumbnail list (multiple sizes)   - is_subscribed: Whether current user is subscribed to this channel (boolean)   - canonical_url: Channel canonical URL path (e.g., \"/@chaijing2023\")   - channel_url: Full channel URL (prefers custom URL) - continuation_token: Next page pagination token - has_more: Whether there are more channels - total_count: Current page channel count  #### When need_format=false: - keyword: Search keyword - channels: Raw channelRenderer object list - continuation_token: Next page pagination token - has_more: Whether there are more channels - total_count: Current page channel count  ### Usage Flow: 1. First request: Only pass keyword parameter 2. Get continuation_token from response 3. Next request: Pass continuation_token (keyword optional) 4. Repeat steps 2-3 until has_more is false  ### Notes: - Each page typically returns 10-20 channels - Search results only include channels, not videos, playlists, etc. - Order and quantity of results determined by YouTube algorithm  ### Price: - $0.001 USD / request  ### [示例/Example] #### 搜索频道: keyword = \"Rick Astley\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.YouTubeWebV2APIApi()
keyword = NULL # object | 搜索关键词/Search keyword (optional)
continuation_token = NULL # object | 分页token/Pagination token (optional)
need_format = NULL # object | 是否格式化数据/Whether to format data (optional)

try:
    # 搜索频道/Search channels
    api_instance.search_channels_api_v1_youtube_web_v2_search_channels_get(keyword=keyword, continuation_token=continuation_token, need_format=need_format)
except ApiException as e:
    print("Exception when calling YouTubeWebV2APIApi->search_channels_api_v1_youtube_web_v2_search_channels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 搜索关键词/Search keyword | [optional] 
 **continuation_token** | [**object**](.md)| 分页token/Pagination token | [optional] 
 **need_format** | [**object**](.md)| 是否格式化数据/Whether to format data | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

