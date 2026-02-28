# TikHub-API-Python-SDK-V2 使用指南

## 1. SDK 概述与功能介绍

### 1.1 概述
TikHub-API-Python-SDK-V2 是一个自动生成的 Python 客户端库，用于与 TikHub API 进行交互。该 SDK 提供了对多个平台的 API 访问能力，包括抖音、TikTok、小红书、B站、Instagram、YouTube 等。

### 1.2 核心功能
- **多平台支持**：支持抖音、TikTok、小红书、B站、Instagram、YouTube、Twitter、Threads、Reddit、Zhihu 等多个平台的 API
- **完整的 API 覆盖**：包含各平台的主要功能，如视频获取、用户信息、搜索、热门榜单等
- **易于使用**：提供简洁的 API 接口，简化开发流程
- **详细的文档**：每个 API 都有详细的文档说明
- **完整的测试用例**：包含全面的测试覆盖

## 2. 环境配置要求

### 2.1 系统要求
- Python 2.7 或 3.4+
- 支持的操作系统：Windows、macOS、Linux

### 2.2 依赖项
SDK 依赖以下 Python 包：
- certifi>=2017.4.17
- python-dateutil>=2.1
- six>=1.10
- urllib3>=1.23

## 3. 安装步骤

### 3.1 从源代码安装
```bash
# 克隆仓库（如果尚未克隆）
git clone https://github.com/your-repository/tikhub-api-python-sdk-v2.git

# 进入 SDK 目录
cd tikhub-api-python-sdk-v2

# 安装依赖
pip install -r requirements.txt

# 安装 SDK
pip install -e .
```

### 3.2 直接安装
```bash
# 从 GitHub 直接安装
pip install git+https://github.com/your-repository/tikhub-api-python-sdk-v2.git

# 或从本地安装（如果已克隆仓库）
pip install /path/to/tikhub-api-python-sdk-v2
```

## 4. 初始化方法

### 4.1 基本初始化
```python
import swagger_client
from swagger_client.rest import ApiException

# 创建配置对象
configuration = swagger_client.Configuration()

# 设置 API 域名（根据所在地区选择）
# 中国大陆用户
configuration.host = "https://api.tikhub.dev"
# 非中国大陆用户
# configuration.host = "https://api.tikhub.io"

# 创建 API 客户端
api_client = swagger_client.ApiClient(configuration)
```

### 4.2 高级配置
```python
# 设置调试模式
configuration.debug = True

# 设置超时时间
# 注意：SDK 内部已处理超时，一般无需手动设置

# 设置代理（如果需要）
# configuration.proxy = "http://your-proxy-server:port"
```

## 5. 核心 API 接口说明

### 5.1 抖音 API

#### 5.1.1 获取单个视频信息
- **方法**：`DouyinAppV3APIApi.fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get`
- **参数**：
  - `video_id`：视频 ID（必填）
- **返回值**：视频详细信息（包含标题、作者、播放量等）
- **示例代码**：
  ```python
  api_instance = swagger_client.DouyinAppV3APIApi(api_client)
  try:
      video_id = "7234567890123456789"
      response = api_instance.fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get(video_id=video_id)
      print(f"视频标题: {response.title}")
      print(f"作者: {response.author.nickname}")
      print(f"播放量: {response.play_count}")
  except ApiException as e:
      print(f"错误: {e}")
  ```

#### 5.1.2 获取用户信息
- **方法**：`DouyinAppV3APIApi.handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get`
- **参数**：
  - `user_id`：用户 ID（必填）
- **返回值**：用户详细信息
- **示例代码**：
  ```python
  api_instance = swagger_client.DouyinAppV3APIApi(api_client)
  try:
      user_id = "1234567890"
      response = api_instance.handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get(user_id=user_id)
      print(f"用户名: {response.nickname}")
      print(f"粉丝数: {response.follower_count}")
      print(f"关注数: {response.following_count}")
  except ApiException as e:
      print(f"错误: {e}")
  ```

### 5.2 TikTok API

#### 5.2.1 获取单个视频信息
- **方法**：`TikTokAppV3APIApi.fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get`
- **参数**：
  - `video_id`：视频 ID（必填）
- **返回值**：视频详细信息
- **示例代码**：
  ```python
  api_instance = swagger_client.TikTokAppV3APIApi(api_client)
  try:
      video_id = "7234567890123456789"
      response = api_instance.fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get(video_id=video_id)
      print(f"视频标题: {response.title}")
      print(f"作者: {response.author.nickname}")
  except ApiException as e:
      print(f"错误: {e}")
  ```

### 5.3 小红书 API

#### 5.3.1 获取笔记信息
- **方法**：`XiaohongshuAppAPIApi.fetch_note_info_api_v1_xiaohongshu_app_fetch_note_info_get`
- **参数**：
  - `note_id`：笔记 ID（必填）
- **返回值**：笔记详细信息
- **示例代码**：
  ```python
  api_instance = swagger_client.XiaohongshuAppAPIApi(api_client)
  try:
      note_id = "6434567890123456789"
      response = api_instance.fetch_note_info_api_v1_xiaohongshu_app_fetch_note_info_get(note_id=note_id)
      print(f"笔记标题: {response.title}")
      print(f"作者: {response.user.nickname}")
  except ApiException as e:
      print(f"错误: {e}")
  ```

### 5.4 B 站 API

