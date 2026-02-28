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


class DouyinWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def douyin_live_room_api_v1_douyin_web_douyin_live_room_get(self, live_room_url, danmaku_type, **kwargs):  # noqa: E501
        """提取直播间弹幕/Extract live room danmaku  # noqa: E501

        # [中文] ### 用途: - 提取直播间弹幕 - 该接口已不再提供线上服务，需要自行购买源代码后在本地部署使用，购买源代码请在Discord服务器联系管理员，Discord邀请链接：https://discord.gg/aMEAS8Xsvz #### 价格: - 每10条数据消耗0.001$，支持阶梯式计费折扣。 ### 参数: - live_room_url: 直播间链接 - danmaku_type: 消息类型     - WebcastRoomMessage：直播间消息     - WebcastLikeMessage：点赞消息     - WebcastMemberMessage：成员消息     - WebcastChatMessage：聊天消息     - WebcastGiftMessage：礼物消息     - WebcastSocialMessage：社交消息     - WebcastRoomUserSeqMessage：用户序列消息     - WebcastUpdateFanTicketMessage：更新粉丝消息     - WebcastCommonTextMessage：常规文本消息     - WebcastMatchAgainstScoreMessage：比赛得分消息     - WebcastFansclubMessage：粉丝俱乐部消息     - WebcastRanklistHourEntranceMessage：排行榜小时入口消息     - WebcastRoomStatsMessage：直播间统计消息     - WebcastLiveShoppingMessage: 直播购物消息     - WebcastLiveEcomGeneralMessage: 直播电商通用消息     - WebcastProductChangeMessage: 直播商品变更消息     - WebcastRoomStreamAdaptationMessage: 直播间流适配消息     - WebcastNotifyEffectMessage: 通知效果消息     - WebcastLightGiftMessage: 亮礼物消息     - WebcastProfitInteractionScoreMessage: 收益互动分消息     - WebcastRoomRankMessage: 直播间排行消息 ### 返回: - 弹幕数据的WebSocket连接信息，需要使用WebSocket连接获取弹幕数据，此接口不返回弹幕数据。  # [English] ### Purpose: - Extract live room danmaku - This interface is no longer available online, you need to purchase the source code and deploy it locally for use. To purchase the source code, please contact the administrator in the Discord server. Discord invite link: https://discord.gg/aMEAS8Xsvz #### Price: - 0.001$ per 10 data, support tiered billing discounts. ### Parameters: - live_room_url: Live room link - danmaku_type: Message type     - WebcastRoomMessage: Live room message     - WebcastLikeMessage: Like message     - WebcastMemberMessage: Member message     - WebcastChatMessage: Chat message     - WebcastGiftMessage: Gift message     - WebcastSocialMessage: Social message     - WebcastRoomUserSeqMessage: User sequence message     - WebcastUpdateFanTicketMessage: Update fan message     - WebcastCommonTextMessage: Common text message     - WebcastMatchAgainstScoreMessage: Match score message     - WebcastFansclubMessage: Fans club message     - WebcastRanklistHourEntranceMessage: Ranking list hour entrance message     - WebcastRoomStatsMessage: Live room statistics message     - WebcastLiveShoppingMessage: Live shopping message     - WebcastLiveEcomGeneralMessage: Live e-commerce general message     - WebcastProductChangeMessage: Live product change message     - WebcastRoomStreamAdaptationMessage: Live room stream adaptation message     - WebcastNotifyEffectMessage: Notification effect message     - WebcastLightGiftMessage: Light gift message     - WebcastProfitInteractionScoreMessage: Profit interaction score message     - WebcastRoomRankMessage: Live room ranking message ### Return: - WebSocket connection information of the danmaku data, you need to use WebSocket connection to get the danmaku data, this interface does not return the danmaku data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.douyin_live_room_api_v1_douyin_web_douyin_live_room_get(live_room_url, danmaku_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object live_room_url: 直播间链接/Live room link (required)
        :param object danmaku_type: 消息类型/Message type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.douyin_live_room_api_v1_douyin_web_douyin_live_room_get_with_http_info(live_room_url, danmaku_type, **kwargs)  # noqa: E501
        else:
            (data) = self.douyin_live_room_api_v1_douyin_web_douyin_live_room_get_with_http_info(live_room_url, danmaku_type, **kwargs)  # noqa: E501
            return data

    def douyin_live_room_api_v1_douyin_web_douyin_live_room_get_with_http_info(self, live_room_url, danmaku_type, **kwargs):  # noqa: E501
        """提取直播间弹幕/Extract live room danmaku  # noqa: E501

        # [中文] ### 用途: - 提取直播间弹幕 - 该接口已不再提供线上服务，需要自行购买源代码后在本地部署使用，购买源代码请在Discord服务器联系管理员，Discord邀请链接：https://discord.gg/aMEAS8Xsvz #### 价格: - 每10条数据消耗0.001$，支持阶梯式计费折扣。 ### 参数: - live_room_url: 直播间链接 - danmaku_type: 消息类型     - WebcastRoomMessage：直播间消息     - WebcastLikeMessage：点赞消息     - WebcastMemberMessage：成员消息     - WebcastChatMessage：聊天消息     - WebcastGiftMessage：礼物消息     - WebcastSocialMessage：社交消息     - WebcastRoomUserSeqMessage：用户序列消息     - WebcastUpdateFanTicketMessage：更新粉丝消息     - WebcastCommonTextMessage：常规文本消息     - WebcastMatchAgainstScoreMessage：比赛得分消息     - WebcastFansclubMessage：粉丝俱乐部消息     - WebcastRanklistHourEntranceMessage：排行榜小时入口消息     - WebcastRoomStatsMessage：直播间统计消息     - WebcastLiveShoppingMessage: 直播购物消息     - WebcastLiveEcomGeneralMessage: 直播电商通用消息     - WebcastProductChangeMessage: 直播商品变更消息     - WebcastRoomStreamAdaptationMessage: 直播间流适配消息     - WebcastNotifyEffectMessage: 通知效果消息     - WebcastLightGiftMessage: 亮礼物消息     - WebcastProfitInteractionScoreMessage: 收益互动分消息     - WebcastRoomRankMessage: 直播间排行消息 ### 返回: - 弹幕数据的WebSocket连接信息，需要使用WebSocket连接获取弹幕数据，此接口不返回弹幕数据。  # [English] ### Purpose: - Extract live room danmaku - This interface is no longer available online, you need to purchase the source code and deploy it locally for use. To purchase the source code, please contact the administrator in the Discord server. Discord invite link: https://discord.gg/aMEAS8Xsvz #### Price: - 0.001$ per 10 data, support tiered billing discounts. ### Parameters: - live_room_url: Live room link - danmaku_type: Message type     - WebcastRoomMessage: Live room message     - WebcastLikeMessage: Like message     - WebcastMemberMessage: Member message     - WebcastChatMessage: Chat message     - WebcastGiftMessage: Gift message     - WebcastSocialMessage: Social message     - WebcastRoomUserSeqMessage: User sequence message     - WebcastUpdateFanTicketMessage: Update fan message     - WebcastCommonTextMessage: Common text message     - WebcastMatchAgainstScoreMessage: Match score message     - WebcastFansclubMessage: Fans club message     - WebcastRanklistHourEntranceMessage: Ranking list hour entrance message     - WebcastRoomStatsMessage: Live room statistics message     - WebcastLiveShoppingMessage: Live shopping message     - WebcastLiveEcomGeneralMessage: Live e-commerce general message     - WebcastProductChangeMessage: Live product change message     - WebcastRoomStreamAdaptationMessage: Live room stream adaptation message     - WebcastNotifyEffectMessage: Notification effect message     - WebcastLightGiftMessage: Light gift message     - WebcastProfitInteractionScoreMessage: Profit interaction score message     - WebcastRoomRankMessage: Live room ranking message ### Return: - WebSocket connection information of the danmaku data, you need to use WebSocket connection to get the danmaku data, this interface does not return the danmaku data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.douyin_live_room_api_v1_douyin_web_douyin_live_room_get_with_http_info(live_room_url, danmaku_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object live_room_url: 直播间链接/Live room link (required)
        :param object danmaku_type: 消息类型/Message type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['live_room_url', 'danmaku_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method douyin_live_room_api_v1_douyin_web_douyin_live_room_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'live_room_url' is set
        if self.api_client.client_side_validation and ('live_room_url' not in params or
                                                       params['live_room_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `live_room_url` when calling `douyin_live_room_api_v1_douyin_web_douyin_live_room_get`")  # noqa: E501
        # verify the required parameter 'danmaku_type' is set
        if self.api_client.client_side_validation and ('danmaku_type' not in params or
                                                       params['danmaku_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `danmaku_type` when calling `douyin_live_room_api_v1_douyin_web_douyin_live_room_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'live_room_url' in params:
            query_params.append(('live_room_url', params['live_room_url']))  # noqa: E501
        if 'danmaku_type' in params:
            query_params.append(('danmaku_type', params['danmaku_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/douyin_live_room', 'GET',
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

    def encrypt_uid_to_sec_user_id_api_v1_douyin_web_encrypt_uid_to_sec_user_id_get(self, uid, **kwargs):  # noqa: E501
        """加密用户uid到sec_user_id/Encrypt user uid to sec_user_id  # noqa: E501

        # [中文] ### 用途: - 加密用户uid到sec_user_id ### 参数: - uid: 用户uid，也就是抖音号的short_id ### 返回: - 用户信息  # [English] ### Purpose: - Encrypt user uid to sec_user_id ### Parameters: - uid: User uid, which is the short_id of the Douyin number ### Return: - User information  # [示例/Example] uid = \"1673937488185292\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.encrypt_uid_to_sec_user_id_api_v1_douyin_web_encrypt_uid_to_sec_user_id_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户uid(short_id)/User uid(short_id) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.encrypt_uid_to_sec_user_id_api_v1_douyin_web_encrypt_uid_to_sec_user_id_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.encrypt_uid_to_sec_user_id_api_v1_douyin_web_encrypt_uid_to_sec_user_id_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def encrypt_uid_to_sec_user_id_api_v1_douyin_web_encrypt_uid_to_sec_user_id_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """加密用户uid到sec_user_id/Encrypt user uid to sec_user_id  # noqa: E501

        # [中文] ### 用途: - 加密用户uid到sec_user_id ### 参数: - uid: 用户uid，也就是抖音号的short_id ### 返回: - 用户信息  # [English] ### Purpose: - Encrypt user uid to sec_user_id ### Parameters: - uid: User uid, which is the short_id of the Douyin number ### Return: - User information  # [示例/Example] uid = \"1673937488185292\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.encrypt_uid_to_sec_user_id_api_v1_douyin_web_encrypt_uid_to_sec_user_id_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户uid(short_id)/User uid(short_id) (required)
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
                    " to method encrypt_uid_to_sec_user_id_api_v1_douyin_web_encrypt_uid_to_sec_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `encrypt_uid_to_sec_user_id_api_v1_douyin_web_encrypt_uid_to_sec_user_id_get`")  # noqa: E501

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
            '/api/v1/douyin/web/encrypt_uid_to_sec_user_id', 'GET',
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

    def fetch_batch_user_profile_v1_api_v1_douyin_web_fetch_batch_user_profile_v1_get(self, sec_user_ids, **kwargs):  # noqa: E501
        """获取批量用户信息(最多10个)/Get batch user profile (up to 10)  # noqa: E501

        # [中文] ### 用途: - 获取批量用户信息，最多支持10个用户 ### 参数: - sec_user_ids: 用户sec_user_id列表，用逗号分隔，最多10个 ### 返回: - 批量用户信息  # [English] ### Purpose: - Get batch user profile, up to 10 users ### Parameters: - sec_user_ids: User sec_user_id list, separated by commas, up to 10 ### Return: - Batch user profile  # [示例/Example] sec_user_ids = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_batch_user_profile_v1_api_v1_douyin_web_fetch_batch_user_profile_v1_get(sec_user_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_ids: 用户sec_user_id列表，用逗号分隔/User sec_user_id list, separated by commas (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_batch_user_profile_v1_api_v1_douyin_web_fetch_batch_user_profile_v1_get_with_http_info(sec_user_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_batch_user_profile_v1_api_v1_douyin_web_fetch_batch_user_profile_v1_get_with_http_info(sec_user_ids, **kwargs)  # noqa: E501
            return data

    def fetch_batch_user_profile_v1_api_v1_douyin_web_fetch_batch_user_profile_v1_get_with_http_info(self, sec_user_ids, **kwargs):  # noqa: E501
        """获取批量用户信息(最多10个)/Get batch user profile (up to 10)  # noqa: E501

        # [中文] ### 用途: - 获取批量用户信息，最多支持10个用户 ### 参数: - sec_user_ids: 用户sec_user_id列表，用逗号分隔，最多10个 ### 返回: - 批量用户信息  # [English] ### Purpose: - Get batch user profile, up to 10 users ### Parameters: - sec_user_ids: User sec_user_id list, separated by commas, up to 10 ### Return: - Batch user profile  # [示例/Example] sec_user_ids = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_batch_user_profile_v1_api_v1_douyin_web_fetch_batch_user_profile_v1_get_with_http_info(sec_user_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_ids: 用户sec_user_id列表，用逗号分隔/User sec_user_id list, separated by commas (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_batch_user_profile_v1_api_v1_douyin_web_fetch_batch_user_profile_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_user_ids' is set
        if self.api_client.client_side_validation and ('sec_user_ids' not in params or
                                                       params['sec_user_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_ids` when calling `fetch_batch_user_profile_v1_api_v1_douyin_web_fetch_batch_user_profile_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_ids' in params:
            query_params.append(('sec_user_ids', params['sec_user_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_batch_user_profile_v1', 'GET',
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

    def fetch_batch_user_profile_v2_api_v1_douyin_web_fetch_batch_user_profile_v2_get(self, sec_user_ids, **kwargs):  # noqa: E501
        """获取批量用户信息(最多50个)/Get batch user profile (up to 50)  # noqa: E501

        # [中文] ### 用途: - 获取批量用户信息，最多支持50个用户 ### 参数: - sec_user_ids: 用户sec_user_id列表，用逗号分隔，最多50个 ### 返回: - 批量用户信息  # [English] ### Purpose: - Get batch user profile, up to 50 users ### Parameters: - sec_user_ids: User sec_user_id list, separated by commas, up to 50 ### Return: - Batch user profile  # [示例/Example] sec_user_ids = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_batch_user_profile_v2_api_v1_douyin_web_fetch_batch_user_profile_v2_get(sec_user_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_ids: 用户sec_user_id列表，用逗号分隔/User sec_user_id list, separated by commas (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_batch_user_profile_v2_api_v1_douyin_web_fetch_batch_user_profile_v2_get_with_http_info(sec_user_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_batch_user_profile_v2_api_v1_douyin_web_fetch_batch_user_profile_v2_get_with_http_info(sec_user_ids, **kwargs)  # noqa: E501
            return data

    def fetch_batch_user_profile_v2_api_v1_douyin_web_fetch_batch_user_profile_v2_get_with_http_info(self, sec_user_ids, **kwargs):  # noqa: E501
        """获取批量用户信息(最多50个)/Get batch user profile (up to 50)  # noqa: E501

        # [中文] ### 用途: - 获取批量用户信息，最多支持50个用户 ### 参数: - sec_user_ids: 用户sec_user_id列表，用逗号分隔，最多50个 ### 返回: - 批量用户信息  # [English] ### Purpose: - Get batch user profile, up to 50 users ### Parameters: - sec_user_ids: User sec_user_id list, separated by commas, up to 50 ### Return: - Batch user profile  # [示例/Example] sec_user_ids = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_batch_user_profile_v2_api_v1_douyin_web_fetch_batch_user_profile_v2_get_with_http_info(sec_user_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_ids: 用户sec_user_id列表，用逗号分隔/User sec_user_id list, separated by commas (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_batch_user_profile_v2_api_v1_douyin_web_fetch_batch_user_profile_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_user_ids' is set
        if self.api_client.client_side_validation and ('sec_user_ids' not in params or
                                                       params['sec_user_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_ids` when calling `fetch_batch_user_profile_v2_api_v1_douyin_web_fetch_batch_user_profile_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_ids' in params:
            query_params.append(('sec_user_ids', params['sec_user_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_batch_user_profile_v2', 'GET',
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

    def fetch_cartoon_aweme_api_v1_douyin_web_fetch_cartoon_aweme_get(self, count, **kwargs):  # noqa: E501
        """二次元作品推荐/Anime Video  # noqa: E501

        # [中文] ### 用途: - 二次元作品 ### 参数: - count: 每页数量，默认为16 - refresh_index: 翻页索引，默认为1 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### 返回: - 二次元作品数据  # [English] ### Purpose: - Cartoon Video ### Parameters: - count: Number per page, default is 16 - refresh_index: Paging index, default is 1 - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Cartoon Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cartoon_aweme_api_v1_douyin_web_fetch_cartoon_aweme_get(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 每页数量/Number per page (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_cartoon_aweme_api_v1_douyin_web_fetch_cartoon_aweme_get_with_http_info(count, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_cartoon_aweme_api_v1_douyin_web_fetch_cartoon_aweme_get_with_http_info(count, **kwargs)  # noqa: E501
            return data

    def fetch_cartoon_aweme_api_v1_douyin_web_fetch_cartoon_aweme_get_with_http_info(self, count, **kwargs):  # noqa: E501
        """二次元作品推荐/Anime Video  # noqa: E501

        # [中文] ### 用途: - 二次元作品 ### 参数: - count: 每页数量，默认为16 - refresh_index: 翻页索引，默认为1 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### 返回: - 二次元作品数据  # [English] ### Purpose: - Cartoon Video ### Parameters: - count: Number per page, default is 16 - refresh_index: Paging index, default is 1 - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Cartoon Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cartoon_aweme_api_v1_douyin_web_fetch_cartoon_aweme_get_with_http_info(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 每页数量/Number per page (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'refresh_index', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_cartoon_aweme_api_v1_douyin_web_fetch_cartoon_aweme_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'count' is set
        if self.api_client.client_side_validation and ('count' not in params or
                                                       params['count'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `count` when calling `fetch_cartoon_aweme_api_v1_douyin_web_fetch_cartoon_aweme_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'refresh_index' in params:
            query_params.append(('refresh_index', params['refresh_index']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_cartoon_aweme', 'GET',
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

    def fetch_cartoon_aweme_api_v1_douyin_web_fetch_food_aweme_get(self, count, **kwargs):  # noqa: E501
        """美食作品推荐/Food Video  # noqa: E501

        # [中文] ### 用途: - 美食作品 ### 参数: - count: 每页数量，默认为16 - refresh_index: 翻页索引，默认为1 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### 返回: - 美食作品数据  # [English] ### Purpose: - Food Video ### Parameters: - count: Number per page, default is 16 - refresh_index: Paging index, default is 1 - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Food Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cartoon_aweme_api_v1_douyin_web_fetch_food_aweme_get(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 每页数量/Number per page (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_cartoon_aweme_api_v1_douyin_web_fetch_food_aweme_get_with_http_info(count, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_cartoon_aweme_api_v1_douyin_web_fetch_food_aweme_get_with_http_info(count, **kwargs)  # noqa: E501
            return data

    def fetch_cartoon_aweme_api_v1_douyin_web_fetch_food_aweme_get_with_http_info(self, count, **kwargs):  # noqa: E501
        """美食作品推荐/Food Video  # noqa: E501

        # [中文] ### 用途: - 美食作品 ### 参数: - count: 每页数量，默认为16 - refresh_index: 翻页索引，默认为1 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### 返回: - 美食作品数据  # [English] ### Purpose: - Food Video ### Parameters: - count: Number per page, default is 16 - refresh_index: Paging index, default is 1 - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Food Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cartoon_aweme_api_v1_douyin_web_fetch_food_aweme_get_with_http_info(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 每页数量/Number per page (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'refresh_index', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_cartoon_aweme_api_v1_douyin_web_fetch_food_aweme_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'count' is set
        if self.api_client.client_side_validation and ('count' not in params or
                                                       params['count'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `count` when calling `fetch_cartoon_aweme_api_v1_douyin_web_fetch_food_aweme_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'refresh_index' in params:
            query_params.append(('refresh_index', params['refresh_index']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_food_aweme', 'GET',
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

    def fetch_cartoon_aweme_api_v1_douyin_web_fetch_music_aweme_get(self, count, **kwargs):  # noqa: E501
        """音乐作品推荐/Music Video  # noqa: E501

        # [中文] ### 用途: - 音乐作品 ### 参数: - count: 每页数量，默认为16 - refresh_index: 翻页索引，默认为1 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### 返回: - 音乐作品数据  # [English] ### Purpose: - Music Video ### Parameters: - count: Number per page, default is 16 - refresh_index: Paging index, default is 1 - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Music Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cartoon_aweme_api_v1_douyin_web_fetch_music_aweme_get(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 每页数量/Number per page (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_cartoon_aweme_api_v1_douyin_web_fetch_music_aweme_get_with_http_info(count, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_cartoon_aweme_api_v1_douyin_web_fetch_music_aweme_get_with_http_info(count, **kwargs)  # noqa: E501
            return data

    def fetch_cartoon_aweme_api_v1_douyin_web_fetch_music_aweme_get_with_http_info(self, count, **kwargs):  # noqa: E501
        """音乐作品推荐/Music Video  # noqa: E501

        # [中文] ### 用途: - 音乐作品 ### 参数: - count: 每页数量，默认为16 - refresh_index: 翻页索引，默认为1 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### 返回: - 音乐作品数据  # [English] ### Purpose: - Music Video ### Parameters: - count: Number per page, default is 16 - refresh_index: Paging index, default is 1 - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Music Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cartoon_aweme_api_v1_douyin_web_fetch_music_aweme_get_with_http_info(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 每页数量/Number per page (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'refresh_index', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_cartoon_aweme_api_v1_douyin_web_fetch_music_aweme_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'count' is set
        if self.api_client.client_side_validation and ('count' not in params or
                                                       params['count'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `count` when calling `fetch_cartoon_aweme_api_v1_douyin_web_fetch_music_aweme_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'refresh_index' in params:
            query_params.append(('refresh_index', params['refresh_index']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_music_aweme', 'GET',
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

    def fetch_challenge_posts_api_v1_douyin_web_fetch_challenge_posts_post(self, **kwargs):  # noqa: E501
        """话题作品/Challenge Posts  # noqa: E501

        # [中文] ### 用途: - 话题作品 ### 参数: - challenge_id: 话题id - sort_type: 排序类型     - 0:综合排序 1:最热排序 2:最新排序 - cursor: 游标 - count: 数量 - cookie: 用户自行提供的Cookie，用于获取更多数据。 ### 返回: - 话题作品  # [English] ### Purpose: - Challenge Posts ### Parameters: - challenge_id: Challenge id - sort_type: Sort type     - 0: Comprehensive sorting 1: Hottest sorting 2: Latest sorting - cursor: Cursor - count: Number - cookie: User provided Cookie, used to get more data ### Return: - Challenge Posts  # [示例/Example] challenge_id = \"1750525814851611\" sort_type = 0 offset = 0 cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_challenge_posts_api_v1_douyin_web_fetch_challenge_posts_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_challenge_posts_api_v1_douyin_web_fetch_challenge_posts_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_challenge_posts_api_v1_douyin_web_fetch_challenge_posts_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_challenge_posts_api_v1_douyin_web_fetch_challenge_posts_post_with_http_info(self, **kwargs):  # noqa: E501
        """话题作品/Challenge Posts  # noqa: E501

        # [中文] ### 用途: - 话题作品 ### 参数: - challenge_id: 话题id - sort_type: 排序类型     - 0:综合排序 1:最热排序 2:最新排序 - cursor: 游标 - count: 数量 - cookie: 用户自行提供的Cookie，用于获取更多数据。 ### 返回: - 话题作品  # [English] ### Purpose: - Challenge Posts ### Parameters: - challenge_id: Challenge id - sort_type: Sort type     - 0: Comprehensive sorting 1: Hottest sorting 2: Latest sorting - cursor: Cursor - count: Number - cookie: User provided Cookie, used to get more data ### Return: - Challenge Posts  # [示例/Example] challenge_id = \"1750525814851611\" sort_type = 0 offset = 0 cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_challenge_posts_api_v1_douyin_web_fetch_challenge_posts_post_with_http_info(async_req=True)
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
                    " to method fetch_challenge_posts_api_v1_douyin_web_fetch_challenge_posts_post" % key
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
            '/api/v1/douyin/web/fetch_challenge_posts', 'POST',
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

    def fetch_douyin_web_guest_cookie_api_v1_douyin_web_fetch_douyin_web_guest_cookie_get(self, user_agent, **kwargs):  # noqa: E501
        """获取抖音Web的游客Cookie/Get the guest Cookie of Douyin Web  # noqa: E501

        # [中文] ### 用途: - 获取抖音Web的游客Cookie - 可以用于爬取抖音Web的数据，如用户作品、合辑作品等。 - 可以固定身份避免部分接口重复数据。 - 请注意：游客Cookie无法爬取所有数据，有一定的限制。 - 可以配合开源项目使用此接口实现抖音Web的数据爬取。 ### 参数: - user_agent: 用户浏览器代理 ### 返回: - 游客Cookie  # [English] ### Purpose: - Get the guest Cookie of Douyin Web - Can be used to crawl data of Douyin Web, such as user videos, mix videos, etc. - Can fix identity to avoid duplicate data for some interfaces. - Please note: Guest Cookie cannot crawl all data, there are certain restrictions. - Can be used with open source projects to implement data crawling of Douyin Web using this interface. ### Parameters: - user_agent: User browser agent ### Return: - Guest Cookie  # [示例/Example] user_agent = \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_douyin_web_guest_cookie_api_v1_douyin_web_fetch_douyin_web_guest_cookie_get(user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_agent: 用户浏览器代理/User browser agent (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_douyin_web_guest_cookie_api_v1_douyin_web_fetch_douyin_web_guest_cookie_get_with_http_info(user_agent, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_douyin_web_guest_cookie_api_v1_douyin_web_fetch_douyin_web_guest_cookie_get_with_http_info(user_agent, **kwargs)  # noqa: E501
            return data

    def fetch_douyin_web_guest_cookie_api_v1_douyin_web_fetch_douyin_web_guest_cookie_get_with_http_info(self, user_agent, **kwargs):  # noqa: E501
        """获取抖音Web的游客Cookie/Get the guest Cookie of Douyin Web  # noqa: E501

        # [中文] ### 用途: - 获取抖音Web的游客Cookie - 可以用于爬取抖音Web的数据，如用户作品、合辑作品等。 - 可以固定身份避免部分接口重复数据。 - 请注意：游客Cookie无法爬取所有数据，有一定的限制。 - 可以配合开源项目使用此接口实现抖音Web的数据爬取。 ### 参数: - user_agent: 用户浏览器代理 ### 返回: - 游客Cookie  # [English] ### Purpose: - Get the guest Cookie of Douyin Web - Can be used to crawl data of Douyin Web, such as user videos, mix videos, etc. - Can fix identity to avoid duplicate data for some interfaces. - Please note: Guest Cookie cannot crawl all data, there are certain restrictions. - Can be used with open source projects to implement data crawling of Douyin Web using this interface. ### Parameters: - user_agent: User browser agent ### Return: - Guest Cookie  # [示例/Example] user_agent = \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_douyin_web_guest_cookie_api_v1_douyin_web_fetch_douyin_web_guest_cookie_get_with_http_info(user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_agent: 用户浏览器代理/User browser agent (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_douyin_web_guest_cookie_api_v1_douyin_web_fetch_douyin_web_guest_cookie_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_agent' is set
        if self.api_client.client_side_validation and ('user_agent' not in params or
                                                       params['user_agent'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_agent` when calling `fetch_douyin_web_guest_cookie_api_v1_douyin_web_fetch_douyin_web_guest_cookie_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_douyin_web_guest_cookie', 'GET',
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

    def fetch_game_aweme_api_v1_douyin_web_fetch_game_aweme_get(self, count, **kwargs):  # noqa: E501
        """游戏作品推荐/Game Video  # noqa: E501

        # [中文] ### 用途: - 知识作品 ### 参数: - count: 每页数量，默认为16 - refresh_index: 翻页索引，默认为1 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### 返回: - 游戏作品数据  # [English] ### Purpose: - Knowledge Video ### Parameters: - count: Number per page, default is 16 - refresh_index: Paging index, default is 1 - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Game Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_game_aweme_api_v1_douyin_web_fetch_game_aweme_get(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 每页数量/Number per page (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_game_aweme_api_v1_douyin_web_fetch_game_aweme_get_with_http_info(count, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_game_aweme_api_v1_douyin_web_fetch_game_aweme_get_with_http_info(count, **kwargs)  # noqa: E501
            return data

    def fetch_game_aweme_api_v1_douyin_web_fetch_game_aweme_get_with_http_info(self, count, **kwargs):  # noqa: E501
        """游戏作品推荐/Game Video  # noqa: E501

        # [中文] ### 用途: - 知识作品 ### 参数: - count: 每页数量，默认为16 - refresh_index: 翻页索引，默认为1 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### 返回: - 游戏作品数据  # [English] ### Purpose: - Knowledge Video ### Parameters: - count: Number per page, default is 16 - refresh_index: Paging index, default is 1 - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Game Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_game_aweme_api_v1_douyin_web_fetch_game_aweme_get_with_http_info(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 每页数量/Number per page (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'refresh_index', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_game_aweme_api_v1_douyin_web_fetch_game_aweme_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'count' is set
        if self.api_client.client_side_validation and ('count' not in params or
                                                       params['count'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `count` when calling `fetch_game_aweme_api_v1_douyin_web_fetch_game_aweme_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'refresh_index' in params:
            query_params.append(('refresh_index', params['refresh_index']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_game_aweme', 'GET',
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

    def fetch_general_search_result_api_v1_douyin_web_fetch_general_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212773e0 ### 用途: - 获取指定关键词的综合搜索结果，此接口有概率失败，如果失败请使用同样的参数重新请求 1-3次。 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212773e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年 - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上 -search_range: 0:不限 1:最近看过 2:还未看过 3:关注的人 -content_type: 0:不限 1:视频 2:图集 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 综合搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212773e0 ### Purpose: - Get comprehensive search results of specified keywords, this interface may fail, if it fails, please use the same parameters to request 1-3 times again. - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212773e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes - search_range: 0: Unlimited 1: Recently viewed 2: Not yet viewed 3: Followed - content_type: 0: Unlimited 1: Video 2: Album - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - Comprehensive search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = \"0\" publish_time = \"0\" filter_duration = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_general_search_result_api_v1_douyin_web_fetch_general_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object filter_duration: 视频时长/Duration filter
        :param object search_range: 搜索范围/Search range
        :param object content_type: 内容类型/Content type
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_general_search_result_api_v1_douyin_web_fetch_general_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_general_search_result_api_v1_douyin_web_fetch_general_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_general_search_result_api_v1_douyin_web_fetch_general_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212773e0 ### 用途: - 获取指定关键词的综合搜索结果，此接口有概率失败，如果失败请使用同样的参数重新请求 1-3次。 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212773e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 - sort_type: 0:综合排序 1:最多点赞 2:最新发布 - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年 - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上 -search_range: 0:不限 1:最近看过 2:还未看过 3:关注的人 -content_type: 0:不限 1:视频 2:图集 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 综合搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212773e0 ### Purpose: - Get comprehensive search results of specified keywords, this interface may fail, if it fails, please use the same parameters to request 1-3 times again. - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212773e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes - search_range: 0: Unlimited 1: Recently viewed 2: Not yet viewed 3: Followed - content_type: 0: Unlimited 1: Video 2: Album - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - Comprehensive search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = \"0\" publish_time = \"0\" filter_duration = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_general_search_result_api_v1_douyin_web_fetch_general_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object filter_duration: 视频时长/Duration filter
        :param object search_range: 搜索范围/Search range
        :param object content_type: 内容类型/Content type
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'sort_type', 'publish_time', 'filter_duration', 'search_range', 'content_type', 'search_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_general_search_result_api_v1_douyin_web_fetch_general_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_general_search_result_api_v1_douyin_web_fetch_general_search_result_get`")  # noqa: E501

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
        if 'search_range' in params:
            query_params.append(('search_range', params['search_range']))  # noqa: E501
        if 'content_type' in params:
            query_params.append(('content_type', params['content_type']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_general_search_result', 'GET',
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

    def fetch_home_feed_api_v1_douyin_web_fetch_home_feed_get(self, **kwargs):  # noqa: E501
        """获取首页推荐数据/Get home feed data  # noqa: E501

        # [中文] ### 用途: - 获取首页推荐数据 ### 参数: - count: 数量，默认为10，建议保持不变。 - refresh_index: 翻页索引，默认为0，然后每次增加1用于翻页。 ### 返回: - Feed数据  # [English] ### Purpose: - Get home feed data ### Parameters: - count: Number, default is 10, it is recommended to keep it unchanged. - refresh_index: Paging index, default is 0, then increase by 1 each time for paging. ### Return: - Feed data  # [示例/Example] count = 10 refresh_index = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_douyin_web_fetch_home_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 数量/Number
        :param object refresh_index: 翻页索引/Paging index
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_feed_api_v1_douyin_web_fetch_home_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_feed_api_v1_douyin_web_fetch_home_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_home_feed_api_v1_douyin_web_fetch_home_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取首页推荐数据/Get home feed data  # noqa: E501

        # [中文] ### 用途: - 获取首页推荐数据 ### 参数: - count: 数量，默认为10，建议保持不变。 - refresh_index: 翻页索引，默认为0，然后每次增加1用于翻页。 ### 返回: - Feed数据  # [English] ### Purpose: - Get home feed data ### Parameters: - count: Number, default is 10, it is recommended to keep it unchanged. - refresh_index: Paging index, default is 0, then increase by 1 each time for paging. ### Return: - Feed data  # [示例/Example] count = 10 refresh_index = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_douyin_web_fetch_home_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 数量/Number
        :param object refresh_index: 翻页索引/Paging index
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'refresh_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_home_feed_api_v1_douyin_web_fetch_home_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'refresh_index' in params:
            query_params.append(('refresh_index', params['refresh_index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_home_feed', 'GET',
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

    def fetch_hot_search_result_api_v1_douyin_web_fetch_hot_search_result_get(self, **kwargs):  # noqa: E501
        """获取抖音热榜数据/Get Douyin hot search results  # noqa: E501

        # [中文] ### 用途: - 获取抖音热榜数据 ### 返回: - 热榜数据  # [English] ### Purpose: - Get Douyin hot search results ### Return: - Hot search results  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_result_api_v1_douyin_web_fetch_hot_search_result_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_result_api_v1_douyin_web_fetch_hot_search_result_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_result_api_v1_douyin_web_fetch_hot_search_result_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_result_api_v1_douyin_web_fetch_hot_search_result_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取抖音热榜数据/Get Douyin hot search results  # noqa: E501

        # [中文] ### 用途: - 获取抖音热榜数据 ### 返回: - 热榜数据  # [English] ### Purpose: - Get Douyin hot search results ### Return: - Hot search results  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_result_api_v1_douyin_web_fetch_hot_search_result_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_search_result_api_v1_douyin_web_fetch_hot_search_result_get" % key
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
            '/api/v1/douyin/web/fetch_hot_search_result', 'GET',
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

    def fetch_knowledge_aweme_api_v1_douyin_web_fetch_knowledge_aweme_get(self, count, **kwargs):  # noqa: E501
        """知识作品推荐/Knowledge Video  # noqa: E501

        # [中文] ### 用途: - 知识作品 ### 参数: - count: 每页数量，默认为16 - refresh_index: 翻页索引，默认为1 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### 返回: - 知识作品数据  # [English] ### Purpose: - Knowledge Video ### Parameters: - count: Number per page, default is 16 - refresh_index: Paging index, default is 1 - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Knowledge Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_knowledge_aweme_api_v1_douyin_web_fetch_knowledge_aweme_get(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 每页数量/Number per page (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_knowledge_aweme_api_v1_douyin_web_fetch_knowledge_aweme_get_with_http_info(count, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_knowledge_aweme_api_v1_douyin_web_fetch_knowledge_aweme_get_with_http_info(count, **kwargs)  # noqa: E501
            return data

    def fetch_knowledge_aweme_api_v1_douyin_web_fetch_knowledge_aweme_get_with_http_info(self, count, **kwargs):  # noqa: E501
        """知识作品推荐/Knowledge Video  # noqa: E501

        # [中文] ### 用途: - 知识作品 ### 参数: - count: 每页数量，默认为16 - refresh_index: 翻页索引，默认为1 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### 返回: - 知识作品数据  # [English] ### Purpose: - Knowledge Video ### Parameters: - count: Number per page, default is 16 - refresh_index: Paging index, default is 1 - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Knowledge Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_knowledge_aweme_api_v1_douyin_web_fetch_knowledge_aweme_get_with_http_info(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 每页数量/Number per page (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'refresh_index', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_knowledge_aweme_api_v1_douyin_web_fetch_knowledge_aweme_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'count' is set
        if self.api_client.client_side_validation and ('count' not in params or
                                                       params['count'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `count` when calling `fetch_knowledge_aweme_api_v1_douyin_web_fetch_knowledge_aweme_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'refresh_index' in params:
            query_params.append(('refresh_index', params['refresh_index']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_knowledge_aweme', 'GET',
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

    def fetch_live_gift_ranking_api_v1_douyin_web_fetch_live_gift_ranking_get(self, room_id, **kwargs):  # noqa: E501
        """获取直播间送礼用户排行榜/Get live room gift user ranking  # noqa: E501

        # [中文] ### 用途: - 获取直播间送礼用户排行榜 ### 参数: - room_id: 直播间room_id - rank_type: 排行类型，默认为30不用修改。 ### 返回: - 排行榜数据  # [English] ### Purpose: - Get live room gift user ranking ### Parameters: - room_id: Room room_id - rank_type: Leaderboard type, default is 30, no need to modify. ### Return: - Leaderboard data  # [示例/Example] room_id = \"7356585666190461731\" rank_type = 30  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_gift_ranking_api_v1_douyin_web_fetch_live_gift_ranking_get(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间room_id/Room room_id (required)
        :param object rank_type: 排行类型/Leaderboard type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_gift_ranking_api_v1_douyin_web_fetch_live_gift_ranking_get_with_http_info(room_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_gift_ranking_api_v1_douyin_web_fetch_live_gift_ranking_get_with_http_info(room_id, **kwargs)  # noqa: E501
            return data

    def fetch_live_gift_ranking_api_v1_douyin_web_fetch_live_gift_ranking_get_with_http_info(self, room_id, **kwargs):  # noqa: E501
        """获取直播间送礼用户排行榜/Get live room gift user ranking  # noqa: E501

        # [中文] ### 用途: - 获取直播间送礼用户排行榜 ### 参数: - room_id: 直播间room_id - rank_type: 排行类型，默认为30不用修改。 ### 返回: - 排行榜数据  # [English] ### Purpose: - Get live room gift user ranking ### Parameters: - room_id: Room room_id - rank_type: Leaderboard type, default is 30, no need to modify. ### Return: - Leaderboard data  # [示例/Example] room_id = \"7356585666190461731\" rank_type = 30  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_gift_ranking_api_v1_douyin_web_fetch_live_gift_ranking_get_with_http_info(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间room_id/Room room_id (required)
        :param object rank_type: 排行类型/Leaderboard type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id', 'rank_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_gift_ranking_api_v1_douyin_web_fetch_live_gift_ranking_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_live_gift_ranking_api_v1_douyin_web_fetch_live_gift_ranking_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501
        if 'rank_type' in params:
            query_params.append(('rank_type', params['rank_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_live_gift_ranking', 'GET',
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

    def fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get(self, room_id, user_unique_id, **kwargs):  # noqa: E501
        """抖音直播间弹幕参数获取/Douyin live room danmaku parameters  # noqa: E501

        # [中文] ### 用途: - 抖音直播间弹幕参数获取 ### 参数: - room_id: 直播间号 - user_unique_id: 用户唯一ID  ### 返回: - 弹幕参数数据  # [English] ### Purpose: - Douyin live room danmaku parameters ### Parameters: - room_id: Live room id - user_unique_id: User unique ID  ### Return: - Danmaku parameter data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get(room_id, user_unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间号/Live room id (required)
        :param object user_unique_id: 用户唯一ID/User unique ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get_with_http_info(room_id, user_unique_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get_with_http_info(room_id, user_unique_id, **kwargs)  # noqa: E501
            return data

    def fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get_with_http_info(self, room_id, user_unique_id, **kwargs):  # noqa: E501
        """抖音直播间弹幕参数获取/Douyin live room danmaku parameters  # noqa: E501

        # [中文] ### 用途: - 抖音直播间弹幕参数获取 ### 参数: - room_id: 直播间号 - user_unique_id: 用户唯一ID  ### 返回: - 弹幕参数数据  # [English] ### Purpose: - Douyin live room danmaku parameters ### Parameters: - room_id: Live room id - user_unique_id: User unique ID  ### Return: - Danmaku parameter data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get_with_http_info(room_id, user_unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间号/Live room id (required)
        :param object user_unique_id: 用户唯一ID/User unique ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id', 'user_unique_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get`")  # noqa: E501
        # verify the required parameter 'user_unique_id' is set
        if self.api_client.client_side_validation and ('user_unique_id' not in params or
                                                       params['user_unique_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_unique_id` when calling `fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501
        if 'user_unique_id' in params:
            query_params.append(('user_unique_id', params['user_unique_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_live_im_fetch', 'GET',
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

    def fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get(self, room_id, author_id, **kwargs):  # noqa: E501
        """抖音直播间商品信息/Douyin live room product information  # noqa: E501

        # [中文] ### 用途: - 抖音直播间商品信息 ### 参数: - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie，如获取失败请手动过一次验证码) - room_id: 直播间room_id - author_id: 作者id - offset: 偏移量 - limit: 数量 ### 返回: - 商品信息 ### 备注: author_id的获取方法：     1. 通过用户的sec_user_id获取用户信息接口获取uid字段即为author_id。     2. 通过直播间room_id获取直播间信息接口获取author_id字段。 roon_id不是固定不变的，每次开播都会变化。  # [English] ### Purpose: - Douyin live room product information ### Parameters: - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie, if the acquisition fails, please manually pass the captcha code once) - room_id: Room room_id - author_id: Author id - offset: Offset - limit: Number ### Return: - Product information ### Note: The method to obtain author_id:     1. Obtain the uid field as author_id through the user information interface by sec_user_id.     2. Obtain the author_id field through the live room information interface by room_id. The roon_id is not fixed, it changes every time the live broadcast starts.  # [示例/Example] cookie = \"YOUR_COOKIE\" room_id = \"7356742011975715619\" author_id = \"2207432981615527\" offset = 0 limit = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get(room_id, author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间room_id/Room room_id (required)
        :param object author_id: 作者id/Author id (required)
        :param object offset: 偏移量/Offset
        :param object limit: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get_with_http_info(room_id, author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get_with_http_info(room_id, author_id, **kwargs)  # noqa: E501
            return data

    def fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get_with_http_info(self, room_id, author_id, **kwargs):  # noqa: E501
        """抖音直播间商品信息/Douyin live room product information  # noqa: E501

        # [中文] ### 用途: - 抖音直播间商品信息 ### 参数: - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie，如获取失败请手动过一次验证码) - room_id: 直播间room_id - author_id: 作者id - offset: 偏移量 - limit: 数量 ### 返回: - 商品信息 ### 备注: author_id的获取方法：     1. 通过用户的sec_user_id获取用户信息接口获取uid字段即为author_id。     2. 通过直播间room_id获取直播间信息接口获取author_id字段。 roon_id不是固定不变的，每次开播都会变化。  # [English] ### Purpose: - Douyin live room product information ### Parameters: - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie, if the acquisition fails, please manually pass the captcha code once) - room_id: Room room_id - author_id: Author id - offset: Offset - limit: Number ### Return: - Product information ### Note: The method to obtain author_id:     1. Obtain the uid field as author_id through the user information interface by sec_user_id.     2. Obtain the author_id field through the live room information interface by room_id. The roon_id is not fixed, it changes every time the live broadcast starts.  # [示例/Example] cookie = \"YOUR_COOKIE\" room_id = \"7356742011975715619\" author_id = \"2207432981615527\" offset = 0 limit = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get_with_http_info(room_id, author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间room_id/Room room_id (required)
        :param object author_id: 作者id/Author id (required)
        :param object offset: 偏移量/Offset
        :param object limit: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id', 'author_id', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get`")  # noqa: E501
        # verify the required parameter 'author_id' is set
        if self.api_client.client_side_validation and ('author_id' not in params or
                                                       params['author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `author_id` when calling `fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501
        if 'author_id' in params:
            query_params.append(('author_id', params['author_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_live_room_product_result', 'GET',
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

    def fetch_live_search_result_api_v1_douyin_web_fetch_live_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 获取指定关键词的直播搜索结果/Get live search results of specified keywords  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212789e0 ### 用途: - 获取指定关键词的直播搜索结果 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212789e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 ### 返回: - 直播搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212789e0 ### Purpose: - Get live search results of specified keywords - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212789e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number ### Return: - Live search results  # [示例/Example] keyword = \"动漫\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_search_result_api_v1_douyin_web_fetch_live_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_search_result_api_v1_douyin_web_fetch_live_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_search_result_api_v1_douyin_web_fetch_live_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_live_search_result_api_v1_douyin_web_fetch_live_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 获取指定关键词的直播搜索结果/Get live search results of specified keywords  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212789e0 ### 用途: - 获取指定关键词的直播搜索结果 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212789e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 ### 返回: - 直播搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212789e0 ### Purpose: - Get live search results of specified keywords - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212789e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number ### Return: - Live search results  # [示例/Example] keyword = \"动漫\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_search_result_api_v1_douyin_web_fetch_live_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'search_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_search_result_api_v1_douyin_web_fetch_live_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_live_search_result_api_v1_douyin_web_fetch_live_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_live_search_result', 'GET',
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

    def fetch_multi_video_api_v1_douyin_web_fetch_multi_video_post(self, **kwargs):  # noqa: E501
        """批量获取视频信息/Batch Get Video Information  # noqa: E501

        # [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持50个视频，此接口收费固定价格为0.001$ * 50 = 0.05$一次。 - 若此接口失效，请使用APP接口替代。 ### 参数: - aweme_ids: 作品id列表，最多支持50个作品id。 ### 返回: - 作品数据  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 50 videos at a time, this interface charges a fixed price of 0.001$ * 50 = 0.05$ each time. - If this interface fails, please use the APP interface instead. ### Parameters: - aweme_ids: List of video ids, up to 50 video ids are supported. ### Return: - Video data  # [示例/Example] aweme_ids = [\"7372484719365098803\", \"7126745726494821640\", \"7372484719365098803\", \"7126745726494821640\", \"7372484719365098803\", \"7126745726494821640\", \"7372484719365098803\", \"7126745726494821640\", \"7372484719365098803\", \"7126745726494821640\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_api_v1_douyin_web_fetch_multi_video_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_multi_video_api_v1_douyin_web_fetch_multi_video_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_multi_video_api_v1_douyin_web_fetch_multi_video_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_multi_video_api_v1_douyin_web_fetch_multi_video_post_with_http_info(self, **kwargs):  # noqa: E501
        """批量获取视频信息/Batch Get Video Information  # noqa: E501

        # [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持50个视频，此接口收费固定价格为0.001$ * 50 = 0.05$一次。 - 若此接口失效，请使用APP接口替代。 ### 参数: - aweme_ids: 作品id列表，最多支持50个作品id。 ### 返回: - 作品数据  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 50 videos at a time, this interface charges a fixed price of 0.001$ * 50 = 0.05$ each time. - If this interface fails, please use the APP interface instead. ### Parameters: - aweme_ids: List of video ids, up to 50 video ids are supported. ### Return: - Video data  # [示例/Example] aweme_ids = [\"7372484719365098803\", \"7126745726494821640\", \"7372484719365098803\", \"7126745726494821640\", \"7372484719365098803\", \"7126745726494821640\", \"7372484719365098803\", \"7126745726494821640\", \"7372484719365098803\", \"7126745726494821640\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_api_v1_douyin_web_fetch_multi_video_post_with_http_info(async_req=True)
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
                    " to method fetch_multi_video_api_v1_douyin_web_fetch_multi_video_post" % key
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
            '/api/v1/douyin/web/fetch_multi_video', 'POST',
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

    def fetch_multi_video_high_quality_play_url_api_v1_douyin_web_fetch_multi_video_high_quality_play_url_post(self, **kwargs):  # noqa: E501
        """批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos  # noqa: E501

        # [中文] ### 用途: - 此接口目前优惠活动价为$0.25，活动结束后恢复原价$0.5。不足50个视频按50个视频收费。 - 批量获取视频的最高画质(原始上传画质)播放链接 - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。 - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。 - 此接口非常适合用于批量获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。 - 使用并发请求，提高批量获取效率。 - 最多支持50个视频ID。 ### 参数: - aweme_ids: 作品id列表，用逗号分隔，例如: \"123,456,789\"，最多50个。 ### 返回: - total: 总数 - success_count: 成功数量 - failed_count: 失败数量 - videos: 视频列表，每个视频包含以下字段：     - video_id: 作品id     - original_video_url: 最高画质(原始上传画质)播放链接     - file_size: 文件大小（字节）     - file_size_in_mb: 文件大小（MB）     - content_type: 内容类型     - success: 是否成功     - error: 错误信息（如果失败） ### 备注: - 由于数量较多，处理时间可能会稍长，请增加等待时间。  # [English] ### Purpose: - This interface is currently on sale for $0.25, and will return to the original price of $0.5 after the event ends. If there are less than 50 videos, they will be charged as 50 videos. - Batch get the highest quality (original upload quality) play URL of videos - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata. - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface. - This interface is very suitable for batch obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc. - Use concurrent requests to improve batch acquisition efficiency. - Support up to 50 video IDs. ### Parameters: - aweme_ids: Video id list, separated by commas, for example: \"123,456,789\", up to 50. ### Return: - total: Total count - success_count: Success count - failed_count: Failed count - videos: Video list, each video contains the following fields:     - video_id: Video id     - original_video_url: Highest quality (original upload quality) play URL     - file_size: File size (bytes)     - file_size_in_mb: File size (MB)     - content_type: Content type     - success: Whether successful     - error: Error message (if failed) ### Note: - Due to the large number, the processing time may be slightly longer, please increase the waiting time. # [示例/Example] aweme_ids = \"7512756548356492544,7448118827402972455,7126745726494821640\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_high_quality_play_url_api_v1_douyin_web_fetch_multi_video_high_quality_play_url_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_multi_video_high_quality_play_url_api_v1_douyin_web_fetch_multi_video_high_quality_play_url_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_multi_video_high_quality_play_url_api_v1_douyin_web_fetch_multi_video_high_quality_play_url_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_multi_video_high_quality_play_url_api_v1_douyin_web_fetch_multi_video_high_quality_play_url_post_with_http_info(self, **kwargs):  # noqa: E501
        """批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos  # noqa: E501

        # [中文] ### 用途: - 此接口目前优惠活动价为$0.25，活动结束后恢复原价$0.5。不足50个视频按50个视频收费。 - 批量获取视频的最高画质(原始上传画质)播放链接 - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。 - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。 - 此接口非常适合用于批量获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。 - 使用并发请求，提高批量获取效率。 - 最多支持50个视频ID。 ### 参数: - aweme_ids: 作品id列表，用逗号分隔，例如: \"123,456,789\"，最多50个。 ### 返回: - total: 总数 - success_count: 成功数量 - failed_count: 失败数量 - videos: 视频列表，每个视频包含以下字段：     - video_id: 作品id     - original_video_url: 最高画质(原始上传画质)播放链接     - file_size: 文件大小（字节）     - file_size_in_mb: 文件大小（MB）     - content_type: 内容类型     - success: 是否成功     - error: 错误信息（如果失败） ### 备注: - 由于数量较多，处理时间可能会稍长，请增加等待时间。  # [English] ### Purpose: - This interface is currently on sale for $0.25, and will return to the original price of $0.5 after the event ends. If there are less than 50 videos, they will be charged as 50 videos. - Batch get the highest quality (original upload quality) play URL of videos - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata. - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface. - This interface is very suitable for batch obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc. - Use concurrent requests to improve batch acquisition efficiency. - Support up to 50 video IDs. ### Parameters: - aweme_ids: Video id list, separated by commas, for example: \"123,456,789\", up to 50. ### Return: - total: Total count - success_count: Success count - failed_count: Failed count - videos: Video list, each video contains the following fields:     - video_id: Video id     - original_video_url: Highest quality (original upload quality) play URL     - file_size: File size (bytes)     - file_size_in_mb: File size (MB)     - content_type: Content type     - success: Whether successful     - error: Error message (if failed) ### Note: - Due to the large number, the processing time may be slightly longer, please increase the waiting time. # [示例/Example] aweme_ids = \"7512756548356492544,7448118827402972455,7126745726494821640\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_high_quality_play_url_api_v1_douyin_web_fetch_multi_video_high_quality_play_url_post_with_http_info(async_req=True)
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
                    " to method fetch_multi_video_high_quality_play_url_api_v1_douyin_web_fetch_multi_video_high_quality_play_url_post" % key
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
            '/api/v1/douyin/web/fetch_multi_video_high_quality_play_url', 'POST',
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

    def fetch_one_video_api_v1_douyin_web_fetch_one_video_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 V1，若此接口失效，请使用 `/fetch_one_video_v2` 接口，或使用APP接口。 ### 参数: - aweme_id: 作品id - need_anchor_info: 是否需要锚点信息，默认为False，开启后会看到一些有关视频的锚点信息，如地理位置，商户信息，商品橱窗等，可能会增加接口响应时间。 - 如果不需要锚点信息，建议保持默认值False，如果接口报错，可以尝试关闭此参数。 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data V1, if this interface fails, please use the `/fetch_one_video_v2` interface, or use the APP interface. ### Parameters: - aweme_id: Video id - need_anchor_info: Whether anchor information is needed, default is False, enabling it will show some anchor information about the video, such as location, merchant information, product showcase, etc., which may increase the interface response time. - If anchor information is not needed, it is recommended to keep the default value False, if the interface reports an error, you can try to turn off this parameter. ### Return: - Video data  # [示例/Example] aweme_id = \"7372484719365098803\" need_anchor_info = False  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_douyin_web_fetch_one_video_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object need_anchor_info: 是否需要锚点信息/Whether anchor information is needed
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_douyin_web_fetch_one_video_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_douyin_web_fetch_one_video_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_douyin_web_fetch_one_video_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 V1，若此接口失效，请使用 `/fetch_one_video_v2` 接口，或使用APP接口。 ### 参数: - aweme_id: 作品id - need_anchor_info: 是否需要锚点信息，默认为False，开启后会看到一些有关视频的锚点信息，如地理位置，商户信息，商品橱窗等，可能会增加接口响应时间。 - 如果不需要锚点信息，建议保持默认值False，如果接口报错，可以尝试关闭此参数。 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data V1, if this interface fails, please use the `/fetch_one_video_v2` interface, or use the APP interface. ### Parameters: - aweme_id: Video id - need_anchor_info: Whether anchor information is needed, default is False, enabling it will show some anchor information about the video, such as location, merchant information, product showcase, etc., which may increase the interface response time. - If anchor information is not needed, it is recommended to keep the default value False, if the interface reports an error, you can try to turn off this parameter. ### Return: - Video data  # [示例/Example] aweme_id = \"7372484719365098803\" need_anchor_info = False  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_douyin_web_fetch_one_video_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object need_anchor_info: 是否需要锚点信息/Whether anchor information is needed
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id', 'need_anchor_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_api_v1_douyin_web_fetch_one_video_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_one_video_api_v1_douyin_web_fetch_one_video_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501
        if 'need_anchor_info' in params:
            query_params.append(('need_anchor_info', params['need_anchor_info']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_one_video', 'GET',
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

    def fetch_one_video_api_v1_douyin_web_fetch_one_video_v2_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 V2，若此接口失效，请使用 `/fetch_one_video` 接口，或使用APP接口。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data V2, if this interface fails, please use the `/fetch_one_video` interface, or use the APP interface. ### Parameters: - aweme_id: Video id ### Return: - Video data  # [示例/Example] aweme_id = \"7372484719365098803\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_douyin_web_fetch_one_video_v2_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_douyin_web_fetch_one_video_v2_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_douyin_web_fetch_one_video_v2_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_douyin_web_fetch_one_video_v2_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 V2，若此接口失效，请使用 `/fetch_one_video` 接口，或使用APP接口。 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data V2, if this interface fails, please use the `/fetch_one_video` interface, or use the APP interface. ### Parameters: - aweme_id: Video id ### Return: - Video data  # [示例/Example] aweme_id = \"7372484719365098803\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_douyin_web_fetch_one_video_v2_get_with_http_info(aweme_id, async_req=True)
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
                    " to method fetch_one_video_api_v1_douyin_web_fetch_one_video_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_one_video_api_v1_douyin_web_fetch_one_video_v2_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_one_video_v2', 'GET',
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

    def fetch_one_video_by_share_url_api_v1_douyin_web_fetch_one_video_by_share_url_get(self, share_url, **kwargs):  # noqa: E501
        """根据分享链接获取单个作品数据/Get single video data by sharing link  # noqa: E501

        # [中文] ### 用途: - 根据分享链接获取单个作品数据 （本质上基于 `/fetch_one_video` 接口实现，建议有能力自行获取视频ID以提升接口响应速度） - 返回的视频画质比APP接口高一些，但是响应字段没有APP接口多。 ### 参数: - share_url: 分享链接 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data by sharing link (Essentially implemented based on the `/fetch_one_video` interface, it is recommended to obtain the video ID by yourself to improve the interface response speed) - The returned video quality is higher than the APP interface, but the response fields are not as many as the APP interface. ### Parameters: - share_url: Share link ### Return: - Video data  # [示例/Example] share_url = \"https://v.douyin.com/e3x2fjE/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_url_api_v1_douyin_web_fetch_one_video_by_share_url_get(share_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_url: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_by_share_url_api_v1_douyin_web_fetch_one_video_by_share_url_get_with_http_info(share_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_by_share_url_api_v1_douyin_web_fetch_one_video_by_share_url_get_with_http_info(share_url, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_by_share_url_api_v1_douyin_web_fetch_one_video_by_share_url_get_with_http_info(self, share_url, **kwargs):  # noqa: E501
        """根据分享链接获取单个作品数据/Get single video data by sharing link  # noqa: E501

        # [中文] ### 用途: - 根据分享链接获取单个作品数据 （本质上基于 `/fetch_one_video` 接口实现，建议有能力自行获取视频ID以提升接口响应速度） - 返回的视频画质比APP接口高一些，但是响应字段没有APP接口多。 ### 参数: - share_url: 分享链接 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data by sharing link (Essentially implemented based on the `/fetch_one_video` interface, it is recommended to obtain the video ID by yourself to improve the interface response speed) - The returned video quality is higher than the APP interface, but the response fields are not as many as the APP interface. ### Parameters: - share_url: Share link ### Return: - Video data  # [示例/Example] share_url = \"https://v.douyin.com/e3x2fjE/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_url_api_v1_douyin_web_fetch_one_video_by_share_url_get_with_http_info(share_url, async_req=True)
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
                    " to method fetch_one_video_by_share_url_api_v1_douyin_web_fetch_one_video_by_share_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_url' is set
        if self.api_client.client_side_validation and ('share_url' not in params or
                                                       params['share_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_url` when calling `fetch_one_video_by_share_url_api_v1_douyin_web_fetch_one_video_by_share_url_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_one_video_by_share_url', 'GET',
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

    def fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get(self, item_id, duration, end_time, start_time, **kwargs):  # noqa: E501
        """获取单个作品视频弹幕数据/Get single video danmaku data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品视频弹幕数据 ### 参数: - item_id: 作品id - duration: 视频总时长 - end_time: 结束时间 - start_time: 开始时间 ### 返回: - 视频弹幕数据  # [English] ### Purpose: - Get single video danmaku data ### Parameters: - item_id: Video id - duration: Video total duration - end_time: End time - start_time: Start time ### Return: - Video danmaku data  # [示例/Example] item_id = \"7355433624046472498\" duration = 15134 end_time = 15133 start_time = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get(item_id, duration, end_time, start_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
        :param object duration: 视频总时长/Video total duration (required)
        :param object end_time: 结束时间/End time (required)
        :param object start_time: 开始时间/Start time (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get_with_http_info(item_id, duration, end_time, start_time, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get_with_http_info(item_id, duration, end_time, start_time, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get_with_http_info(self, item_id, duration, end_time, start_time, **kwargs):  # noqa: E501
        """获取单个作品视频弹幕数据/Get single video danmaku data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品视频弹幕数据 ### 参数: - item_id: 作品id - duration: 视频总时长 - end_time: 结束时间 - start_time: 开始时间 ### 返回: - 视频弹幕数据  # [English] ### Purpose: - Get single video danmaku data ### Parameters: - item_id: Video id - duration: Video total duration - end_time: End time - start_time: Start time ### Return: - Video danmaku data  # [示例/Example] item_id = \"7355433624046472498\" duration = 15134 end_time = 15133 start_time = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get_with_http_info(item_id, duration, end_time, start_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
        :param object duration: 视频总时长/Video total duration (required)
        :param object end_time: 结束时间/End time (required)
        :param object start_time: 开始时间/Start time (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'duration', 'end_time', 'start_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get`")  # noqa: E501
        # verify the required parameter 'duration' is set
        if self.api_client.client_side_validation and ('duration' not in params or
                                                       params['duration'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `duration` when calling `fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get`")  # noqa: E501
        # verify the required parameter 'end_time' is set
        if self.api_client.client_side_validation and ('end_time' not in params or
                                                       params['end_time'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `end_time` when calling `fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get`")  # noqa: E501
        # verify the required parameter 'start_time' is set
        if self.api_client.client_side_validation and ('start_time' not in params or
                                                       params['start_time'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `start_time` when calling `fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))  # noqa: E501
        if 'duration' in params:
            query_params.append(('duration', params['duration']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_one_video_danmaku', 'GET',
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

    def fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get(self, product_id, shop_id, price, author_id, sec_user_id, **kwargs):  # noqa: E501
        """获取商品优惠券信息/Get product coupon information  # noqa: E501

        # [中文]  获取商品优惠券相关信息  # [English]  Get product coupon information  # [示例/Example]  product_id = \"3770337983790711029\" shop_id = \"129508461\" price = \"1490\" author_id = \"3109048548866375\" sec_user_id = \"MS4wLjABAAAALoWx-cZWuQVWWvvlE-HiKgm9jel_nmwMcjAMIaEAwFq25sskN1Zgqy_T3x4D0Goy\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get(product_id, shop_id, price, author_id, sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object shop_id: 店铺ID/Shop ID (required)
        :param object price: 价格/Price (required)
        :param object author_id: 作者ID/Author ID (required)
        :param object sec_user_id: 作者ID/Secure Author ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get_with_http_info(product_id, shop_id, price, author_id, sec_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get_with_http_info(product_id, shop_id, price, author_id, sec_user_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get_with_http_info(self, product_id, shop_id, price, author_id, sec_user_id, **kwargs):  # noqa: E501
        """获取商品优惠券信息/Get product coupon information  # noqa: E501

        # [中文]  获取商品优惠券相关信息  # [English]  Get product coupon information  # [示例/Example]  product_id = \"3770337983790711029\" shop_id = \"129508461\" price = \"1490\" author_id = \"3109048548866375\" sec_user_id = \"MS4wLjABAAAALoWx-cZWuQVWWvvlE-HiKgm9jel_nmwMcjAMIaEAwFq25sskN1Zgqy_T3x4D0Goy\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get_with_http_info(product_id, shop_id, price, author_id, sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object shop_id: 店铺ID/Shop ID (required)
        :param object price: 价格/Price (required)
        :param object author_id: 作者ID/Author ID (required)
        :param object sec_user_id: 作者ID/Secure Author ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'shop_id', 'price', 'author_id', 'sec_user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get`")  # noqa: E501
        # verify the required parameter 'shop_id' is set
        if self.api_client.client_side_validation and ('shop_id' not in params or
                                                       params['shop_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `shop_id` when calling `fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get`")  # noqa: E501
        # verify the required parameter 'price' is set
        if self.api_client.client_side_validation and ('price' not in params or
                                                       params['price'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `price` when calling `fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get`")  # noqa: E501
        # verify the required parameter 'author_id' is set
        if self.api_client.client_side_validation and ('author_id' not in params or
                                                       params['author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `author_id` when calling `fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get`")  # noqa: E501
        # verify the required parameter 'sec_user_id' is set
        if self.api_client.client_side_validation and ('sec_user_id' not in params or
                                                       params['sec_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_id` when calling `fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'shop_id' in params:
            query_params.append(('shop_id', params['shop_id']))  # noqa: E501
        if 'price' in params:
            query_params.append(('price', params['price']))  # noqa: E501
        if 'author_id' in params:
            query_params.append(('author_id', params['author_id']))  # noqa: E501
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_product_coupon', 'GET',
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

    def fetch_product_detail_api_v1_douyin_web_fetch_product_detail_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情/Get product detail  # noqa: E501

        # [中文] ### 用途: - 获取商品详情信息 ### 参数: - product_id: 商品ID（必填） - aweme_id: 作品ID（可选，如果商品来自某个视频） - room_id: 直播间ID（可选，如果商品来自直播间） - sec_user_id: 用户sec_user_id（可选，商品所属用户） ### 返回: - 商品详细信息  # [English] ### Purpose: - Get product detail information ### Parameters: - product_id: Product ID (required) - aweme_id: Video ID (optional, if product is from a video) - room_id: Room ID (optional, if product is from live room) - sec_user_id: User sec_user_id (optional, product owner) ### Return: - Product detail information  # [示例/Example] product_id = \"3654018325143066950\" aweme_id = \"7546956331878501673\"  # 可选 room_id = \"\"  # 可选 sec_user_id = \"MS4wLjABAAAALoWx-cZWuQVWWvvlE-HiKgm9jel_nmwMcjAMIaEAwFq25sskN1Zgqy_T3x4D0Goy\"  # 可选  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_api_v1_douyin_web_fetch_product_detail_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object aweme_id: 作品ID（可选）/Video ID (optional)
        :param object room_id: 直播间ID（可选）/Room ID (optional)
        :param object sec_user_id: 用户sec_user_id（可选）/User sec_user_id (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_detail_api_v1_douyin_web_fetch_product_detail_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_detail_api_v1_douyin_web_fetch_product_detail_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_detail_api_v1_douyin_web_fetch_product_detail_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情/Get product detail  # noqa: E501

        # [中文] ### 用途: - 获取商品详情信息 ### 参数: - product_id: 商品ID（必填） - aweme_id: 作品ID（可选，如果商品来自某个视频） - room_id: 直播间ID（可选，如果商品来自直播间） - sec_user_id: 用户sec_user_id（可选，商品所属用户） ### 返回: - 商品详细信息  # [English] ### Purpose: - Get product detail information ### Parameters: - product_id: Product ID (required) - aweme_id: Video ID (optional, if product is from a video) - room_id: Room ID (optional, if product is from live room) - sec_user_id: User sec_user_id (optional, product owner) ### Return: - Product detail information  # [示例/Example] product_id = \"3654018325143066950\" aweme_id = \"7546956331878501673\"  # 可选 room_id = \"\"  # 可选 sec_user_id = \"MS4wLjABAAAALoWx-cZWuQVWWvvlE-HiKgm9jel_nmwMcjAMIaEAwFq25sskN1Zgqy_T3x4D0Goy\"  # 可选  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_api_v1_douyin_web_fetch_product_detail_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object aweme_id: 作品ID（可选）/Video ID (optional)
        :param object room_id: 直播间ID（可选）/Room ID (optional)
        :param object sec_user_id: 用户sec_user_id（可选）/User sec_user_id (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'aweme_id', 'room_id', 'sec_user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_detail_api_v1_douyin_web_fetch_product_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_detail_api_v1_douyin_web_fetch_product_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_product_detail', 'GET',
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

    def fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get(self, product_id, shop_id, **kwargs):  # noqa: E501
        """获取商品评价列表/Get product review list  # noqa: E501

        # [中文]  获取商品评价列表  # [English]  Get product review list  # [示例/Example]  product_id = \"3770337983790711029\" shop_id = \"129508461\" cursor = 0 count = 20 sort_type = 0  # 0: 默认排序, 1: 最新排序  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get(product_id, shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object shop_id: 店铺ID/Shop ID (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Count
        :param object sort_type: 排序类型 (0: 默认排序, 1: 最新排序)/Sort Type (0: Default, 1: Latest)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get_with_http_info(product_id, shop_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get_with_http_info(product_id, shop_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get_with_http_info(self, product_id, shop_id, **kwargs):  # noqa: E501
        """获取商品评价列表/Get product review list  # noqa: E501

        # [中文]  获取商品评价列表  # [English]  Get product review list  # [示例/Example]  product_id = \"3770337983790711029\" shop_id = \"129508461\" cursor = 0 count = 20 sort_type = 0  # 0: 默认排序, 1: 最新排序  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get_with_http_info(product_id, shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object shop_id: 店铺ID/Shop ID (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Count
        :param object sort_type: 排序类型 (0: 默认排序, 1: 最新排序)/Sort Type (0: Default, 1: Latest)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'shop_id', 'cursor', 'count', 'sort_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get`")  # noqa: E501
        # verify the required parameter 'shop_id' is set
        if self.api_client.client_side_validation and ('shop_id' not in params or
                                                       params['shop_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `shop_id` when calling `fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'shop_id' in params:
            query_params.append(('shop_id', params['shop_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
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
            '/api/v1/douyin/web/fetch_product_review_list', 'GET',
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

    def fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get(self, product_id, shop_id, **kwargs):  # noqa: E501
        """获取商品评价评分/Get product review score  # noqa: E501

        # [中文]  获取商品评价评分  # [English]  Get product review score  # [示例/Example]  product_id = \"3770337983790711029\" shop_id = \"129508461\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get(product_id, shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object shop_id: 店铺ID/Shop ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get_with_http_info(product_id, shop_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get_with_http_info(product_id, shop_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get_with_http_info(self, product_id, shop_id, **kwargs):  # noqa: E501
        """获取商品评价评分/Get product review score  # noqa: E501

        # [中文]  获取商品评价评分  # [English]  Get product review score  # [示例/Example]  product_id = \"3770337983790711029\" shop_id = \"129508461\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get_with_http_info(product_id, shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object shop_id: 店铺ID/Shop ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'shop_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get`")  # noqa: E501
        # verify the required parameter 'shop_id' is set
        if self.api_client.client_side_validation and ('shop_id' not in params or
                                                       params['shop_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `shop_id` when calling `fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'shop_id' in params:
            query_params.append(('shop_id', params['shop_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_product_review_score', 'GET',
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

    def fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get(self, product_id, author_id, **kwargs):  # noqa: E501
        """获取商品SKU列表/Get product SKU list  # noqa: E501

        # [中文]  获取商品SKU列表  # [English]  Get product SKU list  # [示例/Example]  product_id = \"3770337983790711029\" author_id = \"3109048548866375\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get(product_id, author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object author_id: 作者ID/Author ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get_with_http_info(product_id, author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get_with_http_info(product_id, author_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get_with_http_info(self, product_id, author_id, **kwargs):  # noqa: E501
        """获取商品SKU列表/Get product SKU list  # noqa: E501

        # [中文]  获取商品SKU列表  # [English]  Get product SKU list  # [示例/Example]  product_id = \"3770337983790711029\" author_id = \"3109048548866375\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get_with_http_info(product_id, author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object author_id: 作者ID/Author ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'author_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get`")  # noqa: E501
        # verify the required parameter 'author_id' is set
        if self.api_client.client_side_validation and ('author_id' not in params or
                                                       params['author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `author_id` when calling `fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'author_id' in params:
            query_params.append(('author_id', params['author_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_product_sku_list', 'GET',
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

    def fetch_query_user_api_v1_douyin_web_fetch_query_user_post(self, **kwargs):  # noqa: E501
        """查询抖音用户基本信息/Query Douyin user basic information  # noqa: E501

        # [中文] ### 用途: - 查询抖音用户基本信息 ### 参数: - cookie: 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。 ### 返回: - 用户基本信息  # [English] ### Purpose: - Query Douyin user basic information ### Parameters: - cookie: User ttwid Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface to get. ### Return: - User basic information  # [示例/Example] cookie = \"ttwid=xxx;\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_query_user_api_v1_douyin_web_fetch_query_user_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_query_user_api_v1_douyin_web_fetch_query_user_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_query_user_api_v1_douyin_web_fetch_query_user_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_query_user_api_v1_douyin_web_fetch_query_user_post_with_http_info(self, **kwargs):  # noqa: E501
        """查询抖音用户基本信息/Query Douyin user basic information  # noqa: E501

        # [中文] ### 用途: - 查询抖音用户基本信息 ### 参数: - cookie: 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。 ### 返回: - 用户基本信息  # [English] ### Purpose: - Query Douyin user basic information ### Parameters: - cookie: User ttwid Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface to get. ### Return: - User basic information  # [示例/Example] cookie = \"ttwid=xxx;\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_query_user_api_v1_douyin_web_fetch_query_user_post_with_http_info(async_req=True)
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
                    " to method fetch_query_user_api_v1_douyin_web_fetch_query_user_post" % key
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
            '/api/v1/douyin/web/fetch_query_user', 'POST',
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

    def fetch_related_posts_api_v1_douyin_web_fetch_related_posts_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取相关作品推荐数据/Get related posts recommendation data  # noqa: E501

        # [中文] ### 用途: - 获取相关作品推荐数据 ### 参数: - aweme_id: 作品id - refresh_index: 翻页索引，默认为1，然后每次增加1用于翻页。 - count: 数量，默认为20，建议保持不变。 ### 返回: - 作品数据  # [English] ### Purpose: - Get related posts recommendation data ### Parameters: - aweme_id: Video id - refresh_index: Paging index, default is 1, then increase by 1 each time for paging. - count: Number, default is 20, it is recommended to keep it unchanged. ### Return: - Video data  # [示例/Example] aweme_id = \"7393365489105358132\" refresh_index = 1 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_related_posts_api_v1_douyin_web_fetch_related_posts_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_related_posts_api_v1_douyin_web_fetch_related_posts_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_related_posts_api_v1_douyin_web_fetch_related_posts_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_related_posts_api_v1_douyin_web_fetch_related_posts_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取相关作品推荐数据/Get related posts recommendation data  # noqa: E501

        # [中文] ### 用途: - 获取相关作品推荐数据 ### 参数: - aweme_id: 作品id - refresh_index: 翻页索引，默认为1，然后每次增加1用于翻页。 - count: 数量，默认为20，建议保持不变。 ### 返回: - 作品数据  # [English] ### Purpose: - Get related posts recommendation data ### Parameters: - aweme_id: Video id - refresh_index: Paging index, default is 1, then increase by 1 each time for paging. - count: Number, default is 20, it is recommended to keep it unchanged. ### Return: - Video data  # [示例/Example] aweme_id = \"7393365489105358132\" refresh_index = 1 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_related_posts_api_v1_douyin_web_fetch_related_posts_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object refresh_index: 翻页索引/Paging index
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id', 'refresh_index', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_related_posts_api_v1_douyin_web_fetch_related_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_related_posts_api_v1_douyin_web_fetch_related_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501
        if 'refresh_index' in params:
            query_params.append(('refresh_index', params['refresh_index']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_related_posts', 'GET',
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

    def fetch_search_challenge_api_v1_douyin_web_fetch_search_challenge_post(self, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 搜索话题/Search Challenge  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212773e0 ### 用途: - 搜索话题，此接口不带Cookie请求时只能获取到前30条数据，建议自行提供Cookie获取更多数据。 - Cookie获取方式：打开网页抖音，登录后，按F12打开开发者工具，点击Network，刷新页面，找到第一个请求，复制Cookie。 ### 参数: - keyword: 关键词 - cursor: 偏移量 - count: 数量 - cookie: 用户自行提供的Cookie，用于获取更多数据。 ### 返回: - 话题搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212773e0 ### Purpose: - Search Challenge, when this interface is requested without Cookie, only the first 30 data can be obtained, it is recommended to provide Cookie to get more data. - Cookie acquisition method: Open the Douyin webpage, log in, press F12 to open the developer tool, click Network, refresh the page, find the first request, copy the Cookie. ### Parameters: - keyword: Keyword - cursor: Offset - count: Number - cookie: User provided Cookie, used to get more data. ### Return: - Challenge search results  # [示例/Example] keyword = \"动漫\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_challenge_api_v1_douyin_web_fetch_search_challenge_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_challenge_api_v1_douyin_web_fetch_search_challenge_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_challenge_api_v1_douyin_web_fetch_search_challenge_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_search_challenge_api_v1_douyin_web_fetch_search_challenge_post_with_http_info(self, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 搜索话题/Search Challenge  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212773e0 ### 用途: - 搜索话题，此接口不带Cookie请求时只能获取到前30条数据，建议自行提供Cookie获取更多数据。 - Cookie获取方式：打开网页抖音，登录后，按F12打开开发者工具，点击Network，刷新页面，找到第一个请求，复制Cookie。 ### 参数: - keyword: 关键词 - cursor: 偏移量 - count: 数量 - cookie: 用户自行提供的Cookie，用于获取更多数据。 ### 返回: - 话题搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212773e0 ### Purpose: - Search Challenge, when this interface is requested without Cookie, only the first 30 data can be obtained, it is recommended to provide Cookie to get more data. - Cookie acquisition method: Open the Douyin webpage, log in, press F12 to open the developer tool, click Network, refresh the page, find the first request, copy the Cookie. ### Parameters: - keyword: Keyword - cursor: Offset - count: Number - cookie: User provided Cookie, used to get more data. ### Return: - Challenge search results  # [示例/Example] keyword = \"动漫\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_challenge_api_v1_douyin_web_fetch_search_challenge_post_with_http_info(async_req=True)
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
                    " to method fetch_search_challenge_api_v1_douyin_web_fetch_search_challenge_post" % key
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
            '/api/v1/douyin/web/fetch_search_challenge', 'POST',
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

    def fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get(self, offset, count, content_type, **kwargs):  # noqa: E501
        """短剧作品/Series Video  # noqa: E501

        # [中文] ### 用途: - 短剧作品 ### 参数: - offset: 页码，默认为0 - count: 每页数量，默认为16 - content_type: 子类型，默认为0     - 0: 热榜     - 101: 甜宠     - 102: 搞笑     - 104: 正能量     - 105: 成长     - 106: 悬疑     - 109: 家庭     - 110: 都市     - 112: 奇幻     - 113: 玄幻     - 114: 职场     - 115: 青春     - 116: 古装     - 117: 动作     - 119: 逆袭     - 124: 其他 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie ### 返回: - 短剧作品数据  # [English] ### Purpose: - Series Video ### Parameters: - offset: Page number, default is 0 - count: Number per page, default is 16 - content_type: Subtype, default is 0     - 0: Hot list     - 101: Sweet pet     - 102: Funny     - 104: Positive energy     - 105: Growth     - 106: Suspense     - 109: Family     - 110: Urban     - 112: Fantasy     - 113: Fantasy     - 114: Workplace     - 115: Youth     - 116: Ancient costume     - 117: Action     - 119: Counterattack     - 124: Other - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Series Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get(offset, count, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object offset: 页码/Page number (required)
        :param object count: 每页数量/Number per page (required)
        :param object content_type: 短剧类型/Subtype (required)
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get_with_http_info(offset, count, content_type, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get_with_http_info(offset, count, content_type, **kwargs)  # noqa: E501
            return data

    def fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get_with_http_info(self, offset, count, content_type, **kwargs):  # noqa: E501
        """短剧作品/Series Video  # noqa: E501

        # [中文] ### 用途: - 短剧作品 ### 参数: - offset: 页码，默认为0 - count: 每页数量，默认为16 - content_type: 子类型，默认为0     - 0: 热榜     - 101: 甜宠     - 102: 搞笑     - 104: 正能量     - 105: 成长     - 106: 悬疑     - 109: 家庭     - 110: 都市     - 112: 奇幻     - 113: 玄幻     - 114: 职场     - 115: 青春     - 116: 古装     - 117: 动作     - 119: 逆袭     - 124: 其他 - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题 - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie ### 返回: - 短剧作品数据  # [English] ### Purpose: - Series Video ### Parameters: - offset: Page number, default is 0 - count: Number per page, default is 16 - content_type: Subtype, default is 0     - 0: Hot list     - 101: Sweet pet     - 102: Funny     - 104: Positive energy     - 105: Growth     - 106: Suspense     - 109: Family     - 110: Urban     - 112: Fantasy     - 113: Fantasy     - 114: Workplace     - 115: Youth     - 116: Ancient costume     - 117: Action     - 119: Counterattack     - 124: Other - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie  ### Return: - Series Video data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get_with_http_info(offset, count, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object offset: 页码/Page number (required)
        :param object count: 每页数量/Number per page (required)
        :param object content_type: 短剧类型/Subtype (required)
        :param object cookie: 用户自行提供的Cookie/User provided Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'count', 'content_type', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'offset' is set
        if self.api_client.client_side_validation and ('offset' not in params or
                                                       params['offset'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `offset` when calling `fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get`")  # noqa: E501
        # verify the required parameter 'count' is set
        if self.api_client.client_side_validation and ('count' not in params or
                                                       params['count'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `count` when calling `fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if self.api_client.client_side_validation and ('content_type' not in params or
                                                       params['content_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `content_type` when calling `fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'content_type' in params:
            query_params.append(('content_type', params['content_type']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_series_aweme', 'GET',
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

    def fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post(self, **kwargs):  # noqa: E501
        """获取用户收藏作品数据/Get user collection video data  # noqa: E501

        # [中文] ### 用途: - 获取用户收藏作品数据 ### 参数: - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie) - max_cursor: 最大游标 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user collection video data ### Parameters: - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie) - max_cursor: Maximum cursor - count: Maximum number ### Return: - User video data  # [示例/Example] cookie = \"YOUR_COOKIE\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户收藏作品数据/Get user collection video data  # noqa: E501

        # [中文] ### 用途: - 获取用户收藏作品数据 ### 参数: - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie) - max_cursor: 最大游标 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user collection video data ### Parameters: - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie) - max_cursor: Maximum cursor - count: Maximum number ### Return: - User video data  # [示例/Example] cookie = \"YOUR_COOKIE\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post_with_http_info(async_req=True)
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
                    " to method fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post" % key
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
            '/api/v1/douyin/web/fetch_user_collection_videos', 'POST',
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

    def fetch_user_collects_api_v1_douyin_web_fetch_user_collects_post(self, **kwargs):  # noqa: E501
        """获取用户收藏夹/Get user collection  # noqa: E501

        # [中文] ### 用途: - 获取用户收藏夹 ### 参数: - max_cursor: 最大游标 - count: 最大数量 - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie) ### 返回: - 用户收藏夹数据  # [English] ### Purpose: - Get user collection ### Parameters: - max_cursor: Maximum cursor - count: Maximum number - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie) ### Return: - User collection data  # [示例/Example] cookie = \"YOUR_COOKIE\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collects_api_v1_douyin_web_fetch_user_collects_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_collects_api_v1_douyin_web_fetch_user_collects_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_collects_api_v1_douyin_web_fetch_user_collects_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_collects_api_v1_douyin_web_fetch_user_collects_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户收藏夹/Get user collection  # noqa: E501

        # [中文] ### 用途: - 获取用户收藏夹 ### 参数: - max_cursor: 最大游标 - count: 最大数量 - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie) ### 返回: - 用户收藏夹数据  # [English] ### Purpose: - Get user collection ### Parameters: - max_cursor: Maximum cursor - count: Maximum number - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie) ### Return: - User collection data  # [示例/Example] cookie = \"YOUR_COOKIE\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collects_api_v1_douyin_web_fetch_user_collects_post_with_http_info(async_req=True)
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
                    " to method fetch_user_collects_api_v1_douyin_web_fetch_user_collects_post" % key
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
            '/api/v1/douyin/web/fetch_user_collects', 'POST',
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

    def fetch_user_collects_videos_api_v1_douyin_web_fetch_user_collects_videos_get(self, collects_id, **kwargs):  # noqa: E501
        """获取用户收藏夹数据/Get user collection data  # noqa: E501

        # [中文] ### 用途: - 获取用户收藏夹数据 ### 参数: - collects_id: 收藏夹id - max_cursor: 最大游标 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user collection data ### Parameters: - collects_id: Collection id - max_cursor: Maximum cursor - count: Maximum number ### Return: - User video data  # [示例/Example] collects_id = \"\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collects_videos_api_v1_douyin_web_fetch_user_collects_videos_get(collects_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collects_id: 收藏夹id/Collection id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object counts: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_collects_videos_api_v1_douyin_web_fetch_user_collects_videos_get_with_http_info(collects_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_collects_videos_api_v1_douyin_web_fetch_user_collects_videos_get_with_http_info(collects_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_collects_videos_api_v1_douyin_web_fetch_user_collects_videos_get_with_http_info(self, collects_id, **kwargs):  # noqa: E501
        """获取用户收藏夹数据/Get user collection data  # noqa: E501

        # [中文] ### 用途: - 获取用户收藏夹数据 ### 参数: - collects_id: 收藏夹id - max_cursor: 最大游标 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user collection data ### Parameters: - collects_id: Collection id - max_cursor: Maximum cursor - count: Maximum number ### Return: - User video data  # [示例/Example] collects_id = \"\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collects_videos_api_v1_douyin_web_fetch_user_collects_videos_get_with_http_info(collects_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collects_id: 收藏夹id/Collection id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object counts: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collects_id', 'max_cursor', 'counts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_collects_videos_api_v1_douyin_web_fetch_user_collects_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collects_id' is set
        if self.api_client.client_side_validation and ('collects_id' not in params or
                                                       params['collects_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `collects_id` when calling `fetch_user_collects_videos_api_v1_douyin_web_fetch_user_collects_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'collects_id' in params:
            query_params.append(('collects_id', params['collects_id']))  # noqa: E501
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
            '/api/v1/douyin/web/fetch_user_collects_videos', 'GET',
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

    def fetch_user_fans_list_api_v1_douyin_web_fetch_user_fans_list_get(self, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Get user fans list  # noqa: E501

        # [中文] ### 用途: - 获取用户粉丝列表 - 第一次请求时，max_time传`0`，source_type传`2`，然后会返回一个空的粉丝列表，里面包含了max_time，然后再次请求时，max_time传上一次请求返回的max_time，source_type传`1`，即可获取到粉丝列表。 - 如果不按照上述方式请求，可能会导致返回数据包含重复数据。  ### 参数: - sec_user_id: 用户sec_user_id - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。 - count: 数量，默认为20，建议保持不变。 - source_type: 来源类型，默认为`1`，第一次请求时使用`2`作为来源类型，然后再次请求时使用`1`作为来源类型。 ### 返回: - 粉丝列表  # [English] ### Purpose: - Get user fans list - When requesting for the first time, pass `0` for max_time, pass `2` for source_type, and an empty fans list will be returned, which contains max_time, then pass the max_time returned by the previous request for paging each time, pass `1` for source_type, you can get the fans list. - If you do not request according to the above method, it may cause the returned data to contain duplicate data.  ### Parameters: - sec_user_id: User sec_user_id - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging. - count: Number, default is 20, it is recommended to keep it unchanged. - source_type: Source type, default is `1`, use `2` as the source type for the first request, and then use `1` as the source type for the subsequent request. ### Return: - Fans list  # [示例/Example] sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\" max_time = \"0\" count = 20 source_type = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_fans_list_api_v1_douyin_web_fetch_user_fans_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object max_time: 最大时间戳/Maximum timestamp
        :param object count: 数量/Number
        :param object source_type: 来源类型/Source type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_fans_list_api_v1_douyin_web_fetch_user_fans_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_fans_list_api_v1_douyin_web_fetch_user_fans_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_fans_list_api_v1_douyin_web_fetch_user_fans_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Get user fans list  # noqa: E501

        # [中文] ### 用途: - 获取用户粉丝列表 - 第一次请求时，max_time传`0`，source_type传`2`，然后会返回一个空的粉丝列表，里面包含了max_time，然后再次请求时，max_time传上一次请求返回的max_time，source_type传`1`，即可获取到粉丝列表。 - 如果不按照上述方式请求，可能会导致返回数据包含重复数据。  ### 参数: - sec_user_id: 用户sec_user_id - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。 - count: 数量，默认为20，建议保持不变。 - source_type: 来源类型，默认为`1`，第一次请求时使用`2`作为来源类型，然后再次请求时使用`1`作为来源类型。 ### 返回: - 粉丝列表  # [English] ### Purpose: - Get user fans list - When requesting for the first time, pass `0` for max_time, pass `2` for source_type, and an empty fans list will be returned, which contains max_time, then pass the max_time returned by the previous request for paging each time, pass `1` for source_type, you can get the fans list. - If you do not request according to the above method, it may cause the returned data to contain duplicate data.  ### Parameters: - sec_user_id: User sec_user_id - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging. - count: Number, default is 20, it is recommended to keep it unchanged. - source_type: Source type, default is `1`, use `2` as the source type for the first request, and then use `1` as the source type for the subsequent request. ### Return: - Fans list  # [示例/Example] sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\" max_time = \"0\" count = 20 source_type = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_fans_list_api_v1_douyin_web_fetch_user_fans_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object max_time: 最大时间戳/Maximum timestamp
        :param object count: 数量/Number
        :param object source_type: 来源类型/Source type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'max_time', 'count', 'source_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_fans_list_api_v1_douyin_web_fetch_user_fans_list_get" % key
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
        if 'source_type' in params:
            query_params.append(('source_type', params['source_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_user_fans_list', 'GET',
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

    def fetch_user_following_list_api_v1_douyin_web_fetch_user_following_list_get(self, **kwargs):  # noqa: E501
        """获取用户关注列表/Get user following list  # noqa: E501

        # [中文] ### 用途: - 获取用户关注列表 - 第一次请求时，max_time传`0`，source_type传`2`，然后会返回一个空的粉丝列表，里面包含了max_time，然后再次请求时，max_time传上一次请求返回的max_time，source_type传`1`，即可获取到粉丝列表。 - 如果不按照上述方式请求，可能会导致返回数据包含重复数据。 ### 参数: - sec_user_id: 用户sec_user_id - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。 - count: 数量，默认为20，建议保持不变。 - source_type: 来源类型，默认为`1`，第一次请求时使用`2`作为来源类型，然后再次请求时使用`1`作为来源类型。 ### 返回: - 关注列表  # [English] ### Purpose: - Get user following list - When requesting for the first time, pass `0` for max_time, pass `2` for source_type, and an empty fans list will be returned, which contains max_time, then pass the max_time returned by the previous request for paging each time, pass `1` for source_type, you can get the fans list. - If you do not request according to the above method, it may cause the returned data to contain duplicate data.  ### Parameters: - sec_user_id: User sec_user_id - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging. - count: Number, default is 20, it is recommended to keep it unchanged. - source_type: Source type, default is `1`, use `2` as the source type for the first request, and then use `1` as the source type for the subsequent request. ### Return: - Following list  # [示例/Example] sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\" max_time = \"0\" count = 20 source_type = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_list_api_v1_douyin_web_fetch_user_following_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object max_time: 最大时间戳/Maximum timestamp
        :param object count: 数量/Number
        :param object source_type: 来源类型/Source type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_following_list_api_v1_douyin_web_fetch_user_following_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_following_list_api_v1_douyin_web_fetch_user_following_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_following_list_api_v1_douyin_web_fetch_user_following_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户关注列表/Get user following list  # noqa: E501

        # [中文] ### 用途: - 获取用户关注列表 - 第一次请求时，max_time传`0`，source_type传`2`，然后会返回一个空的粉丝列表，里面包含了max_time，然后再次请求时，max_time传上一次请求返回的max_time，source_type传`1`，即可获取到粉丝列表。 - 如果不按照上述方式请求，可能会导致返回数据包含重复数据。 ### 参数: - sec_user_id: 用户sec_user_id - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。 - count: 数量，默认为20，建议保持不变。 - source_type: 来源类型，默认为`1`，第一次请求时使用`2`作为来源类型，然后再次请求时使用`1`作为来源类型。 ### 返回: - 关注列表  # [English] ### Purpose: - Get user following list - When requesting for the first time, pass `0` for max_time, pass `2` for source_type, and an empty fans list will be returned, which contains max_time, then pass the max_time returned by the previous request for paging each time, pass `1` for source_type, you can get the fans list. - If you do not request according to the above method, it may cause the returned data to contain duplicate data.  ### Parameters: - sec_user_id: User sec_user_id - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging. - count: Number, default is 20, it is recommended to keep it unchanged. - source_type: Source type, default is `1`, use `2` as the source type for the first request, and then use `1` as the source type for the subsequent request. ### Return: - Following list  # [示例/Example] sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\" max_time = \"0\" count = 20 source_type = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_list_api_v1_douyin_web_fetch_user_following_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object max_time: 最大时间戳/Maximum timestamp
        :param object count: 数量/Number
        :param object source_type: 来源类型/Source type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'max_time', 'count', 'source_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_following_list_api_v1_douyin_web_fetch_user_following_list_get" % key
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
        if 'source_type' in params:
            query_params.append(('source_type', params['source_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_user_following_list', 'GET',
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

    def fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post(self, **kwargs):  # noqa: E501
        """获取用户喜欢作品数据/Get user like video data  # noqa: E501

        # [中文] ### 用途: - 获取用户喜欢作品数据 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 最大游标 - count: 最大数量 - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie) ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user like video data ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Maximum cursor - count: Maximum count number - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie) ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户喜欢作品数据/Get user like video data  # noqa: E501

        # [中文] ### 用途: - 获取用户喜欢作品数据 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 最大游标 - count: 最大数量 - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie) ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user like video data ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Maximum cursor - count: Maximum count number - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie) ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post_with_http_info(async_req=True)
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
                    " to method fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post" % key
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
            '/api/v1/douyin/web/fetch_user_like_videos', 'POST',
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

    def fetch_user_live_info_by_uid_api_v1_douyin_web_fetch_user_live_info_by_uid_get(self, uid, **kwargs):  # noqa: E501
        """使用UID获取用户开播信息/Get user live information by UID  # noqa: E501

        # [中文] ### 用途: - 使用UID获取用户开播信息 ### 参数: - uid: 用户UID ### 返回: - 用户开播信息，包含room_id与live_status  # [English] ### Purpose: - Get user live information by UID ### Parameters: - uid: User UID ### Return: - User live information, including room_id and live_status  # [示例/Example] uid = \"3081254195702747\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_info_by_uid_api_v1_douyin_web_fetch_user_live_info_by_uid_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID/User UID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_live_info_by_uid_api_v1_douyin_web_fetch_user_live_info_by_uid_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_live_info_by_uid_api_v1_douyin_web_fetch_user_live_info_by_uid_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_live_info_by_uid_api_v1_douyin_web_fetch_user_live_info_by_uid_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """使用UID获取用户开播信息/Get user live information by UID  # noqa: E501

        # [中文] ### 用途: - 使用UID获取用户开播信息 ### 参数: - uid: 用户UID ### 返回: - 用户开播信息，包含room_id与live_status  # [English] ### Purpose: - Get user live information by UID ### Parameters: - uid: User UID ### Return: - User live information, including room_id and live_status  # [示例/Example] uid = \"3081254195702747\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_info_by_uid_api_v1_douyin_web_fetch_user_live_info_by_uid_get_with_http_info(uid, async_req=True)
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
                    " to method fetch_user_live_info_by_uid_api_v1_douyin_web_fetch_user_live_info_by_uid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_live_info_by_uid_api_v1_douyin_web_fetch_user_live_info_by_uid_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_user_live_info_by_uid', 'GET',
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

    def fetch_user_live_videos_api_v1_douyin_web_fetch_user_live_videos_get(self, webcast_id, **kwargs):  # noqa: E501
        """获取用户直播流数据/Get user live video data  # noqa: E501

        # [中文] ### 用途: - 获取用户直播流数据 ### 参数: - webcast_id: 直播间 webcast_id - 获取方法：     - 假设你的直播间链接为：https://www.douyin.com/root/live/376034101029     - 那么直播间webcast_id为：376034101029     - webcast_id为直播间链接的最后一段数字，与room_id不同。 ### 返回: - 直播流数据  # [English] ### Purpose: - Get user live video data ### Parameters: - webcast_id: Room webcast_id - Acquisition method:     - Assuming your live room link is: https://www.douyin.com/root/live/376034101029     - Then the live room webcast_id is: 376034101029     - The webcast_id is the last number of the live room link, which is different from the room_id. ### Return: - Live stream data  # [示例/Example] webcast_id = \"376034101029\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_videos_api_v1_douyin_web_fetch_user_live_videos_get(webcast_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object webcast_id: 直播间webcast_id/Room webcast_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_live_videos_api_v1_douyin_web_fetch_user_live_videos_get_with_http_info(webcast_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_live_videos_api_v1_douyin_web_fetch_user_live_videos_get_with_http_info(webcast_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_live_videos_api_v1_douyin_web_fetch_user_live_videos_get_with_http_info(self, webcast_id, **kwargs):  # noqa: E501
        """获取用户直播流数据/Get user live video data  # noqa: E501

        # [中文] ### 用途: - 获取用户直播流数据 ### 参数: - webcast_id: 直播间 webcast_id - 获取方法：     - 假设你的直播间链接为：https://www.douyin.com/root/live/376034101029     - 那么直播间webcast_id为：376034101029     - webcast_id为直播间链接的最后一段数字，与room_id不同。 ### 返回: - 直播流数据  # [English] ### Purpose: - Get user live video data ### Parameters: - webcast_id: Room webcast_id - Acquisition method:     - Assuming your live room link is: https://www.douyin.com/root/live/376034101029     - Then the live room webcast_id is: 376034101029     - The webcast_id is the last number of the live room link, which is different from the room_id. ### Return: - Live stream data  # [示例/Example] webcast_id = \"376034101029\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_videos_api_v1_douyin_web_fetch_user_live_videos_get_with_http_info(webcast_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object webcast_id: 直播间webcast_id/Room webcast_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webcast_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_live_videos_api_v1_douyin_web_fetch_user_live_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webcast_id' is set
        if self.api_client.client_side_validation and ('webcast_id' not in params or
                                                       params['webcast_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `webcast_id` when calling `fetch_user_live_videos_api_v1_douyin_web_fetch_user_live_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'webcast_id' in params:
            query_params.append(('webcast_id', params['webcast_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_user_live_videos', 'GET',
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

    def fetch_user_live_videos_by_room_id_api_v1_douyin_web_fetch_user_live_videos_by_room_id_get(self, room_id, **kwargs):  # noqa: E501
        """通过room_id获取指定用户的直播流数据 V1/Get live video data of specified user by room_id V1  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的直播流数据 ### 参数: - room_id: 直播间room_id ### 返回: - 直播流数据  # [English] ### Purpose: - Get live video data of specified user ### Parameters: - room_id: Room room_id ### Return: - Live stream data  # [示例/Example] room_id = \"7318296342189919011\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_videos_by_room_id_api_v1_douyin_web_fetch_user_live_videos_by_room_id_get(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间room_id/Room room_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_live_videos_by_room_id_api_v1_douyin_web_fetch_user_live_videos_by_room_id_get_with_http_info(room_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_live_videos_by_room_id_api_v1_douyin_web_fetch_user_live_videos_by_room_id_get_with_http_info(room_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_live_videos_by_room_id_api_v1_douyin_web_fetch_user_live_videos_by_room_id_get_with_http_info(self, room_id, **kwargs):  # noqa: E501
        """通过room_id获取指定用户的直播流数据 V1/Get live video data of specified user by room_id V1  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的直播流数据 ### 参数: - room_id: 直播间room_id ### 返回: - 直播流数据  # [English] ### Purpose: - Get live video data of specified user ### Parameters: - room_id: Room room_id ### Return: - Live stream data  # [示例/Example] room_id = \"7318296342189919011\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_videos_by_room_id_api_v1_douyin_web_fetch_user_live_videos_by_room_id_get_with_http_info(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间room_id/Room room_id (required)
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
                    " to method fetch_user_live_videos_by_room_id_api_v1_douyin_web_fetch_user_live_videos_by_room_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_user_live_videos_by_room_id_api_v1_douyin_web_fetch_user_live_videos_by_room_id_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_user_live_videos_by_room_id', 'GET',
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

    def fetch_user_live_videos_by_room_id_v2_api_v1_douyin_web_fetch_user_live_videos_by_room_id_v2_get(self, room_id, **kwargs):  # noqa: E501
        """通过room_id获取指定用户的直播流数据 V2/Gets the live stream data of the specified user by room_id V2  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的直播流数据V2 ### 参数: - room_id: 直播间room_id ### 返回: - 直播流数据 ### 备注: modify_time字段是直播间的最后更新时间，也就相当于开播时间，如果下播也不会重置回0，而是一直保持最后的更新时间。  # [English] ### Purpose: - Gets the live stream data of the specified user V2 ### Parameters: - room_id: Room room_id ### Return: - Live stream data ### Note: The modify_time field is the last update time of the live room, which is equivalent to the start time. If the live stream is offline, it will not be reset to 0, but will always maintain the last update time.  # [示例/Example] room_id = \"7462723839303093032\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_videos_by_room_id_v2_api_v1_douyin_web_fetch_user_live_videos_by_room_id_v2_get(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间room_id/Room room_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_live_videos_by_room_id_v2_api_v1_douyin_web_fetch_user_live_videos_by_room_id_v2_get_with_http_info(room_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_live_videos_by_room_id_v2_api_v1_douyin_web_fetch_user_live_videos_by_room_id_v2_get_with_http_info(room_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_live_videos_by_room_id_v2_api_v1_douyin_web_fetch_user_live_videos_by_room_id_v2_get_with_http_info(self, room_id, **kwargs):  # noqa: E501
        """通过room_id获取指定用户的直播流数据 V2/Gets the live stream data of the specified user by room_id V2  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的直播流数据V2 ### 参数: - room_id: 直播间room_id ### 返回: - 直播流数据 ### 备注: modify_time字段是直播间的最后更新时间，也就相当于开播时间，如果下播也不会重置回0，而是一直保持最后的更新时间。  # [English] ### Purpose: - Gets the live stream data of the specified user V2 ### Parameters: - room_id: Room room_id ### Return: - Live stream data ### Note: The modify_time field is the last update time of the live room, which is equivalent to the start time. If the live stream is offline, it will not be reset to 0, but will always maintain the last update time.  # [示例/Example] room_id = \"7462723839303093032\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_videos_by_room_id_v2_api_v1_douyin_web_fetch_user_live_videos_by_room_id_v2_get_with_http_info(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间room_id/Room room_id (required)
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
                    " to method fetch_user_live_videos_by_room_id_v2_api_v1_douyin_web_fetch_user_live_videos_by_room_id_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_user_live_videos_by_room_id_v2_api_v1_douyin_web_fetch_user_live_videos_by_room_id_v2_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_user_live_videos_by_room_id_v2', 'GET',
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

    def fetch_user_live_videos_by_sec_uid_api_v1_douyin_web_fetch_user_live_videos_by_sec_uid_get(self, sec_uid, **kwargs):  # noqa: E501
        """通过sec_uid获取指定用户的直播流数据/Get live video data of specified user by sec_uid  # noqa: E501

        # [中文] ### 用途: - 通过sec_uid获取指定用户的直播流数据 ### 参数: - sec_uid: 用户sec_uid，也叫 sec_user_id，可以在用户主页链接中找到。 ### 返回: - 直播流数据  # [English] ### Purpose - Get live video data of specified user by sec_uid ### Parameters - sec_uid: User sec_uid, also called sec_user_id, can be found in the user's homepage link. ### Return - Live stream data  # [示例/Example] sec_uid = \"MS4wLjABAAAAAIKOBr_x6p2fPVKOAhqG8LrC1lwwdWChifKEsl-TXFS-kGSGqpMBRexJdzoAfvUF\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_videos_by_sec_uid_api_v1_douyin_web_fetch_user_live_videos_by_sec_uid_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_uid/User sec_uid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_live_videos_by_sec_uid_api_v1_douyin_web_fetch_user_live_videos_by_sec_uid_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_live_videos_by_sec_uid_api_v1_douyin_web_fetch_user_live_videos_by_sec_uid_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_live_videos_by_sec_uid_api_v1_douyin_web_fetch_user_live_videos_by_sec_uid_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """通过sec_uid获取指定用户的直播流数据/Get live video data of specified user by sec_uid  # noqa: E501

        # [中文] ### 用途: - 通过sec_uid获取指定用户的直播流数据 ### 参数: - sec_uid: 用户sec_uid，也叫 sec_user_id，可以在用户主页链接中找到。 ### 返回: - 直播流数据  # [English] ### Purpose - Get live video data of specified user by sec_uid ### Parameters - sec_uid: User sec_uid, also called sec_user_id, can be found in the user's homepage link. ### Return - Live stream data  # [示例/Example] sec_uid = \"MS4wLjABAAAAAIKOBr_x6p2fPVKOAhqG8LrC1lwwdWChifKEsl-TXFS-kGSGqpMBRexJdzoAfvUF\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_videos_by_sec_uid_api_v1_douyin_web_fetch_user_live_videos_by_sec_uid_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_uid/User sec_uid (required)
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
                    " to method fetch_user_live_videos_by_sec_uid_api_v1_douyin_web_fetch_user_live_videos_by_sec_uid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_user_live_videos_by_sec_uid_api_v1_douyin_web_fetch_user_live_videos_by_sec_uid_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_user_live_videos_by_sec_uid', 'GET',
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

    def fetch_user_mix_videos_api_v1_douyin_web_fetch_user_mix_videos_get(self, mix_id, **kwargs):  # noqa: E501
        """获取用户合辑作品数据/Get user mix video data  # noqa: E501

        # [中文] ### 用途: - 获取用户合辑作品数据 ### 参数: - mix_id: 合辑id - max_cursor: 最大游标 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user mix video data ### Parameters: - mix_id: Mix id - max_cursor: Maximum cursor - count: Maximum number ### Return: - User video data  # [示例/Example] url = https://www.douyin.com/collection/7348687990509553679 mix_id = \"7348687990509553679\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_mix_videos_api_v1_douyin_web_fetch_user_mix_videos_get(mix_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mix_id: 合辑id/Mix id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object counts: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_mix_videos_api_v1_douyin_web_fetch_user_mix_videos_get_with_http_info(mix_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_mix_videos_api_v1_douyin_web_fetch_user_mix_videos_get_with_http_info(mix_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_mix_videos_api_v1_douyin_web_fetch_user_mix_videos_get_with_http_info(self, mix_id, **kwargs):  # noqa: E501
        """获取用户合辑作品数据/Get user mix video data  # noqa: E501

        # [中文] ### 用途: - 获取用户合辑作品数据 ### 参数: - mix_id: 合辑id - max_cursor: 最大游标 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user mix video data ### Parameters: - mix_id: Mix id - max_cursor: Maximum cursor - count: Maximum number ### Return: - User video data  # [示例/Example] url = https://www.douyin.com/collection/7348687990509553679 mix_id = \"7348687990509553679\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_mix_videos_api_v1_douyin_web_fetch_user_mix_videos_get_with_http_info(mix_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mix_id: 合辑id/Mix id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object counts: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mix_id', 'max_cursor', 'counts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_mix_videos_api_v1_douyin_web_fetch_user_mix_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mix_id' is set
        if self.api_client.client_side_validation and ('mix_id' not in params or
                                                       params['mix_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `mix_id` when calling `fetch_user_mix_videos_api_v1_douyin_web_fetch_user_mix_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mix_id' in params:
            query_params.append(('mix_id', params['mix_id']))  # noqa: E501
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
            '/api/v1/douyin/web/fetch_user_mix_videos', 'GET',
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

    def fetch_user_post_videos_api_v1_douyin_web_fetch_user_post_videos_get(self, sec_user_id, **kwargs):  # noqa: E501
        """获取用户主页作品数据/Get user homepage video data  # noqa: E501

        # [中文] ### 用途: - 获取用户主页作品数据 - 注意：请尽量使用APP的接口而不是WEB的接口，因为WEB的接口可能会被不稳定。 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 翻页游标，第一次请求传0，然后每次请求传上一次请求返回的max_cursor进行翻页。 - count: 最大数量，建议不要超过20 - filter_type: 过滤类型，可选参数如下：     - 0: 默认排序     - 3: 热度排序 - cookie: 用户网页版抖音Cookie(此接口可以接受用户提供自己的Cookie) ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data - Note: Please try to use the APP interface instead of the WEB API, because the WEB API may be unstable. ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by the previous request for paging each time. - count: Maximum count number, it is recommended not to exceed 20 - filter_type: Filter type, optional parameters are as follows:     - 0: Default sorting     - 3: Sort by popularity - cookie: User's web version of Douyin Cookie (This interface can accept users to provide their own Cookie) ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\" max_cursor = \"0\" counts = 20 filter_type = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_api_v1_douyin_web_fetch_user_post_videos_get(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object count: 每页数量/Number per page
        :param object filter_type: 过滤类型/Filter type
        :param object cookie: 用户网页版抖音Cookie/Your web version of Douyin Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_post_videos_api_v1_douyin_web_fetch_user_post_videos_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_videos_api_v1_douyin_web_fetch_user_post_videos_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_post_videos_api_v1_douyin_web_fetch_user_post_videos_get_with_http_info(self, sec_user_id, **kwargs):  # noqa: E501
        """获取用户主页作品数据/Get user homepage video data  # noqa: E501

        # [中文] ### 用途: - 获取用户主页作品数据 - 注意：请尽量使用APP的接口而不是WEB的接口，因为WEB的接口可能会被不稳定。 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 翻页游标，第一次请求传0，然后每次请求传上一次请求返回的max_cursor进行翻页。 - count: 最大数量，建议不要超过20 - filter_type: 过滤类型，可选参数如下：     - 0: 默认排序     - 3: 热度排序 - cookie: 用户网页版抖音Cookie(此接口可以接受用户提供自己的Cookie) ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data - Note: Please try to use the APP interface instead of the WEB API, because the WEB API may be unstable. ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by the previous request for paging each time. - count: Maximum count number, it is recommended not to exceed 20 - filter_type: Filter type, optional parameters are as follows:     - 0: Default sorting     - 3: Sort by popularity - cookie: User's web version of Douyin Cookie (This interface can accept users to provide their own Cookie) ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\" max_cursor = \"0\" counts = 20 filter_type = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_api_v1_douyin_web_fetch_user_post_videos_get_with_http_info(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object count: 每页数量/Number per page
        :param object filter_type: 过滤类型/Filter type
        :param object cookie: 用户网页版抖音Cookie/Your web version of Douyin Cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'max_cursor', 'count', 'filter_type', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_post_videos_api_v1_douyin_web_fetch_user_post_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_user_id' is set
        if self.api_client.client_side_validation and ('sec_user_id' not in params or
                                                       params['sec_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_id` when calling `fetch_user_post_videos_api_v1_douyin_web_fetch_user_post_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'max_cursor' in params:
            query_params.append(('max_cursor', params['max_cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'filter_type' in params:
            query_params.append(('filter_type', params['filter_type']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_user_post_videos', 'GET',
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

    def fetch_user_profile_by_short_id_api_v1_douyin_web_fetch_user_profile_by_short_id_get(self, short_id, **kwargs):  # noqa: E501
        """使用Short ID获取用户信息/Get user information by Short ID  # noqa: E501

        # [中文] ### 用途: - 使用Short ID获取用户信息 ### 参数: - short_id: 用户Short ID ### 返回: - 用户信息  # [English] ### Purpose: - Get user information by Short ID ### Parameters: - short_id: User Short ID ### Return: - User information  # [示例/Example] short_id = \"114131058\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_by_short_id_api_v1_douyin_web_fetch_user_profile_by_short_id_get(short_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object short_id: 用户Short ID/User Short ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_profile_by_short_id_api_v1_douyin_web_fetch_user_profile_by_short_id_get_with_http_info(short_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_profile_by_short_id_api_v1_douyin_web_fetch_user_profile_by_short_id_get_with_http_info(short_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_profile_by_short_id_api_v1_douyin_web_fetch_user_profile_by_short_id_get_with_http_info(self, short_id, **kwargs):  # noqa: E501
        """使用Short ID获取用户信息/Get user information by Short ID  # noqa: E501

        # [中文] ### 用途: - 使用Short ID获取用户信息 ### 参数: - short_id: 用户Short ID ### 返回: - 用户信息  # [English] ### Purpose: - Get user information by Short ID ### Parameters: - short_id: User Short ID ### Return: - User information  # [示例/Example] short_id = \"114131058\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_by_short_id_api_v1_douyin_web_fetch_user_profile_by_short_id_get_with_http_info(short_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object short_id: 用户Short ID/User Short ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['short_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_profile_by_short_id_api_v1_douyin_web_fetch_user_profile_by_short_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'short_id' is set
        if self.api_client.client_side_validation and ('short_id' not in params or
                                                       params['short_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `short_id` when calling `fetch_user_profile_by_short_id_api_v1_douyin_web_fetch_user_profile_by_short_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'short_id' in params:
            query_params.append(('short_id', params['short_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_user_profile_by_short_id', 'GET',
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

    def fetch_user_profile_by_uid_api_v1_douyin_web_fetch_user_profile_by_uid_get(self, uid, **kwargs):  # noqa: E501
        """使用UID获取用户信息/Get user information by UID  # noqa: E501

        # [中文] ### 用途: - 使用UID获取用户信息 ### 参数: - uid: 用户UID ### 返回: - 用户信息  # [English] ### Purpose: - Get user information by UID ### Parameters: - uid: User UID ### Return: - User information  # [示例/Example] uid = \"68141954464\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_by_uid_api_v1_douyin_web_fetch_user_profile_by_uid_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户UID/User UID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_profile_by_uid_api_v1_douyin_web_fetch_user_profile_by_uid_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_profile_by_uid_api_v1_douyin_web_fetch_user_profile_by_uid_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_profile_by_uid_api_v1_douyin_web_fetch_user_profile_by_uid_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """使用UID获取用户信息/Get user information by UID  # noqa: E501

        # [中文] ### 用途: - 使用UID获取用户信息 ### 参数: - uid: 用户UID ### 返回: - 用户信息  # [English] ### Purpose: - Get user information by UID ### Parameters: - uid: User UID ### Return: - User information  # [示例/Example] uid = \"68141954464\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_by_uid_api_v1_douyin_web_fetch_user_profile_by_uid_get_with_http_info(uid, async_req=True)
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
                    " to method fetch_user_profile_by_uid_api_v1_douyin_web_fetch_user_profile_by_uid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_profile_by_uid_api_v1_douyin_web_fetch_user_profile_by_uid_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_user_profile_by_uid', 'GET',
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

    def fetch_user_search_result_api_v1_douyin_web_fetch_user_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的用户搜索结果(废弃，替代接口请参考下方文档)/Get user search results of specified keywords (deprecated, please refer to the following document for replacement interface)  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212785e0 ### 用途: - 获取指定关键词的用户搜索结果 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212785e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 - douyin_user_fans: 留空:不限, \"0_1k\": 1000以下, \"1k_1w\": 1000-1万, \"1w_10w\": 1w-10w, \"10w_100w\": 10w-100w，\"100w_\": 100w以上 - douyin_user_type: 留空:不限, \"common_user\": 普通用户, \"enterprise_user\": 企业认证, \"personal_user\": 个人认证 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 用户搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212785e0 ### Purpose: - Get user search results of specified keywords - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212785e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number - douyin_user_fans: Leave blank: Unlimited, \"0_1k\": Below 1000, \"1k_1w\": 1000-10,000, \"1w_10w\": 10,000-100,000, \"10w_100w\": 100,000-1 million, \"100w_\": More than 1 million - douyin_user_type: Leave blank: Unlimited, \"common_user\": Ordinary user, \"enterprise_user\": Enterprise certification, \"personal_user\": Personal certification - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - User search results  # [示例/Example] keyword = \"动漫\" offset = 0 count = 20 douyin_user_fans = \"\" douyin_user_type = \"\" search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_result_api_v1_douyin_web_fetch_user_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object douyin_user_fans: 粉丝数/Fans
        :param object douyin_user_type: 用户类型/User type
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_search_result_api_v1_douyin_web_fetch_user_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_search_result_api_v1_douyin_web_fetch_user_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_user_search_result_api_v1_douyin_web_fetch_user_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的用户搜索结果(废弃，替代接口请参考下方文档)/Get user search results of specified keywords (deprecated, please refer to the following document for replacement interface)  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212785e0 ### 用途: - 获取指定关键词的用户搜索结果 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212785e0 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 - douyin_user_fans: 留空:不限, \"0_1k\": 1000以下, \"1k_1w\": 1000-1万, \"1w_10w\": 1w-10w, \"10w_100w\": 10w-100w，\"100w_\": 100w以上 - douyin_user_type: 留空:不限, \"common_user\": 普通用户, \"enterprise_user\": 企业认证, \"personal_user\": 个人认证 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 用户搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212785e0 ### Purpose: - Get user search results of specified keywords - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212785e0 ### Parameters: - keyword: Keyword - offset: Offset - count: Number - douyin_user_fans: Leave blank: Unlimited, \"0_1k\": Below 1000, \"1k_1w\": 1000-10,000, \"1w_10w\": 10,000-100,000, \"10w_100w\": 100,000-1 million, \"100w_\": More than 1 million - douyin_user_type: Leave blank: Unlimited, \"common_user\": Ordinary user, \"enterprise_user\": Enterprise certification, \"personal_user\": Personal certification - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - User search results  # [示例/Example] keyword = \"动漫\" offset = 0 count = 20 douyin_user_fans = \"\" douyin_user_type = \"\" search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_result_api_v1_douyin_web_fetch_user_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object douyin_user_fans: 粉丝数/Fans
        :param object douyin_user_type: 用户类型/User type
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'douyin_user_fans', 'douyin_user_type', 'search_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_search_result_api_v1_douyin_web_fetch_user_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_user_search_result_api_v1_douyin_web_fetch_user_search_result_get`")  # noqa: E501

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
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_user_search_result', 'GET',
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

    def fetch_user_search_result_v2_api_v1_douyin_web_fetch_user_search_result_v2_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的用户搜索结果 V2 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V2 (deprecated, please refer to the following document for replacement interface)  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212785e0 ### 用途: - 获取指定关键词的用户搜索结果V2 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212785e0 ### 参数: - keyword: 关键词 - cursor: 游标，第一次请求时为0，后续从返回数据中获取，用于翻页。 ### 返回: - 用户搜索结果V2  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212785e0 ### Purpose: - Get user search results of specified keywords V2 - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212785e0 ### Parameters: - keyword: Keyword - cursor: Cursor, 0 for the first request, get from the returned data later, used for paging. ### Return: - User search results V2  # [示例/Example] keyword = \"中华娘\" cursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_result_v2_api_v1_douyin_web_fetch_user_search_result_v2_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_search_result_v2_api_v1_douyin_web_fetch_user_search_result_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_search_result_v2_api_v1_douyin_web_fetch_user_search_result_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_user_search_result_v2_api_v1_douyin_web_fetch_user_search_result_v2_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的用户搜索结果 V2 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V2 (deprecated, please refer to the following document for replacement interface)  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212785e0 ### 用途: - 获取指定关键词的用户搜索结果V2 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212785e0 ### 参数: - keyword: 关键词 - cursor: 游标，第一次请求时为0，后续从返回数据中获取，用于翻页。 ### 返回: - 用户搜索结果V2  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212785e0 ### Purpose: - Get user search results of specified keywords V2 - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212785e0 ### Parameters: - keyword: Keyword - cursor: Cursor, 0 for the first request, get from the returned data later, used for paging. ### Return: - User search results V2  # [示例/Example] keyword = \"中华娘\" cursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_result_v2_api_v1_douyin_web_fetch_user_search_result_v2_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object cursor: 游标/Cursor
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
                    " to method fetch_user_search_result_v2_api_v1_douyin_web_fetch_user_search_result_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_user_search_result_v2_api_v1_douyin_web_fetch_user_search_result_v2_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_user_search_result_v2', 'GET',
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

    def fetch_user_search_result_v3_api_v1_douyin_web_fetch_user_search_result_v3_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的用户搜索结果 V3 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V3 (deprecated, please refer to the following document for replacement interface)  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212785e0 ### 用途: - 获取指定关键词的用户搜索结果 V3 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212785e0 ### 参数: - keyword: 关键词 - cursor: 偏移量 - douyin_user_fans: 留空:不限, \"0_1k\": 1000以下, \"1k_1w\": 1000-1万, \"1w_10w\": 1w-10w, \"10w_100w\": 10w-100w，\"100w_\": 100w以上 - douyin_user_type: 留空:不限, \"common_user\": 普通用户, \"enterprise_user\": 企业认证, \"personal_user\": 个人认证 ### 返回: - 用户搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212785e0 ### Purpose: - Get user search results of specified keywords V3 - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212785e0 ### Parameters: - keyword: Keyword - cursor: Offset - douyin_user_fans: Leave blank: Unlimited, \"0_1k\": Below 1000, \"1k_1w\": 1000-10,000, \"1w_10w\": 10,000-100,000, \"10w_100w\": 100,000-1 million, \"100w_\": More than 1 million - douyin_user_type: Leave blank: Unlimited, \"common_user\": Ordinary user, \"enterprise_user\": Enterprise certification, \"personal_user\": Personal certification ### Return: - User search results  # [示例/Example] keyword = \"中华娘\" cursor = \"0\" douyin_user_fans = \"\" douyin_user_type = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_result_v3_api_v1_douyin_web_fetch_user_search_result_v3_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object cursor: 游标/Cursor
        :param object douyin_user_type: 用户类型/User type
        :param object douyin_user_fans: 粉丝数/Fans
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_search_result_v3_api_v1_douyin_web_fetch_user_search_result_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_search_result_v3_api_v1_douyin_web_fetch_user_search_result_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_user_search_result_v3_api_v1_douyin_web_fetch_user_search_result_v3_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的用户搜索结果 V3 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V3 (deprecated, please refer to the following document for replacement interface)  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212785e0 ### 用途: - 获取指定关键词的用户搜索结果 V3 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212785e0 ### 参数: - keyword: 关键词 - cursor: 偏移量 - douyin_user_fans: 留空:不限, \"0_1k\": 1000以下, \"1k_1w\": 1000-1万, \"1w_10w\": 1w-10w, \"10w_100w\": 10w-100w，\"100w_\": 100w以上 - douyin_user_type: 留空:不限, \"common_user\": 普通用户, \"enterprise_user\": 企业认证, \"personal_user\": 个人认证 ### 返回: - 用户搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212785e0 ### Purpose: - Get user search results of specified keywords V3 - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212785e0 ### Parameters: - keyword: Keyword - cursor: Offset - douyin_user_fans: Leave blank: Unlimited, \"0_1k\": Below 1000, \"1k_1w\": 1000-10,000, \"1w_10w\": 10,000-100,000, \"10w_100w\": 100,000-1 million, \"100w_\": More than 1 million - douyin_user_type: Leave blank: Unlimited, \"common_user\": Ordinary user, \"enterprise_user\": Enterprise certification, \"personal_user\": Personal certification ### Return: - User search results  # [示例/Example] keyword = \"中华娘\" cursor = \"0\" douyin_user_fans = \"\" douyin_user_type = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_result_v3_api_v1_douyin_web_fetch_user_search_result_v3_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object cursor: 游标/Cursor
        :param object douyin_user_type: 用户类型/User type
        :param object douyin_user_fans: 粉丝数/Fans
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'cursor', 'douyin_user_type', 'douyin_user_fans']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_search_result_v3_api_v1_douyin_web_fetch_user_search_result_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_user_search_result_v3_api_v1_douyin_web_fetch_user_search_result_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'douyin_user_type' in params:
            query_params.append(('douyin_user_type', params['douyin_user_type']))  # noqa: E501
        if 'douyin_user_fans' in params:
            query_params.append(('douyin_user_fans', params['douyin_user_fans']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_user_search_result_v3', 'GET',
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

    def fetch_video_channel_result_api_v1_douyin_web_fetch_video_channel_result_get(self, tag_id, **kwargs):  # noqa: E501
        """抖音视频频道数据/Douyin video channel data  # noqa: E501

        # [中文] ### 用途: - 抖音视频频道数据 - https://www.douyin.com/channel/300205 ### 参数: - tag_id: 标签id，从URL中获取 - count: 数量 - refresh_index: 刷新索引 ### 返回: - 视频频道数据  # [English] ### Purpose: - Douyin video channel data - https://www.douyin.com/channel/300205 ### Parameters: - tag_id: Tag id, get from the URL - count: Number - refresh_index: Refresh index ### Return: - Video channel data  # [示例/Example] tag_id = 300203 count = 10 refresh_index = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_channel_result_api_v1_douyin_web_fetch_video_channel_result_get(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tag_id: 标签id/Tag id (required)
        :param object count: 数量/Number
        :param object refresh_index: 刷新索引/Refresh index
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_channel_result_api_v1_douyin_web_fetch_video_channel_result_get_with_http_info(tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_channel_result_api_v1_douyin_web_fetch_video_channel_result_get_with_http_info(tag_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_channel_result_api_v1_douyin_web_fetch_video_channel_result_get_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """抖音视频频道数据/Douyin video channel data  # noqa: E501

        # [中文] ### 用途: - 抖音视频频道数据 - https://www.douyin.com/channel/300205 ### 参数: - tag_id: 标签id，从URL中获取 - count: 数量 - refresh_index: 刷新索引 ### 返回: - 视频频道数据  # [English] ### Purpose: - Douyin video channel data - https://www.douyin.com/channel/300205 ### Parameters: - tag_id: Tag id, get from the URL - count: Number - refresh_index: Refresh index ### Return: - Video channel data  # [示例/Example] tag_id = 300203 count = 10 refresh_index = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_channel_result_api_v1_douyin_web_fetch_video_channel_result_get_with_http_info(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tag_id: 标签id/Tag id (required)
        :param object count: 数量/Number
        :param object refresh_index: 刷新索引/Refresh index
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id', 'count', 'refresh_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_channel_result_api_v1_douyin_web_fetch_video_channel_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if self.api_client.client_side_validation and ('tag_id' not in params or
                                                       params['tag_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tag_id` when calling `fetch_video_channel_result_api_v1_douyin_web_fetch_video_channel_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag_id' in params:
            query_params.append(('tag_id', params['tag_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'refresh_index' in params:
            query_params.append(('refresh_index', params['refresh_index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_video_channel_result', 'GET',
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

    def fetch_video_comments_api_v1_douyin_web_fetch_video_comments_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个视频评论数据/Get single video comments data  # noqa: E501

        # [中文] ### 用途: - 获取单个视频评论数据 ### 参数: - aweme_id: 作品id - cursor: 游标 - count: 数量 ### 返回: - 评论数据  # [English] ### Purpose: - Get single video comments data ### Parameters: - aweme_id: Video id - cursor: Cursor - count: Number ### Return: - Comments data  # [示例/Example] aweme_id = \"7372484719365098803\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_api_v1_douyin_web_fetch_video_comments_get(aweme_id, async_req=True)
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
            return self.fetch_video_comments_api_v1_douyin_web_fetch_video_comments_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_comments_api_v1_douyin_web_fetch_video_comments_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_comments_api_v1_douyin_web_fetch_video_comments_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个视频评论数据/Get single video comments data  # noqa: E501

        # [中文] ### 用途: - 获取单个视频评论数据 ### 参数: - aweme_id: 作品id - cursor: 游标 - count: 数量 ### 返回: - 评论数据  # [English] ### Purpose: - Get single video comments data ### Parameters: - aweme_id: Video id - cursor: Cursor - count: Number ### Return: - Comments data  # [示例/Example] aweme_id = \"7372484719365098803\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_api_v1_douyin_web_fetch_video_comments_get_with_http_info(aweme_id, async_req=True)
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
                    " to method fetch_video_comments_api_v1_douyin_web_fetch_video_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_video_comments_api_v1_douyin_web_fetch_video_comments_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_video_comments', 'GET',
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

    def fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get(self, item_id, comment_id, **kwargs):  # noqa: E501
        """获取指定视频的评论回复数据/Get comment replies data of specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的评论回复数据 ### 参数: - item_id: 作品id - comment_id: 评论id - cursor: 游标 - count: 数量 ### 返回: - 评论回复数据  # [English] ### Purpose: - Get comment replies data of specified video ### Parameters: - item_id: Video id - comment_id: Comment id - cursor: Cursor - count: Number ### Return: - Comment replies data  # [示例/Example] aweme_id = \"7354666303006723354\" comment_id = \"7354669356632638218\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get(item_id, comment_id, async_req=True)
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
            return self.fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get_with_http_info(self, item_id, comment_id, **kwargs):  # noqa: E501
        """获取指定视频的评论回复数据/Get comment replies data of specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的评论回复数据 ### 参数: - item_id: 作品id - comment_id: 评论id - cursor: 游标 - count: 数量 ### 返回: - 评论回复数据  # [English] ### Purpose: - Get comment replies data of specified video ### Parameters: - item_id: Video id - comment_id: Comment id - cursor: Cursor - count: Number ### Return: - Comment replies data  # [示例/Example] aweme_id = \"7354666303006723354\" comment_id = \"7354669356632638218\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get_with_http_info(item_id, comment_id, async_req=True)
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
                    " to method fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_video_comment_replies', 'GET',
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

    def fetch_video_high_quality_play_url_api_v1_douyin_web_fetch_video_high_quality_play_url_get(self, **kwargs):  # noqa: E501
        """获取视频的最高画质播放链接/Get the highest quality play URL of the video  # noqa: E501

        # [中文] ### 用途: - 价格：0.005$ 一次。 - 获取视频的最高画质(原始上传画质)播放链接 - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。 - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。 - 此接口非常适合用于获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。 - 一般情况都可以在线播放，如果不行，可以尝试使用IDM或浏览器下载后播放。 ### 参数: - aweme_id: 作品id，优先使用aweme_id，如果没有则使用share_url。 - share_url: 可选，分享链接，如果提供了作品id，则此参数可以不传。 ### 返回: - video_id： 作品id - original_video_url： 最高画质(原始上传画质)播放链接 - video_data： 视频数据，包含视频的元数据，如时长、大小等。  # [English] ### Purpose: - Price: 0.005$ each time. - Get the highest quality (original upload quality) play URL of the video - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata. - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface. - This interface is very suitable for obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc. - Generally, it can be played online, if not, you can try to download it using IDM or a browser and then play it. ### Parameters: - aweme_id: Video id, prefer to use aweme_id, if not available, use share_url. - share_url: Optional, share link, if the video id is provided, this parameter can be omitted. ### Return: - video_id: Video id - original_video_url: Highest quality (original upload quality) play URL - video_data: Video data, including metadata such as duration, size, etc. # [示例/Example] aweme_id = \"7512756548356492544\" share_url = \"https://www.douyin.com/video/7512756548356492544\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_high_quality_play_url_api_v1_douyin_web_fetch_video_high_quality_play_url_get(async_req=True)
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
            return self.fetch_video_high_quality_play_url_api_v1_douyin_web_fetch_video_high_quality_play_url_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_high_quality_play_url_api_v1_douyin_web_fetch_video_high_quality_play_url_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_video_high_quality_play_url_api_v1_douyin_web_fetch_video_high_quality_play_url_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取视频的最高画质播放链接/Get the highest quality play URL of the video  # noqa: E501

        # [中文] ### 用途: - 价格：0.005$ 一次。 - 获取视频的最高画质(原始上传画质)播放链接 - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。 - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。 - 此接口非常适合用于获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。 - 一般情况都可以在线播放，如果不行，可以尝试使用IDM或浏览器下载后播放。 ### 参数: - aweme_id: 作品id，优先使用aweme_id，如果没有则使用share_url。 - share_url: 可选，分享链接，如果提供了作品id，则此参数可以不传。 ### 返回: - video_id： 作品id - original_video_url： 最高画质(原始上传画质)播放链接 - video_data： 视频数据，包含视频的元数据，如时长、大小等。  # [English] ### Purpose: - Price: 0.005$ each time. - Get the highest quality (original upload quality) play URL of the video - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata. - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface. - This interface is very suitable for obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc. - Generally, it can be played online, if not, you can try to download it using IDM or a browser and then play it. ### Parameters: - aweme_id: Video id, prefer to use aweme_id, if not available, use share_url. - share_url: Optional, share link, if the video id is provided, this parameter can be omitted. ### Return: - video_id: Video id - original_video_url: Highest quality (original upload quality) play URL - video_data: Video data, including metadata such as duration, size, etc. # [示例/Example] aweme_id = \"7512756548356492544\" share_url = \"https://www.douyin.com/video/7512756548356492544\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_high_quality_play_url_api_v1_douyin_web_fetch_video_high_quality_play_url_get_with_http_info(async_req=True)
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
                    " to method fetch_video_high_quality_play_url_api_v1_douyin_web_fetch_video_high_quality_play_url_get" % key
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
            '/api/v1/douyin/web/fetch_video_high_quality_play_url', 'GET',
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

    def fetch_video_search_result_api_v1_douyin_web_fetch_video_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 获取指定关键词的视频搜索结果/Get video search results of specified keywords  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212780e0 ### 用途: - 获取指定关键词的视频搜索结果，此接口有概率失败，如果失败请使用同样的参数重新请求 1-3次，目前的失败率在5%以下。 - 此接口收费相较于其他搜索接口便宜，但是稳定性差，需要配合重试机制使用。 - 请求价格：0.001$ / 次 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212780e0 ### 参数: - keyword: 关键词 - offset: 偏移量，第一次请求时为0，后续从返回数据中获取，用于翻页。     - 例如: offset = 10     - JSON Path-1 : $.data.cursor - count: 数量，默认为10，建议保持不变。 - sort_type:     - 0:综合排序     - 1:最多点赞     - 2:最新发布 - publish_time:     - 0:不限     - 1:最近一天     - 7:最近一周     - 180:最近半年 - filter_duration:     - 0:不限 0-1:1分钟以内     - 1-5:1-5分钟     - 5-10000:5分钟以上 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 视频搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212780e0 ### Purpose: - Get video search results of specified keywords, this interface may fail, if it fails, please use the same parameters to request 1-3 times again, the current failure rate is below 5%. - This interface is cheaper than other search interfaces, but the stability is poor and needs to be used with a retry mechanism. - Request price: 0.001$ / time - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212780e0 ### Parameters: - keyword: Keyword - offset: Offset, 0 for the first request, get from the returned data later, used for paging.     - For example: offset = 10     - JSON Path-1 : $.data.cursor - count: Number, default is 10, it is recommended to keep it unchanged. - sort_type:     - 0: Comprehensive sorting     - 1: Most likes     - 2: Latest release - publish_time:     - 0: Unlimited     - 1: Last day     - 7: Last week     - 180: Last half year - filter_duration:     - 0: Unlimited     - 0-1: Within 1 minute     - 1-5: 1-5 minutes     - 5-10000: More than 5 minutes - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - Video search results  # [示例/Example] keyword = \"游戏\" offset = 0 count = 10 sort_type = \"0\" publish_time = \"0\" filter_duration = \"0\" search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_result_api_v1_douyin_web_fetch_video_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object filter_duration: 视频时长/Duration filter
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_search_result_api_v1_douyin_web_fetch_video_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_search_result_api_v1_douyin_web_fetch_video_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_video_search_result_api_v1_douyin_web_fetch_video_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 获取指定关键词的视频搜索结果/Get video search results of specified keywords  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212780e0 ### 用途: - 获取指定关键词的视频搜索结果，此接口有概率失败，如果失败请使用同样的参数重新请求 1-3次，目前的失败率在5%以下。 - 此接口收费相较于其他搜索接口便宜，但是稳定性差，需要配合重试机制使用。 - 请求价格：0.001$ / 次 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212780e0 ### 参数: - keyword: 关键词 - offset: 偏移量，第一次请求时为0，后续从返回数据中获取，用于翻页。     - 例如: offset = 10     - JSON Path-1 : $.data.cursor - count: 数量，默认为10，建议保持不变。 - sort_type:     - 0:综合排序     - 1:最多点赞     - 2:最新发布 - publish_time:     - 0:不限     - 1:最近一天     - 7:最近一周     - 180:最近半年 - filter_duration:     - 0:不限 0-1:1分钟以内     - 1-5:1-5分钟     - 5-10000:5分钟以上 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 视频搜索结果  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212780e0 ### Purpose: - Get video search results of specified keywords, this interface may fail, if it fails, please use the same parameters to request 1-3 times again, the current failure rate is below 5%. - This interface is cheaper than other search interfaces, but the stability is poor and needs to be used with a retry mechanism. - Request price: 0.001$ / time - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212780e0 ### Parameters: - keyword: Keyword - offset: Offset, 0 for the first request, get from the returned data later, used for paging.     - For example: offset = 10     - JSON Path-1 : $.data.cursor - count: Number, default is 10, it is recommended to keep it unchanged. - sort_type:     - 0: Comprehensive sorting     - 1: Most likes     - 2: Latest release - publish_time:     - 0: Unlimited     - 1: Last day     - 7: Last week     - 180: Last half year - filter_duration:     - 0: Unlimited     - 0-1: Within 1 minute     - 1-5: 1-5 minutes     - 5-10000: More than 5 minutes - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - Video search results  # [示例/Example] keyword = \"游戏\" offset = 0 count = 10 sort_type = \"0\" publish_time = \"0\" filter_duration = \"0\" search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_result_api_v1_douyin_web_fetch_video_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object filter_duration: 视频时长/Duration filter
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'sort_type', 'publish_time', 'filter_duration', 'search_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_search_result_api_v1_douyin_web_fetch_video_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_video_search_result_api_v1_douyin_web_fetch_video_search_result_get`")  # noqa: E501

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
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/fetch_video_search_result', 'GET',
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

    def fetch_video_search_result_v2_api_v1_douyin_web_fetch_video_search_result_v2_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的视频搜索结果 V2 （废弃，替代接口请参考下方文档）/Get video search results of specified keywords V2 (Deprecated, please refer to the following document for replacement interface)  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212780e0 ### 用途: - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。 - 收费标准为：0.01$每次请求。 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212780e0 ### 参数: - keyword: 关键词 - sort_type:     - 排序类型，可用值如下：     - _0 :综合(General)     - _1 :最多点赞(More likes)     - _2 :最新发布(New) - publish_time：     - 发布时间，可用值如下：     - _0 :不限(No Limit)     - _1 :一天之内(last 1 day)     - _7 :一周之内(last 1 week)     - _180 :半年之内(last half year) - filter_duration：     - 视频时长，可用值如下：     - _0 :不限(No Limit)     - _1 :1分钟以下(1 minute and below)     - _2 :1-5分钟 (1-5 minutes)     - _3 :5分钟以上(5 minutes more) - page: 页码     - 默认从1开始，然后依次递增加1 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 视频搜索结果V2  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212780e0 ### Purpose: - Get video search results of specified keywords V2, this interface has better stability and higher cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is recommended to use this interface. - The charging standard is: $0.01 per request. - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212780e0 ### Parameters: - keyword: Keyword - sort_type:     - Sort type, available values are as follows:     - _0 : General     - _1 : More likes     - _2 : New - publish_time:     - Publish time, available values are as follows:     - _0 : No Limit     - _1 : last 1 day     - _7 : last 1 week     - _180 : last half year - filter_duration:     - Duration filter, available values are as follows:     - _0 : No Limit     - _1 : 1 minute and below     - _2 : 1-5 minutes     - _3 : 5 minutes more - page: Page     - Start from 1 by default, then increase by 1 each time - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - Video search results V2  # [示例/Example] keyword = \"中华娘\" sort_type = \"_0\" publish_time = \"_0\" filter_duration = \"_0\" page = 1 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_result_v2_api_v1_douyin_web_fetch_video_search_result_v2_get(keyword, async_req=True)
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
            return self.fetch_video_search_result_v2_api_v1_douyin_web_fetch_video_search_result_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_search_result_v2_api_v1_douyin_web_fetch_video_search_result_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_video_search_result_v2_api_v1_douyin_web_fetch_video_search_result_v2_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的视频搜索结果 V2 （废弃，替代接口请参考下方文档）/Get video search results of specified keywords V2 (Deprecated, please refer to the following document for replacement interface)  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212780e0 ### 用途: - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。 - 收费标准为：0.01$每次请求。 - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212780e0 ### 参数: - keyword: 关键词 - sort_type:     - 排序类型，可用值如下：     - _0 :综合(General)     - _1 :最多点赞(More likes)     - _2 :最新发布(New) - publish_time：     - 发布时间，可用值如下：     - _0 :不限(No Limit)     - _1 :一天之内(last 1 day)     - _7 :一周之内(last 1 week)     - _180 :半年之内(last half year) - filter_duration：     - 视频时长，可用值如下：     - _0 :不限(No Limit)     - _1 :1分钟以下(1 minute and below)     - _2 :1-5分钟 (1-5 minutes)     - _3 :5分钟以上(5 minutes more) - page: 页码     - 默认从1开始，然后依次递增加1 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### 返回: - 视频搜索结果V2  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212780e0 ### Purpose: - Get video search results of specified keywords V2, this interface has better stability and higher cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is recommended to use this interface. - The charging standard is: $0.01 per request. - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212780e0 ### Parameters: - keyword: Keyword - sort_type:     - Sort type, available values are as follows:     - _0 : General     - _1 : More likes     - _2 : New - publish_time:     - Publish time, available values are as follows:     - _0 : No Limit     - _1 : last 1 day     - _7 : last 1 week     - _180 : last half year - filter_duration:     - Duration filter, available values are as follows:     - _0 : No Limit     - _1 : 1 minute and below     - _2 : 1-5 minutes     - _3 : 5 minutes more - page: Page     - Start from 1 by default, then increase by 1 each time - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id ### Return: - Video search results V2  # [示例/Example] keyword = \"中华娘\" sort_type = \"_0\" publish_time = \"_0\" filter_duration = \"_0\" page = 1 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_result_v2_api_v1_douyin_web_fetch_video_search_result_v2_get_with_http_info(keyword, async_req=True)
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
                    " to method fetch_video_search_result_v2_api_v1_douyin_web_fetch_video_search_result_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_video_search_result_v2_api_v1_douyin_web_fetch_video_search_result_v2_get`")  # noqa: E501

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
            '/api/v1/douyin/web/fetch_video_search_result_v2', 'GET',
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

    def generate_a_bogus_api_v1_douyin_web_generate_a_bogus_post(self, **kwargs):  # noqa: E501
        """使用接口网址生成A-Bogus参数/Generate A-Bogus parameter using API URL  # noqa: E501

        # [中文] ### 用途: - 使用接口网址生成A-Bogus参数，提交的URL不能带有a_bogus参数，同时a_bogus参数与请求头中的User-Agent有关，需要一起提交和请求。 ### 参数: - url: API链接，请去除url中的原本的a_boogus参数(如有)。 - data: 请求载荷，只有在POST请求中才需要提交，GET请求中使用空字符串即可。 - user_agent: user-agent，需要提交你请求头中的User-Agent，该值参与a_bogus参数的计算。 - index_0: 加密明文列表的第一个值，无特殊要求，默认为0，不要随意修改。 - index_1: 加密明文列表的第二个值，无特殊要求，默认为1，不要随意修改。 - index_2: 加密明文列表的第三个值，无特殊要求，默认为14，不要随意修改。 ### 返回: - A-Bogus参数  # [English] ### Purpose: - Generate A-Bogus parameter using API URL, the submitted URL cannot contain the original a_boogus parameter, and the a_bogus parameter is related to the User-Agent in the request header, which needs to be submitted and requested together. ### Parameters: - url: API link, please remove the original a_boogus parameter from the url (if any). - data: Request payload, only need to submit in POST request, use an empty string in GET request. - user_agent: user-agent, you need to submit the User-Agent in your request header, which is involved in the calculation of the a_bogus parameter. - index_0: The first value of the encrypted plaintext list, no special requirements, the default is 0, do not modify it at will. - index_1: The second value of the encrypted plaintext list, no special requirements, the default is 1, do not modify it at will. - index_2: The third value of the encrypted plaintext list, no special requirements, the default is 14, do not modify it at will. ### Return: - A-Bogus parameter  # [示例/Example] ```json { \"url\": \"https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&enable_history=1&keyword=%E4%B8%AD%E5%8D%8E%E5%A8%98&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=7346905902554844468&offset=0&count=15&need_filter_settings=1&pc_client_type=1&version_code=190600&version_name=19.6.0&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platform=Win32&browser_name=Firefox&browser_version=124.0&browser_online=true&engine_name=Gecko&engine_version=124.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=&platform=PC&webid=7348962975497324070&msToken=YCTVM6YGmjFdIpQAN9ykXLBXiSiuHdZkOkEQWTeqVOHBEPmOcM0lNwE0Kd9vgHPMPigSndZDHfAq9k-6lDmH3Jqz6mHHxmn-BzQjmLMIfLIPgirgnOixM9x4PwgcNQ%3D%3D\", \"data\": \"\", \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36\", \"index_0\": 0, \"index_1\": 1, \"index_2\": 14 } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_a_bogus_api_v1_douyin_web_generate_a_bogus_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_a_bogus_api_v1_douyin_web_generate_a_bogus_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_a_bogus_api_v1_douyin_web_generate_a_bogus_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_a_bogus_api_v1_douyin_web_generate_a_bogus_post_with_http_info(self, **kwargs):  # noqa: E501
        """使用接口网址生成A-Bogus参数/Generate A-Bogus parameter using API URL  # noqa: E501

        # [中文] ### 用途: - 使用接口网址生成A-Bogus参数，提交的URL不能带有a_bogus参数，同时a_bogus参数与请求头中的User-Agent有关，需要一起提交和请求。 ### 参数: - url: API链接，请去除url中的原本的a_boogus参数(如有)。 - data: 请求载荷，只有在POST请求中才需要提交，GET请求中使用空字符串即可。 - user_agent: user-agent，需要提交你请求头中的User-Agent，该值参与a_bogus参数的计算。 - index_0: 加密明文列表的第一个值，无特殊要求，默认为0，不要随意修改。 - index_1: 加密明文列表的第二个值，无特殊要求，默认为1，不要随意修改。 - index_2: 加密明文列表的第三个值，无特殊要求，默认为14，不要随意修改。 ### 返回: - A-Bogus参数  # [English] ### Purpose: - Generate A-Bogus parameter using API URL, the submitted URL cannot contain the original a_boogus parameter, and the a_bogus parameter is related to the User-Agent in the request header, which needs to be submitted and requested together. ### Parameters: - url: API link, please remove the original a_boogus parameter from the url (if any). - data: Request payload, only need to submit in POST request, use an empty string in GET request. - user_agent: user-agent, you need to submit the User-Agent in your request header, which is involved in the calculation of the a_bogus parameter. - index_0: The first value of the encrypted plaintext list, no special requirements, the default is 0, do not modify it at will. - index_1: The second value of the encrypted plaintext list, no special requirements, the default is 1, do not modify it at will. - index_2: The third value of the encrypted plaintext list, no special requirements, the default is 14, do not modify it at will. ### Return: - A-Bogus parameter  # [示例/Example] ```json { \"url\": \"https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&enable_history=1&keyword=%E4%B8%AD%E5%8D%8E%E5%A8%98&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=7346905902554844468&offset=0&count=15&need_filter_settings=1&pc_client_type=1&version_code=190600&version_name=19.6.0&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platform=Win32&browser_name=Firefox&browser_version=124.0&browser_online=true&engine_name=Gecko&engine_version=124.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=&platform=PC&webid=7348962975497324070&msToken=YCTVM6YGmjFdIpQAN9ykXLBXiSiuHdZkOkEQWTeqVOHBEPmOcM0lNwE0Kd9vgHPMPigSndZDHfAq9k-6lDmH3Jqz6mHHxmn-BzQjmLMIfLIPgirgnOixM9x4PwgcNQ%3D%3D\", \"data\": \"\", \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36\", \"index_0\": 0, \"index_1\": 1, \"index_2\": 14 } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_a_bogus_api_v1_douyin_web_generate_a_bogus_post_with_http_info(async_req=True)
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
                    " to method generate_a_bogus_api_v1_douyin_web_generate_a_bogus_post" % key
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
            '/api/v1/douyin/web/generate_a_bogus', 'POST',
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

    def generate_real_ms_token_api_v1_douyin_web_generate_real_ms_token_get(self, **kwargs):  # noqa: E501
        """生成真实msToken/Generate real msToken  # noqa: E501

        # [中文] ### 用途: - 生成真实msToken ### 返回: - msToken  # [English] ### Purpose: - Generate real msToken ### Return: - msToken  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_real_ms_token_api_v1_douyin_web_generate_real_ms_token_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_real_ms_token_api_v1_douyin_web_generate_real_ms_token_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_real_ms_token_api_v1_douyin_web_generate_real_ms_token_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_real_ms_token_api_v1_douyin_web_generate_real_ms_token_get_with_http_info(self, **kwargs):  # noqa: E501
        """生成真实msToken/Generate real msToken  # noqa: E501

        # [中文] ### 用途: - 生成真实msToken ### 返回: - msToken  # [English] ### Purpose: - Generate real msToken ### Return: - msToken  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_real_ms_token_api_v1_douyin_web_generate_real_ms_token_get_with_http_info(async_req=True)
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
                    " to method generate_real_ms_token_api_v1_douyin_web_generate_real_ms_token_get" % key
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
            '/api/v1/douyin/web/generate_real_msToken', 'GET',
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

    def generate_sv_web_id_api_v1_douyin_web_generate_sv_web_id_get(self, **kwargs):  # noqa: E501
        """生成s_v_web_id/Generate s_v_web_id  # noqa: E501

        # [中文] ### 用途: - 生成s_v_web_id ### 返回: - s_v_web_id  # [English] ### Purpose: - Generate s_v_web_id ### Return: - s_v_web_id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_sv_web_id_api_v1_douyin_web_generate_sv_web_id_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_sv_web_id_api_v1_douyin_web_generate_sv_web_id_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_sv_web_id_api_v1_douyin_web_generate_sv_web_id_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_sv_web_id_api_v1_douyin_web_generate_sv_web_id_get_with_http_info(self, **kwargs):  # noqa: E501
        """生成s_v_web_id/Generate s_v_web_id  # noqa: E501

        # [中文] ### 用途: - 生成s_v_web_id ### 返回: - s_v_web_id  # [English] ### Purpose: - Generate s_v_web_id ### Return: - s_v_web_id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_sv_web_id_api_v1_douyin_web_generate_sv_web_id_get_with_http_info(async_req=True)
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
                    " to method generate_sv_web_id_api_v1_douyin_web_generate_sv_web_id_get" % key
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
            '/api/v1/douyin/web/generate_s_v_web_id', 'GET',
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

    def generate_ttwid_api_v1_douyin_web_generate_ttwid_get(self, **kwargs):  # noqa: E501
        """生成ttwid/Generate ttwid  # noqa: E501

        # [中文] ### 用途: - 生成ttwid ### 返回: - ttwid  # [English] ### Purpose: - Generate ttwid ### Return: - ttwid  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_ttwid_api_v1_douyin_web_generate_ttwid_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_agent:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_ttwid_api_v1_douyin_web_generate_ttwid_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_ttwid_api_v1_douyin_web_generate_ttwid_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_ttwid_api_v1_douyin_web_generate_ttwid_get_with_http_info(self, **kwargs):  # noqa: E501
        """生成ttwid/Generate ttwid  # noqa: E501

        # [中文] ### 用途: - 生成ttwid ### 返回: - ttwid  # [English] ### Purpose: - Generate ttwid ### Return: - ttwid  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_ttwid_api_v1_douyin_web_generate_ttwid_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_agent:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_ttwid_api_v1_douyin_web_generate_ttwid_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/generate_ttwid', 'GET',
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

    def generate_verify_fp_api_v1_douyin_web_generate_verify_fp_get(self, **kwargs):  # noqa: E501
        """生成verify_fp/Generate verify_fp  # noqa: E501

        # [中文] ### 用途: - 生成verify_fp ### 返回: - verify_fp  # [English] ### Purpose: - Generate verify_fp ### Return: - verify_fp  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_verify_fp_api_v1_douyin_web_generate_verify_fp_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_verify_fp_api_v1_douyin_web_generate_verify_fp_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_verify_fp_api_v1_douyin_web_generate_verify_fp_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_verify_fp_api_v1_douyin_web_generate_verify_fp_get_with_http_info(self, **kwargs):  # noqa: E501
        """生成verify_fp/Generate verify_fp  # noqa: E501

        # [中文] ### 用途: - 生成verify_fp ### 返回: - verify_fp  # [English] ### Purpose: - Generate verify_fp ### Return: - verify_fp  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_verify_fp_api_v1_douyin_web_generate_verify_fp_get_with_http_info(async_req=True)
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
                    " to method generate_verify_fp_api_v1_douyin_web_generate_verify_fp_get" % key
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
            '/api/v1/douyin/web/generate_verify_fp', 'GET',
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

    def generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get(self, user_agent, room_id, user_unique_id, **kwargs):  # noqa: E501
        """生成弹幕xb签名/Generate barrage xb signature  # noqa: E501

        # [中文] ### 用途: - 生成弹幕xb签名 ### 参数: - user_agent: 用户浏览器代理 - room_id: 房间号 - user_unique_id: 用户唯一ID ### 返回: - 弹幕xb签名  # [English] ### Purpose: - Generate danmu xb signature ### Parameters: - user_agent: User browser agent - room_id: Room ID - user_unique_id: User unique ID ### Return: - Danmu xb signature  # [示例/Example] user_agent = \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0\" room_id = \"7382517534467115826\" user_unique_id = \"7382524529011246630\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get(user_agent, room_id, user_unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_agent: 用户浏览器代理/User browser agent (required)
        :param object room_id: 房间号/Room ID (required)
        :param object user_unique_id: 用户唯一ID/User unique ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get_with_http_info(user_agent, room_id, user_unique_id, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get_with_http_info(user_agent, room_id, user_unique_id, **kwargs)  # noqa: E501
            return data

    def generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get_with_http_info(self, user_agent, room_id, user_unique_id, **kwargs):  # noqa: E501
        """生成弹幕xb签名/Generate barrage xb signature  # noqa: E501

        # [中文] ### 用途: - 生成弹幕xb签名 ### 参数: - user_agent: 用户浏览器代理 - room_id: 房间号 - user_unique_id: 用户唯一ID ### 返回: - 弹幕xb签名  # [English] ### Purpose: - Generate danmu xb signature ### Parameters: - user_agent: User browser agent - room_id: Room ID - user_unique_id: User unique ID ### Return: - Danmu xb signature  # [示例/Example] user_agent = \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0\" room_id = \"7382517534467115826\" user_unique_id = \"7382524529011246630\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get_with_http_info(user_agent, room_id, user_unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_agent: 用户浏览器代理/User browser agent (required)
        :param object room_id: 房间号/Room ID (required)
        :param object user_unique_id: 用户唯一ID/User unique ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_agent', 'room_id', 'user_unique_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_agent' is set
        if self.api_client.client_side_validation and ('user_agent' not in params or
                                                       params['user_agent'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_agent` when calling `generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get`")  # noqa: E501
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get`")  # noqa: E501
        # verify the required parameter 'user_unique_id' is set
        if self.api_client.client_side_validation and ('user_unique_id' not in params or
                                                       params['user_unique_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_unique_id` when calling `generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))  # noqa: E501
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501
        if 'user_unique_id' in params:
            query_params.append(('user_unique_id', params['user_unique_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/generate_wss_xb_signature', 'GET',
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

    def generate_x_bogus_api_v1_douyin_web_generate_x_bogus_post(self, **kwargs):  # noqa: E501
        """使用接口网址生成X-Bogus参数/Generate X-Bogus parameter using API URL  # noqa: E501

        # [中文] ### 用途: - 使用接口网址生成X-Bogus参数 ### 参数: - url: 接口网址  # [English] ### Purpose: - Generate X-Bogus parameter using API URL ### Parameters: - url: API URL  # [示例/Example]  ```json { \"url\": \"https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=128&device_memory=10240&platform=PC&downlink=10&effective_type=4g&round_trip_time=100\", \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\" } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_x_bogus_api_v1_douyin_web_generate_x_bogus_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_x_bogus_api_v1_douyin_web_generate_x_bogus_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_x_bogus_api_v1_douyin_web_generate_x_bogus_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_x_bogus_api_v1_douyin_web_generate_x_bogus_post_with_http_info(self, **kwargs):  # noqa: E501
        """使用接口网址生成X-Bogus参数/Generate X-Bogus parameter using API URL  # noqa: E501

        # [中文] ### 用途: - 使用接口网址生成X-Bogus参数 ### 参数: - url: 接口网址  # [English] ### Purpose: - Generate X-Bogus parameter using API URL ### Parameters: - url: API URL  # [示例/Example]  ```json { \"url\": \"https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=128&device_memory=10240&platform=PC&downlink=10&effective_type=4g&round_trip_time=100\", \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\" } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_x_bogus_api_v1_douyin_web_generate_x_bogus_post_with_http_info(async_req=True)
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
                    " to method generate_x_bogus_api_v1_douyin_web_generate_x_bogus_post" % key
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
            '/api/v1/douyin/web/generate_x_bogus', 'POST',
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

    def get_all_aweme_id_api_v1_douyin_web_get_all_aweme_id_post(self, **kwargs):  # noqa: E501
        """提取列表作品id/Extract list video id  # noqa: E501

        # [中文]  ### 用途:  - 提取列表作品id（最多支持20个链接）  ### 参数:  - url: 作品链接列表  ### 返回:  - 作品id列表   # [English]  ### Purpose:  - Extract list video id (supports up to 20 links)  ### Parameters:  - url: Video link list  ### Return:  - Video id list   # [示例/Example]  ```json  { \"urls\":[     \"0.53 02/26 I@v.sE Fus:/ 你别太帅了郑润泽# 现场版live # 音乐节 # 郑润泽  https://v.douyin.com/iRNBho6u/ 复制此链接，打开Dou音搜索，直接观看视频!\",     \"https://v.douyin.com/iRNBho6u/\",     \"https://www.iesdouyin.com/share/video/7298145681699622182/?region=CN&mid=7298145762238565171&u_code=l1j9bkbd&did=MS4wLjABAAAAtqpCx0hpOERbdSzQdjRZw-wFPxaqdbAzsKDmbJMUI3KWlMGQHC-n6dXAqa-dM2EP&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=05kGlqGmR4_IwCX.ZGk6xuL0osNA..5ur7b0jbOx6cc-&share_version=170400&ts=1699262937&from_aid=6383&from_ssr=1&from=web_code_link\",     \"https://www.douyin.com/video/7298145681699622182?previous_page=web_code_link\",     \"https://www.douyin.com/video/7298145681699622182\",  ]  }  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_aweme_id_api_v1_douyin_web_get_all_aweme_id_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_aweme_id_api_v1_douyin_web_get_all_aweme_id_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_aweme_id_api_v1_douyin_web_get_all_aweme_id_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_aweme_id_api_v1_douyin_web_get_all_aweme_id_post_with_http_info(self, **kwargs):  # noqa: E501
        """提取列表作品id/Extract list video id  # noqa: E501

        # [中文]  ### 用途:  - 提取列表作品id（最多支持20个链接）  ### 参数:  - url: 作品链接列表  ### 返回:  - 作品id列表   # [English]  ### Purpose:  - Extract list video id (supports up to 20 links)  ### Parameters:  - url: Video link list  ### Return:  - Video id list   # [示例/Example]  ```json  { \"urls\":[     \"0.53 02/26 I@v.sE Fus:/ 你别太帅了郑润泽# 现场版live # 音乐节 # 郑润泽  https://v.douyin.com/iRNBho6u/ 复制此链接，打开Dou音搜索，直接观看视频!\",     \"https://v.douyin.com/iRNBho6u/\",     \"https://www.iesdouyin.com/share/video/7298145681699622182/?region=CN&mid=7298145762238565171&u_code=l1j9bkbd&did=MS4wLjABAAAAtqpCx0hpOERbdSzQdjRZw-wFPxaqdbAzsKDmbJMUI3KWlMGQHC-n6dXAqa-dM2EP&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=05kGlqGmR4_IwCX.ZGk6xuL0osNA..5ur7b0jbOx6cc-&share_version=170400&ts=1699262937&from_aid=6383&from_ssr=1&from=web_code_link\",     \"https://www.douyin.com/video/7298145681699622182?previous_page=web_code_link\",     \"https://www.douyin.com/video/7298145681699622182\",  ]  }  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_aweme_id_api_v1_douyin_web_get_all_aweme_id_post_with_http_info(async_req=True)
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
                    " to method get_all_aweme_id_api_v1_douyin_web_get_all_aweme_id_post" % key
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
            '/api/v1/douyin/web/get_all_aweme_id', 'POST',
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

    def get_all_sec_user_id_api_v1_douyin_web_get_all_sec_user_id_post(self, **kwargs):  # noqa: E501
        """提取列表用户id/Extract list user id  # noqa: E501

        # [中文]  ### 用途:  - 提取列表用户id  ### 参数:  - url: 用户主页链接列表（最多支持10个链接）  ### 返回:  - 如果链接成功获取到sec_user_id，则返回sec_user_id，否则返回原始的输入链接，后续可以手动校验链接无法获取sec_user_id的原因。   # [English]  ### Purpose:  - Extract list user id  ### Parameters:  - url: User homepage link list (supports up to 10 links)  ### Return:  - If the sec_user_id is successfully obtained from the link, the sec_user_id is returned, otherwise the original input link is returned, and the reason why the sec_user_id cannot be obtained can be manually verified later.   # [示例/Example]  ```json  { \"urls\":[    \"https://www.douyin.com/user/MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE?vid=7285950278132616463\",    \"https://www.douyin.com/user/MS4wLjABAAAAVsneOf144eGDFf8Xp9QNb1VW6ovXnNT5SqJBhJfe8KQBKWKDTWK5Hh-_i9mJzb8C\",    \"长按复制此条消息，打开抖音搜索，查看TA的更多作品。 https://v.douyin.com/idFqvUms/\",    \"https://v.douyin.com/idFqvUms/\"     ]  }  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_sec_user_id_api_v1_douyin_web_get_all_sec_user_id_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_sec_user_id_api_v1_douyin_web_get_all_sec_user_id_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_sec_user_id_api_v1_douyin_web_get_all_sec_user_id_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_sec_user_id_api_v1_douyin_web_get_all_sec_user_id_post_with_http_info(self, **kwargs):  # noqa: E501
        """提取列表用户id/Extract list user id  # noqa: E501

        # [中文]  ### 用途:  - 提取列表用户id  ### 参数:  - url: 用户主页链接列表（最多支持10个链接）  ### 返回:  - 如果链接成功获取到sec_user_id，则返回sec_user_id，否则返回原始的输入链接，后续可以手动校验链接无法获取sec_user_id的原因。   # [English]  ### Purpose:  - Extract list user id  ### Parameters:  - url: User homepage link list (supports up to 10 links)  ### Return:  - If the sec_user_id is successfully obtained from the link, the sec_user_id is returned, otherwise the original input link is returned, and the reason why the sec_user_id cannot be obtained can be manually verified later.   # [示例/Example]  ```json  { \"urls\":[    \"https://www.douyin.com/user/MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE?vid=7285950278132616463\",    \"https://www.douyin.com/user/MS4wLjABAAAAVsneOf144eGDFf8Xp9QNb1VW6ovXnNT5SqJBhJfe8KQBKWKDTWK5Hh-_i9mJzb8C\",    \"长按复制此条消息，打开抖音搜索，查看TA的更多作品。 https://v.douyin.com/idFqvUms/\",    \"https://v.douyin.com/idFqvUms/\"     ]  }  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_sec_user_id_api_v1_douyin_web_get_all_sec_user_id_post_with_http_info(async_req=True)
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
                    " to method get_all_sec_user_id_api_v1_douyin_web_get_all_sec_user_id_post" % key
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
            '/api/v1/douyin/web/get_all_sec_user_id', 'POST',
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

    def get_all_webcast_id_api_v1_douyin_web_get_all_webcast_id_post(self, **kwargs):  # noqa: E501
        """提取列表直播间号/Extract list webcast id  # noqa: E501

        # [中文] ### 用途: - 提取列表直播间号 ### 参数: - url: 直播间链接列表（最多支持20个链接） ### 返回: - 直播间号列表  # [English] ### Purpose: - Extract list webcast id ### Parameters: - url: Room link list (supports up to 20 links) ### Return: - Room id list  # [示例/Example] ```json {   \"urls\": [         \"https://live.douyin.com/775841227732\",         \"https://live.douyin.com/775841227732?room_id=7318296342189919011&enter_from_merge=web_share_link&enter_method=web_share_link&previous_page=app_code_link\",         'https://webcast.amemv.com/douyin/webcast/reflow/7318296342189919011?u_code=l1j9bkbd&did=MS4wLjABAAAAEs86TBQPNwAo-RGrcxWyCdwKhI66AK3Pqf3ieo6HaxI&iid=MS4wLjABAAAA0ptpM-zzoliLEeyvWOCUt-_dQza4uSjlIvbtIazXnCY&with_sec_did=1&use_link_command=1&ecom_share_track_params=&extra_params={\"from_request_id\":\"20231230162057EC005772A8EAA0199906\",\"im_channel_invite_id\":\"0\"}&user_id=3644207898042206&liveId=7318296342189919011&from=share&style=share&enter_method=click_share&roomId=7318296342189919011&activity_info={}',         \"6i- Q@x.Sl 03/23 【醒子8ke的直播间】  点击打开👉https://v.douyin.com/i8tBR7hX/  或长按复制此条消息，打开抖音，看TA直播\",         \"https://v.douyin.com/i8tBR7hX/\",         ] } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_webcast_id_api_v1_douyin_web_get_all_webcast_id_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_webcast_id_api_v1_douyin_web_get_all_webcast_id_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_webcast_id_api_v1_douyin_web_get_all_webcast_id_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_webcast_id_api_v1_douyin_web_get_all_webcast_id_post_with_http_info(self, **kwargs):  # noqa: E501
        """提取列表直播间号/Extract list webcast id  # noqa: E501

        # [中文] ### 用途: - 提取列表直播间号 ### 参数: - url: 直播间链接列表（最多支持20个链接） ### 返回: - 直播间号列表  # [English] ### Purpose: - Extract list webcast id ### Parameters: - url: Room link list (supports up to 20 links) ### Return: - Room id list  # [示例/Example] ```json {   \"urls\": [         \"https://live.douyin.com/775841227732\",         \"https://live.douyin.com/775841227732?room_id=7318296342189919011&enter_from_merge=web_share_link&enter_method=web_share_link&previous_page=app_code_link\",         'https://webcast.amemv.com/douyin/webcast/reflow/7318296342189919011?u_code=l1j9bkbd&did=MS4wLjABAAAAEs86TBQPNwAo-RGrcxWyCdwKhI66AK3Pqf3ieo6HaxI&iid=MS4wLjABAAAA0ptpM-zzoliLEeyvWOCUt-_dQza4uSjlIvbtIazXnCY&with_sec_did=1&use_link_command=1&ecom_share_track_params=&extra_params={\"from_request_id\":\"20231230162057EC005772A8EAA0199906\",\"im_channel_invite_id\":\"0\"}&user_id=3644207898042206&liveId=7318296342189919011&from=share&style=share&enter_method=click_share&roomId=7318296342189919011&activity_info={}',         \"6i- Q@x.Sl 03/23 【醒子8ke的直播间】  点击打开👉https://v.douyin.com/i8tBR7hX/  或长按复制此条消息，打开抖音，看TA直播\",         \"https://v.douyin.com/i8tBR7hX/\",         ] } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_webcast_id_api_v1_douyin_web_get_all_webcast_id_post_with_http_info(async_req=True)
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
                    " to method get_all_webcast_id_api_v1_douyin_web_get_all_webcast_id_post" % key
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
            '/api/v1/douyin/web/get_all_webcast_id', 'POST',
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

    def get_aweme_id_api_v1_douyin_web_get_aweme_id_get(self, url, **kwargs):  # noqa: E501
        """提取单个作品id/Extract single video id  # noqa: E501

        # [中文] ### 用途: - 提取单个作品id ### 参数: - url: 作品链接 ### 返回: - 作品id  # [English] ### Purpose: - Extract single video id ### Parameters: - url: Video link ### Return: - Video id  # [示例/Example] url = \"https://www.douyin.com/video/7298145681699622182\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_aweme_id_api_v1_douyin_web_get_aweme_id_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_aweme_id_api_v1_douyin_web_get_aweme_id_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.get_aweme_id_api_v1_douyin_web_get_aweme_id_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def get_aweme_id_api_v1_douyin_web_get_aweme_id_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """提取单个作品id/Extract single video id  # noqa: E501

        # [中文] ### 用途: - 提取单个作品id ### 参数: - url: 作品链接 ### 返回: - 作品id  # [English] ### Purpose: - Extract single video id ### Parameters: - url: Video link ### Return: - Video id  # [示例/Example] url = \"https://www.douyin.com/video/7298145681699622182\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_aweme_id_api_v1_douyin_web_get_aweme_id_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: (required)
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
                    " to method get_aweme_id_api_v1_douyin_web_get_aweme_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `get_aweme_id_api_v1_douyin_web_get_aweme_id_get`")  # noqa: E501

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
            '/api/v1/douyin/web/get_aweme_id', 'GET',
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

    def get_sec_user_id_api_v1_douyin_web_get_sec_user_id_get(self, url, **kwargs):  # noqa: E501
        """提取单个用户id/Extract single user id  # noqa: E501

        # [中文] ### 用途: - 提取单个用户id ### 参数: - url: 用户主页链接 ### 返回: - 用户sec_user_id  # [English] ### Purpose: - Extract single user id ### Parameters: - url: User homepage link ### Return: - User sec_user_id  # [示例/Example] url = \"https://www.douyin.com/user/MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sec_user_id_api_v1_douyin_web_get_sec_user_id_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sec_user_id_api_v1_douyin_web_get_sec_user_id_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sec_user_id_api_v1_douyin_web_get_sec_user_id_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def get_sec_user_id_api_v1_douyin_web_get_sec_user_id_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """提取单个用户id/Extract single user id  # noqa: E501

        # [中文] ### 用途: - 提取单个用户id ### 参数: - url: 用户主页链接 ### 返回: - 用户sec_user_id  # [English] ### Purpose: - Extract single user id ### Parameters: - url: User homepage link ### Return: - User sec_user_id  # [示例/Example] url = \"https://www.douyin.com/user/MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sec_user_id_api_v1_douyin_web_get_sec_user_id_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: (required)
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
                    " to method get_sec_user_id_api_v1_douyin_web_get_sec_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `get_sec_user_id_api_v1_douyin_web_get_sec_user_id_get`")  # noqa: E501

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
            '/api/v1/douyin/web/get_sec_user_id', 'GET',
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

    def get_webcast_id_api_v1_douyin_web_get_webcast_id_get(self, url, **kwargs):  # noqa: E501
        """提取直播间号/Extract webcast id  # noqa: E501

        # [中文] ### 用途: - 提取列表直播间号 ### 参数: - url: 直播间链接 ### 返回: - 直播间号  # [English] ### Purpose: - Extract list webcast id ### Parameters: - url: Room link ### Return: - Room id  # [示例/Example] url = \"https://live.douyin.com/775841227732\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_webcast_id_api_v1_douyin_web_get_webcast_id_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_webcast_id_api_v1_douyin_web_get_webcast_id_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.get_webcast_id_api_v1_douyin_web_get_webcast_id_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def get_webcast_id_api_v1_douyin_web_get_webcast_id_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """提取直播间号/Extract webcast id  # noqa: E501

        # [中文] ### 用途: - 提取列表直播间号 ### 参数: - url: 直播间链接 ### 返回: - 直播间号  # [English] ### Purpose: - Extract list webcast id ### Parameters: - url: Room link ### Return: - Room id  # [示例/Example] url = \"https://live.douyin.com/775841227732\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_webcast_id_api_v1_douyin_web_get_webcast_id_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: (required)
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
                    " to method get_webcast_id_api_v1_douyin_web_get_webcast_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `get_webcast_id_api_v1_douyin_web_get_webcast_id_get`")  # noqa: E501

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
            '/api/v1/douyin/web/get_webcast_id', 'GET',
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

    def handler_shorten_url_api_v1_douyin_web_handler_shorten_url_get(self, target_url, **kwargs):  # noqa: E501
        """生成短链接  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_shorten_url_api_v1_douyin_web_handler_shorten_url_get(target_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object target_url: 待转换的短链接/Target URL to be converted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handler_shorten_url_api_v1_douyin_web_handler_shorten_url_get_with_http_info(target_url, **kwargs)  # noqa: E501
        else:
            (data) = self.handler_shorten_url_api_v1_douyin_web_handler_shorten_url_get_with_http_info(target_url, **kwargs)  # noqa: E501
            return data

    def handler_shorten_url_api_v1_douyin_web_handler_shorten_url_get_with_http_info(self, target_url, **kwargs):  # noqa: E501
        """生成短链接  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_shorten_url_api_v1_douyin_web_handler_shorten_url_get_with_http_info(target_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object target_url: 待转换的短链接/Target URL to be converted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['target_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handler_shorten_url_api_v1_douyin_web_handler_shorten_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'target_url' is set
        if self.api_client.client_side_validation and ('target_url' not in params or
                                                       params['target_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `target_url` when calling `handler_shorten_url_api_v1_douyin_web_handler_shorten_url_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'target_url' in params:
            query_params.append(('target_url', params['target_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/handler_shorten_url', 'GET',
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

    def handler_user_profile_api_v1_douyin_web_handler_user_profile_get(self, sec_user_id, **kwargs):  # noqa: E501
        """使用sec_user_id获取指定用户的信息/Get information of specified user by sec_user_id  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id ### Return: - User information  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_api_v1_douyin_web_handler_user_profile_get(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handler_user_profile_api_v1_douyin_web_handler_user_profile_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.handler_user_profile_api_v1_douyin_web_handler_user_profile_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
            return data

    def handler_user_profile_api_v1_douyin_web_handler_user_profile_get_with_http_info(self, sec_user_id, **kwargs):  # noqa: E501
        """使用sec_user_id获取指定用户的信息/Get information of specified user by sec_user_id  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id ### Return: - User information  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_api_v1_douyin_web_handler_user_profile_get_with_http_info(sec_user_id, async_req=True)
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
                    " to method handler_user_profile_api_v1_douyin_web_handler_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_user_id' is set
        if self.api_client.client_side_validation and ('sec_user_id' not in params or
                                                       params['sec_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_id` when calling `handler_user_profile_api_v1_douyin_web_handler_user_profile_get`")  # noqa: E501

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
            '/api/v1/douyin/web/handler_user_profile', 'GET',
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

    def handler_user_profile_v2_api_v1_douyin_web_handler_user_profile_v2_get(self, unique_id, **kwargs):  # noqa: E501
        """使用unique_id（抖音号）获取指定用户的信息/Get information of specified user by unique_id  # noqa: E501

        # [中文] ### 用途: - 根据抖音号获取指定用户的信息 ### 参数: - unique_id: 用户unique_id ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user by unique_id ### Parameters: - unique_id: User unique_id ### Return: - User information  # [示例/Example] unique_id = \"TheChief\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_v2_api_v1_douyin_web_handler_user_profile_v2_get(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object unique_id: 用户unique_id/User unique_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handler_user_profile_v2_api_v1_douyin_web_handler_user_profile_v2_get_with_http_info(unique_id, **kwargs)  # noqa: E501
        else:
            (data) = self.handler_user_profile_v2_api_v1_douyin_web_handler_user_profile_v2_get_with_http_info(unique_id, **kwargs)  # noqa: E501
            return data

    def handler_user_profile_v2_api_v1_douyin_web_handler_user_profile_v2_get_with_http_info(self, unique_id, **kwargs):  # noqa: E501
        """使用unique_id（抖音号）获取指定用户的信息/Get information of specified user by unique_id  # noqa: E501

        # [中文] ### 用途: - 根据抖音号获取指定用户的信息 ### 参数: - unique_id: 用户unique_id ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user by unique_id ### Parameters: - unique_id: User unique_id ### Return: - User information  # [示例/Example] unique_id = \"TheChief\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_v2_api_v1_douyin_web_handler_user_profile_v2_get_with_http_info(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object unique_id: 用户unique_id/User unique_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['unique_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handler_user_profile_v2_api_v1_douyin_web_handler_user_profile_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'unique_id' is set
        if self.api_client.client_side_validation and ('unique_id' not in params or
                                                       params['unique_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `unique_id` when calling `handler_user_profile_v2_api_v1_douyin_web_handler_user_profile_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'unique_id' in params:
            query_params.append(('unique_id', params['unique_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/handler_user_profile_v2', 'GET',
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

    def handler_user_profile_v3_api_v1_douyin_web_handler_user_profile_v3_get(self, uid, **kwargs):  # noqa: E501
        """根据抖音uid获取指定用户的信息/Get information of specified user by uid  # noqa: E501

        # [中文] ### 用途: - 根据抖音uid获取指定用户的信息 ### 参数: - uid: 用户uid，也就是抖音号的short_id ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user by unique_id ### Parameters: - uid: User uid, which is the short_id of the Douyin number ### Return: - User information  # [示例/Example] uid = \"1673937488185292\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_v3_api_v1_douyin_web_handler_user_profile_v3_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户uid(short_id)/User uid(short_id) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handler_user_profile_v3_api_v1_douyin_web_handler_user_profile_v3_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.handler_user_profile_v3_api_v1_douyin_web_handler_user_profile_v3_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def handler_user_profile_v3_api_v1_douyin_web_handler_user_profile_v3_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """根据抖音uid获取指定用户的信息/Get information of specified user by uid  # noqa: E501

        # [中文] ### 用途: - 根据抖音uid获取指定用户的信息 ### 参数: - uid: 用户uid，也就是抖音号的short_id ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user by unique_id ### Parameters: - uid: User uid, which is the short_id of the Douyin number ### Return: - User information  # [示例/Example] uid = \"1673937488185292\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_v3_api_v1_douyin_web_handler_user_profile_v3_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户uid(short_id)/User uid(short_id) (required)
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
                    " to method handler_user_profile_v3_api_v1_douyin_web_handler_user_profile_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `handler_user_profile_v3_api_v1_douyin_web_handler_user_profile_v3_get`")  # noqa: E501

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
            '/api/v1/douyin/web/handler_user_profile_v3', 'GET',
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

    def handler_user_profile_v4_api_v1_douyin_web_handler_user_profile_v4_get(self, sec_user_id, **kwargs):  # noqa: E501
        """根据sec_user_id获取指定用户的信息（性别，年龄，直播等级、牌子）/Get information of specified user by sec_user_id (gender, age, live level、brand)  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id ### 返回: - 用户信息，包含性别，年龄，直播等级，直播间牌子 ### 说明： - 性别：1为男，2为女，0为未知，在live_user字段中。 - 年龄：在user字段中，-1为未知。  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id ### Return: - User information, including gender, age, live level, live room brand ### Description: - gender: 1 male, 2 female, 0 unknown, in the live_user field. - age: in the user field, -1 unknown.  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_v4_api_v1_douyin_web_handler_user_profile_v4_get(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handler_user_profile_v4_api_v1_douyin_web_handler_user_profile_v4_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.handler_user_profile_v4_api_v1_douyin_web_handler_user_profile_v4_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
            return data

    def handler_user_profile_v4_api_v1_douyin_web_handler_user_profile_v4_get_with_http_info(self, sec_user_id, **kwargs):  # noqa: E501
        """根据sec_user_id获取指定用户的信息（性别，年龄，直播等级、牌子）/Get information of specified user by sec_user_id (gender, age, live level、brand)  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id ### 返回: - 用户信息，包含性别，年龄，直播等级，直播间牌子 ### 说明： - 性别：1为男，2为女，0为未知，在live_user字段中。 - 年龄：在user字段中，-1为未知。  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id ### Return: - User information, including gender, age, live level, live room brand ### Description: - gender: 1 male, 2 female, 0 unknown, in the live_user field. - age: in the user field, -1 unknown.  # [示例/Example] sec_user_id = \"MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_v4_api_v1_douyin_web_handler_user_profile_v4_get_with_http_info(sec_user_id, async_req=True)
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
                    " to method handler_user_profile_v4_api_v1_douyin_web_handler_user_profile_v4_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_user_id' is set
        if self.api_client.client_side_validation and ('sec_user_id' not in params or
                                                       params['sec_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_id` when calling `handler_user_profile_v4_api_v1_douyin_web_handler_user_profile_v4_get`")  # noqa: E501

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
            '/api/v1/douyin/web/handler_user_profile_v4', 'GET',
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

    def webcast_id2_room_id_api_v1_douyin_web_webcast_id2_room_id_get(self, webcast_id, **kwargs):  # noqa: E501
        """直播间号转房间号/Webcast id to room id  # noqa: E501

        # [中文] ### 用途: - 直播间号转房间号 ### 参数: - webcast_id: 直播间号 ### 返回: - 房间号  # [English] ### Purpose: - Webcast id to room id ### Parameters: - webcast_id: Webcast id ### Return: - Room id  # [示例/Example] \"webcast_id = \"775841227732\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webcast_id2_room_id_api_v1_douyin_web_webcast_id2_room_id_get(webcast_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object webcast_id: 直播间号/Webcast id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.webcast_id2_room_id_api_v1_douyin_web_webcast_id2_room_id_get_with_http_info(webcast_id, **kwargs)  # noqa: E501
        else:
            (data) = self.webcast_id2_room_id_api_v1_douyin_web_webcast_id2_room_id_get_with_http_info(webcast_id, **kwargs)  # noqa: E501
            return data

    def webcast_id2_room_id_api_v1_douyin_web_webcast_id2_room_id_get_with_http_info(self, webcast_id, **kwargs):  # noqa: E501
        """直播间号转房间号/Webcast id to room id  # noqa: E501

        # [中文] ### 用途: - 直播间号转房间号 ### 参数: - webcast_id: 直播间号 ### 返回: - 房间号  # [English] ### Purpose: - Webcast id to room id ### Parameters: - webcast_id: Webcast id ### Return: - Room id  # [示例/Example] \"webcast_id = \"775841227732\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.webcast_id2_room_id_api_v1_douyin_web_webcast_id2_room_id_get_with_http_info(webcast_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object webcast_id: 直播间号/Webcast id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webcast_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method webcast_id2_room_id_api_v1_douyin_web_webcast_id2_room_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webcast_id' is set
        if self.api_client.client_side_validation and ('webcast_id' not in params or
                                                       params['webcast_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `webcast_id` when calling `webcast_id2_room_id_api_v1_douyin_web_webcast_id2_room_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'webcast_id' in params:
            query_params.append(('webcast_id', params['webcast_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/web/webcast_id_2_room_id', 'GET',
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
