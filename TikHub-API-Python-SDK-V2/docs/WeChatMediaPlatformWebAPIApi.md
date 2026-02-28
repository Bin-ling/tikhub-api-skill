# swagger_client.WeChatMediaPlatformWebAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_mp_article_ad_api_v1_wechat_mp_web_fetch_mp_article_ad_get**](WeChatMediaPlatformWebAPIApi.md#fetch_mp_article_ad_api_v1_wechat_mp_web_fetch_mp_article_ad_get) | **GET** /api/v1/wechat_mp/web/fetch_mp_article_ad | 获取微信公众号广告/Get Wechat MP Article Ad
[**fetch_mp_article_comment_list_api_v1_wechat_mp_web_fetch_mp_article_comment_list_get**](WeChatMediaPlatformWebAPIApi.md#fetch_mp_article_comment_list_api_v1_wechat_mp_web_fetch_mp_article_comment_list_get) | **GET** /api/v1/wechat_mp/web/fetch_mp_article_comment_list | 获取微信公众号文章评论列表/Get Wechat MP Article Comment List
[**fetch_mp_article_comment_reply_list_api_v1_wechat_mp_web_fetch_mp_article_comment_reply_list_get**](WeChatMediaPlatformWebAPIApi.md#fetch_mp_article_comment_reply_list_api_v1_wechat_mp_web_fetch_mp_article_comment_reply_list_get) | **GET** /api/v1/wechat_mp/web/fetch_mp_article_comment_reply_list | 获取微信公众号文章评论回复列表/Get Wechat MP Article Comment Reply List
[**fetch_mp_article_detail_html_api_v1_wechat_mp_web_fetch_mp_article_detail_html_get**](WeChatMediaPlatformWebAPIApi.md#fetch_mp_article_detail_html_api_v1_wechat_mp_web_fetch_mp_article_detail_html_get) | **GET** /api/v1/wechat_mp/web/fetch_mp_article_detail_html | 获取微信公众号文章详情的HTML/Get Wechat MP Article Detail HTML
[**fetch_mp_article_detail_json_api_v1_wechat_mp_web_fetch_mp_article_detail_json_get**](WeChatMediaPlatformWebAPIApi.md#fetch_mp_article_detail_json_api_v1_wechat_mp_web_fetch_mp_article_detail_json_get) | **GET** /api/v1/wechat_mp/web/fetch_mp_article_detail_json | 获取微信公众号文章详情的JSON/Get Wechat MP Article Detail JSON
[**fetch_mp_article_list_api_v1_wechat_mp_web_fetch_mp_article_list_get**](WeChatMediaPlatformWebAPIApi.md#fetch_mp_article_list_api_v1_wechat_mp_web_fetch_mp_article_list_get) | **GET** /api/v1/wechat_mp/web/fetch_mp_article_list | 获取微信公众号文章列表/Get Wechat MP Article List
[**fetch_mp_article_read_count_api_v1_wechat_mp_web_fetch_mp_article_read_count_get**](WeChatMediaPlatformWebAPIApi.md#fetch_mp_article_read_count_api_v1_wechat_mp_web_fetch_mp_article_read_count_get) | **GET** /api/v1/wechat_mp/web/fetch_mp_article_read_count | 获取微信公众号文章阅读量/Get Wechat MP Article Read Count
[**fetch_mp_article_url_api_v1_wechat_mp_web_fetch_mp_article_url_get**](WeChatMediaPlatformWebAPIApi.md#fetch_mp_article_url_api_v1_wechat_mp_web_fetch_mp_article_url_get) | **GET** /api/v1/wechat_mp/web/fetch_mp_article_url | 获取微信公众号文章永久链接/Get Wechat MP Article URL
[**fetch_mp_article_url_conversion_api_v1_wechat_mp_web_fetch_mp_article_url_conversion_get**](WeChatMediaPlatformWebAPIApi.md#fetch_mp_article_url_conversion_api_v1_wechat_mp_web_fetch_mp_article_url_conversion_get) | **GET** /api/v1/wechat_mp/web/fetch_mp_article_url_conversion | 获取微信公众号长链接转短链接/Get Wechat MP Long URL to Short URL
[**fetch_mp_related_articles_api_v1_wechat_mp_web_fetch_mp_related_articles_get**](WeChatMediaPlatformWebAPIApi.md#fetch_mp_related_articles_api_v1_wechat_mp_web_fetch_mp_related_articles_get) | **GET** /api/v1/wechat_mp/web/fetch_mp_related_articles | 获取微信公众号关联文章/Get Wechat MP Related Articles


# **fetch_mp_article_ad_api_v1_wechat_mp_web_fetch_mp_article_ad_get**
> fetch_mp_article_ad_api_v1_wechat_mp_web_fetch_mp_article_ad_get(url)

获取微信公众号广告/Get Wechat MP Article Ad

# [中文] ### 用途: - 获取微信公众号广告 ### 参数: - url: 文章链接 ### 返回: - 广告  # [English] ### Purpose: - Get Wechat MP Article Ad ### Parameters: - url: Article URL ### Returns: - Ad  # [示例/Example] url = \"https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatMediaPlatformWebAPIApi()
url = NULL # object | 文章链接/Article URL

try:
    # 获取微信公众号广告/Get Wechat MP Article Ad
    api_instance.fetch_mp_article_ad_api_v1_wechat_mp_web_fetch_mp_article_ad_get(url)
except ApiException as e:
    print("Exception when calling WeChatMediaPlatformWebAPIApi->fetch_mp_article_ad_api_v1_wechat_mp_web_fetch_mp_article_ad_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)| 文章链接/Article URL | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_mp_article_comment_list_api_v1_wechat_mp_web_fetch_mp_article_comment_list_get**
> fetch_mp_article_comment_list_api_v1_wechat_mp_web_fetch_mp_article_comment_list_get(url, comment_id=comment_id, buffer=buffer)

获取微信公众号文章评论列表/Get Wechat MP Article Comment List

# [中文] ### 用途: - 获取微信公众号文章评论列表 ### 参数: - url: 文章链接 - comment_id: 评论ID，可以不传获取评论用的id，默认传空字符串 - buffer: 偏移量，第一次传空字符串，后续传上次返回的buffer值 ### 返回: - 评论列表  # [English] ### Purpose: - Get Wechat MP Article Comment List ### Parameters: - url: Article URL - comment_id: Comment ID, can be empty to get the comment ID, default is an empty string - buffer: Offset, first time is an empty string, then pass the buffer value returned last time ### Returns: - Comment List  # [示例/Example] url = \"https://mp.weixin.qq.com/s/Iv-xRzL7WzbL0dUUIgi3Nw\" comment_id = \"\" buffer = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatMediaPlatformWebAPIApi()
url = NULL # object | 文章链接/Article URL
comment_id = NULL # object | 评论ID/Comment ID (optional)
buffer = NULL # object | 偏移量/Offset (optional)

try:
    # 获取微信公众号文章评论列表/Get Wechat MP Article Comment List
    api_instance.fetch_mp_article_comment_list_api_v1_wechat_mp_web_fetch_mp_article_comment_list_get(url, comment_id=comment_id, buffer=buffer)
except ApiException as e:
    print("Exception when calling WeChatMediaPlatformWebAPIApi->fetch_mp_article_comment_list_api_v1_wechat_mp_web_fetch_mp_article_comment_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)| 文章链接/Article URL | 
 **comment_id** | [**object**](.md)| 评论ID/Comment ID | [optional] 
 **buffer** | [**object**](.md)| 偏移量/Offset | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_mp_article_comment_reply_list_api_v1_wechat_mp_web_fetch_mp_article_comment_reply_list_get**
> fetch_mp_article_comment_reply_list_api_v1_wechat_mp_web_fetch_mp_article_comment_reply_list_get(comment_id, content_id, url=url, offset=offset)

获取微信公众号文章评论回复列表/Get Wechat MP Article Comment Reply List

# [中文] ### 用途: - 获取微信公众号文章评论回复列表 ### 参数: - url: 文章链接 - comment_id: 评论ID - content_id: 内容ID - offset: 偏移量 ### 返回: - 评论回复列表  # [English] ### Purpose: - Get Wechat MP Article Comment Reply List ### Parameters: - url: Article URL - comment_id: Comment ID - content_id: Content ID - offset: Offset ### Returns: - Comment Reply List  # [示例/Example] url = \"https://mp.weixin.qq.com/s/RCjkQlkRS4oKZ0GAT9slzA\" comment_id = \"3601466901697855492\" content_id = \"6387234930341970671\" offset = \"0\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatMediaPlatformWebAPIApi()
comment_id = NULL # object | 评论ID/Comment ID
content_id = NULL # object | 内容ID/Content ID
url = NULL # object | 文章链接/Article URL (optional)
offset = NULL # object | 偏移量/Offset (optional)

try:
    # 获取微信公众号文章评论回复列表/Get Wechat MP Article Comment Reply List
    api_instance.fetch_mp_article_comment_reply_list_api_v1_wechat_mp_web_fetch_mp_article_comment_reply_list_get(comment_id, content_id, url=url, offset=offset)
except ApiException as e:
    print("Exception when calling WeChatMediaPlatformWebAPIApi->fetch_mp_article_comment_reply_list_api_v1_wechat_mp_web_fetch_mp_article_comment_reply_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | [**object**](.md)| 评论ID/Comment ID | 
 **content_id** | [**object**](.md)| 内容ID/Content ID | 
 **url** | [**object**](.md)| 文章链接/Article URL | [optional] 
 **offset** | [**object**](.md)| 偏移量/Offset | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_mp_article_detail_html_api_v1_wechat_mp_web_fetch_mp_article_detail_html_get**
> fetch_mp_article_detail_html_api_v1_wechat_mp_web_fetch_mp_article_detail_html_get(url)

获取微信公众号文章详情的HTML/Get Wechat MP Article Detail HTML

# [中文] ### 用途: - 获取微信公众号文章详情的HTML，如果你需要获取详细的JSON格式数据，请使用`/api/v1/wechat_mp/web/fetch_mp_article_detail_json`接口 - 此接口收费贵，价格：0.01$/次 ### 参数: - url: 文章链接 ### 返回: - 文章详情的HTML  # [English] ### Purpose: - Get WeChat MP Article Detail, if you need detailed JSON format data, please use the `/api/v1/wechat_mp/web/fetch_mp_article_detail_json` interface - This interface is more expensive, price: 0.01$/time ### Parameters: - url: Article URL ### Returns: - Article Detail HTML  # [示例/Example] url = \"https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatMediaPlatformWebAPIApi()
url = NULL # object | 文章链接/Article URL

try:
    # 获取微信公众号文章详情的HTML/Get Wechat MP Article Detail HTML
    api_instance.fetch_mp_article_detail_html_api_v1_wechat_mp_web_fetch_mp_article_detail_html_get(url)
except ApiException as e:
    print("Exception when calling WeChatMediaPlatformWebAPIApi->fetch_mp_article_detail_html_api_v1_wechat_mp_web_fetch_mp_article_detail_html_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)| 文章链接/Article URL | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_mp_article_detail_json_api_v1_wechat_mp_web_fetch_mp_article_detail_json_get**
> fetch_mp_article_detail_json_api_v1_wechat_mp_web_fetch_mp_article_detail_json_get(url)

获取微信公众号文章详情的JSON/Get Wechat MP Article Detail JSON

# [中文] ### 用途: - 获取微信公众号文章详情的JSON格式数据 - 此接口收费便宜，如果你需要获取详细的HTML格式数据，请使用`/api/v1/wechat_mp/web/fetch_mp_article_detail_html`接口，但是此接口收费更贵。 - 价格：0.001$/次 ### 参数: - url: 文章链接 ### 返回: - 文章详情的HTML  # [English] ### Purpose: - Get WeChat MP Article Detail in JSON format - This interface is cheaper, if you need detailed HTML format data, please use the `/api/v1/wechat_mp/web/fetch_mp_article_detail_html` interface, but this interface is more expensive. - Price: 0.001$/time ### Parameters: - url: Article URL ### Returns: - Article Detail HTML  # [示例/Example] url = \"https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatMediaPlatformWebAPIApi()
url = NULL # object | 文章链接/Article URL

try:
    # 获取微信公众号文章详情的JSON/Get Wechat MP Article Detail JSON
    api_instance.fetch_mp_article_detail_json_api_v1_wechat_mp_web_fetch_mp_article_detail_json_get(url)
except ApiException as e:
    print("Exception when calling WeChatMediaPlatformWebAPIApi->fetch_mp_article_detail_json_api_v1_wechat_mp_web_fetch_mp_article_detail_json_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)| 文章链接/Article URL | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_mp_article_list_api_v1_wechat_mp_web_fetch_mp_article_list_get**
> fetch_mp_article_list_api_v1_wechat_mp_web_fetch_mp_article_list_get(ghid, offset=offset)

获取微信公众号文章列表/Get Wechat MP Article List

# [中文] ### 用途: - 获取微信公众号文章列表 ### 参数: - ghid: 公众号ID - offset: 偏移量 ### 返回: - 文章列表  # [English] ### Purpose: - Get Wechat MP Article List ### Parameters: - ghid: MP ID - offset: Offset ### Returns: - Article List  # [示例/Example] ghid = \"gh_a3d35d4c9d3f\" offset = \"\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatMediaPlatformWebAPIApi()
ghid = NULL # object | 公众号ID/MP ID
offset = NULL # object | 偏移量/Offset (optional)

try:
    # 获取微信公众号文章列表/Get Wechat MP Article List
    api_instance.fetch_mp_article_list_api_v1_wechat_mp_web_fetch_mp_article_list_get(ghid, offset=offset)
except ApiException as e:
    print("Exception when calling WeChatMediaPlatformWebAPIApi->fetch_mp_article_list_api_v1_wechat_mp_web_fetch_mp_article_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ghid** | [**object**](.md)| 公众号ID/MP ID | 
 **offset** | [**object**](.md)| 偏移量/Offset | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_mp_article_read_count_api_v1_wechat_mp_web_fetch_mp_article_read_count_get**
> fetch_mp_article_read_count_api_v1_wechat_mp_web_fetch_mp_article_read_count_get(url, comment_id)

获取微信公众号文章阅读量/Get Wechat MP Article Read Count

# [中文] ### 用途: - 获取微信公众号文章阅读量 ### 参数: - url: 文章链接 - comment_id: 评论ID ### 返回: - 阅读量  # [English] ### Purpose: - Get Wechat MP Article Read Count ### Parameters: - url: Article URL - comment_id: Comment ID ### Returns: - Read Count  # [示例/Example] url = \"https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg\" comment_id = \"3363399664632332289\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatMediaPlatformWebAPIApi()
url = NULL # object | 文章链接/Article URL
comment_id = NULL # object | 评论ID/Comment ID

try:
    # 获取微信公众号文章阅读量/Get Wechat MP Article Read Count
    api_instance.fetch_mp_article_read_count_api_v1_wechat_mp_web_fetch_mp_article_read_count_get(url, comment_id)
except ApiException as e:
    print("Exception when calling WeChatMediaPlatformWebAPIApi->fetch_mp_article_read_count_api_v1_wechat_mp_web_fetch_mp_article_read_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)| 文章链接/Article URL | 
 **comment_id** | [**object**](.md)| 评论ID/Comment ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_mp_article_url_api_v1_wechat_mp_web_fetch_mp_article_url_get**
> fetch_mp_article_url_api_v1_wechat_mp_web_fetch_mp_article_url_get(sogou_url)

获取微信公众号文章永久链接/Get Wechat MP Article URL

# [中文] ### 用途: - 获取微信公众号文章永久链接 ### 参数: - sogou_url: 搜狗链接 ### 返回: - 永久链接  # [English] ### Purpose: - Get Wechat MP Article URL ### Parameters: - sogou_url: Sogou URL ### Returns: - Article URL  # [示例/Example] sogou_url = \"https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS5mzcw64XRlRaPIdMgILsPEBI9djq3byAlqXa8Fplpd9bV3r44ewJj5IFttt-prmTSHShu8JtNlpDYR_z_1xvD2J_XrGTUriRYOOY2mt9pZSIUQEepUVTybxAOW4P5fEPd23R0CgK6W3KEODtIkcv1U5w5VkZ8a7_lyyAqreiCgr1YH9mz_7mzFDl6rX6ZnkVYNsUHV_OmaXBUCqpZ1Pa6YO8fIRwtipOg..&type=2&query=deepseek&token=C2E90D2050EB6EA5C2C4EDB1541D855FC322013E67C5DC5A&k=4&h=k\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatMediaPlatformWebAPIApi()
sogou_url = NULL # object | 搜狗链接/Sogou URL

try:
    # 获取微信公众号文章永久链接/Get Wechat MP Article URL
    api_instance.fetch_mp_article_url_api_v1_wechat_mp_web_fetch_mp_article_url_get(sogou_url)
except ApiException as e:
    print("Exception when calling WeChatMediaPlatformWebAPIApi->fetch_mp_article_url_api_v1_wechat_mp_web_fetch_mp_article_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sogou_url** | [**object**](.md)| 搜狗链接/Sogou URL | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_mp_article_url_conversion_api_v1_wechat_mp_web_fetch_mp_article_url_conversion_get**
> fetch_mp_article_url_conversion_api_v1_wechat_mp_web_fetch_mp_article_url_conversion_get(url)

获取微信公众号长链接转短链接/Get Wechat MP Long URL to Short URL

# [中文] ### 用途: - 获取微信公众号长链接转短链接 ### 参数: - url: 文章链接 ### 返回: - 短链接  # [English] ### Purpose: - Get Wechat MP Long URL to Short URL ### Parameters: - url: Article URL ### Returns: - Short URL  # [示例/Example] url = \"http://mp.weixin.qq.com/s?__biz=MzIyMDQzMTM4Mg==&mid=2247504868&idx=1&sn=37ee48875df1be54cb766783177ce61d\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatMediaPlatformWebAPIApi()
url = NULL # object | 文章链接/Article URL

try:
    # 获取微信公众号长链接转短链接/Get Wechat MP Long URL to Short URL
    api_instance.fetch_mp_article_url_conversion_api_v1_wechat_mp_web_fetch_mp_article_url_conversion_get(url)
except ApiException as e:
    print("Exception when calling WeChatMediaPlatformWebAPIApi->fetch_mp_article_url_conversion_api_v1_wechat_mp_web_fetch_mp_article_url_conversion_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)| 文章链接/Article URL | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_mp_related_articles_api_v1_wechat_mp_web_fetch_mp_related_articles_get**
> fetch_mp_related_articles_api_v1_wechat_mp_web_fetch_mp_related_articles_get(url)

获取微信公众号关联文章/Get Wechat MP Related Articles

# [中文] ### 用途: - 获取微信公众号关联文章 ### 参数: - url: 文章链接 ### 返回: - 关联文章  # [English] ### Purpose: - Get Wechat MP Related Articles ### Parameters: - url: Article URL ### Returns: - Related Articles  # [示例/Example] url = \"https://mp.weixin.qq.com/s/Ko5V9jw9kwL8TO6Q7J3UqQ\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WeChatMediaPlatformWebAPIApi()
url = NULL # object | 文章链接/Article URL

try:
    # 获取微信公众号关联文章/Get Wechat MP Related Articles
    api_instance.fetch_mp_related_articles_api_v1_wechat_mp_web_fetch_mp_related_articles_get(url)
except ApiException as e:
    print("Exception when calling WeChatMediaPlatformWebAPIApi->fetch_mp_related_articles_api_v1_wechat_mp_web_fetch_mp_related_articles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**object**](.md)| 文章链接/Article URL | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

