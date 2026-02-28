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


class Sora2APIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_video_api_v1_sora2_create_video_post(self, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 文本/图片生成视频/Create video from text or image  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用。AI 相关接口已迁移至独立的 TikHub AI API 服务，与 TikHub 社交媒体 API 分离部署。请访问：https://ai.tikhub.io ### 用途: - 通过文本描述生成 Sora 视频（支持纯文本生成或图片+文本生成） - 支持两种生成模式：     - **纯文本生成**：AI 根据文本描述自动生成视频内容     - **图生视频**：基于上传的图片和文本描述生成视频（需要先调用 upload_image 接口） - 支持两种视频比例：     - **portrait（竖屏）**: 9:16 比例，适合移动端、社交媒体短视频     - **landscape（横屏）**: 16:9 比例，适合桌面端、宽屏展示、电影风格 - 返回生成任务 ID，需要通过其他接口查询生成进度和结果  ### 收费说明: - 本接口请求价格为 1 次调用消耗 **$0.1 美元** - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数  ### 参数: - **prompt** (必填): 视频描述文本，最多 2000 字符     - 描述要生成的视频内容、场景、动作、情节等     - 建议使用清晰、具体的描述以获得更好的生成效果     - 示例：\"A cat is playing Minecraft\" - **orientation** (可选): 视频方向，默认为 portrait（竖屏）     - `portrait`: 竖屏（9:16 比例）     - `landscape`: 横屏（16:9 比例） - **media_id** (可选): 图片 media_id，用于图生视频     - 通过 `/upload_image` 接口上传图片后获取     - 格式：`media_xxxxxxxxxxxxxxxxxxxxxxxxxx`     - 如果不提供，则为纯文本生成视频  ### 返回: - **id**: 视频生成任务 ID     - 格式：`task_xxxxxxxxxxxxxxxxxxxxxxxxxx`     - 使用此 ID 可以查询生成进度和获取最终视频 - **priority**: 任务优先级     - 通常为 1（标准优先级）  ### 注意: - 这是一个异步生成任务，不会立即返回视频 - 视频生成通常需要几分钟时间 - 需要使用任务 ID 通过其他接口轮询查询生成状态 - 请自行保留任务 ID，以便后续查询，否则将无法获取生成结果  # [English] ## ⚠️ This endpoint has been deprecated. AI-related endpoints have been migrated to a dedicated TikHub AI API service, which operates separately from the TikHub Social Media API. Please visit: https://ai.tikhub.io ### Purpose: - Generate Sora video from text description (supports text-only or image+text generation) - Supports two generation modes:     - **Text-only generation**: AI automatically generates video content based on text description     - **Image-to-video**: Generate video based on uploaded image and text description (requires calling upload_image endpoint first) - Supports two video ratios:     - **portrait**: 9:16 ratio, suitable for mobile devices, social media short videos     - **landscape**: 16:9 ratio, suitable for desktop viewing, widescreen display, cinematic style - Returns generation task ID, need to query generation progress and results through other endpoints  ### Pricing: - This API costs **$0.1 USD per request** - This API supports free quota, you can get free requests by checking in daily at the user dashboard  ### Parameters: - **prompt** (required): Video description text, maximum 2000 characters     - Describe the video content, scenes, actions, plots, etc. to be generated     - Recommend using clear and specific descriptions for better generation results     - Example: \"A cat is playing Minecraft\" - **orientation** (optional): Video orientation, defaults to portrait     - `portrait`: Portrait (9:16 ratio)     - `landscape`: Landscape (16:9 ratio) - **media_id** (optional): Image media_id for image-to-video generation     - Obtained from `/upload_image` endpoint after uploading an image     - Format: `media_xxxxxxxxxxxxxxxxxxxxxxxxxx`     - If not provided, text-only video generation will be used  ### Return: - **id**: Video generation task ID     - Format: `task_xxxxxxxxxxxxxxxxxxxxxxxxxx`     - Use this ID to query generation progress and get final video - **priority**: Task priority     - Usually 1 (standard priority)  ### Note: - This is an asynchronous generation task, will not return video immediately - Video generation usually takes several minutes - Need to use task ID to poll generation status through other endpoints - Please keep the task ID for future queries, otherwise you will not be able to get the generation results  # [示例/Example] ```python import requests  # 示例 1：纯文本生成竖屏视频/Example 1: Text-only portrait video url = \"https://api.tikhub.io/api/v1/sora2/create_video\" headers = {\"Authorization\": \"Bearer YOUR_API_TOKEN\"} payload = {     \"prompt\": \"A cat is playing Minecraft\",     \"orientation\": \"portrait\" } response = requests.post(url, headers=headers, json=payload)  # 示例 2：图片+文本生成视频（图生视频）/Example 2: Image-to-video generation # 步骤1：上传图片获取 media_id/Step 1: Upload image to get media_id upload_url = \"https://api.tikhub.io/api/v1/sora2/upload_image\" with open(\"image.png\", \"rb\") as f:     files = {\"file\": (\"image.png\", f, \"image/png\")}     upload_resp = requests.post(upload_url, headers=headers, files=files)     media_id = upload_resp.json()[\"data\"][\"id\"]  # 例如: \"media_01k7...\"  # 步骤2：使用 media_id 生成视频/Step 2: Use media_id to generate video payload = {     \"prompt\": \"Transform this image into a dynamic video scene\",     \"orientation\": \"landscape\",     \"media_id\": media_id  # 来自 upload_image 的 media_id } response = requests.post(url, headers=headers, json=payload)  # 返回示例/Return example {     \"code\": 200,     \"data\": {         \"id\": \"task_01k7e05chaem08va8sq5qy2een\",         \"priority\": 1     } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_video_api_v1_sora2_create_video_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_video_api_v1_sora2_create_video_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_video_api_v1_sora2_create_video_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_video_api_v1_sora2_create_video_post_with_http_info(self, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 文本/图片生成视频/Create video from text or image  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用。AI 相关接口已迁移至独立的 TikHub AI API 服务，与 TikHub 社交媒体 API 分离部署。请访问：https://ai.tikhub.io ### 用途: - 通过文本描述生成 Sora 视频（支持纯文本生成或图片+文本生成） - 支持两种生成模式：     - **纯文本生成**：AI 根据文本描述自动生成视频内容     - **图生视频**：基于上传的图片和文本描述生成视频（需要先调用 upload_image 接口） - 支持两种视频比例：     - **portrait（竖屏）**: 9:16 比例，适合移动端、社交媒体短视频     - **landscape（横屏）**: 16:9 比例，适合桌面端、宽屏展示、电影风格 - 返回生成任务 ID，需要通过其他接口查询生成进度和结果  ### 收费说明: - 本接口请求价格为 1 次调用消耗 **$0.1 美元** - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数  ### 参数: - **prompt** (必填): 视频描述文本，最多 2000 字符     - 描述要生成的视频内容、场景、动作、情节等     - 建议使用清晰、具体的描述以获得更好的生成效果     - 示例：\"A cat is playing Minecraft\" - **orientation** (可选): 视频方向，默认为 portrait（竖屏）     - `portrait`: 竖屏（9:16 比例）     - `landscape`: 横屏（16:9 比例） - **media_id** (可选): 图片 media_id，用于图生视频     - 通过 `/upload_image` 接口上传图片后获取     - 格式：`media_xxxxxxxxxxxxxxxxxxxxxxxxxx`     - 如果不提供，则为纯文本生成视频  ### 返回: - **id**: 视频生成任务 ID     - 格式：`task_xxxxxxxxxxxxxxxxxxxxxxxxxx`     - 使用此 ID 可以查询生成进度和获取最终视频 - **priority**: 任务优先级     - 通常为 1（标准优先级）  ### 注意: - 这是一个异步生成任务，不会立即返回视频 - 视频生成通常需要几分钟时间 - 需要使用任务 ID 通过其他接口轮询查询生成状态 - 请自行保留任务 ID，以便后续查询，否则将无法获取生成结果  # [English] ## ⚠️ This endpoint has been deprecated. AI-related endpoints have been migrated to a dedicated TikHub AI API service, which operates separately from the TikHub Social Media API. Please visit: https://ai.tikhub.io ### Purpose: - Generate Sora video from text description (supports text-only or image+text generation) - Supports two generation modes:     - **Text-only generation**: AI automatically generates video content based on text description     - **Image-to-video**: Generate video based on uploaded image and text description (requires calling upload_image endpoint first) - Supports two video ratios:     - **portrait**: 9:16 ratio, suitable for mobile devices, social media short videos     - **landscape**: 16:9 ratio, suitable for desktop viewing, widescreen display, cinematic style - Returns generation task ID, need to query generation progress and results through other endpoints  ### Pricing: - This API costs **$0.1 USD per request** - This API supports free quota, you can get free requests by checking in daily at the user dashboard  ### Parameters: - **prompt** (required): Video description text, maximum 2000 characters     - Describe the video content, scenes, actions, plots, etc. to be generated     - Recommend using clear and specific descriptions for better generation results     - Example: \"A cat is playing Minecraft\" - **orientation** (optional): Video orientation, defaults to portrait     - `portrait`: Portrait (9:16 ratio)     - `landscape`: Landscape (16:9 ratio) - **media_id** (optional): Image media_id for image-to-video generation     - Obtained from `/upload_image` endpoint after uploading an image     - Format: `media_xxxxxxxxxxxxxxxxxxxxxxxxxx`     - If not provided, text-only video generation will be used  ### Return: - **id**: Video generation task ID     - Format: `task_xxxxxxxxxxxxxxxxxxxxxxxxxx`     - Use this ID to query generation progress and get final video - **priority**: Task priority     - Usually 1 (standard priority)  ### Note: - This is an asynchronous generation task, will not return video immediately - Video generation usually takes several minutes - Need to use task ID to poll generation status through other endpoints - Please keep the task ID for future queries, otherwise you will not be able to get the generation results  # [示例/Example] ```python import requests  # 示例 1：纯文本生成竖屏视频/Example 1: Text-only portrait video url = \"https://api.tikhub.io/api/v1/sora2/create_video\" headers = {\"Authorization\": \"Bearer YOUR_API_TOKEN\"} payload = {     \"prompt\": \"A cat is playing Minecraft\",     \"orientation\": \"portrait\" } response = requests.post(url, headers=headers, json=payload)  # 示例 2：图片+文本生成视频（图生视频）/Example 2: Image-to-video generation # 步骤1：上传图片获取 media_id/Step 1: Upload image to get media_id upload_url = \"https://api.tikhub.io/api/v1/sora2/upload_image\" with open(\"image.png\", \"rb\") as f:     files = {\"file\": (\"image.png\", f, \"image/png\")}     upload_resp = requests.post(upload_url, headers=headers, files=files)     media_id = upload_resp.json()[\"data\"][\"id\"]  # 例如: \"media_01k7...\"  # 步骤2：使用 media_id 生成视频/Step 2: Use media_id to generate video payload = {     \"prompt\": \"Transform this image into a dynamic video scene\",     \"orientation\": \"landscape\",     \"media_id\": media_id  # 来自 upload_image 的 media_id } response = requests.post(url, headers=headers, json=payload)  # 返回示例/Return example {     \"code\": 200,     \"data\": {         \"id\": \"task_01k7e05chaem08va8sq5qy2een\",         \"priority\": 1     } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_video_api_v1_sora2_create_video_post_with_http_info(async_req=True)
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
                    " to method create_video_api_v1_sora2_create_video_post" % key
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
            '/api/v1/sora2/create_video', 'POST',
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

    def get_cameo_leaderboard_api_v1_sora2_get_cameo_leaderboard_get(self, **kwargs):  # noqa: E501
        """获取 Cameo 出镜秀达人排行榜/Fetch Cameo leaderboard  # noqa: E501

        # [中文] ### 用途: - 获取 Sora Cameo 出镜秀达人排行榜 - 展示在 Cameo 功能中被使用最多的用户 - 支持分页获取更多排行榜数据  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - cursor: 翻页参数（可选），从上一次响应的 cursor 字段获取，每页返回 10 个用户  ### 返回: - items: 用户排行榜列表（每页 10 个用户）     - user_id: 用户 ID     - username: 用户名     - display_name: 显示名称     - profile_picture_url: 头像链接     - follower_count: 粉丝数     - cameo_count: 被使用次数 - cursor: 下一页参数，用于获取更多数据（如果为 null 表示已到末页）  # [English] ### Purpose: - Fetch Sora Cameo leaderboard - Shows the most featured users in the Cameo function - Supports pagination to get more leaderboard data  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - cursor: Cursor for pagination (optional), obtained from the cursor field of the previous response, returns 10 users per page  ### Return: - items: User leaderboard list (10 users per page)     - user_id: User ID     - username: Username     - display_name: Display name     - profile_picture_url: Profile picture URL     - follower_count: Follower count     - cameo_count: Feature count - cursor: Next page parameter for fetching more data (null means last page)  # [示例/Example] ```python # 获取第一页排行榜 # Get first page of leaderboard response = await get_cameo_leaderboard()  # 使用 cursor 获取下一页 # Use cursor to get next page cursor = response['cursor'] next_page = await get_cameo_leaderboard(cursor=cursor) ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cameo_leaderboard_api_v1_sora2_get_cameo_leaderboard_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cursor: 翻页参数（可选）/Cursor for pagination (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cameo_leaderboard_api_v1_sora2_get_cameo_leaderboard_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_cameo_leaderboard_api_v1_sora2_get_cameo_leaderboard_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_cameo_leaderboard_api_v1_sora2_get_cameo_leaderboard_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取 Cameo 出镜秀达人排行榜/Fetch Cameo leaderboard  # noqa: E501

        # [中文] ### 用途: - 获取 Sora Cameo 出镜秀达人排行榜 - 展示在 Cameo 功能中被使用最多的用户 - 支持分页获取更多排行榜数据  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - cursor: 翻页参数（可选），从上一次响应的 cursor 字段获取，每页返回 10 个用户  ### 返回: - items: 用户排行榜列表（每页 10 个用户）     - user_id: 用户 ID     - username: 用户名     - display_name: 显示名称     - profile_picture_url: 头像链接     - follower_count: 粉丝数     - cameo_count: 被使用次数 - cursor: 下一页参数，用于获取更多数据（如果为 null 表示已到末页）  # [English] ### Purpose: - Fetch Sora Cameo leaderboard - Shows the most featured users in the Cameo function - Supports pagination to get more leaderboard data  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - cursor: Cursor for pagination (optional), obtained from the cursor field of the previous response, returns 10 users per page  ### Return: - items: User leaderboard list (10 users per page)     - user_id: User ID     - username: Username     - display_name: Display name     - profile_picture_url: Profile picture URL     - follower_count: Follower count     - cameo_count: Feature count - cursor: Next page parameter for fetching more data (null means last page)  # [示例/Example] ```python # 获取第一页排行榜 # Get first page of leaderboard response = await get_cameo_leaderboard()  # 使用 cursor 获取下一页 # Use cursor to get next page cursor = response['cursor'] next_page = await get_cameo_leaderboard(cursor=cursor) ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cameo_leaderboard_api_v1_sora2_get_cameo_leaderboard_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cursor: 翻页参数（可选）/Cursor for pagination (optional)
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
                    " to method get_cameo_leaderboard_api_v1_sora2_get_cameo_leaderboard_get" % key
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
            '/api/v1/sora2/get_cameo_leaderboard', 'GET',
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

    def get_comment_replies_api_v1_sora2_get_comment_replies_get(self, comment_id, **kwargs):  # noqa: E501
        """获取评论的回复/Fetch comment replies  # noqa: E501

        # [中文] ### 用途: - 获取一级评论的回复列表（二级评论） - 支持分页加载，每页返回 10 条回复 - 用于展示评论的完整对话树  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - comment_id: 一级评论的 ID，必填（可从 get_post_comments 接口的返回中获取） - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - children: 回复数据     - items: 回复列表（10条/页）         - id: 回复 ID         - text: 回复文本内容         - posted_by: 回复者用户 ID         - posted_at: 回复时间戳         - like_count: 点赞数         - profile: 回复者信息             - username: 用户名             - display_name: 显示名称             - profile_picture_url: 头像链接     - cursor: 下一页参数（用于获取更多回复，无更多时为 null）     - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch replies for a first-level comment (second-level comments) - Supports pagination, returns 10 replies per page - Used to display complete comment conversation tree  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - comment_id: First-level comment ID, required (can be obtained from get_post_comments response) - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - children: Reply data     - items: Reply list (10 items/page)         - id: Reply ID         - text: Reply text content         - posted_by: Replier user ID         - posted_at: Reply timestamp         - like_count: Like count         - profile: Replier information             - username: Username             - display_name: Display name             - profile_picture_url: Avatar URL     - cursor: Next page cursor (for loading more replies, null when no more)     - has_more: Whether there are more data  # [示例/Example] ```python # 首先获取一级评论 # post_comments = get_post_comments(\"s_68e647d78e5081918cdeaf27e7edc735\") # comment_id = post_comments['children']['items'][0]['id']  # 第一条评论的 ID  # 然后获取该评论的回复 comment_id = \"68e659c5a37081919618c57baf499d0c\" cursor = \"\"  # 首次请求留空 ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_comment_replies_api_v1_sora2_get_comment_replies_get(comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object comment_id: 一级评论ID/First-level comment ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_comment_replies_api_v1_sora2_get_comment_replies_get_with_http_info(comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_comment_replies_api_v1_sora2_get_comment_replies_get_with_http_info(comment_id, **kwargs)  # noqa: E501
            return data

    def get_comment_replies_api_v1_sora2_get_comment_replies_get_with_http_info(self, comment_id, **kwargs):  # noqa: E501
        """获取评论的回复/Fetch comment replies  # noqa: E501

        # [中文] ### 用途: - 获取一级评论的回复列表（二级评论） - 支持分页加载，每页返回 10 条回复 - 用于展示评论的完整对话树  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - comment_id: 一级评论的 ID，必填（可从 get_post_comments 接口的返回中获取） - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - children: 回复数据     - items: 回复列表（10条/页）         - id: 回复 ID         - text: 回复文本内容         - posted_by: 回复者用户 ID         - posted_at: 回复时间戳         - like_count: 点赞数         - profile: 回复者信息             - username: 用户名             - display_name: 显示名称             - profile_picture_url: 头像链接     - cursor: 下一页参数（用于获取更多回复，无更多时为 null）     - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch replies for a first-level comment (second-level comments) - Supports pagination, returns 10 replies per page - Used to display complete comment conversation tree  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - comment_id: First-level comment ID, required (can be obtained from get_post_comments response) - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - children: Reply data     - items: Reply list (10 items/page)         - id: Reply ID         - text: Reply text content         - posted_by: Replier user ID         - posted_at: Reply timestamp         - like_count: Like count         - profile: Replier information             - username: Username             - display_name: Display name             - profile_picture_url: Avatar URL     - cursor: Next page cursor (for loading more replies, null when no more)     - has_more: Whether there are more data  # [示例/Example] ```python # 首先获取一级评论 # post_comments = get_post_comments(\"s_68e647d78e5081918cdeaf27e7edc735\") # comment_id = post_comments['children']['items'][0]['id']  # 第一条评论的 ID  # 然后获取该评论的回复 comment_id = \"68e659c5a37081919618c57baf499d0c\" cursor = \"\"  # 首次请求留空 ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_comment_replies_api_v1_sora2_get_comment_replies_get_with_http_info(comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object comment_id: 一级评论ID/First-level comment ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['comment_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_comment_replies_api_v1_sora2_get_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `get_comment_replies_api_v1_sora2_get_comment_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sora2/get_comment_replies', 'GET',
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

    def get_feed_api_v1_sora2_get_feed_get(self, **kwargs):  # noqa: E501
        """获取Feed流（热门/推荐视频）/Fetch feed  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 的 Feed 流（热门或推荐视频列表） - 默认返回过去 7 天的热门视频 - 支持分页加载，每页返回约 15 条视频 - 可通过 eager_views 参数提供观看记录来获得个性化推荐  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值 - eager_views: 观看记录（可选），JSON 字符串格式     - 默认值：`{\"views\":[]}`（空观看记录，返回通用热门）     - 包含观看记录示例：`{\"views\":[{\"id\":\"s_xxx\",\"watch_time\":0.24,\"dwell_time\":3.94}]}`     - 提供观看记录可获得更个性化的推荐结果  ### 返回: - items: 视频列表（约15条/页）     - post: 作品信息         - id: 作品 ID         - text: 作品描述         - attachments: 视频附件信息         - like_count: 点赞数         - view_count: 浏览数         - reply_count: 评论数         - posted_at: 发布时间戳     - profile: 作者信息 - cursor: 下一页参数（用于获取更多视频，无更多时为 null） - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch Sora's feed stream (trending or recommended video list) - Returns trending videos from the past 7 days by default - Supports pagination, returns approximately 15 videos per page - Can provide watch history via eager_views parameter for personalized recommendations  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests - eager_views: Watch history (optional), JSON string format     - Default value: `{\"views\":[]}` (empty watch history, returns general trending)     - With watch history example: `{\"views\":[{\"id\":\"s_xxx\",\"watch_time\":0.24,\"dwell_time\":3.94}]}`     - Providing watch history enables more personalized recommendation results  ### Return: - items: Video list (approx. 15 items/page)     - post: Post information         - id: Post ID         - text: Post description         - attachments: Video attachment info         - like_count: Like count         - view_count: View count         - reply_count: Comment count         - posted_at: Post timestamp     - profile: Author information - cursor: Next page cursor (for loading more videos, null when no more) - has_more: Whether there are more data  # [示例/Example] ```python # 第一次请求（获取热门视频，无观看记录） cursor = \"\" eager_views = '{\"views\":[]}'  # 第二次请求（带观看记录，获得个性化推荐） eager_views = '{\"views\":[{\"id\":\"s_68e853d2ad448191b3c81e830f53c3a2\",\"watch_time\":0.24,\"dwell_time\":3.94}]}'  # 第三次请求（获取下一页） cursor = \"eyJjdXQiOiJuZjJfdG9wXzdkIiwibGltaXQiOjE1LCJvZmZzZXQiOjE1fQ==\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feed_api_v1_sora2_get_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
        :param object eager_views: 观看记录JSON字符串（可选），用于个性化推荐/Watch history JSON string (optional), for personalized recommendations
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_feed_api_v1_sora2_get_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_feed_api_v1_sora2_get_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_feed_api_v1_sora2_get_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取Feed流（热门/推荐视频）/Fetch feed  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 的 Feed 流（热门或推荐视频列表） - 默认返回过去 7 天的热门视频 - 支持分页加载，每页返回约 15 条视频 - 可通过 eager_views 参数提供观看记录来获得个性化推荐  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值 - eager_views: 观看记录（可选），JSON 字符串格式     - 默认值：`{\"views\":[]}`（空观看记录，返回通用热门）     - 包含观看记录示例：`{\"views\":[{\"id\":\"s_xxx\",\"watch_time\":0.24,\"dwell_time\":3.94}]}`     - 提供观看记录可获得更个性化的推荐结果  ### 返回: - items: 视频列表（约15条/页）     - post: 作品信息         - id: 作品 ID         - text: 作品描述         - attachments: 视频附件信息         - like_count: 点赞数         - view_count: 浏览数         - reply_count: 评论数         - posted_at: 发布时间戳     - profile: 作者信息 - cursor: 下一页参数（用于获取更多视频，无更多时为 null） - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch Sora's feed stream (trending or recommended video list) - Returns trending videos from the past 7 days by default - Supports pagination, returns approximately 15 videos per page - Can provide watch history via eager_views parameter for personalized recommendations  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests - eager_views: Watch history (optional), JSON string format     - Default value: `{\"views\":[]}` (empty watch history, returns general trending)     - With watch history example: `{\"views\":[{\"id\":\"s_xxx\",\"watch_time\":0.24,\"dwell_time\":3.94}]}`     - Providing watch history enables more personalized recommendation results  ### Return: - items: Video list (approx. 15 items/page)     - post: Post information         - id: Post ID         - text: Post description         - attachments: Video attachment info         - like_count: Like count         - view_count: View count         - reply_count: Comment count         - posted_at: Post timestamp     - profile: Author information - cursor: Next page cursor (for loading more videos, null when no more) - has_more: Whether there are more data  # [示例/Example] ```python # 第一次请求（获取热门视频，无观看记录） cursor = \"\" eager_views = '{\"views\":[]}'  # 第二次请求（带观看记录，获得个性化推荐） eager_views = '{\"views\":[{\"id\":\"s_68e853d2ad448191b3c81e830f53c3a2\",\"watch_time\":0.24,\"dwell_time\":3.94}]}'  # 第三次请求（获取下一页） cursor = \"eyJjdXQiOiJuZjJfdG9wXzdkIiwibGltaXQiOjE1LCJvZmZzZXQiOjE1fQ==\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feed_api_v1_sora2_get_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
        :param object eager_views: 观看记录JSON字符串（可选），用于个性化推荐/Watch history JSON string (optional), for personalized recommendations
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cursor', 'eager_views']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feed_api_v1_sora2_get_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'eager_views' in params:
            query_params.append(('eager_views', params['eager_views']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sora2/get_feed', 'GET',
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

    def get_post_comments_api_v1_sora2_get_post_comments_get(self, post_id, **kwargs):  # noqa: E501
        """获取作品一级评论/Fetch post comments  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 作品的一级评论列表（顶层评论） - 支持分页加载，每页返回 10 条评论 - 可用于评论展示、数据分析等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - post_id: 作品 ID，必填 - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - children: 评论数据     - items: 评论列表（10条/页）         - id: 评论 ID         - text: 评论文本内容         - posted_by: 评论者用户 ID         - posted_at: 评论时间戳         - like_count: 点赞数         - reply_count: 回复数（二级评论数）         - profile: 评论者信息             - username: 用户名             - display_name: 显示名称             - profile_picture_url: 头像链接     - cursor: 下一页参数（用于获取更多评论，无更多时为 null）     - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch first-level comments (top-level comments) for a Sora post - Supports pagination, returns 10 comments per page - Can be used for comment display, data analysis, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - post_id: Post ID, required - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - children: Comment data     - items: Comment list (10 items/page)         - id: Comment ID         - text: Comment text content         - posted_by: Commenter user ID         - posted_at: Comment timestamp         - like_count: Like count         - reply_count: Reply count (second-level comments)         - profile: Commenter information             - username: Username             - display_name: Display name             - profile_picture_url: Avatar URL     - cursor: Next page cursor (for loading more comments, null when no more)     - has_more: Whether there are more data  # [示例/Example] ```python # 第一次请求（获取前 10 条评论） post_id = \"s_68e647d78e5081918cdeaf27e7edc735\" cursor = \"\"  # 首次请求留空  # 第二次请求（获取下一页） # 使用上一次响应中的 cursor 值 cursor = \"eyJwb3N0X2lkIjoiNjhlNjQ3ZDc4ZTUwODE5MThjZGVhZjI3ZTdlZGM3MzUi...\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_comments_api_v1_sora2_get_post_comments_get(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 作品ID/Post ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_post_comments_api_v1_sora2_get_post_comments_get_with_http_info(post_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_post_comments_api_v1_sora2_get_post_comments_get_with_http_info(post_id, **kwargs)  # noqa: E501
            return data

    def get_post_comments_api_v1_sora2_get_post_comments_get_with_http_info(self, post_id, **kwargs):  # noqa: E501
        """获取作品一级评论/Fetch post comments  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 作品的一级评论列表（顶层评论） - 支持分页加载，每页返回 10 条评论 - 可用于评论展示、数据分析等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - post_id: 作品 ID，必填 - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - children: 评论数据     - items: 评论列表（10条/页）         - id: 评论 ID         - text: 评论文本内容         - posted_by: 评论者用户 ID         - posted_at: 评论时间戳         - like_count: 点赞数         - reply_count: 回复数（二级评论数）         - profile: 评论者信息             - username: 用户名             - display_name: 显示名称             - profile_picture_url: 头像链接     - cursor: 下一页参数（用于获取更多评论，无更多时为 null）     - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch first-level comments (top-level comments) for a Sora post - Supports pagination, returns 10 comments per page - Can be used for comment display, data analysis, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - post_id: Post ID, required - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - children: Comment data     - items: Comment list (10 items/page)         - id: Comment ID         - text: Comment text content         - posted_by: Commenter user ID         - posted_at: Comment timestamp         - like_count: Like count         - reply_count: Reply count (second-level comments)         - profile: Commenter information             - username: Username             - display_name: Display name             - profile_picture_url: Avatar URL     - cursor: Next page cursor (for loading more comments, null when no more)     - has_more: Whether there are more data  # [示例/Example] ```python # 第一次请求（获取前 10 条评论） post_id = \"s_68e647d78e5081918cdeaf27e7edc735\" cursor = \"\"  # 首次请求留空  # 第二次请求（获取下一页） # 使用上一次响应中的 cursor 值 cursor = \"eyJwb3N0X2lkIjoiNjhlNjQ3ZDc4ZTUwODE5MThjZGVhZjI3ZTdlZGM3MzUi...\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_comments_api_v1_sora2_get_post_comments_get_with_http_info(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 作品ID/Post ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_post_comments_api_v1_sora2_get_post_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_id' is set
        if self.api_client.client_side_validation and ('post_id' not in params or
                                                       params['post_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_id` when calling `get_post_comments_api_v1_sora2_get_post_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sora2/get_post_comments', 'GET',
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

    def get_post_detail_api_v1_sora2_get_post_detail_get(self, **kwargs):  # noqa: E501
        """获取单一作品详情/Fetch single post detail  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 作品的完整详情信息，包括视频信息、作者信息、统计数据等 - 支持通过作品 ID 或作品链接查询 - 可用于数据分析、无水印视频下载等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - post_id: 作品 ID（可选），格式如 `s_68e853d2ad448191b3c81e830f53c3a2` - post_url: 作品链接（可选），格式如 `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2` - **注意**: post_id 和 post_url 至少提供一个  ### 返回: - post: 作品详细信息     - id: 作品 ID     - text: 作品描述文本     - attachments: 附件列表（视频信息）         - url: 无水印视频链接         - downloadable_url: 有水印视频链接         - width/height: 视频尺寸         - encodings: 不同质量的编码版本     - like_count: 点赞数     - view_count: 浏览数     - reply_count: 评论数     - remix_count: 混剪数     - shared_by: 作者用户 ID     - posted_at: 发布时间戳     - permalink: 作品永久链接 - profile: 作者信息     - user_id: 用户 ID     - username: 用户名     - display_name: 显示名称     - profile_picture_url: 头像链接     - follower_count: 粉丝数  # [English] ### Purpose: - Fetch complete details of a Sora post, including video info, author info, and statistics - Supports querying by post ID or post URL - Can be used for data analysis, watermark-free video downloads, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - post_id: Post ID (optional), format like `s_68e853d2ad448191b3c81e830f53c3a2` - post_url: Post URL (optional), format like `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2` - **Note**: At least one of post_id or post_url must be provided  ### Return: - post: Post detailed information     - id: Post ID     - text: Post description text     - attachments: Attachment list (video info)         - url: No watermark video link         - downloadable_url: Watermarked video link         - width/height: Video dimensions         - encodings: Different quality encoding versions     - like_count: Like count     - view_count: View count     - reply_count: Comment count     - remix_count: Remix count     - shared_by: Author user ID     - posted_at: Post timestamp     - permalink: Permanent link - profile: Author information     - user_id: User ID     - username: Username     - display_name: Display name     - profile_picture_url: Avatar URL     - follower_count: Follower count  # [示例/Example] ```python # 使用作品 ID 查询 post_id = \"s_68e853d2ad448191b3c81e830f53c3a2\"  # 或使用作品链接查询 post_url = \"https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_detail_api_v1_sora2_get_post_detail_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 作品ID（可选）/Post ID (optional)
        :param object post_url: 作品链接（可选）/Post URL (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_post_detail_api_v1_sora2_get_post_detail_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_post_detail_api_v1_sora2_get_post_detail_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_post_detail_api_v1_sora2_get_post_detail_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取单一作品详情/Fetch single post detail  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 作品的完整详情信息，包括视频信息、作者信息、统计数据等 - 支持通过作品 ID 或作品链接查询 - 可用于数据分析、无水印视频下载等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - post_id: 作品 ID（可选），格式如 `s_68e853d2ad448191b3c81e830f53c3a2` - post_url: 作品链接（可选），格式如 `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2` - **注意**: post_id 和 post_url 至少提供一个  ### 返回: - post: 作品详细信息     - id: 作品 ID     - text: 作品描述文本     - attachments: 附件列表（视频信息）         - url: 无水印视频链接         - downloadable_url: 有水印视频链接         - width/height: 视频尺寸         - encodings: 不同质量的编码版本     - like_count: 点赞数     - view_count: 浏览数     - reply_count: 评论数     - remix_count: 混剪数     - shared_by: 作者用户 ID     - posted_at: 发布时间戳     - permalink: 作品永久链接 - profile: 作者信息     - user_id: 用户 ID     - username: 用户名     - display_name: 显示名称     - profile_picture_url: 头像链接     - follower_count: 粉丝数  # [English] ### Purpose: - Fetch complete details of a Sora post, including video info, author info, and statistics - Supports querying by post ID or post URL - Can be used for data analysis, watermark-free video downloads, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - post_id: Post ID (optional), format like `s_68e853d2ad448191b3c81e830f53c3a2` - post_url: Post URL (optional), format like `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2` - **Note**: At least one of post_id or post_url must be provided  ### Return: - post: Post detailed information     - id: Post ID     - text: Post description text     - attachments: Attachment list (video info)         - url: No watermark video link         - downloadable_url: Watermarked video link         - width/height: Video dimensions         - encodings: Different quality encoding versions     - like_count: Like count     - view_count: View count     - reply_count: Comment count     - remix_count: Remix count     - shared_by: Author user ID     - posted_at: Post timestamp     - permalink: Permanent link - profile: Author information     - user_id: User ID     - username: Username     - display_name: Display name     - profile_picture_url: Avatar URL     - follower_count: Follower count  # [示例/Example] ```python # 使用作品 ID 查询 post_id = \"s_68e853d2ad448191b3c81e830f53c3a2\"  # 或使用作品链接查询 post_url = \"https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_detail_api_v1_sora2_get_post_detail_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 作品ID（可选）/Post ID (optional)
        :param object post_url: 作品链接（可选）/Post URL (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id', 'post_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_post_detail_api_v1_sora2_get_post_detail_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501
        if 'post_url' in params:
            query_params.append(('post_url', params['post_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sora2/get_post_detail', 'GET',
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

    def get_post_remix_list_api_v1_sora2_get_post_remix_list_get(self, **kwargs):  # noqa: E501
        """获取作品的 Remix 列表/Fetch post remix list  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 作品的 Remix 列表 - 支持通过作品 ID 或作品链接查询 - 支持分页获取更多 Remix 作品  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - post_id: 作品 ID（可选），格式如 `s_68e466aa780c8191b` - post_url: 作品链接（可选），格式如 `https://sora.chatgpt.com/p/s_68e466aa780c8191b2357907ce7d1a39` - cursor: 翻页参数（可选），从上一次响应的 cursor 字段获取 - **注意**: post_id 和 post_url 至少提供一个  ### 返回: - items: Remix 作品列表     - id: 作品 ID     - text: 作品描述文本     - attachments: 附件列表（视频信息）     - like_count: 点赞数     - view_count: 浏览数     - reply_count: 评论数     - remix_count: 混剪数     - shared_by: 作者用户 ID     - posted_at: 发布时间戳 - cursor: 下一页参数，用于获取更多数据（如果为 null 表示已到末页）  # [English] ### Purpose: - Fetch the Remix list of a Sora post - Supports querying by post ID or post URL - Supports pagination to get more Remix posts  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - post_id: Post ID (optional), format like `s_68e466aa780c8191b` - post_url: Post URL (optional), format like `https://sora.chatgpt.com/p/s_68e466aa780c8191b2357907ce7d1a39` - cursor: Cursor for pagination (optional), obtained from the cursor field of the previous response - **Note**: At least one of post_id or post_url must be provided  ### Return: - items: Remix post list     - id: Post ID     - text: Post description text     - attachments: Attachment list (video info)     - like_count: Like count     - view_count: View count     - reply_count: Comment count     - remix_count: Remix count     - shared_by: Author user ID     - posted_at: Post timestamp - cursor: Next page parameter for fetching more data (null means last page)  # [示例/Example] ```python # 使用作品 ID 查询第一页 post_id = \"s_68e466aa780c8191b\"  # 使用 cursor 获取下一页 cursor = \"eyJsYXN0X3Bvc3RfaWQiOiJzXzY4ZTQ2NmFhNzgwYzgxOTFiIn0=\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_remix_list_api_v1_sora2_get_post_remix_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 作品ID（可选）/Post ID (optional)
        :param object post_url: 作品链接（可选）/Post URL (optional)
        :param object cursor: 翻页参数（可选）/Cursor for pagination (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_post_remix_list_api_v1_sora2_get_post_remix_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_post_remix_list_api_v1_sora2_get_post_remix_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_post_remix_list_api_v1_sora2_get_post_remix_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取作品的 Remix 列表/Fetch post remix list  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 作品的 Remix 列表 - 支持通过作品 ID 或作品链接查询 - 支持分页获取更多 Remix 作品  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - post_id: 作品 ID（可选），格式如 `s_68e466aa780c8191b` - post_url: 作品链接（可选），格式如 `https://sora.chatgpt.com/p/s_68e466aa780c8191b2357907ce7d1a39` - cursor: 翻页参数（可选），从上一次响应的 cursor 字段获取 - **注意**: post_id 和 post_url 至少提供一个  ### 返回: - items: Remix 作品列表     - id: 作品 ID     - text: 作品描述文本     - attachments: 附件列表（视频信息）     - like_count: 点赞数     - view_count: 浏览数     - reply_count: 评论数     - remix_count: 混剪数     - shared_by: 作者用户 ID     - posted_at: 发布时间戳 - cursor: 下一页参数，用于获取更多数据（如果为 null 表示已到末页）  # [English] ### Purpose: - Fetch the Remix list of a Sora post - Supports querying by post ID or post URL - Supports pagination to get more Remix posts  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - post_id: Post ID (optional), format like `s_68e466aa780c8191b` - post_url: Post URL (optional), format like `https://sora.chatgpt.com/p/s_68e466aa780c8191b2357907ce7d1a39` - cursor: Cursor for pagination (optional), obtained from the cursor field of the previous response - **Note**: At least one of post_id or post_url must be provided  ### Return: - items: Remix post list     - id: Post ID     - text: Post description text     - attachments: Attachment list (video info)     - like_count: Like count     - view_count: View count     - reply_count: Comment count     - remix_count: Remix count     - shared_by: Author user ID     - posted_at: Post timestamp - cursor: Next page parameter for fetching more data (null means last page)  # [示例/Example] ```python # 使用作品 ID 查询第一页 post_id = \"s_68e466aa780c8191b\"  # 使用 cursor 获取下一页 cursor = \"eyJsYXN0X3Bvc3RfaWQiOiJzXzY4ZTQ2NmFhNzgwYzgxOTFiIn0=\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_post_remix_list_api_v1_sora2_get_post_remix_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 作品ID（可选）/Post ID (optional)
        :param object post_url: 作品链接（可选）/Post URL (optional)
        :param object cursor: 翻页参数（可选）/Cursor for pagination (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id', 'post_url', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_post_remix_list_api_v1_sora2_get_post_remix_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501
        if 'post_url' in params:
            query_params.append(('post_url', params['post_url']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sora2/get_post_remix_list', 'GET',
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

    def get_task_detail_api_v1_sora2_get_task_detail_get(self, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 获取任务生成的作品详情（无水印版本）/Get task-generated post detail (watermark-free)  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用。AI 相关接口已迁移至独立的 TikHub AI API 服务，与 TikHub 社交媒体 API 分离部署。请访问：https://ai.tikhub.io ### 用途: - **获取视频生成任务的完整作品详情，包含无水印版本的视频链接**  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - task_id: 任务 ID（可选），格式如 `task_01k7e17rnkeh79qnrcdwf5fcfs`     - 从 create_video 接口返回的任务 ID     - 必须以 'task_' 开头 - generation_id: 生成 ID（可选），格式如 `gen_01k7e1bff9eq6rxe9pntk7xdcf`     - 从 get_task_status 接口返回的 generations[0].id     - 必须以 'gen_' 开头 - **注意**: task_id 和 generation_id 至少需要提供一个  ### 返回（无水印完整作品详情）: - post: 作品详细信息     - id: 作品 ID     - text: 作品描述文本     - attachments: 附件列表（**无水印视频信息**）         - **url: 无水印视频链接（原始质量）** ⭐         - downloadable_url: 有水印视频链接         - width/height: 视频尺寸         - encodings: 不同质量的编码版本             - **thumbnail: 缩略图（无水印）**             - **md: 中等质量视频（无水印）**             - **gif: 预览 GIF（无水印）**     - like_count: 点赞数     - view_count: 浏览数     - reply_count: 评论数     - remix_count: 混剪数     - posted_at: 发布时间戳     - permalink: 作品永久链接  ### 注意: - **本接口返回的视频链接是无水印的原始质量版本** - 只有任务状态为 succeeded 时才能成功调用 - 如果任务未完成，会返回相应的错误信息 - 推荐使用 generation_id 参数 - 视频链接有时效性，建议及时下载  # [English] ## ⚠️ This endpoint has been deprecated. AI-related endpoints have been migrated to a dedicated TikHub AI API service, which operates separately from the TikHub Social Media API. Please visit: https://ai.tikhub.io ### Purpose: - **Get complete post details of video generation task, including watermark-free video links**  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - task_id: Task ID (optional), format like `task_01k7e17rnkeh79qnrcdwf5fcfs`     - Task ID returned from create_video endpoint     - Must start with 'task_' - generation_id: Generation ID (optional), format like `gen_01k7e1bff9eq6rxe9pntk7xdcf`     - Get from generations[0].id returned by get_task_status endpoint     - Must start with 'gen_' - **Note**: At least one of task_id or generation_id must be provided  ### Return (Watermark-free Complete Post Details): - post: Post detailed information     - id: Post ID     - text: Post description text     - attachments: Attachment list (**Watermark-free video info**)         - **url: Watermark-free video link (original quality)** ⭐         - downloadable_url: Watermarked video link         - width/height: Video dimensions         - encodings: Different quality encoding versions             - **thumbnail: Thumbnail (watermark-free)**             - **md: Medium quality video (watermark-free)**             - **gif: Preview GIF (watermark-free)**     - like_count: Like count     - view_count: View count     - reply_count: Comment count     - remix_count: Remix count     - posted_at: Post timestamp     - permalink: Permanent link  ### Note: - **This endpoint returns watermark-free original quality video links** - Can only be called successfully when task status is succeeded - Will return error message if task is not completed - Recommend using task_id parameter, will auto-fetch required generation_id - Video links have expiration time, recommend downloading promptly  # [示例/Example] ```python # 返回示例 (无水印完整信息) # Return example (watermark-free complete info) {    \"post\":{       \"id\":\"s_68ecb45b40988191b89a0af80135a33c\",       \"posted_to_public\":false,       \"posted_at\":1760343131.252443,       \"updated_at\":1760343140.655776,       \"like_count\":0,       \"recursive_reply_count\":0,       \"reply_count\":0,       \"view_count\":0,       \"unique_view_count\":0,       \"remix_count\":0,       \"user_liked\":false,       \"source\":\"sy\",       \"text\":\"A cat is playing Minecraft\",       \"caption\":null,       \"cover_photo_url\":null,       \"preview_image_url\":\"https://ogimg.chatgpt.com/?postId=s_68ecb45b40988191b89a0af80135a33c\",       \"attachments\":[          {             \"id\":\"s_68ecb45b40988191b89a0af80135a33c-attachment-0\",             \"tags\":[                \"sora\"             ],             \"kind\":\"sora\",             \"generation_id\":\"gen_01k7e9yzk2e4vr88ykfbtpz1ka\",             \"generation_type\":\"video_gen\",             \"url\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=NOaGqX50rV7s4Rrmpk8s0eJoHlhS3WHagn0Cz1wuDAM%3D&az=oaivgprodscus\",             \"downloadable_url\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000_wm%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=xiYmjG29NvQi9t5BGqu0tHl2%2BnRoA8eLNssPbLzmTxI%3D&az=oaivgprodscus\",             \"width\":352,             \"height\":640,             \"prompt\":null,             \"task_id\":null,             \"output_blocked\":false,             \"title\":null,             \"source\":null,             \"encodings\":{                \"source\":{                   \"path\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=NOaGqX50rV7s4Rrmpk8s0eJoHlhS3WHagn0Cz1wuDAM%3D&az=oaivgprodscus\"                },                \"source_wm\":{                   \"path\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000_wm%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=xiYmjG29NvQi9t5BGqu0tHl2%2BnRoA8eLNssPbLzmTxI%3D&az=oaivgprodscus\"                },                \"thumbnail\":{                   \"path\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fthumbnail.webp?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=qKQRiyaELAV9lr5B0mJ89vvHSptRXWrAvZHvSPLfBjc%3D&az=oaivgprodscus\"                },                \"unfurl\":null,                \"md\":{                   \"path\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fmd.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=%2FlBkZ6aqa8z6vwP2x%2FDezkCuM65t%2FM5vtglAEv85v5U%3D&az=oaivgprodscus\"                },                \"gif\":{                   \"path\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fpreview.gif?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=mZsaMyviqaR13sMjZ3W8GAuFPHCYQA2BcPS5jwnIaDg%3D&az=oaivgprodscus\"                }             },             \"asset_pointer\":null,             \"conversation_id\":null          }       ],       \"parent_post_id\":null,       \"root_post_id\":null,       \"parent_path\":null,       \"tombstoned_at\":null,       \"permalink\":\"https://sora.chatgpt.com/p/s_68ecb45b40988191b89a0af80135a33c\",       \"text_facets\":[        ],       \"cameo_profiles\":null,       \"disabled_cameo_user_ids\":null,       \"groups\":[        ],       \"user_disliked\":false,       \"verifications\":[        ],       \"dislike_count\":0,       \"remix_posts\":{          \"items\":[           ],          \"cursor\":null       },       \"ancestors\":{          \"items\":[           ],          \"cursor\":null       },       \"parent_post\":null,       \"emoji\":\"🐱‍💻\",       \"is_featured\":null    } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_task_detail_api_v1_sora2_get_task_detail_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object task_id: 任务ID（可选，与generation_id二选一）/Task ID (optional, choose one with generation_id)
        :param object generation_id: 生成ID（可选，与task_id二选一）/Generation ID (optional, choose one with task_id)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_task_detail_api_v1_sora2_get_task_detail_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_task_detail_api_v1_sora2_get_task_detail_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_task_detail_api_v1_sora2_get_task_detail_get_with_http_info(self, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 获取任务生成的作品详情（无水印版本）/Get task-generated post detail (watermark-free)  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用。AI 相关接口已迁移至独立的 TikHub AI API 服务，与 TikHub 社交媒体 API 分离部署。请访问：https://ai.tikhub.io ### 用途: - **获取视频生成任务的完整作品详情，包含无水印版本的视频链接**  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - task_id: 任务 ID（可选），格式如 `task_01k7e17rnkeh79qnrcdwf5fcfs`     - 从 create_video 接口返回的任务 ID     - 必须以 'task_' 开头 - generation_id: 生成 ID（可选），格式如 `gen_01k7e1bff9eq6rxe9pntk7xdcf`     - 从 get_task_status 接口返回的 generations[0].id     - 必须以 'gen_' 开头 - **注意**: task_id 和 generation_id 至少需要提供一个  ### 返回（无水印完整作品详情）: - post: 作品详细信息     - id: 作品 ID     - text: 作品描述文本     - attachments: 附件列表（**无水印视频信息**）         - **url: 无水印视频链接（原始质量）** ⭐         - downloadable_url: 有水印视频链接         - width/height: 视频尺寸         - encodings: 不同质量的编码版本             - **thumbnail: 缩略图（无水印）**             - **md: 中等质量视频（无水印）**             - **gif: 预览 GIF（无水印）**     - like_count: 点赞数     - view_count: 浏览数     - reply_count: 评论数     - remix_count: 混剪数     - posted_at: 发布时间戳     - permalink: 作品永久链接  ### 注意: - **本接口返回的视频链接是无水印的原始质量版本** - 只有任务状态为 succeeded 时才能成功调用 - 如果任务未完成，会返回相应的错误信息 - 推荐使用 generation_id 参数 - 视频链接有时效性，建议及时下载  # [English] ## ⚠️ This endpoint has been deprecated. AI-related endpoints have been migrated to a dedicated TikHub AI API service, which operates separately from the TikHub Social Media API. Please visit: https://ai.tikhub.io ### Purpose: - **Get complete post details of video generation task, including watermark-free video links**  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - task_id: Task ID (optional), format like `task_01k7e17rnkeh79qnrcdwf5fcfs`     - Task ID returned from create_video endpoint     - Must start with 'task_' - generation_id: Generation ID (optional), format like `gen_01k7e1bff9eq6rxe9pntk7xdcf`     - Get from generations[0].id returned by get_task_status endpoint     - Must start with 'gen_' - **Note**: At least one of task_id or generation_id must be provided  ### Return (Watermark-free Complete Post Details): - post: Post detailed information     - id: Post ID     - text: Post description text     - attachments: Attachment list (**Watermark-free video info**)         - **url: Watermark-free video link (original quality)** ⭐         - downloadable_url: Watermarked video link         - width/height: Video dimensions         - encodings: Different quality encoding versions             - **thumbnail: Thumbnail (watermark-free)**             - **md: Medium quality video (watermark-free)**             - **gif: Preview GIF (watermark-free)**     - like_count: Like count     - view_count: View count     - reply_count: Comment count     - remix_count: Remix count     - posted_at: Post timestamp     - permalink: Permanent link  ### Note: - **This endpoint returns watermark-free original quality video links** - Can only be called successfully when task status is succeeded - Will return error message if task is not completed - Recommend using task_id parameter, will auto-fetch required generation_id - Video links have expiration time, recommend downloading promptly  # [示例/Example] ```python # 返回示例 (无水印完整信息) # Return example (watermark-free complete info) {    \"post\":{       \"id\":\"s_68ecb45b40988191b89a0af80135a33c\",       \"posted_to_public\":false,       \"posted_at\":1760343131.252443,       \"updated_at\":1760343140.655776,       \"like_count\":0,       \"recursive_reply_count\":0,       \"reply_count\":0,       \"view_count\":0,       \"unique_view_count\":0,       \"remix_count\":0,       \"user_liked\":false,       \"source\":\"sy\",       \"text\":\"A cat is playing Minecraft\",       \"caption\":null,       \"cover_photo_url\":null,       \"preview_image_url\":\"https://ogimg.chatgpt.com/?postId=s_68ecb45b40988191b89a0af80135a33c\",       \"attachments\":[          {             \"id\":\"s_68ecb45b40988191b89a0af80135a33c-attachment-0\",             \"tags\":[                \"sora\"             ],             \"kind\":\"sora\",             \"generation_id\":\"gen_01k7e9yzk2e4vr88ykfbtpz1ka\",             \"generation_type\":\"video_gen\",             \"url\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=NOaGqX50rV7s4Rrmpk8s0eJoHlhS3WHagn0Cz1wuDAM%3D&az=oaivgprodscus\",             \"downloadable_url\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000_wm%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=xiYmjG29NvQi9t5BGqu0tHl2%2BnRoA8eLNssPbLzmTxI%3D&az=oaivgprodscus\",             \"width\":352,             \"height\":640,             \"prompt\":null,             \"task_id\":null,             \"output_blocked\":false,             \"title\":null,             \"source\":null,             \"encodings\":{                \"source\":{                   \"path\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=NOaGqX50rV7s4Rrmpk8s0eJoHlhS3WHagn0Cz1wuDAM%3D&az=oaivgprodscus\"                },                \"source_wm\":{                   \"path\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000_wm%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=xiYmjG29NvQi9t5BGqu0tHl2%2BnRoA8eLNssPbLzmTxI%3D&az=oaivgprodscus\"                },                \"thumbnail\":{                   \"path\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fthumbnail.webp?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=qKQRiyaELAV9lr5B0mJ89vvHSptRXWrAvZHvSPLfBjc%3D&az=oaivgprodscus\"                },                \"unfurl\":null,                \"md\":{                   \"path\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fmd.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=%2FlBkZ6aqa8z6vwP2x%2FDezkCuM65t%2FM5vtglAEv85v5U%3D&az=oaivgprodscus\"                },                \"gif\":{                   \"path\":\"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fpreview.gif?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=mZsaMyviqaR13sMjZ3W8GAuFPHCYQA2BcPS5jwnIaDg%3D&az=oaivgprodscus\"                }             },             \"asset_pointer\":null,             \"conversation_id\":null          }       ],       \"parent_post_id\":null,       \"root_post_id\":null,       \"parent_path\":null,       \"tombstoned_at\":null,       \"permalink\":\"https://sora.chatgpt.com/p/s_68ecb45b40988191b89a0af80135a33c\",       \"text_facets\":[        ],       \"cameo_profiles\":null,       \"disabled_cameo_user_ids\":null,       \"groups\":[        ],       \"user_disliked\":false,       \"verifications\":[        ],       \"dislike_count\":0,       \"remix_posts\":{          \"items\":[           ],          \"cursor\":null       },       \"ancestors\":{          \"items\":[           ],          \"cursor\":null       },       \"parent_post\":null,       \"emoji\":\"🐱‍💻\",       \"is_featured\":null    } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_task_detail_api_v1_sora2_get_task_detail_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object task_id: 任务ID（可选，与generation_id二选一）/Task ID (optional, choose one with generation_id)
        :param object generation_id: 生成ID（可选，与task_id二选一）/Generation ID (optional, choose one with task_id)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id', 'generation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task_detail_api_v1_sora2_get_task_detail_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in params:
            query_params.append(('task_id', params['task_id']))  # noqa: E501
        if 'generation_id' in params:
            query_params.append(('generation_id', params['generation_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sora2/get_task_detail', 'GET',
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

    def get_task_status_api_v1_sora2_get_task_status_get(self, task_id, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 查询任务状态/Get task status  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用。AI 相关接口已迁移至独立的 TikHub AI API 服务，与 TikHub 社交媒体 API 分离部署。请访问：https://ai.tikhub.io ### 用途: - 查询视频生成任务的当前状态和结果 - 用于轮询检查视频生成进度 - 任务完成后可获取生成的视频信息（包括 generation_id） - 配合 create_video 接口使用，用于获取异步生成的视频结果  ### 收费说明: - 本接口完全免费，不消耗任何费用 - 速率限制：每秒最多请求 1 次（1 request/second） - 如果请求过快可能会被限流，建议间隔至少 1 秒  ### 参数: - task_id: 任务 ID，必填，格式如 `task_01k7dttf0xfx3t7zhhzycjq8e3`     - 从 create_video 接口返回的任务 ID     - 必须以 'task_' 开头  ### 返回: - id: 任务 ID - status: 任务状态     - queued: 排队中     - processing: 处理中     - succeeded: 已完成     - failed: 失败 - prompt: 视频生成时使用的文本描述 - title: 视频标题（如果有） - progress_pct: 任务进度（0.0-1.0，1.0 表示 100%） - generations: 生成结果数组（任务完成后才有）     - id: 生成 ID（generation_id，格式：gen_xxxxxx）     - kind: 类型（如 sora_draft）     - url: 视频链接（有水印）     - downloadable_url: 下载链接（有水印）     - width: 视频宽度     - height: 视频高度     - created_at: 创建时间戳     - prompt: 生成提示词     - encodings: 不同质量的编码版本         - source: 源文件         - source_wm: 带水印的源文件         - thumbnail: 缩略图         - md: 中等质量视频         - gif: 预览 GIF  ### 注意: - **速率限制**: 本接口每秒最多请求 1 次，建议轮询间隔设置为 1-2 秒 - 建议每 1-2 秒轮询一次，直到 status 变为 succeeded 或 failed - 只有 status 为 succeeded 时，generations 数组才会包含视频数据 - **重要**: 本接口返回的视频链接**只包含有水印的版本** - **获取无水印视频**: 当任务成功后，需要使用 task_id 或 generation_id 调用 `get_task_detail` 接口才能获取**无水印版本** - 从 generations[0].id 可以获取 generation_id，用于后续调用 get_task_detail 接口  # [English] ## ⚠️ This endpoint has been deprecated. AI-related endpoints have been migrated to a dedicated TikHub AI API service, which operates separately from the TikHub Social Media API. Please visit: https://ai.tikhub.io ### Purpose: - Query current status and results of video generation task - Used to poll and check video generation progress - Get generated video information (including generation_id) after task completion - Use with create_video endpoint to get asynchronously generated video results  ### Pricing: - This API is completely free, no charges - Rate limit: Maximum 1 request per second (1 request/second) - Requests may be throttled if too frequent, recommend at least 1 second interval  ### Parameters: - task_id: Task ID, required, format like `task_01k7dttf0xfx3t7zhhzycjq8e3`     - Task ID returned from create_video endpoint     - Must start with 'task_'  ### Return: - id: Task ID - status: Task status     - queued: Queued     - processing: Processing     - succeeded: Completed     - failed: Failed - prompt: Text description used for video generation - title: Video title (if any) - progress_pct: Task progress (0.0-1.0, 1.0 means 100%) - generations: Generation result array (available after task completion)     - id: Generation ID (generation_id, format: gen_xxxxxx)     - kind: Type (e.g., sora_draft)     - url: Video link (with watermark)     - downloadable_url: Download link (with watermark)     - width: Video width     - height: Video height     - created_at: Creation timestamp     - prompt: Generation prompt     - encodings: Different quality encoding versions         - source: Source file         - source_wm: Source file with watermark         - thumbnail: Thumbnail         - md: Medium quality video         - gif: Preview GIF  ### Note: - **Rate limit**: Maximum 1 request per second, recommend polling interval of 1-2 seconds - Recommend polling every 1-2 seconds until status becomes succeeded or failed - Only when status is succeeded, generations array will contain video data - **Important**: This endpoint returns video links **with watermark only** - **Get watermark-free video**: After task succeeds, use task_id or generation_id to call `get_task_detail` endpoint to get **watermark-free version** - Get generation_id from generations[0].id for subsequent get_task_detail API call  # [示例/Example] ```python # 返回示例（任务进行中） # Return example (task in progress) {     \"id\": \"task_01k7dttf0xfx3t7zhhzycjq8e3\",     \"status\": \"processing\",     \"prompt\": \"A cat playing Minecraft\",     \"progress_pct\": 0.45 }  # 返回示例（任务完成） # Return example (task completed) {     \"id\": \"task_01k7dttf0xfx3t7zhhzycjq8e3\",     \"status\": \"succeeded\",     \"prompt\": \"A cat playing Minecraft\",     \"progress_pct\": 1.0,     \"generations\": [         {             \"id\": \"gen_01k7e1bff9eq6rxe9pntk7xdcf\",             \"kind\": \"sora_draft\",             \"url\": \"https://videos.openai.com/...\",             \"width\": 640,             \"height\": 352,             \"encodings\": {                 \"thumbnail\": {\"path\": \"https://...\"},                 \"gif\": {\"path\": \"https://...\"}             }         }     ] } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_task_status_api_v1_sora2_get_task_status_get(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object task_id: 任务ID（从create_video返回）/Task ID (returned from create_video) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_task_status_api_v1_sora2_get_task_status_get_with_http_info(task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_task_status_api_v1_sora2_get_task_status_get_with_http_info(task_id, **kwargs)  # noqa: E501
            return data

    def get_task_status_api_v1_sora2_get_task_status_get_with_http_info(self, task_id, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 查询任务状态/Get task status  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用。AI 相关接口已迁移至独立的 TikHub AI API 服务，与 TikHub 社交媒体 API 分离部署。请访问：https://ai.tikhub.io ### 用途: - 查询视频生成任务的当前状态和结果 - 用于轮询检查视频生成进度 - 任务完成后可获取生成的视频信息（包括 generation_id） - 配合 create_video 接口使用，用于获取异步生成的视频结果  ### 收费说明: - 本接口完全免费，不消耗任何费用 - 速率限制：每秒最多请求 1 次（1 request/second） - 如果请求过快可能会被限流，建议间隔至少 1 秒  ### 参数: - task_id: 任务 ID，必填，格式如 `task_01k7dttf0xfx3t7zhhzycjq8e3`     - 从 create_video 接口返回的任务 ID     - 必须以 'task_' 开头  ### 返回: - id: 任务 ID - status: 任务状态     - queued: 排队中     - processing: 处理中     - succeeded: 已完成     - failed: 失败 - prompt: 视频生成时使用的文本描述 - title: 视频标题（如果有） - progress_pct: 任务进度（0.0-1.0，1.0 表示 100%） - generations: 生成结果数组（任务完成后才有）     - id: 生成 ID（generation_id，格式：gen_xxxxxx）     - kind: 类型（如 sora_draft）     - url: 视频链接（有水印）     - downloadable_url: 下载链接（有水印）     - width: 视频宽度     - height: 视频高度     - created_at: 创建时间戳     - prompt: 生成提示词     - encodings: 不同质量的编码版本         - source: 源文件         - source_wm: 带水印的源文件         - thumbnail: 缩略图         - md: 中等质量视频         - gif: 预览 GIF  ### 注意: - **速率限制**: 本接口每秒最多请求 1 次，建议轮询间隔设置为 1-2 秒 - 建议每 1-2 秒轮询一次，直到 status 变为 succeeded 或 failed - 只有 status 为 succeeded 时，generations 数组才会包含视频数据 - **重要**: 本接口返回的视频链接**只包含有水印的版本** - **获取无水印视频**: 当任务成功后，需要使用 task_id 或 generation_id 调用 `get_task_detail` 接口才能获取**无水印版本** - 从 generations[0].id 可以获取 generation_id，用于后续调用 get_task_detail 接口  # [English] ## ⚠️ This endpoint has been deprecated. AI-related endpoints have been migrated to a dedicated TikHub AI API service, which operates separately from the TikHub Social Media API. Please visit: https://ai.tikhub.io ### Purpose: - Query current status and results of video generation task - Used to poll and check video generation progress - Get generated video information (including generation_id) after task completion - Use with create_video endpoint to get asynchronously generated video results  ### Pricing: - This API is completely free, no charges - Rate limit: Maximum 1 request per second (1 request/second) - Requests may be throttled if too frequent, recommend at least 1 second interval  ### Parameters: - task_id: Task ID, required, format like `task_01k7dttf0xfx3t7zhhzycjq8e3`     - Task ID returned from create_video endpoint     - Must start with 'task_'  ### Return: - id: Task ID - status: Task status     - queued: Queued     - processing: Processing     - succeeded: Completed     - failed: Failed - prompt: Text description used for video generation - title: Video title (if any) - progress_pct: Task progress (0.0-1.0, 1.0 means 100%) - generations: Generation result array (available after task completion)     - id: Generation ID (generation_id, format: gen_xxxxxx)     - kind: Type (e.g., sora_draft)     - url: Video link (with watermark)     - downloadable_url: Download link (with watermark)     - width: Video width     - height: Video height     - created_at: Creation timestamp     - prompt: Generation prompt     - encodings: Different quality encoding versions         - source: Source file         - source_wm: Source file with watermark         - thumbnail: Thumbnail         - md: Medium quality video         - gif: Preview GIF  ### Note: - **Rate limit**: Maximum 1 request per second, recommend polling interval of 1-2 seconds - Recommend polling every 1-2 seconds until status becomes succeeded or failed - Only when status is succeeded, generations array will contain video data - **Important**: This endpoint returns video links **with watermark only** - **Get watermark-free video**: After task succeeds, use task_id or generation_id to call `get_task_detail` endpoint to get **watermark-free version** - Get generation_id from generations[0].id for subsequent get_task_detail API call  # [示例/Example] ```python # 返回示例（任务进行中） # Return example (task in progress) {     \"id\": \"task_01k7dttf0xfx3t7zhhzycjq8e3\",     \"status\": \"processing\",     \"prompt\": \"A cat playing Minecraft\",     \"progress_pct\": 0.45 }  # 返回示例（任务完成） # Return example (task completed) {     \"id\": \"task_01k7dttf0xfx3t7zhhzycjq8e3\",     \"status\": \"succeeded\",     \"prompt\": \"A cat playing Minecraft\",     \"progress_pct\": 1.0,     \"generations\": [         {             \"id\": \"gen_01k7e1bff9eq6rxe9pntk7xdcf\",             \"kind\": \"sora_draft\",             \"url\": \"https://videos.openai.com/...\",             \"width\": 640,             \"height\": 352,             \"encodings\": {                 \"thumbnail\": {\"path\": \"https://...\"},                 \"gif\": {\"path\": \"https://...\"}             }         }     ] } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_task_status_api_v1_sora2_get_task_status_get_with_http_info(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object task_id: 任务ID（从create_video返回）/Task ID (returned from create_video) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task_status_api_v1_sora2_get_task_status_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in params or
                                                       params['task_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `task_id` when calling `get_task_status_api_v1_sora2_get_task_status_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in params:
            query_params.append(('task_id', params['task_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sora2/get_task_status', 'GET',
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

    def get_user_cameo_appearances_api_v1_sora2_get_user_cameo_appearances_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户Cameo出镜秀列表/Fetch user cameo appearances  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 用户的 Cameo 出镜秀列表 - Cameo 出镜秀指该用户在其他创作者作品中的出镜视频 - 支持分页加载，每页返回 30 条记录 - 可用于展示用户的协作作品、出镜记录等  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - user_id: 用户 ID，必填 - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - items: Cameo 出镜秀列表（30条/页）     - post: 作品信息（该用户出镜的作品）         - id: 作品 ID         - text: 作品描述         - attachments: 视频附件信息         - like_count: 点赞数         - view_count: 浏览数         - shared_by: 原创作者 ID         - posted_at: 发布时间戳     - profile: 原创作者信息 - cursor: 下一页参数（用于获取更多记录，无更多时为 null） - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch Sora user's Cameo appearance list - Cameo appearances refer to videos where the user appears in other creators' works - Supports pagination, returns 30 records per page - Can be used to display user's collaborative works, appearance records, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - user_id: User ID, required - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - items: Cameo appearance list (30 items/page)     - post: Post information (works where the user appears)         - id: Post ID         - text: Post description         - attachments: Video attachment info         - like_count: Like count         - view_count: View count         - shared_by: Original creator ID         - posted_at: Post timestamp     - profile: Original creator information - cursor: Next page cursor (for loading more records, null when no more) - has_more: Whether there are more data  # [示例/Example] ```python # 获取用户的 Cameo 出镜秀 user_id = \"user-xiCyLclE6KJcdTXyvVq3Ontc\" cursor = \"\"  # 首次请求留空  # 返回该用户在其他人作品中的出镜记录 ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_cameo_appearances_api_v1_sora2_get_user_cameo_appearances_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_cameo_appearances_api_v1_sora2_get_user_cameo_appearances_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_cameo_appearances_api_v1_sora2_get_user_cameo_appearances_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_cameo_appearances_api_v1_sora2_get_user_cameo_appearances_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户Cameo出镜秀列表/Fetch user cameo appearances  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 用户的 Cameo 出镜秀列表 - Cameo 出镜秀指该用户在其他创作者作品中的出镜视频 - 支持分页加载，每页返回 30 条记录 - 可用于展示用户的协作作品、出镜记录等  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - user_id: 用户 ID，必填 - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - items: Cameo 出镜秀列表（30条/页）     - post: 作品信息（该用户出镜的作品）         - id: 作品 ID         - text: 作品描述         - attachments: 视频附件信息         - like_count: 点赞数         - view_count: 浏览数         - shared_by: 原创作者 ID         - posted_at: 发布时间戳     - profile: 原创作者信息 - cursor: 下一页参数（用于获取更多记录，无更多时为 null） - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch Sora user's Cameo appearance list - Cameo appearances refer to videos where the user appears in other creators' works - Supports pagination, returns 30 records per page - Can be used to display user's collaborative works, appearance records, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - user_id: User ID, required - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - items: Cameo appearance list (30 items/page)     - post: Post information (works where the user appears)         - id: Post ID         - text: Post description         - attachments: Video attachment info         - like_count: Like count         - view_count: View count         - shared_by: Original creator ID         - posted_at: Post timestamp     - profile: Original creator information - cursor: Next page cursor (for loading more records, null when no more) - has_more: Whether there are more data  # [示例/Example] ```python # 获取用户的 Cameo 出镜秀 user_id = \"user-xiCyLclE6KJcdTXyvVq3Ontc\" cursor = \"\"  # 首次请求留空  # 返回该用户在其他人作品中的出镜记录 ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_cameo_appearances_api_v1_sora2_get_user_cameo_appearances_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
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
                    " to method get_user_cameo_appearances_api_v1_sora2_get_user_cameo_appearances_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_cameo_appearances_api_v1_sora2_get_user_cameo_appearances_get`")  # noqa: E501

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
            '/api/v1/sora2/get_user_cameo_appearances', 'GET',
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

    def get_user_followers_api_v1_sora2_get_user_followers_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Fetch user followers  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 用户的粉丝列表 - 支持分页加载，每页返回 50 个粉丝 - 可用于粉丝关系分析、社交网络研究等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - user_id: 用户 ID，必填 - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - items: 粉丝列表（50个/页）     - user_id: 粉丝用户 ID     - username: 粉丝用户名     - display_name: 粉丝显示名称     - profile_picture_url: 粉丝头像链接     - follower_count: 粉丝的粉丝数     - following_count: 粉丝的关注数     - bio: 粉丝个人简介     - is_verified: 是否认证用户 - cursor: 下一页参数（用于获取更多粉丝，无更多时为 null） - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch Sora user's follower list - Supports pagination, returns 50 followers per page - Can be used for follower relationship analysis, social network research, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - user_id: User ID, required - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - items: Follower list (50 items/page)     - user_id: Follower user ID     - username: Follower username     - display_name: Follower display name     - profile_picture_url: Follower avatar URL     - follower_count: Follower's follower count     - following_count: Follower's following count     - bio: Follower biography     - is_verified: Whether verified user - cursor: Next page cursor (for loading more followers, null when no more) - has_more: Whether there are more data  # [示例/Example] ```python # 第一次请求（获取前 50 个粉丝） user_id = \"user-xiCyLclE6KJcdTXyvVq3Ontc\" cursor = \"\"  # 首次请求留空  # 第二次请求（获取下一页） cursor = \"eyJ1c2VyX2lkIjoidXNlci14aUN5TGNsRTZLSmNkVFh5dlZxM09udGMi...\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_followers_api_v1_sora2_get_user_followers_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_followers_api_v1_sora2_get_user_followers_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_followers_api_v1_sora2_get_user_followers_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_followers_api_v1_sora2_get_user_followers_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Fetch user followers  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 用户的粉丝列表 - 支持分页加载，每页返回 50 个粉丝 - 可用于粉丝关系分析、社交网络研究等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - user_id: 用户 ID，必填 - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - items: 粉丝列表（50个/页）     - user_id: 粉丝用户 ID     - username: 粉丝用户名     - display_name: 粉丝显示名称     - profile_picture_url: 粉丝头像链接     - follower_count: 粉丝的粉丝数     - following_count: 粉丝的关注数     - bio: 粉丝个人简介     - is_verified: 是否认证用户 - cursor: 下一页参数（用于获取更多粉丝，无更多时为 null） - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch Sora user's follower list - Supports pagination, returns 50 followers per page - Can be used for follower relationship analysis, social network research, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - user_id: User ID, required - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - items: Follower list (50 items/page)     - user_id: Follower user ID     - username: Follower username     - display_name: Follower display name     - profile_picture_url: Follower avatar URL     - follower_count: Follower's follower count     - following_count: Follower's following count     - bio: Follower biography     - is_verified: Whether verified user - cursor: Next page cursor (for loading more followers, null when no more) - has_more: Whether there are more data  # [示例/Example] ```python # 第一次请求（获取前 50 个粉丝） user_id = \"user-xiCyLclE6KJcdTXyvVq3Ontc\" cursor = \"\"  # 首次请求留空  # 第二次请求（获取下一页） cursor = \"eyJ1c2VyX2lkIjoidXNlci14aUN5TGNsRTZLSmNkVFh5dlZxM09udGMi...\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_followers_api_v1_sora2_get_user_followers_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
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
                    " to method get_user_followers_api_v1_sora2_get_user_followers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_followers_api_v1_sora2_get_user_followers_get`")  # noqa: E501

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
            '/api/v1/sora2/get_user_followers', 'GET',
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

    def get_user_following_api_v1_sora2_get_user_following_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户关注列表/Fetch user following  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 用户的关注列表（用户关注的其他人） - 支持分页加载，每页返回 50 个关注对象 - 可用于关注关系分析、推荐算法等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - user_id: 用户 ID，必填 - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - items: 关注列表（50个/页）     - user_id: 被关注用户 ID     - username: 被关注用户名     - display_name: 被关注用户显示名称     - profile_picture_url: 被关注用户头像链接     - follower_count: 被关注用户的粉丝数     - following_count: 被关注用户的关注数     - bio: 被关注用户个人简介     - is_verified: 是否认证用户 - cursor: 下一页参数（用于获取更多关注，无更多时为 null） - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch Sora user's following list (users that the user follows) - Supports pagination, returns 50 following per page - Can be used for following relationship analysis, recommendation algorithms, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - user_id: User ID, required - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - items: Following list (50 items/page)     - user_id: Followed user ID     - username: Followed username     - display_name: Followed display name     - profile_picture_url: Followed avatar URL     - follower_count: Followed user's follower count     - following_count: Followed user's following count     - bio: Followed user biography     - is_verified: Whether verified user - cursor: Next page cursor (for loading more following, null when no more) - has_more: Whether there are more data  # [示例/Example] ```python # 第一次请求（获取前 50 个关注） user_id = \"user-BOXD64QrAyZVybLCeXTqJWm3\" cursor = \"\"  # 首次请求留空  # 第二次请求（获取下一页） cursor = \"eyJ1c2VyX2lkIjoidXNlci1CT1hENjRRckF5WlZ5YkxDZVhUcUpXbTMi...\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_following_api_v1_sora2_get_user_following_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_following_api_v1_sora2_get_user_following_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_following_api_v1_sora2_get_user_following_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_following_api_v1_sora2_get_user_following_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户关注列表/Fetch user following  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 用户的关注列表（用户关注的其他人） - 支持分页加载，每页返回 50 个关注对象 - 可用于关注关系分析、推荐算法等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - user_id: 用户 ID，必填 - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - items: 关注列表（50个/页）     - user_id: 被关注用户 ID     - username: 被关注用户名     - display_name: 被关注用户显示名称     - profile_picture_url: 被关注用户头像链接     - follower_count: 被关注用户的粉丝数     - following_count: 被关注用户的关注数     - bio: 被关注用户个人简介     - is_verified: 是否认证用户 - cursor: 下一页参数（用于获取更多关注，无更多时为 null） - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch Sora user's following list (users that the user follows) - Supports pagination, returns 50 following per page - Can be used for following relationship analysis, recommendation algorithms, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - user_id: User ID, required - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - items: Following list (50 items/page)     - user_id: Followed user ID     - username: Followed username     - display_name: Followed display name     - profile_picture_url: Followed avatar URL     - follower_count: Followed user's follower count     - following_count: Followed user's following count     - bio: Followed user biography     - is_verified: Whether verified user - cursor: Next page cursor (for loading more following, null when no more) - has_more: Whether there are more data  # [示例/Example] ```python # 第一次请求（获取前 50 个关注） user_id = \"user-BOXD64QrAyZVybLCeXTqJWm3\" cursor = \"\"  # 首次请求留空  # 第二次请求（获取下一页） cursor = \"eyJ1c2VyX2lkIjoidXNlci1CT1hENjRRckF5WlZ5YkxDZVhUcUpXbTMi...\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_following_api_v1_sora2_get_user_following_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
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
                    " to method get_user_following_api_v1_sora2_get_user_following_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_following_api_v1_sora2_get_user_following_get`")  # noqa: E501

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
            '/api/v1/sora2/get_user_following', 'GET',
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

    def get_user_posts_api_v1_sora2_get_user_posts_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户发布的帖子列表/Fetch user posts  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 用户发布的作品列表 - 支持分页加载，每页返回 30 条作品 - 可用于用户主页展示、作品数据采集等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - user_id: 用户 ID，必填 - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - items: 作品列表（30条/页）     - post: 作品信息         - id: 作品 ID         - text: 作品描述         - attachments: 视频附件信息         - like_count: 点赞数         - view_count: 浏览数         - reply_count: 评论数         - posted_at: 发布时间戳     - profile: 作者信息 - cursor: 下一页参数（用于获取更多作品，无更多时为 null） - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch list of posts published by a Sora user - Supports pagination, returns 30 posts per page - Can be used for user homepage display, post data collection, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - user_id: User ID, required - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - items: Post list (30 items/page)     - post: Post information         - id: Post ID         - text: Post description         - attachments: Video attachment info         - like_count: Like count         - view_count: View count         - reply_count: Comment count         - posted_at: Post timestamp     - profile: Author information - cursor: Next page cursor (for loading more posts, null when no more) - has_more: Whether there are more data  # [示例/Example] ```python # 第一次请求（获取前 30 条作品） user_id = \"user-xiCyLclE6KJcdTXyvVq3Ontc\" cursor = \"\"  # 首次请求留空  # 第二次请求（获取下一页） cursor = \"eyJ1c2VyX2lkIjoidXNlci14aUN5TGNsRTZLSmNkVFh5dlZxM09udGMi...\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_posts_api_v1_sora2_get_user_posts_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_posts_api_v1_sora2_get_user_posts_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_posts_api_v1_sora2_get_user_posts_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_posts_api_v1_sora2_get_user_posts_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户发布的帖子列表/Fetch user posts  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 用户发布的作品列表 - 支持分页加载，每页返回 30 条作品 - 可用于用户主页展示、作品数据采集等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - user_id: 用户 ID，必填 - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值  ### 返回: - items: 作品列表（30条/页）     - post: 作品信息         - id: 作品 ID         - text: 作品描述         - attachments: 视频附件信息         - like_count: 点赞数         - view_count: 浏览数         - reply_count: 评论数         - posted_at: 发布时间戳     - profile: 作者信息 - cursor: 下一页参数（用于获取更多作品，无更多时为 null） - has_more: 是否有更多数据  # [English] ### Purpose: - Fetch list of posts published by a Sora user - Supports pagination, returns 30 posts per page - Can be used for user homepage display, post data collection, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - user_id: User ID, required - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests  ### Return: - items: Post list (30 items/page)     - post: Post information         - id: Post ID         - text: Post description         - attachments: Video attachment info         - like_count: Like count         - view_count: View count         - reply_count: Comment count         - posted_at: Post timestamp     - profile: Author information - cursor: Next page cursor (for loading more posts, null when no more) - has_more: Whether there are more data  # [示例/Example] ```python # 第一次请求（获取前 30 条作品） user_id = \"user-xiCyLclE6KJcdTXyvVq3Ontc\" cursor = \"\"  # 首次请求留空  # 第二次请求（获取下一页） cursor = \"eyJ1c2VyX2lkIjoidXNlci14aUN5TGNsRTZLSmNkVFh5dlZxM09udGMi...\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_posts_api_v1_sora2_get_user_posts_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页参数，从上一次响应中获取/Pagination cursor from previous response
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
                    " to method get_user_posts_api_v1_sora2_get_user_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_posts_api_v1_sora2_get_user_posts_get`")  # noqa: E501

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
            '/api/v1/sora2/get_user_posts', 'GET',
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

    def get_user_profile_api_v1_sora2_get_user_profile_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息档案/Fetch user profile  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 用户的个人信息档案 - 包含用户基本信息、统计数据、社交关系等 - 可用于用户资料展示、数据分析等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - user_id: 用户 ID，必填，格式如 `user-xiCyLclE6KJcdTXyvVq3Ontc`  ### 返回: - profile: 用户信息     - user_id: 用户 ID     - username: 用户名     - display_name: 显示名称     - bio: 个人简介     - profile_picture_url: 头像链接     - banner_image_url: 横幅图片链接     - follower_count: 粉丝数     - following_count: 关注数     - post_count: 作品数     - like_count: 获赞总数     - view_count: 浏览总数     - is_verified: 是否认证用户     - created_at: 账号创建时间戳     - social_links: 社交媒体链接（如有）  # [English] ### Purpose: - Fetch Sora user's profile information - Includes user basic info, statistics, social relationships, etc. - Can be used for user profile display, data analysis, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - user_id: User ID, required, format like `user-xiCyLclE6KJcdTXyvVq3Ontc`  ### Return: - profile: User information     - user_id: User ID     - username: Username     - display_name: Display name     - bio: Biography     - profile_picture_url: Avatar URL     - banner_image_url: Banner image URL     - follower_count: Follower count     - following_count: Following count     - post_count: Post count     - like_count: Total likes received     - view_count: Total views     - is_verified: Whether verified user     - created_at: Account creation timestamp     - social_links: Social media links (if any)  # [示例/Example] ```python # 获取用户信息 user_id = \"user-xiCyLclE6KJcdTXyvVq3Ontc\"  # 返回示例 {     \"profile\": {         \"username\": \"creator123\",         \"display_name\": \"Amazing Creator\",         \"follower_count\": 12500,         \"post_count\": 45     } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_profile_api_v1_sora2_get_user_profile_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_profile_api_v1_sora2_get_user_profile_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_profile_api_v1_sora2_get_user_profile_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_profile_api_v1_sora2_get_user_profile_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息档案/Fetch user profile  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 用户的个人信息档案 - 包含用户基本信息、统计数据、社交关系等 - 可用于用户资料展示、数据分析等场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - user_id: 用户 ID，必填，格式如 `user-xiCyLclE6KJcdTXyvVq3Ontc`  ### 返回: - profile: 用户信息     - user_id: 用户 ID     - username: 用户名     - display_name: 显示名称     - bio: 个人简介     - profile_picture_url: 头像链接     - banner_image_url: 横幅图片链接     - follower_count: 粉丝数     - following_count: 关注数     - post_count: 作品数     - like_count: 获赞总数     - view_count: 浏览总数     - is_verified: 是否认证用户     - created_at: 账号创建时间戳     - social_links: 社交媒体链接（如有）  # [English] ### Purpose: - Fetch Sora user's profile information - Includes user basic info, statistics, social relationships, etc. - Can be used for user profile display, data analysis, etc.  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - user_id: User ID, required, format like `user-xiCyLclE6KJcdTXyvVq3Ontc`  ### Return: - profile: User information     - user_id: User ID     - username: Username     - display_name: Display name     - bio: Biography     - profile_picture_url: Avatar URL     - banner_image_url: Banner image URL     - follower_count: Follower count     - following_count: Following count     - post_count: Post count     - like_count: Total likes received     - view_count: Total views     - is_verified: Whether verified user     - created_at: Account creation timestamp     - social_links: Social media links (if any)  # [示例/Example] ```python # 获取用户信息 user_id = \"user-xiCyLclE6KJcdTXyvVq3Ontc\"  # 返回示例 {     \"profile\": {         \"username\": \"creator123\",         \"display_name\": \"Amazing Creator\",         \"follower_count\": 12500,         \"post_count\": 45     } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_profile_api_v1_sora2_get_user_profile_get_with_http_info(user_id, async_req=True)
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
                    " to method get_user_profile_api_v1_sora2_get_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_profile_api_v1_sora2_get_user_profile_get`")  # noqa: E501

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
            '/api/v1/sora2/get_user_profile', 'GET',
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

    def get_video_download_info_api_v1_sora2_get_video_download_info_get(self, **kwargs):  # noqa: E501
        """获取无水印视频下载信息/Fetch none watermark video download info  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 作品的简化下载信息，专为视频下载场景优化 - 直接返回无水印视频链接和关键信息，无需解析复杂的完整数据 - 适合需要快速下载视频的场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - post_id: 作品 ID（可选），格式如 `s_68e853d2ad448191b3c81e830f53c3a2` - post_url: 作品链接（可选），格式如 `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2` - **注意**: post_id 和 post_url 至少提供一个  ### 返回: - post_id: 作品 ID - title: 作品描述文本 - video: 视频信息     - no_watermark: 无水印视频链接（原始质量）     - watermark: 有水印视频链接     - width: 视频宽度     - height: 视频高度     - thumbnail: 缩略图链接     - preview_gif: 预览 GIF 链接     - medium_quality: 中等质量视频链接 - author: 作者信息     - user_id: 用户 ID     - username: 用户名     - display_name: 显示名称     - avatar: 头像链接 - stats: 统计数据     - like_count: 点赞数     - view_count: 浏览数     - comment_count: 评论数     - remix_count: 混剪数 - permalink: 作品永久链接 - created_at: 创建时间戳  # [English] ### Purpose: - Get simplified download information for Sora posts, optimized for video download scenarios - Directly returns watermark-free video links and key information without parsing complex full data - Suitable for quick video download scenarios  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - post_id: Post ID (optional), format like `s_68e853d2ad448191b3c81e830f53c3a2` - post_url: Post URL (optional), format like `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2` - **Note**: At least one of post_id or post_url must be provided  ### Return: - post_id: Post ID - title: Post description text - video: Video information     - no_watermark: No watermark video link (original quality)     - watermark: Watermarked video link     - width: Video width     - height: Video height     - thumbnail: Thumbnail link     - preview_gif: Preview GIF link     - medium_quality: Medium quality video link - author: Author information     - user_id: User ID     - username: Username     - display_name: Display name     - avatar: Avatar URL - stats: Statistics     - like_count: Like count     - view_count: View count     - comment_count: Comment count     - remix_count: Remix count - permalink: Permanent link - created_at: Creation timestamp  # [示例/Example] ```python # 使用作品 ID 查询 post_id = \"s_68e853d2ad448191b3c81e830f53c3a2\"  # 返回示例 {     \"video\": {         \"no_watermark\": \"https://cdn.openai.com/...\",  # 直接下载此链接         \"thumbnail\": \"https://cdn.openai.com/...\",         \"width\": 1920,         \"height\": 1080     },     \"title\": \"Amazing Sora video\",     \"author\": {\"username\": \"creator123\"} } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_download_info_api_v1_sora2_get_video_download_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 作品ID（可选）/Post ID (optional)
        :param object post_url: 作品链接（可选）/Post URL (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_video_download_info_api_v1_sora2_get_video_download_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_video_download_info_api_v1_sora2_get_video_download_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_video_download_info_api_v1_sora2_get_video_download_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取无水印视频下载信息/Fetch none watermark video download info  # noqa: E501

        # [中文] ### 用途: - 获取 Sora 作品的简化下载信息，专为视频下载场景优化 - 直接返回无水印视频链接和关键信息，无需解析复杂的完整数据 - 适合需要快速下载视频的场景  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - post_id: 作品 ID（可选），格式如 `s_68e853d2ad448191b3c81e830f53c3a2` - post_url: 作品链接（可选），格式如 `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2` - **注意**: post_id 和 post_url 至少提供一个  ### 返回: - post_id: 作品 ID - title: 作品描述文本 - video: 视频信息     - no_watermark: 无水印视频链接（原始质量）     - watermark: 有水印视频链接     - width: 视频宽度     - height: 视频高度     - thumbnail: 缩略图链接     - preview_gif: 预览 GIF 链接     - medium_quality: 中等质量视频链接 - author: 作者信息     - user_id: 用户 ID     - username: 用户名     - display_name: 显示名称     - avatar: 头像链接 - stats: 统计数据     - like_count: 点赞数     - view_count: 浏览数     - comment_count: 评论数     - remix_count: 混剪数 - permalink: 作品永久链接 - created_at: 创建时间戳  # [English] ### Purpose: - Get simplified download information for Sora posts, optimized for video download scenarios - Directly returns watermark-free video links and key information without parsing complex full data - Suitable for quick video download scenarios  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - post_id: Post ID (optional), format like `s_68e853d2ad448191b3c81e830f53c3a2` - post_url: Post URL (optional), format like `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2` - **Note**: At least one of post_id or post_url must be provided  ### Return: - post_id: Post ID - title: Post description text - video: Video information     - no_watermark: No watermark video link (original quality)     - watermark: Watermarked video link     - width: Video width     - height: Video height     - thumbnail: Thumbnail link     - preview_gif: Preview GIF link     - medium_quality: Medium quality video link - author: Author information     - user_id: User ID     - username: Username     - display_name: Display name     - avatar: Avatar URL - stats: Statistics     - like_count: Like count     - view_count: View count     - comment_count: Comment count     - remix_count: Remix count - permalink: Permanent link - created_at: Creation timestamp  # [示例/Example] ```python # 使用作品 ID 查询 post_id = \"s_68e853d2ad448191b3c81e830f53c3a2\"  # 返回示例 {     \"video\": {         \"no_watermark\": \"https://cdn.openai.com/...\",  # 直接下载此链接         \"thumbnail\": \"https://cdn.openai.com/...\",         \"width\": 1920,         \"height\": 1080     },     \"title\": \"Amazing Sora video\",     \"author\": {\"username\": \"creator123\"} } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_download_info_api_v1_sora2_get_video_download_info_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 作品ID（可选）/Post ID (optional)
        :param object post_url: 作品链接（可选）/Post URL (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id', 'post_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_download_info_api_v1_sora2_get_video_download_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501
        if 'post_url' in params:
            query_params.append(('post_url', params['post_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sora2/get_video_download_info', 'GET',
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

    def search_users_api_v1_sora2_search_users_get(self, username, **kwargs):  # noqa: E501
        """搜索用户/Search users  # noqa: E501

        # [中文] ### 用途: - 搜索 Sora 用户（主要用于 @ 提及功能） - 根据用户名关键词搜索匹配的用户 - 返回用户信息和提及 Token（用于在评论中 @ 用户） - 注意：实际返回结果可能超过 20 个，比预期的更多  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - username: 搜索关键词，必填，支持部分匹配  ### 返回: - items: 用户搜索结果列表     - profile: 用户信息         - user_id: 用户 ID         - username: 用户名         - display_name: 显示名称         - profile_picture_url: 头像链接         - follower_count: 粉丝数         - following_count: 关注数         - bio: 个人简介         - is_verified: 是否认证用户     - token: 提及 Token（用于 @ 提及功能）         - 格式：`<@user-xxxxxxxx>`         - 在评论中使用此 Token 可以提及该用户  # [English] ### Purpose: - Search Sora users (mainly for @ mention functionality) - Search for matching users based on username keywords - Returns user information and mention tokens (for @mentioning users in comments) - Note: Actual results may exceed 20 users, more than expected  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - username: Search keyword, required, supports partial matching  ### Return: - items: User search result list     - profile: User information         - user_id: User ID         - username: Username         - display_name: Display name         - profile_picture_url: Avatar URL         - follower_count: Follower count         - following_count: Following count         - bio: Biography         - is_verified: Whether verified user     - token: Mention token (for @ mention functionality)         - Format: `<@user-xxxxxxxx>`         - Use this token in comments to mention the user  # [示例/Example] ```python # 搜索用户名包含 \"sam\" 的用户 username = \"sam\"  # 返回示例 {     \"items\": [         {             \"profile\": {                 \"username\": \"samuel\",                 \"display_name\": \"Samuel Creator\",                 \"follower_count\": 20000             },             \"token\": \"<@user-abc123xyz>\"         },         {             \"profile\": {                 \"username\": \"samantha\",                 \"display_name\": \"Samantha Artist\"             },             \"token\": \"<@user-def456uvw>\"         }     ] }  # 在评论中使用 token 提及用户 # comment_text = \"Great work <@user-abc123xyz>!\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_api_v1_sora2_search_users_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 搜索关键词（用户名）/Search keyword (username) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_users_api_v1_sora2_search_users_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.search_users_api_v1_sora2_search_users_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def search_users_api_v1_sora2_search_users_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """搜索用户/Search users  # noqa: E501

        # [中文] ### 用途: - 搜索 Sora 用户（主要用于 @ 提及功能） - 根据用户名关键词搜索匹配的用户 - 返回用户信息和提及 Token（用于在评论中 @ 用户） - 注意：实际返回结果可能超过 20 个，比预期的更多  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.05 美元 - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。  ### 参数: - username: 搜索关键词，必填，支持部分匹配  ### 返回: - items: 用户搜索结果列表     - profile: 用户信息         - user_id: 用户 ID         - username: 用户名         - display_name: 显示名称         - profile_picture_url: 头像链接         - follower_count: 粉丝数         - following_count: 关注数         - bio: 个人简介         - is_verified: 是否认证用户     - token: 提及 Token（用于 @ 提及功能）         - 格式：`<@user-xxxxxxxx>`         - 在评论中使用此 Token 可以提及该用户  # [English] ### Purpose: - Search Sora users (mainly for @ mention functionality) - Search for matching users based on username keywords - Returns user information and mention tokens (for @mentioning users in comments) - Note: Actual results may exceed 20 users, more than expected  ### Pricing: - This API costs $0.05 per request - This API supports free quota, you can get free requests by checking in daily at the user dashboard.  ### Parameters: - username: Search keyword, required, supports partial matching  ### Return: - items: User search result list     - profile: User information         - user_id: User ID         - username: Username         - display_name: Display name         - profile_picture_url: Avatar URL         - follower_count: Follower count         - following_count: Following count         - bio: Biography         - is_verified: Whether verified user     - token: Mention token (for @ mention functionality)         - Format: `<@user-xxxxxxxx>`         - Use this token in comments to mention the user  # [示例/Example] ```python # 搜索用户名包含 \"sam\" 的用户 username = \"sam\"  # 返回示例 {     \"items\": [         {             \"profile\": {                 \"username\": \"samuel\",                 \"display_name\": \"Samuel Creator\",                 \"follower_count\": 20000             },             \"token\": \"<@user-abc123xyz>\"         },         {             \"profile\": {                 \"username\": \"samantha\",                 \"display_name\": \"Samantha Artist\"             },             \"token\": \"<@user-def456uvw>\"         }     ] }  # 在评论中使用 token 提及用户 # comment_text = \"Great work <@user-abc123xyz>!\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_api_v1_sora2_search_users_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 搜索关键词（用户名）/Search keyword (username) (required)
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
                    " to method search_users_api_v1_sora2_search_users_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `search_users_api_v1_sora2_search_users_get`")  # noqa: E501

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
            '/api/v1/sora2/search_users', 'GET',
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

    def upload_image_api_v1_sora2_upload_image_post(self, **kwargs):  # noqa: E501
        """上传图片获取media_id/Upload image to get media_id  # noqa: E501

        # [中文] ### 用途: - 上传图片到 Sora 服务器获取 media_id - 获取的 media_id 可用于后续的 AI 视频生成功能 - 支持 PNG、JPG、JPEG 格式的图片文件  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.001 美元 （防止恶意请求） - 速率限制：每秒最多请求 1 次（1 request/second） - 如果请求过快可能会被限流，建议间隔至少 1 秒  ### 参数说明: - **file** (必填): 图片文件   - 支持格式: PNG, JPG, JPEG   - 文件大小: 最大 10MB  ### 返回数据: - **id**: Media ID（用于视频生成） - **url**: 图片访问链接 - **kind**: 资源类型（通常为 \"image\"） - **width**: 图片宽度（像素） - **height**: 图片高度（像素） - **file_name**: 文件名  ### 注意事项: - 上传的图片会存储在服务器上 - 返回的 media_id 有效期通常为 24 小时 - 建议在获取 media_id 后及时使用 - 文件名会自动清理特殊字符以确保安全  ---  # [English] ### Purpose: - Upload image to Sora server to get media_id - The obtained media_id can be used for subsequent AI video generation - Supports PNG, JPG, JPEG format image files  ### Pricing: - This API costs $0.001 per request (to prevent abuse requests) - Rate limit: Maximum 1 request per second - If requests are too frequent, you may be rate limited; it is recommended to wait at least 1 second between requests  ### Parameters: - **file** (required): Image file   - Supported formats: PNG, JPG, JPEG   - File size: Maximum 10MB  ### Response Data: - **id**: Media ID (for video generation) - **url**: Image access link - **kind**: Resource type (usually \"image\") - **width**: Image width (pixels) - **height**: Image height (pixels) - **file_name**: File name  ### Notes: - Uploaded images are stored on the server - The returned media_id is usually valid for 24 hours - Recommend using media_id promptly after obtaining - File names are automatically sanitized for security  ---  # [示例/Example] ```python {    \"id\":\"media_01k7edmn2ge988d9x6g5zg1hhw\",    \"type\":\"image\",    \"created_at\":\"2025-10-13T09:15:20.063403Z\",    \"filename\":\"20760448.jpeg\",    \"extension\":\"jpeg\",    \"mime_type\":\"image/jpeg\",    \"url\":\"https://videos.openai.com/vg-assets/assets%2Fclient_upload%2Fmedia%2F084bcb820761572154494edb38c9ff2b4a3254fd%2Fmedia_01k7edmn2ge988d9x6g5zg1hhw.jpeg?se=2025-10-13T10%3A15%3A20Z&sp=r&sv=2024-08-04&sr=b&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-10-13T08%3A24%3A12Z&ske=2025-10-13T12%3A29%3A12Z&sks=b&skv=2024-08-04&sig=3xnRz6u%2BJcO3Db7EAvDXkw08xDttCc5xSvvL2k2nEN8%3D&az=oaivgprodscus\",    \"width\":460,    \"height\":460,    \"duration_sec\":null,    \"n_frames\":1,    \"size_bytes\":51902,    \"thumbnail_url\":\"https://videos.openai.com/vg-assets/assets%2Fclient_upload%2Fmedia%2F084bcb820761572154494edb38c9ff2b4a3254fd%2Fmedia_01k7edmn2ge988d9x6g5zg1hhw.jpg?se=2025-10-13T10%3A15%3A20Z&sp=r&sv=2024-08-04&sr=b&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-10-13T08%3A24%3A12Z&ske=2025-10-13T12%3A29%3A12Z&sks=b&skv=2024-08-04&sig=chcnDmB%2BKipH%2BOAPHQGmZv8zCldny/U0HDtsvjuZoqA%3D&az=oaivgprodscus\" } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_image_api_v1_sora2_upload_image_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_image_api_v1_sora2_upload_image_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.upload_image_api_v1_sora2_upload_image_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def upload_image_api_v1_sora2_upload_image_post_with_http_info(self, **kwargs):  # noqa: E501
        """上传图片获取media_id/Upload image to get media_id  # noqa: E501

        # [中文] ### 用途: - 上传图片到 Sora 服务器获取 media_id - 获取的 media_id 可用于后续的 AI 视频生成功能 - 支持 PNG、JPG、JPEG 格式的图片文件  ### 收费说明: - 本接口请求价格为 1 次调用消耗 0.001 美元 （防止恶意请求） - 速率限制：每秒最多请求 1 次（1 request/second） - 如果请求过快可能会被限流，建议间隔至少 1 秒  ### 参数说明: - **file** (必填): 图片文件   - 支持格式: PNG, JPG, JPEG   - 文件大小: 最大 10MB  ### 返回数据: - **id**: Media ID（用于视频生成） - **url**: 图片访问链接 - **kind**: 资源类型（通常为 \"image\"） - **width**: 图片宽度（像素） - **height**: 图片高度（像素） - **file_name**: 文件名  ### 注意事项: - 上传的图片会存储在服务器上 - 返回的 media_id 有效期通常为 24 小时 - 建议在获取 media_id 后及时使用 - 文件名会自动清理特殊字符以确保安全  ---  # [English] ### Purpose: - Upload image to Sora server to get media_id - The obtained media_id can be used for subsequent AI video generation - Supports PNG, JPG, JPEG format image files  ### Pricing: - This API costs $0.001 per request (to prevent abuse requests) - Rate limit: Maximum 1 request per second - If requests are too frequent, you may be rate limited; it is recommended to wait at least 1 second between requests  ### Parameters: - **file** (required): Image file   - Supported formats: PNG, JPG, JPEG   - File size: Maximum 10MB  ### Response Data: - **id**: Media ID (for video generation) - **url**: Image access link - **kind**: Resource type (usually \"image\") - **width**: Image width (pixels) - **height**: Image height (pixels) - **file_name**: File name  ### Notes: - Uploaded images are stored on the server - The returned media_id is usually valid for 24 hours - Recommend using media_id promptly after obtaining - File names are automatically sanitized for security  ---  # [示例/Example] ```python {    \"id\":\"media_01k7edmn2ge988d9x6g5zg1hhw\",    \"type\":\"image\",    \"created_at\":\"2025-10-13T09:15:20.063403Z\",    \"filename\":\"20760448.jpeg\",    \"extension\":\"jpeg\",    \"mime_type\":\"image/jpeg\",    \"url\":\"https://videos.openai.com/vg-assets/assets%2Fclient_upload%2Fmedia%2F084bcb820761572154494edb38c9ff2b4a3254fd%2Fmedia_01k7edmn2ge988d9x6g5zg1hhw.jpeg?se=2025-10-13T10%3A15%3A20Z&sp=r&sv=2024-08-04&sr=b&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-10-13T08%3A24%3A12Z&ske=2025-10-13T12%3A29%3A12Z&sks=b&skv=2024-08-04&sig=3xnRz6u%2BJcO3Db7EAvDXkw08xDttCc5xSvvL2k2nEN8%3D&az=oaivgprodscus\",    \"width\":460,    \"height\":460,    \"duration_sec\":null,    \"n_frames\":1,    \"size_bytes\":51902,    \"thumbnail_url\":\"https://videos.openai.com/vg-assets/assets%2Fclient_upload%2Fmedia%2F084bcb820761572154494edb38c9ff2b4a3254fd%2Fmedia_01k7edmn2ge988d9x6g5zg1hhw.jpg?se=2025-10-13T10%3A15%3A20Z&sp=r&sv=2024-08-04&sr=b&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-10-13T08%3A24%3A12Z&ske=2025-10-13T12%3A29%3A12Z&sks=b&skv=2024-08-04&sig=chcnDmB%2BKipH%2BOAPHQGmZv8zCldny/U0HDtsvjuZoqA%3D&az=oaivgprodscus\" } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_image_api_v1_sora2_upload_image_post_with_http_info(async_req=True)
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
                    " to method upload_image_api_v1_sora2_upload_image_post" % key
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
            '/api/v1/sora2/upload_image', 'POST',
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
