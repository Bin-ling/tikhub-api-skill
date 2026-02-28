# swagger_client.TwitterWebAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get**](TwitterWebAPIApi.md#fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get) | **GET** /api/v1/twitter/web/fetch_latest_post_comments | 获取最新的推文评论/Get the latest tweet comments
[**fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get**](TwitterWebAPIApi.md#fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get) | **GET** /api/v1/twitter/web/fetch_post_comments | 获取评论/Get comments
[**fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get**](TwitterWebAPIApi.md#fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get) | **GET** /api/v1/twitter/web/fetch_retweet_user_list | 转推用户列表/ReTweet User list
[**fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get**](TwitterWebAPIApi.md#fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get) | **GET** /api/v1/twitter/web/fetch_search_timeline | 搜索/Search
[**fetch_trending_api_v1_twitter_web_fetch_trending_get**](TwitterWebAPIApi.md#fetch_trending_api_v1_twitter_web_fetch_trending_get) | **GET** /api/v1/twitter/web/fetch_trending | 趋势/Trending
[**fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get**](TwitterWebAPIApi.md#fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get) | **GET** /api/v1/twitter/web/fetch_tweet_detail | 获取单个推文数据/Get single tweet data
[**fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get**](TwitterWebAPIApi.md#fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get) | **GET** /api/v1/twitter/web/fetch_user_followers | 用户粉丝/User Followers
[**fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get**](TwitterWebAPIApi.md#fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get) | **GET** /api/v1/twitter/web/fetch_user_followings | 用户关注/User Followings
[**fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get**](TwitterWebAPIApi.md#fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get) | **GET** /api/v1/twitter/web/fetch_user_highlights_tweets | 获取用户高光推文/Get user highlights tweets
[**fetch_user_media_api_v1_twitter_web_fetch_user_media_get**](TwitterWebAPIApi.md#fetch_user_media_api_v1_twitter_web_fetch_user_media_get) | **GET** /api/v1/twitter/web/fetch_user_media | 获取用户媒体/Get user media
[**fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get**](TwitterWebAPIApi.md#fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get) | **GET** /api/v1/twitter/web/fetch_user_post_tweet | 获取用户发帖/Get user post
[**fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get**](TwitterWebAPIApi.md#fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get) | **GET** /api/v1/twitter/web/fetch_user_profile | 获取用户资料/Get user profile
[**fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get**](TwitterWebAPIApi.md#fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get) | **GET** /api/v1/twitter/web/fetch_user_tweet_replies | 获取用户推文回复/Get user tweet replies


# **fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get**
> fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get(tweet_id, cursor=cursor)

获取最新的推文评论/Get the latest tweet comments

# [中文] ### 用途: - 获取最新的推文评论 ### 参数: - tweet_id: 推文ID - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 推文评论  # [English] ### Purpose: - Get the latest tweet comments ### Parameters: - tweet_id: Tweet ID - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - Tweet comments  # [示例/Example] tweet_id = \"1808168603721650364\" cursor = None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
tweet_id = NULL # object | 推文ID/Tweet ID
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取最新的推文评论/Get the latest tweet comments
    api_instance.fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get(tweet_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tweet_id** | [**object**](.md)| 推文ID/Tweet ID | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get**
> fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get(tweet_id, cursor=cursor)

获取评论/Get comments

# [中文] ### 用途: - 获取推文下的评论 ### 参数: - tweet_id: 推文ID - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 评论  # [English] ### Purpose: - Get comments under the tweet ### Parameters: - tweet_id: Tweet ID - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - Comments  # [示例/Example] tweet_id = \"1808168603721650364\" cursor = None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
tweet_id = NULL # object | 推文ID/Tweet ID
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取评论/Get comments
    api_instance.fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get(tweet_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tweet_id** | [**object**](.md)| 推文ID/Tweet ID | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get**
> fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get(tweet_id, cursor=cursor)

转推用户列表/ReTweet User list

# [中文] ### 用途: - 获取转推用户列表 ### 参数: - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的 1808168603721650364。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 转推用户列表  # [English] ### Purpose: - Get ReTweet User list ### Parameters: - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364 - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - ReTweet User list  # [示例/Example] tweet_id = \"1808168603721650364\" cursor = None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
tweet_id = NULL # object | 推文ID/Tweet ID
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 转推用户列表/ReTweet User list
    api_instance.fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get(tweet_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tweet_id** | [**object**](.md)| 推文ID/Tweet ID | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get**
> fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get(keyword, search_type=search_type, cursor=cursor)

搜索/Search

# [中文] ### 用途: - 搜索 ### 参数: - keyword: 搜索关键字 - search_type: 搜索类型，默认为Top，其他可选值为Latest，Media，People, Lists - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 搜索结果  # [English] ### Purpose: - Search ### Parameters: - keyword: Search keyword - search_type: Search type, default is Top, other optional values are Latest, Media, People, Lists - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - Search results  # [示例/Example] keyword = \"Elon Musk\" search_type = \"Top\" cursor = None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
keyword = NULL # object | 搜索关键字/Search Keyword
search_type = NULL # object | 搜索类型/Search Type (optional)
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 搜索/Search
    api_instance.fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get(keyword, search_type=search_type, cursor=cursor)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 搜索关键字/Search Keyword | 
 **search_type** | [**object**](.md)| 搜索类型/Search Type | [optional] 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_trending_api_v1_twitter_web_fetch_trending_get**
> fetch_trending_api_v1_twitter_web_fetch_trending_get(country=country)

趋势/Trending

# [中文] ### 用途: - 获取趋势 ### 参数: - country: 国家，默认为UnitedStates，其他可选值见下方     - China     - India     - Japan     - Russia     - Germany     - Indonesia     - Brazil     - France     - UnitedKingdom     - Turkey     - Italy     - Mexico     - SouthKorea     - Canada     - Spain     - SaudiArabia     - Egypt     - Australia     - Poland     - Iran     - Pakistan     - Vietnam     - Nigeria     - Bangladesh     - Netherlands     - Argentina     - Philippines     - Malaysia     - Colombia     - UniteArabEmirates     - Romania     - Belgium     - Switzerland     - Singapore     - Sweden     - Norway     - Austria     - Kazakhstan     - Algeria     - Chile     - Czechia     - Peru     - Iraq     - Israel     - Ukraine     - Denmark     - Portugal     - Hungary     - Greece     - Finland     - NewZealand     - Belarus     - Slovakia     - Serbia     - Lithuania     - Luxembourg     - Estonia  ### 返回: - 趋势  # [English] ### Purpose: - Get Trending ### Parameters: - country: Country, default is UnitedStates, other optional values are as follows     - China     - India     - Japan     - Russia     - Germany     - Indonesia     - Brazil     - France     - UnitedKingdom     - Turkey     - Italy     - Mexico     - SouthKorea     - Canada     - Spain     - SaudiArabia     - Egypt     - Australia     - Poland     - Iran     - Pakistan     - Vietnam     - Nigeria     - Bangladesh     - Netherlands     - Argentina     - Philippines     - Malaysia     - Colombia     - UniteArabEmirates     - Romania     - Belgium     - Switzerland     - Singapore     - Sweden     - Norway     - Austria     - Kazakhstan     - Algeria     - Chile     - Czechia     - Peru  ### Return: - Trending  # [示例/Example] country = \"UnitedStates\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
country = NULL # object | 国家/Country (optional)

try:
    # 趋势/Trending
    api_instance.fetch_trending_api_v1_twitter_web_fetch_trending_get(country=country)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_trending_api_v1_twitter_web_fetch_trending_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | [**object**](.md)| 国家/Country | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get**
> fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get(tweet_id)

获取单个推文数据/Get single tweet data

# [中文] ### 用途: - 获取单个推文数据 ### 参数: - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的 1808168603721650364。 ### 返回: - 推文数据  # [English] ### Purpose: - Get single tweet data ### Parameters: - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364 ### Return: - Tweet data  # [示例/Example] tweet_id = \"1808168603721650364\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
tweet_id = NULL # object | 推文ID/Tweet ID

try:
    # 获取单个推文数据/Get single tweet data
    api_instance.fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get(tweet_id)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tweet_id** | [**object**](.md)| 推文ID/Tweet ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get**
> fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get(screen_name, cursor=cursor)

用户粉丝/User Followers

# [中文] ### 用途: - 获取用户粉丝 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 用户粉丝  # [English] ### Purpose: - Get User Followers ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - User Followers  # [示例/Example] screen_name = \"elonmusk\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
screen_name = NULL # object | 用户名/Screen Name
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 用户粉丝/User Followers
    api_instance.fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get(screen_name, cursor=cursor)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screen_name** | [**object**](.md)| 用户名/Screen Name | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get**
> fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get(screen_name, cursor=cursor)

用户关注/User Followings

# [中文] ### 用途: - 获取用户关注 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 用户关注  # [English] ### Purpose: - Get User Followings ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - User Followings  # [示例/Example] screen_name = \"elonmusk\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
screen_name = NULL # object | 用户名/Screen Name
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 用户关注/User Followings
    api_instance.fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get(screen_name, cursor=cursor)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screen_name** | [**object**](.md)| 用户名/Screen Name | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get**
> fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get(user_id, count=count, cursor=cursor)

获取用户高光推文/Get user highlights tweets

# [中文] ### 用途: - 获取用户高光推文 ### 参数: - userId: 用户ID - count: 数量，默认为20 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取     - JSONPath: $.data.data.user.result.timeline_v2.timeline.instructions.[1].entries.[-1].content.value ### 返回: - 用户高光推文  # [English] ### Purpose: - Get user highlights tweets ### Parameters: - userId: User ID - count: Count, default is 20 - cursor: Cursor, default is None, used for paging, obtained from the last request     - JSONPath: $.data.data.user.result.timeline_v2.timeline.instructions.[1].entries.[-1].content.value ### Return: - User highlights tweets  # [示例/Example] userId = \"44196397\" count = 20 cursor = None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
user_id = NULL # object | 用户ID/User ID
count = NULL # object | 数量/Count (optional)
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取用户高光推文/Get user highlights tweets
    api_instance.fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get(user_id, count=count, cursor=cursor)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户ID/User ID | 
 **count** | [**object**](.md)| 数量/Count | [optional] 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_media_api_v1_twitter_web_fetch_user_media_get**
> fetch_user_media_api_v1_twitter_web_fetch_user_media_get(screen_name, rest_id=rest_id, cursor=cursor)

获取用户媒体/Get user media

# [中文] ### 用途: - 获取用户媒体 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中的 `next_cursor` 获取 ### 返回: - 用户媒体  # [English] ### Purpose: - Get user media ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. - cursor: Cursor, default is None, used for paging, obtained from the `next_cursor` in the last request ### Return: - User media  # [示例/Example] screen_name = \"elonmusk\" cursor = \"\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
screen_name = NULL # object | 用户名/Screen Name
rest_id = NULL # object | 用户ID/User ID (optional)
cursor = NULL # object | 翻页游标/Page Cursor (optional)

try:
    # 获取用户媒体/Get user media
    api_instance.fetch_user_media_api_v1_twitter_web_fetch_user_media_get(screen_name, rest_id=rest_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_user_media_api_v1_twitter_web_fetch_user_media_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screen_name** | [**object**](.md)| 用户名/Screen Name | 
 **rest_id** | [**object**](.md)| 用户ID/User ID | [optional] 
 **cursor** | [**object**](.md)| 翻页游标/Page Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get**
> fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get(screen_name=screen_name, rest_id=rest_id, cursor=cursor)

获取用户发帖/Get user post

# [中文] ### 用途: - 获取用户发帖 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中的JSON中获取。 ### 返回: - 用户发帖  # [English] ### Purpose: - Get user post ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. - cursor: Cursor, default is None, used for paging, obtained from the JSON in the last request.  # [示例/Example] screen_name = \"elonmusk\" rest_id = 44196397 cursor = None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
screen_name = NULL # object | 用户名/Screen Name (optional)
rest_id = NULL # object | 用户ID/User ID (optional)
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取用户发帖/Get user post
    api_instance.fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get(screen_name=screen_name, rest_id=rest_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screen_name** | [**object**](.md)| 用户名/Screen Name | [optional] 
 **rest_id** | [**object**](.md)| 用户ID/User ID | [optional] 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get**
> fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get(screen_name=screen_name, rest_id=rest_id)

获取用户资料/Get user profile

# [中文] ### 用途: - 获取用户资料 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。 ### 返回: - 用户资料  # [English] ### Purpose: - Get user profile ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. ### Return: - User profile  # [示例/Example] screen_name = \"elonmusk\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
screen_name = NULL # object | 用户名/Screen Name (optional)
rest_id = NULL # object | 用户ID（如果使用用户ID则会忽略用户名）/User ID (If the user ID is used, the user name will be ignored) (optional)

try:
    # 获取用户资料/Get user profile
    api_instance.fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get(screen_name=screen_name, rest_id=rest_id)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screen_name** | [**object**](.md)| 用户名/Screen Name | [optional] 
 **rest_id** | [**object**](.md)| 用户ID（如果使用用户ID则会忽略用户名）/User ID (If the user ID is used, the user name will be ignored) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get**
> fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get(screen_name, cursor=cursor)

获取用户推文回复/Get user tweet replies

# [中文] ### 用途: - 获取用户推文回复 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 用户推文回复  # [English] ### Purpose: - Get user tweet replies ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - User tweet replies  # [示例/Example] screen_name = \"elonmusk\" cursor = None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWebAPIApi()
screen_name = NULL # object | 用户名/Screen Name
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取用户推文回复/Get user tweet replies
    api_instance.fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get(screen_name, cursor=cursor)
except ApiException as e:
    print("Exception when calling TwitterWebAPIApi->fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screen_name** | [**object**](.md)| 用户名/Screen Name | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

