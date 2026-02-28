const { createSkill } = require('./index.js');

async function testSkill() {
  console.log('Testing TikTok Hub Skill...');
  
  // 创建技能实例
  const skill = createSkill();
  
  // 初始化技能
  console.log('\n1. Initializing skill...');
  const initResult = await skill.initialize();
  console.log('Initialization result:', initResult);
  
  // 测试获取 API 端点
  console.log('\n2. Testing get_tikhub_endpoints tool...');
  const endpointsResult = await skill.get_tikhub_endpoints();
  console.log('Endpoints result:', {
    success: endpointsResult.success,
    platforms: endpointsResult.success ? Object.keys(endpointsResult.data).length : 0
  });
  
  // 测试更新配置
  console.log('\n3. Testing update_tikhub_config tool...');
  const configResult = await skill.update_tikhub_config({ 
    base_url: 'https://api.tikhub.io',
    api_key: 'test_api_key'
  });
  console.log('Config update result:', configResult);
  
  // 测试 API 调用（模拟）
  console.log('\n4. Testing call_tikhub_api tool...');
  try {
    // 这里我们只是测试参数验证，不会实际调用 API
    const apiResult = await skill.call_tikhub_api({
      platform: 'douyin',
      module: 'web',
      method: 'fetch_one_video_api_v1_douyin_web_fetch_one_video_get',
      params: { video_id: '123456' }
    });
    console.log('API call result:', apiResult);
  } catch (error) {
    console.log('API call error (expected):', error.message);
  }
  
  console.log('\n=== Skill Test Complete ===');
}

testSkill().catch(console.error);
