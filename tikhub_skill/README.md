# TikTok Hub API 技能模块

这是一个为 OpenClaw 设计的技能模块，用于调用 TikTok Hub API 获取短视频平台数据。

## 功能特性

- 支持多个短视频平台的 API 调用，包括抖音、快手、TikTok 等
- 提供配置管理功能，可自定义 API 基础 URL 和 API 密钥
- 自动加载和解析 API 端点信息
- 提供简洁的工具接口，方便 OpenClaw 调用
- **新增**：参数验证机制，确保请求参数格式正确
- **新增**：完善的错误处理和日志记录功能
- **新增**：API 响应数据保存和缓存机制
- **新增**：端点解析优化和缓存机制
- **新增**：API 端口索引机制，提高查询效率

## 安装依赖

```bash
npm install
```

## 配置

1. 编辑 `config.json` 文件，设置 API 基础 URL 和 API 密钥：

```json
{
  "base_url": "https://api.tikhub.io",
  "api_key": "your_api_key_here"
}
```

2. 或编辑 `.env` 文件，设置环境变量：

```
BASE_URL=https://api.tikhub.io
API_KEY=your_api_key_here
```

## 可用工具

### 1. call_tikhub_api

调用 TikTok Hub API 获取短视频平台数据。

**参数**：
- `platform` (string, 必填)：平台名称，如 douyin、kuaishou、tiktok 等
- `module` (string, 必填)：模块名称，如 web、app、creator 等
- `method` (string, 必填)：方法名称，如 get_video_detail、get_user_info 等
- `params` (object, 可选)：API 调用参数

**返回**：
```json
{
  "success": true,
  "data": {
    // API 响应数据
  }
}
```

**参数验证**：
- 自动验证 `tags` 和 `query_tag` 字段的格式
- 确保请求参数符合 API 要求的格式规范

### 2. get_tikhub_endpoints

获取所有可用的 API 端点。

**参数**：无

**返回**：
```json
{
  "success": true,
  "data": {
    // 端点信息
  }
}
```

### 3. update_tikhub_config

更新 TikTok Hub 配置。

**参数**：
- `base_url` (string, 可选)：API 基础 URL
- `api_key` (string, 可选)：API 密钥

**返回**：
```json
{
  "success": true,
  "message": "配置更新成功"
}
```

### 4. list_api_resources

列出 api_by_tags 文件夹中的所有 API 资源。

**参数**：
- `platform` (string, 可选)：平台名称，如 Douyin、TikTok 等，用于过滤
- `filter` (string, 可选)：过滤条件

**返回**：
```json
{
  "success": true,
  "data": {
    "api_resources": [
      {
        "file_name": "Douyin-App-V3-API.json",
        "platform": "Douyin",
        "api_count": 50
      }
    ],
    "total_files": 50
  }
}
```

### 5. analyze_api_file

分析指定的 API 文件，提取 API 用途描述和端点信息。

**参数**：
- `file_name` (string, 必填)：API 文件名，如 Douyin-App-V3-API.json

**返回**：
```json
{
  "success": true,
  "data": {
    "file_name": "Douyin-App-V3-API.json",
    "platform": "Douyin",
    "api_count": 50,
    "endpoints": [
      {
        "name": "获取单个作品数据",
        "method": "GET",
        "path": "/api/v1/douyin/app/v3/fetch_one_video",
        "description": "获取单个作品数据，支持图文、视频等",
        "parameters": [],
        "response": {}
      }
    ]
  }
}
```

### 6. generate_api_call

生成 API 调用示例代码和使用建议。

**参数**：
- `file_name` (string, 必填)：API 文件名
- `api_name` (string, 必填)：API 名称
- `parameters` (object, 可选)：API 调用参数

**返回**：
```json
{
  "success": true,
  "data": {
    "name": "获取单个作品数据",
    "method": "GET",
    "path": "/api/v1/douyin/app/v3/fetch_one_video",
    "parameters": {
      "aweme_id": "7448118827402972455"
    },
    "example_code": "// Example GET request...",
    "usage_suggestion": ["Use this API to analyze content performance"]
  }
}
```

## 使用示例

```javascript
const { createSkill } = require('./tikhub_skill');

// 创建技能实例
const tikhubSkill = createSkill();

// 初始化技能
await tikhubSkill.initialize();

// 调用 API 获取抖音视频详情
const result = await tikhubSkill.call_tikhub_api({
  platform: 'douyin',
  module: 'web',
  method: 'get_video_detail',
  params: {
    url: 'https://v.douyin.com/xxxxxx'
  }
});

console.log(result);

// 调用 API 获取热点榜数据（带标签参数）
const hotListResult = await tikhubSkill.call_tikhub_api({
  platform: 'douyin',
  module: 'billboard',
  method: 'fetch_hot_total_list',
  params: {
    page: 1,
    page_size: 10,
    type: 'snapshot',
    tags: {
      "value": 628,
      "children": [
        {"value": 62808}
      ]
    }
  }
});

console.log(hotListResult);
```

## 常见问题解答

### 1. API 调用失败，提示 "tags字段格式错误"

**解决方案**：确保 tags 字段格式正确，应为包含 value 和 children 的对象或对象数组。

**正确格式示例**：
```json
{
  "tags": {
    "value": 628,
    "children": [
      {"value": 62808}
    ]
  }
}
```

### 2. API 调用成功但返回值为空

**解决方案**：系统会自动检测空返回值并提供明确的错误提示。请检查 API 密钥是否正确，以及网络连接是否正常。

### 3. 如何提高 API 调用效率

**解决方案**：
- 利用系统的端点缓存机制，避免重复加载端点定义
- 使用批量 API 调用减少请求次数
- 合理设置 API 调用频率，避免触发速率限制

### 4. 如何查看 API 调用日志

**解决方案**：系统会自动记录 API 调用日志，包括请求参数、响应状态和错误信息。日志输出到控制台，可用于调试和问题排查。

## 故障排除

- **API 调用失败**：检查 API 密钥是否正确，以及网络连接是否正常
- **端点不存在**：检查 platform、module 和 method 参数是否正确
- **配置更新失败**：检查文件权限是否正确
- **参数格式错误**：确保 tags 和 query_tag 字段格式正确
- **返回值为空**：检查 API 密钥权限和网络连接

## 版本历史

- 1.1.0：优化版本，添加参数验证、错误处理、日志记录和缓存机制
- 1.0.0：初始版本，支持基本的 API 调用和配置管理