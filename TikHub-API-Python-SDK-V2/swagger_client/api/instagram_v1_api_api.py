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


class InstagramV1APIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_cities_api_v1_instagram_v1_fetch_cities_get(self, country_code, **kwargs):  # noqa: E501
        """获取国家城市列表/Get cities by country  # noqa: E501

        # [中文] ### 用途: - 获取指定国家的城市/地区列表 ### 参数: - country_code: 国家代码，如US、CN、JP - page: 页码，默认1 ### 返回: - `country_info`: 国家信息 - `city_list`: 城市列表 - `next_page`: 下一页页码 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get cities/regions list of specified country ### Parameters: - country_code: Country code, e.g. US, CN, JP - page: Page number, default 1 ### Return: - `country_info`: Country info - `city_list`: Cities list - `next_page`: Next page number ### Price: - 0.001 USD/request  # [示例/Example] country_code = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cities_api_v1_instagram_v1_fetch_cities_get(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object country_code: 国家代码（如US、CN、JP）/Country code (e.g. US, CN, JP) (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_cities_api_v1_instagram_v1_fetch_cities_get_with_http_info(country_code, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_cities_api_v1_instagram_v1_fetch_cities_get_with_http_info(country_code, **kwargs)  # noqa: E501
            return data

    def fetch_cities_api_v1_instagram_v1_fetch_cities_get_with_http_info(self, country_code, **kwargs):  # noqa: E501
        """获取国家城市列表/Get cities by country  # noqa: E501

        # [中文] ### 用途: - 获取指定国家的城市/地区列表 ### 参数: - country_code: 国家代码，如US、CN、JP - page: 页码，默认1 ### 返回: - `country_info`: 国家信息 - `city_list`: 城市列表 - `next_page`: 下一页页码 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get cities/regions list of specified country ### Parameters: - country_code: Country code, e.g. US, CN, JP - page: Page number, default 1 ### Return: - `country_info`: Country info - `city_list`: Cities list - `next_page`: Next page number ### Price: - 0.001 USD/request  # [示例/Example] country_code = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_cities_api_v1_instagram_v1_fetch_cities_get_with_http_info(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object country_code: 国家代码（如US、CN、JP）/Country code (e.g. US, CN, JP) (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_cities_api_v1_instagram_v1_fetch_cities_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code' is set
        if self.api_client.client_side_validation and ('country_code' not in params or
                                                       params['country_code'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `country_code` when calling `fetch_cities_api_v1_instagram_v1_fetch_cities_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_cities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get(self, media_id, comment_id, **kwargs):  # noqa: E501
        """获取评论的子评论列表/Get comment replies  # noqa: E501

        # [中文] ### 用途: - 获取指定评论下的子评论（二级评论/回复），支持分页 ### 参数: - media_id: 帖子ID（媒体ID） - comment_id: 父评论ID（从fetch_post_comments_v2返回的评论pk字段获取） - min_id: 分页游标，首次请求不传，从上一次响应的`page_info.next_min_id`字段获取 ### 返回: - `child_comments`: 子评论列表，每个评论包含：   - `pk`: 评论ID   - `text`: 评论内容   - `created_at`/`created_at_utc`: 评论时间戳   - `user`: 评论者信息（pk, username, full_name, is_verified, profile_pic_url等）   - `comment_like_count`: 评论点赞数   - `parent_comment_id`: 父评论ID   - `has_translation`: 是否有翻译 - `child_comment_count`: 子评论总数 - `has_more_tail_child_comments`: 是否有更多子评论 - `next_min_child_cursor`: 下一页游标 - `page_info`: 分页信息汇总 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get child comments (replies) under a specific comment with pagination ### Parameters: - media_id: Post ID (Media ID) - comment_id: Parent comment ID (get from pk field in fetch_post_comments_v2 response) - min_id: Pagination cursor, omit for first request, get from previous response's `page_info.next_min_id` ### Return: - `child_comments`: Child comment list, each comment contains:   - `pk`: Comment ID   - `text`: Comment content   - `created_at`/`created_at_utc`: Comment timestamp   - `user`: Commenter info (pk, username, full_name, is_verified, profile_pic_url, etc.)   - `comment_like_count`: Comment like count   - `parent_comment_id`: Parent comment ID   - `has_translation`: Has translation - `child_comment_count`: Total child comment count - `has_more_tail_child_comments`: Has more child comments - `next_min_child_cursor`: Next page cursor - `page_info`: Pagination info summary ### Price: - 0.001 USD/request  # [示例/Example] media_id = \"3766120364183949816\" comment_id = \"17871667485468098\" min_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get(media_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子ID（媒体ID）/Post ID (Media ID) (required)
        :param object comment_id: 父评论ID/Parent comment ID (required)
        :param object min_id: 分页游标，从上一次响应的next_min_id获取/Pagination cursor from previous response's next_min_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get_with_http_info(media_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get_with_http_info(media_id, comment_id, **kwargs)  # noqa: E501
            return data

    def fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get_with_http_info(self, media_id, comment_id, **kwargs):  # noqa: E501
        """获取评论的子评论列表/Get comment replies  # noqa: E501

        # [中文] ### 用途: - 获取指定评论下的子评论（二级评论/回复），支持分页 ### 参数: - media_id: 帖子ID（媒体ID） - comment_id: 父评论ID（从fetch_post_comments_v2返回的评论pk字段获取） - min_id: 分页游标，首次请求不传，从上一次响应的`page_info.next_min_id`字段获取 ### 返回: - `child_comments`: 子评论列表，每个评论包含：   - `pk`: 评论ID   - `text`: 评论内容   - `created_at`/`created_at_utc`: 评论时间戳   - `user`: 评论者信息（pk, username, full_name, is_verified, profile_pic_url等）   - `comment_like_count`: 评论点赞数   - `parent_comment_id`: 父评论ID   - `has_translation`: 是否有翻译 - `child_comment_count`: 子评论总数 - `has_more_tail_child_comments`: 是否有更多子评论 - `next_min_child_cursor`: 下一页游标 - `page_info`: 分页信息汇总 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get child comments (replies) under a specific comment with pagination ### Parameters: - media_id: Post ID (Media ID) - comment_id: Parent comment ID (get from pk field in fetch_post_comments_v2 response) - min_id: Pagination cursor, omit for first request, get from previous response's `page_info.next_min_id` ### Return: - `child_comments`: Child comment list, each comment contains:   - `pk`: Comment ID   - `text`: Comment content   - `created_at`/`created_at_utc`: Comment timestamp   - `user`: Commenter info (pk, username, full_name, is_verified, profile_pic_url, etc.)   - `comment_like_count`: Comment like count   - `parent_comment_id`: Parent comment ID   - `has_translation`: Has translation - `child_comment_count`: Total child comment count - `has_more_tail_child_comments`: Has more child comments - `next_min_child_cursor`: Next page cursor - `page_info`: Pagination info summary ### Price: - 0.001 USD/request  # [示例/Example] media_id = \"3766120364183949816\" comment_id = \"17871667485468098\" min_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get_with_http_info(media_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子ID（媒体ID）/Post ID (Media ID) (required)
        :param object comment_id: 父评论ID/Parent comment ID (required)
        :param object min_id: 分页游标，从上一次响应的next_min_id获取/Pagination cursor from previous response's next_min_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['media_id', 'comment_id', 'min_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'media_id' is set
        if self.api_client.client_side_validation and ('media_id' not in params or
                                                       params['media_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `media_id` when calling `fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'media_id' in params:
            query_params.append(('media_id', params['media_id']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'min_id' in params:
            query_params.append(('min_id', params['min_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_comment_replies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_explore_sections_api_v1_instagram_v1_fetch_explore_sections_get(self, **kwargs):  # noqa: E501
        """获取探索页面分类/Get explore page sections  # noqa: E501

        # [中文] ### 用途: - 获取Instagram探索页面的所有分类和子分类 ### 返回: - `sections`: 分类列表，包含分类名称、子分类和推荐内容 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get all sections and subsections of Instagram explore page ### Return: - `sections`: Sections list with names, subsections and recommended content ### Price: - 0.001 USD/request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_explore_sections_api_v1_instagram_v1_fetch_explore_sections_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_explore_sections_api_v1_instagram_v1_fetch_explore_sections_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_explore_sections_api_v1_instagram_v1_fetch_explore_sections_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_explore_sections_api_v1_instagram_v1_fetch_explore_sections_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取探索页面分类/Get explore page sections  # noqa: E501

        # [中文] ### 用途: - 获取Instagram探索页面的所有分类和子分类 ### 返回: - `sections`: 分类列表，包含分类名称、子分类和推荐内容 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get all sections and subsections of Instagram explore page ### Return: - `sections`: Sections list with names, subsections and recommended content ### Price: - 0.001 USD/request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_explore_sections_api_v1_instagram_v1_fetch_explore_sections_get_with_http_info(async_req=True)
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
                    " to method fetch_explore_sections_api_v1_instagram_v1_fetch_explore_sections_get" % key
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
            '/api/v1/instagram/v1/fetch_explore_sections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get(self, hashtag, **kwargs):  # noqa: E501
        """获取话题标签下的帖子/Get posts by hashtag  # noqa: E501

        # [中文] ### 用途: - 获取指定话题标签下的帖子列表 ### 参数: - hashtag: 话题标签名称（不含#号） - end_cursor: 分页游标，首次请求不传 ### 返回: - GraphQL风格响应，包含`data.hashtag.edge_hashtag_to_media` ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get posts under specific hashtag ### Parameters: - hashtag: Hashtag name (without #) - end_cursor: Pagination cursor, omit for first request ### Return: - GraphQL style response with `data.hashtag.edge_hashtag_to_media` ### Price: - 0.001 USD/request  # [示例/Example] hashtag = \"cat\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get(hashtag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object hashtag: 话题标签名称（不含#号）/Hashtag name (without #) (required)
        :param object end_cursor: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get_with_http_info(hashtag, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get_with_http_info(hashtag, **kwargs)  # noqa: E501
            return data

    def fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get_with_http_info(self, hashtag, **kwargs):  # noqa: E501
        """获取话题标签下的帖子/Get posts by hashtag  # noqa: E501

        # [中文] ### 用途: - 获取指定话题标签下的帖子列表 ### 参数: - hashtag: 话题标签名称（不含#号） - end_cursor: 分页游标，首次请求不传 ### 返回: - GraphQL风格响应，包含`data.hashtag.edge_hashtag_to_media` ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get posts under specific hashtag ### Parameters: - hashtag: Hashtag name (without #) - end_cursor: Pagination cursor, omit for first request ### Return: - GraphQL style response with `data.hashtag.edge_hashtag_to_media` ### Price: - 0.001 USD/request  # [示例/Example] hashtag = \"cat\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get_with_http_info(hashtag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object hashtag: 话题标签名称（不含#号）/Hashtag name (without #) (required)
        :param object end_cursor: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hashtag', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hashtag' is set
        if self.api_client.client_side_validation and ('hashtag' not in params or
                                                       params['hashtag'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hashtag` when calling `fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hashtag' in params:
            query_params.append(('hashtag', params['hashtag']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_hashtag_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_location_info_api_v1_instagram_v1_fetch_location_info_get(self, location_id, **kwargs):  # noqa: E501
        """获取地点信息/Get location info  # noqa: E501

        # [中文] ### 用途: - 获取指定地点的详细信息 ### 参数: - location_id: 地点ID ### 返回: - `location_info`: 地点信息，包含名称、地址、坐标等 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get detailed information of specified location ### Parameters: - location_id: Location ID ### Return: - `location_info`: Location info including name, address, coordinates etc. ### Price: - 0.001 USD/request  # [示例/Example] location_id = \"703457703\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_location_info_api_v1_instagram_v1_fetch_location_info_get(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object location_id: 地点ID/Location ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_location_info_api_v1_instagram_v1_fetch_location_info_get_with_http_info(location_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_location_info_api_v1_instagram_v1_fetch_location_info_get_with_http_info(location_id, **kwargs)  # noqa: E501
            return data

    def fetch_location_info_api_v1_instagram_v1_fetch_location_info_get_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """获取地点信息/Get location info  # noqa: E501

        # [中文] ### 用途: - 获取指定地点的详细信息 ### 参数: - location_id: 地点ID ### 返回: - `location_info`: 地点信息，包含名称、地址、坐标等 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get detailed information of specified location ### Parameters: - location_id: Location ID ### Return: - `location_info`: Location info including name, address, coordinates etc. ### Price: - 0.001 USD/request  # [示例/Example] location_id = \"703457703\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_location_info_api_v1_instagram_v1_fetch_location_info_get_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object location_id: 地点ID/Location ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_location_info_api_v1_instagram_v1_fetch_location_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in params or
                                                       params['location_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `location_id` when calling `fetch_location_info_api_v1_instagram_v1_fetch_location_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'location_id' in params:
            query_params.append(('location_id', params['location_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_location_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get(self, location_id, **kwargs):  # noqa: E501
        """获取地点下的帖子/Get posts by location  # noqa: E501

        # [中文] ### 用途: - 获取指定地点标记的帖子列表 ### 参数: - location_id: 地点ID - tab: 排序方式，ranked(热门)/recent(最新) - end_cursor: 分页游标，首次请求不传 ### 返回: - `edges`: 帖子列表 - `page_info`: 分页信息 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get posts tagged at specified location ### Parameters: - location_id: Location ID - tab: Sorting method, ranked(top)/recent(latest) - end_cursor: Pagination cursor, omit for first request ### Return: - `edges`: Posts list - `page_info`: Pagination info ### Price: - 0.001 USD/request  # [示例/Example] location_id = \"703457703\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object location_id: 地点ID/Location ID (required)
        :param object tab: 排序方式：ranked(热门)/recent(最新)/Sorting: ranked(top)/recent(latest)
        :param object end_cursor: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get_with_http_info(location_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get_with_http_info(location_id, **kwargs)  # noqa: E501
            return data

    def fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """获取地点下的帖子/Get posts by location  # noqa: E501

        # [中文] ### 用途: - 获取指定地点标记的帖子列表 ### 参数: - location_id: 地点ID - tab: 排序方式，ranked(热门)/recent(最新) - end_cursor: 分页游标，首次请求不传 ### 返回: - `edges`: 帖子列表 - `page_info`: 分页信息 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get posts tagged at specified location ### Parameters: - location_id: Location ID - tab: Sorting method, ranked(top)/recent(latest) - end_cursor: Pagination cursor, omit for first request ### Return: - `edges`: Posts list - `page_info`: Pagination info ### Price: - 0.001 USD/request  # [示例/Example] location_id = \"703457703\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object location_id: 地点ID/Location ID (required)
        :param object tab: 排序方式：ranked(热门)/recent(最新)/Sorting: ranked(top)/recent(latest)
        :param object end_cursor: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'tab', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in params or
                                                       params['location_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `location_id` when calling `fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'location_id' in params:
            query_params.append(('location_id', params['location_id']))  # noqa: E501
        if 'tab' in params:
            query_params.append(('tab', params['tab']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_location_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_locations_api_v1_instagram_v1_fetch_locations_get(self, city_id, **kwargs):  # noqa: E501
        """获取城市地点列表/Get locations by city  # noqa: E501

        # [中文] ### 用途: - 获取指定城市下的Instagram地点列表 ### 参数: - city_id: 城市ID（可从fetch_cities接口获取） - page: 页码，默认1 ### 返回: - `country_info`: 国家信息 - `city_info`: 城市信息 - `location_list`: 地点列表 - `next_page`: 下一页页码 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get Instagram locations list of specified city ### Parameters: - city_id: City ID (from fetch_cities API) - page: Page number, default 1 ### Return: - `country_info`: Country info - `city_info`: City info - `location_list`: Locations list - `next_page`: Next page number ### Price: - 0.001 USD/request  # [示例/Example] city_id = \"c2791472\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_locations_api_v1_instagram_v1_fetch_locations_get(city_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object city_id: 城市ID（从fetch_cities获取）/City ID (from fetch_cities) (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_locations_api_v1_instagram_v1_fetch_locations_get_with_http_info(city_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_locations_api_v1_instagram_v1_fetch_locations_get_with_http_info(city_id, **kwargs)  # noqa: E501
            return data

    def fetch_locations_api_v1_instagram_v1_fetch_locations_get_with_http_info(self, city_id, **kwargs):  # noqa: E501
        """获取城市地点列表/Get locations by city  # noqa: E501

        # [中文] ### 用途: - 获取指定城市下的Instagram地点列表 ### 参数: - city_id: 城市ID（可从fetch_cities接口获取） - page: 页码，默认1 ### 返回: - `country_info`: 国家信息 - `city_info`: 城市信息 - `location_list`: 地点列表 - `next_page`: 下一页页码 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get Instagram locations list of specified city ### Parameters: - city_id: City ID (from fetch_cities API) - page: Page number, default 1 ### Return: - `country_info`: Country info - `city_info`: City info - `location_list`: Locations list - `next_page`: Next page number ### Price: - 0.001 USD/request  # [示例/Example] city_id = \"c2791472\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_locations_api_v1_instagram_v1_fetch_locations_get_with_http_info(city_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object city_id: 城市ID（从fetch_cities获取）/City ID (from fetch_cities) (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['city_id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_locations_api_v1_instagram_v1_fetch_locations_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'city_id' is set
        if self.api_client.client_side_validation and ('city_id' not in params or
                                                       params['city_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `city_id` when calling `fetch_locations_api_v1_instagram_v1_fetch_locations_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'city_id' in params:
            query_params.append(('city_id', params['city_id']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_locations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_music_posts_api_v1_instagram_v1_fetch_music_posts_get(self, **kwargs):  # noqa: E501
        """获取使用特定音乐的帖子/Get posts using specific music  # noqa: E501

        # [中文] ### 用途: - 获取使用指定音乐/音频的Reels和帖子列表 ### 参数: - music_id: 音乐ID（与music_url二选一） - music_url: 音乐URL，会自动提取ID（与music_id二选一） - max_id: 分页游标，首次请求不传 ### 返回: - `items`: 帖子列表 - `metadata`: 音乐元数据 - `paging_info`: 分页信息 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get Reels and posts using specific music/audio ### Parameters: - music_id: Music ID (alternative to music_url) - music_url: Music URL, ID will be extracted automatically (alternative to music_id) - max_id: Pagination cursor, omit for first request ### Return: - `items`: Posts list - `metadata`: Music metadata - `paging_info`: Pagination info ### Price: - 0.001 USD/request  # [示例/Example] music_id = \"564058920086577\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_posts_api_v1_instagram_v1_fetch_music_posts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object music_id: 音乐ID/Music ID
        :param object music_url: 音乐URL（与music_id二选一）/Music URL (alternative to music_id)
        :param object max_id: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_music_posts_api_v1_instagram_v1_fetch_music_posts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_music_posts_api_v1_instagram_v1_fetch_music_posts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_music_posts_api_v1_instagram_v1_fetch_music_posts_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取使用特定音乐的帖子/Get posts using specific music  # noqa: E501

        # [中文] ### 用途: - 获取使用指定音乐/音频的Reels和帖子列表 ### 参数: - music_id: 音乐ID（与music_url二选一） - music_url: 音乐URL，会自动提取ID（与music_id二选一） - max_id: 分页游标，首次请求不传 ### 返回: - `items`: 帖子列表 - `metadata`: 音乐元数据 - `paging_info`: 分页信息 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get Reels and posts using specific music/audio ### Parameters: - music_id: Music ID (alternative to music_url) - music_url: Music URL, ID will be extracted automatically (alternative to music_id) - max_id: Pagination cursor, omit for first request ### Return: - `items`: Posts list - `metadata`: Music metadata - `paging_info`: Pagination info ### Price: - 0.001 USD/request  # [示例/Example] music_id = \"564058920086577\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_posts_api_v1_instagram_v1_fetch_music_posts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object music_id: 音乐ID/Music ID
        :param object music_url: 音乐URL（与music_id二选一）/Music URL (alternative to music_id)
        :param object max_id: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['music_id', 'music_url', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_music_posts_api_v1_instagram_v1_fetch_music_posts_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'music_id' in params:
            query_params.append(('music_id', params['music_id']))  # noqa: E501
        if 'music_url' in params:
            query_params.append(('music_url', params['music_url']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_music_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get(self, post_id, **kwargs):  # noqa: E501
        """通过ID获取帖子详情/Get post by ID  # noqa: E501

        # [中文] ### 用途: - 通过ID获取单个帖子的详细信息 ### 参数: - post_id: 帖子ID ### 返回: - 帖子详情对象，包含媒体、点赞数、评论等 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get single post details by ID ### Parameters: - post_id: Post ID ### Return: - Post details object with media, likes, comments etc. ### Price: - 0.001 USD/request  # [示例/Example] post_id = \"3742637871112032100\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get_with_http_info(post_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get_with_http_info(post_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get_with_http_info(self, post_id, **kwargs):  # noqa: E501
        """通过ID获取帖子详情/Get post by ID  # noqa: E501

        # [中文] ### 用途: - 通过ID获取单个帖子的详细信息 ### 参数: - post_id: 帖子ID ### 返回: - 帖子详情对象，包含媒体、点赞数、评论等 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get single post details by ID ### Parameters: - post_id: Post ID ### Return: - Post details object with media, likes, comments etc. ### Price: - 0.001 USD/request  # [示例/Example] post_id = \"3742637871112032100\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get_with_http_info(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_id' is set
        if self.api_client.client_side_validation and ('post_id' not in params or
                                                       params['post_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_id` when calling `fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_post_by_id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get(self, post_url, **kwargs):  # noqa: E501
        """通过URL获取帖子详情/Get post by URL  # noqa: E501

        # [中文] ### 用途: - 通过URL获取单个帖子的详细信息 ### 参数: - post_url: 帖子URL ### 返回: - 帖子详情对象，包含媒体、点赞数、评论等 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get single post details by URL ### Parameters: - post_url: Post URL ### Return: - Post details object with media, likes, comments etc. ### Price: - 0.001 USD/request  # [示例/Example] post_url = \"https://www.instagram.com/p/DPwhVB-jo9k/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get(post_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_url: 帖子URL/Post URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get_with_http_info(post_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get_with_http_info(post_url, **kwargs)  # noqa: E501
            return data

    def fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get_with_http_info(self, post_url, **kwargs):  # noqa: E501
        """通过URL获取帖子详情/Get post by URL  # noqa: E501

        # [中文] ### 用途: - 通过URL获取单个帖子的详细信息 ### 参数: - post_url: 帖子URL ### 返回: - 帖子详情对象，包含媒体、点赞数、评论等 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get single post details by URL ### Parameters: - post_url: Post URL ### Return: - Post details object with media, likes, comments etc. ### Price: - 0.001 USD/request  # [示例/Example] post_url = \"https://www.instagram.com/p/DPwhVB-jo9k/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get_with_http_info(post_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_url: 帖子URL/Post URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_url' is set
        if self.api_client.client_side_validation and ('post_url' not in params or
                                                       params['post_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_url` when calling `fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_url' in params:
            query_params.append(('post_url', params['post_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_post_by_url', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get(self, post_url, **kwargs):  # noqa: E501
        """通过URL获取帖子详情 V2/Get post by URL V2  # noqa: E501

        # [中文] ### 用途: - 通过URL获取单个帖子的详细信息 V2 - 数据没有V1完整，但速度更快，用于下载大量帖子时推荐使用。 ### 参数: - post_url: 帖子URL ### 返回: - 帖子详情对象，包含媒体、点赞数、评论等 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get single post details by URL V2 - Data is not as complete as V1, but faster. Recommended for downloading large number of posts. ### Parameters: - post_url: Post URL ### Return: - Post details object with media, likes, comments etc. ### Price: - 0.001 USD/request  # [示例/Example] post_url = \"https://www.instagram.com/p/DPwhVB-jo9k/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get(post_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_url: 帖子URL/Post URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get_with_http_info(post_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get_with_http_info(post_url, **kwargs)  # noqa: E501
            return data

    def fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get_with_http_info(self, post_url, **kwargs):  # noqa: E501
        """通过URL获取帖子详情 V2/Get post by URL V2  # noqa: E501

        # [中文] ### 用途: - 通过URL获取单个帖子的详细信息 V2 - 数据没有V1完整，但速度更快，用于下载大量帖子时推荐使用。 ### 参数: - post_url: 帖子URL ### 返回: - 帖子详情对象，包含媒体、点赞数、评论等 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get single post details by URL V2 - Data is not as complete as V1, but faster. Recommended for downloading large number of posts. ### Parameters: - post_url: Post URL ### Return: - Post details object with media, likes, comments etc. ### Price: - 0.001 USD/request  # [示例/Example] post_url = \"https://www.instagram.com/p/DPwhVB-jo9k/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get_with_http_info(post_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_url: 帖子URL/Post URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_url' is set
        if self.api_client.client_side_validation and ('post_url' not in params or
                                                       params['post_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_url` when calling `fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_url' in params:
            query_params.append(('post_url', params['post_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_post_by_url_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get(self, media_id, **kwargs):  # noqa: E501
        """获取帖子评论列表V2/Get post comments V2  # noqa: E501

        # [中文] ### 用途: - 获取帖子评论列表，支持分页 - 返回的评论数据更完整，包含子评论预览和更多元数据 ### 参数: - media_id: 帖子ID（媒体ID） - sort_order: 排序方式，popular(热门)/recent(最新) - min_id: 分页游标，首次请求不传，从上一次响应的`next_min_id`字段获取 ### 返回: - `comment_count`: 评论总数 - `comments`: 评论列表，每个评论包含：   - `pk`: 评论ID   - `text`: 评论内容   - `created_at`/`created_at_utc`: 评论时间戳   - `user`: 评论者信息（pk, username, full_name, is_verified, profile_pic_url等）   - `comment_like_count`: 评论点赞数   - `child_comment_count`: 子评论数量   - `preview_child_comments`: 子评论预览列表   - `is_liked_by_media_owner`: 是否被帖子作者点赞   - `has_translation`: 是否有翻译 - `next_min_id`: 下一页游标（JSON格式字符串） - `has_more_headload_comments`: 是否有更多评论 - `caption`: 帖子描述信息 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get post comments list with pagination - Returns more complete comment data including child comment previews and more metadata ### Parameters: - media_id: Post ID (Media ID) - sort_order: Sorting method, popular/recent - min_id: Pagination cursor, omit for first request, get from previous response's `next_min_id` ### Return: - `comment_count`: Total comments count - `comments`: Comments list, each comment contains:   - `pk`: Comment ID   - `text`: Comment content   - `created_at`/`created_at_utc`: Comment timestamp   - `user`: Commenter info (pk, username, full_name, is_verified, profile_pic_url etc.)   - `comment_like_count`: Comment likes count   - `child_comment_count`: Child comments count   - `preview_child_comments`: Child comments preview list   - `is_liked_by_media_owner`: Whether liked by post author   - `has_translation`: Whether translation available - `next_min_id`: Next page cursor (JSON format string) - `has_more_headload_comments`: Whether more comments available - `caption`: Post caption info ### Price: - 0.001 USD/request  # [示例/Example] media_id = \"3766120364183949816\" sort_order = \"recent\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get(media_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子ID（媒体ID）/Post ID (Media ID) (required)
        :param object sort_order: 排序方式：popular(热门)/recent(最新)/Sorting: popular/recent
        :param object min_id: 分页游标，从上一次响应的next_min_id获取/Pagination cursor from previous response's next_min_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get_with_http_info(media_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get_with_http_info(media_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get_with_http_info(self, media_id, **kwargs):  # noqa: E501
        """获取帖子评论列表V2/Get post comments V2  # noqa: E501

        # [中文] ### 用途: - 获取帖子评论列表，支持分页 - 返回的评论数据更完整，包含子评论预览和更多元数据 ### 参数: - media_id: 帖子ID（媒体ID） - sort_order: 排序方式，popular(热门)/recent(最新) - min_id: 分页游标，首次请求不传，从上一次响应的`next_min_id`字段获取 ### 返回: - `comment_count`: 评论总数 - `comments`: 评论列表，每个评论包含：   - `pk`: 评论ID   - `text`: 评论内容   - `created_at`/`created_at_utc`: 评论时间戳   - `user`: 评论者信息（pk, username, full_name, is_verified, profile_pic_url等）   - `comment_like_count`: 评论点赞数   - `child_comment_count`: 子评论数量   - `preview_child_comments`: 子评论预览列表   - `is_liked_by_media_owner`: 是否被帖子作者点赞   - `has_translation`: 是否有翻译 - `next_min_id`: 下一页游标（JSON格式字符串） - `has_more_headload_comments`: 是否有更多评论 - `caption`: 帖子描述信息 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get post comments list with pagination - Returns more complete comment data including child comment previews and more metadata ### Parameters: - media_id: Post ID (Media ID) - sort_order: Sorting method, popular/recent - min_id: Pagination cursor, omit for first request, get from previous response's `next_min_id` ### Return: - `comment_count`: Total comments count - `comments`: Comments list, each comment contains:   - `pk`: Comment ID   - `text`: Comment content   - `created_at`/`created_at_utc`: Comment timestamp   - `user`: Commenter info (pk, username, full_name, is_verified, profile_pic_url etc.)   - `comment_like_count`: Comment likes count   - `child_comment_count`: Child comments count   - `preview_child_comments`: Child comments preview list   - `is_liked_by_media_owner`: Whether liked by post author   - `has_translation`: Whether translation available - `next_min_id`: Next page cursor (JSON format string) - `has_more_headload_comments`: Whether more comments available - `caption`: Post caption info ### Price: - 0.001 USD/request  # [示例/Example] media_id = \"3766120364183949816\" sort_order = \"recent\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get_with_http_info(media_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子ID（媒体ID）/Post ID (Media ID) (required)
        :param object sort_order: 排序方式：popular(热门)/recent(最新)/Sorting: popular/recent
        :param object min_id: 分页游标，从上一次响应的next_min_id获取/Pagination cursor from previous response's next_min_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['media_id', 'sort_order', 'min_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'media_id' is set
        if self.api_client.client_side_validation and ('media_id' not in params or
                                                       params['media_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `media_id` when calling `fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'media_id' in params:
            query_params.append(('media_id', params['media_id']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501
        if 'min_id' in params:
            query_params.append(('min_id', params['min_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_post_comments_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get(self, user_id, **kwargs):  # noqa: E501
        """获取相关用户推荐/Get related profiles  # noqa: E501

        # [中文] ### 用途: - 获取与指定用户相关/相似的用户推荐列表 ### 参数: - user_id: Instagram用户ID ### 返回: - GraphQL风格响应，包含`data.user.edge_related_profiles` ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get related/similar user recommendations ### Parameters: - user_id: Instagram user ID ### Return: - GraphQL style response with `data.user.edge_related_profiles` ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取相关用户推荐/Get related profiles  # noqa: E501

        # [中文] ### 用途: - 获取与指定用户相关/相似的用户推荐列表 ### 参数: - user_id: Instagram用户ID ### 返回: - GraphQL风格响应，包含`data.user.edge_related_profiles` ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get related/similar user recommendations ### Parameters: - user_id: Instagram user ID ### Return: - GraphQL style response with `data.user.edge_related_profiles` ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
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
                    " to method fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get`")  # noqa: E501

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
            '/api/v1/instagram/v1/fetch_related_profiles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_search_api_v1_instagram_v1_fetch_search_get(self, query, **kwargs):  # noqa: E501
        """搜索用户/话题/地点/Search users/hashtags/places  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram上的用户、话题标签或地点 ### 参数: - query: 搜索关键词 - select: 筛选类型（可选）   - `users`: 仅返回用户   - `hashtags`: 仅返回话题标签   - `places`: 仅返回地点   - 不传: 返回所有类型 ### 返回: - `users`: 用户列表 - `hashtags`: 话题列表 - `places`: 地点列表 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Search users, hashtags or places on Instagram ### Parameters: - query: Search keyword - select: Filter type (optional)   - `users`: Only return users   - `hashtags`: Only return hashtags   - `places`: Only return places   - omit: Return all types ### Return: - `users`: Users list - `hashtags`: Hashtags list - `places`: Places list ### Price: - 0.001 USD/request  # [示例/Example] query = \"taylorswift\" select = \"users\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_api_v1_instagram_v1_fetch_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object select: 筛选类型：users/hashtags/places，不传则返回全部/Filter type: users/hashtags/places, omit for all
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_api_v1_instagram_v1_fetch_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_api_v1_instagram_v1_fetch_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_search_api_v1_instagram_v1_fetch_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """搜索用户/话题/地点/Search users/hashtags/places  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram上的用户、话题标签或地点 ### 参数: - query: 搜索关键词 - select: 筛选类型（可选）   - `users`: 仅返回用户   - `hashtags`: 仅返回话题标签   - `places`: 仅返回地点   - 不传: 返回所有类型 ### 返回: - `users`: 用户列表 - `hashtags`: 话题列表 - `places`: 地点列表 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Search users, hashtags or places on Instagram ### Parameters: - query: Search keyword - select: Filter type (optional)   - `users`: Only return users   - `hashtags`: Only return hashtags   - `places`: Only return places   - omit: Return all types ### Return: - `users`: Users list - `hashtags`: Hashtags list - `places`: Places list ### Price: - 0.001 USD/request  # [示例/Example] query = \"taylorswift\" select = \"users\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_api_v1_instagram_v1_fetch_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object select: 筛选类型：users/hashtags/places，不传则返回全部/Filter type: users/hashtags/places, omit for all
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'select']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_api_v1_instagram_v1_fetch_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_search_api_v1_instagram_v1_fetch_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get(self, section_id, **kwargs):  # noqa: E501
        """获取分类下的帖子/Get posts by section  # noqa: E501

        # [中文] ### 用途: - 获取探索页面某个分类下的帖子列表 ### 参数: - section_id: 分类ID（可从fetch_explore_sections接口获取） - count: 每页数量，默认20 - max_id: 分页游标，首次请求不传 ### 返回: - `section_name`: 分类名称 - `items`: 帖子列表 - `subsections`: 子分类列表 - `max_id`: 下一页游标 - `more_available`: 是否有更多数据 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get posts under specific explore section ### Parameters: - section_id: Section ID (from fetch_explore_sections API) - count: Count per page, default 20 - max_id: Pagination cursor, omit for first request ### Return: - `section_name`: Section name - `items`: Posts list - `subsections`: Subsections list - `max_id`: Next page cursor - `more_available`: Whether more data available ### Price: - 0.001 USD/request  # [示例/Example] section_id = \"10156104410190727\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get(section_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object section_id: 分类ID（从fetch_explore_sections获取）/Section ID (from fetch_explore_sections) (required)
        :param object count: 每页数量/Count per page
        :param object max_id: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get_with_http_info(section_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get_with_http_info(section_id, **kwargs)  # noqa: E501
            return data

    def fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get_with_http_info(self, section_id, **kwargs):  # noqa: E501
        """获取分类下的帖子/Get posts by section  # noqa: E501

        # [中文] ### 用途: - 获取探索页面某个分类下的帖子列表 ### 参数: - section_id: 分类ID（可从fetch_explore_sections接口获取） - count: 每页数量，默认20 - max_id: 分页游标，首次请求不传 ### 返回: - `section_name`: 分类名称 - `items`: 帖子列表 - `subsections`: 子分类列表 - `max_id`: 下一页游标 - `more_available`: 是否有更多数据 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get posts under specific explore section ### Parameters: - section_id: Section ID (from fetch_explore_sections API) - count: Count per page, default 20 - max_id: Pagination cursor, omit for first request ### Return: - `section_name`: Section name - `items`: Posts list - `subsections`: Subsections list - `max_id`: Next page cursor - `more_available`: Whether more data available ### Price: - 0.001 USD/request  # [示例/Example] section_id = \"10156104410190727\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get_with_http_info(section_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object section_id: 分类ID（从fetch_explore_sections获取）/Section ID (from fetch_explore_sections) (required)
        :param object count: 每页数量/Count per page
        :param object max_id: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['section_id', 'count', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'section_id' is set
        if self.api_client.client_side_validation and ('section_id' not in params or
                                                       params['section_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `section_id` when calling `fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'section_id' in params:
            query_params.append(('section_id', params['section_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_section_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户的About信息/Get user about info  # noqa: E501

        # [中文] ### 用途: - 获取用户的\"关于此账户\"（About This Account）信息 - 包含账户创建日期、所在地区、认证状态等详细信息 ### 参数: - user_id: Instagram用户ID（数字格式） ### 返回: - `status`: 请求状态 - `user_id`: 用户ID - `username`: 用户名 - `profile_pic_url`: 头像URL - `is_verified`: 是否认证 - `date_joined`: 账户创建日期（如：\"June 2012\"） - `account_based_in`: 账户所在地区（如：\"United States\"） - `verified_date`: 认证日期（如：\"August 2017\"，未认证则为None） ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user's \"About This Account\" information - Contains account creation date, location, verification status and more ### Parameters: - user_id: Instagram user ID (numeric format) ### Return: - `status`: Request status - `user_id`: User ID - `username`: Username - `profile_pic_url`: Profile picture URL - `is_verified`: Whether verified - `date_joined`: Account creation date (e.g., \"June 2012\") - `account_based_in`: Account location (e.g., \"United States\") - `verified_date`: Verification date (e.g., \"August 2017\", None if not verified) ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"182988865\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户的About信息/Get user about info  # noqa: E501

        # [中文] ### 用途: - 获取用户的\"关于此账户\"（About This Account）信息 - 包含账户创建日期、所在地区、认证状态等详细信息 ### 参数: - user_id: Instagram用户ID（数字格式） ### 返回: - `status`: 请求状态 - `user_id`: 用户ID - `username`: 用户名 - `profile_pic_url`: 头像URL - `is_verified`: 是否认证 - `date_joined`: 账户创建日期（如：\"June 2012\"） - `account_based_in`: 账户所在地区（如：\"United States\"） - `verified_date`: 认证日期（如：\"August 2017\"，未认证则为None） ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user's \"About This Account\" information - Contains account creation date, location, verification status and more ### Parameters: - user_id: Instagram user ID (numeric format) ### Return: - `status`: Request status - `user_id`: User ID - `username`: Username - `profile_pic_url`: Profile picture URL - `is_verified`: Whether verified - `date_joined`: Account creation date (e.g., \"June 2012\") - `account_based_in`: Account location (e.g., \"United States\") - `verified_date`: Verification date (e.g., \"August 2017\", None if not verified) ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"182988865\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
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
                    " to method fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get`")  # noqa: E501

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
            '/api/v1/instagram/v1/fetch_user_about_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get(self, user_id, **kwargs):  # noqa: E501
        """根据用户ID获取用户数据/Get user data by user ID  # noqa: E501

        # [中文] ### 用途: - 根据Instagram用户ID获取用户数据 ### 参数: - user_id: Instagram用户ID ### 返回: - 用户信息对象，包含时间线媒体、高清头像等完整数据 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user data by Instagram user ID ### Parameters: - user_id: Instagram user ID ### Return: - User information object with timeline media, HD avatar and complete data ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """根据用户ID获取用户数据/Get user data by user ID  # noqa: E501

        # [中文] ### 用途: - 根据Instagram用户ID获取用户数据 ### 参数: - user_id: Instagram用户ID ### 返回: - 用户信息对象，包含时间线媒体、高清头像等完整数据 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user data by Instagram user ID ### Parameters: - user_id: Instagram user ID ### Return: - User information object with timeline media, HD avatar and complete data ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
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
                    " to method fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get`")  # noqa: E501

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
            '/api/v1/instagram/v1/fetch_user_info_by_id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get(self, user_id, **kwargs):  # noqa: E501
        """根据用户ID获取用户数据V2/Get user data by user ID V2  # noqa: E501

        # [中文] ### 用途: - 根据Instagram用户ID获取用户数据，返回更详细的信息 ### 参数: - user_id: Instagram用户ID ### 返回: - 用户信息对象，包含bio_links、hd_profile_pic_url_info等更多字段 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user data by Instagram user ID with more details ### Parameters: - user_id: Instagram user ID ### Return: - User information object with bio_links, hd_profile_pic_url_info and more ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """根据用户ID获取用户数据V2/Get user data by user ID V2  # noqa: E501

        # [中文] ### 用途: - 根据Instagram用户ID获取用户数据，返回更详细的信息 ### 参数: - user_id: Instagram用户ID ### 返回: - 用户信息对象，包含bio_links、hd_profile_pic_url_info等更多字段 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user data by Instagram user ID with more details ### Parameters: - user_id: Instagram user ID ### Return: - User information object with bio_links, hd_profile_pic_url_info and more ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
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
                    " to method fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get`")  # noqa: E501

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
            '/api/v1/instagram/v1/fetch_user_info_by_id_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get(self, username, **kwargs):  # noqa: E501
        """根据用户名获取用户数据/Get user data by username  # noqa: E501

        # [中文] ### 用途: - 根据Instagram用户名获取用户数据 ### 参数: - username: Instagram用户名 ### 返回: - 用户信息对象，包含以下主要字段：   - `id`: 用户ID   - `username`: 用户名   - `full_name`: 用户全名   - `biography`: 个人简介   - `bio_links`: 个人简介链接列表   - `edge_followed_by`: 粉丝数 {count: xxx}   - `edge_follow`: 关注数 {count: xxx}   - `profile_pic_url`: 头像URL   - `profile_pic_url_hd`: 高清头像URL   - `is_private`: 是否私密账户   - `is_verified`: 是否已认证   - `external_url`: 外部链接   - `is_business_account`: 是否商业账户   - `is_professional_account`: 是否专业账户   - `highlight_reel_count`: 精选集数量   - `edge_owner_to_timeline_media`: 时间线媒体（包含最近帖子） ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user data by Instagram username ### Parameters: - username: Instagram username ### Return: - User information object with main fields:   - `id`: User ID   - `username`: Username   - `full_name`: Full name   - `biography`: Bio   - `bio_links`: Bio links list   - `edge_followed_by`: Followers count {count: xxx}   - `edge_follow`: Following count {count: xxx}   - `profile_pic_url`: Profile picture URL   - `profile_pic_url_hd`: HD profile picture URL   - `is_private`: Whether account is private   - `is_verified`: Whether account is verified   - `external_url`: External link   - `is_business_account`: Whether business account   - `is_professional_account`: Whether professional account   - `highlight_reel_count`: Highlights count   - `edge_owner_to_timeline_media`: Timeline media (contains recent posts) ### Price: - 0.001 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: Instagram用户名/Instagram username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """根据用户名获取用户数据/Get user data by username  # noqa: E501

        # [中文] ### 用途: - 根据Instagram用户名获取用户数据 ### 参数: - username: Instagram用户名 ### 返回: - 用户信息对象，包含以下主要字段：   - `id`: 用户ID   - `username`: 用户名   - `full_name`: 用户全名   - `biography`: 个人简介   - `bio_links`: 个人简介链接列表   - `edge_followed_by`: 粉丝数 {count: xxx}   - `edge_follow`: 关注数 {count: xxx}   - `profile_pic_url`: 头像URL   - `profile_pic_url_hd`: 高清头像URL   - `is_private`: 是否私密账户   - `is_verified`: 是否已认证   - `external_url`: 外部链接   - `is_business_account`: 是否商业账户   - `is_professional_account`: 是否专业账户   - `highlight_reel_count`: 精选集数量   - `edge_owner_to_timeline_media`: 时间线媒体（包含最近帖子） ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user data by Instagram username ### Parameters: - username: Instagram username ### Return: - User information object with main fields:   - `id`: User ID   - `username`: Username   - `full_name`: Full name   - `biography`: Bio   - `bio_links`: Bio links list   - `edge_followed_by`: Followers count {count: xxx}   - `edge_follow`: Following count {count: xxx}   - `profile_pic_url`: Profile picture URL   - `profile_pic_url_hd`: HD profile picture URL   - `is_private`: Whether account is private   - `is_verified`: Whether account is verified   - `external_url`: External link   - `is_business_account`: Whether business account   - `is_professional_account`: Whether professional account   - `highlight_reel_count`: Highlights count   - `edge_owner_to_timeline_media`: Timeline media (contains recent posts) ### Price: - 0.001 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: Instagram用户名/Instagram username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_user_info_by_username', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get(self, username, **kwargs):  # noqa: E501
        """根据用户名获取用户数据V2/Get user data by username V2  # noqa: E501

        # [中文] ### 用途: - 根据Instagram用户名获取用户数据 ### 参数: - username: Instagram用户名 ### 返回: - 用户信息对象，包含以下主要字段：   - `id`: 用户ID   - `username`: 用户名   - `full_name`: 用户全名   - `biography`: 个人简介   - `bio_links`: 个人简介链接列表   - `edge_followed_by`: 粉丝数 {count: xxx}   - `edge_follow`: 关注数 {count: xxx}   - `profile_pic_url`: 头像URL   - `profile_pic_url_hd`: 高清头像URL   - `is_private`: 是否私密账户   - `is_verified`: 是否已认证   - `external_url`: 外部链接   - `is_business_account`: 是否商业账户   - `is_professional_account`: 是否专业账户   - `highlight_reel_count`: 精选集数量   - `edge_owner_to_timeline_media`: 时间线媒体（包含最近12条帖子）   - `status`: 请求状态   - `attempts`: 尝试次数 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user data by Instagram username ### Parameters: - username: Instagram username ### Return: - User information object with main fields:   - `id`: User ID   - `username`: Username   - `full_name`: Full name   - `biography`: Bio   - `bio_links`: Bio links list   - `edge_followed_by`: Followers count {count: xxx}   - `edge_follow`: Following count {count: xxx}   - `profile_pic_url`: Profile picture URL   - `profile_pic_url_hd`: HD profile picture URL   - `is_private`: Whether account is private   - `is_verified`: Whether account is verified   - `external_url`: External link   - `is_business_account`: Whether business account   - `is_professional_account`: Whether professional account   - `highlight_reel_count`: Highlights count   - `edge_owner_to_timeline_media`: Timeline media (contains recent 12 posts)   - `status`: Request status   - `attempts`: Retry attempts ### Price: - 0.001 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: Instagram用户名/Instagram username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """根据用户名获取用户数据V2/Get user data by username V2  # noqa: E501

        # [中文] ### 用途: - 根据Instagram用户名获取用户数据 ### 参数: - username: Instagram用户名 ### 返回: - 用户信息对象，包含以下主要字段：   - `id`: 用户ID   - `username`: 用户名   - `full_name`: 用户全名   - `biography`: 个人简介   - `bio_links`: 个人简介链接列表   - `edge_followed_by`: 粉丝数 {count: xxx}   - `edge_follow`: 关注数 {count: xxx}   - `profile_pic_url`: 头像URL   - `profile_pic_url_hd`: 高清头像URL   - `is_private`: 是否私密账户   - `is_verified`: 是否已认证   - `external_url`: 外部链接   - `is_business_account`: 是否商业账户   - `is_professional_account`: 是否专业账户   - `highlight_reel_count`: 精选集数量   - `edge_owner_to_timeline_media`: 时间线媒体（包含最近12条帖子）   - `status`: 请求状态   - `attempts`: 尝试次数 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user data by Instagram username ### Parameters: - username: Instagram username ### Return: - User information object with main fields:   - `id`: User ID   - `username`: Username   - `full_name`: Full name   - `biography`: Bio   - `bio_links`: Bio links list   - `edge_followed_by`: Followers count {count: xxx}   - `edge_follow`: Following count {count: xxx}   - `profile_pic_url`: Profile picture URL   - `profile_pic_url_hd`: HD profile picture URL   - `is_private`: Whether account is private   - `is_verified`: Whether account is verified   - `external_url`: External link   - `is_business_account`: Whether business account   - `is_professional_account`: Whether professional account   - `highlight_reel_count`: Highlights count   - `edge_owner_to_timeline_media`: Timeline media (contains recent 12 posts)   - `status`: Request status   - `attempts`: Retry attempts ### Price: - 0.001 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: Instagram用户名/Instagram username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_user_info_by_username_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get(self, username, **kwargs):  # noqa: E501
        """根据用户名获取用户数据V3/Get user data by username V3  # noqa: E501

        # [中文] ### 用途: - 根据Instagram用户名获取用户数据，返回更详细的信息 ### 参数: - username: Instagram用户名 ### 返回: - 用户信息对象，包含以下主要字段：   - `pk/id`: 用户ID   - `username`: 用户名   - `full_name`: 用户全名   - `biography`: 个人简介   - `bio_links`: 个人简介链接列表   - `follower_count`: 粉丝数   - `following_count`: 关注数   - `media_count`: 媒体数量   - `profile_pic_url`: 头像URL   - `hd_profile_pic_url_info`: 高清头像URL信息   - `is_private`: 是否私密账户   - `is_verified`: 是否已认证 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user data by Instagram username with more details ### Parameters: - username: Instagram username ### Return: - User information object with main fields:   - `pk/id`: User ID   - `username`: Username   - `full_name`: Full name   - `biography`: Bio   - `bio_links`: Bio links list   - `follower_count`: Followers count   - `following_count`: Following count   - `media_count`: Media count   - `profile_pic_url`: Profile picture URL   - `hd_profile_pic_url_info`: HD profile picture URL info   - `is_private`: Whether account is private   - `is_verified`: Whether account is verified ### Price: - 0.001 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: Instagram用户名/Instagram username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """根据用户名获取用户数据V3/Get user data by username V3  # noqa: E501

        # [中文] ### 用途: - 根据Instagram用户名获取用户数据，返回更详细的信息 ### 参数: - username: Instagram用户名 ### 返回: - 用户信息对象，包含以下主要字段：   - `pk/id`: 用户ID   - `username`: 用户名   - `full_name`: 用户全名   - `biography`: 个人简介   - `bio_links`: 个人简介链接列表   - `follower_count`: 粉丝数   - `following_count`: 关注数   - `media_count`: 媒体数量   - `profile_pic_url`: 头像URL   - `hd_profile_pic_url_info`: 高清头像URL信息   - `is_private`: 是否私密账户   - `is_verified`: 是否已认证 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user data by Instagram username with more details ### Parameters: - username: Instagram username ### Return: - User information object with main fields:   - `pk/id`: User ID   - `username`: Username   - `full_name`: Full name   - `biography`: Bio   - `bio_links`: Bio links list   - `follower_count`: Followers count   - `following_count`: Following count   - `media_count`: Media count   - `profile_pic_url`: Profile picture URL   - `hd_profile_pic_url_info`: HD profile picture URL info   - `is_private`: Whether account is private   - `is_verified`: Whether account is verified ### Price: - 0.001 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: Instagram用户名/Instagram username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_user_info_by_username_v3', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户帖子列表/Get user posts list  # noqa: E501

        # [中文] ### 用途: - 获取用户帖子列表，支持分页 ### 参数: - user_id: Instagram用户ID - count: 每页数量，默认12 - max_id: 分页游标，首次请求不传 ### 返回: - `items`: 帖子列表 - `more_available`: 是否有更多数据 - `next_max_id`: 下一页游标 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user posts list with pagination support ### Parameters: - user_id: Instagram user ID - count: Count per page, default 12 - max_id: Pagination cursor, omit for first request ### Return: - `items`: Posts list - `more_available`: Whether more data available - `next_max_id`: Next page cursor ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :param object count: 每页数量/Count per page
        :param object max_id: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户帖子列表/Get user posts list  # noqa: E501

        # [中文] ### 用途: - 获取用户帖子列表，支持分页 ### 参数: - user_id: Instagram用户ID - count: 每页数量，默认12 - max_id: 分页游标，首次请求不传 ### 返回: - `items`: 帖子列表 - `more_available`: 是否有更多数据 - `next_max_id`: 下一页游标 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user posts list with pagination support ### Parameters: - user_id: Instagram user ID - count: Count per page, default 12 - max_id: Pagination cursor, omit for first request ### Return: - `items`: Posts list - `more_available`: Whether more data available - `next_max_id`: Next page cursor ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :param object count: 每页数量/Count per page
        :param object max_id: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'count', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_user_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户帖子列表V2/Get user posts list V2  # noqa: E501

        # [中文] ### 用途: - 获取用户帖子列表，支持分页 ### 参数: - user_id: Instagram用户ID - count: 每页数量，默认12 - end_cursor: 分页游标，首次请求不传 ### 返回: - GraphQL风格响应，包含`data.user.edge_owner_to_timeline_media` ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user posts list with pagination ### Parameters: - user_id: Instagram user ID - count: Count per page, default 12 - end_cursor: Pagination cursor, omit for first request ### Return: - GraphQL style response with `data.user.edge_owner_to_timeline_media` ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :param object count: 每页数量/Count per page
        :param object end_cursor: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户帖子列表V2/Get user posts list V2  # noqa: E501

        # [中文] ### 用途: - 获取用户帖子列表，支持分页 ### 参数: - user_id: Instagram用户ID - count: 每页数量，默认12 - end_cursor: 分页游标，首次请求不传 ### 返回: - GraphQL风格响应，包含`data.user.edge_owner_to_timeline_media` ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user posts list with pagination ### Parameters: - user_id: Instagram user ID - count: Count per page, default 12 - end_cursor: Pagination cursor, omit for first request ### Return: - GraphQL style response with `data.user.edge_owner_to_timeline_media` ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :param object count: 每页数量/Count per page
        :param object end_cursor: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'count', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_user_posts_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户Reels列表/Get user Reels list  # noqa: E501

        # [中文] ### 用途: - 获取用户Reels短视频列表，支持分页 ### 参数: - user_id: Instagram用户ID - count: 每页数量，默认12 - max_id: 分页游标，首次请求不传 ### 返回: - `items`: Reels列表 - `paging_info`: 分页信息 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user Reels list with pagination ### Parameters: - user_id: Instagram user ID - count: Count per page, default 12 - max_id: Pagination cursor, omit for first request ### Return: - `items`: Reels list - `paging_info`: Pagination info ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :param object count: 每页数量/Count per page
        :param object max_id: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户Reels列表/Get user Reels list  # noqa: E501

        # [中文] ### 用途: - 获取用户Reels短视频列表，支持分页 ### 参数: - user_id: Instagram用户ID - count: 每页数量，默认12 - max_id: 分页游标，首次请求不传 ### 返回: - `items`: Reels列表 - `paging_info`: 分页信息 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user Reels list with pagination ### Parameters: - user_id: Instagram user ID - count: Count per page, default 12 - max_id: Pagination cursor, omit for first request ### Return: - `items`: Reels list - `paging_info`: Pagination info ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :param object count: 每页数量/Count per page
        :param object max_id: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'count', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_user_reels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户转发列表/Get user reposts list  # noqa: E501

        # [中文] ### 用途: - 获取用户转发/分享的帖子列表，支持分页 ### 参数: - user_id: Instagram用户ID - max_id: 分页游标，首次请求不传 ### 返回: - `items`: 转发帖子列表 - `more_available`: 是否有更多数据 - `next_max_id`: 下一页游标 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user reposts/shares list with pagination ### Parameters: - user_id: Instagram user ID - max_id: Pagination cursor, omit for first request ### Return: - `items`: Reposts list - `more_available`: Whether more data available - `next_max_id`: Next page cursor ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :param object max_id: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户转发列表/Get user reposts list  # noqa: E501

        # [中文] ### 用途: - 获取用户转发/分享的帖子列表，支持分页 ### 参数: - user_id: Instagram用户ID - max_id: 分页游标，首次请求不传 ### 返回: - `items`: 转发帖子列表 - `more_available`: 是否有更多数据 - `next_max_id`: 下一页游标 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user reposts/shares list with pagination ### Parameters: - user_id: Instagram user ID - max_id: Pagination cursor, omit for first request ### Return: - `items`: Reposts list - `more_available`: Whether more data available - `next_max_id`: Next page cursor ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :param object max_id: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_user_reposts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户被标记的帖子/Get user tagged posts  # noqa: E501

        # [中文] ### 用途: - 获取其他用户帖子中标记了该用户的帖子列表 ### 参数: - user_id: Instagram用户ID - count: 每页数量，默认12 - end_cursor: 分页游标，首次请求不传 ### 返回: - GraphQL风格响应，包含`data.user.edge_user_to_photos_of_you` ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get posts where this user is tagged by others ### Parameters: - user_id: Instagram user ID - count: Count per page, default 12 - end_cursor: Pagination cursor, omit for first request ### Return: - GraphQL style response with `data.user.edge_user_to_photos_of_you` ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :param object count: 每页数量/Count per page
        :param object end_cursor: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户被标记的帖子/Get user tagged posts  # noqa: E501

        # [中文] ### 用途: - 获取其他用户帖子中标记了该用户的帖子列表 ### 参数: - user_id: Instagram用户ID - count: 每页数量，默认12 - end_cursor: 分页游标，首次请求不传 ### 返回: - GraphQL风格响应，包含`data.user.edge_user_to_photos_of_you` ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get posts where this user is tagged by others ### Parameters: - user_id: Instagram user ID - count: Count per page, default 12 - end_cursor: Pagination cursor, omit for first request ### Return: - GraphQL style response with `data.user.edge_user_to_photos_of_you` ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"25025320\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: Instagram用户ID/Instagram user ID (required)
        :param object count: 每页数量/Count per page
        :param object end_cursor: 分页游标，用于获取下一页/Pagination cursor for next page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'count', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/fetch_user_tagged_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get(self, media_id, **kwargs):  # noqa: E501
        """Media ID转Shortcode/Convert media ID to shortcode  # noqa: E501

        # [中文] ### 用途: - 将Instagram帖子的Media ID转换为Shortcode - Shortcode可用于构建帖子URL：instagram.com/p/{shortcode}/ ### 参数: - media_id: 帖子的Media ID ### 返回: - `status`: 转换状态 - `media_id`: 原始Media ID - `shortcode`: 转换后的Shortcode ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Convert Instagram post media ID to shortcode - Shortcode can be used to construct post URL: instagram.com/p/{shortcode}/ ### Parameters: - media_id: Post media ID ### Return: - `status`: Conversion status - `media_id`: Original media ID - `shortcode`: Converted shortcode ### Price: - 0.001 USD/request  # [示例/Example] media_id = \"3774507992167247878\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get(media_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子Media ID/Post media ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get_with_http_info(media_id, **kwargs)  # noqa: E501
        else:
            (data) = self.media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get_with_http_info(media_id, **kwargs)  # noqa: E501
            return data

    def media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get_with_http_info(self, media_id, **kwargs):  # noqa: E501
        """Media ID转Shortcode/Convert media ID to shortcode  # noqa: E501

        # [中文] ### 用途: - 将Instagram帖子的Media ID转换为Shortcode - Shortcode可用于构建帖子URL：instagram.com/p/{shortcode}/ ### 参数: - media_id: 帖子的Media ID ### 返回: - `status`: 转换状态 - `media_id`: 原始Media ID - `shortcode`: 转换后的Shortcode ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Convert Instagram post media ID to shortcode - Shortcode can be used to construct post URL: instagram.com/p/{shortcode}/ ### Parameters: - media_id: Post media ID ### Return: - `status`: Conversion status - `media_id`: Original media ID - `shortcode`: Converted shortcode ### Price: - 0.001 USD/request  # [示例/Example] media_id = \"3774507992167247878\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get_with_http_info(media_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子Media ID/Post media ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['media_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'media_id' is set
        if self.api_client.client_side_validation and ('media_id' not in params or
                                                       params['media_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `media_id` when calling `media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'media_id' in params:
            query_params.append(('media_id', params['media_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/media_id_to_shortcode', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get(self, shortcode, **kwargs):  # noqa: E501
        """Shortcode转Media ID/Convert shortcode to media ID  # noqa: E501

        # [中文] ### 用途: - 将Instagram帖子的Shortcode转换为Media ID - Shortcode是帖子URL中的唯一标识，如 instagram.com/p/DRhvwVLAHAG/ 中的 DRhvwVLAHAG ### 参数: - shortcode: 帖子的Shortcode ### 返回: - `status`: 转换状态 - `shortcode`: 原始Shortcode - `media_id`: 转换后的Media ID ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Convert Instagram post shortcode to media ID - Shortcode is the unique identifier in post URL, e.g., DRhvwVLAHAG in instagram.com/p/DRhvwVLAHAG/ ### Parameters: - shortcode: Post shortcode ### Return: - `status`: Conversion status - `shortcode`: Original shortcode - `media_id`: Converted media ID ### Price: - 0.001 USD/request  # [示例/Example] shortcode = \"DRhvwVLAHAG\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get(shortcode, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object shortcode: 帖子Shortcode/Post shortcode (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get_with_http_info(shortcode, **kwargs)  # noqa: E501
        else:
            (data) = self.shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get_with_http_info(shortcode, **kwargs)  # noqa: E501
            return data

    def shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get_with_http_info(self, shortcode, **kwargs):  # noqa: E501
        """Shortcode转Media ID/Convert shortcode to media ID  # noqa: E501

        # [中文] ### 用途: - 将Instagram帖子的Shortcode转换为Media ID - Shortcode是帖子URL中的唯一标识，如 instagram.com/p/DRhvwVLAHAG/ 中的 DRhvwVLAHAG ### 参数: - shortcode: 帖子的Shortcode ### 返回: - `status`: 转换状态 - `shortcode`: 原始Shortcode - `media_id`: 转换后的Media ID ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Convert Instagram post shortcode to media ID - Shortcode is the unique identifier in post URL, e.g., DRhvwVLAHAG in instagram.com/p/DRhvwVLAHAG/ ### Parameters: - shortcode: Post shortcode ### Return: - `status`: Conversion status - `shortcode`: Original shortcode - `media_id`: Converted media ID ### Price: - 0.001 USD/request  # [示例/Example] shortcode = \"DRhvwVLAHAG\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get_with_http_info(shortcode, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object shortcode: 帖子Shortcode/Post shortcode (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shortcode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shortcode' is set
        if self.api_client.client_side_validation and ('shortcode' not in params or
                                                       params['shortcode'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `shortcode` when calling `shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'shortcode' in params:
            query_params.append(('shortcode', params['shortcode']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v1/shortcode_to_media_id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_id_to_username_api_v1_instagram_v1_user_id_to_username_get(self, user_id, **kwargs):  # noqa: E501
        """用户ID转用户信息/Get user info by user ID  # noqa: E501

        # [中文] ### 用途: - 通过Instagram用户ID获取用户信息 - 可用于将用户ID转换为用户名及获取完整用户资料 ### 参数: - user_id: 用户ID ### 返回: - `pk`/`pk_id`: 用户ID - `username`: 用户名 - `full_name`: 用户全名 - `is_private`: 是否私密账户 - `is_verified`: 是否已认证 - `profile_pic_url`: 头像URL - `biography`: 个人简介 - `follower_count`: 粉丝数 - `following_count`: 关注数 - `media_count`: 帖子数 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user info by Instagram user ID - Can be used to convert user ID to username and get full profile ### Parameters: - user_id: User ID ### Return: - `pk`/`pk_id`: User ID - `username`: Username - `full_name`: Full name - `is_private`: Whether account is private - `is_verified`: Whether account is verified - `profile_pic_url`: Profile picture URL - `biography`: Bio - `follower_count`: Followers count - `following_count`: Following count - `media_count`: Posts count ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"18527\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_id_to_username_api_v1_instagram_v1_user_id_to_username_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_id_to_username_api_v1_instagram_v1_user_id_to_username_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.user_id_to_username_api_v1_instagram_v1_user_id_to_username_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def user_id_to_username_api_v1_instagram_v1_user_id_to_username_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """用户ID转用户信息/Get user info by user ID  # noqa: E501

        # [中文] ### 用途: - 通过Instagram用户ID获取用户信息 - 可用于将用户ID转换为用户名及获取完整用户资料 ### 参数: - user_id: 用户ID ### 返回: - `pk`/`pk_id`: 用户ID - `username`: 用户名 - `full_name`: 用户全名 - `is_private`: 是否私密账户 - `is_verified`: 是否已认证 - `profile_pic_url`: 头像URL - `biography`: 个人简介 - `follower_count`: 粉丝数 - `following_count`: 关注数 - `media_count`: 帖子数 ### 价格: - 0.001 USD/请求  # [English] ### Purpose: - Get user info by Instagram user ID - Can be used to convert user ID to username and get full profile ### Parameters: - user_id: User ID ### Return: - `pk`/`pk_id`: User ID - `username`: Username - `full_name`: Full name - `is_private`: Whether account is private - `is_verified`: Whether account is verified - `profile_pic_url`: Profile picture URL - `biography`: Bio - `follower_count`: Followers count - `following_count`: Following count - `media_count`: Posts count ### Price: - 0.001 USD/request  # [示例/Example] user_id = \"18527\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_id_to_username_api_v1_instagram_v1_user_id_to_username_get_with_http_info(user_id, async_req=True)
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
                    " to method user_id_to_username_api_v1_instagram_v1_user_id_to_username_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `user_id_to_username_api_v1_instagram_v1_user_id_to_username_get`")  # noqa: E501

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
            '/api/v1/instagram/v1/user_id_to_username', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