#### 5.4.1 获取单个视频信息
- **方法**：`BilibiliAppAPIApi.fetch_one_video_api_v1_bilibili_app_fetch_one_video_get`
- **参数**：
  - `aid`：视频 aid（必填）
- **返回值**：视频详细信息
- **示例代码**：
  ```python
  api_instance = swagger_client.BilibiliAppAPIApi(api_client)
  try:
      aid = "123456789"
      response = api_instance.fetch_one_video_api_v1_bilibili_app_fetch_one_video_get(aid=aid)
      print(f"视频标题: {response.title}")
      print(f"作者: {response.owner.name}")
  except ApiException as e:
      print(f"错误: {e}")
  ```

## 6. 常见使用场景示例

### 6.1 批量获取视频信息
```python
import swagger_client
from swagger_client.rest import ApiException

# 初始化配置
configuration = swagger_client.Configuration()
configuration.host = "https://api.tikhub.dev"
api_client = swagger_client.ApiClient(configuration)

# 创建 API 实例
api_instance = swagger_client.DouyinAppV3APIApi(api_client)

# 批量获取视频信息
video_ids = ["7234567890123456789", "7234567890123456790", "7234567890123456791"]

for video_id in video_ids:
    try:
        response = api_instance.fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get(video_id=video_id)
        print(f"视频 ID: {video_id}")
        print(f"标题: {response.title}")
        print(f"播放量: {response.play_count}")
        print("---")
    except ApiException as e:
        print(f"获取视频 {video_id} 失败: {e}")
```

### 6.2 获取热门搜索
```python
import swagger_client
from swagger_client.rest import ApiException

# 初始化配置
configuration = swagger_client.Configuration()
configuration.host = "https://api.tikhub.dev"
api_client = swagger_client.ApiClient(configuration)

# 创建 API 实例
api_instance = swagger_client.DouyinAppV3APIApi(api_client)

# 获取热门搜索
try:
    response = api_instance.fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get()
    print("抖音热门搜索:")
    for i, item in enumerate(response, 1):
        print(f"{i}. {item.keyword} - 热度: {item.hot_value}")
except ApiException as e:
    print(f"错误: {e}")
```

### 6.3 获取用户作品列表
```python
import swagger_client
from swagger_client.rest import ApiException

# 初始化配置
configuration = swagger_client.Configuration()
configuration.host = "https://api.tikhub.dev"
api_client = swagger_client.ApiClient(configuration)

# 创建 API 实例
api_instance = swagger_client.DouyinAppV3APIApi(api_client)

# 获取用户作品列表
try:
    user_id = "1234567890"
    response = api_instance.fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get(user_id=user_id)
    print(f"用户 {user_id} 的作品:")
    for i, video in enumerate(response, 1):
        print(f"{i}. {video.title} - 播放量: {video.play_count}")
except ApiException as e:
    print(f"错误: {e}")
```

## 7. 错误处理机制

### 7.1 异常类型
- **ApiException**：API 调用异常，包含错误码、错误信息等

### 7.2 错误处理示例
```python
try:
    # API 调用
    response = api_instance.fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get(video_id=video_id)
except ApiException as e:
    # 处理 API 异常
    print(f"API 错误: {e}")
    print(f"错误码: {e.status}")
    print(f"错误信息: {e.reason}")
except Exception as e:
    # 处理其他异常
    print(f"其他错误: {e}")
```

### 7.3 常见错误及解决方案
| 错误码 | 错误信息 | 解决方案 |
|--------|----------|----------|
| 400 | Bad Request | 检查请求参数是否正确 |
| 401 | Unauthorized | 检查 API 密钥是否正确 |
| 403 | Forbidden | 检查权限是否足够 |
| 404 | Not Found | 检查资源是否存在 |
| 429 | Too Many Requests | 减少请求频率，遵守 QPS 限制 |
| 500 | Internal Server Error | 稍后重试 |

## 8. 注意事项及最佳实践

### 8.1 注意事项
1. **API 速率限制**：遵守 QPS 限制（10/秒），避免过度请求
2. **域名选择**：中国大陆用户请使用 `https://api.tikhub.dev`，非中国大陆用户使用 `https://api.tikhub.io`
3. **参数验证**：确保传递的参数符合 API 要求
4. **错误处理**：妥善处理 API 异常，提高代码健壮性
5. **缓存机制**：对于频繁访问的数据，考虑使用缓存

### 8.2 最佳实践
1. **模块化设计**：将 API 调用封装成函数或类，提高代码可维护性
2. **异步处理**：对于大量 API 调用，考虑使用异步方式
3. **日志记录**：记录 API 调用日志，便于调试和监控
4. **错误重试**：对于临时性错误，实现适当的重试机制
5. **参数优化**：根据 API 文档，优化请求参数，提高响应速度

### 8.3 性能优化
1. **批量请求**：使用批量 API 减少请求次数
2. **合理缓存**：缓存频繁访问的数据
3. **并发处理**：使用多线程或异步方式处理多个请求
4. **超时设置**：合理设置超时时间，避免请求阻塞

## 9. 总结

TikHub-API-Python-SDK-V2 是一个功能强大、易于使用的 SDK，为开发者提供了便捷的方式来访问多个平台的 API。通过本指南，您应该能够快速上手并有效地使用该 SDK 进行开发工作。

如果您在使用过程中遇到任何问题，请参考 API 文档或联系 TikHub 支持团队获取帮助。

---

**文档更新时间**：2026-03-01
**SDK 版本**：V5.3.2