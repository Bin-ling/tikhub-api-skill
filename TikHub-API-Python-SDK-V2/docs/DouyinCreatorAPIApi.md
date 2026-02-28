# swagger_client.DouyinCreatorAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get**](DouyinCreatorAPIApi.md#fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get) | **GET** /api/v1/douyin/creator/fetch_creator_activity_detail | 获取创作者活动详情/Get creator activity detail
[**fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get**](DouyinCreatorAPIApi.md#fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get) | **GET** /api/v1/douyin/creator/fetch_creator_activity_list | 获取创作者活动列表/Get creator activity list
[**fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get**](DouyinCreatorAPIApi.md#fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get) | **GET** /api/v1/douyin/creator/fetch_creator_content_category | 获取创作者内容创作合集分类/Get creator content creation category
[**fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get**](DouyinCreatorAPIApi.md#fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get) | **GET** /api/v1/douyin/creator/fetch_creator_content_course | 获取创作者内容创作课程/Get creator content creation course
[**fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get**](DouyinCreatorAPIApi.md#fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get) | **GET** /api/v1/douyin/creator/fetch_creator_hot_challenge_billboard | 获取创作者热门挑战榜单/Get creator hot challenge billboard
[**fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get**](DouyinCreatorAPIApi.md#fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get) | **GET** /api/v1/douyin/creator/fetch_creator_hot_course | 获取创作者热门课程/Get creator hot course
[**fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get**](DouyinCreatorAPIApi.md#fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get) | **GET** /api/v1/douyin/creator/fetch_creator_hot_music_billboard | 获取创作者热门音乐榜单/Get creator hot music billboard
[**fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get**](DouyinCreatorAPIApi.md#fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get) | **GET** /api/v1/douyin/creator/fetch_creator_hot_props_billboard | 获取创作者热门道具榜单/Get creator hot props billboard
[**fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get**](DouyinCreatorAPIApi.md#fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get) | **GET** /api/v1/douyin/creator/fetch_creator_hot_spot_billboard | 获取创作者中心创作热点/Get creator hot spot billboard
[**fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get**](DouyinCreatorAPIApi.md#fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get) | **GET** /api/v1/douyin/creator/fetch_creator_hot_topic_billboard | 获取创作者热门话题榜单/Get creator hot topic billboard
[**fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get**](DouyinCreatorAPIApi.md#fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get) | **GET** /api/v1/douyin/creator/fetch_creator_material_center_billboard | 获取创作者中心热门视频榜单/Get creator material center billboard
[**fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get**](DouyinCreatorAPIApi.md#fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get) | **GET** /api/v1/douyin/creator/fetch_creator_material_center_config | 获取创作者中心配置/Get creator material center config
[**fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get**](DouyinCreatorAPIApi.md#fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get) | **GET** /api/v1/douyin/creator/fetch_industry_category_config | 获取行业分类配置/Get industry category config
[**fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get**](DouyinCreatorAPIApi.md#fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get) | **GET** /api/v1/douyin/creator/fetch_mission_task_list | 获取商单任务列表/Get mission task list
[**fetch_user_search_api_v1_douyin_creator_fetch_user_search_get**](DouyinCreatorAPIApi.md#fetch_user_search_api_v1_douyin_creator_fetch_user_search_get) | **GET** /api/v1/douyin/creator/fetch_user_search | 搜索用户/Search users
[**fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get**](DouyinCreatorAPIApi.md#fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get) | **GET** /api/v1/douyin/creator/fetch_video_danmaku_list | 获取作品弹幕列表/Get video danmaku list


# **fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get**
> fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get(activity_id)

获取创作者活动详情/Get creator activity detail

# [中文] ### 用途: - 获取抖音创作者活动详情数据 ### 参数: - activity_id: 活动ID（从活动列表接口获取） ### 返回: - 创作者活动详情数据  # [English] ### Purpose: - Get Douyin creator activity detail data ### Parameters: - activity_id: Activity ID (obtained from activity list interface) ### Return: - Creator activity detail data  # [示例/Example] activity_id = \"7545335931785450534\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
activity_id = NULL # object | 活动ID/Activity ID

try:
    # 获取创作者活动详情/Get creator activity detail
    api_instance.fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get(activity_id)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | [**object**](.md)| 活动ID/Activity ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get**
> fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get(start_time, end_time)

获取创作者活动列表/Get creator activity list

# [中文] ### 用途: - 获取抖音创作者活动列表数据 ### 参数: - start_time: 开始时间戳 - end_time: 结束时间戳 ### 返回: - 创作者活动列表数据  # [English] ### Purpose: - Get Douyin creator activity list data ### Parameters: - start_time: Start timestamp - end_time: End timestamp ### Return: - Creator activity list data  # [示例/Example] start_time = 1756656000 end_time = 1759247999

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
start_time = NULL # object | 开始时间戳/Start timestamp
end_time = NULL # object | 结束时间戳/End timestamp

try:
    # 获取创作者活动列表/Get creator activity list
    api_instance.fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get(start_time, end_time)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | [**object**](.md)| 开始时间戳/Start timestamp | 
 **end_time** | [**object**](.md)| 结束时间戳/End timestamp | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get**
> fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get()

获取创作者内容创作合集分类/Get creator content creation category

# [中文] ### 用途: - 获取抖音创作者平台内容创作的合集分类列表 ### 参数: - 无需额外参数 ### 返回: - 内容创作合集分类数据  # [English] ### Purpose: - Get Douyin creator platform content creation category list ### Parameters: - No additional parameters required ### Return: - Content creation category data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()

try:
    # 获取创作者内容创作合集分类/Get creator content creation category
    api_instance.fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get()
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get: %s\n" % e)
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

# **fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get**
> fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get(category_id, order=order, limit=limit, offset=offset)

获取创作者内容创作课程/Get creator content creation course

# [中文] ### 用途: - 获取抖音创作者平台指定分类的内容创作课程 ### 参数: - category_id: 分类ID (更多分类ID请通过内容创作合集分类接口获取)     常见分类ID示例:     - 184: 视频创作     - 185: 直播创作     - 186: 图文创作     - 188: 美食视频创作     - 180: 内容创作基础 - order: 排序方式 (1=推荐排序, 2=最受欢迎, 3=最新上传) - limit: 每页数量 (建议24，范围1-100) - offset: 偏移量 (起始位置) ### 返回: - 指定分类的内容创作课程数据  # [English] ### Purpose: - Get Douyin creator platform content creation courses for specified category ### Parameters: - category_id: Category ID (for more category IDs, please refer to the content creation category interface)     Common category ID examples:     - 184: Video Creation     - 185: Live Streaming Creation     - 186: Image & Text Creation     - 188: Food Video Creation     - 180: Content Creation Basics - order: Order type (1=recommended order, 2=most popular, 3=latest upload) - limit: Items per page (recommended 24, range 1-100) - offset: Offset (starting position) ### Return: - Content creation course data for specified category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
category_id = NULL # object | 分类ID/Category ID
order = NULL # object | 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传) (optional)
limit = NULL # object | 每页数量/Items per page (optional)
offset = NULL # object | 偏移量/Offset (starting position) (optional)

try:
    # 获取创作者内容创作课程/Get creator content creation course
    api_instance.fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get(category_id, order=order, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | [**object**](.md)| 分类ID/Category ID | 
 **order** | [**object**](.md)| 排序方式/Order type (1&#x3D;推荐排序, 2&#x3D;最受欢迎, 3&#x3D;最新上传) | [optional] 
 **limit** | [**object**](.md)| 每页数量/Items per page | [optional] 
 **offset** | [**object**](.md)| 偏移量/Offset (starting position) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get**
> fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get()

获取创作者热门挑战榜单/Get creator hot challenge billboard

# [中文] ### 用途: - 获取抖音创作者平台热门挑战榜单数据 ### 返回: - 热门挑战榜单数据  # [English] ### Purpose: - Get Douyin creator platform hot challenge billboard data ### Return: - Hot challenge billboard data  # [示例/Example] 无需参数，直接调用即可获取当前热门挑战榜单 No parameters required, call directly to get current hot challenge billboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()

try:
    # 获取创作者热门挑战榜单/Get creator hot challenge billboard
    api_instance.fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get()
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get: %s\n" % e)
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

# **fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get**
> fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get(order=order, limit=limit, offset=offset, category_id=category_id)

获取创作者热门课程/Get creator hot course

# [中文] ### 用途: - 获取抖音创作者平台热门课程数据或精选专题课程 ### 参数: - order: 排序方式 (1=推荐排序, 2=最受欢迎, 3=最新上传) - limit: 每页数量 (建议24，范围1-100) - offset: 偏移量 (起始位置) - category_id: 精选专题分类ID (不传则获取热门课程，传入则获取指定分类的精选专题)     可选值:     - 6976547830546582816: 知识品类     - 6976547923849006336: 生活品类     - 6976547940311633165: 娱乐品类     - 6976547972108635404: 美食品类     - 6980288134957272352: 正能量     - 6980288181744766219: 游戏品类     - 6980288219548011776: 通用 ### 返回: - 热门课程数据或精选专题课程数据  # [English] ### Purpose: - Get Douyin creator platform hot course data or selected topic courses ### Parameters: - order: Order type (1=recommended order, 2=most popular, 3=latest upload) - limit: Items per page (recommended 24, range 1-100) - offset: Offset (starting position) - category_id: Selected topic category ID (empty for hot courses, specific ID for selected topics)     Available values:     - 6976547830546582816: Knowledge Category     - 6976547923849006336: Life Category     - 6976547940311633165: Entertainment Category     - 6976547972108635404: Food Category     - 6980288134957272352: Positive Energy     - 6980288181744766219: Gaming Category     - 6980288219548011776: General ### Return: - Hot course data or selected topic course data  # [示例/Example] ``` # 获取热门课程/Get hot courses GET /fetch_creator_hot_course?order=1&limit=24&offset=0  # 获取知识品类精选专题/Get knowledge category selected topics GET /fetch_creator_hot_course?order=1&limit=24&offset=0&category_id=6976547830546582816  # 获取美食品类精选专题/Get food category selected topics GET /fetch_creator_hot_course?order=1&limit=24&offset=0&category_id=6976547972108635404 ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
order = NULL # object | 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传) (optional)
limit = NULL # object | 每页数量/Items per page (建议24) (optional)
offset = NULL # object | 偏移量/Offset (optional)
category_id = NULL # object | 精选专题分类ID/Selected topic category ID - 不传则为热门课程，传入则为精选专题         可选值/Available values:         6976547830546582816=知识品类, 6976547923849006336=生活品类, 6976547940311633165=娱乐品类,         6976547972108635404=美食品类, 6980288134957272352=正能量, 6980288181744766219=游戏品类,         6980288219548011776=通用 (optional)

try:
    # 获取创作者热门课程/Get creator hot course
    api_instance.fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get(order=order, limit=limit, offset=offset, category_id=category_id)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**object**](.md)| 排序方式/Order type (1&#x3D;推荐排序, 2&#x3D;最受欢迎, 3&#x3D;最新上传) | [optional] 
 **limit** | [**object**](.md)| 每页数量/Items per page (建议24) | [optional] 
 **offset** | [**object**](.md)| 偏移量/Offset | [optional] 
 **category_id** | [**object**](.md)| 精选专题分类ID/Selected topic category ID - 不传则为热门课程，传入则为精选专题         可选值/Available values:         6976547830546582816&#x3D;知识品类, 6976547923849006336&#x3D;生活品类, 6976547940311633165&#x3D;娱乐品类,         6976547972108635404&#x3D;美食品类, 6980288134957272352&#x3D;正能量, 6980288181744766219&#x3D;游戏品类,         6980288219548011776&#x3D;通用 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get**
> fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get(billboard_tag=billboard_tag, order_key=order_key, time_filter=time_filter)

获取创作者热门音乐榜单/Get creator hot music billboard

# [中文] ### 用途: - 获取抖音创作者平台热门音乐榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过配置接口获取 - order_key: 排序键 (1=播放最高, 2=点赞最多, 4=热度最高, 5=投稿最多) - time_filter: 时间筛选 (1=24小时, 2=7天, 3=30天) ### 返回: - 热门音乐榜单数据  # [English] ### Purpose: - Get Douyin creator platform hot music billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface - order_key: Order key (1=highest views, 2=most likes, 4=highest popularity, 5=most submissions) - time_filter: Time filter (1=24 hours, 2=7 days, 3=30 days) ### Return: - Hot music billboard data  # [示例/Example] billboard_tag = 0   # 全部/All order_key = 1   # 播放最高/Highest views time_filter = 1 # 24小时/24 hours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
billboard_tag = NULL # object | 榜单标签/Billboard tag (0=全部，具体分类值可通过配置接口获取) (optional)
order_key = NULL # object | 排序键/Order key (1=播放最高, 2=点赞最多, 4=热度最高, 5=投稿最多) (optional)
time_filter = NULL # object | 时间筛选/Time filter (1=24小时, 2=7天, 3=30天) (optional)

try:
    # 获取创作者热门音乐榜单/Get creator hot music billboard
    api_instance.fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get(billboard_tag=billboard_tag, order_key=order_key, time_filter=time_filter)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billboard_tag** | [**object**](.md)| 榜单标签/Billboard tag (0&#x3D;全部，具体分类值可通过配置接口获取) | [optional] 
 **order_key** | [**object**](.md)| 排序键/Order key (1&#x3D;播放最高, 2&#x3D;点赞最多, 4&#x3D;热度最高, 5&#x3D;投稿最多) | [optional] 
 **time_filter** | [**object**](.md)| 时间筛选/Time filter (1&#x3D;24小时, 2&#x3D;7天, 3&#x3D;30天) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get**
> fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get(billboard_tag=billboard_tag, order_key=order_key, time_filter=time_filter)

获取创作者热门道具榜单/Get creator hot props billboard

# [中文] ### 用途: - 获取抖音创作者热门道具榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取     - 0: 全部     - 333: 美食     - 334: 旅行     - 299: 泛生活     - 335: 汽车     - 336: 科技     - 302: 游戏     - 296: 二次元     - 337: 娱乐     - 311: 明星     - 298: 体育     - 300: 文化教育     - 301: 校园     - 297: 政务     - 305: 时尚     - 306: 才艺     - 669: 财经     - 314: 随拍     - 307: 动植物     - 309: 图文控     - 308: 剧情     - 315: 亲子     - 718: 三农     - 310: 创意     - 312: 户外     - 926: 公益 - order_key: 排序键     - 1: 播放最高     - 5: 投稿最多     - 6: 展现最高     - 7: 收藏最高 - time_filter: 时间筛选     - 1: 24小时     - 2: 7天     - 3: 30天 ### 返回: - 创作者热门道具榜单数据  # [English] ### Purpose: - Get Douyin creator hot props billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface     - 0: All     - 333: Food     - 334: Travel     - 299: Lifestyle     - 335: Automotive     - 336: Technology     - 302: Gaming     - 296: Anime     - 337: Entertainment     - 311: Celebrity     - 298: Sports     - 300: Culture & Education     - 301: Campus     - 297: Government     - 305: Fashion     - 306: Talent Show     - 669: Finance     - 314: Random     - 307: Animals & Plants     - 309: Graphics & Text     - 308: Drama     - 315: Parenting     - 718: Agriculture     - 310: Creative     - 312: Outdoor     - 926: Public Welfare - order_key: Order key     - 1: Highest views     - 5: Most submissions     - 6: Highest exposure     - 7: Most favorites - time_filter: Time filter     - 1: 24 hours     - 2: 7 days     - 3: 30 days ### Return: - Creator hot props billboard data  # [示例/Example] billboard_tag = 0 order_key = 1  # 播放最高/Highest views time_filter = 1  # 24小时/24 hours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
billboard_tag = NULL # object | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface (optional)
order_key = NULL # object | 排序键: 1=播放最高, 5=投稿最多, 6=展现最高, 7=收藏最高/Order key: 1=highest views, 5=most submissions, 6=highest exposure, 7=most favorites (optional)
time_filter = NULL # object | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days (optional)

try:
    # 获取创作者热门道具榜单/Get creator hot props billboard
    api_instance.fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get(billboard_tag=billboard_tag, order_key=order_key, time_filter=time_filter)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billboard_tag** | [**object**](.md)| 榜单标签，0&#x3D;全部，其他值请通过config接口获取/Billboard tag, 0&#x3D;all, other values can be obtained through config interface | [optional] 
 **order_key** | [**object**](.md)| 排序键: 1&#x3D;播放最高, 5&#x3D;投稿最多, 6&#x3D;展现最高, 7&#x3D;收藏最高/Order key: 1&#x3D;highest views, 5&#x3D;most submissions, 6&#x3D;highest exposure, 7&#x3D;most favorites | [optional] 
 **time_filter** | [**object**](.md)| 时间筛选: 1&#x3D;24小时, 2&#x3D;7天, 3&#x3D;30天/Time filter: 1&#x3D;24 hours, 2&#x3D;7 days, 3&#x3D;30 days | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get**
> fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get(billboard_tag=billboard_tag, hot_search_type=hot_search_type, city_code=city_code)

获取创作者中心创作热点/Get creator hot spot billboard

# [中文] ### 用途: - 获取抖音创作者热点榜单数据 ### 参数: - billboard_tag: 热点标签，多个标签用逗号分隔     可选值:     - 站内玩法: 1004,1000,1002,1003,1001     - 话题互动: 20001,20006,20000,20003,20005,20002,20     - 娱乐: 2007,2000,2011,2012,2009,2010,2004,2005,2003,2008,2001,2002,2006     - 社会: 4005,4006,4007,4003,4004,4000     - 二次元: 13000     - 交通: 23000     - 亲子: 19000     - 体育: 5002,5000,5001     - 军事: 21000     - 剧情: 18000     - 动物萌宠: 8000     - 天气: 22001,22002     - 才艺: 17000     - 文化教育: 14000     - 旅行: 10000     - 时尚: 16000     - 时政: 3000,3001,3002     - 校园: 15000     - 汽车: 11000     - 游戏: 12000,12001     - 科技: 6000     - 美食: 9000     - 财经: 7000 - hot_search_type: 热搜类型     - 1: 热点总榜     - 2: 同城热点榜     - 3: 热点上升榜 - city_code: 城市代码，当hot_search_type=2时必需 ### 返回: - 创作者热点榜单数据  # [English] ### Purpose: - Get Douyin creator hot spot billboard data ### Parameters: - billboard_tag: Hot spot tag - multiple tags separated by comma     Available values:     - Platform Features: 1004,1000,1002,1003,1001     - Topic Interaction: 20001,20006,20000,20003,20005,20002,20     - Entertainment: 2007,2000,2011,2012,2009,2010,2004,2005,2003,2008,2001,2002,2006     - Society: 4005,4006,4007,4003,4004,4000     - Anime: 13000     - Transportation: 23000     - Parenting: 19000     - Sports: 5002,5000,5001     - Military: 21000     - Drama: 18000     - Animals & Pets: 8000     - Weather: 22001,22002     - Talent Show: 17000     - Culture & Education: 14000     - Travel: 10000     - Fashion: 16000     - Politics: 3000,3001,3002     - Campus: 15000     - Automotive: 11000     - Gaming: 12000,12001     - Technology: 6000     - Food: 9000     - Finance: 7000 - hot_search_type: Hot search type     - 1: Hot Spot Overall Ranking     - 2: Local Hot Spot Ranking     - 3: Rising Hot Spot Ranking - city_code: City code - required when hot_search_type=2 ### Return: - Creator hot spot billboard data  # [示例/Example] billboard_tag = \"0\"  # 全部/All hot_search_type = 1  # 热点总榜/Overall ranking city_code = None  # 可选/Optional

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
billboard_tag = NULL # object | 热点标签，多个标签用逗号分隔，如'1004,1000,1002'/Hot spot tag - multiple tags separated by comma, like '1004,1000,1002' (optional)
hot_search_type = NULL # object | 热搜类型: 1=热点总榜, 2=同城热点榜, 3=热点上升榜/Hot search type: 1=Overall ranking, 2=Local ranking, 3=Rising ranking (optional)
city_code = NULL # object | 城市代码，当hot_search_type=2时必需/City code - required when hot_search_type=2 (optional)

try:
    # 获取创作者中心创作热点/Get creator hot spot billboard
    api_instance.fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get(billboard_tag=billboard_tag, hot_search_type=hot_search_type, city_code=city_code)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billboard_tag** | [**object**](.md)| 热点标签，多个标签用逗号分隔，如&#39;1004,1000,1002&#39;/Hot spot tag - multiple tags separated by comma, like &#39;1004,1000,1002&#39; | [optional] 
 **hot_search_type** | [**object**](.md)| 热搜类型: 1&#x3D;热点总榜, 2&#x3D;同城热点榜, 3&#x3D;热点上升榜/Hot search type: 1&#x3D;Overall ranking, 2&#x3D;Local ranking, 3&#x3D;Rising ranking | [optional] 
 **city_code** | [**object**](.md)| 城市代码，当hot_search_type&#x3D;2时必需/City code - required when hot_search_type&#x3D;2 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get**
> fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get(billboard_tag=billboard_tag, order_key=order_key, time_filter=time_filter)

获取创作者热门话题榜单/Get creator hot topic billboard

# [中文] ### 用途: - 获取抖音创作者热门话题榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取     - 0: 全部     - 333: 美食     - 334: 旅行     - 299: 泛生活     - 335: 汽车     - 336: 科技     - 302: 游戏     - 296: 二次元     - 337: 娱乐     - 311: 明星     - 298: 体育     - 300: 文化教育     - 301: 校园     - 297: 政务     - 305: 时尚     - 306: 才艺     - 669: 财经     - 314: 随拍     - 307: 动植物     - 309: 图文控     - 308: 剧情     - 315: 亲子     - 718: 三农     - 310: 创意     - 312: 户外     - 926: 公益 - order_key: 排序键     - 1: 播放最高     - 2: 点赞最多     - 3: 评论最多     - 4: 投稿最多 - time_filter: 时间筛选     - 1: 24小时     - 2: 7天     - 3: 30天 ### 返回: - 创作者热门话题榜单数据  # [English] ### Purpose: - Get Douyin creator hot topic billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface     - 0: All     - 333: Food     - 334: Travel     - 299: Lifestyle     - 335: Automotive     - 336: Technology     - 302: Gaming     - 296: Anime     - 337: Entertainment     - 311: Celebrity     - 298: Sports     - 300: Culture & Education     - 301: Campus     - 297: Government     - 305: Fashion     - 306: Talent Show     - 669: Finance     - 314: Random     - 307: Animals & Plants     - 309: Graphics & Text     - 308: Drama     - 315: Parenting     - 718: Agriculture     - 310: Creative     - 312: Outdoor     - 926: Public Welfare - order_key: Order key     - 1: Highest views     - 2: Most likes     - 3: Most comments     - 4: Most submissions - time_filter: Time filter     - 1: 24 hours     - 2: 7 days     - 3: 30 days ### Return: - Creator hot topic billboard data  # [示例/Example] billboard_tag = 0 order_key = 1  # 播放最高/Highest views time_filter = 1  # 24小时/24 hours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
billboard_tag = NULL # object | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface (optional)
order_key = NULL # object | 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=投稿最多/Order key: 1=highest views, 2=most likes, 3=most comments, 4=most submissions (optional)
time_filter = NULL # object | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days (optional)

try:
    # 获取创作者热门话题榜单/Get creator hot topic billboard
    api_instance.fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get(billboard_tag=billboard_tag, order_key=order_key, time_filter=time_filter)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billboard_tag** | [**object**](.md)| 榜单标签，0&#x3D;全部，其他值请通过config接口获取/Billboard tag, 0&#x3D;all, other values can be obtained through config interface | [optional] 
 **order_key** | [**object**](.md)| 排序键: 1&#x3D;播放最高, 2&#x3D;点赞最多, 3&#x3D;评论最多, 4&#x3D;投稿最多/Order key: 1&#x3D;highest views, 2&#x3D;most likes, 3&#x3D;most comments, 4&#x3D;most submissions | [optional] 
 **time_filter** | [**object**](.md)| 时间筛选: 1&#x3D;24小时, 2&#x3D;7天, 3&#x3D;30天/Time filter: 1&#x3D;24 hours, 2&#x3D;7 days, 3&#x3D;30 days | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get**
> fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get(billboard_tag=billboard_tag, order_key=order_key, time_filter=time_filter)

获取创作者中心热门视频榜单/Get creator material center billboard

# [中文] ### 用途: - 获取抖音创作者中心热门视频榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取     - 0: 全部     - 333: 美食     - 334: 旅行     - 299: 泛生活     - 335: 汽车     - 336: 科技     - 302: 游戏     - 296: 二次元     - 337: 娱乐     - 311: 明星     - 298: 体育     - 300: 文化教育     - 301: 校园     - 297: 政务     - 305: 时尚     - 306: 才艺     - 669: 财经     - 314: 随拍     - 307: 动植物     - 309: 图文控     - 308: 剧情     - 315: 亲子     - 718: 三农     - 310: 创意     - 312: 户外     - 926: 公益 - order_key: 排序键     - 1: 播放最高     - 2: 点赞最多     - 3: 评论最多     - 4: 热度最高 - time_filter: 时间筛选     - 1: 24小时     - 2: 7天     - 3: 30天 ### 返回: - 创作者中心热门视频榜单数据  # [English] ### Purpose: - Get Douyin creator material center billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface     - 0: All     - 333: Food     - 334: Travel     - 299: Lifestyle     - 335: Automotive     - 336: Technology     - 302: Gaming     - 296: Anime     - 337: Entertainment     - 311: Celebrity     - 298: Sports     - 300: Culture & Education     - 301: Campus     - 297: Government     - 305: Fashion     - 306: Talent Show     - 669: Finance     - 314: Random     - 307: Animals & Plants     - 309: Graphics & Text     - 308: Drama     - 315: Parenting     - 718: Agriculture     - 310: Creative     - 312: Outdoor     - 926: Public Welfare - order_key: Order key     - 1: Highest views     - 2: Most likes     - 3: Most comments     - 4: Highest popularity - time_filter: Time filter     - 1: 24 hours     - 2: 7 days     - 3: 30 days ### Return: - Creator material center billboard data  # [示例/Example] billboard_tag = 0 order_key = 1  # 播放最高/Highest views time_filter = 1  # 24小时/24 hours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
billboard_tag = NULL # object | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface (optional)
order_key = NULL # object | 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=热度最高/Order key: 1=highest views, 2=most likes, 3=most comments, 4=highest popularity (optional)
time_filter = NULL # object | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days (optional)

try:
    # 获取创作者中心热门视频榜单/Get creator material center billboard
    api_instance.fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get(billboard_tag=billboard_tag, order_key=order_key, time_filter=time_filter)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billboard_tag** | [**object**](.md)| 榜单标签，0&#x3D;全部，其他值请通过config接口获取/Billboard tag, 0&#x3D;all, other values can be obtained through config interface | [optional] 
 **order_key** | [**object**](.md)| 排序键: 1&#x3D;播放最高, 2&#x3D;点赞最多, 3&#x3D;评论最多, 4&#x3D;热度最高/Order key: 1&#x3D;highest views, 2&#x3D;most likes, 3&#x3D;most comments, 4&#x3D;highest popularity | [optional] 
 **time_filter** | [**object**](.md)| 时间筛选: 1&#x3D;24小时, 2&#x3D;7天, 3&#x3D;30天/Time filter: 1&#x3D;24 hours, 2&#x3D;7 days, 3&#x3D;30 days | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get**
> fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get()

获取创作者中心配置/Get creator material center config

# [中文] ### 用途: - 获取抖音创作者中心配置信息 ### 返回: - 创作者中心配置数据  # [English] ### Purpose: - Get Douyin creator material center configuration ### Return: - Creator material center config data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()

try:
    # 获取创作者中心配置/Get creator material center config
    api_instance.fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get()
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get: %s\n" % e)
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

# **fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get**
> fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get()

获取行业分类配置/Get industry category config

# [中文] ### 用途: - 获取抖音创作者平台的行业分类配置 - 返回所有可用的行业分类层级结构 - **建议在调用商单任务列表接口前先调用此接口获取完整的行业分类信息**  ### 重要说明: - 此接口已优化为Redis缓存，首次调用后数据将缓存30天 - 缓存键: `douyin_creator:industry_categories` - 数据结构包含一级行业和二级行业的完整映射关系  ### 数据结构: ```json {     \"status_code\": 0,     \"status_msg\": \"success\",     \"data\": {         \"industry_categories\": [             {\"key\": \"-1\", \"label\": \"全部\"},             {\"key\": 1901, \"label\": \"3C及电器\"},             {\"key\": 1913, \"label\": \"游戏\"},             ...         ],         \"industry_subcategories\": {             1913: [                 {\"key\": \"-1\", \"label\": \"全部\"},                 {\"key\": 191301, \"label\": \"休闲游戏\"},                 {\"key\": 191302, \"label\": \"棋牌桌游\"},                 ...             ],             ...         }     } } ```  ### 在商单任务筛选中的使用: 1. **获取全部行业任务**: `industry_lv1=-1` (此时industry_lv2无需设置) 2. **获取特定一级行业**: `industry_lv1=1913` (游戏行业) 3. **获取特定二级行业**: `industry_lv1=1913&industry_lv2=191301` (游戏-休闲游戏)  ### 性能优化: - 首次调用时从本地JSON文件读取并缓存到Redis - 后续调用直接从Redis缓存读取，大幅提升响应速度 - 缓存有效期30天，确保数据时效性  ### 返回: - 返回完整的行业分类树结构 - 包含32个一级行业分类和对应的二级行业分类 - 每个分类包含分类ID(key)和名称(label)  # [English] ### Purpose: - Get industry category configuration from Douyin Creator platform - Returns all available industry classification hierarchy - **Recommend calling this API first before using mission task list API to get complete industry classification info**  ### Important Notes: - This API is optimized with Redis caching, data will be cached for 30 days after first call - Cache key: `douyin_creator:industry_categories` - Data structure contains complete mapping relationship between primary and secondary industries  ### Data Structure: ```json {     \"status_code\": 0,     \"status_msg\": \"success\",     \"data\": {         \"industry_categories\": [             {\"key\": \"-1\", \"label\": \"All\"},             {\"key\": 1901, \"label\": \"3C & Electronics\"},             {\"key\": 1913, \"label\": \"Gaming\"},             ...         ],         \"industry_subcategories\": {             1913: [                 {\"key\": \"-1\", \"label\": \"All\"},                 {\"key\": 191301, \"label\": \"Casual Games\"},                 {\"key\": 191302, \"label\": \"Board Games\"},                 ...             ],             ...         }     } } ```  ### Usage in Mission Task Filtering: 1. **Get all industry tasks**: `industry_lv1=-1` (industry_lv2 not needed) 2. **Get specific primary industry**: `industry_lv1=1913` (Gaming industry) 3. **Get specific secondary industry**: `industry_lv1=1913&industry_lv2=191301` (Gaming-Casual Games)  ### Performance Optimization: - First call reads from local JSON file and caches to Redis - Subsequent calls read directly from Redis cache, significantly improving response speed - Cache validity period of 30 days ensures data timeliness  ### Return: - Returns complete industry classification tree structure - Contains 32 primary industry categories and corresponding secondary industry categories - Each category contains category ID(key) and name(label)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()

try:
    # 获取行业分类配置/Get industry category config
    api_instance.fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get()
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get: %s\n" % e)
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

# **fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get**
> fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get(cursor=cursor, limit=limit, mission_type=mission_type, tab_scene=tab_scene, industry_lv1=industry_lv1, industry_lv2=industry_lv2, platform_channel=platform_channel, pay_type=pay_type, greater_than_cost_progress=greater_than_cost_progress, publish_time_start=publish_time_start, quick_selector_scene=quick_selector_scene, keyword=keyword)

获取商单任务列表/Get mission task list

# [中文] ### 用途: - 获取抖音创作者平台的商单任务列表 - 支持多种筛选条件，包括行业分类、付费类型、平台渠道等  ### 重要参数使用说明: #### 行业分类组合规则: - **industry_lv1=-1 (全部)**: 当选择全部一级行业时，industry_lv2参数将被忽略，无需设置 - **industry_lv1=具体值**: 当选择具体一级行业时，可配合industry_lv2进行二级筛选     - industry_lv2=-1: 该一级行业下的所有二级分类     - industry_lv2=具体值: 该一级行业下的具体二级分类  #### 可选参数 (选择\"全部\"时无需传入): - **platform_channel**: 不传入表示全部平台渠道 - **pay_type**: 不传入表示全部付费类型 - **greater_than_cost_progress**: 不传入表示不限制成本进度 - **publish_time_start**: 不传入表示不限制发布时间 - **quick_selector_scene**: 不传入表示不使用快速筛选 - **keyword**: 不传入表示不进行关键词搜索  ### 参数详解: - cursor: 游标，用于分页，0表示第一页 - limit: 每页返回的任务数量，建议24 - mission_type: 任务类型，通常为1 - tab_scene: 场景类型     - 1: 可投稿 (可以直接投稿的任务)     - 2: 可报名 (需要报名审核的任务)     - 3: 好物测评 (商品测评类任务) - industry_lv1/lv2: 行业分类 (建议先调用fetch_industry_category_config获取完整分类)     - -1: 全部行业     - 具体数值: 对应具体行业类别 (如1913=游戏, 1903=食品饮料) - platform_channel: 平台渠道 (可选)     - 1: 抖音视频     - 2: 抖音直播     - 3: 抖音图文 - pay_type: 付费类型 (可选)     - 1: 视频等级 (按粉丝量等级定价)     - 2: 自定义 (商家自定义价格)     - 3: 按转化付费 (按转化效果付费)     - 4: 按有效播放量 (按播放量付费)     - 5: 按销售量 (按商品销售量付费)     - 9: 按核销量 (按核销数量付费)     - 14: 按付费分佣 (按分佣比例付费) - greater_than_cost_progress: 成本进度筛选 (可选)     - 20: 高于20%成本进度的任务     - 50: 高于50%成本进度的任务     - 80: 高于80%成本进度的任务 - publish_time_start: 发布开始时间过滤 (可选，时间戳格式) - quick_selector_scene: 快速筛选场景 (可选)     - 1: 高收益任务     - 4: 保底收入任务     - 5: 曾经合作过的商家 - keyword: 关键词搜索 (可选，支持任务名称或任务ID)  ### 使用示例: ``` # 获取全部行业的可投稿任务 GET /fetch_mission_task_list?industry_lv1=-1&tab_scene=1  # 获取游戏行业休闲游戏分类的按播放量付费任务 GET /fetch_mission_task_list?industry_lv1=1913&industry_lv2=191301&pay_type=4  # 获取高收益的抖音视频任务 GET /fetch_mission_task_list?platform_channel=1&quick_selector_scene=1 ```  ### 返回: - 返回符合条件的商单任务列表 - 包含任务详情、报酬信息、要求等  # [English] ### Purpose: - Get mission task list from Douyin Creator platform - Supports multiple filtering conditions including industry classification, payment type, platform channel, etc.  ### Important Parameter Usage Guidelines: #### Industry Classification Combination Rules: - **industry_lv1=-1 (All)**: When selecting all primary industries, industry_lv2 parameter will be ignored, no need to set - **industry_lv1=specific value**: When selecting specific primary industry, can be combined with industry_lv2 for secondary filtering     - industry_lv2=-1: All secondary categories under the primary industry     - industry_lv2=specific value: Specific secondary category under the primary industry  #### Optional Parameters (No need to pass when selecting \"All\"): - **platform_channel**: Not passing means all platform channels - **pay_type**: Not passing means all payment types - **greater_than_cost_progress**: Not passing means no cost progress restriction - **publish_time_start**: Not passing means no publish time restriction - **quick_selector_scene**: Not passing means no quick filtering - **keyword**: Not passing means no keyword search  ### Parameter Details: - cursor: Cursor for pagination, 0 for first page - limit: Number of tasks per page, recommended 24 - mission_type: Mission type, usually 1 - tab_scene: Scene type     - 1: Submittable (tasks that can be submitted directly)     - 2: Registrable (tasks that require registration and approval)     - 3: Product Review (product evaluation tasks) - industry_lv1/lv2: Industry classification (recommend calling fetch_industry_category_config first)     - -1: All industries     - Specific values: Corresponding to specific industry categories (e.g., 1913=Gaming, 1903=Food&Beverage) - platform_channel: Platform channel (optional)     - 1: Douyin Video     - 2: Douyin Live     - 3: Douyin Image&Text - pay_type: Payment type (optional)     - 1: Video Level (pricing by follower level)     - 2: Custom (merchant custom pricing)     - 3: Conversion-based (pay by conversion effect)     - 4: Valid Views (pay by view count)     - 5: Sales Volume (pay by product sales)     - 9: Verification Volume (pay by verification count)     - 14: Commission-based (pay by commission ratio) - greater_than_cost_progress: Cost progress filter (optional)     - 20: Tasks with more than 20% cost progress     - 50: Tasks with more than 50% cost progress     - 80: Tasks with more than 80% cost progress - publish_time_start: Publish start time filter (optional, timestamp format) - quick_selector_scene: Quick filter scene (optional)     - 1: High revenue tasks     - 4: Guaranteed income tasks     - 5: Previously collaborated merchants - keyword: Keyword search (optional, supports task name or task ID)  ### Usage Examples: ``` # Get submittable tasks from all industries GET /fetch_mission_task_list?industry_lv1=-1&tab_scene=1  # Get tasks from gaming industry casual games category with view-based payment GET /fetch_mission_task_list?industry_lv1=1913&industry_lv2=191301&pay_type=4  # Get high-revenue Douyin video tasks GET /fetch_mission_task_list?platform_channel=1&quick_selector_scene=1 ```  ### Return: - Returns mission task list matching the conditions - Contains task details, compensation info, requirements, etc.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
cursor = NULL # object | 游标/Cursor (分页) (optional)
limit = NULL # object | 每页数量/Items per page (optional)
mission_type = NULL # object | 任务类型/Mission type (optional)
tab_scene = NULL # object | 场景类型/Scene type (1=可投稿, 2=可报名, 3=好物测评) (optional)
industry_lv1 = NULL # object | 一级行业/Primary industry (-1=全部) (optional)
industry_lv2 = NULL # object | 二级行业/Secondary industry (-1=全部) (optional)
platform_channel = NULL # object | 平台渠道/Platform channel (1=抖音视频, 2=抖音直播, 3=抖音图文) (optional)
pay_type = NULL # object | 付费类型/Pay type (1=视频等级, 2=自定义, 3=按转化付费, 4=按有效播放量, 5=按销售量, 9=按核销量, 14=按付费分佣) (optional)
greater_than_cost_progress = NULL # object | 成本进度/Cost progress (20=高于20%, 50=高于50%, 80=高于80%) (optional)
publish_time_start = NULL # object | 发布开始时间/Publish start time (时间戳) (optional)
quick_selector_scene = NULL # object | 快速选择场景/Quick selector (1=高收益, 4=保底收入, 5=合作过) (optional)
keyword = NULL # object | 关键词/Keyword (任务名称或ID) (optional)

try:
    # 获取商单任务列表/Get mission task list
    api_instance.fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get(cursor=cursor, limit=limit, mission_type=mission_type, tab_scene=tab_scene, industry_lv1=industry_lv1, industry_lv2=industry_lv2, platform_channel=platform_channel, pay_type=pay_type, greater_than_cost_progress=greater_than_cost_progress, publish_time_start=publish_time_start, quick_selector_scene=quick_selector_scene, keyword=keyword)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | [**object**](.md)| 游标/Cursor (分页) | [optional] 
 **limit** | [**object**](.md)| 每页数量/Items per page | [optional] 
 **mission_type** | [**object**](.md)| 任务类型/Mission type | [optional] 
 **tab_scene** | [**object**](.md)| 场景类型/Scene type (1&#x3D;可投稿, 2&#x3D;可报名, 3&#x3D;好物测评) | [optional] 
 **industry_lv1** | [**object**](.md)| 一级行业/Primary industry (-1&#x3D;全部) | [optional] 
 **industry_lv2** | [**object**](.md)| 二级行业/Secondary industry (-1&#x3D;全部) | [optional] 
 **platform_channel** | [**object**](.md)| 平台渠道/Platform channel (1&#x3D;抖音视频, 2&#x3D;抖音直播, 3&#x3D;抖音图文) | [optional] 
 **pay_type** | [**object**](.md)| 付费类型/Pay type (1&#x3D;视频等级, 2&#x3D;自定义, 3&#x3D;按转化付费, 4&#x3D;按有效播放量, 5&#x3D;按销售量, 9&#x3D;按核销量, 14&#x3D;按付费分佣) | [optional] 
 **greater_than_cost_progress** | [**object**](.md)| 成本进度/Cost progress (20&#x3D;高于20%, 50&#x3D;高于50%, 80&#x3D;高于80%) | [optional] 
 **publish_time_start** | [**object**](.md)| 发布开始时间/Publish start time (时间戳) | [optional] 
 **quick_selector_scene** | [**object**](.md)| 快速选择场景/Quick selector (1&#x3D;高收益, 4&#x3D;保底收入, 5&#x3D;合作过) | [optional] 
 **keyword** | [**object**](.md)| 关键词/Keyword (任务名称或ID) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_search_api_v1_douyin_creator_fetch_user_search_get**
> fetch_user_search_api_v1_douyin_creator_fetch_user_search_get(user_name)

搜索用户/Search users

# [中文] ### 用途: - 搜索抖音用户，支持抖音号和抖音昵称搜索 ### 参数: - user_name: 用户名 (支持抖音号和抖音昵称)     - 抖音号: 如 \"rmrbxmt\"     - 抖音昵称: 如 \"Y\"、\"人民日报\" ### 返回: - 最多返回20个匹配的用户信息 - 包含用户基本信息如头像、昵称、抖音号等  # [English] ### Purpose: - Search Douyin users by Douyin ID or nickname ### Parameters: - user_name: Username (supports Douyin ID and nickname)     - Douyin ID: e.g., \"rmrbxmt\"     - Nickname: e.g., \"Y\", \"人民日报\" ### Return: - Returns up to 20 matching user information - Contains basic user info like avatar, nickname, Douyin ID, etc.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
user_name = NULL # object | 用户名/Username (支持抖音号和抖音昵称)

try:
    # 搜索用户/Search users
    api_instance.fetch_user_search_api_v1_douyin_creator_fetch_user_search_get(user_name)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_user_search_api_v1_douyin_creator_fetch_user_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | [**object**](.md)| 用户名/Username (支持抖音号和抖音昵称) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get**
> fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get(item_id, count=count, offset=offset, order_type=order_type, is_blocked=is_blocked)

获取作品弹幕列表/Get video danmaku list

# [中文] ### 用途: - 获取指定作品的弹幕列表，支持管理和筛选弹幕 ### 参数: - item_id: 作品ID (必需参数，从作品链接或API获取) - count: 每页弹幕数量 (建议20，范围1-100) - offset: 偏移量 (分页使用，起始位置) - order_type: 排序类型 (1=时间排序, 2=其他排序) - is_blocked: 是否获取被屏蔽的弹幕 (false=正常弹幕, true=被屏蔽弹幕) ### 返回: - 作品弹幕列表数据  # [English] ### Purpose: - Get danmaku list for specified video, supports management and filtering ### Parameters: - item_id: Video item ID (required, get from video link or API) - count: Items per page (recommended 20, range 1-100) - offset: Offset (for pagination, starting position) - order_type: Order type (1=time order, 2=other order) - is_blocked: Whether to get blocked danmaku (false=normal, true=blocked) ### Return: - Video danmaku list data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DouyinCreatorAPIApi()
item_id = NULL # object | 作品ID/Video item ID
count = NULL # object | 每页数量/Items per page (optional)
offset = NULL # object | 偏移量/Offset (starting position) (optional)
order_type = NULL # object | 排序类型/Order type (1=时间排序, 2=其他排序) (optional)
is_blocked = NULL # object | 是否被屏蔽/Is blocked (optional)

try:
    # 获取作品弹幕列表/Get video danmaku list
    api_instance.fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get(item_id, count=count, offset=offset, order_type=order_type, is_blocked=is_blocked)
except ApiException as e:
    print("Exception when calling DouyinCreatorAPIApi->fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**object**](.md)| 作品ID/Video item ID | 
 **count** | [**object**](.md)| 每页数量/Items per page | [optional] 
 **offset** | [**object**](.md)| 偏移量/Offset (starting position) | [optional] 
 **order_type** | [**object**](.md)| 排序类型/Order type (1&#x3D;时间排序, 2&#x3D;其他排序) | [optional] 
 **is_blocked** | [**object**](.md)| 是否被屏蔽/Is blocked | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

