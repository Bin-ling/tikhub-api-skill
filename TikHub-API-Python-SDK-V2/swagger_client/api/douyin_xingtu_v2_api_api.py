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


class DouyinXingtuV2APIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get(self, o_author_id, **kwargs):  # noqa: E501
        """获取创作者基本信息/Get Author Base Info  # noqa: E501

        # [中文] ### 用途: - 获取创作者基本信息 - 价格：0.001$ / 次 ### 参数: - o_author_id: 创作者ID - platform_source: 平台来源，默认1 - platform_channel: 平台渠道，默认1 - recommend: 是否返回推荐信息，默认True - need_sec_uid: 是否返回sec_uid，默认True - need_linkage_info: 是否返回联动信息，默认True ### 返回: - 创作者基本信息数据  # [English] ### Purpose: - Get creator/author base information - Price: 0.001$ / time ### Parameters: - o_author_id: Creator/author ID - platform_source: Platform source, default 1 - platform_channel: Platform channel, default 1 - recommend: Whether to return recommendation info, default True - need_sec_uid: Whether to return sec_uid, default True - need_linkage_info: Whether to return linkage info, default True ### Return: - Creator base info data  # [示例/Example] o_author_id = \"7589271892177518598\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get(o_author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object o_author_id: 创作者ID/Creator author ID (required)
        :param object platform_source: 平台来源/Platform source
        :param object platform_channel: 平台渠道/Platform channel
        :param object recommend: 是否返回推荐信息/Whether to return recommendation info
        :param object need_sec_uid: 是否返回sec_uid/Whether to return sec_uid
        :param object need_linkage_info: 是否返回联动信息/Whether to return linkage info
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get_with_http_info(o_author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get_with_http_info(o_author_id, **kwargs)  # noqa: E501
            return data

    def get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get_with_http_info(self, o_author_id, **kwargs):  # noqa: E501
        """获取创作者基本信息/Get Author Base Info  # noqa: E501

        # [中文] ### 用途: - 获取创作者基本信息 - 价格：0.001$ / 次 ### 参数: - o_author_id: 创作者ID - platform_source: 平台来源，默认1 - platform_channel: 平台渠道，默认1 - recommend: 是否返回推荐信息，默认True - need_sec_uid: 是否返回sec_uid，默认True - need_linkage_info: 是否返回联动信息，默认True ### 返回: - 创作者基本信息数据  # [English] ### Purpose: - Get creator/author base information - Price: 0.001$ / time ### Parameters: - o_author_id: Creator/author ID - platform_source: Platform source, default 1 - platform_channel: Platform channel, default 1 - recommend: Whether to return recommendation info, default True - need_sec_uid: Whether to return sec_uid, default True - need_linkage_info: Whether to return linkage info, default True ### Return: - Creator base info data  # [示例/Example] o_author_id = \"7589271892177518598\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get_with_http_info(o_author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object o_author_id: 创作者ID/Creator author ID (required)
        :param object platform_source: 平台来源/Platform source
        :param object platform_channel: 平台渠道/Platform channel
        :param object recommend: 是否返回推荐信息/Whether to return recommendation info
        :param object need_sec_uid: 是否返回sec_uid/Whether to return sec_uid
        :param object need_linkage_info: 是否返回联动信息/Whether to return linkage info
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o_author_id', 'platform_source', 'platform_channel', 'recommend', 'need_sec_uid', 'need_linkage_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o_author_id' is set
        if self.api_client.client_side_validation and ('o_author_id' not in params or
                                                       params['o_author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `o_author_id` when calling `get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'o_author_id' in params:
            query_params.append(('o_author_id', params['o_author_id']))  # noqa: E501
        if 'platform_source' in params:
            query_params.append(('platform_source', params['platform_source']))  # noqa: E501
        if 'platform_channel' in params:
            query_params.append(('platform_channel', params['platform_channel']))  # noqa: E501
        if 'recommend' in params:
            query_params.append(('recommend', params['recommend']))  # noqa: E501
        if 'need_sec_uid' in params:
            query_params.append(('need_sec_uid', params['need_sec_uid']))  # noqa: E501
        if 'need_linkage_info' in params:
            query_params.append(('need_linkage_info', params['need_linkage_info']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_author_base_info', 'GET',
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

    def get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get(self, o_author_id, **kwargs):  # noqa: E501
        """获取创作者商业卡片信息/Get Author Business Card Info  # noqa: E501

        # [中文] ### 用途: - 获取创作者商业卡片信息 - 价格：0.001$ / 次 ### 参数: - o_author_id: 创作者ID ### 返回: - 创作者商业卡片信息数据  # [English] ### Purpose: - Get creator/author business card information - Price: 0.001$ / time ### Parameters: - o_author_id: Creator/author ID ### Return: - Creator business card info data  # [示例/Example] o_author_id = \"7589271892177518598\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get(o_author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object o_author_id: 创作者ID/Creator author ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get_with_http_info(o_author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get_with_http_info(o_author_id, **kwargs)  # noqa: E501
            return data

    def get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get_with_http_info(self, o_author_id, **kwargs):  # noqa: E501
        """获取创作者商业卡片信息/Get Author Business Card Info  # noqa: E501

        # [中文] ### 用途: - 获取创作者商业卡片信息 - 价格：0.001$ / 次 ### 参数: - o_author_id: 创作者ID ### 返回: - 创作者商业卡片信息数据  # [English] ### Purpose: - Get creator/author business card information - Price: 0.001$ / time ### Parameters: - o_author_id: Creator/author ID ### Return: - Creator business card info data  # [示例/Example] o_author_id = \"7589271892177518598\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get_with_http_info(o_author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object o_author_id: 创作者ID/Creator author ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o_author_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o_author_id' is set
        if self.api_client.client_side_validation and ('o_author_id' not in params or
                                                       params['o_author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `o_author_id` when calling `get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'o_author_id' in params:
            query_params.append(('o_author_id', params['o_author_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_author_business_card_info', 'GET',
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

    def get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get(self, author_id, **kwargs):  # noqa: E501
        """获取创作者内容热词/Get Author Content Hot Keywords  # noqa: E501

        # [中文] ### 用途: - 获取创作者内容热词 - 价格：0.001$ / 次 ### 参数: - author_id: 创作者ID - keyword_type: 热词类型，默认0 ### 返回: - 创作者内容热词数据  # [English] ### Purpose: - Get creator/author content hot keywords - Price: 0.001$ / time ### Parameters: - author_id: Creator/author ID - keyword_type: Keyword type, default 0 ### Return: - Creator content hot keywords data  # [示例/Example] author_id = \"7589271892177518598\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get(author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object author_id: 创作者ID/Creator author ID (required)
        :param object keyword_type: 热词类型/Keyword type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get_with_http_info(author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get_with_http_info(author_id, **kwargs)  # noqa: E501
            return data

    def get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get_with_http_info(self, author_id, **kwargs):  # noqa: E501
        """获取创作者内容热词/Get Author Content Hot Keywords  # noqa: E501

        # [中文] ### 用途: - 获取创作者内容热词 - 价格：0.001$ / 次 ### 参数: - author_id: 创作者ID - keyword_type: 热词类型，默认0 ### 返回: - 创作者内容热词数据  # [English] ### Purpose: - Get creator/author content hot keywords - Price: 0.001$ / time ### Parameters: - author_id: Creator/author ID - keyword_type: Keyword type, default 0 ### Return: - Creator content hot keywords data  # [示例/Example] author_id = \"7589271892177518598\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get_with_http_info(author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object author_id: 创作者ID/Creator author ID (required)
        :param object keyword_type: 热词类型/Keyword type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['author_id', 'keyword_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'author_id' is set
        if self.api_client.client_side_validation and ('author_id' not in params or
                                                       params['author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `author_id` when calling `get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'author_id' in params:
            query_params.append(('author_id', params['author_id']))  # noqa: E501
        if 'keyword_type' in params:
            query_params.append(('keyword_type', params['keyword_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_author_content_hot_keywords', 'GET',
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

    def get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get(self, author_id, **kwargs):  # noqa: E501
        """获取创作者评论热词/Get Author Hot Comment Tokens  # noqa: E501

        # [中文] ### 用途: - 获取创作者评论热词 - 价格：0.001$ / 次 ### 参数: - author_id: 创作者ID - num: 返回热词数量，默认10 - without_emoji: 是否排除emoji，默认True ### 返回: - 创作者评论热词数据  # [English] ### Purpose: - Get creator/author hot comment tokens/keywords - Price: 0.001$ / time ### Parameters: - author_id: Creator/author ID - num: Number of hot tokens, default 10 - without_emoji: Whether to exclude emoji, default True ### Return: - Creator hot comment tokens data  # [示例/Example] author_id = \"7589271892177518598\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get(author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object author_id: 创作者ID/Creator author ID (required)
        :param object num: 返回热词数量/Number of hot tokens
        :param object without_emoji: 是否排除emoji/Whether to exclude emoji
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get_with_http_info(author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get_with_http_info(author_id, **kwargs)  # noqa: E501
            return data

    def get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get_with_http_info(self, author_id, **kwargs):  # noqa: E501
        """获取创作者评论热词/Get Author Hot Comment Tokens  # noqa: E501

        # [中文] ### 用途: - 获取创作者评论热词 - 价格：0.001$ / 次 ### 参数: - author_id: 创作者ID - num: 返回热词数量，默认10 - without_emoji: 是否排除emoji，默认True ### 返回: - 创作者评论热词数据  # [English] ### Purpose: - Get creator/author hot comment tokens/keywords - Price: 0.001$ / time ### Parameters: - author_id: Creator/author ID - num: Number of hot tokens, default 10 - without_emoji: Whether to exclude emoji, default True ### Return: - Creator hot comment tokens data  # [示例/Example] author_id = \"7589271892177518598\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get_with_http_info(author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object author_id: 创作者ID/Creator author ID (required)
        :param object num: 返回热词数量/Number of hot tokens
        :param object without_emoji: 是否排除emoji/Whether to exclude emoji
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['author_id', 'num', 'without_emoji']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'author_id' is set
        if self.api_client.client_side_validation and ('author_id' not in params or
                                                       params['author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `author_id` when calling `get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'author_id' in params:
            query_params.append(('author_id', params['author_id']))  # noqa: E501
        if 'num' in params:
            query_params.append(('num', params['num']))  # noqa: E501
        if 'without_emoji' in params:
            query_params.append(('without_emoji', params['without_emoji']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_author_hot_comment_tokens', 'GET',
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

    def get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get(self, o_author_id, **kwargs):  # noqa: E501
        """获取创作者位置信息/Get Author Local Info  # noqa: E501

        # [中文] ### 用途: - 获取创作者位置信息 - 价格：0.001$ / 次 ### 参数: - o_author_id: 创作者ID - platform_source: 平台来源，默认1 - platform_channel: 平台渠道，默认1 - time_range: 时间范围(天)，默认30 ### 返回: - 创作者位置信息数据  # [English] ### Purpose: - Get creator/author location information - Price: 0.001$ / time ### Parameters: - o_author_id: Creator/author ID - platform_source: Platform source, default 1 - platform_channel: Platform channel, default 1 - time_range: Time range in days, default 30 ### Return: - Creator location info data  # [示例/Example] o_author_id = \"7146074596666507300\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get(o_author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object o_author_id: 创作者ID/Creator author ID (required)
        :param object platform_source: 平台来源/Platform source
        :param object platform_channel: 平台渠道/Platform channel
        :param object time_range: 时间范围(天)/Time range in days
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get_with_http_info(o_author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get_with_http_info(o_author_id, **kwargs)  # noqa: E501
            return data

    def get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get_with_http_info(self, o_author_id, **kwargs):  # noqa: E501
        """获取创作者位置信息/Get Author Local Info  # noqa: E501

        # [中文] ### 用途: - 获取创作者位置信息 - 价格：0.001$ / 次 ### 参数: - o_author_id: 创作者ID - platform_source: 平台来源，默认1 - platform_channel: 平台渠道，默认1 - time_range: 时间范围(天)，默认30 ### 返回: - 创作者位置信息数据  # [English] ### Purpose: - Get creator/author location information - Price: 0.001$ / time ### Parameters: - o_author_id: Creator/author ID - platform_source: Platform source, default 1 - platform_channel: Platform channel, default 1 - time_range: Time range in days, default 30 ### Return: - Creator location info data  # [示例/Example] o_author_id = \"7146074596666507300\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get_with_http_info(o_author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object o_author_id: 创作者ID/Creator author ID (required)
        :param object platform_source: 平台来源/Platform source
        :param object platform_channel: 平台渠道/Platform channel
        :param object time_range: 时间范围(天)/Time range in days
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o_author_id', 'platform_source', 'platform_channel', 'time_range']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o_author_id' is set
        if self.api_client.client_side_validation and ('o_author_id' not in params or
                                                       params['o_author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `o_author_id` when calling `get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'o_author_id' in params:
            query_params.append(('o_author_id', params['o_author_id']))  # noqa: E501
        if 'platform_source' in params:
            query_params.append(('platform_source', params['platform_source']))  # noqa: E501
        if 'platform_channel' in params:
            query_params.append(('platform_channel', params['platform_channel']))  # noqa: E501
        if 'time_range' in params:
            query_params.append(('time_range', params['time_range']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_author_local_info', 'GET',
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

    def get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get(self, **kwargs):  # noqa: E501
        """获取达人广场筛选字段/Get Author Market Fields  # noqa: E501

        # [中文] ### 用途: - 获取达人广场所有筛选字段选项 - 价格：0.001$ / 次 ### 参数: - market_scene: 市场场景，1=默认场景 ### 返回: - 达人广场筛选字段数据  # [English] ### Purpose: - Get all filter field options for the creator marketplace - Price: 0.001$ / time ### Parameters: - market_scene: Market scene, 1=default ### Return: - Creator marketplace filter fields data  # [示例/Example] market_scene = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object market_scene: 市场场景，1=默认场景/Market scene, 1=default
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取达人广场筛选字段/Get Author Market Fields  # noqa: E501

        # [中文] ### 用途: - 获取达人广场所有筛选字段选项 - 价格：0.001$ / 次 ### 参数: - market_scene: 市场场景，1=默认场景 ### 返回: - 达人广场筛选字段数据  # [English] ### Purpose: - Get all filter field options for the creator marketplace - Price: 0.001$ / time ### Parameters: - market_scene: Market scene, 1=default ### Return: - Creator marketplace filter fields data  # [示例/Example] market_scene = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object market_scene: 市场场景，1=默认场景/Market scene, 1=default
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['market_scene']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'market_scene' in params:
            query_params.append(('market_scene', params['market_scene']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_author_market_fields', 'GET',
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

    def get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get(self, o_author_id, **kwargs):  # noqa: E501
        """获取创作者视频列表/Get Author Show Items  # noqa: E501

        # [中文] ### 用途: - 获取创作者视频列表 - 价格：0.001$ / 次 ### 参数: - o_author_id: 创作者ID - platform_source: 平台来源，默认1 - platform_channel: 平台渠道，默认1 - limit: 返回数量，默认10 - only_assign: 仅看指派视频（只针对星图视频生效），默认False - flow_type: 流量类型，默认0 ### 返回: - 创作者视频列表数据  # [English] ### Purpose: - Get creator/author video list - Price: 0.001$ / time ### Parameters: - o_author_id: Creator/author ID - platform_source: Platform source, default 1 - platform_channel: Platform channel, default 1 - limit: Result limit, default 10 - only_assign: Only show assigned videos (only for XingTu videos), default False - flow_type: Flow type, default 0 ### Return: - Creator video list data  # [示例/Example] o_author_id = \"7589271892177518598\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get(o_author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object o_author_id: 创作者ID/Creator author ID (required)
        :param object platform_source: 平台来源/Platform source
        :param object platform_channel: 平台渠道/Platform channel
        :param object limit: 返回数量/Result limit
        :param object only_assign: 仅看指派视频/Only show assigned videos
        :param object flow_type: 流量类型/Flow type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get_with_http_info(o_author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get_with_http_info(o_author_id, **kwargs)  # noqa: E501
            return data

    def get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get_with_http_info(self, o_author_id, **kwargs):  # noqa: E501
        """获取创作者视频列表/Get Author Show Items  # noqa: E501

        # [中文] ### 用途: - 获取创作者视频列表 - 价格：0.001$ / 次 ### 参数: - o_author_id: 创作者ID - platform_source: 平台来源，默认1 - platform_channel: 平台渠道，默认1 - limit: 返回数量，默认10 - only_assign: 仅看指派视频（只针对星图视频生效），默认False - flow_type: 流量类型，默认0 ### 返回: - 创作者视频列表数据  # [English] ### Purpose: - Get creator/author video list - Price: 0.001$ / time ### Parameters: - o_author_id: Creator/author ID - platform_source: Platform source, default 1 - platform_channel: Platform channel, default 1 - limit: Result limit, default 10 - only_assign: Only show assigned videos (only for XingTu videos), default False - flow_type: Flow type, default 0 ### Return: - Creator video list data  # [示例/Example] o_author_id = \"7589271892177518598\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get_with_http_info(o_author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object o_author_id: 创作者ID/Creator author ID (required)
        :param object platform_source: 平台来源/Platform source
        :param object platform_channel: 平台渠道/Platform channel
        :param object limit: 返回数量/Result limit
        :param object only_assign: 仅看指派视频/Only show assigned videos
        :param object flow_type: 流量类型/Flow type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o_author_id', 'platform_source', 'platform_channel', 'limit', 'only_assign', 'flow_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o_author_id' is set
        if self.api_client.client_side_validation and ('o_author_id' not in params or
                                                       params['o_author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `o_author_id` when calling `get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'o_author_id' in params:
            query_params.append(('o_author_id', params['o_author_id']))  # noqa: E501
        if 'platform_source' in params:
            query_params.append(('platform_source', params['platform_source']))  # noqa: E501
        if 'platform_channel' in params:
            query_params.append(('platform_channel', params['platform_channel']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'only_assign' in params:
            query_params.append(('only_assign', params['only_assign']))  # noqa: E501
        if 'flow_type' in params:
            query_params.append(('flow_type', params['flow_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_author_show_items', 'GET',
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

    def get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get(self, o_author_id, **kwargs):  # noqa: E501
        """获取创作者传播价值/Get Author Spread Info  # noqa: E501

        # [中文] ### 用途: - 获取创作者商业能力的传播价值信息 - 价格：0.001$ / 次 ### 参数: - o_author_id: 创作者ID - platform_source: 平台来源，默认1 - platform_channel: 平台渠道，默认1 - type: 视频类型，1=个人视频 - flow_type: 流量类型，默认0 - only_assign: 仅看指派视频，默认False - range: 时间范围，2=近30天，3=近90天 ### 返回: - 创作者传播价值数据  # [English] ### Purpose: - Get creator/author spread value information (commercial capability) - Price: 0.001$ / time ### Parameters: - o_author_id: Creator/author ID - platform_source: Platform source, default 1 - platform_channel: Platform channel, default 1 - type: Video type, 1=personal video - flow_type: Flow type, default 0 - only_assign: Only assigned videos, default False - range: Time range, 2=last 30 days, 3=last 90 days ### Return: - Creator spread value data  # [示例/Example] o_author_id = \"7589271892177518598\" range = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get(o_author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object o_author_id: 创作者ID/Creator author ID (required)
        :param object platform_source: 平台来源/Platform source
        :param object platform_channel: 平台渠道/Platform channel
        :param object type: 视频类型，1=个人视频/Video type, 1=personal video
        :param object flow_type: 流量类型/Flow type
        :param object only_assign: 仅看指派视频/Only assigned videos
        :param object range: 时间范围，2=近30天，3=近90天/Time range, 2=last 30 days, 3=last 90 days
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get_with_http_info(o_author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get_with_http_info(o_author_id, **kwargs)  # noqa: E501
            return data

    def get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get_with_http_info(self, o_author_id, **kwargs):  # noqa: E501
        """获取创作者传播价值/Get Author Spread Info  # noqa: E501

        # [中文] ### 用途: - 获取创作者商业能力的传播价值信息 - 价格：0.001$ / 次 ### 参数: - o_author_id: 创作者ID - platform_source: 平台来源，默认1 - platform_channel: 平台渠道，默认1 - type: 视频类型，1=个人视频 - flow_type: 流量类型，默认0 - only_assign: 仅看指派视频，默认False - range: 时间范围，2=近30天，3=近90天 ### 返回: - 创作者传播价值数据  # [English] ### Purpose: - Get creator/author spread value information (commercial capability) - Price: 0.001$ / time ### Parameters: - o_author_id: Creator/author ID - platform_source: Platform source, default 1 - platform_channel: Platform channel, default 1 - type: Video type, 1=personal video - flow_type: Flow type, default 0 - only_assign: Only assigned videos, default False - range: Time range, 2=last 30 days, 3=last 90 days ### Return: - Creator spread value data  # [示例/Example] o_author_id = \"7589271892177518598\" range = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get_with_http_info(o_author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object o_author_id: 创作者ID/Creator author ID (required)
        :param object platform_source: 平台来源/Platform source
        :param object platform_channel: 平台渠道/Platform channel
        :param object type: 视频类型，1=个人视频/Video type, 1=personal video
        :param object flow_type: 流量类型/Flow type
        :param object only_assign: 仅看指派视频/Only assigned videos
        :param object range: 时间范围，2=近30天，3=近90天/Time range, 2=last 30 days, 3=last 90 days
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o_author_id', 'platform_source', 'platform_channel', 'type', 'flow_type', 'only_assign', 'range']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o_author_id' is set
        if self.api_client.client_side_validation and ('o_author_id' not in params or
                                                       params['o_author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `o_author_id` when calling `get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'o_author_id' in params:
            query_params.append(('o_author_id', params['o_author_id']))  # noqa: E501
        if 'platform_source' in params:
            query_params.append(('platform_source', params['platform_source']))  # noqa: E501
        if 'platform_channel' in params:
            query_params.append(('platform_channel', params['platform_channel']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'flow_type' in params:
            query_params.append(('flow_type', params['flow_type']))  # noqa: E501
        if 'only_assign' in params:
            query_params.append(('only_assign', params['only_assign']))  # noqa: E501
        if 'range' in params:
            query_params.append(('range', params['range']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_author_spread_info', 'GET',
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

    def get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get(self, **kwargs):  # noqa: E501
        """获取内容趋势指南/Get Content Trend Guide  # noqa: E501

        # [中文] ### 用途: - 获取内容趋势指南数据（CDN静态JSON，无需Cookie） - 价格：0.001$ / 次 ### 返回: - 内容趋势指南数据  # [English] ### Purpose: - Get content trend guide data (CDN static JSON, no cookie needed) - Price: 0.001$ / time ### Return: - Content trend guide data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取内容趋势指南/Get Content Trend Guide  # noqa: E501

        # [中文] ### 用途: - 获取内容趋势指南数据（CDN静态JSON，无需Cookie） - 价格：0.001$ / 次 ### 返回: - 内容趋势指南数据  # [English] ### Purpose: - Get content trend guide data (CDN static JSON, no cookie needed) - Price: 0.001$ / time ### Return: - Content trend guide data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get_with_http_info(async_req=True)
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
                    " to method get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get" % key
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
            '/api/v1/douyin/xingtu_v2/get_content_trend_guide', 'GET',
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

    def get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get(self, **kwargs):  # noqa: E501
        """搜索MCN机构列表/Get Demander MCN List  # noqa: E501

        # [中文] ### 用途: - 搜索MCN机构列表 - 价格：0.001$ / 次 ### 参数: - mcn_name: MCN机构名称，支持模糊搜索 - page: 页码，默认1 - limit: 每页数量，默认20 - order_by: 排序方式，`platform_scores`=平台评分 ### 返回: - MCN机构列表数据  # [English] ### Purpose: - Search MCN organization list - Price: 0.001$ / time ### Parameters: - mcn_name: MCN name, supports fuzzy search - page: Page number, default 1 - limit: Page size, default 20 - order_by: Sort by, `platform_scores`=platform scores ### Return: - MCN organization list data  # [示例/Example] mcn_name = \"\" page = 1 limit = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mcn_name: MCN机构名称，支持模糊搜索/MCN name, supports fuzzy search
        :param object page: 页码/Page number
        :param object limit: 每页数量/Page size
        :param object order_by: 排序方式/Sort by
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """搜索MCN机构列表/Get Demander MCN List  # noqa: E501

        # [中文] ### 用途: - 搜索MCN机构列表 - 价格：0.001$ / 次 ### 参数: - mcn_name: MCN机构名称，支持模糊搜索 - page: 页码，默认1 - limit: 每页数量，默认20 - order_by: 排序方式，`platform_scores`=平台评分 ### 返回: - MCN机构列表数据  # [English] ### Purpose: - Search MCN organization list - Price: 0.001$ / time ### Parameters: - mcn_name: MCN name, supports fuzzy search - page: Page number, default 1 - limit: Page size, default 20 - order_by: Sort by, `platform_scores`=platform scores ### Return: - MCN organization list data  # [示例/Example] mcn_name = \"\" page = 1 limit = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mcn_name: MCN机构名称，支持模糊搜索/MCN name, supports fuzzy search
        :param object page: 页码/Page number
        :param object limit: 每页数量/Page size
        :param object order_by: 排序方式/Sort by
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mcn_name', 'page', 'limit', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mcn_name' in params:
            query_params.append(('mcn_name', params['mcn_name']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_demander_mcn_list', 'GET',
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

    def get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get(self, **kwargs):  # noqa: E501
        """获取优秀行业分类列表/Get Excellent Case Category List  # noqa: E501

        # [中文] ### 用途: - 获取连接用户漏斗中的优秀行业分类列表 - 价格：0.001$ / 次 ### 参数: - platform_source: 平台来源，默认1 ### 返回: - 优秀行业分类列表数据  # [English] ### Purpose: - Get the excellent case category list in the user connection funnel - Price: 0.001$ / time ### Parameters: - platform_source: Platform source, default 1 ### Return: - Excellent case category list data  # [示例/Example] platform_source = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object platform_source: 平台来源/Platform source
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取优秀行业分类列表/Get Excellent Case Category List  # noqa: E501

        # [中文] ### 用途: - 获取连接用户漏斗中的优秀行业分类列表 - 价格：0.001$ / 次 ### 参数: - platform_source: 平台来源，默认1 ### 返回: - 优秀行业分类列表数据  # [English] ### Purpose: - Get the excellent case category list in the user connection funnel - Price: 0.001$ / time ### Parameters: - platform_source: Platform source, default 1 ### Return: - Excellent case category list data  # [示例/Example] platform_source = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object platform_source: 平台来源/Platform source
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform_source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'platform_source' in params:
            query_params.append(('platform_source', params['platform_source']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_excellent_case_category_list', 'GET',
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

    def get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get(self, id, **kwargs):  # noqa: E501
        """获取星图IP活动详情/Get IP Activity Detail  # noqa: E501

        # [中文] ### 用途: - 获取星图IP日历活动详情 - 价格：0.001$ / 次 ### 参数: - id: 活动ID，从`get_ip_activity_list`获取 ### 返回: - IP活动详情数据  # [English] ### Purpose: - Get XingTu IP calendar activity detail - Price: 0.001$ / time ### Parameters: - id: Activity ID, from `get_ip_activity_list` ### Return: - IP activity detail data  # [示例/Example] id = 347  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 活动ID，从get_ip_activity_list获取/Activity ID from get_ip_activity_list (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """获取星图IP活动详情/Get IP Activity Detail  # noqa: E501

        # [中文] ### 用途: - 获取星图IP日历活动详情 - 价格：0.001$ / 次 ### 参数: - id: 活动ID，从`get_ip_activity_list`获取 ### 返回: - IP活动详情数据  # [English] ### Purpose: - Get XingTu IP calendar activity detail - Price: 0.001$ / time ### Parameters: - id: Activity ID, from `get_ip_activity_list` ### Return: - IP activity detail data  # [示例/Example] id = 347  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 活动ID，从get_ip_activity_list获取/Activity ID from get_ip_activity_list (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_ip_activity_detail', 'GET',
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

    def get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get(self, **kwargs):  # noqa: E501
        """获取星图IP日历行业列表/Get IP Activity Industry List  # noqa: E501

        # [中文] ### 用途: - 获取星图IP日历的行业列表 - 价格：0.001$ / 次 ### 返回: - 行业列表数据  # [English] ### Purpose: - Get the industry list for XingTu IP calendar - Price: 0.001$ / time ### Return: - Industry list data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取星图IP日历行业列表/Get IP Activity Industry List  # noqa: E501

        # [中文] ### 用途: - 获取星图IP日历的行业列表 - 价格：0.001$ / 次 ### 返回: - 行业列表数据  # [English] ### Purpose: - Get the industry list for XingTu IP calendar - Price: 0.001$ / time ### Return: - Industry list data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get_with_http_info(async_req=True)
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
                    " to method get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get" % key
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
            '/api/v1/douyin/xingtu_v2/get_ip_activity_industry_list', 'GET',
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

    def get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post(self, **kwargs):  # noqa: E501
        """获取星图IP日历活动列表/Get IP Activity List  # noqa: E501

        # [中文] ### 用途: - 获取星图IP日历活动列表 - 价格：0.001$ / 次 ### 参数: - query_start_time: 查询开始时间戳，如`1767196800` - query_end_time: 查询结束时间戳，如`1774972799` - industry_id_list (可选): 行业ID列表，从`get_ip_activity_industry_list`获取     - 例：`[\"1930\"]`=美妆, `[\"1901\"]`=3C及电器, `[\"1903\"]`=食品饮料 - category_list (可选): IP类型列表     - 1=星图大事件, 2=电商节点, 3=情绪节点, 4=创意营销, 5=行业活动 - status_list (可选): IP状态列表     - 40=筹备中, 50=招商中, 30=资源上线, 20=已结束 ### 返回: - IP日历活动列表数据  # [English] ### Purpose: - Get XingTu IP calendar activity list - Price: 0.001$ / time ### Parameters: - query_start_time: Query start timestamp, e.g. `1767196800` - query_end_time: Query end timestamp, e.g. `1774972799` - industry_id_list (optional): Industry ID list from `get_ip_activity_industry_list`     - Example: `[\"1930\"]`=Beauty, `[\"1901\"]`=3C & Electronics, `[\"1903\"]`=Food & Beverage - category_list (optional): IP category list     - 1=XingTu Big Event, 2=E-commerce Node, 3=Emotion Node, 4=Creative Marketing, 5=Industry Activity - status_list (optional): IP status list     - 40=Preparing, 50=Recruiting, 30=Resources Online, 20=Ended ### Return: - IP calendar activity list data  # [示例/Example] query_start_time = \"1767196800\" query_end_time = \"1774972799\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取星图IP日历活动列表/Get IP Activity List  # noqa: E501

        # [中文] ### 用途: - 获取星图IP日历活动列表 - 价格：0.001$ / 次 ### 参数: - query_start_time: 查询开始时间戳，如`1767196800` - query_end_time: 查询结束时间戳，如`1774972799` - industry_id_list (可选): 行业ID列表，从`get_ip_activity_industry_list`获取     - 例：`[\"1930\"]`=美妆, `[\"1901\"]`=3C及电器, `[\"1903\"]`=食品饮料 - category_list (可选): IP类型列表     - 1=星图大事件, 2=电商节点, 3=情绪节点, 4=创意营销, 5=行业活动 - status_list (可选): IP状态列表     - 40=筹备中, 50=招商中, 30=资源上线, 20=已结束 ### 返回: - IP日历活动列表数据  # [English] ### Purpose: - Get XingTu IP calendar activity list - Price: 0.001$ / time ### Parameters: - query_start_time: Query start timestamp, e.g. `1767196800` - query_end_time: Query end timestamp, e.g. `1774972799` - industry_id_list (optional): Industry ID list from `get_ip_activity_industry_list`     - Example: `[\"1930\"]`=Beauty, `[\"1901\"]`=3C & Electronics, `[\"1903\"]`=Food & Beverage - category_list (optional): IP category list     - 1=XingTu Big Event, 2=E-commerce Node, 3=Emotion Node, 4=Creative Marketing, 5=Industry Activity - status_list (optional): IP status list     - 40=Preparing, 50=Recruiting, 30=Resources Online, 20=Ended ### Return: - IP calendar activity list data  # [示例/Example] query_start_time = \"1767196800\" query_end_time = \"1774972799\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post_with_http_info(async_req=True)
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
                    " to method get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post" % key
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
            '/api/v1/douyin/xingtu_v2/get_ip_activity_list', 'POST',
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

    def get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post(self, **kwargs):  # noqa: E501
        """获取短剧演员热榜分类/Get Playlet Actor Rank Catalog  # noqa: E501

        # [中文] ### 用途: - 获取短剧演员热榜分类列表 - 价格：0.001$ / 次 ### 返回: - 短剧演员热榜分类数据  # [English] ### Purpose: - Get XingTu playlet actor ranking catalog - Price: 0.001$ / time ### Return: - Playlet actor ranking catalog data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取短剧演员热榜分类/Get Playlet Actor Rank Catalog  # noqa: E501

        # [中文] ### 用途: - 获取短剧演员热榜分类列表 - 价格：0.001$ / 次 ### 返回: - 短剧演员热榜分类数据  # [English] ### Purpose: - Get XingTu playlet actor ranking catalog - Price: 0.001$ / time ### Return: - Playlet actor ranking catalog data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post_with_http_info(async_req=True)
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
                    " to method get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post" % key
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
            '/api/v1/douyin/xingtu_v2/get_playlet_actor_rank_catalog', 'POST',
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

    def get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get(self, **kwargs):  # noqa: E501
        """获取短剧演员热榜/Get Playlet Actor Rank List  # noqa: E501

        # [中文] ### 用途: - 获取短剧演员热榜数据 - 价格：0.001$ / 次 ### 参数: - category: 分类，默认`playlet_actor_list` - name: 榜单名称，`playlet_actor_composite_list`=综合榜 - qualifier: 达人类型，空字符串=不限 - period: 统计周期，7=周榜，30=月榜 - date: 统计日期，格式YYYYMMDD - limit: 返回数量，默认100 ### 返回: - 短剧演员热榜数据  # [English] ### Purpose: - Get XingTu playlet actor ranking list data - Price: 0.001$ / time ### Parameters: - category: Category, default `playlet_actor_list` - name: Ranking name, `playlet_actor_composite_list`=composite list - qualifier: Actor type, empty=all - period: 7=weekly, 30=monthly - date: Date, format YYYYMMDD - limit: Result limit, default 100 ### Return: - Playlet actor ranking data  # [示例/Example] category = \"playlet_actor_list\" name = \"playlet_actor_composite_list\" period = 30 date = \"20251130\" limit = 100  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category: 分类/Category
        :param object name: 榜单名称/Ranking name
        :param object qualifier: 达人类型，空字符串=不限/Actor type, empty=all
        :param object period: 统计周期，7=周榜，30=月榜/Period, 7=weekly, 30=monthly
        :param object _date: 统计日期，格式YYYYMMDD/Date, format YYYYMMDD
        :param object limit: 返回数量/Result limit
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取短剧演员热榜/Get Playlet Actor Rank List  # noqa: E501

        # [中文] ### 用途: - 获取短剧演员热榜数据 - 价格：0.001$ / 次 ### 参数: - category: 分类，默认`playlet_actor_list` - name: 榜单名称，`playlet_actor_composite_list`=综合榜 - qualifier: 达人类型，空字符串=不限 - period: 统计周期，7=周榜，30=月榜 - date: 统计日期，格式YYYYMMDD - limit: 返回数量，默认100 ### 返回: - 短剧演员热榜数据  # [English] ### Purpose: - Get XingTu playlet actor ranking list data - Price: 0.001$ / time ### Parameters: - category: Category, default `playlet_actor_list` - name: Ranking name, `playlet_actor_composite_list`=composite list - qualifier: Actor type, empty=all - period: 7=weekly, 30=monthly - date: Date, format YYYYMMDD - limit: Result limit, default 100 ### Return: - Playlet actor ranking data  # [示例/Example] category = \"playlet_actor_list\" name = \"playlet_actor_composite_list\" period = 30 date = \"20251130\" limit = 100  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category: 分类/Category
        :param object name: 榜单名称/Ranking name
        :param object qualifier: 达人类型，空字符串=不限/Actor type, empty=all
        :param object period: 统计周期，7=周榜，30=月榜/Period, 7=weekly, 30=monthly
        :param object _date: 统计日期，格式YYYYMMDD/Date, format YYYYMMDD
        :param object limit: 返回数量/Result limit
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category', 'name', 'qualifier', 'period', '_date', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category' in params:
            query_params.append(('category', params['category']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'qualifier' in params:
            query_params.append(('qualifier', params['qualifier']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if '_date' in params:
            query_params.append(('date', params['_date']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_playlet_actor_rank_list', 'GET',
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

    def get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get(self, **kwargs):  # noqa: E501
        """获取星图热榜分类/Get Ranking List Catalog  # noqa: E501

        # [中文] ### 用途: - 获取星图热榜分类列表，返回qualifier_id等分类信息 - 价格：0.001$ / 次 ### 参数: - codes: 分类代码，默认为空字符串 - biz_scene: 业务场景     - `douyin_flow_split_video_author_ranks`: 短视频达人热榜     - `douyin_flow_split_live_author_ranks`: 直播达人热榜 ### 返回: - 热榜分类数据  # [English] ### Purpose: - Get XingTu hot ranking list catalog, returns qualifier_id and other category information - Price: 0.001$ / time ### Parameters: - codes: Classification codes, default is empty string - biz_scene: Business scene     - `douyin_flow_split_video_author_ranks`: Video creator ranking     - `douyin_flow_split_live_author_ranks`: Live streamer ranking ### Return: - Hot ranking catalog data  # [示例/Example] codes = \"\" biz_scene = \"douyin_flow_split_video_author_ranks\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object codes: 分类代码，默认为空字符串/Classification codes, default is empty string
        :param object biz_scene: 业务场景/Business scene
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取星图热榜分类/Get Ranking List Catalog  # noqa: E501

        # [中文] ### 用途: - 获取星图热榜分类列表，返回qualifier_id等分类信息 - 价格：0.001$ / 次 ### 参数: - codes: 分类代码，默认为空字符串 - biz_scene: 业务场景     - `douyin_flow_split_video_author_ranks`: 短视频达人热榜     - `douyin_flow_split_live_author_ranks`: 直播达人热榜 ### 返回: - 热榜分类数据  # [English] ### Purpose: - Get XingTu hot ranking list catalog, returns qualifier_id and other category information - Price: 0.001$ / time ### Parameters: - codes: Classification codes, default is empty string - biz_scene: Business scene     - `douyin_flow_split_video_author_ranks`: Video creator ranking     - `douyin_flow_split_live_author_ranks`: Live streamer ranking ### Return: - Hot ranking catalog data  # [示例/Example] codes = \"\" biz_scene = \"douyin_flow_split_video_author_ranks\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object codes: 分类代码，默认为空字符串/Classification codes, default is empty string
        :param object biz_scene: 业务场景/Business scene
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['codes', 'biz_scene']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'codes' in params:
            query_params.append(('codes', params['codes']))  # noqa: E501
        if 'biz_scene' in params:
            query_params.append(('biz_scene', params['biz_scene']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_ranking_list_catalog', 'GET',
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

    def get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get(self, **kwargs):  # noqa: E501
        """获取星图达人商业榜数据/Get Ranking List Data  # noqa: E501

        # [中文] ### 用途: - 获取星图达人商业榜数据 - qualifier可以从`get_ranking_list_catalog`接口获取 - 价格：0.001$ / 次 ### 参数: - code: 榜单类型代码     - 短视频-达人商业榜: 1=品牌优选榜, 2=A3种草榜, 3=看后搜榜, 4=带货榜, 5=投流榜, 6=高潜榜     - 短视频-达人内容榜: 17=涨粉黑马榜, 18=头部必选榜     - 直播达人榜-主播类型: 23=游戏主播, 30=其他主播, 37=带货主播 (version=base)     - 直播达人榜-榜单类型: 23=游戏行业品牌优选榜, 24=非游戏行业品牌优选榜, 25=组件点击榜, 26=下载转化榜, 27=线索收集榜, 28=投流榜, 29=高潜榜 - qualifier: 榜单分类ID，从`get_ranking_list_catalog`获取 - version: 版本，`flow_split`=短视频榜单默认，`base`=直播榜单常用 - period: 统计周期，7=周榜，30=月榜 - date: 统计日期，格式YYYYMMDD - limit: 返回数量，默认100 ### 返回: - 达人商业榜数据  # [English] ### Purpose: - Get XingTu creator business ranking list data - qualifier can be obtained from `get_ranking_list_catalog` API - Price: 0.001$ / time ### Parameters: - code: Ranking type code     - Video business ranking: 1=Brand Premium, 2=A3 Seeding, 3=Search After Watch, 4=E-commerce, 5=Ad Flow, 6=High Potential     - Video content ranking: 17=Follower Growth Dark Horse, 18=Top Must-Pick     - Live streamer type: 23=Game Streamer, 30=Other Streamer, 37=E-commerce Streamer (version=base)     - Live ranking type: 23=Game Brand Premium, 24=Non-game Brand Premium, 25=Component Click, 26=Download Conversion, 27=Lead Collection, 28=Ad Flow, 29=High Potential - qualifier: Category qualifier_id from `get_ranking_list_catalog` - version: `flow_split`=default for video rankings, `base`=commonly used for live rankings - period: 7=weekly, 30=monthly - date: Date, format YYYYMMDD - limit: Result limit, default 100 ### Return: - Creator business ranking data  # [示例/Example] code = 1 qualifier = \"1901\" version = \"flow_split\" period = 30 date = \"20260131\" limit = 100  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code: 榜单类型代码/Ranking type code
        :param object qualifier: 榜单分类ID，从get_ranking_list_catalog获取/Category qualifier_id
        :param object version: 版本/Version
        :param object period: 统计周期，7=周榜，30=月榜/Period, 7=weekly, 30=monthly
        :param object _date: 统计日期，格式YYYYMMDD/Date, format YYYYMMDD
        :param object limit: 返回数量/Result limit
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取星图达人商业榜数据/Get Ranking List Data  # noqa: E501

        # [中文] ### 用途: - 获取星图达人商业榜数据 - qualifier可以从`get_ranking_list_catalog`接口获取 - 价格：0.001$ / 次 ### 参数: - code: 榜单类型代码     - 短视频-达人商业榜: 1=品牌优选榜, 2=A3种草榜, 3=看后搜榜, 4=带货榜, 5=投流榜, 6=高潜榜     - 短视频-达人内容榜: 17=涨粉黑马榜, 18=头部必选榜     - 直播达人榜-主播类型: 23=游戏主播, 30=其他主播, 37=带货主播 (version=base)     - 直播达人榜-榜单类型: 23=游戏行业品牌优选榜, 24=非游戏行业品牌优选榜, 25=组件点击榜, 26=下载转化榜, 27=线索收集榜, 28=投流榜, 29=高潜榜 - qualifier: 榜单分类ID，从`get_ranking_list_catalog`获取 - version: 版本，`flow_split`=短视频榜单默认，`base`=直播榜单常用 - period: 统计周期，7=周榜，30=月榜 - date: 统计日期，格式YYYYMMDD - limit: 返回数量，默认100 ### 返回: - 达人商业榜数据  # [English] ### Purpose: - Get XingTu creator business ranking list data - qualifier can be obtained from `get_ranking_list_catalog` API - Price: 0.001$ / time ### Parameters: - code: Ranking type code     - Video business ranking: 1=Brand Premium, 2=A3 Seeding, 3=Search After Watch, 4=E-commerce, 5=Ad Flow, 6=High Potential     - Video content ranking: 17=Follower Growth Dark Horse, 18=Top Must-Pick     - Live streamer type: 23=Game Streamer, 30=Other Streamer, 37=E-commerce Streamer (version=base)     - Live ranking type: 23=Game Brand Premium, 24=Non-game Brand Premium, 25=Component Click, 26=Download Conversion, 27=Lead Collection, 28=Ad Flow, 29=High Potential - qualifier: Category qualifier_id from `get_ranking_list_catalog` - version: `flow_split`=default for video rankings, `base`=commonly used for live rankings - period: 7=weekly, 30=monthly - date: Date, format YYYYMMDD - limit: Result limit, default 100 ### Return: - Creator business ranking data  # [示例/Example] code = 1 qualifier = \"1901\" version = \"flow_split\" period = 30 date = \"20260131\" limit = 100  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code: 榜单类型代码/Ranking type code
        :param object qualifier: 榜单分类ID，从get_ranking_list_catalog获取/Category qualifier_id
        :param object version: 版本/Version
        :param object period: 统计周期，7=周榜，30=月榜/Period, 7=weekly, 30=monthly
        :param object _date: 统计日期，格式YYYYMMDD/Date, format YYYYMMDD
        :param object limit: 返回数量/Result limit
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'qualifier', 'version', 'period', '_date', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'qualifier' in params:
            query_params.append(('qualifier', params['qualifier']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if '_date' in params:
            query_params.append(('date', params['_date']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_ranking_list_data', 'GET',
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

    def get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post(self, **kwargs):  # noqa: E501
        """获取相似创作者推荐/Get Recommend Similar Star Authors  # noqa: E501

        # [中文] ### 用途: - 获取相似创作者推荐 - 价格：0.001$ / 次 ### 参数: - author_ids: 创作者ID列表 - similar_type: 相似类型     - `comprehension`: 综合相似     - `content`: 内容相似     - `audience`: 用户相似     - `commercial`: 商业能力相似 - page: 页码，默认1 - limit: 每页数量，默认12 ### 返回: - 相似创作者推荐数据  # [English] ### Purpose: - Get similar creator recommendation - Price: 0.001$ / time ### Parameters: - author_ids: List of creator/author IDs - similar_type: Similarity type     - `comprehension`: Comprehensive similarity     - `content`: Content similarity     - `audience`: Audience similarity     - `commercial`: Commercial capability similarity - page: Page number, default 1 - limit: Page size, default 12 ### Return: - Similar creator recommendation data  # [示例/Example] author_ids = [\"7589271892177518598\"] similar_type = \"content\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取相似创作者推荐/Get Recommend Similar Star Authors  # noqa: E501

        # [中文] ### 用途: - 获取相似创作者推荐 - 价格：0.001$ / 次 ### 参数: - author_ids: 创作者ID列表 - similar_type: 相似类型     - `comprehension`: 综合相似     - `content`: 内容相似     - `audience`: 用户相似     - `commercial`: 商业能力相似 - page: 页码，默认1 - limit: 每页数量，默认12 ### 返回: - 相似创作者推荐数据  # [English] ### Purpose: - Get similar creator recommendation - Price: 0.001$ / time ### Parameters: - author_ids: List of creator/author IDs - similar_type: Similarity type     - `comprehension`: Comprehensive similarity     - `content`: Content similarity     - `audience`: Audience similarity     - `commercial`: Commercial capability similarity - page: Page number, default 1 - limit: Page size, default 12 ### Return: - Similar creator recommendation data  # [示例/Example] author_ids = [\"7589271892177518598\"] similar_type = \"content\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post_with_http_info(async_req=True)
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
                    " to method get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post" % key
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
            '/api/v1/douyin/xingtu_v2/get_recommend_for_star_authors', 'POST',
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

    def get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get(self, resource_id, **kwargs):  # noqa: E501
        """获取营销活动案例/Get Resource List  # noqa: E501

        # [中文] ### 用途: - 获取营销活动案例列表 - 价格：0.001$ / 次 ### 参数: - resource_id: 资源ID ### 返回: - 营销活动案例数据  # [English] ### Purpose: - Get marketing activity resource list - Price: 0.001$ / time ### Parameters: - resource_id: Resource ID ### Return: - Marketing activity resource data  # [示例/Example] resource_id = 1052  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get(resource_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object resource_id: 资源ID/Resource ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get_with_http_info(resource_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get_with_http_info(resource_id, **kwargs)  # noqa: E501
            return data

    def get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get_with_http_info(self, resource_id, **kwargs):  # noqa: E501
        """获取营销活动案例/Get Resource List  # noqa: E501

        # [中文] ### 用途: - 获取营销活动案例列表 - 价格：0.001$ / 次 ### 参数: - resource_id: 资源ID ### 返回: - 营销活动案例数据  # [English] ### Purpose: - Get marketing activity resource list - Price: 0.001$ / time ### Parameters: - resource_id: Resource ID ### Return: - Marketing activity resource data  # [示例/Example] resource_id = 1052  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get_with_http_info(resource_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object resource_id: 资源ID/Resource ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resource_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resource_id' is set
        if self.api_client.client_side_validation and ('resource_id' not in params or
                                                       params['resource_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `resource_id` when calling `get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_id' in params:
            query_params.append(('resource_id', params['resource_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_resource_list', 'GET',
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

    def get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get(self, **kwargs):  # noqa: E501
        """获取用户主页二维码/Get User Profile QRCode  # noqa: E501

        # [中文] ### 用途: - 生成用户主页二维码 - core_user_id和sec_uid二选一传入即可 - 价格：0.001$ / 次 ### 参数: - core_user_id: 用户核心ID（与sec_uid二选一） - sec_uid: 用户sec_uid（与core_user_id二选一） ### 返回: - 用户主页二维码数据  # [English] ### Purpose: - Generate user profile QR code - Either core_user_id or sec_uid is required - Price: 0.001$ / time ### Parameters: - core_user_id: User core ID (pick one with sec_uid) - sec_uid: User sec_uid (pick one with core_user_id) ### Return: - User profile QR code data  # [示例/Example] core_user_id = \"1113181577281568\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object core_user_id: 用户核心ID(与sec_uid二选一)/User core ID (pick one with sec_uid)
        :param object sec_uid: 用户sec_uid(与core_user_id二选一)/User sec_uid (pick one with core_user_id)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户主页二维码/Get User Profile QRCode  # noqa: E501

        # [中文] ### 用途: - 生成用户主页二维码 - core_user_id和sec_uid二选一传入即可 - 价格：0.001$ / 次 ### 参数: - core_user_id: 用户核心ID（与sec_uid二选一） - sec_uid: 用户sec_uid（与core_user_id二选一） ### 返回: - 用户主页二维码数据  # [English] ### Purpose: - Generate user profile QR code - Either core_user_id or sec_uid is required - Price: 0.001$ / time ### Parameters: - core_user_id: User core ID (pick one with sec_uid) - sec_uid: User sec_uid (pick one with core_user_id) ### Return: - User profile QR code data  # [示例/Example] core_user_id = \"1113181577281568\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object core_user_id: 用户核心ID(与sec_uid二选一)/User core ID (pick one with sec_uid)
        :param object sec_uid: 用户sec_uid(与core_user_id二选一)/User sec_uid (pick one with core_user_id)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['core_user_id', 'sec_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'core_user_id' in params:
            query_params.append(('core_user_id', params['core_user_id']))  # noqa: E501
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/douyin/xingtu_v2/get_user_profile_qrcode', 'GET',
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
