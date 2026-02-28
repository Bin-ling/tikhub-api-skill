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


class InstagramV2APIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get(self, code_or_url, comment_id, **kwargs):  # noqa: E501
        """获取评论回复/Get comment replies  # noqa: E501

        # [中文] ### 用途: - 获取评论的回复列表 - 需要先通过fetch_post_comments获取评论ID - 支持分页获取 ### 参数: - code_or_url: 帖子Shortcode或完整URL - comment_id: 评论ID - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 回复列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of replies to a comment - Need to get comment ID from fetch_post_comments first - Support pagination ### Parameters: - code_or_url: Post shortcode or full URL - comment_id: Comment ID - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of replies - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] code_or_url = \"DRhvwVLAHAG\" comment_id = \"18067775592012345\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get(code_or_url, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code_or_url: 帖子Shortcode或URL/Post shortcode or URL (required)
        :param object comment_id: 评论ID/Comment ID (required)
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get_with_http_info(code_or_url, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get_with_http_info(code_or_url, comment_id, **kwargs)  # noqa: E501
            return data

    def fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get_with_http_info(self, code_or_url, comment_id, **kwargs):  # noqa: E501
        """获取评论回复/Get comment replies  # noqa: E501

        # [中文] ### 用途: - 获取评论的回复列表 - 需要先通过fetch_post_comments获取评论ID - 支持分页获取 ### 参数: - code_or_url: 帖子Shortcode或完整URL - comment_id: 评论ID - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 回复列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of replies to a comment - Need to get comment ID from fetch_post_comments first - Support pagination ### Parameters: - code_or_url: Post shortcode or full URL - comment_id: Comment ID - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of replies - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] code_or_url = \"DRhvwVLAHAG\" comment_id = \"18067775592012345\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get_with_http_info(code_or_url, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code_or_url: 帖子Shortcode或URL/Post shortcode or URL (required)
        :param object comment_id: 评论ID/Comment ID (required)
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_or_url', 'comment_id', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code_or_url' is set
        if self.api_client.client_side_validation and ('code_or_url' not in params or
                                                       params['code_or_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `code_or_url` when calling `fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code_or_url' in params:
            query_params.append(('code_or_url', params['code_or_url']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_comment_replies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hashtag_posts_api_v1_instagram_v2_fetch_hashtag_posts_get(self, keyword, **kwargs):  # noqa: E501
        """获取话题帖子/Get hashtag posts  # noqa: E501

        # [中文] ### 用途: - 获取指定话题标签下的帖子列表 - 支持按热门、最新或仅Reels筛选 - 支持分页获取 ### 参数: - keyword: 话题关键词（不含#号） - feed_type: 帖子类型，\"top\"（热门）、\"recent\"（最新）或\"reels\"（仅Reels），默认top - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 帖子列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get posts under specified hashtag - Support filtering by top, recent, or reels only - Support pagination ### Parameters: - keyword: Hashtag keyword (without #) - feed_type: Feed type \"top\", \"recent\", or \"reels\", default top - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of posts - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"cat\" feed_type = \"top\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_posts_api_v1_instagram_v2_fetch_hashtag_posts_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 话题关键词（不含#号）/Hashtag keyword (without #) (required)
        :param object feed_type: 帖子类型: top(热门), recent(最新), reels(仅Reels)/Feed type: top, recent, or reels
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hashtag_posts_api_v1_instagram_v2_fetch_hashtag_posts_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hashtag_posts_api_v1_instagram_v2_fetch_hashtag_posts_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_hashtag_posts_api_v1_instagram_v2_fetch_hashtag_posts_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取话题帖子/Get hashtag posts  # noqa: E501

        # [中文] ### 用途: - 获取指定话题标签下的帖子列表 - 支持按热门、最新或仅Reels筛选 - 支持分页获取 ### 参数: - keyword: 话题关键词（不含#号） - feed_type: 帖子类型，\"top\"（热门）、\"recent\"（最新）或\"reels\"（仅Reels），默认top - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 帖子列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get posts under specified hashtag - Support filtering by top, recent, or reels only - Support pagination ### Parameters: - keyword: Hashtag keyword (without #) - feed_type: Feed type \"top\", \"recent\", or \"reels\", default top - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of posts - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"cat\" feed_type = \"top\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_posts_api_v1_instagram_v2_fetch_hashtag_posts_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 话题关键词（不含#号）/Hashtag keyword (without #) (required)
        :param object feed_type: 帖子类型: top(热门), recent(最新), reels(仅Reels)/Feed type: top, recent, or reels
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'feed_type', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hashtag_posts_api_v1_instagram_v2_fetch_hashtag_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_hashtag_posts_api_v1_instagram_v2_fetch_hashtag_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'feed_type' in params:
            query_params.append(('feed_type', params['feed_type']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_hashtag_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_highlight_stories_api_v1_instagram_v2_fetch_highlight_stories_get(self, highlight_id, **kwargs):  # noqa: E501
        """获取精选故事详情/Get highlight stories  # noqa: E501

        # [中文] ### 用途: - 获取指定精选（Highlight）中的所有故事 - 需要先通过fetch_user_highlights获取精选ID ### 参数: - highlight_id: 精选ID（可带或不带\"highlight:\"前缀） ### 返回: - `data.items`: 故事列表，包含图片/视频URL、发布时间等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get all stories in a specific highlight - Need to get highlight ID from fetch_user_highlights first ### Parameters: - highlight_id: Highlight ID (with or without \"highlight:\" prefix) ### Return: - `data.items`: List of stories with image/video URLs, publish time, etc. ### Price: - 0.002 USD/request  # [示例/Example] highlight_id = \"17895069621772257\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_highlight_stories_api_v1_instagram_v2_fetch_highlight_stories_get(highlight_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object highlight_id: 精选ID/Highlight ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_highlight_stories_api_v1_instagram_v2_fetch_highlight_stories_get_with_http_info(highlight_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_highlight_stories_api_v1_instagram_v2_fetch_highlight_stories_get_with_http_info(highlight_id, **kwargs)  # noqa: E501
            return data

    def fetch_highlight_stories_api_v1_instagram_v2_fetch_highlight_stories_get_with_http_info(self, highlight_id, **kwargs):  # noqa: E501
        """获取精选故事详情/Get highlight stories  # noqa: E501

        # [中文] ### 用途: - 获取指定精选（Highlight）中的所有故事 - 需要先通过fetch_user_highlights获取精选ID ### 参数: - highlight_id: 精选ID（可带或不带\"highlight:\"前缀） ### 返回: - `data.items`: 故事列表，包含图片/视频URL、发布时间等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get all stories in a specific highlight - Need to get highlight ID from fetch_user_highlights first ### Parameters: - highlight_id: Highlight ID (with or without \"highlight:\" prefix) ### Return: - `data.items`: List of stories with image/video URLs, publish time, etc. ### Price: - 0.002 USD/request  # [示例/Example] highlight_id = \"17895069621772257\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_highlight_stories_api_v1_instagram_v2_fetch_highlight_stories_get_with_http_info(highlight_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object highlight_id: 精选ID/Highlight ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['highlight_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_highlight_stories_api_v1_instagram_v2_fetch_highlight_stories_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'highlight_id' is set
        if self.api_client.client_side_validation and ('highlight_id' not in params or
                                                       params['highlight_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `highlight_id` when calling `fetch_highlight_stories_api_v1_instagram_v2_fetch_highlight_stories_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'highlight_id' in params:
            query_params.append(('highlight_id', params['highlight_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_highlight_stories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_location_posts_api_v1_instagram_v2_fetch_location_posts_get(self, location_id, **kwargs):  # noqa: E501
        """获取地点帖子/Get location posts  # noqa: E501

        # [中文] ### 用途: - 获取指定地点的帖子列表 - 地点ID可通过search_locations获取 - 支持分页获取 ### 参数: - location_id: 地点ID - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 帖子列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get posts at specified location - Location ID can be obtained from search_locations - Support pagination ### Parameters: - location_id: Location ID - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of posts - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] location_id = \"331004901\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_location_posts_api_v1_instagram_v2_fetch_location_posts_get(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object location_id: 地点ID/Location ID (required)
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_location_posts_api_v1_instagram_v2_fetch_location_posts_get_with_http_info(location_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_location_posts_api_v1_instagram_v2_fetch_location_posts_get_with_http_info(location_id, **kwargs)  # noqa: E501
            return data

    def fetch_location_posts_api_v1_instagram_v2_fetch_location_posts_get_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """获取地点帖子/Get location posts  # noqa: E501

        # [中文] ### 用途: - 获取指定地点的帖子列表 - 地点ID可通过search_locations获取 - 支持分页获取 ### 参数: - location_id: 地点ID - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 帖子列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get posts at specified location - Location ID can be obtained from search_locations - Support pagination ### Parameters: - location_id: Location ID - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of posts - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] location_id = \"331004901\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_location_posts_api_v1_instagram_v2_fetch_location_posts_get_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object location_id: 地点ID/Location ID (required)
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_location_posts_api_v1_instagram_v2_fetch_location_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in params or
                                                       params['location_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `location_id` when calling `fetch_location_posts_api_v1_instagram_v2_fetch_location_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'location_id' in params:
            query_params.append(('location_id', params['location_id']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_location_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_music_posts_api_v1_instagram_v2_fetch_music_posts_get(self, audio_canonical_id, **kwargs):  # noqa: E501
        """获取音乐帖子/Get music posts  # noqa: E501

        # [中文] ### 用途: - 获取使用指定音乐的帖子列表 - 音频ID可从帖子详情中获取 - 支持分页获取 ### 参数: - audio_canonical_id: 音频ID - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 帖子列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get posts using specified music - Audio ID can be obtained from post details - Support pagination ### Parameters: - audio_canonical_id: Audio ID - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of posts - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] audio_canonical_id = \"564058920086577\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_posts_api_v1_instagram_v2_fetch_music_posts_get(audio_canonical_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object audio_canonical_id: 音频ID/Audio ID (required)
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_music_posts_api_v1_instagram_v2_fetch_music_posts_get_with_http_info(audio_canonical_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_music_posts_api_v1_instagram_v2_fetch_music_posts_get_with_http_info(audio_canonical_id, **kwargs)  # noqa: E501
            return data

    def fetch_music_posts_api_v1_instagram_v2_fetch_music_posts_get_with_http_info(self, audio_canonical_id, **kwargs):  # noqa: E501
        """获取音乐帖子/Get music posts  # noqa: E501

        # [中文] ### 用途: - 获取使用指定音乐的帖子列表 - 音频ID可从帖子详情中获取 - 支持分页获取 ### 参数: - audio_canonical_id: 音频ID - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 帖子列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get posts using specified music - Audio ID can be obtained from post details - Support pagination ### Parameters: - audio_canonical_id: Audio ID - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of posts - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] audio_canonical_id = \"564058920086577\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_posts_api_v1_instagram_v2_fetch_music_posts_get_with_http_info(audio_canonical_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object audio_canonical_id: 音频ID/Audio ID (required)
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['audio_canonical_id', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_music_posts_api_v1_instagram_v2_fetch_music_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'audio_canonical_id' is set
        if self.api_client.client_side_validation and ('audio_canonical_id' not in params or
                                                       params['audio_canonical_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `audio_canonical_id` when calling `fetch_music_posts_api_v1_instagram_v2_fetch_music_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'audio_canonical_id' in params:
            query_params.append(('audio_canonical_id', params['audio_canonical_id']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_music_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_comments_api_v1_instagram_v2_fetch_post_comments_get(self, code_or_url, **kwargs):  # noqa: E501
        """获取帖子评论/Get post comments  # noqa: E501

        # [中文] ### 用途: - 获取帖子的评论列表 - 支持按最新或热门排序 - 支持分页获取 ### 参数: - code_or_url: 帖子Shortcode或完整URL - sort_by: 排序方式，\"recent\"（最新）或\"popular\"（热门），默认recent - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 评论列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of comments on the post - Support sorting by recent or popular - Support pagination ### Parameters: - code_or_url: Post shortcode or full URL - sort_by: Sort by \"recent\" or \"popular\", default recent - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of comments - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] code_or_url = \"DRhvwVLAHAG\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_instagram_v2_fetch_post_comments_get(code_or_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code_or_url: 帖子Shortcode或URL/Post shortcode or URL (required)
        :param object sort_by: 排序方式: recent(最新) 或 popular(热门)/Sort by: recent or popular
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comments_api_v1_instagram_v2_fetch_post_comments_get_with_http_info(code_or_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comments_api_v1_instagram_v2_fetch_post_comments_get_with_http_info(code_or_url, **kwargs)  # noqa: E501
            return data

    def fetch_post_comments_api_v1_instagram_v2_fetch_post_comments_get_with_http_info(self, code_or_url, **kwargs):  # noqa: E501
        """获取帖子评论/Get post comments  # noqa: E501

        # [中文] ### 用途: - 获取帖子的评论列表 - 支持按最新或热门排序 - 支持分页获取 ### 参数: - code_or_url: 帖子Shortcode或完整URL - sort_by: 排序方式，\"recent\"（最新）或\"popular\"（热门），默认recent - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 评论列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of comments on the post - Support sorting by recent or popular - Support pagination ### Parameters: - code_or_url: Post shortcode or full URL - sort_by: Sort by \"recent\" or \"popular\", default recent - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of comments - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] code_or_url = \"DRhvwVLAHAG\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_instagram_v2_fetch_post_comments_get_with_http_info(code_or_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code_or_url: 帖子Shortcode或URL/Post shortcode or URL (required)
        :param object sort_by: 排序方式: recent(最新) 或 popular(热门)/Sort by: recent or popular
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_or_url', 'sort_by', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comments_api_v1_instagram_v2_fetch_post_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code_or_url' is set
        if self.api_client.client_side_validation and ('code_or_url' not in params or
                                                       params['code_or_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `code_or_url` when calling `fetch_post_comments_api_v1_instagram_v2_fetch_post_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code_or_url' in params:
            query_params.append(('code_or_url', params['code_or_url']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_post_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_info_api_v1_instagram_v2_fetch_post_info_get(self, code_or_url, **kwargs):  # noqa: E501
        """获取帖子详情/Get post info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram帖子的详细信息 - 支持Shortcode或完整URL ### 参数: - code_or_url: 帖子Shortcode或完整URL ### 返回: - `data`: 帖子详情，包含媒体资源、描述、点赞数、评论数等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get detailed information of Instagram post - Support shortcode or full URL ### Parameters: - code_or_url: Post shortcode or full URL ### Return: - `data`: Post details including media, caption, likes, comments, etc. ### Price: - 0.002 USD/request  # [示例/Example] code_or_url = \"DRhvwVLAHAG\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_info_api_v1_instagram_v2_fetch_post_info_get(code_or_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code_or_url: 帖子Shortcode或URL/Post shortcode or URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_info_api_v1_instagram_v2_fetch_post_info_get_with_http_info(code_or_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_info_api_v1_instagram_v2_fetch_post_info_get_with_http_info(code_or_url, **kwargs)  # noqa: E501
            return data

    def fetch_post_info_api_v1_instagram_v2_fetch_post_info_get_with_http_info(self, code_or_url, **kwargs):  # noqa: E501
        """获取帖子详情/Get post info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram帖子的详细信息 - 支持Shortcode或完整URL ### 参数: - code_or_url: 帖子Shortcode或完整URL ### 返回: - `data`: 帖子详情，包含媒体资源、描述、点赞数、评论数等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get detailed information of Instagram post - Support shortcode or full URL ### Parameters: - code_or_url: Post shortcode or full URL ### Return: - `data`: Post details including media, caption, likes, comments, etc. ### Price: - 0.002 USD/request  # [示例/Example] code_or_url = \"DRhvwVLAHAG\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_info_api_v1_instagram_v2_fetch_post_info_get_with_http_info(code_or_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code_or_url: 帖子Shortcode或URL/Post shortcode or URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_or_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_info_api_v1_instagram_v2_fetch_post_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code_or_url' is set
        if self.api_client.client_side_validation and ('code_or_url' not in params or
                                                       params['code_or_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `code_or_url` when calling `fetch_post_info_api_v1_instagram_v2_fetch_post_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code_or_url' in params:
            query_params.append(('code_or_url', params['code_or_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_post_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_likes_api_v1_instagram_v2_fetch_post_likes_get(self, code_or_url, **kwargs):  # noqa: E501
        """获取帖子点赞列表/Get post likes  # noqa: E501

        # [中文] ### 用途: - 获取帖子的点赞用户列表 - 支持分页获取 ### 参数: - code_or_url: 帖子Shortcode或完整URL - end_cursor: 分页游标，从上一次响应获取 ### 返回: - `data.items`: 点赞用户列表 - `end_cursor`: 下一页游标 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of users who liked the post - Support pagination ### Parameters: - code_or_url: Post shortcode or full URL - end_cursor: Pagination cursor from previous response ### Return: - `data.items`: List of users who liked - `end_cursor`: Next page cursor ### Price: - 0.002 USD/request  # [示例/Example] code_or_url = \"DRhvwVLAHAG\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_likes_api_v1_instagram_v2_fetch_post_likes_get(code_or_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code_or_url: 帖子Shortcode或URL/Post shortcode or URL (required)
        :param object end_cursor: 分页游标/Pagination cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_likes_api_v1_instagram_v2_fetch_post_likes_get_with_http_info(code_or_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_likes_api_v1_instagram_v2_fetch_post_likes_get_with_http_info(code_or_url, **kwargs)  # noqa: E501
            return data

    def fetch_post_likes_api_v1_instagram_v2_fetch_post_likes_get_with_http_info(self, code_or_url, **kwargs):  # noqa: E501
        """获取帖子点赞列表/Get post likes  # noqa: E501

        # [中文] ### 用途: - 获取帖子的点赞用户列表 - 支持分页获取 ### 参数: - code_or_url: 帖子Shortcode或完整URL - end_cursor: 分页游标，从上一次响应获取 ### 返回: - `data.items`: 点赞用户列表 - `end_cursor`: 下一页游标 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of users who liked the post - Support pagination ### Parameters: - code_or_url: Post shortcode or full URL - end_cursor: Pagination cursor from previous response ### Return: - `data.items`: List of users who liked - `end_cursor`: Next page cursor ### Price: - 0.002 USD/request  # [示例/Example] code_or_url = \"DRhvwVLAHAG\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_likes_api_v1_instagram_v2_fetch_post_likes_get_with_http_info(code_or_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code_or_url: 帖子Shortcode或URL/Post shortcode or URL (required)
        :param object end_cursor: 分页游标/Pagination cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_or_url', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_likes_api_v1_instagram_v2_fetch_post_likes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code_or_url' is set
        if self.api_client.client_side_validation and ('code_or_url' not in params or
                                                       params['code_or_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `code_or_url` when calling `fetch_post_likes_api_v1_instagram_v2_fetch_post_likes_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code_or_url' in params:
            query_params.append(('code_or_url', params['code_or_url']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_post_likes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_similar_users_api_v1_instagram_v2_fetch_similar_users_get(self, **kwargs):  # noqa: E501
        """获取相似用户/Get similar users  # noqa: E501

        # [中文] ### 用途: - 获取与指定用户相似的用户推荐列表 - 基于Instagram的推荐算法 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） ### 返回: - `data.items`: 相似用户列表 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get recommended similar users - Based on Instagram's recommendation algorithm ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) ### Return: - `data.items`: List of similar users ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_similar_users_api_v1_instagram_v2_fetch_similar_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_similar_users_api_v1_instagram_v2_fetch_similar_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_similar_users_api_v1_instagram_v2_fetch_similar_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_similar_users_api_v1_instagram_v2_fetch_similar_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取相似用户/Get similar users  # noqa: E501

        # [中文] ### 用途: - 获取与指定用户相似的用户推荐列表 - 基于Instagram的推荐算法 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） ### 返回: - `data.items`: 相似用户列表 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get recommended similar users - Based on Instagram's recommendation algorithm ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) ### Return: - `data.items`: List of similar users ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_similar_users_api_v1_instagram_v2_fetch_similar_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_similar_users_api_v1_instagram_v2_fetch_similar_users_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_similar_users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_followers_api_v1_instagram_v2_fetch_user_followers_get(self, **kwargs):  # noqa: E501
        """获取用户粉丝/Get user followers  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的粉丝列表 - 支持分页获取 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 粉丝列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of followers of Instagram user - Support pagination ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of followers - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_followers_api_v1_instagram_v2_fetch_user_followers_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_followers_api_v1_instagram_v2_fetch_user_followers_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_followers_api_v1_instagram_v2_fetch_user_followers_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_followers_api_v1_instagram_v2_fetch_user_followers_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户粉丝/Get user followers  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的粉丝列表 - 支持分页获取 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 粉丝列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of followers of Instagram user - Support pagination ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of followers - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_followers_api_v1_instagram_v2_fetch_user_followers_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'user_id', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_followers_api_v1_instagram_v2_fetch_user_followers_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_user_followers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_following_api_v1_instagram_v2_fetch_user_following_get(self, **kwargs):  # noqa: E501
        """获取用户关注/Get user following  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户关注的用户列表 - 支持分页获取 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 关注列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of users that Instagram user is following - Support pagination ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of following - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_api_v1_instagram_v2_fetch_user_following_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_following_api_v1_instagram_v2_fetch_user_following_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_following_api_v1_instagram_v2_fetch_user_following_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_following_api_v1_instagram_v2_fetch_user_following_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户关注/Get user following  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户关注的用户列表 - 支持分页获取 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 关注列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of users that Instagram user is following - Support pagination ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of following - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_api_v1_instagram_v2_fetch_user_following_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'user_id', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_following_api_v1_instagram_v2_fetch_user_following_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_user_following', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_highlights_api_v1_instagram_v2_fetch_user_highlights_get(self, **kwargs):  # noqa: E501
        """获取用户精选/Get user highlights  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的精选故事（Highlights）列表 - 精选是用户保存的故事合集 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） ### 返回: - `data.items`: 精选列表，包含精选ID、标题、封面等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's highlights list - Highlights are saved story collections ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) ### Return: - `data.items`: List of highlights with ID, title, cover, etc. ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_highlights_api_v1_instagram_v2_fetch_user_highlights_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_highlights_api_v1_instagram_v2_fetch_user_highlights_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_highlights_api_v1_instagram_v2_fetch_user_highlights_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_highlights_api_v1_instagram_v2_fetch_user_highlights_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户精选/Get user highlights  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的精选故事（Highlights）列表 - 精选是用户保存的故事合集 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） ### 返回: - `data.items`: 精选列表，包含精选ID、标题、封面等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's highlights list - Highlights are saved story collections ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) ### Return: - `data.items`: List of highlights with ID, title, cover, etc. ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_highlights_api_v1_instagram_v2_fetch_user_highlights_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_highlights_api_v1_instagram_v2_fetch_user_highlights_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_user_highlights', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_api_v1_instagram_v2_fetch_user_info_get(self, **kwargs):  # noqa: E501
        """获取用户信息/Get user info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的详细信息 - 支持通过用户名或用户ID查询 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） ### 返回: - `data`: 用户信息，包含用户名、头像、简介、粉丝数、关注数、帖子数等 - 此接口会返回用户的关于信息，包括国家，加入时间，是否认证等信息。 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get detailed Instagram user information - Support query by username or user ID ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) ### Return: - `data`: User info including username, avatar, bio, followers, following, posts count, etc. - This endpoint returns user's about info including country, join date, verification status, etc. ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_instagram_v2_fetch_user_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_instagram_v2_fetch_user_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_instagram_v2_fetch_user_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_instagram_v2_fetch_user_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户信息/Get user info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的详细信息 - 支持通过用户名或用户ID查询 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） ### 返回: - `data`: 用户信息，包含用户名、头像、简介、粉丝数、关注数、帖子数等 - 此接口会返回用户的关于信息，包括国家，加入时间，是否认证等信息。 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get detailed Instagram user information - Support query by username or user ID ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) ### Return: - `data`: User info including username, avatar, bio, followers, following, posts count, etc. - This endpoint returns user's about info including country, join date, verification status, etc. ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_instagram_v2_fetch_user_info_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_info_api_v1_instagram_v2_fetch_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_user_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_posts_api_v1_instagram_v2_fetch_user_posts_get(self, **kwargs):  # noqa: E501
        """获取用户帖子/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户发布的帖子列表 - 支持分页获取 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 帖子列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of posts published by Instagram user - Support pagination ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of posts - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_instagram_v2_fetch_user_posts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_posts_api_v1_instagram_v2_fetch_user_posts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_posts_api_v1_instagram_v2_fetch_user_posts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_posts_api_v1_instagram_v2_fetch_user_posts_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户帖子/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户发布的帖子列表 - 支持分页获取 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 帖子列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of posts published by Instagram user - Support pagination ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of posts - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_instagram_v2_fetch_user_posts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'user_id', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_posts_api_v1_instagram_v2_fetch_user_posts_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_user_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_reels_api_v1_instagram_v2_fetch_user_reels_get(self, **kwargs):  # noqa: E501
        """获取用户Reels/Get user reels  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户发布的Reels短视频列表 - 支持分页获取 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: Reels列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of Reels published by Instagram user - Support pagination ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of reels - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_reels_api_v1_instagram_v2_fetch_user_reels_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_reels_api_v1_instagram_v2_fetch_user_reels_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_reels_api_v1_instagram_v2_fetch_user_reels_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_reels_api_v1_instagram_v2_fetch_user_reels_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户Reels/Get user reels  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户发布的Reels短视频列表 - 支持分页获取 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: Reels列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get list of Reels published by Instagram user - Support pagination ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of reels - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_reels_api_v1_instagram_v2_fetch_user_reels_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'user_id', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_reels_api_v1_instagram_v2_fetch_user_reels_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_user_reels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_stories_api_v1_instagram_v2_fetch_user_stories_get(self, **kwargs):  # noqa: E501
        """获取用户故事/Get user stories  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户当前发布的故事（Stories） - 故事在24小时后过期 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） ### 返回: - `data.items`: 故事列表，包含图片/视频URL、发布时间等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get current stories published by Instagram user - Stories expire after 24 hours ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) ### Return: - `data.items`: List of stories with image/video URLs, publish time, etc. ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_stories_api_v1_instagram_v2_fetch_user_stories_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_stories_api_v1_instagram_v2_fetch_user_stories_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_stories_api_v1_instagram_v2_fetch_user_stories_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_stories_api_v1_instagram_v2_fetch_user_stories_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户故事/Get user stories  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户当前发布的故事（Stories） - 故事在24小时后过期 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） ### 返回: - `data.items`: 故事列表，包含图片/视频URL、发布时间等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get current stories published by Instagram user - Stories expire after 24 hours ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) ### Return: - `data.items`: List of stories with image/video URLs, publish time, etc. ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_stories_api_v1_instagram_v2_fetch_user_stories_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_stories_api_v1_instagram_v2_fetch_user_stories_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_user_stories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_tagged_posts_api_v1_instagram_v2_fetch_user_tagged_posts_get(self, **kwargs):  # noqa: E501
        """获取用户被标记的帖子/Get user tagged posts  # noqa: E501

        # [中文] ### 用途: - 获取其他用户标记了该用户的帖子列表 - 支持分页获取 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 帖子列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get posts where the user is tagged by others - Support pagination ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of posts - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_tagged_posts_api_v1_instagram_v2_fetch_user_tagged_posts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_tagged_posts_api_v1_instagram_v2_fetch_user_tagged_posts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_tagged_posts_api_v1_instagram_v2_fetch_user_tagged_posts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_tagged_posts_api_v1_instagram_v2_fetch_user_tagged_posts_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户被标记的帖子/Get user tagged posts  # noqa: E501

        # [中文] ### 用途: - 获取其他用户标记了该用户的帖子列表 - 支持分页获取 ### 参数: - username: 用户名（与user_id二选一） - user_id: 用户ID（与username二选一） - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 帖子列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get posts where the user is tagged by others - Support pagination ### Parameters: - username: Username (either username or user_id required) - user_id: User ID (either username or user_id required) - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of posts - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] username = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_tagged_posts_api_v1_instagram_v2_fetch_user_tagged_posts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'user_id', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_tagged_posts_api_v1_instagram_v2_fetch_user_tagged_posts_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/fetch_user_tagged_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def general_search_api_v1_instagram_v2_general_search_get(self, keyword, **kwargs):  # noqa: E501
        """综合搜索/General search  # noqa: E501

        # [中文] ### 用途: - 根据关键词进行Instagram综合搜索 - 支持分页获取 ### 参数: - keyword: 搜索关键词 - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 综合搜索结果列表，包含用户、帖子、Reels等 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Perform general search on Instagram by keyword - Support pagination ### Parameters: - keyword: Search keyword - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of general search results including users, posts, reels, etc. - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"cat\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.general_search_api_v1_instagram_v2_general_search_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.general_search_api_v1_instagram_v2_general_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.general_search_api_v1_instagram_v2_general_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def general_search_api_v1_instagram_v2_general_search_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """综合搜索/General search  # noqa: E501

        # [中文] ### 用途: - 根据关键词进行Instagram综合搜索 - 支持分页获取 ### 参数: - keyword: 搜索关键词 - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: 综合搜索结果列表，包含用户、帖子、Reels等 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Perform general search on Instagram by keyword - Support pagination ### Parameters: - keyword: Search keyword - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of general search results including users, posts, reels, etc. - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"cat\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.general_search_api_v1_instagram_v2_general_search_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method general_search_api_v1_instagram_v2_general_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `general_search_api_v1_instagram_v2_general_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/general_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_id_to_shortcode_api_v1_instagram_v2_media_id_to_shortcode_get(self, media_id, **kwargs):  # noqa: E501
        """Media ID转Shortcode/Convert media ID to shortcode  # noqa: E501

        # [中文] ### 用途: - 将Instagram帖子的Media ID转换为Shortcode - Shortcode可用于构建帖子URL：instagram.com/p/{shortcode}/ ### 参数: - media_id: 帖子的Media ID ### 返回: - `status`: 转换状态 - `media_id`: 原始Media ID - `shortcode`: 转换后的Shortcode ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Convert Instagram post media ID to shortcode - Shortcode can be used to construct post URL: instagram.com/p/{shortcode}/ ### Parameters: - media_id: Post media ID ### Return: - `status`: Conversion status - `media_id`: Original media ID - `shortcode`: Converted shortcode ### Price: - 0.002 USD/request  # [示例/Example] media_id = \"3774507992167247878\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_id_to_shortcode_api_v1_instagram_v2_media_id_to_shortcode_get(media_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子Media ID/Post media ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_id_to_shortcode_api_v1_instagram_v2_media_id_to_shortcode_get_with_http_info(media_id, **kwargs)  # noqa: E501
        else:
            (data) = self.media_id_to_shortcode_api_v1_instagram_v2_media_id_to_shortcode_get_with_http_info(media_id, **kwargs)  # noqa: E501
            return data

    def media_id_to_shortcode_api_v1_instagram_v2_media_id_to_shortcode_get_with_http_info(self, media_id, **kwargs):  # noqa: E501
        """Media ID转Shortcode/Convert media ID to shortcode  # noqa: E501

        # [中文] ### 用途: - 将Instagram帖子的Media ID转换为Shortcode - Shortcode可用于构建帖子URL：instagram.com/p/{shortcode}/ ### 参数: - media_id: 帖子的Media ID ### 返回: - `status`: 转换状态 - `media_id`: 原始Media ID - `shortcode`: 转换后的Shortcode ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Convert Instagram post media ID to shortcode - Shortcode can be used to construct post URL: instagram.com/p/{shortcode}/ ### Parameters: - media_id: Post media ID ### Return: - `status`: Conversion status - `media_id`: Original media ID - `shortcode`: Converted shortcode ### Price: - 0.002 USD/request  # [示例/Example] media_id = \"3774507992167247878\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_id_to_shortcode_api_v1_instagram_v2_media_id_to_shortcode_get_with_http_info(media_id, async_req=True)
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
                    " to method media_id_to_shortcode_api_v1_instagram_v2_media_id_to_shortcode_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'media_id' is set
        if self.api_client.client_side_validation and ('media_id' not in params or
                                                       params['media_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `media_id` when calling `media_id_to_shortcode_api_v1_instagram_v2_media_id_to_shortcode_get`")  # noqa: E501

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
            '/api/v1/instagram/v2/media_id_to_shortcode', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get(self, latitude, longitude, **kwargs):  # noqa: E501
        """根据坐标搜索地点/Search locations by coordinates  # noqa: E501

        # [中文] ### 用途: - 根据GPS坐标搜索附近的Instagram地点 ### 参数: - latitude: 纬度 - longitude: 经度 ### 返回: - `data.items`: 附近地点列表，包含名称、地址、分类等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search nearby Instagram locations by GPS coordinates ### Parameters: - latitude: Latitude - longitude: Longitude ### Return: - `data.items`: List of nearby locations with name, address, category, etc. ### Price: - 0.002 USD/request  # [示例/Example] latitude = 40.7 longitude = -74  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get(latitude, longitude, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object latitude: 纬度/Latitude (required)
        :param object longitude: 经度/Longitude (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get_with_http_info(latitude, longitude, **kwargs)  # noqa: E501
        else:
            (data) = self.search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get_with_http_info(latitude, longitude, **kwargs)  # noqa: E501
            return data

    def search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get_with_http_info(self, latitude, longitude, **kwargs):  # noqa: E501
        """根据坐标搜索地点/Search locations by coordinates  # noqa: E501

        # [中文] ### 用途: - 根据GPS坐标搜索附近的Instagram地点 ### 参数: - latitude: 纬度 - longitude: 经度 ### 返回: - `data.items`: 附近地点列表，包含名称、地址、分类等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search nearby Instagram locations by GPS coordinates ### Parameters: - latitude: Latitude - longitude: Longitude ### Return: - `data.items`: List of nearby locations with name, address, category, etc. ### Price: - 0.002 USD/request  # [示例/Example] latitude = 40.7 longitude = -74  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get_with_http_info(latitude, longitude, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object latitude: 纬度/Latitude (required)
        :param object longitude: 经度/Longitude (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['latitude', 'longitude']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'latitude' is set
        if self.api_client.client_side_validation and ('latitude' not in params or
                                                       params['latitude'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `latitude` when calling `search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get`")  # noqa: E501
        # verify the required parameter 'longitude' is set
        if self.api_client.client_side_validation and ('longitude' not in params or
                                                       params['longitude'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `longitude` when calling `search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'latitude' in params:
            query_params.append(('latitude', params['latitude']))  # noqa: E501
        if 'longitude' in params:
            query_params.append(('longitude', params['longitude']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/search_by_coordinates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_hashtags_api_v1_instagram_v2_search_hashtags_get(self, keyword, **kwargs):  # noqa: E501
        """搜索话题标签/Search hashtags  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram话题标签 ### 参数: - keyword: 搜索关键词 ### 返回: - `data.items`: 话题标签列表，包含名称、帖子数量等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search Instagram hashtags by keyword ### Parameters: - keyword: Search keyword ### Return: - `data.items`: List of hashtags with name, post count, etc. ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"cat\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_hashtags_api_v1_instagram_v2_search_hashtags_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_hashtags_api_v1_instagram_v2_search_hashtags_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_hashtags_api_v1_instagram_v2_search_hashtags_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_hashtags_api_v1_instagram_v2_search_hashtags_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索话题标签/Search hashtags  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram话题标签 ### 参数: - keyword: 搜索关键词 ### 返回: - `data.items`: 话题标签列表，包含名称、帖子数量等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search Instagram hashtags by keyword ### Parameters: - keyword: Search keyword ### Return: - `data.items`: List of hashtags with name, post count, etc. ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"cat\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_hashtags_api_v1_instagram_v2_search_hashtags_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
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
                    " to method search_hashtags_api_v1_instagram_v2_search_hashtags_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_hashtags_api_v1_instagram_v2_search_hashtags_get`")  # noqa: E501

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
            '/api/v1/instagram/v2/search_hashtags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_locations_api_v1_instagram_v2_search_locations_get(self, keyword, **kwargs):  # noqa: E501
        """搜索地点/Search locations  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram地点 ### 参数: - keyword: 搜索关键词（地点名称、城市等） ### 返回: - `data.items`: 地点列表，包含名称、地址、坐标等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search Instagram locations by keyword ### Parameters: - keyword: Search keyword (location name, city, etc.) ### Return: - `data.items`: List of locations with name, address, coordinates, etc. ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"paris\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_locations_api_v1_instagram_v2_search_locations_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_locations_api_v1_instagram_v2_search_locations_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_locations_api_v1_instagram_v2_search_locations_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_locations_api_v1_instagram_v2_search_locations_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索地点/Search locations  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram地点 ### 参数: - keyword: 搜索关键词（地点名称、城市等） ### 返回: - `data.items`: 地点列表，包含名称、地址、坐标等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search Instagram locations by keyword ### Parameters: - keyword: Search keyword (location name, city, etc.) ### Return: - `data.items`: List of locations with name, address, coordinates, etc. ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"paris\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_locations_api_v1_instagram_v2_search_locations_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
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
                    " to method search_locations_api_v1_instagram_v2_search_locations_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_locations_api_v1_instagram_v2_search_locations_get`")  # noqa: E501

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
            '/api/v1/instagram/v2/search_locations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_music_api_v1_instagram_v2_search_music_get(self, keyword, **kwargs):  # noqa: E501
        """搜索音乐/Search music  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram上可用的音乐 ### 参数: - keyword: 搜索关键词 ### 返回: - `data.items`: 音乐列表，包含标题、艺术家、时长、音频ID等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search available music on Instagram by keyword ### Parameters: - keyword: Search keyword ### Return: - `data.items`: List of music with title, artist, duration, audio ID, etc. ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"happy\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_music_api_v1_instagram_v2_search_music_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_music_api_v1_instagram_v2_search_music_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_music_api_v1_instagram_v2_search_music_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_music_api_v1_instagram_v2_search_music_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索音乐/Search music  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram上可用的音乐 ### 参数: - keyword: 搜索关键词 ### 返回: - `data.items`: 音乐列表，包含标题、艺术家、时长、音频ID等 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search available music on Instagram by keyword ### Parameters: - keyword: Search keyword ### Return: - `data.items`: List of music with title, artist, duration, audio ID, etc. ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"happy\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_music_api_v1_instagram_v2_search_music_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
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
                    " to method search_music_api_v1_instagram_v2_search_music_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_music_api_v1_instagram_v2_search_music_get`")  # noqa: E501

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
            '/api/v1/instagram/v2/search_music', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_reels_api_v1_instagram_v2_search_reels_get(self, keyword, **kwargs):  # noqa: E501
        """搜索Reels/Search reels  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram Reels短视频 - 支持分页获取 ### 参数: - keyword: 搜索关键词 - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: Reels列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search Instagram Reels by keyword - Support pagination ### Parameters: - keyword: Search keyword - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of reels - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"cat\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_reels_api_v1_instagram_v2_search_reels_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_reels_api_v1_instagram_v2_search_reels_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_reels_api_v1_instagram_v2_search_reels_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_reels_api_v1_instagram_v2_search_reels_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索Reels/Search reels  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram Reels短视频 - 支持分页获取 ### 参数: - keyword: 搜索关键词 - pagination_token: 分页token，从上一次响应获取 ### 返回: - `data.items`: Reels列表 - `pagination_token`: 下一页token ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search Instagram Reels by keyword - Support pagination ### Parameters: - keyword: Search keyword - pagination_token: Pagination token from previous response ### Return: - `data.items`: List of reels - `pagination_token`: Next page token ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"cat\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_reels_api_v1_instagram_v2_search_reels_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object pagination_token: 分页token/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_reels_api_v1_instagram_v2_search_reels_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_reels_api_v1_instagram_v2_search_reels_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v2/search_reels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_users_api_v1_instagram_v2_search_users_get(self, keyword, **kwargs):  # noqa: E501
        """搜索用户/Search users  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram用户 ### 参数: - keyword: 搜索关键词 ### 返回: - `data.items`: 用户列表 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search Instagram users by keyword ### Parameters: - keyword: Search keyword ### Return: - `data.items`: List of users ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_api_v1_instagram_v2_search_users_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_users_api_v1_instagram_v2_search_users_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_users_api_v1_instagram_v2_search_users_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_users_api_v1_instagram_v2_search_users_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索用户/Search users  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索Instagram用户 ### 参数: - keyword: 搜索关键词 ### 返回: - `data.items`: 用户列表 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Search Instagram users by keyword ### Parameters: - keyword: Search keyword ### Return: - `data.items`: List of users ### Price: - 0.002 USD/request  # [示例/Example] keyword = \"instagram\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_api_v1_instagram_v2_search_users_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
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
                    " to method search_users_api_v1_instagram_v2_search_users_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_users_api_v1_instagram_v2_search_users_get`")  # noqa: E501

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
            '/api/v1/instagram/v2/search_users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def shortcode_to_media_id_api_v1_instagram_v2_shortcode_to_media_id_get(self, shortcode, **kwargs):  # noqa: E501
        """Shortcode转Media ID/Convert shortcode to media ID  # noqa: E501

        # [中文] ### 用途: - 将Instagram帖子的Shortcode转换为Media ID - Shortcode是帖子URL中的唯一标识，如 instagram.com/p/DRhvwVLAHAG/ 中的 DRhvwVLAHAG ### 参数: - shortcode: 帖子的Shortcode ### 返回: - `status`: 转换状态 - `shortcode`: 原始Shortcode - `media_id`: 转换后的Media ID ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Convert Instagram post shortcode to media ID - Shortcode is the unique identifier in post URL, e.g., DRhvwVLAHAG in instagram.com/p/DRhvwVLAHAG/ ### Parameters: - shortcode: Post shortcode ### Return: - `status`: Conversion status - `shortcode`: Original shortcode - `media_id`: Converted media ID ### Price: - 0.002 USD/request  # [示例/Example] shortcode = \"DRhvwVLAHAG\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shortcode_to_media_id_api_v1_instagram_v2_shortcode_to_media_id_get(shortcode, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object shortcode: 帖子Shortcode/Post shortcode (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.shortcode_to_media_id_api_v1_instagram_v2_shortcode_to_media_id_get_with_http_info(shortcode, **kwargs)  # noqa: E501
        else:
            (data) = self.shortcode_to_media_id_api_v1_instagram_v2_shortcode_to_media_id_get_with_http_info(shortcode, **kwargs)  # noqa: E501
            return data

    def shortcode_to_media_id_api_v1_instagram_v2_shortcode_to_media_id_get_with_http_info(self, shortcode, **kwargs):  # noqa: E501
        """Shortcode转Media ID/Convert shortcode to media ID  # noqa: E501

        # [中文] ### 用途: - 将Instagram帖子的Shortcode转换为Media ID - Shortcode是帖子URL中的唯一标识，如 instagram.com/p/DRhvwVLAHAG/ 中的 DRhvwVLAHAG ### 参数: - shortcode: 帖子的Shortcode ### 返回: - `status`: 转换状态 - `shortcode`: 原始Shortcode - `media_id`: 转换后的Media ID ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Convert Instagram post shortcode to media ID - Shortcode is the unique identifier in post URL, e.g., DRhvwVLAHAG in instagram.com/p/DRhvwVLAHAG/ ### Parameters: - shortcode: Post shortcode ### Return: - `status`: Conversion status - `shortcode`: Original shortcode - `media_id`: Converted media ID ### Price: - 0.002 USD/request  # [示例/Example] shortcode = \"DRhvwVLAHAG\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shortcode_to_media_id_api_v1_instagram_v2_shortcode_to_media_id_get_with_http_info(shortcode, async_req=True)
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
                    " to method shortcode_to_media_id_api_v1_instagram_v2_shortcode_to_media_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shortcode' is set
        if self.api_client.client_side_validation and ('shortcode' not in params or
                                                       params['shortcode'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `shortcode` when calling `shortcode_to_media_id_api_v1_instagram_v2_shortcode_to_media_id_get`")  # noqa: E501

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
            '/api/v1/instagram/v2/shortcode_to_media_id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_id_to_username_api_v1_instagram_v2_user_id_to_username_get(self, user_id, **kwargs):  # noqa: E501
        """用户ID转用户信息/Get user info by user ID  # noqa: E501

        # [中文] ### 用途: - 通过Instagram用户ID获取用户信息 - 可用于将用户ID转换为用户名及获取完整用户资料 ### 参数: - user_id: 用户ID ### 返回: - `pk`/`pk_id`: 用户ID - `username`: 用户名 - `full_name`: 用户全名 - `is_private`: 是否私密账户 - `is_verified`: 是否已认证 - `profile_pic_url`: 头像URL - `biography`: 个人简介 - `follower_count`: 粉丝数 - `following_count`: 关注数 - `media_count`: 帖子数 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get user info by Instagram user ID - Can be used to convert user ID to username and get full profile ### Parameters: - user_id: User ID ### Return: - `pk`/`pk_id`: User ID - `username`: Username - `full_name`: Full name - `is_private`: Whether account is private - `is_verified`: Whether account is verified - `profile_pic_url`: Profile picture URL - `biography`: Bio - `follower_count`: Followers count - `following_count`: Following count - `media_count`: Posts count ### Price: - 0.002 USD/request  # [示例/Example] user_id = \"18527\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_id_to_username_api_v1_instagram_v2_user_id_to_username_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_id_to_username_api_v1_instagram_v2_user_id_to_username_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.user_id_to_username_api_v1_instagram_v2_user_id_to_username_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def user_id_to_username_api_v1_instagram_v2_user_id_to_username_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """用户ID转用户信息/Get user info by user ID  # noqa: E501

        # [中文] ### 用途: - 通过Instagram用户ID获取用户信息 - 可用于将用户ID转换为用户名及获取完整用户资料 ### 参数: - user_id: 用户ID ### 返回: - `pk`/`pk_id`: 用户ID - `username`: 用户名 - `full_name`: 用户全名 - `is_private`: 是否私密账户 - `is_verified`: 是否已认证 - `profile_pic_url`: 头像URL - `biography`: 个人简介 - `follower_count`: 粉丝数 - `following_count`: 关注数 - `media_count`: 帖子数 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get user info by Instagram user ID - Can be used to convert user ID to username and get full profile ### Parameters: - user_id: User ID ### Return: - `pk`/`pk_id`: User ID - `username`: Username - `full_name`: Full name - `is_private`: Whether account is private - `is_verified`: Whether account is verified - `profile_pic_url`: Profile picture URL - `biography`: Bio - `follower_count`: Followers count - `following_count`: Following count - `media_count`: Posts count ### Price: - 0.002 USD/request  # [示例/Example] user_id = \"18527\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_id_to_username_api_v1_instagram_v2_user_id_to_username_get_with_http_info(user_id, async_req=True)
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
                    " to method user_id_to_username_api_v1_instagram_v2_user_id_to_username_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `user_id_to_username_api_v1_instagram_v2_user_id_to_username_get`")  # noqa: E501

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
            '/api/v1/instagram/v2/user_id_to_username', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
