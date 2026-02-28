const fs = require('fs');
const path = require('path');

// 解析JSON文件中的API端点信息
function parseJsonEndpoints(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const openapiDoc = JSON.parse(content);
    const endpoints = {};
    
    // 解析paths部分
    if (openapiDoc.paths) {
      for (const [path, methods] of Object.entries(openapiDoc.paths)) {
        for (const [method, info] of Object.entries(methods)) {
          // 提取操作ID作为端点名称
          const operationId = info.operationId || `${method}_${path.replace(/\//g, '_').replace(/[^a-zA-Z0-9_]/g, '')}`;
          
          // 构建端点信息
          const endpointInfo = {
            path: path,
            method: method.toUpperCase(),
            summary: info.summary || '',
            description: info.description || '',
            parameters: info.parameters || [],
            requestBody: info.requestBody || null
          };
          
          endpoints[operationId] = endpointInfo;
        }
      }
    }
    
    return endpoints;
  } catch (error) {
    console.error(`Error parsing ${filePath}:`, error.message);
    return null;
  }
}

// 加载所有平台的API端点
function loadApiEndpoints() {
  const endpoints = {};
  const apiGroupsDir = path.join(__dirname, '../api_groups');
  
  if (fs.existsSync(apiGroupsDir)) {
    const files = fs.readdirSync(apiGroupsDir);
    
    for (const filename of files) {
      if (filename.endsWith('.json')) {
        const filePath = path.join(apiGroupsDir, filename);
        const moduleName = filename.replace('.json', '');
        const parts = moduleName.split('_');
        
        if (parts.length >= 2) {
          const platform = parts[0];
          const moduleType = parts.slice(1).join('_');
          
          if (!endpoints[platform]) {
            endpoints[platform] = {};
          }
          
          const moduleEndpoints = parseJsonEndpoints(filePath);
          if (moduleEndpoints) {
            endpoints[platform][moduleType] = moduleEndpoints;
            console.log(`Loaded ${platform}_${moduleType} with ${Object.keys(moduleEndpoints).length} endpoints`);
          }
        }
      }
    }
  }
  
  return endpoints;
}

// 导出API端点
const apiEndpoints = loadApiEndpoints();
module.exports = {
  endpoints: apiEndpoints,
  loadApiEndpoints
};