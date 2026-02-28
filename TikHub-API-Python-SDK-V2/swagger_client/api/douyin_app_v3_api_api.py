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


class DouyinAppV3APIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get(self, aweme_type, item_id, **kwargs):  # noqa: E501
        """根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID  # noqa: E501

        # [中文] ### 用途: - 根据视频ID来增加作品的播放数 - 该接口默认使用游客Cookie，如果需要使用登录用户的Cookie，请在参数中传入。 - 单一作品每次调用增加1次播放数，请求约 `1000` 次后会被抖音限制，需要等待一段时间（如：2小时后）后再继续调用。 - 该限制是针对作品的，不是针对接口的，在未登录的情况下，使用不同IP的浏览器或在APP中浏览作品，该作品的播放数也不会增加。 - 可以携带抖音网页端的Cookie来请求此接口，但是不保证一定有效，需要自行测试。 - 上述的限制是根据测试结果得出的，具体限制可能会有所不同，仅供参考。 ### 参数: - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。 - item_id: 作品id，别名为aweme_id - cookie: 可选，默认使用游客Cookie ### 返回: - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。  # [English] ### Purpose: - Increase the number of plays of the work according to the video ID - This interface uses guest Cookie by default. If you need to use the Cookie of the logged-in user, please pass it in the parameters. - Each call to a single work increases the number of plays by 1. After about `1000` calls, Douyin will restrict it. You need to wait for a period of time (such as 2 hours) before continuing to call. - This restriction is for the work, not for the interface. When browsing the work without logging in, using different IP browsers or browsing the work in the APP, the number of plays of the work will not increase. - You can carry the Cookie of the Douyin web page to request this interface, but it is not guaranteed to be effective and needs to be tested by yourself. - The above restrictions are based on test results, and the specific restrictions may vary, for reference only. ### Parameters: - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data interface. - item_id: Video id, alias aweme_id - cookie: Optional, use guest Cookie by default ### Return: - The current timestamp and status code. When the status code is 200, it means success, otherwise it is a failure. You can try to change another work id and call it again, or wait for a period of time and call it again.  # [示例/Example] aweme_type = 0 item_id = \"7197598285882789120\" cookie = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get(aweme_type, item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_type: 作品类型/Video type (required)
        :param object item_id: 作品id/Video id (required)
        :param object cookie: 可选，默认使用游客Cookie/Optional, use guest Cookie by default
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get_with_http_info(aweme_type, item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get_with_http_info(aweme_type, item_id, **kwargs)  # noqa: E501
            return data

    def add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get_with_http_info(self, aweme_type, item_id, **kwargs):  # noqa: E501
        """根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID  # noqa: E501

        # [中文] ### 用途: - 根据视频ID来增加作品的播放数 - 该接口默认使用游客Cookie，如果需要使用登录用户的Cookie，请在参数中传入。 - 单一作品每次调用增加1次播放数，请求约 `1000` 次后会被抖音限制，需要等待一段时间（如：2小时后）后再继续调用。 - 该限制是针对作品的，不是针对接口的，在未登录的情况下，使用不同IP的浏览器或在APP中浏览作品，该作品的播放数也不会增加。 - 可以携带抖音网页端的Cookie来请求此接口，但是不保证一定有效，需要自行测试。 - 上述的限制是根据测试结果得出的，具体限制可能会有所不同，仅供参考。 ### 参数: - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。 - item_id: 作品id，别名为aweme_id - cookie: 可选，默认使用游客Cookie ### 返回: - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。  # [English] ### Purpose: - Increase the number of plays of the work according to the video ID - This interface uses guest Cookie by default. If you need to use the Cookie of the logged-in user, please pass it in the parameters. - Each call to a single work increases the number of plays by 1. After about `1000` calls, Douyin will restrict it. You need to wait for a period of time (such as 2 hours) before continuing to call. - This restriction is for the work, not for the interface. When browsing the work without logging in, using different IP browsers or browsing the work in the APP, the number of plays of the work will not increase. - You can carry the Cookie of the Douyin web page to request this interface, but it is not guaranteed to be effective and needs to be tested by yourself. - The above restrictions are based on test results, and the specific restrictions may vary, for reference only. ### Parameters: - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data interface. - item_id: Video id, alias aweme_id - cookie: Optional, use guest Cookie by default ### Return: - The current timestamp and status code. When the status code is 200, it means success, otherwise it is a failure. You can try to change another work id and call it again, or wait for a period of time and call it again.  # [示例/Example] aweme_type = 0 item_id = \"7197598285882789120\" cookie = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get_with_http_info(aweme_type, item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_type: 作品类型/Video type (required)
        :param object item_id: 作品id/Video id (required)
        :param object cookie: 可选，默认使用游客Cookie/Optional, use guest Cookie by default
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_type', 'item_id', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_type' is set
        if self.api_client.client_side_validation and ('aweme_type' not in params or
                                                       params['aweme_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_type` when calling `add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get`")  # noqa: E501
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_type' in params:
            query_params.append(('aweme_type', params['aweme_type']))  # noqa: E501
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/add_video_play_count', 'GET',
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

    def fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的综合搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212773e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年 - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上 - content_type: 0:不限 1:视频 2:图片 3:文章 ### 返回: - 综合搜索结果  # [English] ### Purpose: - Get comprehensive search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212773e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes - content_type: 0: Unlimited 1: Video 2: Picture 3: Article ### Return: - Comprehensive search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = \"0\" publish_time = \"0\" filter_duration = \"0\" content_type = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object filter_duration: 时长/Duration
        :param object content_type: 内容类型/Content type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的综合搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212773e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年 - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上 - content_type: 0:不限 1:视频 2:图片 3:文章 ### 返回: - 综合搜索结果  # [English] ### Purpose: - Get comprehensive search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212773e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes - content_type: 0: Unlimited 1: Video 2: Picture 3: Article ### Return: - Comprehensive search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = \"0\" publish_time = \"0\" filter_duration = \"0\" content_type = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object filter_duration: 时长/Duration
        :param object content_type: 内容类型/Content type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'sort_type', 'publish_time', 'filter_duration', 'content_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'publish_time' in params:
            query_params.append(('publish_time', params['publish_time']))  # noqa: E501
        if 'filter_duration' in params:
            query_params.append(('filter_duration', params['filter_duration']))  # noqa: E501
        if 'content_type' in params:
            query_params.append(('content_type', params['content_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_general_search_result', 'GET',
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

    def fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get(self, ch_id, **kwargs):  # noqa: E501
        """获取指定话题的详情数据/Get details of specified hashtag  # noqa: E501

        # [中文] ### 用途: - 获取指定话题的详情数据 ### 参数: - ch_id: 话题id ### 返回: - 话题详情数据  # [English] ### Purpose: - Get details of specified hashtag ### Parameters: - ch_id: Hashtag id ### Return: - Hashtag details data  # [示例/Example] ch_id = 1575791821492238  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get(ch_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ch_id: 话题id/Hashtag id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get_with_http_info(ch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get_with_http_info(ch_id, **kwargs)  # noqa: E501
            return data

    def fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get_with_http_info(self, ch_id, **kwargs):  # noqa: E501
        """获取指定话题的详情数据/Get details of specified hashtag  # noqa: E501

        # [中文] ### 用途: - 获取指定话题的详情数据 ### 参数: - ch_id: 话题id ### 返回: - 话题详情数据  # [English] ### Purpose: - Get details of specified hashtag ### Parameters: - ch_id: Hashtag id ### Return: - Hashtag details data  # [示例/Example] ch_id = 1575791821492238  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get_with_http_info(ch_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ch_id: 话题id/Hashtag id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ch_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ch_id' is set
        if self.api_client.client_side_validation and ('ch_id' not in params or
                                                       params['ch_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ch_id` when calling `fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ch_id' in params:
            query_params.append(('ch_id', params['ch_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_hashtag_detail', 'GET',
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

    def fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的话题搜索结果（弃用，替代接口见下方文档说明）/Get hashtag search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的话题搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212794e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 话题搜索结果  # [English] ### Purpose: - Get hashtag search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212794e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Hashtag search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的话题搜索结果（弃用，替代接口见下方文档说明）/Get hashtag search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的话题搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212794e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 话题搜索结果  # [English] ### Purpose: - Get hashtag search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212794e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Hashtag search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_hashtag_search_result', 'GET',
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

    def fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get(self, ch_id, **kwargs):  # noqa: E501
        """获取指定话题的作品数据/Get video list of specified hashtag  # noqa: E501

        # [中文] ### 用途: - 获取指定话题的作品数据 ### 参数: - ch_id: 话题id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 话题作品数据  # [English] ### Purpose: - Get video list of specified hashtag ### Parameters: - ch_id: Hashtag id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Hashtag video list data  # [示例/Example] ch_id = 1575791821492238 cursor = 0 sort_type = 0 count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get(ch_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ch_id: 话题id/Hashtag id (required)
        :param object cursor: 游标/Cursor
        :param object sort_type: 排序类型/Sort type
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get_with_http_info(ch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get_with_http_info(ch_id, **kwargs)  # noqa: E501
            return data

    def fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get_with_http_info(self, ch_id, **kwargs):  # noqa: E501
        """获取指定话题的作品数据/Get video list of specified hashtag  # noqa: E501

        # [中文] ### 用途: - 获取指定话题的作品数据 ### 参数: - ch_id: 话题id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 话题作品数据  # [English] ### Purpose: - Get video list of specified hashtag ### Parameters: - ch_id: Hashtag id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Hashtag video list data  # [示例/Example] ch_id = 1575791821492238 cursor = 0 sort_type = 0 count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get_with_http_info(ch_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ch_id: 话题id/Hashtag id (required)
        :param object cursor: 游标/Cursor
        :param object sort_type: 排序类型/Sort type
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ch_id', 'cursor', 'sort_type', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ch_id' is set
        if self.api_client.client_side_validation and ('ch_id' not in params or
                                                       params['ch_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ch_id` when calling `fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ch_id' in params:
            query_params.append(('ch_id', params['ch_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_hashtag_video_list', 'GET',
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

    def fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get(self, category_id, **kwargs):  # noqa: E501
        """获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data  # noqa: E501

        # [中文] ### 用途: - 获取抖音品牌热榜具体分类数据 ### 参数: - category_id: 分类id ### 返回: - 品牌热搜榜具体分类数据  # [English] ### Purpose: - Get Douyin brand hot search list detail data ### Parameters: - category_id: Category id ### Return: - Hot brand search list detail data  # [示例/Example] category_id = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category_id: 分类id/Category id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get_with_http_info(category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get_with_http_info(category_id, **kwargs)  # noqa: E501
            return data

    def fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get_with_http_info(self, category_id, **kwargs):  # noqa: E501
        """获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data  # noqa: E501

        # [中文] ### 用途: - 获取抖音品牌热榜具体分类数据 ### 参数: - category_id: 分类id ### 返回: - 品牌热搜榜具体分类数据  # [English] ### Purpose: - Get Douyin brand hot search list detail data ### Parameters: - category_id: Category id ### Return: - Hot brand search list detail data  # [示例/Example] category_id = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get_with_http_info(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category_id: 分类id/Category id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if self.api_client.client_side_validation and ('category_id' not in params or
                                                       params['category_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `category_id` when calling `fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category_id' in params:
            query_params.append(('category_id', params['category_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_brand_hot_search_list_detail', 'GET',
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

    def fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get(self, **kwargs):  # noqa: E501
        """获取抖音品牌热榜分类数据/Get Douyin brand hot search list data  # noqa: E501

        # [中文] ### 用途: - 获取抖音品牌热榜分类数据 ### 返回: - 品牌热搜榜分类数据  # [English] ### Purpose: - Get Douyin brand hot search category data ### Return: - Hot brand search category data  # [示例/Example] pass  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取抖音品牌热榜分类数据/Get Douyin brand hot search list data  # noqa: E501

        # [中文] ### 用途: - 获取抖音品牌热榜分类数据 ### 返回: - 品牌热搜榜分类数据  # [English] ### Purpose: - Get Douyin brand hot search category data ### Return: - Hot brand search category data  # [示例/Example] pass  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get" % key
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
            '/api/v1/douyin/app/v3/fetch_brand_hot_search_list', 'GET',
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

    def fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get(self, **kwargs):  # noqa: E501
        """获取抖音热搜榜数据/Get Douyin hot search list data  # noqa: E501

        # [中文] ### 用途: - 获取抖音热榜数据，包括：     - 热点榜     - 种草榜     - 娱乐榜     - 社会榜     - 挑战榜 ### 参数: - board_type:     - 0: 热点榜（默认）     - 2: 其他榜单，如种草榜等，需要传入对应的board_sub_type参数。 - board_sub_type:     - 空字符串: 热点榜（默认）     - seeding: 种草榜     - 2: 娱乐榜     - 4: 社会榜     - hotspot_challenge: 挑战榜 ### 返回: - 热搜榜数据  # [English] ### Purpose: - Get Douyin hot search list data, including:     - Hot search list     - Seeding list     - Entertainment list     - Social list     - Challenge list  ### Parameters: - board_type:     - 0: Hot search list (default)     - 2: Other lists, such as seeding list, etc., need to pass in the corresponding board_sub_type parameter. - board_sub_type:     - Empty string: Hot search list (default)     - seeding: Seeding list     - 2: Entertainment list     - 4: Social list     - hotspot_challenge: Challenge list ### Return: - Hot search list data  # [示例/Example] - 获取热点榜数据     - board_type = 0     - board_sub_type = \"\" - 获取种草榜数据     - board_type = 2     - board_sub_type = \"seeding\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object board_type: 榜单类型/Board type
        :param object board_sub_type: 榜单子类型/Board sub type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取抖音热搜榜数据/Get Douyin hot search list data  # noqa: E501

        # [中文] ### 用途: - 获取抖音热榜数据，包括：     - 热点榜     - 种草榜     - 娱乐榜     - 社会榜     - 挑战榜 ### 参数: - board_type:     - 0: 热点榜（默认）     - 2: 其他榜单，如种草榜等，需要传入对应的board_sub_type参数。 - board_sub_type:     - 空字符串: 热点榜（默认）     - seeding: 种草榜     - 2: 娱乐榜     - 4: 社会榜     - hotspot_challenge: 挑战榜 ### 返回: - 热搜榜数据  # [English] ### Purpose: - Get Douyin hot search list data, including:     - Hot search list     - Seeding list     - Entertainment list     - Social list     - Challenge list  ### Parameters: - board_type:     - 0: Hot search list (default)     - 2: Other lists, such as seeding list, etc., need to pass in the corresponding board_sub_type parameter. - board_sub_type:     - Empty string: Hot search list (default)     - seeding: Seeding list     - 2: Entertainment list     - 4: Social list     - hotspot_challenge: Challenge list ### Return: - Hot search list data  # [示例/Example] - 获取热点榜数据     - board_type = 0     - board_sub_type = \"\" - 获取种草榜数据     - board_type = 2     - board_sub_type = \"seeding\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object board_type: 榜单类型/Board type
        :param object board_sub_type: 榜单子类型/Board sub type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['board_type', 'board_sub_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'board_type' in params:
            query_params.append(('board_type', params['board_type']))  # noqa: E501
        if 'board_sub_type' in params:
            query_params.append(('board_sub_type', params['board_sub_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_hot_search_list', 'GET',
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

    def fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get(self, **kwargs):  # noqa: E501
        """获取抖音直播热搜榜数据/Get Douyin live hot search list data  # noqa: E501

        # [中文] ### 用途: - 获取抖音直播热搜榜数据 ### 返回: - 直播热搜榜数据  # [English] ### Purpose: - Get Douyin live hot search list data ### Return: - Live hot search list data  # [示例/Example] pass  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取抖音直播热搜榜数据/Get Douyin live hot search list data  # noqa: E501

        # [中文] ### 用途: - 获取抖音直播热搜榜数据 ### 返回: - 直播热搜榜数据  # [English] ### Purpose: - Get Douyin live hot search list data ### Return: - Live hot search list data  # [示例/Example] pass  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get_with_http_info(async_req=True)
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
                    " to method fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get" % key
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
            '/api/v1/douyin/app/v3/fetch_live_hot_search_list', 'GET',
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

    def fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的直播搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212789e0 ### 参数: - keyword: 关键词 - cursor: 偏移量，从0开始，每次请求从上次请求返回响应中的cursor中获取。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 直播搜索结果  # [English] ### Purpose: - Get live search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212789e0 ### Parameters: - keyword: Keyword - cursor: Offset, starting from 0, each request gets from the cursor in the response returned by the last request. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Live search results  # [示例/Example] keyword = \"小米商城\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object cursor: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的直播搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212789e0 ### 参数: - keyword: 关键词 - cursor: 偏移量，从0开始，每次请求从上次请求返回响应中的cursor中获取。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 直播搜索结果  # [English] ### Purpose: - Get live search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212789e0 ### Parameters: - keyword: Keyword - cursor: Offset, starting from 0, each request gets from the cursor in the response returned by the last request. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Live search results  # [示例/Example] keyword = \"小米商城\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object cursor: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_live_search_result', 'GET',
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

    def fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post(self, **kwargs):  # noqa: E501
        """批量获取视频信息 V1/Batch Get Video Information V1  # noqa: E501

        # [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。 ### 参数: - aweme_ids: 作品id列表，最多支持10个作品id。 ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface charges a fixed price of 0.001$ * 10 = 0.01$ each time. ### Parameters: - aweme_ids: List of video ids, up to 10 video ids are supported. ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_ids = [\"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post_with_http_info(self, **kwargs):  # noqa: E501
        """批量获取视频信息 V1/Batch Get Video Information V1  # noqa: E501

        # [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。 ### 参数: - aweme_ids: 作品id列表，最多支持10个作品id。 ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface charges a fixed price of 0.001$ * 10 = 0.01$ each time. ### Parameters: - aweme_ids: List of video ids, up to 10 video ids are supported. ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_ids = [\"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post_with_http_info(async_req=True)
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
                    " to method fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post" % key
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
            '/api/v1/douyin/app/v3/fetch_multi_video', 'POST',
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

    def fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post(self, **kwargs):  # noqa: E501
        """批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos  # noqa: E501

        # [中文] ### 用途: - 此接口目前优惠活动价为$0.25，活动结束后恢复原价$0.5。不足50个视频按50个视频收费。 - 批量获取视频的最高画质(原始上传画质)播放链接 - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。 - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。 - 此接口非常适合用于批量获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。 - 使用并发请求，提高批量获取效率。 - 最多支持50个视频ID。 ### 参数: - aweme_ids: 作品id列表，用逗号分隔，例如: \"123,456,789\"，最多50个。 ### 返回: - total: 总数 - success_count: 成功数量 - failed_count: 失败数量 - videos: 视频列表，每个视频包含以下字段：     - video_id: 作品id     - original_video_url: 最高画质(原始上传画质)播放链接     - file_size: 文件大小（字节）     - file_size_in_mb: 文件大小（MB）     - content_type: 内容类型     - success: 是否成功     - error: 错误信息（如果失败） ### 备注: - 由于数量较多，处理时间可能会稍长，请增加等待时间。  # [English] ### Purpose: - This interface is currently on sale for $0.25, and will return to the original price of $0.5 after the event ends. If there are less than 50 videos, they will be charged as 50 videos. - Batch get the highest quality (original upload quality) play URL of videos - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata. - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface. - This interface is very suitable for batch obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc. - Use concurrent requests to improve batch acquisition efficiency. - Support up to 50 video IDs. ### Parameters: - aweme_ids: Video id list, separated by commas, for example: \"123,456,789\", up to 50. ### Return: - total: Total count - success_count: Success count - failed_count: Failed count - videos: Video list, each video contains the following fields:     - video_id: Video id     - original_video_url: Highest quality (original upload quality) play URL     - file_size: File size (bytes)     - file_size_in_mb: File size (MB)     - content_type: Content type     - success: Whether successful     - error: Error message (if failed) ### Note: - Due to the large number, the processing time may be slightly longer, please increase the waiting time. # [示例/Example] aweme_ids = \"7512756548356492544,7448118827402972455,7126745726494821640\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post_with_http_info(self, **kwargs):  # noqa: E501
        """批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos  # noqa: E501

        # [中文] ### 用途: - 此接口目前优惠活动价为$0.25，活动结束后恢复原价$0.5。不足50个视频按50个视频收费。 - 批量获取视频的最高画质(原始上传画质)播放链接 - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。 - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。 - 此接口非常适合用于批量获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。 - 使用并发请求，提高批量获取效率。 - 最多支持50个视频ID。 ### 参数: - aweme_ids: 作品id列表，用逗号分隔，例如: \"123,456,789\"，最多50个。 ### 返回: - total: 总数 - success_count: 成功数量 - failed_count: 失败数量 - videos: 视频列表，每个视频包含以下字段：     - video_id: 作品id     - original_video_url: 最高画质(原始上传画质)播放链接     - file_size: 文件大小（字节）     - file_size_in_mb: 文件大小（MB）     - content_type: 内容类型     - success: 是否成功     - error: 错误信息（如果失败） ### 备注: - 由于数量较多，处理时间可能会稍长，请增加等待时间。  # [English] ### Purpose: - This interface is currently on sale for $0.25, and will return to the original price of $0.5 after the event ends. If there are less than 50 videos, they will be charged as 50 videos. - Batch get the highest quality (original upload quality) play URL of videos - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata. - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface. - This interface is very suitable for batch obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc. - Use concurrent requests to improve batch acquisition efficiency. - Support up to 50 video IDs. ### Parameters: - aweme_ids: Video id list, separated by commas, for example: \"123,456,789\", up to 50. ### Return: - total: Total count - success_count: Success count - failed_count: Failed count - videos: Video list, each video contains the following fields:     - video_id: Video id     - original_video_url: Highest quality (original upload quality) play URL     - file_size: File size (bytes)     - file_size_in_mb: File size (MB)     - content_type: Content type     - success: Whether successful     - error: Error message (if failed) ### Note: - Due to the large number, the processing time may be slightly longer, please increase the waiting time. # [示例/Example] aweme_ids = \"7512756548356492544,7448118827402972455,7126745726494821640\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post_with_http_info(async_req=True)
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
                    " to method fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post" % key
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
            '/api/v1/douyin/app/v3/fetch_multi_video_high_quality_play_url', 'POST',
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

    def fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get(self, aweme_ids, **kwargs):  # noqa: E501
        """根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)  # noqa: E501

        # [中文] ### 用途: - 根据视频ID获取作品的统计数据，支持多个视频id，一次性最多支持50个视频。 - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。 - 价格为：0.025$一次。 - 可以获取到的统计有：     - 点赞数（digg_count）     - 下载数（download_count）     - 播放数（play_count）     - 分享数（share_count） ### 参数: - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过50个，单个也可以，则无需逗号。 ### 返回: - 作品统计数据  # [English] ### Purpose: - Get the statistical data of the Post according to the video ID, support multiple video ids, up to 50 videos at a time. - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be obtained through this interface. - Price: 0.025$ each time. - List of statistics that can be obtained:     - Like count (digg_count)     - Download count (download_count)     - Play count (play_count)     - Share count (share_count) ### Parameters: - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 50, single is also possible, no need for commas. ### Return: - Post statistics data  # [示例/Example] aweme_ids = \"7448118827402972455,7126745726494821640\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get(aweme_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_ids: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get_with_http_info(aweme_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get_with_http_info(aweme_ids, **kwargs)  # noqa: E501
            return data

    def fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get_with_http_info(self, aweme_ids, **kwargs):  # noqa: E501
        """根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)  # noqa: E501

        # [中文] ### 用途: - 根据视频ID获取作品的统计数据，支持多个视频id，一次性最多支持50个视频。 - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。 - 价格为：0.025$一次。 - 可以获取到的统计有：     - 点赞数（digg_count）     - 下载数（download_count）     - 播放数（play_count）     - 分享数（share_count） ### 参数: - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过50个，单个也可以，则无需逗号。 ### 返回: - 作品统计数据  # [English] ### Purpose: - Get the statistical data of the Post according to the video ID, support multiple video ids, up to 50 videos at a time. - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be obtained through this interface. - Price: 0.025$ each time. - List of statistics that can be obtained:     - Like count (digg_count)     - Download count (download_count)     - Play count (play_count)     - Share count (share_count) ### Parameters: - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 50, single is also possible, no need for commas. ### Return: - Post statistics data  # [示例/Example] aweme_ids = \"7448118827402972455,7126745726494821640\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get_with_http_info(aweme_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_ids: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_ids' is set
        if self.api_client.client_side_validation and ('aweme_ids' not in params or
                                                       params['aweme_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_ids` when calling `fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_ids' in params:
            query_params.append(('aweme_ids', params['aweme_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_multi_video_statistics', 'GET',
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

    def fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post(self, **kwargs):  # noqa: E501
        """批量获取视频信息 V2/Batch Get Video Information V2  # noqa: E501

        # [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持50个视频，此接口收费固定价格为0.001$ * 50 = 0.05$一次。 ### 参数: - aweme_ids: 作品id列表，最多支持50个作品id。 ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 50 videos at a time, this interface charges a fixed price of 0.001$ * 50 = 0.05$ each time. ### Parameters: - aweme_ids: List of video ids, up to 50 video ids are supported. ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_ids = [\"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post_with_http_info(self, **kwargs):  # noqa: E501
        """批量获取视频信息 V2/Batch Get Video Information V2  # noqa: E501

        # [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持50个视频，此接口收费固定价格为0.001$ * 50 = 0.05$一次。 ### 参数: - aweme_ids: 作品id列表，最多支持50个作品id。 ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 50 videos at a time, this interface charges a fixed price of 0.001$ * 50 = 0.05$ each time. ### Parameters: - aweme_ids: List of video ids, up to 50 video ids are supported. ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_ids = [\"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\", \"7448118827402972455\", \"7126745726494821640\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post_with_http_info(async_req=True)
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
                    " to method fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post" % key
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
            '/api/v1/douyin/app/v3/fetch_multi_video_v2', 'POST',
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

    def fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get(self, music_id, **kwargs):  # noqa: E501
        """获取指定音乐的详情数据/Get details of specified music  # noqa: E501

        # [中文] ### 用途: - 获取指定音乐的详情数据 ### 参数: - music_id: 音乐id ### 返回: - 音乐详情数据  # [English] ### Purpose: - Get details of specified music ### Parameters: - music_id: Music id ### Return: - Music details data  # [示例/Example] music_id = \"7136850194742315016\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get(music_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object music_id: 音乐id/Music id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get_with_http_info(music_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get_with_http_info(music_id, **kwargs)  # noqa: E501
            return data

    def fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get_with_http_info(self, music_id, **kwargs):  # noqa: E501
        """获取指定音乐的详情数据/Get details of specified music  # noqa: E501

        # [中文] ### 用途: - 获取指定音乐的详情数据 ### 参数: - music_id: 音乐id ### 返回: - 音乐详情数据  # [English] ### Purpose: - Get details of specified music ### Parameters: - music_id: Music id ### Return: - Music details data  # [示例/Example] music_id = \"7136850194742315016\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get_with_http_info(music_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object music_id: 音乐id/Music id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['music_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'music_id' is set
        if self.api_client.client_side_validation and ('music_id' not in params or
                                                       params['music_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `music_id` when calling `fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'music_id' in params:
            query_params.append(('music_id', params['music_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_music_detail', 'GET',
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

    def fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get(self, **kwargs):  # noqa: E501
        """获取抖音音乐榜数据/Get Douyin music hot search list data  # noqa: E501

        # [中文] ### 用途: - 获取抖音音乐热榜数据 ### 参数: - chart_type: 榜单类型，默认值为'hot'，支持下面的值：     - 'hot': 热门榜     - 'trending': 飙升榜     - 'original': 原创榜 - cursor: 游标，默认值为'0'，用于分页获取数据，每次请求后会返回下一个游标值，并且通过 `has_more` 字段指示是否有更多数据可供获取。 ### 返回: - 音乐热搜榜数据  # [English] ### Purpose: - Get Douyin music hot search list data ### Parameters: - chart_type: Chart type, default value is 'hot', supports the following values:     - 'hot': Hot chart     - 'trending': Trending chart     - 'original': Original chart - cursor: Cursor, default value is '0', used for paginating data retrieval. After each request, the next cursor value will be returned, and the `has_more` field indicates whether there is more data available. ### Return: - Music hot search list data  # [示例/Example] chart_type = \"hot\" cursor = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object chart_type: 榜单类型/Chart type
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取抖音音乐榜数据/Get Douyin music hot search list data  # noqa: E501

        # [中文] ### 用途: - 获取抖音音乐热榜数据 ### 参数: - chart_type: 榜单类型，默认值为'hot'，支持下面的值：     - 'hot': 热门榜     - 'trending': 飙升榜     - 'original': 原创榜 - cursor: 游标，默认值为'0'，用于分页获取数据，每次请求后会返回下一个游标值，并且通过 `has_more` 字段指示是否有更多数据可供获取。 ### 返回: - 音乐热搜榜数据  # [English] ### Purpose: - Get Douyin music hot search list data ### Parameters: - chart_type: Chart type, default value is 'hot', supports the following values:     - 'hot': Hot chart     - 'trending': Trending chart     - 'original': Original chart - cursor: Cursor, default value is '0', used for paginating data retrieval. After each request, the next cursor value will be returned, and the `has_more` field indicates whether there is more data available. ### Return: - Music hot search list data  # [示例/Example] chart_type = \"hot\" cursor = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object chart_type: 榜单类型/Chart type
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chart_type', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'chart_type' in params:
            query_params.append(('chart_type', params['chart_type']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_music_hot_search_list', 'GET',
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

    def fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的音乐搜索结果（弃用，替代接口见下方文档说明）/Get music search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的音乐搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212797e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 音乐搜索结果  # [English] ### Purpose: - Get music search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212797e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Music search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的音乐搜索结果（弃用，替代接口见下方文档说明）/Get music search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的音乐搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212797e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 音乐搜索结果  # [English] ### Purpose: - Get music search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212797e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Music search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_music_search_result', 'GET',
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

    def fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get(self, music_id, **kwargs):  # noqa: E501
        """获取指定音乐的视频列表数据/Get video list of specified music  # noqa: E501

        # [中文] ### 用途: - 获取指定音乐的视频列表数据 ### 参数: - music_id: 音乐id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 音乐视频列表数据  # [English] ### Purpose: - Get video list of specified music ### Parameters: - music_id: Music id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Music video list data  # [示例/Example] music_id = \"7136850194742315016\" cursor = 0 count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get(music_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object music_id: 音乐id/Music id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get_with_http_info(music_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get_with_http_info(music_id, **kwargs)  # noqa: E501
            return data

    def fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get_with_http_info(self, music_id, **kwargs):  # noqa: E501
        """获取指定音乐的视频列表数据/Get video list of specified music  # noqa: E501

        # [中文] ### 用途: - 获取指定音乐的视频列表数据 ### 参数: - music_id: 音乐id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 音乐视频列表数据  # [English] ### Purpose: - Get video list of specified music ### Parameters: - music_id: Music id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Music video list data  # [示例/Example] music_id = \"7136850194742315016\" cursor = 0 count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get_with_http_info(music_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object music_id: 音乐id/Music id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['music_id', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'music_id' is set
        if self.api_client.client_side_validation and ('music_id' not in params or
                                                       params['music_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `music_id` when calling `fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'music_id' in params:
            query_params.append(('music_id', params['music_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_music_video_list', 'GET',
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

    def fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据，支持图文、视频等。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Get single video data, support photo, video, etc. ### Parameters: - aweme_id: Video id ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_id = \"7448118827402972455\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据，支持图文、视频等。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Get single video data, support photo, video, etc. ### Parameters: - aweme_id: Video id ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_id = \"7448118827402972455\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_one_video', 'GET',
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

    def fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get(self, share_url, **kwargs):  # noqa: E501
        """根据分享链接获取单个作品数据/Get single video data by sharing link  # noqa: E501

        # [中文] ### 用途: - 根据分享链接获取单个作品数据 ### 参数: - share_url: 分享链接 ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Get single video data by sharing link ### Parameters: - share_url: Share link ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] share_url = \"https://v.douyin.com/e3x2fjE/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get(share_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_url: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get_with_http_info(share_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get_with_http_info(share_url, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get_with_http_info(self, share_url, **kwargs):  # noqa: E501
        """根据分享链接获取单个作品数据/Get single video data by sharing link  # noqa: E501

        # [中文] ### 用途: - 根据分享链接获取单个作品数据 ### 参数: - share_url: 分享链接 ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Get single video data by sharing link ### Parameters: - share_url: Share link ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] share_url = \"https://v.douyin.com/e3x2fjE/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get_with_http_info(share_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_url: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['share_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_url' is set
        if self.api_client.client_side_validation and ('share_url' not in params or
                                                       params['share_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_url` when calling `fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_url' in params:
            query_params.append(('share_url', params['share_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_one_video_by_share_url', 'GET',
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

    def fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get(self, share_code, **kwargs):  # noqa: E501
        """根据分享口令获取分享信息/Get share info by share code  # noqa: E501

        # [中文] ### 用途: - 根据分享口令获取分享信息，比如抖音文章的分享口令提取分享人信息和文章ID等然后再去请求单一作品数据接口获取文章内容。 ### 参数: - share_code: 分享口令 ### 返回: - 分享信息，包含分享人信息和文章ID等  # [English] ### Purpose: - Get share info by share code, such as extracting sharer information and article ID from Douyin article share code, and then requesting a single video data interface to get the article content. ### Parameters: - share_code: Share code ### Return: - Share info, including sharer information and article ID, etc.  # [示例/Example] share_code = \"8:/ h@O.kP 05/21 【生意场上，装逼就是节省沟通成本】长按复制打开抖音，即可阅读文章 ︽︽2QnCB9aIZZ29︽︽\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get(share_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_code: 分享口令/Share code (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get_with_http_info(share_code, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get_with_http_info(share_code, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get_with_http_info(self, share_code, **kwargs):  # noqa: E501
        """根据分享口令获取分享信息/Get share info by share code  # noqa: E501

        # [中文] ### 用途: - 根据分享口令获取分享信息，比如抖音文章的分享口令提取分享人信息和文章ID等然后再去请求单一作品数据接口获取文章内容。 ### 参数: - share_code: 分享口令 ### 返回: - 分享信息，包含分享人信息和文章ID等  # [English] ### Purpose: - Get share info by share code, such as extracting sharer information and article ID from Douyin article share code, and then requesting a single video data interface to get the article content. ### Parameters: - share_code: Share code ### Return: - Share info, including sharer information and article ID, etc.  # [示例/Example] share_code = \"8:/ h@O.kP 05/21 【生意场上，装逼就是节省沟通成本】长按复制打开抖音，即可阅读文章 ︽︽2QnCB9aIZZ29︽︽\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get_with_http_info(share_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_code: 分享口令/Share code (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['share_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_code' is set
        if self.api_client.client_side_validation and ('share_code' not in params or
                                                       params['share_code'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_code` when calling `fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_code' in params:
            query_params.append(('share_code', params['share_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_share_info_by_share_code', 'GET',
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

    def fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据，支持图文、视频等。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Get single video data, support photo, video, etc. ### Parameters: - aweme_id: Video id ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_id = \"7448118827402972455\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据，支持图文、视频等。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据 ### 备注: - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：     - JSON PATH: $.data.filter_list[0].reason     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）     - 8：视频不存在或已被删除     - 5：该内容被标记为私人内容，没有公开展示权限     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见     - 更多状态码请提交给我们的客户支持进行补充。  # [English] ### Purpose: - Get single video data, support photo, video, etc. ### Parameters: - aweme_id: Video id ### Return: - Video data ### Note: - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:     - JSON PATH: $.data.filter_list[0].reason     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)     - 8: The video does not exist or has been deleted     - 5: This content is marked as private content and does not have public display permissions     - 10: This content is marked as partially visible, only visible to some users chosen by the author     - For more status codes, please submit them to our customer support for supplementation.  # [示例/Example] aweme_id = \"7448118827402972455\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_one_video_v2', 'GET',
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

    def fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V3 (无版权限制)/Get single video data V3 (No copyright restrictions)  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据，支持文章、图文、视频等。 - V3版本的接口，解决了版权限制问题，可以获取更多受限内容，比如 V1，V2版本返回的Reason为8的内容和部分文章或短剧等。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data, support article, photo, video, etc. - V3 version of the interface, which solves the copyright restriction problem and can obtain more restricted content, such as content with Reason 8 returned by V1 and V2 versions and some articles or short dramas. ### Parameters: - aweme_id: Video id ### Return: - Video data  # [示例/Example] aweme_id = \"7592116912205630761\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品或文章ID/Video or Article ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V3 (无版权限制)/Get single video data V3 (No copyright restrictions)  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据，支持文章、图文、视频等。 - V3版本的接口，解决了版权限制问题，可以获取更多受限内容，比如 V1，V2版本返回的Reason为8的内容和部分文章或短剧等。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data, support article, photo, video, etc. - V3 version of the interface, which solves the copyright restriction problem and can obtain more restricted content, such as content with Reason 8 returned by V1 and V2 versions and some articles or short dramas. ### Parameters: - aweme_id: Video id ### Return: - Video data  # [示例/Example] aweme_id = \"7592116912205630761\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品或文章ID/Video or Article ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_one_video_v3', 'GET',
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

    def fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get(self, series_id, **kwargs):  # noqa: E501
        """获取短剧详情信息/Get series detail  # noqa: E501

        # [中文] ### 用途: - 获取短剧详情信息 ### 参数: - series_id: 短剧id ### 返回: - 短剧详情数据 ### 备注: - 该接口返回短剧的详细信息，包括：     - 短剧名称、描述、封面     - 作者信息     - 总集数、更新状态     - 播放量、收藏量等统计数据     - 付费信息（如有）  # [English] ### Purpose: - Get series/playlet detail information ### Parameters: - series_id: Series id ### Return: - Series detail data ### Note: - This interface returns detailed information of the series, including:     - Series name, description, cover     - Author information     - Total episodes, update status     - Play count, collection count and other statistics     - Payment information (if any)  # [示例/Example] series_id = \"7592054624643713067\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get(series_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object series_id: 短剧id/Series id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get_with_http_info(series_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get_with_http_info(series_id, **kwargs)  # noqa: E501
            return data

    def fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get_with_http_info(self, series_id, **kwargs):  # noqa: E501
        """获取短剧详情信息/Get series detail  # noqa: E501

        # [中文] ### 用途: - 获取短剧详情信息 ### 参数: - series_id: 短剧id ### 返回: - 短剧详情数据 ### 备注: - 该接口返回短剧的详细信息，包括：     - 短剧名称、描述、封面     - 作者信息     - 总集数、更新状态     - 播放量、收藏量等统计数据     - 付费信息（如有）  # [English] ### Purpose: - Get series/playlet detail information ### Parameters: - series_id: Series id ### Return: - Series detail data ### Note: - This interface returns detailed information of the series, including:     - Series name, description, cover     - Author information     - Total episodes, update status     - Play count, collection count and other statistics     - Payment information (if any)  # [示例/Example] series_id = \"7592054624643713067\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get_with_http_info(series_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object series_id: 短剧id/Series id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['series_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'series_id' is set
        if self.api_client.client_side_validation and ('series_id' not in params or
                                                       params['series_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `series_id` when calling `fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'series_id' in params:
            query_params.append(('series_id', params['series_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_series_detail', 'GET',
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

    def fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get(self, series_id, **kwargs):  # noqa: E501
        """获取短剧视频列表/Get series video list  # noqa: E501

        # [中文] ### 用途: - 获取短剧视频列表 ### 参数: - series_id: 短剧id - cursor: 游标，用于翻页，第一页为0，第二页通常为count的值（如15）。 ### 返回: - 短剧视频列表数据 ### 备注: - 该接口返回短剧中的所有视频列表 - 响应中的 aweme_list 包含短剧的各集视频信息 - has_more 字段表示是否还有更多数据  # [English] ### Purpose: - Get series/playlet video list ### Parameters: - series_id: Series id - cursor: Cursor, used for paging, the first page is 0, the second page is usually the value of count (e.g., 15). ### Return: - Series video list data ### Note: - This interface returns all video list in the series - The aweme_list in the response contains video information of each episode - The has_more field indicates whether there is more data  # [示例/Example] series_id = \"7592054624643713067\" cursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get(series_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object series_id: 短剧id/Series id (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get_with_http_info(series_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get_with_http_info(series_id, **kwargs)  # noqa: E501
            return data

    def fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get_with_http_info(self, series_id, **kwargs):  # noqa: E501
        """获取短剧视频列表/Get series video list  # noqa: E501

        # [中文] ### 用途: - 获取短剧视频列表 ### 参数: - series_id: 短剧id - cursor: 游标，用于翻页，第一页为0，第二页通常为count的值（如15）。 ### 返回: - 短剧视频列表数据 ### 备注: - 该接口返回短剧中的所有视频列表 - 响应中的 aweme_list 包含短剧的各集视频信息 - has_more 字段表示是否还有更多数据  # [English] ### Purpose: - Get series/playlet video list ### Parameters: - series_id: Series id - cursor: Cursor, used for paging, the first page is 0, the second page is usually the value of count (e.g., 15). ### Return: - Series video list data ### Note: - This interface returns all video list in the series - The aweme_list in the response contains video information of each episode - The has_more field indicates whether there is more data  # [示例/Example] series_id = \"7592054624643713067\" cursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get_with_http_info(series_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object series_id: 短剧id/Series id (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['series_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'series_id' is set
        if self.api_client.client_side_validation and ('series_id' not in params or
                                                       params['series_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `series_id` when calling `fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'series_id' in params:
            query_params.append(('series_id', params['series_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_series_video_list', 'GET',
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

    def fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get(self, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Get user fans list  # noqa: E501

        # [中文] ### 用途: - 获取用户粉丝列表 ### 参数: - sec_user_id: 用户sec_user_id - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。 - count: 数量，默认为20，建议保持不变。 ### 返回: - 粉丝列表  # [English] ### Purpose: - Get user fans list ### Parameters: - sec_user_id: User sec_user_id - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging. - count: Number, default is 20, it is recommended to keep it unchanged. ### Return: - Fans list  # [示例/Example] sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\" max_time = \"0\" count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object max_time: 最大时间戳/Maximum timestamp
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Get user fans list  # noqa: E501

        # [中文] ### 用途: - 获取用户粉丝列表 ### 参数: - sec_user_id: 用户sec_user_id - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。 - count: 数量，默认为20，建议保持不变。 ### 返回: - 粉丝列表  # [English] ### Purpose: - Get user fans list ### Parameters: - sec_user_id: User sec_user_id - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging. - count: Number, default is 20, it is recommended to keep it unchanged. ### Return: - Fans list  # [示例/Example] sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\" max_time = \"0\" count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object max_time: 最大时间戳/Maximum timestamp
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'max_time', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'max_time' in params:
            query_params.append(('max_time', params['max_time']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_user_fans_list', 'GET',
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

    def fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get(self, **kwargs):  # noqa: E501
        """获取用户关注列表 (弃用，使用 /api/v1/douyin/web/fetch_user_following_list 替代)/Get user following list (Deprecated, use /api/v1/douyin/web/fetch_user_following_list instead)  # noqa: E501

        # [中文] ### 用途: - 获取用户关注列表 ### 参数: - sec_user_id: 用户sec_user_id - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。 - count: 数量，默认为20，建议保持不变。 ### 返回: - 关注列表  # [English] ### Purpose: - Get user following list ### Parameters: - sec_user_id: User sec_user_id - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging. - count: Number, default is 20, it is recommended to keep it unchanged. ### Return: - Following list  # [示例/Example] sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\" max_time = \"0\" count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object max_time: 最大时间戳/Maximum timestamp
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户关注列表 (弃用，使用 /api/v1/douyin/web/fetch_user_following_list 替代)/Get user following list (Deprecated, use /api/v1/douyin/web/fetch_user_following_list instead)  # noqa: E501

        # [中文] ### 用途: - 获取用户关注列表 ### 参数: - sec_user_id: 用户sec_user_id - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。 - count: 数量，默认为20，建议保持不变。 ### 返回: - 关注列表  # [English] ### Purpose: - Get user following list ### Parameters: - sec_user_id: User sec_user_id - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging. - count: Number, default is 20, it is recommended to keep it unchanged. ### Return: - Following list  # [示例/Example] sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\" max_time = \"0\" count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object max_time: 最大时间戳/Maximum timestamp
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'max_time', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'max_time' in params:
            query_params.append(('max_time', params['max_time']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_user_following_list', 'GET',
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

    def fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get(self, sec_user_id, **kwargs):  # noqa: E501
        """获取用户喜欢作品数据/Get user like video data  # noqa: E501

        # [中文] ### 用途: - 获取用户喜欢作品数据 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user like video data ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object counts: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get_with_http_info(self, sec_user_id, **kwargs):  # noqa: E501
        """获取用户喜欢作品数据/Get user like video data  # noqa: E501

        # [中文] ### 用途: - 获取用户喜欢作品数据 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user like video data ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get_with_http_info(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object counts: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'max_cursor', 'counts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_user_id' is set
        if self.api_client.client_side_validation and ('sec_user_id' not in params or
                                                       params['sec_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_id` when calling `fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'max_cursor' in params:
            query_params.append(('max_cursor', params['max_cursor']))  # noqa: E501
        if 'counts' in params:
            query_params.append(('counts', params['counts']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_user_like_videos', 'GET',
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

    def fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get(self, sec_user_id, **kwargs):  # noqa: E501
        """获取用户主页作品数据/Get user homepage video data  # noqa: E501

        # [中文] ### 用途: - 获取用户主页作品数据 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量，不要超过20，建议保持不变。 - sort_type: 排序类型，可选值如下：     - `0`: 最新排序-默认     - `1`: 最热排序 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number, do not exceed 20, it is recommended to keep it unchanged. - sort_type: Sort type, optional values are as follows:     - `0`: Latest sorting - default     - `1`: Hottest sorting ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\" max_cursor = 0 counts = 20 sort_type = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object count: 每页数量/Number per page
        :param object sort_type: 排序类型/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get_with_http_info(self, sec_user_id, **kwargs):  # noqa: E501
        """获取用户主页作品数据/Get user homepage video data  # noqa: E501

        # [中文] ### 用途: - 获取用户主页作品数据 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量，不要超过20，建议保持不变。 - sort_type: 排序类型，可选值如下：     - `0`: 最新排序-默认     - `1`: 最热排序 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number, do not exceed 20, it is recommended to keep it unchanged. - sort_type: Sort type, optional values are as follows:     - `0`: Latest sorting - default     - `1`: Hottest sorting ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\" max_cursor = 0 counts = 20 sort_type = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get_with_http_info(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object count: 每页数量/Number per page
        :param object sort_type: 排序类型/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'max_cursor', 'count', 'sort_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_user_id' is set
        if self.api_client.client_side_validation and ('sec_user_id' not in params or
                                                       params['sec_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_id` when calling `fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'max_cursor' in params:
            query_params.append(('max_cursor', params['max_cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_user_post_videos', 'GET',
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

    def fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的用户搜索结果（弃用，替代接口见下方文档说明）/Get user search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的用户搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212785e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 - douyin_user_fans(粉丝数量):     - \"\": 不限     - \"0_1k\": 1000以下     - \"1k_1w\": 1000-1万     - \"1w_10w\": 1w-10w     - \"10w_100w\": 10w-100w     - \"100w_\": 100w以上 - douyin_user_type(用户类型，请使用英文而不是中文):     - \"\": 不限     - \"common_user\": 普通用户     - \"enterprise_user\": 企业认证     - \"personal_user\": 个人认证 ### 返回: - 用户搜索结果  # [English] ### Purpose: - Get user search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212785e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. - douyin_user_fans(Fans):     - \"\": Unlimited     - \"0_1k\": Less than 1000     - \"1k_1w\": 1000-10,000     - \"1w_10w\": 10,000-100,000     - \"10w_100w\": 100,000-1,000,000     - \"100w_\": More than 1,000,000 - douyin_user_type(User type, please use English instead of Chinese):     - \"\": Unlimited     - \"common_user\": Common user     - \"enterprise_user\": Enterprise certification     - \"personal_user\": Personal certification ### Return: - User search results  # [示例/Example] keyword = \"动漫\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object douyin_user_fans: 粉丝数/Fans
        :param object douyin_user_type: 用户类型/User type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的用户搜索结果（弃用，替代接口见下方文档说明）/Get user search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的用户搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212785e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 - douyin_user_fans(粉丝数量):     - \"\": 不限     - \"0_1k\": 1000以下     - \"1k_1w\": 1000-1万     - \"1w_10w\": 1w-10w     - \"10w_100w\": 10w-100w     - \"100w_\": 100w以上 - douyin_user_type(用户类型，请使用英文而不是中文):     - \"\": 不限     - \"common_user\": 普通用户     - \"enterprise_user\": 企业认证     - \"personal_user\": 个人认证 ### 返回: - 用户搜索结果  # [English] ### Purpose: - Get user search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212785e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. - douyin_user_fans(Fans):     - \"\": Unlimited     - \"0_1k\": Less than 1000     - \"1k_1w\": 1000-10,000     - \"1w_10w\": 10,000-100,000     - \"10w_100w\": 100,000-1,000,000     - \"100w_\": More than 1,000,000 - douyin_user_type(User type, please use English instead of Chinese):     - \"\": Unlimited     - \"common_user\": Common user     - \"enterprise_user\": Enterprise certification     - \"personal_user\": Personal certification ### Return: - User search results  # [示例/Example] keyword = \"动漫\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object douyin_user_fans: 粉丝数/Fans
        :param object douyin_user_type: 用户类型/User type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'douyin_user_fans', 'douyin_user_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'douyin_user_fans' in params:
            query_params.append(('douyin_user_fans', params['douyin_user_fans']))  # noqa: E501
        if 'douyin_user_type' in params:
            query_params.append(('douyin_user_type', params['douyin_user_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_user_search_result', 'GET',
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

    def fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get(self, **kwargs):  # noqa: E501
        """获取用户短剧合集列表/Get user series list  # noqa: E501

        # [中文] ### 用途: - 获取用户的短剧合集列表 ### 参数: - user_id: 用户id，与sec_user_id二选一即可 - sec_user_id: 用户加密id，与user_id二选一即可 - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 ### 返回: - 用户短剧合集列表数据 ### 备注: - 该接口返回用户发布的所有短剧合集 - 响应中的 series_id 可用于获取短剧详情和视频列表  # [English] ### Purpose: - Get user's series/playlet collection list ### Parameters: - user_id: User id - sec_user_id: User encrypted id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. ### Return: - User series list data ### Note: - This interface returns all series collections published by the user - The series_id in the response can be used to get series details and video list  # [示例/Example] user_id = \"3010877781453635\" sec_user_id = \"MS4wLjABAAAAfAU5kMk-W4569G1z2iRsy8t6-kOxO17Eaz6yte4NQokeUeOpeqTGEc480e34O8lK\" cursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id
        :param object sec_user_id: 用户加密id/User sec id
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户短剧合集列表/Get user series list  # noqa: E501

        # [中文] ### 用途: - 获取用户的短剧合集列表 ### 参数: - user_id: 用户id，与sec_user_id二选一即可 - sec_user_id: 用户加密id，与user_id二选一即可 - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 ### 返回: - 用户短剧合集列表数据 ### 备注: - 该接口返回用户发布的所有短剧合集 - 响应中的 series_id 可用于获取短剧详情和视频列表  # [English] ### Purpose: - Get user's series/playlet collection list ### Parameters: - user_id: User id - sec_user_id: User encrypted id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. ### Return: - User series list data ### Note: - This interface returns all series collections published by the user - The series_id in the response can be used to get series details and video list  # [示例/Example] user_id = \"3010877781453635\" sec_user_id = \"MS4wLjABAAAAfAU5kMk-W4569G1z2iRsy8t6-kOxO17Eaz6yte4NQokeUeOpeqTGEc480e34O8lK\" cursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id
        :param object sec_user_id: 用户加密id/User sec id
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'sec_user_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_user_series_list', 'GET',
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

    def fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个视频评论数据/Get single video comments data  # noqa: E501

        # [中文] ### 用途: - 获取单个视频评论数据 ### 参数: - aweme_id: 作品id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 评论数据  # [English] ### Purpose: - Get single video comments data ### Parameters: - aweme_id: Video id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Comments data  # [示例/Example] aweme_id = \"7448118827402972455\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个视频评论数据/Get single video comments data  # noqa: E501

        # [中文] ### 用途: - 获取单个视频评论数据 ### 参数: - aweme_id: 作品id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 评论数据  # [English] ### Purpose: - Get single video comments data ### Parameters: - aweme_id: Video id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Comments data  # [示例/Example] aweme_id = \"7448118827402972455\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_video_comments', 'GET',
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

    def fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get(self, item_id, comment_id, **kwargs):  # noqa: E501
        """获取指定视频的评论回复数据/Get comment replies data of specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的评论回复数据 ### 参数: - item_id: 作品id - comment_id: 评论id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 评论回复数据  # [English] ### Purpose: - Get comment replies data of specified video ### Parameters: - item_id: Video id - comment_id: Comment id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Comment replies data  # [示例/Example] aweme_id = \"7354666303006723354\" comment_id = \"7354669356632638218\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
        :param object comment_id: 评论id/Comment id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get_with_http_info(self, item_id, comment_id, **kwargs):  # noqa: E501
        """获取指定视频的评论回复数据/Get comment replies data of specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的评论回复数据 ### 参数: - item_id: 作品id - comment_id: 评论id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 评论回复数据  # [English] ### Purpose: - Get comment replies data of specified video ### Parameters: - item_id: Video id - comment_id: Comment id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Comment replies data  # [示例/Example] aweme_id = \"7354666303006723354\" comment_id = \"7354669356632638218\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get_with_http_info(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
        :param object comment_id: 评论id/Comment id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'comment_id', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_video_comment_replies', 'GET',
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

    def fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get(self, **kwargs):  # noqa: E501
        """获取视频的最高画质播放链接/Get the highest quality play URL of the video  # noqa: E501

        # [中文] ### 用途: - 价格：0.005$ 一次。 - 获取视频的最高画质(原始上传画质)播放链接 - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。 - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。 - 此接口非常适合用于获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。 - 一般情况都可以在线播放，如果不行，可以尝试使用IDM或浏览器下载后播放。 ### 参数: - aweme_id: 作品id，优先使用aweme_id，如果没有则使用share_url。 - share_url: 可选，分享链接，如果提供了作品id，则此参数可以不传。 ### 返回: - video_id： 作品id - original_video_url： 最高画质(原始上传画质)播放链接 - video_data： 视频数据，包含视频的元数据，如时长、大小等。  # [English] ### Purpose: - Price: 0.005$ each time. - Get the highest quality (original upload quality) play URL of the video - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata. - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface. - This interface is very suitable for obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc. - Generally, it can be played online, if not, you can try to download it using IDM or a browser and then play it. ### Parameters: - aweme_id: Video id, prefer to use aweme_id, if not available, use share_url. - share_url: Optional, share link, if the video id is provided, this parameter can be omitted. ### Return: - video_id: Video id - original_video_url: Highest quality (original upload quality) play URL - video_data: Video data, including metadata such as duration, size, etc. # [示例/Example] aweme_id = \"7512756548356492544\" share_url = \"https://www.douyin.com/video/7512756548356492544\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id
        :param object share_url: 可选，分享链接/Optional, share link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取视频的最高画质播放链接/Get the highest quality play URL of the video  # noqa: E501

        # [中文] ### 用途: - 价格：0.005$ 一次。 - 获取视频的最高画质(原始上传画质)播放链接 - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。 - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。 - 此接口非常适合用于获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。 - 一般情况都可以在线播放，如果不行，可以尝试使用IDM或浏览器下载后播放。 ### 参数: - aweme_id: 作品id，优先使用aweme_id，如果没有则使用share_url。 - share_url: 可选，分享链接，如果提供了作品id，则此参数可以不传。 ### 返回: - video_id： 作品id - original_video_url： 最高画质(原始上传画质)播放链接 - video_data： 视频数据，包含视频的元数据，如时长、大小等。  # [English] ### Purpose: - Price: 0.005$ each time. - Get the highest quality (original upload quality) play URL of the video - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata. - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface. - This interface is very suitable for obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc. - Generally, it can be played online, if not, you can try to download it using IDM or a browser and then play it. ### Parameters: - aweme_id: Video id, prefer to use aweme_id, if not available, use share_url. - share_url: Optional, share link, if the video id is provided, this parameter can be omitted. ### Return: - video_id: Video id - original_video_url: Highest quality (original upload quality) play URL - video_data: Video data, including metadata such as duration, size, etc. # [示例/Example] aweme_id = \"7512756548356492544\" share_url = \"https://www.douyin.com/video/7512756548356492544\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id
        :param object share_url: 可选，分享链接/Optional, share link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id', 'share_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501
        if 'share_url' in params:
            query_params.append(('share_url', params['share_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_video_high_quality_play_url', 'GET',
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

    def fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get(self, mix_id, **kwargs):  # noqa: E501
        """获取抖音视频合集详情数据/Get Douyin video mix detail data  # noqa: E501

        # [中文] ### 用途: - 获取抖音视频合集详情数据 ### 参数: - mix_id: 合集id ### 返回: - 视频合集详情数据  # [English] ### Purpose: - Get Douyin video mix detail data ### Parameters: - mix_id: Mix id ### Return: - Video mix detail data  # [示例/Example] mix_id = \"7302011174286002217\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get(mix_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mix_id: 合集id/Mix id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get_with_http_info(mix_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get_with_http_info(mix_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get_with_http_info(self, mix_id, **kwargs):  # noqa: E501
        """获取抖音视频合集详情数据/Get Douyin video mix detail data  # noqa: E501

        # [中文] ### 用途: - 获取抖音视频合集详情数据 ### 参数: - mix_id: 合集id ### 返回: - 视频合集详情数据  # [English] ### Purpose: - Get Douyin video mix detail data ### Parameters: - mix_id: Mix id ### Return: - Video mix detail data  # [示例/Example] mix_id = \"7302011174286002217\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get_with_http_info(mix_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mix_id: 合集id/Mix id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mix_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mix_id' is set
        if self.api_client.client_side_validation and ('mix_id' not in params or
                                                       params['mix_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `mix_id` when calling `fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mix_id' in params:
            query_params.append(('mix_id', params['mix_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_video_mix_detail', 'GET',
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

    def fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get(self, mix_id, **kwargs):  # noqa: E501
        """获取抖音视频合集作品列表数据/Get Douyin video mix post list data  # noqa: E501

        # [中文] ### 用途: - 获取抖音视频合集作品列表数据 ### 参数: - mix_id: 合集id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 视频合集作品列表数据  # [English] ### Purpose: - Get Douyin video mix post list data ### Parameters: - mix_id: Mix id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Video mix post list data  # [示例/Example] mix_id = \"7302011174286002217\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get(mix_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mix_id: 合集id/Mix id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get_with_http_info(mix_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get_with_http_info(mix_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get_with_http_info(self, mix_id, **kwargs):  # noqa: E501
        """获取抖音视频合集作品列表数据/Get Douyin video mix post list data  # noqa: E501

        # [中文] ### 用途: - 获取抖音视频合集作品列表数据 ### 参数: - mix_id: 合集id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量，请保持默认，否则会出现BUG。 ### 返回: - 视频合集作品列表数据  # [English] ### Purpose: - Get Douyin video mix post list data ### Parameters: - mix_id: Mix id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number Please keep the default, otherwise there will be BUG. ### Return: - Video mix post list data  # [示例/Example] mix_id = \"7302011174286002217\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get_with_http_info(mix_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mix_id: 合集id/Mix id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mix_id', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mix_id' is set
        if self.api_client.client_side_validation and ('mix_id' not in params or
                                                       params['mix_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `mix_id` when calling `fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mix_id' in params:
            query_params.append(('mix_id', params['mix_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_video_mix_post_list', 'GET',
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

    def fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的视频搜索结果（弃用，替代接口见下方文档说明）/Get video search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的视频搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212780e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年 - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上 - content_type: 0:不限 1:视频 2:图文 ### 返回: - 视频搜索结果  # [English] ### Purpose: - Get video search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212780e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes - content_type: 0: Unlimited 1: Video 2: Graphic and text ### Return: - Video search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = \"0\" publish_time = \"0\" filter_duration = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object filter_duration: 时长/Duration
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的视频搜索结果（弃用，替代接口见下方文档说明）/Get video search results of specified keywords (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的视频搜索结果 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212780e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量，请保持默认，否则会出现BUG。 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年 - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上 - content_type: 0:不限 1:视频 2:图文 ### 返回: - 视频搜索结果  # [English] ### Purpose: - Get video search results of specified keywords - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212780e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number Please keep the default, otherwise there will be BUG. - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes - content_type: 0: Unlimited 1: Video 2: Graphic and text ### Return: - Video search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = \"0\" publish_time = \"0\" filter_duration = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object filter_duration: 时长/Duration
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'sort_type', 'publish_time', 'filter_duration']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'publish_time' in params:
            query_params.append(('publish_time', params['publish_time']))  # noqa: E501
        if 'filter_duration' in params:
            query_params.append(('filter_duration', params['filter_duration']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_video_search_result', 'GET',
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

    def fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。 - 收费标准为：0.01$每次请求。 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212780e0 ### 参数: - keyword: 关键词 - sort_type:     - 排序类型，可用值如下：     - _0 :综合(General)     - _1 :最多点赞(More likes)     - _2 :最新发布(New) - publish_time：     - 发布时间，可用值如下：     - _0 :不限(No Limit)     - _1 :一天之内(last 1 day)     - _7 :一周之内(last 1 week)     - _180 :半年之内(last half year) - filter_duration：     - 视频时长，可用值如下：     - _0 :不限(No Limit)     - _1 :1分钟以下(1 minute and below)     - _2 :1-5分钟 (1-5 minutes)     - _3 :5分钟以上(5 minutes more) - page: 页码     - 默认从1开始，然后依次递增加1 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 视频搜索结果V2  # [English] ### Purpose: - Get video search results of specified keywords V2, this interface has better stability and higher cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is recommended to use this interface. - The charging standard is: $0.01 per request. - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212780e0 ### Parameters: - keyword: Keyword - sort_type:     - Sort type, available values are as follows:     - _0 : General     - _1 : More likes     - _2 : New - publish_time:     - Publish time, available values are as follows:     - _0 : No Limit     - _1 : last 1 day     - _7 : last 1 week     - _180 : last half year - filter_duration:     - Duration filter, available values are as follows:     - _0 : No Limit     - _1 : 1 minute and below     - _2 : 1-5 minutes     - _3 : 5 minutes more - page: Page     - Start from 1 by default, then increase by 1 each time - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - Video search results V2  # [示例/Example] keyword = \"中华娘\" sort_type = \"_0\" publish_time = \"_0\" filter_duration = \"_0\" page = 1 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object filter_duration: 视频时长/Duration filter
        :param object page: 页码/Page
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated, see the documentation below for alternative interfaces)  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。 - 收费标准为：0.01$每次请求。 - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212780e0 ### 参数: - keyword: 关键词 - sort_type:     - 排序类型，可用值如下：     - _0 :综合(General)     - _1 :最多点赞(More likes)     - _2 :最新发布(New) - publish_time：     - 发布时间，可用值如下：     - _0 :不限(No Limit)     - _1 :一天之内(last 1 day)     - _7 :一周之内(last 1 week)     - _180 :半年之内(last half year) - filter_duration：     - 视频时长，可用值如下：     - _0 :不限(No Limit)     - _1 :1分钟以下(1 minute and below)     - _2 :1-5分钟 (1-5 minutes)     - _3 :5分钟以上(5 minutes more) - page: 页码     - 默认从1开始，然后依次递增加1 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 视频搜索结果V2  # [English] ### Purpose: - Get video search results of specified keywords V2, this interface has better stability and higher cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is recommended to use this interface. - The charging standard is: $0.01 per request. - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212780e0 ### Parameters: - keyword: Keyword - sort_type:     - Sort type, available values are as follows:     - _0 : General     - _1 : More likes     - _2 : New - publish_time:     - Publish time, available values are as follows:     - _0 : No Limit     - _1 : last 1 day     - _7 : last 1 week     - _180 : last half year - filter_duration:     - Duration filter, available values are as follows:     - _0 : No Limit     - _1 : 1 minute and below     - _2 : 1-5 minutes     - _3 : 5 minutes more - page: Page     - Start from 1 by default, then increase by 1 each time - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - Video search results V2  # [示例/Example] keyword = \"中华娘\" sort_type = \"_0\" publish_time = \"_0\" filter_duration = \"_0\" page = 1 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object filter_duration: 视频时长/Duration filter
        :param object page: 页码/Page
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'sort_type', 'publish_time', 'filter_duration', 'page', 'search_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'publish_time' in params:
            query_params.append(('publish_time', params['publish_time']))  # noqa: E501
        if 'filter_duration' in params:
            query_params.append(('filter_duration', params['filter_duration']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_video_search_result_v2', 'GET',
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

    def fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get(self, aweme_ids, **kwargs):  # noqa: E501
        """根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)  # noqa: E501

        # [中文] ### 用途: - 根据视频ID获取作品的统计数据 - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。 - 可以获取到的统计有：     - 点赞数（digg_count）     - 下载数（download_count）     - 播放数（play_count）     - 分享数（share_count） ### 参数: - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过2个，单个也可以，则无需逗号。 ### 返回: - 作品统计数据  # [English] ### Purpose: - Get the statistical data of the Post according to the video ID - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be obtained through this interface. - List of statistics that can be obtained:     - Like count (digg_count)     - Download count (download_count)     - Play count (play_count)     - Share count (share_count) ### Parameters: - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 2, single is also possible, no need for commas. ### Return: - Post statistics data  # [示例/Example] aweme_ids = \"7448118827402972455,7126745726494821640\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get(aweme_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_ids: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get_with_http_info(aweme_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get_with_http_info(aweme_ids, **kwargs)  # noqa: E501
            return data

    def fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get_with_http_info(self, aweme_ids, **kwargs):  # noqa: E501
        """根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)  # noqa: E501

        # [中文] ### 用途: - 根据视频ID获取作品的统计数据 - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。 - 可以获取到的统计有：     - 点赞数（digg_count）     - 下载数（download_count）     - 播放数（play_count）     - 分享数（share_count） ### 参数: - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过2个，单个也可以，则无需逗号。 ### 返回: - 作品统计数据  # [English] ### Purpose: - Get the statistical data of the Post according to the video ID - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be obtained through this interface. - List of statistics that can be obtained:     - Like count (digg_count)     - Download count (download_count)     - Play count (play_count)     - Share count (share_count) ### Parameters: - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 2, single is also possible, no need for commas. ### Return: - Post statistics data  # [示例/Example] aweme_ids = \"7448118827402972455,7126745726494821640\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get_with_http_info(aweme_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_ids: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_ids' is set
        if self.api_client.client_side_validation and ('aweme_ids' not in params or
                                                       params['aweme_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_ids` when calling `fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_ids' in params:
            query_params.append(('aweme_ids', params['aweme_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/fetch_video_statistics', 'GET',
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

    def generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get(self, url, **kwargs):  # noqa: E501
        """生成抖音短链接/Generate Douyin short link  # noqa: E501

        # [中文] ### 用途: - 生成抖音短链接 ### 参数: - url: 抖音链接 ### 返回: - 短链接数据  # [English] ### Purpose: - Generate Douyin short link ### Parameters: - url: Douyin link ### Return: - Short link data  # [示例/Example] url = \"https://www.douyin.com/passport/web/logout/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 抖音链接/Douyin link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """生成抖音短链接/Generate Douyin short link  # noqa: E501

        # [中文] ### 用途: - 生成抖音短链接 ### 参数: - url: 抖音链接 ### 返回: - 短链接数据  # [English] ### Purpose: - Generate Douyin short link ### Parameters: - url: Douyin link ### Return: - Short link data  # [示例/Example] url = \"https://www.douyin.com/passport/web/logout/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 抖音链接/Douyin link (required)
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
                    " to method generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get`")  # noqa: E501

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
            '/api/v1/douyin/app/v3/generate_douyin_short_url', 'GET',
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

    def generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get(self, object_id, **kwargs):  # noqa: E501
        """生成抖音视频分享二维码/Generate Douyin video share QR code  # noqa: E501

        # [中文] ### 用途: - 生成抖音视频分享二维码 ### 参数: - object_id: 作品id或作者uid ### 返回: - 二维码数据  # [English] ### Purpose: - Generate Douyin video share QR code ### Parameters: - object_id: Video id or author uid ### Return: - QR code data  # [示例/Example] object_id = \"7348044435755846962\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get(object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object object_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get_with_http_info(object_id, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get_with_http_info(object_id, **kwargs)  # noqa: E501
            return data

    def generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get_with_http_info(self, object_id, **kwargs):  # noqa: E501
        """生成抖音视频分享二维码/Generate Douyin video share QR code  # noqa: E501

        # [中文] ### 用途: - 生成抖音视频分享二维码 ### 参数: - object_id: 作品id或作者uid ### 返回: - 二维码数据  # [English] ### Purpose: - Generate Douyin video share QR code ### Parameters: - object_id: Video id or author uid ### Return: - QR code data  # [示例/Example] object_id = \"7348044435755846962\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get_with_http_info(object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object object_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['object_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'object_id' is set
        if self.api_client.client_side_validation and ('object_id' not in params or
                                                       params['object_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `object_id` when calling `generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in params:
            query_params.append(('object_id', params['object_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/generate_douyin_video_share_qrcode', 'GET',
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

    def handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get(self, sec_user_id, **kwargs):  # noqa: E501
        """获取指定用户的信息/Get information of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id ### Return: - User information  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
            return data

    def handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get_with_http_info(self, sec_user_id, **kwargs):  # noqa: E501
        """获取指定用户的信息/Get information of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id ### Return: - User information  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get_with_http_info(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_user_id' is set
        if self.api_client.client_side_validation and ('sec_user_id' not in params or
                                                       params['sec_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_id` when calling `handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/handler_user_profile', 'GET',
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

    def open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get(self, keyword, **kwargs):  # noqa: E501
        """生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result  # noqa: E501

        # [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果。  ### 参数: - keyword: 关键词  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result  ### Parameters: - keyword: Keyword  ### Return: - Share link  # [示例/Example] keyword = \"雷军\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result  # noqa: E501

        # [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果。  ### 参数: - keyword: 关键词  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result  ### Parameters: - keyword: Keyword  ### Return: - Share link  # [示例/Example] keyword = \"雷军\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/open_douyin_app_to_keyword_search', 'GET',
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

    def open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get(self, uid, sec_uid, **kwargs):  # noqa: E501
        """生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users  # noqa: E501

        # [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，给指定用户发送私信。  ### 参数: - uid: 用户id - sec_uid: 用户sec_uid - 注意: 请确保user_id和sec_uid都有值，否则无法发送私信给指定用户。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and send private messages to specified users  ### Parameters: - uid: User id - sec_uid: User sec_uid - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot send private messages to the specified user.  ### Return: - Share link  # [示例/Example] uid = \"96874812426\" sec_uid = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get(uid, sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :param object sec_uid: 用户sec_uid/User sec_uid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get_with_http_info(uid, sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get_with_http_info(uid, sec_uid, **kwargs)  # noqa: E501
            return data

    def open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get_with_http_info(self, uid, sec_uid, **kwargs):  # noqa: E501
        """生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users  # noqa: E501

        # [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，给指定用户发送私信。  ### 参数: - uid: 用户id - sec_uid: 用户sec_uid - 注意: 请确保user_id和sec_uid都有值，否则无法发送私信给指定用户。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and send private messages to specified users  ### Parameters: - uid: User id - sec_uid: User sec_uid - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot send private messages to the specified user.  ### Return: - Share link  # [示例/Example] uid = \"96874812426\" sec_uid = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get_with_http_info(uid, sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :param object sec_uid: 用户sec_uid/User sec_uid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'sec_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get`")  # noqa: E501
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/open_douyin_app_to_send_private_message', 'GET',
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

    def open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get(self, uid, sec_uid, **kwargs):  # noqa: E501
        """生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile  # noqa: E501

        # [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，跳转指定用户主页。  ### 参数: - uid: 用户id - sec_uid: 用户sec_uid - 注意: 请确保user_id和sec_uid都有值，否则无法跳转到指定用户主页。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and jump to the specified user profile  ### Parameters: - uid: User id - sec_uid: User sec_uid - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot jump to the specified user profile.  ### Return: - Share link  # [示例/Example] uid = \"96874812426\" sec_uid = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get(uid, sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :param object sec_uid: 用户sec_uid/User sec_uid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get_with_http_info(uid, sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get_with_http_info(uid, sec_uid, **kwargs)  # noqa: E501
            return data

    def open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get_with_http_info(self, uid, sec_uid, **kwargs):  # noqa: E501
        """生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile  # noqa: E501

        # [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，跳转指定用户主页。  ### 参数: - uid: 用户id - sec_uid: 用户sec_uid - 注意: 请确保user_id和sec_uid都有值，否则无法跳转到指定用户主页。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and jump to the specified user profile  ### Parameters: - uid: User id - sec_uid: User sec_uid - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot jump to the specified user profile.  ### Return: - Share link  # [示例/Example] uid = \"96874812426\" sec_uid = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get_with_http_info(uid, sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :param object sec_uid: 用户sec_uid/User sec_uid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'sec_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get`")  # noqa: E501
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/open_douyin_app_to_user_profile', 'GET',
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

    def open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get(self, aweme_id, **kwargs):  # noqa: E501
        """生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page  # noqa: E501

        # [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页。  ### 参数: - aweme_id: 作品id  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and jump to the specified video  ### Parameters: - aweme_id: Video id  ### Return: - Share link  # [示例/Example] aweme_id = \"7197598285882789120\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page  # noqa: E501

        # [中文] ### 用途: - 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页。  ### 参数: - aweme_id: 作品id  ### 返回: - 分享链接  # [English] ### Purpose: - Generate Douyin share link, call Douyin APP, and jump to the specified video  ### Parameters: - aweme_id: Video id  ### Return: - Share link  # [示例/Example] aweme_id = \"7197598285882789120\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/open_douyin_app_to_video_detail', 'GET',
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

    def register_device_api_v1_douyin_app_v3_register_device_get(self, **kwargs):  # noqa: E501
        """抖音APP注册设备/Douyin APP register device  # noqa: E501

        # [中文] ### 用途: - 抖音APP注册设备，获取设备信息以及设备的Cookie信息。  ### 参数: - proxy: 代理，要带http://或https://，仅支持http代理。   - 格式: username:password@ip:port  ### 返回: - 设备信息以及设备的Cookie信息。  # [English] ### Purpose: - Register device in Douyin APP, retrieve device information and device cookies.  ### Parameters: - proxy: Proxy, with http:// or https://, only supports http proxies.   - Format: username:password@ip:port  ### Return: - Device information and device cookies.  # [示例/Example] proxy = \"http://username:password@ip:port\"  # [响应/Response] ```json {     \"code\": 200,     \"router\": \"/api/v1/douyin/app/v3/register_device\",     \"params\": {         \"proxy\": \"username:password@ip:port\"     },     \"data\": {         \"iid\": \"3631064037200330\",         \"device_id\": \"3631064037196234\",         \"mssdk_token\": \"\",         \"device_platform\": \"android\",         \"channel\": \"xiaomi_64_1775\",         \"version_code\": 240900,         \"version_name\": \"24.9.0\",         \"manifest_version_code\": 240901,         \"update_version_code\": 24909900,         \"device_type\": \"V1963A\",         \"device_brand\": \"vivo\",         \"device_model\": \"V1963A\",         \"openudid\": \"5d736335afc17aab\",         \"os_api\": 29,         \"os_version\": \"10\",         \"resolution\": \"2400x1080\",         \"dpi\": 480,         \"host_abi\": \"arm64-v8a\",         \"ua\": \"com.ss.android.ugc.aweme/240901 (Linux; U; Android 10; zh_CN; V1963A; Build/compiler10301842;tt-ok/3.12.13.4-tiktok)\",         \"cookies\": {             \"install_id\": \"3631064037200330\",             \"odin_tt\": \"5ef413aaa319b3a4077814a1da3d3e1bcec3e8640ddc3ad30945a8518f59d1563d24c3b7a3c59d97fbd5344f13208a25cf143312acf4462b028e56cd0b611cc3fc2a64318f7375470d6db86440f92841\",             \"d_ticket\": \"42186c5b0c54ea1a2a9e02d4e62bf6ab\",             \"store-region\": \"cn-js\",             \"store-region-src\": \"did\",             \"multi_sids\": \"462868309327184:38167255076198698951907954929873\",             \"passport_csrf_token\": \"6f75287240634ad1f51f3b3bdcdb5424\",             \"passport_csrf_token_default\": \"6f75287240634ad1f51f3b3bdcdb5424\",             \"ttreq\": \"1$7f616210b41fc044b1f164542ac4e064288b5163\"         },         \"lanusk\": \"\",         \"device_manufacturer\": \"vivo\",         \"uuid\": \"357125675341697\",         \"cdid\": \"f64372bf-4d1d-4883-bc8a-d3d6fa87a9e3\",         \"first_launch_timestamp\": 1726970498636,         \"x_tt_dt\": \"AAA2FGV24A2GAOHJJ3D3XCJ32IZDZ26XXKMQAOTDNUDWTB644ISU5YA3GBYVX2Y3XVOQ3ISDH3UA4JXGGNFXBLJ6AAZU7QTIBKHFYJLDJMDG5K36LVPBRCKLHW2XM\",         \"BootTime\": 1726980411,         \"MbTime\": 1726780411,         \"server_time\": 1726980500,         \"mc\": \"2A:66:7A:2D:8B:29\",         \"rom\": \"compiler10301842\",         \"rom_version\": \"PD1963-user 10 QP1A.190711.020 compiler10301842 release-keys\"     } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_device_api_v1_douyin_app_v3_register_device_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object proxy: 代理/Proxy
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.register_device_api_v1_douyin_app_v3_register_device_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.register_device_api_v1_douyin_app_v3_register_device_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def register_device_api_v1_douyin_app_v3_register_device_get_with_http_info(self, **kwargs):  # noqa: E501
        """抖音APP注册设备/Douyin APP register device  # noqa: E501

        # [中文] ### 用途: - 抖音APP注册设备，获取设备信息以及设备的Cookie信息。  ### 参数: - proxy: 代理，要带http://或https://，仅支持http代理。   - 格式: username:password@ip:port  ### 返回: - 设备信息以及设备的Cookie信息。  # [English] ### Purpose: - Register device in Douyin APP, retrieve device information and device cookies.  ### Parameters: - proxy: Proxy, with http:// or https://, only supports http proxies.   - Format: username:password@ip:port  ### Return: - Device information and device cookies.  # [示例/Example] proxy = \"http://username:password@ip:port\"  # [响应/Response] ```json {     \"code\": 200,     \"router\": \"/api/v1/douyin/app/v3/register_device\",     \"params\": {         \"proxy\": \"username:password@ip:port\"     },     \"data\": {         \"iid\": \"3631064037200330\",         \"device_id\": \"3631064037196234\",         \"mssdk_token\": \"\",         \"device_platform\": \"android\",         \"channel\": \"xiaomi_64_1775\",         \"version_code\": 240900,         \"version_name\": \"24.9.0\",         \"manifest_version_code\": 240901,         \"update_version_code\": 24909900,         \"device_type\": \"V1963A\",         \"device_brand\": \"vivo\",         \"device_model\": \"V1963A\",         \"openudid\": \"5d736335afc17aab\",         \"os_api\": 29,         \"os_version\": \"10\",         \"resolution\": \"2400x1080\",         \"dpi\": 480,         \"host_abi\": \"arm64-v8a\",         \"ua\": \"com.ss.android.ugc.aweme/240901 (Linux; U; Android 10; zh_CN; V1963A; Build/compiler10301842;tt-ok/3.12.13.4-tiktok)\",         \"cookies\": {             \"install_id\": \"3631064037200330\",             \"odin_tt\": \"5ef413aaa319b3a4077814a1da3d3e1bcec3e8640ddc3ad30945a8518f59d1563d24c3b7a3c59d97fbd5344f13208a25cf143312acf4462b028e56cd0b611cc3fc2a64318f7375470d6db86440f92841\",             \"d_ticket\": \"42186c5b0c54ea1a2a9e02d4e62bf6ab\",             \"store-region\": \"cn-js\",             \"store-region-src\": \"did\",             \"multi_sids\": \"462868309327184:38167255076198698951907954929873\",             \"passport_csrf_token\": \"6f75287240634ad1f51f3b3bdcdb5424\",             \"passport_csrf_token_default\": \"6f75287240634ad1f51f3b3bdcdb5424\",             \"ttreq\": \"1$7f616210b41fc044b1f164542ac4e064288b5163\"         },         \"lanusk\": \"\",         \"device_manufacturer\": \"vivo\",         \"uuid\": \"357125675341697\",         \"cdid\": \"f64372bf-4d1d-4883-bc8a-d3d6fa87a9e3\",         \"first_launch_timestamp\": 1726970498636,         \"x_tt_dt\": \"AAA2FGV24A2GAOHJJ3D3XCJ32IZDZ26XXKMQAOTDNUDWTB644ISU5YA3GBYVX2Y3XVOQ3ISDH3UA4JXGGNFXBLJ6AAZU7QTIBKHFYJLDJMDG5K36LVPBRCKLHW2XM\",         \"BootTime\": 1726980411,         \"MbTime\": 1726780411,         \"server_time\": 1726980500,         \"mc\": \"2A:66:7A:2D:8B:29\",         \"rom\": \"compiler10301842\",         \"rom_version\": \"PD1963-user 10 QP1A.190711.020 compiler10301842 release-keys\"     } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_device_api_v1_douyin_app_v3_register_device_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object proxy: 代理/Proxy
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['proxy']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_device_api_v1_douyin_app_v3_register_device_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'proxy' in params:
            query_params.append(('proxy', params['proxy']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/app/v3/register_device', 'GET',
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
