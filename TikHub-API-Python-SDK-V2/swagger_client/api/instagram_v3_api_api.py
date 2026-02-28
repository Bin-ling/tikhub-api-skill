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


class InstagramV3APIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get(self, comment_ids, **kwargs):  # noqa: E501
        """批量翻译评论/Bulk translate comments  # noqa: E501

        # [中文] ### 用途: - 批量翻译Instagram评论 - 支持同时翻译多条评论，效率更高 - 评论ID可从 get_post_comments 接口获取 ### 参数: - comment_ids: 评论ID列表，多个ID用逗号分隔，**最多10条**     - 例如: `18099342953509681` （单个）     - 例如: `18099342953509681,18099342953509682,18099342953509683` （多个） ### 注意: - 单次请求最多支持10条评论ID，超过会返回错误 ### 返回: - `data.comment_translations`: 翻译结果映射     - key: 评论ID     - value: 翻译后的文本 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Bulk translate Instagram comments - Support translating multiple comments at once for better efficiency - Comment IDs can be obtained from get_post_comments API ### Parameters: - comment_ids: Comment ID list, separated by commas, **max 10 IDs**     - Example: `18099342953509681` (single)     - Example: `18099342953509681,18099342953509682,18099342953509683` (multiple) ### Note: - Maximum 10 comment IDs per request, exceeding will return an error ### Return: - `data.comment_translations`: Translation result mapping     - key: Comment ID     - value: Translated text ### Price: - 0.002 USD/request  ### 示例/Example ``` comment_ids = \"18099342953509681\" # comment_ids = \"18099342953509681,18099342953509682\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get(comment_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object comment_ids: 评论ID列表，逗号分隔/Comment ID list, comma separated (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get_with_http_info(comment_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get_with_http_info(comment_ids, **kwargs)  # noqa: E501
            return data

    def bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get_with_http_info(self, comment_ids, **kwargs):  # noqa: E501
        """批量翻译评论/Bulk translate comments  # noqa: E501

        # [中文] ### 用途: - 批量翻译Instagram评论 - 支持同时翻译多条评论，效率更高 - 评论ID可从 get_post_comments 接口获取 ### 参数: - comment_ids: 评论ID列表，多个ID用逗号分隔，**最多10条**     - 例如: `18099342953509681` （单个）     - 例如: `18099342953509681,18099342953509682,18099342953509683` （多个） ### 注意: - 单次请求最多支持10条评论ID，超过会返回错误 ### 返回: - `data.comment_translations`: 翻译结果映射     - key: 评论ID     - value: 翻译后的文本 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Bulk translate Instagram comments - Support translating multiple comments at once for better efficiency - Comment IDs can be obtained from get_post_comments API ### Parameters: - comment_ids: Comment ID list, separated by commas, **max 10 IDs**     - Example: `18099342953509681` (single)     - Example: `18099342953509681,18099342953509682,18099342953509683` (multiple) ### Note: - Maximum 10 comment IDs per request, exceeding will return an error ### Return: - `data.comment_translations`: Translation result mapping     - key: Comment ID     - value: Translated text ### Price: - 0.002 USD/request  ### 示例/Example ``` comment_ids = \"18099342953509681\" # comment_ids = \"18099342953509681,18099342953509682\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get_with_http_info(comment_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object comment_ids: 评论ID列表，逗号分隔/Comment ID list, comma separated (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['comment_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'comment_ids' is set
        if self.api_client.client_side_validation and ('comment_ids' not in params or
                                                       params['comment_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_ids` when calling `bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'comment_ids' in params:
            query_params.append(('comment_ids', params['comment_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/bulk_translate_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def general_search_api_v1_instagram_v3_general_search_get(self, query, **kwargs):  # noqa: E501
        """综合搜索（支持分页）/General search (with pagination)  # noqa: E501

        # [中文] ### 用途: - Instagram综合搜索接口（支持分页） - 支持通过 next_max_id 分页获取大量搜索结果 - 返回用户、话题标签、地点等综合结果 ### 参数: - query: 搜索关键词 - next_max_id: 分页ID，首次请求不传，从上一次响应的 `data.next_max_id` 获取 - rank_token: 排序token，首次请求不传，从上一次响应的 `data.rank_token` 获取 - enable_metadata: 是否启用元数据 ### 返回: - `data.num_results`: 结果数量 - `data.users`: 用户搜索结果列表 - `data.places`: 地点搜索结果列表 - `data.hashtags`: 话题标签搜索结果列表 - `data.next_max_id`: 下一页分页ID（传给下次请求的next_max_id参数） - `data.rank_token`: 排序token（传给下次请求的rank_token参数） - `data.has_more`: 是否有更多结果 ### 注意事项: - ⚠️ **已知问题**: 综合搜索结果可能存在重复数据，这是 Instagram API 的已知行为 - 搜索话题标签时，query 需要带上 `#` 前缀，例如搜索 fashion 话题应传入 `#fashion` - `#` 符号在 URL 中需要进行 URL 编码为 `%23`，例如: `?query=%23fashion` - 如果使用 HTTP 客户端库（如 requests/httpx），直接传入 `#fashion` 即可，库会自动处理编码 ### 分页使用方法: 1. 首次请求：只传 `query` 参数 2. 获取响应中的 `next_max_id` 和 `rank_token` 3. 下次请求：传入 `query`、`next_max_id` 和 `rank_token` 4. 重复步骤 2-3 直到 `has_more` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Instagram general search API (with pagination) - Support pagination via next_max_id to fetch more search results - Returns blended results of users, hashtags, places, etc. ### Parameters: - query: Search keyword - next_max_id: Pagination ID, omit for first request, get from previous response `data.next_max_id` - rank_token: Rank token, omit for first request, get from previous response `data.rank_token` - enable_metadata: Enable metadata ### Return: - `data.num_results`: Number of results - `data.users`: User search results - `data.places`: Place search results - `data.hashtags`: Hashtag search results - `data.next_max_id`: Next page pagination ID (use as next_max_id in next request) - `data.rank_token`: Rank token (use as rank_token in next request) - `data.has_more`: Whether has more results ### Notes: - ⚠️ **Known Issue**: General search results may contain duplicate data, this is a known behavior of Instagram API - When searching for hashtags, `query` must include the `#` prefix, e.g., use `#fashion` to search for the fashion hashtag - The `#` character must be URL-encoded as `%23` in the URL, e.g., `?query=%23fashion` - If using an HTTP client library (e.g., requests/httpx), just pass `#fashion` directly and the library will handle encoding automatically ### Pagination usage: 1. First request: Only pass `query` parameter 2. Get `next_max_id` and `rank_token` from response 3. Next request: Pass `query`, `next_max_id` and `rank_token` 4. Repeat steps 2-3 until `has_more` is false ### Price: - 0.002 USD/request  ### 示例/Example ``` query = \"justin\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.general_search_api_v1_instagram_v3_general_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object next_max_id: 分页ID，首次请求不传，从上一次响应的next_max_id获取/Pagination ID, omit for first request, get from previous response next_max_id
        :param object rank_token: 排序token，首次请求不传，从上一次响应获取/Rank token, omit for first request, get from previous response
        :param object enable_metadata: 是否启用元数据/Enable metadata
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.general_search_api_v1_instagram_v3_general_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.general_search_api_v1_instagram_v3_general_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def general_search_api_v1_instagram_v3_general_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """综合搜索（支持分页）/General search (with pagination)  # noqa: E501

        # [中文] ### 用途: - Instagram综合搜索接口（支持分页） - 支持通过 next_max_id 分页获取大量搜索结果 - 返回用户、话题标签、地点等综合结果 ### 参数: - query: 搜索关键词 - next_max_id: 分页ID，首次请求不传，从上一次响应的 `data.next_max_id` 获取 - rank_token: 排序token，首次请求不传，从上一次响应的 `data.rank_token` 获取 - enable_metadata: 是否启用元数据 ### 返回: - `data.num_results`: 结果数量 - `data.users`: 用户搜索结果列表 - `data.places`: 地点搜索结果列表 - `data.hashtags`: 话题标签搜索结果列表 - `data.next_max_id`: 下一页分页ID（传给下次请求的next_max_id参数） - `data.rank_token`: 排序token（传给下次请求的rank_token参数） - `data.has_more`: 是否有更多结果 ### 注意事项: - ⚠️ **已知问题**: 综合搜索结果可能存在重复数据，这是 Instagram API 的已知行为 - 搜索话题标签时，query 需要带上 `#` 前缀，例如搜索 fashion 话题应传入 `#fashion` - `#` 符号在 URL 中需要进行 URL 编码为 `%23`，例如: `?query=%23fashion` - 如果使用 HTTP 客户端库（如 requests/httpx），直接传入 `#fashion` 即可，库会自动处理编码 ### 分页使用方法: 1. 首次请求：只传 `query` 参数 2. 获取响应中的 `next_max_id` 和 `rank_token` 3. 下次请求：传入 `query`、`next_max_id` 和 `rank_token` 4. 重复步骤 2-3 直到 `has_more` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Instagram general search API (with pagination) - Support pagination via next_max_id to fetch more search results - Returns blended results of users, hashtags, places, etc. ### Parameters: - query: Search keyword - next_max_id: Pagination ID, omit for first request, get from previous response `data.next_max_id` - rank_token: Rank token, omit for first request, get from previous response `data.rank_token` - enable_metadata: Enable metadata ### Return: - `data.num_results`: Number of results - `data.users`: User search results - `data.places`: Place search results - `data.hashtags`: Hashtag search results - `data.next_max_id`: Next page pagination ID (use as next_max_id in next request) - `data.rank_token`: Rank token (use as rank_token in next request) - `data.has_more`: Whether has more results ### Notes: - ⚠️ **Known Issue**: General search results may contain duplicate data, this is a known behavior of Instagram API - When searching for hashtags, `query` must include the `#` prefix, e.g., use `#fashion` to search for the fashion hashtag - The `#` character must be URL-encoded as `%23` in the URL, e.g., `?query=%23fashion` - If using an HTTP client library (e.g., requests/httpx), just pass `#fashion` directly and the library will handle encoding automatically ### Pagination usage: 1. First request: Only pass `query` parameter 2. Get `next_max_id` and `rank_token` from response 3. Next request: Pass `query`, `next_max_id` and `rank_token` 4. Repeat steps 2-3 until `has_more` is false ### Price: - 0.002 USD/request  ### 示例/Example ``` query = \"justin\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.general_search_api_v1_instagram_v3_general_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object next_max_id: 分页ID，首次请求不传，从上一次响应的next_max_id获取/Pagination ID, omit for first request, get from previous response next_max_id
        :param object rank_token: 排序token，首次请求不传，从上一次响应获取/Rank token, omit for first request, get from previous response
        :param object enable_metadata: 是否启用元数据/Enable metadata
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'next_max_id', 'rank_token', 'enable_metadata']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method general_search_api_v1_instagram_v3_general_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `general_search_api_v1_instagram_v3_general_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'next_max_id' in params:
            query_params.append(('next_max_id', params['next_max_id']))  # noqa: E501
        if 'rank_token' in params:
            query_params.append(('rank_token', params['rank_token']))  # noqa: E501
        if 'enable_metadata' in params:
            query_params.append(('enable_metadata', params['enable_metadata']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/general_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_comment_replies_api_v1_instagram_v3_get_comment_replies_get(self, comment_id, **kwargs):  # noqa: E501
        """获取评论的子评论/回复/Get comment replies  # noqa: E501

        # [中文] ### 用途: - 获取Instagram评论的子评论（回复）列表 - 支持分页获取所有回复 - 父评论的 comment_id 可从 get_post_comments 接口的评论列表中获取 - 支持通过 media_id、短代码（code）或帖子URL定位帖子 ### 参数（三选一定位帖子）: - media_id: 帖子的媒体ID（数字ID） - code: 帖子短代码（如 DUajw4YkorV） - url: 帖子URL（如 `https://www.instagram.com/p/DUajw4YkorV/`） ### 必填参数: - comment_id: 父评论ID（从 get_post_comments 返回的评论中获取 `pk` 字段） ### 其他参数: - min_id: 分页游标，首次请求不传，从上一次响应的 `data.next_min_child_cursor` 获取 ### 返回: - `data.child_comments`: 子评论列表     - `user`: 评论者信息     - `text`: 评论文本     - `created_at`: 评论时间戳     - `comment_like_count`: 评论点赞数     - `pk`: 评论ID - `data.next_min_child_cursor`: 下一页分页游标（传给下次请求的min_id参数） - `data.has_more_tail_child_comments`: 是否有更多子评论 - `data.num_tail_child_comments`: 剩余子评论数 ### 分页使用方法: 1. 首次请求：传 `media_id` 和 `comment_id` 参数 2. 获取响应中的 `data.next_min_child_cursor` 3. 下次请求：传入 `media_id`、`comment_id` 和 `min_id` (使用上次的next_min_child_cursor) 4. 重复步骤 2-3 直到 `data.has_more_tail_child_comments` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram comment's child comments (replies) list - Support pagination to fetch all replies - Parent comment's comment_id can be obtained from get_post_comments API - Support querying by media_id, shortcode (code), or post URL ### Parameters (one of to locate post): - media_id: Post media ID (numeric ID) - code: Post shortcode (e.g., DUajw4YkorV) - url: Post URL (e.g., `https://www.instagram.com/p/DUajw4YkorV/`) ### Required: - comment_id: Parent comment ID (get `pk` field from get_post_comments response) ### Other parameters: - min_id: Pagination cursor, omit for first request, get from previous response `data.next_min_child_cursor` ### Return: - `data.child_comments`: Child comments list     - `user`: Commenter info     - `text`: Comment text     - `created_at`: Comment timestamp     - `comment_like_count`: Comment likes count     - `pk`: Comment ID - `data.next_min_child_cursor`: Next page cursor (use as min_id in next request) - `data.has_more_tail_child_comments`: Whether has more child comments - `data.num_tail_child_comments`: Remaining child comments count ### Pagination usage: 1. First request: Pass `media_id` and `comment_id` parameters 2. Get `data.next_min_child_cursor` from response 3. Next request: Pass `media_id`, `comment_id`, and `min_id` (use next_min_child_cursor from previous) 4. Repeat steps 2-3 until `data.has_more_tail_child_comments` is false ### Price: - 0.002 USD/request  ### 示例/Example media_id = \"3829530490739515971\" comment_id = \"18065937092249736\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_comment_replies_api_v1_instagram_v3_get_comment_replies_get(comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object comment_id: 父评论ID/Parent comment ID (required)
        :param object media_id: 帖子媒体ID/Post media ID
        :param object code: 帖子短代码/Post shortcode
        :param object url: 帖子URL/Post URL
        :param object min_id: 分页游标，首次请求不传，从上一次响应的 next_min_child_cursor 获取/Pagination cursor, omit for first request, get from previous response next_min_child_cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_comment_replies_api_v1_instagram_v3_get_comment_replies_get_with_http_info(comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_comment_replies_api_v1_instagram_v3_get_comment_replies_get_with_http_info(comment_id, **kwargs)  # noqa: E501
            return data

    def get_comment_replies_api_v1_instagram_v3_get_comment_replies_get_with_http_info(self, comment_id, **kwargs):  # noqa: E501
        """获取评论的子评论/回复/Get comment replies  # noqa: E501

        # [中文] ### 用途: - 获取Instagram评论的子评论（回复）列表 - 支持分页获取所有回复 - 父评论的 comment_id 可从 get_post_comments 接口的评论列表中获取 - 支持通过 media_id、短代码（code）或帖子URL定位帖子 ### 参数（三选一定位帖子）: - media_id: 帖子的媒体ID（数字ID） - code: 帖子短代码（如 DUajw4YkorV） - url: 帖子URL（如 `https://www.instagram.com/p/DUajw4YkorV/`） ### 必填参数: - comment_id: 父评论ID（从 get_post_comments 返回的评论中获取 `pk` 字段） ### 其他参数: - min_id: 分页游标，首次请求不传，从上一次响应的 `data.next_min_child_cursor` 获取 ### 返回: - `data.child_comments`: 子评论列表     - `user`: 评论者信息     - `text`: 评论文本     - `created_at`: 评论时间戳     - `comment_like_count`: 评论点赞数     - `pk`: 评论ID - `data.next_min_child_cursor`: 下一页分页游标（传给下次请求的min_id参数） - `data.has_more_tail_child_comments`: 是否有更多子评论 - `data.num_tail_child_comments`: 剩余子评论数 ### 分页使用方法: 1. 首次请求：传 `media_id` 和 `comment_id` 参数 2. 获取响应中的 `data.next_min_child_cursor` 3. 下次请求：传入 `media_id`、`comment_id` 和 `min_id` (使用上次的next_min_child_cursor) 4. 重复步骤 2-3 直到 `data.has_more_tail_child_comments` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram comment's child comments (replies) list - Support pagination to fetch all replies - Parent comment's comment_id can be obtained from get_post_comments API - Support querying by media_id, shortcode (code), or post URL ### Parameters (one of to locate post): - media_id: Post media ID (numeric ID) - code: Post shortcode (e.g., DUajw4YkorV) - url: Post URL (e.g., `https://www.instagram.com/p/DUajw4YkorV/`) ### Required: - comment_id: Parent comment ID (get `pk` field from get_post_comments response) ### Other parameters: - min_id: Pagination cursor, omit for first request, get from previous response `data.next_min_child_cursor` ### Return: - `data.child_comments`: Child comments list     - `user`: Commenter info     - `text`: Comment text     - `created_at`: Comment timestamp     - `comment_like_count`: Comment likes count     - `pk`: Comment ID - `data.next_min_child_cursor`: Next page cursor (use as min_id in next request) - `data.has_more_tail_child_comments`: Whether has more child comments - `data.num_tail_child_comments`: Remaining child comments count ### Pagination usage: 1. First request: Pass `media_id` and `comment_id` parameters 2. Get `data.next_min_child_cursor` from response 3. Next request: Pass `media_id`, `comment_id`, and `min_id` (use next_min_child_cursor from previous) 4. Repeat steps 2-3 until `data.has_more_tail_child_comments` is false ### Price: - 0.002 USD/request  ### 示例/Example media_id = \"3829530490739515971\" comment_id = \"18065937092249736\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_comment_replies_api_v1_instagram_v3_get_comment_replies_get_with_http_info(comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object comment_id: 父评论ID/Parent comment ID (required)
        :param object media_id: 帖子媒体ID/Post media ID
        :param object code: 帖子短代码/Post shortcode
        :param object url: 帖子URL/Post URL
        :param object min_id: 分页游标，首次请求不传，从上一次响应的 next_min_child_cursor 获取/Pagination cursor, omit for first request, get from previous response next_min_child_cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['comment_id', 'media_id', 'code', 'url', 'min_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_comment_replies_api_v1_instagram_v3_get_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `get_comment_replies_api_v1_instagram_v3_get_comment_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'media_id' in params:
            query_params.append(('media_id', params['media_id']))  # noqa: E501
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501
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
            '/api/v1/instagram/v3/get_comment_replies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_explore_api_v1_instagram_v3_get_explore_get(self, **kwargs):  # noqa: E501
        """获取探索页推荐帖子/Get explore feed  # noqa: E501

        # [中文] ### 用途: - 获取Instagram探索/发现页的推荐帖子 - 返回个性化推荐的帖子列表 - 支持分页获取更多推荐内容 ### 参数: - max_id: 分页游标，首次请求不传，从上一次响应的 `data.next_max_id` 获取 ### 返回: - `data.sectional_items`: 推荐内容分区列表     - `layout_content.medias`: 媒体列表         - `media.id`: 帖子ID         - `media.code`: 帖子短代码         - `media.media_type`: 媒体类型（1=图片, 2=视频, 8=合集）         - `media.like_count`: 点赞数         - `media.comment_count`: 评论数         - `media.caption.text`: 帖子文本         - `media.user`: 发布者信息         - `media.image_versions2`: 图片版本列表         - `media.video_versions`: 视频版本列表（视频时存在） - `data.next_max_id`: 下一页分页游标（传给下次请求的max_id参数） - `data.more_available`: 是否有更多内容 ### 分页使用方法: 1. 首次请求：不传任何参数 2. 获取响应中的 `data.next_max_id` 3. 下次请求：传入 `max_id` (使用上次的next_max_id) 4. 重复步骤 2-3 直到 `data.more_available` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram Explore/Discover page recommended posts - Returns personalized recommended post list - Support pagination to fetch more recommendations ### Parameters: - max_id: Pagination cursor, omit for first request, get from previous response `data.next_max_id` ### Return: - `data.sectional_items`: Recommended content section list     - `layout_content.medias`: Media list         - `media.id`: Post ID         - `media.code`: Post shortcode         - `media.media_type`: Media type (1=image, 2=video, 8=carousel)         - `media.like_count`: Likes count         - `media.comment_count`: Comments count         - `media.caption.text`: Post caption text         - `media.user`: Publisher info         - `media.image_versions2`: Image version list         - `media.video_versions`: Video version list (exists for videos) - `data.next_max_id`: Next page cursor (use as max_id in next request) - `data.more_available`: Whether has more content ### Pagination usage: 1. First request: No parameters needed 2. Get `data.next_max_id` from response 3. Next request: Pass `max_id` (use next_max_id from previous) 4. Repeat steps 2-3 until `data.more_available` is false ### Price: - 0.002 USD/request  ### 示例/Example ``` # 第一页 / First page (不传参数 / no parameters) # 第二页 / Second page # max_id = \"...\"  # 从第一页响应中获取 / Get from first page response ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_explore_api_v1_instagram_v3_get_explore_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object max_id: 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_explore_api_v1_instagram_v3_get_explore_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_explore_api_v1_instagram_v3_get_explore_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_explore_api_v1_instagram_v3_get_explore_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取探索页推荐帖子/Get explore feed  # noqa: E501

        # [中文] ### 用途: - 获取Instagram探索/发现页的推荐帖子 - 返回个性化推荐的帖子列表 - 支持分页获取更多推荐内容 ### 参数: - max_id: 分页游标，首次请求不传，从上一次响应的 `data.next_max_id` 获取 ### 返回: - `data.sectional_items`: 推荐内容分区列表     - `layout_content.medias`: 媒体列表         - `media.id`: 帖子ID         - `media.code`: 帖子短代码         - `media.media_type`: 媒体类型（1=图片, 2=视频, 8=合集）         - `media.like_count`: 点赞数         - `media.comment_count`: 评论数         - `media.caption.text`: 帖子文本         - `media.user`: 发布者信息         - `media.image_versions2`: 图片版本列表         - `media.video_versions`: 视频版本列表（视频时存在） - `data.next_max_id`: 下一页分页游标（传给下次请求的max_id参数） - `data.more_available`: 是否有更多内容 ### 分页使用方法: 1. 首次请求：不传任何参数 2. 获取响应中的 `data.next_max_id` 3. 下次请求：传入 `max_id` (使用上次的next_max_id) 4. 重复步骤 2-3 直到 `data.more_available` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram Explore/Discover page recommended posts - Returns personalized recommended post list - Support pagination to fetch more recommendations ### Parameters: - max_id: Pagination cursor, omit for first request, get from previous response `data.next_max_id` ### Return: - `data.sectional_items`: Recommended content section list     - `layout_content.medias`: Media list         - `media.id`: Post ID         - `media.code`: Post shortcode         - `media.media_type`: Media type (1=image, 2=video, 8=carousel)         - `media.like_count`: Likes count         - `media.comment_count`: Comments count         - `media.caption.text`: Post caption text         - `media.user`: Publisher info         - `media.image_versions2`: Image version list         - `media.video_versions`: Video version list (exists for videos) - `data.next_max_id`: Next page cursor (use as max_id in next request) - `data.more_available`: Whether has more content ### Pagination usage: 1. First request: No parameters needed 2. Get `data.next_max_id` from response 3. Next request: Pass `max_id` (use next_max_id from previous) 4. Repeat steps 2-3 until `data.more_available` is false ### Price: - 0.002 USD/request  ### 示例/Example ``` # 第一页 / First page (不传参数 / no parameters) # 第二页 / Second page # max_id = \"...\"  # 从第一页响应中获取 / Get from first page response ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_explore_api_v1_instagram_v3_get_explore_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object max_id: 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_explore_api_v1_instagram_v3_get_explore_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_explore', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get(self, highlight_id, **kwargs):  # noqa: E501
        """获取Highlight精选详情/Get highlight stories  # noqa: E501

        # [中文] ### 用途: - 获取Instagram Highlight精选的详细故事/帖子内容 - 返回精选集合中的所有Stories媒体 ### 参数: - highlight_id: 精选ID，格式为 `highlight:xxx`（从 get_user_highlights 接口获取） - reel_ids: 精选ID列表，逗号分隔（可选，如不提供则仅查询highlight_id指定的精选）     - 例如: `highlight:18064916456320419,highlight:18155682898389765`     - 可同时查询多个精选的内容 ### 返回: - `data.story_highlight_tray`: 精选故事集合     - `id`: 精选ID     - `title`: 精选标题     - `items`: 故事列表         - `id`: 故事ID         - `pk`: 故事PK         - `taken_at`: 发布时间戳         - `media_type`: 媒体类型（1=图片, 2=视频）         - `image_versions2`: 图片版本列表         - `video_versions`: 视频版本列表（视频时存在）         - `user`: 发布者信息 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram Highlight's detailed story/post content - Returns all Stories media in the highlight collection ### Parameters: - highlight_id: Highlight ID, format `highlight:xxx` (get from get_user_highlights API) - reel_ids: Highlight ID list, comma separated (optional, if not provided only queries the highlight_id)     - Example: `highlight:18064916456320419,highlight:18155682898389765`     - Can query multiple highlights at once ### Return: - `data.story_highlight_tray`: Highlight story collection     - `id`: Highlight ID     - `title`: Highlight title     - `items`: Story list         - `id`: Story ID         - `pk`: Story PK         - `taken_at`: Published timestamp         - `media_type`: Media type (1=image, 2=video)         - `image_versions2`: Image version list         - `video_versions`: Video version list (exists for videos)         - `user`: Publisher info ### Price: - 0.002 USD/request  ### 示例/Example ``` highlight_id = \"highlight:18064916456320419\" # reel_ids = \"highlight:18064916456320419,highlight:18155682898389765\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get(highlight_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object highlight_id: 精选ID/Highlight ID (格式/format: highlight:xxx) (required)
        :param object reel_ids: 精选ID列表，逗号分隔，如不提供则仅查询highlight_id/Highlight ID list, comma separated, if not provided only query highlight_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get_with_http_info(highlight_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get_with_http_info(highlight_id, **kwargs)  # noqa: E501
            return data

    def get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get_with_http_info(self, highlight_id, **kwargs):  # noqa: E501
        """获取Highlight精选详情/Get highlight stories  # noqa: E501

        # [中文] ### 用途: - 获取Instagram Highlight精选的详细故事/帖子内容 - 返回精选集合中的所有Stories媒体 ### 参数: - highlight_id: 精选ID，格式为 `highlight:xxx`（从 get_user_highlights 接口获取） - reel_ids: 精选ID列表，逗号分隔（可选，如不提供则仅查询highlight_id指定的精选）     - 例如: `highlight:18064916456320419,highlight:18155682898389765`     - 可同时查询多个精选的内容 ### 返回: - `data.story_highlight_tray`: 精选故事集合     - `id`: 精选ID     - `title`: 精选标题     - `items`: 故事列表         - `id`: 故事ID         - `pk`: 故事PK         - `taken_at`: 发布时间戳         - `media_type`: 媒体类型（1=图片, 2=视频）         - `image_versions2`: 图片版本列表         - `video_versions`: 视频版本列表（视频时存在）         - `user`: 发布者信息 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram Highlight's detailed story/post content - Returns all Stories media in the highlight collection ### Parameters: - highlight_id: Highlight ID, format `highlight:xxx` (get from get_user_highlights API) - reel_ids: Highlight ID list, comma separated (optional, if not provided only queries the highlight_id)     - Example: `highlight:18064916456320419,highlight:18155682898389765`     - Can query multiple highlights at once ### Return: - `data.story_highlight_tray`: Highlight story collection     - `id`: Highlight ID     - `title`: Highlight title     - `items`: Story list         - `id`: Story ID         - `pk`: Story PK         - `taken_at`: Published timestamp         - `media_type`: Media type (1=image, 2=video)         - `image_versions2`: Image version list         - `video_versions`: Video version list (exists for videos)         - `user`: Publisher info ### Price: - 0.002 USD/request  ### 示例/Example ``` highlight_id = \"highlight:18064916456320419\" # reel_ids = \"highlight:18064916456320419,highlight:18155682898389765\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get_with_http_info(highlight_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object highlight_id: 精选ID/Highlight ID (格式/format: highlight:xxx) (required)
        :param object reel_ids: 精选ID列表，逗号分隔，如不提供则仅查询highlight_id/Highlight ID list, comma separated, if not provided only query highlight_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['highlight_id', 'reel_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'highlight_id' is set
        if self.api_client.client_side_validation and ('highlight_id' not in params or
                                                       params['highlight_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `highlight_id` when calling `get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'highlight_id' in params:
            query_params.append(('highlight_id', params['highlight_id']))  # noqa: E501
        if 'reel_ids' in params:
            query_params.append(('reel_ids', params['reel_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_highlight_stories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_location_info_api_v1_instagram_v3_get_location_info_get(self, location_id, **kwargs):  # noqa: E501
        """获取地点详情/Get location info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram地点的详细信息 - 包含地点名称、地址、坐标、附近地点等 - 地点ID可从搜索接口（search_places）或帖子详情中获取 ### 参数: - location_id: 地点ID（数字） - show_nearby: 是否显示附近地点（默认true） ### 返回: - `data.native_location_data`: 地点基本信息     - `name`: 地点名称     - `address`: 地址     - `city`: 城市     - `lat`: 纬度     - `lng`: 经度     - `website`: 网站     - `phone`: 电话     - `category`: 分类     - `media_count`: 关联帖子数 - `data.ranked`: 热门帖子信息 - `data.recent`: 最新帖子信息 - `data.nearby_locations`: 附近地点列表（show_nearby=true时） ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram location/place detail info - Including name, address, coordinates, nearby places, etc. - Location ID can be obtained from search API (search_places) or post details ### Parameters: - location_id: Location ID (numeric) - show_nearby: Whether to show nearby places (default true) ### Return: - `data.native_location_data`: Location basic info     - `name`: Location name     - `address`: Address     - `city`: City     - `lat`: Latitude     - `lng`: Longitude     - `website`: Website     - `phone`: Phone     - `category`: Category     - `media_count`: Associated posts count - `data.ranked`: Top posts info - `data.recent`: Recent posts info - `data.nearby_locations`: Nearby locations list (when show_nearby=true) ### Price: - 0.002 USD/request  ### 示例/Example location_id = \"1016248898\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_location_info_api_v1_instagram_v3_get_location_info_get(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object location_id: 地点ID/Location ID (required)
        :param object show_nearby: 是否显示附近地点/Whether to show nearby places
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_location_info_api_v1_instagram_v3_get_location_info_get_with_http_info(location_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_location_info_api_v1_instagram_v3_get_location_info_get_with_http_info(location_id, **kwargs)  # noqa: E501
            return data

    def get_location_info_api_v1_instagram_v3_get_location_info_get_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """获取地点详情/Get location info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram地点的详细信息 - 包含地点名称、地址、坐标、附近地点等 - 地点ID可从搜索接口（search_places）或帖子详情中获取 ### 参数: - location_id: 地点ID（数字） - show_nearby: 是否显示附近地点（默认true） ### 返回: - `data.native_location_data`: 地点基本信息     - `name`: 地点名称     - `address`: 地址     - `city`: 城市     - `lat`: 纬度     - `lng`: 经度     - `website`: 网站     - `phone`: 电话     - `category`: 分类     - `media_count`: 关联帖子数 - `data.ranked`: 热门帖子信息 - `data.recent`: 最新帖子信息 - `data.nearby_locations`: 附近地点列表（show_nearby=true时） ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram location/place detail info - Including name, address, coordinates, nearby places, etc. - Location ID can be obtained from search API (search_places) or post details ### Parameters: - location_id: Location ID (numeric) - show_nearby: Whether to show nearby places (default true) ### Return: - `data.native_location_data`: Location basic info     - `name`: Location name     - `address`: Address     - `city`: City     - `lat`: Latitude     - `lng`: Longitude     - `website`: Website     - `phone`: Phone     - `category`: Category     - `media_count`: Associated posts count - `data.ranked`: Top posts info - `data.recent`: Recent posts info - `data.nearby_locations`: Nearby locations list (when show_nearby=true) ### Price: - 0.002 USD/request  ### 示例/Example location_id = \"1016248898\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_location_info_api_v1_instagram_v3_get_location_info_get_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object location_id: 地点ID/Location ID (required)
        :param object show_nearby: 是否显示附近地点/Whether to show nearby places
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'show_nearby']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_location_info_api_v1_instagram_v3_get_location_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in params or
                                                       params['location_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `location_id` when calling `get_location_info_api_v1_instagram_v3_get_location_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'location_id' in params:
            query_params.append(('location_id', params['location_id']))  # noqa: E501
        if 'show_nearby' in params:
            query_params.append(('show_nearby', params['show_nearby']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_location_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_location_posts_api_v1_instagram_v3_get_location_posts_get(self, location_id, **kwargs):  # noqa: E501
        """获取地点相关帖子/Get location posts  # noqa: E501

        # [中文] ### 用途: - 获取Instagram地点相关的帖子列表 - 支持按热门或最新排序 - 地点ID可从搜索接口（search_places）或帖子详情中获取 ### 参数: - location_id: 地点ID（数字） - tab: 帖子排序方式     - `ranked`: 热门帖子（默认）     - `recent`: 最新帖子 - page_size_override: 每页帖子数量（默认12） ### 返回: - `data.sections`: 帖子分区列表     - `layout_content.medias`: 媒体列表         - `media.id`: 帖子ID         - `media.code`: 帖子短代码         - `media.media_type`: 媒体类型（1=图片, 2=视频, 8=合集）         - `media.like_count`: 点赞数         - `media.comment_count`: 评论数         - `media.caption.text`: 帖子文本         - `media.user`: 发布者信息 - `data.next_max_id`: 下一页分页游标 - `data.next_page`: 下一页信息 - `data.more_available`: 是否有更多内容 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram location-related posts - Support sorting by top or latest - Location ID can be obtained from search API (search_places) or post details ### Parameters: - location_id: Location ID (numeric) - tab: Post sort order     - `ranked`: Top posts (default)     - `recent`: Latest posts - page_size_override: Posts per page (default 12) ### Return: - `data.sections`: Post section list     - `layout_content.medias`: Media list         - `media.id`: Post ID         - `media.code`: Post shortcode         - `media.media_type`: Media type (1=image, 2=video, 8=carousel)         - `media.like_count`: Likes count         - `media.comment_count`: Comments count         - `media.caption.text`: Post caption text         - `media.user`: Publisher info - `data.next_max_id`: Next page cursor - `data.next_page`: Next page info - `data.more_available`: Whether has more content ### Price: - 0.002 USD/request  ### 示例/Example location_id = \"1016248898\" tab = \"ranked\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_location_posts_api_v1_instagram_v3_get_location_posts_get(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object location_id: 地点ID/Location ID (required)
        :param object tab: 帖子类型: ranked(热门), recent(最新)/Post type: ranked(top), recent(latest)
        :param object page_size_override: 每页数量/Page size
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_location_posts_api_v1_instagram_v3_get_location_posts_get_with_http_info(location_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_location_posts_api_v1_instagram_v3_get_location_posts_get_with_http_info(location_id, **kwargs)  # noqa: E501
            return data

    def get_location_posts_api_v1_instagram_v3_get_location_posts_get_with_http_info(self, location_id, **kwargs):  # noqa: E501
        """获取地点相关帖子/Get location posts  # noqa: E501

        # [中文] ### 用途: - 获取Instagram地点相关的帖子列表 - 支持按热门或最新排序 - 地点ID可从搜索接口（search_places）或帖子详情中获取 ### 参数: - location_id: 地点ID（数字） - tab: 帖子排序方式     - `ranked`: 热门帖子（默认）     - `recent`: 最新帖子 - page_size_override: 每页帖子数量（默认12） ### 返回: - `data.sections`: 帖子分区列表     - `layout_content.medias`: 媒体列表         - `media.id`: 帖子ID         - `media.code`: 帖子短代码         - `media.media_type`: 媒体类型（1=图片, 2=视频, 8=合集）         - `media.like_count`: 点赞数         - `media.comment_count`: 评论数         - `media.caption.text`: 帖子文本         - `media.user`: 发布者信息 - `data.next_max_id`: 下一页分页游标 - `data.next_page`: 下一页信息 - `data.more_available`: 是否有更多内容 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram location-related posts - Support sorting by top or latest - Location ID can be obtained from search API (search_places) or post details ### Parameters: - location_id: Location ID (numeric) - tab: Post sort order     - `ranked`: Top posts (default)     - `recent`: Latest posts - page_size_override: Posts per page (default 12) ### Return: - `data.sections`: Post section list     - `layout_content.medias`: Media list         - `media.id`: Post ID         - `media.code`: Post shortcode         - `media.media_type`: Media type (1=image, 2=video, 8=carousel)         - `media.like_count`: Likes count         - `media.comment_count`: Comments count         - `media.caption.text`: Post caption text         - `media.user`: Publisher info - `data.next_max_id`: Next page cursor - `data.next_page`: Next page info - `data.more_available`: Whether has more content ### Price: - 0.002 USD/request  ### 示例/Example location_id = \"1016248898\" tab = \"ranked\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_location_posts_api_v1_instagram_v3_get_location_posts_get_with_http_info(location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object location_id: 地点ID/Location ID (required)
        :param object tab: 帖子类型: ranked(热门), recent(最新)/Post type: ranked(top), recent(latest)
        :param object page_size_override: 每页数量/Page size
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'tab', 'page_size_override']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_location_posts_api_v1_instagram_v3_get_location_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location_id' is set
        if self.api_client.client_side_validation and ('location_id' not in params or
                                                       params['location_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `location_id` when calling `get_location_posts_api_v1_instagram_v3_get_location_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'location_id' in params:
            query_params.append(('location_id', params['location_id']))  # noqa: E501
        if 'tab' in params:
            query_params.append(('tab', params['tab']))  # noqa: E501
        if 'page_size_override' in params:
            query_params.append(('page_size_override', params['page_size_override']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_location_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_post_comments_api_v1_instagram_v3_get_post_comments_get(self, **kwargs):  # noqa: E501
        """获取帖子评论/Get post comments  # noqa: E501

        # [中文] ### 用途: - 获取Instagram帖子的评论列表 - 支持分页获取所有评论 - 支持按热门或最新排序 - 支持通过 media_id、短代码（code）或帖子URL查询 ### 参数（三选一）: - media_id: 帖子的媒体ID（数字ID） - code: 帖子短代码（如 DUajw4YkorV） - url: 帖子URL（如 `https://www.instagram.com/p/DUajw4YkorV/`） ### 其他参数: - min_id: 分页游标，首次请求不传，从上一次响应的 `data.next_min_id` 获取 - sort_order: 排序方式     - `popular`: 按热门排序（默认）     - `newest`: 按最新排序 ### 返回: - `data.comments`: 评论列表     - `user`: 评论者信息     - `text`: 评论文本     - `created_at`: 评论时间戳     - `comment_like_count`: 评论点赞数     - `child_comment_count`: 子评论数 - `data.next_min_id`: 下一页分页游标（传给下次请求的min_id参数） - `data.has_more_comments`: 是否有更多评论 - `data.comment_count`: 评论总数 ### 分页使用方法: 1. 首次请求：传 `media_id`/`code`/`url` 参数 2. 获取响应中的 `data.next_min_id` 3. 下次请求：传入 `media_id` 和 `min_id` (使用上次的next_min_id) 4. 重复步骤 2-3 直到 `data.has_more_comments` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram post comment list - Support pagination to fetch all comments - Support sorting by popular or newest - Support querying by media_id, shortcode (code), or post URL ### Parameters (one of): - media_id: Post media ID (numeric ID) - code: Post shortcode (e.g., DUajw4YkorV) - url: Post URL (e.g., `https://www.instagram.com/p/DUajw4YkorV/`) ### Other parameters: - min_id: Pagination cursor, omit for first request, get from previous response `data.next_min_id` - sort_order: Sort order     - `popular`: Sort by popular (default)     - `newest`: Sort by newest ### Return: - `data.comments`: Comment list     - `user`: Commenter info     - `text`: Comment text     - `created_at`: Comment timestamp     - `comment_like_count`: Comment likes count     - `child_comment_count`: Child comments count - `data.next_min_id`: Next page cursor (use as min_id in next request) - `data.has_more_comments`: Whether has more comments - `data.comment_count`: Total comment count ### Pagination usage: 1. First request: Pass `media_id`/`code`/`url` parameter 2. Get `data.next_min_id` from response 3. Next request: Pass `media_id` and `min_id` (use next_min_id from previous) 4. Repeat steps 2-3 until `data.has_more_comments` is false ### Price: - 0.002 USD/request  ### 示例/Example media_id = \"3815455163747032886\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_comments_api_v1_instagram_v3_get_post_comments_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子媒体ID/Post media ID
        :param object code: 帖子短代码/Post shortcode (e.g., DUajw4YkorV)
        :param object url: 帖子URL/Post URL
        :param object min_id: 分页游标，首次请求不传，从上一次响应的 next_min_id 获取/Pagination cursor, omit for first request, get from previous response next_min_id
        :param object sort_order: 排序方式: popular(热门), newest(最新)/Sort order: popular, newest
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_post_comments_api_v1_instagram_v3_get_post_comments_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_post_comments_api_v1_instagram_v3_get_post_comments_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_post_comments_api_v1_instagram_v3_get_post_comments_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取帖子评论/Get post comments  # noqa: E501

        # [中文] ### 用途: - 获取Instagram帖子的评论列表 - 支持分页获取所有评论 - 支持按热门或最新排序 - 支持通过 media_id、短代码（code）或帖子URL查询 ### 参数（三选一）: - media_id: 帖子的媒体ID（数字ID） - code: 帖子短代码（如 DUajw4YkorV） - url: 帖子URL（如 `https://www.instagram.com/p/DUajw4YkorV/`） ### 其他参数: - min_id: 分页游标，首次请求不传，从上一次响应的 `data.next_min_id` 获取 - sort_order: 排序方式     - `popular`: 按热门排序（默认）     - `newest`: 按最新排序 ### 返回: - `data.comments`: 评论列表     - `user`: 评论者信息     - `text`: 评论文本     - `created_at`: 评论时间戳     - `comment_like_count`: 评论点赞数     - `child_comment_count`: 子评论数 - `data.next_min_id`: 下一页分页游标（传给下次请求的min_id参数） - `data.has_more_comments`: 是否有更多评论 - `data.comment_count`: 评论总数 ### 分页使用方法: 1. 首次请求：传 `media_id`/`code`/`url` 参数 2. 获取响应中的 `data.next_min_id` 3. 下次请求：传入 `media_id` 和 `min_id` (使用上次的next_min_id) 4. 重复步骤 2-3 直到 `data.has_more_comments` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram post comment list - Support pagination to fetch all comments - Support sorting by popular or newest - Support querying by media_id, shortcode (code), or post URL ### Parameters (one of): - media_id: Post media ID (numeric ID) - code: Post shortcode (e.g., DUajw4YkorV) - url: Post URL (e.g., `https://www.instagram.com/p/DUajw4YkorV/`) ### Other parameters: - min_id: Pagination cursor, omit for first request, get from previous response `data.next_min_id` - sort_order: Sort order     - `popular`: Sort by popular (default)     - `newest`: Sort by newest ### Return: - `data.comments`: Comment list     - `user`: Commenter info     - `text`: Comment text     - `created_at`: Comment timestamp     - `comment_like_count`: Comment likes count     - `child_comment_count`: Child comments count - `data.next_min_id`: Next page cursor (use as min_id in next request) - `data.has_more_comments`: Whether has more comments - `data.comment_count`: Total comment count ### Pagination usage: 1. First request: Pass `media_id`/`code`/`url` parameter 2. Get `data.next_min_id` from response 3. Next request: Pass `media_id` and `min_id` (use next_min_id from previous) 4. Repeat steps 2-3 until `data.has_more_comments` is false ### Price: - 0.002 USD/request  ### 示例/Example media_id = \"3815455163747032886\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_comments_api_v1_instagram_v3_get_post_comments_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子媒体ID/Post media ID
        :param object code: 帖子短代码/Post shortcode (e.g., DUajw4YkorV)
        :param object url: 帖子URL/Post URL
        :param object min_id: 分页游标，首次请求不传，从上一次响应的 next_min_id 获取/Pagination cursor, omit for first request, get from previous response next_min_id
        :param object sort_order: 排序方式: popular(热门), newest(最新)/Sort order: popular, newest
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['media_id', 'code', 'url', 'min_id', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_post_comments_api_v1_instagram_v3_get_post_comments_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'media_id' in params:
            query_params.append(('media_id', params['media_id']))  # noqa: E501
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501
        if 'min_id' in params:
            query_params.append(('min_id', params['min_id']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_post_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_post_info_api_v1_instagram_v3_get_post_info_get(self, **kwargs):  # noqa: E501
        """获取帖子详情/Get post info (media_id or URL)  # noqa: E501

        # [中文] ### 用途: - 获取帖子详情 - 支持通过 media_id 或帖子 URL 获取 - 返回帖子的完整信息，包括图片/视频、点赞数、评论数、发布者信息等 ### 参数（二选一）: - media_id: 帖子的媒体ID（数字ID） - url: 帖子的完整URL（如 `https://www.instagram.com/p/DUajw4YkorV/`） ### 返回: - `data.items`: 帖子信息列表（通常只有一个元素）     - `id`: 帖子ID     - `code`: 帖子短代码     - `media_type`: 媒体类型（1=图片, 2=视频, 8=合集）     - `like_count`: 点赞数     - `comment_count`: 评论数     - `caption.text`: 帖子文本     - `user`: 发布者信息     - `image_versions2`: 图片版本列表     - `video_versions`: 视频版本列表（视频时存在）     - `carousel_media`: 合集媒体列表（合集时存在）     - `taken_at`: 发布时间戳 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get post details - Support fetching by media_id or post URL - Returns complete post info including images/videos, likes, comments, author info, etc. ### Parameters (one of): - media_id: Post media ID (numeric ID) - url: Full post URL (e.g., `https://www.instagram.com/p/DUajw4YkorV/`) ### Return: - `data.items`: Post info list (usually only one element)     - `id`: Post ID     - `code`: Post shortcode     - `media_type`: Media type (1=image, 2=video, 8=carousel)     - `like_count`: Likes count     - `comment_count`: Comments count     - `caption.text`: Post caption text     - `user`: Publisher info     - `image_versions2`: Image version list     - `video_versions`: Video version list (exists for videos)     - `carousel_media`: Carousel media list (exists for carousels)     - `taken_at`: Published timestamp ### Price: - 0.002 USD/request  ### 示例/Example ``` media_id = \"3800418264661789225\" # 或通过URL / Or by URL # url = \"https://www.instagram.com/p/DUajw4YkorV/\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_info_api_v1_instagram_v3_get_post_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子媒体ID/Post media ID
        :param object url: 帖子URL/Post URL
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_post_info_api_v1_instagram_v3_get_post_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_post_info_api_v1_instagram_v3_get_post_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_post_info_api_v1_instagram_v3_get_post_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取帖子详情/Get post info (media_id or URL)  # noqa: E501

        # [中文] ### 用途: - 获取帖子详情 - 支持通过 media_id 或帖子 URL 获取 - 返回帖子的完整信息，包括图片/视频、点赞数、评论数、发布者信息等 ### 参数（二选一）: - media_id: 帖子的媒体ID（数字ID） - url: 帖子的完整URL（如 `https://www.instagram.com/p/DUajw4YkorV/`） ### 返回: - `data.items`: 帖子信息列表（通常只有一个元素）     - `id`: 帖子ID     - `code`: 帖子短代码     - `media_type`: 媒体类型（1=图片, 2=视频, 8=合集）     - `like_count`: 点赞数     - `comment_count`: 评论数     - `caption.text`: 帖子文本     - `user`: 发布者信息     - `image_versions2`: 图片版本列表     - `video_versions`: 视频版本列表（视频时存在）     - `carousel_media`: 合集媒体列表（合集时存在）     - `taken_at`: 发布时间戳 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get post details - Support fetching by media_id or post URL - Returns complete post info including images/videos, likes, comments, author info, etc. ### Parameters (one of): - media_id: Post media ID (numeric ID) - url: Full post URL (e.g., `https://www.instagram.com/p/DUajw4YkorV/`) ### Return: - `data.items`: Post info list (usually only one element)     - `id`: Post ID     - `code`: Post shortcode     - `media_type`: Media type (1=image, 2=video, 8=carousel)     - `like_count`: Likes count     - `comment_count`: Comments count     - `caption.text`: Post caption text     - `user`: Publisher info     - `image_versions2`: Image version list     - `video_versions`: Video version list (exists for videos)     - `carousel_media`: Carousel media list (exists for carousels)     - `taken_at`: Published timestamp ### Price: - 0.002 USD/request  ### 示例/Example ``` media_id = \"3800418264661789225\" # 或通过URL / Or by URL # url = \"https://www.instagram.com/p/DUajw4YkorV/\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_info_api_v1_instagram_v3_get_post_info_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object media_id: 帖子媒体ID/Post media ID
        :param object url: 帖子URL/Post URL
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['media_id', 'url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_post_info_api_v1_instagram_v3_get_post_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'media_id' in params:
            query_params.append(('media_id', params['media_id']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_post_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_post_info_by_code_api_v1_instagram_v3_get_post_info_by_code_get(self, **kwargs):  # noqa: E501
        """获取帖子详情(code)/Get post info by shortcode  # noqa: E501

        # [中文] ### 用途: - 通过帖子的短代码（code/shortcode）或URL获取帖子详情 - 短代码即帖子URL中的标识符，如 `https://www.instagram.com/p/DUajw4YkorV/` 中的 `DUajw4YkorV` - 返回帖子的完整信息 ### 参数（二选一）: - code: 帖子短代码（如 DUajw4YkorV） - url: 帖子URL（自动提取短代码） ### 返回: - `data.items`: 帖子信息列表     - `id`: 帖子ID     - `code`: 帖子短代码     - `media_type`: 媒体类型（1=图片, 2=视频, 8=合集）     - `like_count`: 点赞数     - `comment_count`: 评论数     - `caption.text`: 帖子文本     - `user`: 发布者信息     - `image_versions2`: 图片版本列表     - `video_versions`: 视频版本列表（视频时存在）     - `carousel_media`: 合集媒体列表（合集时存在）     - `taken_at`: 发布时间戳 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get post details by shortcode - Shortcode is the identifier in the post URL, e.g., `DUajw4YkorV` from `https://www.instagram.com/p/DUajw4YkorV/` - Returns complete post info ### Parameters: - code: Post shortcode (e.g., DUajw4YkorV) ### Return: - `data.items`: Post info list     - `id`: Post ID     - `code`: Post shortcode     - `media_type`: Media type (1=image, 2=video, 8=carousel)     - `like_count`: Likes count     - `comment_count`: Comments count     - `caption.text`: Post caption text     - `user`: Publisher info     - `image_versions2`: Image version list     - `video_versions`: Video version list (exists for videos)     - `carousel_media`: Carousel media list (exists for carousels)     - `taken_at`: Published timestamp ### Price: - 0.002 USD/request  ### 示例/Example code = \"DUajw4YkorV\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_info_by_code_api_v1_instagram_v3_get_post_info_by_code_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code: 帖子短代码/Post shortcode
        :param object url: 帖子URL（自动提取短代码）/Post URL (auto extract shortcode)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_post_info_by_code_api_v1_instagram_v3_get_post_info_by_code_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_post_info_by_code_api_v1_instagram_v3_get_post_info_by_code_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_post_info_by_code_api_v1_instagram_v3_get_post_info_by_code_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取帖子详情(code)/Get post info by shortcode  # noqa: E501

        # [中文] ### 用途: - 通过帖子的短代码（code/shortcode）或URL获取帖子详情 - 短代码即帖子URL中的标识符，如 `https://www.instagram.com/p/DUajw4YkorV/` 中的 `DUajw4YkorV` - 返回帖子的完整信息 ### 参数（二选一）: - code: 帖子短代码（如 DUajw4YkorV） - url: 帖子URL（自动提取短代码） ### 返回: - `data.items`: 帖子信息列表     - `id`: 帖子ID     - `code`: 帖子短代码     - `media_type`: 媒体类型（1=图片, 2=视频, 8=合集）     - `like_count`: 点赞数     - `comment_count`: 评论数     - `caption.text`: 帖子文本     - `user`: 发布者信息     - `image_versions2`: 图片版本列表     - `video_versions`: 视频版本列表（视频时存在）     - `carousel_media`: 合集媒体列表（合集时存在）     - `taken_at`: 发布时间戳 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get post details by shortcode - Shortcode is the identifier in the post URL, e.g., `DUajw4YkorV` from `https://www.instagram.com/p/DUajw4YkorV/` - Returns complete post info ### Parameters: - code: Post shortcode (e.g., DUajw4YkorV) ### Return: - `data.items`: Post info list     - `id`: Post ID     - `code`: Post shortcode     - `media_type`: Media type (1=image, 2=video, 8=carousel)     - `like_count`: Likes count     - `comment_count`: Comments count     - `caption.text`: Post caption text     - `user`: Publisher info     - `image_versions2`: Image version list     - `video_versions`: Video version list (exists for videos)     - `carousel_media`: Carousel media list (exists for carousels)     - `taken_at`: Published timestamp ### Price: - 0.002 USD/request  ### 示例/Example code = \"DUajw4YkorV\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_info_by_code_api_v1_instagram_v3_get_post_info_by_code_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object code: 帖子短代码/Post shortcode
        :param object url: 帖子URL（自动提取短代码）/Post URL (auto extract shortcode)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_post_info_by_code_api_v1_instagram_v3_get_post_info_by_code_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_post_info_by_code', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_post_oembed_api_v1_instagram_v3_get_post_oembed_get(self, url, **kwargs):  # noqa: E501
        """获取帖子oEmbed内嵌信息/Get post oEmbed info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram帖子的oEmbed内嵌信息 - 返回可直接嵌入网页的HTML代码和帖子元信息 - 适用于需要在第三方网站嵌入Instagram帖子的场景 ### 参数: - url: Instagram帖子的完整URL（如 `https://www.instagram.com/p/xxx/` 或 `https://www.instagram.com/reel/xxx/`） - hidecaption: 是否隐藏帖子文本（默认false） - maxwidth: 嵌入的最大宽度（像素，默认540） ### 返回: - `data.version`: oEmbed版本 - `data.title`: 帖子标题 - `data.author_name`: 作者名称 - `data.author_url`: 作者主页URL - `data.author_id`: 作者ID - `data.media_id`: 媒体ID - `data.provider_name`: 提供者名称（Instagram） - `data.provider_url`: 提供者URL - `data.type`: 类型（rich） - `data.width`: 宽度 - `data.html`: HTML嵌入代码 - `data.thumbnail_url`: 缩略图URL - `data.thumbnail_width`: 缩略图宽度 - `data.thumbnail_height`: 缩略图高度 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram post oEmbed embed info - Returns HTML code for embedding and post metadata - Suitable for embedding Instagram posts on third-party websites ### Parameters: - url: Full Instagram post URL (e.g., `https://www.instagram.com/p/xxx/` or `https://www.instagram.com/reel/xxx/`) - hidecaption: Whether to hide caption (default false) - maxwidth: Max embed width in pixels (default 540) ### Return: - `data.version`: oEmbed version - `data.title`: Post title - `data.author_name`: Author name - `data.author_url`: Author profile URL - `data.author_id`: Author ID - `data.media_id`: Media ID - `data.provider_name`: Provider name (Instagram) - `data.provider_url`: Provider URL - `data.type`: Type (rich) - `data.width`: Width - `data.html`: HTML embed code - `data.thumbnail_url`: Thumbnail URL - `data.thumbnail_width`: Thumbnail width - `data.thumbnail_height`: Thumbnail height ### Price: - 0.002 USD/request  ### 示例/Example url = \"https://www.instagram.com/reel/DUlObENDmJD\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_oembed_api_v1_instagram_v3_get_post_oembed_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: Instagram帖子的完整URL/Full URL of Instagram post (required)
        :param object hidecaption: 是否隐藏帖子文本/Whether to hide caption
        :param object maxwidth: 最大宽度（像素）/Max width in pixels
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_post_oembed_api_v1_instagram_v3_get_post_oembed_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.get_post_oembed_api_v1_instagram_v3_get_post_oembed_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def get_post_oembed_api_v1_instagram_v3_get_post_oembed_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """获取帖子oEmbed内嵌信息/Get post oEmbed info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram帖子的oEmbed内嵌信息 - 返回可直接嵌入网页的HTML代码和帖子元信息 - 适用于需要在第三方网站嵌入Instagram帖子的场景 ### 参数: - url: Instagram帖子的完整URL（如 `https://www.instagram.com/p/xxx/` 或 `https://www.instagram.com/reel/xxx/`） - hidecaption: 是否隐藏帖子文本（默认false） - maxwidth: 嵌入的最大宽度（像素，默认540） ### 返回: - `data.version`: oEmbed版本 - `data.title`: 帖子标题 - `data.author_name`: 作者名称 - `data.author_url`: 作者主页URL - `data.author_id`: 作者ID - `data.media_id`: 媒体ID - `data.provider_name`: 提供者名称（Instagram） - `data.provider_url`: 提供者URL - `data.type`: 类型（rich） - `data.width`: 宽度 - `data.html`: HTML嵌入代码 - `data.thumbnail_url`: 缩略图URL - `data.thumbnail_width`: 缩略图宽度 - `data.thumbnail_height`: 缩略图高度 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram post oEmbed embed info - Returns HTML code for embedding and post metadata - Suitable for embedding Instagram posts on third-party websites ### Parameters: - url: Full Instagram post URL (e.g., `https://www.instagram.com/p/xxx/` or `https://www.instagram.com/reel/xxx/`) - hidecaption: Whether to hide caption (default false) - maxwidth: Max embed width in pixels (default 540) ### Return: - `data.version`: oEmbed version - `data.title`: Post title - `data.author_name`: Author name - `data.author_url`: Author profile URL - `data.author_id`: Author ID - `data.media_id`: Media ID - `data.provider_name`: Provider name (Instagram) - `data.provider_url`: Provider URL - `data.type`: Type (rich) - `data.width`: Width - `data.html`: HTML embed code - `data.thumbnail_url`: Thumbnail URL - `data.thumbnail_width`: Thumbnail width - `data.thumbnail_height`: Thumbnail height ### Price: - 0.002 USD/request  ### 示例/Example url = \"https://www.instagram.com/reel/DUlObENDmJD\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_oembed_api_v1_instagram_v3_get_post_oembed_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: Instagram帖子的完整URL/Full URL of Instagram post (required)
        :param object hidecaption: 是否隐藏帖子文本/Whether to hide caption
        :param object maxwidth: 最大宽度（像素）/Max width in pixels
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['url', 'hidecaption', 'maxwidth']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_post_oembed_api_v1_instagram_v3_get_post_oembed_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `get_post_oembed_api_v1_instagram_v3_get_post_oembed_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501
        if 'hidecaption' in params:
            query_params.append(('hidecaption', params['hidecaption']))  # noqa: E501
        if 'maxwidth' in params:
            query_params.append(('maxwidth', params['maxwidth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_post_oembed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_recommended_reels_api_v1_instagram_v3_get_recommended_reels_get(self, **kwargs):  # noqa: E501
        """获取Reels推荐列表/Get recommended Reels feed  # noqa: E501

        # [中文] ### 用途: - 获取Instagram Reels推荐列表 - 支持分页获取更多Reels ### 参数: - first: 每次获取的Reels数量（默认12） - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取 ### 返回: - `data.edges`: Reels列表     - `node.media`: Reels媒体信息         - `code`: 帖子短代码         - `pk`: 帖子ID         - `like_count`: 点赞数         - `comment_count`: 评论数         - `play_count`: 播放数         - `caption.text`: 描述文本         - `user`: 发布者信息         - `video_versions`: 视频版本列表         - `image_versions2`: 封面图版本列表 - `data.page_info`: 分页信息     - `has_next_page`: 是否有下一页     - `end_cursor`: 下一页游标（传给下次请求的after参数） ### 分页使用方法: 1. 首次请求：只传 `first` 参数 2. 获取响应中的 `data.page_info.end_cursor` 3. 下次请求：传入 `first` 和 `after` (使用上次的end_cursor) 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram Reels recommendation feed - Support pagination to fetch more Reels ### Parameters: - first: Number of Reels to fetch per request (default 12) - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` ### Return: - `data.edges`: Reels list     - `node.media`: Reels media info         - `code`: Post shortcode         - `pk`: Post ID         - `like_count`: Likes count         - `comment_count`: Comments count         - `play_count`: Play count         - `caption.text`: Description text         - `user`: Publisher info         - `video_versions`: Video version list         - `image_versions2`: Cover image version list - `data.page_info`: Pagination info     - `has_next_page`: Whether has next page     - `end_cursor`: Next page cursor (use as after parameter in next request) ### Pagination usage: 1. First request: Only pass `first` parameter 2. Get `data.page_info.end_cursor` from response 3. Next request: Pass `first` and `after` (use end_cursor from previous) 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false ### Price: - 0.002 USD/request  ### 示例/Example first = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recommended_reels_api_v1_instagram_v3_get_recommended_reels_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object first: 获取数量/Number of reels to fetch
        :param object after: 分页游标，首次请求不传，从上一次响应的 page_info.end_cursor 获取/Pagination cursor, omit for first request, get from previous response page_info.end_cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_recommended_reels_api_v1_instagram_v3_get_recommended_reels_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_recommended_reels_api_v1_instagram_v3_get_recommended_reels_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_recommended_reels_api_v1_instagram_v3_get_recommended_reels_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取Reels推荐列表/Get recommended Reels feed  # noqa: E501

        # [中文] ### 用途: - 获取Instagram Reels推荐列表 - 支持分页获取更多Reels ### 参数: - first: 每次获取的Reels数量（默认12） - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取 ### 返回: - `data.edges`: Reels列表     - `node.media`: Reels媒体信息         - `code`: 帖子短代码         - `pk`: 帖子ID         - `like_count`: 点赞数         - `comment_count`: 评论数         - `play_count`: 播放数         - `caption.text`: 描述文本         - `user`: 发布者信息         - `video_versions`: 视频版本列表         - `image_versions2`: 封面图版本列表 - `data.page_info`: 分页信息     - `has_next_page`: 是否有下一页     - `end_cursor`: 下一页游标（传给下次请求的after参数） ### 分页使用方法: 1. 首次请求：只传 `first` 参数 2. 获取响应中的 `data.page_info.end_cursor` 3. 下次请求：传入 `first` 和 `after` (使用上次的end_cursor) 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram Reels recommendation feed - Support pagination to fetch more Reels ### Parameters: - first: Number of Reels to fetch per request (default 12) - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` ### Return: - `data.edges`: Reels list     - `node.media`: Reels media info         - `code`: Post shortcode         - `pk`: Post ID         - `like_count`: Likes count         - `comment_count`: Comments count         - `play_count`: Play count         - `caption.text`: Description text         - `user`: Publisher info         - `video_versions`: Video version list         - `image_versions2`: Cover image version list - `data.page_info`: Pagination info     - `has_next_page`: Whether has next page     - `end_cursor`: Next page cursor (use as after parameter in next request) ### Pagination usage: 1. First request: Only pass `first` parameter 2. Get `data.page_info.end_cursor` from response 3. Next request: Pass `first` and `after` (use end_cursor from previous) 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false ### Price: - 0.002 USD/request  ### 示例/Example first = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recommended_reels_api_v1_instagram_v3_get_recommended_reels_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object first: 获取数量/Number of reels to fetch
        :param object after: 分页游标，首次请求不传，从上一次响应的 page_info.end_cursor 获取/Pagination cursor, omit for first request, get from previous response page_info.end_cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['first', 'after']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recommended_reels_api_v1_instagram_v3_get_recommended_reels_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'first' in params:
            query_params.append(('first', params['first']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_recommended_reels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_about_api_v1_instagram_v3_get_user_about_get(self, **kwargs):  # noqa: E501
        """获取用户账户简介/Get user about info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的账户简介信息（About This Account） - 包含账户创建日期、所在地区、曾用名等信息 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 ### 返回: - 账户创建日期 - 账户所在地区/国家 - 曾用名历史 - 其他账户相关信息 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's About This Account information - Including account creation date, location, former usernames, etc. ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Return: - Account creation date - Account location/country - Former username history - Other account related info ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"791258468\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_about_api_v1_instagram_v3_get_user_about_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_about_api_v1_instagram_v3_get_user_about_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_about_api_v1_instagram_v3_get_user_about_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_about_api_v1_instagram_v3_get_user_about_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户账户简介/Get user about info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的账户简介信息（About This Account） - 包含账户创建日期、所在地区、曾用名等信息 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 ### 返回: - 账户创建日期 - 账户所在地区/国家 - 曾用名历史 - 其他账户相关信息 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's About This Account information - Including account creation date, location, former usernames, etc. ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Return: - Account creation date - Account location/country - Former username history - Other account related info ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"791258468\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_about_api_v1_instagram_v3_get_user_about_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_about_api_v1_instagram_v3_get_user_about_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_user_about', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_brief_api_v1_instagram_v3_get_user_brief_get(self, user_id, username, **kwargs):  # noqa: E501
        """获取用户短详情/Get user brief info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的短详情/悬浮卡片信息 - 返回用户核心信息，响应速度比 get_user_profile 更快 - 适用于批量获取用户摘要信息的场景 ### 参数: - user_id: Instagram用户ID（数字） - username: Instagram用户名 ### 返回: - `data.id`: 用户ID - `data.username`: 用户名 - `data.full_name`: 全名 - `data.biography`: 个人简介 - `data.profile_pic_url`: 头像URL - `data.is_verified`: 是否认证 - `data.is_private`: 是否私密账号 - `data.edge_followed_by.count`: 粉丝数 - `data.edge_follow.count`: 关注数 - `data.edge_owner_to_timeline_media`: 最近帖子预览 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user brief/hover card info - Returns core user info, faster response than get_user_profile - Suitable for batch fetching user summary info ### Parameters: - user_id: Instagram user ID (numeric) - username: Instagram username ### Return: - `data.id`: User ID - `data.username`: Username - `data.full_name`: Full name - `data.biography`: Biography - `data.profile_pic_url`: Profile picture URL - `data.is_verified`: Whether verified - `data.is_private`: Whether private account - `data.edge_followed_by.count`: Followers count - `data.edge_follow.count`: Following count - `data.edge_owner_to_timeline_media`: Recent posts preview ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"77919494141\" username = \"emo.__0202\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_brief_api_v1_instagram_v3_get_user_brief_get(user_id, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object username: 用户名/Username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_brief_api_v1_instagram_v3_get_user_brief_get_with_http_info(user_id, username, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_brief_api_v1_instagram_v3_get_user_brief_get_with_http_info(user_id, username, **kwargs)  # noqa: E501
            return data

    def get_user_brief_api_v1_instagram_v3_get_user_brief_get_with_http_info(self, user_id, username, **kwargs):  # noqa: E501
        """获取用户短详情/Get user brief info  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的短详情/悬浮卡片信息 - 返回用户核心信息，响应速度比 get_user_profile 更快 - 适用于批量获取用户摘要信息的场景 ### 参数: - user_id: Instagram用户ID（数字） - username: Instagram用户名 ### 返回: - `data.id`: 用户ID - `data.username`: 用户名 - `data.full_name`: 全名 - `data.biography`: 个人简介 - `data.profile_pic_url`: 头像URL - `data.is_verified`: 是否认证 - `data.is_private`: 是否私密账号 - `data.edge_followed_by.count`: 粉丝数 - `data.edge_follow.count`: 关注数 - `data.edge_owner_to_timeline_media`: 最近帖子预览 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user brief/hover card info - Returns core user info, faster response than get_user_profile - Suitable for batch fetching user summary info ### Parameters: - user_id: Instagram user ID (numeric) - username: Instagram username ### Return: - `data.id`: User ID - `data.username`: Username - `data.full_name`: Full name - `data.biography`: Biography - `data.profile_pic_url`: Profile picture URL - `data.is_verified`: Whether verified - `data.is_private`: Whether private account - `data.edge_followed_by.count`: Followers count - `data.edge_follow.count`: Following count - `data.edge_owner_to_timeline_media`: Recent posts preview ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"77919494141\" username = \"emo.__0202\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_brief_api_v1_instagram_v3_get_user_brief_get_with_http_info(user_id, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object username: 用户名/Username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_brief_api_v1_instagram_v3_get_user_brief_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_brief_api_v1_instagram_v3_get_user_brief_get`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_user_brief_api_v1_instagram_v3_get_user_brief_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_user_brief', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_followers_api_v1_instagram_v3_get_user_followers_get(self, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Get user followers list  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的粉丝列表 - 返回关注该用户的所有账号信息 - 支持分页获取 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - count: 每次获取数量（默认12） - max_id: 分页游标，首次请求不传，从上一次响应的 `data.next_max_id` 获取 ### 返回: - `data.users`: 粉丝用户列表     - `pk`: 用户ID     - `username`: 用户名     - `full_name`: 全名     - `is_private`: 是否私密账号     - `is_verified`: 是否认证     - `profile_pic_url`: 头像URL - `data.next_max_id`: 下一页分页游标（传给下次请求的max_id参数） - `data.big_list`: 是否有更多数据 - `data.page_size`: 每页数量 - `data.status`: 状态 ### 分页使用方法: 1. 首次请求：只传 `user_id` 和 `count` 参数 2. 获取响应中的 `data.next_max_id` 3. 下次请求：传入 `user_id`、`count` 和 `max_id` (使用上次的next_max_id) 4. 重复步骤 2-3 直到响应中没有 `next_max_id` 字段 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's followers list - Returns all accounts that follow this user - Support pagination ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - count: Number of users to fetch per request (default 12) - max_id: Pagination cursor, omit for first request, get from previous response `data.next_max_id` ### Return: - `data.users`: Followers user list     - `pk`: User ID     - `username`: Username     - `full_name`: Full name     - `is_private`: Whether private account     - `is_verified`: Whether verified     - `profile_pic_url`: Profile picture URL - `data.next_max_id`: Next page cursor (use as max_id in next request) - `data.big_list`: Whether has more data - `data.page_size`: Page size - `data.status`: Status ### Pagination usage: 1. First request: Only pass `user_id` and `count` parameters 2. Get `data.next_max_id` from response 3. Next request: Pass `user_id`, `count`, and `max_id` (use next_max_id from previous) 4. Repeat steps 2-3 until response has no `next_max_id` field ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\" count = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_followers_api_v1_instagram_v3_get_user_followers_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object count: 每次获取数量/Number of users to fetch per request
        :param object max_id: 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_followers_api_v1_instagram_v3_get_user_followers_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_followers_api_v1_instagram_v3_get_user_followers_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_followers_api_v1_instagram_v3_get_user_followers_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Get user followers list  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的粉丝列表 - 返回关注该用户的所有账号信息 - 支持分页获取 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - count: 每次获取数量（默认12） - max_id: 分页游标，首次请求不传，从上一次响应的 `data.next_max_id` 获取 ### 返回: - `data.users`: 粉丝用户列表     - `pk`: 用户ID     - `username`: 用户名     - `full_name`: 全名     - `is_private`: 是否私密账号     - `is_verified`: 是否认证     - `profile_pic_url`: 头像URL - `data.next_max_id`: 下一页分页游标（传给下次请求的max_id参数） - `data.big_list`: 是否有更多数据 - `data.page_size`: 每页数量 - `data.status`: 状态 ### 分页使用方法: 1. 首次请求：只传 `user_id` 和 `count` 参数 2. 获取响应中的 `data.next_max_id` 3. 下次请求：传入 `user_id`、`count` 和 `max_id` (使用上次的next_max_id) 4. 重复步骤 2-3 直到响应中没有 `next_max_id` 字段 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's followers list - Returns all accounts that follow this user - Support pagination ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - count: Number of users to fetch per request (default 12) - max_id: Pagination cursor, omit for first request, get from previous response `data.next_max_id` ### Return: - `data.users`: Followers user list     - `pk`: User ID     - `username`: Username     - `full_name`: Full name     - `is_private`: Whether private account     - `is_verified`: Whether verified     - `profile_pic_url`: Profile picture URL - `data.next_max_id`: Next page cursor (use as max_id in next request) - `data.big_list`: Whether has more data - `data.page_size`: Page size - `data.status`: Status ### Pagination usage: 1. First request: Only pass `user_id` and `count` parameters 2. Get `data.next_max_id` from response 3. Next request: Pass `user_id`, `count`, and `max_id` (use next_max_id from previous) 4. Repeat steps 2-3 until response has no `next_max_id` field ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\" count = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_followers_api_v1_instagram_v3_get_user_followers_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object count: 每次获取数量/Number of users to fetch per request
        :param object max_id: 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'username', 'count', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_followers_api_v1_instagram_v3_get_user_followers_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
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
            '/api/v1/instagram/v3/get_user_followers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_following_api_v1_instagram_v3_get_user_following_get(self, **kwargs):  # noqa: E501
        """获取用户关注列表/Get user following list  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的关注列表 - 返回用户关注的所有账号信息 - 支持分页获取 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - count: 每次获取数量（默认12） - max_id: 分页游标，首次请求不传，从上一次响应的 `data.next_max_id` 获取 ### 返回: - `data.users`: 关注用户列表     - `pk`: 用户ID     - `username`: 用户名     - `full_name`: 全名     - `is_private`: 是否私密账号     - `is_verified`: 是否认证     - `profile_pic_url`: 头像URL - `data.next_max_id`: 下一页分页游标（传给下次请求的max_id参数） - `data.big_list`: 是否有更多数据 - `data.page_size`: 每页数量 - `data.status`: 状态 ### 分页使用方法: 1. 首次请求：只传 `user_id` 和 `count` 参数 2. 获取响应中的 `data.next_max_id` 3. 下次请求：传入 `user_id`、`count` 和 `max_id` (使用上次的next_max_id) 4. 重复步骤 2-3 直到响应中没有 `next_max_id` 字段 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's following list - Returns all accounts the user follows - Support pagination ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - count: Number of users to fetch per request (default 12) - max_id: Pagination cursor, omit for first request, get from previous response `data.next_max_id` ### Return: - `data.users`: Following user list     - `pk`: User ID     - `username`: Username     - `full_name`: Full name     - `is_private`: Whether private account     - `is_verified`: Whether verified     - `profile_pic_url`: Profile picture URL - `data.next_max_id`: Next page cursor (use as max_id in next request) - `data.big_list`: Whether has more data - `data.page_size`: Page size - `data.status`: Status ### Pagination usage: 1. First request: Only pass `user_id` and `count` parameters 2. Get `data.next_max_id` from response 3. Next request: Pass `user_id`, `count`, and `max_id` (use next_max_id from previous) 4. Repeat steps 2-3 until response has no `next_max_id` field ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\" count = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_following_api_v1_instagram_v3_get_user_following_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object count: 每次获取数量/Number of users to fetch per request
        :param object max_id: 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_following_api_v1_instagram_v3_get_user_following_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_following_api_v1_instagram_v3_get_user_following_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_following_api_v1_instagram_v3_get_user_following_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户关注列表/Get user following list  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的关注列表 - 返回用户关注的所有账号信息 - 支持分页获取 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - count: 每次获取数量（默认12） - max_id: 分页游标，首次请求不传，从上一次响应的 `data.next_max_id` 获取 ### 返回: - `data.users`: 关注用户列表     - `pk`: 用户ID     - `username`: 用户名     - `full_name`: 全名     - `is_private`: 是否私密账号     - `is_verified`: 是否认证     - `profile_pic_url`: 头像URL - `data.next_max_id`: 下一页分页游标（传给下次请求的max_id参数） - `data.big_list`: 是否有更多数据 - `data.page_size`: 每页数量 - `data.status`: 状态 ### 分页使用方法: 1. 首次请求：只传 `user_id` 和 `count` 参数 2. 获取响应中的 `data.next_max_id` 3. 下次请求：传入 `user_id`、`count` 和 `max_id` (使用上次的next_max_id) 4. 重复步骤 2-3 直到响应中没有 `next_max_id` 字段 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's following list - Returns all accounts the user follows - Support pagination ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - count: Number of users to fetch per request (default 12) - max_id: Pagination cursor, omit for first request, get from previous response `data.next_max_id` ### Return: - `data.users`: Following user list     - `pk`: User ID     - `username`: Username     - `full_name`: Full name     - `is_private`: Whether private account     - `is_verified`: Whether verified     - `profile_pic_url`: Profile picture URL - `data.next_max_id`: Next page cursor (use as max_id in next request) - `data.big_list`: Whether has more data - `data.page_size`: Page size - `data.status`: Status ### Pagination usage: 1. First request: Only pass `user_id` and `count` parameters 2. Get `data.next_max_id` from response 3. Next request: Pass `user_id`, `count`, and `max_id` (use next_max_id from previous) 4. Repeat steps 2-3 until response has no `next_max_id` field ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\" count = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_following_api_v1_instagram_v3_get_user_following_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object count: 每次获取数量/Number of users to fetch per request
        :param object max_id: 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'username', 'count', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_following_api_v1_instagram_v3_get_user_following_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
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
            '/api/v1/instagram/v3/get_user_following', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_highlights_api_v1_instagram_v3_get_user_highlights_get(self, **kwargs):  # noqa: E501
        """获取用户精选Highlights列表/Get user highlights  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的精选Highlights列表 - 返回用户创建的所有精选集合 - 支持分页获取 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - first: 每次获取的精选数量（默认10） - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取 ### 返回: - `data.edges`: 精选列表     - `node.id`: 精选ID（格式: highlight:xxx）     - `node.title`: 精选标题     - `node.cover_media`: 封面媒体信息     - `node.cover_media_cropped_thumbnail`: 裁剪后的封面缩略图     - `node.media_count`: 精选中的故事数量 - `data.page_info`: 分页信息     - `has_next_page`: 是否有下一页     - `end_cursor`: 下一页游标（传给下次请求的after参数） ### 分页使用方法: 1. 首次请求：只传 `user_id` 和 `first` 参数 2. 获取响应中的 `data.page_info.end_cursor` 3. 下次请求：传入 `user_id`、`first` 和 `after` (使用上次的end_cursor) 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's Highlights list - Returns all highlight collections created by the user - Support pagination ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - first: Number of highlights to fetch per request (default 10) - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` ### Return: - `data.edges`: Highlights list     - `node.id`: Highlight ID (format: highlight:xxx)     - `node.title`: Highlight title     - `node.cover_media`: Cover media info     - `node.cover_media_cropped_thumbnail`: Cropped cover thumbnail     - `node.media_count`: Number of stories in highlight - `data.page_info`: Pagination info     - `has_next_page`: Whether has next page     - `end_cursor`: Next page cursor (use as after parameter in next request) ### Pagination usage: 1. First request: Only pass `user_id` and `first` parameters 2. Get `data.page_info.end_cursor` from response 3. Next request: Pass `user_id`, `first`, and `after` (use end_cursor from previous) 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\" first = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_highlights_api_v1_instagram_v3_get_user_highlights_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object first: 获取数量/Number of highlights to fetch
        :param object after: 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_highlights_api_v1_instagram_v3_get_user_highlights_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_highlights_api_v1_instagram_v3_get_user_highlights_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_highlights_api_v1_instagram_v3_get_user_highlights_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户精选Highlights列表/Get user highlights  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的精选Highlights列表 - 返回用户创建的所有精选集合 - 支持分页获取 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - first: 每次获取的精选数量（默认10） - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取 ### 返回: - `data.edges`: 精选列表     - `node.id`: 精选ID（格式: highlight:xxx）     - `node.title`: 精选标题     - `node.cover_media`: 封面媒体信息     - `node.cover_media_cropped_thumbnail`: 裁剪后的封面缩略图     - `node.media_count`: 精选中的故事数量 - `data.page_info`: 分页信息     - `has_next_page`: 是否有下一页     - `end_cursor`: 下一页游标（传给下次请求的after参数） ### 分页使用方法: 1. 首次请求：只传 `user_id` 和 `first` 参数 2. 获取响应中的 `data.page_info.end_cursor` 3. 下次请求：传入 `user_id`、`first` 和 `after` (使用上次的end_cursor) 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's Highlights list - Returns all highlight collections created by the user - Support pagination ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - first: Number of highlights to fetch per request (default 10) - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` ### Return: - `data.edges`: Highlights list     - `node.id`: Highlight ID (format: highlight:xxx)     - `node.title`: Highlight title     - `node.cover_media`: Cover media info     - `node.cover_media_cropped_thumbnail`: Cropped cover thumbnail     - `node.media_count`: Number of stories in highlight - `data.page_info`: Pagination info     - `has_next_page`: Whether has next page     - `end_cursor`: Next page cursor (use as after parameter in next request) ### Pagination usage: 1. First request: Only pass `user_id` and `first` parameters 2. Get `data.page_info.end_cursor` from response 3. Next request: Pass `user_id`, `first`, and `after` (use end_cursor from previous) 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\" first = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_highlights_api_v1_instagram_v3_get_user_highlights_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object first: 获取数量/Number of highlights to fetch
        :param object after: 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'username', 'first', 'after']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_highlights_api_v1_instagram_v3_get_user_highlights_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'first' in params:
            query_params.append(('first', params['first']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_user_highlights', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_posts_api_v1_instagram_v3_get_user_posts_get(self, **kwargs):  # noqa: E501
        """获取用户帖子列表/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的帖子列表 - 支持分页获取，可获取用户的所有帖子 ### 参数（二选一）: - username: Instagram用户名 - user_id: Instagram用户ID（数字，内部会自动转换为用户名） - first: 每次获取的帖子数量（默认12） - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取 ### 返回: - `data.edges`: 帖子列表     - `node.id`: 帖子ID     - `node.code`: 帖子短代码     - `node.display_url`: 展示图片URL     - `node.taken_at`: 发布时间戳     - `node.like_count`: 点赞数     - `node.comment_count`: 评论数     - `node.caption.text`: 帖子文本 - `data.page_info`: 分页信息     - `has_next_page`: 是否有下一页     - `end_cursor`: 下一页游标（传给下次请求的after参数） ### 分页使用方法: 1. 首次请求：只传 `username` 和 `first` 参数 2. 获取响应中的 `data.page_info.end_cursor` 3. 下次请求：传入 `username`、`first` 和 `after` (使用上次的end_cursor) 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's post list - Support pagination to fetch all user posts ### Parameters (one of): - username: Instagram username - user_id: Instagram user ID (numeric, will be auto-converted to username) ### Other parameters: - first: Number of posts to fetch per request (default 12) - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` ### Return: - `data.edges`: Post list     - `node.id`: Post ID     - `node.code`: Post shortcode     - `node.display_url`: Display image URL     - `node.taken_at`: Published timestamp     - `node.like_count`: Likes count     - `node.comment_count`: Comments count     - `node.caption.text`: Post caption text - `data.page_info`: Pagination info     - `has_next_page`: Whether has next page     - `end_cursor`: Next page cursor (use as after parameter in next request) ### Pagination usage: 1. First request: Only pass `username` and `first` parameters 2. Get `data.page_info.end_cursor` from response 3. Next request: Pass `username`, `first`, and `after` (use end_cursor from previous) 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false ### Price: - 0.002 USD/request  ### 示例/Example ``` # 第一页 / First page username = \"liensue.talks\" first = 12  # 第二页 / Second page # username = \"liensue.talks\" # first = 12 # after = \"QVFCcmN1YlF...\"  # 从第一页响应中获取 / Get from first page response ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_posts_api_v1_instagram_v3_get_user_posts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object first: 获取帖子数量/Number of posts to fetch
        :param object after: 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_posts_api_v1_instagram_v3_get_user_posts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_posts_api_v1_instagram_v3_get_user_posts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_posts_api_v1_instagram_v3_get_user_posts_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户帖子列表/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的帖子列表 - 支持分页获取，可获取用户的所有帖子 ### 参数（二选一）: - username: Instagram用户名 - user_id: Instagram用户ID（数字，内部会自动转换为用户名） - first: 每次获取的帖子数量（默认12） - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取 ### 返回: - `data.edges`: 帖子列表     - `node.id`: 帖子ID     - `node.code`: 帖子短代码     - `node.display_url`: 展示图片URL     - `node.taken_at`: 发布时间戳     - `node.like_count`: 点赞数     - `node.comment_count`: 评论数     - `node.caption.text`: 帖子文本 - `data.page_info`: 分页信息     - `has_next_page`: 是否有下一页     - `end_cursor`: 下一页游标（传给下次请求的after参数） ### 分页使用方法: 1. 首次请求：只传 `username` 和 `first` 参数 2. 获取响应中的 `data.page_info.end_cursor` 3. 下次请求：传入 `username`、`first` 和 `after` (使用上次的end_cursor) 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's post list - Support pagination to fetch all user posts ### Parameters (one of): - username: Instagram username - user_id: Instagram user ID (numeric, will be auto-converted to username) ### Other parameters: - first: Number of posts to fetch per request (default 12) - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` ### Return: - `data.edges`: Post list     - `node.id`: Post ID     - `node.code`: Post shortcode     - `node.display_url`: Display image URL     - `node.taken_at`: Published timestamp     - `node.like_count`: Likes count     - `node.comment_count`: Comments count     - `node.caption.text`: Post caption text - `data.page_info`: Pagination info     - `has_next_page`: Whether has next page     - `end_cursor`: Next page cursor (use as after parameter in next request) ### Pagination usage: 1. First request: Only pass `username` and `first` parameters 2. Get `data.page_info.end_cursor` from response 3. Next request: Pass `username`, `first`, and `after` (use end_cursor from previous) 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false ### Price: - 0.002 USD/request  ### 示例/Example ``` # 第一页 / First page username = \"liensue.talks\" first = 12  # 第二页 / Second page # username = \"liensue.talks\" # first = 12 # after = \"QVFCcmN1YlF...\"  # 从第一页响应中获取 / Get from first page response ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_posts_api_v1_instagram_v3_get_user_posts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username
        :param object user_id: 用户ID/User ID
        :param object first: 获取帖子数量/Number of posts to fetch
        :param object after: 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'user_id', 'first', 'after']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_posts_api_v1_instagram_v3_get_user_posts_get" % key
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
        if 'first' in params:
            query_params.append(('first', params['first']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_user_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_profile_api_v1_instagram_v3_get_user_profile_get(self, **kwargs):  # noqa: E501
        """获取用户信息/Get user profile  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的完整个人资料信息 - 包含用户基本信息、统计数据、最近帖子等 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 ### 返回: - `data.user.id`: 用户ID - `data.user.username`: 用户名 - `data.user.full_name`: 全名 - `data.user.biography`: 个人简介 - `data.user.external_url`: 外部链接 - `data.user.profile_pic_url`: 头像URL（标准） - `data.user.profile_pic_url_hd`: 头像URL（高清） - `data.user.is_verified`: 是否认证 - `data.user.is_private`: 是否私密账号 - `data.user.edge_followed_by.count`: 粉丝数 - `data.user.edge_follow.count`: 关注数 - `data.user.edge_owner_to_timeline_media.count`: 帖子总数 - `data.user.edge_felix_video_timeline.count`: Reels/视频数 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get complete Instagram user profile information - Including basic info, statistics, recent posts, etc. ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Return: - `data.user.id`: User ID - `data.user.username`: Username - `data.user.full_name`: Full name - `data.user.biography`: Biography - `data.user.external_url`: External URL - `data.user.profile_pic_url`: Profile picture URL (standard) - `data.user.profile_pic_url_hd`: Profile picture URL (HD) - `data.user.is_verified`: Whether verified - `data.user.is_private`: Whether private account - `data.user.edge_followed_by.count`: Followers count - `data.user.edge_follow.count`: Following count - `data.user.edge_owner_to_timeline_media.count`: Total posts count - `data.user.edge_felix_video_timeline.count`: Reels/videos count ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_profile_api_v1_instagram_v3_get_user_profile_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_profile_api_v1_instagram_v3_get_user_profile_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_profile_api_v1_instagram_v3_get_user_profile_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_profile_api_v1_instagram_v3_get_user_profile_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户信息/Get user profile  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的完整个人资料信息 - 包含用户基本信息、统计数据、最近帖子等 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 ### 返回: - `data.user.id`: 用户ID - `data.user.username`: 用户名 - `data.user.full_name`: 全名 - `data.user.biography`: 个人简介 - `data.user.external_url`: 外部链接 - `data.user.profile_pic_url`: 头像URL（标准） - `data.user.profile_pic_url_hd`: 头像URL（高清） - `data.user.is_verified`: 是否认证 - `data.user.is_private`: 是否私密账号 - `data.user.edge_followed_by.count`: 粉丝数 - `data.user.edge_follow.count`: 关注数 - `data.user.edge_owner_to_timeline_media.count`: 帖子总数 - `data.user.edge_felix_video_timeline.count`: Reels/视频数 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get complete Instagram user profile information - Including basic info, statistics, recent posts, etc. ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Return: - `data.user.id`: User ID - `data.user.username`: Username - `data.user.full_name`: Full name - `data.user.biography`: Biography - `data.user.external_url`: External URL - `data.user.profile_pic_url`: Profile picture URL (standard) - `data.user.profile_pic_url_hd`: Profile picture URL (HD) - `data.user.is_verified`: Whether verified - `data.user.is_private`: Whether private account - `data.user.edge_followed_by.count`: Followers count - `data.user.edge_follow.count`: Following count - `data.user.edge_owner_to_timeline_media.count`: Total posts count - `data.user.edge_felix_video_timeline.count`: Reels/videos count ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_profile_api_v1_instagram_v3_get_user_profile_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_profile_api_v1_instagram_v3_get_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_user_profile', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_reels_api_v1_instagram_v3_get_user_reels_get(self, **kwargs):  # noqa: E501
        """获取用户Reels列表/Get user reels  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的Reels列表 - 支持分页获取用户发布的所有Reels ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - first: 每次获取的Reels数量（默认12） - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取 ### 返回: - `data.edges`: Reels列表     - `node.media`: Reels媒体信息         - `code`: 帖子短代码         - `pk`: 帖子ID         - `like_count`: 点赞数         - `comment_count`: 评论数         - `play_count`: 播放数         - `caption.text`: 描述文本         - `user`: 发布者信息         - `video_versions`: 视频版本列表         - `image_versions2`: 封面图版本列表 - `data.page_info`: 分页信息     - `has_next_page`: 是否有下一页     - `end_cursor`: 下一页游标（传给下次请求的after参数） ### 分页使用方法: 1. 首次请求：只传 `user_id` 和 `first` 参数 2. 获取响应中的 `data.page_info.end_cursor` 3. 下次请求：传入 `user_id`、`first` 和 `after` (使用上次的end_cursor) 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's Reels list - Support pagination to fetch all user's Reels ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - first: Number of Reels to fetch per request (default 12) - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` ### Return: - `data.edges`: Reels list     - `node.media`: Reels media info         - `code`: Post shortcode         - `pk`: Post ID         - `like_count`: Likes count         - `comment_count`: Comments count         - `play_count`: Play count         - `caption.text`: Description text         - `user`: Publisher info         - `video_versions`: Video version list         - `image_versions2`: Cover image version list - `data.page_info`: Pagination info     - `has_next_page`: Whether has next page     - `end_cursor`: Next page cursor (use as after parameter in next request) ### Pagination usage: 1. First request: Only pass `user_id` and `first` parameters 2. Get `data.page_info.end_cursor` from response 3. Next request: Pass `user_id`, `first`, and `after` (use end_cursor from previous) 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\" first = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_reels_api_v1_instagram_v3_get_user_reels_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object first: 获取数量/Number of reels to fetch
        :param object after: 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_reels_api_v1_instagram_v3_get_user_reels_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_reels_api_v1_instagram_v3_get_user_reels_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_reels_api_v1_instagram_v3_get_user_reels_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户Reels列表/Get user reels  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的Reels列表 - 支持分页获取用户发布的所有Reels ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - first: 每次获取的Reels数量（默认12） - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取 ### 返回: - `data.edges`: Reels列表     - `node.media`: Reels媒体信息         - `code`: 帖子短代码         - `pk`: 帖子ID         - `like_count`: 点赞数         - `comment_count`: 评论数         - `play_count`: 播放数         - `caption.text`: 描述文本         - `user`: 发布者信息         - `video_versions`: 视频版本列表         - `image_versions2`: 封面图版本列表 - `data.page_info`: 分页信息     - `has_next_page`: 是否有下一页     - `end_cursor`: 下一页游标（传给下次请求的after参数） ### 分页使用方法: 1. 首次请求：只传 `user_id` 和 `first` 参数 2. 获取响应中的 `data.page_info.end_cursor` 3. 下次请求：传入 `user_id`、`first` 和 `after` (使用上次的end_cursor) 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's Reels list - Support pagination to fetch all user's Reels ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - first: Number of Reels to fetch per request (default 12) - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` ### Return: - `data.edges`: Reels list     - `node.media`: Reels media info         - `code`: Post shortcode         - `pk`: Post ID         - `like_count`: Likes count         - `comment_count`: Comments count         - `play_count`: Play count         - `caption.text`: Description text         - `user`: Publisher info         - `video_versions`: Video version list         - `image_versions2`: Cover image version list - `data.page_info`: Pagination info     - `has_next_page`: Whether has next page     - `end_cursor`: Next page cursor (use as after parameter in next request) ### Pagination usage: 1. First request: Only pass `user_id` and `first` parameters 2. Get `data.page_info.end_cursor` from response 3. Next request: Pass `user_id`, `first`, and `after` (use end_cursor from previous) 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\" first = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_reels_api_v1_instagram_v3_get_user_reels_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object first: 获取数量/Number of reels to fetch
        :param object after: 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'username', 'first', 'after']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_reels_api_v1_instagram_v3_get_user_reels_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'first' in params:
            query_params.append(('first', params['first']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_user_reels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_stories_api_v1_instagram_v3_get_user_stories_get(self, **kwargs):  # noqa: E501
        """获取用户Stories（快拍）/Get user stories  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的Stories（快拍）列表 - 即点击用户头像后展示的24小时内发布的快拍内容 - 支持同时获取多个用户的Stories ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - reel_ids: 用户ID列表，逗号分隔（可选，如不提供则仅查询user_id指定的用户）     - 例如: `58208242181,791258468`     - 可同时查询多个用户的Stories ### 返回: - `data.reels_media`: Stories列表（按用户分组）     - `id`: 用户ID     - `user`: 用户信息         - `username`: 用户名         - `full_name`: 全名         - `profile_pic_url`: 头像URL     - `items`: Stories条目列表         - `id`: Story ID         - `pk`: Story PK         - `taken_at`: 发布时间戳         - `media_type`: 媒体类型（1=图片, 2=视频）         - `image_versions2`: 图片版本列表         - `video_versions`: 视频版本列表（视频时存在）         - `story_cta`: Story链接（如果有） - `data.reels`: Stories详细信息 ### 注意: - Stories有24小时有效期，过期后无法获取 - 私密账号的Stories需要关注后才能查看 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's Stories list - Stories displayed when clicking on user's profile picture (published within 24 hours) - Support fetching multiple users' Stories at once ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - reel_ids: User ID list, comma separated (optional, if not provided only queries the user_id)     - Example: `58208242181,791258468`     - Can query multiple users' Stories at once ### Return: - `data.reels_media`: Stories list (grouped by user)     - `id`: User ID     - `user`: User info         - `username`: Username         - `full_name`: Full name         - `profile_pic_url`: Profile picture URL     - `items`: Stories item list         - `id`: Story ID         - `pk`: Story PK         - `taken_at`: Published timestamp         - `media_type`: Media type (1=image, 2=video)         - `image_versions2`: Image version list         - `video_versions`: Video version list (exists for videos)         - `story_cta`: Story link (if any) - `data.reels`: Stories detailed info ### Note: - Stories have a 24-hour expiration, cannot be fetched after expiration - Private account's Stories require following to view ### Price: - 0.002 USD/request  ### 示例/Example ``` user_id = \"58208242181\" # reel_ids = \"58208242181,791258468\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_stories_api_v1_instagram_v3_get_user_stories_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object reel_ids: 用户ID列表，逗号分隔，可同时获取多个用户的Stories（如不提供则仅查询user_id）/User ID list, comma separated, fetch multiple users' stories at once (if not provided, only queries user_id)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_stories_api_v1_instagram_v3_get_user_stories_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_stories_api_v1_instagram_v3_get_user_stories_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_stories_api_v1_instagram_v3_get_user_stories_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户Stories（快拍）/Get user stories  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户的Stories（快拍）列表 - 即点击用户头像后展示的24小时内发布的快拍内容 - 支持同时获取多个用户的Stories ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - reel_ids: 用户ID列表，逗号分隔（可选，如不提供则仅查询user_id指定的用户）     - 例如: `58208242181,791258468`     - 可同时查询多个用户的Stories ### 返回: - `data.reels_media`: Stories列表（按用户分组）     - `id`: 用户ID     - `user`: 用户信息         - `username`: 用户名         - `full_name`: 全名         - `profile_pic_url`: 头像URL     - `items`: Stories条目列表         - `id`: Story ID         - `pk`: Story PK         - `taken_at`: 发布时间戳         - `media_type`: 媒体类型（1=图片, 2=视频）         - `image_versions2`: 图片版本列表         - `video_versions`: 视频版本列表（视频时存在）         - `story_cta`: Story链接（如果有） - `data.reels`: Stories详细信息 ### 注意: - Stories有24小时有效期，过期后无法获取 - 私密账号的Stories需要关注后才能查看 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's Stories list - Stories displayed when clicking on user's profile picture (published within 24 hours) - Support fetching multiple users' Stories at once ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - reel_ids: User ID list, comma separated (optional, if not provided only queries the user_id)     - Example: `58208242181,791258468`     - Can query multiple users' Stories at once ### Return: - `data.reels_media`: Stories list (grouped by user)     - `id`: User ID     - `user`: User info         - `username`: Username         - `full_name`: Full name         - `profile_pic_url`: Profile picture URL     - `items`: Stories item list         - `id`: Story ID         - `pk`: Story PK         - `taken_at`: Published timestamp         - `media_type`: Media type (1=image, 2=video)         - `image_versions2`: Image version list         - `video_versions`: Video version list (exists for videos)         - `story_cta`: Story link (if any) - `data.reels`: Stories detailed info ### Note: - Stories have a 24-hour expiration, cannot be fetched after expiration - Private account's Stories require following to view ### Price: - 0.002 USD/request  ### 示例/Example ``` user_id = \"58208242181\" # reel_ids = \"58208242181,791258468\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_stories_api_v1_instagram_v3_get_user_stories_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object reel_ids: 用户ID列表，逗号分隔，可同时获取多个用户的Stories（如不提供则仅查询user_id）/User ID list, comma separated, fetch multiple users' stories at once (if not provided, only queries user_id)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'username', 'reel_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_stories_api_v1_instagram_v3_get_user_stories_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'reel_ids' in params:
            query_params.append(('reel_ids', params['reel_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_user_stories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_tagged_posts_api_v1_instagram_v3_get_user_tagged_posts_get(self, **kwargs):  # noqa: E501
        """获取用户被标记的帖子/Get user tagged posts  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户被标记（tagged）的帖子列表 - 即其他用户在帖子中标记了该用户的内容 - 支持分页获取 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - first: 每次获取的帖子数量（默认12） - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取 ### 返回: - `data.edges`: 帖子列表     - `node.id`: 帖子ID     - `node.code`: 帖子短代码     - `node.display_url`: 展示图片URL     - `node.taken_at`: 发布时间戳     - `node.like_count`: 点赞数     - `node.comment_count`: 评论数     - `node.caption.text`: 帖子文本     - `node.user`: 发帖者信息 - `data.page_info`: 分页信息     - `has_next_page`: 是否有下一页     - `end_cursor`: 下一页游标（传给下次请求的after参数） ### 分页使用方法: 1. 首次请求：只传 `user_id` 和 `first` 参数 2. 获取响应中的 `data.page_info.end_cursor` 3. 下次请求：传入 `user_id`、`first` 和 `after` (使用上次的end_cursor) 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's tagged posts list - Posts where other users tagged this user - Support pagination ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - first: Number of posts to fetch per request (default 12) - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` ### Return: - `data.edges`: Post list     - `node.id`: Post ID     - `node.code`: Post shortcode     - `node.display_url`: Display image URL     - `node.taken_at`: Published timestamp     - `node.like_count`: Likes count     - `node.comment_count`: Comments count     - `node.caption.text`: Post caption text     - `node.user`: Post author info - `data.page_info`: Pagination info     - `has_next_page`: Whether has next page     - `end_cursor`: Next page cursor (use as after parameter in next request) ### Pagination usage: 1. First request: Only pass `user_id`/`username` and `first` parameters 2. Get `data.page_info.end_cursor` from response 3. Next request: Pass `user_id`, `first`, and `after` (use end_cursor from previous) 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\" first = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_tagged_posts_api_v1_instagram_v3_get_user_tagged_posts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object first: 获取帖子数量/Number of posts to fetch
        :param object after: 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_tagged_posts_api_v1_instagram_v3_get_user_tagged_posts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_tagged_posts_api_v1_instagram_v3_get_user_tagged_posts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_tagged_posts_api_v1_instagram_v3_get_user_tagged_posts_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户被标记的帖子/Get user tagged posts  # noqa: E501

        # [中文] ### 用途: - 获取Instagram用户被标记（tagged）的帖子列表 - 即其他用户在帖子中标记了该用户的内容 - 支持分页获取 ### 参数（二选一）: - user_id: Instagram用户ID（数字） - username: Instagram用户名 - first: 每次获取的帖子数量（默认12） - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取 ### 返回: - `data.edges`: 帖子列表     - `node.id`: 帖子ID     - `node.code`: 帖子短代码     - `node.display_url`: 展示图片URL     - `node.taken_at`: 发布时间戳     - `node.like_count`: 点赞数     - `node.comment_count`: 评论数     - `node.caption.text`: 帖子文本     - `node.user`: 发帖者信息 - `data.page_info`: 分页信息     - `has_next_page`: 是否有下一页     - `end_cursor`: 下一页游标（传给下次请求的after参数） ### 分页使用方法: 1. 首次请求：只传 `user_id` 和 `first` 参数 2. 获取响应中的 `data.page_info.end_cursor` 3. 下次请求：传入 `user_id`、`first` 和 `after` (使用上次的end_cursor) 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Get Instagram user's tagged posts list - Posts where other users tagged this user - Support pagination ### Parameters (one of): - user_id: Instagram user ID (numeric) - username: Instagram username ### Other parameters: - first: Number of posts to fetch per request (default 12) - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` ### Return: - `data.edges`: Post list     - `node.id`: Post ID     - `node.code`: Post shortcode     - `node.display_url`: Display image URL     - `node.taken_at`: Published timestamp     - `node.like_count`: Likes count     - `node.comment_count`: Comments count     - `node.caption.text`: Post caption text     - `node.user`: Post author info - `data.page_info`: Pagination info     - `has_next_page`: Whether has next page     - `end_cursor`: Next page cursor (use as after parameter in next request) ### Pagination usage: 1. First request: Only pass `user_id`/`username` and `first` parameters 2. Get `data.page_info.end_cursor` from response 3. Next request: Pass `user_id`, `first`, and `after` (use end_cursor from previous) 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false ### Price: - 0.002 USD/request  ### 示例/Example user_id = \"58208242181\" first = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_tagged_posts_api_v1_instagram_v3_get_user_tagged_posts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object username: 用户名/Username
        :param object first: 获取帖子数量/Number of posts to fetch
        :param object after: 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'username', 'first', 'after']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_tagged_posts_api_v1_instagram_v3_get_user_tagged_posts_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'first' in params:
            query_params.append(('first', params['first']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/get_user_tagged_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_hashtags_api_v1_instagram_v3_search_hashtags_get(self, query, **kwargs):  # noqa: E501
        """搜索话题标签/Search hashtags  # noqa: E501

        # [中文] ### 用途: - Instagram话题标签搜索接口 - 仅返回话题标签搜索结果 ### 参数: - query: 搜索关键词 ### 返回: - `data.hashtags`: 话题标签搜索结果列表 - `data.rank_token`: 排序token - `data.see_more`: 更多信息 - `data.inform_module`: 提示模块 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Instagram hashtag search API - Returns only hashtag search results ### Parameters: - query: Search keyword ### Return: - `data.hashtags`: Hashtag search results - `data.rank_token`: Rank token - `data.see_more`: See more info - `data.inform_module`: Inform module ### Price: - 0.002 USD/request  ### 示例/Example query = \"fashion\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_hashtags_api_v1_instagram_v3_search_hashtags_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_hashtags_api_v1_instagram_v3_search_hashtags_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_hashtags_api_v1_instagram_v3_search_hashtags_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_hashtags_api_v1_instagram_v3_search_hashtags_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """搜索话题标签/Search hashtags  # noqa: E501

        # [中文] ### 用途: - Instagram话题标签搜索接口 - 仅返回话题标签搜索结果 ### 参数: - query: 搜索关键词 ### 返回: - `data.hashtags`: 话题标签搜索结果列表 - `data.rank_token`: 排序token - `data.see_more`: 更多信息 - `data.inform_module`: 提示模块 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Instagram hashtag search API - Returns only hashtag search results ### Parameters: - query: Search keyword ### Return: - `data.hashtags`: Hashtag search results - `data.rank_token`: Rank token - `data.see_more`: See more info - `data.inform_module`: Inform module ### Price: - 0.002 USD/request  ### 示例/Example query = \"fashion\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_hashtags_api_v1_instagram_v3_search_hashtags_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_hashtags_api_v1_instagram_v3_search_hashtags_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `search_hashtags_api_v1_instagram_v3_search_hashtags_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/search_hashtags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_places_api_v1_instagram_v3_search_places_get(self, query, **kwargs):  # noqa: E501
        """搜索地点/Search places  # noqa: E501

        # [中文] ### 用途: - Instagram地点搜索接口 - 仅返回地点搜索结果 ### 参数: - query: 搜索关键词 ### 返回: - `data.places`: 地点搜索结果列表 - `data.rank_token`: 排序token - `data.see_more`: 更多信息 - `data.inform_module`: 提示模块 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Instagram place search API - Returns only place search results ### Parameters: - query: Search keyword ### Return: - `data.places`: Place search results - `data.rank_token`: Rank token - `data.see_more`: See more info - `data.inform_module`: Inform module ### Price: - 0.002 USD/request  ### 示例/Example query = \"tokyo\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_places_api_v1_instagram_v3_search_places_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_places_api_v1_instagram_v3_search_places_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_places_api_v1_instagram_v3_search_places_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_places_api_v1_instagram_v3_search_places_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """搜索地点/Search places  # noqa: E501

        # [中文] ### 用途: - Instagram地点搜索接口 - 仅返回地点搜索结果 ### 参数: - query: 搜索关键词 ### 返回: - `data.places`: 地点搜索结果列表 - `data.rank_token`: 排序token - `data.see_more`: 更多信息 - `data.inform_module`: 提示模块 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Instagram place search API - Returns only place search results ### Parameters: - query: Search keyword ### Return: - `data.places`: Place search results - `data.rank_token`: Rank token - `data.see_more`: See more info - `data.inform_module`: Inform module ### Price: - 0.002 USD/request  ### 示例/Example query = \"tokyo\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_places_api_v1_instagram_v3_search_places_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_places_api_v1_instagram_v3_search_places_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `search_places_api_v1_instagram_v3_search_places_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/search_places', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_users_api_v1_instagram_v3_search_users_get(self, query, **kwargs):  # noqa: E501
        """搜索用户/Search users  # noqa: E501

        # [中文] ### 用途: - Instagram用户搜索接口 - 仅返回用户搜索结果 ### 参数: - query: 搜索关键词 ### 返回: - `data.users`: 用户搜索结果列表 - `data.rank_token`: 排序token - `data.see_more`: 更多信息 - `data.inform_module`: 提示模块 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Instagram user search API - Returns only user search results ### Parameters: - query: Search keyword ### Return: - `data.users`: User search results - `data.rank_token`: Rank token - `data.see_more`: See more info - `data.inform_module`: Inform module ### Price: - 0.002 USD/request  ### 示例/Example query = \"justin\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_api_v1_instagram_v3_search_users_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_users_api_v1_instagram_v3_search_users_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_users_api_v1_instagram_v3_search_users_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_users_api_v1_instagram_v3_search_users_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """搜索用户/Search users  # noqa: E501

        # [中文] ### 用途: - Instagram用户搜索接口 - 仅返回用户搜索结果 ### 参数: - query: 搜索关键词 ### 返回: - `data.users`: 用户搜索结果列表 - `data.rank_token`: 排序token - `data.see_more`: 更多信息 - `data.inform_module`: 提示模块 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Instagram user search API - Returns only user search results ### Parameters: - query: Search keyword ### Return: - `data.users`: User search results - `data.rank_token`: Rank token - `data.see_more`: See more info - `data.inform_module`: Inform module ### Price: - 0.002 USD/request  ### 示例/Example query = \"justin\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_api_v1_instagram_v3_search_users_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_users_api_v1_instagram_v3_search_users_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `search_users_api_v1_instagram_v3_search_users_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/search_users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def translate_comment_api_v1_instagram_v3_translate_comment_get(self, comment_id, **kwargs):  # noqa: E501
        """翻译评论/帖子文本/Translate comment or caption  # noqa: E501

        # [中文] ### 用途: - 翻译Instagram帖子文本（caption） - 内部强制 is_caption=True，专门用于翻译帖子的文字说明 ### 参数: - comment_id: 帖子媒体ID ### 返回: - `data.translation`: 翻译后的文本 - `data.source_language`: 原文语言 ### 注意: - 翻译目标语言取决于请求所使用的 Cookie 对应账号的语言设置（通常为英语） - 无法指定翻译目标语言，由 Instagram 服务端根据账号设置自动决定 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Translate Instagram post caption - Internally forces is_caption=True, specifically for translating post captions ### Parameters: - comment_id: Post media ID ### Return: - `data.translation`: Translated text - `data.source_language`: Source language ### Note: - The target translation language depends on the language setting of the account associated with the cookie used (usually English) - Cannot specify the target language, it is automatically determined by Instagram based on the account settings ### Price: - 0.002 USD/request  ### 示例/Example comment_id = \"18191961100350646\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translate_comment_api_v1_instagram_v3_translate_comment_get(comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object comment_id: 帖子媒体ID/Post media ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.translate_comment_api_v1_instagram_v3_translate_comment_get_with_http_info(comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.translate_comment_api_v1_instagram_v3_translate_comment_get_with_http_info(comment_id, **kwargs)  # noqa: E501
            return data

    def translate_comment_api_v1_instagram_v3_translate_comment_get_with_http_info(self, comment_id, **kwargs):  # noqa: E501
        """翻译评论/帖子文本/Translate comment or caption  # noqa: E501

        # [中文] ### 用途: - 翻译Instagram帖子文本（caption） - 内部强制 is_caption=True，专门用于翻译帖子的文字说明 ### 参数: - comment_id: 帖子媒体ID ### 返回: - `data.translation`: 翻译后的文本 - `data.source_language`: 原文语言 ### 注意: - 翻译目标语言取决于请求所使用的 Cookie 对应账号的语言设置（通常为英语） - 无法指定翻译目标语言，由 Instagram 服务端根据账号设置自动决定 ### 价格: - 0.002 USD/请求  # [English] ### Purpose: - Translate Instagram post caption - Internally forces is_caption=True, specifically for translating post captions ### Parameters: - comment_id: Post media ID ### Return: - `data.translation`: Translated text - `data.source_language`: Source language ### Note: - The target translation language depends on the language setting of the account associated with the cookie used (usually English) - Cannot specify the target language, it is automatically determined by Instagram based on the account settings ### Price: - 0.002 USD/request  ### 示例/Example comment_id = \"18191961100350646\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translate_comment_api_v1_instagram_v3_translate_comment_get_with_http_info(comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object comment_id: 帖子媒体ID/Post media ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['comment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method translate_comment_api_v1_instagram_v3_translate_comment_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `translate_comment_api_v1_instagram_v3_translate_comment_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/instagram/v3/translate_comment', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
