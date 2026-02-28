const fs = require('fs');

try {
  const jsonContent = fs.readFileSync('OpenClaw_skills_combined.json', 'utf8');
  JSON.parse(jsonContent);
  console.log('JSON syntax is valid');
} catch (e) {
  console.error('JSON syntax error:', e.message);
  process.exit(1);
}
