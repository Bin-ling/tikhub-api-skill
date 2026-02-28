# coding: utf-8

"""
    TikHub Douyin/TikTok/Xiaohongshu/Lemon8/Bilibili/Sora2/Kuaishou/Pipixia/Weibo/WeChat/Instagram/YouTube/Twitter/Threads/Reddit/Zhihu/Captcha Solver/Temp Mail API

     ----  #### 📋 Release Information/发布信息 - **🔢 Version/版本**: `V5.3.2` - **🕒 Update Time/更新时间**: `2026-02-23` - **🖥️ Environment/环境**: `Production` - **🔗 Base URL/基础路径**: `https://api.tikhub.io`  #### 🌐 Basic HTTP Setup/基本HTTP设置 - **📝 HTTP Method/请求方法**: `GET`、`POST` - **🔄 Retry on Error/错误重试**: `Max Retry: 3` - **⏱️ Timeout/超时**: `>=30s and <=60s` - **⚡ Rate Limit/速率限制**: `QPS: 10/Second`  ----  📢 **重要提醒：域名访问优化（适用于中国大陆用户）**  由于主域名 `api.tikhub.io` 在中国大陆被长城防火墙拦截，**请中国大陆用户改用新域名进行请求**：  * 🇨🇳 **大陆用户请使用**：`https://api.tikhub.dev`（无需代理，直接可用） * 🌍 **非大陆用户继续使用**：`https://api.tikhub.io`  接口路径和参数保持不变，仅需替换域名即可。**请勿跨区使用，会影响访问速度。**  ----  #### 🔗 Useful Links / 有用的链接  - 🏡 **Home**: [https://www.tikhub.io](https://www.tikhub.io) - 🐙 **GitHub Organization** (代码仓库/Repositories): [https://github.com/TikHub](https://github.com/TikHub) - 🛠 **Python SDK V1** (开发套件/SDK): [https://github.com/TikHub/TikHub-API-Python-SDK](https://github.com/TikHub/TikHub-API-Python-SDK) - 🛠 **Python SDK V2** (开发套件/SDK): [https://github.com/TikHub/TikHub-API-Python-SDK-V2](https://github.com/TikHub/TikHub-API-Python-SDK-V2) - 📥 **Multi-Functional Downloader** (工具/Utilities): [https://github.com/TikHub/TikHub-Multi-Functional-Downloader](https://github.com/TikHub/TikHub-Multi-Functional-Downloader) - 🖥️ **API Demo** (示例项目/Demo Project): [https://github.com/TikHub/TikHub-API-Demo](https://github.com/TikHub/TikHub-API-Demo) - 📜 **Swagger UI** (接口文档/API Documentation): [https://api.tikhub.io](https://api.tikhub.io) - 📚 **Apifox UI** (接口文档/API Documentation): [https://docs.tikhub.io](https://docs.tikhub.io) - 🧪 **API Playground** (接口测试/API Testing): [https://app.apifox.com/project/4705614](https://app.apifox.com/project/4705614) - 📈 **API Status Monitor** (服务监控/Service Monitoring): [https://monitor.tikhub.io](https://monitor.tikhub.io) - 💬 **Discord Server** (客服/Support): [https://discord.gg/aMEAS8Xsvz](https://discord.gg/aMEAS8Xsvz) - ✨ **X.com** (更新/Updates): [https://x.com/TikHubio](https://x.com/TikHubio)  ----  #### 📝 备注 - 🌐 TikHub API 是一个多社交媒体数据分析平台，为开发者提供以下数据接口服务，并且还在不断更新中：     - 📱 [抖音网页版数据接口](https://api.tikhub.io/#/Douyin-Web-API)     - 📱 [抖音App V1数据接口](https://api.tikhub.io/#/Douyin-App-V1-API) - （已弃用并且下架接口文档，请使用新版接口）     - 📱 [抖音App V2数据接口](https://api.tikhub.io/#/Douyin-App-V2-API) - （已弃用并且下架接口文档，请使用新版接口）     - 📱 [抖音App V3数据接口](https://api.tikhub.io/#/Douyin-App-V3-API)     - 🔥 [抖音搜索数据接口](https://api.tikhub.io/#/Douyin-Search-API)     - 🔥 [抖音热点榜数据接口](https://api.tikhub.io/#/Douyin-Billboard-API)     - ⭐ [抖音星图数据接口](https://api.tikhub.io/#/Douyin-Xingtu-API)     - ⭐ [抖音星图V2数据接口](https://api.tikhub.io/#/Douyin-Xingtu-V2-API)     - 👨‍🎨 [抖音创作者数据接口](https://api.tikhub.io/#/Douyin-Creator-API)     - 👨‍🎨 [抖音创作者 V2数据接口](https://api.tikhub.io/#/Douyin-Creator-V2-API) - （需要用户Cookie，可获取作品流量总览等数据）     - 🎵 [TikTok网页版数据接口](https://api.tikhub.io/#/TikTok-Web-API)     - 🎵 [TikTok App V2数据接口](https://api.tikhub.io/#/TikTok-App-V2-API) - （已弃用并且下架接口文档，请使用新版接口）     - 🎵 [TikTok App V3数据接口](https://api.tikhub.io/#/TikTok-App-V3-API)     - 👨‍🎨 [TikTok创作者数据接口 - 电商](https://api.tikhub.io/#/TikTok-Creator-API)     - 🎵 [TikTok数据分析接口 - MCN](https://api.tikhub.io/#/TikTok-Analytics-API)     - 🎵 [TikTok商城网页版数据接口](https://api.tikhub.io/#/TikTok-Shop-Web-API)     - 🎵 [TikTok广告创意中心数据接口 - Ads](https://api.tikhub.io/#/TikTok-Ads-API)     - 🍉 [西瓜视频App V2数据接口](https://api.tikhub.io/#/Xigua-App-V2-API)     - 📕 [小红书网页版数据接口](https://api.tikhub.io/#/Xiaohongshu-Web-API)     - 📕 [小红书网页版 V2数据接口](https://api.tikhub.io/#/Xiaohongshu-Web-V2-API)     - 📕 [小红书App数据接口](https://api.tikhub.io/#/Xiaohongshu-App-API)     - 🍋 [Lemon8 App数据接口](https://api.tikhub.io/#/Lemon8-App-API)     - 📺 [哔哩哔哩网页版数据接口](https://api.tikhub.io/#/Bilibili-Web-API)     - 📺 [哔哩哔哩App数据接口](https://api.tikhub.io/#/Bilibili-App-API)     - 🎬 [Sora2 接口](https://api.tikhub.io/#/Sora2-API)     - ⚡ [快手网页版数据接口](https://api.tikhub.io/#/Kuaishou-Web-API)     - ⚡ [快手 App 数据接口](https://api.tikhub.io/#/Kuaishou-App-API)     - 🦐 [皮皮虾 App 数据接口](https://api.tikhub.io/#/PiPiXia-App-API)     - 🔄 [微博网页版数据接口](https://api.tikhub.io/#/Weibo-Web-API)     - 🔄 [微博网页版 V2数据接口](https://api.tikhub.io/#/Weibo-Web-V2-API)     - 🔄 [微博APP数据接口](https://api.tikhub.io/#/Weibo-App-API)     - 💬 [微信公众号网页版数据接口](https://api.tikhub.io/#/WeChat-Channels-API)     - 📱 [微信视频号数据接口](https://api.tikhub.io/#/WeChat-Channels-API)     - 📸 [Instagram Web以及APP数据接口](https://api.tikhub.io/#/Instagram-Web-And-APP-API) - （已弃用并且下架接口文档，请使用新版接口）     - 📸 [Instagram V1数据接口](https://api.tikhub.io/#/Instagram-V1-API)     - 📸 [Instagram V2数据接口](https://api.tikhub.io/#/Instagram-V2-API)     - 📹 [YouTube Web数据接口](https://api.tikhub.io/#/YouTube-Web-API)     - 📹 [YouTube Web V2数据接口](https://api.tikhub.io/#/YouTube-Web-V2-API)     - 🎵 [网易云音乐App数据接口](https://api.tikhub.io/#/NetEase-Cloud-Music-API)     - 🐦 [Twitter Web数据接口](https://api.tikhub.io/#/Twitter-Web-API)     - 🧵 [Threads Web数据接口](https://api.tikhub.io/#/Threads-Web-API)     - 🔴 [Reddit Web数据接口](https://api.tikhub.io/#/Reddit-Web-API)     - 🔴 [Reddit APP数据接口](https://api.tikhub.io/#/Reddit-APP-API)     - 💼 [LinkedIn Web数据接口](https://api.tikhub.io/#/LinkedIn-Web-API)     - ❓ [知乎Web数据接口](https://api.tikhub.io/#/Zhihu-Web-API)     - 🤖 [验证码绕过接口](https://api.tikhub.io/#/Captcha-Solver)     - ✉️ [临时邮箱接口](https://api.tikhub.io/#/Temp-Mail-API) - 📢 请将任何问题或错误报告给[Discord服务器](https://discord.gg/aMEAS8Xsvz)。  #### 👤 用户 - **🖥️ 官网/用户后台/用户支付**: [TikHub User](https://user.tikhub.io/users/signin)  #### 📢 更新通知 - **👋 新用户注册**   - 请注册并**✅ 验证邮箱**后，才能使用API及购买服务。 - **💰 支付**     - 💸 PayPal 支付：支持 Visa、MasterCard、American Express 等国际信用卡；中国用户可直接使用**任意银联信用/储蓄卡**。付款时**无需注册 PayPal**，请在页面选择「信用卡/借记卡」方式完成支付。     - 🪙 Cryptocurrency支付: 支持USDT TRC20 加密货币支付。     - 📞 如果以上支付方式无法满足您的需求，请联系我们。 - **🎁 推荐码**     - 您可以将推荐码注册链接发送给朋友。当您和您的朋友都成为付费用户后，双方将各获得2美元的余额（约2000次请求量）。     - 🔑 推荐码注册链接在个人主页中查看和生成     - ⏱️ 推荐码注册链接有效期为90天     - ✅ 使用推荐码的时候要确保您的账户已验证邮箱并且是付费用户 - **🔑 API Key使用**     - 🔐 请在生成API Key后立即保存，因为API Key只会在创建后显示一次。     - 🔢 每位用户最多可创建20个API Key。 - **🆓 API免费试用**     - 每个用户注册并且验证邮箱后，可以在用户后台的右上角点击签到按钮，获取免费试用额度，每24小时可以签到一次。  ----  #### 🔑 API令牌简介: ##### 📝 方法一：在请求头中使用API令牌（推荐） - **🏷️ 请求头**: `Authorization` - **📋 格式**: `Bearer your_token` - **📄 示例**: `\"Authorization\": \"Bearer your_token\"` - **🖥️ Swagger UI**: 点击页面右上角的`Authorize`按钮或点击要请求的接口旁的 `🔒` 图标，然后直接输入API令牌，无需`Bearer`关键字。  ##### 📝 方法二：在Cookie中使用API令牌（不推荐，仅在无法使用方法一时使用） - **🍪 Cookie**: `Authorization` - **📋 格式**: `Bearer your_token` - **📄 示例**: `Authorization=Bearer your_token`  #### 🔑 获取API令牌: 1. 📝 在TikHub网站注册并登录账户。 2. 👤 进入用户中心，点击API令牌菜单，创建API令牌。 3. 📋 复制并在请求头中使用API令牌。 4. 🔒 保密您的API令牌，仅在请求头中使用。  ----  #### 📝 Note - 🌐 TikHub API is a multi-social media data analysis platform that provides the following data interface services for developers and is constantly being updated:     - 📱 [Douyin Web API](https://api.tikhub.io/#/Douyin-Web-API)     - 📱 [Douyin App V1 API](https://api.tikhub.io/#/Douyin-App-V1-API) - (This API version is deprecated and has been removed. Please use the new version of the API.)     - 📱 [Douyin App V2 API](https://api.tikhub.io/#/Douyin-App-V2-API) - (This API version is deprecated and has been removed. Please use the new version of the API.)     - 📱 [Douyin App V3 API](https://api.tikhub.io/#/Douyin-App-V3-API)     - 🔥 [Douyin Search API](https://api.tikhub.io/#/Douyin-Search-API)     - 🔥 [Douyin Billboard API](https://api.tikhub.io/#/Douyin-Billboard-API)     - ⭐ [Douyin Xingtu API](https://api.tikhub.io/#/Douyin-Xingtu-API)     - ⭐ [Douyin Xingtu V2 API](https://api.tikhub.io/#/Douyin-Xingtu-V2-API)     - 🎵 [TikTok Web API](https://api.tikhub.io/#/TikTok-Web-API)     - 🎵 [TikTok App V2 API](https://api.tikhub.io/#/TikTok-App-V2-API) - (This API version is deprecated and has been removed. Please use the new version of the API.)     - 🎵 [TikTok App V3 API](https://api.tikhub.io/#/TikTok-App-V3-API)     - 👨‍🎨 [TikTok Creator API - E-commerce](https://api.tikhub.io/#/TikTok-Creator-API)     - 🎵 [TikTok Analytics API - MCN](https://api.tikhub.io/#/TikTok-Analytics-API)     - 🎵 [TikTok Shop Web API](https://api.tikhub.io/#/TikTok-Shop-Web-API)     - 🎵 [TikTok Ads API -Ads](https://api.tikhub.io/#/TikTok-Ads-API)     - 🍉 [Xigua App V2 API](https://api.tikhub.io/#/Xigua-App-V2-API)     - 📕 [Xiaohongshu Web API](https://api.tikhub.io/#/Xiaohongshu-Web-API)     - 📕 [Xiaohongshu Web V2 API](https://api.tikhub.io/#/Xiaohongshu-Web-V2-API)     - 📕 [Xiaohongshu App API](https://api.tikhub.io/#/Xiaohongshu-App-API)     - 🍋 [Lemon8 App API](https://api.tikhub.io/#/Lemon8-App-API)     - 📺 [Bilibili Web API](https://api.tikhub.io/#/Bilibili-Web-API)     - 📺 [Bilibili App API](https://api.tikhub.io/#/Bilibili-App-API)     - 🎬 [Sora2 API](https://api.tikhub.io/#/Sora2-API)     - ⚡ [Kuaishou Web API](https://api.tikhub.io/#/Kuaishou-Web-API)     - ⚡ [Kuaishou App API](https://api.tikhub.io/#/Kuaishou-App-API)     - 🦐 [PiPiXia App API](https://api.tikhub.io/#/PiPiXia-App-API)     - 🔄 [Weibo Web API](https://api.tikhub.io/#/Weibo-Web-API)     - 🔄 [Weibo Web V2 API](https://api.tikhub.io/#/Weibo-Web-V2-API)     - 🔄 [Weibo APP API](https://api.tikhub.io/#/Weibo-App-API)     - 💬 [WeChat MP Web API](https://api.tikhub.io/#/WeChat-Channels-API)     - 📱 [WeChat Channels API](https://api.tikhub.io/#/WeChat-Channels-API)     - 📸 [Instagram Web & APP API](https://api.tikhub.io/#/Instagram-Web-And-APP-API) - (This API version is deprecated and has been removed. Please use the new version of the API.)     - 📸 [Instagram V1 API](https://api.tikhub.io/#/Instagram-V1-API)     - 📸 [Instagram V2 API](https://api.tikhub.io/#/Instagram-V2-API)     - 📹 [YouTube Web API](https://api.tikhub.io/#/YouTube-Web-API)     - 📹 [YouTube Web V2 API](https://api.tikhub.io/#/YouTube-Web-V2-API)     - 🎵 [NetEase Cloud Music App API](https://api.tikhub.io/#/NetEase-Cloud-Music-API)     - 🐦 [Twitter Web API](https://api.tikhub.io/#/Twitter-Web-API)     - 🧵 [Threads Web API](https://api.tikhub.io/#/Threads-Web-API)     - 🔴 [Reddit Web API](https://api.tikhub.io/#/Reddit-Web-API)     - 🔴 [Reddit APP API](https://api.tikhub.io/#/Reddit-APP-API)     - 💼 [LinkedIn Web API](https://api.tikhub.io/#/LinkedIn-Web-API)     - ❓ [Zhihu Web API](https://api.tikhub.io/#/Zhihu-Web-API)     - 🤖 [Captcha Solver](https://api.tikhub.io/#/Captcha-Solver)     - ✉️ [Temp Mail API](https://api.tikhub.io/#/Temp-Mail-API) - 📢 Please report any issues or errors to the [Discord server](https://discord.gg/aMEAS8Xsvz).  #### 👤 Users - **🖥️ Official Website/User Dashboard**: [TikHub User](https://user.tikhub.io/users/signin)  #### 📢 Update Notice - **👋 New User Registration**     - Please register and **✅ verify your email** before using the API and purchasing services. - **💰 Payment**     - 💸 PayPal Payment: We accept Visa, MasterCard, American Express, and other major cards. If you’re in China, simply use any **UnionPay credit** or debit card. **No PayPal account is needed**—just select the “Credit or Debit Card” option at checkout.     - 🪙 Cryptocurrency Payment: Supports USDT TRC20 cryptocurrencies.     - 📞 If the above payment methods do not meet your needs, please contact us. - **🎁 Referral Code**     - You can share your referral link with friends. Once both you and your friend become paid users, each of you will receive $2 in credits (approximately 2,000 requests).     - 🔑 The referral code registration link can be viewed and generated on the personal homepage.     - ⏱️ The referral code registration link is valid for 90 days.     - ✅ When using the referral code, make sure your account has verified the email and is a paid user. - **🔑 API Key Usage**     - 🔐 Please save the API Key immediately after generating it, as the API Key will only be displayed once after creation.     - 🔢 Each user can create up to 20 API Keys. - **🆓 API Free Trial**     - After registering and verifying your email, you can click the Check-in button in the upper right corner of the user dashboard to get a free trial balance, you can sign in once every 24 hours.  ----  #### 🔑 API Token Introduction: ##### 📝 Method 1: Use API Token in the Request Header (Recommended) - **🏷️ Header**: `Authorization` - **📋 Format**: `Bearer your_token` - **📄 Example**: `\"Authorization\": \"Bearer your_token\"` - **🖥️ Swagger UI**: Click on the `Authorize` button in the upper right corner of the page or click the `🔒` icon next to the interface you want to request, and then directly enter the API token without the `Bearer` keyword.  ##### 📝 Method 2: Use API Token in the Cookie (Not Recommended, Use Only When Method 1 is Unavailable) - **🍪 Cookie**: `Authorization` - **📋 Format**: `Bearer your_token` - **📄 Example**: `Authorization=Bearer your_token`  #### 🔑 Get API Token: 1. 📝 Register and log in to your account on the TikHub website. 2. 👤 Go to the user center, click on the API token menu, and create an API token. 3. 📋 Copy and use the API token in the request header. 4. 🔒 Keep your API token confidential and use it only in the request header.  ----  #### 📚 API List Index/接口列表索引 - 👤 [TikHub User API | TikHub用户接口](https://api.tikhub.io/#/TikHub-User-API) - 📱 [Douyin Web API | 抖音网页接口](https://api.tikhub.io/#/Douyin-Web-API) - 📱 [Douyin App V1 API | 抖音App V1接口](https://api.tikhub.io/#/Douyin-App-V1-API) - 📱 [Douyin App V2 API | 抖音App V2接口](https://api.tikhub.io/#/Douyin-App-V2-API) - 📱 [Douyin App V3 API | 抖音App V3接口](https://api.tikhub.io/#/Douyin-App-V3-API) - 🔥 [Douyin Search API | 抖音搜索接口](https://api.tikhub.io/#/Douyin-Search-API) - 🔥 [Douyin Billboard API | 抖音热点榜接口](https://api.tikhub.io/#/Douyin-Billboard-API) - ⭐ [Douyin Xingtu API | 抖音星图接口](https://api.tikhub.io/#/Douyin-Xingtu-API) - ⭐ [Douyin Xingtu V2 API | 抖音星图V2接口](https://api.tikhub.io/#/Douyin-Xingtu-V2-API) - 🎵 [TikTok Web API | TikTok网页接口](https://api.tikhub.io/#/TikTok-Web-API) - 🎵 [TikTok App V2 API | TikTok App V2接口](https://api.tikhub.io/#/TikTok-App-V2-API) - 🎵 [TikTok App V3 API | TikTok App V3接口](https://api.tikhub.io/#/TikTok-App-V3-API) - 👨‍🎨 [TikTok Creator API | TikTok创作者接口](https://api.tikhub.io/#/TikTok-Creator-API) - 🎵 [TikTok Analytics API | TikTok数据分析接口](https://api.tikhub.io/#/TikTok-Analytics-API) - 🎵 [TikTok Ads API | TikTok广告创意中心接口](https://api.tikhub.io/#/TikTok-Ads-API) - 🍉 [Xigua App V2 API | 西瓜视频App V2接口](https://api.tikhub.io/#/Xigua-App-V2-API) - 📕 [Xiaohongshu Web API | 小红书Web接口](https://api.tikhub.io/#/Xiaohongshu-Web-API) - 📕 [Xiaohongshu Web V2 API | 小红书WebV2接口](https://api.tikhub.io/#/Xiaohongshu-Web-V2-API) - 📕 [Xiaohongshu App API | 小红书App接口](https://api.tikhub.io/#/Xiaohongshu-App-API) - 🍋 [Lemon8 App API | Lemon8 App接口](https://api.tikhub.io/#/Lemon8-App-API) - 📺 [Bilibili Web API | 哔哩哔哩Web接口](https://api.tikhub.io/#/Bilibili-Web-API) - 📺 [Bilibili App API | 哔哩哔哩Web接口](https://api.tikhub.io/#/Bilibili-App-API) - 🎬 [Sora2 API | Sora2 接口](https://api.tikhub.io/#/Sora2-API) - ⚡ [Kuaishou Web API | 快手网页接口](https://api.tikhub.io/#/Kuaishou-Web-API) - ⚡ [Kuaishou App API | 快手App接口](https://api.tikhub.io/#/Kuaishou-App-API) - 🦐 [PiPiXia App API | 皮皮虾App接口](https://api.tikhub.io/#/PiPiXia-App-API) - 🔄 [Weibo Web API | 微博网页接口](https://api.tikhub.io/#/Weibo-Web-API) - 🔄 [Weibo Web V2 API | 微博网页V2接口](https://api.tikhub.io/#/Weibo-Web-V2-API) - 🔄 [Weibo APP API | 微博APP接口](https://api.tikhub.io/#/Weibo-App-API) - 💬 [WeChat MP Web API | 微信公众号Web接口](https://api.tikhub.io/#/WeChat-Channels-API) - 📱 [WeChat Channels API | 微信视频号接口](https://api.tikhub.io/#/WeChat-Channels-API) - 📸 [Instagram Web & APP API | Instagram Web和APP接口](https://api.tikhub.io/#/Instagram-Web-And-APP-API) - 📸 [Instagram V1 API | Instagram V1接口](https://api.tikhub.io/#/Instagram-V1-API) - 📸 [Instagram V2 API | Instagram V2接口](https://api.tikhub.io/#/Instagram-V2-API) - 📹 [YouTube Web API | YouTube Web接口](https://api.tikhub.io/#/YouTube-Web-API) - 📹 [YouTube Web V2 API | YouTube Web V2接口](https://api.tikhub.io/#/YouTube-Web-V2-API) - 🎵 [NetEase Cloud Music API | 网易云音乐App接口](https://api.tikhub.io/#/NetEase-Cloud-Music-API) - 🐦 [Twitter Web API | Twitter Web接口](https://api.tikhub.io/#/Twitter-Web-API) - 🧵 [Threads Web API | Threads Web接口](https://api.tikhub.io/#/Threads-Web-API) - 🔴 [Reddit Web API | Reddit Web接口](https://api.tikhub.io/#/Reddit-Web-API) - 🔴 [Reddit APP数据接口 | Reddit APP API](https://api.tikhub.io/#/Reddit-APP-API) - 💼 [LinkedIn Web API | LinkedIn Web接口](https://api.tikhub.io/#/LinkedIn-Web-API) - ❓ [Zhihu Web API | 知乎Web接口](https://api.tikhub.io/#/Zhihu-Web-API) - 🤖 [Captcha Solver | 各种验证码绕过接口](https://api.tikhub.io/#/Captcha-Solver) - ✉️ [Temp Mail API | 临时邮箱接口](https://api.tikhub.io/#/Temp-Mail-API)   # noqa: E501

    OpenAPI spec version: V5.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class BilibiliAppAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get(self, **kwargs):  # noqa: E501
        """获取番剧推荐/Get bangumi tab  # noqa: E501

        # [中文] ### 用途: - 获取主页番剧推荐 ### 返回: - 番剧推荐数据  # [English] ### Purpose: - Get bangumi tab (anime recommendations) ### Return: - Bangumi tab data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取番剧推荐/Get bangumi tab  # noqa: E501

        # [中文] ### 用途: - 获取主页番剧推荐 ### 返回: - 番剧推荐数据  # [English] ### Purpose: - Get bangumi tab (anime recommendations) ### Return: - Bangumi tab data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_bangumi_tab', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get(self, **kwargs):  # noqa: E501
        """获取影视推荐/Get cinema tab  # noqa: E501

        # [中文] ### 用途: - 获取主页影视推荐 ### 返回: - 影视推荐数据  # [English] ### Purpose: - Get cinema tab (movies/TV recommendations) ### Return: - Cinema tab data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取影视推荐/Get cinema tab  # noqa: E501

        # [中文] ### 用途: - 获取主页影视推荐 ### 返回: - 影视推荐数据  # [English] ### Purpose: - Get cinema tab (movies/TV recommendations) ### Return: - Cinema tab data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_cinema_tab', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get(self, **kwargs):  # noqa: E501
        """获取主页推荐视频流/Get home feed  # noqa: E501

        # [中文] ### 用途: - 获取主页推荐视频流 ### 参数: - idx: 页面索引，默认使用当前时间戳 - flush: 刷新标记（0=普通加载, 1=刷新） - pull: 是否下拉刷新 ### 返回: - 推荐视频流数据  # [English] ### Purpose: - Get home feed (recommended videos) ### Parameters: - idx: Page index, defaults to current timestamp - flush: Flush flag (0=normal load, 1=refresh) - pull: Pull to refresh ### Return: - Home feed data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idx: 页面索引/Page index
        :param object flush: 刷新标记/Flush flag (0=普通加载, 1=刷新)
        :param object pull: 是否下拉刷新/Pull to refresh
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取主页推荐视频流/Get home feed  # noqa: E501

        # [中文] ### 用途: - 获取主页推荐视频流 ### 参数: - idx: 页面索引，默认使用当前时间戳 - flush: 刷新标记（0=普通加载, 1=刷新） - pull: 是否下拉刷新 ### 返回: - 推荐视频流数据  # [English] ### Purpose: - Get home feed (recommended videos) ### Parameters: - idx: Page index, defaults to current timestamp - flush: Flush flag (0=normal load, 1=refresh) - pull: Pull to refresh ### Return: - Home feed data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idx: 页面索引/Page index
        :param object flush: 刷新标记/Flush flag (0=普通加载, 1=刷新)
        :param object pull: 是否下拉刷新/Pull to refresh
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['idx', 'flush', 'pull']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'idx' in params:
            query_params.append(('idx', params['idx']))  # noqa: E501
        if 'flush' in params:
            query_params.append(('flush', params['flush']))  # noqa: E501
        if 'pull' in params:
            query_params.append(('pull', params['pull']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_home_feed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_one_video_api_v1_bilibili_app_fetch_one_video_get(self, **kwargs):  # noqa: E501
        """获取单个视频详情信息/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个视频详情信息（APP接口） ### 参数: - av_id: AV号（与bv_id二选一） - bv_id: BV号（与av_id二选一） ### 返回: - 视频详情信息  # [English] ### Purpose: - Get single video data (APP API) ### Parameters: - av_id: AV ID (choose one of av_id or bv_id) - bv_id: BV ID (choose one of av_id or bv_id) ### Return: - Video data  # [示例/Example] av_id = \"115568241811221\" bv_id = \"BV18SCrBGE9E\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_app_fetch_one_video_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object av_id: AV号/AV ID
        :param object bv_id: BV号/BV ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_bilibili_app_fetch_one_video_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_bilibili_app_fetch_one_video_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_bilibili_app_fetch_one_video_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取单个视频详情信息/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个视频详情信息（APP接口） ### 参数: - av_id: AV号（与bv_id二选一） - bv_id: BV号（与av_id二选一） ### 返回: - 视频详情信息  # [English] ### Purpose: - Get single video data (APP API) ### Parameters: - av_id: AV ID (choose one of av_id or bv_id) - bv_id: BV ID (choose one of av_id or bv_id) ### Return: - Video data  # [示例/Example] av_id = \"115568241811221\" bv_id = \"BV18SCrBGE9E\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_app_fetch_one_video_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object av_id: AV号/AV ID
        :param object bv_id: BV号/BV ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['av_id', 'bv_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_api_v1_bilibili_app_fetch_one_video_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'av_id' in params:
            query_params.append(('av_id', params['av_id']))  # noqa: E501
        if 'bv_id' in params:
            query_params.append(('bv_id', params['bv_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_one_video', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get(self, **kwargs):  # noqa: E501
        """获取热门推荐/Get popular feed  # noqa: E501

        # [中文] ### 用途: - 获取热门推荐视频 ### 参数: - idx: 页面索引（从1开始） - last_param: 上一页最后一个视频的ID（用于分页） ### 返回: - 热门推荐视频数据  # [English] ### Purpose: - Get popular feed ### Parameters: - idx: Page index (starting from 1) - last_param: Last video ID from previous page (for pagination) ### Return: - Popular feed data  # [示例/Example] idx = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idx: 页面索引/Page index
        :param object last_param: 上一页最后一个视频ID/Last video ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热门推荐/Get popular feed  # noqa: E501

        # [中文] ### 用途: - 获取热门推荐视频 ### 参数: - idx: 页面索引（从1开始） - last_param: 上一页最后一个视频的ID（用于分页） ### 返回: - 热门推荐视频数据  # [English] ### Purpose: - Get popular feed ### Parameters: - idx: Page index (starting from 1) - last_param: Last video ID from previous page (for pagination) ### Return: - Popular feed data  # [示例/Example] idx = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idx: 页面索引/Page index
        :param object last_param: 上一页最后一个视频ID/Last video ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['idx', 'last_param']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'idx' in params:
            query_params.append(('idx', params['idx']))  # noqa: E501
        if 'last_param' in params:
            query_params.append(('last_param', params['last_param']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_popular_feed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get(self, root, **kwargs):  # noqa: E501
        """获取二级评论回复/Get reply detail  # noqa: E501

        # [中文] ### 用途: - 获取二级评论回复 ### 参数: - root: 一级评论ID（必填） - av_id: AV号（与bv_id二选一） - bv_id: BV号（与av_id二选一） - next_offset: 下一页游标 - ps: 每页数量 ### 返回: - 二级评论列表数据  # [English] ### Purpose: - Get reply detail (second level comments) ### Parameters: - root: Root comment ID (required) - av_id: AV ID (choose one of av_id or bv_id) - bv_id: BV ID (choose one of av_id or bv_id) - next_offset: Next page cursor - ps: Page size ### Return: - Reply data  # [示例/Example] root = \"241743663521\" av_id = \"113100682434775\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get(root, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object root: 一级评论ID/Root comment ID (required)
        :param object av_id: AV号/AV ID
        :param object bv_id: BV号/BV ID
        :param object next_offset: 下一页游标/Next page cursor
        :param object ps: 每页数量/Page size
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get_with_http_info(root, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get_with_http_info(root, **kwargs)  # noqa: E501
            return data

    def fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get_with_http_info(self, root, **kwargs):  # noqa: E501
        """获取二级评论回复/Get reply detail  # noqa: E501

        # [中文] ### 用途: - 获取二级评论回复 ### 参数: - root: 一级评论ID（必填） - av_id: AV号（与bv_id二选一） - bv_id: BV号（与av_id二选一） - next_offset: 下一页游标 - ps: 每页数量 ### 返回: - 二级评论列表数据  # [English] ### Purpose: - Get reply detail (second level comments) ### Parameters: - root: Root comment ID (required) - av_id: AV ID (choose one of av_id or bv_id) - bv_id: BV ID (choose one of av_id or bv_id) - next_offset: Next page cursor - ps: Page size ### Return: - Reply data  # [示例/Example] root = \"241743663521\" av_id = \"113100682434775\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get_with_http_info(root, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object root: 一级评论ID/Root comment ID (required)
        :param object av_id: AV号/AV ID
        :param object bv_id: BV号/BV ID
        :param object next_offset: 下一页游标/Next page cursor
        :param object ps: 每页数量/Page size
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['root', 'av_id', 'bv_id', 'next_offset', 'ps']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'root' is set
        if self.api_client.client_side_validation and ('root' not in params or
                                                       params['root'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `root` when calling `fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'root' in params:
            query_params.append(('root', params['root']))  # noqa: E501
        if 'av_id' in params:
            query_params.append(('av_id', params['av_id']))  # noqa: E501
        if 'bv_id' in params:
            query_params.append(('bv_id', params['bv_id']))  # noqa: E501
        if 'next_offset' in params:
            query_params.append(('next_offset', params['next_offset']))  # noqa: E501
        if 'ps' in params:
            query_params.append(('ps', params['ps']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_reply_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_search_all_api_v1_bilibili_app_fetch_search_all_get(self, keyword, **kwargs):  # noqa: E501
        """综合搜索/search all  # noqa: E501

        # [中文] ### 用途: - 综合搜索（返回所有类型的搜索结果） ### 参数: - keyword: 搜索关键词（必填） - page: 页码，从1开始 - page_size: 每页结果数量 - order: 排序方式（0=综合排序） ### 返回: - 搜索结果，包含nav（分类导航）、item（搜索结果）、pagination（分页信息）等  # [English] ### Purpose: -  search all (returns all types of search results) ### Parameters: - keyword: Search keyword (required) - page: Page number, starting from 1 - page_size: Results per page - order: Sort order (0=comprehensive) ### Return: - Search results including nav (category navigation), item (results), pagination, etc.  # [示例/Example] keyword = \"原神\" page = 1 page_size = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_all_api_v1_bilibili_app_fetch_search_all_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
        :param object page_size: 每页数量/Page size
        :param object order: 排序方式/Sort order (0=综合排序)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_all_api_v1_bilibili_app_fetch_search_all_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_all_api_v1_bilibili_app_fetch_search_all_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_all_api_v1_bilibili_app_fetch_search_all_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """综合搜索/search all  # noqa: E501

        # [中文] ### 用途: - 综合搜索（返回所有类型的搜索结果） ### 参数: - keyword: 搜索关键词（必填） - page: 页码，从1开始 - page_size: 每页结果数量 - order: 排序方式（0=综合排序） ### 返回: - 搜索结果，包含nav（分类导航）、item（搜索结果）、pagination（分页信息）等  # [English] ### Purpose: -  search all (returns all types of search results) ### Parameters: - keyword: Search keyword (required) - page: Page number, starting from 1 - page_size: Results per page - order: Sort order (0=comprehensive) ### Return: - Search results including nav (category navigation), item (results), pagination, etc.  # [示例/Example] keyword = \"原神\" page = 1 page_size = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_all_api_v1_bilibili_app_fetch_search_all_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
        :param object page_size: 每页数量/Page size
        :param object order: 排序方式/Sort order (0=综合排序)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page', 'page_size', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_all_api_v1_bilibili_app_fetch_search_all_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_all_api_v1_bilibili_app_fetch_search_all_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_search_all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get(self, keyword, **kwargs):  # noqa: E501
        """分类搜索/ search by type  # noqa: E501

        # [中文] ### 用途: - 分类搜索（按类型搜索） ### 参数: - keyword: 搜索关键词（必填） - search_type: 搜索类型     - video: 视频     - bangumi: 番剧     - pgc: 影视     - live: 直播     - article: 专栏     - user: 用户 - page: 页码，从1开始 - page_size: 每页结果数量 - order: 排序方式     - 0: 综合排序     - 1: 最新发布     - 2: 播放量     - 3: 弹幕数 ### 返回: - 搜索结果  # [English] ### Purpose: -  search by type ### Parameters: - keyword: Search keyword (required) - search_type: Search type     - video: Videos     - bangumi: Anime     - pgc: Movies/TV     - live: Live streams     - article: Articles     - user: Users - page: Page number, starting from 1 - page_size: Results per page - order: Sort order     - 0: Comprehensive     - 1: Latest     - 2: Play count     - 3: Danmaku count ### Return: - Search results  # [示例/Example] keyword = \"原神\" search_type = \"video\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object search_type: 搜索类型/Search type (video/bangumi/pgc/live/article/user)
        :param object page: 页码/Page number
        :param object page_size: 每页数量/Page size
        :param object order: 排序方式/Sort order (0=综合, 1=最新, 2=播放量, 3=弹幕数)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """分类搜索/ search by type  # noqa: E501

        # [中文] ### 用途: - 分类搜索（按类型搜索） ### 参数: - keyword: 搜索关键词（必填） - search_type: 搜索类型     - video: 视频     - bangumi: 番剧     - pgc: 影视     - live: 直播     - article: 专栏     - user: 用户 - page: 页码，从1开始 - page_size: 每页结果数量 - order: 排序方式     - 0: 综合排序     - 1: 最新发布     - 2: 播放量     - 3: 弹幕数 ### 返回: - 搜索结果  # [English] ### Purpose: -  search by type ### Parameters: - keyword: Search keyword (required) - search_type: Search type     - video: Videos     - bangumi: Anime     - pgc: Movies/TV     - live: Live streams     - article: Articles     - user: Users - page: Page number, starting from 1 - page_size: Results per page - order: Sort order     - 0: Comprehensive     - 1: Latest     - 2: Play count     - 3: Danmaku count ### Return: - Search results  # [示例/Example] keyword = \"原神\" search_type = \"video\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object search_type: 搜索类型/Search type (video/bangumi/pgc/live/article/user)
        :param object page: 页码/Page number
        :param object page_size: 每页数量/Page size
        :param object order: 排序方式/Sort order (0=综合, 1=最新, 2=播放量, 3=弹幕数)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'search_type', 'page', 'page_size', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'search_type' in params:
            query_params.append(('search_type', params['search_type']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_search_by_type', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_api_v1_bilibili_app_fetch_user_info_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息/Get user info  # noqa: E501

        # [中文] ### 用途: - 获取用户信息 ### 参数: - user_id: 用户ID（必填） ### 返回: - 用户信息（包含粉丝数、关注数、投稿数等）  # [English] ### Purpose: - Get user info ### Parameters: - user_id: User ID (required) ### Return: - User info (including followers, following, videos count, etc.)  # [示例/Example] user_id = \"203680252\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_bilibili_app_fetch_user_info_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_bilibili_app_fetch_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_bilibili_app_fetch_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_bilibili_app_fetch_user_info_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息/Get user info  # noqa: E501

        # [中文] ### 用途: - 获取用户信息 ### 参数: - user_id: 用户ID（必填） ### 返回: - 用户信息（包含粉丝数、关注数、投稿数等）  # [English] ### Purpose: - Get user info ### Parameters: - user_id: User ID (required) ### Return: - User info (including followers, following, videos count, etc.)  # [示例/Example] user_id = \"203680252\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_bilibili_app_fetch_user_info_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_info_api_v1_bilibili_app_fetch_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_info_api_v1_bilibili_app_fetch_user_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_user_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户投稿视频/Get user videos  # noqa: E501

        # [中文] ### 用途: - 获取用户投稿视频列表 ### 参数: - user_id: 用户ID（必填） - post_filter: 过滤类型（archive=投稿, season=合集, contribute=贡献） - page: 页码 - ps: 每页数量 ### 返回: - 用户投稿视频列表  # [English] ### Purpose: - Get user uploaded videos ### Parameters: - user_id: User ID (required) - post_filter: Filter type (archive/season/contribute) - page: Page number - ps: Page size ### Return: - User videos data  # [示例/Example] user_id = \"203680252\" post_filter = \"archive\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object post_filter: 过滤类型/Filter type (archive/season/contribute)
        :param object page: 页码/Page number
        :param object ps: 每页数量/Page size
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户投稿视频/Get user videos  # noqa: E501

        # [中文] ### 用途: - 获取用户投稿视频列表 ### 参数: - user_id: 用户ID（必填） - post_filter: 过滤类型（archive=投稿, season=合集, contribute=贡献） - page: 页码 - ps: 每页数量 ### 返回: - 用户投稿视频列表  # [English] ### Purpose: - Get user uploaded videos ### Parameters: - user_id: User ID (required) - post_filter: Filter type (archive/season/contribute) - page: Page number - ps: Page size ### Return: - User videos data  # [示例/Example] user_id = \"203680252\" post_filter = \"archive\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object post_filter: 过滤类型/Filter type (archive/season/contribute)
        :param object page: 页码/Page number
        :param object ps: 每页数量/Page size
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'post_filter', 'page', 'ps']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'post_filter' in params:
            query_params.append(('post_filter', params['post_filter']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'ps' in params:
            query_params.append(('ps', params['ps']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_user_videos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get(self, **kwargs):  # noqa: E501
        """获取视频评论列表/Get video comments  # noqa: E501

        # [中文] ### 用途: - 获取视频评论列表 ### 参数: - av_id: AV号（与bv_id二选一） - bv_id: BV号（与av_id二选一） - mode: 排序模式（3=热门, 2=时间） - next_offset: 分页游标 ### 返回: - 评论列表数据  # [English] ### Purpose: - Get video comments ### Parameters: - av_id: AV ID (choose one of av_id or bv_id) - bv_id: BV ID (choose one of av_id or bv_id) - mode: Sort mode (3=hot, 2=time) - next_offset: Pagination cursor ### Return: - Comments data  # [示例/Example] bv_id = \"BV18SCrBGE9E\" mode = 3 next_offset = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object av_id: AV号/AV ID
        :param object bv_id: BV号/BV ID
        :param object mode: 排序模式/Sort mode (3=热门/hot, 2=时间/time)
        :param object next_offset: 分页游标/Pagination cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取视频评论列表/Get video comments  # noqa: E501

        # [中文] ### 用途: - 获取视频评论列表 ### 参数: - av_id: AV号（与bv_id二选一） - bv_id: BV号（与av_id二选一） - mode: 排序模式（3=热门, 2=时间） - next_offset: 分页游标 ### 返回: - 评论列表数据  # [English] ### Purpose: - Get video comments ### Parameters: - av_id: AV ID (choose one of av_id or bv_id) - bv_id: BV ID (choose one of av_id or bv_id) - mode: Sort mode (3=hot, 2=time) - next_offset: Pagination cursor ### Return: - Comments data  # [示例/Example] bv_id = \"BV18SCrBGE9E\" mode = 3 next_offset = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object av_id: AV号/AV ID
        :param object bv_id: BV号/BV ID
        :param object mode: 排序模式/Sort mode (3=热门/hot, 2=时间/time)
        :param object next_offset: 分页游标/Pagination cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['av_id', 'bv_id', 'mode', 'next_offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'av_id' in params:
            query_params.append(('av_id', params['av_id']))  # noqa: E501
        if 'bv_id' in params:
            query_params.append(('bv_id', params['bv_id']))  # noqa: E501
        if 'mode' in params:
            query_params.append(('mode', params['mode']))  # noqa: E501
        if 'next_offset' in params:
            query_params.append(('next_offset', params['next_offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/app/fetch_video_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
