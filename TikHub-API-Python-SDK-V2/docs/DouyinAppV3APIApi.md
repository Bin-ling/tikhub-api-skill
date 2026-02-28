# swagger_client.DouyinAppV3APIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get**](DouyinAppV3APIApi.md#add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get) | **GET** /api/v1/douyin/app/v3/add_video_play_count | 根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID
[**fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get**](DouyinAppV3APIApi.md#fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get) | **GET** /api/v1/douyin/app/v3/fetch_general_search_result | 获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
[**fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get**](DouyinAppV3APIApi.md#fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get) | **GET** /api/v1/douyin/app/v3/fetch_hashtag_detail | 获取指定话题的详情数据/Get details of specified hashtag
[**fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get**](DouyinAppV3APIApi.md#fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get) | **GET** /api/v1/douyin/app/v3/fetch_hashtag_search_result | 获取指定关键词的话题搜索结果（弃用，替代接口见下方文档说明）/Get hashtag search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
[**fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get**](DouyinAppV3APIApi.md#fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get) | **GET** /api/v1/douyin/app/v3/fetch_hashtag_video_list | 获取指定话题的作品数据/Get video list of specified hashtag
[**fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get**](DouyinAppV3APIApi.md#fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get) | **GET** /api/v1/douyin/app/v3/fetch_brand_hot_search_list_detail | 获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data
[**fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get**](DouyinAppV3APIApi.md#fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get) | **GET** /api/v1/douyin/app/v3/fetch_brand_hot_search_list | 获取抖音品牌热榜分类数据/Get Douyin brand hot search list data
[**fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get**](DouyinAppV3APIApi.md#fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get) | **GET** /api/v1/douyin/app/v3/fetch_hot_search_list | 获取抖音热搜榜数据/Get Douyin hot search list data
[**fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get**](DouyinAppV3APIApi.md#fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get) | **GET** /api/v1/douyin/app/v3/fetch_live_hot_search_list | 获取抖音直播热搜榜数据/Get Douyin live hot search list data
[**fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get**](DouyinAppV3APIApi.md#fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get) | **GET** /api/v1/douyin/app/v3/fetch_live_search_result | 获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
[**fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post**](DouyinAppV3APIApi.md#fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post) | **POST** /api/v1/douyin/app/v3/fetch_multi_video | 批量获取视频信息 V1/Batch Get Video Information V1
[**fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post**](DouyinAppV3APIApi.md#fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post) | **POST** /api/v1/douyin/app/v3/fetch_multi_video_high_quality_play_url | 批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos
[**fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get**](DouyinAppV3APIApi.md#fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get) | **GET** /api/v1/douyin/app/v3/fetch_multi_video_statistics | 根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)
[**fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post**](DouyinAppV3APIApi.md#fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post) | **POST** /api/v1/douyin/app/v3/fetch_multi_video_v2 | 批量获取视频信息 V2/Batch Get Video Information V2
[**fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get**](DouyinAppV3APIApi.md#fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get) | **GET** /api/v1/douyin/app/v3/fetch_music_detail | 获取指定音乐的详情数据/Get details of specified music
[**fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get**](DouyinAppV3APIApi.md#fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get) | **GET** /api/v1/douyin/app/v3/fetch_music_hot_search_list | 获取抖音音乐榜数据/Get Douyin music hot search list data
[**fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get**](DouyinAppV3APIApi.md#fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get) | **GET** /api/v1/douyin/app/v3/fetch_music_search_result | 获取指定关键词的音乐搜索结果（弃用，替代接口见下方文档说明）/Get music search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
[**fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get**](DouyinAppV3APIApi.md#fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get) | **GET** /api/v1/douyin/app/v3/fetch_music_video_list | 获取指定音乐的视频列表数据/Get video list of specified music
[**fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get**](DouyinAppV3APIApi.md#fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get) | **GET** /api/v1/douyin/app/v3/fetch_one_video | 获取单个作品数据/Get single video data
[**fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get**](DouyinAppV3APIApi.md#fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get) | **GET** /api/v1/douyin/app/v3/fetch_one_video_by_share_url | 根据分享链接获取单个作品数据/Get single video data by sharing link
[**fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get**](DouyinAppV3APIApi.md#fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get) | **GET** /api/v1/douyin/app/v3/fetch_share_info_by_share_code | 根据分享口令获取分享信息/Get share info by share code
[**fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get**](DouyinAppV3APIApi.md#fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get) | **GET** /api/v1/douyin/app/v3/fetch_one_video_v2 | 获取单个作品数据 V2/Get single video data V2
[**fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get**](DouyinAppV3APIApi.md#fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get) | **GET** /api/v1/douyin/app/v3/fetch_one_video_v3 | 获取单个作品数据 V3 (无版权限制)/Get single video data V3 (No copyright restrictions)
[**fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get**](DouyinAppV3APIApi.md#fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get) | **GET** /api/v1/douyin/app/v3/fetch_series_detail | 获取短剧详情信息/Get series detail
[**fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get**](DouyinAppV3APIApi.md#fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get) | **GET** /api/v1/douyin/app/v3/fetch_series_video_list | 获取短剧视频列表/Get series video list
[**fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get**](DouyinAppV3APIApi.md#fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get) | **GET** /api/v1/douyin/app/v3/fetch_user_fans_list | 获取用户粉丝列表/Get user fans list
[**fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get**](DouyinAppV3APIApi.md#fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get) | **GET** /api/v1/douyin/app/v3/fetch_user_following_list | 获取用户关注列表 (弃用，使用 /api/v1/douyin/web/fetch_user_following_list 替代)/Get user following list (Deprecated, use /api/v1/douyin/web/fetch_user_following_list instead)
[**fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get**](DouyinAppV3APIApi.md#fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get) | **GET** /api/v1/douyin/app/v3/fetch_user_like_videos | 获取用户喜欢作品数据/Get user like video data
[**fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get**](DouyinAppV3APIApi.md#fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get) | **GET** /api/v1/douyin/app/v3/fetch_user_post_videos | 获取用户主页作品数据/Get user homepage video data
[**fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get**](DouyinAppV3APIApi.md#fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get) | **GET** /api/v1/douyin/app/v3/fetch_user_search_result | 获取指定关键词的用户搜索结果（弃用，替代接口见下方文档说明）/Get user search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
[**fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get**](DouyinAppV3APIApi.md#fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get) | **GET** /api/v1/douyin/app/v3/fetch_user_series_list | 获取用户短剧合集列表/Get user series list
[**fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get**](DouyinAppV3APIApi.md#fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get) | **GET** /api/v1/douyin/app/v3/fetch_video_comments | 获取单个视频评论数据/Get single video comments data
[**fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get**](DouyinAppV3APIApi.md#fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get) | **GET** /api/v1/douyin/app/v3/fetch_video_comment_replies | 获取指定视频的评论回复数据/Get comment replies data of specified video
[**fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get**](DouyinAppV3APIApi.md#fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get) | **GET** /api/v1/douyin/app/v3/fetch_video_high_quality_play_url | 获取视频的最高画质播放链接/Get the highest quality play URL of the video
[**fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get**](DouyinAppV3APIApi.md#fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get) | **GET** /api/v1/douyin/app/v3/fetch_video_mix_detail | 获取抖音视频合集详情数据/Get Douyin video mix detail data
[**fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get**](DouyinAppV3APIApi.md#fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get) | **GET** /api/v1/douyin/app/v3/fetch_video_mix_post_list | 获取抖音视频合集作品列表数据/Get Douyin video mix post list data
[**fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get**](DouyinAppV3APIApi.md#fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get) | **GET** /api/v1/douyin/app/v3/fetch_video_search_result | 获取指定关键词的视频搜索结果（弃用，替代接口见下方文档说明）/Get video search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
[**fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get**](DouyinAppV3APIApi.md#fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get) | **GET** /api/v1/douyin/app/v3/fetch_video_search_result_v2 | 获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated, see the documentation below for alternative interfaces)
[**fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get**](DouyinAppV3APIApi.md#fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get) | **GET** /api/v1/douyin/app/v3/fetch_video_statistics | 根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)
[**generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get**](DouyinAppV3APIApi.md#generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get) | **GET** /api/v1/douyin/app/v3/generate_douyin_short_url | 生成抖音短链接/Generate Douyin short link
[**generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get**](DouyinAppV3APIApi.md#generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get) | **GET** /api/v1/douyin/app/v3/generate_douyin_video_share_qrcode | 生成抖音视频分享二维码/Generate Douyin video share QR code
[**handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get**](DouyinAppV3APIApi.md#handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get) | **GET** /api/v1/douyin/app/v3/handler_user_profile | 获取指定用户的信息/Get information of specified user
[**open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get**](DouyinAppV3APIApi.md#open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get) | **GET** /api/v1/douyin/app/v3/open_douyin_app_to_keyword_search | 生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result
[**open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get**](DouyinAppV3APIApi.md#open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get) | **GET** /api/v1/douyin/app/v3/open_douyin_app_to_send_private_message | 生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users
[**open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get**](DouyinAppV3APIApi.md#open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get) | **GET** /api/v1/douyin/app/v3/open_douyin_app_to_user_profile | 生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile
[**open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get**](DouyinAppV3APIApi.md#open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get) | **GET** /api/v1/douyin/app/v3/open_douyin_app_to_video_detail | 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page
[**register_device_api_v1_douyin_app_v3_register_device_get**](DouyinAppV3APIApi.md#register_device_api_v1_douyin_app_v3_register_device_get) | **GET** /api/v1/douyin/app/v3/register_device | 抖音APP注册设备/Douyin APP register device


# **add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get**
> add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get(aweme_type, item_id, cookie=cookie)

根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID

# [中文] ### 用途: - 根据视频ID来增加作品的播放数 - 该接口默认使用游客Cookie，如果需要使用登录用户的Cookie，请在参数中传入。 - 单一作品每次调用增加1次播放数，请求约 `1000` 次后会被抖音限制，需要等待一段时间（如：2小时后）后再继续调用。 - 该限制是针对作品的，不是针对接口的，在未登录的情况下，使用不同IP的浏览器或在APP中浏览作品，该作品的播放数也不会增加。 - 可以携带抖音网页端的Cookie来请求此接口，但是不保证一定有效，需要自行测试。 - 上述的限制是根据测试结果得出的，具体限制可能会有所不同，仅供参考。 ### 参数: - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。 - item_id: 作品id，别名为aweme_id - cookie: 可选，默认使用游客Cookie ### 返回: - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。  # [English] ### Purpose: - Increase the number of plays of the work according to the video ID - This interface uses guest Cookie by default. If you need to use the Cookie of the logged-in user, please pass it in the parameters. - Each call to a single work increases the number of plays by 1. After about `1000` calls, Douyin will restrict it. You need to wait for a period of time (such as 2 hours) before continuing to call. - This restriction is for the work, not for the interface. When browsing the work without logging in, using different IP browsers or browsing the work in the APP, the number of plays of the work will not increase. - You can carry the Cookie of the Douyin web page to request this interface, but it is not guaranteed to be effective and needs to be tested by yourself. - The above restrictions are based on test results, and the specific restrictions may vary, for reference only. ### Parameters: - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data interface. - item_id: Video id, alias aweme_id - cookie: Optional, use guest Cookie by default ### Return: - The current timestamp and status code. When the status code is 200, it means success, otherwise it is a failure. You can try to change another work id and call it again, or wait for a period of time and call it again.  # [示例/Example] aweme_type = 0 item_id = \"7197598285882789120\" cookie = None

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
aweme_type = NULL # object | 作品类型/Video type
item_id = NULL # object | 作品id/Video id
cookie = NULL # object | 可选，默认使用游客Cookie/Optional, use guest Cookie by default (optional)

try:
    # 根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID
    api_instance.add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get(aweme_type, item_id, cookie=cookie)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_type** | [**object**](.md)| 作品类型/Video type | 
 **item_id** | [**object**](.md)| 作品id/Video id | 
 **cookie** | [**object**](.md)| 可选，默认使用游客Cookie/Optional, use guest Cookie by default | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get**
> fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get(keyword, offset=offset, count=count, sort_type=sort_type, publish_time=publish_time, filter_duration=filter_duration, content_type=content_type)

获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated, see the documentation below for alternative interfaces)

# [中文] ### 用途: - 获取指定关键词的综合搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212773e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年 - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上 - content_type: 0:不限 1:视频 2:图片 3:文章 ### 返回: - 综合搜索结果  # [English] ### Purpose: - Get comprehensive search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212773e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes - content_type: 0: Unlimited 1: Video 2: Picture 3: Article ### Return: - Comprehensive search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = \"0\" publish_time = \"0\" filter_duration = \"0\" content_type = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
keyword = NULL # object | 关键词/Keyword
offset = NULL # object | 偏移量/Offset (optional)
count = NULL # object | 数量/Number (optional)
sort_type = NULL # object | 排序类型/Sort type (optional)
publish_time = NULL # object | 发布时间/Publish time (optional)
filter_duration = NULL # object | 时长/Duration (optional)
content_type = NULL # object | 内容类型/Content type (optional)

try:
    # 获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
    api_instance.fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get(keyword, offset=offset, count=count, sort_type=sort_type, publish_time=publish_time, filter_duration=filter_duration, content_type=content_type)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 关键词/Keyword | 
 **offset** | [**object**](.md)| 偏移量/Offset | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 
 **sort_type** | [**object**](.md)| 排序类型/Sort type | [optional] 
 **publish_time** | [**object**](.md)| 发布时间/Publish time | [optional] 
 **filter_duration** | [**object**](.md)| 时长/Duration | [optional] 
 **content_type** | [**object**](.md)| 内容类型/Content type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get**
> fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get(ch_id)

获取指定话题的详情数据/Get details of specified hashtag

# [中文] ### 用途: - 获取指定话题的详情数据 ### 参数: - ch_id: 话题id ### 返回: - 话题详情数据  # [English] ### Purpose: - Get details of specified hashtag ### Parameters: - ch_id: Hashtag id ### Return: - Hashtag details data  # [示例/Example] ch_id = 1575791821492238

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
ch_id = NULL # object | 话题id/Hashtag id

try:
    # 获取指定话题的详情数据/Get details of specified hashtag
    api_instance.fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get(ch_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ch_id** | [**object**](.md)| 话题id/Hashtag id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get**
> fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get(keyword, offset=offset, count=count)

获取指定关键词的话题搜索结果（弃用，替代接口见下方文档说明）/Get hashtag search results of specified keywords (deprecated, see the documentation below for alternative interfaces)

# [中文] ### 用途: - 获取指定关键词的话题搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212794e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 话题搜索结果  # [English] ### Purpose: - Get hashtag search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212794e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Hashtag search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
keyword = NULL # object | 关键词/Keyword
offset = NULL # object | 偏移量/Offset (optional)
count = NULL # object | 数量/Number (optional)

try:
    # 获取指定关键词的话题搜索结果（弃用，替代接口见下方文档说明）/Get hashtag search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
    api_instance.fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get(keyword, offset=offset, count=count)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 关键词/Keyword | 
 **offset** | [**object**](.md)| 偏移量/Offset | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get**
> fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get(ch_id, cursor=cursor, sort_type=sort_type, count=count)

获取指定话题的作品数据/Get video list of specified hashtag

# [中文] ### 用途: - 获取指定话题的作品数据 ### 参数: - ch_id: 话题id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 话题作品数据  # [English] ### Purpose: - Get video list of specified hashtag ### Parameters: - ch_id: Hashtag id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Hashtag video list data  # [示例/Example] ch_id = 1575791821492238 cursor = 0 sort_type = 0 count = 10

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
ch_id = NULL # object | 话题id/Hashtag id
cursor = NULL # object | 游标/Cursor (optional)
sort_type = NULL # object | 排序类型/Sort type (optional)
count = NULL # object | 数量/Number (optional)

try:
    # 获取指定话题的作品数据/Get video list of specified hashtag
    api_instance.fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get(ch_id, cursor=cursor, sort_type=sort_type, count=count)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ch_id** | [**object**](.md)| 话题id/Hashtag id | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 
 **sort_type** | [**object**](.md)| 排序类型/Sort type | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get**
> fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get(category_id)

获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data

# [中文] ### 用途: - 获取抖音品牌热榜具体分类数据 ### 参数: - category_id: 分类id ### 返回: - 品牌热搜榜具体分类数据  # [English] ### Purpose: - Get Douyin brand hot search list detail data ### Parameters: - category_id: Category id ### Return: - Hot brand search list detail data  # [示例/Example] category_id = 10

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
category_id = NULL # object | 分类id/Category id

try:
    # 获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data
    api_instance.fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get(category_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | [**object**](.md)| 分类id/Category id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get**
> fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get()

获取抖音品牌热榜分类数据/Get Douyin brand hot search list data

# [中文] ### 用途: - 获取抖音品牌热榜分类数据 ### 返回: - 品牌热搜榜分类数据  # [English] ### Purpose: - Get Douyin brand hot search category data ### Return: - Hot brand search category data  # [示例/Example] pass

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()

try:
    # 获取抖音品牌热榜分类数据/Get Douyin brand hot search list data
    api_instance.fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get()
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get: %s\n" % e)
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

# **fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get**
> fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get(board_type=board_type, board_sub_type=board_sub_type)

获取抖音热搜榜数据/Get Douyin hot search list data

# [中文] ### 用途: - 获取抖音热榜数据，包括：     - 热点榜     - 种草榜     - 娱乐榜     - 社会榜     - 挑战榜 ### 参数: - board_type:     - 0: 热点榜（默认）     - 2: 其他榜单，如种草榜等，需要传入对应的board_sub_type参数。 - board_sub_type:     - 空字符串: 热点榜（默认）     - seeding: 种草榜     - 2: 娱乐榜     - 4: 社会榜     - hotspot_challenge: 挑战榜 ### 返回: - 热搜榜数据  # [English] ### Purpose: - Get Douyin hot search list data, including:     - Hot search list     - Seeding list     - Entertainment list     - Social list     - Challenge list  ### Parameters: - board_type:     - 0: Hot search list (default)     - 2: Other lists, such as seeding list, etc., need to pass in the corresponding board_sub_type parameter. - board_sub_type:     - Empty string: Hot search list (default)     - seeding: Seeding list     - 2: Entertainment list     - 4: Social list     - hotspot_challenge: Challenge list ### Return: - Hot search list data  # [示例/Example] - 获取热点榜数据     - board_type = 0     - board_sub_type = \"\" - 获取种草榜数据     - board_type = 2     - board_sub_type = \"seeding\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
board_type = NULL # object | 榜单类型/Board type (optional)
board_sub_type = NULL # object | 榜单子类型/Board sub type (optional)

try:
    # 获取抖音热搜榜数据/Get Douyin hot search list data
    api_instance.fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get(board_type=board_type, board_sub_type=board_sub_type)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_type** | [**object**](.md)| 榜单类型/Board type | [optional] 
 **board_sub_type** | [**object**](.md)| 榜单子类型/Board sub type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get**
> fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get()

获取抖音直播热搜榜数据/Get Douyin live hot search list data

# [中文] ### 用途: - 获取抖音直播热搜榜数据 ### 返回: - 直播热搜榜数据  # [English] ### Purpose: - Get Douyin live hot search list data ### Return: - Live hot search list data  # [示例/Example] pass

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()

try:
    # 获取抖音直播热搜榜数据/Get Douyin live hot search list data
    api_instance.fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get()
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get: %s\n" % e)
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

# **fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get**
> fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get(keyword, cursor=cursor, count=count)

获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the documentation below for alternative interfaces)

# [中文] ### 用途: - 获取指定关键词的直播搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212789e0 ### 参数: - keyword: 关键词 - cursor: 偏移量，从0开始，每次请求从上次请求返回响应中的cursor中获取。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 直播搜索结果  # [English] ### Purpose: - Get live search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212789e0 ### Parameters: - keyword: Keyword - cursor: Offset, starting from 0, each request gets from the cursor in the response returned by the last request. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Live search results  # [示例/Example] keyword = \"小米商城\" cursor = 0 count = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
keyword = NULL # object | 关键词/Keyword
cursor = NULL # object | 偏移量/Offset (optional)
count = NULL # object | 数量/Number (optional)

try:
    # 获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
    api_instance.fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get(keyword, cursor=cursor, count=count)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 关键词/Keyword | 
 **cursor** | [**object**](.md)| 偏移量/Offset | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post**
> fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post()

批量获取视频信息 V1/Batch Get Video Information V1

# [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。 ### 参数: - aweme_ids: 作品id列表，最多支持10个作品id。 ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface charges a fixed price of 0.001$ * 10 = 0.01$ each time. ### Parameters: - aweme_ids: List of video ids, up to 10 video ids are supported. ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_ids = [\"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\"]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()

try:
    # 批量获取视频信息 V1/Batch Get Video Information V1
    api_instance.fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post()
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post: %s\n" % e)
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

# **fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post**
> fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post()

批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos

# [中文] ### 用途: - 此接口目前优惠活动价为$0.25，活动结束后恢复原价$0.5。不足50个视频按50个视频收费。 - 批量获取视频的最高画质(原始上传画质)播放链接 - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。 - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。 - 此接口非常适合用于批量获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。 - 使用并发请求，提高批量获取效率。 - 最多支持50个视频ID。 ### 参数: - aweme_ids: 作品id列表，用逗号分隔，例如: \"123,456,789\"，最多50个。 ### 返回: - total: 总数 - success_count: 成功数量 - failed_count: 失败数量 - videos: 视频列表，每个视频包含以下字段：     - video_id: 作品id     - original_video_url: 最高画质(原始上传画质)播放链接     - file_size: 文件大小（字节）     - file_size_in_mb: 文件大小（MB）     - content_type: 内容类型     - success: 是否成功     - error: 错误信息（如果失败） ### 备注: - 由于数量较多，处理时间可能会稍长，请增加等待时间。  # [English] ### Purpose: - This interface is currently on sale for $0.25, and will return to the original price of $0.5 after the event ends. If there are less than 50 videos, they will be charged as 50 videos. - Batch get the highest quality (original upload quality) play URL of videos - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata. - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface. - This interface is very suitable for batch obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc. - Use concurrent requests to improve batch acquisition efficiency. - Support up to 50 video IDs. ### Parameters: - aweme_ids: Video id list, separated by commas, for example: \"123,456,789\", up to 50. ### Return: - total: Total count - success_count: Success count - failed_count: Failed count - videos: Video list, each video contains the following fields:     - video_id: Video id     - original_video_url: Highest quality (original upload quality) play URL     - file_size: File size (bytes)     - file_size_in_mb: File size (MB)     - content_type: Content type     - success: Whether successful     - error: Error message (if failed) ### Note: - Due to the large number, the processing time may be slightly longer, please increase the waiting time. # [示例/Example] aweme_ids = \"7512756548356492544,7448118827402972455,7126745726494821640\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()

try:
    # 批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos
    api_instance.fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post()
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post: %s\n" % e)
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

# **fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get**
> fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get(aweme_ids)

根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)

# [中文] ### 用途: - 根据视频ID获取作品的统计数据，支持多个视频id，一次性最多支持50个视频。 - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。 - 价格为：0.025$一次。 - 可以获取到的统计有：     - 点赞数（digg_count）     - 下载数（download_count）     - 播放数（play_count）     - 分享数（share_count） ### 参数: - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过50个，单个也可以，则无需逗号。 ### 返回: - 作品统计数据  # [English] ### Purpose: - Get the statistical data of the Post according to the video ID, support multiple video ids, up to 50 videos at a time. - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be obtained through this interface. - Price: 0.025$ each time. - List of statistics that can be obtained:     - Like count (digg_count)     - Download count (download_count)     - Play count (play_count)     - Share count (share_count) ### Parameters: - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 50, single is also possible, no need for commas. ### Return: - Post statistics data  # [示例/Example] aweme_ids = \"7448118827402972455,7126745726494821640\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
aweme_ids = NULL # object | 作品id/Video id

try:
    # 根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)
    api_instance.fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get(aweme_ids)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_ids** | [**object**](.md)| 作品id/Video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post**
> fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post()

批量获取视频信息 V2/Batch Get Video Information V2

# [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持50个视频，此接口收费固定价格为0.001$ * 50 = 0.05$一次。 ### 参数: - aweme_ids: 作品id列表，最多支持50个作品id。 ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 50 videos at a time, this interface charges a fixed price of 0.001$ * 50 = 0.05$ each time. ### Parameters: - aweme_ids: List of video ids, up to 50 video ids are supported. ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_ids = [\"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\"]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()

try:
    # 批量获取视频信息 V2/Batch Get Video Information V2
    api_instance.fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post()
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post: %s\n" % e)
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

# **fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get**
> fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get(music_id)

获取指定音乐的详情数据/Get details of specified music

# [中文] ### 用途: - 获取指定音乐的详情数据 ### 参数: - music_id: 音乐id ### 返回: - 音乐详情数据  # [English] ### Purpose: - Get details of specified music ### Parameters: - music_id: Music id ### Return: - Music details data  # [示例/Example] music_id = \"7136850194742315016\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
music_id = NULL # object | 音乐id/Music id

try:
    # 获取指定音乐的详情数据/Get details of specified music
    api_instance.fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get(music_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **music_id** | [**object**](.md)| 音乐id/Music id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get**
> fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get(chart_type=chart_type, cursor=cursor)

获取抖音音乐榜数据/Get Douyin music hot search list data

# [中文] ### 用途: - 获取抖音音乐热榜数据 ### 参数: - chart_type: 榜单类型，默认值为'hot'，支持下面的值：     - 'hot': 热门榜     - 'trending': 飙升榜     - 'original': 原创榜 - cursor: 游标，默认值为'0'，用于分页获取数据，每次请求后会返回下一个游标值，并且通过 `has_more` 字段指示是否有更多数据可供获取。 ### 返回: - 音乐热搜榜数据  # [English] ### Purpose: - Get Douyin music hot search list data ### Parameters: - chart_type: Chart type, default value is 'hot', supports the following values:     - 'hot': Hot chart     - 'trending': Trending chart     - 'original': Original chart - cursor: Cursor, default value is '0', used for paginating data retrieval. After each request, the next cursor value will be returned, and the `has_more` field indicates whether there is more data available. ### Return: - Music hot search list data  # [示例/Example] chart_type = \"hot\" cursor = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
chart_type = NULL # object | 榜单类型/Chart type (optional)
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取抖音音乐榜数据/Get Douyin music hot search list data
    api_instance.fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get(chart_type=chart_type, cursor=cursor)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_type** | [**object**](.md)| 榜单类型/Chart type | [optional] 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get**
> fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get(keyword, offset=offset, count=count)

获取指定关键词的音乐搜索结果（弃用，替代接口见下方文档说明）/Get music search results of specified keywords (deprecated, see the documentation below for alternative interfaces)

# [中文] ### 用途: - 获取指定关键词的音乐搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212797e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 音乐搜索结果  # [English] ### Purpose: - Get music search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212797e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Music search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
keyword = NULL # object | 关键词/Keyword
offset = NULL # object | 偏移量/Offset (optional)
count = NULL # object | 数量/Number (optional)

try:
    # 获取指定关键词的音乐搜索结果（弃用，替代接口见下方文档说明）/Get music search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
    api_instance.fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get(keyword, offset=offset, count=count)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 关键词/Keyword | 
 **offset** | [**object**](.md)| 偏移量/Offset | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get**
> fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get(music_id, cursor=cursor, count=count)

获取指定音乐的视频列表数据/Get video list of specified music

# [中文] ### 用途: - 获取指定音乐的视频列表数据 ### 参数: - music_id: 音乐id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 音乐视频列表数据  # [English] ### Purpose: - Get video list of specified music ### Parameters: - music_id: Music id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Music video list data  # [示例/Example] music_id = \"7136850194742315016\" cursor = 0 count = 10

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
music_id = NULL # object | 音乐id/Music id
cursor = NULL # object | 游标/Cursor (optional)
count = NULL # object | 数量/Number (optional)

try:
    # 获取指定音乐的视频列表数据/Get video list of specified music
    api_instance.fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get(music_id, cursor=cursor, count=count)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **music_id** | [**object**](.md)| 音乐id/Music id | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get**
> fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get(aweme_id)

获取单个作品数据/Get single video data

# [中文] ### 用途: - 获取单个作品数据，支持图文、视频等。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Get single video data, support photo, video, etc. ### Parameters: - aweme_id: Video id ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_id = \"7448118827402972455\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
aweme_id = NULL # object | 作品id/Video id

try:
    # 获取单个作品数据/Get single video data
    api_instance.fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get(aweme_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | [**object**](.md)| 作品id/Video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get**
> fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get(share_url)

根据分享链接获取单个作品数据/Get single video data by sharing link

# [中文] ### 用途: - 根据分享链接获取单个作品数据 ### 参数: - share_url: 分享链接 ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Get single video data by sharing link ### Parameters: - share_url: Share link ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] share_url = \"https://v.douyin.com/e3x2fjE/\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
share_url = NULL # object | 分享链接/Share link

try:
    # 根据分享链接获取单个作品数据/Get single video data by sharing link
    api_instance.fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get(share_url)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_url** | [**object**](.md)| 分享链接/Share link | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get**
> fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get(share_code)

根据分享口令获取分享信息/Get share info by share code

# [中文] ### 用途: - 根据分享口令获取分享信息，比如抖音文章的分享口令提取分享人信息和文章ID等然后再去请求单一作品数据接口获取文章内容。 ### 参数: - share_code: 分享口令 ### 返回: - 分享信息，包含分享人信息和文章ID等  # [English] ### Purpose: - Get share info by share code, such as extracting sharer information and article ID from Douyin article share code, and then requesting a single video data interface to get the article content. ### Parameters: - share_code: Share code ### Return: - Share info, including sharer information and article ID, etc.  # [示例/Example] share_code = \"8:/ h@O.kP 05/21 【生意场上，装逼就是节省沟通成本】长按复制打开抖音，即可阅读文章 ︽︽2QnCB9aIZZ29︽︽\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
share_code = NULL # object | 分享口令/Share code

try:
    # 根据分享口令获取分享信息/Get share info by share code
    api_instance.fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get(share_code)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_code** | [**object**](.md)| 分享口令/Share code | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get**
> fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get(aweme_id)

获取单个作品数据 V2/Get single video data V2

# [中文] ### 用途: - 获取单个作品数据，支持图文、视频等。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Get single video data, support photo, video, etc. ### Parameters: - aweme_id: Video id ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_id = \"7448118827402972455\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
aweme_id = NULL # object | 作品id/Video id

try:
    # 获取单个作品数据 V2/Get single video data V2
    api_instance.fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get(aweme_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | [**object**](.md)| 作品id/Video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get**
> fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get(aweme_id)

获取单个作品数据 V3 (无版权限制)/Get single video data V3 (No copyright restrictions)

# [中文] ### 用途: - 获取单个作品数据，支持文章、图文、视频等。 - V3版本的接口，解决了版权限制问题，可以获取更多受限内容，比如 V1，V2版本返回的Reason为8的内容和部分文章或短剧等。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data, support article, photo, video, etc. - V3 version of the interface, which solves the copyright restriction problem and can obtain more restricted content, such as content with Reason 8 returned by V1 and V2 versions and some articles or short dramas. ### Parameters: - aweme_id: Video id ### Return: - Video data  # [示例/Example] aweme_id = \"7592116912205630761\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
aweme_id = NULL # object | 作品或文章ID/Video or Article ID

try:
    # 获取单个作品数据 V3 (无版权限制)/Get single video data V3 (No copyright restrictions)
    api_instance.fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get(aweme_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | [**object**](.md)| 作品或文章ID/Video or Article ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get**
> fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get(series_id)

获取短剧详情信息/Get series detail

# [中文] ### 用途: - 获取短剧详情信息 ### 参数: - series_id: 短剧id ### 返回: - 短剧详情数据 ### 备注: - 该接口返回短剧的详细信息，包括：     - 短剧名称、描述、封面     - 作者信息     - 总集数、更新状态     - 播放量、收藏量等统计数据     - 付费信息（如有）  # [English] ### Purpose: - Get series/playlet detail information ### Parameters: - series_id: Series id ### Return: - Series detail data ### Note: - This interface returns detailed information of the series, including:     - Series name, description, cover     - Author information     - Total episodes, update status     - Play count, collection count and other statistics     - Payment information (if any)  # [示例/Example] series_id = \"7592054624643713067\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
series_id = NULL # object | 短剧id/Series id

try:
    # 获取短剧详情信息/Get series detail
    api_instance.fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get(series_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | [**object**](.md)| 短剧id/Series id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get**
> fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get(series_id, cursor=cursor)

获取短剧视频列表/Get series video list

# [中文] ### 用途: - 获取短剧视频列表 ### 参数: - series_id: 短剧id - cursor: 游标，用于翻页，第一页为0，第二页通常为count的值（如15）。 ### 返回: - 短剧视频列表数据 ### 备注: - 该接口返回短剧中的所有视频列表 - 响应中的 aweme_list 包含短剧的各集视频信息 - has_more 字段表示是否还有更多数据  # [English] ### Purpose: - Get series/playlet video list ### Parameters: - series_id: Series id - cursor: Cursor, used for paging, the first page is 0, the second page is usually the value of count (e.g., 15). ### Return: - Series video list data ### Note: - This interface returns all video list in the series - The aweme_list in the response contains video information of each episode - The has_more field indicates whether there is more data  # [示例/Example] series_id = \"7592054624643713067\" cursor = 0

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
series_id = NULL # object | 短剧id/Series id
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取短剧视频列表/Get series video list
    api_instance.fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get(series_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | [**object**](.md)| 短剧id/Series id | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get**
> fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get(sec_user_id=sec_user_id, max_time=max_time, count=count)

获取用户粉丝列表/Get user fans list

# [中文] ### 用途: - 获取用户粉丝列表 ### 参数: - sec_user_id: 用户sec_user_id - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。 - count: 数量，默认为20，建议保持不变。 ### 返回: - 粉丝列表  # [English] ### Purpose: - Get user fans list ### Parameters: - sec_user_id: User sec_user_id - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging. - count: Number, default is 20, it is recommended to keep it unchanged. ### Return: - Fans list  # [示例/Example] sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\" max_time = \"0\" count = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
sec_user_id = NULL # object | 用户sec_user_id/User sec_user_id (optional)
max_time = NULL # object | 最大时间戳/Maximum timestamp (optional)
count = NULL # object | 数量/Number (optional)

try:
    # 获取用户粉丝列表/Get user fans list
    api_instance.fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get(sec_user_id=sec_user_id, max_time=max_time, count=count)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sec_user_id** | [**object**](.md)| 用户sec_user_id/User sec_user_id | [optional] 
 **max_time** | [**object**](.md)| 最大时间戳/Maximum timestamp | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get**
> fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get(sec_user_id=sec_user_id, max_time=max_time, count=count)

获取用户关注列表 (弃用，使用 /api/v1/douyin/web/fetch_user_following_list 替代)/Get user following list (Deprecated, use /api/v1/douyin/web/fetch_user_following_list instead)

# [中文] ### 用途: - 获取用户关注列表 ### 参数: - sec_user_id: 用户sec_user_id - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。 - count: 数量，默认为20，建议保持不变。 ### 返回: - 关注列表  # [English] ### Purpose: - Get user following list ### Parameters: - sec_user_id: User sec_user_id - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging. - count: Number, default is 20, it is recommended to keep it unchanged. ### Return: - Following list  # [示例/Example] sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\" max_time = \"0\" count = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
sec_user_id = NULL # object | 用户sec_user_id/User sec_user_id (optional)
max_time = NULL # object | 最大时间戳/Maximum timestamp (optional)
count = NULL # object | 数量/Number (optional)

try:
    # 获取用户关注列表 (弃用，使用 /api/v1/douyin/web/fetch_user_following_list 替代)/Get user following list (Deprecated, use /api/v1/douyin/web/fetch_user_following_list instead)
    api_instance.fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get(sec_user_id=sec_user_id, max_time=max_time, count=count)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sec_user_id** | [**object**](.md)| 用户sec_user_id/User sec_user_id | [optional] 
 **max_time** | [**object**](.md)| 最大时间戳/Maximum timestamp | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get**
> fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get(sec_user_id, max_cursor=max_cursor, counts=counts)

获取用户喜欢作品数据/Get user like video data

# [中文] ### 用途: - 获取用户喜欢作品数据 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user like video data ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\" max_cursor = 0 counts = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
sec_user_id = NULL # object | 用户sec_user_id/User sec_user_id
max_cursor = NULL # object | 最大游标/Maximum cursor (optional)
counts = NULL # object | 每页数量/Number per page (optional)

try:
    # 获取用户喜欢作品数据/Get user like video data
    api_instance.fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get(sec_user_id, max_cursor=max_cursor, counts=counts)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sec_user_id** | [**object**](.md)| 用户sec_user_id/User sec_user_id | 
 **max_cursor** | [**object**](.md)| 最大游标/Maximum cursor | [optional] 
 **counts** | [**object**](.md)| 每页数量/Number per page | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get**
> fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get(sec_user_id, max_cursor=max_cursor, count=count, sort_type=sort_type)

获取用户主页作品数据/Get user homepage video data

# [中文] ### 用途: - 获取用户主页作品数据 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量，不要超过20，建议保持不变。 - sort_type: 排序类型，可选值如下：     - `0`: 最新排序-默认     - `1`: 最热排序 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number, do not exceed 20, it is recommended to keep it unchanged. - sort_type: Sort type, optional values are as follows:     - `0`: Latest sorting - default     - `1`: Hottest sorting ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\" max_cursor = 0 counts = 20 sort_type = 0

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
sec_user_id = NULL # object | 用户sec_user_id/User sec_user_id
max_cursor = NULL # object | 最大游标/Maximum cursor (optional)
count = NULL # object | 每页数量/Number per page (optional)
sort_type = NULL # object | 排序类型/Sort type (optional)

try:
    # 获取用户主页作品数据/Get user homepage video data
    api_instance.fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get(sec_user_id, max_cursor=max_cursor, count=count, sort_type=sort_type)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sec_user_id** | [**object**](.md)| 用户sec_user_id/User sec_user_id | 
 **max_cursor** | [**object**](.md)| 最大游标/Maximum cursor | [optional] 
 **count** | [**object**](.md)| 每页数量/Number per page | [optional] 
 **sort_type** | [**object**](.md)| 排序类型/Sort type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get**
> fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get(keyword, offset=offset, count=count, douyin_user_fans=douyin_user_fans, douyin_user_type=douyin_user_type)

获取指定关键词的用户搜索结果（弃用，替代接口见下方文档说明）/Get user search results of specified keywords (deprecated, see the documentation below for alternative interfaces)

# [中文] ### 用途: - 获取指定关键词的用户搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212785e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 - douyin_user_fans(粉丝数量):     - \"\": 不限     - \"0_1k\": 1000以下     - \"1k_1w\": 1000-1万     - \"1w_10w\": 1w-10w     - \"10w_100w\": 10w-100w     - \"100w_\": 100w以上 - douyin_user_type(用户类型，请使用英文而不是中文):     - \"\": 不限     - \"common_user\": 普通用户     - \"enterprise_user\": 企业认证     - \"personal_user\": 个人认证 ### 返回: - 用户搜索结果  # [English] ### Purpose: - Get user search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212785e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. - douyin_user_fans(Fans):     - \"\": Unlimited     - \"0_1k\": Less than 1000     - \"1k_1w\": 1000-10,000     - \"1w_10w\": 10,000-100,000     - \"10w_100w\": 100,000-1,000,000     - \"100w_\": More than 1,000,000 - douyin_user_type(User type, please use English instead of Chinese):     - \"\": Unlimited     - \"common_user\": Common user     - \"enterprise_user\": Enterprise certification     - \"personal_user\": Personal certification ### Return: - User search results  # [示例/Example] keyword = \"动漫\" offset = 0 count = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
keyword = NULL # object | 关键词/Keyword
offset = NULL # object | 偏移量/Offset (optional)
count = NULL # object | 数量/Number (optional)
douyin_user_fans = NULL # object | 粉丝数/Fans (optional)
douyin_user_type = NULL # object | 用户类型/User type (optional)

try:
    # 获取指定关键词的用户搜索结果（弃用，替代接口见下方文档说明）/Get user search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
    api_instance.fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get(keyword, offset=offset, count=count, douyin_user_fans=douyin_user_fans, douyin_user_type=douyin_user_type)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 关键词/Keyword | 
 **offset** | [**object**](.md)| 偏移量/Offset | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 
 **douyin_user_fans** | [**object**](.md)| 粉丝数/Fans | [optional] 
 **douyin_user_type** | [**object**](.md)| 用户类型/User type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get**
> fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get(user_id=user_id, sec_user_id=sec_user_id, cursor=cursor)

获取用户短剧合集列表/Get user series list

# [中文] ### 用途: - 获取用户的短剧合集列表 ### 参数: - user_id: 用户id，与sec_user_id二选一即可 - sec_user_id: 用户加密id，与user_id二选一即可 - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 ### 返回: - 用户短剧合集列表数据 ### 备注: - 该接口返回用户发布的所有短剧合集 - 响应中的 series_id 可用于获取短剧详情和视频列表  # [English] ### Purpose: - Get user's series/playlet collection list ### Parameters: - user_id: User id - sec_user_id: User encrypted id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. ### Return: - User series list data ### Note: - This interface returns all series collections published by the user - The series_id in the response can be used to get series details and video list  # [示例/Example] user_id = \"3010877781453635\" sec_user_id = \"MS4wLjABAAAAfAU5kMk-W4569G1z2iRsy8t6-kOxO17Eaz6yte4NQokeUeOpeqTGEc480e34O8lK\" cursor = 0

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
user_id = NULL # object | 用户id/User id (optional)
sec_user_id = NULL # object | 用户加密id/User sec id (optional)
cursor = NULL # object | 游标/Cursor (optional)

try:
    # 获取用户短剧合集列表/Get user series list
    api_instance.fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get(user_id=user_id, sec_user_id=sec_user_id, cursor=cursor)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| 用户id/User id | [optional] 
 **sec_user_id** | [**object**](.md)| 用户加密id/User sec id | [optional] 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get**
> fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get(aweme_id, cursor=cursor, count=count)

获取单个视频评论数据/Get single video comments data

# [中文] ### 用途: - 获取单个视频评论数据 ### 参数: - aweme_id: 作品id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 评论数据  # [English] ### Purpose: - Get single video comments data ### Parameters: - aweme_id: Video id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Comments data  # [示例/Example] aweme_id = \"7448118827402972455\" cursor = 0 count = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
aweme_id = NULL # object | 作品id/Video id
cursor = NULL # object | 游标/Cursor (optional)
count = NULL # object | 数量/Number (optional)

try:
    # 获取单个视频评论数据/Get single video comments data
    api_instance.fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get(aweme_id, cursor=cursor, count=count)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | [**object**](.md)| 作品id/Video id | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get**
> fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get(item_id, comment_id, cursor=cursor, count=count)

获取指定视频的评论回复数据/Get comment replies data of specified video

# [中文] ### 用途: - 获取指定视频的评论回复数据 ### 参数: - item_id: 作品id - comment_id: 评论id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 评论回复数据  # [English] ### Purpose: - Get comment replies data of specified video ### Parameters: - item_id: Video id - comment_id: Comment id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Comment replies data  # [示例/Example] aweme_id = \"7354666303006723354\" comment_id = \"7354669356632638218\" cursor = 0 count = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
item_id = NULL # object | 作品id/Video id
comment_id = NULL # object | 评论id/Comment id
cursor = NULL # object | 游标/Cursor (optional)
count = NULL # object | 数量/Number (optional)

try:
    # 获取指定视频的评论回复数据/Get comment replies data of specified video
    api_instance.fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get(item_id, comment_id, cursor=cursor, count=count)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**object**](.md)| 作品id/Video id | 
 **comment_id** | [**object**](.md)| 评论id/Comment id | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get**
> fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get(aweme_id=aweme_id, share_url=share_url)

获取视频的最高画质播放链接/Get the highest quality play URL of the video

# [中文] ### 用途: - 价格：0.005$ 一次。 - 获取视频的最高画质(原始上传画质)播放链接 - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。 - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。 - 此接口非常适合用于获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。 - 一般情况都可以在线播放，如果不行，可以尝试使用IDM或浏览器下载后播放。 ### 参数: - aweme_id: 作品id，优先使用aweme_id，如果没有则使用share_url。 - share_url: 可选，分享链接，如果提供了作品id，则此参数可以不传。 ### 返回: - video_id： 作品id - original_video_url： 最高画质(原始上传画质)播放链接 - video_data： 视频数据，包含视频的元数据，如时长、大小等。  # [English] ### Purpose: - Price: 0.005$ each time. - Get the highest quality (original upload quality) play URL of the video - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata. - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface. - This interface is very suitable for obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc. - Generally, it can be played online, if not, you can try to download it using IDM or a browser and then play it. ### Parameters: - aweme_id: Video id, prefer to use aweme_id, if not available, use share_url. - share_url: Optional, share link, if the video id is provided, this parameter can be omitted. ### Return: - video_id: Video id - original_video_url: Highest quality (original upload quality) play URL - video_data: Video data, including metadata such as duration, size, etc. # [示例/Example] aweme_id = \"7512756548356492544\" share_url = \"https://www.douyin.com/video/7512756548356492544\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
aweme_id = NULL # object | 作品id/Video id (optional)
share_url = NULL # object | 可选，分享链接/Optional, share link (optional)

try:
    # 获取视频的最高画质播放链接/Get the highest quality play URL of the video
    api_instance.fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get(aweme_id=aweme_id, share_url=share_url)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | [**object**](.md)| 作品id/Video id | [optional] 
 **share_url** | [**object**](.md)| 可选，分享链接/Optional, share link | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get**
> fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get(mix_id)

获取抖音视频合集详情数据/Get Douyin video mix detail data

# [中文] ### 用途: - 获取抖音视频合集详情数据 ### 参数: - mix_id: 合集id ### 返回: - 视频合集详情数据  # [English] ### Purpose: - Get Douyin video mix detail data ### Parameters: - mix_id: Mix id ### Return: - Video mix detail data  # [示例/Example] mix_id = \"7302011174286002217\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
mix_id = NULL # object | 合集id/Mix id

try:
    # 获取抖音视频合集详情数据/Get Douyin video mix detail data
    api_instance.fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get(mix_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mix_id** | [**object**](.md)| 合集id/Mix id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get**
> fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get(mix_id, cursor=cursor, count=count)

获取抖音视频合集作品列表数据/Get Douyin video mix post list data

# [中文] ### 用途: - 获取抖音视频合集作品列表数据 ### 参数: - mix_id: 合集id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 视频合集作品列表数据  # [English] ### Purpose: - Get Douyin video mix post list data ### Parameters: - mix_id: Mix id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Video mix post list data  # [示例/Example] mix_id = \"7302011174286002217\" cursor = 0 count = 20

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
mix_id = NULL # object | 合集id/Mix id
cursor = NULL # object | 游标/Cursor (optional)
count = NULL # object | 数量/Number (optional)

try:
    # 获取抖音视频合集作品列表数据/Get Douyin video mix post list data
    api_instance.fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get(mix_id, cursor=cursor, count=count)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mix_id** | [**object**](.md)| 合集id/Mix id | 
 **cursor** | [**object**](.md)| 游标/Cursor | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get**
> fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get(keyword, offset=offset, count=count, sort_type=sort_type, publish_time=publish_time, filter_duration=filter_duration)

获取指定关键词的视频搜索结果（弃用，替代接口见下方文档说明）/Get video search results of specified keywords (deprecated, see the documentation below for alternative interfaces)

# [中文] ### 用途: - 获取指定关键词的视频搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212780e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年 - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上 - content_type: 0:不限 1:视频 2:图文 ### 返回: - 视频搜索结果  # [English] ### Purpose: - Get video search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212780e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes - content_type: 0: Unlimited 1: Video 2: Graphic and text ### Return: - Video search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = \"0\" publish_time = \"0\" filter_duration = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
keyword = NULL # object | 关键词/Keyword
offset = NULL # object | 偏移量/Offset (optional)
count = NULL # object | 数量/Number (optional)
sort_type = NULL # object | 排序类型/Sort type (optional)
publish_time = NULL # object | 发布时间/Publish time (optional)
filter_duration = NULL # object | 时长/Duration (optional)

try:
    # 获取指定关键词的视频搜索结果（弃用，替代接口见下方文档说明）/Get video search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
    api_instance.fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get(keyword, offset=offset, count=count, sort_type=sort_type, publish_time=publish_time, filter_duration=filter_duration)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 关键词/Keyword | 
 **offset** | [**object**](.md)| 偏移量/Offset | [optional] 
 **count** | [**object**](.md)| 数量/Number | [optional] 
 **sort_type** | [**object**](.md)| 排序类型/Sort type | [optional] 
 **publish_time** | [**object**](.md)| 发布时间/Publish time | [optional] 
 **filter_duration** | [**object**](.md)| 时长/Duration | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get**
> fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get(keyword, sort_type=sort_type, publish_time=publish_time, filter_duration=filter_duration, page=page, search_id=search_id)

获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated, see the documentation below for alternative interfaces)

# [中文] ### 用途: - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。 - 收费标准为：0.01$每次请求。 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212780e0 ### 参数: - keyword: 关键词 - sort_type:     - 排序类型，可用值如下：     - _0 :综合(General)     - _1 :最多点赞(More likes)     - _2 :最新发布(New) - publish_time：     - 发布时间，可用值如下：     - _0 :不限(No Limit)     - _1 :一天之内(last 1 day)     - _7 :一周之内(last 1 week)     - _180 :半年之内(last half year) - filter_duration：     - 视频时长，可用值如下：     - _0 :不限(No Limit)     - _1 :1分钟以下(1 minute and below)     - _2 :1-5分钟 (1-5 minutes)     - _3 :5分钟以上(5 minutes more) - page: 页码     - 默认从1开始，然后依次递增加1 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 视频搜索结果V2  # [English] ### Purpose: - Get video search results of specified keywords V2, this interface has better stability and higher cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is recommended to use this interface. - The charging standard is: $0.01 per request. - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212780e0 ### Parameters: - keyword: Keyword - sort_type:     - Sort type, available values are as follows:     - _0 : General     - _1 : More likes     - _2 : New - publish_time:     - Publish time, available values are as follows:     - _0 : No Limit     - _1 : last 1 day     - _7 : last 1 week     - _180 : last half year - filter_duration:     - Duration filter, available values are as follows:     - _0 : No Limit     - _1 : 1 minute and below     - _2 : 1-5 minutes     - _3 : 5 minutes more - page: Page     - Start from 1 by default, then increase by 1 each time - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - Video search results V2  # [示例/Example] keyword = \"中华娘\" sort_type = \"_0\" publish_time = \"_0\" filter_duration = \"_0\" page = 1 search_id = \"\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
keyword = NULL # object | 关键词/Keyword
sort_type = NULL # object | 排序类型/Sort type (optional)
publish_time = NULL # object | 发布时间/Publish time (optional)
filter_duration = NULL # object | 视频时长/Duration filter (optional)
page = NULL # object | 页码/Page (optional)
search_id = NULL # object | 搜索id，翻页时需要提供/Search id, need to provide when paging (optional)

try:
    # 获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated, see the documentation below for alternative interfaces)
    api_instance.fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get(keyword, sort_type=sort_type, publish_time=publish_time, filter_duration=filter_duration, page=page, search_id=search_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 关键词/Keyword | 
 **sort_type** | [**object**](.md)| 排序类型/Sort type | [optional] 
 **publish_time** | [**object**](.md)| 发布时间/Publish time | [optional] 
 **filter_duration** | [**object**](.md)| 视频时长/Duration filter | [optional] 
 **page** | [**object**](.md)| 页码/Page | [optional] 
 **search_id** | [**object**](.md)| 搜索id，翻页时需要提供/Search id, need to provide when paging | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get**
> fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get(aweme_ids)

根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)

# [中文] ### 用途: - 根据视频ID获取作品的统计数据 - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。 - 可以获取到的统计有：     - 点赞数（digg_count）     - 下载数（download_count）     - 播放数（play_count）     - 分享数（share_count） ### 参数: - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过2个，单个也可以，则无需逗号。 ### 返回: - 作品统计数据  # [English] ### Purpose: - Get the statistical data of the Post according to the video ID - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be obtained through this interface. - List of statistics that can be obtained:     - Like count (digg_count)     - Download count (download_count)     - Play count (play_count)     - Share count (share_count) ### Parameters: - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 2, single is also possible, no need for commas. ### Return: - Post statistics data  # [示例/Example] aweme_ids = \"7448118827402972455,7126745726494821640\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
aweme_ids = NULL # object | 作品id/Video id

try:
    # 根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)
    api_instance.fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get(aweme_ids)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_ids** | [**object**](.md)| 作品id/Video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get**
> generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get(url)

生成抖音短链接/Generate Douyin short link

# [中文] ### 用途: - 生成抖音短链接 ### 参数: - url: 抖音链接 ### 返回: - 短链接数据  # [English] ### Purpose: - Generate Douyin short link ### Parameters: - url: Douyin link ### Return: - Short link data  # [示例/Example] url = \"https://www.douyin.com/passport/web/logout/\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
url = NULL # object | 抖音链接/Douyin link

try:
    # 生成抖音短链接/Generate Douyin short link
    api_instance.generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get(url)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)| 抖音链接/Douyin link | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get**
> generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get(object_id)

生成抖音视频分享二维码/Generate Douyin video share QR code

# [中文] ### 用途: - 生成抖音视频分享二维码 ### 参数: - object_id: 作品id或作者uid ### 返回: - 二维码数据  # [English] ### Purpose: - Generate Douyin video share QR code ### Parameters: - object_id: Video id or author uid ### Return: - QR code data  # [示例/Example] object_id = \"7348044435755846962\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
object_id = NULL # object | 作品id/Video id

try:
    # 生成抖音视频分享二维码/Generate Douyin video share QR code
    api_instance.generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get(object_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | [**object**](.md)| 作品id/Video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get**
> handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get(sec_user_id)

获取指定用户的信息/Get information of specified user

# [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id ### Return: - User information  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
sec_user_id = NULL # object | 用户sec_user_id/User sec_user_id

try:
    # 获取指定用户的信息/Get information of specified user
    api_instance.handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get(sec_user_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sec_user_id** | [**object**](.md)| 用户sec_user_id/User sec_user_id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get**
> open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get(keyword)

生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result

# [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果。  ### 参数: - keyword: 关键词  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result  ### Parameters: - keyword: Keyword  ### Return: - Share link  # [示例/Example] keyword = \"雷军\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
keyword = NULL # object | 关键词/Keyword

try:
    # 生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result
    api_instance.open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get(keyword)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | [**object**](.md)| 关键词/Keyword | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get**
> open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get(uid, sec_uid)

生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users

# [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，给指定用户发送私信。  ### 参数: - uid: 用户id - sec_uid: 用户sec_uid - 注意: 请确保user_id和sec_uid都有值，否则无法发送私信给指定用户。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and send private messages to specified users  ### Parameters: - uid: User id - sec_uid: User sec_uid - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot send private messages to the specified user.  ### Return: - Share link  # [示例/Example] uid = \"96874812426\" sec_uid = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
uid = NULL # object | 用户id/User id
sec_uid = NULL # object | 用户sec_uid/User sec_uid

try:
    # 生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users
    api_instance.open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get(uid, sec_uid)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | [**object**](.md)| 用户id/User id | 
 **sec_uid** | [**object**](.md)| 用户sec_uid/User sec_uid | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get**
> open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get(uid, sec_uid)

生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile

# [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，跳转指定用户主页。  ### 参数: - uid: 用户id - sec_uid: 用户sec_uid - 注意: 请确保user_id和sec_uid都有值，否则无法跳转到指定用户主页。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and jump to the specified user profile  ### Parameters: - uid: User id - sec_uid: User sec_uid - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot jump to the specified user profile.  ### Return: - Share link  # [示例/Example] uid = \"96874812426\" sec_uid = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
uid = NULL # object | 用户id/User id
sec_uid = NULL # object | 用户sec_uid/User sec_uid

try:
    # 生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile
    api_instance.open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get(uid, sec_uid)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | [**object**](.md)| 用户id/User id | 
 **sec_uid** | [**object**](.md)| 用户sec_uid/User sec_uid | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get**
> open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get(aweme_id)

生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page

# [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页。  ### 参数: - aweme_id: 作品id  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and jump to the specified video  ### Parameters: - aweme_id: Video id  ### Return: - Share link  # [示例/Example] aweme_id = \"7197598285882789120\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
aweme_id = NULL # object | 作品id/Video id

try:
    # 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page
    api_instance.open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get(aweme_id)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | [**object**](.md)| 作品id/Video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_device_api_v1_douyin_app_v3_register_device_get**
> register_device_api_v1_douyin_app_v3_register_device_get(proxy=proxy)

抖音APP注册设备/Douyin APP register device

# [中文] ### 用途: - 抖音APP注册设备，获取设备信息以及设备的Cookie信息。  ### 参数: - proxy: 代理，要带http://或https://，仅支持http代理。   - 格式: username:password@ip:port  ### 返回: - 设备信息以及设备的Cookie信息。  # [English] ### Purpose: - Register device in Douyin APP, retrieve device information and device cookies.  ### Parameters: - proxy: Proxy, with http:// or https://, only supports http proxies.   - Format: username:password@ip:port  ### Return: - Device information and device cookies.  # [示例/Example] proxy = \"http://username:password@ip:port\"  # [响应/Response] ```json {     \"code\": 200,     \"router\": \"/api/v1/douyin/app/v3/register_device\",     \"params\": {         \"proxy\": \"username:password@ip:port\"     },     \"data\": {         \"iid\": \"3631064037200330\",         \"device_id\": \"3631064037196234\",         \"mssdk_token\": \"\",         \"device_platform\": \"android\",         \"channel\": \"xiaomi_64_1775\",         \"version_code\": 240900,         \"version_name\": \"24.9.0\",         \"manifest_version_code\": 240901,         \"update_version_code\": 24909900,         \"device_type\": \"V1963A\",         \"device_brand\": \"vivo\",         \"device_model\": \"V1963A\",         \"openudid\": \"5d736335afc17aab\",         \"os_api\": 29,         \"os_version\": \"10\",         \"resolution\": \"2400x1080\",         \"dpi\": 480,         \"host_abi\": \"arm64-v8a\",         \"ua\": \"com.ss.android.ugc.aweme/240901 (Linux; U; Android 10; zh_CN; V1963A; Build/compiler10301842;tt-ok/3.12.13.4-tiktok)\",         \"cookies\": {             \"install_id\": \"3631064037200330\",             \"odin_tt\": \"5ef413aaa319b3a4077814a1da3d3e1bcec3e8640ddc3ad30945a8518f59d1563d24c3b7a3c59d97fbd5344f13208a25cf143312acf4462b028e56cd0b611cc3fc2a64318f7375470d6db86440f92841\",             \"d_ticket\": \"42186c5b0c54ea1a2a9e02d4e62bf6ab\",             \"store-region\": \"cn-js\",             \"store-region-src\": \"did\",             \"multi_sids\": \"462868309327184:38167255076198698951907954929873\",             \"passport_csrf_token\": \"6f75287240634ad1f51f3b3bdcdb5424\",             \"passport_csrf_token_default\": \"6f75287240634ad1f51f3b3bdcdb5424\",             \"ttreq\": \"1$7f616210b41fc044b1f164542ac4e064288b5163\"         },         \"lanusk\": \"\",         \"device_manufacturer\": \"vivo\",         \"uuid\": \"357125675341697\",         \"cdid\": \"f64372bf-4d1d-4883-bc8a-d3d6fa87a9e3\",         \"first_launch_timestamp\": 1726970498636,         \"x_tt_dt\": \"AAA2FGV24A2GAOHJJ3D3XCJ32IZDZ26XXKMQAOTDNUDWTB644ISU5YA3GBYVX2Y3XVOQ3ISDH3UA4JXGGNFXBLJ6AAZU7QTIBKHFYJLDJMDG5K36LVPBRCKLHW2XM\",         \"BootTime\": 1726980411,         \"MbTime\": 1726780411,         \"server_time\": 1726980500,         \"mc\": \"2A:66:7A:2D:8B:29\",         \"rom\": \"compiler10301842\",         \"rom_version\": \"PD1963-user 10 QP1A.190711.020 compiler10301842 release-keys\"     } } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinAppV3APIApi()
proxy = NULL # object | 代理/Proxy (optional)

try:
    # 抖音APP注册设备/Douyin APP register device
    api_instance.register_device_api_v1_douyin_app_v3_register_device_get(proxy=proxy)
except ApiException as e:
    print("Exception when calling DouyinAppV3APIApi->register_device_api_v1_douyin_app_v3_register_device_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy** | [**object**](.md)| 代理/Proxy | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

