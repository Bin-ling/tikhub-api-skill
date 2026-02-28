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


class DouyinBillboardAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get(self, **kwargs):  # noqa: E501
        """获取中国城市列表/Fetch Chinese city list  # noqa: E501

        # [中文] ### 用途: - 获取城市列表 ### 参数: - 无 ### 返回: - 中国城市列表  # [English] ### Purpose: - Get city list ### Parameters: - None ### Return: - Chinese city list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取中国城市列表/Fetch Chinese city list  # noqa: E501

        # [中文] ### 用途: - 获取城市列表 ### 参数: - 无 ### 返回: - 中国城市列表  # [English] ### Purpose: - Get city list ### Parameters: - None ### Return: - Chinese city list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get_with_http_info(async_req=True)
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
                    " to method fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get" % key
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
            '/api/v1/douyin/billboard/fetch_city_list', 'GET',
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

    def fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get(self, **kwargs):  # noqa: E501
        """获取垂类内容标签/Fetch vertical content tags  # noqa: E501

        # [中文] ### 用途: - 获取垂类内容标签 ### 参数: - 无 ### 返回: - 垂类内容标签 ### 注意: - 该接口用于获取垂类内容标签，用于query_tag参数构建 ### 示例: 已知顶级垂类内容标签 `美食`，它的顶级垂类id为 `628`；`美食` 的子垂类标签 `品酒教学`，它的子垂类id为 `62802`。 那么构建标签查询参数为 `{\"value\": 628, \"children\": [{\"value\": 62808}]}`  如果需要多个子垂类标签，所有的美食子垂类标签为 `{\"value\":628,\"children\":[{\"value\":62808},{\"value\":62804},{\"value\":62806},{\"value\":62803},{\"value\":62802},{\"value\":62801},{\"value\":62811},{\"value\":62807},{\"value\":62805},{\"value\":62810}]}`  # [English] ### Purpose: - Get vertical content tags ### Parameters: - None ### Return: - Vertical content tags ### Note: - This interface is used to obtain vertical content tags, used to construct the query_tag parameter ### Example: Given the top-level vertical content tag `Food`, its top-level vertical id is `628`; `Food`'s sub-vertical tag `Wine Tasting`, its sub-vertical id is `62802`. Then the constructed tag query parameter is `{\"value\": 628, \"children\": [{\"value\": 62808}]}`  If you need multiple sub-vertical tags, all food sub-vertical tags are `{\"value\":628,\"children\":[{\"value\":62808},{\"value\":62804},{\"value\":62806},{\"value\":62803},{\"value\":62802},{\"value\":62801},{\"value\":62811},{\"value\":62807},{\"value\":62805},{\"value\":62810}]}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取垂类内容标签/Fetch vertical content tags  # noqa: E501

        # [中文] ### 用途: - 获取垂类内容标签 ### 参数: - 无 ### 返回: - 垂类内容标签 ### 注意: - 该接口用于获取垂类内容标签，用于query_tag参数构建 ### 示例: 已知顶级垂类内容标签 `美食`，它的顶级垂类id为 `628`；`美食` 的子垂类标签 `品酒教学`，它的子垂类id为 `62802`。 那么构建标签查询参数为 `{\"value\": 628, \"children\": [{\"value\": 62808}]}`  如果需要多个子垂类标签，所有的美食子垂类标签为 `{\"value\":628,\"children\":[{\"value\":62808},{\"value\":62804},{\"value\":62806},{\"value\":62803},{\"value\":62802},{\"value\":62801},{\"value\":62811},{\"value\":62807},{\"value\":62805},{\"value\":62810}]}`  # [English] ### Purpose: - Get vertical content tags ### Parameters: - None ### Return: - Vertical content tags ### Note: - This interface is used to obtain vertical content tags, used to construct the query_tag parameter ### Example: Given the top-level vertical content tag `Food`, its top-level vertical id is `628`; `Food`'s sub-vertical tag `Wine Tasting`, its sub-vertical id is `62802`. Then the constructed tag query parameter is `{\"value\": 628, \"children\": [{\"value\": 62808}]}`  If you need multiple sub-vertical tags, all food sub-vertical tags are `{\"value\":628,\"children\":[{\"value\":62808},{\"value\":62804},{\"value\":62806},{\"value\":62803},{\"value\":62802},{\"value\":62801},{\"value\":62811},{\"value\":62807},{\"value\":62805},{\"value\":62810}]}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get_with_http_info(async_req=True)
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
                    " to method fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get" % key
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
            '/api/v1/douyin/billboard/fetch_content_tag', 'GET',
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

    def fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取粉丝兴趣作者 20个用户/Fetch fan interest author 20 users  # noqa: E501

        # [中文] ### 用途: - 获取粉丝兴趣作者 20个用户 ### 参数: - sec_uid: 用户sec_id ### 返回: - 粉丝兴趣作者 20个用户  # [English] ### Purpose: - Get the fan interest author 20 users ### Parameters: - sec_uid: User sec_id ### Return: - Fan interest author 20 users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取粉丝兴趣作者 20个用户/Fetch fan interest author 20 users  # noqa: E501

        # [中文] ### 用途: - 获取粉丝兴趣作者 20个用户 ### 参数: - sec_uid: 用户sec_id ### 返回: - 粉丝兴趣作者 20个用户  # [English] ### Purpose: - Get the fan interest author 20 users ### Parameters: - sec_uid: User sec_id ### Return: - Fan interest author 20 users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_account_fans_interest_account_list', 'GET',
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

    def fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取粉丝近3天搜索词 10个搜索词/Fetch fan interest search term in the last 3 days 10 search terms  # noqa: E501

        # [中文] ### 用途: - 获取粉丝近3天搜索词 10个搜索词 ### 参数: - sec_uid: 用户sec_id ### 返回: - 粉丝近3天搜索词 10个搜索词  # [English] ### Purpose: - Get the fan interest search term in the last 3 days 10 search terms ### Parameters: - sec_uid: User sec_id ### Return: - Fan interest search term in the last 3 days 10 search terms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取粉丝近3天搜索词 10个搜索词/Fetch fan interest search term in the last 3 days 10 search terms  # noqa: E501

        # [中文] ### 用途: - 获取粉丝近3天搜索词 10个搜索词 ### 参数: - sec_uid: 用户sec_id ### 返回: - 粉丝近3天搜索词 10个搜索词  # [English] ### Purpose: - Get the fan interest search term in the last 3 days 10 search terms ### Parameters: - sec_uid: User sec_id ### Return: - Fan interest search term in the last 3 days 10 search terms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_account_fans_interest_search_list', 'GET',
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

    def fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取粉丝近3天感兴趣的话题 10个话题/Fetch fan interest topic in the last 3 days 10 topics  # noqa: E501

        # [中文] ### 用途: - 获取粉丝近3天感兴趣的话题 10个话题 ### 参数: - sec_uid: 用户sec_id ### 返回: - 粉丝近3天感兴趣的话题 10个话题  # [English] ### Purpose: - Get the fan interest topic in the last 3 days 10 topics ### Parameters: - sec_uid: User sec_id ### Return: - Fan interest topic in the last 3 days 10 topics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取粉丝近3天感兴趣的话题 10个话题/Fetch fan interest topic in the last 3 days 10 topics  # noqa: E501

        # [中文] ### 用途: - 获取粉丝近3天感兴趣的话题 10个话题 ### 参数: - sec_uid: 用户sec_id ### 返回: - 粉丝近3天感兴趣的话题 10个话题  # [English] ### Purpose: - Get the fan interest topic in the last 3 days 10 topics ### Parameters: - sec_uid: User sec_id ### Return: - Fan interest topic in the last 3 days 10 topics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_account_fans_interest_topic_list', 'GET',
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

    def fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取粉丝画像/Fetch fan portrait  # noqa: E501

        # [中文] ### 用途: - 获取粉丝画像 ### 参数: - sec_uid: 用户sec_id - option: 选项，默认值为：1 手机价格分布     - `1` = 手机价格分布     - `2` = 性别分布     - `3` = 年龄分布     - `4` = 地域分布-省份     - `5` = 地域分布-城市     - `6` = 城市等级     - `7` = 手机品牌分布     - `8` = 兴趣标签分析 百分比 ### 返回: - 粉丝画像  # [English] ### Purpose: - Get the fan portrait ### Parameters: - sec_uid: User sec_id - option: Option     - 1 Mobile price     - 2 Gender distribution     - 3 Age distribution     - 4 Regional distribution - province     - 5 Regional distribution - city     - 6 City level     - 7 Mobile brand distribution     - 8 Interest tag analysis percentage ### Return: - Fan portrait  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :param object option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布 8 兴趣标签分析 百分比
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取粉丝画像/Fetch fan portrait  # noqa: E501

        # [中文] ### 用途: - 获取粉丝画像 ### 参数: - sec_uid: 用户sec_id - option: 选项，默认值为：1 手机价格分布     - `1` = 手机价格分布     - `2` = 性别分布     - `3` = 年龄分布     - `4` = 地域分布-省份     - `5` = 地域分布-城市     - `6` = 城市等级     - `7` = 手机品牌分布     - `8` = 兴趣标签分析 百分比 ### 返回: - 粉丝画像  # [English] ### Purpose: - Get the fan portrait ### Parameters: - sec_uid: User sec_id - option: Option     - 1 Mobile price     - 2 Gender distribution     - 3 Age distribution     - 4 Regional distribution - province     - 5 Regional distribution - city     - 6 City level     - 7 Mobile brand distribution     - 8 Interest tag analysis percentage ### Return: - Fan portrait  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :param object option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布 8 兴趣标签分析 百分比
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid', 'option']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501
        if 'option' in params:
            query_params.append(('option', params['option']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_account_fans_portrait_list', 'GET',
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

    def fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取账号作品分析-上周/Fetch account work analysis - last week  # noqa: E501

        # [中文] ### 用途: - 获取账号作品分析 ### 参数: - sec_uid: 用户sec_id - day: 天数，默认7天 ### 返回: - 账号作品分析  # [English] ### Purpose: - Get the account work analysis ### Parameters: - sec_uid: User sec_id - day: Number of days, default 7 days ### Return: - Account work analysis  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取账号作品分析-上周/Fetch account work analysis - last week  # noqa: E501

        # [中文] ### 用途: - 获取账号作品分析 ### 参数: - sec_uid: 用户sec_id - day: 天数，默认7天 ### 返回: - 账号作品分析  # [English] ### Purpose: - Get the account work analysis ### Parameters: - sec_uid: User sec_id - day: Number of days, default 7 days ### Return: - Account work analysis  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_account_item_analysis_list', 'GET',
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

    def fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post(self, **kwargs):  # noqa: E501
        """获取热门账号/Fetch hot account list  # noqa: E501

        # [中文] ### 用途: - 获取热门账号 ### 参数: - date_window: 时间窗口，格式 小时，默认24小时 - page_num: 页码，默认1 - page_size: 每页数量，默认20 - query_tag: 子级垂类标签，空则为全部，多个标签需传入 {\"value\": \"{顶级垂类标签id}\", \"children\": [     {\"value\": \"{子级垂类标签id}\"},     {\"value\": \"{子级垂类标签id}\"} ]} ### 返回: - 热门账号  # [English] ### Purpose: - Get the hot account ### Parameters: - date_window: Time window, format hour, default 24 hours - page_num: Page number, default 1 - page_size: Number of items per page, default 20 - query_tag: Sub-level vertical category tag, empty for all, multiple tags need to be passed in {\"value\": \"{top-level vertical category id}\", \"children\": [     {\"value\": \"{sub-level vertical category id}\"},     {\"value\": \"{sub-level vertical category id}\"} ]} ### Return: - Hot account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取热门账号/Fetch hot account list  # noqa: E501

        # [中文] ### 用途: - 获取热门账号 ### 参数: - date_window: 时间窗口，格式 小时，默认24小时 - page_num: 页码，默认1 - page_size: 每页数量，默认20 - query_tag: 子级垂类标签，空则为全部，多个标签需传入 {\"value\": \"{顶级垂类标签id}\", \"children\": [     {\"value\": \"{子级垂类标签id}\"},     {\"value\": \"{子级垂类标签id}\"} ]} ### 返回: - 热门账号  # [English] ### Purpose: - Get the hot account ### Parameters: - date_window: Time window, format hour, default 24 hours - page_num: Page number, default 1 - page_size: Number of items per page, default 20 - query_tag: Sub-level vertical category tag, empty for all, multiple tags need to be passed in {\"value\": \"{top-level vertical category id}\", \"children\": [     {\"value\": \"{sub-level vertical category id}\"},     {\"value\": \"{sub-level vertical category id}\"} ]} ### Return: - Hot account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_account_list', 'POST',
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

    def fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get(self, keyword, cursor, **kwargs):  # noqa: E501
        """搜索用户名或抖音号/Fetch account search list  # noqa: E501

        # [中文] ### 用途: - 获取搜索用户名或抖音号 ### 参数: - keyword: 搜索的用户名或抖音号 - cursor: 游标，默认空 ### 返回: - 搜索结果  # [English] ### Purpose: - Get the search username or Douyin number ### Parameters: - keyword: Search username or Douyin number - cursor: Cursor, default empty ### Return: - Search result  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get(keyword, cursor, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索的用户名或抖音号 (required)
        :param object cursor: 游标，默认空 (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get_with_http_info(keyword, cursor, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get_with_http_info(keyword, cursor, **kwargs)  # noqa: E501
            return data

    def fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get_with_http_info(self, keyword, cursor, **kwargs):  # noqa: E501
        """搜索用户名或抖音号/Fetch account search list  # noqa: E501

        # [中文] ### 用途: - 获取搜索用户名或抖音号 ### 参数: - keyword: 搜索的用户名或抖音号 - cursor: 游标，默认空 ### 返回: - 搜索结果  # [English] ### Purpose: - Get the search username or Douyin number ### Parameters: - keyword: Search username or Douyin number - cursor: Cursor, default empty ### Return: - Search result  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get_with_http_info(keyword, cursor, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索的用户名或抖音号 (required)
        :param object cursor: 游标，默认空 (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get`")  # noqa: E501
        # verify the required parameter 'cursor' is set
        if self.api_client.client_side_validation and ('cursor' not in params or
                                                       params['cursor'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cursor` when calling `fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_account_search_list', 'GET',
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

    def fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取账号粉丝数据趋势/Fetch account fan data trend  # noqa: E501

        # [中文] ### 用途: - 获取账号粉丝数据趋势 ### 参数: - sec_uid: 用户sec_id - option: 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量 - date_window: 时间窗口，1 按小时 2 按天 ### 返回: - 账号粉丝数据趋势  # [English] ### Purpose: - Get the account fan data trend ### Parameters: - sec_uid: User sec_id - option: Option, 2 New like 3 New work 4 New comment 5 New share - date_window: Time window, 1 by hour 2 by day ### Return: - Account fan data trend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :param object option: 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
        :param object date_window: 时间窗口，1 按小时 2 按天
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取账号粉丝数据趋势/Fetch account fan data trend  # noqa: E501

        # [中文] ### 用途: - 获取账号粉丝数据趋势 ### 参数: - sec_uid: 用户sec_id - option: 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量 - date_window: 时间窗口，1 按小时 2 按天 ### 返回: - 账号粉丝数据趋势  # [English] ### Purpose: - Get the account fan data trend ### Parameters: - sec_uid: User sec_id - option: Option, 2 New like 3 New work 4 New comment 5 New share - date_window: Time window, 1 by hour 2 by day ### Return: - Account fan data trend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_id (required)
        :param object option: 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
        :param object date_window: 时间窗口，1 按小时 2 按天
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid', 'option', 'date_window']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501
        if 'option' in params:
            query_params.append(('option', params['option']))  # noqa: E501
        if 'date_window' in params:
            query_params.append(('date_window', params['date_window']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_account_trends_list', 'GET',
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

    def fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get(self, calendar_id, **kwargs):  # noqa: E501
        """获取活动日历详情/Fetch activity calendar detail  # noqa: E501

        # [中文] ### 用途: - 获取活动日历详情 ### 参数: - calendar_id: 活动id ### 返回: - 活动日历详情  # [English] ### Purpose: - Get the activity calendar details ### Parameters: - calendar_id: Activity id ### Return: - Activity calendar details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get(calendar_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object calendar_id: 活动id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get_with_http_info(calendar_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get_with_http_info(calendar_id, **kwargs)  # noqa: E501
            return data

    def fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get_with_http_info(self, calendar_id, **kwargs):  # noqa: E501
        """获取活动日历详情/Fetch activity calendar detail  # noqa: E501

        # [中文] ### 用途: - 获取活动日历详情 ### 参数: - calendar_id: 活动id ### 返回: - 活动日历详情  # [English] ### Purpose: - Get the activity calendar details ### Parameters: - calendar_id: Activity id ### Return: - Activity calendar details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get_with_http_info(calendar_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object calendar_id: 活动id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['calendar_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'calendar_id' is set
        if self.api_client.client_side_validation and ('calendar_id' not in params or
                                                       params['calendar_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `calendar_id` when calling `fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'calendar_id' in params:
            query_params.append(('calendar_id', params['calendar_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_calendar_detail', 'GET',
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

    def fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post(self, **kwargs):  # noqa: E501
        """获取活动日历/Fetch activity calendar  # noqa: E501

        # [中文] ### 用途: - 获取活动日历 ### 参数: - city_code: 城市编码，从城市列表获取，空为全部 - category_code: 热点榜分类编码，从热点榜分类获取，空为全部 - end_date: 快照结束时间 格式10位时间戳 - start_date: 快照开始时间 格式10位时间戳 ### 返回: - 活动日历  # [English] ### Purpose: - Get the activity calendar ### Parameters: - city_code: City code, get from city list, empty for all - category_code: Hot list category code, get from hot list category, empty for all - end_date: Snapshot end time format 10 digit timestamp - start_date: Snapshot start time format 10 digit timestamp ### Return: - Activity calendar  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取活动日历/Fetch activity calendar  # noqa: E501

        # [中文] ### 用途: - 获取活动日历 ### 参数: - city_code: 城市编码，从城市列表获取，空为全部 - category_code: 热点榜分类编码，从热点榜分类获取，空为全部 - end_date: 快照结束时间 格式10位时间戳 - start_date: 快照开始时间 格式10位时间戳 ### 返回: - 活动日历  # [English] ### Purpose: - Get the activity calendar ### Parameters: - city_code: City code, get from city list, empty for all - category_code: Hot list category code, get from hot list category, empty for all - end_date: Snapshot end time format 10 digit timestamp - start_date: Snapshot start time format 10 digit timestamp ### Return: - Activity calendar  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_calendar_list', 'POST',
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

    def fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get(self, billboard_type, **kwargs):  # noqa: E501
        """获取热点榜分类/Fetch hot list category  # noqa: E501

        # [中文] ### 用途: - 获取热点榜分类的id与热度 - 注意：使用start_date和end_date参数需要移除snapshot_time参数才可以生效 ### 参数: - billboard_type: 榜单类型     - rise 上升热点榜     - city 城市热点榜     - total 热点总榜 - snapshot_time: 快照时间 - start_date: 快照开始时间 - end_date: 快照结束时间 - keyword: 热点搜索词 ### 返回: - 热点榜分类  # [English] ### Purpose: - Get the id and popularity of the hot list category - Note: Using start_date and end_date parameters requires removing the snapshot_time parameter - Note: snapshot_time and start_date, end_date parameters cannot be empty at the same time ### Parameters: - billboard_type: Billboard type     - rise Rising hot list     - city City hot list     - total Total hot list - snapshot_time: Snapshot time - start_date: Snapshot start time - end_date: Snapshot end time - keyword: Hot search term ### Return: - Hot category list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get(billboard_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_type: 榜单类型 (required)
        :param object snapshot_time: 快照时间 格式yyyyMMddHHmmss
        :param object start_date: 快照开始时间 格式yyyyMMdd
        :param object end_date: 快照结束时间 格式yyyyMMdd
        :param object keyword: 热点搜索词
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get_with_http_info(billboard_type, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get_with_http_info(billboard_type, **kwargs)  # noqa: E501
            return data

    def fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get_with_http_info(self, billboard_type, **kwargs):  # noqa: E501
        """获取热点榜分类/Fetch hot list category  # noqa: E501

        # [中文] ### 用途: - 获取热点榜分类的id与热度 - 注意：使用start_date和end_date参数需要移除snapshot_time参数才可以生效 ### 参数: - billboard_type: 榜单类型     - rise 上升热点榜     - city 城市热点榜     - total 热点总榜 - snapshot_time: 快照时间 - start_date: 快照开始时间 - end_date: 快照结束时间 - keyword: 热点搜索词 ### 返回: - 热点榜分类  # [English] ### Purpose: - Get the id and popularity of the hot list category - Note: Using start_date and end_date parameters requires removing the snapshot_time parameter - Note: snapshot_time and start_date, end_date parameters cannot be empty at the same time ### Parameters: - billboard_type: Billboard type     - rise Rising hot list     - city City hot list     - total Total hot list - snapshot_time: Snapshot time - start_date: Snapshot start time - end_date: Snapshot end time - keyword: Hot search term ### Return: - Hot category list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get_with_http_info(billboard_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_type: 榜单类型 (required)
        :param object snapshot_time: 快照时间 格式yyyyMMddHHmmss
        :param object start_date: 快照开始时间 格式yyyyMMdd
        :param object end_date: 快照结束时间 格式yyyyMMdd
        :param object keyword: 热点搜索词
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billboard_type', 'snapshot_time', 'start_date', 'end_date', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'billboard_type' is set
        if self.api_client.client_side_validation and ('billboard_type' not in params or
                                                       params['billboard_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `billboard_type` when calling `fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'billboard_type' in params:
            query_params.append(('billboard_type', params['billboard_type']))  # noqa: E501
        if 'snapshot_time' in params:
            query_params.append(('snapshot_time', params['snapshot_time']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_category_list', 'GET',
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

    def fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get(self, page, page_size, **kwargs):  # noqa: E501
        """获取挑战热榜/Fetch hot challenge list  # noqa: E501

        # [中文] ### 用途: - 获取挑战榜 ### 参数: - page: 页码 - page_size: 每页数量 - keyword: 热点搜索词 ### 返回: - 挑战榜  # [English] ### Purpose: - Get the challenge list ### Parameters: - page: Page number - page_size: Number of items per page - keyword: Hot search term ### Return: - Challenge list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get(page, page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码 (required)
        :param object page_size: 每页数量 (required)
        :param object keyword: 热点搜索词
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get_with_http_info(page, page_size, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get_with_http_info(page, page_size, **kwargs)  # noqa: E501
            return data

    def fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get_with_http_info(self, page, page_size, **kwargs):  # noqa: E501
        """获取挑战热榜/Fetch hot challenge list  # noqa: E501

        # [中文] ### 用途: - 获取挑战榜 ### 参数: - page: 页码 - page_size: 每页数量 - keyword: 热点搜索词 ### 返回: - 挑战榜  # [English] ### Purpose: - Get the challenge list ### Parameters: - page: Page number - page_size: Number of items per page - keyword: Hot search term ### Return: - Challenge list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get_with_http_info(page, page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码 (required)
        :param object page_size: 每页数量 (required)
        :param object keyword: 热点搜索词
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page' is set
        if self.api_client.client_side_validation and ('page' not in params or
                                                       params['page'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page` when calling `fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if self.api_client.client_side_validation and ('page_size' not in params or
                                                       params['page_size'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page_size` when calling `fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_challenge_list', 'GET',
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

    def fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get(self, page, page_size, order, **kwargs):  # noqa: E501
        """获取同城热点榜/Fetch city hot list  # noqa: E501

        # [中文] ### 用途: - 获取同城热点榜 ### 参数: - page: 页码 - page_size: 每页数量 - order: 排序方式     - rank 按热度排序     - rank_diff 按排名变化 - city_code: 城市编码，从城市列表获取，空为全部 - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 - keyword: 热点搜索词 ### 返回: - 同城热点榜  # [English] ### Purpose: - Get the city hot list ### Parameters: - page: Page number - page_size: Number of items per page - order: Sorting method     - rank Sort by popularity     - rank_diff Sort by ranking change - city_code: City code, get from city list, empty for all - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by commas, empty for all - keyword: Hot search term ### Return: - City hot list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get(page, page_size, order, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码 (required)
        :param object page_size: 每页数量 (required)
        :param object order: 排序方式 (required)
        :param object city_code: 城市编码，从城市列表获取，空为全部
        :param object sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
        :param object keyword: 热点搜索词
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get_with_http_info(page, page_size, order, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get_with_http_info(page, page_size, order, **kwargs)  # noqa: E501
            return data

    def fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get_with_http_info(self, page, page_size, order, **kwargs):  # noqa: E501
        """获取同城热点榜/Fetch city hot list  # noqa: E501

        # [中文] ### 用途: - 获取同城热点榜 ### 参数: - page: 页码 - page_size: 每页数量 - order: 排序方式     - rank 按热度排序     - rank_diff 按排名变化 - city_code: 城市编码，从城市列表获取，空为全部 - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 - keyword: 热点搜索词 ### 返回: - 同城热点榜  # [English] ### Purpose: - Get the city hot list ### Parameters: - page: Page number - page_size: Number of items per page - order: Sorting method     - rank Sort by popularity     - rank_diff Sort by ranking change - city_code: City code, get from city list, empty for all - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by commas, empty for all - keyword: Hot search term ### Return: - City hot list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get_with_http_info(page, page_size, order, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码 (required)
        :param object page_size: 每页数量 (required)
        :param object order: 排序方式 (required)
        :param object city_code: 城市编码，从城市列表获取，空为全部
        :param object sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
        :param object keyword: 热点搜索词
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size', 'order', 'city_code', 'sentence_tag', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page' is set
        if self.api_client.client_side_validation and ('page' not in params or
                                                       params['page'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page` when calling `fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if self.api_client.client_side_validation and ('page_size' not in params or
                                                       params['page_size'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page_size` when calling `fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get`")  # noqa: E501
        # verify the required parameter 'order' is set
        if self.api_client.client_side_validation and ('order' not in params or
                                                       params['order'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `order` when calling `fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'city_code' in params:
            query_params.append(('city_code', params['city_code']))  # noqa: E501
        if 'sentence_tag' in params:
            query_params.append(('sentence_tag', params['sentence_tag']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_city_list', 'GET',
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

    def fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取作品评论分析-词云权重/Fetch work comment analysis word cloud weight  # noqa: E501

        # [中文] ### 用途: - 获取作品评论分析-词云权重 ### 参数: - aweme_id: 作品id ### 返回: - 作品评论分析-词云权重  # [English] ### Purpose: - Get the work comment analysis word cloud weight ### Parameters: - aweme_id: Work id ### Return: - Work comment analysis word cloud weight  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取作品评论分析-词云权重/Fetch work comment analysis word cloud weight  # noqa: E501

        # [中文] ### 用途: - 获取作品评论分析-词云权重 ### 参数: - aweme_id: 作品id ### 返回: - 作品评论分析-词云权重  # [English] ### Purpose: - Get the work comment analysis word cloud weight ### Parameters: - aweme_id: Work id ### Return: - Work comment analysis word cloud weight  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id (required)
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
                    " to method fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get`")  # noqa: E501

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
            '/api/v1/douyin/billboard/fetch_hot_comment_word_list', 'GET',
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

    def fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get(self, **kwargs):  # noqa: E501
        """获取作品数据趋势/Fetch post data trend  # noqa: E501

        # [中文] ### 用途: - 获取作品数据趋势 ### 参数: - aweme_id: 作品id - option: 选项，7 点赞量 8 分享量 9 评论量 - date_window: 时间窗口，1 按小时 2 按天 ### 返回: - 作品数据趋势  # [English] ### Purpose: - Get the work data trend ### Parameters: - aweme_id: Work id - option: Option, 7 Like 8 Share 9 Comment - date_window: Time window, 1 by hour 2 by day ### Return: - Work data trend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id
        :param object option: 选项，7 点赞量 8 分享量 9 评论量
        :param object date_window: 时间窗口，1 按小时 2 按天
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取作品数据趋势/Fetch post data trend  # noqa: E501

        # [中文] ### 用途: - 获取作品数据趋势 ### 参数: - aweme_id: 作品id - option: 选项，7 点赞量 8 分享量 9 评论量 - date_window: 时间窗口，1 按小时 2 按天 ### 返回: - 作品数据趋势  # [English] ### Purpose: - Get the work data trend ### Parameters: - aweme_id: Work id - option: Option, 7 Like 8 Share 9 Comment - date_window: Time window, 1 by hour 2 by day ### Return: - Work data trend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id
        :param object option: 选项，7 点赞量 8 分享量 9 评论量
        :param object date_window: 时间窗口，1 按小时 2 按天
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id', 'option', 'date_window']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501
        if 'option' in params:
            query_params.append(('option', params['option']))  # noqa: E501
        if 'date_window' in params:
            query_params.append(('date_window', params['date_window']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_item_trends_list', 'GET',
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

    def fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get(self, page, page_size, order, **kwargs):  # noqa: E501
        """获取上升热点榜/Fetch rising hot list  # noqa: E501

        # [中文] ### 用途: - 获取上升热点榜 ### 参数: - page: 页码 - page_size: 每页数量 - order: 排序方式     - rank 按热度排序     - rank_diff 按排名变化 - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 - keyword: 热点搜索词 ### 返回: - 上升热点榜  # [English] ### Purpose: - Get the rising hot list ### Parameters: - page: Page number - page_size: Number of items per page - order: Sorting method     - rank Sort by popularity     - rank_diff Sort by ranking change - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by commas, empty for all - keyword: Hot search term ### Return: - Rising hot list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get(page, page_size, order, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码 (required)
        :param object page_size: 每页数量 (required)
        :param object order: 排序方式 (required)
        :param object sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
        :param object keyword: 热点搜索词
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get_with_http_info(page, page_size, order, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get_with_http_info(page, page_size, order, **kwargs)  # noqa: E501
            return data

    def fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get_with_http_info(self, page, page_size, order, **kwargs):  # noqa: E501
        """获取上升热点榜/Fetch rising hot list  # noqa: E501

        # [中文] ### 用途: - 获取上升热点榜 ### 参数: - page: 页码 - page_size: 每页数量 - order: 排序方式     - rank 按热度排序     - rank_diff 按排名变化 - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 - keyword: 热点搜索词 ### 返回: - 上升热点榜  # [English] ### Purpose: - Get the rising hot list ### Parameters: - page: Page number - page_size: Number of items per page - order: Sorting method     - rank Sort by popularity     - rank_diff Sort by ranking change - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by commas, empty for all - keyword: Hot search term ### Return: - Rising hot list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get_with_http_info(page, page_size, order, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码 (required)
        :param object page_size: 每页数量 (required)
        :param object order: 排序方式 (required)
        :param object sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
        :param object keyword: 热点搜索词
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size', 'order', 'sentence_tag', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page' is set
        if self.api_client.client_side_validation and ('page' not in params or
                                                       params['page'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page` when calling `fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if self.api_client.client_side_validation and ('page_size' not in params or
                                                       params['page_size'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page_size` when calling `fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get`")  # noqa: E501
        # verify the required parameter 'order' is set
        if self.api_client.client_side_validation and ('order' not in params or
                                                       params['order'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `order` when calling `fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'sentence_tag' in params:
            query_params.append(('sentence_tag', params['sentence_tag']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_rise_list', 'GET',
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

    def fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post(self, **kwargs):  # noqa: E501
        """获取高涨粉率榜/Fetch high fan rate list  # noqa: E501

        # [中文] ### 用途: - 获取高涨粉率榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 高涨粉率榜  # [English] ### Purpose: - Get the high fan rate list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - High fan rate list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取高涨粉率榜/Fetch high fan rate list  # noqa: E501

        # [中文] ### 用途: - 获取高涨粉率榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 高涨粉率榜  # [English] ### Purpose: - Get the high fan rate list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - High fan rate list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_total_high_fan_list', 'POST',
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

    def fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post(self, **kwargs):  # noqa: E501
        """获取高点赞率榜/Fetch high like rate list  # noqa: E501

        # [中文] ### 用途: - 获取高点赞率榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 高点赞率榜  # [English] ### Purpose: - Get the high like rate list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - High like rate list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取高点赞率榜/Fetch high like rate list  # noqa: E501

        # [中文] ### 用途: - 获取高点赞率榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 高点赞率榜  # [English] ### Purpose: - Get the high like rate list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - High like rate list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_total_high_like_list', 'POST',
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

    def fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post(self, **kwargs):  # noqa: E501
        """获取高完播率榜/Fetch high completion rate list  # noqa: E501

        # [中文] ### 用途: - 获取高完播率榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 高完播率榜  # [English] ### Purpose: - Get the high completion rate list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - High completion rate list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取高完播率榜/Fetch high completion rate list  # noqa: E501

        # [中文] ### 用途: - 获取高完播率榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 高完播率榜  # [English] ### Purpose: - Get the high completion rate list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - High completion rate list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_total_high_play_list', 'POST',
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

    def fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post(self, **kwargs):  # noqa: E501
        """获取热度飙升的搜索榜/Fetch search list with rising popularity  # noqa: E501

        # [中文] ### 用途: - 获取热度飙升的搜索榜 ### 参数: - page_num: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - keyword: 搜索关键字 ### 返回: - 热度飙升的搜索榜  # [English] ### Purpose: - Get the search list with rising popularity ### Parameters: - page_num: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - keyword: Search keyword ### Return: - Search list with rising popularity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取热度飙升的搜索榜/Fetch search list with rising popularity  # noqa: E501

        # [中文] ### 用途: - 获取热度飙升的搜索榜 ### 参数: - page_num: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - keyword: 搜索关键字 ### 返回: - 热度飙升的搜索榜  # [English] ### Purpose: - Get the search list with rising popularity ### Parameters: - page_num: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - keyword: Search keyword ### Return: - Search list with rising popularity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_total_high_search_list', 'POST',
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

    def fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post(self, **kwargs):  # noqa: E501
        """获取热度飙升的话题榜/Fetch topic list with rising popularity  # noqa: E501

        # [中文] ### 用途: - 获取热度飙升的话题榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 热度飙升的话题榜  # [English] ### Purpose: - Get the topic list with rising popularity ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - Topic list with rising popularity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取热度飙升的话题榜/Fetch topic list with rising popularity  # noqa: E501

        # [中文] ### 用途: - 获取热度飙升的话题榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 热度飙升的话题榜  # [English] ### Purpose: - Get the topic list with rising popularity ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - Topic list with rising popularity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_total_high_topic_list', 'POST',
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

    def fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get(self, keyword, word_id, query_day, **kwargs):  # noqa: E501
        """获取内容词详情/Fetch content word details  # noqa: E501

        # [中文] ### 用途: - 获取内容词详情 ### 参数: - keyword: 搜索关键字 - word_id: 内容词id - query_day: 查询日期，格式为YYYYMMDD ### 返回: - 内容词详情  # [English] ### Purpose: - Get the details of content words ### Parameters: - keyword: Search keyword - word_id: Content word id - query_day: Query date, format is YYYYMMDD ### Return: - Details of content words  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get(keyword, word_id, query_day, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键字 (required)
        :param object word_id: 内容词id (required)
        :param object query_day: 查询日期，格式为YYYYMMDD，需为当日 (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get_with_http_info(keyword, word_id, query_day, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get_with_http_info(keyword, word_id, query_day, **kwargs)  # noqa: E501
            return data

    def fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get_with_http_info(self, keyword, word_id, query_day, **kwargs):  # noqa: E501
        """获取内容词详情/Fetch content word details  # noqa: E501

        # [中文] ### 用途: - 获取内容词详情 ### 参数: - keyword: 搜索关键字 - word_id: 内容词id - query_day: 查询日期，格式为YYYYMMDD ### 返回: - 内容词详情  # [English] ### Purpose: - Get the details of content words ### Parameters: - keyword: Search keyword - word_id: Content word id - query_day: Query date, format is YYYYMMDD ### Return: - Details of content words  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get_with_http_info(keyword, word_id, query_day, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键字 (required)
        :param object word_id: 内容词id (required)
        :param object query_day: 查询日期，格式为YYYYMMDD，需为当日 (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'word_id', 'query_day']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get`")  # noqa: E501
        # verify the required parameter 'word_id' is set
        if self.api_client.client_side_validation and ('word_id' not in params or
                                                       params['word_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `word_id` when calling `fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get`")  # noqa: E501
        # verify the required parameter 'query_day' is set
        if self.api_client.client_side_validation and ('query_day' not in params or
                                                       params['query_day'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query_day` when calling `fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'word_id' in params:
            query_params.append(('word_id', params['word_id']))  # noqa: E501
        if 'query_day' in params:
            query_params.append(('query_day', params['query_day']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_total_hot_word_detail_list', 'GET',
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

    def fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post(self, **kwargs):  # noqa: E501
        """获取全部热门内容词/Fetch all hot content words  # noqa: E501

        # [中文] ### 用途: - 获取全部内容词 ### 参数: - page_num: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - keyword: 搜索关键字 ### 返回: - 全部内容词  # [English] ### Purpose: - Get the list of all content words ### Parameters: - page_num: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - keyword: Search keyword ### Return: - List of all content words  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取全部热门内容词/Fetch all hot content words  # noqa: E501

        # [中文] ### 用途: - 获取全部内容词 ### 参数: - page_num: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - keyword: 搜索关键字 ### 返回: - 全部内容词  # [English] ### Purpose: - Get the list of all content words ### Parameters: - page_num: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - keyword: Search keyword ### Return: - List of all content words  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_total_hot_word_list', 'POST',
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

    def fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get(self, page, page_size, type, **kwargs):  # noqa: E501
        """获取热点总榜/Fetch total hot list  # noqa: E501

        # [中文] ### 用途: - 获取热点总榜 ### 参数: - page: 页码 - page_size: 每页数量 - type: 快照类型 snapshot 按时刻查看 range 按时间范围。     - 备注：snapshot_time 在 snapshot时有效，start_date 和 end_date 在 range 时有效 - snapshot_time: 快照时间 格式yyyyMMddHHmmss - start_date: 快照开始时间 格式yyyyMMdd - end_date: 快照结束时间 格式yyyyMMdd - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 - keyword: 热点搜索词 ### 返回: - 热点总榜  # [English] ### Purpose: - Get the total hot list ### Parameters: - page: Page number - page_size: Number of items per page - type: Snapshot type snapshot view by time range view by time range.     - Note: snapshot_time is valid when snapshot, start_date and end_date are valid when range - snapshot_time: Snapshot time format yyyyMMddHHmmss - start_date: Snapshot start time format yyyyMMdd - end_date: Snapshot end time format yyyyMMdd - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by commas, empty for all - keyword: Hot search term ### Return: - Total hot list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get(page, page_size, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码 (required)
        :param object page_size: 每页数量 (required)
        :param object type: 快照类型 snapshot 按时刻查看 range 按时间范围 (required)
        :param object snapshot_time: 快照时间 格式yyyyMMddHHmmss
        :param object start_date: 快照开始时间 格式yyyyMMdd
        :param object end_date: 快照结束时间 格式yyyyMMdd
        :param object sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
        :param object keyword: 热点搜索词
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get_with_http_info(page, page_size, type, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get_with_http_info(page, page_size, type, **kwargs)  # noqa: E501
            return data

    def fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get_with_http_info(self, page, page_size, type, **kwargs):  # noqa: E501
        """获取热点总榜/Fetch total hot list  # noqa: E501

        # [中文] ### 用途: - 获取热点总榜 ### 参数: - page: 页码 - page_size: 每页数量 - type: 快照类型 snapshot 按时刻查看 range 按时间范围。     - 备注：snapshot_time 在 snapshot时有效，start_date 和 end_date 在 range 时有效 - snapshot_time: 快照时间 格式yyyyMMddHHmmss - start_date: 快照开始时间 格式yyyyMMdd - end_date: 快照结束时间 格式yyyyMMdd - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 - keyword: 热点搜索词 ### 返回: - 热点总榜  # [English] ### Purpose: - Get the total hot list ### Parameters: - page: Page number - page_size: Number of items per page - type: Snapshot type snapshot view by time range view by time range.     - Note: snapshot_time is valid when snapshot, start_date and end_date are valid when range - snapshot_time: Snapshot time format yyyyMMddHHmmss - start_date: Snapshot start time format yyyyMMdd - end_date: Snapshot end time format yyyyMMdd - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by commas, empty for all - keyword: Hot search term ### Return: - Total hot list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get_with_http_info(page, page_size, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码 (required)
        :param object page_size: 每页数量 (required)
        :param object type: 快照类型 snapshot 按时刻查看 range 按时间范围 (required)
        :param object snapshot_time: 快照时间 格式yyyyMMddHHmmss
        :param object start_date: 快照开始时间 格式yyyyMMdd
        :param object end_date: 快照结束时间 格式yyyyMMdd
        :param object sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
        :param object keyword: 热点搜索词
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size', 'type', 'snapshot_time', 'start_date', 'end_date', 'sentence_tag', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page' is set
        if self.api_client.client_side_validation and ('page' not in params or
                                                       params['page'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page` when calling `fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if self.api_client.client_side_validation and ('page_size' not in params or
                                                       params['page_size'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page_size` when calling `fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get`")  # noqa: E501
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and ('type' not in params or
                                                       params['type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `type` when calling `fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'snapshot_time' in params:
            query_params.append(('snapshot_time', params['snapshot_time']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'sentence_tag' in params:
            query_params.append(('sentence_tag', params['sentence_tag']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_total_list', 'GET',
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

    def fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post(self, **kwargs):  # noqa: E501
        """获取低粉爆款榜/Fetch low fan explosion list  # noqa: E501

        # [中文] ### 用途: - 获取低粉爆款榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 低粉爆款榜  # [English] ### Purpose: - Get the low fan explosion list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - Low fan explosion list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取低粉爆款榜/Fetch low fan explosion list  # noqa: E501

        # [中文] ### 用途: - 获取低粉爆款榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 低粉爆款榜  # [English] ### Purpose: - Get the low fan explosion list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - Low fan explosion list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_total_low_fan_list', 'POST',
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

    def fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post(self, **kwargs):  # noqa: E501
        """获取搜索热榜/Fetch search hot list  # noqa: E501

        # [中文] ### 用途: - 获取搜索榜 ### 参数: - page_num: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - keyword: 搜索关键字 ### 返回: - 搜索榜  # [English] ### Purpose: - Get the search list ### Parameters: - page_num: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - keyword: Search keyword ### Return: - Search list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取搜索热榜/Fetch search hot list  # noqa: E501

        # [中文] ### 用途: - 获取搜索榜 ### 参数: - page_num: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - keyword: 搜索关键字 ### 返回: - 搜索榜  # [English] ### Purpose: - Get the search list ### Parameters: - page_num: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - keyword: Search keyword ### Return: - Search list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_total_search_list', 'POST',
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

    def fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post(self, **kwargs):  # noqa: E501
        """获取话题热榜/Fetch topic hot list  # noqa: E501

        # [中文] ### 用途: - 获取话题榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 话题榜  # [English] ### Purpose: - Get the topic list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - Topic list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取话题热榜/Fetch topic hot list  # noqa: E501

        # [中文] ### 用途: - 获取话题榜 ### 参数: - page: 页码 - page_size: 每页数量 - date_window: 时间窗口，1 按小时 2 按天 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 话题榜  # [English] ### Purpose: - Get the topic list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - Topic list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_total_topic_list', 'POST',
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

    def fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post(self, **kwargs):  # noqa: E501
        """获取视频热榜/Fetch video hot list  # noqa: E501

        # [中文] ### 用途: - 获取视频榜 ### 参数: - page: 页码，默认1 - page_size: 每页数量，默认10 - date_window: 时间窗口，1 按小时 2 按天 - sub_type: 榜单分类，1001 视频总榜 1002 低粉爆款 1003 高完播率 1004 高涨粉率 1005 高点赞率 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 视频榜  # [English] ### Purpose: - Get the video list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - sub_type: List category, 1001 Video total list 1002 Low fan explosion 1003 High completion rate 1004 High fan growth rate 1005 High like rate - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - Video list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取视频热榜/Fetch video hot list  # noqa: E501

        # [中文] ### 用途: - 获取视频榜 ### 参数: - page: 页码，默认1 - page_size: 每页数量，默认10 - date_window: 时间窗口，1 按小时 2 按天 - sub_type: 榜单分类，1001 视频总榜 1002 低粉爆款 1003 高完播率 1004 高涨粉率 1005 高点赞率 - tags: 子级垂类标签，空则为全部，多个标签需传入     {\"value\": \"{顶级垂类标签id}\", \"children\": [         {\"value\": \"{子级垂类标签id}\"},         {\"value\": \"{子级垂类标签id}\"}     ]} ### 返回: - 视频榜  # [English] ### Purpose: - Get the video list ### Parameters: - page: Page number - page_size: Number of items per page - date_window: Time window, 1 by hour 2 by day - sub_type: List category, 1001 Video total list 1002 Low fan explosion 1003 High completion rate 1004 High fan growth rate 1005 High like rate - tags: Sub-level vertical category tag, empty for all, multiple tags need to be passed in     {\"value\": \"{top-level vertical category id}\", \"children\": [         {\"value\": \"{sub-level vertical category id}\"},         {\"value\": \"{sub-level vertical category id}\"}     ]} ### Return: - Video list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post_with_http_info(async_req=True)
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
                    " to method fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post" % key
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
            '/api/v1/douyin/billboard/fetch_hot_total_video_list', 'POST',
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

    def fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only  # noqa: E501

        # [中文] ### 用途: - 获取作品点赞观众画像 ### 参数: - aweme_id: 作品id - option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布 ### 返回: - 作品点赞观众画像  # [English] ### Purpose: - Get the work like audience portrait ### Parameters: - aweme_id: Work id - option: Option     - 1 Mobile price     - 2 Gender distribution     - 3 Age distribution     - 4 Regional distribution - province     - 5 Regional distribution - city     - 6 City level     - 7 Mobile brand distribution ### Return: - Work like audience portrait  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id (required)
        :param object option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only  # noqa: E501

        # [中文] ### 用途: - 获取作品点赞观众画像 ### 参数: - aweme_id: 作品id - option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布 ### 返回: - 作品点赞观众画像  # [English] ### Purpose: - Get the work like audience portrait ### Parameters: - aweme_id: Work id - option: Option     - 1 Mobile price     - 2 Gender distribution     - 3 Age distribution     - 4 Regional distribution - province     - 5 Regional distribution - city     - 6 City level     - 7 Mobile brand distribution ### Return: - Work like audience portrait  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id (required)
        :param object option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id', 'option']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501
        if 'option' in params:
            query_params.append(('option', params['option']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/billboard/fetch_hot_user_portrait_list', 'GET',
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
