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


class KuaishouWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get(self, share_link, **kwargs):  # noqa: E501
        """获取用户ID/Fetch user ID  # noqa: E501

        # [中文] ### 用途: - 通过用户分享链接获取用户ID ### 参数: - share_link: 用户分享链接 ### 返回: - 用户ID  # [English] ### Purpose: - Fetch user ID via user share link ### Parameters: - share_link: User share link ### Returns: - User ID  # [示例/Example] share_link = \"https://v.kuaishou.com/KcdKDwFp\"  share_link = \"https://c.kuaishou.com/fw/user/3xcuu5habgc8z29\"  share_link = \"https://live.kuaishou.com/profile/3xcuu5habgc8z29?fid=2357689552&cc=share_copylink\"  # [返回示例/Example Response] ```json ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get_with_http_info(share_link, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get_with_http_info(share_link, **kwargs)  # noqa: E501
            return data

    def fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get_with_http_info(self, share_link, **kwargs):  # noqa: E501
        """获取用户ID/Fetch user ID  # noqa: E501

        # [中文] ### 用途: - 通过用户分享链接获取用户ID ### 参数: - share_link: 用户分享链接 ### 返回: - 用户ID  # [English] ### Purpose: - Fetch user ID via user share link ### Parameters: - share_link: User share link ### Returns: - User ID  # [示例/Example] share_link = \"https://v.kuaishou.com/KcdKDwFp\"  share_link = \"https://c.kuaishou.com/fw/user/3xcuu5habgc8z29\"  share_link = \"https://live.kuaishou.com/profile/3xcuu5habgc8z29?fid=2357689552&cc=share_copylink\"  # [返回示例/Example Response] ```json ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get_with_http_info(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['share_link']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_link' is set
        if self.api_client.client_side_validation and ('share_link' not in params or
                                                       params['share_link'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_link` when calling `fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_link' in params:
            query_params.append(('share_link', params['share_link']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/web/fetch_get_user_id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get(self, **kwargs):  # noqa: E501
        """获取快手热榜 V1/Fetch Kuaishou Hot List V1  # noqa: E501

        # [中文] ### 用途: - 获取快手热榜 V1 ### 参数: - 无 ### 返回: - 快手热榜 V1 列表  # [English] ### Purpose: - Fetch Kuaishou Hot List V1 ### Parameters: - None ### Returns: - Kuaishou Hot List V1  # [示例/Example]  # [返回示例/Example Response] ```json  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取快手热榜 V1/Fetch Kuaishou Hot List V1  # noqa: E501

        # [中文] ### 用途: - 获取快手热榜 V1 ### 参数: - 无 ### 返回: - 快手热榜 V1 列表  # [English] ### Purpose: - Fetch Kuaishou Hot List V1 ### Parameters: - None ### Returns: - Kuaishou Hot List V1  # [示例/Example]  # [返回示例/Example Response] ```json  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get_with_http_info(async_req=True)
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
                    " to method fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get" % key
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
            '/api/v1/kuaishou/web/fetch_kuaishou_hot_list_v1', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get(self, **kwargs):  # noqa: E501
        """获取快手热榜 V2/Fetch Kuaishou Hot List V2  # noqa: E501

        # [中文] ### 用途: - 获取快手热榜 V2 ### 参数: - board_type 榜单类型，默认值为 1:     1 - 热榜     2 - 文娱     3 - 社会     4 - 有用     5 - 挑战     6 - 搜索 ### 返回: - 快手热榜 V2 列表  # [English] ### Purpose: - Fetch Kuaishou Hot List V2 ### Parameters: - board_type: Board Type, default is 1:     1 - Hot List     2 - Entertainment     3 - Society     4 - Useful     5 - Challenge     6 - Search ### Returns: - Kuaishou Hot List V2  # [示例/Example]  # [返回示例/Example Response] ```json  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object board_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取快手热榜 V2/Fetch Kuaishou Hot List V2  # noqa: E501

        # [中文] ### 用途: - 获取快手热榜 V2 ### 参数: - board_type 榜单类型，默认值为 1:     1 - 热榜     2 - 文娱     3 - 社会     4 - 有用     5 - 挑战     6 - 搜索 ### 返回: - 快手热榜 V2 列表  # [English] ### Purpose: - Fetch Kuaishou Hot List V2 ### Parameters: - board_type: Board Type, default is 1:     1 - Hot List     2 - Entertainment     3 - Society     4 - Useful     5 - Challenge     6 - Search ### Returns: - Kuaishou Hot List V2  # [示例/Example]  # [返回示例/Example Response] ```json  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object board_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['board_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'board_type' in params:
            query_params.append(('board_type', params['board_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/web/fetch_kuaishou_hot_list_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get(self, share_text, **kwargs):  # noqa: E501
        """获取单个作品数据 V1/Get single video data V1  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据，此接口不支持图文作品。 ### 参数: - share_text: 作品分享链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video data, this interface does not support photo only posts. ### Parameters: - share_text: Photo share link ### Returns: - Video data  # [示例/Example] share_text = \"https://www.kuaishou.com/f/X-f2k5KJpiXN1SY\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get(share_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get_with_http_info(share_text, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get_with_http_info(share_text, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get_with_http_info(self, share_text, **kwargs):  # noqa: E501
        """获取单个作品数据 V1/Get single video data V1  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据，此接口不支持图文作品。 ### 参数: - share_text: 作品分享链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video data, this interface does not support photo only posts. ### Parameters: - share_text: Photo share link ### Returns: - Video data  # [示例/Example] share_text = \"https://www.kuaishou.com/f/X-f2k5KJpiXN1SY\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get_with_http_info(share_text, async_req=True)
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
                    " to method fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_text' is set
        if self.api_client.client_side_validation and ('share_text' not in params or
                                                       params['share_text'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_text` when calling `fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get`")  # noqa: E501

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
            '/api/v1/kuaishou/web/fetch_one_video', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get(self, url, **kwargs):  # noqa: E501
        """链接获取作品数据/Fetch single video by URL  # noqa: E501

        # [中文] ### 用途: - 根据链接获取单个作品数据 ### 参数: - url: 作品链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video by URL ### Parameters: - url: Photo URL ### Returns: - Video data  # [示例/Example] url = \"https://v.kuaishou.com/GKTpYm\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """链接获取作品数据/Fetch single video by URL  # noqa: E501

        # [中文] ### 用途: - 根据链接获取单个作品数据 ### 参数: - url: 作品链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video by URL ### Parameters: - url: Photo URL ### Returns: - Video data  # [示例/Example] url = \"https://v.kuaishou.com/GKTpYm\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_with_http_info(url, async_req=True)
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
                    " to method fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get`")  # noqa: E501

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
            '/api/v1/kuaishou/web/fetch_one_video_by_url', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get(self, photo_id, **kwargs):  # noqa: E501
        """获取作品一级评论/Fetch video comments  # noqa: E501

        # [中文] ### 用途: - 获取单个作品评论数据 ### 参数: - photo_id: 作品ID - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 评论数据  # [English] ### Purpose: - Fetch single video comment data ### Parameters: - photo_id: Photo ID - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Comments data  # [示例/Example] photo_id = \"3x7gxp2zhgjv832\" pcursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get(photo_id, async_req=True)
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
            return self.fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get_with_http_info(photo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get_with_http_info(photo_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get_with_http_info(self, photo_id, **kwargs):  # noqa: E501
        """获取作品一级评论/Fetch video comments  # noqa: E501

        # [中文] ### 用途: - 获取单个作品评论数据 ### 参数: - photo_id: 作品ID - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 评论数据  # [English] ### Purpose: - Fetch single video comment data ### Parameters: - photo_id: Photo ID - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Comments data  # [示例/Example] photo_id = \"3x7gxp2zhgjv832\" pcursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get_with_http_info(photo_id, async_req=True)
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
                    " to method fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'photo_id' is set
        if self.api_client.client_side_validation and ('photo_id' not in params or
                                                       params['photo_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `photo_id` when calling `fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get`")  # noqa: E501

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
            '/api/v1/kuaishou/web/fetch_one_video_comment', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get(self, photo_id, root_comment_id, **kwargs):  # noqa: E501
        """获取作品二级评论/Fetch video sub comments  # noqa: E501

        # [中文] ### 用途: - 获取单个作品二级评论数据 ### 参数: - photo_id: 作品ID - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 - root_comment_id: 根评论ID ### 返回: - 评论数据  # [English] ### Purpose: - Fetch single video comment data ### Parameters: - photo_id: Photo ID - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. - root_comment_id: Root comment ID ### Returns: - Comments data  # [示例/Example] photo_id = \"3xgarycnydawq3g\" pcursor = \"909377053156\" root_comment_id = \"908850553827\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get(photo_id, root_comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object photo_id: (required)
        :param object root_comment_id: (required)
        :param object pcursor:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get_with_http_info(photo_id, root_comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get_with_http_info(photo_id, root_comment_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get_with_http_info(self, photo_id, root_comment_id, **kwargs):  # noqa: E501
        """获取作品二级评论/Fetch video sub comments  # noqa: E501

        # [中文] ### 用途: - 获取单个作品二级评论数据 ### 参数: - photo_id: 作品ID - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 - root_comment_id: 根评论ID ### 返回: - 评论数据  # [English] ### Purpose: - Fetch single video comment data ### Parameters: - photo_id: Photo ID - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. - root_comment_id: Root comment ID ### Returns: - Comments data  # [示例/Example] photo_id = \"3xgarycnydawq3g\" pcursor = \"909377053156\" root_comment_id = \"908850553827\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get_with_http_info(photo_id, root_comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object photo_id: (required)
        :param object root_comment_id: (required)
        :param object pcursor:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['photo_id', 'root_comment_id', 'pcursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'photo_id' is set
        if self.api_client.client_side_validation and ('photo_id' not in params or
                                                       params['photo_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `photo_id` when calling `fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get`")  # noqa: E501
        # verify the required parameter 'root_comment_id' is set
        if self.api_client.client_side_validation and ('root_comment_id' not in params or
                                                       params['root_comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `root_comment_id` when calling `fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'photo_id' in params:
            query_params.append(('photo_id', params['photo_id']))  # noqa: E501
        if 'pcursor' in params:
            query_params.append(('pcursor', params['pcursor']))  # noqa: E501
        if 'root_comment_id' in params:
            query_params.append(('root_comment_id', params['root_comment_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/kuaishou/web/fetch_one_video_sub_comment', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get(self, photo_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 快手单一视频查询接口V2 ### 参数: - photo_id: 作品ID，作品ID可以从作品链接中提取 ### 返回: - 视频数据  # [English] ### Purpose: - Kuaishou single video query API V2 ### Parameters: - photo_id: Photo ID, the photo ID can be extracted from the photo link ### Returns: - Video data  # [示例/Example] photo_id = \"3xtdqvdnqd3psuc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get(photo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object photo_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_with_http_info(photo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_with_http_info(photo_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_with_http_info(self, photo_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 快手单一视频查询接口V2 ### 参数: - photo_id: 作品ID，作品ID可以从作品链接中提取 ### 返回: - 视频数据  # [English] ### Purpose: - Kuaishou single video query API V2 ### Parameters: - photo_id: Photo ID, the photo ID can be extracted from the photo link ### Returns: - Video data  # [示例/Example] photo_id = \"3xtdqvdnqd3psuc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_with_http_info(photo_id, async_req=True)
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
                    " to method fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'photo_id' is set
        if self.api_client.client_side_validation and ('photo_id' not in params or
                                                       params['photo_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `photo_id` when calling `fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get`")  # noqa: E501

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
            '/api/v1/kuaishou/web/fetch_one_video_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户收藏作品/Fetch user collect  # noqa: E501

        # [中文] ### 用途: - 获取用户收藏作品 ### 参数: - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取 - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid - 备注：不支持使用uid也就是纯数字的用户ID查询 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 用户收藏作品列表  # [English] ### Purpose: - Fetch user favorite - Note: This API requires the user's eid, which can be extracted from the user's profile URL. - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq. - Note: Querying with uid (pure numeric user ID) is not supported. ### Parameters: - user_id: User ID - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - User favorite list  # [示例/Example] user_id = \"3xz63mn6fngqtiq\" pcursor = None  # [返回示例/Example Response] ```json  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get(user_id, async_req=True)
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
            return self.fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户收藏作品/Fetch user collect  # noqa: E501

        # [中文] ### 用途: - 获取用户收藏作品 ### 参数: - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取 - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid - 备注：不支持使用uid也就是纯数字的用户ID查询 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 用户收藏作品列表  # [English] ### Purpose: - Fetch user favorite - Note: This API requires the user's eid, which can be extracted from the user's profile URL. - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq. - Note: Querying with uid (pure numeric user ID) is not supported. ### Parameters: - user_id: User ID - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - User favorite list  # [示例/Example] user_id = \"3xz63mn6fngqtiq\" pcursor = None  # [返回示例/Example Response] ```json  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get_with_http_info(user_id, async_req=True)
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
                    " to method fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get`")  # noqa: E501

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
            '/api/v1/kuaishou/web/fetch_user_collect', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息/Fetch user info  # noqa: E501

        # [中文]     ### 用途:     - 获取用户信息     - 备注：     - 此接口在请求时请将超时时间设置为30秒以上，否则可能会导致客户端未及时收到请求响应并且导致计费。     - 此接口由于风控的特殊性，我们尽可能保持稳定，但仍然无法保证100%稳定，如果遇到请求失败，请稍后重试。     - 推荐一直重复请求，直到成功为止，并且超时时间设置为30秒以上。     ### 参数:     - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取     - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid     - 备注：不支持使用uid也就是纯数字的用户ID查询     ### 返回:     - 用户信息，包括昵称、头像、粉丝数、关注数、获赞数、性别等      # [English]     ### Purpose:     - Fetch user info     - Note: This API requires the user's eid, which can be extracted from the user's profile URL.     - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq.     - Note: Querying with uid (pure numeric user ID) is not supported.     - Note: Please set the timeout to more than 30 seconds when making requests to this API, otherwise it may cause the client to not receive the response in time and result in billing.     - Due to the special nature of risk control for this API, we try to keep it stable, but we still cannot guarantee 100% stability. If you encounter a request failure, please try again later.     - It is recommended to keep retrying until successful, and set the timeout to more than 30 seconds.     ### Parameters:     - user_id: User ID     ### Returns:     - User info, including nickname, avatar, number of followers, number of followings, number      # [示例/Example]     user_id = \"3xz63mn6fngqtiq\"      # [返回示例/Example Response]     ```json     {         \"code\": 200,         \"request_id\": \"782e6fa2-4c8e-4fac-b151-78db03c10b8d\",         \"router\": \"/api/v1/kuaishou/web/fetch_user_info\",         \"params\": {             \"user_id\": \"3xz63mn6fngqtiq\"         },         \"data\": {             \"result\": 1,             \"userProfile\": {                 \"profile\": {                     \"user_profile_bg_url\": \"//s2-10623.kwimgs.com/kos/nlav10623/vision_images/profile_background.5bc08b1bf4fba1f4.svg\",                     \"user_id\": \"3xz63mn6fngqtiq\",                     \"user_name\": \"权少爱吃小汉堡🍔\",                     \"headurl\": \"https://p66-pro.a.yximgs.com/uhead/AB/2025/08/11/21/BMjAyNTA4MTEyMTEyNDlfMjI4OTA1ODAyXzFfaGQ5ODdfODg4_s.jpg\",                     \"user_text\": \"感谢你的关注木木哒 我玩得游戏叫:Gmod  禁止冒充搬运视频 违者必究\"                 },                 \"gender\": \"M\",                 \"showCollectTab\": false,                 \"livingInfo\": {                     \"living\": false,                     \"livingId\": null,                     \"iconType\": 0                 },                 \"ownerCount\": {                     \"fan\": 4300985,                     \"like\": 37676016,                     \"follow\": 198,                     \"photo_public\": 237                 },                 \"userDefineId\": \"quanshaogmod\",                 \"isFollowing\": false,                 \"isUserIsolated\": false             },             \"host-name\": \"public-bjzey-c3-kce-node67.idchb1az3.hb1.kwaidc.com\"         }     }     ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息/Fetch user info  # noqa: E501

        # [中文]     ### 用途:     - 获取用户信息     - 备注：     - 此接口在请求时请将超时时间设置为30秒以上，否则可能会导致客户端未及时收到请求响应并且导致计费。     - 此接口由于风控的特殊性，我们尽可能保持稳定，但仍然无法保证100%稳定，如果遇到请求失败，请稍后重试。     - 推荐一直重复请求，直到成功为止，并且超时时间设置为30秒以上。     ### 参数:     - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取     - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid     - 备注：不支持使用uid也就是纯数字的用户ID查询     ### 返回:     - 用户信息，包括昵称、头像、粉丝数、关注数、获赞数、性别等      # [English]     ### Purpose:     - Fetch user info     - Note: This API requires the user's eid, which can be extracted from the user's profile URL.     - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq.     - Note: Querying with uid (pure numeric user ID) is not supported.     - Note: Please set the timeout to more than 30 seconds when making requests to this API, otherwise it may cause the client to not receive the response in time and result in billing.     - Due to the special nature of risk control for this API, we try to keep it stable, but we still cannot guarantee 100% stability. If you encounter a request failure, please try again later.     - It is recommended to keep retrying until successful, and set the timeout to more than 30 seconds.     ### Parameters:     - user_id: User ID     ### Returns:     - User info, including nickname, avatar, number of followers, number of followings, number      # [示例/Example]     user_id = \"3xz63mn6fngqtiq\"      # [返回示例/Example Response]     ```json     {         \"code\": 200,         \"request_id\": \"782e6fa2-4c8e-4fac-b151-78db03c10b8d\",         \"router\": \"/api/v1/kuaishou/web/fetch_user_info\",         \"params\": {             \"user_id\": \"3xz63mn6fngqtiq\"         },         \"data\": {             \"result\": 1,             \"userProfile\": {                 \"profile\": {                     \"user_profile_bg_url\": \"//s2-10623.kwimgs.com/kos/nlav10623/vision_images/profile_background.5bc08b1bf4fba1f4.svg\",                     \"user_id\": \"3xz63mn6fngqtiq\",                     \"user_name\": \"权少爱吃小汉堡🍔\",                     \"headurl\": \"https://p66-pro.a.yximgs.com/uhead/AB/2025/08/11/21/BMjAyNTA4MTEyMTEyNDlfMjI4OTA1ODAyXzFfaGQ5ODdfODg4_s.jpg\",                     \"user_text\": \"感谢你的关注木木哒 我玩得游戏叫:Gmod  禁止冒充搬运视频 违者必究\"                 },                 \"gender\": \"M\",                 \"showCollectTab\": false,                 \"livingInfo\": {                     \"living\": false,                     \"livingId\": null,                     \"iconType\": 0                 },                 \"ownerCount\": {                     \"fan\": 4300985,                     \"like\": 37676016,                     \"follow\": 198,                     \"photo_public\": 237                 },                 \"userDefineId\": \"quanshaogmod\",                 \"isFollowing\": false,                 \"isUserIsolated\": false             },             \"host-name\": \"public-bjzey-c3-kce-node67.idchb1az3.hb1.kwaidc.com\"         }     }     ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get_with_http_info(user_id, async_req=True)
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
                    " to method fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get`")  # noqa: E501

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
            '/api/v1/kuaishou/web/fetch_user_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户直播回放/Fetch user live replay  # noqa: E501

        # [中文] ### 用途: - 获取用户直播回放列表 ### 参数: - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取 - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid - 备注：不支持使用uid也就是纯数字的用户ID查询 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 用户直播回放列表  # [English] ### Purpose: - Fetch user live replay - Note: This API requires the user's eid, which can be extracted from the user's profile URL. - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq. - Note: Querying with uid (pure numeric user ID) is not supported. ### Parameters: - user_id: User ID - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - User live replay list  # [示例/Example] user_id = \"3xz63mn6fngqtiq\" pcursor = None  # [返回示例/Example Response] ```json  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get(user_id, async_req=True)
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
            return self.fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户直播回放/Fetch user live replay  # noqa: E501

        # [中文] ### 用途: - 获取用户直播回放列表 ### 参数: - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取 - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid - 备注：不支持使用uid也就是纯数字的用户ID查询 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 用户直播回放列表  # [English] ### Purpose: - Fetch user live replay - Note: This API requires the user's eid, which can be extracted from the user's profile URL. - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq. - Note: Querying with uid (pure numeric user ID) is not supported. ### Parameters: - user_id: User ID - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - User live replay list  # [示例/Example] user_id = \"3xz63mn6fngqtiq\" pcursor = None  # [返回示例/Example Response] ```json  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get_with_http_info(user_id, async_req=True)
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
                    " to method fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get`")  # noqa: E501

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
            '/api/v1/kuaishou/web/fetch_user_live_replay', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户发布作品/Fetch user posts  # noqa: E501

        # [中文] ### 用途: - 获取用户作品列表 ### 参数: - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取 - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid - 备注： - 不支持使用uid也就是纯数字的用户ID查询 - 此接口在请求时请将超时时间设置为30秒以上，否则可能会导致客户端未及时收到请求响应并且导致计费。 - 此接口由于风控的特殊性，我们尽可能保持稳定，但仍然无法保证100%稳定，如果遇到请求失败，请稍后重试。 - 推荐一直重复请求，直到成功为止，并且超时时间设置为30秒以上。 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 用户作品列表  # [English] ### Purpose: - Fetch user posts - Note: This API requires the user's eid, which can be extracted from the user's profile URL. - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq. - Note: - Querying with uid (pure numeric user ID) is not supported. - Note: Please set the timeout to more than 30 seconds when making requests to this API, otherwise it may cause the client to not receive the response in time and result in billing. - Due to the special nature of risk control for this API, we try to keep it - stable, but we still cannot guarantee 100% stability. If you encounter a request failure, please try again later. - It is recommended to keep retrying until successful, and set the timeout to more than 30 seconds. ### Parameters: - user_id: User ID - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - User posts list  # [示例/Example] user_id = \"3xz63mn6fngqtiq\" pcursor = None  # [部分返回示例/Part Example Response] ```json {     \"code\": 200,     \"request_id\": \"de055431-bf7d-4a24-a332-9cc1654ab247\",     \"router\": \"/api/v1/kuaishou/web/fetch_user_post\",     \"params\": {         \"user_id\": \"3xz63mn6fngqtiq\",         \"pcursor\": \"1.698748219278E12\"     },     \"data\": {         \"result\": 1,         \"pcursor\": \"1.692702206373E12\",         \"feeds\": [             {                 \"type\": 1,                 \"photo\": {                     \"manifestH265\": {                         \"version\": \"1.0.0\",                         \"businessType\": 2,                         \"mediaType\": 2,                         \"videoId\": \"b1a31deb8e75e7be\",                         \"hideAuto\": false,                         \"manualDefaultSelect\": false,                         \"stereoType\": 0,                         \"adaptationSet\": [                             {                                 \"id\": 1,                                 \"duration\": 84937,                                 \"representation\": [                                     {                                         \"id\": 1,                                         \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_hd15_Bfb2327ef432b8e22bee0565c052210d0.mp4?tag=1-1756664181-unknown-0-4pez7u9yx4-11bcd04505e80c93&provider=self&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=hd15&ss=vpm\",                                         \"backupUrl\": [                                             \"https://v1.kwaicdn.com/ksc2/WsLapasbDJwa_d5-gSoI2EwR1RYcYI6MpzWrlOzqoBPJ1eG7TRpv8UtWiNxv2xy-tsiAXr2VvmiqAJQmxNCMawMQCe7orKomsXk6v-GJKt55XiiE9GdcOTmXM0Uj_MN1np_i8ffWmDHyxrrCfhiIKRMXGETtR5BcJTIxz5hg3BgWZAEVV8VxRcZ2PwP4phUM.mp4?pkey=AAWWdaRz9xwLglSkzE1QAdM0NoasskNdA0fRCgDJSWyTPo4tra_0jYCqgP_ieXHG4ky9vMQafXhiVaetL-iijtgENHHeQG2YMY8NxTVz_PjB8T1hTNmOXW8mQTnf2NHOa0k&tag=1-1756664181-unknown-1-0vq1m73bcl-d99c4fa7dba7dbf0&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=hd15&ss=vpm\"                                         ],                                         \"maxBitrate\": 3000,                                         \"avgBitrate\": 1622,                                         \"width\": 1280,                                         \"height\": 720,                                         \"frameRate\": 60.0,                                         \"quality\": 1.5,                                         \"kvqScore\": {                                             \"FR\": -1.0,                                             \"NR\": 3.4632160663604736,                                             \"FRPost\": -1.0,                                             \"NRPost\": -1.0,                                             \"sharpness\": 0.4285,                                             \"blur\": 0.2377                                         },                                         \"qualityType\": \"720p\",                                         \"qualityLabel\": \"高清\",                                         \"featureP2sp\": false,                                         \"p2spCode\": \"{\"fRsn\":0,\"fixOpt\":-1,\"schTask\":\"\",\"schCode\":-1,\"schRes\":\"\",\"pushTask\":\"v=0&p=0&s=0&d=0\",\"pushCode\":-1}\",                                         \"hidden\": false,                                         \"disableAdaptive\": false,                                         \"defaultSelect\": false,                                         \"comment\": \"videoId=b1a31deb8e75e7be/ttExplain=HEVC_Turbo2_720P_高码率/tt=hd15\",                                         \"hdrType\": 0,                                         \"fileSize\": 17227811,                                         \"agc\": false,                                         \"mute\": false,                                         \"oriLoudness\": 0.0,                                         \"makeupGain\": 0.0,                                         \"realLoudness\": -9.532,                                         \"realNormalizeGain\": 1.0,                                         \"normalizeGain\": 0.0                                     }                                 ]                             }                         ],                         \"playInfo\": {                             \"bizType\": 0,                             \"cdnTimeRangeLevel\": 0                         },                         \"videoFeature\": {                             \"blurProbability\": 0.02436523512005806,                             \"blockyProbability\": 0.5486664772033691,                             \"avgEntropy\": 11.74826078414917,                             \"mosScore\": 0.6893717646598816                         }                     },                     \"photoUrls\": [                         {                             \"cdn\": \"k0u2ayecy7bycz.djvod.ndcimgs.com\",                             \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_b_Baea19a439f265123a9b5c73a99b387c9.mp4?tag=1-1756664181-unknown-0-ngtc9b5fkw-400249aac756fa3c&provider=self&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=b&ss=vps\"                         },                         {                             \"cdn\": \"v2.kwaicdn.com\",                             \"url\": \"https://v2.kwaicdn.com/ksc2/PtGMNZW1atApoKjZtdZAeYBv_Hk3rukAMsduvp-BRuBp66aB3ZFXpDnlTON3Xy5ehrz5fc5c4ys3g0Nays7EXtftXSi7JkRjPKFMN-vbPXVZ68800hSKYaFZejJUW1GKp2ttjc9vIgAKHkCkn1E8e709mnQxJz6nzJRRixcAEvJ6PxVraa3OqiGkiA12zLt0.mp4?pkey=AAVID_YMrWOJ06oySpzkfx8i-z7z8Iyx34JyeXW13PQLMfVfPDvy1b0cEQh_2ri0Bs7F_GvTuADCNUK0SR0f0zes8DixR10HM6lJQkpQ64nHhqlVoxHkP9DQGPvgr1nZ-l4&tag=1-1756664181-unknown-1-cpfxvlhxnd-8304a252b8387036&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=b&ss=vps\"                         }                     ],                     \"manifest\": {                         \"version\": \"1.0.0\",                         \"businessType\": 2,                         \"mediaType\": 2,                         \"videoId\": \"b1a31deb8e75e7be\",                         \"hideAuto\": false,                         \"manualDefaultSelect\": false,                         \"stereoType\": 0,                         \"adaptationSet\": [                             {                                 \"id\": 1,                                 \"duration\": 84937,                                 \"representation\": [                                     {                                         \"id\": 1,                                         \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_b_Baea19a439f265123a9b5c73a99b387c9.mp4?tag=1-1756664181-unknown-0-raca8mq3p7-df6cf126f2ba1979&provider=self&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=b&ss=vpm\",                                         \"backupUrl\": [                                             \"https://v2.kwaicdn.com/ksc2/PtGMNZW1atApoKjZtdZAeYBv_Hk3rukAMsduvp-BRuBp66aB3ZFXpDnlTON3Xy5ehrz5fc5c4ys3g0Nays7EXtftXSi7JkRjPKFMN-vbPXVZ68800hSKYaFZejJUW1GKp2ttjc9vIgAKHkCkn1E8e709mnQxJz6nzJRRixcAEvJ6PxVraa3OqiGkiA12zLt0.mp4?pkey=AAUkTComC4sD_jFDy6Q8DZvnU7bttEcUKZYUyPGThMFjvLORo0aHnSv2Y7qhYldRnSBe9H1NRLi9yC1zprgWULvlD6mm7Q8pWup3vG3BabToQqpNmpHI2hwzk6m0UE-8j38&tag=1-1756664181-unknown-1-frwqzvnubq-3aeb9dc39d8958ed&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=b&ss=vpm\"                                         ],                                         \"maxBitrate\": 4900,                                         \"avgBitrate\": 3482,                                         \"width\": 1280,                                         \"height\": 720,                                         \"frameRate\": 60.0,                                         \"quality\": 1.5,                                         \"kvqScore\": {                                             \"FR\": -1.0,                                             \"NR\": 3.5491535663604736,                                             \"FRPost\": -1.0,                                             \"NRPost\": -1.0,                                             \"sharpness\": 0.3316,                                             \"blur\": 0.2374                                         },                                         \"qualityType\": \"720p\",                                         \"qualityLabel\": \"高清\",                                         \"featureP2sp\": false,                                         \"p2spCode\": \"{\"fRsn\":0,\"fixOpt\":-1,\"schTask\":\"\",\"schCode\":-1,\"schRes\":\"\",\"pushTask\":\"v=0&p=0&s=0&d=0\",\"pushCode\":-1}\",                                         \"hidden\": false,                                         \"disableAdaptive\": false,                                         \"defaultSelect\": false,                                         \"comment\": \"videoId=b1a31deb8e75e7be/ttExplain=AVC_VeryFast_720P_高码率_Basic/tt=b\",                                         \"hdrType\": 0,                                         \"fileSize\": 36976273,                                         \"bitratePattern\": [                                             5000,                                             3471,                                             6733,                                             481,                                             1569                                         ],                                         \"agc\": false,                                         \"mute\": false,                                         \"oriLoudness\": 0.0,                                         \"makeupGain\": 0.0,                                         \"realLoudness\": -9.532,                                         \"realNormalizeGain\": 1.0,                                         \"normalizeGain\": 0.0                                     }                                 ]                             }                         ],                         \"playInfo\": {                             \"bizType\": 0,                             \"cdnTimeRangeLevel\": 0                         },                         \"videoFeature\": {                             \"blurProbability\": 0.02436523512005806,                             \"blockyProbability\": 0.5486664772033691,                             \"avgEntropy\": 11.74826078414917,                             \"mosScore\": 0.6893717646598816                         }                     },                     \"photoH265Urls\": [                         {                             \"cdn\": \"k0u2ayecy7bycz.djvod.ndcimgs.com\",                             \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_hd15_Bfb2327ef432b8e22bee0565c052210d0.mp4?tag=1-1756664181-unknown-0-ra3mc5pqwz-b5d377ade7d0a512&provider=self&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=hd15&ss=vps\"                         },                         {                             \"cdn\": \"v1.kwaicdn.com\",                             \"url\": \"https://v1.kwaicdn.com/ksc2/WsLapasbDJwa_d5-gSoI2EwR1RYcYI6MpzWrlOzqoBPJ1eG7TRpv8UtWiNxv2xy-tsiAXr2VvmiqAJQmxNCMawMQCe7orKomsXk6v-GJKt55XiiE9GdcOTmXM0Uj_MN1np_i8ffWmDHyxrrCfhiIKRMXGETtR5BcJTIxz5hg3BgWZAEVV8VxRcZ2PwP4phUM.mp4?pkey=AAVktrin9oeeededNfrZf8LaIR1CvEQJ8FlSEH5iw-Azi03uiv1Eh297Xfd7f6yLLkZNDEyqFg4KqNphKlDhQmAw3TKsBqJYmLfLtR3cRWzJ5VY6FadrIRrGZvuCwgCob4A&tag=1-1756664181-unknown-1-tx8vx8qkhx-44a6a7306fccf2ff&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=hd15&ss=vps\"                         }                     ],                     \"viewCount\": 1594389,                     \"width\": 1280,                     \"id\": \"3xezqrk27gdc5a4\",                     \"animatedCoverUrl\": \"https://p1.a.yximgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_animatedV5_Beaaaeb032c640d38decbda1f52bc209e.webp?tag=1-1756664181-xpcwebprofile-0-tdiakvxcxz-98dff964a1098863&clientCacheKey=3xezqrk27gdc5a4_animatedV5.webp&di=3da39dcf&bp=14734\",                     \"overrideCoverUrl\": \"https://p1.a.yximgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_ccc_B39cbb17aaf65e0a76080064fd78dfc64.jpg?tag=1-1756664181-xpcwebprofile-0-gg941gqowe-afd116662be96449&clientCacheKey=3xezqrk27gdc5a4_ccc.jpg&di=3da39dcf&bp=14734\",                     \"collectCount\": 22057,                     \"riskTagContent\": null,                     \"expTag\": \"1_a/2008712974016392641_xpcwebprofilexxnull0\",                     \"riskTagUrl\": null,                     \"timestamp\": 1698748219278,                     \"stereoType\": 0,                     \"likeCount\": 75604,                     \"collected\": false,                     \"duration\": 84816,                     \"liked\": false,                     \"coverUrl\": \"https://p1.a.yximgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_ccc_B39cbb17aaf65e0a76080064fd78dfc64.jpg?tag=1-1756664181-xpcwebprofile-0-lznq3kgead-b3f7c6ea108bb5d1&clientCacheKey=3xezqrk27gdc5a4_ccc.jpg&di=3da39dcf&bp=14734\",                     \"caption\": \"健 身 鸭 脖\",                     \"height\": 720                 },                 \"author\": {                     \"id\": \"3xz63mn6fngqtiq\",                     \"headerUrl\": \"https://p66-pro.a.yximgs.com/uhead/AB/2025/08/11/21/BMjAyNTA4MTEyMTEyNDlfMjI4OTA1ODAyXzFfaGQ5ODdfODg4_s.jpg\",                     \"livingInfo\": {                         \"living\": false,                         \"livingId\": null,                         \"iconType\": 0                     },                     \"name\": \"权少爱吃小汉堡🍔\",                     \"following\": false                 },                 \"comment\": {                     \"us_c\": 0                 },                 \"danmakuSwitch\": true             }             },         ],         \"llsid\": \"2008712974016392641\",         \"host-name\": \"public-bjx-c26-kce-node642.idchb1az1.hb1.kwaidc.com\",         \"webPageArea\": \"profilexxnull\"     } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get(user_id, async_req=True)
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
            return self.fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户发布作品/Fetch user posts  # noqa: E501

        # [中文] ### 用途: - 获取用户作品列表 ### 参数: - user_id: 用户ID，这个接口需要传入用户的 eid，可以从用户主页链接中提取 - 例如：https://www.kuaishou.com/profile/3xz63mn6fngqtiq 其中 3xz63mn6fngqtiq 即为用户的 eid - 备注： - 不支持使用uid也就是纯数字的用户ID查询 - 此接口在请求时请将超时时间设置为30秒以上，否则可能会导致客户端未及时收到请求响应并且导致计费。 - 此接口由于风控的特殊性，我们尽可能保持稳定，但仍然无法保证100%稳定，如果遇到请求失败，请稍后重试。 - 推荐一直重复请求，直到成功为止，并且超时时间设置为30秒以上。 - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 用户作品列表  # [English] ### Purpose: - Fetch user posts - Note: This API requires the user's eid, which can be extracted from the user's profile URL. - For example: In the URL https://www.kuaishou.com/profile/3xz63mn6fngqtiq, the eid is 3xz63mn6fngqtiq. - Note: - Querying with uid (pure numeric user ID) is not supported. - Note: Please set the timeout to more than 30 seconds when making requests to this API, otherwise it may cause the client to not receive the response in time and result in billing. - Due to the special nature of risk control for this API, we try to keep it - stable, but we still cannot guarantee 100% stability. If you encounter a request failure, please try again later. - It is recommended to keep retrying until successful, and set the timeout to more than 30 seconds. ### Parameters: - user_id: User ID - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - User posts list  # [示例/Example] user_id = \"3xz63mn6fngqtiq\" pcursor = None  # [部分返回示例/Part Example Response] ```json {     \"code\": 200,     \"request_id\": \"de055431-bf7d-4a24-a332-9cc1654ab247\",     \"router\": \"/api/v1/kuaishou/web/fetch_user_post\",     \"params\": {         \"user_id\": \"3xz63mn6fngqtiq\",         \"pcursor\": \"1.698748219278E12\"     },     \"data\": {         \"result\": 1,         \"pcursor\": \"1.692702206373E12\",         \"feeds\": [             {                 \"type\": 1,                 \"photo\": {                     \"manifestH265\": {                         \"version\": \"1.0.0\",                         \"businessType\": 2,                         \"mediaType\": 2,                         \"videoId\": \"b1a31deb8e75e7be\",                         \"hideAuto\": false,                         \"manualDefaultSelect\": false,                         \"stereoType\": 0,                         \"adaptationSet\": [                             {                                 \"id\": 1,                                 \"duration\": 84937,                                 \"representation\": [                                     {                                         \"id\": 1,                                         \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_hd15_Bfb2327ef432b8e22bee0565c052210d0.mp4?tag=1-1756664181-unknown-0-4pez7u9yx4-11bcd04505e80c93&provider=self&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=hd15&ss=vpm\",                                         \"backupUrl\": [                                             \"https://v1.kwaicdn.com/ksc2/WsLapasbDJwa_d5-gSoI2EwR1RYcYI6MpzWrlOzqoBPJ1eG7TRpv8UtWiNxv2xy-tsiAXr2VvmiqAJQmxNCMawMQCe7orKomsXk6v-GJKt55XiiE9GdcOTmXM0Uj_MN1np_i8ffWmDHyxrrCfhiIKRMXGETtR5BcJTIxz5hg3BgWZAEVV8VxRcZ2PwP4phUM.mp4?pkey=AAWWdaRz9xwLglSkzE1QAdM0NoasskNdA0fRCgDJSWyTPo4tra_0jYCqgP_ieXHG4ky9vMQafXhiVaetL-iijtgENHHeQG2YMY8NxTVz_PjB8T1hTNmOXW8mQTnf2NHOa0k&tag=1-1756664181-unknown-1-0vq1m73bcl-d99c4fa7dba7dbf0&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=hd15&ss=vpm\"                                         ],                                         \"maxBitrate\": 3000,                                         \"avgBitrate\": 1622,                                         \"width\": 1280,                                         \"height\": 720,                                         \"frameRate\": 60.0,                                         \"quality\": 1.5,                                         \"kvqScore\": {                                             \"FR\": -1.0,                                             \"NR\": 3.4632160663604736,                                             \"FRPost\": -1.0,                                             \"NRPost\": -1.0,                                             \"sharpness\": 0.4285,                                             \"blur\": 0.2377                                         },                                         \"qualityType\": \"720p\",                                         \"qualityLabel\": \"高清\",                                         \"featureP2sp\": false,                                         \"p2spCode\": \"{\"fRsn\":0,\"fixOpt\":-1,\"schTask\":\"\",\"schCode\":-1,\"schRes\":\"\",\"pushTask\":\"v=0&p=0&s=0&d=0\",\"pushCode\":-1}\",                                         \"hidden\": false,                                         \"disableAdaptive\": false,                                         \"defaultSelect\": false,                                         \"comment\": \"videoId=b1a31deb8e75e7be/ttExplain=HEVC_Turbo2_720P_高码率/tt=hd15\",                                         \"hdrType\": 0,                                         \"fileSize\": 17227811,                                         \"agc\": false,                                         \"mute\": false,                                         \"oriLoudness\": 0.0,                                         \"makeupGain\": 0.0,                                         \"realLoudness\": -9.532,                                         \"realNormalizeGain\": 1.0,                                         \"normalizeGain\": 0.0                                     }                                 ]                             }                         ],                         \"playInfo\": {                             \"bizType\": 0,                             \"cdnTimeRangeLevel\": 0                         },                         \"videoFeature\": {                             \"blurProbability\": 0.02436523512005806,                             \"blockyProbability\": 0.5486664772033691,                             \"avgEntropy\": 11.74826078414917,                             \"mosScore\": 0.6893717646598816                         }                     },                     \"photoUrls\": [                         {                             \"cdn\": \"k0u2ayecy7bycz.djvod.ndcimgs.com\",                             \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_b_Baea19a439f265123a9b5c73a99b387c9.mp4?tag=1-1756664181-unknown-0-ngtc9b5fkw-400249aac756fa3c&provider=self&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=b&ss=vps\"                         },                         {                             \"cdn\": \"v2.kwaicdn.com\",                             \"url\": \"https://v2.kwaicdn.com/ksc2/PtGMNZW1atApoKjZtdZAeYBv_Hk3rukAMsduvp-BRuBp66aB3ZFXpDnlTON3Xy5ehrz5fc5c4ys3g0Nays7EXtftXSi7JkRjPKFMN-vbPXVZ68800hSKYaFZejJUW1GKp2ttjc9vIgAKHkCkn1E8e709mnQxJz6nzJRRixcAEvJ6PxVraa3OqiGkiA12zLt0.mp4?pkey=AAVID_YMrWOJ06oySpzkfx8i-z7z8Iyx34JyeXW13PQLMfVfPDvy1b0cEQh_2ri0Bs7F_GvTuADCNUK0SR0f0zes8DixR10HM6lJQkpQ64nHhqlVoxHkP9DQGPvgr1nZ-l4&tag=1-1756664181-unknown-1-cpfxvlhxnd-8304a252b8387036&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=b&ss=vps\"                         }                     ],                     \"manifest\": {                         \"version\": \"1.0.0\",                         \"businessType\": 2,                         \"mediaType\": 2,                         \"videoId\": \"b1a31deb8e75e7be\",                         \"hideAuto\": false,                         \"manualDefaultSelect\": false,                         \"stereoType\": 0,                         \"adaptationSet\": [                             {                                 \"id\": 1,                                 \"duration\": 84937,                                 \"representation\": [                                     {                                         \"id\": 1,                                         \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_b_Baea19a439f265123a9b5c73a99b387c9.mp4?tag=1-1756664181-unknown-0-raca8mq3p7-df6cf126f2ba1979&provider=self&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=b&ss=vpm\",                                         \"backupUrl\": [                                             \"https://v2.kwaicdn.com/ksc2/PtGMNZW1atApoKjZtdZAeYBv_Hk3rukAMsduvp-BRuBp66aB3ZFXpDnlTON3Xy5ehrz5fc5c4ys3g0Nays7EXtftXSi7JkRjPKFMN-vbPXVZ68800hSKYaFZejJUW1GKp2ttjc9vIgAKHkCkn1E8e709mnQxJz6nzJRRixcAEvJ6PxVraa3OqiGkiA12zLt0.mp4?pkey=AAUkTComC4sD_jFDy6Q8DZvnU7bttEcUKZYUyPGThMFjvLORo0aHnSv2Y7qhYldRnSBe9H1NRLi9yC1zprgWULvlD6mm7Q8pWup3vG3BabToQqpNmpHI2hwzk6m0UE-8j38&tag=1-1756664181-unknown-1-frwqzvnubq-3aeb9dc39d8958ed&clientCacheKey=3xezqrk27gdc5a4_b.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=b&ss=vpm\"                                         ],                                         \"maxBitrate\": 4900,                                         \"avgBitrate\": 3482,                                         \"width\": 1280,                                         \"height\": 720,                                         \"frameRate\": 60.0,                                         \"quality\": 1.5,                                         \"kvqScore\": {                                             \"FR\": -1.0,                                             \"NR\": 3.5491535663604736,                                             \"FRPost\": -1.0,                                             \"NRPost\": -1.0,                                             \"sharpness\": 0.3316,                                             \"blur\": 0.2374                                         },                                         \"qualityType\": \"720p\",                                         \"qualityLabel\": \"高清\",                                         \"featureP2sp\": false,                                         \"p2spCode\": \"{\"fRsn\":0,\"fixOpt\":-1,\"schTask\":\"\",\"schCode\":-1,\"schRes\":\"\",\"pushTask\":\"v=0&p=0&s=0&d=0\",\"pushCode\":-1}\",                                         \"hidden\": false,                                         \"disableAdaptive\": false,                                         \"defaultSelect\": false,                                         \"comment\": \"videoId=b1a31deb8e75e7be/ttExplain=AVC_VeryFast_720P_高码率_Basic/tt=b\",                                         \"hdrType\": 0,                                         \"fileSize\": 36976273,                                         \"bitratePattern\": [                                             5000,                                             3471,                                             6733,                                             481,                                             1569                                         ],                                         \"agc\": false,                                         \"mute\": false,                                         \"oriLoudness\": 0.0,                                         \"makeupGain\": 0.0,                                         \"realLoudness\": -9.532,                                         \"realNormalizeGain\": 1.0,                                         \"normalizeGain\": 0.0                                     }                                 ]                             }                         ],                         \"playInfo\": {                             \"bizType\": 0,                             \"cdnTimeRangeLevel\": 0                         },                         \"videoFeature\": {                             \"blurProbability\": 0.02436523512005806,                             \"blockyProbability\": 0.5486664772033691,                             \"avgEntropy\": 11.74826078414917,                             \"mosScore\": 0.6893717646598816                         }                     },                     \"photoH265Urls\": [                         {                             \"cdn\": \"k0u2ayecy7bycz.djvod.ndcimgs.com\",                             \"url\": \"https://k0u2ayecy7bycz.djvod.ndcimgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_hd15_Bfb2327ef432b8e22bee0565c052210d0.mp4?tag=1-1756664181-unknown-0-ra3mc5pqwz-b5d377ade7d0a512&provider=self&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&x-ks-ptid=116174197553&kwai-not-alloc=self-cdn&kcdntag=p:Henan;i:ChinaUnicom;ft:UNKNOWN;h:COLD;pn:kuaishouVideoProjection&ocid=300000173&tt=hd15&ss=vps\"                         },                         {                             \"cdn\": \"v1.kwaicdn.com\",                             \"url\": \"https://v1.kwaicdn.com/ksc2/WsLapasbDJwa_d5-gSoI2EwR1RYcYI6MpzWrlOzqoBPJ1eG7TRpv8UtWiNxv2xy-tsiAXr2VvmiqAJQmxNCMawMQCe7orKomsXk6v-GJKt55XiiE9GdcOTmXM0Uj_MN1np_i8ffWmDHyxrrCfhiIKRMXGETtR5BcJTIxz5hg3BgWZAEVV8VxRcZ2PwP4phUM.mp4?pkey=AAVktrin9oeeededNfrZf8LaIR1CvEQJ8FlSEH5iw-Azi03uiv1Eh297Xfd7f6yLLkZNDEyqFg4KqNphKlDhQmAw3TKsBqJYmLfLtR3cRWzJ5VY6FadrIRrGZvuCwgCob4A&tag=1-1756664181-unknown-1-tx8vx8qkhx-44a6a7306fccf2ff&clientCacheKey=3xezqrk27gdc5a4_hd15.mp4&di=3da39dcf&bp=14734&kwai-not-alloc=0&tt=hd15&ss=vps\"                         }                     ],                     \"viewCount\": 1594389,                     \"width\": 1280,                     \"id\": \"3xezqrk27gdc5a4\",                     \"animatedCoverUrl\": \"https://p1.a.yximgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_animatedV5_Beaaaeb032c640d38decbda1f52bc209e.webp?tag=1-1756664181-xpcwebprofile-0-tdiakvxcxz-98dff964a1098863&clientCacheKey=3xezqrk27gdc5a4_animatedV5.webp&di=3da39dcf&bp=14734\",                     \"overrideCoverUrl\": \"https://p1.a.yximgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_ccc_B39cbb17aaf65e0a76080064fd78dfc64.jpg?tag=1-1756664181-xpcwebprofile-0-gg941gqowe-afd116662be96449&clientCacheKey=3xezqrk27gdc5a4_ccc.jpg&di=3da39dcf&bp=14734\",                     \"collectCount\": 22057,                     \"riskTagContent\": null,                     \"expTag\": \"1_a/2008712974016392641_xpcwebprofilexxnull0\",                     \"riskTagUrl\": null,                     \"timestamp\": 1698748219278,                     \"stereoType\": 0,                     \"likeCount\": 75604,                     \"collected\": false,                     \"duration\": 84816,                     \"liked\": false,                     \"coverUrl\": \"https://p1.a.yximgs.com/upic/2023/10/31/18/BMjAyMzEwMzExODI5MTJfMjI4OTA1ODAyXzExNjE3NDE5NzU1M18yXzM=_ccc_B39cbb17aaf65e0a76080064fd78dfc64.jpg?tag=1-1756664181-xpcwebprofile-0-lznq3kgead-b3f7c6ea108bb5d1&clientCacheKey=3xezqrk27gdc5a4_ccc.jpg&di=3da39dcf&bp=14734\",                     \"caption\": \"健 身 鸭 脖\",                     \"height\": 720                 },                 \"author\": {                     \"id\": \"3xz63mn6fngqtiq\",                     \"headerUrl\": \"https://p66-pro.a.yximgs.com/uhead/AB/2025/08/11/21/BMjAyNTA4MTEyMTEyNDlfMjI4OTA1ODAyXzFfaGQ5ODdfODg4_s.jpg\",                     \"livingInfo\": {                         \"living\": false,                         \"livingId\": null,                         \"iconType\": 0                     },                     \"name\": \"权少爱吃小汉堡🍔\",                     \"following\": false                 },                 \"comment\": {                     \"us_c\": 0                 },                 \"danmakuSwitch\": true             }             },         ],         \"llsid\": \"2008712974016392641\",         \"host-name\": \"public-bjx-c26-kce-node642.idchb1az1.hb1.kwaidc.com\",         \"webPageArea\": \"profilexxnull\"     } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get_with_http_info(user_id, async_req=True)
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
                    " to method fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get`")  # noqa: E501

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
            '/api/v1/kuaishou/web/fetch_user_post', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get(self, photo_id, **kwargs):  # noqa: E501
        """生成分享短连接/Generate share short URL  # noqa: E501

        # [中文] ### 用途: - 生成分享短连接 ### 参数: - photo_id: 作品ID ### 返回: - 短连接  # [English] ### Purpose: - Generate share short URL ### Parameters: - photo_id: Photo ID ### Returns: - Short URL  # [示例/Example] body = {     \"photo_id\": \"3xtdqvdnqd3psuc\" }  # [返回示例/Example Response] ```json {   \"code\": 200,   \"request_id\": \"3fe5f6dc-e88c-4915-a6fa-2a63a2743342\",   \"router\": \"/api/v1/kuaishou/web/generate_share_short_url\",   \"params\": {     \"photo_id\": \"3xtdqvdnqd3psuc\"   },   \"data\": {     \"result\": 1,     \"hostName\": \"public-bjzey-rs6-kce-node1155.idchb1az3.hb1.kwaidc.com\",     \"cache-scope\": \"nocache\",     \"error_msg\": null,     \"max-age\": 0,     \"share\": {       \"shareMethod\": \"TOKEN\",       \"shareMethodType\": null,       \"shareChannel\": \"COPY_LINK\",       \"shareMode\": \"APP\",       \"kpn\": \"KUAISHOU\",       \"subBiz\": \"BROWSE_SLIDE_PHOTO\",       \"appName\": \"as\",       \"appIconUrl\": \"https://static.yximgs.com/udata/pkg/ks-share-sdk/cardlogonew.png\",       \"shareObject\": {         \"copylinkSuccessTips\": \"链接复制成功，快去分享给朋友吧\",         \"shareMessage\": \"https://v.kuaishou.com/KDh1s1j1 上一秒他是市民，下一秒他是市长 大哥突如其来的专业，让人笑不活了。\"搞笑 \"非物质文化遗产 \"...更多\",         \"kwaiToken\": \"X8hIM7myjQen2bi\",         \"shareId\": \"18546252276277\",         \"shareObjectId\": \"3xtdqvdnqd3psuc\",         \"shareResourceType\": \"PHOTO_OTHER\",         \"shortLink\": \"https://v.kuaishou.com/KDh1s1j1\"       },       \"extParams\": {         \"shareMode\": \"app\",         \"tokenExtParams\": \"{}\",         \"expTag\": \"1_i/0_unknown0\",         \"shareMethod\": \"token\",         \"useMmuTitle\": false,         \"logExt\": \"{\"expTag\":\"1_i/0_unknown0\",\"trendingType\":\"\"}\",         \"templateStyle\": \"\",         \"shareInfoWrap\": \"{\"shareTitleInfo\":{\"title\":\"分享一个作品给你\",\"subTitle\":\"推荐你看这个视频\"},\"shareId\":\"18546252276277\",\"docId\":9,\"groupName\":\"\",\"shareType\":\"PHOTO_OTHER\",\"coverUrlKey\":null,\"coverUrl\":null,\"tagType\":null,\"webShareVerifyData\":null}\",         \"battleTemplateId\": \"\",         \"templateGenerationType\": \"\"       }     },     \"host-name\": \"public-bjzey-rs6-kce-node1155.idchb1az3.hb1.kwaidc.com\"   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get(photo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object photo_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get_with_http_info(photo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get_with_http_info(photo_id, **kwargs)  # noqa: E501
            return data

    def generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get_with_http_info(self, photo_id, **kwargs):  # noqa: E501
        """生成分享短连接/Generate share short URL  # noqa: E501

        # [中文] ### 用途: - 生成分享短连接 ### 参数: - photo_id: 作品ID ### 返回: - 短连接  # [English] ### Purpose: - Generate share short URL ### Parameters: - photo_id: Photo ID ### Returns: - Short URL  # [示例/Example] body = {     \"photo_id\": \"3xtdqvdnqd3psuc\" }  # [返回示例/Example Response] ```json {   \"code\": 200,   \"request_id\": \"3fe5f6dc-e88c-4915-a6fa-2a63a2743342\",   \"router\": \"/api/v1/kuaishou/web/generate_share_short_url\",   \"params\": {     \"photo_id\": \"3xtdqvdnqd3psuc\"   },   \"data\": {     \"result\": 1,     \"hostName\": \"public-bjzey-rs6-kce-node1155.idchb1az3.hb1.kwaidc.com\",     \"cache-scope\": \"nocache\",     \"error_msg\": null,     \"max-age\": 0,     \"share\": {       \"shareMethod\": \"TOKEN\",       \"shareMethodType\": null,       \"shareChannel\": \"COPY_LINK\",       \"shareMode\": \"APP\",       \"kpn\": \"KUAISHOU\",       \"subBiz\": \"BROWSE_SLIDE_PHOTO\",       \"appName\": \"as\",       \"appIconUrl\": \"https://static.yximgs.com/udata/pkg/ks-share-sdk/cardlogonew.png\",       \"shareObject\": {         \"copylinkSuccessTips\": \"链接复制成功，快去分享给朋友吧\",         \"shareMessage\": \"https://v.kuaishou.com/KDh1s1j1 上一秒他是市民，下一秒他是市长 大哥突如其来的专业，让人笑不活了。\"搞笑 \"非物质文化遗产 \"...更多\",         \"kwaiToken\": \"X8hIM7myjQen2bi\",         \"shareId\": \"18546252276277\",         \"shareObjectId\": \"3xtdqvdnqd3psuc\",         \"shareResourceType\": \"PHOTO_OTHER\",         \"shortLink\": \"https://v.kuaishou.com/KDh1s1j1\"       },       \"extParams\": {         \"shareMode\": \"app\",         \"tokenExtParams\": \"{}\",         \"expTag\": \"1_i/0_unknown0\",         \"shareMethod\": \"token\",         \"useMmuTitle\": false,         \"logExt\": \"{\"expTag\":\"1_i/0_unknown0\",\"trendingType\":\"\"}\",         \"templateStyle\": \"\",         \"shareInfoWrap\": \"{\"shareTitleInfo\":{\"title\":\"分享一个作品给你\",\"subTitle\":\"推荐你看这个视频\"},\"shareId\":\"18546252276277\",\"docId\":9,\"groupName\":\"\",\"shareType\":\"PHOTO_OTHER\",\"coverUrlKey\":null,\"coverUrl\":null,\"tagType\":null,\"webShareVerifyData\":null}\",         \"battleTemplateId\": \"\",         \"templateGenerationType\": \"\"       }     },     \"host-name\": \"public-bjzey-rs6-kce-node1155.idchb1az3.hb1.kwaidc.com\"   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get_with_http_info(photo_id, async_req=True)
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
                    " to method generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'photo_id' is set
        if self.api_client.client_side_validation and ('photo_id' not in params or
                                                       params['photo_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `photo_id` when calling `generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get`")  # noqa: E501

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
            '/api/v1/kuaishou/web/generate_share_short_url', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
