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


class DouyinXingtuAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get(self, kol_id, **kwargs):  # noqa: E501
        """获取kol热词分析内容V1/Get Author Content Hot Comment Keywords V1  # noqa: E501

        # [中文] ### 用途: - 获取kol热词分析内容V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol热词分析内容  # [English] ### Purpose: - Get Author Content Hot Comment Keywords V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - Author Content Hot Comment Keywords  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
        else:
            (data) = self.author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
            return data

    def author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get_with_http_info(self, kol_id, **kwargs):  # noqa: E501
        """获取kol热词分析内容V1/Get Author Content Hot Comment Keywords V1  # noqa: E501

        # [中文] ### 用途: - 获取kol热词分析内容V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol热词分析内容  # [English] ### Purpose: - Get Author Content Hot Comment Keywords V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - Author Content Hot Comment Keywords  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get_with_http_info(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/author_content_hot_comment_keywords_v1', 'GET',
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

    def author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get(self, kol_id, **kwargs):  # noqa: E501
        """获取kol热词分析评论V1/Get Author Hot Comment Tokens V1  # noqa: E501

        # [中文] ### 用途: - 获取kol热词分析评论V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol热词分析评论  # [English] ### Purpose: - Get Author Hot Comment Tokens V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - Author Hot Comment Tokens  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
        else:
            (data) = self.author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
            return data

    def author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get_with_http_info(self, kol_id, **kwargs):  # noqa: E501
        """获取kol热词分析评论V1/Get Author Hot Comment Tokens V1  # noqa: E501

        # [中文] ### 用途: - 获取kol热词分析评论V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol热词分析评论  # [English] ### Purpose: - Get Author Hot Comment Tokens V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - Author Hot Comment Tokens  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get_with_http_info(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/author_hot_comment_tokens_v1', 'GET',
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

    def get_sign_image_api_v1_douyin_xingtu_get_sign_image_get(self, uri, **kwargs):  # noqa: E501
        """获取加密图片解析/Get Sign Image  # noqa: E501

        # [中文] ### 用途: - 解析星图加密图片，获取可访问的图片URL - 价格：0.001$ / 次 ### 参数: - uri: 图片的uri，通常从其他星图接口返回的数据中获取     - 例如：`tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ` - durationTS: 有效期时长（秒），默认86400（24小时） - format: 图片格式，默认webp，支持：webp、jpg、png等 ### 返回: - 解析后的图片数据，包含可访问的图片URL  # [English] ### Purpose: - Parse encrypted XingTu image and get accessible image URL - Price: 0.001$ / time ### Parameters: - uri: Image URI, usually obtained from other XingTu API responses     - Example: `tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ` - durationTS: Duration in seconds, default 86400 (24 hours) - format: Image format, default webp, supports: webp, jpg, png, etc. ### Return: - Parsed image data with accessible image URL  # [示例/Example] uri = \"tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ\" durationTS = 86400 format = \"webp\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sign_image_api_v1_douyin_xingtu_get_sign_image_get(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uri: 图片的uri/Image URI (required)
        :param object duration_ts: 有效期时长（秒）/Duration in seconds
        :param object format: 图片格式/Image format
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sign_image_api_v1_douyin_xingtu_get_sign_image_get_with_http_info(uri, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sign_image_api_v1_douyin_xingtu_get_sign_image_get_with_http_info(uri, **kwargs)  # noqa: E501
            return data

    def get_sign_image_api_v1_douyin_xingtu_get_sign_image_get_with_http_info(self, uri, **kwargs):  # noqa: E501
        """获取加密图片解析/Get Sign Image  # noqa: E501

        # [中文] ### 用途: - 解析星图加密图片，获取可访问的图片URL - 价格：0.001$ / 次 ### 参数: - uri: 图片的uri，通常从其他星图接口返回的数据中获取     - 例如：`tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ` - durationTS: 有效期时长（秒），默认86400（24小时） - format: 图片格式，默认webp，支持：webp、jpg、png等 ### 返回: - 解析后的图片数据，包含可访问的图片URL  # [English] ### Purpose: - Parse encrypted XingTu image and get accessible image URL - Price: 0.001$ / time ### Parameters: - uri: Image URI, usually obtained from other XingTu API responses     - Example: `tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ` - durationTS: Duration in seconds, default 86400 (24 hours) - format: Image format, default webp, supports: webp, jpg, png, etc. ### Return: - Parsed image data with accessible image URL  # [示例/Example] uri = \"tos-cn-i-0813c000-ce/oMKzDA3A9QGAuebfsDIAwlDoAfCFEEzSEw8FQZ\" durationTS = 86400 format = \"webp\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sign_image_api_v1_douyin_xingtu_get_sign_image_get_with_http_info(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uri: 图片的uri/Image URI (required)
        :param object duration_ts: 有效期时长（秒）/Duration in seconds
        :param object format: 图片格式/Image format
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uri', 'duration_ts', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sign_image_api_v1_douyin_xingtu_get_sign_image_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uri' is set
        if self.api_client.client_side_validation and ('uri' not in params or
                                                       params['uri'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uri` when calling `get_sign_image_api_v1_douyin_xingtu_get_sign_image_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uri' in params:
            query_params.append(('uri', params['uri']))  # noqa: E501
        if 'duration_ts' in params:
            query_params.append(('durationTS', params['duration_ts']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/get_sign_image', 'GET',
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

    def get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get(self, sec_user_id, **kwargs):  # noqa: E501
        """根据抖音sec_user_id获取游客星图kolid/Get XingTu kolid by Douyin sec_user_id  # noqa: E501

        # [中文] ### 用途: - 通过抖音sec_user_id获取游客星图kolid - 价格：0.001$ / 次 ### 参数: - sec_user_id: sec_user_id, 可以从接口以下接口获取：     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### 返回: - 游客星图kolid  # [English] ### Purpose: - Get XingTu kolid by Douyin sec_user_id - Price: 0.001$ / time ### Parameters: - sec_user_id: sec_user_id, can be obtained from the following interfaces:     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### Return: - XingTu kolid  # [示例/Example] sec_user_id = \"MS4wLjABAAAAoxwUZouIdKL6sZ8EB96KDjkrhfBMS1KbCgsMJR1kIUs\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 抖音用户sec_user_id/Douyin User sec_user_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
            return data

    def get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get_with_http_info(self, sec_user_id, **kwargs):  # noqa: E501
        """根据抖音sec_user_id获取游客星图kolid/Get XingTu kolid by Douyin sec_user_id  # noqa: E501

        # [中文] ### 用途: - 通过抖音sec_user_id获取游客星图kolid - 价格：0.001$ / 次 ### 参数: - sec_user_id: sec_user_id, 可以从接口以下接口获取：     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### 返回: - 游客星图kolid  # [English] ### Purpose: - Get XingTu kolid by Douyin sec_user_id - Price: 0.001$ / time ### Parameters: - sec_user_id: sec_user_id, can be obtained from the following interfaces:     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### Return: - XingTu kolid  # [示例/Example] sec_user_id = \"MS4wLjABAAAAoxwUZouIdKL6sZ8EB96KDjkrhfBMS1KbCgsMJR1kIUs\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get_with_http_info(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 抖音用户sec_user_id/Douyin User sec_user_id (required)
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
                    " to method get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_user_id' is set
        if self.api_client.client_side_validation and ('sec_user_id' not in params or
                                                       params['sec_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_id` when calling `get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get`")  # noqa: E501

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
            '/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id', 'GET',
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

    def get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get(self, uid, **kwargs):  # noqa: E501
        """根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID  # noqa: E501

        # [中文] ### 用途: - 通过抖音用户ID获取游客星图kolid - 价格：0.001$ / 次 ### 参数: - uid: 用户ID, 可以从接口以下接口获取：     - `/api/v1/douyin/web/fetch_user_profile_by_uid`     - `/api/v1/douyin/web/fetch_user_profile_by_short_id`     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### 返回: - 游客星图kolid  # [English] ### Purpose: - Get XingTu kolid by Douyin User ID - Price: 0.001$ / time ### Parameters: - uid: User ID, can be obtained from the following interfaces:     - `/api/v1/douyin/web/fetch_user_profile_by_uid`     - `/api/v1/douyin/web/fetch_user_profile_by_short_id`     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### Return: - XingTu kolid  # [示例/Example] uid = \"70452002324\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 抖音用户ID/Douyin User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID  # noqa: E501

        # [中文] ### 用途: - 通过抖音用户ID获取游客星图kolid - 价格：0.001$ / 次 ### 参数: - uid: 用户ID, 可以从接口以下接口获取：     - `/api/v1/douyin/web/fetch_user_profile_by_uid`     - `/api/v1/douyin/web/fetch_user_profile_by_short_id`     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### 返回: - 游客星图kolid  # [English] ### Purpose: - Get XingTu kolid by Douyin User ID - Price: 0.001$ / time ### Parameters: - uid: User ID, can be obtained from the following interfaces:     - `/api/v1/douyin/web/fetch_user_profile_by_uid`     - `/api/v1/douyin/web/fetch_user_profile_by_short_id`     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### Return: - XingTu kolid  # [示例/Example] uid = \"70452002324\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 抖音用户ID/Douyin User ID (required)
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
                    " to method get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get`")  # noqa: E501

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
            '/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid', 'GET',
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

    def get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get(self, unique_id, **kwargs):  # noqa: E501
        """根据抖音号获取游客星图kolid/Get XingTu kolid by Douyin unique_id  # noqa: E501

        # [中文] ### 用途: - 通过抖音号获取游客星图kolid - 价格：0.001$ / 次 ### 参数: - unique_id: 抖音号, 可以从接口以下接口获取：     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### 返回: - 游客星图kolid  # [English] ### Purpose: - Get XingTu kolid by Douyin unique_id - Price: 0.001$ / time ### Parameters: - unique_id: unique_id, can be obtained from the following interfaces:     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### Return: - XingTu kolid  # [示例/Example] unique_id = \"m6640150\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object unique_id: 抖音号/Douyin User unique_id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get_with_http_info(unique_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get_with_http_info(unique_id, **kwargs)  # noqa: E501
            return data

    def get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get_with_http_info(self, unique_id, **kwargs):  # noqa: E501
        """根据抖音号获取游客星图kolid/Get XingTu kolid by Douyin unique_id  # noqa: E501

        # [中文] ### 用途: - 通过抖音号获取游客星图kolid - 价格：0.001$ / 次 ### 参数: - unique_id: 抖音号, 可以从接口以下接口获取：     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### 返回: - 游客星图kolid  # [English] ### Purpose: - Get XingTu kolid by Douyin unique_id - Price: 0.001$ / time ### Parameters: - unique_id: unique_id, can be obtained from the following interfaces:     - `/api/v1/douyin/web/handler_user_profile`     - `/api/v1/douyin/web/handler_user_profile_v2`     - `/api/v1/douyin/web/handler_user_profile_v3`     - `/api/v1/douyin/app/v3/handler_user_profile` ### Return: - XingTu kolid  # [示例/Example] unique_id = \"m6640150\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get_with_http_info(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object unique_id: 抖音号/Douyin User unique_id (required)
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
                    " to method get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'unique_id' is set
        if self.api_client.client_side_validation and ('unique_id' not in params or
                                                       params['unique_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `unique_id` when calling `get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get`")  # noqa: E501

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
            '/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id', 'GET',
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

    def kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get(self, kol_id, **kwargs):  # noqa: E501
        """获取kol观众画像V1/Get kol Audience Portrait V1  # noqa: E501

        # [中文] ### 用途: - 获取kol观众画像V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol观众画像  # [English] ### Purpose: - Get kol Audience Portrait V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Audience Portrait  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
            return data

    def kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get_with_http_info(self, kol_id, **kwargs):  # noqa: E501
        """获取kol观众画像V1/Get kol Audience Portrait V1  # noqa: E501

        # [中文] ### 用途: - 获取kol观众画像V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol观众画像  # [English] ### Purpose: - Get kol Audience Portrait V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Audience Portrait  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get_with_http_info(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_audience_portrait_v1', 'GET',
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

    def kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get(self, kol_id, platform_channel, **kwargs):  # noqa: E501
        """获取kol基本信息V1/Get kol Base Info V1  # noqa: E501

        # [中文] ### 用途: - 获取kol基本信息V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - platformChannel:     - 平台渠道，支持以下参数:     - _1 :抖音短视频(Video)     - _10 :抖音直播(Live) ### 返回: - kol基本信息  # [English] ### Purpose: - Get kol Base Info V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - platformChannel:     - Platform channel, supports the following parameters:     - _1 :Douyin Video     - _10 :Douyin Live ### Return: - kol Base Info  # [示例/Example] kolId = \"7048929565493690398\" platformChannel = \"_1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get(kol_id, platform_channel, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object platform_channel: 平台渠道/Platform Channel (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get_with_http_info(kol_id, platform_channel, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get_with_http_info(kol_id, platform_channel, **kwargs)  # noqa: E501
            return data

    def kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get_with_http_info(self, kol_id, platform_channel, **kwargs):  # noqa: E501
        """获取kol基本信息V1/Get kol Base Info V1  # noqa: E501

        # [中文] ### 用途: - 获取kol基本信息V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - platformChannel:     - 平台渠道，支持以下参数:     - _1 :抖音短视频(Video)     - _10 :抖音直播(Live) ### 返回: - kol基本信息  # [English] ### Purpose: - Get kol Base Info V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - platformChannel:     - Platform channel, supports the following parameters:     - _1 :Douyin Video     - _10 :Douyin Live ### Return: - kol Base Info  # [示例/Example] kolId = \"7048929565493690398\" platformChannel = \"_1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get_with_http_info(kol_id, platform_channel, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object platform_channel: 平台渠道/Platform Channel (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id', 'platform_channel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get`")  # noqa: E501
        # verify the required parameter 'platform_channel' is set
        if self.api_client.client_side_validation and ('platform_channel' not in params or
                                                       params['platform_channel'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `platform_channel` when calling `kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501
        if 'platform_channel' in params:
            query_params.append(('platformChannel', params['platform_channel']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_base_info_v1', 'GET',
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

    def kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get(self, kol_id, range, **kwargs):  # noqa: E501
        """获取kol转化能力分析V1/Get kol Conversion Ability Analysis V1  # noqa: E501

        # [中文] ### 用途: - 获取kol转化能力分析V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - _range: 时间范围, 支持以下参数:     - _1 :近7天(last 7 days)     - _2 :30天(last 30 days)     - _3 :90天(last 90 days) ### 返回: - kol转化能力分析  # [English] ### Purpose: - Get kol Conversion Ability Analysis V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - _range: Time range, supports the following parameters:     - _1 :Last 7 days     - _2 :Last 30 days     - _3 :Last 90 days ### Return: - kol Conversion Ability Analysis  # [示例/Example] kolId = \"7048929565493690398\" _range = \"_1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get(kol_id, range, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object range: 时间范围/Time Range (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get_with_http_info(kol_id, range, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get_with_http_info(kol_id, range, **kwargs)  # noqa: E501
            return data

    def kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get_with_http_info(self, kol_id, range, **kwargs):  # noqa: E501
        """获取kol转化能力分析V1/Get kol Conversion Ability Analysis V1  # noqa: E501

        # [中文] ### 用途: - 获取kol转化能力分析V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - _range: 时间范围, 支持以下参数:     - _1 :近7天(last 7 days)     - _2 :30天(last 30 days)     - _3 :90天(last 90 days) ### 返回: - kol转化能力分析  # [English] ### Purpose: - Get kol Conversion Ability Analysis V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - _range: Time range, supports the following parameters:     - _1 :Last 7 days     - _2 :Last 30 days     - _3 :Last 90 days ### Return: - kol Conversion Ability Analysis  # [示例/Example] kolId = \"7048929565493690398\" _range = \"_1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get_with_http_info(kol_id, range, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object range: 时间范围/Time Range (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id', 'range']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get`")  # noqa: E501
        # verify the required parameter 'range' is set
        if self.api_client.client_side_validation and ('range' not in params or
                                                       params['range'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `range` when calling `kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501
        if 'range' in params:
            query_params.append(('_range', params['range']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_conversion_ability_analysis_v1', 'GET',
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

    def kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get(self, kol_id, detail_type, page, **kwargs):  # noqa: E501
        """获取kol转化视频展示V1/Get kol Convert Video Display V1  # noqa: E501

        # [中文] ### 用途: - 获取kol转化视频展示V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - detailType: 详情类型, 支持以下参数:     - _1 :相关视频数据(Video Data)     - _2 :相关商品数据(Product Data) ### 返回: - kol转化视频展示  # [English] ### Purpose: - Get kol Convert Video Display V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - detailType: Detail type, supports the following parameters:     - _1 :Video Data     - _2 :Product Data - page: Page number, starting from 1 ### Return: - kol Convert Video Display  # [示例/Example] kolId = \"7048929565493690398\" detailType = \"_1\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get(kol_id, detail_type, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object detail_type: 详情类型/Detail Type (required)
        :param object page: 页码/Page (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get_with_http_info(kol_id, detail_type, page, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get_with_http_info(kol_id, detail_type, page, **kwargs)  # noqa: E501
            return data

    def kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get_with_http_info(self, kol_id, detail_type, page, **kwargs):  # noqa: E501
        """获取kol转化视频展示V1/Get kol Convert Video Display V1  # noqa: E501

        # [中文] ### 用途: - 获取kol转化视频展示V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - detailType: 详情类型, 支持以下参数:     - _1 :相关视频数据(Video Data)     - _2 :相关商品数据(Product Data) ### 返回: - kol转化视频展示  # [English] ### Purpose: - Get kol Convert Video Display V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - detailType: Detail type, supports the following parameters:     - _1 :Video Data     - _2 :Product Data - page: Page number, starting from 1 ### Return: - kol Convert Video Display  # [示例/Example] kolId = \"7048929565493690398\" detailType = \"_1\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get_with_http_info(kol_id, detail_type, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object detail_type: 详情类型/Detail Type (required)
        :param object page: 页码/Page (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id', 'detail_type', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get`")  # noqa: E501
        # verify the required parameter 'detail_type' is set
        if self.api_client.client_side_validation and ('detail_type' not in params or
                                                       params['detail_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `detail_type` when calling `kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if self.api_client.client_side_validation and ('page' not in params or
                                                       params['page'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page` when calling `kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501
        if 'detail_type' in params:
            query_params.append(('detailType', params['detail_type']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_convert_video_display_v1', 'GET',
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

    def kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get(self, kol_id, **kwargs):  # noqa: E501
        """获取kol性价比能力分析V1/Get kol Cp Info V1  # noqa: E501

        # [中文] ### 用途: - 获取kol性价比能力分析V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol性价比能力分析  # [English] ### Purpose: - Get kol Cp Info V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Cp Info  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
            return data

    def kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get_with_http_info(self, kol_id, **kwargs):  # noqa: E501
        """获取kol性价比能力分析V1/Get kol Cp Info V1  # noqa: E501

        # [中文] ### 用途: - 获取kol性价比能力分析V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol性价比能力分析  # [English] ### Purpose: - Get kol Cp Info V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Cp Info  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get_with_http_info(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_cp_info_v1', 'GET',
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

    def kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get(self, kol_id, start_date, end_date, **kwargs):  # noqa: E501
        """获取kol粉丝趋势V1/Get kol Daily Fans V1  # noqa: E501

        # [中文] ### 用途: - 获取kol粉丝趋势V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - startDate: 开始日期，格式为：yyyy-MM-dd - endDate: 结束日期，格式为：yyyy-MM-dd ### 返回: - kol粉丝趋势  # [English] ### Purpose: - Get kol Daily Fans V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - startDate: Start date, format: yyyy-MM-dd - endDate: End date, format: yyyy-MM-dd ### Return: - kol Daily Fans  # [示例/Example] kolId = \"7048929565493690398\" startDate = \"2024-12-01\" endDate = \"2025-01-01\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get(kol_id, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object start_date: 开始日期/Start Date (required)
        :param object end_date: 结束日期/End Date (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get_with_http_info(kol_id, start_date, end_date, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get_with_http_info(kol_id, start_date, end_date, **kwargs)  # noqa: E501
            return data

    def kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get_with_http_info(self, kol_id, start_date, end_date, **kwargs):  # noqa: E501
        """获取kol粉丝趋势V1/Get kol Daily Fans V1  # noqa: E501

        # [中文] ### 用途: - 获取kol粉丝趋势V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - startDate: 开始日期，格式为：yyyy-MM-dd - endDate: 结束日期，格式为：yyyy-MM-dd ### 返回: - kol粉丝趋势  # [English] ### Purpose: - Get kol Daily Fans V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - startDate: Start date, format: yyyy-MM-dd - endDate: End date, format: yyyy-MM-dd ### Return: - kol Daily Fans  # [示例/Example] kolId = \"7048929565493690398\" startDate = \"2024-12-01\" endDate = \"2025-01-01\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get_with_http_info(kol_id, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object start_date: 开始日期/Start Date (required)
        :param object end_date: 结束日期/End Date (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id', 'start_date', 'end_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get`")  # noqa: E501
        # verify the required parameter 'start_date' is set
        if self.api_client.client_side_validation and ('start_date' not in params or
                                                       params['start_date'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `start_date` when calling `kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get`")  # noqa: E501
        # verify the required parameter 'end_date' is set
        if self.api_client.client_side_validation and ('end_date' not in params or
                                                       params['end_date'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `end_date` when calling `kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_daily_fans_v1', 'GET',
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

    def kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get(self, kol_id, type, range, flow_type, **kwargs):  # noqa: E501
        """获取kol数据概览V1/Get kol Data Overview V1  # noqa: E501

        # [中文] ### 用途: - 获取kol数据概览V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - _type: 类型, 支持以下参数:     - _1 :个人视频(personal video)     - _2 :星图视频(xingtu video) - _range: 范围, 支持以下参数:     - _2 :近30天(last 30 days)     - _3 :近90天(last 90 days) - flowType: 流量类型, 支持以下参数:     - 1 : 默认(default) - onlyAssign (可选): 是否指派，具体参数如下:     - 不传递 : 使用API默认行为     - false : 全部数据     - true : 仅指派数据 ### 返回: - kol数据概览  # [English] ### Purpose: - Get kol Data Overview V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - _type: Type, supports the following parameters:     - _1 :Personal Video     - _2 :Xingtu Video - _range: Range, supports the following parameters:     - _2 :Last 30 days     - _3 :Last 90 days - flowType: Flow Type, supports the following parameters:     - 1 : Default - onlyAssign (optional): Whether assigned, the specific parameters are as follows:     - Not provided : Use API default behavior     - false : All data     - true : Only assigned data ### Return: - kol Data Overview  # [示例/Example] kolId = \"7048929565493690398\" _type = \"_1\" _range = \"_2\" flowType = 1 onlyAssign = None  # or True/False if needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get(kol_id, type, range, flow_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object type: 类型/Type (required)
        :param object range: 范围/Range (required)
        :param object flow_type: 流量类型/Flow Type (required)
        :param object only_assign: 是否指派/Whether assigned (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get_with_http_info(kol_id, type, range, flow_type, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get_with_http_info(kol_id, type, range, flow_type, **kwargs)  # noqa: E501
            return data

    def kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get_with_http_info(self, kol_id, type, range, flow_type, **kwargs):  # noqa: E501
        """获取kol数据概览V1/Get kol Data Overview V1  # noqa: E501

        # [中文] ### 用途: - 获取kol数据概览V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - _type: 类型, 支持以下参数:     - _1 :个人视频(personal video)     - _2 :星图视频(xingtu video) - _range: 范围, 支持以下参数:     - _2 :近30天(last 30 days)     - _3 :近90天(last 90 days) - flowType: 流量类型, 支持以下参数:     - 1 : 默认(default) - onlyAssign (可选): 是否指派，具体参数如下:     - 不传递 : 使用API默认行为     - false : 全部数据     - true : 仅指派数据 ### 返回: - kol数据概览  # [English] ### Purpose: - Get kol Data Overview V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - _type: Type, supports the following parameters:     - _1 :Personal Video     - _2 :Xingtu Video - _range: Range, supports the following parameters:     - _2 :Last 30 days     - _3 :Last 90 days - flowType: Flow Type, supports the following parameters:     - 1 : Default - onlyAssign (optional): Whether assigned, the specific parameters are as follows:     - Not provided : Use API default behavior     - false : All data     - true : Only assigned data ### Return: - kol Data Overview  # [示例/Example] kolId = \"7048929565493690398\" _type = \"_1\" _range = \"_2\" flowType = 1 onlyAssign = None  # or True/False if needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get_with_http_info(kol_id, type, range, flow_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object type: 类型/Type (required)
        :param object range: 范围/Range (required)
        :param object flow_type: 流量类型/Flow Type (required)
        :param object only_assign: 是否指派/Whether assigned (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id', 'type', 'range', 'flow_type', 'only_assign']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get`")  # noqa: E501
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and ('type' not in params or
                                                       params['type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `type` when calling `kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get`")  # noqa: E501
        # verify the required parameter 'range' is set
        if self.api_client.client_side_validation and ('range' not in params or
                                                       params['range'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `range` when calling `kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get`")  # noqa: E501
        # verify the required parameter 'flow_type' is set
        if self.api_client.client_side_validation and ('flow_type' not in params or
                                                       params['flow_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `flow_type` when calling `kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501
        if 'type' in params:
            query_params.append(('_type', params['type']))  # noqa: E501
        if 'range' in params:
            query_params.append(('_range', params['range']))  # noqa: E501
        if 'flow_type' in params:
            query_params.append(('flowType', params['flow_type']))  # noqa: E501
        if 'only_assign' in params:
            query_params.append(('onlyAssign', params['only_assign']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_data_overview_v1', 'GET',
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

    def kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get(self, kol_id, **kwargs):  # noqa: E501
        """获取kol粉丝画像V1/Get kol Fans Portrait V1  # noqa: E501

        # [中文] ### 用途: - 获取kol粉丝画像V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - fansType: 粉丝类型，支持以下参数:     - _1: 粉丝画像 (Fans Portrait) - 默认值     - _2: 粉丝团画像 (Fans Group Portrait)     - _5: 铁粉画像 (Iron Fans Portrait) ### 返回: - kol粉丝画像  # [English] ### Purpose: - Get kol Fans Portrait V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - fansType: Fans Type, supports the following parameters:     - _1: Fans Portrait - Default     - _2: Fans Group Portrait     - _5: Iron Fans Portrait ### Return: - kol Fans Portrait  # [示例/Example] kolId = \"7048929565493690398\" fansType = \"_1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object fans_type: 粉丝类型/Fans Type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
            return data

    def kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get_with_http_info(self, kol_id, **kwargs):  # noqa: E501
        """获取kol粉丝画像V1/Get kol Fans Portrait V1  # noqa: E501

        # [中文] ### 用途: - 获取kol粉丝画像V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - fansType: 粉丝类型，支持以下参数:     - _1: 粉丝画像 (Fans Portrait) - 默认值     - _2: 粉丝团画像 (Fans Group Portrait)     - _5: 铁粉画像 (Iron Fans Portrait) ### 返回: - kol粉丝画像  # [English] ### Purpose: - Get kol Fans Portrait V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - fansType: Fans Type, supports the following parameters:     - _1: Fans Portrait - Default     - _2: Fans Group Portrait     - _5: Iron Fans Portrait ### Return: - kol Fans Portrait  # [示例/Example] kolId = \"7048929565493690398\" fansType = \"_1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get_with_http_info(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object fans_type: 粉丝类型/Fans Type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id', 'fans_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501
        if 'fans_type' in params:
            query_params.append(('fansType', params['fans_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_fans_portrait_v1', 'GET',
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

    def kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get(self, kol_id, **kwargs):  # noqa: E501
        """获取kol连接用户V1/Get kol Link Struct V1  # noqa: E501

        # [中文] ### 用途: - 获取kol连接用户V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol连接用户  # [English] ### Purpose: - Get kol Link Struct V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Link Struct  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
            return data

    def kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get_with_http_info(self, kol_id, **kwargs):  # noqa: E501
        """获取kol连接用户V1/Get kol Link Struct V1  # noqa: E501

        # [中文] ### 用途: - 获取kol连接用户V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol连接用户  # [English] ### Purpose: - Get kol Link Struct V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Link Struct  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get_with_http_info(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_link_struct_v1', 'GET',
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

    def kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get(self, kol_id, **kwargs):  # noqa: E501
        """获取kol内容表现V1/Get kol Rec Videos V1  # noqa: E501

        # [中文] ### 用途: - 获取kol内容表现V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol内容表现  # [English] ### Purpose: - Get kol Rec Videos V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Rec Videos  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
            return data

    def kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get_with_http_info(self, kol_id, **kwargs):  # noqa: E501
        """获取kol内容表现V1/Get kol Rec Videos V1  # noqa: E501

        # [中文] ### 用途: - 获取kol内容表现V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol内容表现  # [English] ### Purpose: - Get kol Rec Videos V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Rec Videos  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get_with_http_info(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_rec_videos_v1', 'GET',
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

    def kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get(self, kol_id, platform_channel, **kwargs):  # noqa: E501
        """获取kol服务报价V1/Get kol Service Price V1  # noqa: E501

        # [中文] ### 用途: - 获取kol服务报价V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - platformChannel:     - 平台渠道，支持以下参数:     - _1: 抖音短视频(Video)     - _10: 抖音直播(Live) ### 返回: kol服务报价  # [English] ### Purpose: - Get kol Service Price V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - platformChannel:     - Platform channel, supports the following parameters:     - _1: Douyin Video     - _10: Douyin Live ### Return: - kol Service Price  # [示例/Example] kolId = \"7048929565493690398\" platformChannel = \"_1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get(kol_id, platform_channel, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object platform_channel: 平台渠道/Platform Channel (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get_with_http_info(kol_id, platform_channel, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get_with_http_info(kol_id, platform_channel, **kwargs)  # noqa: E501
            return data

    def kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get_with_http_info(self, kol_id, platform_channel, **kwargs):  # noqa: E501
        """获取kol服务报价V1/Get kol Service Price V1  # noqa: E501

        # [中文] ### 用途: - 获取kol服务报价V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - platformChannel:     - 平台渠道，支持以下参数:     - _1: 抖音短视频(Video)     - _10: 抖音直播(Live) ### 返回: kol服务报价  # [English] ### Purpose: - Get kol Service Price V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - platformChannel:     - Platform channel, supports the following parameters:     - _1: Douyin Video     - _10: Douyin Live ### Return: - kol Service Price  # [示例/Example] kolId = \"7048929565493690398\" platformChannel = \"_1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get_with_http_info(kol_id, platform_channel, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object platform_channel: 平台渠道/Platform Channel (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id', 'platform_channel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get`")  # noqa: E501
        # verify the required parameter 'platform_channel' is set
        if self.api_client.client_side_validation and ('platform_channel' not in params or
                                                       params['platform_channel'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `platform_channel` when calling `kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501
        if 'platform_channel' in params:
            query_params.append(('platformChannel', params['platform_channel']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_service_price_v1', 'GET',
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

    def kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get(self, kol_id, **kwargs):  # noqa: E501
        """获取kol连接用户来源V1/Get kol Touch Distribution V1  # noqa: E501

        # [中文] ### 用途: - 获取kol连接用户来源V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol连接用户来源  # [English] ### Purpose: - Get kol Touch Distribution V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Touch Distribution  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
            return data

    def kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get_with_http_info(self, kol_id, **kwargs):  # noqa: E501
        """获取kol连接用户来源V1/Get kol Touch Distribution V1  # noqa: E501

        # [中文] ### 用途: - 获取kol连接用户来源V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol连接用户来源  # [English] ### Purpose: - Get kol Touch Distribution V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Touch Distribution  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get_with_http_info(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_touch_distribution_v1', 'GET',
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

    def kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get(self, kol_id, only_assign, **kwargs):  # noqa: E501
        """获取kol视频表现V1/Get kol Video Performance V1  # noqa: E501

        # [中文] ### 用途: - 获取kol视频表现V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - onlyAssign: 是否只显示分配作品，具体参数如下:     - false : 显示全部，包括个人作品和分配作品，默认值。     - true : 只显示来自星图的分配作品。 ### 返回: - kol视频表现  # [English] ### Purpose: - Get kol Video Performance V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - onlyAssign: Whether to display only assigned works, the specific parameters are as follows:     - false : Show all, including personal works and assigned works, default value.     - true : Only display assigned works from XingTu. ### Return: - kol Video Performance  # [示例/Example] kolId = \"7048929565493690398\" onlyAssign = False  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get(kol_id, only_assign, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object only_assign: 是否只显示分配作品/Whether to display only assigned works (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get_with_http_info(kol_id, only_assign, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get_with_http_info(kol_id, only_assign, **kwargs)  # noqa: E501
            return data

    def kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get_with_http_info(self, kol_id, only_assign, **kwargs):  # noqa: E501
        """获取kol视频表现V1/Get kol Video Performance V1  # noqa: E501

        # [中文] ### 用途: - 获取kol视频表现V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - onlyAssign: 是否只显示分配作品，具体参数如下:     - false : 显示全部，包括个人作品和分配作品，默认值。     - true : 只显示来自星图的分配作品。 ### 返回: - kol视频表现  # [English] ### Purpose: - Get kol Video Performance V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` - onlyAssign: Whether to display only assigned works, the specific parameters are as follows:     - false : Show all, including personal works and assigned works, default value.     - true : Only display assigned works from XingTu. ### Return: - kol Video Performance  # [示例/Example] kolId = \"7048929565493690398\" onlyAssign = False  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get_with_http_info(kol_id, only_assign, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :param object only_assign: 是否只显示分配作品/Whether to display only assigned works (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id', 'only_assign']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get`")  # noqa: E501
        # verify the required parameter 'only_assign' is set
        if self.api_client.client_side_validation and ('only_assign' not in params or
                                                       params['only_assign'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `only_assign` when calling `kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501
        if 'only_assign' in params:
            query_params.append(('onlyAssign', params['only_assign']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_video_performance_v1', 'GET',
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

    def kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get(self, kol_id, **kwargs):  # noqa: E501
        """获取kol星图指数V1/Get kol Xingtu Index V1  # noqa: E501

        # [中文] ### 用途: - 获取kol星图指数V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol星图指数  # [English] ### Purpose: - Get kol Xingtu Index V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Xingtu Index  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
        else:
            (data) = self.kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get_with_http_info(kol_id, **kwargs)  # noqa: E501
            return data

    def kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get_with_http_info(self, kol_id, **kwargs):  # noqa: E501
        """获取kol星图指数V1/Get kol Xingtu Index V1  # noqa: E501

        # [中文] ### 用途: - 获取kol星图指数V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - kolId: 用户的kolId, 可以从接口以下接口获取：     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### 返回: - kol星图指数  # [English] ### Purpose: - Get kol Xingtu Index V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - kolId: User kolId, can be obtained from the following interfaces:     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`     - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id` ### Return: - kol Xingtu Index  # [示例/Example] kolId = \"7048929565493690398\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get_with_http_info(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 用户的kolId/User kolId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kolId', params['kol_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/kol_xingtu_index_v1', 'GET',
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

    def search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get(self, keyword, platform_source, page, **kwargs):  # noqa: E501
        """关键词搜索kol V1/Search Kol V1  # noqa: E501

        # [中文] ### 用途: - 关键词搜索kol V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - keyword: 关键词 - platformSource:     - 平台来源，支持以下参数:     - _1 :抖音(douyin)     - _2 :头条(toutiao)     - _3 :西瓜(xigua) - page: 页码，从1开始 ### 返回: - kol列表  # [English] ### Purpose: - Search Kol V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - keyword: Keyword - platformSource:     - Platform source, supports the following parameters:     - _1 :Douyin     - _2 :Toutiao     - _3 :Xigua - page: Page number, starting from 1 ### Return: - Kol List  # [示例/Example] keyword = \"人工智能\" platformSource = \"_1\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get(keyword, platform_source, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object platform_source: 平台来源/Platform Source (required)
        :param object page: 页码/Page (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get_with_http_info(keyword, platform_source, page, **kwargs)  # noqa: E501
        else:
            (data) = self.search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get_with_http_info(keyword, platform_source, page, **kwargs)  # noqa: E501
            return data

    def search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get_with_http_info(self, keyword, platform_source, page, **kwargs):  # noqa: E501
        """关键词搜索kol V1/Search Kol V1  # noqa: E501

        # [中文] ### 用途: - 关键词搜索kol V1 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - keyword: 关键词 - platformSource:     - 平台来源，支持以下参数:     - _1 :抖音(douyin)     - _2 :头条(toutiao)     - _3 :西瓜(xigua) - page: 页码，从1开始 ### 返回: - kol列表  # [English] ### Purpose: - Search Kol V1 - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - keyword: Keyword - platformSource:     - Platform source, supports the following parameters:     - _1 :Douyin     - _2 :Toutiao     - _3 :Xigua - page: Page number, starting from 1 ### Return: - Kol List  # [示例/Example] keyword = \"人工智能\" platformSource = \"_1\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get_with_http_info(keyword, platform_source, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object platform_source: 平台来源/Platform Source (required)
        :param object page: 页码/Page (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'platform_source', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get`")  # noqa: E501
        # verify the required parameter 'platform_source' is set
        if self.api_client.client_side_validation and ('platform_source' not in params or
                                                       params['platform_source'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `platform_source` when calling `search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if self.api_client.client_side_validation and ('page' not in params or
                                                       params['page'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page` when calling `search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'platform_source' in params:
            query_params.append(('platformSource', params['platform_source']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/search_kol_v1', 'GET',
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

    def search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get(self, keyword, **kwargs):  # noqa: E501
        """高级搜索kol V2/Search Kol Advanced V2  # noqa: E501

        # [中文] ### 用途: - 高级搜索kol V2，支持粉丝范围和内容标签筛选 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - keyword: 关键词 - followerRange (可选): 粉丝范围，格式：最小值-最大值     - 例如：10-100 表示粉丝范围在 10万-100万 之间     - 不传递此参数则不限制粉丝范围 - contentTag (可选): 内容标签，支持以下格式:     - tag-{id}: 一级标签，例如 tag-1 (美妆)     - tag_level_two-{id}: 二级标签，例如 tag_level_two-7 (穿搭)     - 标签列表参考文档中的 contentTag 映射表     - 不传递此参数则不限制内容标签 ### 返回: - kol列表（支持高级筛选）  # [English] ### Purpose: - Advanced Search Kol V2, supports follower range and content tag filtering - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - keyword: Keyword - followerRange (optional): Follower range, format: min-max     - Example: 10-100 indicates follower range between 100,000 and 1,000,000     - Do not pass this parameter to not limit the follower range - contentTag (optional): Content tag, supports the following formats:     - tag-{id}: First-level tag, e.g., tag-1 (Beauty)     - tag_level_two-{id}: Second-level tag, e.g., tag_level_two-7 (Outfit)     - Refer to the contentTag mapping table in the documentation     - Do not pass this parameter to not limit content tags ### Return: - Kol List (with advanced filtering)  # [示例/Example] keyword = \"美妆\" followerRange = \"10-100\"  # 10万-100万粉丝 contentTag = \"tag-1\"  # 美妆一级标签 contentTag = \"tag_level_two-2\"  # 美妆教程二级标签  # [内容标签映射表/Content Tag Mapping]  ## 一级标签 (First-level tags) - 格式: tag-{id}  | 参数 | 分类 | 参数 | 分类 | 参数 | 分类 | |------|------|------|------|------|------| | tag-1 | 美妆 | tag-6 | 时尚 | tag-11 | 萌宠 | | tag-15 | 测评 | tag-23 | 游戏 | tag-25 | 二次元 | | tag-27 | 旅行 | tag-31 | 汽车 | tag-36 | 生活 | | tag-41 | 音乐 | tag-46 | 舞蹈* | tag-48 | 美食 | | tag-55 | 母婴亲子 | tag-60 | 运动健身 | tag-64 | 科技数码 | | tag-68 | 教育培训 | tag-72 | 颜值达人 | tag-79 | 才艺技能 | | tag-85 | 影视娱乐 | tag-87 | 艺术文化 | tag-91 | 财经投资 | | tag-95 | 三农* | tag-97 | 剧情搞笑 | tag-100 | 情感* | | tag-102 | 园艺* | tag-130 | 随拍* | tag-139 | 房产 | | tag-1001 | 生活家居 | tag-1002 | 媒体号* | | |  *注: 标记*的分类无二级标签  ## 二级标签 (Second-level tags) - 格式: tag_level_two-{id}  ### 美妆 (tag-1) - tag_level_two-2: 美妆教程 - tag_level_two-3: 妆容展示 - tag_level_two-4: 护肤保养 - tag_level_two-5: 美妆测评种草  ### 时尚 (tag-6) - tag_level_two-7: 穿搭 - tag_level_two-8: 街拍 - tag_level_two-10: 造型 - tag_level_two-135: 时尚媒体  ### 萌宠 (tag-11) - tag_level_two-12: 日常宠物 - tag_level_two-13: 特别宠物 - tag_level_two-14: 宠物周边  ### 测评 (tag-15) - tag_level_two-16: 美妆测评 - tag_level_two-17: 3C数码测评 - tag_level_two-18: 汽车测评 - tag_level_two-19: 美食产品测评 - tag_level_two-20: 母婴产品测评 - tag_level_two-21: 综合测评 - tag_level_two-132: 酒店测评  ### 游戏 (tag-23) - tag_level_two-121: 游戏剧情 - tag_level_two-122: 游戏解说 - tag_level_two-123: 游戏资讯 - tag_level_two-124: 游戏其他 - tag_level_two-440: 游戏录屏 - tag_level_two-441: 游戏集锦  ### 二次元 (tag-25) - tag_level_two-125: 二次元真人 - tag_level_two-126: 动画漫画 - tag_level_two-127: 配音声优 - tag_level_two-128: 宅物手办  ### 旅行 (tag-27) - tag_level_two-28: 旅行记录 - tag_level_two-29: 旅行攻略 - tag_level_two-30: 旅行推荐 - tag_level_two-442: 户外生活  ### 汽车 (tag-31) - tag_level_two-32: 汽车测评 - tag_level_two-33: 汽车知识 - tag_level_two-34: 汽车周边  ### 生活 (tag-36) - tag_level_two-37: 生活记录 - tag_level_two-39: 生活小窍门 - tag_level_two-40: 好物推荐 - tag_level_two-118: 健康养生 - tag_level_two-422: 婚恋  ### 音乐 (tag-41) - tag_level_two-42: 歌曲演唱 - tag_level_two-43: 乐器演奏 - tag_level_two-44: 音乐教学 - tag_level_two-45: 音乐其他 - tag_level_two-136: 音乐剪辑  ### 美食 (tag-48) - tag_level_two-49: 美食教程 - tag_level_two-50: 美食探店 - tag_level_two-52: 美食产品测评 - tag_level_two-53: 乡村野食 - tag_level_two-54: 美食其他 - tag_level_two-423: 酒类  ### 母婴亲子 (tag-55) - tag_level_two-56: 育儿科普 - tag_level_two-57: 萌娃日常 - tag_level_two-58: 亲子互动 - tag_level_two-59: 测评种草  ### 运动健身 (tag-60) - tag_level_two-61: 健身 - tag_level_two-63: 极限运动 - tag_level_two-424: 体育资讯 - tag_level_two-443: 冰雪 - tag_level_two-444: 垂钓 - tag_level_two-445: 格斗 - tag_level_two-446: 球类项目 - tag_level_two-447: 综合体育  ### 科技数码 (tag-64) - tag_level_two-65: 3C数码 - tag_level_two-66: 家居电器 - tag_level_two-133: 科技  ### 教育培训 (tag-68) - tag_level_two-69: 考学培训 - tag_level_two-70: 语言教学 - tag_level_two-71: 个人管理 - tag_level_two-425: 职业教育  ### 颜值达人 (tag-72) - tag_level_two-73: 美女 - tag_level_two-74: 帅哥  ### 才艺技能 (tag-79) - tag_level_two-80: 创意才能 - tag_level_two-81: 手工 - tag_level_two-82: 摄影 - tag_level_two-83: 绘画 - tag_level_two-84: 其他才艺  ### 影视娱乐 (tag-85) - tag_level_two-413: 影视解说 - tag_level_two-414: 影视混剪 - tag_level_two-415: 明星资讯 - tag_level_two-416: 综艺解说 - tag_level_two-417: 综艺混剪  ### 艺术文化 (tag-87) - tag_level_two-88: 传统文化 - tag_level_two-89: 人文科普 - tag_level_two-90: 自然科学  ### 财经投资 (tag-91) - tag_level_two-92: 传统金融 - tag_level_two-93: 互联网金融 - tag_level_two-94: 财经知识  ### 剧情搞笑 (tag-97) - tag_level_two-98: 剧情 - tag_level_two-99: 搞笑  ### 生活家居 (tag-1001) - tag_level_two-100101: 硬装 - tag_level_two-100102: 软装 - tag_level_two-100103: 生活技巧 - tag_level_two-100104: 家居氛围  ### 房产 (tag-139) - tag_level_two-140: 其他房产 - tag_level_two-437: 房产知识 - tag_level_two-439: 房产及投资 - tag_level_two-448: 楼盘评测 - tag_level_two-449: 楼市资讯 - tag_level_two-450: 租房  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object follower_range: 粉丝范围(可选)/Follower Range (optional), 例如 10-100 表示10万-100万粉丝
        :param object content_tag: 内容标签(可选)/Content Tag (optional), 例如 tag-1 或 tag_level_two-7
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """高级搜索kol V2/Search Kol Advanced V2  # noqa: E501

        # [中文] ### 用途: - 高级搜索kol V2，支持粉丝范围和内容标签筛选 - 该接口数据使用企业账号进行请求，收费较贵。 - 价格：0.02$ / 次 ### 参数: - keyword: 关键词 - followerRange (可选): 粉丝范围，格式：最小值-最大值     - 例如：10-100 表示粉丝范围在 10万-100万 之间     - 不传递此参数则不限制粉丝范围 - contentTag (可选): 内容标签，支持以下格式:     - tag-{id}: 一级标签，例如 tag-1 (美妆)     - tag_level_two-{id}: 二级标签，例如 tag_level_two-7 (穿搭)     - 标签列表参考文档中的 contentTag 映射表     - 不传递此参数则不限制内容标签 ### 返回: - kol列表（支持高级筛选）  # [English] ### Purpose: - Advanced Search Kol V2, supports follower range and content tag filtering - The interface data is requested using an enterprise account, which is more expensive. - Price: 0.02$ / time ### Parameters: - keyword: Keyword - followerRange (optional): Follower range, format: min-max     - Example: 10-100 indicates follower range between 100,000 and 1,000,000     - Do not pass this parameter to not limit the follower range - contentTag (optional): Content tag, supports the following formats:     - tag-{id}: First-level tag, e.g., tag-1 (Beauty)     - tag_level_two-{id}: Second-level tag, e.g., tag_level_two-7 (Outfit)     - Refer to the contentTag mapping table in the documentation     - Do not pass this parameter to not limit content tags ### Return: - Kol List (with advanced filtering)  # [示例/Example] keyword = \"美妆\" followerRange = \"10-100\"  # 10万-100万粉丝 contentTag = \"tag-1\"  # 美妆一级标签 contentTag = \"tag_level_two-2\"  # 美妆教程二级标签  # [内容标签映射表/Content Tag Mapping]  ## 一级标签 (First-level tags) - 格式: tag-{id}  | 参数 | 分类 | 参数 | 分类 | 参数 | 分类 | |------|------|------|------|------|------| | tag-1 | 美妆 | tag-6 | 时尚 | tag-11 | 萌宠 | | tag-15 | 测评 | tag-23 | 游戏 | tag-25 | 二次元 | | tag-27 | 旅行 | tag-31 | 汽车 | tag-36 | 生活 | | tag-41 | 音乐 | tag-46 | 舞蹈* | tag-48 | 美食 | | tag-55 | 母婴亲子 | tag-60 | 运动健身 | tag-64 | 科技数码 | | tag-68 | 教育培训 | tag-72 | 颜值达人 | tag-79 | 才艺技能 | | tag-85 | 影视娱乐 | tag-87 | 艺术文化 | tag-91 | 财经投资 | | tag-95 | 三农* | tag-97 | 剧情搞笑 | tag-100 | 情感* | | tag-102 | 园艺* | tag-130 | 随拍* | tag-139 | 房产 | | tag-1001 | 生活家居 | tag-1002 | 媒体号* | | |  *注: 标记*的分类无二级标签  ## 二级标签 (Second-level tags) - 格式: tag_level_two-{id}  ### 美妆 (tag-1) - tag_level_two-2: 美妆教程 - tag_level_two-3: 妆容展示 - tag_level_two-4: 护肤保养 - tag_level_two-5: 美妆测评种草  ### 时尚 (tag-6) - tag_level_two-7: 穿搭 - tag_level_two-8: 街拍 - tag_level_two-10: 造型 - tag_level_two-135: 时尚媒体  ### 萌宠 (tag-11) - tag_level_two-12: 日常宠物 - tag_level_two-13: 特别宠物 - tag_level_two-14: 宠物周边  ### 测评 (tag-15) - tag_level_two-16: 美妆测评 - tag_level_two-17: 3C数码测评 - tag_level_two-18: 汽车测评 - tag_level_two-19: 美食产品测评 - tag_level_two-20: 母婴产品测评 - tag_level_two-21: 综合测评 - tag_level_two-132: 酒店测评  ### 游戏 (tag-23) - tag_level_two-121: 游戏剧情 - tag_level_two-122: 游戏解说 - tag_level_two-123: 游戏资讯 - tag_level_two-124: 游戏其他 - tag_level_two-440: 游戏录屏 - tag_level_two-441: 游戏集锦  ### 二次元 (tag-25) - tag_level_two-125: 二次元真人 - tag_level_two-126: 动画漫画 - tag_level_two-127: 配音声优 - tag_level_two-128: 宅物手办  ### 旅行 (tag-27) - tag_level_two-28: 旅行记录 - tag_level_two-29: 旅行攻略 - tag_level_two-30: 旅行推荐 - tag_level_two-442: 户外生活  ### 汽车 (tag-31) - tag_level_two-32: 汽车测评 - tag_level_two-33: 汽车知识 - tag_level_two-34: 汽车周边  ### 生活 (tag-36) - tag_level_two-37: 生活记录 - tag_level_two-39: 生活小窍门 - tag_level_two-40: 好物推荐 - tag_level_two-118: 健康养生 - tag_level_two-422: 婚恋  ### 音乐 (tag-41) - tag_level_two-42: 歌曲演唱 - tag_level_two-43: 乐器演奏 - tag_level_two-44: 音乐教学 - tag_level_two-45: 音乐其他 - tag_level_two-136: 音乐剪辑  ### 美食 (tag-48) - tag_level_two-49: 美食教程 - tag_level_two-50: 美食探店 - tag_level_two-52: 美食产品测评 - tag_level_two-53: 乡村野食 - tag_level_two-54: 美食其他 - tag_level_two-423: 酒类  ### 母婴亲子 (tag-55) - tag_level_two-56: 育儿科普 - tag_level_two-57: 萌娃日常 - tag_level_two-58: 亲子互动 - tag_level_two-59: 测评种草  ### 运动健身 (tag-60) - tag_level_two-61: 健身 - tag_level_two-63: 极限运动 - tag_level_two-424: 体育资讯 - tag_level_two-443: 冰雪 - tag_level_two-444: 垂钓 - tag_level_two-445: 格斗 - tag_level_two-446: 球类项目 - tag_level_two-447: 综合体育  ### 科技数码 (tag-64) - tag_level_two-65: 3C数码 - tag_level_two-66: 家居电器 - tag_level_two-133: 科技  ### 教育培训 (tag-68) - tag_level_two-69: 考学培训 - tag_level_two-70: 语言教学 - tag_level_two-71: 个人管理 - tag_level_two-425: 职业教育  ### 颜值达人 (tag-72) - tag_level_two-73: 美女 - tag_level_two-74: 帅哥  ### 才艺技能 (tag-79) - tag_level_two-80: 创意才能 - tag_level_two-81: 手工 - tag_level_two-82: 摄影 - tag_level_two-83: 绘画 - tag_level_two-84: 其他才艺  ### 影视娱乐 (tag-85) - tag_level_two-413: 影视解说 - tag_level_two-414: 影视混剪 - tag_level_two-415: 明星资讯 - tag_level_two-416: 综艺解说 - tag_level_two-417: 综艺混剪  ### 艺术文化 (tag-87) - tag_level_two-88: 传统文化 - tag_level_two-89: 人文科普 - tag_level_two-90: 自然科学  ### 财经投资 (tag-91) - tag_level_two-92: 传统金融 - tag_level_two-93: 互联网金融 - tag_level_two-94: 财经知识  ### 剧情搞笑 (tag-97) - tag_level_two-98: 剧情 - tag_level_two-99: 搞笑  ### 生活家居 (tag-1001) - tag_level_two-100101: 硬装 - tag_level_two-100102: 软装 - tag_level_two-100103: 生活技巧 - tag_level_two-100104: 家居氛围  ### 房产 (tag-139) - tag_level_two-140: 其他房产 - tag_level_two-437: 房产知识 - tag_level_two-439: 房产及投资 - tag_level_two-448: 楼盘评测 - tag_level_two-449: 楼市资讯 - tag_level_two-450: 租房  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object follower_range: 粉丝范围(可选)/Follower Range (optional), 例如 10-100 表示10万-100万粉丝
        :param object content_tag: 内容标签(可选)/Content Tag (optional), 例如 tag-1 或 tag_level_two-7
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'follower_range', 'content_tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'follower_range' in params:
            query_params.append(('followerRange', params['follower_range']))  # noqa: E501
        if 'content_tag' in params:
            query_params.append(('contentTag', params['content_tag']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu/search_kol_v2', 'GET',
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
