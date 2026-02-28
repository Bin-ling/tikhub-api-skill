# swagger_client.TikHubDownloaderAPIApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redirect_download_api_v1_tikhub_downloader_redirect_download_get**](TikHubDownloaderAPIApi.md#redirect_download_api_v1_tikhub_downloader_redirect_download_get) | **GET** /api/v1/tikhub/downloader/redirect_download | 重定向到最新版本的下载链接 / Redirect to the latest version download link
[**update_check_api_v1_tikhub_downloader_version_get**](TikHubDownloaderAPIApi.md#update_check_api_v1_tikhub_downloader_version_get) | **GET** /api/v1/tikhub/downloader/version | 检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates


# **redirect_download_api_v1_tikhub_downloader_redirect_download_get**
> redirect_download_api_v1_tikhub_downloader_redirect_download_get()

重定向到最新版本的下载链接 / Redirect to the latest version download link

# [中文]  ### 用途说明:  - 该接口用于检测客户端操作系统，并重定向到相应的 GitHub Release 直链，方便用户请求后直接开始下载最新版本的文件。  ### 参数说明:  - 无参数。  ### 返回结果:  - Windows 用户：重定向到 `.exe` 下载地址。 - Mac 用户：重定向到 `.zip` 下载地址。 - 其他用户：重定向到 GitHub Release 页面。  # [English]  ### Purpose:  - This endpoint detects the client operating system and redirects to the corresponding GitHub Release direct link, allowing users to start downloading the latest version file immediately.  ### Parameter Description:  - No parameters.  ### Return Result:  - Windows users: Redirect to `.exe` download URL. - Mac users: Redirect to `.zip` download URL. - Other users: Redirect to the GitHub Release page.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TikHubDownloaderAPIApi()

try:
    # 重定向到最新版本的下载链接 / Redirect to the latest version download link
    api_instance.redirect_download_api_v1_tikhub_downloader_redirect_download_get()
except ApiException as e:
    print("Exception when calling TikHubDownloaderAPIApi->redirect_download_api_v1_tikhub_downloader_redirect_download_get: %s\n" % e)
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

# **update_check_api_v1_tikhub_downloader_version_get**
> update_check_api_v1_tikhub_downloader_version_get()

检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates

# [中文]  ### 用途说明:  - 检查TikHub下载器的版本更新。  ### 参数说明:  - 无参数。  ### 返回结果:  - `latest_version`: 最新版本号。 - `update_date`: 更新日期。 - `download_url`: 下载链接。 - `upload_note`: 更新说明。  # [English]  ### Purpose:  - Check for TikHub Downloader version updates.  ### Parameter Description:  - No parameters.  ### Return Result:  - `latest_version`: Latest version number. - `update_date`: Update date. - `download_url`: Download link. - `upload_note`: Update note.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TikHubDownloaderAPIApi()

try:
    # 检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates
    api_instance.update_check_api_v1_tikhub_downloader_version_get()
except ApiException as e:
    print("Exception when calling TikHubDownloaderAPIApi->update_check_api_v1_tikhub_downloader_version_get: %s\n" % e)
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

