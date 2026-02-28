const axios = require('axios');
const dotenv = require('dotenv');
const fs = require('fs');
const path = require('path');

// 加载环境变量
dotenv.config();

// 配置管理
class ConfigManager {
  constructor() {
    this.config = this.loadConfig();
  }

  loadConfig() {
    const configPath = path.join(__dirname, 'config.json');
    let config = {};
    
    // 从配置文件加载
    if (fs.existsSync(configPath)) {
      try {
        config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
      } catch (error) {
        console.error('Error loading config file:', error);
      }
    }
    
    // 从环境变量加载，覆盖配置文件
    if (process.env.BASE_URL) {
      config.base_url = process.env.BASE_URL;
    }
    if (process.env.API_KEY) {
      config.api_key = process.env.API_KEY;
    }
    
    // 默认值
    if (!config.base_url) {
      config.base_url = 'https://api.tikhub.io';
    }
    if (!config.api_key) {
      config.api_key = '';
    }
    
    return config;
  }

  saveConfig() {
    const configPath = path.join(__dirname, 'config.json');
    try {
      fs.writeFileSync(configPath, JSON.stringify(this.config, null, 2), 'utf-8');
      return true;
    } catch (error) {
      console.error('Error saving config file:', error);
      return false;
    }
  }

  updateConfig(newConfig) {
    this.config = { ...this.config, ...newConfig };
    return this.saveConfig();
  }
}

