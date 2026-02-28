# swagger_client.DemoAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get**](DemoAPIApi.md#douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get) | **GET** /api/v1/demo/douyin/app/fetch_one_video | 【Demo】抖音APP获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin APP Fixed Video Data with Cache
[**douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get**](DemoAPIApi.md#douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get) | **GET** /api/v1/demo/douyin_search/app/general_search | 【Demo】抖音搜索综合搜索（1小时缓存）/[Demo] Douyin General Search with Cache
[**douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get**](DemoAPIApi.md#douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get) | **GET** /api/v1/demo/douyin/web/fetch_one_video | 【Demo】抖音Web获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin Web Fixed Video Data with Cache
[**instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get**](DemoAPIApi.md#instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get) | **GET** /api/v1/demo/instagram/web/fetch_user_info | 【Demo】Instagram获取固定用户信息（1小时缓存）/[Demo] Instagram Fixed User Profile with Cache
[**kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get**](DemoAPIApi.md#kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get) | **GET** /api/v1/demo/kuaishou/web/fetch_one_video | 【Demo】快手获取固定视频信息（1小时缓存）/[Demo] Kuaishou Fixed Video with Cache
[**tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get**](DemoAPIApi.md#tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get) | **GET** /api/v1/demo/tiktok/app/fetch_one_video | 【Demo】TikTok APP获取固定视频详情（1小时缓存）/[Demo] TikTok APP Fixed Video Detail with Cache
[**tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get**](DemoAPIApi.md#tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get) | **GET** /api/v1/demo/tiktok/web/fetch_user_profile | 【Demo】TikTok固定用户信息（1小时缓存）/[Demo] TikTok Fixed User Profile with Cache
[**view_cache_status_api_v1_demo_demo_cache_status_get**](DemoAPIApi.md#view_cache_status_api_v1_demo_demo_cache_status_get) | **GET** /api/v1/demo/demo/cache_status | 查看Demo缓存状态/View Demo Cache Status
[**wechat_article_extract_api_v1_demo_wechat_article_extract_get**](DemoAPIApi.md#wechat_article_extract_api_v1_demo_wechat_article_extract_get) | **GET** /api/v1/demo/wechat/article_extract | 【Demo】微信公众号文章提取（1小时缓存）/[Demo] WeChat Article Extract with Cache


# **douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get**
> douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get()

【Demo】抖音APP获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin APP Fixed Video Data with Cache

# 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示(Demo)接口，仅用于测试和展示功能** - **不允许修改aweme_id参数，始终返回固定作品的数据** - **数据缓存1小时**  ### 用途: - 用于测试API连接和数据格式 - 了解返回数据结构 - 开发阶段的功能验证  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定作品ID: 7534641277405531446 - ✅ 固定作品的对应链接: https://www.douyin.com/video/7534641277405531446 - ✅ 免费使用，无需计费  ### 返回: - 固定作品的缓存数据  ---  ## [English] ### ⚠️ Important Notice: - **This is a DEMO endpoint for testing and demonstration only** - **The aweme_id parameter cannot be modified, always returns data for a fixed video** - **Data is cached for 1 hour**  ### Purpose: - Test API connection and data format - Understand return data structure - Feature validation during development  ### Features: - ✅ 1-hour data caching - ✅ Fixed video ID: 7534641277405531446 - ✅ Fixed video link: https://www.douyin.com/video/7534641277405531446 - ✅ Free to use, no billing  ### Return: - Cached data for the fixed video  ---  # [示例/Example] ``` # 无需参数，始终返回固定作品数据 # No parameters needed, always returns fixed video data GET /api/v1/douyin/app/fetch_one_video ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemoAPIApi()

try:
    # 【Demo】抖音APP获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin APP Fixed Video Data with Cache
    api_instance.douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get()
except ApiException as e:
    print("Exception when calling DemoAPIApi->douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get: %s\n" % e)
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

# **douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get**
> douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get()

【Demo】抖音搜索综合搜索（1小时缓存）/[Demo] Douyin General Search with Cache

# 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示接口，返回固定关键词的搜索结果** - **搜索关键词固定为\"美食\"** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定搜索关键词: 美食 - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Demo endpoint returning fixed keyword search results** - **Search keyword fixed as \"美食\" (Food)** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed search keyword: 美食 - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定关键词搜索结果 # No parameters needed, always returns fixed keyword search results GET /api/v1/douyin_search/app/general_search ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemoAPIApi()

try:
    # 【Demo】抖音搜索综合搜索（1小时缓存）/[Demo] Douyin General Search with Cache
    api_instance.douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get()
except ApiException as e:
    print("Exception when calling DemoAPIApi->douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get: %s\n" % e)
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

# **douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get**
> douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get()

【Demo】抖音Web获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin Web Fixed Video Data with Cache

# 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示(Demo)接口，仅用于测试和展示功能** - **不允许修改aweme_id参数，始终返回固定作品的数据** - **数据缓存1小时**  ### 用途: - 用于测试API连接和数据格式 - 了解返回数据结构 - 开发阶段的功能验证  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定作品ID: 7534641277405531446 - ✅ 固定作品的对应链接: https://www.douyin.com/video/7534641277405531446 - ✅ 免费使用，无需计费  ### 返回: - 固定作品的缓存数据  ---  ## [English] ### ⚠️ Important Notice: - **This is a DEMO endpoint for testing and demonstration only** - **The aweme_id parameter cannot be modified, always returns data for a fixed video** - **Data is cached for 1 hour**  ### Purpose: - Test API connection and data format - Understand return data structure - Feature validation during development  ### Features: - ✅ 1-hour data caching - ✅ Fixed video ID: 7534641277405531446 - ✅ Fixed video link: https://www.douyin.com/video/7534641277405531446 - ✅ Free to use, no billing  ### Return: - Cached data for the fixed video  ---  # [示例/Example] ``` # 无需参数，始终返回固定作品数据 # No parameters needed, always returns fixed video data GET /api/v1/douyin/web/fetch_one_video ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemoAPIApi()

try:
    # 【Demo】抖音Web获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin Web Fixed Video Data with Cache
    api_instance.douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get()
except ApiException as e:
    print("Exception when calling DemoAPIApi->douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get: %s\n" % e)
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

# **instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get**
> instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get()

【Demo】Instagram获取固定用户信息（1小时缓存）/[Demo] Instagram Fixed User Profile with Cache

# 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定Instagram用户信息** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定用户: Instagram - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed Instagram user profile** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed user: Instagram - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定用户数据 # No parameters needed, always returns fixed user data GET /api/v1/instagram/web/fetch_user_info ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemoAPIApi()

try:
    # 【Demo】Instagram获取固定用户信息（1小时缓存）/[Demo] Instagram Fixed User Profile with Cache
    api_instance.instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get()
except ApiException as e:
    print("Exception when calling DemoAPIApi->instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get: %s\n" % e)
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

# **kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get**
> kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get()

【Demo】快手获取固定视频信息（1小时缓存）/[Demo] Kuaishou Fixed Video with Cache

# 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定快手视频信息** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定视频数据，参数：https://www.kuaishou.com/short-video/3x73wr9tdt7nxqy - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed Kuaishou video info** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed video data, parameter: https://www.kuaishou.com/short-video/3x73wr9tdt7nxqy - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定视频数据 # No parameters needed, always returns fixed video data GET /api/v1/kuaishou/web/fetch_one_video ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemoAPIApi()

try:
    # 【Demo】快手获取固定视频信息（1小时缓存）/[Demo] Kuaishou Fixed Video with Cache
    api_instance.kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get()
except ApiException as e:
    print("Exception when calling DemoAPIApi->kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get: %s\n" % e)
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

# **tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get**
> tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get()

【Demo】TikTok APP获取固定视频详情（1小时缓存）/[Demo] TikTok APP Fixed Video Detail with Cache

# 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定TikTok视频详情** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定视频详情，参数: 7319033421676653855 - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed TikTok video detail** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed video detail, parameter: 7319033421676653855 - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定视频数据 # No parameters needed, always returns fixed video data GET /api/v1/tiktok/app/fetch_one_video ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemoAPIApi()

try:
    # 【Demo】TikTok APP获取固定视频详情（1小时缓存）/[Demo] TikTok APP Fixed Video Detail with Cache
    api_instance.tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get()
except ApiException as e:
    print("Exception when calling DemoAPIApi->tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get: %s\n" % e)
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

# **tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get**
> tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get()

【Demo】TikTok固定用户信息（1小时缓存）/[Demo] TikTok Fixed User Profile with Cache

# 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定TikTok用户信息** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定用户: tiktok - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed TikTok user profile** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed user: tiktok - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定用户数据 # No parameters needed, always returns fixed user data GET /api/v1/tiktok/web/fetch_user_profile ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemoAPIApi()

try:
    # 【Demo】TikTok固定用户信息（1小时缓存）/[Demo] TikTok Fixed User Profile with Cache
    api_instance.tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get()
except ApiException as e:
    print("Exception when calling DemoAPIApi->tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get: %s\n" % e)
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

# **view_cache_status_api_v1_demo_demo_cache_status_get**
> view_cache_status_api_v1_demo_demo_cache_status_get()

查看Demo缓存状态/View Demo Cache Status

# 查看所有Demo接口的缓存状态  ## [中文] ### 用途: - 查看当前缓存的Demo数据 - 了解缓存过期时间  ## [English] ### Purpose: - View current cached Demo data - Check cache expiration times

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemoAPIApi()

try:
    # 查看Demo缓存状态/View Demo Cache Status
    api_instance.view_cache_status_api_v1_demo_demo_cache_status_get()
except ApiException as e:
    print("Exception when calling DemoAPIApi->view_cache_status_api_v1_demo_demo_cache_status_get: %s\n" % e)
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

# **wechat_article_extract_api_v1_demo_wechat_article_extract_get**
> wechat_article_extract_api_v1_demo_wechat_article_extract_get()

【Demo】微信公众号文章提取（1小时缓存）/[Demo] WeChat Article Extract with Cache

# 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示(Demo)接口，仅用于测试和展示功能** - **不允许修改URL参数，始终返回固定文章的数据** - **数据缓存1小时**  ### 用途: - 用于测试API连接和数据格式 - 了解返回数据结构 - 开发阶段的功能验证  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定文章URL: https://mp.weixin.qq.com/s/c7_-h_3XJLpOBqpUfIlJ9w - ✅ 免费使用，无需计费  ### 返回: - 固定文章的缓存数据  ---  ## [English] ### ⚠️ Important Notice: - **This is a DEMO endpoint for testing and demonstration only** - **The URL parameter cannot be modified, always returns data for a fixed article** - **Data is cached for 1 hour**  ### Purpose: - Test API connection and data format - Understand return data structure - Feature validation during development  ### Features: - ✅ 1-hour data caching - ✅ Fixed article URL: https://mp.weixin.qq.com/s/c7_-h_3XJLpOBqpUfIlJ9w - ✅ Free to use, no billing  ### Return: - Cached data for the fixed article  ---  # [示例/Example] ``` # 无需参数，始终返回固定文章数据 # No parameters needed, always returns fixed article data GET /api/v1/wechat/article_extract ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DemoAPIApi()

try:
    # 【Demo】微信公众号文章提取（1小时缓存）/[Demo] WeChat Article Extract with Cache
    api_instance.wechat_article_extract_api_v1_demo_wechat_article_extract_get()
except ApiException as e:
    print("Exception when calling DemoAPIApi->wechat_article_extract_api_v1_demo_wechat_article_extract_get: %s\n" % e)
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

