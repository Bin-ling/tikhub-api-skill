const fs = require('fs');
const path = require('path');

// 导入 API 加载器
const { loadApiEndpoints } = require('./apis/index.js');

console.log('Testing JSON API parsing...');

// 加载 API 端点
const endpoints = loadApiEndpoints();

// 输出加载结果
console.log('\n=== API Loading Results ===');
console.log(`Total platforms: ${Object.keys(endpoints).length}`);

// 遍历每个平台
for (const platform in endpoints) {
  console.log(`\nPlatform: ${platform}`);
  const modules = endpoints[platform];
  console.log(`Modules: ${Object.keys(modules).length}`);
  
  // 遍历每个模块
  for (const moduleName in modules) {
    const moduleEndpoints = modules[moduleName];
    console.log(`  - ${moduleName}: ${Object.keys(moduleEndpoints).length} endpoints`);
    
    // 显示前5个端点作为示例
    const endpointKeys = Object.keys(moduleEndpoints);
    if (endpointKeys.length > 0) {
      console.log('    Sample endpoints:');
      for (let i = 0; i < Math.min(5, endpointKeys.length); i++) {
        const key = endpointKeys[i];
        const endpoint = moduleEndpoints[key];
        console.log(`      * ${key}: ${endpoint.method} ${endpoint.path}`);
      }
    }
  }
}

console.log('\n=== Testing Complete ===');