// 日志记录器
class Logger {
  static log(message, data = {}) {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] ${message}`, data);
  }

  static error(message, error = {}) {
    const timestamp = new Date().toISOString();
    console.error(`[${timestamp}] ERROR: ${message}`, error);
  }

  static debug(message, data = {}) {
    const timestamp = new Date().toISOString();
    console.debug(`[${timestamp}] DEBUG: ${message}`, data);
  }
}

// 参数验证器
class ParamValidator {
  static validateTags(tags) {
    if (!tags) return true;
    
    if (Array.isArray(tags)) {
      return tags.every(tag => {
        return typeof tag === 'object' && tag !== null && 
               'value' in tag && 
               (!('children' in tag) || Array.isArray(tag.children));
      });
    } else if (typeof tags === 'object' && tags !== null) {
      return 'value' in tags && 
             (!('children' in tags) || Array.isArray(tags.children));
    }
    return false;
  }

  static validateParams(params, endpointInfo) {
    if (!params) return { valid: true, errors: [] };
    
    const errors = [];
    
    // 验证tags字段
    if ('tags' in params) {
      if (!this.validateTags(params.tags)) {
        errors.push('tags字段格式错误，应为对象或对象数组');
      }
    }
    
    // 验证query_tag字段（如果存在）
    if ('query_tag' in params) {
      if (!this.validateTags(params.query_tag)) {
        errors.push('query_tag字段格式错误，应为包含value和children的对象');
      }
    }
    
    return {
      valid: errors.length === 0,
      errors
    };
  }
}

// API客户端
class APIClient {
  constructor(baseUrl, apiKey) {
    this.baseUrl = baseUrl;
    this.apiKey = apiKey;
    this.client = axios.create({
      baseURL: baseUrl,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': apiKey ? `Bearer ${apiKey}` : ''
      },
      timeout: 60000
    });
  }

  async request(method, endpoint, params) {
    try {
      Logger.log(`API请求: ${method} ${endpoint}`, { params });
      
      let response;
      if (method.toUpperCase() === 'GET') {
        response = await this.client.get(endpoint, { params });
      } else if (method.toUpperCase() === 'POST') {
        response = await this.client.post(endpoint, params);
      } else {
        throw new Error('Unsupported method');
      }
      
      Logger.log(`API响应: ${method} ${endpoint}`, { status: response.status, data: response.data });
      
      // 检查返回值是否为空
      if (!response.data || (typeof response.data === 'object' && Object.keys(response.data).length === 0)) {
        throw new Error('API返回为空');
      }
      
      return response.data;
    } catch (error) {
      Logger.error(`API请求失败: ${method} ${endpoint}`, {
        error: error.message,
        stack: error.stack,
        params
      });
      throw error;
    }
  }
}

// 端点缓存
let endpointsCache = null;
let cacheTimestamp = 0;
const CACHE_DURATION = 3600000; // 1小时缓存

// 加载API端点信息
const { loadApiEndpoints: loadApiEndpointsFromDir } = require('./apis');

function loadApiEndpoints() {
  // 检查缓存是否有效
  const now = Date.now();
  if (endpointsCache && (now - cacheTimestamp) < CACHE_DURATION) {
    Logger.log('使用缓存的API端点');
    return endpointsCache;
  }
  
  // 从目录加载API端点
  Logger.log('加载API端点定义');
  const endpoints = loadApiEndpointsFromDir();
  
  // 如果没有加载到端点，使用默认端点
  if (Object.keys(endpoints).length === 0) {
    Logger.log('使用默认API端点');
    endpointsCache = {
      douyin: {
        web: {
          get_video_detail: {
            path: '/douyin/web/get_video_detail',
            method: 'POST',
            description: '获取抖音视频详情'
          },
          get_user_info: {
            path: '/douyin/web/get_user_info',
            method: 'POST',
            description: '获取抖音用户信息'
          },
          get_hot_list: {
            path: '/douyin/web/get_hot_list',
            method: 'GET',
            description: '获取抖音热榜'
          }
        }
      }
    };
  } else {
    endpointsCache = endpoints;
  }
  
  cacheTimestamp = now;
  Logger.log(`API端点加载完成，共${Object.keys(endpointsCache).length}个平台`);
  return endpointsCache;
}

// 清除端点缓存
function clearEndpointsCache() {
  endpointsCache = null;
  cacheTimestamp = 0;
  Logger.log('API端点缓存已清除');
}

// 技能模块元数据
const skillMetadata = {
  name: 'tikhub-api-skill',
  version: '1.0.0',
  description: '短视频信息获取工具 - 支持抖音、快手、TikTok等多个平台的API调用',
  author: '',
  category: '工具',
  tags: ['短视频', 'API', '信息获取'],
  icon: '📱',
  config: {
    base_url: {
      type: 'string',
      default: 'https://api.tikhub.io',
      description: 'API基础URL'
    },
    api_key: {
      type: 'string',
      default: '',
      description: 'API密钥'
    }
  },
  tools: [
    {
      name: 'call_tikhub_api',
      description: '调用TikTok Hub API获取短视频平台数据',
      parameters: {
        platform: {
          type: 'string',
          required: true,
          description: '平台名称，如douyin、kuaishou、tiktok等'
        },
        module: {
          type: 'string',
          required: true,
          description: '模块名称，如web、app、creator等'
        },
        method: {
          type: 'string',
          required: true,
          description: '方法名称，如get_video_detail、get_user_info等'
        },
        params: {
          type: 'object',
          required: false,
          description: 'API调用参数'
        }
      }
    },
    {
      name: 'get_tikhub_endpoints',
      description: '获取所有可用的API端点',
      parameters: {}
    },
    {
      name: 'update_tikhub_config',
      description: '更新TikTok Hub配置',
      parameters: {
        base_url: {
          type: 'string',
          required: false,
          description: 'API基础URL'
        },
        api_key: {
          type: 'string',
          required: false,
          description: 'API密钥'
        }
      }
    },
    {
      name: 'list_api_resources',
      description: '列出api_by_tags文件夹中的所有API资源',
      parameters: {
        platform: {
          type: 'string',
          required: false,
          description: '平台名称，如Douyin、TikTok等，用于过滤'
        },
        filter: {
          type: 'string',
          required: false,
          description: '过滤条件'
        }
      }
    },
    {
      name: 'analyze_api_file',
      description: '分析指定的API文件，提取API用途描述和端点信息',
      parameters: {
        file_name: {
          type: 'string',
          required: true,
          description: 'API文件名，如Douyin-App-V3-API.json'
        }
      }
    },
    {
      name: 'generate_api_call',
      description: '生成API调用示例代码和使用建议',
      parameters: {
        file_name: {
          type: 'string',
          required: true,
          description: 'API文件名'
        },
        api_name: {
          type: 'string',
          required: true,
          description: 'API名称'
        },
        parameters: {
          type: 'object',
          required: false,
          description: 'API调用参数'
        }
      }
    }
  ]
};

// 技能模块类
class TikhubSkill {
  constructor() {
    this.configManager = new ConfigManager();
    this.apiClient = null;
    this.endpoints = loadApiEndpoints();
    this.apiByTagsPath = path.join(__dirname, '../api_by_tags');
    this.initApiClient();
  }

  initApiClient() {
    const config = this.configManager.config;
    this.apiClient = new APIClient(config.base_url, config.api_key);
  }

  // 初始化函数
  async initialize() {
    console.log('TikTok Hub Skill initialized');
    return {
      success: true,
      message: '技能初始化成功'
    };
  }

  // 调用API工具
  async call_tikhub_api({ platform, module, method, params = {} }) {
    try {
      // 验证参数
      if (!platform || !module || !method) {
        throw new Error('缺少必要参数');
      }

      if (!this.endpoints[platform]) {
        throw new Error('平台不存在');
      }

      if (!this.endpoints[platform][module]) {
        throw new Error('模块不存在');
      }

      if (!this.endpoints[platform][module][method]) {
        throw new Error('方法不存在');
      }

      // 获取端点信息
      const endpointInfo = this.endpoints[platform][module][method];
      const endpoint = endpointInfo.path;
      const httpMethod = endpointInfo.method;

      // 验证请求参数
      const validation = ParamValidator.validateParams(params, endpointInfo);
      if (!validation.valid) {
        throw new Error(validation.errors.join('; '));
      }

      // 执行API调用
      const response = await this.apiClient.request(httpMethod, endpoint, params);

      // 保存关键数据（这里可以根据需要实现具体的保存逻辑）
      this.saveApiResponse({ platform, module, method, params, response });

      return {
        success: true,
        data: response
      };
    } catch (error) {
      Logger.error('API调用失败', {
        platform,
        module,
        method,
        params,
        error: error.message
      });
      return {
        success: false,
        error: error.message
      };
    }
  }

  // 保存API响应数据
  saveApiResponse({ platform, module, method, params, response }) {
    try {
      // 这里可以实现具体的数据保存逻辑
      // 例如保存到数据库、文件或缓存
      Logger.log('保存API响应数据', {
        platform,
        module,
        method,
        response_size: response ? JSON.stringify(response).length : 0
      });
      
      // 简单的内存缓存实现
      if (!this.responseCache) {
        this.responseCache = {};
      }
      const cacheKey = `${platform}_${module}_${method}`;
      this.responseCache[cacheKey] = {
        timestamp: Date.now(),
        params,
        response,
        expiry: Date.now() + 3600000 // 1小时过期
      };
    } catch (error) {
      Logger.error('保存API响应数据失败', error);
    }
  }

  // 获取API端点工具
  async get_tikhub_endpoints() {
    try {
      return {
        success: true,
        data: this.endpoints
      };
    } catch (error) {
      return {
        success: false,
        error: error.message
      };
    }
  }

  // 更新配置工具
  async update_tikhub_config({ base_url, api_key }) {
    try {
      const updateData = {};
      if (base_url) {
        updateData.base_url = base_url;
      }
      if (api_key) {
        updateData.api_key = api_key;
      }

      const success = this.configManager.updateConfig(updateData);
      if (success) {
        this.initApiClient();
        return {
          success: true,
          message: '配置更新成功'
        };
      } else {
        throw new Error('配置更新失败');
      }
    } catch (error) {
      return {
        success: false,
        error: error.message
      };
    }
  }

  // 列出API资源工具
  async list_api_resources({ platform, filter } = {}) {
    try {
      const apiFiles = fs.readdirSync(this.apiByTagsPath).filter(file => file.endsWith('.json'));
      
      const resources = [];
      for (const file of apiFiles) {
        if (platform && !file.includes(platform)) {
          continue;
        }
        
        const filePath = path.join(this.apiByTagsPath, file);
        const content = fs.readFileSync(filePath, 'utf8');
        try {
          const apiData = JSON.parse(content);
          resources.push({
            file_name: file,
            platform: this.extractPlatformFromFilename(file),
            api_count: Array.isArray(apiData) ? apiData.length : 0
          });
        } catch (parseError) {
          console.error(`Error parsing ${file}:`, parseError);
        }
      }
      
      return {
        success: true,
        data: {
          api_resources: resources,
          total_files: resources.length
        }
      };
    } catch (error) {
      return {
        success: false,
        error: error.message
      };
    }
  }

  // 分析API文件工具
  async analyze_api_file({ file_name }) {
    try {
      const filePath = path.join(this.apiByTagsPath, file_name);
      
      if (!fs.existsSync(filePath)) {
        throw new Error(`API file not found: ${file_name}`);
      }
      
      const content = fs.readFileSync(filePath, 'utf8');
      const apiData = JSON.parse(content);
      
      const analysis = {
        file_name,
        platform: this.extractPlatformFromFilename(file_name),
        api_count: Array.isArray(apiData) ? apiData.length : 0,
        endpoints: []
      };
      
      if (Array.isArray(apiData)) {
        apiData.forEach(api => {
          analysis.endpoints.push({
            name: api.summary || api.name || 'Unnamed API',
            method: api.method || 'GET',
            path: api.path || '',
            description: api.description || 'No description',
            parameters: api.parameters || [],
            response: api.response || {}
          });
        });
      }
      
      return {
        success: true,
        data: analysis
      };
    } catch (error) {
      return {
        success: false,
        error: error.message
      };
    }
  }

  // 生成API调用示例工具
  async generate_api_call({ file_name, api_name, parameters }) {
    try {
      const filePath = path.join(this.apiByTagsPath, file_name);
      
      if (!fs.existsSync(filePath)) {
        throw new Error(`API file not found: ${file_name}`);
      }
      
      const content = fs.readFileSync(filePath, 'utf8');
      const apiData = JSON.parse(content);
      
      const targetApi = Array.isArray(apiData) ? 
        apiData.find(api => (api.summary === api_name) || (api.name === api_name)) : 
        null;
      
      if (!targetApi) {
        throw new Error(`API not found: ${api_name} in ${file_name}`);
      }
      
      const apiCall = {
        name: targetApi.summary || targetApi.name,
        method: targetApi.method || 'GET',
        path: targetApi.path || '',
        parameters: parameters || {},
        example_code: this.generateExampleCode(targetApi, parameters),
        usage_suggestion: this.generateUsageSuggestion(targetApi)
      };
      
      return {
        success: true,
        data: apiCall
      };
    } catch (error) {
      return {
        success: false,
        error: error.message
      };
    }
  }

  // 从文件名提取平台
  extractPlatformFromFilename(filename) {
    const platformMap = {
      'Douyin': ['douyin', '抖音'],
      'TikTok': ['tiktok'],
      'Bilibili': ['bilibili', '哔哩哔哩'],
      'Xiaohongshu': ['xiaohongshu', '小红书'],
      'Kuaishou': ['kuaishou', '快手'],
      'Weibo': ['weibo', '微博'],
      'YouTube': ['youtube'],
      'Instagram': ['instagram'],
      'Twitter': ['twitter'],
      'LinkedIn': ['linkedin'],
      'WeChat': ['wechat', '微信'],
      'Toutiao': ['toutiao', '头条'],
      'Xigua': ['xigua', '西瓜'],
      'Lemon8': ['lemon8'],
      'Threads': ['threads'],
      'Reddit': ['reddit'],
      'PiPiXia': ['pipixia', '皮皮虾']
    };
    
    const lowerFilename = filename.toLowerCase();
    for (const [platform, keywords] of Object.entries(platformMap)) {
      if (keywords.some(keyword => lowerFilename.includes(keyword.toLowerCase()))) {
        return platform;
      }
    }
    return 'Unknown';
  }

  // 生成示例代码
  generateExampleCode(api, parameters) {
    const method = api.method || 'GET';
    const path = api.path || '';
    
    if (method === 'GET') {
      const queryParams = parameters ? 
        '?' + Object.entries(parameters).map(([key, value]) => `${key}=${encodeURIComponent(value)}`).join('&') : 
        '';
      return `// Example ${method} request\nconst response = await fetch('${path}${queryParams}', {\n  method: '${method}',\n  headers: {\n    'Content-Type': 'application/json',\n    // Add authentication headers if needed\n  }\n});\n\nconst data = await response.json();\nconsole.log(data);`;
    } else {
      return `// Example ${method} request\nconst response = await fetch('${path}', {\n  method: '${method}',\n  headers: {\n    'Content-Type': 'application/json',\n    // Add authentication headers if needed\n  },\n  body: JSON.stringify(${JSON.stringify(parameters, null, 2)})\n});\n\nconst data = await response.json();\nconsole.log(data);`;
    }
  }

  // 生成使用建议
  generateUsageSuggestion(api) {
    const suggestions = [];
    const apiName = api.summary || api.name || '';
    
    if (apiName.includes('hot') || apiName.includes('trend')) {
      suggestions.push('Use this API to monitor current hot topics and trends');
      suggestions.push('Schedule regular calls to track trend changes over time');
    }
    
    if (apiName.includes('user') || apiName.includes('profile')) {
      suggestions.push('Use this API to analyze competitor profiles');
      suggestions.push('Integrate with user data analysis for audience insights');
    }
    
    if (apiName.includes('video') || apiName.includes('content')) {
      suggestions.push('Use this API to analyze content performance');
      suggestions.push('Combine with other APIs to get comprehensive content insights');
    }
    
    if (apiName.includes('comment')) {
      suggestions.push('Use this API to understand audience feedback');
      suggestions.push('Analyze comment sentiment for content optimization');
    }
    
    if (suggestions.length === 0) {
      suggestions.push('Use this API according to your specific use case');
      suggestions.push('Refer to the API documentation for detailed usage instructions');
    }
    
    return suggestions;
  }

  // 获取技能元数据
  getMetadata() {
    return skillMetadata;
  }

  // 获取工具列表
  getTools() {
    return skillMetadata.tools;
  }
}

// 导出技能模块
module.exports = {
  metadata: skillMetadata,
  createSkill: () => new TikhubSkill()
};