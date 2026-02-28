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


class KuaishouAppAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_brand_top_list_api_v1_kuaishou_app_fetch_brand_top_list_get(self, **kwargs):  # noqa: E501
        """快手品牌榜单/Kuaishou brand top list  # noqa: E501

        # [中文] ### 用途: - 快手品牌榜单 ### 参数: 获取快手品牌榜单，支持多个子榜单，具体参数如下：  - 品牌榜单热门美妆榜对应参数：     - subTabId = 0     - subTabName = None - 品牌榜单热门服饰榜对应参数：     - subTabId = 131     - subTabName = \"服饰\" - 品牌榜单热门汽车榜对应参数：     - subTabId = 1     - subTabName = \"汽车\" - 品牌榜单热门游戏榜对应参数：     - subTabId = 25     - subTabName = \"游戏\" - 品牌榜单热门医疗健康榜对应参数：     - subTabId = 24     - subTabName = \"医疗健康\" - 品牌榜单热门3C数码榜对应参数：     - subTabId = 130     - subTabName = \"3C数码\" - 品牌榜单热门手机榜对应参数：     - subTabId = 128     - subTabName = \"手机\" - 品牌榜单热门家电榜对应参数：     - subTabId = 11     - subTabName = \"家电\" - 品牌榜单热门母婴榜对应参数：     - subTabId = 4     - subTabName = \"母婴\" - 品牌榜单热门食品饮料榜对应参数：     - subTabId = 2     - subTabName = \"食品饮料\"  ### 返回: - 榜单数据  # [English] ### Purpose: - Kuaishou brand top list ### Parameters: Get the Kuaishou brand top list, support multiple sub-top lists, specific parameters are as follows:  - Corresponding parameters for the brand hot beauty list:     - subTabId = 0     - subTabName = None - Corresponding parameters for the brand hot clothing list:     - subTabId = 131     - subTabName = \"Clothing\" - Corresponding parameters for the brand hot car list:     - subTabId = 1     - subTabName = \"Car\" - Corresponding parameters for the brand hot game list:     - subTabId = 25     - subTabName = \"Game\" - Corresponding parameters for the brand hot medical health list:     - subTabId = 24     - subTabName = \"Medical Health\" - Corresponding parameters for the brand hot 3C digital list:     - subTabId = 130     - subTabName = \"3C Digital\" - Corresponding parameters for the brand hot mobile phone list:     - subTabId = 128     - subTabName = \"Mobile Phone\" - Corresponding parameters for the brand hot home appliance list:     - subTabId = 11     - subTabName = \"Home Appliance\" - Corresponding parameters for the brand hot maternal and child list:     - subTabId = 4     - subTabName = \"Maternal and Child\" - Corresponding parameters for the brand hot food and beverage list:     - subTabId = 2     - subTabName = \"Food and Beverage\"   ### Returns: - List data  # [示例/Example] subTabId = 0 subTabName = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_brand_top_list_api_v1_kuaishou_app_fetch_brand_top_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sub_tab_id:
        :param object sub_tab_name:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_brand_top_list_api_v1_kuaishou_app_fetch_brand_top_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_brand_top_list_api_v1_kuaishou_app_fetch_brand_top_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_brand_top_list_api_v1_kuaishou_app_fetch_brand_top_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """快手品牌榜单/Kuaishou brand top list  # noqa: E501

        # [中文] ### 用途: - 快手品牌榜单 ### 参数: 获取快手品牌榜单，支持多个子榜单，具体参数如下：  - 品牌榜单热门美妆榜对应参数：     - subTabId = 0     - subTabName = None - 品牌榜单热门服饰榜对应参数：     - subTabId = 131     - subTabName = \"服饰\" - 品牌榜单热门汽车榜对应参数：     - subTabId = 1     - subTabName = \"汽车\" - 品牌榜单热门游戏榜对应参数：     - subTabId = 25     - subTabName = \"游戏\" - 品牌榜单热门医疗健康榜对应参数：     - subTabId = 24     - subTabName = \"医疗健康\" - 品牌榜单热门3C数码榜对应参数：     - subTabId = 130     - subTabName = \"3C数码\" - 品牌榜单热门手机榜对应参数：     - subTabId = 128     - subTabName = \"手机\" - 品牌榜单热门家电榜对应参数：     - subTabId = 11     - subTabName = \"家电\" - 品牌榜单热门母婴榜对应参数：     - subTabId = 4     - subTabName = \"母婴\" - 品牌榜单热门食品饮料榜对应参数：     - subTabId = 2     - subTabName = \"食品饮料\"  ### 返回: - 榜单数据  # [English] ### Purpose: - Kuaishou brand top list ### Parameters: Get the Kuaishou brand top list, support multiple sub-top lists, specific parameters are as follows:  - Corresponding parameters for the brand hot beauty list:     - subTabId = 0     - subTabName = None - Corresponding parameters for the brand hot clothing list:     - subTabId = 131     - subTabName = \"Clothing\" - Corresponding parameters for the brand hot car list:     - subTabId = 1     - subTabName = \"Car\" - Corresponding parameters for the brand hot game list:     - subTabId = 25     - subTabName = \"Game\" - Corresponding parameters for the brand hot medical health list:     - subTabId = 24     - subTabName = \"Medical Health\" - Corresponding parameters for the brand hot 3C digital list:     - subTabId = 130     - subTabName = \"3C Digital\" - Corresponding parameters for the brand hot mobile phone list:     - subTabId = 128     - subTabName = \"Mobile Phone\" - Corresponding parameters for the brand hot home appliance list:     - subTabId = 11     - subTabName = \"Home Appliance\" - Corresponding parameters for the brand hot maternal and child list:     - subTabId = 4     - subTabName = \"Maternal and Child\" - Corresponding parameters for the brand hot food and beverage list:     - subTabId = 2     - subTabName = \"Food and Beverage\"   ### Returns: - List data  # [示例/Example] subTabId = 0 subTabName = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_brand_top_list_api_v1_kuaishou_app_fetch_brand_top_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sub_tab_id:
        :param object sub_tab_name:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sub_tab_id', 'sub_tab_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_brand_top_list_api_v1_kuaishou_app_fetch_brand_top_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sub_tab_id' in params:
            query_params.append(('subTabId', params['sub_tab_id']))  # noqa: E501
        if 'sub_tab_name' in params:
            query_params.append(('subTabName', params['sub_tab_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_brand_top_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hot_board_categories_api_v1_kuaishou_app_fetch_hot_board_categories_get(self, **kwargs):  # noqa: E501
        """快手热榜分类/Kuaishou hot categories  # noqa: E501

        # [中文] ### 用途: - 快手热榜分类 ### 返回: - 分类数据  # [English] ### Purpose: - Kuaishou hot categories ### Returns: - Categories data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_board_categories_api_v1_kuaishou_app_fetch_hot_board_categories_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_board_categories_api_v1_kuaishou_app_fetch_hot_board_categories_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_board_categories_api_v1_kuaishou_app_fetch_hot_board_categories_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_board_categories_api_v1_kuaishou_app_fetch_hot_board_categories_get_with_http_info(self, **kwargs):  # noqa: E501
        """快手热榜分类/Kuaishou hot categories  # noqa: E501

        # [中文] ### 用途: - 快手热榜分类 ### 返回: - 分类数据  # [English] ### Purpose: - Kuaishou hot categories ### Returns: - Categories data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_board_categories_api_v1_kuaishou_app_fetch_hot_board_categories_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_board_categories_api_v1_kuaishou_app_fetch_hot_board_categories_get" % key
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
            '/api/v1/kuaishou/app/fetch_hot_board_categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hot_board_detail_api_v1_kuaishou_app_fetch_hot_board_detail_get(self, **kwargs):  # noqa: E501
        """快手热榜详情/Kuaishou hot board detail  # noqa: E501

        # [中文] ### 用途: - 快手热榜详情 ### 参数: - boardType: 榜单类型 - boardId: 榜单ID - boardType 和 boardId 可以从热榜分类接口中获取。 ### 返回: - 详情数据  # [English] ### Purpose: - Kuaishou hot board detail ### Parameters: - boardType: Board type - boardId: Board ID - boardType and boardId can be obtained from the hot board categories interface. ### Returns: - Detail data  # [示例/Example] boardType = 1 boardId = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_board_detail_api_v1_kuaishou_app_fetch_hot_board_detail_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object board_type:
        :param object board_id:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_board_detail_api_v1_kuaishou_app_fetch_hot_board_detail_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_board_detail_api_v1_kuaishou_app_fetch_hot_board_detail_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_board_detail_api_v1_kuaishou_app_fetch_hot_board_detail_get_with_http_info(self, **kwargs):  # noqa: E501
        """快手热榜详情/Kuaishou hot board detail  # noqa: E501

        # [中文] ### 用途: - 快手热榜详情 ### 参数: - boardType: 榜单类型 - boardId: 榜单ID - boardType 和 boardId 可以从热榜分类接口中获取。 ### 返回: - 详情数据  # [English] ### Purpose: - Kuaishou hot board detail ### Parameters: - boardType: Board type - boardId: Board ID - boardType and boardId can be obtained from the hot board categories interface. ### Returns: - Detail data  # [示例/Example] boardType = 1 boardId = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_board_detail_api_v1_kuaishou_app_fetch_hot_board_detail_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object board_type:
        :param object board_id:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['board_type', 'board_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_board_detail_api_v1_kuaishou_app_fetch_hot_board_detail_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'board_type' in params:
            query_params.append(('boardType', params['board_type']))  # noqa: E501
        if 'board_id' in params:
            query_params.append(('boardId', params['board_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_hot_board_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hot_search_person_api_v1_kuaishou_app_fetch_hot_search_person_get(self, **kwargs):  # noqa: E501
        """快手热搜人物榜单/Kuaishou hot search person board  # noqa: E501

        # [中文] ### 用途: - 快手热搜人物榜单 ### 返回: - 榜单数据  # [English] ### Purpose: - Kuaishou hot search person board ### Returns: - Board data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_person_api_v1_kuaishou_app_fetch_hot_search_person_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_person_api_v1_kuaishou_app_fetch_hot_search_person_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_person_api_v1_kuaishou_app_fetch_hot_search_person_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_person_api_v1_kuaishou_app_fetch_hot_search_person_get_with_http_info(self, **kwargs):  # noqa: E501
        """快手热搜人物榜单/Kuaishou hot search person board  # noqa: E501

        # [中文] ### 用途: - 快手热搜人物榜单 ### 返回: - 榜单数据  # [English] ### Purpose: - Kuaishou hot search person board ### Returns: - Board data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_person_api_v1_kuaishou_app_fetch_hot_search_person_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_search_person_api_v1_kuaishou_app_fetch_hot_search_person_get" % key
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
            '/api/v1/kuaishou/app/fetch_hot_search_person', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_live_top_list_api_v1_kuaishou_app_fetch_live_top_list_get(self, **kwargs):  # noqa: E501
        """快手直播榜单/Kuaishou live top list  # noqa: E501

        # [中文] ### 用途: - 快手直播榜单 ### 参数: 获取快手直播榜单，支持多个子榜单，具体参数如下：  - 直播总榜对应参数：     - subTabId = 0     - subTabName = None - 直播音乐榜对应参数：     - subTabId = 102     - subTabName = \"音乐\" - 直播舞蹈榜对应参数：     - subTabId = 107     - subTabName = \"舞蹈\" - 直播颜值榜对应参数：     - subTabId = 101     - subTabName = \"颜值\" - 直播国艺榜对应参数：     - subTabId = 105     - subTabName = \"国艺\" - 直播相亲榜对应参数：     - subTabId = 111     - subTabName = \"相亲\" - 直播游戏榜对应参数：     - subTabId = 106     - subTabName = \"游戏\" - 直播二次元榜对应参数：     - subTabId = 110     - subTabName = \"二次元\" - 直播故事榜对应参数：     - subTabId = 104     - subTabName = \"故事\" - 直播团播榜对应参数：     - subTabId = 113     - subTabName = \"团播\" - 直播九宫格榜对应参数：     - subTabId = 114     - subTabName = \"九宫格\"  ### 返回: - 榜单数据  # [English] ### Purpose: - Kuaishou live top list ### Parameters: Get the Kuaishou live top list, support multiple sub-top lists, specific parameters are as follows:  - Corresponding parameters for the live total list:     - subTabId = 0     - subTabName = None - Corresponding parameters for the live music list:     - subTabId = 102     - subTabName = \"Music\" - Corresponding parameters for the live dance list:     - subTabId = 107     - subTabName = \"Dance\" - Corresponding parameters for the live beauty list:     - subTabId = 101     - subTabName = \"Beauty\" - Corresponding parameters for the live national art list:     - subTabId = 105     - subTabName = \"National Art\" - Corresponding parameters for the live blind date list:     - subTabId = 111     - subTabName = \"Blind Date\" - Corresponding parameters for the live game list:     - subTabId = 106     - subTabName = \"Game\" - Corresponding parameters for the live second element list:     - subTabId = 110     - subTabName = \"Second Element\" - Corresponding parameters for the live story list:     - subTabId = 104     - subTabName = \"Story\" - Corresponding parameters for the live group broadcast list:     - subTabId = 113     - subTabName = \"Group Broadcast\" - Corresponding parameters for the live nine-grid list:     - subTabId = 114     - subTabName = \"Nine Grid\"  ### Returns: - List data  # [示例/Example] subTabId = 0 subTabName = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_top_list_api_v1_kuaishou_app_fetch_live_top_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sub_tab_id:
        :param object sub_tab_name:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_top_list_api_v1_kuaishou_app_fetch_live_top_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_top_list_api_v1_kuaishou_app_fetch_live_top_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_live_top_list_api_v1_kuaishou_app_fetch_live_top_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """快手直播榜单/Kuaishou live top list  # noqa: E501

        # [中文] ### 用途: - 快手直播榜单 ### 参数: 获取快手直播榜单，支持多个子榜单，具体参数如下：  - 直播总榜对应参数：     - subTabId = 0     - subTabName = None - 直播音乐榜对应参数：     - subTabId = 102     - subTabName = \"音乐\" - 直播舞蹈榜对应参数：     - subTabId = 107     - subTabName = \"舞蹈\" - 直播颜值榜对应参数：     - subTabId = 101     - subTabName = \"颜值\" - 直播国艺榜对应参数：     - subTabId = 105     - subTabName = \"国艺\" - 直播相亲榜对应参数：     - subTabId = 111     - subTabName = \"相亲\" - 直播游戏榜对应参数：     - subTabId = 106     - subTabName = \"游戏\" - 直播二次元榜对应参数：     - subTabId = 110     - subTabName = \"二次元\" - 直播故事榜对应参数：     - subTabId = 104     - subTabName = \"故事\" - 直播团播榜对应参数：     - subTabId = 113     - subTabName = \"团播\" - 直播九宫格榜对应参数：     - subTabId = 114     - subTabName = \"九宫格\"  ### 返回: - 榜单数据  # [English] ### Purpose: - Kuaishou live top list ### Parameters: Get the Kuaishou live top list, support multiple sub-top lists, specific parameters are as follows:  - Corresponding parameters for the live total list:     - subTabId = 0     - subTabName = None - Corresponding parameters for the live music list:     - subTabId = 102     - subTabName = \"Music\" - Corresponding parameters for the live dance list:     - subTabId = 107     - subTabName = \"Dance\" - Corresponding parameters for the live beauty list:     - subTabId = 101     - subTabName = \"Beauty\" - Corresponding parameters for the live national art list:     - subTabId = 105     - subTabName = \"National Art\" - Corresponding parameters for the live blind date list:     - subTabId = 111     - subTabName = \"Blind Date\" - Corresponding parameters for the live game list:     - subTabId = 106     - subTabName = \"Game\" - Corresponding parameters for the live second element list:     - subTabId = 110     - subTabName = \"Second Element\" - Corresponding parameters for the live story list:     - subTabId = 104     - subTabName = \"Story\" - Corresponding parameters for the live group broadcast list:     - subTabId = 113     - subTabName = \"Group Broadcast\" - Corresponding parameters for the live nine-grid list:     - subTabId = 114     - subTabName = \"Nine Grid\"  ### Returns: - List data  # [示例/Example] subTabId = 0 subTabName = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_top_list_api_v1_kuaishou_app_fetch_live_top_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sub_tab_id:
        :param object sub_tab_name:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sub_tab_id', 'sub_tab_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_top_list_api_v1_kuaishou_app_fetch_live_top_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sub_tab_id' in params:
            query_params.append(('subTabId', params['sub_tab_id']))  # noqa: E501
        if 'sub_tab_name' in params:
            query_params.append(('subTabName', params['sub_tab_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_live_top_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get(self, magic_face_id, **kwargs):  # noqa: E501
        """获取魔法表情热门视频/Fetch magic face hot videos  # noqa: E501

        # [中文] ### 用途: - 获取快手魔法表情热门视频列表（H5接口） ### 参数: - magic_face_id: 魔法表情ID - pcursor: 分页游标，首页为\"0\"，后续使用响应中返回的pcursor值 - count: 每页数量，默认18 ### 返回: - 魔法表情热门视频列表  # [English] ### Purpose: - Fetch Kuaishou magic face hot videos list (H5 API) ### Parameters: - magic_face_id: Magic face ID - pcursor: Pagination cursor, \"0\" for first page, use pcursor from response for subsequent pages - count: Count per page, default 18 ### Returns: - Magic face hot videos list  # [示例/Example] magic_face_id = \"11541661\" pcursor = \"0\" count = 18  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get(magic_face_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object magic_face_id: (required)
        :param object pcursor:
        :param object count:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get_with_http_info(magic_face_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get_with_http_info(magic_face_id, **kwargs)  # noqa: E501
            return data

    def fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get_with_http_info(self, magic_face_id, **kwargs):  # noqa: E501
        """获取魔法表情热门视频/Fetch magic face hot videos  # noqa: E501

        # [中文] ### 用途: - 获取快手魔法表情热门视频列表（H5接口） ### 参数: - magic_face_id: 魔法表情ID - pcursor: 分页游标，首页为\"0\"，后续使用响应中返回的pcursor值 - count: 每页数量，默认18 ### 返回: - 魔法表情热门视频列表  # [English] ### Purpose: - Fetch Kuaishou magic face hot videos list (H5 API) ### Parameters: - magic_face_id: Magic face ID - pcursor: Pagination cursor, \"0\" for first page, use pcursor from response for subsequent pages - count: Count per page, default 18 ### Returns: - Magic face hot videos list  # [示例/Example] magic_face_id = \"11541661\" pcursor = \"0\" count = 18  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get_with_http_info(magic_face_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object magic_face_id: (required)
        :param object pcursor:
        :param object count:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['magic_face_id', 'pcursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'magic_face_id' is set
        if self.api_client.client_side_validation and ('magic_face_id' not in params or
                                                       params['magic_face_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `magic_face_id` when calling `fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'magic_face_id' in params:
            query_params.append(('magic_face_id', params['magic_face_id']))  # noqa: E501
        if 'pcursor' in params:
            query_params.append(('pcursor', params['pcursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_magic_face_hot', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get(self, magic_face_id, **kwargs):  # noqa: E501
        """获取魔法表情使用人数/Fetch magic face usage count  # noqa: E501

        # [中文] ### 用途: - 获取快手魔法表情使用人数（H5接口） ### 参数: - magic_face_id: 魔法表情ID ### 返回: - 魔法表情使用人数  # [English] ### Purpose: - Fetch Kuaishou magic face usage count (H5 API) ### Parameters: - magic_face_id: Magic face ID ### Returns: - Magic face usage count  # [示例/Example] magic_face_id = \"11541661\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get(magic_face_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object magic_face_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get_with_http_info(magic_face_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get_with_http_info(magic_face_id, **kwargs)  # noqa: E501
            return data

    def fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get_with_http_info(self, magic_face_id, **kwargs):  # noqa: E501
        """获取魔法表情使用人数/Fetch magic face usage count  # noqa: E501

        # [中文] ### 用途: - 获取快手魔法表情使用人数（H5接口） ### 参数: - magic_face_id: 魔法表情ID ### 返回: - 魔法表情使用人数  # [English] ### Purpose: - Fetch Kuaishou magic face usage count (H5 API) ### Parameters: - magic_face_id: Magic face ID ### Returns: - Magic face usage count  # [示例/Example] magic_face_id = \"11541661\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get_with_http_info(magic_face_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object magic_face_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['magic_face_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'magic_face_id' is set
        if self.api_client.client_side_validation and ('magic_face_id' not in params or
                                                       params['magic_face_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `magic_face_id` when calling `fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'magic_face_id' in params:
            query_params.append(('magic_face_id', params['magic_face_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_magic_face_usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get(self, user_id, **kwargs):  # noqa: E501
        """获取单个用户数据V2/Get single user data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个用户数据 V2 - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。 ### 参数: - user_id: 支持`eid`或`userId`，eid是用户主页链接中的一部分，user_id则可以从不同的接口中获取。 - 两种用户ID都可以使用，下面是两种用户ID的示例，这两个ID都指向同一个用户：     - eid = \"3xz63mn6fngqtiq\"     - userId = \"228905802\" ### 返回: - 用户数据  # [English] ### Purpose: - Fetch single user data V2 - This API is more expensive, but more stable, please check the price list in the user background for specific prices. ### Parameters: - user_id: Supports `eid` or `userId`, `eid` is part of the user profile link, and `user_id` can be obtained from different interfaces. - Both user IDs can be used, here are examples of the two user IDs, both of which point to the same user:     - eid = \"3xz63mn6fngqtiq\"     - userId = \"228905802\" ### Returns: - User data  # [示例/Example] user_id = \"3xz63mn6fngqtiq\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取单个用户数据V2/Get single user data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个用户数据 V2 - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。 ### 参数: - user_id: 支持`eid`或`userId`，eid是用户主页链接中的一部分，user_id则可以从不同的接口中获取。 - 两种用户ID都可以使用，下面是两种用户ID的示例，这两个ID都指向同一个用户：     - eid = \"3xz63mn6fngqtiq\"     - userId = \"228905802\" ### 返回: - 用户数据  # [English] ### Purpose: - Fetch single user data V2 - This API is more expensive, but more stable, please check the price list in the user background for specific prices. ### Parameters: - user_id: Supports `eid` or `userId`, `eid` is part of the user profile link, and `user_id` can be obtained from different interfaces. - Both user IDs can be used, here are examples of the two user IDs, both of which point to the same user:     - eid = \"3xz63mn6fngqtiq\"     - userId = \"228905802\" ### Returns: - User data  # [示例/Example] user_id = \"3xz63mn6fngqtiq\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: (required)
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
                    " to method fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get`")  # noqa: E501

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
            '/api/v1/kuaishou/app/fetch_one_user_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get(self, share_text, **kwargs):  # noqa: E501
        """根据链接获取单个作品数据/Fetch single video by URL  # noqa: E501

        # [中文] ### 用途: - 根据链接获取单个作品数据，此接口默认使用价格更便宜的V1接口进行请求。 ### 参数: - share_text: 作品链接或分享文本 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video by URL, this API defaults to using the cheaper V1 API for requests. ### Parameters: - share_text: Photo URL or share text ### Returns: - Video data  # [示例/Example] share_text = \"https://v.kuaishou.com/cNYP0Z\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get(share_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get_with_http_info(share_text, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get_with_http_info(share_text, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get_with_http_info(self, share_text, **kwargs):  # noqa: E501
        """根据链接获取单个作品数据/Fetch single video by URL  # noqa: E501

        # [中文] ### 用途: - 根据链接获取单个作品数据，此接口默认使用价格更便宜的V1接口进行请求。 ### 参数: - share_text: 作品链接或分享文本 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video by URL, this API defaults to using the cheaper V1 API for requests. ### Parameters: - share_text: Photo URL or share text ### Returns: - Video data  # [示例/Example] share_text = \"https://v.kuaishou.com/cNYP0Z\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get_with_http_info(share_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['share_text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_text' is set
        if self.api_client.client_side_validation and ('share_text' not in params or
                                                       params['share_text'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_text` when calling `fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_text' in params:
            query_params.append(('share_text', params['share_text']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_one_video_by_url', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get(self, photo_id, **kwargs):  # noqa: E501
        """视频详情V1/Video detailsV1  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据接口 V1。 ### 参数: - photo_id: 作品ID，作品ID可以从分享链接中提取     - 格式备注：支持纯数字版本的ID，也支持短字符串版本（eID）的ID，两种ID可以混合使用。 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video data API V1. ### Parameters: - photo_id: Photo ID, the photo ID can be extracted from the share link     - Format note: Supports both pure digital version IDs and short string version (eID) IDs, both types can be mixed. ### Returns: - Video data  # [示例/Example] photo_id = \"3xhpk3xcf6e4iac\" photo_id = \"5246975215478907538\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get(photo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object photo_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get_with_http_info(photo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get_with_http_info(photo_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get_with_http_info(self, photo_id, **kwargs):  # noqa: E501
        """视频详情V1/Video detailsV1  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据接口 V1。 ### 参数: - photo_id: 作品ID，作品ID可以从分享链接中提取     - 格式备注：支持纯数字版本的ID，也支持短字符串版本（eID）的ID，两种ID可以混合使用。 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video data API V1. ### Parameters: - photo_id: Photo ID, the photo ID can be extracted from the share link     - Format note: Supports both pure digital version IDs and short string version (eID) IDs, both types can be mixed. ### Returns: - Video data  # [示例/Example] photo_id = \"3xhpk3xcf6e4iac\" photo_id = \"5246975215478907538\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get_with_http_info(photo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object photo_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['photo_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'photo_id' is set
        if self.api_client.client_side_validation and ('photo_id' not in params or
                                                       params['photo_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `photo_id` when calling `fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'photo_id' in params:
            query_params.append(('photo_id', params['photo_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_one_video', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_shopping_top_list_api_v1_kuaishou_app_fetch_shopping_top_list_get(self, **kwargs):  # noqa: E501
        """快手购物榜单/Kuaishou shopping top list  # noqa: E501

        # [中文] ### 用途: - 快手购物榜单 ### 参数: 获取快手购物榜单，支持多个子榜单，具体参数如下：  - 购物榜单热门主播榜对应参数：     - subTabId = 0     - subTabName = None - 购物榜单热销商品榜对应参数：     - subTabId = 102     - subTabName = \"热销商品\"  ### 返回: - 榜单数据  # [English] ### Purpose: - Kuaishou shopping top list ### Parameters: Get the Kuaishou shopping top list, support multiple sub-top lists, specific parameters are as follows:  - Corresponding parameters for the shopping hot anchor list:     - subTabId = 0     - subTabName = None - Corresponding parameters for the shopping hot selling product list:     - subTabId = 102     - subTabName = \"Hot Selling Product\"  ### Returns: - List data  # [示例/Example] subTabId = 0 subTabName = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shopping_top_list_api_v1_kuaishou_app_fetch_shopping_top_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sub_tab_id:
        :param object sub_tab_name:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_shopping_top_list_api_v1_kuaishou_app_fetch_shopping_top_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_shopping_top_list_api_v1_kuaishou_app_fetch_shopping_top_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_shopping_top_list_api_v1_kuaishou_app_fetch_shopping_top_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """快手购物榜单/Kuaishou shopping top list  # noqa: E501

        # [中文] ### 用途: - 快手购物榜单 ### 参数: 获取快手购物榜单，支持多个子榜单，具体参数如下：  - 购物榜单热门主播榜对应参数：     - subTabId = 0     - subTabName = None - 购物榜单热销商品榜对应参数：     - subTabId = 102     - subTabName = \"热销商品\"  ### 返回: - 榜单数据  # [English] ### Purpose: - Kuaishou shopping top list ### Parameters: Get the Kuaishou shopping top list, support multiple sub-top lists, specific parameters are as follows:  - Corresponding parameters for the shopping hot anchor list:     - subTabId = 0     - subTabName = None - Corresponding parameters for the shopping hot selling product list:     - subTabId = 102     - subTabName = \"Hot Selling Product\"  ### Returns: - List data  # [示例/Example] subTabId = 0 subTabName = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shopping_top_list_api_v1_kuaishou_app_fetch_shopping_top_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sub_tab_id:
        :param object sub_tab_name:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sub_tab_id', 'sub_tab_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_shopping_top_list_api_v1_kuaishou_app_fetch_shopping_top_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sub_tab_id' in params:
            query_params.append(('subTabId', params['sub_tab_id']))  # noqa: E501
        if 'sub_tab_name' in params:
            query_params.append(('subTabName', params['sub_tab_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_shopping_top_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户热门作品数据/Get user hot post data  # noqa: E501

        # [中文] ### 用途: - 获取用户热门作品数据 ### 参数: - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。 - user_id 可以从获取单个用户数据接口中获取。 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 作品数据  # [English] ### Purpose: - Get user hot post data ### Parameters: - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure digital ID. - user_id can be obtained from the get single user data interface. - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Post data  # [示例/Example] user_id = \"228905802\" pcursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: (required)
        :param object pcursor:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户热门作品数据/Get user hot post data  # noqa: E501

        # [中文] ### 用途: - 获取用户热门作品数据 ### 参数: - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。 - user_id 可以从获取单个用户数据接口中获取。 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 作品数据  # [English] ### Purpose: - Get user hot post data ### Parameters: - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure digital ID. - user_id can be obtained from the get single user data interface. - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Post data  # [示例/Example] user_id = \"228905802\" pcursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: (required)
        :param object pcursor:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'pcursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'pcursor' in params:
            query_params.append(('pcursor', params['pcursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_user_hot_post', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户直播信息/Get user live info  # noqa: E501

        # [中文] ### 用途: - 获取用户直播信息 ### 参数: - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。 - user_id 可以从获取单个用户数据接口中获取。 ### 返回: - 直播信息  # [English] ### Purpose: - Get user live info ### Parameters: - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure digital ID. - user_id can be obtained from the get single user data interface. ### Returns: - Live info  # [示例/Example] user_id = \"1377082950\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户直播信息/Get user live info  # noqa: E501

        # [中文] ### 用途: - 获取用户直播信息 ### 参数: - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。 - user_id 可以从获取单个用户数据接口中获取。 ### 返回: - 直播信息  # [English] ### Purpose: - Get user live info ### Parameters: - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure digital ID. - user_id can be obtained from the get single user data interface. ### Returns: - Live info  # [示例/Example] user_id = \"1377082950\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: (required)
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
                    " to method fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get`")  # noqa: E501

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
            '/api/v1/kuaishou/app/fetch_user_live_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get(self, user_id, **kwargs):  # noqa: E501
        """用户视频列表V2/User video list V2  # noqa: E501

        # [中文] ### 用途: - 用户视频列表 V2 - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。 ### 参数: - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。 - user_id 可以从获取单个用户数据接口中获取。 - pcursor: 视频游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 视频数据  # [English] ### Purpose: - User video list V2 - This API is more expensive, but more stable, please check the price list in the user background for specific prices. ### Parameters: - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure digital ID. - user_id can be obtained from the get single user data interface. - pcursor: Video cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Videos data  # [示例/Example] user_id = \"903511772\" pcursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: (required)
        :param object pcursor:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """用户视频列表V2/User video list V2  # noqa: E501

        # [中文] ### 用途: - 用户视频列表 V2 - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。 ### 参数: - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。 - user_id 可以从获取单个用户数据接口中获取。 - pcursor: 视频游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 视频数据  # [English] ### Purpose: - User video list V2 - This API is more expensive, but more stable, please check the price list in the user background for specific prices. ### Parameters: - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure digital ID. - user_id can be obtained from the get single user data interface. - pcursor: Video cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Videos data  # [示例/Example] user_id = \"903511772\" pcursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: (required)
        :param object pcursor:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'pcursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'pcursor' in params:
            query_params.append(('pcursor', params['pcursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_user_post_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get(self, photo_id, **kwargs):  # noqa: E501
        """获取单个作品评论数据/Get single video comment data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品评论数据 ### 参数: - photo_id: 作品ID     - 格式备注：支持纯数字版本的ID，也支持短字符串版本（eID）的ID，两种ID可以混合使用。 - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 评论数据  # [English] ### Purpose: - Fetch single video comment data ### Parameters: - photo_id: Photo ID     - Format note: Supports both pure digital version IDs and short string version (eID) IDs, both types can be mixed. - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Comments data  # [示例/Example] photo_id = \"3x7gxp2zhgjv832\" pcursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get(photo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object photo_id: (required)
        :param object pcursor:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get_with_http_info(photo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get_with_http_info(photo_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get_with_http_info(self, photo_id, **kwargs):  # noqa: E501
        """获取单个作品评论数据/Get single video comment data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品评论数据 ### 参数: - photo_id: 作品ID     - 格式备注：支持纯数字版本的ID，也支持短字符串版本（eID）的ID，两种ID可以混合使用。 - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 评论数据  # [English] ### Purpose: - Fetch single video comment data ### Parameters: - photo_id: Photo ID     - Format note: Supports both pure digital version IDs and short string version (eID) IDs, both types can be mixed. - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Comments data  # [示例/Example] photo_id = \"3x7gxp2zhgjv832\" pcursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get_with_http_info(photo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object photo_id: (required)
        :param object pcursor:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['photo_id', 'pcursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'photo_id' is set
        if self.api_client.client_side_validation and ('photo_id' not in params or
                                                       params['photo_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `photo_id` when calling `fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'photo_id' in params:
            query_params.append(('photo_id', params['photo_id']))  # noqa: E501
        if 'pcursor' in params:
            query_params.append(('pcursor', params['pcursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_one_video_comment', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get(self, photo_ids, **kwargs):  # noqa: E501
        """快手批量视频查询接口/Kuaishou batch video query API  # noqa: E501

        # [中文] ### 用途: - 批量获取多个作品数据，单次请求最多支持40个视频ID。 - 如果此接口连续请求失败，可以尝试使用价格更昂贵的V2接口进行冗余请求。 - 此接口收费标准默认为：40 * 0.001 = 0.04 美元/次。 ### 参数: - photo_ids: 作品ID列表，多个ID用英文逗号分隔，单次最多40个     - 格式备注：支持纯数字版本的ID，也支持短字符串版本（eID）的ID，两种ID可以混合使用。 ### 返回: - 视频数据列表  # [English] ### Purpose: - Batch fetch multiple video data, supports up to 40 video IDs per request. - If this API continuously fails, you can try to use the more expensive V2 API for redundant requests. - The default charging standard for this API is: 40 * 0.001 = 0.04 USD/time. ### Parameters: - photo_ids: Photo ID list, multiple IDs separated by commas, max 40 per request     - Format note: Supports both pure digital version IDs and short string version (eID) IDs, both types can be mixed. ### Returns: - Video data list  # [示例/Example] photo_ids = \"5228960823332207296,5196309727975443273,5222486898325987583\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get(photo_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object photo_ids: 多个作品ID用逗号分隔，单次最多40个/Multiple photo IDs separated by commas, max 40 per request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get_with_http_info(photo_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get_with_http_info(photo_ids, **kwargs)  # noqa: E501
            return data

    def fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get_with_http_info(self, photo_ids, **kwargs):  # noqa: E501
        """快手批量视频查询接口/Kuaishou batch video query API  # noqa: E501

        # [中文] ### 用途: - 批量获取多个作品数据，单次请求最多支持40个视频ID。 - 如果此接口连续请求失败，可以尝试使用价格更昂贵的V2接口进行冗余请求。 - 此接口收费标准默认为：40 * 0.001 = 0.04 美元/次。 ### 参数: - photo_ids: 作品ID列表，多个ID用英文逗号分隔，单次最多40个     - 格式备注：支持纯数字版本的ID，也支持短字符串版本（eID）的ID，两种ID可以混合使用。 ### 返回: - 视频数据列表  # [English] ### Purpose: - Batch fetch multiple video data, supports up to 40 video IDs per request. - If this API continuously fails, you can try to use the more expensive V2 API for redundant requests. - The default charging standard for this API is: 40 * 0.001 = 0.04 USD/time. ### Parameters: - photo_ids: Photo ID list, multiple IDs separated by commas, max 40 per request     - Format note: Supports both pure digital version IDs and short string version (eID) IDs, both types can be mixed. ### Returns: - Video data list  # [示例/Example] photo_ids = \"5228960823332207296,5196309727975443273,5222486898325987583\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get_with_http_info(photo_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object photo_ids: 多个作品ID用逗号分隔，单次最多40个/Multiple photo IDs separated by commas, max 40 per request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['photo_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'photo_ids' is set
        if self.api_client.client_side_validation and ('photo_ids' not in params or
                                                       params['photo_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `photo_ids` when calling `fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'photo_ids' in params:
            query_params.append(('photo_ids', params['photo_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/fetch_videos_batch', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get(self, share_object_id, **kwargs):  # noqa: E501
        """生成快手分享链接/Generate Kuaishou share link  # noqa: E501

        # [中文] ### 用途: - 生成快手分享链接 ### 参数: - shareObjectId: 作品ID ### 返回: - 分享链接  # [English] ### Purpose: - Generate Kuaishou share link ### Parameters: - photo_id: Photo ID ### Returns: - Share link  # [示例/Example] shareObjectId = \"3xg5wjqdtekbb3u\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get(share_object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_object_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get_with_http_info(share_object_id, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get_with_http_info(share_object_id, **kwargs)  # noqa: E501
            return data

    def generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get_with_http_info(self, share_object_id, **kwargs):  # noqa: E501
        """生成快手分享链接/Generate Kuaishou share link  # noqa: E501

        # [中文] ### 用途: - 生成快手分享链接 ### 参数: - shareObjectId: 作品ID ### 返回: - 分享链接  # [English] ### Purpose: - Generate Kuaishou share link ### Parameters: - photo_id: Photo ID ### Returns: - Share link  # [示例/Example] shareObjectId = \"3xg5wjqdtekbb3u\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get_with_http_info(share_object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_object_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['share_object_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_object_id' is set
        if self.api_client.client_side_validation and ('share_object_id' not in params or
                                                       params['share_object_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_object_id` when calling `generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_object_id' in params:
            query_params.append(('shareObjectId', params['share_object_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/generate_kuaishou_share_link', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get(self, keyword, **kwargs):  # noqa: E501
        """综合搜索/Comprehensive search  # noqa: E501

        # [中文] ### 用途: - 快手综合搜索接口，支持搜索视频、用户等内容，并提供多维度筛选功能。 ### 参数: - keyword: 搜索关键词（必填） - pcursor: 分页游标，首次请求为空，后续使用响应中的pcursor值 - sort_type: 排序方式     - all: 综合排序（默认）     - newest: 最新发布     - most_likes: 最多点赞 - publish_time: 发布时间筛选     - all: 全部时间（默认）     - one_day: 近一日     - one_week: 近一周     - one_month: 近一月 - duration: 作品时长筛选     - all: 全部时长（默认）     - under_1_min: 1分钟以内     - 1_to_5_min: 1-5分钟     - over_5_min: 5分钟以上 - search_scope: 搜索范围     - all: 全部（默认） ### 返回: - 搜索结果数据  # [English] ### Purpose: - Kuaishou comprehensive search API, supports searching videos, users, etc., and provides multi-dimensional filtering. ### Parameters: - keyword: Search keyword (required) - pcursor: Pagination cursor, empty for first request, use pcursor from response for subsequent pages - sort_type: Sort type     - all: Comprehensive sort (default)     - newest: Latest release     - most_likes: Most likes - publish_time: Publish time filter     - all: All time (default)     - one_day: Last day     - one_week: Last week     - one_month: Last month - duration: Duration filter     - all: All duration (default)     - under_1_min: Under 1 minute     - 1_to_5_min: 1-5 minutes     - over_5_min: Over 5 minutes - search_scope: Search scope     - all: All (default) ### Returns: - Search result data  # [示例/Example] keyword = \"汽车之家\" sort_type = \"most_likes\" publish_time = \"one_week\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: (required)
        :param object pcursor:
        :param object sort_type: 可选值: all(综合排序), newest(最新发布), most_likes(最多点赞)
        :param object publish_time: 可选值: all(全部), one_day(近一日), one_week(近一周), one_month(近一月)
        :param object duration: 可选值: all(全部), under_1_min(1分钟以内), 1_to_5_min(1-5分钟), over_5_min(5分钟以上)
        :param object search_scope: 可选值: all(全部)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """综合搜索/Comprehensive search  # noqa: E501

        # [中文] ### 用途: - 快手综合搜索接口，支持搜索视频、用户等内容，并提供多维度筛选功能。 ### 参数: - keyword: 搜索关键词（必填） - pcursor: 分页游标，首次请求为空，后续使用响应中的pcursor值 - sort_type: 排序方式     - all: 综合排序（默认）     - newest: 最新发布     - most_likes: 最多点赞 - publish_time: 发布时间筛选     - all: 全部时间（默认）     - one_day: 近一日     - one_week: 近一周     - one_month: 近一月 - duration: 作品时长筛选     - all: 全部时长（默认）     - under_1_min: 1分钟以内     - 1_to_5_min: 1-5分钟     - over_5_min: 5分钟以上 - search_scope: 搜索范围     - all: 全部（默认） ### 返回: - 搜索结果数据  # [English] ### Purpose: - Kuaishou comprehensive search API, supports searching videos, users, etc., and provides multi-dimensional filtering. ### Parameters: - keyword: Search keyword (required) - pcursor: Pagination cursor, empty for first request, use pcursor from response for subsequent pages - sort_type: Sort type     - all: Comprehensive sort (default)     - newest: Latest release     - most_likes: Most likes - publish_time: Publish time filter     - all: All time (default)     - one_day: Last day     - one_week: Last week     - one_month: Last month - duration: Duration filter     - all: All duration (default)     - under_1_min: Under 1 minute     - 1_to_5_min: 1-5 minutes     - over_5_min: Over 5 minutes - search_scope: Search scope     - all: All (default) ### Returns: - Search result data  # [示例/Example] keyword = \"汽车之家\" sort_type = \"most_likes\" publish_time = \"one_week\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: (required)
        :param object pcursor:
        :param object sort_type: 可选值: all(综合排序), newest(最新发布), most_likes(最多点赞)
        :param object publish_time: 可选值: all(全部), one_day(近一日), one_week(近一周), one_month(近一月)
        :param object duration: 可选值: all(全部), under_1_min(1分钟以内), 1_to_5_min(1-5分钟), over_5_min(5分钟以上)
        :param object search_scope: 可选值: all(全部)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'pcursor', 'sort_type', 'publish_time', 'duration', 'search_scope']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'pcursor' in params:
            query_params.append(('pcursor', params['pcursor']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'publish_time' in params:
            query_params.append(('publish_time', params['publish_time']))  # noqa: E501
        if 'duration' in params:
            query_params.append(('duration', params['duration']))  # noqa: E501
        if 'search_scope' in params:
            query_params.append(('search_scope', params['search_scope']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/search_comprehensive', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_user_v2_api_v1_kuaishou_app_search_user_v2_get(self, keyword, **kwargs):  # noqa: E501
        """搜索用户V2/Search user V2  # noqa: E501

        # [中文] ### 用途: - 搜索用户 V2 - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。 ### 参数: - keyword: 搜索关键词 - page: 用户页数，从1开始 ### 返回: - 用户数据  # [English] ### Purpose: - Search user V2 - This API is more expensive, but more stable, please check the price list in the user background for specific prices. ### Parameters: - keyword: Search keyword - page: User page number, starting from 1 ### Returns: - User data  # [示例/Example] keyword = \"人工智能\" page = \"1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_user_v2_api_v1_kuaishou_app_search_user_v2_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: (required)
        :param object page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_user_v2_api_v1_kuaishou_app_search_user_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_user_v2_api_v1_kuaishou_app_search_user_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_user_v2_api_v1_kuaishou_app_search_user_v2_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索用户V2/Search user V2  # noqa: E501

        # [中文] ### 用途: - 搜索用户 V2 - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。 ### 参数: - keyword: 搜索关键词 - page: 用户页数，从1开始 ### 返回: - 用户数据  # [English] ### Purpose: - Search user V2 - This API is more expensive, but more stable, please check the price list in the user background for specific prices. ### Parameters: - keyword: Search keyword - page: User page number, starting from 1 ### Returns: - User data  # [示例/Example] keyword = \"人工智能\" page = \"1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_user_v2_api_v1_kuaishou_app_search_user_v2_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: (required)
        :param object page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_user_v2_api_v1_kuaishou_app_search_user_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_user_v2_api_v1_kuaishou_app_search_user_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/search_user_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_video_v2_api_v1_kuaishou_app_search_video_v2_get(self, keyword, **kwargs):  # noqa: E501
        """搜索视频V2/Search video V2  # noqa: E501

        # [中文] ### 用途: - 搜索视频 V2 - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。 ### 参数: - keyword: 搜索关键词 - page: 视频页数，从1开始 ### 返回: - 视频数据  # [English] ### Purpose: - Search video V2 - This API is more expensive, but more stable, please check the price list in the user background for specific prices. ### Parameters: - keyword: Search keyword - page: Page number, starting from 1 ### Returns: - Videos data  # [示例/Example] keyword = \"人工智能\" page = \"1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_video_v2_api_v1_kuaishou_app_search_video_v2_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: (required)
        :param object page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_video_v2_api_v1_kuaishou_app_search_video_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_video_v2_api_v1_kuaishou_app_search_video_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_video_v2_api_v1_kuaishou_app_search_video_v2_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索视频V2/Search video V2  # noqa: E501

        # [中文] ### 用途: - 搜索视频 V2 - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。 ### 参数: - keyword: 搜索关键词 - page: 视频页数，从1开始 ### 返回: - 视频数据  # [English] ### Purpose: - Search video V2 - This API is more expensive, but more stable, please check the price list in the user background for specific prices. ### Parameters: - keyword: Search keyword - page: Page number, starting from 1 ### Returns: - Videos data  # [示例/Example] keyword = \"人工智能\" page = \"1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_video_v2_api_v1_kuaishou_app_search_video_v2_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: (required)
        :param object page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_video_v2_api_v1_kuaishou_app_search_video_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_video_v2_api_v1_kuaishou_app_search_video_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/app/search_video_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
