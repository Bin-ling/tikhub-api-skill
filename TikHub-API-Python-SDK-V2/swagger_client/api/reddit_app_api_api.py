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


class RedditAPPAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get(self, subreddit_id, **kwargs):  # noqa: E501
        """检查版块是否静音/Check if Subreddit is Muted  # noqa: E501

        # [中文] ### 用途: - 检查指定Reddit版块是否被当前用户静音 ### 参数: - subreddit_id: 版块ID,格式为\"t5_\"开头,可从fetch_subreddit_info接口获取 ### 返回: - 静音状态JSON数据,包含:   - isMuted: 是否静音的布尔值   - subredditId: 版块ID ### 注意: - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 版块ID前缀: t5_ (例如: t5_2qh0u)  # [English] ### Purpose: - Check if a specified Reddit subreddit is muted by the current user ### Parameters: - subreddit_id: Subreddit ID starting with \"t5_\", can be obtained from fetch_subreddit_info endpoint ### Returns: - JSON data of mute status containing:   - isMuted: Boolean value indicating if muted   - subredditId: Subreddit ID ### Note: - **APP API ID format differs from Web API, requires type prefix** - Subreddit ID prefix: t5_ (e.g., t5_2qh0u)  # [示例/Example] subreddit_id=\"t5_2qh0u\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get(subreddit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_id: 版块ID/Subreddit ID (format: t5_xxxxx) (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get_with_http_info(subreddit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get_with_http_info(subreddit_id, **kwargs)  # noqa: E501
            return data

    def check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get_with_http_info(self, subreddit_id, **kwargs):  # noqa: E501
        """检查版块是否静音/Check if Subreddit is Muted  # noqa: E501

        # [中文] ### 用途: - 检查指定Reddit版块是否被当前用户静音 ### 参数: - subreddit_id: 版块ID,格式为\"t5_\"开头,可从fetch_subreddit_info接口获取 ### 返回: - 静音状态JSON数据,包含:   - isMuted: 是否静音的布尔值   - subredditId: 版块ID ### 注意: - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 版块ID前缀: t5_ (例如: t5_2qh0u)  # [English] ### Purpose: - Check if a specified Reddit subreddit is muted by the current user ### Parameters: - subreddit_id: Subreddit ID starting with \"t5_\", can be obtained from fetch_subreddit_info endpoint ### Returns: - JSON data of mute status containing:   - isMuted: Boolean value indicating if muted   - subredditId: Subreddit ID ### Note: - **APP API ID format differs from Web API, requires type prefix** - Subreddit ID prefix: t5_ (e.g., t5_2qh0u)  # [示例/Example] subreddit_id=\"t5_2qh0u\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get_with_http_info(subreddit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_id: 版块ID/Subreddit ID (format: t5_xxxxx) (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subreddit_id', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subreddit_id' is set
        if self.api_client.client_side_validation and ('subreddit_id' not in params or
                                                       params['subreddit_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subreddit_id` when calling `check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subreddit_id' in params:
            query_params.append(('subreddit_id', params['subreddit_id']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/check_subreddit_muted', 'GET',
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

    def fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get(self, post_id, cursor, **kwargs):  # noqa: E501
        """获取Reddit APP评论回复（二级评论）/Fetch Reddit APP Comment Replies (Sub-comments)  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定评论下的回复（二级评论/子评论） - 当评论节点有 more.cursor 字段时，使用此接口获取该评论的子评论 ### 参数: - post_id: 帖子ID，格式如 \"t3_XXXXXX\" - cursor: 评论游标，从评论数据的 more.cursor 字段获取，格式如 \"commenttree:ex:(xxx)\" - sort_type: 排序方式，支持CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM ### 返回: - 指定评论下的回复JSON数据，包含：   - 子评论列表   - 每个子评论的详细信息（内容、作者、点赞数等）   - 分页信息 ### 使用步骤: 1. 先调用 fetch_post_comments 获取帖子的一级评论 2. 在返回数据中找到有子评论的节点（childCount > 0） 3. 获取该节点的 more.cursor 值 4. 使用该 cursor 调用本接口获取子评论 ### 注意: - cursor 值来自评论数据的 more.cursor 字段 - 路径示例: $.data.postInfoById.commentForest.trees[*].more.cursor - cursor 格式类似: \"commenttree:ex:(RjiJd\"  # [English] ### Purpose: - Fetch replies (sub-comments/second-level comments) under a specified Reddit APP comment - Use this endpoint when a comment node has more.cursor field to get its sub-comments ### Parameters: - post_id: Post ID, format like \"t3_XXXXXX\" - cursor: Comment cursor from the more.cursor field in comment data, format like \"commenttree:ex:(xxx)\" - sort_type: Sort method, supports CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM ### Returns: - JSON data of replies under the specified comment, containing:   - List of sub-comments   - Detailed information for each sub-comment (content, author, upvotes, etc.)   - Pagination information ### Usage Steps: 1. First call fetch_post_comments to get top-level comments 2. Find comment nodes with sub-comments (childCount > 0) 3. Get the more.cursor value from that node 4. Use that cursor to call this endpoint to fetch sub-comments ### Note: - cursor value comes from the more.cursor field in comment data - Path example: $.data.postInfoById.commentForest.trees[*].more.cursor - cursor format example: \"commenttree:ex:(RjiJd\"  # [示例/Example] post_id=\"t3_1qmup73\" cursor=\"commenttree:ex:(RjiJd\" sort_type=\"CONFIDENCE\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get(post_id, cursor, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (e.g., t3_1qmup73) (required)
        :param object cursor: 评论游标/Comment cursor from more.cursor field (e.g., commenttree:ex:(RjiJd) (required)
        :param object sort_type: 排序方式/Sort method: CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get_with_http_info(post_id, cursor, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get_with_http_info(post_id, cursor, **kwargs)  # noqa: E501
            return data

    def fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get_with_http_info(self, post_id, cursor, **kwargs):  # noqa: E501
        """获取Reddit APP评论回复（二级评论）/Fetch Reddit APP Comment Replies (Sub-comments)  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定评论下的回复（二级评论/子评论） - 当评论节点有 more.cursor 字段时，使用此接口获取该评论的子评论 ### 参数: - post_id: 帖子ID，格式如 \"t3_XXXXXX\" - cursor: 评论游标，从评论数据的 more.cursor 字段获取，格式如 \"commenttree:ex:(xxx)\" - sort_type: 排序方式，支持CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM ### 返回: - 指定评论下的回复JSON数据，包含：   - 子评论列表   - 每个子评论的详细信息（内容、作者、点赞数等）   - 分页信息 ### 使用步骤: 1. 先调用 fetch_post_comments 获取帖子的一级评论 2. 在返回数据中找到有子评论的节点（childCount > 0） 3. 获取该节点的 more.cursor 值 4. 使用该 cursor 调用本接口获取子评论 ### 注意: - cursor 值来自评论数据的 more.cursor 字段 - 路径示例: $.data.postInfoById.commentForest.trees[*].more.cursor - cursor 格式类似: \"commenttree:ex:(RjiJd\"  # [English] ### Purpose: - Fetch replies (sub-comments/second-level comments) under a specified Reddit APP comment - Use this endpoint when a comment node has more.cursor field to get its sub-comments ### Parameters: - post_id: Post ID, format like \"t3_XXXXXX\" - cursor: Comment cursor from the more.cursor field in comment data, format like \"commenttree:ex:(xxx)\" - sort_type: Sort method, supports CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM ### Returns: - JSON data of replies under the specified comment, containing:   - List of sub-comments   - Detailed information for each sub-comment (content, author, upvotes, etc.)   - Pagination information ### Usage Steps: 1. First call fetch_post_comments to get top-level comments 2. Find comment nodes with sub-comments (childCount > 0) 3. Get the more.cursor value from that node 4. Use that cursor to call this endpoint to fetch sub-comments ### Note: - cursor value comes from the more.cursor field in comment data - Path example: $.data.postInfoById.commentForest.trees[*].more.cursor - cursor format example: \"commenttree:ex:(RjiJd\"  # [示例/Example] post_id=\"t3_1qmup73\" cursor=\"commenttree:ex:(RjiJd\" sort_type=\"CONFIDENCE\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get_with_http_info(post_id, cursor, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (e.g., t3_1qmup73) (required)
        :param object cursor: 评论游标/Comment cursor from more.cursor field (e.g., commenttree:ex:(RjiJd) (required)
        :param object sort_type: 排序方式/Sort method: CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id', 'cursor', 'sort_type', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_id' is set
        if self.api_client.client_side_validation and ('post_id' not in params or
                                                       params['post_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_id` when calling `fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get`")  # noqa: E501
        # verify the required parameter 'cursor' is set
        if self.api_client.client_side_validation and ('cursor' not in params or
                                                       params['cursor'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cursor` when calling `fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_comment_replies', 'GET',
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

    def fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get(self, subreddit_id, **kwargs):  # noqa: E501
        """获取Reddit APP社区亮点/Fetch Reddit APP Community Highlights  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定社区的精选亮点内容,包括热门帖子和重要公告 ### 参数: - subreddit_id: 版块ID,格式为\"t5_\"开头,可从fetch_subreddit_info接口获取 ### 返回: - 社区亮点JSON数据,包含:   - 精选帖子列表   - 置顶公告   - 社区重要动态   - 推荐内容 ### 注意: - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 版块ID前缀: t5_ (例如: t5_2qh0u)  # [English] ### Purpose: - Fetch featured highlight content of a specified Reddit APP community, including popular posts and important announcements ### Parameters: - subreddit_id: Subreddit ID starting with \"t5_\", can be obtained from fetch_subreddit_info endpoint ### Returns: - JSON data of community highlights containing:   - Featured post list   - Pinned announcements   - Important community updates   - Recommended content ### Note: - **APP API ID format differs from Web API, requires type prefix** - Subreddit ID prefix: t5_ (e.g., t5_2qh0u)  # [示例/Example] subreddit_id=\"t5_2qh0u\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get(subreddit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_id: 版块ID/Subreddit ID (format: t5_xxxxx) (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get_with_http_info(subreddit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get_with_http_info(subreddit_id, **kwargs)  # noqa: E501
            return data

    def fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get_with_http_info(self, subreddit_id, **kwargs):  # noqa: E501
        """获取Reddit APP社区亮点/Fetch Reddit APP Community Highlights  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定社区的精选亮点内容,包括热门帖子和重要公告 ### 参数: - subreddit_id: 版块ID,格式为\"t5_\"开头,可从fetch_subreddit_info接口获取 ### 返回: - 社区亮点JSON数据,包含:   - 精选帖子列表   - 置顶公告   - 社区重要动态   - 推荐内容 ### 注意: - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 版块ID前缀: t5_ (例如: t5_2qh0u)  # [English] ### Purpose: - Fetch featured highlight content of a specified Reddit APP community, including popular posts and important announcements ### Parameters: - subreddit_id: Subreddit ID starting with \"t5_\", can be obtained from fetch_subreddit_info endpoint ### Returns: - JSON data of community highlights containing:   - Featured post list   - Pinned announcements   - Important community updates   - Recommended content ### Note: - **APP API ID format differs from Web API, requires type prefix** - Subreddit ID prefix: t5_ (e.g., t5_2qh0u)  # [示例/Example] subreddit_id=\"t5_2qh0u\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get_with_http_info(subreddit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_id: 版块ID/Subreddit ID (format: t5_xxxxx) (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subreddit_id', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subreddit_id' is set
        if self.api_client.client_side_validation and ('subreddit_id' not in params or
                                                       params['subreddit_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subreddit_id` when calling `fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subreddit_id' in params:
            query_params.append(('subreddit_id', params['subreddit_id']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_community_highlights', 'GET',
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

    def fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get(self, query, **kwargs):  # noqa: E501
        """获取Reddit APP动态搜索结果/Fetch Reddit APP Dynamic Search Results  # noqa: E501

        # [中文] ### 用途: - 执行Reddit APP动态搜索,支持搜索帖子、社区、评论、媒体和用户 ### 参数: - query: 搜索关键词 - search_type: 搜索类型,可选值:   - post: 搜索帖子(默认)   - community: 搜索社区/版块   - comment: 搜索评论   - media: 搜索媒体(图片/视频/GIF)   - people: 搜索用户 - sort: 排序方式(仅适用于post/comment/media类型),可选值:   - RELEVANCE: 相关性   - HOT: 热门   - TOP: 最受欢迎   - NEW: 最新   - COMMENTS: 评论数(仅适用于post类型) - time_range: 时间范围(仅适用于post/media类型),可选值:   - all: 所有时间   - year: 去年   - month: 上个月   - week: 上周   - day: 今天   - hour: 过去1小时 - safe_search: 安全搜索设置,\"unset\"或\"strict\" - allow_nsfw: 是否允许NSFW内容,\"0\"或\"1\" - after: 分页参数,用于获取下一页结果 ### 返回: - 搜索结果JSON数据,包含:   - 匹配的结果列表(根据search_type不同返回不同类型的数据)   - 分页信息 ### 注意: - community和people类型不支持sort和time_range参数 - COMMENTS排序方式仅适用于post类型 - time_range参数仅适用于post和media类型  # [English] ### Purpose: - Perform Reddit APP dynamic search, supporting posts, communities, comments, media, and users ### Parameters: - query: Search keyword - search_type: Search type, options:   - post: Search posts (default)   - community: Search communities/subreddits   - comment: Search comments   - media: Search media (images/videos/GIFs)   - people: Search users - sort: Sort method (only for post/comment/media types), options:   - RELEVANCE: By relevance   - HOT: Hot/trending   - TOP: Most popular   - NEW: Newest   - COMMENTS: By comment count (only for post type) - time_range: Time range (only for post/media types), options:   - all: All time   - year: Past year   - month: Past month   - week: Past week   - day: Today   - hour: Past hour - safe_search: Safe search setting, \"unset\" or \"strict\" - allow_nsfw: Allow NSFW content, \"0\" or \"1\" - after: Pagination parameter for fetching next page ### Returns: - JSON data of search results containing:   - List of matching results (different data types based on search_type)   - Pagination information ### Notes: - community and people types do not support sort and time_range parameters - COMMENTS sort option only applies to post type - time_range parameter only applies to post and media types  # [示例/Example] query=\"python programming\" search_type=\"post\" sort=\"RELEVANCE\" time_range=\"all\" safe_search=\"unset\" allow_nsfw=\"0\" after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search query (required)
        :param object search_type: 搜索类型/Search type: post(帖子), community(社区), comment(评论), media(媒体), people(用户)
        :param object sort: 排序方式(仅适用于post/comment/media)/Sort method (only for post/comment/media): RELEVANCE(相关性), HOT(热门), TOP(最受欢迎), NEW(最新), COMMENTS(评论数,仅post)
        :param object time_range: 时间范围(仅适用于post/media)/Time range (only for post/media): all(所有时间), year(去年), month(上月), week(上周), day(今天), hour(过去1小时)
        :param object safe_search: 安全搜索设置/Safe search setting: unset, strict
        :param object allow_nsfw: 是否允许NSFW内容/Allow NSFW content: 0, 1
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """获取Reddit APP动态搜索结果/Fetch Reddit APP Dynamic Search Results  # noqa: E501

        # [中文] ### 用途: - 执行Reddit APP动态搜索,支持搜索帖子、社区、评论、媒体和用户 ### 参数: - query: 搜索关键词 - search_type: 搜索类型,可选值:   - post: 搜索帖子(默认)   - community: 搜索社区/版块   - comment: 搜索评论   - media: 搜索媒体(图片/视频/GIF)   - people: 搜索用户 - sort: 排序方式(仅适用于post/comment/media类型),可选值:   - RELEVANCE: 相关性   - HOT: 热门   - TOP: 最受欢迎   - NEW: 最新   - COMMENTS: 评论数(仅适用于post类型) - time_range: 时间范围(仅适用于post/media类型),可选值:   - all: 所有时间   - year: 去年   - month: 上个月   - week: 上周   - day: 今天   - hour: 过去1小时 - safe_search: 安全搜索设置,\"unset\"或\"strict\" - allow_nsfw: 是否允许NSFW内容,\"0\"或\"1\" - after: 分页参数,用于获取下一页结果 ### 返回: - 搜索结果JSON数据,包含:   - 匹配的结果列表(根据search_type不同返回不同类型的数据)   - 分页信息 ### 注意: - community和people类型不支持sort和time_range参数 - COMMENTS排序方式仅适用于post类型 - time_range参数仅适用于post和media类型  # [English] ### Purpose: - Perform Reddit APP dynamic search, supporting posts, communities, comments, media, and users ### Parameters: - query: Search keyword - search_type: Search type, options:   - post: Search posts (default)   - community: Search communities/subreddits   - comment: Search comments   - media: Search media (images/videos/GIFs)   - people: Search users - sort: Sort method (only for post/comment/media types), options:   - RELEVANCE: By relevance   - HOT: Hot/trending   - TOP: Most popular   - NEW: Newest   - COMMENTS: By comment count (only for post type) - time_range: Time range (only for post/media types), options:   - all: All time   - year: Past year   - month: Past month   - week: Past week   - day: Today   - hour: Past hour - safe_search: Safe search setting, \"unset\" or \"strict\" - allow_nsfw: Allow NSFW content, \"0\" or \"1\" - after: Pagination parameter for fetching next page ### Returns: - JSON data of search results containing:   - List of matching results (different data types based on search_type)   - Pagination information ### Notes: - community and people types do not support sort and time_range parameters - COMMENTS sort option only applies to post type - time_range parameter only applies to post and media types  # [示例/Example] query=\"python programming\" search_type=\"post\" sort=\"RELEVANCE\" time_range=\"all\" safe_search=\"unset\" allow_nsfw=\"0\" after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search query (required)
        :param object search_type: 搜索类型/Search type: post(帖子), community(社区), comment(评论), media(媒体), people(用户)
        :param object sort: 排序方式(仅适用于post/comment/media)/Sort method (only for post/comment/media): RELEVANCE(相关性), HOT(热门), TOP(最受欢迎), NEW(最新), COMMENTS(评论数,仅post)
        :param object time_range: 时间范围(仅适用于post/media)/Time range (only for post/media): all(所有时间), year(去年), month(上月), week(上周), day(今天), hour(过去1小时)
        :param object safe_search: 安全搜索设置/Safe search setting: unset, strict
        :param object allow_nsfw: 是否允许NSFW内容/Allow NSFW content: 0, 1
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'search_type', 'sort', 'time_range', 'safe_search', 'allow_nsfw', 'after', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'search_type' in params:
            query_params.append(('search_type', params['search_type']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'time_range' in params:
            query_params.append(('time_range', params['time_range']))  # noqa: E501
        if 'safe_search' in params:
            query_params.append(('safe_search', params['safe_search']))  # noqa: E501
        if 'allow_nsfw' in params:
            query_params.append(('allow_nsfw', params['allow_nsfw']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_dynamic_search', 'GET',
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

    def fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get(self, **kwargs):  # noqa: E501
        """获取Reddit APP游戏推荐内容/Fetch Reddit APP Games Feed  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP游戏相关的推荐内容,展示游戏社区的热门帖子 ### 参数: - sort: 排序方式,可选: NEW(最新), HOT(热门), TOP(顶级), RISING(上升中) - time: 时间范围,可选: ALL(全部时间), HOUR(一小时), DAY(一天), WEEK(一周), MONTH(一个月), YEAR(一年) - after: 分页参数,获取下一页时使用 ### 返回: - 游戏推荐内容JSON数据,包含:   - 游戏相关帖子列表   - 游戏社区讨论   - 游戏新闻和更新  # [English] ### Purpose: - Fetch gaming-related recommended content on Reddit APP, displaying popular posts from gaming communities ### Parameters: - sort: Sort method, options: NEW, HOT, TOP, RISING - time: Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR - after: Pagination parameter for fetching next page ### Returns: - JSON data of games feed containing:   - List of gaming-related posts   - Gaming community discussions   - Game news and updates  # [示例/Example] sort=\"HOT\" time=\"WEEK\" after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sort: 排序方式/Sort method: NEW, HOT, TOP, RISING
        :param object time: 时间范围/Time range: ALL, HOUR, DAY, WEEK, MONTH, YEAR
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取Reddit APP游戏推荐内容/Fetch Reddit APP Games Feed  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP游戏相关的推荐内容,展示游戏社区的热门帖子 ### 参数: - sort: 排序方式,可选: NEW(最新), HOT(热门), TOP(顶级), RISING(上升中) - time: 时间范围,可选: ALL(全部时间), HOUR(一小时), DAY(一天), WEEK(一周), MONTH(一个月), YEAR(一年) - after: 分页参数,获取下一页时使用 ### 返回: - 游戏推荐内容JSON数据,包含:   - 游戏相关帖子列表   - 游戏社区讨论   - 游戏新闻和更新  # [English] ### Purpose: - Fetch gaming-related recommended content on Reddit APP, displaying popular posts from gaming communities ### Parameters: - sort: Sort method, options: NEW, HOT, TOP, RISING - time: Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR - after: Pagination parameter for fetching next page ### Returns: - JSON data of games feed containing:   - List of gaming-related posts   - Gaming community discussions   - Game news and updates  # [示例/Example] sort=\"HOT\" time=\"WEEK\" after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sort: 排序方式/Sort method: NEW, HOT, TOP, RISING
        :param object time: 时间范围/Time range: ALL, HOUR, DAY, WEEK, MONTH, YEAR
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'time', 'after', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'time' in params:
            query_params.append(('time', params['time']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_games_feed', 'GET',
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

    def fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get(self, **kwargs):  # noqa: E501
        """获取Reddit APP首页推荐内容/Fetch Reddit APP Home Feed  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP首页推荐内容 ### 参数: - sort: 排序方式，支持HOT, NEW, TOP, BEST, CONTROVERSIAL - filter_posts: 过滤掉指定的帖子ID列表，用于排除已获取的帖子，避免重复获取 - after: 分页参数，获取下一页时使用 ### 返回: - Reddit APP首页推荐内容的JSON数据  # [English] ### Purpose: - Fetch Reddit APP home feed content ### Parameters: - sort: Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL - filter_posts: List of post IDs to filter out, used to exclude already fetched posts - after: Pagination parameter for fetching the next page ### Returns: - JSON data of Reddit APP home feed content  # [示例/Example] sort=\"BEST\"  filter_posts=[\"t3_1ojjquz\",\"t3_1ohepm2\",\"t3_1ojxzzz\",\"t3_1ojnvca\",\"t3_1oj9dcb\",\"t3_1ojxubp\",\"t3_1oj5x2b\"]  after=\"dDNfMW9qNXgyYg==\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sort: 排序方式/Sort method: HOT, NEW, TOP, BEST, CONTROVERSIAL
        :param object filter_posts: 过滤掉指定的帖子ID列表/Filter out specified post IDs
        :param object after: 分页参数/Pagination parameter for fetching next page
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取Reddit APP首页推荐内容/Fetch Reddit APP Home Feed  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP首页推荐内容 ### 参数: - sort: 排序方式，支持HOT, NEW, TOP, BEST, CONTROVERSIAL - filter_posts: 过滤掉指定的帖子ID列表，用于排除已获取的帖子，避免重复获取 - after: 分页参数，获取下一页时使用 ### 返回: - Reddit APP首页推荐内容的JSON数据  # [English] ### Purpose: - Fetch Reddit APP home feed content ### Parameters: - sort: Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL - filter_posts: List of post IDs to filter out, used to exclude already fetched posts - after: Pagination parameter for fetching the next page ### Returns: - JSON data of Reddit APP home feed content  # [示例/Example] sort=\"BEST\"  filter_posts=[\"t3_1ojjquz\",\"t3_1ohepm2\",\"t3_1ojxzzz\",\"t3_1ojnvca\",\"t3_1oj9dcb\",\"t3_1ojxubp\",\"t3_1oj5x2b\"]  after=\"dDNfMW9qNXgyYg==\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sort: 排序方式/Sort method: HOT, NEW, TOP, BEST, CONTROVERSIAL
        :param object filter_posts: 过滤掉指定的帖子ID列表/Filter out specified post IDs
        :param object after: 分页参数/Pagination parameter for fetching next page
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'filter_posts', 'after', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'filter_posts' in params:
            query_params.append(('filter_posts', params['filter_posts']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_home_feed', 'GET',
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

    def fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get(self, **kwargs):  # noqa: E501
        """获取Reddit APP资讯推荐内容/Fetch Reddit APP News Feed  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP新闻资讯推荐内容,展示最新的新闻和时事讨论 ### 参数: - subtopic_ids: 子话题ID列表,默认[\"all\"]表示所有新闻类别 - after: 分页参数,获取下一页时使用 ### 返回: - 新闻推荐内容JSON数据,包含:   - 新闻帖子列表   - 时事讨论   - 热点话题   - 新闻来源和链接  # [English] ### Purpose: - Fetch news-related recommended content on Reddit APP, displaying latest news and current affairs discussions ### Parameters: - subtopic_ids: List of subtopic IDs, default [\"all\"] means all news categories - after: Pagination parameter for fetching next page ### Returns: - JSON data of news feed containing:   - List of news posts   - Current affairs discussions   - Trending topics   - News sources and links  # [示例/Example] subtopic_ids=[\"all\"] after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subtopic_ids: 子话题ID列表/Subtopic IDs list
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取Reddit APP资讯推荐内容/Fetch Reddit APP News Feed  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP新闻资讯推荐内容,展示最新的新闻和时事讨论 ### 参数: - subtopic_ids: 子话题ID列表,默认[\"all\"]表示所有新闻类别 - after: 分页参数,获取下一页时使用 ### 返回: - 新闻推荐内容JSON数据,包含:   - 新闻帖子列表   - 时事讨论   - 热点话题   - 新闻来源和链接  # [English] ### Purpose: - Fetch news-related recommended content on Reddit APP, displaying latest news and current affairs discussions ### Parameters: - subtopic_ids: List of subtopic IDs, default [\"all\"] means all news categories - after: Pagination parameter for fetching next page ### Returns: - JSON data of news feed containing:   - List of news posts   - Current affairs discussions   - Trending topics   - News sources and links  # [示例/Example] subtopic_ids=[\"all\"] after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subtopic_ids: 子话题ID列表/Subtopic IDs list
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subtopic_ids', 'after', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subtopic_ids' in params:
            query_params.append(('subtopic_ids', params['subtopic_ids']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_news_feed', 'GET',
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

    def fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get(self, **kwargs):  # noqa: E501
        """获取Reddit APP流行推荐内容/Fetch Reddit APP Popular Feed  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP流行/热门推荐内容,展示全站最受欢迎的帖子 ### 参数: - sort: 排序方式,可选: BEST(最佳), HOT(热门), NEW(最新), TOP(顶级), CONTROVERSIAL(有争议), RISING(上升中) - time: 时间范围,可选: ALL(全部时间), HOUR(一小时), DAY(一天), WEEK(一周), MONTH(一个月), YEAR(一年) - filter_posts: 过滤掉指定的帖子ID列表,用于避免重复获取 - after: 分页参数,获取下一页时使用 ### 返回: - 流行推荐内容JSON数据,包含:   - 热门帖子列表   - 帖子详细信息(标题、内容、点赞数、评论数等)   - 分页信息(after参数用于下一页)  # [English] ### Purpose: - Fetch popular/trending recommended content on Reddit APP, displaying the most popular posts site-wide ### Parameters: - sort: Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING - time: Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR - filter_posts: List of post IDs to filter out, used to avoid duplicate fetches - after: Pagination parameter for fetching next page ### Returns: - JSON data of popular feed containing:   - List of trending posts   - Detailed post information (title, content, upvotes, comments, etc.)   - Pagination information (after parameter for next page)  # [示例/Example] sort=\"HOT\" time=\"DAY\" filter_posts=[] after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sort: 排序方式/Sort method: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING
        :param object time: 时间范围/Time range: ALL, HOUR, DAY, WEEK, MONTH, YEAR
        :param object filter_posts: 过滤帖子ID列表/Filter post IDs
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取Reddit APP流行推荐内容/Fetch Reddit APP Popular Feed  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP流行/热门推荐内容,展示全站最受欢迎的帖子 ### 参数: - sort: 排序方式,可选: BEST(最佳), HOT(热门), NEW(最新), TOP(顶级), CONTROVERSIAL(有争议), RISING(上升中) - time: 时间范围,可选: ALL(全部时间), HOUR(一小时), DAY(一天), WEEK(一周), MONTH(一个月), YEAR(一年) - filter_posts: 过滤掉指定的帖子ID列表,用于避免重复获取 - after: 分页参数,获取下一页时使用 ### 返回: - 流行推荐内容JSON数据,包含:   - 热门帖子列表   - 帖子详细信息(标题、内容、点赞数、评论数等)   - 分页信息(after参数用于下一页)  # [English] ### Purpose: - Fetch popular/trending recommended content on Reddit APP, displaying the most popular posts site-wide ### Parameters: - sort: Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING - time: Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR - filter_posts: List of post IDs to filter out, used to avoid duplicate fetches - after: Pagination parameter for fetching next page ### Returns: - JSON data of popular feed containing:   - List of trending posts   - Detailed post information (title, content, upvotes, comments, etc.)   - Pagination information (after parameter for next page)  # [示例/Example] sort=\"HOT\" time=\"DAY\" filter_posts=[] after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sort: 排序方式/Sort method: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING
        :param object time: 时间范围/Time range: ALL, HOUR, DAY, WEEK, MONTH, YEAR
        :param object filter_posts: 过滤帖子ID列表/Filter post IDs
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'time', 'filter_posts', 'after', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'time' in params:
            query_params.append(('time', params['time']))  # noqa: E501
        if 'filter_posts' in params:
            query_params.append(('filter_posts', params['filter_posts']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_popular_feed', 'GET',
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

    def fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get(self, post_id, **kwargs):  # noqa: E501
        """获取Reddit APP帖子评论/Fetch Reddit APP Post Comments  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定帖子下的评论 ### 参数: - post_id: 帖子ID，格式如 \"t3_XXXXXX\" - sort_type: 排序方式，支持CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM - after: 分页参数，获取下一页时使用，在commentForest里的最后一个评论节点中可以找到，例如$.data.postInfoById.commentForest.trees[-1].more.cursor ### 返回: - 指定帖子下的评论JSON数据 ### 注意: - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 帖子ID前缀: t3_ (例如: t3_1ojnvca)  # [English] ### Purpose: - Fetch comments under a specified Reddit APP post ### Parameters: - post_id: Post ID, format like \"t3_XXXXXX\" - sort_type: Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL - after: Pagination parameter for fetching the next page, can be found in the last comment node in commentForest, e.g., $.data.postInfoById.commentForest.trees[-1].more.cursor ### Returns: - JSON data of comments under the specified post ### Note: - **APP API ID format differs from Web API, requires type prefix** - Post ID prefix: t3_ (e.g., t3_1ojnvca)  # [示例/Example] post_id=\"t3_1ojnvca\"  sort=\"CONFIDENCE\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (required)
        :param object sort_type: 排序方式/Sort method: CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM
        :param object after: 分页参数/Pagination parameter for fetching next page
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get_with_http_info(post_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get_with_http_info(post_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get_with_http_info(self, post_id, **kwargs):  # noqa: E501
        """获取Reddit APP帖子评论/Fetch Reddit APP Post Comments  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定帖子下的评论 ### 参数: - post_id: 帖子ID，格式如 \"t3_XXXXXX\" - sort_type: 排序方式，支持CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM - after: 分页参数，获取下一页时使用，在commentForest里的最后一个评论节点中可以找到，例如$.data.postInfoById.commentForest.trees[-1].more.cursor ### 返回: - 指定帖子下的评论JSON数据 ### 注意: - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 帖子ID前缀: t3_ (例如: t3_1ojnvca)  # [English] ### Purpose: - Fetch comments under a specified Reddit APP post ### Parameters: - post_id: Post ID, format like \"t3_XXXXXX\" - sort_type: Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL - after: Pagination parameter for fetching the next page, can be found in the last comment node in commentForest, e.g., $.data.postInfoById.commentForest.trees[-1].more.cursor ### Returns: - JSON data of comments under the specified post ### Note: - **APP API ID format differs from Web API, requires type prefix** - Post ID prefix: t3_ (e.g., t3_1ojnvca)  # [示例/Example] post_id=\"t3_1ojnvca\"  sort=\"CONFIDENCE\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get_with_http_info(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (required)
        :param object sort_type: 排序方式/Sort method: CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM
        :param object after: 分页参数/Pagination parameter for fetching next page
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id', 'sort_type', 'after', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_id' is set
        if self.api_client.client_side_validation and ('post_id' not in params or
                                                       params['post_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_id` when calling `fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_post_comments', 'GET',
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

    def fetch_post_details_api_v1_reddit_app_fetch_post_details_get(self, post_id, **kwargs):  # noqa: E501
        """获取单个Reddit帖子详情/Fetch Single Reddit Post Details  # noqa: E501

        # [中文] ## 用途: - 根据帖子ID获取单个帖子详情 - 可选择性包含特定评论的上下文  ## 参数: - post_id: 帖子ID，格式如 \"t3_XXXXXX\" - include_comment_id: 是否包含特定评论ID，默认False - comment_id: 评论ID（当include_comment_id为True时使用），格式如 \"t1_XXXXXX\"  ## 返回: - 包含帖子详细信息的数据，包括:   - 帖子内容、标题、作者   - 统计数据（点赞数、评论数等）   - 版块信息   - 奖励信息   - 媒体资源   - 推荐原因等  ## 注意: - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 帖子ID前缀: t3_ (例如: t3_1ojnh50) - 评论ID前缀: t1_ (例如: t1_abcd123)  ---  # [English] ## Purpose: - Fetch single post details by post ID - Optionally include context for specific comments  ## Parameters: - post_id: Post ID, format like \"t3_XXXXXX\" - include_comment_id: Whether to include specific comment ID, default False - comment_id: Comment ID (used when include_comment_id is True), format like \"t1_XXXXXX\"  ## Returns: - Data containing detailed post information including:   - Post content, title, author   - Statistics (upvotes, comment count, etc.)   - Subreddit information   - Award information   - Media resources   - Recommendation reasons, etc.  ## Note: - **APP API ID format differs from Web API, requires type prefix** - Post ID prefix: t3_ (e.g., t3_1ojnh50) - Comment ID prefix: t1_ (e.g., t1_abcd123)  # [示例/Example] post_id=\"t3_1ojnh50\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_details_api_v1_reddit_app_fetch_post_details_get(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (e.g., t3_1ojnh50) (required)
        :param object include_comment_id: 是否包含特定评论ID/Include specific comment ID
        :param object comment_id: 评论ID/Comment ID (when include_comment_id is True)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_details_api_v1_reddit_app_fetch_post_details_get_with_http_info(post_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_details_api_v1_reddit_app_fetch_post_details_get_with_http_info(post_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_details_api_v1_reddit_app_fetch_post_details_get_with_http_info(self, post_id, **kwargs):  # noqa: E501
        """获取单个Reddit帖子详情/Fetch Single Reddit Post Details  # noqa: E501

        # [中文] ## 用途: - 根据帖子ID获取单个帖子详情 - 可选择性包含特定评论的上下文  ## 参数: - post_id: 帖子ID，格式如 \"t3_XXXXXX\" - include_comment_id: 是否包含特定评论ID，默认False - comment_id: 评论ID（当include_comment_id为True时使用），格式如 \"t1_XXXXXX\"  ## 返回: - 包含帖子详细信息的数据，包括:   - 帖子内容、标题、作者   - 统计数据（点赞数、评论数等）   - 版块信息   - 奖励信息   - 媒体资源   - 推荐原因等  ## 注意: - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 帖子ID前缀: t3_ (例如: t3_1ojnh50) - 评论ID前缀: t1_ (例如: t1_abcd123)  ---  # [English] ## Purpose: - Fetch single post details by post ID - Optionally include context for specific comments  ## Parameters: - post_id: Post ID, format like \"t3_XXXXXX\" - include_comment_id: Whether to include specific comment ID, default False - comment_id: Comment ID (used when include_comment_id is True), format like \"t1_XXXXXX\"  ## Returns: - Data containing detailed post information including:   - Post content, title, author   - Statistics (upvotes, comment count, etc.)   - Subreddit information   - Award information   - Media resources   - Recommendation reasons, etc.  ## Note: - **APP API ID format differs from Web API, requires type prefix** - Post ID prefix: t3_ (e.g., t3_1ojnh50) - Comment ID prefix: t1_ (e.g., t1_abcd123)  # [示例/Example] post_id=\"t3_1ojnh50\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_details_api_v1_reddit_app_fetch_post_details_get_with_http_info(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (e.g., t3_1ojnh50) (required)
        :param object include_comment_id: 是否包含特定评论ID/Include specific comment ID
        :param object comment_id: 评论ID/Comment ID (when include_comment_id is True)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id', 'include_comment_id', 'comment_id', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_details_api_v1_reddit_app_fetch_post_details_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_id' is set
        if self.api_client.client_side_validation and ('post_id' not in params or
                                                       params['post_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_id` when calling `fetch_post_details_api_v1_reddit_app_fetch_post_details_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501
        if 'include_comment_id' in params:
            query_params.append(('include_comment_id', params['include_comment_id']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_post_details', 'GET',
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

    def fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get(self, post_ids, **kwargs):  # noqa: E501
        """批量获取Reddit帖子详情(最多5条)/Fetch Reddit Post Details in Batch (Max 5)  # noqa: E501

        # [中文] ## 用途: - 根据帖子ID列表批量获取帖子详情 - 支持最多5条帖子的批量查询 - 可选择性包含特定评论的上下文  ## 参数: - post_ids: 帖子ID列表，逗号分隔，格式如 \"t3_XXXXXX,t3_YYYYYY\"，最多支持5条 - include_comment_id: 是否包含特定评论ID，默认False - comment_id: 评论ID（当include_comment_id为True时使用），格式如 \"t1_XXXXXX\"  ## 返回: - 包含帖子详细信息的数据，包括:   - 帖子内容、标题、作者   - 统计数据（点赞数、评论数等）   - 版块信息   - 奖励信息   - 媒体资源   - 推荐原因等  ## 注意: - 最多支持5条帖子的批量查询 - 超过5条将返回错误 - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 帖子ID前缀: t3_ (例如: t3_1ojnh50) - 评论ID前缀: t1_ (例如: t1_abcd123)  ---  # [English] ## Purpose: - Fetch post details in batch by post ID list - Support batch query for up to 5 posts - Optionally include context for specific comments  ## Parameters: - post_ids: Post IDs comma-separated, format like \"t3_XXXXXX,t3_YYYYYY\", max 5 posts - include_comment_id: Whether to include specific comment ID, default False - comment_id: Comment ID (used when include_comment_id is True), format like \"t1_XXXXXX\"  ## Returns: - Data containing detailed post information including:   - Post content, title, author   - Statistics (upvotes, comment count, etc.)   - Subreddit information   - Award information   - Media resources   - Recommendation reasons, etc.  ## Notes: - Maximum 5 posts per batch query - Error will be returned if exceeds 5 posts - **APP API ID format differs from Web API, requires type prefix** - Post ID prefix: t3_ (e.g., t3_1ojnh50) - Comment ID prefix: t1_ (e.g., t1_abcd123)  # [示例/Example] post_ids=\"t3_1ojnh50,t3_1ok432f,t3_1nwil8j\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get(post_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_ids: 帖子ID列表，逗号分隔，最多5条/Post IDs comma-separated, max 5 (e.g., t3_1ojnh50,t3_1ok432f) (required)
        :param object include_comment_id: 是否包含特定评论ID/Include specific comment ID
        :param object comment_id: 评论ID/Comment ID (when include_comment_id is True)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get_with_http_info(post_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get_with_http_info(post_ids, **kwargs)  # noqa: E501
            return data

    def fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get_with_http_info(self, post_ids, **kwargs):  # noqa: E501
        """批量获取Reddit帖子详情(最多5条)/Fetch Reddit Post Details in Batch (Max 5)  # noqa: E501

        # [中文] ## 用途: - 根据帖子ID列表批量获取帖子详情 - 支持最多5条帖子的批量查询 - 可选择性包含特定评论的上下文  ## 参数: - post_ids: 帖子ID列表，逗号分隔，格式如 \"t3_XXXXXX,t3_YYYYYY\"，最多支持5条 - include_comment_id: 是否包含特定评论ID，默认False - comment_id: 评论ID（当include_comment_id为True时使用），格式如 \"t1_XXXXXX\"  ## 返回: - 包含帖子详细信息的数据，包括:   - 帖子内容、标题、作者   - 统计数据（点赞数、评论数等）   - 版块信息   - 奖励信息   - 媒体资源   - 推荐原因等  ## 注意: - 最多支持5条帖子的批量查询 - 超过5条将返回错误 - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 帖子ID前缀: t3_ (例如: t3_1ojnh50) - 评论ID前缀: t1_ (例如: t1_abcd123)  ---  # [English] ## Purpose: - Fetch post details in batch by post ID list - Support batch query for up to 5 posts - Optionally include context for specific comments  ## Parameters: - post_ids: Post IDs comma-separated, format like \"t3_XXXXXX,t3_YYYYYY\", max 5 posts - include_comment_id: Whether to include specific comment ID, default False - comment_id: Comment ID (used when include_comment_id is True), format like \"t1_XXXXXX\"  ## Returns: - Data containing detailed post information including:   - Post content, title, author   - Statistics (upvotes, comment count, etc.)   - Subreddit information   - Award information   - Media resources   - Recommendation reasons, etc.  ## Notes: - Maximum 5 posts per batch query - Error will be returned if exceeds 5 posts - **APP API ID format differs from Web API, requires type prefix** - Post ID prefix: t3_ (e.g., t3_1ojnh50) - Comment ID prefix: t1_ (e.g., t1_abcd123)  # [示例/Example] post_ids=\"t3_1ojnh50,t3_1ok432f,t3_1nwil8j\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get_with_http_info(post_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_ids: 帖子ID列表，逗号分隔，最多5条/Post IDs comma-separated, max 5 (e.g., t3_1ojnh50,t3_1ok432f) (required)
        :param object include_comment_id: 是否包含特定评论ID/Include specific comment ID
        :param object comment_id: 评论ID/Comment ID (when include_comment_id is True)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_ids', 'include_comment_id', 'comment_id', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_ids' is set
        if self.api_client.client_side_validation and ('post_ids' not in params or
                                                       params['post_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_ids` when calling `fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_ids' in params:
            query_params.append(('post_ids', params['post_ids']))  # noqa: E501
        if 'include_comment_id' in params:
            query_params.append(('include_comment_id', params['include_comment_id']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_post_details_batch', 'GET',
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

    def fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get(self, post_ids, **kwargs):  # noqa: E501
        """大批量获取Reddit帖子详情(最多30条)/Fetch Reddit Post Details in Large Batch (Max 30)  # noqa: E501

        # [中文] ## 用途: - 根据帖子ID列表大批量获取帖子详情 - 支持最多30条帖子的批量查询 - 可选择性包含特定评论的上下文  ## 参数: - post_ids: 帖子ID列表，逗号分隔，格式如 \"t3_XXXXXX,t3_YYYYYY,...\"，最多支持30条 - include_comment_id: 是否包含特定评论ID，默认False - comment_id: 评论ID（当include_comment_id为True时使用），格式如 \"t1_XXXXXX\"  ## 返回: - 包含帖子详细信息的数据，包括:   - 帖子内容、标题、作者   - 统计数据（点赞数、评论数等）   - 版块信息   - 奖励信息   - 媒体资源   - 推荐原因等  ## 注意: - 最多支持30条帖子的批量查询 - 超过30条将返回错误 - 大批量查询可能需要较长的响应时间 - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 帖子ID前缀: t3_ (例如: t3_1ojnh50) - 评论ID前缀: t1_ (例如: t1_abcd123)  ---  # [English] ## Purpose: - Fetch post details in large batch by post ID list - Support batch query for up to 30 posts - Optionally include context for specific comments  ## Parameters: - post_ids: Post IDs comma-separated, format like \"t3_XXXXXX,t3_YYYYYY,...\", max 30 posts - include_comment_id: Whether to include specific comment ID, default False - comment_id: Comment ID (used when include_comment_id is True), format like \"t1_XXXXXX\"  ## Returns: - Data containing detailed post information including:   - Post content, title, author   - Statistics (upvotes, comment count, etc.)   - Subreddit information   - Award information   - Media resources   - Recommendation reasons, etc.  ## Notes: - Maximum 30 posts per batch query - Error will be returned if exceeds 30 posts - Large batch queries may take longer to respond - **APP API ID format differs from Web API, requires type prefix** - Post ID prefix: t3_ (e.g., t3_1ojnh50) - Comment ID prefix: t1_ (e.g., t1_abcd123)  # [示例/Example] post_ids=\"t3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd,...\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get(post_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_ids: 帖子ID列表，逗号分隔，最多30条/Post IDs comma-separated, max 30 (e.g., t3_1ojnh50,t3_1ok432f,...) (required)
        :param object include_comment_id: 是否包含特定评论ID/Include specific comment ID
        :param object comment_id: 评论ID/Comment ID (when include_comment_id is True)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get_with_http_info(post_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get_with_http_info(post_ids, **kwargs)  # noqa: E501
            return data

    def fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get_with_http_info(self, post_ids, **kwargs):  # noqa: E501
        """大批量获取Reddit帖子详情(最多30条)/Fetch Reddit Post Details in Large Batch (Max 30)  # noqa: E501

        # [中文] ## 用途: - 根据帖子ID列表大批量获取帖子详情 - 支持最多30条帖子的批量查询 - 可选择性包含特定评论的上下文  ## 参数: - post_ids: 帖子ID列表，逗号分隔，格式如 \"t3_XXXXXX,t3_YYYYYY,...\"，最多支持30条 - include_comment_id: 是否包含特定评论ID，默认False - comment_id: 评论ID（当include_comment_id为True时使用），格式如 \"t1_XXXXXX\"  ## 返回: - 包含帖子详细信息的数据，包括:   - 帖子内容、标题、作者   - 统计数据（点赞数、评论数等）   - 版块信息   - 奖励信息   - 媒体资源   - 推荐原因等  ## 注意: - 最多支持30条帖子的批量查询 - 超过30条将返回错误 - 大批量查询可能需要较长的响应时间 - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 帖子ID前缀: t3_ (例如: t3_1ojnh50) - 评论ID前缀: t1_ (例如: t1_abcd123)  ---  # [English] ## Purpose: - Fetch post details in large batch by post ID list - Support batch query for up to 30 posts - Optionally include context for specific comments  ## Parameters: - post_ids: Post IDs comma-separated, format like \"t3_XXXXXX,t3_YYYYYY,...\", max 30 posts - include_comment_id: Whether to include specific comment ID, default False - comment_id: Comment ID (used when include_comment_id is True), format like \"t1_XXXXXX\"  ## Returns: - Data containing detailed post information including:   - Post content, title, author   - Statistics (upvotes, comment count, etc.)   - Subreddit information   - Award information   - Media resources   - Recommendation reasons, etc.  ## Notes: - Maximum 30 posts per batch query - Error will be returned if exceeds 30 posts - Large batch queries may take longer to respond - **APP API ID format differs from Web API, requires type prefix** - Post ID prefix: t3_ (e.g., t3_1ojnh50) - Comment ID prefix: t1_ (e.g., t1_abcd123)  # [示例/Example] post_ids=\"t3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd,...\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get_with_http_info(post_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_ids: 帖子ID列表，逗号分隔，最多30条/Post IDs comma-separated, max 30 (e.g., t3_1ojnh50,t3_1ok432f,...) (required)
        :param object include_comment_id: 是否包含特定评论ID/Include specific comment ID
        :param object comment_id: 评论ID/Comment ID (when include_comment_id is True)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_ids', 'include_comment_id', 'comment_id', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_ids' is set
        if self.api_client.client_side_validation and ('post_ids' not in params or
                                                       params['post_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_ids` when calling `fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_ids' in params:
            query_params.append(('post_ids', params['post_ids']))  # noqa: E501
        if 'include_comment_id' in params:
            query_params.append(('include_comment_id', params['include_comment_id']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_post_details_batch_large', 'GET',
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

    def fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get(self, query, **kwargs):  # noqa: E501
        """获取Reddit APP搜索自动补全建议/Fetch Reddit APP Search Typeahead Suggestions  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP搜索框的自动补全建议,包括推荐的版块、用户和搜索词 ### 参数: - query: 搜索关键词,输入的搜索文本 - safe_search: 安全搜索设置,可选值为\"unset\"(未设置)或\"strict\"(严格模式) - allow_nsfw: 是否允许显示NSFW(成人)内容,\"0\"表示不允许,\"1\"表示允许 ### 返回: - 搜索建议JSON数据,包含以下类型的建议:   - 相关版块(subreddits)   - 相关用户(users)   - 搜索词建议(search suggestions)   - 热门话题(trending topics)  # [English] ### Purpose: - Fetch autocomplete suggestions for the Reddit APP search box, including recommended subreddits, users, and search terms ### Parameters: - query: Search keyword, the search text being typed - safe_search: Safe search setting, options are \"unset\" or \"strict\" - allow_nsfw: Whether to allow NSFW (adult) content display, \"0\" means disallow, \"1\" means allow ### Returns: - JSON data of search suggestions containing the following types:   - Related subreddits   - Related users   - Search term suggestions   - Trending topics  # [示例/Example] query=\"programming\" safe_search=\"unset\" allow_nsfw=\"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search query (required)
        :param object safe_search: 安全搜索设置/Safe search setting: unset, strict
        :param object allow_nsfw: 是否允许NSFW内容/Allow NSFW content: 0 or 1
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """获取Reddit APP搜索自动补全建议/Fetch Reddit APP Search Typeahead Suggestions  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP搜索框的自动补全建议,包括推荐的版块、用户和搜索词 ### 参数: - query: 搜索关键词,输入的搜索文本 - safe_search: 安全搜索设置,可选值为\"unset\"(未设置)或\"strict\"(严格模式) - allow_nsfw: 是否允许显示NSFW(成人)内容,\"0\"表示不允许,\"1\"表示允许 ### 返回: - 搜索建议JSON数据,包含以下类型的建议:   - 相关版块(subreddits)   - 相关用户(users)   - 搜索词建议(search suggestions)   - 热门话题(trending topics)  # [English] ### Purpose: - Fetch autocomplete suggestions for the Reddit APP search box, including recommended subreddits, users, and search terms ### Parameters: - query: Search keyword, the search text being typed - safe_search: Safe search setting, options are \"unset\" or \"strict\" - allow_nsfw: Whether to allow NSFW (adult) content display, \"0\" means disallow, \"1\" means allow ### Returns: - JSON data of search suggestions containing the following types:   - Related subreddits   - Related users   - Search term suggestions   - Trending topics  # [示例/Example] query=\"programming\" safe_search=\"unset\" allow_nsfw=\"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search query (required)
        :param object safe_search: 安全搜索设置/Safe search setting: unset, strict
        :param object allow_nsfw: 是否允许NSFW内容/Allow NSFW content: 0 or 1
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'safe_search', 'allow_nsfw', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'safe_search' in params:
            query_params.append(('safe_search', params['safe_search']))  # noqa: E501
        if 'allow_nsfw' in params:
            query_params.append(('allow_nsfw', params['allow_nsfw']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_search_typeahead', 'GET',
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

    def fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get(self, subreddit_name, **kwargs):  # noqa: E501
        """获取Reddit APP版块Feed内容/Fetch Reddit APP Subreddit Feed  # noqa: E501

        # [中文] ### 用途: - 获取指定Reddit版块的Feed内容流,展示该版块的帖子列表 ### 参数: - subreddit_name: 版块名称(不带r/前缀),如\"pics\", \"funny\"等 - sort: 排序方式,可选: BEST(最佳), HOT(热门), NEW(最新), TOP(顶级), CONTROVERSIAL(有争议), RISING(上升中) - filter_posts: 过滤掉指定的帖子ID列表 - after: 分页参数,获取下一页时使用 ### 返回: - 版块Feed JSON数据,包含:   - 该版块的帖子列表   - 帖子详细信息   - 版块元数据   - 分页信息  # [English] ### Purpose: - Fetch feed content stream of a specified Reddit subreddit, displaying the post list of that subreddit ### Parameters: - subreddit_name: Subreddit name (without r/ prefix), e.g., \"pics\", \"funny\" - sort: Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING - filter_posts: List of post IDs to filter out - after: Pagination parameter for fetching next page ### Returns: - JSON data of subreddit feed containing:   - List of posts in the subreddit   - Detailed post information   - Subreddit metadata   - Pagination information  # [示例/Example] subreddit_name=\"AskReddit\" sort=\"HOT\" filter_posts=[] after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get(subreddit_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_name: 版块名称/Subreddit name (required)
        :param object sort: 排序方式/Sort method: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING
        :param object filter_posts: 过滤帖子ID列表/Filter post IDs
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get_with_http_info(subreddit_name, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get_with_http_info(subreddit_name, **kwargs)  # noqa: E501
            return data

    def fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get_with_http_info(self, subreddit_name, **kwargs):  # noqa: E501
        """获取Reddit APP版块Feed内容/Fetch Reddit APP Subreddit Feed  # noqa: E501

        # [中文] ### 用途: - 获取指定Reddit版块的Feed内容流,展示该版块的帖子列表 ### 参数: - subreddit_name: 版块名称(不带r/前缀),如\"pics\", \"funny\"等 - sort: 排序方式,可选: BEST(最佳), HOT(热门), NEW(最新), TOP(顶级), CONTROVERSIAL(有争议), RISING(上升中) - filter_posts: 过滤掉指定的帖子ID列表 - after: 分页参数,获取下一页时使用 ### 返回: - 版块Feed JSON数据,包含:   - 该版块的帖子列表   - 帖子详细信息   - 版块元数据   - 分页信息  # [English] ### Purpose: - Fetch feed content stream of a specified Reddit subreddit, displaying the post list of that subreddit ### Parameters: - subreddit_name: Subreddit name (without r/ prefix), e.g., \"pics\", \"funny\" - sort: Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING - filter_posts: List of post IDs to filter out - after: Pagination parameter for fetching next page ### Returns: - JSON data of subreddit feed containing:   - List of posts in the subreddit   - Detailed post information   - Subreddit metadata   - Pagination information  # [示例/Example] subreddit_name=\"AskReddit\" sort=\"HOT\" filter_posts=[] after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get_with_http_info(subreddit_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_name: 版块名称/Subreddit name (required)
        :param object sort: 排序方式/Sort method: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING
        :param object filter_posts: 过滤帖子ID列表/Filter post IDs
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subreddit_name', 'sort', 'filter_posts', 'after', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subreddit_name' is set
        if self.api_client.client_side_validation and ('subreddit_name' not in params or
                                                       params['subreddit_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subreddit_name` when calling `fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subreddit_name' in params:
            query_params.append(('subreddit_name', params['subreddit_name']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'filter_posts' in params:
            query_params.append(('filter_posts', params['filter_posts']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_subreddit_feed', 'GET',
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

    def fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get(self, **kwargs):  # noqa: E501
        """获取Reddit APP版块信息/Fetch Reddit APP Subreddit Info  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定版块的详细信息,包括版块描述、成员数量、创建时间、规则等元数据 ### 参数: - subreddit_name: 版块名称(不带r/前缀),例如\"pics\", \"funny\", \"AskReddit\"等 ### 返回: - 指定版块的详细信息JSON数据 # [English] ### Purpose: - Fetch detailed information of a specified Reddit APP subreddit, including description, subscriber count, creation time, rules, and other metadata ### Parameters: - subreddit_name: Subreddit name (without r/ prefix), e.g., \"pics\", \"funny\", \"AskReddit\" ### Returns: - JSON data containing detailed subreddit information  # [示例/Example] subreddit_name=\"pics\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_name: 版块名称/Subreddit name
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取Reddit APP版块信息/Fetch Reddit APP Subreddit Info  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定版块的详细信息,包括版块描述、成员数量、创建时间、规则等元数据 ### 参数: - subreddit_name: 版块名称(不带r/前缀),例如\"pics\", \"funny\", \"AskReddit\"等 ### 返回: - 指定版块的详细信息JSON数据 # [English] ### Purpose: - Fetch detailed information of a specified Reddit APP subreddit, including description, subscriber count, creation time, rules, and other metadata ### Parameters: - subreddit_name: Subreddit name (without r/ prefix), e.g., \"pics\", \"funny\", \"AskReddit\" ### Returns: - JSON data containing detailed subreddit information  # [示例/Example] subreddit_name=\"pics\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_name: 版块名称/Subreddit name
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subreddit_name', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subreddit_name' in params:
            query_params.append(('subreddit_name', params['subreddit_name']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_subreddit_info', 'GET',
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

    def fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get(self, **kwargs):  # noqa: E501
        """获取Reddit APP版块帖子频道信息/Fetch Reddit APP Subreddit Post Channels  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定版块的帖子频道信息 ### 参数: - subreddit_name: 版块名称(不带r/前缀) - sort: 排序方式，支持HOT, NEW, TOP, CONTROVERSIAL, RISING - range: 时间范围，支持HOUR, DAY, WEEK, MONTH, YEAR, ALL ### 返回: - 指定版块的帖子频道信息JSON数据  # [English] ### Purpose: - Fetch post channel information of a specified Reddit APP subreddit ### Parameters: - subreddit_name: Subreddit name - sort: Sort method, supports HOT, NEW, TOP, CONTROVERSIAL, RISING - range: Time range, supports HOUR, DAY, WEEK, MONTH, YEAR, ALL ### Returns: - JSON data of post channel information of the specified subreddit  # [示例/Example] subreddit_name=\"pics\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_name: 版块名称/Subreddit name
        :param object sort: 排序方式/Sort method: HOT, NEW, TOP, CONTROVERSIAL, RISING
        :param object range: 时间范围/Time range: HOUR, DAY, WEEK, MONTH, YEAR, ALL
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取Reddit APP版块帖子频道信息/Fetch Reddit APP Subreddit Post Channels  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定版块的帖子频道信息 ### 参数: - subreddit_name: 版块名称(不带r/前缀) - sort: 排序方式，支持HOT, NEW, TOP, CONTROVERSIAL, RISING - range: 时间范围，支持HOUR, DAY, WEEK, MONTH, YEAR, ALL ### 返回: - 指定版块的帖子频道信息JSON数据  # [English] ### Purpose: - Fetch post channel information of a specified Reddit APP subreddit ### Parameters: - subreddit_name: Subreddit name - sort: Sort method, supports HOT, NEW, TOP, CONTROVERSIAL, RISING - range: Time range, supports HOUR, DAY, WEEK, MONTH, YEAR, ALL ### Returns: - JSON data of post channel information of the specified subreddit  # [示例/Example] subreddit_name=\"pics\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_name: 版块名称/Subreddit name
        :param object sort: 排序方式/Sort method: HOT, NEW, TOP, CONTROVERSIAL, RISING
        :param object range: 时间范围/Time range: HOUR, DAY, WEEK, MONTH, YEAR, ALL
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subreddit_name', 'sort', 'range', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subreddit_name' in params:
            query_params.append(('subreddit_name', params['subreddit_name']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'range' in params:
            query_params.append(('range', params['range']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_subreddit_post_channels', 'GET',
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

    def fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get(self, subreddit_id, **kwargs):  # noqa: E501
        """获取Reddit APP版块设置/Fetch Reddit APP Subreddit Settings  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定版块的设置信息,包括发帖规则、用户标签设置、审核设置等配置信息 ### 参数: - subreddit_id: 版块ID,格式为t5_开头的唯一标识符,例如\"t5_2qh0u\"(可从fetch_subreddit_info接口获取版块ID) ### 返回: - 指定版块的设置信息JSON数据,包含以下主要字段:   - subredditType: 版块类型(public/private/restricted)   - submissionType: 允许提交的内容类型(any/link/self)   - allowImages: 是否允许图片   - allowVideos: 是否允许视频   - allowPolls: 是否允许投票   - suggestedCommentSort: 建议的评论排序方式   - spoilersEnabled: 是否启用剧透标记   - allowedPostTypes: 允许的帖子类型配置   - contentOptions: 内容选项设置   - flairSettings: 用户/帖子标签设置 ### 注意事项: - 需要先通过fetch_subreddit_info接口获取版块ID(subreddit.id字段) - 版块ID格式必须为\"t5_\"开头 - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 版块ID前缀: t5_ (例如: t5_2qh0u)  # [English] ### Purpose: - Fetch settings information of a specified Reddit APP subreddit, including posting rules, flair settings, moderation settings, and other configurations ### Parameters: - subreddit_id: Subreddit ID with format starting with t5_, e.g., \"t5_2qh0u\" (can be obtained from the fetch_subreddit_info endpoint) ### Returns: - JSON data containing subreddit settings with the following main fields:   - subredditType: Subreddit type (public/private/restricted)   - submissionType: Allowed submission content types (any/link/self)   - allowImages: Whether images are allowed   - allowVideos: Whether videos are allowed   - allowPolls: Whether polls are allowed   - suggestedCommentSort: Suggested comment sort method   - spoilersEnabled: Whether spoiler tags are enabled   - allowedPostTypes: Allowed post types configuration   - contentOptions: Content options settings   - flairSettings: User/post flair settings ### Notes: - You need to first get the subreddit ID (subreddit.id field) via the fetch_subreddit_info endpoint - Subreddit ID format must start with \"t5_\" - **APP API ID format differs from Web API, requires type prefix** - Subreddit ID prefix: t5_ (e.g., t5_2qh0u)  # [示例/Example] subreddit_id=\"t5_2qh0u\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get(subreddit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_id: 版块ID/Subreddit ID (format: t5_xxxxx) (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get_with_http_info(subreddit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get_with_http_info(subreddit_id, **kwargs)  # noqa: E501
            return data

    def fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get_with_http_info(self, subreddit_id, **kwargs):  # noqa: E501
        """获取Reddit APP版块设置/Fetch Reddit APP Subreddit Settings  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定版块的设置信息,包括发帖规则、用户标签设置、审核设置等配置信息 ### 参数: - subreddit_id: 版块ID,格式为t5_开头的唯一标识符,例如\"t5_2qh0u\"(可从fetch_subreddit_info接口获取版块ID) ### 返回: - 指定版块的设置信息JSON数据,包含以下主要字段:   - subredditType: 版块类型(public/private/restricted)   - submissionType: 允许提交的内容类型(any/link/self)   - allowImages: 是否允许图片   - allowVideos: 是否允许视频   - allowPolls: 是否允许投票   - suggestedCommentSort: 建议的评论排序方式   - spoilersEnabled: 是否启用剧透标记   - allowedPostTypes: 允许的帖子类型配置   - contentOptions: 内容选项设置   - flairSettings: 用户/帖子标签设置 ### 注意事项: - 需要先通过fetch_subreddit_info接口获取版块ID(subreddit.id字段) - 版块ID格式必须为\"t5_\"开头 - **APP接口的ID格式与Web接口不同，需要添加类型前缀** - 版块ID前缀: t5_ (例如: t5_2qh0u)  # [English] ### Purpose: - Fetch settings information of a specified Reddit APP subreddit, including posting rules, flair settings, moderation settings, and other configurations ### Parameters: - subreddit_id: Subreddit ID with format starting with t5_, e.g., \"t5_2qh0u\" (can be obtained from the fetch_subreddit_info endpoint) ### Returns: - JSON data containing subreddit settings with the following main fields:   - subredditType: Subreddit type (public/private/restricted)   - submissionType: Allowed submission content types (any/link/self)   - allowImages: Whether images are allowed   - allowVideos: Whether videos are allowed   - allowPolls: Whether polls are allowed   - suggestedCommentSort: Suggested comment sort method   - spoilersEnabled: Whether spoiler tags are enabled   - allowedPostTypes: Allowed post types configuration   - contentOptions: Content options settings   - flairSettings: User/post flair settings ### Notes: - You need to first get the subreddit ID (subreddit.id field) via the fetch_subreddit_info endpoint - Subreddit ID format must start with \"t5_\" - **APP API ID format differs from Web API, requires type prefix** - Subreddit ID prefix: t5_ (e.g., t5_2qh0u)  # [示例/Example] subreddit_id=\"t5_2qh0u\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get_with_http_info(subreddit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_id: 版块ID/Subreddit ID (format: t5_xxxxx) (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subreddit_id', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subreddit_id' is set
        if self.api_client.client_side_validation and ('subreddit_id' not in params or
                                                       params['subreddit_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subreddit_id` when calling `fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subreddit_id' in params:
            query_params.append(('subreddit_id', params['subreddit_id']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_subreddit_settings', 'GET',
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

    def fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get(self, **kwargs):  # noqa: E501
        """获取Reddit APP版块规则样式信息/Fetch Reddit APP Subreddit Rules and Style Info  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定版块的规则和样式信息 ### 参数: - subreddit_name: 版块名称(不带r/前缀) ### 返回: - 指定版块的规则和样式信息JSON数据  # [English] ### Purpose: - Fetch rules and style information of a specified Reddit APP subreddit ### Parameters: - subreddit_name: Subreddit name ### Returns: - JSON data of rules and style information of the specified subreddit  # [示例/Example] subreddit_name=\"pics\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_name: 版块名称/Subreddit name
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取Reddit APP版块规则样式信息/Fetch Reddit APP Subreddit Rules and Style Info  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定版块的规则和样式信息 ### 参数: - subreddit_name: 版块名称(不带r/前缀) ### 返回: - 指定版块的规则和样式信息JSON数据  # [English] ### Purpose: - Fetch rules and style information of a specified Reddit APP subreddit ### Parameters: - subreddit_name: Subreddit name ### Returns: - JSON data of rules and style information of the specified subreddit  # [示例/Example] subreddit_name=\"pics\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subreddit_name: 版块名称/Subreddit name
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subreddit_name', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subreddit_name' in params:
            query_params.append(('subreddit_name', params['subreddit_name']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_subreddit_style', 'GET',
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

    def fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get(self, **kwargs):  # noqa: E501
        """获取Reddit APP今日热门搜索/Fetch Reddit APP Trending Searches  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP当前热门搜索话题和趋势内容 ### 参数: - 无需参数 ### 返回: - 热门搜索JSON数据,包含:   - 热门搜索关键词列表   - 趋势话题   - 每个话题的搜索量和热度   - 相关帖子预览  # [English] ### Purpose: - Fetch currently trending search topics and content on Reddit APP ### Parameters: - No parameters required ### Returns: - JSON data of trending searches containing:   - List of trending search keywords   - Trending topics   - Search volume and popularity for each topic   - Related post previews  # [示例/Example] 无需参数/No parameters required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取Reddit APP今日热门搜索/Fetch Reddit APP Trending Searches  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP当前热门搜索话题和趋势内容 ### 参数: - 无需参数 ### 返回: - 热门搜索JSON数据,包含:   - 热门搜索关键词列表   - 趋势话题   - 每个话题的搜索量和热度   - 相关帖子预览  # [English] ### Purpose: - Fetch currently trending search topics and content on Reddit APP ### Parameters: - No parameters required ### Returns: - JSON data of trending searches containing:   - List of trending search keywords   - Trending topics   - Search volume and popularity for each topic   - Related post previews  # [示例/Example] 无需参数/No parameters required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_trending_searches', 'GET',
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

    def fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get(self, username, **kwargs):  # noqa: E501
        """获取用户活跃的社区列表/Fetch User's Active Subreddits  # noqa: E501

        # [中文] ### 用途: - 获取指定用户最活跃的Reddit社区列表 ### 参数: - username: Reddit用户名 ### 返回: - 用户活跃社区JSON数据,包含:   - 用户最常发帖/评论的社区列表   - 每个社区的活跃度信息   - 社区基本信息(名称、图标、成员数等)  # [English] ### Purpose: - Fetch list of Reddit communities where the specified user is most active ### Parameters: - username: Reddit username ### Returns: - JSON data of user's active communities containing:   - List of communities where user posts/comments most   - Activity level in each community   - Basic community information (name, icon, member count, etc.)  # [示例/Example] username=\"spez\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """获取用户活跃的社区列表/Fetch User's Active Subreddits  # noqa: E501

        # [中文] ### 用途: - 获取指定用户最活跃的Reddit社区列表 ### 参数: - username: Reddit用户名 ### 返回: - 用户活跃社区JSON数据,包含:   - 用户最常发帖/评论的社区列表   - 每个社区的活跃度信息   - 社区基本信息(名称、图标、成员数等)  # [English] ### Purpose: - Fetch list of Reddit communities where the specified user is most active ### Parameters: - username: Reddit username ### Returns: - JSON data of user's active communities containing:   - List of communities where user posts/comments most   - Activity level in each community   - Basic community information (name, icon, member count, etc.)  # [示例/Example] username=\"spez\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_user_active_subreddits', 'GET',
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

    def fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get(self, username, **kwargs):  # noqa: E501
        """获取用户评论列表/Fetch User Comments  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发表的评论列表 ### 参数: - username: Reddit用户名 - sort: 排序方式,可选值: NEW(最新), TOP(最热), HOT(热门), CONTROVERSIAL(有争议) - page_size: 每页返回的评论数量,默认25条 - after: 分页参数,用于获取下一页 ### 返回: - 用户评论列表JSON数据,包含:   - 评论内容   - 评论所在的帖子信息   - 评论时间   - 点赞数   - 回复数   - 分页信息  # [English] ### Purpose: - Fetch list of comments posted by the specified user ### Parameters: - username: Reddit username - sort: Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial) - page_size: Number of comments per page, default 25 - after: Pagination parameter for fetching next page ### Returns: - JSON data of user comments containing:   - Comment content   - Information about the post where comment was made   - Comment timestamp   - Upvote count   - Reply count   - Pagination information  # [示例/Example] username=\"spez\" sort=\"NEW\" page_size=25 after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object sort: 排序方式/Sort method: NEW, TOP, HOT, CONTROVERSIAL
        :param object page_size: 每页数量/Page size (default: 25)
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """获取用户评论列表/Fetch User Comments  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发表的评论列表 ### 参数: - username: Reddit用户名 - sort: 排序方式,可选值: NEW(最新), TOP(最热), HOT(热门), CONTROVERSIAL(有争议) - page_size: 每页返回的评论数量,默认25条 - after: 分页参数,用于获取下一页 ### 返回: - 用户评论列表JSON数据,包含:   - 评论内容   - 评论所在的帖子信息   - 评论时间   - 点赞数   - 回复数   - 分页信息  # [English] ### Purpose: - Fetch list of comments posted by the specified user ### Parameters: - username: Reddit username - sort: Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial) - page_size: Number of comments per page, default 25 - after: Pagination parameter for fetching next page ### Returns: - JSON data of user comments containing:   - Comment content   - Information about the post where comment was made   - Comment timestamp   - Upvote count   - Reply count   - Pagination information  # [示例/Example] username=\"spez\" sort=\"NEW\" page_size=25 after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object sort: 排序方式/Sort method: NEW, TOP, HOT, CONTROVERSIAL
        :param object page_size: 每页数量/Page size (default: 25)
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'sort', 'page_size', 'after', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_user_comments', 'GET',
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

    def fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get(self, username, **kwargs):  # noqa: E501
        """获取用户发布的帖子列表/Fetch User Posts  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的帖子列表 ### 参数: - username: Reddit用户名 - sort: 排序方式,可选值: NEW(最新), TOP(最热), HOT(热门), CONTROVERSIAL(有争议) - after: 分页参数,用于获取下一页 ### 返回: - 用户帖子列表JSON数据,包含:   - 帖子标题和内容   - 发布时间   - 所属版块   - 点赞数和评论数   - 帖子类型(文本/图片/视频/链接)   - 媒体内容(如有)   - 分页信息  # [English] ### Purpose: - Fetch list of posts submitted by the specified user ### Parameters: - username: Reddit username - sort: Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial) - after: Pagination parameter for fetching next page ### Returns: - JSON data of user posts containing:   - Post title and content   - Submission time   - Subreddit   - Upvote and comment counts   - Post type (text/image/video/link)   - Media content (if any)   - Pagination information  # [示例/Example] username=\"spez\" sort=\"NEW\" after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object sort: 排序方式/Sort method: NEW, TOP, HOT, CONTROVERSIAL
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """获取用户发布的帖子列表/Fetch User Posts  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的帖子列表 ### 参数: - username: Reddit用户名 - sort: 排序方式,可选值: NEW(最新), TOP(最热), HOT(热门), CONTROVERSIAL(有争议) - after: 分页参数,用于获取下一页 ### 返回: - 用户帖子列表JSON数据,包含:   - 帖子标题和内容   - 发布时间   - 所属版块   - 点赞数和评论数   - 帖子类型(文本/图片/视频/链接)   - 媒体内容(如有)   - 分页信息  # [English] ### Purpose: - Fetch list of posts submitted by the specified user ### Parameters: - username: Reddit username - sort: Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial) - after: Pagination parameter for fetching next page ### Returns: - JSON data of user posts containing:   - Post title and content   - Submission time   - Subreddit   - Upvote and comment counts   - Post type (text/image/video/link)   - Media content (if any)   - Pagination information  # [示例/Example] username=\"spez\" sort=\"NEW\" after=\"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object sort: 排序方式/Sort method: NEW, TOP, HOT, CONTROVERSIAL
        :param object after: 分页参数/Pagination parameter
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'sort', 'after', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_user_posts', 'GET',
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

    def fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get(self, username, **kwargs):  # noqa: E501
        """获取Reddit APP用户资料信息/Fetch Reddit APP User Profile  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定用户的详细资料信息 ### 参数: - username: Reddit用户名(不带u/前缀) ### 返回: - 用户资料JSON数据,包含:   - 用户名和ID   - 账号创建时间   - Karma值(帖子karma和评论karma)   - 头像和横幅图片   - 个人简介   - 是否验证账号   - 徽章和奖励   - 关注者数量  # [English] ### Purpose: - Fetch detailed profile information of a specified Reddit APP user ### Parameters: - username: Reddit username (without u/ prefix) ### Returns: - JSON data of user profile containing:   - Username and ID   - Account creation date   - Karma values (post karma and comment karma)   - Avatar and banner images   - Bio/description   - Verification status   - Badges and awards   - Follower count  # [示例/Example] username=\"spez\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """获取Reddit APP用户资料信息/Fetch Reddit APP User Profile  # noqa: E501

        # [中文] ### 用途: - 获取Reddit APP指定用户的详细资料信息 ### 参数: - username: Reddit用户名(不带u/前缀) ### 返回: - 用户资料JSON数据,包含:   - 用户名和ID   - 账号创建时间   - Karma值(帖子karma和评论karma)   - 头像和横幅图片   - 个人简介   - 是否验证账号   - 徽章和奖励   - 关注者数量  # [English] ### Purpose: - Fetch detailed profile information of a specified Reddit APP user ### Parameters: - username: Reddit username (without u/ prefix) ### Returns: - JSON data of user profile containing:   - Username and ID   - Account creation date   - Karma values (post karma and comment karma)   - Avatar and banner images   - Bio/description   - Verification status   - Badges and awards   - Follower count  # [示例/Example] username=\"spez\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_user_profile', 'GET',
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

    def fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get(self, username, **kwargs):  # noqa: E501
        """获取用户公开奖杯/Fetch User Public Trophies  # noqa: E501

        # [中文] ### 用途: - 获取指定Reddit用户的公开奖杯/成就列表 ### 参数: - username: Reddit用户名(不带u/前缀) ### 返回: - 用户奖杯JSON数据,包含:   - 奖杯列表(trophy list)   - 每个奖杯的详细信息:     - 奖杯名称     - 奖杯描述     - 奖杯图标URL     - 获得时间   - 特殊徽章和成就  # [English] ### Purpose: - Fetch public trophies/achievements list of a specified Reddit user ### Parameters: - username: Reddit username (without u/ prefix) ### Returns: - JSON data of user trophies containing:   - Trophy list   - Detailed information for each trophy:     - Trophy name     - Trophy description     - Trophy icon URL     - Award date   - Special badges and achievements  # [示例/Example] username=\"spez\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """获取用户公开奖杯/Fetch User Public Trophies  # noqa: E501

        # [中文] ### 用途: - 获取指定Reddit用户的公开奖杯/成就列表 ### 参数: - username: Reddit用户名(不带u/前缀) ### 返回: - 用户奖杯JSON数据,包含:   - 奖杯列表(trophy list)   - 每个奖杯的详细信息:     - 奖杯名称     - 奖杯描述     - 奖杯图标URL     - 获得时间   - 特殊徽章和成就  # [English] ### Purpose: - Fetch public trophies/achievements list of a specified Reddit user ### Parameters: - username: Reddit username (without u/ prefix) ### Returns: - JSON data of user trophies containing:   - Trophy list   - Detailed information for each trophy:     - Trophy name     - Trophy description     - Trophy icon URL     - Award date   - Special badges and achievements  # [示例/Example] username=\"spez\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object need_format: 是否需要清洗数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reddit/app/fetch_user_trophies', 'GET',
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
