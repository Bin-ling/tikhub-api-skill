# TikTok Hub API 技能模块

这是一个为 OpenClaw 设计的技能模块，用于调用 TikTok Hub API 获取短视频平台数据。

## 功能特性

- 支持多个短视频平台的 API 调用，包括抖音、快手、TikTok 等
- 提供配置管理功能，可自定义 API 基础 URL 和 API 密钥
- 自动加载和解析 API 端点信息
- 提供简洁的工具接口，方便 OpenClaw 调用

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
```

## 注意事项

1. 请确保您有有效的 API 密钥，否则可能无法正常调用 API
2. 部分 API 可能需要特定的参数，请参考 TikTok Hub API 文档
3. 本技能模块依赖于 api_groups 目录下的 JSON 格式 API 端点定义文件

## 故障排除

- **API 调用失败**：检查 API 密钥是否正确，以及网络连接是否正常
- **端点不存在**：检查 platform、module 和 method 参数是否正确
- **配置更新失败**：检查文件权限是否正确

## 版本历史

- 1.0.0：初始版本，支持基本的 API 调用和配置管理