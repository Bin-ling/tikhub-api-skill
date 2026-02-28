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


class LinkedInWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_company_job_count_api_v1_linkedin_web_get_company_job_count_get(self, company_id, **kwargs):  # noqa: E501
        """获取公司职位数量/Get company job count  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn公司职位数量  ### 参数: - company_id: 公司ID（必填）  ### 返回: - 公司职位数量数据  # [English] ### Purpose: - Get LinkedIn company job count  ### Parameters: - company_id: Company ID (required)  ### Returns: - Company job count data  # [示例/Example] company_id = \"783611\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_job_count_api_v1_linkedin_web_get_company_job_count_get(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object company_id: 公司ID/Company ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_job_count_api_v1_linkedin_web_get_company_job_count_get_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_job_count_api_v1_linkedin_web_get_company_job_count_get_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def get_company_job_count_api_v1_linkedin_web_get_company_job_count_get_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """获取公司职位数量/Get company job count  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn公司职位数量  ### 参数: - company_id: 公司ID（必填）  ### 返回: - 公司职位数量数据  # [English] ### Purpose: - Get LinkedIn company job count  ### Parameters: - company_id: Company ID (required)  ### Returns: - Company job count data  # [示例/Example] company_id = \"783611\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_job_count_api_v1_linkedin_web_get_company_job_count_get_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object company_id: 公司ID/Company ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_job_count_api_v1_linkedin_web_get_company_job_count_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if self.api_client.client_side_validation and ('company_id' not in params or
                                                       params['company_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `company_id` when calling `get_company_job_count_api_v1_linkedin_web_get_company_job_count_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company_id' in params:
            query_params.append(('company_id', params['company_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_company_job_count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company_jobs_api_v1_linkedin_web_get_company_jobs_get(self, company_id, **kwargs):  # noqa: E501
        """获取公司职位/Get company jobs  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn公司职位列表  ### 参数: - company_id: 公司ID（必填） - page: 页码（可选），默认为1 - sort_by: 排序方式（可选）：recent(最新), relevant(相关) - date_posted: 发布时间过滤（可选）：anytime, past_month, past_week, past_24_hours - experience_level: 经验级别（可选）：internship, entry_level, associate, mid_senior, director, executive - remote: 工作地点类型（可选）：onsite, remote, hybrid - job_type: 工作类型（可选）：full_time, part_time, contract, temporary, volunteer, internship, other - easy_apply: 是否易申请（可选） - under_10_applicants: 是否少于10个申请者（可选） - fair_chance_employer: 是否公平机会雇主（可选）  ### 返回: - 公司职位列表数据  # [English] ### Purpose: - Get LinkedIn company jobs list  ### Parameters: - company_id: Company ID (required) - page: Page number (optional), default is 1 - sort_by: Sort by (optional): recent, relevant - date_posted: Date posted filter (optional): anytime, past_month, past_week, past_24_hours - experience_level: Experience level (optional): internship, entry_level, associate, mid_senior, director, executive - remote: Remote filter (optional): onsite, remote, hybrid - job_type: Job type (optional): full_time, part_time, contract, temporary, volunteer, internship, other - easy_apply: Easy apply filter (optional) - under_10_applicants: Under 10 applicants filter (optional) - fair_chance_employer: Fair chance employer filter (optional)  ### Returns: - Company jobs list data  # [示例/Example] company_id = \"783611\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_jobs_api_v1_linkedin_web_get_company_jobs_get(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object company_id: 公司ID/Company ID (required)
        :param object page: 页码/Page number
        :param object sort_by: 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant
        :param object date_posted: 发布时间过滤：anytime, past_month, past_week, past_24_hours
        :param object experience_level: 经验级别：internship, entry_level, associate, mid_senior, director, executive
        :param object remote: 工作地点类型：onsite, remote, hybrid
        :param object job_type: 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other
        :param object easy_apply: 是否易申请/Filter easy apply jobs
        :param object under_10_applicants: 是否少于10个申请者/Filter jobs with under 10 applicants
        :param object fair_chance_employer: 是否公平机会雇主/Filter fair chance employer jobs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_jobs_api_v1_linkedin_web_get_company_jobs_get_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_jobs_api_v1_linkedin_web_get_company_jobs_get_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def get_company_jobs_api_v1_linkedin_web_get_company_jobs_get_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """获取公司职位/Get company jobs  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn公司职位列表  ### 参数: - company_id: 公司ID（必填） - page: 页码（可选），默认为1 - sort_by: 排序方式（可选）：recent(最新), relevant(相关) - date_posted: 发布时间过滤（可选）：anytime, past_month, past_week, past_24_hours - experience_level: 经验级别（可选）：internship, entry_level, associate, mid_senior, director, executive - remote: 工作地点类型（可选）：onsite, remote, hybrid - job_type: 工作类型（可选）：full_time, part_time, contract, temporary, volunteer, internship, other - easy_apply: 是否易申请（可选） - under_10_applicants: 是否少于10个申请者（可选） - fair_chance_employer: 是否公平机会雇主（可选）  ### 返回: - 公司职位列表数据  # [English] ### Purpose: - Get LinkedIn company jobs list  ### Parameters: - company_id: Company ID (required) - page: Page number (optional), default is 1 - sort_by: Sort by (optional): recent, relevant - date_posted: Date posted filter (optional): anytime, past_month, past_week, past_24_hours - experience_level: Experience level (optional): internship, entry_level, associate, mid_senior, director, executive - remote: Remote filter (optional): onsite, remote, hybrid - job_type: Job type (optional): full_time, part_time, contract, temporary, volunteer, internship, other - easy_apply: Easy apply filter (optional) - under_10_applicants: Under 10 applicants filter (optional) - fair_chance_employer: Fair chance employer filter (optional)  ### Returns: - Company jobs list data  # [示例/Example] company_id = \"783611\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_jobs_api_v1_linkedin_web_get_company_jobs_get_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object company_id: 公司ID/Company ID (required)
        :param object page: 页码/Page number
        :param object sort_by: 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant
        :param object date_posted: 发布时间过滤：anytime, past_month, past_week, past_24_hours
        :param object experience_level: 经验级别：internship, entry_level, associate, mid_senior, director, executive
        :param object remote: 工作地点类型：onsite, remote, hybrid
        :param object job_type: 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other
        :param object easy_apply: 是否易申请/Filter easy apply jobs
        :param object under_10_applicants: 是否少于10个申请者/Filter jobs with under 10 applicants
        :param object fair_chance_employer: 是否公平机会雇主/Filter fair chance employer jobs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'page', 'sort_by', 'date_posted', 'experience_level', 'remote', 'job_type', 'easy_apply', 'under_10_applicants', 'fair_chance_employer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_jobs_api_v1_linkedin_web_get_company_jobs_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if self.api_client.client_side_validation and ('company_id' not in params or
                                                       params['company_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `company_id` when calling `get_company_jobs_api_v1_linkedin_web_get_company_jobs_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company_id' in params:
            query_params.append(('company_id', params['company_id']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'date_posted' in params:
            query_params.append(('date_posted', params['date_posted']))  # noqa: E501
        if 'experience_level' in params:
            query_params.append(('experience_level', params['experience_level']))  # noqa: E501
        if 'remote' in params:
            query_params.append(('remote', params['remote']))  # noqa: E501
        if 'job_type' in params:
            query_params.append(('job_type', params['job_type']))  # noqa: E501
        if 'easy_apply' in params:
            query_params.append(('easy_apply', params['easy_apply']))  # noqa: E501
        if 'under_10_applicants' in params:
            query_params.append(('under_10_applicants', params['under_10_applicants']))  # noqa: E501
        if 'fair_chance_employer' in params:
            query_params.append(('fair_chance_employer', params['fair_chance_employer']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_company_jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company_people_api_v1_linkedin_web_get_company_people_get(self, company_id, **kwargs):  # noqa: E501
        """获取公司员工/Get company people  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn公司员工列表  ### 参数: - company_id: 公司ID（必填） - page: 页码（可选），默认为1  ### 返回: - 公司员工列表数据  # [English] ### Purpose: - Get LinkedIn company people/employees list  ### Parameters: - company_id: Company ID (required) - page: Page number (optional), default is 1  ### Returns: - Company people list data  # [示例/Example] company_id = \"1066442\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_people_api_v1_linkedin_web_get_company_people_get(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object company_id: 公司ID/Company ID (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_people_api_v1_linkedin_web_get_company_people_get_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_people_api_v1_linkedin_web_get_company_people_get_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def get_company_people_api_v1_linkedin_web_get_company_people_get_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """获取公司员工/Get company people  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn公司员工列表  ### 参数: - company_id: 公司ID（必填） - page: 页码（可选），默认为1  ### 返回: - 公司员工列表数据  # [English] ### Purpose: - Get LinkedIn company people/employees list  ### Parameters: - company_id: Company ID (required) - page: Page number (optional), default is 1  ### Returns: - Company people list data  # [示例/Example] company_id = \"1066442\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_people_api_v1_linkedin_web_get_company_people_get_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object company_id: 公司ID/Company ID (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_people_api_v1_linkedin_web_get_company_people_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if self.api_client.client_side_validation and ('company_id' not in params or
                                                       params['company_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `company_id` when calling `get_company_people_api_v1_linkedin_web_get_company_people_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company_id' in params:
            query_params.append(('company_id', params['company_id']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_company_people', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company_posts_api_v1_linkedin_web_get_company_posts_get(self, company_id, **kwargs):  # noqa: E501
        """获取公司帖子/Get company posts  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn公司发布的帖子  ### 参数: - company_id: 公司ID（必填） - page: 页码（可选），默认为1 - sort_by: 排序方式（可选），默认为top     - top: 热门帖子     - recent: 最新帖子  ### 返回: - 公司帖子列表数据  # [English] ### Purpose: - Get posts published by LinkedIn company  ### Parameters: - company_id: Company ID (required) - page: Page number (optional), default is 1 - sort_by: Sort by (optional), default is top     - top: Top posts     - recent: Recent posts  ### Returns: - Company posts list data  # [示例/Example] company_id = \"10649600\" page = 1 sort_by = \"top\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_posts_api_v1_linkedin_web_get_company_posts_get(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object company_id: 公司ID/Company ID (required)
        :param object page: 页码/Page number
        :param object sort_by: 排序方式：top(热门)或recent(最新)/Sort by: top or recent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_posts_api_v1_linkedin_web_get_company_posts_get_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_posts_api_v1_linkedin_web_get_company_posts_get_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def get_company_posts_api_v1_linkedin_web_get_company_posts_get_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """获取公司帖子/Get company posts  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn公司发布的帖子  ### 参数: - company_id: 公司ID（必填） - page: 页码（可选），默认为1 - sort_by: 排序方式（可选），默认为top     - top: 热门帖子     - recent: 最新帖子  ### 返回: - 公司帖子列表数据  # [English] ### Purpose: - Get posts published by LinkedIn company  ### Parameters: - company_id: Company ID (required) - page: Page number (optional), default is 1 - sort_by: Sort by (optional), default is top     - top: Top posts     - recent: Recent posts  ### Returns: - Company posts list data  # [示例/Example] company_id = \"10649600\" page = 1 sort_by = \"top\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_posts_api_v1_linkedin_web_get_company_posts_get_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object company_id: 公司ID/Company ID (required)
        :param object page: 页码/Page number
        :param object sort_by: 排序方式：top(热门)或recent(最新)/Sort by: top or recent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'page', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_posts_api_v1_linkedin_web_get_company_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if self.api_client.client_side_validation and ('company_id' not in params or
                                                       params['company_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `company_id` when calling `get_company_posts_api_v1_linkedin_web_get_company_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company_id' in params:
            query_params.append(('company_id', params['company_id']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_company_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company_profile_api_v1_linkedin_web_get_company_profile_get(self, **kwargs):  # noqa: E501
        """获取公司资料/Get company profile  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn公司资料信息  ### 参数: - company: 公司名称（可选） - company_id: 公司ID（可选，额外消耗1次请求）  ### 注意: - company和company_id至少需要提供一个  ### 返回: - 公司资料数据  # [English] ### Purpose: - Get LinkedIn company profile information  ### Parameters: - company: Company name (optional) - company_id: Company ID (optional, +1 request)  ### Note: - At least one of company or company_id must be provided  ### Returns: - Company profile data  # [示例/Example] company = \"rapidapi\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_profile_api_v1_linkedin_web_get_company_profile_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object company: 公司名称/Company name
        :param object company_id: 公司ID（额外消耗1次请求）/Company ID (+1 request)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_profile_api_v1_linkedin_web_get_company_profile_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_company_profile_api_v1_linkedin_web_get_company_profile_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_company_profile_api_v1_linkedin_web_get_company_profile_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取公司资料/Get company profile  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn公司资料信息  ### 参数: - company: 公司名称（可选） - company_id: 公司ID（可选，额外消耗1次请求）  ### 注意: - company和company_id至少需要提供一个  ### 返回: - 公司资料数据  # [English] ### Purpose: - Get LinkedIn company profile information  ### Parameters: - company: Company name (optional) - company_id: Company ID (optional, +1 request)  ### Note: - At least one of company or company_id must be provided  ### Returns: - Company profile data  # [示例/Example] company = \"rapidapi\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_profile_api_v1_linkedin_web_get_company_profile_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object company: 公司名称/Company name
        :param object company_id: 公司ID（额外消耗1次请求）/Company ID (+1 request)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company', 'company_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_profile_api_v1_linkedin_web_get_company_profile_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company' in params:
            query_params.append(('company', params['company']))  # noqa: E501
        if 'company_id' in params:
            query_params.append(('company_id', params['company_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_company_profile', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_job_detail_api_v1_linkedin_web_get_job_detail_get(self, job_id, **kwargs):  # noqa: E501
        """获取职位详情/Get job detail  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn职位详情  ### 参数: - job_id: 职位ID（必填） - include_skills: 包含职位技能要求（可选，额外消耗1次请求）  ### 返回: - 职位详情数据  # [English] ### Purpose: - Get LinkedIn job detail  ### Parameters: - job_id: Job ID (required) - include_skills: Include job skills (optional, +1 request)  ### Returns: - Job detail data  # [示例/Example] job_id = \"4172815660\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_detail_api_v1_linkedin_web_get_job_detail_get(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object job_id: 职位ID/Job ID (required)
        :param object include_skills: 包含职位技能要求（额外消耗1次请求）/Include job skills (+1 request)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_job_detail_api_v1_linkedin_web_get_job_detail_get_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_job_detail_api_v1_linkedin_web_get_job_detail_get_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def get_job_detail_api_v1_linkedin_web_get_job_detail_get_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """获取职位详情/Get job detail  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn职位详情  ### 参数: - job_id: 职位ID（必填） - include_skills: 包含职位技能要求（可选，额外消耗1次请求）  ### 返回: - 职位详情数据  # [English] ### Purpose: - Get LinkedIn job detail  ### Parameters: - job_id: Job ID (required) - include_skills: Include job skills (optional, +1 request)  ### Returns: - Job detail data  # [示例/Example] job_id = \"4172815660\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_detail_api_v1_linkedin_web_get_job_detail_get_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object job_id: 职位ID/Job ID (required)
        :param object include_skills: 包含职位技能要求（额外消耗1次请求）/Include job skills (+1 request)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'include_skills']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_job_detail_api_v1_linkedin_web_get_job_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if self.api_client.client_side_validation and ('job_id' not in params or
                                                       params['job_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `job_id` when calling `get_job_detail_api_v1_linkedin_web_get_job_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in params:
            query_params.append(('job_id', params['job_id']))  # noqa: E501
        if 'include_skills' in params:
            query_params.append(('include_skills', params['include_skills']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_job_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_about_api_v1_linkedin_web_get_user_about_get(self, urn, **kwargs):  # noqa: E501
        """获取用户简介/Get user about  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户简介/关于信息  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取  ### 返回: - 用户简介数据  # [English] ### Purpose: - Get LinkedIn user about/bio information  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint  ### Returns: - User about data  # [示例/Example] urn = \"ACoAAA8BYqEBCGLg_vT_ca6mMEqkpp9nVffJ3hc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_about_api_v1_linkedin_web_get_user_about_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_about_api_v1_linkedin_web_get_user_about_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_about_api_v1_linkedin_web_get_user_about_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_about_api_v1_linkedin_web_get_user_about_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户简介/Get user about  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户简介/关于信息  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取  ### 返回: - 用户简介数据  # [English] ### Purpose: - Get LinkedIn user about/bio information  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint  ### Returns: - User about data  # [示例/Example] urn = \"ACoAAA8BYqEBCGLg_vT_ca6mMEqkpp9nVffJ3hc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_about_api_v1_linkedin_web_get_user_about_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_about_api_v1_linkedin_web_get_user_about_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_about_api_v1_linkedin_web_get_user_about_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_about', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_certifications_api_v1_linkedin_web_get_user_certifications_get(self, urn, **kwargs):  # noqa: E501
        """获取用户认证/Get user certifications  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户认证  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户认证列表数据  # [English] ### Purpose: - Get LinkedIn user certifications  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User certifications list data  # [示例/Example] urn = \"ACoAAARpiwIBp_SzoeHPlUfOvmtibe08Ea1iCh4\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_certifications_api_v1_linkedin_web_get_user_certifications_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_certifications_api_v1_linkedin_web_get_user_certifications_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_certifications_api_v1_linkedin_web_get_user_certifications_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_certifications_api_v1_linkedin_web_get_user_certifications_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户认证/Get user certifications  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户认证  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户认证列表数据  # [English] ### Purpose: - Get LinkedIn user certifications  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User certifications list data  # [示例/Example] urn = \"ACoAAARpiwIBp_SzoeHPlUfOvmtibe08Ea1iCh4\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_certifications_api_v1_linkedin_web_get_user_certifications_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_certifications_api_v1_linkedin_web_get_user_certifications_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_certifications_api_v1_linkedin_web_get_user_certifications_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_certifications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_comments_api_v1_linkedin_web_get_user_comments_get(self, urn, **kwargs):  # noqa: E501
        """获取用户评论/Get user comments  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户的评论  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1 - pagination_token: 分页令牌（可选）  ### 返回: - 用户评论列表数据  # [English] ### Purpose: - Get comments made by LinkedIn user  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1 - pagination_token: Pagination token (optional)  ### Returns: - User comments list data  # [示例/Example] urn = \"ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_comments_api_v1_linkedin_web_get_user_comments_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :param object pagination_token: 分页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_comments_api_v1_linkedin_web_get_user_comments_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_comments_api_v1_linkedin_web_get_user_comments_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_comments_api_v1_linkedin_web_get_user_comments_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户评论/Get user comments  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户的评论  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1 - pagination_token: 分页令牌（可选）  ### 返回: - 用户评论列表数据  # [English] ### Purpose: - Get comments made by LinkedIn user  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1 - pagination_token: Pagination token (optional)  ### Returns: - User comments list data  # [示例/Example] urn = \"ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_comments_api_v1_linkedin_web_get_user_comments_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :param object pagination_token: 分页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_comments_api_v1_linkedin_web_get_user_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_comments_api_v1_linkedin_web_get_user_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_contact_api_v1_linkedin_web_get_user_contact_get(self, username, **kwargs):  # noqa: E501
        """获取用户联系信息/Get user contact information  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户的联系信息  ### 参数: - username: LinkedIn用户名（必填）  ### 返回: - 用户联系信息数据  # [English] ### Purpose: - Get LinkedIn user contact information  ### Parameters: - username: LinkedIn username (required)  ### Returns: - User contact information data  # [示例/Example] username = \"shubhangi-shrivastava-39161bb7\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_contact_api_v1_linkedin_web_get_user_contact_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: LinkedIn用户名/LinkedIn username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_contact_api_v1_linkedin_web_get_user_contact_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_contact_api_v1_linkedin_web_get_user_contact_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def get_user_contact_api_v1_linkedin_web_get_user_contact_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """获取用户联系信息/Get user contact information  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户的联系信息  ### 参数: - username: LinkedIn用户名（必填）  ### 返回: - 用户联系信息数据  # [English] ### Purpose: - Get LinkedIn user contact information  ### Parameters: - username: LinkedIn username (required)  ### Returns: - User contact information data  # [示例/Example] username = \"shubhangi-shrivastava-39161bb7\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_contact_api_v1_linkedin_web_get_user_contact_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: LinkedIn用户名/LinkedIn username (required)
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
                    " to method get_user_contact_api_v1_linkedin_web_get_user_contact_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_user_contact_api_v1_linkedin_web_get_user_contact_get`")  # noqa: E501

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
            '/api/v1/linkedin/web/get_user_contact', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_educations_api_v1_linkedin_web_get_user_educations_get(self, urn, **kwargs):  # noqa: E501
        """获取用户教育背景/Get user educations  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户教育背景  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户教育背景列表数据  # [English] ### Purpose: - Get LinkedIn user educations  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User educations list data  # [示例/Example] urn = \"ACoAAARpiwIBp_SzoeHPlUfOvmtibe08Ea1iCh4\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_educations_api_v1_linkedin_web_get_user_educations_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_educations_api_v1_linkedin_web_get_user_educations_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_educations_api_v1_linkedin_web_get_user_educations_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_educations_api_v1_linkedin_web_get_user_educations_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户教育背景/Get user educations  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户教育背景  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户教育背景列表数据  # [English] ### Purpose: - Get LinkedIn user educations  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User educations list data  # [示例/Example] urn = \"ACoAAARpiwIBp_SzoeHPlUfOvmtibe08Ea1iCh4\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_educations_api_v1_linkedin_web_get_user_educations_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_educations_api_v1_linkedin_web_get_user_educations_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_educations_api_v1_linkedin_web_get_user_educations_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_educations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_experience_api_v1_linkedin_web_get_user_experience_get(self, urn, **kwargs):  # noqa: E501
        """获取用户工作经历/Get user experience  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户工作经历  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户工作经历列表数据  # [English] ### Purpose: - Get LinkedIn user work experience  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User experience list data  # [示例/Example] urn = \"ACoAAAjpjWIBMh1iBR4OgSPK5GXetlQ6dYUT-qo\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_experience_api_v1_linkedin_web_get_user_experience_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_experience_api_v1_linkedin_web_get_user_experience_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_experience_api_v1_linkedin_web_get_user_experience_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_experience_api_v1_linkedin_web_get_user_experience_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户工作经历/Get user experience  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户工作经历  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户工作经历列表数据  # [English] ### Purpose: - Get LinkedIn user work experience  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User experience list data  # [示例/Example] urn = \"ACoAAAjpjWIBMh1iBR4OgSPK5GXetlQ6dYUT-qo\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_experience_api_v1_linkedin_web_get_user_experience_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_experience_api_v1_linkedin_web_get_user_experience_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_experience_api_v1_linkedin_web_get_user_experience_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_experience', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get(self, username, **kwargs):  # noqa: E501
        """获取用户粉丝和连接数/Get user follower and connection  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户粉丝和连接数  ### 参数: - username: LinkedIn用户名（必填）  ### 返回: - 用户粉丝和连接数数据  # [English] ### Purpose: - Get LinkedIn user follower and connection count  ### Parameters: - username: LinkedIn username (required)  ### Returns: - User follower and connection data  # [示例/Example] username = \"zoranmilosevic\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: LinkedIn用户名/LinkedIn username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """获取用户粉丝和连接数/Get user follower and connection  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户粉丝和连接数  ### 参数: - username: LinkedIn用户名（必填）  ### 返回: - 用户粉丝和连接数数据  # [English] ### Purpose: - Get LinkedIn user follower and connection count  ### Parameters: - username: LinkedIn username (required)  ### Returns: - User follower and connection data  # [示例/Example] username = \"zoranmilosevic\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: LinkedIn用户名/LinkedIn username (required)
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
                    " to method get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get`")  # noqa: E501

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
            '/api/v1/linkedin/web/get_user_follower_and_connection', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_honors_api_v1_linkedin_web_get_user_honors_get(self, urn, **kwargs):  # noqa: E501
        """获取用户荣誉奖项/Get user honors  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户荣誉奖项  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户荣誉奖项列表数据  # [English] ### Purpose: - Get LinkedIn user honors and awards  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User honors list data  # [示例/Example] urn = \"ACoAAC41xVEBx77koDz3k1eJ5E9t8UZ7g0IVGj4\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_honors_api_v1_linkedin_web_get_user_honors_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_honors_api_v1_linkedin_web_get_user_honors_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_honors_api_v1_linkedin_web_get_user_honors_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_honors_api_v1_linkedin_web_get_user_honors_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户荣誉奖项/Get user honors  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户荣誉奖项  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户荣誉奖项列表数据  # [English] ### Purpose: - Get LinkedIn user honors and awards  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User honors list data  # [示例/Example] urn = \"ACoAAC41xVEBx77koDz3k1eJ5E9t8UZ7g0IVGj4\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_honors_api_v1_linkedin_web_get_user_honors_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_honors_api_v1_linkedin_web_get_user_honors_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_honors_api_v1_linkedin_web_get_user_honors_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_honors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_images_api_v1_linkedin_web_get_user_images_get(self, urn, **kwargs):  # noqa: E501
        """获取用户图片/Get user images  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户发布的图片  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1 - pagination_token: 分页令牌（可选）  ### 返回: - 用户图片列表数据  # [English] ### Purpose: - Get images published by LinkedIn user  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1 - pagination_token: Pagination token (optional)  ### Returns: - User images list data  # [示例/Example] urn = \"ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_images_api_v1_linkedin_web_get_user_images_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :param object pagination_token: 分页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_images_api_v1_linkedin_web_get_user_images_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_images_api_v1_linkedin_web_get_user_images_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_images_api_v1_linkedin_web_get_user_images_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户图片/Get user images  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户发布的图片  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1 - pagination_token: 分页令牌（可选）  ### 返回: - 用户图片列表数据  # [English] ### Purpose: - Get images published by LinkedIn user  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1 - pagination_token: Pagination token (optional)  ### Returns: - User images list data  # [示例/Example] urn = \"ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_images_api_v1_linkedin_web_get_user_images_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :param object pagination_token: 分页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_images_api_v1_linkedin_web_get_user_images_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_images_api_v1_linkedin_web_get_user_images_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_images', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get(self, urn, **kwargs):  # noqa: E501
        """获取用户感兴趣的公司/Get user interests companies  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户感兴趣的公司  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户感兴趣的公司列表数据  # [English] ### Purpose: - Get LinkedIn user interests - companies  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User interests companies list data  # [示例/Example] urn = \"ACoAAEDH77YBEVIYXAaEwTicp5CcB_hR7DfFL9o\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户感兴趣的公司/Get user interests companies  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户感兴趣的公司  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户感兴趣的公司列表数据  # [English] ### Purpose: - Get LinkedIn user interests - companies  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User interests companies list data  # [示例/Example] urn = \"ACoAAEDH77YBEVIYXAaEwTicp5CcB_hR7DfFL9o\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_interests_companies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get(self, urn, **kwargs):  # noqa: E501
        """获取用户感兴趣的群组/Get user interests groups  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户感兴趣的群组  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户感兴趣的群组列表数据  # [English] ### Purpose: - Get LinkedIn user interests - groups  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User interests groups list data  # [示例/Example] urn = \"ACoAAAjpjWIBMh1iBR4OgSPK5GXetlQ6dYUT-qo\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户感兴趣的群组/Get user interests groups  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户感兴趣的群组  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户感兴趣的群组列表数据  # [English] ### Purpose: - Get LinkedIn user interests - groups  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User interests groups list data  # [示例/Example] urn = \"ACoAAAjpjWIBMh1iBR4OgSPK5GXetlQ6dYUT-qo\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_interests_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_posts_api_v1_linkedin_web_get_user_posts_get(self, urn, **kwargs):  # noqa: E501
        """获取用户帖子/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户发布的帖子  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1 - pagination_token: 分页令牌（可选）  ### 返回: - 用户帖子列表数据  # [English] ### Purpose: - Get posts published by LinkedIn user  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1 - pagination_token: Pagination token (optional)  ### Returns: - User posts list data  # [示例/Example] urn = \"ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_posts_api_v1_linkedin_web_get_user_posts_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :param object pagination_token: 分页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_posts_api_v1_linkedin_web_get_user_posts_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_posts_api_v1_linkedin_web_get_user_posts_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_posts_api_v1_linkedin_web_get_user_posts_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户帖子/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户发布的帖子  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1 - pagination_token: 分页令牌（可选）  ### 返回: - 用户帖子列表数据  # [English] ### Purpose: - Get posts published by LinkedIn user  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1 - pagination_token: Pagination token (optional)  ### Returns: - User posts list data  # [示例/Example] urn = \"ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_posts_api_v1_linkedin_web_get_user_posts_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :param object pagination_token: 分页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_posts_api_v1_linkedin_web_get_user_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_posts_api_v1_linkedin_web_get_user_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_posts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_profile_api_v1_linkedin_web_get_user_profile_get(self, username, **kwargs):  # noqa: E501
        """获取用户资料/Get user profile  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户资料信息  ### 参数: - username: LinkedIn用户名（必填），可以从个人资料URL中获取，例如：https://www.linkedin.com/in/jack 则用户名为 jack - include_follower_and_connection: 包含粉丝和连接数（可选，额外消耗1次请求） - include_experiences: 包含工作经历（可选，额外消耗1次请求） - include_skills: 包含技能（可选，额外消耗1次请求） - include_certifications: 包含认证（可选，额外消耗1次请求） - include_publications: 包含出版物（可选，额外消耗1次请求） - include_educations: 包含教育背景（可选，额外消耗1次请求） - include_volunteers: 包含志愿者经历（可选，额外消耗1次请求） - include_honors: 包含荣誉奖项（可选，额外消耗1次请求） - include_interests: 包含兴趣（可选，额外消耗1次请求） - include_bio: 包含个人简介（可选，额外消耗1次请求）  ### 返回: - 用户资料数据，包含：     - id: 用户ID     - urn: 用户URN     - public_identifier: 公开标识符     - first_name: 名     - last_name: 姓     - full_name: 全名     - headline: 头衔/职位描述     - is_premium: 是否高级会员     - is_open_to_work: 是否开放工作机会     - is_hiring: 是否在招聘     - location: 位置信息     - cover: 封面图片     - 以及根据参数选择的其他信息  # [English] ### Purpose: - Get LinkedIn user profile information  ### Parameters: - username: LinkedIn username (required), can be obtained from profile URL, e.g., for https://www.linkedin.com/in/jack, the username is jack - include_follower_and_connection: Include follower and connection count (optional, +1 request) - include_experiences: Include work experiences (optional, +1 request) - include_skills: Include skills (optional, +1 request) - include_certifications: Include certifications (optional, +1 request) - include_publications: Include publications (optional, +1 request) - include_educations: Include educational background (optional, +1 request) - include_volunteers: Include volunteer experiences (optional, +1 request) - include_honors: Include honors and awards (optional, +1 request) - include_interests: Include interests (optional, +1 request) - include_bio: Include bio/about (optional, +1 request)  ### Returns: - User profile data including:     - id: User ID     - urn: User URN     - public_identifier: Public identifier     - first_name: First name     - last_name: Last name     - full_name: Full name     - headline: Headline/job description     - is_premium: Premium member status     - is_open_to_work: Open to work status     - is_hiring: Hiring status     - location: Location information     - cover: Cover images     - And other information based on selected parameters  # [示例/Example] username = \"jack\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_profile_api_v1_linkedin_web_get_user_profile_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: LinkedIn用户名/LinkedIn username (required)
        :param object include_follower_and_connection: 包含粉丝和连接数（额外消耗1次请求）/Include follower and connection count (+1 request)
        :param object include_experiences: 包含工作经历（额外消耗1次请求）/Include work experiences (+1 request)
        :param object include_skills: 包含技能（额外消耗1次请求）/Include skills (+1 request)
        :param object include_certifications: 包含认证（额外消耗1次请求）/Include certifications (+1 request)
        :param object include_publications: 包含出版物（额外消耗1次请求）/Include publications (+1 request)
        :param object include_educations: 包含教育背景（额外消耗1次请求）/Include educational background (+1 request)
        :param object include_volunteers: 包含志愿者经历（额外消耗1次请求）/Include volunteer experiences (+1 request)
        :param object include_honors: 包含荣誉奖项（额外消耗1次请求）/Include honors and awards (+1 request)
        :param object include_interests: 包含兴趣（额外消耗1次请求）/Include interests (+1 request)
        :param object include_bio: 包含个人简介（额外消耗1次请求）/Include bio/about (+1 request)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_profile_api_v1_linkedin_web_get_user_profile_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_profile_api_v1_linkedin_web_get_user_profile_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def get_user_profile_api_v1_linkedin_web_get_user_profile_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """获取用户资料/Get user profile  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户资料信息  ### 参数: - username: LinkedIn用户名（必填），可以从个人资料URL中获取，例如：https://www.linkedin.com/in/jack 则用户名为 jack - include_follower_and_connection: 包含粉丝和连接数（可选，额外消耗1次请求） - include_experiences: 包含工作经历（可选，额外消耗1次请求） - include_skills: 包含技能（可选，额外消耗1次请求） - include_certifications: 包含认证（可选，额外消耗1次请求） - include_publications: 包含出版物（可选，额外消耗1次请求） - include_educations: 包含教育背景（可选，额外消耗1次请求） - include_volunteers: 包含志愿者经历（可选，额外消耗1次请求） - include_honors: 包含荣誉奖项（可选，额外消耗1次请求） - include_interests: 包含兴趣（可选，额外消耗1次请求） - include_bio: 包含个人简介（可选，额外消耗1次请求）  ### 返回: - 用户资料数据，包含：     - id: 用户ID     - urn: 用户URN     - public_identifier: 公开标识符     - first_name: 名     - last_name: 姓     - full_name: 全名     - headline: 头衔/职位描述     - is_premium: 是否高级会员     - is_open_to_work: 是否开放工作机会     - is_hiring: 是否在招聘     - location: 位置信息     - cover: 封面图片     - 以及根据参数选择的其他信息  # [English] ### Purpose: - Get LinkedIn user profile information  ### Parameters: - username: LinkedIn username (required), can be obtained from profile URL, e.g., for https://www.linkedin.com/in/jack, the username is jack - include_follower_and_connection: Include follower and connection count (optional, +1 request) - include_experiences: Include work experiences (optional, +1 request) - include_skills: Include skills (optional, +1 request) - include_certifications: Include certifications (optional, +1 request) - include_publications: Include publications (optional, +1 request) - include_educations: Include educational background (optional, +1 request) - include_volunteers: Include volunteer experiences (optional, +1 request) - include_honors: Include honors and awards (optional, +1 request) - include_interests: Include interests (optional, +1 request) - include_bio: Include bio/about (optional, +1 request)  ### Returns: - User profile data including:     - id: User ID     - urn: User URN     - public_identifier: Public identifier     - first_name: First name     - last_name: Last name     - full_name: Full name     - headline: Headline/job description     - is_premium: Premium member status     - is_open_to_work: Open to work status     - is_hiring: Hiring status     - location: Location information     - cover: Cover images     - And other information based on selected parameters  # [示例/Example] username = \"jack\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_profile_api_v1_linkedin_web_get_user_profile_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: LinkedIn用户名/LinkedIn username (required)
        :param object include_follower_and_connection: 包含粉丝和连接数（额外消耗1次请求）/Include follower and connection count (+1 request)
        :param object include_experiences: 包含工作经历（额外消耗1次请求）/Include work experiences (+1 request)
        :param object include_skills: 包含技能（额外消耗1次请求）/Include skills (+1 request)
        :param object include_certifications: 包含认证（额外消耗1次请求）/Include certifications (+1 request)
        :param object include_publications: 包含出版物（额外消耗1次请求）/Include publications (+1 request)
        :param object include_educations: 包含教育背景（额外消耗1次请求）/Include educational background (+1 request)
        :param object include_volunteers: 包含志愿者经历（额外消耗1次请求）/Include volunteer experiences (+1 request)
        :param object include_honors: 包含荣誉奖项（额外消耗1次请求）/Include honors and awards (+1 request)
        :param object include_interests: 包含兴趣（额外消耗1次请求）/Include interests (+1 request)
        :param object include_bio: 包含个人简介（额外消耗1次请求）/Include bio/about (+1 request)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'include_follower_and_connection', 'include_experiences', 'include_skills', 'include_certifications', 'include_publications', 'include_educations', 'include_volunteers', 'include_honors', 'include_interests', 'include_bio']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_profile_api_v1_linkedin_web_get_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_user_profile_api_v1_linkedin_web_get_user_profile_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'include_follower_and_connection' in params:
            query_params.append(('include_follower_and_connection', params['include_follower_and_connection']))  # noqa: E501
        if 'include_experiences' in params:
            query_params.append(('include_experiences', params['include_experiences']))  # noqa: E501
        if 'include_skills' in params:
            query_params.append(('include_skills', params['include_skills']))  # noqa: E501
        if 'include_certifications' in params:
            query_params.append(('include_certifications', params['include_certifications']))  # noqa: E501
        if 'include_publications' in params:
            query_params.append(('include_publications', params['include_publications']))  # noqa: E501
        if 'include_educations' in params:
            query_params.append(('include_educations', params['include_educations']))  # noqa: E501
        if 'include_volunteers' in params:
            query_params.append(('include_volunteers', params['include_volunteers']))  # noqa: E501
        if 'include_honors' in params:
            query_params.append(('include_honors', params['include_honors']))  # noqa: E501
        if 'include_interests' in params:
            query_params.append(('include_interests', params['include_interests']))  # noqa: E501
        if 'include_bio' in params:
            query_params.append(('include_bio', params['include_bio']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_profile', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_publications_api_v1_linkedin_web_get_user_publications_get(self, urn, **kwargs):  # noqa: E501
        """获取用户出版物/Get user publications  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户出版物  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户出版物列表数据  # [English] ### Purpose: - Get LinkedIn user publications  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User publications list data  # [示例/Example] urn = \"ACoAAB8rG_UB7cstjC__gk5318uYsZOIVkyysi4\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_publications_api_v1_linkedin_web_get_user_publications_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_publications_api_v1_linkedin_web_get_user_publications_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_publications_api_v1_linkedin_web_get_user_publications_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_publications_api_v1_linkedin_web_get_user_publications_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户出版物/Get user publications  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户出版物  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户出版物列表数据  # [English] ### Purpose: - Get LinkedIn user publications  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User publications list data  # [示例/Example] urn = \"ACoAAB8rG_UB7cstjC__gk5318uYsZOIVkyysi4\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_publications_api_v1_linkedin_web_get_user_publications_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_publications_api_v1_linkedin_web_get_user_publications_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_publications_api_v1_linkedin_web_get_user_publications_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_publications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get(self, urn, **kwargs):  # noqa: E501
        """获取用户推荐信/Get user recommendations  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户的推荐信  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1 - type: 推荐类型（可选），默认为received     - received: 收到的推荐信     - given: 给出的推荐信 - pagination_token: 分页令牌（可选）  ### 返回: - 用户推荐信列表数据  # [English] ### Purpose: - Get LinkedIn user recommendations  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1 - type: Recommendation type (optional), default is received     - received: Recommendations received     - given: Recommendations given - pagination_token: Pagination token (optional)  ### Returns: - User recommendations list data  # [示例/Example] urn = \"ACoAAC3iNKcB3qbWJrP7K5Z3i89AF5c1snr8bhc\" page = 1 type = \"received\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :param object type: 推荐类型：received(收到的)或given(给出的)/Type: received or given
        :param object pagination_token: 分页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户推荐信/Get user recommendations  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户的推荐信  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1 - type: 推荐类型（可选），默认为received     - received: 收到的推荐信     - given: 给出的推荐信 - pagination_token: 分页令牌（可选）  ### 返回: - 用户推荐信列表数据  # [English] ### Purpose: - Get LinkedIn user recommendations  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1 - type: Recommendation type (optional), default is received     - received: Recommendations received     - given: Recommendations given - pagination_token: Pagination token (optional)  ### Returns: - User recommendations list data  # [示例/Example] urn = \"ACoAAC3iNKcB3qbWJrP7K5Z3i89AF5c1snr8bhc\" page = 1 type = \"received\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :param object type: 推荐类型：received(收到的)或given(给出的)/Type: received or given
        :param object pagination_token: 分页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page', 'type', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_recommendations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_skills_api_v1_linkedin_web_get_user_skills_get(self, urn, **kwargs):  # noqa: E501
        """获取用户技能/Get user skills  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户技能  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户技能列表数据  # [English] ### Purpose: - Get LinkedIn user skills  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User skills list data  # [示例/Example] urn = \"ACoAACkphDcBDruPBdXiAnqyc834jkTkd_4kRnU\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_skills_api_v1_linkedin_web_get_user_skills_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_skills_api_v1_linkedin_web_get_user_skills_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_skills_api_v1_linkedin_web_get_user_skills_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_skills_api_v1_linkedin_web_get_user_skills_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户技能/Get user skills  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户技能  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1  ### 返回: - 用户技能列表数据  # [English] ### Purpose: - Get LinkedIn user skills  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1  ### Returns: - User skills list data  # [示例/Example] urn = \"ACoAACkphDcBDruPBdXiAnqyc834jkTkd_4kRnU\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_skills_api_v1_linkedin_web_get_user_skills_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_skills_api_v1_linkedin_web_get_user_skills_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_skills_api_v1_linkedin_web_get_user_skills_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_skills', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_videos_api_v1_linkedin_web_get_user_videos_get(self, urn, **kwargs):  # noqa: E501
        """获取用户视频/Get user videos  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户发布的视频  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1 - pagination_token: 分页令牌（可选）  ### 返回: - 用户视频列表数据  # [English] ### Purpose: - Get videos published by LinkedIn user  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1 - pagination_token: Pagination token (optional)  ### Returns: - User videos list data  # [示例/Example] urn = \"ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_videos_api_v1_linkedin_web_get_user_videos_get(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :param object pagination_token: 分页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_videos_api_v1_linkedin_web_get_user_videos_get_with_http_info(urn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_videos_api_v1_linkedin_web_get_user_videos_get_with_http_info(urn, **kwargs)  # noqa: E501
            return data

    def get_user_videos_api_v1_linkedin_web_get_user_videos_get_with_http_info(self, urn, **kwargs):  # noqa: E501
        """获取用户视频/Get user videos  # noqa: E501

        # [中文] ### 用途: - 获取LinkedIn用户发布的视频  ### 参数: - urn: 用户URN（必填），可通过get_user_profile接口获取 - page: 页码（可选），默认为1 - pagination_token: 分页令牌（可选）  ### 返回: - 用户视频列表数据  # [English] ### Purpose: - Get videos published by LinkedIn user  ### Parameters: - urn: User URN (required), can be obtained from get_user_profile endpoint - page: Page number (optional), default is 1 - pagination_token: Pagination token (optional)  ### Returns: - User videos list data  # [示例/Example] urn = \"ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_videos_api_v1_linkedin_web_get_user_videos_get_with_http_info(urn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object urn: 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint (required)
        :param object page: 页码/Page number
        :param object pagination_token: 分页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['urn', 'page', 'pagination_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_videos_api_v1_linkedin_web_get_user_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'urn' is set
        if self.api_client.client_side_validation and ('urn' not in params or
                                                       params['urn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `urn` when calling `get_user_videos_api_v1_linkedin_web_get_user_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'urn' in params:
            query_params.append(('urn', params['urn']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'pagination_token' in params:
            query_params.append(('pagination_token', params['pagination_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/get_user_videos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_jobs_api_v1_linkedin_web_search_jobs_get(self, keyword, **kwargs):  # noqa: E501
        """搜索职位/Search jobs  # noqa: E501

        # [中文] ### 用途: - 搜索LinkedIn职位  ### 参数: - keyword: 搜索关键词（必填） - page: 页码（可选），默认为1 - sort_by: 排序方式（可选）：recent(最新), relevant(相关) - date_posted: 发布时间过滤（可选）：anytime, past_month, past_week, past_24_hours - geocode: 地理位置代码（可选） - company: 公司ID过滤（可选） - experience_level: 经验级别（可选）：internship, entry_level, associate, mid_senior, director, executive - remote: 工作地点类型（可选）：onsite, remote, hybrid - job_type: 工作类型（可选）：full_time, part_time, contract, temporary, volunteer, internship, other - easy_apply: 是否易申请（可选） - has_verifications: 是否有公司认证（可选） - under_10_applicants: 是否少于10个申请者（可选） - fair_chance_employer: 是否公平机会雇主（可选）  ### 返回: - 职位搜索结果列表数据  # [English] ### Purpose: - Search LinkedIn jobs  ### Parameters: - keyword: Search keyword (required) - page: Page number (optional), default is 1 - sort_by: Sort by (optional): recent, relevant - date_posted: Date posted filter (optional): anytime, past_month, past_week, past_24_hours - geocode: Geocode for location (optional) - company: Company ID filter (optional) - experience_level: Experience level (optional): internship, entry_level, associate, mid_senior, director, executive - remote: Remote filter (optional): onsite, remote, hybrid - job_type: Job type (optional): full_time, part_time, contract, temporary, volunteer, internship, other - easy_apply: Easy apply filter (optional) - has_verifications: Has verifications filter (optional) - under_10_applicants: Under 10 applicants filter (optional) - fair_chance_employer: Fair chance employer filter (optional)  ### Returns: - Job search results list data  # [示例/Example] keyword = \"backend\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_jobs_api_v1_linkedin_web_search_jobs_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
        :param object sort_by: 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant
        :param object date_posted: 发布时间过滤：anytime, past_month, past_week, past_24_hours
        :param object geocode: 地理位置代码，可通过Search Geocode Location获取/Geocode for location
        :param object company: 公司ID过滤/Company ID filter (e.g., 1441 for Google)
        :param object experience_level: 经验级别：internship, entry_level, associate, mid_senior, director, executive
        :param object remote: 工作地点类型：onsite, remote, hybrid
        :param object job_type: 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other
        :param object easy_apply: 是否易申请/Filter easy apply jobs
        :param object has_verifications: 是否有公司认证/Filter jobs with company verifications
        :param object under_10_applicants: 是否少于10个申请者/Filter jobs with under 10 applicants
        :param object fair_chance_employer: 是否公平机会雇主/Filter fair chance employer jobs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_jobs_api_v1_linkedin_web_search_jobs_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_jobs_api_v1_linkedin_web_search_jobs_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_jobs_api_v1_linkedin_web_search_jobs_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索职位/Search jobs  # noqa: E501

        # [中文] ### 用途: - 搜索LinkedIn职位  ### 参数: - keyword: 搜索关键词（必填） - page: 页码（可选），默认为1 - sort_by: 排序方式（可选）：recent(最新), relevant(相关) - date_posted: 发布时间过滤（可选）：anytime, past_month, past_week, past_24_hours - geocode: 地理位置代码（可选） - company: 公司ID过滤（可选） - experience_level: 经验级别（可选）：internship, entry_level, associate, mid_senior, director, executive - remote: 工作地点类型（可选）：onsite, remote, hybrid - job_type: 工作类型（可选）：full_time, part_time, contract, temporary, volunteer, internship, other - easy_apply: 是否易申请（可选） - has_verifications: 是否有公司认证（可选） - under_10_applicants: 是否少于10个申请者（可选） - fair_chance_employer: 是否公平机会雇主（可选）  ### 返回: - 职位搜索结果列表数据  # [English] ### Purpose: - Search LinkedIn jobs  ### Parameters: - keyword: Search keyword (required) - page: Page number (optional), default is 1 - sort_by: Sort by (optional): recent, relevant - date_posted: Date posted filter (optional): anytime, past_month, past_week, past_24_hours - geocode: Geocode for location (optional) - company: Company ID filter (optional) - experience_level: Experience level (optional): internship, entry_level, associate, mid_senior, director, executive - remote: Remote filter (optional): onsite, remote, hybrid - job_type: Job type (optional): full_time, part_time, contract, temporary, volunteer, internship, other - easy_apply: Easy apply filter (optional) - has_verifications: Has verifications filter (optional) - under_10_applicants: Under 10 applicants filter (optional) - fair_chance_employer: Fair chance employer filter (optional)  ### Returns: - Job search results list data  # [示例/Example] keyword = \"backend\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_jobs_api_v1_linkedin_web_search_jobs_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
        :param object sort_by: 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant
        :param object date_posted: 发布时间过滤：anytime, past_month, past_week, past_24_hours
        :param object geocode: 地理位置代码，可通过Search Geocode Location获取/Geocode for location
        :param object company: 公司ID过滤/Company ID filter (e.g., 1441 for Google)
        :param object experience_level: 经验级别：internship, entry_level, associate, mid_senior, director, executive
        :param object remote: 工作地点类型：onsite, remote, hybrid
        :param object job_type: 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other
        :param object easy_apply: 是否易申请/Filter easy apply jobs
        :param object has_verifications: 是否有公司认证/Filter jobs with company verifications
        :param object under_10_applicants: 是否少于10个申请者/Filter jobs with under 10 applicants
        :param object fair_chance_employer: 是否公平机会雇主/Filter fair chance employer jobs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page', 'sort_by', 'date_posted', 'geocode', 'company', 'experience_level', 'remote', 'job_type', 'easy_apply', 'has_verifications', 'under_10_applicants', 'fair_chance_employer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_jobs_api_v1_linkedin_web_search_jobs_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_jobs_api_v1_linkedin_web_search_jobs_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'date_posted' in params:
            query_params.append(('date_posted', params['date_posted']))  # noqa: E501
        if 'geocode' in params:
            query_params.append(('geocode', params['geocode']))  # noqa: E501
        if 'company' in params:
            query_params.append(('company', params['company']))  # noqa: E501
        if 'experience_level' in params:
            query_params.append(('experience_level', params['experience_level']))  # noqa: E501
        if 'remote' in params:
            query_params.append(('remote', params['remote']))  # noqa: E501
        if 'job_type' in params:
            query_params.append(('job_type', params['job_type']))  # noqa: E501
        if 'easy_apply' in params:
            query_params.append(('easy_apply', params['easy_apply']))  # noqa: E501
        if 'has_verifications' in params:
            query_params.append(('has_verifications', params['has_verifications']))  # noqa: E501
        if 'under_10_applicants' in params:
            query_params.append(('under_10_applicants', params['under_10_applicants']))  # noqa: E501
        if 'fair_chance_employer' in params:
            query_params.append(('fair_chance_employer', params['fair_chance_employer']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/search_jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_people_api_v1_linkedin_web_search_people_get(self, **kwargs):  # noqa: E501
        """搜索用户/Search people  # noqa: E501

        # [中文] ### 用途: - 搜索LinkedIn用户  ### 参数: - name: 搜索关键词（可选） - first_name: 名（可选） - last_name: 姓（可选） - title: 职位（可选） - company: 公司（可选） - school: 学校（可选） - page: 页码（可选），默认为1 - geocode_location: 地理位置代码（可选） - current_company: 当前公司ID（可选） - profile_language: 个人资料语言（可选） - industry: 行业ID（可选） - service_category: 服务类别ID（可选）  ### 返回: - 用户搜索结果列表数据  # [English] ### Purpose: - Search LinkedIn people  ### Parameters: - name: Search keyword (optional) - first_name: First name (optional) - last_name: Last name (optional) - title: Title (optional) - company: Company (optional) - school: School (optional) - page: Page number (optional), default is 1 - geocode_location: Geocode for location (optional) - current_company: Current company ID (optional) - profile_language: Profile language (optional) - industry: Industry ID (optional) - service_category: Service category ID (optional)  ### Returns: - People search results list data  # [示例/Example] name = \"john\" first_name = \"john\" last_name = \"oliver\" title = \"manager\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_people_api_v1_linkedin_web_search_people_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object name: 搜索关键词/Search keyword for people
        :param object first_name: 名/First name
        :param object last_name: 姓/Last name
        :param object title: 职位/Title
        :param object company: 公司/Company
        :param object school: 学校/School
        :param object page: 页码/Page number
        :param object geocode_location: 地理位置代码/Geocode for location (e.g., 103644278 for United States)
        :param object current_company: 当前公司ID/Current company ID
        :param object profile_language: 个人资料语言/Profile language
        :param object industry: 行业ID/Industry ID
        :param object service_category: 服务类别ID/Service category ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_people_api_v1_linkedin_web_search_people_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_people_api_v1_linkedin_web_search_people_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_people_api_v1_linkedin_web_search_people_get_with_http_info(self, **kwargs):  # noqa: E501
        """搜索用户/Search people  # noqa: E501

        # [中文] ### 用途: - 搜索LinkedIn用户  ### 参数: - name: 搜索关键词（可选） - first_name: 名（可选） - last_name: 姓（可选） - title: 职位（可选） - company: 公司（可选） - school: 学校（可选） - page: 页码（可选），默认为1 - geocode_location: 地理位置代码（可选） - current_company: 当前公司ID（可选） - profile_language: 个人资料语言（可选） - industry: 行业ID（可选） - service_category: 服务类别ID（可选）  ### 返回: - 用户搜索结果列表数据  # [English] ### Purpose: - Search LinkedIn people  ### Parameters: - name: Search keyword (optional) - first_name: First name (optional) - last_name: Last name (optional) - title: Title (optional) - company: Company (optional) - school: School (optional) - page: Page number (optional), default is 1 - geocode_location: Geocode for location (optional) - current_company: Current company ID (optional) - profile_language: Profile language (optional) - industry: Industry ID (optional) - service_category: Service category ID (optional)  ### Returns: - People search results list data  # [示例/Example] name = \"john\" first_name = \"john\" last_name = \"oliver\" title = \"manager\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_people_api_v1_linkedin_web_search_people_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object name: 搜索关键词/Search keyword for people
        :param object first_name: 名/First name
        :param object last_name: 姓/Last name
        :param object title: 职位/Title
        :param object company: 公司/Company
        :param object school: 学校/School
        :param object page: 页码/Page number
        :param object geocode_location: 地理位置代码/Geocode for location (e.g., 103644278 for United States)
        :param object current_company: 当前公司ID/Current company ID
        :param object profile_language: 个人资料语言/Profile language
        :param object industry: 行业ID/Industry ID
        :param object service_category: 服务类别ID/Service category ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'first_name', 'last_name', 'title', 'company', 'school', 'page', 'geocode_location', 'current_company', 'profile_language', 'industry', 'service_category']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_people_api_v1_linkedin_web_search_people_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'first_name' in params:
            query_params.append(('first_name', params['first_name']))  # noqa: E501
        if 'last_name' in params:
            query_params.append(('last_name', params['last_name']))  # noqa: E501
        if 'title' in params:
            query_params.append(('title', params['title']))  # noqa: E501
        if 'company' in params:
            query_params.append(('company', params['company']))  # noqa: E501
        if 'school' in params:
            query_params.append(('school', params['school']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'geocode_location' in params:
            query_params.append(('geocode_location', params['geocode_location']))  # noqa: E501
        if 'current_company' in params:
            query_params.append(('current_company', params['current_company']))  # noqa: E501
        if 'profile_language' in params:
            query_params.append(('profile_language', params['profile_language']))  # noqa: E501
        if 'industry' in params:
            query_params.append(('industry', params['industry']))  # noqa: E501
        if 'service_category' in params:
            query_params.append(('service_category', params['service_category']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/linkedin/web/search_people', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
