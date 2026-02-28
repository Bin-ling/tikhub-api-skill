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


class DemoAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get(self, **kwargs):  # noqa: E501
        """【Demo】抖音APP获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin APP Fixed Video Data with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示(Demo)接口，仅用于测试和展示功能** - **不允许修改aweme_id参数，始终返回固定作品的数据** - **数据缓存1小时**  ### 用途: - 用于测试API连接和数据格式 - 了解返回数据结构 - 开发阶段的功能验证  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定作品ID: 7534641277405531446 - ✅ 固定作品的对应链接: https://www.douyin.com/video/7534641277405531446 - ✅ 免费使用，无需计费  ### 返回: - 固定作品的缓存数据  ---  ## [English] ### ⚠️ Important Notice: - **This is a DEMO endpoint for testing and demonstration only** - **The aweme_id parameter cannot be modified, always returns data for a fixed video** - **Data is cached for 1 hour**  ### Purpose: - Test API connection and data format - Understand return data structure - Feature validation during development  ### Features: - ✅ 1-hour data caching - ✅ Fixed video ID: 7534641277405531446 - ✅ Fixed video link: https://www.douyin.com/video/7534641277405531446 - ✅ Free to use, no billing  ### Return: - Cached data for the fixed video  ---  # [示例/Example] ``` # 无需参数，始终返回固定作品数据 # No parameters needed, always returns fixed video data GET /api/v1/douyin/app/fetch_one_video ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get_with_http_info(self, **kwargs):  # noqa: E501
        """【Demo】抖音APP获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin APP Fixed Video Data with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示(Demo)接口，仅用于测试和展示功能** - **不允许修改aweme_id参数，始终返回固定作品的数据** - **数据缓存1小时**  ### 用途: - 用于测试API连接和数据格式 - 了解返回数据结构 - 开发阶段的功能验证  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定作品ID: 7534641277405531446 - ✅ 固定作品的对应链接: https://www.douyin.com/video/7534641277405531446 - ✅ 免费使用，无需计费  ### 返回: - 固定作品的缓存数据  ---  ## [English] ### ⚠️ Important Notice: - **This is a DEMO endpoint for testing and demonstration only** - **The aweme_id parameter cannot be modified, always returns data for a fixed video** - **Data is cached for 1 hour**  ### Purpose: - Test API connection and data format - Understand return data structure - Feature validation during development  ### Features: - ✅ 1-hour data caching - ✅ Fixed video ID: 7534641277405531446 - ✅ Fixed video link: https://www.douyin.com/video/7534641277405531446 - ✅ Free to use, no billing  ### Return: - Cached data for the fixed video  ---  # [示例/Example] ``` # 无需参数，始终返回固定作品数据 # No parameters needed, always returns fixed video data GET /api/v1/douyin/app/fetch_one_video ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get_with_http_info(async_req=True)
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
                    " to method douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get" % key
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
            '/api/v1/demo/douyin/app/fetch_one_video', 'GET',
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

    def douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get(self, **kwargs):  # noqa: E501
        """【Demo】抖音搜索综合搜索（1小时缓存）/[Demo] Douyin General Search with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示接口，返回固定关键词的搜索结果** - **搜索关键词固定为\"美食\"** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定搜索关键词: 美食 - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Demo endpoint returning fixed keyword search results** - **Search keyword fixed as \"美食\" (Food)** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed search keyword: 美食 - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定关键词搜索结果 # No parameters needed, always returns fixed keyword search results GET /api/v1/douyin_search/app/general_search ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get_with_http_info(self, **kwargs):  # noqa: E501
        """【Demo】抖音搜索综合搜索（1小时缓存）/[Demo] Douyin General Search with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示接口，返回固定关键词的搜索结果** - **搜索关键词固定为\"美食\"** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定搜索关键词: 美食 - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Demo endpoint returning fixed keyword search results** - **Search keyword fixed as \"美食\" (Food)** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed search keyword: 美食 - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定关键词搜索结果 # No parameters needed, always returns fixed keyword search results GET /api/v1/douyin_search/app/general_search ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get_with_http_info(async_req=True)
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
                    " to method douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get" % key
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
            '/api/v1/demo/douyin_search/app/general_search', 'GET',
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

    def douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get(self, **kwargs):  # noqa: E501
        """【Demo】抖音Web获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin Web Fixed Video Data with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示(Demo)接口，仅用于测试和展示功能** - **不允许修改aweme_id参数，始终返回固定作品的数据** - **数据缓存1小时**  ### 用途: - 用于测试API连接和数据格式 - 了解返回数据结构 - 开发阶段的功能验证  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定作品ID: 7534641277405531446 - ✅ 固定作品的对应链接: https://www.douyin.com/video/7534641277405531446 - ✅ 免费使用，无需计费  ### 返回: - 固定作品的缓存数据  ---  ## [English] ### ⚠️ Important Notice: - **This is a DEMO endpoint for testing and demonstration only** - **The aweme_id parameter cannot be modified, always returns data for a fixed video** - **Data is cached for 1 hour**  ### Purpose: - Test API connection and data format - Understand return data structure - Feature validation during development  ### Features: - ✅ 1-hour data caching - ✅ Fixed video ID: 7534641277405531446 - ✅ Fixed video link: https://www.douyin.com/video/7534641277405531446 - ✅ Free to use, no billing  ### Return: - Cached data for the fixed video  ---  # [示例/Example] ``` # 无需参数，始终返回固定作品数据 # No parameters needed, always returns fixed video data GET /api/v1/douyin/web/fetch_one_video ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get_with_http_info(self, **kwargs):  # noqa: E501
        """【Demo】抖音Web获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin Web Fixed Video Data with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示(Demo)接口，仅用于测试和展示功能** - **不允许修改aweme_id参数，始终返回固定作品的数据** - **数据缓存1小时**  ### 用途: - 用于测试API连接和数据格式 - 了解返回数据结构 - 开发阶段的功能验证  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定作品ID: 7534641277405531446 - ✅ 固定作品的对应链接: https://www.douyin.com/video/7534641277405531446 - ✅ 免费使用，无需计费  ### 返回: - 固定作品的缓存数据  ---  ## [English] ### ⚠️ Important Notice: - **This is a DEMO endpoint for testing and demonstration only** - **The aweme_id parameter cannot be modified, always returns data for a fixed video** - **Data is cached for 1 hour**  ### Purpose: - Test API connection and data format - Understand return data structure - Feature validation during development  ### Features: - ✅ 1-hour data caching - ✅ Fixed video ID: 7534641277405531446 - ✅ Fixed video link: https://www.douyin.com/video/7534641277405531446 - ✅ Free to use, no billing  ### Return: - Cached data for the fixed video  ---  # [示例/Example] ``` # 无需参数，始终返回固定作品数据 # No parameters needed, always returns fixed video data GET /api/v1/douyin/web/fetch_one_video ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get_with_http_info(async_req=True)
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
                    " to method douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get" % key
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
            '/api/v1/demo/douyin/web/fetch_one_video', 'GET',
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

    def instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get(self, **kwargs):  # noqa: E501
        """【Demo】Instagram获取固定用户信息（1小时缓存）/[Demo] Instagram Fixed User Profile with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定Instagram用户信息** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定用户: Instagram - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed Instagram user profile** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed user: Instagram - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定用户数据 # No parameters needed, always returns fixed user data GET /api/v1/instagram/web/fetch_user_info ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """【Demo】Instagram获取固定用户信息（1小时缓存）/[Demo] Instagram Fixed User Profile with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定Instagram用户信息** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定用户: Instagram - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed Instagram user profile** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed user: Instagram - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定用户数据 # No parameters needed, always returns fixed user data GET /api/v1/instagram/web/fetch_user_info ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get_with_http_info(async_req=True)
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
                    " to method instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get" % key
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
            '/api/v1/demo/instagram/web/fetch_user_info', 'GET',
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

    def kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get(self, **kwargs):  # noqa: E501
        """【Demo】快手获取固定视频信息（1小时缓存）/[Demo] Kuaishou Fixed Video with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定快手视频信息** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定视频数据，参数：https://www.kuaishou.com/short-video/3x73wr9tdt7nxqy - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed Kuaishou video info** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed video data, parameter: https://www.kuaishou.com/short-video/3x73wr9tdt7nxqy - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定视频数据 # No parameters needed, always returns fixed video data GET /api/v1/kuaishou/web/fetch_one_video ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get_with_http_info(self, **kwargs):  # noqa: E501
        """【Demo】快手获取固定视频信息（1小时缓存）/[Demo] Kuaishou Fixed Video with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定快手视频信息** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定视频数据，参数：https://www.kuaishou.com/short-video/3x73wr9tdt7nxqy - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed Kuaishou video info** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed video data, parameter: https://www.kuaishou.com/short-video/3x73wr9tdt7nxqy - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定视频数据 # No parameters needed, always returns fixed video data GET /api/v1/kuaishou/web/fetch_one_video ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get_with_http_info(async_req=True)
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
                    " to method kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get" % key
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
            '/api/v1/demo/kuaishou/web/fetch_one_video', 'GET',
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

    def tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get(self, **kwargs):  # noqa: E501
        """【Demo】TikTok APP获取固定视频详情（1小时缓存）/[Demo] TikTok APP Fixed Video Detail with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定TikTok视频详情** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定视频详情，参数: 7319033421676653855 - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed TikTok video detail** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed video detail, parameter: 7319033421676653855 - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定视频数据 # No parameters needed, always returns fixed video data GET /api/v1/tiktok/app/fetch_one_video ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get_with_http_info(self, **kwargs):  # noqa: E501
        """【Demo】TikTok APP获取固定视频详情（1小时缓存）/[Demo] TikTok APP Fixed Video Detail with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定TikTok视频详情** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定视频详情，参数: 7319033421676653855 - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed TikTok video detail** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed video detail, parameter: 7319033421676653855 - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定视频数据 # No parameters needed, always returns fixed video data GET /api/v1/tiktok/app/fetch_one_video ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get_with_http_info(async_req=True)
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
                    " to method tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get" % key
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
            '/api/v1/demo/tiktok/app/fetch_one_video', 'GET',
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

    def tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get(self, **kwargs):  # noqa: E501
        """【Demo】TikTok固定用户信息（1小时缓存）/[Demo] TikTok Fixed User Profile with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定TikTok用户信息** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定用户: tiktok - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed TikTok user profile** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed user: tiktok - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定用户数据 # No parameters needed, always returns fixed user data GET /api/v1/tiktok/web/fetch_user_profile ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get_with_http_info(self, **kwargs):  # noqa: E501
        """【Demo】TikTok固定用户信息（1小时缓存）/[Demo] TikTok Fixed User Profile with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **返回固定TikTok用户信息** - **数据缓存1小时**  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定用户: tiktok - ✅ 免费使用  ## [English] ### ⚠️ Important Notice: - **Returns fixed TikTok user profile** - **Data cached for 1 hour**  ### Features: - ✅ 1-hour data caching - ✅ Fixed user: tiktok - ✅ Free to use  ---  # [示例/Example] ``` # 无需参数，始终返回固定用户数据 # No parameters needed, always returns fixed user data GET /api/v1/tiktok/web/fetch_user_profile ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get_with_http_info(async_req=True)
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
                    " to method tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get" % key
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
            '/api/v1/demo/tiktok/web/fetch_user_profile', 'GET',
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

    def view_cache_status_api_v1_demo_demo_cache_status_get(self, **kwargs):  # noqa: E501
        """查看Demo缓存状态/View Demo Cache Status  # noqa: E501

        # 查看所有Demo接口的缓存状态  ## [中文] ### 用途: - 查看当前缓存的Demo数据 - 了解缓存过期时间  ## [English] ### Purpose: - View current cached Demo data - Check cache expiration times  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.view_cache_status_api_v1_demo_demo_cache_status_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.view_cache_status_api_v1_demo_demo_cache_status_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.view_cache_status_api_v1_demo_demo_cache_status_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def view_cache_status_api_v1_demo_demo_cache_status_get_with_http_info(self, **kwargs):  # noqa: E501
        """查看Demo缓存状态/View Demo Cache Status  # noqa: E501

        # 查看所有Demo接口的缓存状态  ## [中文] ### 用途: - 查看当前缓存的Demo数据 - 了解缓存过期时间  ## [English] ### Purpose: - View current cached Demo data - Check cache expiration times  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.view_cache_status_api_v1_demo_demo_cache_status_get_with_http_info(async_req=True)
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
                    " to method view_cache_status_api_v1_demo_demo_cache_status_get" % key
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
            '/api/v1/demo/demo/cache_status', 'GET',
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

    def wechat_article_extract_api_v1_demo_wechat_article_extract_get(self, **kwargs):  # noqa: E501
        """【Demo】微信公众号文章提取（1小时缓存）/[Demo] WeChat Article Extract with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示(Demo)接口，仅用于测试和展示功能** - **不允许修改URL参数，始终返回固定文章的数据** - **数据缓存1小时**  ### 用途: - 用于测试API连接和数据格式 - 了解返回数据结构 - 开发阶段的功能验证  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定文章URL: https://mp.weixin.qq.com/s/c7_-h_3XJLpOBqpUfIlJ9w - ✅ 免费使用，无需计费  ### 返回: - 固定文章的缓存数据  ---  ## [English] ### ⚠️ Important Notice: - **This is a DEMO endpoint for testing and demonstration only** - **The URL parameter cannot be modified, always returns data for a fixed article** - **Data is cached for 1 hour**  ### Purpose: - Test API connection and data format - Understand return data structure - Feature validation during development  ### Features: - ✅ 1-hour data caching - ✅ Fixed article URL: https://mp.weixin.qq.com/s/c7_-h_3XJLpOBqpUfIlJ9w - ✅ Free to use, no billing  ### Return: - Cached data for the fixed article  ---  # [示例/Example] ``` # 无需参数，始终返回固定文章数据 # No parameters needed, always returns fixed article data GET /api/v1/wechat/article_extract ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wechat_article_extract_api_v1_demo_wechat_article_extract_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wechat_article_extract_api_v1_demo_wechat_article_extract_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.wechat_article_extract_api_v1_demo_wechat_article_extract_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def wechat_article_extract_api_v1_demo_wechat_article_extract_get_with_http_info(self, **kwargs):  # noqa: E501
        """【Demo】微信公众号文章提取（1小时缓存）/[Demo] WeChat Article Extract with Cache  # noqa: E501

        # 🎯 **这是一个DEMO接口**  ## [中文] ### ⚠️ 重要说明: - **这是一个演示(Demo)接口，仅用于测试和展示功能** - **不允许修改URL参数，始终返回固定文章的数据** - **数据缓存1小时**  ### 用途: - 用于测试API连接和数据格式 - 了解返回数据结构 - 开发阶段的功能验证  ### 特性: - ✅ 1小时数据缓存 - ✅ 固定文章URL: https://mp.weixin.qq.com/s/c7_-h_3XJLpOBqpUfIlJ9w - ✅ 免费使用，无需计费  ### 返回: - 固定文章的缓存数据  ---  ## [English] ### ⚠️ Important Notice: - **This is a DEMO endpoint for testing and demonstration only** - **The URL parameter cannot be modified, always returns data for a fixed article** - **Data is cached for 1 hour**  ### Purpose: - Test API connection and data format - Understand return data structure - Feature validation during development  ### Features: - ✅ 1-hour data caching - ✅ Fixed article URL: https://mp.weixin.qq.com/s/c7_-h_3XJLpOBqpUfIlJ9w - ✅ Free to use, no billing  ### Return: - Cached data for the fixed article  ---  # [示例/Example] ``` # 无需参数，始终返回固定文章数据 # No parameters needed, always returns fixed article data GET /api/v1/wechat/article_extract ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wechat_article_extract_api_v1_demo_wechat_article_extract_get_with_http_info(async_req=True)
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
                    " to method wechat_article_extract_api_v1_demo_wechat_article_extract_get" % key
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
            '/api/v1/demo/wechat/article_extract', 'GET',
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
