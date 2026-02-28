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


class BilibiliWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_collect_folders_api_v1_bilibili_web_fetch_all_live_areas_get(self, **kwargs):  # noqa: E501
        """获取所有直播分区列表/Get a list of all live areas  # noqa: E501

        # [中文] ### 用途: - 获取所有直播分区列表 ### 参数: ### 返回: - 所有直播分区列表  # [English] ### Purpose: - Get a list of all live areas ### Parameters: ### Return: - list of all live areas  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_all_live_areas_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_collect_folders_api_v1_bilibili_web_fetch_all_live_areas_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_collect_folders_api_v1_bilibili_web_fetch_all_live_areas_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_collect_folders_api_v1_bilibili_web_fetch_all_live_areas_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取所有直播分区列表/Get a list of all live areas  # noqa: E501

        # [中文] ### 用途: - 获取所有直播分区列表 ### 参数: ### 返回: - 所有直播分区列表  # [English] ### Purpose: - Get a list of all live areas ### Parameters: ### Return: - list of all live areas  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_all_live_areas_get_with_http_info(async_req=True)
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
                    " to method fetch_collect_folders_api_v1_bilibili_web_fetch_all_live_areas_get" % key
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
            '/api/v1/bilibili/web/fetch_all_live_areas', 'GET',
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

    def fetch_collect_folders_api_v1_bilibili_web_fetch_collect_folders_get(self, uid, **kwargs):  # noqa: E501
        """获取用户所有收藏夹信息/Get user collection folders  # noqa: E501

        # [中文] ### 用途: - 获取用户收藏作品数据 ### 参数: - uid: 用户UID ### 返回: - 用户收藏夹信息  # [English] ### Purpose: - Get user collection folders ### Parameters: - uid: User UID ### Return: - user collection folders  # [示例/Example] uid = \"178360345\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_collect_folders_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_collect_folders_api_v1_bilibili_web_fetch_collect_folders_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_collect_folders_api_v1_bilibili_web_fetch_collect_folders_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_collect_folders_api_v1_bilibili_web_fetch_collect_folders_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户所有收藏夹信息/Get user collection folders  # noqa: E501

        # [中文] ### 用途: - 获取用户收藏作品数据 ### 参数: - uid: 用户UID ### 返回: - 用户收藏夹信息  # [English] ### Purpose: - Get user collection folders ### Parameters: - uid: User UID ### Return: - user collection folders  # [示例/Example] uid = \"178360345\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_collect_folders_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_collect_folders_api_v1_bilibili_web_fetch_collect_folders_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_collect_folders_api_v1_bilibili_web_fetch_collect_folders_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_collect_folders', 'GET',
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

    def fetch_collect_folders_api_v1_bilibili_web_fetch_com_popular_get(self, **kwargs):  # noqa: E501
        """获取综合热门视频信息/Get comprehensive popular video information  # noqa: E501

        # [中文] ### 用途: - 获取综合热门视频信息 ### 参数: - pn: 页码 ### 返回: - 综合热门视频信息  # [English] ### Purpose: - Get comprehensive popular video information ### Parameters: - pn: Page number ### Return: - comprehensive popular video information  # [示例/Example] pn = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_com_popular_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object pn: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_collect_folders_api_v1_bilibili_web_fetch_com_popular_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_collect_folders_api_v1_bilibili_web_fetch_com_popular_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_collect_folders_api_v1_bilibili_web_fetch_com_popular_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取综合热门视频信息/Get comprehensive popular video information  # noqa: E501

        # [中文] ### 用途: - 获取综合热门视频信息 ### 参数: - pn: 页码 ### 返回: - 综合热门视频信息  # [English] ### Purpose: - Get comprehensive popular video information ### Parameters: - pn: Page number ### Return: - comprehensive popular video information  # [示例/Example] pn = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_com_popular_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object pn: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_collect_folders_api_v1_bilibili_web_fetch_com_popular_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pn' in params:
            query_params.append(('pn', params['pn']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_com_popular', 'GET',
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

    def fetch_collect_folders_api_v1_bilibili_web_fetch_comment_reply_get(self, bv_id, rpid, **kwargs):  # noqa: E501
        """获取视频下指定评论的回复/Get reply to the specified comment  # noqa: E501

        # [中文] ### 用途: - 获取视频下指定评论的回复 ### 参数: - bv_id: 作品id - pn: 页码 - rpid: 回复id ### 返回: - 指定评论的回复数据  # [English] ### Purpose: - Get reply to the specified comment ### Parameters: - bv_id: Video id - pn: Page number - rpid: Reply id ### Return: - Reply of the specified comment  # [示例/Example] bv_id = \"BV1M1421t7hT\" pn = 1 rpid = \"237109455120\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_comment_reply_get(bv_id, rpid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :param object rpid: 回复id/Reply id (required)
        :param object pn: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_collect_folders_api_v1_bilibili_web_fetch_comment_reply_get_with_http_info(bv_id, rpid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_collect_folders_api_v1_bilibili_web_fetch_comment_reply_get_with_http_info(bv_id, rpid, **kwargs)  # noqa: E501
            return data

    def fetch_collect_folders_api_v1_bilibili_web_fetch_comment_reply_get_with_http_info(self, bv_id, rpid, **kwargs):  # noqa: E501
        """获取视频下指定评论的回复/Get reply to the specified comment  # noqa: E501

        # [中文] ### 用途: - 获取视频下指定评论的回复 ### 参数: - bv_id: 作品id - pn: 页码 - rpid: 回复id ### 返回: - 指定评论的回复数据  # [English] ### Purpose: - Get reply to the specified comment ### Parameters: - bv_id: Video id - pn: Page number - rpid: Reply id ### Return: - Reply of the specified comment  # [示例/Example] bv_id = \"BV1M1421t7hT\" pn = 1 rpid = \"237109455120\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_comment_reply_get_with_http_info(bv_id, rpid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :param object rpid: 回复id/Reply id (required)
        :param object pn: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bv_id', 'rpid', 'pn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_collect_folders_api_v1_bilibili_web_fetch_comment_reply_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bv_id' is set
        if self.api_client.client_side_validation and ('bv_id' not in params or
                                                       params['bv_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bv_id` when calling `fetch_collect_folders_api_v1_bilibili_web_fetch_comment_reply_get`")  # noqa: E501
        # verify the required parameter 'rpid' is set
        if self.api_client.client_side_validation and ('rpid' not in params or
                                                       params['rpid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `rpid` when calling `fetch_collect_folders_api_v1_bilibili_web_fetch_comment_reply_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bv_id' in params:
            query_params.append(('bv_id', params['bv_id']))  # noqa: E501
        if 'pn' in params:
            query_params.append(('pn', params['pn']))  # noqa: E501
        if 'rpid' in params:
            query_params.append(('rpid', params['rpid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_comment_reply', 'GET',
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

    def fetch_collect_folders_api_v1_bilibili_web_fetch_live_room_detail_get(self, room_id, **kwargs):  # noqa: E501
        """获取指定直播间信息/Get information of specified live room  # noqa: E501

        # [中文] ### 用途: - 获取指定直播间信息 ### 参数: - room_id: 直播间ID ### 返回: - 指定直播间信息  # [English] ### Purpose: - Get information of specified live room ### Parameters: - room_id: Live room ID ### Return: - information of specified live room  # [示例/Example] room_id = \"22816111\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_live_room_detail_get(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间ID/Live room ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_collect_folders_api_v1_bilibili_web_fetch_live_room_detail_get_with_http_info(room_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_collect_folders_api_v1_bilibili_web_fetch_live_room_detail_get_with_http_info(room_id, **kwargs)  # noqa: E501
            return data

    def fetch_collect_folders_api_v1_bilibili_web_fetch_live_room_detail_get_with_http_info(self, room_id, **kwargs):  # noqa: E501
        """获取指定直播间信息/Get information of specified live room  # noqa: E501

        # [中文] ### 用途: - 获取指定直播间信息 ### 参数: - room_id: 直播间ID ### 返回: - 指定直播间信息  # [English] ### Purpose: - Get information of specified live room ### Parameters: - room_id: Live room ID ### Return: - information of specified live room  # [示例/Example] room_id = \"22816111\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_live_room_detail_get_with_http_info(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间ID/Live room ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_collect_folders_api_v1_bilibili_web_fetch_live_room_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_collect_folders_api_v1_bilibili_web_fetch_live_room_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_live_room_detail', 'GET',
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

    def fetch_collect_folders_api_v1_bilibili_web_fetch_live_streamers_get(self, area_id, **kwargs):  # noqa: E501
        """获取指定分区正在直播的主播/Get live streamers of specified live area  # noqa: E501

        # [中文] ### 用途: - 获取指定分区正在直播的主播 ### 参数: - area_id: 直播分区id - pn: 页码 ### 返回: - 指定分区正在直播的主播  # [English] ### Purpose: - Get live streamers of specified live area ### Parameters: - area_id: Live area ID - pn: Page number ### Return: - live streamers of specified live area  # [示例/Example] area_id = \"9\" pn = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_live_streamers_get(area_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object area_id: 直播分区id/Live area ID (required)
        :param object pn: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_collect_folders_api_v1_bilibili_web_fetch_live_streamers_get_with_http_info(area_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_collect_folders_api_v1_bilibili_web_fetch_live_streamers_get_with_http_info(area_id, **kwargs)  # noqa: E501
            return data

    def fetch_collect_folders_api_v1_bilibili_web_fetch_live_streamers_get_with_http_info(self, area_id, **kwargs):  # noqa: E501
        """获取指定分区正在直播的主播/Get live streamers of specified live area  # noqa: E501

        # [中文] ### 用途: - 获取指定分区正在直播的主播 ### 参数: - area_id: 直播分区id - pn: 页码 ### 返回: - 指定分区正在直播的主播  # [English] ### Purpose: - Get live streamers of specified live area ### Parameters: - area_id: Live area ID - pn: Page number ### Return: - live streamers of specified live area  # [示例/Example] area_id = \"9\" pn = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_live_streamers_get_with_http_info(area_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object area_id: 直播分区id/Live area ID (required)
        :param object pn: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['area_id', 'pn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_collect_folders_api_v1_bilibili_web_fetch_live_streamers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'area_id' is set
        if self.api_client.client_side_validation and ('area_id' not in params or
                                                       params['area_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `area_id` when calling `fetch_collect_folders_api_v1_bilibili_web_fetch_live_streamers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'area_id' in params:
            query_params.append(('area_id', params['area_id']))  # noqa: E501
        if 'pn' in params:
            query_params.append(('pn', params['pn']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_live_streamers', 'GET',
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

    def fetch_collect_folders_api_v1_bilibili_web_fetch_live_videos_get(self, room_id, **kwargs):  # noqa: E501
        """获取直播间视频流/Get live video data of specified room  # noqa: E501

        # [中文] ### 用途: - 获取指定直播间视频流 ### 参数: - room_id: 直播间ID ### 返回: - 指定直播间视频流  # [English] ### Purpose: - Get live video data of specified room ### Parameters: - room_id: Live room ID ### Return: - live video data of specified room  # [示例/Example] room_id = \"1815229528\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_live_videos_get(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间ID/Live room ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_collect_folders_api_v1_bilibili_web_fetch_live_videos_get_with_http_info(room_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_collect_folders_api_v1_bilibili_web_fetch_live_videos_get_with_http_info(room_id, **kwargs)  # noqa: E501
            return data

    def fetch_collect_folders_api_v1_bilibili_web_fetch_live_videos_get_with_http_info(self, room_id, **kwargs):  # noqa: E501
        """获取直播间视频流/Get live video data of specified room  # noqa: E501

        # [中文] ### 用途: - 获取指定直播间视频流 ### 参数: - room_id: 直播间ID ### 返回: - 指定直播间视频流  # [English] ### Purpose: - Get live video data of specified room ### Parameters: - room_id: Live room ID ### Return: - live video data of specified room  # [示例/Example] room_id = \"1815229528\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_live_videos_get_with_http_info(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间ID/Live room ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_collect_folders_api_v1_bilibili_web_fetch_live_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_collect_folders_api_v1_bilibili_web_fetch_live_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_live_videos', 'GET',
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

    def fetch_collect_folders_api_v1_bilibili_web_fetch_user_dynamic_get(self, uid, **kwargs):  # noqa: E501
        """获取指定用户动态/Get dynamic information of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户动态 ### 参数: - uid: 用户UID - offset: 开始索引 ### 返回: - 指定用户动态数据  # [English] ### Purpose: - Get dynamic information of specified user ### Parameters: - uid: User UID - offset: offset ### Return: - dynamic information of specified user  # [示例/Example] uid = \"178360345\" offset = \"953154282154098691\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_user_dynamic_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID (required)
        :param object offset: 开始索引/offset
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_collect_folders_api_v1_bilibili_web_fetch_user_dynamic_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_collect_folders_api_v1_bilibili_web_fetch_user_dynamic_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_collect_folders_api_v1_bilibili_web_fetch_user_dynamic_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取指定用户动态/Get dynamic information of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户动态 ### 参数: - uid: 用户UID - offset: 开始索引 ### 返回: - 指定用户动态数据  # [English] ### Purpose: - Get dynamic information of specified user ### Parameters: - uid: User UID - offset: offset ### Return: - dynamic information of specified user  # [示例/Example] uid = \"178360345\" offset = \"953154282154098691\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_user_dynamic_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID (required)
        :param object offset: 开始索引/offset
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_collect_folders_api_v1_bilibili_web_fetch_user_dynamic_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_collect_folders_api_v1_bilibili_web_fetch_user_dynamic_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_user_dynamic', 'GET',
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

    def fetch_collect_folders_api_v1_bilibili_web_fetch_user_profile_get(self, uid, **kwargs):  # noqa: E501
        """获取指定用户的信息/Get information of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - uid: 用户UID ### 返回: - 指定用户的个人信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - uid: User UID ### Return: - information of specified user  # [示例/Example] uid = \"178360345\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_user_profile_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_collect_folders_api_v1_bilibili_web_fetch_user_profile_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_collect_folders_api_v1_bilibili_web_fetch_user_profile_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_collect_folders_api_v1_bilibili_web_fetch_user_profile_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取指定用户的信息/Get information of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - uid: 用户UID ### 返回: - 指定用户的个人信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - uid: User UID ### Return: - information of specified user  # [示例/Example] uid = \"178360345\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_user_profile_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_collect_folders_api_v1_bilibili_web_fetch_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_collect_folders_api_v1_bilibili_web_fetch_user_profile_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_user_profile', 'GET',
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

    def fetch_collect_folders_api_v1_bilibili_web_fetch_video_comments_get(self, bv_id, **kwargs):  # noqa: E501
        """获取指定视频的评论/Get comments on the specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的评论 ### 参数: - bv_id: 作品id - pn: 页码 ### 返回: - 指定视频的评论数据  # [English] ### Purpose: - Get comments on the specified video ### Parameters: - bv_id: Video id - pn: Page number ### Return: - comments of the specified video  # [示例/Example] bv_id = \"BV1M1421t7hT\" pn = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_video_comments_get(bv_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :param object pn: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_collect_folders_api_v1_bilibili_web_fetch_video_comments_get_with_http_info(bv_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_collect_folders_api_v1_bilibili_web_fetch_video_comments_get_with_http_info(bv_id, **kwargs)  # noqa: E501
            return data

    def fetch_collect_folders_api_v1_bilibili_web_fetch_video_comments_get_with_http_info(self, bv_id, **kwargs):  # noqa: E501
        """获取指定视频的评论/Get comments on the specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的评论 ### 参数: - bv_id: 作品id - pn: 页码 ### 返回: - 指定视频的评论数据  # [English] ### Purpose: - Get comments on the specified video ### Parameters: - bv_id: Video id - pn: Page number ### Return: - comments of the specified video  # [示例/Example] bv_id = \"BV1M1421t7hT\" pn = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_collect_folders_api_v1_bilibili_web_fetch_video_comments_get_with_http_info(bv_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :param object pn: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bv_id', 'pn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_collect_folders_api_v1_bilibili_web_fetch_video_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bv_id' is set
        if self.api_client.client_side_validation and ('bv_id' not in params or
                                                       params['bv_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bv_id` when calling `fetch_collect_folders_api_v1_bilibili_web_fetch_video_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bv_id' in params:
            query_params.append(('bv_id', params['bv_id']))  # noqa: E501
        if 'pn' in params:
            query_params.append(('pn', params['pn']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_video_comments', 'GET',
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

    def fetch_general_search_api_v1_bilibili_web_fetch_general_search_get(self, keyword, order, page, page_size, **kwargs):  # noqa: E501
        """获取综合搜索信息/Get general search data  # noqa: E501

        # [中文] ### 用途: - 获取综合搜索信息 ### 参数: - keyword: 搜索关键词 - order: 排序方式     - totalrank 综合排序     - click 最多播放     - pubdate 最新发布     - dm 最多弹幕     - stow 最多收藏 - page: 页码 - page_size: 每页数量 - duration: 时长筛选     - 0 全部时长     - 1 10分钟以下     - 2 10-30分钟     - 3 30分钟-60分钟     - 4 60分钟以上 - pubtime_begin_s: 开始日期，10位时间戳，需要小于结束日期 - pubtime_end_s: 结束日期，10位时间戳，需要大于开始日期 ### 返回: - 综合搜索信息  # [English] ### Purpose: - Get general search data ### Parameters: - keyword: Search keyword - order: Order method     - totalrank Comprehensive sorting     - click Most played     - pubdate Latest release     - dm Most barrage     - stow Most collection - page: Page number - page_size: Number per page - duration: Duration filter     - 0 All durations     - 1 Under 10 minutes     - 2 10-30 minutes     - 3 30-60 minutes     - 4 Over 60 minutes - pubtime_begin_s: Start date, 10-digit timestamp, must be less than end date - pubtime_end_s: End date, 10-digit timestamp, must be greater than start date ### Return: - General search data  # [示例/Example] keyword = \"火影忍者\" order = \"totalrank\" page = 1 page_size = 42 duration = 0 pubtime_begin_s = 0 pubtime_end_s = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_general_search_api_v1_bilibili_web_fetch_general_search_get(keyword, order, page, page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object order: 排序方式/Order method (required)
        :param object page: 页码/Page number (required)
        :param object page_size: 每页数量/Number per page (required)
        :param object duration: 时长筛选/Duration filter
        :param object pubtime_begin_s: 开始日期/Start date (10-digit timestamp)
        :param object pubtime_end_s: 结束日期/End date (10-digit timestamp)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_general_search_api_v1_bilibili_web_fetch_general_search_get_with_http_info(keyword, order, page, page_size, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_general_search_api_v1_bilibili_web_fetch_general_search_get_with_http_info(keyword, order, page, page_size, **kwargs)  # noqa: E501
            return data

    def fetch_general_search_api_v1_bilibili_web_fetch_general_search_get_with_http_info(self, keyword, order, page, page_size, **kwargs):  # noqa: E501
        """获取综合搜索信息/Get general search data  # noqa: E501

        # [中文] ### 用途: - 获取综合搜索信息 ### 参数: - keyword: 搜索关键词 - order: 排序方式     - totalrank 综合排序     - click 最多播放     - pubdate 最新发布     - dm 最多弹幕     - stow 最多收藏 - page: 页码 - page_size: 每页数量 - duration: 时长筛选     - 0 全部时长     - 1 10分钟以下     - 2 10-30分钟     - 3 30分钟-60分钟     - 4 60分钟以上 - pubtime_begin_s: 开始日期，10位时间戳，需要小于结束日期 - pubtime_end_s: 结束日期，10位时间戳，需要大于开始日期 ### 返回: - 综合搜索信息  # [English] ### Purpose: - Get general search data ### Parameters: - keyword: Search keyword - order: Order method     - totalrank Comprehensive sorting     - click Most played     - pubdate Latest release     - dm Most barrage     - stow Most collection - page: Page number - page_size: Number per page - duration: Duration filter     - 0 All durations     - 1 Under 10 minutes     - 2 10-30 minutes     - 3 30-60 minutes     - 4 Over 60 minutes - pubtime_begin_s: Start date, 10-digit timestamp, must be less than end date - pubtime_end_s: End date, 10-digit timestamp, must be greater than start date ### Return: - General search data  # [示例/Example] keyword = \"火影忍者\" order = \"totalrank\" page = 1 page_size = 42 duration = 0 pubtime_begin_s = 0 pubtime_end_s = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_general_search_api_v1_bilibili_web_fetch_general_search_get_with_http_info(keyword, order, page, page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object order: 排序方式/Order method (required)
        :param object page: 页码/Page number (required)
        :param object page_size: 每页数量/Number per page (required)
        :param object duration: 时长筛选/Duration filter
        :param object pubtime_begin_s: 开始日期/Start date (10-digit timestamp)
        :param object pubtime_end_s: 结束日期/End date (10-digit timestamp)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'order', 'page', 'page_size', 'duration', 'pubtime_begin_s', 'pubtime_end_s']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_general_search_api_v1_bilibili_web_fetch_general_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_general_search_api_v1_bilibili_web_fetch_general_search_get`")  # noqa: E501
        # verify the required parameter 'order' is set
        if self.api_client.client_side_validation and ('order' not in params or
                                                       params['order'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `order` when calling `fetch_general_search_api_v1_bilibili_web_fetch_general_search_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if self.api_client.client_side_validation and ('page' not in params or
                                                       params['page'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page` when calling `fetch_general_search_api_v1_bilibili_web_fetch_general_search_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if self.api_client.client_side_validation and ('page_size' not in params or
                                                       params['page_size'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page_size` when calling `fetch_general_search_api_v1_bilibili_web_fetch_general_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'duration' in params:
            query_params.append(('duration', params['duration']))  # noqa: E501
        if 'pubtime_begin_s' in params:
            query_params.append(('pubtime_begin_s', params['pubtime_begin_s']))  # noqa: E501
        if 'pubtime_end_s' in params:
            query_params.append(('pubtime_end_s', params['pubtime_end_s']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_general_search', 'GET',
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

    def fetch_get_user_id_api_v1_bilibili_web_fetch_get_user_id_get(self, share_link, **kwargs):  # noqa: E501
        """提取用户ID/Extract user ID  # noqa: E501

        # [中文] ### 用途: - 提取用户ID ### 参数: - share_link: 用户分享链接 ### 返回: - 用户ID  # [English] ### Purpose: - Extract user ID ### Parameters: - share_link: User share link ### Return: - User ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_get_user_id_api_v1_bilibili_web_fetch_get_user_id_get(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: 用户分享链接/User share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_get_user_id_api_v1_bilibili_web_fetch_get_user_id_get_with_http_info(share_link, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_get_user_id_api_v1_bilibili_web_fetch_get_user_id_get_with_http_info(share_link, **kwargs)  # noqa: E501
            return data

    def fetch_get_user_id_api_v1_bilibili_web_fetch_get_user_id_get_with_http_info(self, share_link, **kwargs):  # noqa: E501
        """提取用户ID/Extract user ID  # noqa: E501

        # [中文] ### 用途: - 提取用户ID ### 参数: - share_link: 用户分享链接 ### 返回: - 用户ID  # [English] ### Purpose: - Extract user ID ### Parameters: - share_link: User share link ### Return: - User ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_get_user_id_api_v1_bilibili_web_fetch_get_user_id_get_with_http_info(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: 用户分享链接/User share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['share_link']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_get_user_id_api_v1_bilibili_web_fetch_get_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_link' is set
        if self.api_client.client_side_validation and ('share_link' not in params or
                                                       params['share_link'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_link` when calling `fetch_get_user_id_api_v1_bilibili_web_fetch_get_user_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_link' in params:
            query_params.append(('share_link', params['share_link']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_get_user_id', 'GET',
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

    def fetch_hot_search_api_v1_bilibili_web_fetch_hot_search_get(self, limit, **kwargs):  # noqa: E501
        """获取热门搜索信息/Get hot search data  # noqa: E501

        # [中文] ### 用途: - 获取热门搜索信息 ### 参数: - limit: 返回数量 ### 返回: - 热门搜索信息 ### 说明: - limit默认为10，上限为50  # [English] ### Purpose: - Get hot search data ### Parameters: - limit: Return number ### Return: - Hot search data ### Note: - limit default is 10, maximum is 50  # [示例/Example] limit = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_api_v1_bilibili_web_fetch_hot_search_get(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit: 返回数量/Return number (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_api_v1_bilibili_web_fetch_hot_search_get_with_http_info(limit, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_api_v1_bilibili_web_fetch_hot_search_get_with_http_info(limit, **kwargs)  # noqa: E501
            return data

    def fetch_hot_search_api_v1_bilibili_web_fetch_hot_search_get_with_http_info(self, limit, **kwargs):  # noqa: E501
        """获取热门搜索信息/Get hot search data  # noqa: E501

        # [中文] ### 用途: - 获取热门搜索信息 ### 参数: - limit: 返回数量 ### 返回: - 热门搜索信息 ### 说明: - limit默认为10，上限为50  # [English] ### Purpose: - Get hot search data ### Parameters: - limit: Return number ### Return: - Hot search data ### Note: - limit default is 10, maximum is 50  # [示例/Example] limit = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_api_v1_bilibili_web_fetch_hot_search_get_with_http_info(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit: 返回数量/Return number (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_search_api_v1_bilibili_web_fetch_hot_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if self.api_client.client_side_validation and ('limit' not in params or
                                                       params['limit'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `limit` when calling `fetch_hot_search_api_v1_bilibili_web_fetch_hot_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_hot_search', 'GET',
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

    def fetch_one_video_api_v1_bilibili_web_bv_to_aid_get(self, bv_id, **kwargs):  # noqa: E501
        """通过bv号获得视频aid号/Generate aid by bvid  # noqa: E501

        # [中文] ### 用途: - 通过bv号获得视频aid号 ### 参数: - bv_id: 作品id ### 返回: - 视频aid号  # [English] ### Purpose: - Generate aid by bvid ### Parameters: - bv_id: Video id ### Return: - Video aid  # [示例/Example] bv_id = \"BV1M1421t7hT\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_web_bv_to_aid_get(bv_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_bilibili_web_bv_to_aid_get_with_http_info(bv_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_bilibili_web_bv_to_aid_get_with_http_info(bv_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_bilibili_web_bv_to_aid_get_with_http_info(self, bv_id, **kwargs):  # noqa: E501
        """通过bv号获得视频aid号/Generate aid by bvid  # noqa: E501

        # [中文] ### 用途: - 通过bv号获得视频aid号 ### 参数: - bv_id: 作品id ### 返回: - 视频aid号  # [English] ### Purpose: - Generate aid by bvid ### Parameters: - bv_id: Video id ### Return: - Video aid  # [示例/Example] bv_id = \"BV1M1421t7hT\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_web_bv_to_aid_get_with_http_info(bv_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bv_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_api_v1_bilibili_web_bv_to_aid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bv_id' is set
        if self.api_client.client_side_validation and ('bv_id' not in params or
                                                       params['bv_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bv_id` when calling `fetch_one_video_api_v1_bilibili_web_bv_to_aid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bv_id' in params:
            query_params.append(('bv_id', params['bv_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/bv_to_aid', 'GET',
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

    def fetch_one_video_api_v1_bilibili_web_fetch_one_video_get(self, bv_id, **kwargs):  # noqa: E501
        """获取单个视频详情信息/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个视频详情信息 ### 参数: - bv_id: 作品id ### 返回: - 视频详情信息  # [English] ### Purpose: - Get single video data ### Parameters: - bv_id: Video id ### Return: - Video data  # [示例/Example] bv_id = \"BV1M1421t7hT\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_web_fetch_one_video_get(bv_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_bilibili_web_fetch_one_video_get_with_http_info(bv_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_bilibili_web_fetch_one_video_get_with_http_info(bv_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_bilibili_web_fetch_one_video_get_with_http_info(self, bv_id, **kwargs):  # noqa: E501
        """获取单个视频详情信息/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个视频详情信息 ### 参数: - bv_id: 作品id ### 返回: - 视频详情信息  # [English] ### Purpose: - Get single video data ### Parameters: - bv_id: Video id ### Return: - Video data  # [示例/Example] bv_id = \"BV1M1421t7hT\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_web_fetch_one_video_get_with_http_info(bv_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bv_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_api_v1_bilibili_web_fetch_one_video_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bv_id' is set
        if self.api_client.client_side_validation and ('bv_id' not in params or
                                                       params['bv_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bv_id` when calling `fetch_one_video_api_v1_bilibili_web_fetch_one_video_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bv_id' in params:
            query_params.append(('bv_id', params['bv_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_one_video', 'GET',
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

    def fetch_one_video_api_v1_bilibili_web_fetch_video_danmaku_get(self, cid, **kwargs):  # noqa: E501
        """获取视频实时弹幕/Get Video Danmaku  # noqa: E501

        # [中文] ### 用途: - 获取视频实时弹幕 ### 参数: - cid: 作品cid ### 返回: - 视频实时弹幕  # [English] ### Purpose: - Get Video Danmaku ### Parameters: - cid: Video cid ### Return: - Video Danmaku  # [示例/Example] cid = \"1639235405\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_web_fetch_video_danmaku_get(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cid: 作品cid/Video cid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_bilibili_web_fetch_video_danmaku_get_with_http_info(cid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_bilibili_web_fetch_video_danmaku_get_with_http_info(cid, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_bilibili_web_fetch_video_danmaku_get_with_http_info(self, cid, **kwargs):  # noqa: E501
        """获取视频实时弹幕/Get Video Danmaku  # noqa: E501

        # [中文] ### 用途: - 获取视频实时弹幕 ### 参数: - cid: 作品cid ### 返回: - 视频实时弹幕  # [English] ### Purpose: - Get Video Danmaku ### Parameters: - cid: Video cid ### Return: - Video Danmaku  # [示例/Example] cid = \"1639235405\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_web_fetch_video_danmaku_get_with_http_info(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cid: 作品cid/Video cid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_api_v1_bilibili_web_fetch_video_danmaku_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cid' is set
        if self.api_client.client_side_validation and ('cid' not in params or
                                                       params['cid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cid` when calling `fetch_one_video_api_v1_bilibili_web_fetch_video_danmaku_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cid' in params:
            query_params.append(('cid', params['cid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_video_danmaku', 'GET',
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

    def fetch_one_video_api_v1_bilibili_web_fetch_video_parts_get(self, bv_id, **kwargs):  # noqa: E501
        """通过bv号获得视频分p信息/Get Video Parts By bvid  # noqa: E501

        # [中文] ### 用途: - 通过bv号获得视频分p信息 ### 参数: - bv_id: 作品id ### 返回: - 视频分p信息  # [English] ### Purpose: - Get Video Parts By bvid ### Parameters: - bv_id: Video id ### Return: - Video Parts  # [示例/Example] bv_id = \"BV1vf421i7hV\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_web_fetch_video_parts_get(bv_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_bilibili_web_fetch_video_parts_get_with_http_info(bv_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_bilibili_web_fetch_video_parts_get_with_http_info(bv_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_bilibili_web_fetch_video_parts_get_with_http_info(self, bv_id, **kwargs):  # noqa: E501
        """通过bv号获得视频分p信息/Get Video Parts By bvid  # noqa: E501

        # [中文] ### 用途: - 通过bv号获得视频分p信息 ### 参数: - bv_id: 作品id ### 返回: - 视频分p信息  # [English] ### Purpose: - Get Video Parts By bvid ### Parameters: - bv_id: Video id ### Return: - Video Parts  # [示例/Example] bv_id = \"BV1vf421i7hV\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_web_fetch_video_parts_get_with_http_info(bv_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bv_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_api_v1_bilibili_web_fetch_video_parts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bv_id' is set
        if self.api_client.client_side_validation and ('bv_id' not in params or
                                                       params['bv_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bv_id` when calling `fetch_one_video_api_v1_bilibili_web_fetch_video_parts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bv_id' in params:
            query_params.append(('bv_id', params['bv_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_video_parts', 'GET',
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

    def fetch_one_video_api_v1_bilibili_web_fetch_video_playurl_get(self, bv_id, cid, **kwargs):  # noqa: E501
        """获取视频流地址/Get video playurl  # noqa: E501

        # [中文] ### 用途: - 获取视频流地址 ### 参数: - bv_id: 作品id - cid: 作品cid ### 返回: - 视频流地址  # [English] ### Purpose: - Get video playurl ### Parameters: - bv_id: Video id - cid: Video cid ### Return: - Video playurl  # [示例/Example] bv_id = \"BV1y7411Q7Eq\" cid = \"171776208\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_web_fetch_video_playurl_get(bv_id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :param object cid: 作品cid/Video cid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_bilibili_web_fetch_video_playurl_get_with_http_info(bv_id, cid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_bilibili_web_fetch_video_playurl_get_with_http_info(bv_id, cid, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_bilibili_web_fetch_video_playurl_get_with_http_info(self, bv_id, cid, **kwargs):  # noqa: E501
        """获取视频流地址/Get video playurl  # noqa: E501

        # [中文] ### 用途: - 获取视频流地址 ### 参数: - bv_id: 作品id - cid: 作品cid ### 返回: - 视频流地址  # [English] ### Purpose: - Get video playurl ### Parameters: - bv_id: Video id - cid: Video cid ### Return: - Video playurl  # [示例/Example] bv_id = \"BV1y7411Q7Eq\" cid = \"171776208\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_bilibili_web_fetch_video_playurl_get_with_http_info(bv_id, cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object bv_id: 作品id/Video id (required)
        :param object cid: 作品cid/Video cid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bv_id', 'cid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_api_v1_bilibili_web_fetch_video_playurl_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bv_id' is set
        if self.api_client.client_side_validation and ('bv_id' not in params or
                                                       params['bv_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bv_id` when calling `fetch_one_video_api_v1_bilibili_web_fetch_video_playurl_get`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if self.api_client.client_side_validation and ('cid' not in params or
                                                       params['cid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cid` when calling `fetch_one_video_api_v1_bilibili_web_fetch_video_playurl_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bv_id' in params:
            query_params.append(('bv_id', params['bv_id']))  # noqa: E501
        if 'cid' in params:
            query_params.append(('cid', params['cid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_video_playurl', 'GET',
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

    def fetch_one_video_v2_api_v1_bilibili_web_fetch_one_video_v2_get(self, a_id, c_id, **kwargs):  # noqa: E501
        """获取单个视频详情信息V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个视频详情信息V2 ### 参数: - a_id: 作品id - c_id: 作品cid ### 返回: - 视频详情信息V2  # [English] ### Purpose: - Get single video data V2 ### Parameters: - a_id: Video id - c_id: Video cid ### Return: - Video data V2  # [示例/Example] a_id = \"114006081739452\" c_id = \"28400484458\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v2_api_v1_bilibili_web_fetch_one_video_v2_get(a_id, c_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object a_id: 作品id/Video id (required)
        :param object c_id: 作品cid/Video cid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_v2_api_v1_bilibili_web_fetch_one_video_v2_get_with_http_info(a_id, c_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_v2_api_v1_bilibili_web_fetch_one_video_v2_get_with_http_info(a_id, c_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_v2_api_v1_bilibili_web_fetch_one_video_v2_get_with_http_info(self, a_id, c_id, **kwargs):  # noqa: E501
        """获取单个视频详情信息V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个视频详情信息V2 ### 参数: - a_id: 作品id - c_id: 作品cid ### 返回: - 视频详情信息V2  # [English] ### Purpose: - Get single video data V2 ### Parameters: - a_id: Video id - c_id: Video cid ### Return: - Video data V2  # [示例/Example] a_id = \"114006081739452\" c_id = \"28400484458\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v2_api_v1_bilibili_web_fetch_one_video_v2_get_with_http_info(a_id, c_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object a_id: 作品id/Video id (required)
        :param object c_id: 作品cid/Video cid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['a_id', 'c_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_v2_api_v1_bilibili_web_fetch_one_video_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'a_id' is set
        if self.api_client.client_side_validation and ('a_id' not in params or
                                                       params['a_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `a_id` when calling `fetch_one_video_v2_api_v1_bilibili_web_fetch_one_video_v2_get`")  # noqa: E501
        # verify the required parameter 'c_id' is set
        if self.api_client.client_side_validation and ('c_id' not in params or
                                                       params['c_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `c_id` when calling `fetch_one_video_v2_api_v1_bilibili_web_fetch_one_video_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'a_id' in params:
            query_params.append(('a_id', params['a_id']))  # noqa: E501
        if 'c_id' in params:
            query_params.append(('c_id', params['c_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_one_video_v2', 'GET',
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

    def fetch_one_video_v3_api_v1_bilibili_web_fetch_one_video_v3_get(self, url, **kwargs):  # noqa: E501
        """获取单个视频详情信息V3/Get single video data V3  # noqa: E501

        # [中文] ### 用途: - 获取单个视频详情信息V3 ### 参数: - url: 视频链接 ### 返回: - 视频详情信息V3  # [English] ### Purpose: - Get single video data V3 ### Parameters: - url: Video URL ### Return: - Video data V3  # [示例/Example] url = \"https://www.bilibili.com/video/BV1S5uKzzE4r\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v3_api_v1_bilibili_web_fetch_one_video_v3_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 视频链接/Video URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_v3_api_v1_bilibili_web_fetch_one_video_v3_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_v3_api_v1_bilibili_web_fetch_one_video_v3_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_v3_api_v1_bilibili_web_fetch_one_video_v3_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """获取单个视频详情信息V3/Get single video data V3  # noqa: E501

        # [中文] ### 用途: - 获取单个视频详情信息V3 ### 参数: - url: 视频链接 ### 返回: - 视频详情信息V3  # [English] ### Purpose: - Get single video data V3 ### Parameters: - url: Video URL ### Return: - Video data V3  # [示例/Example] url = \"https://www.bilibili.com/video/BV1S5uKzzE4r\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v3_api_v1_bilibili_web_fetch_one_video_v3_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 视频链接/Video URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_v3_api_v1_bilibili_web_fetch_one_video_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `fetch_one_video_v3_api_v1_bilibili_web_fetch_one_video_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_one_video_v3', 'GET',
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

    def fetch_user_collection_videos_api_v1_bilibili_web_fetch_user_collection_videos_get(self, folder_id, **kwargs):  # noqa: E501
        """获取指定收藏夹内视频数据/Gets video data from a collection folder  # noqa: E501

        # [中文] ### 用途: - 获取指定收藏夹内视频数据 ### 参数: - folder_id: 用户UID - pn: 页码 ### 返回: - 指定收藏夹内视频数据  # [English] ### Purpose: - Gets video data from a collection folder ### Parameters: - folder_id: collection folder id - pn: Page number ### Return: - video data from collection folder  # [示例/Example] folder_id = \"1756059545\" pn = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collection_videos_api_v1_bilibili_web_fetch_user_collection_videos_get(folder_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object folder_id: 收藏夹id/collection folder id (required)
        :param object pn: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_collection_videos_api_v1_bilibili_web_fetch_user_collection_videos_get_with_http_info(folder_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_collection_videos_api_v1_bilibili_web_fetch_user_collection_videos_get_with_http_info(folder_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_collection_videos_api_v1_bilibili_web_fetch_user_collection_videos_get_with_http_info(self, folder_id, **kwargs):  # noqa: E501
        """获取指定收藏夹内视频数据/Gets video data from a collection folder  # noqa: E501

        # [中文] ### 用途: - 获取指定收藏夹内视频数据 ### 参数: - folder_id: 用户UID - pn: 页码 ### 返回: - 指定收藏夹内视频数据  # [English] ### Purpose: - Gets video data from a collection folder ### Parameters: - folder_id: collection folder id - pn: Page number ### Return: - video data from collection folder  # [示例/Example] folder_id = \"1756059545\" pn = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collection_videos_api_v1_bilibili_web_fetch_user_collection_videos_get_with_http_info(folder_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object folder_id: 收藏夹id/collection folder id (required)
        :param object pn: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id', 'pn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_collection_videos_api_v1_bilibili_web_fetch_user_collection_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if self.api_client.client_side_validation and ('folder_id' not in params or
                                                       params['folder_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder_id` when calling `fetch_user_collection_videos_api_v1_bilibili_web_fetch_user_collection_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'folder_id' in params:
            query_params.append(('folder_id', params['folder_id']))  # noqa: E501
        if 'pn' in params:
            query_params.append(('pn', params['pn']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_user_collection_videos', 'GET',
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

    def fetch_user_post_videos_api_v1_bilibili_web_fetch_user_post_videos_get(self, uid, **kwargs):  # noqa: E501
        """获取用户主页作品数据/Get user homepage video data  # noqa: E501

        # [中文] ### 用途: - 获取用户发布的视频数据 ### 参数: - uid: 用户UID - pn: 页码 - order: 排序方式     - pubdate 最新发布     - click 最多播放     - stow 最多收藏 ### 返回: - 用户发布的视频数据  # [English] ### Purpose: - Get user post video data ### Parameters: - uid: User UID - pn: Page number - order: Order method     - pubdate Latest release     - click Most played     - stow Most collection ### Return: - User posted video data  # [示例/Example] uid = \"178360345\" pn = 1 order = \"pubdate\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_api_v1_bilibili_web_fetch_user_post_videos_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID (required)
        :param object pn: 页码/Page number
        :param object order: 排序方式/Order method
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_post_videos_api_v1_bilibili_web_fetch_user_post_videos_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_videos_api_v1_bilibili_web_fetch_user_post_videos_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_post_videos_api_v1_bilibili_web_fetch_user_post_videos_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户主页作品数据/Get user homepage video data  # noqa: E501

        # [中文] ### 用途: - 获取用户发布的视频数据 ### 参数: - uid: 用户UID - pn: 页码 - order: 排序方式     - pubdate 最新发布     - click 最多播放     - stow 最多收藏 ### 返回: - 用户发布的视频数据  # [English] ### Purpose: - Get user post video data ### Parameters: - uid: User UID - pn: Page number - order: Order method     - pubdate Latest release     - click Most played     - stow Most collection ### Return: - User posted video data  # [示例/Example] uid = \"178360345\" pn = 1 order = \"pubdate\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_api_v1_bilibili_web_fetch_user_post_videos_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID (required)
        :param object pn: 页码/Page number
        :param object order: 排序方式/Order method
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'pn', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_post_videos_api_v1_bilibili_web_fetch_user_post_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_post_videos_api_v1_bilibili_web_fetch_user_post_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'pn' in params:
            query_params.append(('pn', params['pn']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_user_post_videos', 'GET',
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

    def fetch_user_relation_stat_api_v1_bilibili_web_fetch_user_relation_stat_get(self, uid, **kwargs):  # noqa: E501
        """获取用户关系状态统计/Get user relation stat (following and followers)  # noqa: E501

        # [中文] ### 用途: - 获取用户关系状态统计信息（关注数、粉丝数） ### 参数: - uid: 用户UID ### 返回: - 用户关系状态统计数据     - following: 关注数     - follower: 粉丝数  # [English] ### Purpose: - Get user relation stat (following count and follower count) ### Parameters: - uid: User UID ### Return: - User relation stat data     - following: Following count     - follower: Follower count  # [示例/Example] uid = \"178360345\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_relation_stat_api_v1_bilibili_web_fetch_user_relation_stat_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID/User UID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_relation_stat_api_v1_bilibili_web_fetch_user_relation_stat_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_relation_stat_api_v1_bilibili_web_fetch_user_relation_stat_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_relation_stat_api_v1_bilibili_web_fetch_user_relation_stat_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户关系状态统计/Get user relation stat (following and followers)  # noqa: E501

        # [中文] ### 用途: - 获取用户关系状态统计信息（关注数、粉丝数） ### 参数: - uid: 用户UID ### 返回: - 用户关系状态统计数据     - following: 关注数     - follower: 粉丝数  # [English] ### Purpose: - Get user relation stat (following count and follower count) ### Parameters: - uid: User UID ### Return: - User relation stat data     - following: Following count     - follower: Follower count  # [示例/Example] uid = \"178360345\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_relation_stat_api_v1_bilibili_web_fetch_user_relation_stat_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID/User UID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_relation_stat_api_v1_bilibili_web_fetch_user_relation_stat_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_relation_stat_api_v1_bilibili_web_fetch_user_relation_stat_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_user_relation_stat', 'GET',
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

    def fetch_user_up_stat_api_v1_bilibili_web_fetch_user_up_stat_get(self, uid, **kwargs):  # noqa: E501
        """获取UP主状态统计/Get UP stat (total likes and views)  # noqa: E501

        # [中文] ### 用途: - 获取UP主状态统计信息（总获赞数、总播放数） ### 参数: - uid: 用户UID ### 返回: - UP主状态统计数据     - archive: 视频相关统计         - view: 总播放数     - likes: 总获赞数  # [English] ### Purpose: - Get UP stat (total likes and total views) ### Parameters: - uid: User UID ### Return: - UP stat data     - archive: Video statistics         - view: Total views     - likes: Total likes  # [示例/Example] uid = \"178360345\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_up_stat_api_v1_bilibili_web_fetch_user_up_stat_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID/User UID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_up_stat_api_v1_bilibili_web_fetch_user_up_stat_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_up_stat_api_v1_bilibili_web_fetch_user_up_stat_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_up_stat_api_v1_bilibili_web_fetch_user_up_stat_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取UP主状态统计/Get UP stat (total likes and views)  # noqa: E501

        # [中文] ### 用途: - 获取UP主状态统计信息（总获赞数、总播放数） ### 参数: - uid: 用户UID ### 返回: - UP主状态统计数据     - archive: 视频相关统计         - view: 总播放数     - likes: 总获赞数  # [English] ### Purpose: - Get UP stat (total likes and total views) ### Parameters: - uid: User UID ### Return: - UP stat data     - archive: Video statistics         - view: Total views     - likes: Total likes  # [示例/Example] uid = \"178360345\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_up_stat_api_v1_bilibili_web_fetch_user_up_stat_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID/User UID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_up_stat_api_v1_bilibili_web_fetch_user_up_stat_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_up_stat_api_v1_bilibili_web_fetch_user_up_stat_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_user_up_stat', 'GET',
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

    def fetch_video_detail_api_v1_bilibili_web_fetch_video_detail_get(self, aid, **kwargs):  # noqa: E501
        """获取单个视频详情/Get single video detail  # noqa: E501

        # [中文] ### 用途: - 获取单个视频详情 ### 参数: - aid: 作品id ### 返回: - 视频详情  # [English] ### Purpose: - Get single video detail ### Parameters: - aid: Video id ### Return: - Video detail  # [示例/Example] aid = \"114902186396822\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_detail_api_v1_bilibili_web_fetch_video_detail_get(aid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aid: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_detail_api_v1_bilibili_web_fetch_video_detail_get_with_http_info(aid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_detail_api_v1_bilibili_web_fetch_video_detail_get_with_http_info(aid, **kwargs)  # noqa: E501
            return data

    def fetch_video_detail_api_v1_bilibili_web_fetch_video_detail_get_with_http_info(self, aid, **kwargs):  # noqa: E501
        """获取单个视频详情/Get single video detail  # noqa: E501

        # [中文] ### 用途: - 获取单个视频详情 ### 参数: - aid: 作品id ### 返回: - 视频详情  # [English] ### Purpose: - Get single video detail ### Parameters: - aid: Video id ### Return: - Video detail  # [示例/Example] aid = \"114902186396822\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_detail_api_v1_bilibili_web_fetch_video_detail_get_with_http_info(aid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aid: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_detail_api_v1_bilibili_web_fetch_video_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aid' is set
        if self.api_client.client_side_validation and ('aid' not in params or
                                                       params['aid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aid` when calling `fetch_video_detail_api_v1_bilibili_web_fetch_video_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aid' in params:
            query_params.append(('aid', params['aid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_video_detail', 'GET',
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

    def fetch_video_play_info_api_v1_bilibili_web_fetch_video_play_info_get(self, url, **kwargs):  # noqa: E501
        """获取单个视频播放信息/Get single video play info  # noqa: E501

        # [中文] ### 用途: - 获取单个视频播放信息 ### 参数: - url: 视频链接 ### 返回: - 视频播放信息  # [English] ### Purpose: - Get single video play info ### Parameters: - url: Video URL ### Return: - Video data  # [示例/Example] url = \"https://www.bilibili.com/video/BV1S5uKzzE4r\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_play_info_api_v1_bilibili_web_fetch_video_play_info_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 视频链接/Video URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_play_info_api_v1_bilibili_web_fetch_video_play_info_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_play_info_api_v1_bilibili_web_fetch_video_play_info_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def fetch_video_play_info_api_v1_bilibili_web_fetch_video_play_info_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """获取单个视频播放信息/Get single video play info  # noqa: E501

        # [中文] ### 用途: - 获取单个视频播放信息 ### 参数: - url: 视频链接 ### 返回: - 视频播放信息  # [English] ### Purpose: - Get single video play info ### Parameters: - url: Video URL ### Return: - Video data  # [示例/Example] url = \"https://www.bilibili.com/video/BV1S5uKzzE4r\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_play_info_api_v1_bilibili_web_fetch_video_play_info_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 视频链接/Video URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_play_info_api_v1_bilibili_web_fetch_video_play_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `fetch_video_play_info_api_v1_bilibili_web_fetch_video_play_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bilibili/web/fetch_video_play_info', 'GET',
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

    def fetch_vip_video_playurl_api_v1_bilibili_web_fetch_vip_video_playurl_post(self, **kwargs):  # noqa: E501
        """获取大会员清晰度视频流地址/Get VIP video playurl  # noqa: E501

        # [中文] ### 用途: - 获取大会员清晰度视频流地址 ### 参数: - bv_id: 作品id - cid: 作品cid - cookie: 大会员用户Cookie ### 返回: - 大会员清晰度视频流地址  # [English] ### Purpose: - Get VIP video playurl ### Parameters: - bv_id: Video id - cid: Video cid - cookie: VIP User Cookie ### Return: - VIP video playurl  # [示例/Example] bv_id = \"BV1y7411Q7Eq\" cid = \"171776208\" cookie = \"your_vip_bilibili_cookie\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_vip_video_playurl_api_v1_bilibili_web_fetch_vip_video_playurl_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_vip_video_playurl_api_v1_bilibili_web_fetch_vip_video_playurl_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_vip_video_playurl_api_v1_bilibili_web_fetch_vip_video_playurl_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_vip_video_playurl_api_v1_bilibili_web_fetch_vip_video_playurl_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取大会员清晰度视频流地址/Get VIP video playurl  # noqa: E501

        # [中文] ### 用途: - 获取大会员清晰度视频流地址 ### 参数: - bv_id: 作品id - cid: 作品cid - cookie: 大会员用户Cookie ### 返回: - 大会员清晰度视频流地址  # [English] ### Purpose: - Get VIP video playurl ### Parameters: - bv_id: Video id - cid: Video cid - cookie: VIP User Cookie ### Return: - VIP video playurl  # [示例/Example] bv_id = \"BV1y7411Q7Eq\" cid = \"171776208\" cookie = \"your_vip_bilibili_cookie\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_vip_video_playurl_api_v1_bilibili_web_fetch_vip_video_playurl_post_with_http_info(async_req=True)
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
                    " to method fetch_vip_video_playurl_api_v1_bilibili_web_fetch_vip_video_playurl_post" % key
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
            '/api/v1/bilibili/web/fetch_vip_video_playurl', 'POST',
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
