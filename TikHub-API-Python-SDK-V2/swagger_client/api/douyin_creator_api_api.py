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


class DouyinCreatorAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get(self, activity_id, **kwargs):  # noqa: E501
        """获取创作者活动详情/Get creator activity detail  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者活动详情数据 ### 参数: - activity_id: 活动ID（从活动列表接口获取） ### 返回: - 创作者活动详情数据  # [English] ### Purpose: - Get Douyin creator activity detail data ### Parameters: - activity_id: Activity ID (obtained from activity list interface) ### Return: - Creator activity detail data  # [示例/Example] activity_id = \"7545335931785450534\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get(activity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object activity_id: 活动ID/Activity ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get_with_http_info(activity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get_with_http_info(activity_id, **kwargs)  # noqa: E501
            return data

    def fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get_with_http_info(self, activity_id, **kwargs):  # noqa: E501
        """获取创作者活动详情/Get creator activity detail  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者活动详情数据 ### 参数: - activity_id: 活动ID（从活动列表接口获取） ### 返回: - 创作者活动详情数据  # [English] ### Purpose: - Get Douyin creator activity detail data ### Parameters: - activity_id: Activity ID (obtained from activity list interface) ### Return: - Creator activity detail data  # [示例/Example] activity_id = \"7545335931785450534\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get_with_http_info(activity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object activity_id: 活动ID/Activity ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activity_id' is set
        if self.api_client.client_side_validation and ('activity_id' not in params or
                                                       params['activity_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `activity_id` when calling `fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'activity_id' in params:
            query_params.append(('activity_id', params['activity_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_creator_activity_detail', 'GET',
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

    def fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get(self, start_time, end_time, **kwargs):  # noqa: E501
        """获取创作者活动列表/Get creator activity list  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者活动列表数据 ### 参数: - start_time: 开始时间戳 - end_time: 结束时间戳 ### 返回: - 创作者活动列表数据  # [English] ### Purpose: - Get Douyin creator activity list data ### Parameters: - start_time: Start timestamp - end_time: End timestamp ### Return: - Creator activity list data  # [示例/Example] start_time = 1756656000 end_time = 1759247999  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get(start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object start_time: 开始时间戳/Start timestamp (required)
        :param object end_time: 结束时间戳/End timestamp (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get_with_http_info(start_time, end_time, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get_with_http_info(start_time, end_time, **kwargs)  # noqa: E501
            return data

    def fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get_with_http_info(self, start_time, end_time, **kwargs):  # noqa: E501
        """获取创作者活动列表/Get creator activity list  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者活动列表数据 ### 参数: - start_time: 开始时间戳 - end_time: 结束时间戳 ### 返回: - 创作者活动列表数据  # [English] ### Purpose: - Get Douyin creator activity list data ### Parameters: - start_time: Start timestamp - end_time: End timestamp ### Return: - Creator activity list data  # [示例/Example] start_time = 1756656000 end_time = 1759247999  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get_with_http_info(start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object start_time: 开始时间戳/Start timestamp (required)
        :param object end_time: 结束时间戳/End timestamp (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start_time' is set
        if self.api_client.client_side_validation and ('start_time' not in params or
                                                       params['start_time'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `start_time` when calling `fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if self.api_client.client_side_validation and ('end_time' not in params or
                                                       params['end_time'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `end_time` when calling `fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_creator_activity_list', 'GET',
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

    def fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get(self, **kwargs):  # noqa: E501
        """获取创作者内容创作合集分类/Get creator content creation category  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台内容创作的合集分类列表 ### 参数: - 无需额外参数 ### 返回: - 内容创作合集分类数据  # [English] ### Purpose: - Get Douyin creator platform content creation category list ### Parameters: - No additional parameters required ### Return: - Content creation category data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者内容创作合集分类/Get creator content creation category  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台内容创作的合集分类列表 ### 参数: - 无需额外参数 ### 返回: - 内容创作合集分类数据  # [English] ### Purpose: - Get Douyin creator platform content creation category list ### Parameters: - No additional parameters required ### Return: - Content creation category data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get_with_http_info(async_req=True)
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
                    " to method fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get" % key
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
            '/api/v1/douyin/creator/fetch_creator_content_category', 'GET',
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

    def fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get(self, category_id, **kwargs):  # noqa: E501
        """获取创作者内容创作课程/Get creator content creation course  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台指定分类的内容创作课程 ### 参数: - category_id: 分类ID (更多分类ID请通过内容创作合集分类接口获取)     常见分类ID示例:     - 184: 视频创作     - 185: 直播创作     - 186: 图文创作     - 188: 美食视频创作     - 180: 内容创作基础 - order: 排序方式 (1=推荐排序, 2=最受欢迎, 3=最新上传) - limit: 每页数量 (建议24，范围1-100) - offset: 偏移量 (起始位置) ### 返回: - 指定分类的内容创作课程数据  # [English] ### Purpose: - Get Douyin creator platform content creation courses for specified category ### Parameters: - category_id: Category ID (for more category IDs, please refer to the content creation category interface)     Common category ID examples:     - 184: Video Creation     - 185: Live Streaming Creation     - 186: Image & Text Creation     - 188: Food Video Creation     - 180: Content Creation Basics - order: Order type (1=recommended order, 2=most popular, 3=latest upload) - limit: Items per page (recommended 24, range 1-100) - offset: Offset (starting position) ### Return: - Content creation course data for specified category  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category_id: 分类ID/Category ID (required)
        :param object order: 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传)
        :param object limit: 每页数量/Items per page
        :param object offset: 偏移量/Offset (starting position)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get_with_http_info(category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get_with_http_info(category_id, **kwargs)  # noqa: E501
            return data

    def fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get_with_http_info(self, category_id, **kwargs):  # noqa: E501
        """获取创作者内容创作课程/Get creator content creation course  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台指定分类的内容创作课程 ### 参数: - category_id: 分类ID (更多分类ID请通过内容创作合集分类接口获取)     常见分类ID示例:     - 184: 视频创作     - 185: 直播创作     - 186: 图文创作     - 188: 美食视频创作     - 180: 内容创作基础 - order: 排序方式 (1=推荐排序, 2=最受欢迎, 3=最新上传) - limit: 每页数量 (建议24，范围1-100) - offset: 偏移量 (起始位置) ### 返回: - 指定分类的内容创作课程数据  # [English] ### Purpose: - Get Douyin creator platform content creation courses for specified category ### Parameters: - category_id: Category ID (for more category IDs, please refer to the content creation category interface)     Common category ID examples:     - 184: Video Creation     - 185: Live Streaming Creation     - 186: Image & Text Creation     - 188: Food Video Creation     - 180: Content Creation Basics - order: Order type (1=recommended order, 2=most popular, 3=latest upload) - limit: Items per page (recommended 24, range 1-100) - offset: Offset (starting position) ### Return: - Content creation course data for specified category  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get_with_http_info(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category_id: 分类ID/Category ID (required)
        :param object order: 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传)
        :param object limit: 每页数量/Items per page
        :param object offset: 偏移量/Offset (starting position)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'order', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if self.api_client.client_side_validation and ('category_id' not in params or
                                                       params['category_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `category_id` when calling `fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category_id' in params:
            query_params.append(('category_id', params['category_id']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_creator_content_course', 'GET',
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

    def fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get(self, **kwargs):  # noqa: E501
        """获取创作者热门挑战榜单/Get creator hot challenge billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台热门挑战榜单数据 ### 返回: - 热门挑战榜单数据  # [English] ### Purpose: - Get Douyin creator platform hot challenge billboard data ### Return: - Hot challenge billboard data  # [示例/Example] 无需参数，直接调用即可获取当前热门挑战榜单 No parameters required, call directly to get current hot challenge billboard  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者热门挑战榜单/Get creator hot challenge billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台热门挑战榜单数据 ### 返回: - 热门挑战榜单数据  # [English] ### Purpose: - Get Douyin creator platform hot challenge billboard data ### Return: - Hot challenge billboard data  # [示例/Example] 无需参数，直接调用即可获取当前热门挑战榜单 No parameters required, call directly to get current hot challenge billboard  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get_with_http_info(async_req=True)
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
                    " to method fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get" % key
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
            '/api/v1/douyin/creator/fetch_creator_hot_challenge_billboard', 'GET',
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

    def fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get(self, **kwargs):  # noqa: E501
        """获取创作者热门课程/Get creator hot course  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台热门课程数据或精选专题课程 ### 参数: - order: 排序方式 (1=推荐排序, 2=最受欢迎, 3=最新上传) - limit: 每页数量 (建议24，范围1-100) - offset: 偏移量 (起始位置) - category_id: 精选专题分类ID (不传则获取热门课程，传入则获取指定分类的精选专题)     可选值:     - 6976547830546582816: 知识品类     - 6976547923849006336: 生活品类     - 6976547940311633165: 娱乐品类     - 6976547972108635404: 美食品类     - 6980288134957272352: 正能量     - 6980288181744766219: 游戏品类     - 6980288219548011776: 通用 ### 返回: - 热门课程数据或精选专题课程数据  # [English] ### Purpose: - Get Douyin creator platform hot course data or selected topic courses ### Parameters: - order: Order type (1=recommended order, 2=most popular, 3=latest upload) - limit: Items per page (recommended 24, range 1-100) - offset: Offset (starting position) - category_id: Selected topic category ID (empty for hot courses, specific ID for selected topics)     Available values:     - 6976547830546582816: Knowledge Category     - 6976547923849006336: Life Category     - 6976547940311633165: Entertainment Category     - 6976547972108635404: Food Category     - 6980288134957272352: Positive Energy     - 6980288181744766219: Gaming Category     - 6980288219548011776: General ### Return: - Hot course data or selected topic course data  # [示例/Example] ``` # 获取热门课程/Get hot courses GET /fetch_creator_hot_course?order=1&limit=24&offset=0  # 获取知识品类精选专题/Get knowledge category selected topics GET /fetch_creator_hot_course?order=1&limit=24&offset=0&category_id=6976547830546582816  # 获取美食品类精选专题/Get food category selected topics GET /fetch_creator_hot_course?order=1&limit=24&offset=0&category_id=6976547972108635404 ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object order: 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传)
        :param object limit: 每页数量/Items per page (建议24)
        :param object offset: 偏移量/Offset
        :param object category_id: 精选专题分类ID/Selected topic category ID - 不传则为热门课程，传入则为精选专题         可选值/Available values:         6976547830546582816=知识品类, 6976547923849006336=生活品类, 6976547940311633165=娱乐品类,         6976547972108635404=美食品类, 6980288134957272352=正能量, 6980288181744766219=游戏品类,         6980288219548011776=通用
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者热门课程/Get creator hot course  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台热门课程数据或精选专题课程 ### 参数: - order: 排序方式 (1=推荐排序, 2=最受欢迎, 3=最新上传) - limit: 每页数量 (建议24，范围1-100) - offset: 偏移量 (起始位置) - category_id: 精选专题分类ID (不传则获取热门课程，传入则获取指定分类的精选专题)     可选值:     - 6976547830546582816: 知识品类     - 6976547923849006336: 生活品类     - 6976547940311633165: 娱乐品类     - 6976547972108635404: 美食品类     - 6980288134957272352: 正能量     - 6980288181744766219: 游戏品类     - 6980288219548011776: 通用 ### 返回: - 热门课程数据或精选专题课程数据  # [English] ### Purpose: - Get Douyin creator platform hot course data or selected topic courses ### Parameters: - order: Order type (1=recommended order, 2=most popular, 3=latest upload) - limit: Items per page (recommended 24, range 1-100) - offset: Offset (starting position) - category_id: Selected topic category ID (empty for hot courses, specific ID for selected topics)     Available values:     - 6976547830546582816: Knowledge Category     - 6976547923849006336: Life Category     - 6976547940311633165: Entertainment Category     - 6976547972108635404: Food Category     - 6980288134957272352: Positive Energy     - 6980288181744766219: Gaming Category     - 6980288219548011776: General ### Return: - Hot course data or selected topic course data  # [示例/Example] ``` # 获取热门课程/Get hot courses GET /fetch_creator_hot_course?order=1&limit=24&offset=0  # 获取知识品类精选专题/Get knowledge category selected topics GET /fetch_creator_hot_course?order=1&limit=24&offset=0&category_id=6976547830546582816  # 获取美食品类精选专题/Get food category selected topics GET /fetch_creator_hot_course?order=1&limit=24&offset=0&category_id=6976547972108635404 ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object order: 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传)
        :param object limit: 每页数量/Items per page (建议24)
        :param object offset: 偏移量/Offset
        :param object category_id: 精选专题分类ID/Selected topic category ID - 不传则为热门课程，传入则为精选专题         可选值/Available values:         6976547830546582816=知识品类, 6976547923849006336=生活品类, 6976547940311633165=娱乐品类,         6976547972108635404=美食品类, 6980288134957272352=正能量, 6980288181744766219=游戏品类,         6980288219548011776=通用
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order', 'limit', 'offset', 'category_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'category_id' in params:
            query_params.append(('category_id', params['category_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_creator_hot_course', 'GET',
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

    def fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get(self, **kwargs):  # noqa: E501
        """获取创作者热门音乐榜单/Get creator hot music billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台热门音乐榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过配置接口获取 - order_key: 排序键 (1=播放最高, 2=点赞最多, 4=热度最高, 5=投稿最多) - time_filter: 时间筛选 (1=24小时, 2=7天, 3=30天) ### 返回: - 热门音乐榜单数据  # [English] ### Purpose: - Get Douyin creator platform hot music billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface - order_key: Order key (1=highest views, 2=most likes, 4=highest popularity, 5=most submissions) - time_filter: Time filter (1=24 hours, 2=7 days, 3=30 days) ### Return: - Hot music billboard data  # [示例/Example] billboard_tag = 0   # 全部/All order_key = 1   # 播放最高/Highest views time_filter = 1 # 24小时/24 hours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_tag: 榜单标签/Billboard tag (0=全部，具体分类值可通过配置接口获取)
        :param object order_key: 排序键/Order key (1=播放最高, 2=点赞最多, 4=热度最高, 5=投稿最多)
        :param object time_filter: 时间筛选/Time filter (1=24小时, 2=7天, 3=30天)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者热门音乐榜单/Get creator hot music billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台热门音乐榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过配置接口获取 - order_key: 排序键 (1=播放最高, 2=点赞最多, 4=热度最高, 5=投稿最多) - time_filter: 时间筛选 (1=24小时, 2=7天, 3=30天) ### 返回: - 热门音乐榜单数据  # [English] ### Purpose: - Get Douyin creator platform hot music billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface - order_key: Order key (1=highest views, 2=most likes, 4=highest popularity, 5=most submissions) - time_filter: Time filter (1=24 hours, 2=7 days, 3=30 days) ### Return: - Hot music billboard data  # [示例/Example] billboard_tag = 0   # 全部/All order_key = 1   # 播放最高/Highest views time_filter = 1 # 24小时/24 hours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_tag: 榜单标签/Billboard tag (0=全部，具体分类值可通过配置接口获取)
        :param object order_key: 排序键/Order key (1=播放最高, 2=点赞最多, 4=热度最高, 5=投稿最多)
        :param object time_filter: 时间筛选/Time filter (1=24小时, 2=7天, 3=30天)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billboard_tag', 'order_key', 'time_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'billboard_tag' in params:
            query_params.append(('billboard_tag', params['billboard_tag']))  # noqa: E501
        if 'order_key' in params:
            query_params.append(('order_key', params['order_key']))  # noqa: E501
        if 'time_filter' in params:
            query_params.append(('time_filter', params['time_filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_creator_hot_music_billboard', 'GET',
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

    def fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get(self, **kwargs):  # noqa: E501
        """获取创作者热门道具榜单/Get creator hot props billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者热门道具榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取     - 0: 全部     - 333: 美食     - 334: 旅行     - 299: 泛生活     - 335: 汽车     - 336: 科技     - 302: 游戏     - 296: 二次元     - 337: 娱乐     - 311: 明星     - 298: 体育     - 300: 文化教育     - 301: 校园     - 297: 政务     - 305: 时尚     - 306: 才艺     - 669: 财经     - 314: 随拍     - 307: 动植物     - 309: 图文控     - 308: 剧情     - 315: 亲子     - 718: 三农     - 310: 创意     - 312: 户外     - 926: 公益 - order_key: 排序键     - 1: 播放最高     - 5: 投稿最多     - 6: 展现最高     - 7: 收藏最高 - time_filter: 时间筛选     - 1: 24小时     - 2: 7天     - 3: 30天 ### 返回: - 创作者热门道具榜单数据  # [English] ### Purpose: - Get Douyin creator hot props billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface     - 0: All     - 333: Food     - 334: Travel     - 299: Lifestyle     - 335: Automotive     - 336: Technology     - 302: Gaming     - 296: Anime     - 337: Entertainment     - 311: Celebrity     - 298: Sports     - 300: Culture & Education     - 301: Campus     - 297: Government     - 305: Fashion     - 306: Talent Show     - 669: Finance     - 314: Random     - 307: Animals & Plants     - 309: Graphics & Text     - 308: Drama     - 315: Parenting     - 718: Agriculture     - 310: Creative     - 312: Outdoor     - 926: Public Welfare - order_key: Order key     - 1: Highest views     - 5: Most submissions     - 6: Highest exposure     - 7: Most favorites - time_filter: Time filter     - 1: 24 hours     - 2: 7 days     - 3: 30 days ### Return: - Creator hot props billboard data  # [示例/Example] billboard_tag = 0 order_key = 1  # 播放最高/Highest views time_filter = 1  # 24小时/24 hours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface
        :param object order_key: 排序键: 1=播放最高, 5=投稿最多, 6=展现最高, 7=收藏最高/Order key: 1=highest views, 5=most submissions, 6=highest exposure, 7=most favorites
        :param object time_filter: 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者热门道具榜单/Get creator hot props billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者热门道具榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取     - 0: 全部     - 333: 美食     - 334: 旅行     - 299: 泛生活     - 335: 汽车     - 336: 科技     - 302: 游戏     - 296: 二次元     - 337: 娱乐     - 311: 明星     - 298: 体育     - 300: 文化教育     - 301: 校园     - 297: 政务     - 305: 时尚     - 306: 才艺     - 669: 财经     - 314: 随拍     - 307: 动植物     - 309: 图文控     - 308: 剧情     - 315: 亲子     - 718: 三农     - 310: 创意     - 312: 户外     - 926: 公益 - order_key: 排序键     - 1: 播放最高     - 5: 投稿最多     - 6: 展现最高     - 7: 收藏最高 - time_filter: 时间筛选     - 1: 24小时     - 2: 7天     - 3: 30天 ### 返回: - 创作者热门道具榜单数据  # [English] ### Purpose: - Get Douyin creator hot props billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface     - 0: All     - 333: Food     - 334: Travel     - 299: Lifestyle     - 335: Automotive     - 336: Technology     - 302: Gaming     - 296: Anime     - 337: Entertainment     - 311: Celebrity     - 298: Sports     - 300: Culture & Education     - 301: Campus     - 297: Government     - 305: Fashion     - 306: Talent Show     - 669: Finance     - 314: Random     - 307: Animals & Plants     - 309: Graphics & Text     - 308: Drama     - 315: Parenting     - 718: Agriculture     - 310: Creative     - 312: Outdoor     - 926: Public Welfare - order_key: Order key     - 1: Highest views     - 5: Most submissions     - 6: Highest exposure     - 7: Most favorites - time_filter: Time filter     - 1: 24 hours     - 2: 7 days     - 3: 30 days ### Return: - Creator hot props billboard data  # [示例/Example] billboard_tag = 0 order_key = 1  # 播放最高/Highest views time_filter = 1  # 24小时/24 hours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface
        :param object order_key: 排序键: 1=播放最高, 5=投稿最多, 6=展现最高, 7=收藏最高/Order key: 1=highest views, 5=most submissions, 6=highest exposure, 7=most favorites
        :param object time_filter: 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billboard_tag', 'order_key', 'time_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'billboard_tag' in params:
            query_params.append(('billboard_tag', params['billboard_tag']))  # noqa: E501
        if 'order_key' in params:
            query_params.append(('order_key', params['order_key']))  # noqa: E501
        if 'time_filter' in params:
            query_params.append(('time_filter', params['time_filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_creator_hot_props_billboard', 'GET',
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

    def fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get(self, **kwargs):  # noqa: E501
        """获取创作者中心创作热点/Get creator hot spot billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者热点榜单数据 ### 参数: - billboard_tag: 热点标签，多个标签用逗号分隔     可选值:     - 站内玩法: 1004,1000,1002,1003,1001     - 话题互动: 20001,20006,20000,20003,20005,20002,20     - 娱乐: 2007,2000,2011,2012,2009,2010,2004,2005,2003,2008,2001,2002,2006     - 社会: 4005,4006,4007,4003,4004,4000     - 二次元: 13000     - 交通: 23000     - 亲子: 19000     - 体育: 5002,5000,5001     - 军事: 21000     - 剧情: 18000     - 动物萌宠: 8000     - 天气: 22001,22002     - 才艺: 17000     - 文化教育: 14000     - 旅行: 10000     - 时尚: 16000     - 时政: 3000,3001,3002     - 校园: 15000     - 汽车: 11000     - 游戏: 12000,12001     - 科技: 6000     - 美食: 9000     - 财经: 7000 - hot_search_type: 热搜类型     - 1: 热点总榜     - 2: 同城热点榜     - 3: 热点上升榜 - city_code: 城市代码，当hot_search_type=2时必需 ### 返回: - 创作者热点榜单数据  # [English] ### Purpose: - Get Douyin creator hot spot billboard data ### Parameters: - billboard_tag: Hot spot tag - multiple tags separated by comma     Available values:     - Platform Features: 1004,1000,1002,1003,1001     - Topic Interaction: 20001,20006,20000,20003,20005,20002,20     - Entertainment: 2007,2000,2011,2012,2009,2010,2004,2005,2003,2008,2001,2002,2006     - Society: 4005,4006,4007,4003,4004,4000     - Anime: 13000     - Transportation: 23000     - Parenting: 19000     - Sports: 5002,5000,5001     - Military: 21000     - Drama: 18000     - Animals & Pets: 8000     - Weather: 22001,22002     - Talent Show: 17000     - Culture & Education: 14000     - Travel: 10000     - Fashion: 16000     - Politics: 3000,3001,3002     - Campus: 15000     - Automotive: 11000     - Gaming: 12000,12001     - Technology: 6000     - Food: 9000     - Finance: 7000 - hot_search_type: Hot search type     - 1: Hot Spot Overall Ranking     - 2: Local Hot Spot Ranking     - 3: Rising Hot Spot Ranking - city_code: City code - required when hot_search_type=2 ### Return: - Creator hot spot billboard data  # [示例/Example] billboard_tag = \"0\"  # 全部/All hot_search_type = 1  # 热点总榜/Overall ranking city_code = None  # 可选/Optional  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_tag: 热点标签，多个标签用逗号分隔，如'1004,1000,1002'/Hot spot tag - multiple tags separated by comma, like '1004,1000,1002'
        :param object hot_search_type: 热搜类型: 1=热点总榜, 2=同城热点榜, 3=热点上升榜/Hot search type: 1=Overall ranking, 2=Local ranking, 3=Rising ranking
        :param object city_code: 城市代码，当hot_search_type=2时必需/City code - required when hot_search_type=2
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者中心创作热点/Get creator hot spot billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者热点榜单数据 ### 参数: - billboard_tag: 热点标签，多个标签用逗号分隔     可选值:     - 站内玩法: 1004,1000,1002,1003,1001     - 话题互动: 20001,20006,20000,20003,20005,20002,20     - 娱乐: 2007,2000,2011,2012,2009,2010,2004,2005,2003,2008,2001,2002,2006     - 社会: 4005,4006,4007,4003,4004,4000     - 二次元: 13000     - 交通: 23000     - 亲子: 19000     - 体育: 5002,5000,5001     - 军事: 21000     - 剧情: 18000     - 动物萌宠: 8000     - 天气: 22001,22002     - 才艺: 17000     - 文化教育: 14000     - 旅行: 10000     - 时尚: 16000     - 时政: 3000,3001,3002     - 校园: 15000     - 汽车: 11000     - 游戏: 12000,12001     - 科技: 6000     - 美食: 9000     - 财经: 7000 - hot_search_type: 热搜类型     - 1: 热点总榜     - 2: 同城热点榜     - 3: 热点上升榜 - city_code: 城市代码，当hot_search_type=2时必需 ### 返回: - 创作者热点榜单数据  # [English] ### Purpose: - Get Douyin creator hot spot billboard data ### Parameters: - billboard_tag: Hot spot tag - multiple tags separated by comma     Available values:     - Platform Features: 1004,1000,1002,1003,1001     - Topic Interaction: 20001,20006,20000,20003,20005,20002,20     - Entertainment: 2007,2000,2011,2012,2009,2010,2004,2005,2003,2008,2001,2002,2006     - Society: 4005,4006,4007,4003,4004,4000     - Anime: 13000     - Transportation: 23000     - Parenting: 19000     - Sports: 5002,5000,5001     - Military: 21000     - Drama: 18000     - Animals & Pets: 8000     - Weather: 22001,22002     - Talent Show: 17000     - Culture & Education: 14000     - Travel: 10000     - Fashion: 16000     - Politics: 3000,3001,3002     - Campus: 15000     - Automotive: 11000     - Gaming: 12000,12001     - Technology: 6000     - Food: 9000     - Finance: 7000 - hot_search_type: Hot search type     - 1: Hot Spot Overall Ranking     - 2: Local Hot Spot Ranking     - 3: Rising Hot Spot Ranking - city_code: City code - required when hot_search_type=2 ### Return: - Creator hot spot billboard data  # [示例/Example] billboard_tag = \"0\"  # 全部/All hot_search_type = 1  # 热点总榜/Overall ranking city_code = None  # 可选/Optional  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_tag: 热点标签，多个标签用逗号分隔，如'1004,1000,1002'/Hot spot tag - multiple tags separated by comma, like '1004,1000,1002'
        :param object hot_search_type: 热搜类型: 1=热点总榜, 2=同城热点榜, 3=热点上升榜/Hot search type: 1=Overall ranking, 2=Local ranking, 3=Rising ranking
        :param object city_code: 城市代码，当hot_search_type=2时必需/City code - required when hot_search_type=2
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billboard_tag', 'hot_search_type', 'city_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'billboard_tag' in params:
            query_params.append(('billboard_tag', params['billboard_tag']))  # noqa: E501
        if 'hot_search_type' in params:
            query_params.append(('hot_search_type', params['hot_search_type']))  # noqa: E501
        if 'city_code' in params:
            query_params.append(('city_code', params['city_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_creator_hot_spot_billboard', 'GET',
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

    def fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get(self, **kwargs):  # noqa: E501
        """获取创作者热门话题榜单/Get creator hot topic billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者热门话题榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取     - 0: 全部     - 333: 美食     - 334: 旅行     - 299: 泛生活     - 335: 汽车     - 336: 科技     - 302: 游戏     - 296: 二次元     - 337: 娱乐     - 311: 明星     - 298: 体育     - 300: 文化教育     - 301: 校园     - 297: 政务     - 305: 时尚     - 306: 才艺     - 669: 财经     - 314: 随拍     - 307: 动植物     - 309: 图文控     - 308: 剧情     - 315: 亲子     - 718: 三农     - 310: 创意     - 312: 户外     - 926: 公益 - order_key: 排序键     - 1: 播放最高     - 2: 点赞最多     - 3: 评论最多     - 4: 投稿最多 - time_filter: 时间筛选     - 1: 24小时     - 2: 7天     - 3: 30天 ### 返回: - 创作者热门话题榜单数据  # [English] ### Purpose: - Get Douyin creator hot topic billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface     - 0: All     - 333: Food     - 334: Travel     - 299: Lifestyle     - 335: Automotive     - 336: Technology     - 302: Gaming     - 296: Anime     - 337: Entertainment     - 311: Celebrity     - 298: Sports     - 300: Culture & Education     - 301: Campus     - 297: Government     - 305: Fashion     - 306: Talent Show     - 669: Finance     - 314: Random     - 307: Animals & Plants     - 309: Graphics & Text     - 308: Drama     - 315: Parenting     - 718: Agriculture     - 310: Creative     - 312: Outdoor     - 926: Public Welfare - order_key: Order key     - 1: Highest views     - 2: Most likes     - 3: Most comments     - 4: Most submissions - time_filter: Time filter     - 1: 24 hours     - 2: 7 days     - 3: 30 days ### Return: - Creator hot topic billboard data  # [示例/Example] billboard_tag = 0 order_key = 1  # 播放最高/Highest views time_filter = 1  # 24小时/24 hours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface
        :param object order_key: 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=投稿最多/Order key: 1=highest views, 2=most likes, 3=most comments, 4=most submissions
        :param object time_filter: 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者热门话题榜单/Get creator hot topic billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者热门话题榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取     - 0: 全部     - 333: 美食     - 334: 旅行     - 299: 泛生活     - 335: 汽车     - 336: 科技     - 302: 游戏     - 296: 二次元     - 337: 娱乐     - 311: 明星     - 298: 体育     - 300: 文化教育     - 301: 校园     - 297: 政务     - 305: 时尚     - 306: 才艺     - 669: 财经     - 314: 随拍     - 307: 动植物     - 309: 图文控     - 308: 剧情     - 315: 亲子     - 718: 三农     - 310: 创意     - 312: 户外     - 926: 公益 - order_key: 排序键     - 1: 播放最高     - 2: 点赞最多     - 3: 评论最多     - 4: 投稿最多 - time_filter: 时间筛选     - 1: 24小时     - 2: 7天     - 3: 30天 ### 返回: - 创作者热门话题榜单数据  # [English] ### Purpose: - Get Douyin creator hot topic billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface     - 0: All     - 333: Food     - 334: Travel     - 299: Lifestyle     - 335: Automotive     - 336: Technology     - 302: Gaming     - 296: Anime     - 337: Entertainment     - 311: Celebrity     - 298: Sports     - 300: Culture & Education     - 301: Campus     - 297: Government     - 305: Fashion     - 306: Talent Show     - 669: Finance     - 314: Random     - 307: Animals & Plants     - 309: Graphics & Text     - 308: Drama     - 315: Parenting     - 718: Agriculture     - 310: Creative     - 312: Outdoor     - 926: Public Welfare - order_key: Order key     - 1: Highest views     - 2: Most likes     - 3: Most comments     - 4: Most submissions - time_filter: Time filter     - 1: 24 hours     - 2: 7 days     - 3: 30 days ### Return: - Creator hot topic billboard data  # [示例/Example] billboard_tag = 0 order_key = 1  # 播放最高/Highest views time_filter = 1  # 24小时/24 hours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface
        :param object order_key: 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=投稿最多/Order key: 1=highest views, 2=most likes, 3=most comments, 4=most submissions
        :param object time_filter: 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billboard_tag', 'order_key', 'time_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'billboard_tag' in params:
            query_params.append(('billboard_tag', params['billboard_tag']))  # noqa: E501
        if 'order_key' in params:
            query_params.append(('order_key', params['order_key']))  # noqa: E501
        if 'time_filter' in params:
            query_params.append(('time_filter', params['time_filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_creator_hot_topic_billboard', 'GET',
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

    def fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get(self, **kwargs):  # noqa: E501
        """获取创作者中心热门视频榜单/Get creator material center billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者中心热门视频榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取     - 0: 全部     - 333: 美食     - 334: 旅行     - 299: 泛生活     - 335: 汽车     - 336: 科技     - 302: 游戏     - 296: 二次元     - 337: 娱乐     - 311: 明星     - 298: 体育     - 300: 文化教育     - 301: 校园     - 297: 政务     - 305: 时尚     - 306: 才艺     - 669: 财经     - 314: 随拍     - 307: 动植物     - 309: 图文控     - 308: 剧情     - 315: 亲子     - 718: 三农     - 310: 创意     - 312: 户外     - 926: 公益 - order_key: 排序键     - 1: 播放最高     - 2: 点赞最多     - 3: 评论最多     - 4: 热度最高 - time_filter: 时间筛选     - 1: 24小时     - 2: 7天     - 3: 30天 ### 返回: - 创作者中心热门视频榜单数据  # [English] ### Purpose: - Get Douyin creator material center billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface     - 0: All     - 333: Food     - 334: Travel     - 299: Lifestyle     - 335: Automotive     - 336: Technology     - 302: Gaming     - 296: Anime     - 337: Entertainment     - 311: Celebrity     - 298: Sports     - 300: Culture & Education     - 301: Campus     - 297: Government     - 305: Fashion     - 306: Talent Show     - 669: Finance     - 314: Random     - 307: Animals & Plants     - 309: Graphics & Text     - 308: Drama     - 315: Parenting     - 718: Agriculture     - 310: Creative     - 312: Outdoor     - 926: Public Welfare - order_key: Order key     - 1: Highest views     - 2: Most likes     - 3: Most comments     - 4: Highest popularity - time_filter: Time filter     - 1: 24 hours     - 2: 7 days     - 3: 30 days ### Return: - Creator material center billboard data  # [示例/Example] billboard_tag = 0 order_key = 1  # 播放最高/Highest views time_filter = 1  # 24小时/24 hours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface
        :param object order_key: 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=热度最高/Order key: 1=highest views, 2=most likes, 3=most comments, 4=highest popularity
        :param object time_filter: 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者中心热门视频榜单/Get creator material center billboard  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者中心热门视频榜单数据 ### 参数: - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取     - 0: 全部     - 333: 美食     - 334: 旅行     - 299: 泛生活     - 335: 汽车     - 336: 科技     - 302: 游戏     - 296: 二次元     - 337: 娱乐     - 311: 明星     - 298: 体育     - 300: 文化教育     - 301: 校园     - 297: 政务     - 305: 时尚     - 306: 才艺     - 669: 财经     - 314: 随拍     - 307: 动植物     - 309: 图文控     - 308: 剧情     - 315: 亲子     - 718: 三农     - 310: 创意     - 312: 户外     - 926: 公益 - order_key: 排序键     - 1: 播放最高     - 2: 点赞最多     - 3: 评论最多     - 4: 热度最高 - time_filter: 时间筛选     - 1: 24小时     - 2: 7天     - 3: 30天 ### 返回: - 创作者中心热门视频榜单数据  # [English] ### Purpose: - Get Douyin creator material center billboard data ### Parameters: - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface     - 0: All     - 333: Food     - 334: Travel     - 299: Lifestyle     - 335: Automotive     - 336: Technology     - 302: Gaming     - 296: Anime     - 337: Entertainment     - 311: Celebrity     - 298: Sports     - 300: Culture & Education     - 301: Campus     - 297: Government     - 305: Fashion     - 306: Talent Show     - 669: Finance     - 314: Random     - 307: Animals & Plants     - 309: Graphics & Text     - 308: Drama     - 315: Parenting     - 718: Agriculture     - 310: Creative     - 312: Outdoor     - 926: Public Welfare - order_key: Order key     - 1: Highest views     - 2: Most likes     - 3: Most comments     - 4: Highest popularity - time_filter: Time filter     - 1: 24 hours     - 2: 7 days     - 3: 30 days ### Return: - Creator material center billboard data  # [示例/Example] billboard_tag = 0 order_key = 1  # 播放最高/Highest views time_filter = 1  # 24小时/24 hours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface
        :param object order_key: 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=热度最高/Order key: 1=highest views, 2=most likes, 3=most comments, 4=highest popularity
        :param object time_filter: 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billboard_tag', 'order_key', 'time_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'billboard_tag' in params:
            query_params.append(('billboard_tag', params['billboard_tag']))  # noqa: E501
        if 'order_key' in params:
            query_params.append(('order_key', params['order_key']))  # noqa: E501
        if 'time_filter' in params:
            query_params.append(('time_filter', params['time_filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_creator_material_center_billboard', 'GET',
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

    def fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get(self, **kwargs):  # noqa: E501
        """获取创作者中心配置/Get creator material center config  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者中心配置信息 ### 返回: - 创作者中心配置数据  # [English] ### Purpose: - Get Douyin creator material center configuration ### Return: - Creator material center config data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者中心配置/Get creator material center config  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者中心配置信息 ### 返回: - 创作者中心配置数据  # [English] ### Purpose: - Get Douyin creator material center configuration ### Return: - Creator material center config data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get_with_http_info(async_req=True)
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
                    " to method fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get" % key
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
            '/api/v1/douyin/creator/fetch_creator_material_center_config', 'GET',
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

    def fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get(self, **kwargs):  # noqa: E501
        """获取行业分类配置/Get industry category config  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台的行业分类配置 - 返回所有可用的行业分类层级结构 - **建议在调用商单任务列表接口前先调用此接口获取完整的行业分类信息**  ### 重要说明: - 此接口已优化为Redis缓存，首次调用后数据将缓存30天 - 缓存键: `douyin_creator:industry_categories` - 数据结构包含一级行业和二级行业的完整映射关系  ### 数据结构: ```json {     \"status_code\": 0,     \"status_msg\": \"success\",     \"data\": {         \"industry_categories\": [             {\"key\": \"-1\", \"label\": \"全部\"},             {\"key\": 1901, \"label\": \"3C及电器\"},             {\"key\": 1913, \"label\": \"游戏\"},             ...         ],         \"industry_subcategories\": {             1913: [                 {\"key\": \"-1\", \"label\": \"全部\"},                 {\"key\": 191301, \"label\": \"休闲游戏\"},                 {\"key\": 191302, \"label\": \"棋牌桌游\"},                 ...             ],             ...         }     } } ```  ### 在商单任务筛选中的使用: 1. **获取全部行业任务**: `industry_lv1=-1` (此时industry_lv2无需设置) 2. **获取特定一级行业**: `industry_lv1=1913` (游戏行业) 3. **获取特定二级行业**: `industry_lv1=1913&industry_lv2=191301` (游戏-休闲游戏)  ### 性能优化: - 首次调用时从本地JSON文件读取并缓存到Redis - 后续调用直接从Redis缓存读取，大幅提升响应速度 - 缓存有效期30天，确保数据时效性  ### 返回: - 返回完整的行业分类树结构 - 包含32个一级行业分类和对应的二级行业分类 - 每个分类包含分类ID(key)和名称(label)  # [English] ### Purpose: - Get industry category configuration from Douyin Creator platform - Returns all available industry classification hierarchy - **Recommend calling this API first before using mission task list API to get complete industry classification info**  ### Important Notes: - This API is optimized with Redis caching, data will be cached for 30 days after first call - Cache key: `douyin_creator:industry_categories` - Data structure contains complete mapping relationship between primary and secondary industries  ### Data Structure: ```json {     \"status_code\": 0,     \"status_msg\": \"success\",     \"data\": {         \"industry_categories\": [             {\"key\": \"-1\", \"label\": \"All\"},             {\"key\": 1901, \"label\": \"3C & Electronics\"},             {\"key\": 1913, \"label\": \"Gaming\"},             ...         ],         \"industry_subcategories\": {             1913: [                 {\"key\": \"-1\", \"label\": \"All\"},                 {\"key\": 191301, \"label\": \"Casual Games\"},                 {\"key\": 191302, \"label\": \"Board Games\"},                 ...             ],             ...         }     } } ```  ### Usage in Mission Task Filtering: 1. **Get all industry tasks**: `industry_lv1=-1` (industry_lv2 not needed) 2. **Get specific primary industry**: `industry_lv1=1913` (Gaming industry) 3. **Get specific secondary industry**: `industry_lv1=1913&industry_lv2=191301` (Gaming-Casual Games)  ### Performance Optimization: - First call reads from local JSON file and caches to Redis - Subsequent calls read directly from Redis cache, significantly improving response speed - Cache validity period of 30 days ensures data timeliness  ### Return: - Returns complete industry classification tree structure - Contains 32 primary industry categories and corresponding secondary industry categories - Each category contains category ID(key) and name(label)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取行业分类配置/Get industry category config  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台的行业分类配置 - 返回所有可用的行业分类层级结构 - **建议在调用商单任务列表接口前先调用此接口获取完整的行业分类信息**  ### 重要说明: - 此接口已优化为Redis缓存，首次调用后数据将缓存30天 - 缓存键: `douyin_creator:industry_categories` - 数据结构包含一级行业和二级行业的完整映射关系  ### 数据结构: ```json {     \"status_code\": 0,     \"status_msg\": \"success\",     \"data\": {         \"industry_categories\": [             {\"key\": \"-1\", \"label\": \"全部\"},             {\"key\": 1901, \"label\": \"3C及电器\"},             {\"key\": 1913, \"label\": \"游戏\"},             ...         ],         \"industry_subcategories\": {             1913: [                 {\"key\": \"-1\", \"label\": \"全部\"},                 {\"key\": 191301, \"label\": \"休闲游戏\"},                 {\"key\": 191302, \"label\": \"棋牌桌游\"},                 ...             ],             ...         }     } } ```  ### 在商单任务筛选中的使用: 1. **获取全部行业任务**: `industry_lv1=-1` (此时industry_lv2无需设置) 2. **获取特定一级行业**: `industry_lv1=1913` (游戏行业) 3. **获取特定二级行业**: `industry_lv1=1913&industry_lv2=191301` (游戏-休闲游戏)  ### 性能优化: - 首次调用时从本地JSON文件读取并缓存到Redis - 后续调用直接从Redis缓存读取，大幅提升响应速度 - 缓存有效期30天，确保数据时效性  ### 返回: - 返回完整的行业分类树结构 - 包含32个一级行业分类和对应的二级行业分类 - 每个分类包含分类ID(key)和名称(label)  # [English] ### Purpose: - Get industry category configuration from Douyin Creator platform - Returns all available industry classification hierarchy - **Recommend calling this API first before using mission task list API to get complete industry classification info**  ### Important Notes: - This API is optimized with Redis caching, data will be cached for 30 days after first call - Cache key: `douyin_creator:industry_categories` - Data structure contains complete mapping relationship between primary and secondary industries  ### Data Structure: ```json {     \"status_code\": 0,     \"status_msg\": \"success\",     \"data\": {         \"industry_categories\": [             {\"key\": \"-1\", \"label\": \"All\"},             {\"key\": 1901, \"label\": \"3C & Electronics\"},             {\"key\": 1913, \"label\": \"Gaming\"},             ...         ],         \"industry_subcategories\": {             1913: [                 {\"key\": \"-1\", \"label\": \"All\"},                 {\"key\": 191301, \"label\": \"Casual Games\"},                 {\"key\": 191302, \"label\": \"Board Games\"},                 ...             ],             ...         }     } } ```  ### Usage in Mission Task Filtering: 1. **Get all industry tasks**: `industry_lv1=-1` (industry_lv2 not needed) 2. **Get specific primary industry**: `industry_lv1=1913` (Gaming industry) 3. **Get specific secondary industry**: `industry_lv1=1913&industry_lv2=191301` (Gaming-Casual Games)  ### Performance Optimization: - First call reads from local JSON file and caches to Redis - Subsequent calls read directly from Redis cache, significantly improving response speed - Cache validity period of 30 days ensures data timeliness  ### Return: - Returns complete industry classification tree structure - Contains 32 primary industry categories and corresponding secondary industry categories - Each category contains category ID(key) and name(label)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get_with_http_info(async_req=True)
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
                    " to method fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get" % key
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
            '/api/v1/douyin/creator/fetch_industry_category_config', 'GET',
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

    def fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get(self, **kwargs):  # noqa: E501
        """获取商单任务列表/Get mission task list  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台的商单任务列表 - 支持多种筛选条件，包括行业分类、付费类型、平台渠道等  ### 重要参数使用说明: #### 行业分类组合规则: - **industry_lv1=-1 (全部)**: 当选择全部一级行业时，industry_lv2参数将被忽略，无需设置 - **industry_lv1=具体值**: 当选择具体一级行业时，可配合industry_lv2进行二级筛选     - industry_lv2=-1: 该一级行业下的所有二级分类     - industry_lv2=具体值: 该一级行业下的具体二级分类  #### 可选参数 (选择\"全部\"时无需传入): - **platform_channel**: 不传入表示全部平台渠道 - **pay_type**: 不传入表示全部付费类型 - **greater_than_cost_progress**: 不传入表示不限制成本进度 - **publish_time_start**: 不传入表示不限制发布时间 - **quick_selector_scene**: 不传入表示不使用快速筛选 - **keyword**: 不传入表示不进行关键词搜索  ### 参数详解: - cursor: 游标，用于分页，0表示第一页 - limit: 每页返回的任务数量，建议24 - mission_type: 任务类型，通常为1 - tab_scene: 场景类型     - 1: 可投稿 (可以直接投稿的任务)     - 2: 可报名 (需要报名审核的任务)     - 3: 好物测评 (商品测评类任务) - industry_lv1/lv2: 行业分类 (建议先调用fetch_industry_category_config获取完整分类)     - -1: 全部行业     - 具体数值: 对应具体行业类别 (如1913=游戏, 1903=食品饮料) - platform_channel: 平台渠道 (可选)     - 1: 抖音视频     - 2: 抖音直播     - 3: 抖音图文 - pay_type: 付费类型 (可选)     - 1: 视频等级 (按粉丝量等级定价)     - 2: 自定义 (商家自定义价格)     - 3: 按转化付费 (按转化效果付费)     - 4: 按有效播放量 (按播放量付费)     - 5: 按销售量 (按商品销售量付费)     - 9: 按核销量 (按核销数量付费)     - 14: 按付费分佣 (按分佣比例付费) - greater_than_cost_progress: 成本进度筛选 (可选)     - 20: 高于20%成本进度的任务     - 50: 高于50%成本进度的任务     - 80: 高于80%成本进度的任务 - publish_time_start: 发布开始时间过滤 (可选，时间戳格式) - quick_selector_scene: 快速筛选场景 (可选)     - 1: 高收益任务     - 4: 保底收入任务     - 5: 曾经合作过的商家 - keyword: 关键词搜索 (可选，支持任务名称或任务ID)  ### 使用示例: ``` # 获取全部行业的可投稿任务 GET /fetch_mission_task_list?industry_lv1=-1&tab_scene=1  # 获取游戏行业休闲游戏分类的按播放量付费任务 GET /fetch_mission_task_list?industry_lv1=1913&industry_lv2=191301&pay_type=4  # 获取高收益的抖音视频任务 GET /fetch_mission_task_list?platform_channel=1&quick_selector_scene=1 ```  ### 返回: - 返回符合条件的商单任务列表 - 包含任务详情、报酬信息、要求等  # [English] ### Purpose: - Get mission task list from Douyin Creator platform - Supports multiple filtering conditions including industry classification, payment type, platform channel, etc.  ### Important Parameter Usage Guidelines: #### Industry Classification Combination Rules: - **industry_lv1=-1 (All)**: When selecting all primary industries, industry_lv2 parameter will be ignored, no need to set - **industry_lv1=specific value**: When selecting specific primary industry, can be combined with industry_lv2 for secondary filtering     - industry_lv2=-1: All secondary categories under the primary industry     - industry_lv2=specific value: Specific secondary category under the primary industry  #### Optional Parameters (No need to pass when selecting \"All\"): - **platform_channel**: Not passing means all platform channels - **pay_type**: Not passing means all payment types - **greater_than_cost_progress**: Not passing means no cost progress restriction - **publish_time_start**: Not passing means no publish time restriction - **quick_selector_scene**: Not passing means no quick filtering - **keyword**: Not passing means no keyword search  ### Parameter Details: - cursor: Cursor for pagination, 0 for first page - limit: Number of tasks per page, recommended 24 - mission_type: Mission type, usually 1 - tab_scene: Scene type     - 1: Submittable (tasks that can be submitted directly)     - 2: Registrable (tasks that require registration and approval)     - 3: Product Review (product evaluation tasks) - industry_lv1/lv2: Industry classification (recommend calling fetch_industry_category_config first)     - -1: All industries     - Specific values: Corresponding to specific industry categories (e.g., 1913=Gaming, 1903=Food&Beverage) - platform_channel: Platform channel (optional)     - 1: Douyin Video     - 2: Douyin Live     - 3: Douyin Image&Text - pay_type: Payment type (optional)     - 1: Video Level (pricing by follower level)     - 2: Custom (merchant custom pricing)     - 3: Conversion-based (pay by conversion effect)     - 4: Valid Views (pay by view count)     - 5: Sales Volume (pay by product sales)     - 9: Verification Volume (pay by verification count)     - 14: Commission-based (pay by commission ratio) - greater_than_cost_progress: Cost progress filter (optional)     - 20: Tasks with more than 20% cost progress     - 50: Tasks with more than 50% cost progress     - 80: Tasks with more than 80% cost progress - publish_time_start: Publish start time filter (optional, timestamp format) - quick_selector_scene: Quick filter scene (optional)     - 1: High revenue tasks     - 4: Guaranteed income tasks     - 5: Previously collaborated merchants - keyword: Keyword search (optional, supports task name or task ID)  ### Usage Examples: ``` # Get submittable tasks from all industries GET /fetch_mission_task_list?industry_lv1=-1&tab_scene=1  # Get tasks from gaming industry casual games category with view-based payment GET /fetch_mission_task_list?industry_lv1=1913&industry_lv2=191301&pay_type=4  # Get high-revenue Douyin video tasks GET /fetch_mission_task_list?platform_channel=1&quick_selector_scene=1 ```  ### Return: - Returns mission task list matching the conditions - Contains task details, compensation info, requirements, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cursor: 游标/Cursor (分页)
        :param object limit: 每页数量/Items per page
        :param object mission_type: 任务类型/Mission type
        :param object tab_scene: 场景类型/Scene type (1=可投稿, 2=可报名, 3=好物测评)
        :param object industry_lv1: 一级行业/Primary industry (-1=全部)
        :param object industry_lv2: 二级行业/Secondary industry (-1=全部)
        :param object platform_channel: 平台渠道/Platform channel (1=抖音视频, 2=抖音直播, 3=抖音图文)
        :param object pay_type: 付费类型/Pay type (1=视频等级, 2=自定义, 3=按转化付费, 4=按有效播放量, 5=按销售量, 9=按核销量, 14=按付费分佣)
        :param object greater_than_cost_progress: 成本进度/Cost progress (20=高于20%, 50=高于50%, 80=高于80%)
        :param object publish_time_start: 发布开始时间/Publish start time (时间戳)
        :param object quick_selector_scene: 快速选择场景/Quick selector (1=高收益, 4=保底收入, 5=合作过)
        :param object keyword: 关键词/Keyword (任务名称或ID)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取商单任务列表/Get mission task list  # noqa: E501

        # [中文] ### 用途: - 获取抖音创作者平台的商单任务列表 - 支持多种筛选条件，包括行业分类、付费类型、平台渠道等  ### 重要参数使用说明: #### 行业分类组合规则: - **industry_lv1=-1 (全部)**: 当选择全部一级行业时，industry_lv2参数将被忽略，无需设置 - **industry_lv1=具体值**: 当选择具体一级行业时，可配合industry_lv2进行二级筛选     - industry_lv2=-1: 该一级行业下的所有二级分类     - industry_lv2=具体值: 该一级行业下的具体二级分类  #### 可选参数 (选择\"全部\"时无需传入): - **platform_channel**: 不传入表示全部平台渠道 - **pay_type**: 不传入表示全部付费类型 - **greater_than_cost_progress**: 不传入表示不限制成本进度 - **publish_time_start**: 不传入表示不限制发布时间 - **quick_selector_scene**: 不传入表示不使用快速筛选 - **keyword**: 不传入表示不进行关键词搜索  ### 参数详解: - cursor: 游标，用于分页，0表示第一页 - limit: 每页返回的任务数量，建议24 - mission_type: 任务类型，通常为1 - tab_scene: 场景类型     - 1: 可投稿 (可以直接投稿的任务)     - 2: 可报名 (需要报名审核的任务)     - 3: 好物测评 (商品测评类任务) - industry_lv1/lv2: 行业分类 (建议先调用fetch_industry_category_config获取完整分类)     - -1: 全部行业     - 具体数值: 对应具体行业类别 (如1913=游戏, 1903=食品饮料) - platform_channel: 平台渠道 (可选)     - 1: 抖音视频     - 2: 抖音直播     - 3: 抖音图文 - pay_type: 付费类型 (可选)     - 1: 视频等级 (按粉丝量等级定价)     - 2: 自定义 (商家自定义价格)     - 3: 按转化付费 (按转化效果付费)     - 4: 按有效播放量 (按播放量付费)     - 5: 按销售量 (按商品销售量付费)     - 9: 按核销量 (按核销数量付费)     - 14: 按付费分佣 (按分佣比例付费) - greater_than_cost_progress: 成本进度筛选 (可选)     - 20: 高于20%成本进度的任务     - 50: 高于50%成本进度的任务     - 80: 高于80%成本进度的任务 - publish_time_start: 发布开始时间过滤 (可选，时间戳格式) - quick_selector_scene: 快速筛选场景 (可选)     - 1: 高收益任务     - 4: 保底收入任务     - 5: 曾经合作过的商家 - keyword: 关键词搜索 (可选，支持任务名称或任务ID)  ### 使用示例: ``` # 获取全部行业的可投稿任务 GET /fetch_mission_task_list?industry_lv1=-1&tab_scene=1  # 获取游戏行业休闲游戏分类的按播放量付费任务 GET /fetch_mission_task_list?industry_lv1=1913&industry_lv2=191301&pay_type=4  # 获取高收益的抖音视频任务 GET /fetch_mission_task_list?platform_channel=1&quick_selector_scene=1 ```  ### 返回: - 返回符合条件的商单任务列表 - 包含任务详情、报酬信息、要求等  # [English] ### Purpose: - Get mission task list from Douyin Creator platform - Supports multiple filtering conditions including industry classification, payment type, platform channel, etc.  ### Important Parameter Usage Guidelines: #### Industry Classification Combination Rules: - **industry_lv1=-1 (All)**: When selecting all primary industries, industry_lv2 parameter will be ignored, no need to set - **industry_lv1=specific value**: When selecting specific primary industry, can be combined with industry_lv2 for secondary filtering     - industry_lv2=-1: All secondary categories under the primary industry     - industry_lv2=specific value: Specific secondary category under the primary industry  #### Optional Parameters (No need to pass when selecting \"All\"): - **platform_channel**: Not passing means all platform channels - **pay_type**: Not passing means all payment types - **greater_than_cost_progress**: Not passing means no cost progress restriction - **publish_time_start**: Not passing means no publish time restriction - **quick_selector_scene**: Not passing means no quick filtering - **keyword**: Not passing means no keyword search  ### Parameter Details: - cursor: Cursor for pagination, 0 for first page - limit: Number of tasks per page, recommended 24 - mission_type: Mission type, usually 1 - tab_scene: Scene type     - 1: Submittable (tasks that can be submitted directly)     - 2: Registrable (tasks that require registration and approval)     - 3: Product Review (product evaluation tasks) - industry_lv1/lv2: Industry classification (recommend calling fetch_industry_category_config first)     - -1: All industries     - Specific values: Corresponding to specific industry categories (e.g., 1913=Gaming, 1903=Food&Beverage) - platform_channel: Platform channel (optional)     - 1: Douyin Video     - 2: Douyin Live     - 3: Douyin Image&Text - pay_type: Payment type (optional)     - 1: Video Level (pricing by follower level)     - 2: Custom (merchant custom pricing)     - 3: Conversion-based (pay by conversion effect)     - 4: Valid Views (pay by view count)     - 5: Sales Volume (pay by product sales)     - 9: Verification Volume (pay by verification count)     - 14: Commission-based (pay by commission ratio) - greater_than_cost_progress: Cost progress filter (optional)     - 20: Tasks with more than 20% cost progress     - 50: Tasks with more than 50% cost progress     - 80: Tasks with more than 80% cost progress - publish_time_start: Publish start time filter (optional, timestamp format) - quick_selector_scene: Quick filter scene (optional)     - 1: High revenue tasks     - 4: Guaranteed income tasks     - 5: Previously collaborated merchants - keyword: Keyword search (optional, supports task name or task ID)  ### Usage Examples: ``` # Get submittable tasks from all industries GET /fetch_mission_task_list?industry_lv1=-1&tab_scene=1  # Get tasks from gaming industry casual games category with view-based payment GET /fetch_mission_task_list?industry_lv1=1913&industry_lv2=191301&pay_type=4  # Get high-revenue Douyin video tasks GET /fetch_mission_task_list?platform_channel=1&quick_selector_scene=1 ```  ### Return: - Returns mission task list matching the conditions - Contains task details, compensation info, requirements, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cursor: 游标/Cursor (分页)
        :param object limit: 每页数量/Items per page
        :param object mission_type: 任务类型/Mission type
        :param object tab_scene: 场景类型/Scene type (1=可投稿, 2=可报名, 3=好物测评)
        :param object industry_lv1: 一级行业/Primary industry (-1=全部)
        :param object industry_lv2: 二级行业/Secondary industry (-1=全部)
        :param object platform_channel: 平台渠道/Platform channel (1=抖音视频, 2=抖音直播, 3=抖音图文)
        :param object pay_type: 付费类型/Pay type (1=视频等级, 2=自定义, 3=按转化付费, 4=按有效播放量, 5=按销售量, 9=按核销量, 14=按付费分佣)
        :param object greater_than_cost_progress: 成本进度/Cost progress (20=高于20%, 50=高于50%, 80=高于80%)
        :param object publish_time_start: 发布开始时间/Publish start time (时间戳)
        :param object quick_selector_scene: 快速选择场景/Quick selector (1=高收益, 4=保底收入, 5=合作过)
        :param object keyword: 关键词/Keyword (任务名称或ID)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cursor', 'limit', 'mission_type', 'tab_scene', 'industry_lv1', 'industry_lv2', 'platform_channel', 'pay_type', 'greater_than_cost_progress', 'publish_time_start', 'quick_selector_scene', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'mission_type' in params:
            query_params.append(('mission_type', params['mission_type']))  # noqa: E501
        if 'tab_scene' in params:
            query_params.append(('tab_scene', params['tab_scene']))  # noqa: E501
        if 'industry_lv1' in params:
            query_params.append(('industry_lv1', params['industry_lv1']))  # noqa: E501
        if 'industry_lv2' in params:
            query_params.append(('industry_lv2', params['industry_lv2']))  # noqa: E501
        if 'platform_channel' in params:
            query_params.append(('platform_channel', params['platform_channel']))  # noqa: E501
        if 'pay_type' in params:
            query_params.append(('pay_type', params['pay_type']))  # noqa: E501
        if 'greater_than_cost_progress' in params:
            query_params.append(('greater_than_cost_progress', params['greater_than_cost_progress']))  # noqa: E501
        if 'publish_time_start' in params:
            query_params.append(('publish_time_start', params['publish_time_start']))  # noqa: E501
        if 'quick_selector_scene' in params:
            query_params.append(('quick_selector_scene', params['quick_selector_scene']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_mission_task_list', 'GET',
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

    def fetch_user_search_api_v1_douyin_creator_fetch_user_search_get(self, user_name, **kwargs):  # noqa: E501
        """搜索用户/Search users  # noqa: E501

        # [中文] ### 用途: - 搜索抖音用户，支持抖音号和抖音昵称搜索 ### 参数: - user_name: 用户名 (支持抖音号和抖音昵称)     - 抖音号: 如 \"rmrbxmt\"     - 抖音昵称: 如 \"Y\"、\"人民日报\" ### 返回: - 最多返回20个匹配的用户信息 - 包含用户基本信息如头像、昵称、抖音号等  # [English] ### Purpose: - Search Douyin users by Douyin ID or nickname ### Parameters: - user_name: Username (supports Douyin ID and nickname)     - Douyin ID: e.g., \"rmrbxmt\"     - Nickname: e.g., \"Y\", \"人民日报\" ### Return: - Returns up to 20 matching user information - Contains basic user info like avatar, nickname, Douyin ID, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_api_v1_douyin_creator_fetch_user_search_get(user_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_name: 用户名/Username (支持抖音号和抖音昵称) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_search_api_v1_douyin_creator_fetch_user_search_get_with_http_info(user_name, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_search_api_v1_douyin_creator_fetch_user_search_get_with_http_info(user_name, **kwargs)  # noqa: E501
            return data

    def fetch_user_search_api_v1_douyin_creator_fetch_user_search_get_with_http_info(self, user_name, **kwargs):  # noqa: E501
        """搜索用户/Search users  # noqa: E501

        # [中文] ### 用途: - 搜索抖音用户，支持抖音号和抖音昵称搜索 ### 参数: - user_name: 用户名 (支持抖音号和抖音昵称)     - 抖音号: 如 \"rmrbxmt\"     - 抖音昵称: 如 \"Y\"、\"人民日报\" ### 返回: - 最多返回20个匹配的用户信息 - 包含用户基本信息如头像、昵称、抖音号等  # [English] ### Purpose: - Search Douyin users by Douyin ID or nickname ### Parameters: - user_name: Username (supports Douyin ID and nickname)     - Douyin ID: e.g., \"rmrbxmt\"     - Nickname: e.g., \"Y\", \"人民日报\" ### Return: - Returns up to 20 matching user information - Contains basic user info like avatar, nickname, Douyin ID, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_api_v1_douyin_creator_fetch_user_search_get_with_http_info(user_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_name: 用户名/Username (支持抖音号和抖音昵称) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_search_api_v1_douyin_creator_fetch_user_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_name' is set
        if self.api_client.client_side_validation and ('user_name' not in params or
                                                       params['user_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_name` when calling `fetch_user_search_api_v1_douyin_creator_fetch_user_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in params:
            query_params.append(('user_name', params['user_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_user_search', 'GET',
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

    def fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get(self, item_id, **kwargs):  # noqa: E501
        """获取作品弹幕列表/Get video danmaku list  # noqa: E501

        # [中文] ### 用途: - 获取指定作品的弹幕列表，支持管理和筛选弹幕 ### 参数: - item_id: 作品ID (必需参数，从作品链接或API获取) - count: 每页弹幕数量 (建议20，范围1-100) - offset: 偏移量 (分页使用，起始位置) - order_type: 排序类型 (1=时间排序, 2=其他排序) - is_blocked: 是否获取被屏蔽的弹幕 (false=正常弹幕, true=被屏蔽弹幕) ### 返回: - 作品弹幕列表数据  # [English] ### Purpose: - Get danmaku list for specified video, supports management and filtering ### Parameters: - item_id: Video item ID (required, get from video link or API) - count: Items per page (recommended 20, range 1-100) - offset: Offset (for pagination, starting position) - order_type: Order type (1=time order, 2=other order) - is_blocked: Whether to get blocked danmaku (false=normal, true=blocked) ### Return: - Video danmaku list data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品ID/Video item ID (required)
        :param object count: 每页数量/Items per page
        :param object offset: 偏移量/Offset (starting position)
        :param object order_type: 排序类型/Order type (1=时间排序, 2=其他排序)
        :param object is_blocked: 是否被屏蔽/Is blocked
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get_with_http_info(item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get_with_http_info(item_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get_with_http_info(self, item_id, **kwargs):  # noqa: E501
        """获取作品弹幕列表/Get video danmaku list  # noqa: E501

        # [中文] ### 用途: - 获取指定作品的弹幕列表，支持管理和筛选弹幕 ### 参数: - item_id: 作品ID (必需参数，从作品链接或API获取) - count: 每页弹幕数量 (建议20，范围1-100) - offset: 偏移量 (分页使用，起始位置) - order_type: 排序类型 (1=时间排序, 2=其他排序) - is_blocked: 是否获取被屏蔽的弹幕 (false=正常弹幕, true=被屏蔽弹幕) ### 返回: - 作品弹幕列表数据  # [English] ### Purpose: - Get danmaku list for specified video, supports management and filtering ### Parameters: - item_id: Video item ID (required, get from video link or API) - count: Items per page (recommended 20, range 1-100) - offset: Offset (for pagination, starting position) - order_type: Order type (1=time order, 2=other order) - is_blocked: Whether to get blocked danmaku (false=normal, true=blocked) ### Return: - Video danmaku list data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get_with_http_info(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品ID/Video item ID (required)
        :param object count: 每页数量/Items per page
        :param object offset: 偏移量/Offset (starting position)
        :param object order_type: 排序类型/Order type (1=时间排序, 2=其他排序)
        :param object is_blocked: 是否被屏蔽/Is blocked
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'count', 'offset', 'order_type', 'is_blocked']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'order_type' in params:
            query_params.append(('order_type', params['order_type']))  # noqa: E501
        if 'is_blocked' in params:
            query_params.append(('is_blocked', params['is_blocked']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/creator/fetch_video_danmaku_list', 'GET',
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
