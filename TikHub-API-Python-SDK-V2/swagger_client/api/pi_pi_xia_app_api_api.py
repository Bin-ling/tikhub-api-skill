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


class PiPiXiaAppAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get(self, hashtag_id, **kwargs):  # noqa: E501
        """获取话题详情/Get hashtag detail  # noqa: E501

        # [中文] ### 用途: - 获取话题详情数据。 ### 参数: - hashtag_id: 话题id，可以从分享链接中获取。 ### 返回: - 话题详情数据  # [English] ### Purpose: - Get hashtag detail data. ### Parameters: - hashtag_id: AKA hashtag id, can be obtained from the share link. ### Return: - Hashtag detail data # [示例/Example] hashtag_id = \"129559\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get(hashtag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object hashtag_id: 话题id/Hashtag id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get_with_http_info(hashtag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get_with_http_info(hashtag_id, **kwargs)  # noqa: E501
            return data

    def fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get_with_http_info(self, hashtag_id, **kwargs):  # noqa: E501
        """获取话题详情/Get hashtag detail  # noqa: E501

        # [中文] ### 用途: - 获取话题详情数据。 ### 参数: - hashtag_id: 话题id，可以从分享链接中获取。 ### 返回: - 话题详情数据  # [English] ### Purpose: - Get hashtag detail data. ### Parameters: - hashtag_id: AKA hashtag id, can be obtained from the share link. ### Return: - Hashtag detail data # [示例/Example] hashtag_id = \"129559\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get_with_http_info(hashtag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object hashtag_id: 话题id/Hashtag id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hashtag_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hashtag_id' is set
        if self.api_client.client_side_validation and ('hashtag_id' not in params or
                                                       params['hashtag_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hashtag_id` when calling `fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hashtag_id' in params:
            query_params.append(('hashtag_id', params['hashtag_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_hashtag_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get(self, hashtag_id, **kwargs):  # noqa: E501
        """获取话题作品列表/Get hashtag post list  # noqa: E501

        # [中文] ### 用途: - 获取话题作品列表数据。 ### 参数: - hashtag_id: 话题id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 - feed_count: 翻页数量，默认为0，后续每次翻页加1，比如第一页为0，第二页为1，第三页为2，以此类推。 - hashtag_request_type: 话题请求类型，默认为0，可用值如下：     - 0: 热门     - 1: 最新     - 2: 精华 - hashtag_sort_type: 话题排序类型，默认为3，可用值如下：     - 3: 按热度     - 2: 按时间，从新到旧     - 1: 精华 ### 返回: - 话题作品列表数据  # [English] ### Purpose: - Get hashtag post list data. ### Parameters: - hashtag_id: AKA hashtag id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. - feed_count: Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. ### Return: - Hashtag post list data  # [示例/Example] hashtag_id = \"129559\" cursor = \"0\" feed_count = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get(hashtag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object hashtag_id: 话题id/Hashtag id (required)
        :param object cursor: 翻页游标/Page cursor
        :param object feed_count: 翻页数量/Page count
        :param object hashtag_request_type: 话题请求类型/Hashtag request type
        :param object hashtag_sort_type: 话题排序类型/Hashtag sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get_with_http_info(hashtag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get_with_http_info(hashtag_id, **kwargs)  # noqa: E501
            return data

    def fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get_with_http_info(self, hashtag_id, **kwargs):  # noqa: E501
        """获取话题作品列表/Get hashtag post list  # noqa: E501

        # [中文] ### 用途: - 获取话题作品列表数据。 ### 参数: - hashtag_id: 话题id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 - feed_count: 翻页数量，默认为0，后续每次翻页加1，比如第一页为0，第二页为1，第三页为2，以此类推。 - hashtag_request_type: 话题请求类型，默认为0，可用值如下：     - 0: 热门     - 1: 最新     - 2: 精华 - hashtag_sort_type: 话题排序类型，默认为3，可用值如下：     - 3: 按热度     - 2: 按时间，从新到旧     - 1: 精华 ### 返回: - 话题作品列表数据  # [English] ### Purpose: - Get hashtag post list data. ### Parameters: - hashtag_id: AKA hashtag id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. - feed_count: Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. ### Return: - Hashtag post list data  # [示例/Example] hashtag_id = \"129559\" cursor = \"0\" feed_count = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get_with_http_info(hashtag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object hashtag_id: 话题id/Hashtag id (required)
        :param object cursor: 翻页游标/Page cursor
        :param object feed_count: 翻页数量/Page count
        :param object hashtag_request_type: 话题请求类型/Hashtag request type
        :param object hashtag_sort_type: 话题排序类型/Hashtag sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hashtag_id', 'cursor', 'feed_count', 'hashtag_request_type', 'hashtag_sort_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hashtag_id' is set
        if self.api_client.client_side_validation and ('hashtag_id' not in params or
                                                       params['hashtag_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hashtag_id` when calling `fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hashtag_id' in params:
            query_params.append(('hashtag_id', params['hashtag_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'feed_count' in params:
            query_params.append(('feed_count', params['feed_count']))  # noqa: E501
        if 'hashtag_request_type' in params:
            query_params.append(('hashtag_request_type', params['hashtag_request_type']))  # noqa: E501
        if 'hashtag_sort_type' in params:
            query_params.append(('hashtag_sort_type', params['hashtag_sort_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_hashtag_post_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get(self, **kwargs):  # noqa: E501
        """获取首页推荐/Get home feed  # noqa: E501

        # [中文] ### 用途: - 获取首页推荐数据。 ### 参数: - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 ### 返回: - 首页推荐数据  # [English] ### Purpose: - Get home feed data. ### Parameters: - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. ### Return: - Home feed data  # [示例/Example] cursor = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cursor: 翻页游标/Page cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取首页推荐/Get home feed  # noqa: E501

        # [中文] ### 用途: - 获取首页推荐数据。 ### 参数: - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 ### 返回: - 首页推荐数据  # [English] ### Purpose: - Get home feed data. ### Parameters: - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. ### Return: - Home feed data  # [示例/Example] cursor = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cursor: 翻页游标/Page cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_home_feed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get(self, **kwargs):  # noqa: E501
        """获取首页短剧推荐/Get home short drama feed  # noqa: E501

        # [中文] ### 用途: - 获取首页短剧推荐数据。 ### 参数: - page: 页码，默认为1，每次翻页加1。 ### 返回: - 首页短剧推荐数据  # [English] ### Purpose: - Get home short drama feed data. ### Parameters: - page: Page number, default is 1, add 1 for each page. ### Return: - Home short drama feed data  # [示例/Example] page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取首页短剧推荐/Get home short drama feed  # noqa: E501

        # [中文] ### 用途: - 获取首页短剧推荐数据。 ### 参数: - page: 页码，默认为1，每次翻页加1。 ### 返回: - 首页短剧推荐数据  # [English] ### Purpose: - Get home short drama feed data. ### Parameters: - page: Page number, default is 1, add 1 for each page. ### Return: - Home short drama feed data  # [示例/Example] page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_home_short_drama_feed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get(self, block_type, **kwargs):  # noqa: E501
        """获取热搜榜单详情/Get hot search board detail  # noqa: E501

        # [中文] ### 用途: - 获取热搜榜单详情数据。 ### 参数: - block_type: 榜单类型，可以从`/fetch_hot_search_board_list`接口中获取。 ### 返回: - 热搜榜单详情数据  # [English] ### Purpose: - Get hot search board detail data. ### Parameters: - block_type: Board type, can be obtained from the `/fetch_hot_search_board_list` interface. ### Return: - Hot search board detail data  # [示例/Example] block_type = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get(block_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object block_type: 榜单类型/Board type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get_with_http_info(block_type, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get_with_http_info(block_type, **kwargs)  # noqa: E501
            return data

    def fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get_with_http_info(self, block_type, **kwargs):  # noqa: E501
        """获取热搜榜单详情/Get hot search board detail  # noqa: E501

        # [中文] ### 用途: - 获取热搜榜单详情数据。 ### 参数: - block_type: 榜单类型，可以从`/fetch_hot_search_board_list`接口中获取。 ### 返回: - 热搜榜单详情数据  # [English] ### Purpose: - Get hot search board detail data. ### Parameters: - block_type: Board type, can be obtained from the `/fetch_hot_search_board_list` interface. ### Return: - Hot search board detail data  # [示例/Example] block_type = 12  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get_with_http_info(block_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object block_type: 榜单类型/Board type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['block_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'block_type' is set
        if self.api_client.client_side_validation and ('block_type' not in params or
                                                       params['block_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `block_type` when calling `fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'block_type' in params:
            query_params.append(('block_type', params['block_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_hot_search_board_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get(self, **kwargs):  # noqa: E501
        """获取热搜榜单列表/Get hot search board list  # noqa: E501

        # [中文] ### 用途: - 获取热搜榜单列表数据。 ### 返回: - 热搜榜单列表数据  # [English] ### Purpose: - Get hot search board list data. ### Return: - Hot search board list data  # [示例/Example] 无/None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热搜榜单列表/Get hot search board list  # noqa: E501

        # [中文] ### 用途: - 获取热搜榜单列表数据。 ### 返回: - 热搜榜单列表数据  # [English] ### Purpose: - Get hot search board list data. ### Return: - Hot search board list data  # [示例/Example] 无/None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get" % key
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
            '/api/v1/pipixia/app/fetch_hot_search_board_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get(self, **kwargs):  # noqa: E501
        """获取热搜词条/Get hot search words  # noqa: E501

        # [中文] ### 用途: - 获取热搜词条数据。 ### 返回: - 热搜词条数据  # [English] ### Purpose: - Get hot search words data. ### Return: - Hot search words data  # [示例/Example] 无/None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热搜词条/Get hot search words  # noqa: E501

        # [中文] ### 用途: - 获取热搜词条数据。 ### 返回: - 热搜词条数据  # [English] ### Purpose: - Get hot search words data. ### Return: - Hot search words data  # [示例/Example] 无/None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get" % key
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
            '/api/v1/pipixia/app/fetch_hot_search_words', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get(self, cell_id, **kwargs):  # noqa: E501
        """增加作品浏览数/Increase post view count  # noqa: E501

        # [中文] ### 用途: - 增加作品浏览数。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 - cell_type: 作品类型，1为视频，多大数保持默认值即可。 ### 返回: - 执行结果  # [English] ### Purpose: - Increase post view count. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. - cell_type: Video type, 1 for video, keep the default value for other types. ### Return: - Execution result  # [示例/Example] cell_id = \"7411193113223371043\" cell_type = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cell_id: 作品id/Video id (required)
        :param object cell_type: 作品类型/Video type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get_with_http_info(cell_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get_with_http_info(cell_id, **kwargs)  # noqa: E501
            return data

    def fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get_with_http_info(self, cell_id, **kwargs):  # noqa: E501
        """增加作品浏览数/Increase post view count  # noqa: E501

        # [中文] ### 用途: - 增加作品浏览数。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 - cell_type: 作品类型，1为视频，多大数保持默认值即可。 ### 返回: - 执行结果  # [English] ### Purpose: - Increase post view count. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. - cell_type: Video type, 1 for video, keep the default value for other types. ### Return: - Execution result  # [示例/Example] cell_id = \"7411193113223371043\" cell_type = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get_with_http_info(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cell_id: 作品id/Video id (required)
        :param object cell_type: 作品类型/Video type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cell_id', 'cell_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cell_id' is set
        if self.api_client.client_side_validation and ('cell_id' not in params or
                                                       params['cell_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cell_id` when calling `fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cell_id' in params:
            query_params.append(('cell_id', params['cell_id']))  # noqa: E501
        if 'cell_type' in params:
            query_params.append(('cell_type', params['cell_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_increase_post_view_count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get(self, cell_id, **kwargs):  # noqa: E501
        """获取作品评论列表/Get post comment list  # noqa: E501

        # [中文] ### 用途: - 获取作品的评论列表。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 - cell_type: 作品类型，1为视频，多大数保持默认值即可。 - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。 ### 返回: - 作品评论列表  # [English] ### Purpose: - Get the comment list of a post. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. - cell_type: Video type, 1 for video, keep the default value for other types. - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. ### Return: - Post comment list  # [示例/Example] cell_id = \"7411193113223371043\" cell_type = 1 offset = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cell_id: 作品id/Video id (required)
        :param object cell_type: 作品类型/Video type
        :param object offset: 翻页游标/Page cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get_with_http_info(cell_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get_with_http_info(cell_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get_with_http_info(self, cell_id, **kwargs):  # noqa: E501
        """获取作品评论列表/Get post comment list  # noqa: E501

        # [中文] ### 用途: - 获取作品的评论列表。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 - cell_type: 作品类型，1为视频，多大数保持默认值即可。 - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。 ### 返回: - 作品评论列表  # [English] ### Purpose: - Get the comment list of a post. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. - cell_type: Video type, 1 for video, keep the default value for other types. - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. ### Return: - Post comment list  # [示例/Example] cell_id = \"7411193113223371043\" cell_type = 1 offset = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get_with_http_info(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cell_id: 作品id/Video id (required)
        :param object cell_type: 作品类型/Video type
        :param object offset: 翻页游标/Page cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cell_id', 'cell_type', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cell_id' is set
        if self.api_client.client_side_validation and ('cell_id' not in params or
                                                       params['cell_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cell_id` when calling `fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cell_id' in params:
            query_params.append(('cell_id', params['cell_id']))  # noqa: E501
        if 'cell_type' in params:
            query_params.append(('cell_type', params['cell_type']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_post_comment_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get(self, cell_id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据，支持图文、视频等。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 - cell_type: 作品类型，1为视频，多大数保持默认值即可。 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data, support photo, video, etc. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. - cell_type: Video type, 1 for video, keep the default value for other types. ### Return: - Video data  # [示例/Example] cell_id = \"7411193113223371043\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cell_id: 作品id/Video id (required)
        :param object cell_type: 作品类型/Video type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get_with_http_info(cell_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get_with_http_info(cell_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get_with_http_info(self, cell_id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据，支持图文、视频等。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 - cell_type: 作品类型，1为视频，多大数保持默认值即可。 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data, support photo, video, etc. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. - cell_type: Video type, 1 for video, keep the default value for other types. ### Return: - Video data  # [示例/Example] cell_id = \"7411193113223371043\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get_with_http_info(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cell_id: 作品id/Video id (required)
        :param object cell_type: 作品类型/Video type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cell_id', 'cell_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cell_id' is set
        if self.api_client.client_side_validation and ('cell_id' not in params or
                                                       params['cell_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cell_id` when calling `fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cell_id' in params:
            query_params.append(('cell_id', params['cell_id']))  # noqa: E501
        if 'cell_type' in params:
            query_params.append(('cell_type', params['cell_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_post_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get(self, cell_id, **kwargs):  # noqa: E501
        """获取作品统计数据/Get post statistics  # noqa: E501

        # [中文] ### 用途: - 获取单个作品的统计数据，如点赞数、评论数、转发数等。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 ### 返回: - 作品统计数据  # [English] ### Purpose: - Get the statistics of a single post, such as the number of likes, comments, reposts, etc. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. ### Return: - Post statistics  # [示例/Example] cell_id = \"7411193113223371043\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cell_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get_with_http_info(cell_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get_with_http_info(cell_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get_with_http_info(self, cell_id, **kwargs):  # noqa: E501
        """获取作品统计数据/Get post statistics  # noqa: E501

        # [中文] ### 用途: - 获取单个作品的统计数据，如点赞数、评论数、转发数等。 ### 参数: - cell_id: 作品id，可以从分享链接中获取。 ### 返回: - 作品统计数据  # [English] ### Purpose: - Get the statistics of a single post, such as the number of likes, comments, reposts, etc. ### Parameters: - cell_id: AKA video id, can be obtained from the share link. ### Return: - Post statistics  # [示例/Example] cell_id = \"7411193113223371043\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get_with_http_info(cell_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cell_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cell_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cell_id' is set
        if self.api_client.client_side_validation and ('cell_id' not in params or
                                                       params['cell_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cell_id` when calling `fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cell_id' in params:
            query_params.append(('cell_id', params['cell_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_post_statistics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_search_api_v1_pipixia_app_fetch_search_get(self, keyword, **kwargs):  # noqa: E501
        """搜索接口/Search API  # noqa: E501

        # [中文] ### 用途: - 搜索接口，支持搜索用户、作品等。 ### 参数: - keyword: 搜索关键词。 - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。 - search_type: 搜索类型，可用值如下：     - 1: 综合     - 8: 热门     - 9: 新鲜     - 2：视频     - 3：图文     - 4：用户     - 5：话题 ### 返回: - 搜索结果  # [English] ### Purpose: - Search API, support search user, post, etc. ### Parameters: - keyword: Search keyword. - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. - search_type: Search type, available values are as follows:     - 1: Comprehensive     - 8: Hot     - 9: Fresh     - 2: Video     - 3: Photo     - 4: User     - 5: Hashtag ### Return: - Search result  # [示例/Example] keyword = \"皮皮虾\" offset = \"0\" search_type = \"1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_api_v1_pipixia_app_fetch_search_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object offset: 翻页游标/Page cursor
        :param object search_type: 搜索类型/Search type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_api_v1_pipixia_app_fetch_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_api_v1_pipixia_app_fetch_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_api_v1_pipixia_app_fetch_search_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索接口/Search API  # noqa: E501

        # [中文] ### 用途: - 搜索接口，支持搜索用户、作品等。 ### 参数: - keyword: 搜索关键词。 - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。 - search_type: 搜索类型，可用值如下：     - 1: 综合     - 8: 热门     - 9: 新鲜     - 2：视频     - 3：图文     - 4：用户     - 5：话题 ### 返回: - 搜索结果  # [English] ### Purpose: - Search API, support search user, post, etc. ### Parameters: - keyword: Search keyword. - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. - search_type: Search type, available values are as follows:     - 1: Comprehensive     - 8: Hot     - 9: Fresh     - 2: Video     - 3: Photo     - 4: User     - 5: Hashtag ### Return: - Search result  # [示例/Example] keyword = \"皮皮虾\" offset = \"0\" search_type = \"1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_api_v1_pipixia_app_fetch_search_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object offset: 翻页游标/Page cursor
        :param object search_type: 搜索类型/Search type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'search_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_api_v1_pipixia_app_fetch_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_api_v1_pipixia_app_fetch_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'search_type' in params:
            query_params.append(('search_type', params['search_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_short_url_api_v1_pipixia_app_fetch_short_url_get(self, original_url, **kwargs):  # noqa: E501
        """生成短连接/Generate short URL  # noqa: E501

        # [中文] ### 用途: - 生成短连接。 ### 参数: - original_url: 原始链接，可以是任意链接。 ### 返回: - 短连接  # [English] ### Purpose: - Generate short URL. ### Parameters: - original_url: Original URL, can be any link. ### Return: - Short URL  # [示例/Example] original_url = \"https://h5.pipix.com/item/7385813877985909043\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_short_url_api_v1_pipixia_app_fetch_short_url_get(original_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object original_url: 原始链接/Original URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_short_url_api_v1_pipixia_app_fetch_short_url_get_with_http_info(original_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_short_url_api_v1_pipixia_app_fetch_short_url_get_with_http_info(original_url, **kwargs)  # noqa: E501
            return data

    def fetch_short_url_api_v1_pipixia_app_fetch_short_url_get_with_http_info(self, original_url, **kwargs):  # noqa: E501
        """生成短连接/Generate short URL  # noqa: E501

        # [中文] ### 用途: - 生成短连接。 ### 参数: - original_url: 原始链接，可以是任意链接。 ### 返回: - 短连接  # [English] ### Purpose: - Generate short URL. ### Parameters: - original_url: Original URL, can be any link. ### Return: - Short URL  # [示例/Example] original_url = \"https://h5.pipix.com/item/7385813877985909043\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_short_url_api_v1_pipixia_app_fetch_short_url_get_with_http_info(original_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object original_url: 原始链接/Original URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['original_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_short_url_api_v1_pipixia_app_fetch_short_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'original_url' is set
        if self.api_client.client_side_validation and ('original_url' not in params or
                                                       params['original_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `original_url` when calling `fetch_short_url_api_v1_pipixia_app_fetch_short_url_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'original_url' in params:
            query_params.append(('original_url', params['original_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_short_url', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Get user follower list  # noqa: E501

        # [中文] ### 用途: - 获取用户的粉丝列表。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 ### 返回: - 用户粉丝列表  # [English] ### Purpose: - Get user's follower list. ### Parameters: - user_id: AKA user id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. ### Return: - User follower list  # [示例/Example] user_id = \"1310254082831248\" cursor = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id (required)
        :param object cursor: 翻页游标/Page cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Get user follower list  # noqa: E501

        # [中文] ### 用途: - 获取用户的粉丝列表。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 ### 返回: - 用户粉丝列表  # [English] ### Purpose: - Get user's follower list. ### Parameters: - user_id: AKA user id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. ### Return: - User follower list  # [示例/Example] user_id = \"1310254082831248\" cursor = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id (required)
        :param object cursor: 翻页游标/Page cursor
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
                    " to method fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get`")  # noqa: E501

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
            '/api/v1/pipixia/app/fetch_user_follower_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户关注列表/Get user following list  # noqa: E501

        # [中文] ### 用途: - 获取用户的关注列表。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 ### 返回: - 用户关注列表  # [English] ### Purpose: - Get user's following list. ### Parameters: - user_id: AKA user id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. ### Return: - User following list  # [示例/Example] user_id = \"1310254082831248\" cursor = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id (required)
        :param object cursor: 翻页游标/Page cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户关注列表/Get user following list  # noqa: E501

        # [中文] ### 用途: - 获取用户的关注列表。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 ### 返回: - 用户关注列表  # [English] ### Purpose: - Get user's following list. ### Parameters: - user_id: AKA user id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. ### Return: - User following list  # [示例/Example] user_id = \"1310254082831248\" cursor = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id (required)
        :param object cursor: 翻页游标/Page cursor
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
                    " to method fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get`")  # noqa: E501

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
            '/api/v1/pipixia/app/fetch_user_following_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_api_v1_pipixia_app_fetch_user_info_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息/Get user information  # noqa: E501

        # [中文] ### 用途: - 获取用户信息，如昵称、性别、头像等。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 ### 返回: - 用户信息  # [English] ### Purpose: - Get user information, such as nickname and avatar. ### Parameters: - user_id: AKA user id, can be obtained from the share link. ### Return: - User information  # [示例/Example] user_id = \"1310254082831248\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_pipixia_app_fetch_user_info_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_pipixia_app_fetch_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_pipixia_app_fetch_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_pipixia_app_fetch_user_info_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息/Get user information  # noqa: E501

        # [中文] ### 用途: - 获取用户信息，如昵称、性别、头像等。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 ### 返回: - 用户信息  # [English] ### Purpose: - Get user information, such as nickname and avatar. ### Parameters: - user_id: AKA user id, can be obtained from the share link. ### Return: - User information  # [示例/Example] user_id = \"1310254082831248\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_pipixia_app_fetch_user_info_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id (required)
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
                    " to method fetch_user_info_api_v1_pipixia_app_fetch_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_info_api_v1_pipixia_app_fetch_user_info_get`")  # noqa: E501

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
            '/api/v1/pipixia/app/fetch_user_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户作品列表/Get user post list  # noqa: E501

        # [中文] ### 用途: - 获取用户作品列表，如视频、图文等。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 - feed_count: 翻页数量，默认为0，后续每次翻页加1，比如第一页为0，第二页为1，第三页为2，以此类推。 ### 返回: - 用户作品列表  # [English] ### Purpose: - Get user post list, such as videos, photos, etc. ### Parameters: - user_id: AKA user id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. - feed_count: Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. ### Return: - User post list  # [示例/Example] user_id = \"1310254082831248\" cursor = \"0\" feed_count = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id (required)
        :param object cursor: 翻页游标/Page cursor
        :param object feed_count: 翻页数量/Page count
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户作品列表/Get user post list  # noqa: E501

        # [中文] ### 用途: - 获取用户作品列表，如视频、图文等。 ### 参数: - user_id: 用户id，可以从分享链接中获取。 - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。 - feed_count: 翻页数量，默认为0，后续每次翻页加1，比如第一页为0，第二页为1，第三页为2，以此类推。 ### 返回: - 用户作品列表  # [English] ### Purpose: - Get user post list, such as videos, photos, etc. ### Parameters: - user_id: AKA user id, can be obtained from the share link. - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. - feed_count: Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. ### Return: - User post list  # [示例/Example] user_id = \"1310254082831248\" cursor = \"0\" feed_count = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id (required)
        :param object cursor: 翻页游标/Page cursor
        :param object feed_count: 翻页数量/Page count
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'cursor', 'feed_count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'feed_count' in params:
            query_params.append(('feed_count', params['feed_count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipixia/app/fetch_user_post_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
