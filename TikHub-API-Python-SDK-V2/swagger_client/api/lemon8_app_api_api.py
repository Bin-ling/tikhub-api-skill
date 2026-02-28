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


class Lemon8AppAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get(self, **kwargs):  # noqa: E501
        """获取发现页Banner/Get banners of discover page  # noqa: E501

        # [中文] ### 用途: - 获取发现页Banner（搜索页上方的滚动内容） ### 返回: - Banner列表  # [English] ### Purpose: - Get banners of discover page ### Return: - Banners list  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取发现页Banner/Get banners of discover page  # noqa: E501

        # [中文] ### 用途: - 获取发现页Banner（搜索页上方的滚动内容） ### 返回: - Banner列表  # [English] ### Purpose: - Get banners of discover page ### Return: - Banners list  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get_with_http_info(async_req=True)
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
                    " to method fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get" % key
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
            '/api/v1/lemon8/app/fetch_discover_banners', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get(self, **kwargs):  # noqa: E501
        """获取发现页主体内容/Get main content of discover page  # noqa: E501

        # [中文] ### 用途: - 获取发现页（搜索页主体内容） ### 返回: - 主体内容  # [English] ### Purpose: - Get main content of discover page ### Return: - Main content  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取发现页主体内容/Get main content of discover page  # noqa: E501

        # [中文] ### 用途: - 获取发现页（搜索页主体内容） ### 返回: - 主体内容  # [English] ### Purpose: - Get main content of discover page ### Return: - Main content  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get_with_http_info(async_req=True)
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
                    " to method fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get" % key
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
            '/api/v1/lemon8/app/fetch_discover_tab', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get(self, **kwargs):  # noqa: E501
        """获取发现页的 Editor's Picks/Get Editor's Picks of discover page  # noqa: E501

        # [中文] ### 用途: - 获取发现页（搜索页下方的推荐内容 - Editor's Picks） ### 返回: - 推荐内容  # [English] ### Purpose: - Get Editor's Picks of discover page ### Return: - Editor's Picks  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取发现页的 Editor's Picks/Get Editor's Picks of discover page  # noqa: E501

        # [中文] ### 用途: - 获取发现页（搜索页下方的推荐内容 - Editor's Picks） ### 返回: - 推荐内容  # [English] ### Purpose: - Get Editor's Picks of discover page ### Return: - Editor's Picks  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get_with_http_info(async_req=True)
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
                    " to method fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get" % key
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
            '/api/v1/lemon8/app/fetch_discover_tab_information_tabs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get(self, **kwargs):  # noqa: E501
        """获取热搜关键词/Get hot search keywords  # noqa: E501

        # [中文] ### 用途: - 获取热搜关键词 ### 返回: - 热搜关键词列表  # [English] ### Purpose: - Get hot search keywords ### Return: - Hot search keywords list  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热搜关键词/Get hot search keywords  # noqa: E501

        # [中文] ### 用途: - 获取热搜关键词 ### 返回: - 热搜关键词列表  # [English] ### Purpose: - Get hot search keywords ### Return: - Hot search keywords list  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get" % key
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
            '/api/v1/lemon8/app/fetch_hot_search_keywords', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get(self, group_id, item_id, media_id, **kwargs):  # noqa: E501
        """获取指定作品的评论列表/Get comments list of specified post  # noqa: E501

        # [中文] ### 用途: - 获取指定作品的评论列表 ### 参数: - group_id: 作品的group_id，可以从接口`/lemon8/app/fetch_post_detail`获取 - item_id: 作品的item_id，可以从接口`/lemon8/app/fetch_post_detail` 或 `/lemon8/app/get_item_id`获取 - media_id: 作品的media_id，可以从接口`/lemon8/app/fetch_post_detail`获取 - offset: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的offset进行翻页。 ### 返回: - 评论列表  # [English] ### Purpose: - Get comments list of specified post ### Parameters: - group_id: Post's group_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` - item_id: Post's item_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` or `/lemon8/app/get_item_id` - media_id: Post's media_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` - offset: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the offset returned by the last request is used for subsequent requests. ### Return: - Comments list  # [示例/Example] group_id = \"7361926875709129222\" item_id = \"7361926875709129222\" media_id = \"7428056850216862763\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get(group_id, item_id, media_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object group_id: 作品的group_id/Post's group_id (required)
        :param object item_id: 作品的item_id/Post's item_id (required)
        :param object media_id: 作品的media_id/Post's media_id (required)
        :param object offset: 翻页参数/Pagination parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get_with_http_info(group_id, item_id, media_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get_with_http_info(group_id, item_id, media_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get_with_http_info(self, group_id, item_id, media_id, **kwargs):  # noqa: E501
        """获取指定作品的评论列表/Get comments list of specified post  # noqa: E501

        # [中文] ### 用途: - 获取指定作品的评论列表 ### 参数: - group_id: 作品的group_id，可以从接口`/lemon8/app/fetch_post_detail`获取 - item_id: 作品的item_id，可以从接口`/lemon8/app/fetch_post_detail` 或 `/lemon8/app/get_item_id`获取 - media_id: 作品的media_id，可以从接口`/lemon8/app/fetch_post_detail`获取 - offset: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的offset进行翻页。 ### 返回: - 评论列表  # [English] ### Purpose: - Get comments list of specified post ### Parameters: - group_id: Post's group_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` - item_id: Post's item_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` or `/lemon8/app/get_item_id` - media_id: Post's media_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` - offset: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the offset returned by the last request is used for subsequent requests. ### Return: - Comments list  # [示例/Example] group_id = \"7361926875709129222\" item_id = \"7361926875709129222\" media_id = \"7428056850216862763\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get_with_http_info(group_id, item_id, media_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object group_id: 作品的group_id/Post's group_id (required)
        :param object item_id: 作品的item_id/Post's item_id (required)
        :param object media_id: 作品的media_id/Post's media_id (required)
        :param object offset: 翻页参数/Pagination parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'item_id', 'media_id', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in params or
                                                       params['group_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `group_id` when calling `fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get`")  # noqa: E501
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get`")  # noqa: E501
        # verify the required parameter 'media_id' is set
        if self.api_client.client_side_validation and ('media_id' not in params or
                                                       params['media_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `media_id` when calling `fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))  # noqa: E501
        if 'media_id' in params:
            query_params.append(('media_id', params['media_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/lemon8/app/fetch_post_comment_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get(self, item_id, **kwargs):  # noqa: E501
        """获取指定作品的信息/Get information of specified post  # noqa: E501

        # [中文] ### 用途: - 获取指定作品的信息 ### 参数: - item_id: 作品ID，可以从接口`/lemon8/app/get_item_id`获取 ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - item_id: Post ID, can be obtained from the interface `/lemon8/app/get_item_id` ### Return: - Post information  # [示例/Example] item_id = \"7361926875709129222\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品ID/Post ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get_with_http_info(item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get_with_http_info(item_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get_with_http_info(self, item_id, **kwargs):  # noqa: E501
        """获取指定作品的信息/Get information of specified post  # noqa: E501

        # [中文] ### 用途: - 获取指定作品的信息 ### 参数: - item_id: 作品ID，可以从接口`/lemon8/app/get_item_id`获取 ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - item_id: Post ID, can be obtained from the interface `/lemon8/app/get_item_id` ### Return: - Post information  # [示例/Example] item_id = \"7361926875709129222\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get_with_http_info(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品ID/Post ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/lemon8/app/fetch_post_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_search_api_v1_lemon8_app_fetch_search_get(self, query, **kwargs):  # noqa: E501
        """搜索接口/Search API  # noqa: E501

        # [中文] ### 用途: - 搜索接口 ### 参数: - query: 搜索关键词 - max_cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的`max_cursor`进行翻页，可以通过返回结果的`has_more`字段判断是否还有更多数据。 - filter_type: 搜索过滤类型，默认为空字符串，可选值如下：     - 空字符串：All（全部，默认使用此参数搜索）     - video：只搜索视频作品     - posts：只搜索文章作品 - order_by: 搜索排序方式，默认为空字符串，可选值如下：     - 空字符串：Relevance（相关度，默认使用此参数排序）     - popular：流行度排序     - recent：从新到旧排序 - search_tab: 搜索类型，默认为`main`，可选值如下：     - main：APP中显示为 `Top`（综合搜索，默认使用此参数搜索）     - user：APP中显示为 `Accounts` （搜索用户账号）     - hashtag：APP中显示为 `Hashtags`（搜索话题）     - article：APP中显示为 `Posts`（搜索文章） ### 返回: - 搜索结果  # [English] ### Purpose: - Search API ### Parameters: - query: Search keyword - max_cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the `max_cursor` returned by the last request is used for subsequent requests. You can judge whether there is more data by the `has_more` field in the return result. - filter_type: Search filter type, default is an empty string, optional values are as follows:     - Empty string: All (default using this parameter to search)     - video: Search only video     - posts: Search only posts - order_by: Search sort type, default is an empty string, optional values are as follows:     - Empty string: Relevance (default using this parameter to sort)     - popular: Sort by popularity     - recent: Sort from new to old - search_tab: Search type, default is `main`, optional values are as follows:     - main: Display as `Top` in the APP (comprehensive search, default using this parameter to search)     - user: Display as `Accounts` in the APP (search user accounts)     - hashtag: Display as `Hashtags` in the APP (search hashtags)     - article: Display as `Posts` in the APP (search articles) ### Return: - Search results  # [示例/Example] query = \"lemon8\" max_cursor = \"\" filter_type = \"\" order_by = \"\" search_tab = \"main\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_api_v1_lemon8_app_fetch_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object max_cursor: 翻页参数/Pagination parameter
        :param object filter_type: 搜索过滤类型/Search filter type
        :param object order_by: 搜索排序方式/Search sort type
        :param object search_tab: 搜索类型/Search type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_api_v1_lemon8_app_fetch_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_api_v1_lemon8_app_fetch_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_search_api_v1_lemon8_app_fetch_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """搜索接口/Search API  # noqa: E501

        # [中文] ### 用途: - 搜索接口 ### 参数: - query: 搜索关键词 - max_cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的`max_cursor`进行翻页，可以通过返回结果的`has_more`字段判断是否还有更多数据。 - filter_type: 搜索过滤类型，默认为空字符串，可选值如下：     - 空字符串：All（全部，默认使用此参数搜索）     - video：只搜索视频作品     - posts：只搜索文章作品 - order_by: 搜索排序方式，默认为空字符串，可选值如下：     - 空字符串：Relevance（相关度，默认使用此参数排序）     - popular：流行度排序     - recent：从新到旧排序 - search_tab: 搜索类型，默认为`main`，可选值如下：     - main：APP中显示为 `Top`（综合搜索，默认使用此参数搜索）     - user：APP中显示为 `Accounts` （搜索用户账号）     - hashtag：APP中显示为 `Hashtags`（搜索话题）     - article：APP中显示为 `Posts`（搜索文章） ### 返回: - 搜索结果  # [English] ### Purpose: - Search API ### Parameters: - query: Search keyword - max_cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the `max_cursor` returned by the last request is used for subsequent requests. You can judge whether there is more data by the `has_more` field in the return result. - filter_type: Search filter type, default is an empty string, optional values are as follows:     - Empty string: All (default using this parameter to search)     - video: Search only video     - posts: Search only posts - order_by: Search sort type, default is an empty string, optional values are as follows:     - Empty string: Relevance (default using this parameter to sort)     - popular: Sort by popularity     - recent: Sort from new to old - search_tab: Search type, default is `main`, optional values are as follows:     - main: Display as `Top` in the APP (comprehensive search, default using this parameter to search)     - user: Display as `Accounts` in the APP (search user accounts)     - hashtag: Display as `Hashtags` in the APP (search hashtags)     - article: Display as `Posts` in the APP (search articles) ### Return: - Search results  # [示例/Example] query = \"lemon8\" max_cursor = \"\" filter_type = \"\" order_by = \"\" search_tab = \"main\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_api_v1_lemon8_app_fetch_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object max_cursor: 翻页参数/Pagination parameter
        :param object filter_type: 搜索过滤类型/Search filter type
        :param object order_by: 搜索排序方式/Search sort type
        :param object search_tab: 搜索类型/Search type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'max_cursor', 'filter_type', 'order_by', 'search_tab']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_api_v1_lemon8_app_fetch_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_search_api_v1_lemon8_app_fetch_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'max_cursor' in params:
            query_params.append(('max_cursor', params['max_cursor']))  # noqa: E501
        if 'filter_type' in params:
            query_params.append(('filter_type', params['filter_type']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'search_tab' in params:
            query_params.append(('search_tab', params['search_tab']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/lemon8/app/fetch_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get(self, forum_id, **kwargs):  # noqa: E501
        """获取话题信息/Get topic information  # noqa: E501

        # [中文] ### 用途: - 获取话题信息 ### 参数: - forum_id: 话题ID，可以从下面的接口获取     - 获取指定作品的信息：`/lemon8/app/fetch_post_detail`     - 获取发现页的 Editor's Picks：`/lemon8/app/fetch_discover_tab_information_tabs`     - 通过接口搜索 Hashtag：`/lemon8/app/fetch_search?search_tab=hashtag&keyword=lemon8` ### 返回: - 话题信息  # [English] ### Purpose: - Get topic information ### Parameters: - forum_id: Topic ID, can be obtained from the following interfaces     - Get information of specified post: `/lemon8/app/fetch_post_detail`     - Get Editor's Picks of discover page: `/lemon8/app/fetch_discover_tab_information_tabs`     - Search Hashtag through interface: `/lemon8/app/fetch_search?search_tab=hashtag&keyword=lemon8` ### Return: - Topic information  # [示例/Example] forum_id = \"7174447913778593798\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get(forum_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object forum_id: 话题ID/Topic ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get_with_http_info(forum_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get_with_http_info(forum_id, **kwargs)  # noqa: E501
            return data

    def fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get_with_http_info(self, forum_id, **kwargs):  # noqa: E501
        """获取话题信息/Get topic information  # noqa: E501

        # [中文] ### 用途: - 获取话题信息 ### 参数: - forum_id: 话题ID，可以从下面的接口获取     - 获取指定作品的信息：`/lemon8/app/fetch_post_detail`     - 获取发现页的 Editor's Picks：`/lemon8/app/fetch_discover_tab_information_tabs`     - 通过接口搜索 Hashtag：`/lemon8/app/fetch_search?search_tab=hashtag&keyword=lemon8` ### 返回: - 话题信息  # [English] ### Purpose: - Get topic information ### Parameters: - forum_id: Topic ID, can be obtained from the following interfaces     - Get information of specified post: `/lemon8/app/fetch_post_detail`     - Get Editor's Picks of discover page: `/lemon8/app/fetch_discover_tab_information_tabs`     - Search Hashtag through interface: `/lemon8/app/fetch_search?search_tab=hashtag&keyword=lemon8` ### Return: - Topic information  # [示例/Example] forum_id = \"7174447913778593798\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get_with_http_info(forum_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object forum_id: 话题ID/Topic ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['forum_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'forum_id' is set
        if self.api_client.client_side_validation and ('forum_id' not in params or
                                                       params['forum_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `forum_id` when calling `fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'forum_id' in params:
            query_params.append(('forum_id', params['forum_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/lemon8/app/fetch_topic_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get(self, category, category_parameter, hashtag_name, **kwargs):  # noqa: E501
        """获取话题作品列表/Get topic post list  # noqa: E501

        # [中文] ### 用途: - 获取话题作品列表 ### 参数: - category: 话题分类 ID，可以从接口`/lemon8/app/fetch_topic_info`获取 - max_behot_time: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的max_behot_time进行翻页。 - category_parameter: 分类参数ID，可以从接口`/lemon8/app/fetch_topic_info`获取 - hashtag_name: Hashtag名称，可以从接口`/lemon8/app/fetch_topic_info`获取 - sort_type: 排序方式，0为默认排序，当前只支持使用默认排序，请不要传入其他值。 ### 返回: - 作品列表  # [English] ### Purpose: - Get topic post list ### Parameters: - category: Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info` - max_behot_time: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the max_behot_time returned by the last request is used for subsequent requests. - category_parameter: Category parameter ID, can be obtained from the interface `/lemon8/app/fetch_topic_info` - hashtag_name: Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info` - sort_type: Sort type, 0 for default sort, currently only support default sort, please do not pass other values. ### Return: - Post list  # [示例/Example] category = \"590\" max_behot_time = \"\" category_parameter = \"7174447913778593798\" hashtag_name = \"lemon8christmas\" sort_type = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get(category, category_parameter, hashtag_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category: 话题分类 ID/Topic category ID (required)
        :param object category_parameter: 分类参数/Category parameter (required)
        :param object hashtag_name: Hashtag名称/Hashtag name (required)
        :param object max_behot_time: 翻页参数/Pagination parameter
        :param object sort_type: 排序方式/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get_with_http_info(category, category_parameter, hashtag_name, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get_with_http_info(category, category_parameter, hashtag_name, **kwargs)  # noqa: E501
            return data

    def fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get_with_http_info(self, category, category_parameter, hashtag_name, **kwargs):  # noqa: E501
        """获取话题作品列表/Get topic post list  # noqa: E501

        # [中文] ### 用途: - 获取话题作品列表 ### 参数: - category: 话题分类 ID，可以从接口`/lemon8/app/fetch_topic_info`获取 - max_behot_time: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的max_behot_time进行翻页。 - category_parameter: 分类参数ID，可以从接口`/lemon8/app/fetch_topic_info`获取 - hashtag_name: Hashtag名称，可以从接口`/lemon8/app/fetch_topic_info`获取 - sort_type: 排序方式，0为默认排序，当前只支持使用默认排序，请不要传入其他值。 ### 返回: - 作品列表  # [English] ### Purpose: - Get topic post list ### Parameters: - category: Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info` - max_behot_time: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the max_behot_time returned by the last request is used for subsequent requests. - category_parameter: Category parameter ID, can be obtained from the interface `/lemon8/app/fetch_topic_info` - hashtag_name: Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info` - sort_type: Sort type, 0 for default sort, currently only support default sort, please do not pass other values. ### Return: - Post list  # [示例/Example] category = \"590\" max_behot_time = \"\" category_parameter = \"7174447913778593798\" hashtag_name = \"lemon8christmas\" sort_type = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get_with_http_info(category, category_parameter, hashtag_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category: 话题分类 ID/Topic category ID (required)
        :param object category_parameter: 分类参数/Category parameter (required)
        :param object hashtag_name: Hashtag名称/Hashtag name (required)
        :param object max_behot_time: 翻页参数/Pagination parameter
        :param object sort_type: 排序方式/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category', 'category_parameter', 'hashtag_name', 'max_behot_time', 'sort_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category' is set
        if self.api_client.client_side_validation and ('category' not in params or
                                                       params['category'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `category` when calling `fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get`")  # noqa: E501
        # verify the required parameter 'category_parameter' is set
        if self.api_client.client_side_validation and ('category_parameter' not in params or
                                                       params['category_parameter'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `category_parameter` when calling `fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get`")  # noqa: E501
        # verify the required parameter 'hashtag_name' is set
        if self.api_client.client_side_validation and ('hashtag_name' not in params or
                                                       params['hashtag_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hashtag_name` when calling `fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category' in params:
            query_params.append(('category', params['category']))  # noqa: E501
        if 'max_behot_time' in params:
            query_params.append(('max_behot_time', params['max_behot_time']))  # noqa: E501
        if 'category_parameter' in params:
            query_params.append(('category_parameter', params['category_parameter']))  # noqa: E501
        if 'hashtag_name' in params:
            query_params.append(('hashtag_name', params['hashtag_name']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/lemon8/app/fetch_topic_post_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get(self, user_id, **kwargs):  # noqa: E501
        """获取指定用户的粉丝列表/Get fans list of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的粉丝列表 ### 参数: - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取 - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。 ### 返回: - 粉丝列表  # [English] ### Purpose: - Get fans list of specified user ### Parameters: - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id` - cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests. ### Return: - Fans list  # [示例/Example] user_id = \"7428056850216862763\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数/Pagination parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取指定用户的粉丝列表/Get fans list of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的粉丝列表 ### 参数: - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取 - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。 ### 返回: - 粉丝列表  # [English] ### Purpose: - Get fans list of specified user ### Parameters: - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id` - cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests. ### Return: - Fans list  # [示例/Example] user_id = \"7428056850216862763\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数/Pagination parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/lemon8/app/fetch_user_follower_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get(self, user_id, **kwargs):  # noqa: E501
        """获取指定用户的关注列表/Get following list of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的关注列表 ### 参数: - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取 - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。 ### 返回: - 关注列表  # [English] ### Purpose: - Get following list of specified user ### Parameters: - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id` - cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests. ### Return: - Following list  # [示例/Example] user_id = \"7428056850216862763\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数/Pagination parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取指定用户的关注列表/Get following list of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的关注列表 ### 参数: - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取 - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。 ### 返回: - 关注列表  # [English] ### Purpose: - Get following list of specified user ### Parameters: - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id` - cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests. ### Return: - Following list  # [示例/Example] user_id = \"7428056850216862763\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数/Pagination parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/lemon8/app/fetch_user_following_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_item_id_api_v1_lemon8_app_get_item_id_get(self, share_text, **kwargs):  # noqa: E501
        """通过分享链接获取作品ID/Get post ID through sharing link  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取作品ID ### 参数: - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 作品ID  # [English] ### Purpose: - Get post ID through sharing link ### Parameters: - share_text: Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - Post ID  # [示例/Example] share_text = \"https://www.lemon8-app.com/@deathlabs_/7445613324903006766\" share_text = \"https://v.lemon8-app.com/al/OghwFTppx\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_id_api_v1_lemon8_app_get_item_id_get(share_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_item_id_api_v1_lemon8_app_get_item_id_get_with_http_info(share_text, **kwargs)  # noqa: E501
        else:
            (data) = self.get_item_id_api_v1_lemon8_app_get_item_id_get_with_http_info(share_text, **kwargs)  # noqa: E501
            return data

    def get_item_id_api_v1_lemon8_app_get_item_id_get_with_http_info(self, share_text, **kwargs):  # noqa: E501
        """通过分享链接获取作品ID/Get post ID through sharing link  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取作品ID ### 参数: - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 作品ID  # [English] ### Purpose: - Get post ID through sharing link ### Parameters: - share_text: Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - Post ID  # [示例/Example] share_text = \"https://www.lemon8-app.com/@deathlabs_/7445613324903006766\" share_text = \"https://v.lemon8-app.com/al/OghwFTppx\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_id_api_v1_lemon8_app_get_item_id_get_with_http_info(share_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: 分享链接/Share link (required)
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
                    " to method get_item_id_api_v1_lemon8_app_get_item_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_text' is set
        if self.api_client.client_side_validation and ('share_text' not in params or
                                                       params['share_text'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_text` when calling `get_item_id_api_v1_lemon8_app_get_item_id_get`")  # noqa: E501

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
            '/api/v1/lemon8/app/get_item_id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_item_ids_api_v1_lemon8_app_get_item_ids_post(self, **kwargs):  # noqa: E501
        """通过分享链接批量获取作品ID/Get post IDs in batch through sharing links  # noqa: E501

        # [中文] ### 用途: - 通过分享链接批量获取作品ID，一次最多获取10个 ### 参数: - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 作品ID列表  # [English] ### Purpose: - Get post IDs in batch through sharing links, up to 10 at a time ### Parameters: - share_texts: Share links list, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - Post IDs list  # [示例/Example] share_texts = [     \"https://www.lemon8-app.com/@deathlabs_/7445613324903006766\",     \"https://v.lemon8-app.com/al/OghwFTppx\" ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_ids_api_v1_lemon8_app_get_item_ids_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_item_ids_api_v1_lemon8_app_get_item_ids_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_item_ids_api_v1_lemon8_app_get_item_ids_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_item_ids_api_v1_lemon8_app_get_item_ids_post_with_http_info(self, **kwargs):  # noqa: E501
        """通过分享链接批量获取作品ID/Get post IDs in batch through sharing links  # noqa: E501

        # [中文] ### 用途: - 通过分享链接批量获取作品ID，一次最多获取10个 ### 参数: - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 作品ID列表  # [English] ### Purpose: - Get post IDs in batch through sharing links, up to 10 at a time ### Parameters: - share_texts: Share links list, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - Post IDs list  # [示例/Example] share_texts = [     \"https://www.lemon8-app.com/@deathlabs_/7445613324903006766\",     \"https://v.lemon8-app.com/al/OghwFTppx\" ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_ids_api_v1_lemon8_app_get_item_ids_post_with_http_info(async_req=True)
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
                    " to method get_item_ids_api_v1_lemon8_app_get_item_ids_post" % key
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
            '/api/v1/lemon8/app/get_item_ids', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_id_api_v1_lemon8_app_get_user_id_get(self, share_text, **kwargs):  # noqa: E501
        """通过分享链接获取用户ID/Get user ID through sharing link  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取用户ID ### 参数: - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 用户ID  # [English] ### Purpose: - Get user ID through sharing link ### Parameters: - share_text: Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - User ID  # [示例/Example] share_text = \"https://www.lemon8-app.com/lemon8cars?region=us\" share_text = \"https://v.lemon8-app.com/al/OgZrsUppx\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_id_api_v1_lemon8_app_get_user_id_get(share_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_id_api_v1_lemon8_app_get_user_id_get_with_http_info(share_text, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_id_api_v1_lemon8_app_get_user_id_get_with_http_info(share_text, **kwargs)  # noqa: E501
            return data

    def get_user_id_api_v1_lemon8_app_get_user_id_get_with_http_info(self, share_text, **kwargs):  # noqa: E501
        """通过分享链接获取用户ID/Get user ID through sharing link  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取用户ID ### 参数: - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 用户ID  # [English] ### Purpose: - Get user ID through sharing link ### Parameters: - share_text: Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - User ID  # [示例/Example] share_text = \"https://www.lemon8-app.com/lemon8cars?region=us\" share_text = \"https://v.lemon8-app.com/al/OgZrsUppx\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_id_api_v1_lemon8_app_get_user_id_get_with_http_info(share_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: 分享链接/Share link (required)
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
                    " to method get_user_id_api_v1_lemon8_app_get_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_text' is set
        if self.api_client.client_side_validation and ('share_text' not in params or
                                                       params['share_text'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_text` when calling `get_user_id_api_v1_lemon8_app_get_user_id_get`")  # noqa: E501

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
            '/api/v1/lemon8/app/get_user_id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_ids_api_v1_lemon8_app_get_user_ids_post(self, **kwargs):  # noqa: E501
        """通过分享链接批量获取用户ID/Get user IDs in batch through sharing links  # noqa: E501

        # [中文] ### 用途: - 通过分享链接批量获取用户ID，一次最多获取10个 ### 参数: - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 用户ID列表  # [English] ### Purpose: - Get user IDs in batch through sharing links, up to 10 at a time ### Parameters: - share_texts: Share links list, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - User IDs list  # [示例/Example] share_texts = [     \"https://www.lemon8-app.com/lemon8cars?region=us\",     \"https://v.lemon8-app.com/al/OgZrsUppx\" ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_ids_api_v1_lemon8_app_get_user_ids_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_ids_api_v1_lemon8_app_get_user_ids_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_ids_api_v1_lemon8_app_get_user_ids_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_ids_api_v1_lemon8_app_get_user_ids_post_with_http_info(self, **kwargs):  # noqa: E501
        """通过分享链接批量获取用户ID/Get user IDs in batch through sharing links  # noqa: E501

        # [中文] ### 用途: - 通过分享链接批量获取用户ID，一次最多获取10个 ### 参数: - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。 ### 返回: - 用户ID列表  # [English] ### Purpose: - Get user IDs in batch through sharing links, up to 10 at a time ### Parameters: - share_texts: Share links list, supports long links and short links, can be obtained and copied from the share button on the web and APP. ### Return: - User IDs list  # [示例/Example] share_texts = [     \"https://www.lemon8-app.com/lemon8cars?region=us\",     \"https://v.lemon8-app.com/al/OgZrsUppx\" ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_ids_api_v1_lemon8_app_get_user_ids_post_with_http_info(async_req=True)
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
                    " to method get_user_ids_api_v1_lemon8_app_get_user_ids_post" % key
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
            '/api/v1/lemon8/app/get_user_ids', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get(self, user_id, **kwargs):  # noqa: E501
        """获取指定用户的信息/Get information of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取 ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id` ### Return: - User information  # [示例/Example] user_id = \"7217844966059656197\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取指定用户的信息/Get information of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取 ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id` ### Return: - User information  # [示例/Example] user_id = \"7217844966059656197\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get_with_http_info(user_id, async_req=True)
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
                    " to method handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get`")  # noqa: E501

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
            '/api/v1/lemon8/app/fetch_user_profile', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
