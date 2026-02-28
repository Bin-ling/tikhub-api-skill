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


class ThreadsWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_post_comments_api_v1_threads_web_fetch_post_comments_get(self, post_id, **kwargs):  # noqa: E501
        """获取帖子评论/Get post comments  # noqa: E501

        # [中文] ### 用途: - 获取Threads帖子评论列表 - 价格：0.002$ / 次 ### 参数: - post_id: 帖子ID，例如：3390920896561588969 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 帖子评论列表数据，包含:     - comments: 评论列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Get Threads post comments list - Price: 0.002$ / time ### Parameters: - post_id: Post ID, for example: 3390920896561588969 - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - Post comments list data, including:     - comments: Comment list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] post_id = \"3390920896561588969\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_threads_web_fetch_post_comments_get(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comments_api_v1_threads_web_fetch_post_comments_get_with_http_info(post_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comments_api_v1_threads_web_fetch_post_comments_get_with_http_info(post_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_comments_api_v1_threads_web_fetch_post_comments_get_with_http_info(self, post_id, **kwargs):  # noqa: E501
        """获取帖子评论/Get post comments  # noqa: E501

        # [中文] ### 用途: - 获取Threads帖子评论列表 - 价格：0.002$ / 次 ### 参数: - post_id: 帖子ID，例如：3390920896561588969 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 帖子评论列表数据，包含:     - comments: 评论列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Get Threads post comments list - Price: 0.002$ / time ### Parameters: - post_id: Post ID, for example: 3390920896561588969 - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - Post comments list data, including:     - comments: Comment list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] post_id = \"3390920896561588969\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_threads_web_fetch_post_comments_get_with_http_info(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comments_api_v1_threads_web_fetch_post_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_id' is set
        if self.api_client.client_side_validation and ('post_id' not in params or
                                                       params['post_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_id` when calling `fetch_post_comments_api_v1_threads_web_fetch_post_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/threads/web/fetch_post_comments', 'GET',
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

    def fetch_post_detail_api_v1_threads_web_fetch_post_detail_get(self, post_id, **kwargs):  # noqa: E501
        """获取帖子详情/Get post detail  # noqa: E501

        # [中文] ### 用途: - 获取Threads帖子详情 - 价格：0.002$ / 次 ### 参数: - post_id: 帖子ID（纯数字），例如：3349029093483693129，可以从其他接口获取，如果是使用URL获取，去调用 /fetch_post_detail_v2 接口。 ### 返回: - 帖子详情数据，包含:     - id: 帖子ID     - text: 帖子文本内容     - user: 发布者信息     - image_versions2: 图片信息     - video_versions: 视频信息     - like_count: 点赞数     - text_post_app_info: 帖子应用信息     - 等等...  # [English] ### Purpose: - Get Threads post detail - Price: 0.002$ / time ### Parameters: - post_id: Post ID (numeric only), for example: 3349029093483693129, can be obtained from other APIs. If using URL to get, call /fetch_post_detail_v2 API. ### Return: - Post detail data, including:     - id: Post ID     - text: Post text content     - user: Publisher information     - image_versions2: Image information     - video_versions: Video information     - like_count: Like count     - text_post_app_info: Post app information     - etc...  # [示例/Example] post_id = \"3349029093483693129\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_threads_web_fetch_post_detail_get(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子ID/Post ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_detail_api_v1_threads_web_fetch_post_detail_get_with_http_info(post_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_detail_api_v1_threads_web_fetch_post_detail_get_with_http_info(post_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_detail_api_v1_threads_web_fetch_post_detail_get_with_http_info(self, post_id, **kwargs):  # noqa: E501
        """获取帖子详情/Get post detail  # noqa: E501

        # [中文] ### 用途: - 获取Threads帖子详情 - 价格：0.002$ / 次 ### 参数: - post_id: 帖子ID（纯数字），例如：3349029093483693129，可以从其他接口获取，如果是使用URL获取，去调用 /fetch_post_detail_v2 接口。 ### 返回: - 帖子详情数据，包含:     - id: 帖子ID     - text: 帖子文本内容     - user: 发布者信息     - image_versions2: 图片信息     - video_versions: 视频信息     - like_count: 点赞数     - text_post_app_info: 帖子应用信息     - 等等...  # [English] ### Purpose: - Get Threads post detail - Price: 0.002$ / time ### Parameters: - post_id: Post ID (numeric only), for example: 3349029093483693129, can be obtained from other APIs. If using URL to get, call /fetch_post_detail_v2 API. ### Return: - Post detail data, including:     - id: Post ID     - text: Post text content     - user: Publisher information     - image_versions2: Image information     - video_versions: Video information     - like_count: Like count     - text_post_app_info: Post app information     - etc...  # [示例/Example] post_id = \"3349029093483693129\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_threads_web_fetch_post_detail_get_with_http_info(post_id, async_req=True)
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
                    " to method fetch_post_detail_api_v1_threads_web_fetch_post_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_id' is set
        if self.api_client.client_side_validation and ('post_id' not in params or
                                                       params['post_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_id` when calling `fetch_post_detail_api_v1_threads_web_fetch_post_detail_get`")  # noqa: E501

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
            '/api/v1/threads/web/fetch_post_detail', 'GET',
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

    def fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get(self, **kwargs):  # noqa: E501
        """获取帖子详情 V2(支持链接)/Get post detail V2(supports URL)  # noqa: E501

        # [中文] ### 用途: - 获取Threads帖子详情（支持短代码和完整URL） - 价格：0.002$ / 次 ### 参数: - post_id: 帖子短代码（可选），例如：DPVUglOjOUu，可以从帖子URL中提取，例如：https://www.threads.com/@taylorswift/post/DPVUglOjOUu 中的 DPVUglOjOUu - url: 完整的帖子URL（可选），例如：https://www.threads.com/@taylorswift/post/DPVUglOjOUu - 注意：post_id 和 url 至少提供一个参数 ### 返回: - 帖子详情数据，包含:     - post_id: 帖子ID     - text: 帖子文本内容     - user: 发布者信息     - media: 媒体信息（图片、视频）     - like_count: 点赞数     - reply_count: 回复数     - repost_count: 转发数     - timestamp: 发布时间     - 等等...  # [English] ### Purpose: - Get Threads post detail (supports short code and full URL) - Price: 0.002$ / time ### Parameters: - post_id: Post short code (optional), for example: DPVUglOjOUu, can be extracted from post URL, e.g., DPVUglOjOUu in https://www.threads.com/@taylorswift/post/DPVUglOjOUu - url: Full post URL (optional), for example: https://www.threads.com/@taylorswift/post/DPVUglOjOUu - Note: At least one of post_id or url must be provided ### Return: - Post detail data, including:     - post_id: Post ID     - text: Post text content     - user: Publisher information     - media: Media information (images, videos)     - like_count: Like count     - reply_count: Reply count     - repost_count: Repost count     - timestamp: Publish timestamp     - etc...  # [示例/Example] post_id = \"DPVUglOjOUu\" # or url = \"https://www.threads.com/@taylorswift/post/DPVUglOjOUu\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子短代码/Post short code
        :param object url: 完整帖子URL/Full post URL
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取帖子详情 V2(支持链接)/Get post detail V2(supports URL)  # noqa: E501

        # [中文] ### 用途: - 获取Threads帖子详情（支持短代码和完整URL） - 价格：0.002$ / 次 ### 参数: - post_id: 帖子短代码（可选），例如：DPVUglOjOUu，可以从帖子URL中提取，例如：https://www.threads.com/@taylorswift/post/DPVUglOjOUu 中的 DPVUglOjOUu - url: 完整的帖子URL（可选），例如：https://www.threads.com/@taylorswift/post/DPVUglOjOUu - 注意：post_id 和 url 至少提供一个参数 ### 返回: - 帖子详情数据，包含:     - post_id: 帖子ID     - text: 帖子文本内容     - user: 发布者信息     - media: 媒体信息（图片、视频）     - like_count: 点赞数     - reply_count: 回复数     - repost_count: 转发数     - timestamp: 发布时间     - 等等...  # [English] ### Purpose: - Get Threads post detail (supports short code and full URL) - Price: 0.002$ / time ### Parameters: - post_id: Post short code (optional), for example: DPVUglOjOUu, can be extracted from post URL, e.g., DPVUglOjOUu in https://www.threads.com/@taylorswift/post/DPVUglOjOUu - url: Full post URL (optional), for example: https://www.threads.com/@taylorswift/post/DPVUglOjOUu - Note: At least one of post_id or url must be provided ### Return: - Post detail data, including:     - post_id: Post ID     - text: Post text content     - user: Publisher information     - media: Media information (images, videos)     - like_count: Like count     - reply_count: Reply count     - repost_count: Repost count     - timestamp: Publish timestamp     - etc...  # [示例/Example] post_id = \"DPVUglOjOUu\" # or url = \"https://www.threads.com/@taylorswift/post/DPVUglOjOUu\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 帖子短代码/Post short code
        :param object url: 完整帖子URL/Full post URL
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id', 'url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/threads/web/fetch_post_detail_v2', 'GET',
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

    def fetch_user_info_api_v1_threads_web_fetch_user_info_get(self, username, **kwargs):  # noqa: E501
        """获取用户信息/Get user info  # noqa: E501

        # [中文] ### 用途: - 获取Threads用户信息 - 价格：0.002$ / 次 ### 参数: - username: 用户名，例如：lilbieber，可以从用户主页链接中获取，例如：https://www.threads.net/@lilbieber 中的 lilbieber。 ### 返回: - 用户信息数据，包含:     - pk: 用户ID     - username: 用户名     - full_name: 全名     - biography: 个人简介     - profile_pic_url: 头像URL     - follower_count: 粉丝数     - is_verified: 是否认证     - 等等...  # [English] ### Purpose: - Get Threads user information - Price: 0.002$ / time ### Parameters: - username: Username, for example: lilbieber, can be obtained from the user's homepage link, for example: lilbieber in https://www.threads.net/@lilbieber ### Return: - User information data, including:     - pk: User ID     - username: Username     - full_name: Full name     - biography: Biography     - profile_pic_url: Profile picture URL     - follower_count: Follower count     - is_verified: Is verified     - etc...  # [示例/Example] username = \"lilbieber\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_threads_web_fetch_user_info_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_threads_web_fetch_user_info_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_threads_web_fetch_user_info_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_threads_web_fetch_user_info_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """获取用户信息/Get user info  # noqa: E501

        # [中文] ### 用途: - 获取Threads用户信息 - 价格：0.002$ / 次 ### 参数: - username: 用户名，例如：lilbieber，可以从用户主页链接中获取，例如：https://www.threads.net/@lilbieber 中的 lilbieber。 ### 返回: - 用户信息数据，包含:     - pk: 用户ID     - username: 用户名     - full_name: 全名     - biography: 个人简介     - profile_pic_url: 头像URL     - follower_count: 粉丝数     - is_verified: 是否认证     - 等等...  # [English] ### Purpose: - Get Threads user information - Price: 0.002$ / time ### Parameters: - username: Username, for example: lilbieber, can be obtained from the user's homepage link, for example: lilbieber in https://www.threads.net/@lilbieber ### Return: - User information data, including:     - pk: User ID     - username: Username     - full_name: Full name     - biography: Biography     - profile_pic_url: Profile picture URL     - follower_count: Follower count     - is_verified: Is verified     - etc...  # [示例/Example] username = \"lilbieber\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_threads_web_fetch_user_info_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
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
                    " to method fetch_user_info_api_v1_threads_web_fetch_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_user_info_api_v1_threads_web_fetch_user_info_get`")  # noqa: E501

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
            '/api/v1/threads/web/fetch_user_info', 'GET',
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

    def fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get(self, user_id, **kwargs):  # noqa: E501
        """根据用户ID获取用户信息/Get user info by ID  # noqa: E501

        # [中文] ### 用途: - 根据用户ID获取Threads用户信息 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：67027868801，可以从用户主页API或帖子数据中获取。 ### 返回: - 用户信息数据，包含:     - pk: 用户ID     - username: 用户名     - full_name: 全名     - biography: 个人简介     - profile_pic_url: 头像URL     - follower_count: 粉丝数     - is_verified: 是否认证     - 等等...  # [English] ### Purpose: - Get Threads user information by user ID - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 67027868801, can be obtained from user profile API or post data ### Return: - User information data, including:     - pk: User ID     - username: Username     - full_name: Full name     - biography: Biography     - profile_pic_url: Profile picture URL     - follower_count: Follower count     - is_verified: Is verified     - etc...  # [示例/Example] user_id = \"67027868801\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """根据用户ID获取用户信息/Get user info by ID  # noqa: E501

        # [中文] ### 用途: - 根据用户ID获取Threads用户信息 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：67027868801，可以从用户主页API或帖子数据中获取。 ### 返回: - 用户信息数据，包含:     - pk: 用户ID     - username: 用户名     - full_name: 全名     - biography: 个人简介     - profile_pic_url: 头像URL     - follower_count: 粉丝数     - is_verified: 是否认证     - 等等...  # [English] ### Purpose: - Get Threads user information by user ID - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 67027868801, can be obtained from user profile API or post data ### Return: - User information data, including:     - pk: User ID     - username: Username     - full_name: Full name     - biography: Biography     - profile_pic_url: Profile picture URL     - follower_count: Follower count     - is_verified: Is verified     - etc...  # [示例/Example] user_id = \"67027868801\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get_with_http_info(user_id, async_req=True)
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
                    " to method fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get`")  # noqa: E501

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
            '/api/v1/threads/web/fetch_user_info_by_id', 'GET',
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

    def fetch_user_posts_api_v1_threads_web_fetch_user_posts_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户帖子列表/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取Threads用户的帖子列表 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：63625256886，可以从用户主页API获取。 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 用户帖子列表数据，包含:     - threads: 帖子列表数组     - next_cursor: 下一页游标     - has_more: 是否有更多数据     - 每个帖子包含:         - id: 帖子ID         - text: 帖子文本内容         - user: 发布者信息         - image_versions2: 图片信息         - video_versions: 视频信息         - like_count: 点赞数         - text_post_app_info: 帖子应用信息         - 等等...  # [English] ### Purpose: - Get Threads user's post list - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 63625256886, can be obtained from user profile API - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - User post list data, including:     - threads: Post list array     - next_cursor: Next page cursor     - has_more: Has more data     - Each post contains:         - id: Post ID         - text: Post text content         - user: Publisher information         - image_versions2: Image information         - video_versions: Video information         - like_count: Like count         - text_post_app_info: Post app information         - etc...  # [示例/Example] user_id = \"63625256886\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_threads_web_fetch_user_posts_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_posts_api_v1_threads_web_fetch_user_posts_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_posts_api_v1_threads_web_fetch_user_posts_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_posts_api_v1_threads_web_fetch_user_posts_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户帖子列表/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取Threads用户的帖子列表 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：63625256886，可以从用户主页API获取。 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 用户帖子列表数据，包含:     - threads: 帖子列表数组     - next_cursor: 下一页游标     - has_more: 是否有更多数据     - 每个帖子包含:         - id: 帖子ID         - text: 帖子文本内容         - user: 发布者信息         - image_versions2: 图片信息         - video_versions: 视频信息         - like_count: 点赞数         - text_post_app_info: 帖子应用信息         - 等等...  # [English] ### Purpose: - Get Threads user's post list - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 63625256886, can be obtained from user profile API - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - User post list data, including:     - threads: Post list array     - next_cursor: Next page cursor     - has_more: Has more data     - Each post contains:         - id: Post ID         - text: Post text content         - user: Publisher information         - image_versions2: Image information         - video_versions: Video information         - like_count: Like count         - text_post_app_info: Post app information         - etc...  # [示例/Example] user_id = \"63625256886\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_threads_web_fetch_user_posts_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_posts_api_v1_threads_web_fetch_user_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_posts_api_v1_threads_web_fetch_user_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/threads/web/fetch_user_posts', 'GET',
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

    def fetch_user_replies_api_v1_threads_web_fetch_user_replies_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户回复列表/Get user replies  # noqa: E501

        # [中文] ### 用途: - 获取Threads用户的回复列表 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：63625256886 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 用户回复列表数据，包含:     - threads: 回复列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Get Threads user's reply list - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 63625256886 - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - User reply list data, including:     - threads: Reply list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] user_id = \"63625256886\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_replies_api_v1_threads_web_fetch_user_replies_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_replies_api_v1_threads_web_fetch_user_replies_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_replies_api_v1_threads_web_fetch_user_replies_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_replies_api_v1_threads_web_fetch_user_replies_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户回复列表/Get user replies  # noqa: E501

        # [中文] ### 用途: - 获取Threads用户的回复列表 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：63625256886 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 用户回复列表数据，包含:     - threads: 回复列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Get Threads user's reply list - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 63625256886 - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - User reply list data, including:     - threads: Reply list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] user_id = \"63625256886\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_replies_api_v1_threads_web_fetch_user_replies_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_replies_api_v1_threads_web_fetch_user_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_replies_api_v1_threads_web_fetch_user_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/threads/web/fetch_user_replies', 'GET',
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

    def fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户转发列表/Get user reposts  # noqa: E501

        # [中文] ### 用途: - 获取Threads用户的转发列表 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：63625256886 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 用户转发列表数据，包含:     - threads: 转发列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Get Threads user's repost list - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 63625256886 - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - User repost list data, including:     - threads: Repost list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] user_id = \"63625256886\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户转发列表/Get user reposts  # noqa: E501

        # [中文] ### 用途: - 获取Threads用户的转发列表 - 价格：0.002$ / 次 ### 参数: - user_id: 用户ID，例如：63625256886 - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 用户转发列表数据，包含:     - threads: 转发列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Get Threads user's repost list - Price: 0.002$ / time ### Parameters: - user_id: User ID, for example: 63625256886 - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - User repost list data, including:     - threads: Repost list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] user_id = \"63625256886\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/threads/web/fetch_user_reposts', 'GET',
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

    def search_profiles_api_v1_threads_web_search_profiles_get(self, query, **kwargs):  # noqa: E501
        """搜索用户档案/Search profiles  # noqa: E501

        # [中文] ### 用途: - 搜索Threads用户档案 - 价格：0.002$ / 次 ### 参数: - query: 搜索关键词，例如：mark ### 返回: - 搜索结果数据，包含:     - users: 用户列表     - 每个用户包含:         - pk: 用户ID         - username: 用户名         - full_name: 全名         - profile_pic_url: 头像URL         - is_verified: 是否认证         - follower_count: 粉丝数         - 等等...  # [English] ### Purpose: - Search Threads user profiles - Price: 0.002$ / time ### Parameters: - query: Search query, for example: mark ### Return: - Search result data, including:     - users: User list     - Each user contains:         - pk: User ID         - username: Username         - full_name: Full name         - profile_pic_url: Profile picture URL         - is_verified: Is verified         - follower_count: Follower count         - etc...  # [示例/Example] query = \"mark\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_profiles_api_v1_threads_web_search_profiles_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search query (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_profiles_api_v1_threads_web_search_profiles_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_profiles_api_v1_threads_web_search_profiles_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_profiles_api_v1_threads_web_search_profiles_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """搜索用户档案/Search profiles  # noqa: E501

        # [中文] ### 用途: - 搜索Threads用户档案 - 价格：0.002$ / 次 ### 参数: - query: 搜索关键词，例如：mark ### 返回: - 搜索结果数据，包含:     - users: 用户列表     - 每个用户包含:         - pk: 用户ID         - username: 用户名         - full_name: 全名         - profile_pic_url: 头像URL         - is_verified: 是否认证         - follower_count: 粉丝数         - 等等...  # [English] ### Purpose: - Search Threads user profiles - Price: 0.002$ / time ### Parameters: - query: Search query, for example: mark ### Return: - Search result data, including:     - users: User list     - Each user contains:         - pk: User ID         - username: Username         - full_name: Full name         - profile_pic_url: Profile picture URL         - is_verified: Is verified         - follower_count: Follower count         - etc...  # [示例/Example] query = \"mark\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_profiles_api_v1_threads_web_search_profiles_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search query (required)
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
                    " to method search_profiles_api_v1_threads_web_search_profiles_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `search_profiles_api_v1_threads_web_search_profiles_get`")  # noqa: E501

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
            '/api/v1/threads/web/search_profiles', 'GET',
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

    def search_recent_api_v1_threads_web_search_recent_get(self, query, **kwargs):  # noqa: E501
        """搜索最新内容/Search recent content  # noqa: E501

        # [中文] ### 用途: - 搜索Threads最新内容 - 价格：0.002$ / 次 ### 参数: - query: 搜索关键词，例如：bitcoin - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 搜索结果数据，包含:     - threads: 帖子列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Search Threads recent content - Price: 0.002$ / time ### Parameters: - query: Search query, for example: bitcoin - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - Search result data, including:     - threads: Post list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] query = \"bitcoin\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_recent_api_v1_threads_web_search_recent_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search query (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_recent_api_v1_threads_web_search_recent_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_recent_api_v1_threads_web_search_recent_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_recent_api_v1_threads_web_search_recent_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """搜索最新内容/Search recent content  # noqa: E501

        # [中文] ### 用途: - 搜索Threads最新内容 - 价格：0.002$ / 次 ### 参数: - query: 搜索关键词，例如：bitcoin - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 搜索结果数据，包含:     - threads: 帖子列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Search Threads recent content - Price: 0.002$ / time ### Parameters: - query: Search query, for example: bitcoin - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - Search result data, including:     - threads: Post list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] query = \"bitcoin\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_recent_api_v1_threads_web_search_recent_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search query (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_recent_api_v1_threads_web_search_recent_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `search_recent_api_v1_threads_web_search_recent_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/threads/web/search_recent', 'GET',
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

    def search_top_api_v1_threads_web_search_top_get(self, query, **kwargs):  # noqa: E501
        """搜索热门内容/Search top content  # noqa: E501

        # [中文] ### 用途: - 搜索Threads热门内容 - 价格：0.002$ / 次 ### 参数: - query: 搜索关键词，例如：bitcoin - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 搜索结果数据，包含:     - threads: 帖子列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Search Threads top content - Price: 0.002$ / time ### Parameters: - query: Search query, for example: bitcoin - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - Search result data, including:     - threads: Post list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] query = \"bitcoin\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_top_api_v1_threads_web_search_top_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search query (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_top_api_v1_threads_web_search_top_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_top_api_v1_threads_web_search_top_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_top_api_v1_threads_web_search_top_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """搜索热门内容/Search top content  # noqa: E501

        # [中文] ### 用途: - 搜索Threads热门内容 - 价格：0.002$ / 次 ### 参数: - query: 搜索关键词，例如：bitcoin - end_cursor: 分页游标（可选），用于获取下一页数据 ### 返回: - 搜索结果数据，包含:     - threads: 帖子列表     - next_cursor: 下一页游标     - has_more: 是否有更多数据  # [English] ### Purpose: - Search Threads top content - Price: 0.002$ / time ### Parameters: - query: Search query, for example: bitcoin - end_cursor: Pagination cursor (optional), used to get next page data ### Return: - Search result data, including:     - threads: Post list     - next_cursor: Next page cursor     - has_more: Has more data  # [示例/Example] query = \"bitcoin\" end_cursor = None  # or a cursor string from previous response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_top_api_v1_threads_web_search_top_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search query (required)
        :param object end_cursor: 分页游标/Pagination cursor (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'end_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_top_api_v1_threads_web_search_top_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `search_top_api_v1_threads_web_search_top_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'end_cursor' in params:
            query_params.append(('end_cursor', params['end_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/threads/web/search_top', 'GET',
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
