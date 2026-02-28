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


class TikTokAdsAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get(self, material_id, **kwargs):  # noqa: E501
        """获取广告互动分析/Get ad interactive analysis  # noqa: E501

        # [中文] ### 用途: - 获取广告的互动时间分析，了解观众在视频不同时间点的留存和互动情况 - 分析广告视频的吸引力曲线，找出最佳时长和关键互动点 - 优化广告内容结构，提高整体效果  ### 参数: - material_id: 广告素材ID，必填参数 - metric_type: 分析类型     - ctr: 点击率分析     - cvr: 转化率分析     - clicks: 点击次数分析     - conversion: 转化次数分析     - remain: 留存率分析 (默认) - period_type: 时间范围，默认180天  ### 返回内容说明: - `interactive_data`: 互动分析数据   - `time_series`: 时间序列数据     - `time`: 视频播放时间点（秒）     - `value`: 对应的指标值（如留存率）   - `average_watch_time`: 平均观看时长   - `completion_rate`: 完播率   - `peak_interaction_time`: 互动高峰时间点  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",   \"params\": {     \"material_id\": \"7213258221116751874\",     \"metric_type\": \"remain\",     \"period_type\": 180   },   \"data\": {     \"interactive_data\": {       \"time_series\": [         {\"time\": 0, \"value\": 100},         {\"time\": 1, \"value\": 95},         {\"time\": 2, \"value\": 88}       ],       \"average_watch_time\": 8.5,       \"completion_rate\": 65.2,       \"peak_interaction_time\": 3     }   } } ```  # [English] ### Purpose: - Get ad interactive time analysis to understand audience retention and engagement at different video time points - Analyze ad video attractiveness curve to find optimal duration and key interaction points - Optimize ad content structure to improve overall effectiveness  ### Parameters: - material_id: Ad material ID, required parameter - metric_type: Analysis type     - ctr: Click-through rate analysis     - cvr: Conversion rate analysis     - clicks: Click count analysis     - conversion: Conversion count analysis     - remain: Retention rate analysis (default) - period_type: Time range, default 180 days  ### Return Description: - `interactive_data`: Interactive analysis data   - `time_series`: Time series data     - `time`: Video playback time point (seconds)     - `value`: Corresponding metric value (e.g., retention rate)   - `average_watch_time`: Average watch time   - `completion_rate`: Completion rate   - `peak_interaction_time`: Peak interaction time point  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",   \"params\": {     \"material_id\": \"7213258221116751874\",     \"metric_type\": \"remain\",     \"period_type\": 180   },   \"data\": {     \"interactive_data\": {       \"time_series\": [         {\"time\": 0, \"value\": 100},         {\"time\": 1, \"value\": 95},         {\"time\": 2, \"value\": 88}       ],       \"average_watch_time\": 8.5,       \"completion_rate\": 65.2,       \"peak_interaction_time\": 3     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get(material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object material_id: 广告素材ID/Ad material ID (required)
        :param object metric_type: 分析类型/Analysis type (ctr, cvr, clicks, conversion, remain)
        :param object period_type: 时间范围(天)/Period type (days)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get_with_http_info(material_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get_with_http_info(material_id, **kwargs)  # noqa: E501
            return data

    def get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get_with_http_info(self, material_id, **kwargs):  # noqa: E501
        """获取广告互动分析/Get ad interactive analysis  # noqa: E501

        # [中文] ### 用途: - 获取广告的互动时间分析，了解观众在视频不同时间点的留存和互动情况 - 分析广告视频的吸引力曲线，找出最佳时长和关键互动点 - 优化广告内容结构，提高整体效果  ### 参数: - material_id: 广告素材ID，必填参数 - metric_type: 分析类型     - ctr: 点击率分析     - cvr: 转化率分析     - clicks: 点击次数分析     - conversion: 转化次数分析     - remain: 留存率分析 (默认) - period_type: 时间范围，默认180天  ### 返回内容说明: - `interactive_data`: 互动分析数据   - `time_series`: 时间序列数据     - `time`: 视频播放时间点（秒）     - `value`: 对应的指标值（如留存率）   - `average_watch_time`: 平均观看时长   - `completion_rate`: 完播率   - `peak_interaction_time`: 互动高峰时间点  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",   \"params\": {     \"material_id\": \"7213258221116751874\",     \"metric_type\": \"remain\",     \"period_type\": 180   },   \"data\": {     \"interactive_data\": {       \"time_series\": [         {\"time\": 0, \"value\": 100},         {\"time\": 1, \"value\": 95},         {\"time\": 2, \"value\": 88}       ],       \"average_watch_time\": 8.5,       \"completion_rate\": 65.2,       \"peak_interaction_time\": 3     }   } } ```  # [English] ### Purpose: - Get ad interactive time analysis to understand audience retention and engagement at different video time points - Analyze ad video attractiveness curve to find optimal duration and key interaction points - Optimize ad content structure to improve overall effectiveness  ### Parameters: - material_id: Ad material ID, required parameter - metric_type: Analysis type     - ctr: Click-through rate analysis     - cvr: Conversion rate analysis     - clicks: Click count analysis     - conversion: Conversion count analysis     - remain: Retention rate analysis (default) - period_type: Time range, default 180 days  ### Return Description: - `interactive_data`: Interactive analysis data   - `time_series`: Time series data     - `time`: Video playback time point (seconds)     - `value`: Corresponding metric value (e.g., retention rate)   - `average_watch_time`: Average watch time   - `completion_rate`: Completion rate   - `peak_interaction_time`: Peak interaction time point  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",   \"params\": {     \"material_id\": \"7213258221116751874\",     \"metric_type\": \"remain\",     \"period_type\": 180   },   \"data\": {     \"interactive_data\": {       \"time_series\": [         {\"time\": 0, \"value\": 100},         {\"time\": 1, \"value\": 95},         {\"time\": 2, \"value\": 88}       ],       \"average_watch_time\": 8.5,       \"completion_rate\": 65.2,       \"peak_interaction_time\": 3     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get_with_http_info(material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object material_id: 广告素材ID/Ad material ID (required)
        :param object metric_type: 分析类型/Analysis type (ctr, cvr, clicks, conversion, remain)
        :param object period_type: 时间范围(天)/Period type (days)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['material_id', 'metric_type', 'period_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'material_id' is set
        if self.api_client.client_side_validation and ('material_id' not in params or
                                                       params['material_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `material_id` when calling `get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'material_id' in params:
            query_params.append(('material_id', params['material_id']))  # noqa: E501
        if 'metric_type' in params:
            query_params.append(('metric_type', params['metric_type']))  # noqa: E501
        if 'period_type' in params:
            query_params.append(('period_type', params['period_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_ad_interactive_analysis', 'GET',
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

    def get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get(self, material_id, **kwargs):  # noqa: E501
        """获取广告关键帧分析/Get ad keyframe analysis  # noqa: E501

        # [中文] ### 用途: - 获取广告视频的关键帧分析，了解视频在不同时间点的观众留存情况 - 分析哪些时间点最吸引观众，哪些时间点观众流失最多 - 帮助优化广告视频结构，提高观看完成率  ### 参数: - material_id: 广告素材ID，必填参数 - metric: 分析指标，可选值：   - retain_ctr: 留存点击率（默认）   - retain_cvr: 留存转化率   - click_cnt: 点击次数   - convert_cnt: 转化次数   - play_retain_cnt: 播放留存量  ### 返回内容说明: - `keyframe_data`: 关键帧数据   - `time_points`: 时间点列表（秒）   - `retention_rates`: 对应时间点的留存率（百分比）   - `drop_points`: 流失率较高的时间点   - `highlight_points`: 观众兴趣较高的时间点  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",   \"params\": {     \"material_id\": \"7213258221116751874\"   },   \"data\": {     \"keyframe_data\": {       \"time_points\": [0, 1, 2, 3, 4, 5],       \"retention_rates\": [100, 95, 88, 82, 78, 75],       \"drop_points\": [2, 4],       \"highlight_points\": [1, 5]     }   } } ```  # [English] ### Purpose: - Get keyframe analysis of ad videos to understand audience retention at different time points - Analyze which time points attract viewers most and where viewers drop off - Help optimize ad video structure to improve completion rates  ### Parameters: - material_id: Ad material ID, required parameter - metric: Analysis metric, options:   - retain_ctr: Retention CTR (default)   - retain_cvr: Retention CVR   - click_cnt: Click count   - convert_cnt: Conversion count   - play_retain_cnt: Play retention count  ### Return Description: - `keyframe_data`: Keyframe data   - `time_points`: List of time points (seconds)   - `retention_rates`: Retention rates at corresponding time points (percentage)   - `drop_points`: Time points with high drop-off rates   - `highlight_points`: Time points with high viewer interest  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",   \"params\": {     \"material_id\": \"7213258221116751874\"   },   \"data\": {     \"keyframe_data\": {       \"time_points\": [0, 1, 2, 3, 4, 5],       \"retention_rates\": [100, 95, 88, 82, 78, 75],       \"drop_points\": [2, 4],       \"highlight_points\": [1, 5]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get(material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object material_id: 广告素材ID/Ad material ID (required)
        :param object metric: 分析指标/Analysis metric (retain_ctr, retain_cvr, click_cnt, convert_cnt, play_retain_cnt)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get_with_http_info(material_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get_with_http_info(material_id, **kwargs)  # noqa: E501
            return data

    def get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get_with_http_info(self, material_id, **kwargs):  # noqa: E501
        """获取广告关键帧分析/Get ad keyframe analysis  # noqa: E501

        # [中文] ### 用途: - 获取广告视频的关键帧分析，了解视频在不同时间点的观众留存情况 - 分析哪些时间点最吸引观众，哪些时间点观众流失最多 - 帮助优化广告视频结构，提高观看完成率  ### 参数: - material_id: 广告素材ID，必填参数 - metric: 分析指标，可选值：   - retain_ctr: 留存点击率（默认）   - retain_cvr: 留存转化率   - click_cnt: 点击次数   - convert_cnt: 转化次数   - play_retain_cnt: 播放留存量  ### 返回内容说明: - `keyframe_data`: 关键帧数据   - `time_points`: 时间点列表（秒）   - `retention_rates`: 对应时间点的留存率（百分比）   - `drop_points`: 流失率较高的时间点   - `highlight_points`: 观众兴趣较高的时间点  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",   \"params\": {     \"material_id\": \"7213258221116751874\"   },   \"data\": {     \"keyframe_data\": {       \"time_points\": [0, 1, 2, 3, 4, 5],       \"retention_rates\": [100, 95, 88, 82, 78, 75],       \"drop_points\": [2, 4],       \"highlight_points\": [1, 5]     }   } } ```  # [English] ### Purpose: - Get keyframe analysis of ad videos to understand audience retention at different time points - Analyze which time points attract viewers most and where viewers drop off - Help optimize ad video structure to improve completion rates  ### Parameters: - material_id: Ad material ID, required parameter - metric: Analysis metric, options:   - retain_ctr: Retention CTR (default)   - retain_cvr: Retention CVR   - click_cnt: Click count   - convert_cnt: Conversion count   - play_retain_cnt: Play retention count  ### Return Description: - `keyframe_data`: Keyframe data   - `time_points`: List of time points (seconds)   - `retention_rates`: Retention rates at corresponding time points (percentage)   - `drop_points`: Time points with high drop-off rates   - `highlight_points`: Time points with high viewer interest  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",   \"params\": {     \"material_id\": \"7213258221116751874\"   },   \"data\": {     \"keyframe_data\": {       \"time_points\": [0, 1, 2, 3, 4, 5],       \"retention_rates\": [100, 95, 88, 82, 78, 75],       \"drop_points\": [2, 4],       \"highlight_points\": [1, 5]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get_with_http_info(material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object material_id: 广告素材ID/Ad material ID (required)
        :param object metric: 分析指标/Analysis metric (retain_ctr, retain_cvr, click_cnt, convert_cnt, play_retain_cnt)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['material_id', 'metric']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'material_id' is set
        if self.api_client.client_side_validation and ('material_id' not in params or
                                                       params['material_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `material_id` when calling `get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'material_id' in params:
            query_params.append(('material_id', params['material_id']))  # noqa: E501
        if 'metric' in params:
            query_params.append(('metric', params['metric']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_ad_keyframe_analysis', 'GET',
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

    def get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get(self, material_id, **kwargs):  # noqa: E501
        """获取广告百分位数据/Get ad percentile data  # noqa: E501

        # [中文] ### 用途: - 获取广告在同行业中的百分位排名数据 - 了解广告在各项指标上相对于同行的表现水平 - 帮助评估广告效果并制定优化策略  ### 参数: - material_id: 广告素材ID，必填参数 - metric: 分析指标，可选值：   - ctr_percentile: 点击率百分位（默认）   - time_attr_conversion_rate_percentile: 时间归因转化率百分位   - click_cnt_percentile: 点击次数百分位   - time_attr_convert_cnt_percentile: 时间归因转化次数百分位   - show_cnt_percentile: 展示次数百分位 - period_type: 时间范围(天)，默认180天  ### 返回内容说明: - `percentile_data`: 百分位数据   - `ctr_percentile`: 点击率百分位（0-100）   - `cvr_percentile`: 转化率百分位   - `engagement_percentile`: 互动率百分位   - `view_percentile`: 观看量百分位   - `industry_average`: 行业平均值对比  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",   \"params\": {     \"material_id\": \"7213258221116751874\"   },   \"data\": {     \"percentile_data\": {       \"ctr_percentile\": 85,       \"cvr_percentile\": 72,       \"engagement_percentile\": 90,       \"view_percentile\": 88,       \"industry_average\": {         \"ctr\": 2.5,         \"cvr\": 1.2,         \"engagement\": 5.8       }     }   } } ```  # [English] ### Purpose: - Get ad percentile ranking data within the industry - Understand ad performance levels relative to peers across various metrics - Help evaluate ad effectiveness and develop optimization strategies  ### Parameters: - material_id: Ad material ID, required parameter - metric: Analysis metric, options:   - ctr_percentile: CTR percentile (default)   - time_attr_conversion_rate_percentile: Time-attributed conversion rate percentile   - click_cnt_percentile: Click count percentile   - time_attr_convert_cnt_percentile: Time-attributed conversion count percentile   - show_cnt_percentile: Impression count percentile - period_type: Time period in days, default 180  ### Return Description: - `percentile_data`: Percentile data   - `ctr_percentile`: Click-through rate percentile (0-100)   - `cvr_percentile`: Conversion rate percentile   - `engagement_percentile`: Engagement rate percentile   - `view_percentile`: View count percentile   - `industry_average`: Industry average comparison  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",   \"params\": {     \"material_id\": \"7213258221116751874\"   },   \"data\": {     \"percentile_data\": {       \"ctr_percentile\": 85,       \"cvr_percentile\": 72,       \"engagement_percentile\": 90,       \"view_percentile\": 88,       \"industry_average\": {         \"ctr\": 2.5,         \"cvr\": 1.2,         \"engagement\": 5.8       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get(material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object material_id: 广告素材ID/Ad material ID (required)
        :param object metric: 分析指标/Analysis metric (ctr_percentile, time_attr_conversion_rate_percentile, click_cnt_percentile, time_attr_convert_cnt_percentile, show_cnt_percentile)
        :param object period_type: 时间范围(天)/Time period (days)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get_with_http_info(material_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get_with_http_info(material_id, **kwargs)  # noqa: E501
            return data

    def get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get_with_http_info(self, material_id, **kwargs):  # noqa: E501
        """获取广告百分位数据/Get ad percentile data  # noqa: E501

        # [中文] ### 用途: - 获取广告在同行业中的百分位排名数据 - 了解广告在各项指标上相对于同行的表现水平 - 帮助评估广告效果并制定优化策略  ### 参数: - material_id: 广告素材ID，必填参数 - metric: 分析指标，可选值：   - ctr_percentile: 点击率百分位（默认）   - time_attr_conversion_rate_percentile: 时间归因转化率百分位   - click_cnt_percentile: 点击次数百分位   - time_attr_convert_cnt_percentile: 时间归因转化次数百分位   - show_cnt_percentile: 展示次数百分位 - period_type: 时间范围(天)，默认180天  ### 返回内容说明: - `percentile_data`: 百分位数据   - `ctr_percentile`: 点击率百分位（0-100）   - `cvr_percentile`: 转化率百分位   - `engagement_percentile`: 互动率百分位   - `view_percentile`: 观看量百分位   - `industry_average`: 行业平均值对比  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",   \"params\": {     \"material_id\": \"7213258221116751874\"   },   \"data\": {     \"percentile_data\": {       \"ctr_percentile\": 85,       \"cvr_percentile\": 72,       \"engagement_percentile\": 90,       \"view_percentile\": 88,       \"industry_average\": {         \"ctr\": 2.5,         \"cvr\": 1.2,         \"engagement\": 5.8       }     }   } } ```  # [English] ### Purpose: - Get ad percentile ranking data within the industry - Understand ad performance levels relative to peers across various metrics - Help evaluate ad effectiveness and develop optimization strategies  ### Parameters: - material_id: Ad material ID, required parameter - metric: Analysis metric, options:   - ctr_percentile: CTR percentile (default)   - time_attr_conversion_rate_percentile: Time-attributed conversion rate percentile   - click_cnt_percentile: Click count percentile   - time_attr_convert_cnt_percentile: Time-attributed conversion count percentile   - show_cnt_percentile: Impression count percentile - period_type: Time period in days, default 180  ### Return Description: - `percentile_data`: Percentile data   - `ctr_percentile`: Click-through rate percentile (0-100)   - `cvr_percentile`: Conversion rate percentile   - `engagement_percentile`: Engagement rate percentile   - `view_percentile`: View count percentile   - `industry_average`: Industry average comparison  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",   \"params\": {     \"material_id\": \"7213258221116751874\"   },   \"data\": {     \"percentile_data\": {       \"ctr_percentile\": 85,       \"cvr_percentile\": 72,       \"engagement_percentile\": 90,       \"view_percentile\": 88,       \"industry_average\": {         \"ctr\": 2.5,         \"cvr\": 1.2,         \"engagement\": 5.8       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get_with_http_info(material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object material_id: 广告素材ID/Ad material ID (required)
        :param object metric: 分析指标/Analysis metric (ctr_percentile, time_attr_conversion_rate_percentile, click_cnt_percentile, time_attr_convert_cnt_percentile, show_cnt_percentile)
        :param object period_type: 时间范围(天)/Time period (days)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['material_id', 'metric', 'period_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'material_id' is set
        if self.api_client.client_side_validation and ('material_id' not in params or
                                                       params['material_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `material_id` when calling `get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'material_id' in params:
            query_params.append(('material_id', params['material_id']))  # noqa: E501
        if 'metric' in params:
            query_params.append(('metric', params['metric']))  # noqa: E501
        if 'period_type' in params:
            query_params.append(('period_type', params['period_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_ad_percentile', 'GET',
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

    def get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get(self, ads_id, **kwargs):  # noqa: E501
        """获取单个广告详情/Get single ad detail  # noqa: E501

        # [中文] ### 用途: - 获取TikTok单个广告的详细信息，包括广告素材、创作者信息、互动数据等 - 分析广告的表现指标，如观看量、点赞数、评论数等核心数据 - 帮助广告主和营销人员深入了解特定广告的效果和用户反馈  ### 参数: - ads_id: 广告ID，必填参数，可从广告列表或TikTok Ads Creative Center获取  ### 返回内容说明: - `ad_title`: 广告标题 - `brand_name`: 品牌名称 - `comment`: 评论数 - `cost`: 花费等级(1-5) - `country_code`: 投放国家代码列表 - `ctr`: 点击率（百分比） - `favorite`: 是否收藏 - `has_summary`: 是否有摘要 - `highlight_text`: 高亮文本 - `id`: 广告ID - `industry_key`: 行业标签 - `is_search`: 是否搜索结果 - `keyword_list`: 关键词列表 - `landing_page`: 落地页URL - `like`: 点赞数 - `objective_key`: 广告目标键 - `objectives`: 广告目标列表   - `label`: 目标标签   - `value`: 目标值 - `pattern_label`: 模式标签列表 - `share`: 分享数 - `source`: 来源 - `source_key`: 来源键值 - `tag`: 标签 - `video_info`: 视频信息   - `vid`: 视频ID   - `duration`: 时长（秒）   - `cover`: 封面图URL   - `video_url`: 视频播放地址     - `720p`: 720p质量视频URL   - `width`: 视频宽度   - `height`: 视频高度 - `voice_over`: 是否有配音  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",   \"params\": {     \"ads_id\": \"7131673574381518849\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",       \"brand_name\": \"The Bamboo Breeze Shop\",       \"comment\": 232,       \"cost\": 2,       \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],       \"ctr\": 0.14,       \"favorite\": false,       \"has_summary\": true,       \"highlight_text\": \"\",       \"id\": \"7131673574381518849\",       \"industry_key\": \"label_29100000000\",       \"is_search\": false,       \"keyword_list\": [         \"adjustable back posture corrector\",         \"poor posture\",         \"eliminate unnecessary back pain\"       ],       \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-corrector\",       \"like\": 61242,       \"objective_key\": \"campaign_objective_conversion\",       \"objectives\": [         {           \"label\": \"campaign_objective_conversion\",           \"value\": 3         },         {           \"label\": \"campaign_objective_product_sales\",           \"value\": 15         }       ],       \"pattern_label\": [],       \"share\": 6486,       \"source\": \"TikTok Ads Manager\",       \"source_key\": 1,       \"tag\": 3,       \"video_info\": {         \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",         \"duration\": 17,         \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",         \"video_url\": {           \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"         },         \"width\": 576,         \"height\": 1024       },       \"voice_over\": true     }   } } ```  # [English] ### Purpose: - Retrieve detailed information about a single TikTok ad, including creative content, creator info, and engagement data - Analyze ad performance metrics such as views, likes, comments, and other core statistics - Help advertisers and marketers gain deep insights into specific ad effectiveness and user feedback  ### Parameters: - ads_id: Ad ID, required parameter, can be obtained from ad lists or TikTok Ads Creative Center  ### Return Description: - `ad_title`: Ad title - `brand_name`: Brand name - `comment`: Comment count - `cost`: Cost level (1-5) - `country_code`: List of target country codes - `ctr`: Click-through rate (percentage) - `favorite`: Whether favorited - `has_summary`: Whether has summary - `highlight_text`: Highlight text - `id`: Ad ID - `industry_key`: Industry label - `is_search`: Whether from search results - `keyword_list`: List of keywords - `landing_page`: Landing page URL - `like`: Like count - `objective_key`: Ad objective key - `objectives`: List of ad objectives   - `label`: Objective label   - `value`: Objective value - `pattern_label`: List of pattern labels - `share`: Share count - `source`: Source - `source_key`: Source key value - `tag`: Tag - `video_info`: Video information   - `vid`: Video ID   - `duration`: Duration (seconds)   - `cover`: Cover image URL   - `video_url`: Video playback URLs     - `720p`: 720p quality video URL   - `width`: Video width   - `height`: Video height - `voice_over`: Whether has voice over  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",   \"params\": {     \"ads_id\": \"7131673574381518849\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",       \"brand_name\": \"The Bamboo Breeze Shop\",       \"comment\": 232,       \"cost\": 2,       \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],       \"ctr\": 0.14,       \"favorite\": false,       \"has_summary\": true,       \"highlight_text\": \"\",       \"id\": \"7131673574381518849\",       \"industry_key\": \"label_29100000000\",       \"is_search\": false,       \"keyword_list\": [         \"adjustable back posture corrector\",         \"poor posture\",         \"eliminate unnecessary back pain\"       ],       \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-corrector\",       \"like\": 61242,       \"objective_key\": \"campaign_objective_conversion\",       \"objectives\": [         {           \"label\": \"campaign_objective_conversion\",           \"value\": 3         },         {           \"label\": \"campaign_objective_product_sales\",           \"value\": 15         }       ],       \"pattern_label\": [],       \"share\": 6486,       \"source\": \"TikTok Ads Manager\",       \"source_key\": 1,       \"tag\": 3,       \"video_info\": {         \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",         \"duration\": 17,         \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",         \"video_url\": {           \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"         },         \"width\": 576,         \"height\": 1024       },       \"voice_over\": true     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get(ads_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ads_id: 广告ID/Ad ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get_with_http_info(ads_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get_with_http_info(ads_id, **kwargs)  # noqa: E501
            return data

    def get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get_with_http_info(self, ads_id, **kwargs):  # noqa: E501
        """获取单个广告详情/Get single ad detail  # noqa: E501

        # [中文] ### 用途: - 获取TikTok单个广告的详细信息，包括广告素材、创作者信息、互动数据等 - 分析广告的表现指标，如观看量、点赞数、评论数等核心数据 - 帮助广告主和营销人员深入了解特定广告的效果和用户反馈  ### 参数: - ads_id: 广告ID，必填参数，可从广告列表或TikTok Ads Creative Center获取  ### 返回内容说明: - `ad_title`: 广告标题 - `brand_name`: 品牌名称 - `comment`: 评论数 - `cost`: 花费等级(1-5) - `country_code`: 投放国家代码列表 - `ctr`: 点击率（百分比） - `favorite`: 是否收藏 - `has_summary`: 是否有摘要 - `highlight_text`: 高亮文本 - `id`: 广告ID - `industry_key`: 行业标签 - `is_search`: 是否搜索结果 - `keyword_list`: 关键词列表 - `landing_page`: 落地页URL - `like`: 点赞数 - `objective_key`: 广告目标键 - `objectives`: 广告目标列表   - `label`: 目标标签   - `value`: 目标值 - `pattern_label`: 模式标签列表 - `share`: 分享数 - `source`: 来源 - `source_key`: 来源键值 - `tag`: 标签 - `video_info`: 视频信息   - `vid`: 视频ID   - `duration`: 时长（秒）   - `cover`: 封面图URL   - `video_url`: 视频播放地址     - `720p`: 720p质量视频URL   - `width`: 视频宽度   - `height`: 视频高度 - `voice_over`: 是否有配音  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",   \"params\": {     \"ads_id\": \"7131673574381518849\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",       \"brand_name\": \"The Bamboo Breeze Shop\",       \"comment\": 232,       \"cost\": 2,       \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],       \"ctr\": 0.14,       \"favorite\": false,       \"has_summary\": true,       \"highlight_text\": \"\",       \"id\": \"7131673574381518849\",       \"industry_key\": \"label_29100000000\",       \"is_search\": false,       \"keyword_list\": [         \"adjustable back posture corrector\",         \"poor posture\",         \"eliminate unnecessary back pain\"       ],       \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-corrector\",       \"like\": 61242,       \"objective_key\": \"campaign_objective_conversion\",       \"objectives\": [         {           \"label\": \"campaign_objective_conversion\",           \"value\": 3         },         {           \"label\": \"campaign_objective_product_sales\",           \"value\": 15         }       ],       \"pattern_label\": [],       \"share\": 6486,       \"source\": \"TikTok Ads Manager\",       \"source_key\": 1,       \"tag\": 3,       \"video_info\": {         \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",         \"duration\": 17,         \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",         \"video_url\": {           \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"         },         \"width\": 576,         \"height\": 1024       },       \"voice_over\": true     }   } } ```  # [English] ### Purpose: - Retrieve detailed information about a single TikTok ad, including creative content, creator info, and engagement data - Analyze ad performance metrics such as views, likes, comments, and other core statistics - Help advertisers and marketers gain deep insights into specific ad effectiveness and user feedback  ### Parameters: - ads_id: Ad ID, required parameter, can be obtained from ad lists or TikTok Ads Creative Center  ### Return Description: - `ad_title`: Ad title - `brand_name`: Brand name - `comment`: Comment count - `cost`: Cost level (1-5) - `country_code`: List of target country codes - `ctr`: Click-through rate (percentage) - `favorite`: Whether favorited - `has_summary`: Whether has summary - `highlight_text`: Highlight text - `id`: Ad ID - `industry_key`: Industry label - `is_search`: Whether from search results - `keyword_list`: List of keywords - `landing_page`: Landing page URL - `like`: Like count - `objective_key`: Ad objective key - `objectives`: List of ad objectives   - `label`: Objective label   - `value`: Objective value - `pattern_label`: List of pattern labels - `share`: Share count - `source`: Source - `source_key`: Source key value - `tag`: Tag - `video_info`: Video information   - `vid`: Video ID   - `duration`: Duration (seconds)   - `cover`: Cover image URL   - `video_url`: Video playback URLs     - `720p`: 720p quality video URL   - `width`: Video width   - `height`: Video height - `voice_over`: Whether has voice over  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",   \"params\": {     \"ads_id\": \"7131673574381518849\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",       \"brand_name\": \"The Bamboo Breeze Shop\",       \"comment\": 232,       \"cost\": 2,       \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],       \"ctr\": 0.14,       \"favorite\": false,       \"has_summary\": true,       \"highlight_text\": \"\",       \"id\": \"7131673574381518849\",       \"industry_key\": \"label_29100000000\",       \"is_search\": false,       \"keyword_list\": [         \"adjustable back posture corrector\",         \"poor posture\",         \"eliminate unnecessary back pain\"       ],       \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-corrector\",       \"like\": 61242,       \"objective_key\": \"campaign_objective_conversion\",       \"objectives\": [         {           \"label\": \"campaign_objective_conversion\",           \"value\": 3         },         {           \"label\": \"campaign_objective_product_sales\",           \"value\": 15         }       ],       \"pattern_label\": [],       \"share\": 6486,       \"source\": \"TikTok Ads Manager\",       \"source_key\": 1,       \"tag\": 3,       \"video_info\": {         \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",         \"duration\": 17,         \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",         \"video_url\": {           \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"         },         \"width\": 576,         \"height\": 1024       },       \"voice_over\": true     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get_with_http_info(ads_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ads_id: 广告ID/Ad ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ads_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ads_id' is set
        if self.api_client.client_side_validation and ('ads_id' not in params or
                                                       params['ads_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ads_id` when calling `get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ads_id' in params:
            query_params.append(('ads_id', params['ads_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_ads_detail', 'GET',
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

    def get_creative_patterns_api_v1_tiktok_ads_get_creative_patterns_get(self, **kwargs):  # noqa: E501
        """获取创意模式排行榜/Get creative pattern rankings  # noqa: E501

        # [中文] ### 用途: - 获取特定行业的创意模式排行榜，了解哪些创意模式效果最好 - 分析不同创意模式的点击率、完播率等关键指标 - 为广告创意制作提供数据支持的最佳实践  ### 参数: - first_industry_id: 行业ID，如游戏行业：25000000000 - period_type: 时间类型，\"week\"=周数据，\"month\"=月数据 - order_field: 排序字段，\"ctr\"=点击率，\"play_over_rate\"=播放完成率 - order_type: 排序方式，desc（降序）或asc（升序） - week: 查看特定周的数据，格式：YYYY-MM-DD（可选）  ### 返回内容说明: - `list`: 创意模式列表   - `label_info`: 模式标签信息     - `value`: 模式名称     - `description`: 模式描述   - `ctr`: 点击率（百分比）   - `play_over_rate`: 播放完成率（百分比）   - `avg_watch_time`: 平均观看时长   - `example_count`: 示例数量  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",   \"params\": {     \"first_industry_id\": \"25000000000\",     \"period_type\": \"week\",     \"order_field\": \"ctr\"   },   \"data\": {     \"list\": [       {         \"label_info\": {           \"value\": \"Problem-Solution\",           \"description\": \"Present a problem and show the solution\"         },         \"ctr\": 4.5,         \"play_over_rate\": 68.2,         \"avg_watch_time\": 12.3,         \"example_count\": 234       }     ]   } } ```  # [English] ### Purpose: - Get creative pattern rankings for specific industries to understand which patterns perform best - Analyze key metrics like CTR and completion rate for different creative patterns - Provide data-driven best practices for ad creative production  ### Parameters: - first_industry_id: Industry ID, e.g., Games: 25000000000 - period_type: Period type, \"week\"=Weekly data, \"month\"=Monthly data - order_field: Sort field, \"ctr\"=Click-through rate, \"play_over_rate\"=Completion rate - order_type: Sort order, desc (descending) or asc (ascending) - week: View data for specific week, format: YYYY-MM-DD (optional)  ### Return Description: - `list`: Creative pattern list   - `label_info`: Pattern label information     - `value`: Pattern name     - `description`: Pattern description   - `ctr`: Click-through rate (percentage)   - `play_over_rate`: Play completion rate (percentage)   - `avg_watch_time`: Average watch time   - `example_count`: Number of examples  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",   \"params\": {     \"first_industry_id\": \"25000000000\",     \"period_type\": \"week\",     \"order_field\": \"ctr\"   },   \"data\": {     \"list\": [       {         \"label_info\": {           \"value\": \"Problem-Solution\",           \"description\": \"Present a problem and show the solution\"         },         \"ctr\": 4.5,         \"play_over_rate\": 68.2,         \"avg_watch_time\": 12.3,         \"example_count\": 234       }     ]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_creative_patterns_api_v1_tiktok_ads_get_creative_patterns_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object first_industry_id: 一级行业ID/First industry ID
        :param object period_type: 时间周期类型/Period type (week, month)
        :param object order_field: 排序字段/Order field (ctr, play_over_rate)
        :param object order_type: 排序方式/Sort order (desc, asc)
        :param object week: 特定周（可选）/Specific week (optional)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_creative_patterns_api_v1_tiktok_ads_get_creative_patterns_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_creative_patterns_api_v1_tiktok_ads_get_creative_patterns_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_creative_patterns_api_v1_tiktok_ads_get_creative_patterns_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创意模式排行榜/Get creative pattern rankings  # noqa: E501

        # [中文] ### 用途: - 获取特定行业的创意模式排行榜，了解哪些创意模式效果最好 - 分析不同创意模式的点击率、完播率等关键指标 - 为广告创意制作提供数据支持的最佳实践  ### 参数: - first_industry_id: 行业ID，如游戏行业：25000000000 - period_type: 时间类型，\"week\"=周数据，\"month\"=月数据 - order_field: 排序字段，\"ctr\"=点击率，\"play_over_rate\"=播放完成率 - order_type: 排序方式，desc（降序）或asc（升序） - week: 查看特定周的数据，格式：YYYY-MM-DD（可选）  ### 返回内容说明: - `list`: 创意模式列表   - `label_info`: 模式标签信息     - `value`: 模式名称     - `description`: 模式描述   - `ctr`: 点击率（百分比）   - `play_over_rate`: 播放完成率（百分比）   - `avg_watch_time`: 平均观看时长   - `example_count`: 示例数量  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",   \"params\": {     \"first_industry_id\": \"25000000000\",     \"period_type\": \"week\",     \"order_field\": \"ctr\"   },   \"data\": {     \"list\": [       {         \"label_info\": {           \"value\": \"Problem-Solution\",           \"description\": \"Present a problem and show the solution\"         },         \"ctr\": 4.5,         \"play_over_rate\": 68.2,         \"avg_watch_time\": 12.3,         \"example_count\": 234       }     ]   } } ```  # [English] ### Purpose: - Get creative pattern rankings for specific industries to understand which patterns perform best - Analyze key metrics like CTR and completion rate for different creative patterns - Provide data-driven best practices for ad creative production  ### Parameters: - first_industry_id: Industry ID, e.g., Games: 25000000000 - period_type: Period type, \"week\"=Weekly data, \"month\"=Monthly data - order_field: Sort field, \"ctr\"=Click-through rate, \"play_over_rate\"=Completion rate - order_type: Sort order, desc (descending) or asc (ascending) - week: View data for specific week, format: YYYY-MM-DD (optional)  ### Return Description: - `list`: Creative pattern list   - `label_info`: Pattern label information     - `value`: Pattern name     - `description`: Pattern description   - `ctr`: Click-through rate (percentage)   - `play_over_rate`: Play completion rate (percentage)   - `avg_watch_time`: Average watch time   - `example_count`: Number of examples  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",   \"params\": {     \"first_industry_id\": \"25000000000\",     \"period_type\": \"week\",     \"order_field\": \"ctr\"   },   \"data\": {     \"list\": [       {         \"label_info\": {           \"value\": \"Problem-Solution\",           \"description\": \"Present a problem and show the solution\"         },         \"ctr\": 4.5,         \"play_over_rate\": 68.2,         \"avg_watch_time\": 12.3,         \"example_count\": 234       }     ]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_creative_patterns_api_v1_tiktok_ads_get_creative_patterns_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object first_industry_id: 一级行业ID/First industry ID
        :param object period_type: 时间周期类型/Period type (week, month)
        :param object order_field: 排序字段/Order field (ctr, play_over_rate)
        :param object order_type: 排序方式/Sort order (desc, asc)
        :param object week: 特定周（可选）/Specific week (optional)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['first_industry_id', 'period_type', 'order_field', 'order_type', 'week', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_creative_patterns_api_v1_tiktok_ads_get_creative_patterns_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'first_industry_id' in params:
            query_params.append(('first_industry_id', params['first_industry_id']))  # noqa: E501
        if 'period_type' in params:
            query_params.append(('period_type', params['period_type']))  # noqa: E501
        if 'order_field' in params:
            query_params.append(('order_field', params['order_field']))  # noqa: E501
        if 'order_type' in params:
            query_params.append(('order_type', params['order_type']))  # noqa: E501
        if 'week' in params:
            query_params.append(('week', params['week']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_creative_patterns', 'GET',
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

    def get_creator_filters_api_v1_tiktok_ads_get_creator_filters_get(self, **kwargs):  # noqa: E501
        """获取创作者筛选器/Get creator filters  # noqa: E501

        # [中文] ### 用途: - 获取创作者搜索和筛选的可用选项 - 了解支持的国家、排序方式等筛选维度 - 为创作者分析提供参数参考  ### 返回内容说明: - `audience_country`: 受众国家列表   - `id`: 国家代码   - `value`: 国家名称 - `creator_country`: 创作者所在国家列表 - `sort_by`: 支持的排序方式   - follower: 按粉丝数排序   - engagement: 按互动率排序   - avg_views: 按平均观看量排序  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",   \"params\": {},   \"data\": {     \"audience_country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"creator_country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]   } } ```  # [English] ### Purpose: - Get available options for creator search and filtering - Understand supported countries, sorting methods and other filter dimensions - Provide parameter reference for creator analysis  ### Return Description: - `audience_country`: Audience country list   - `id`: Country code   - `value`: Country name - `creator_country`: Creator country list - `sort_by`: Supported sorting methods   - follower: Sort by follower count   - engagement: Sort by engagement rate   - avg_views: Sort by average views  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",   \"params\": {},   \"data\": {     \"audience_country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"creator_country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_creator_filters_api_v1_tiktok_ads_get_creator_filters_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_creator_filters_api_v1_tiktok_ads_get_creator_filters_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_creator_filters_api_v1_tiktok_ads_get_creator_filters_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_creator_filters_api_v1_tiktok_ads_get_creator_filters_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者筛选器/Get creator filters  # noqa: E501

        # [中文] ### 用途: - 获取创作者搜索和筛选的可用选项 - 了解支持的国家、排序方式等筛选维度 - 为创作者分析提供参数参考  ### 返回内容说明: - `audience_country`: 受众国家列表   - `id`: 国家代码   - `value`: 国家名称 - `creator_country`: 创作者所在国家列表 - `sort_by`: 支持的排序方式   - follower: 按粉丝数排序   - engagement: 按互动率排序   - avg_views: 按平均观看量排序  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",   \"params\": {},   \"data\": {     \"audience_country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"creator_country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]   } } ```  # [English] ### Purpose: - Get available options for creator search and filtering - Understand supported countries, sorting methods and other filter dimensions - Provide parameter reference for creator analysis  ### Return Description: - `audience_country`: Audience country list   - `id`: Country code   - `value`: Country name - `creator_country`: Creator country list - `sort_by`: Supported sorting methods   - follower: Sort by follower count   - engagement: Sort by engagement rate   - avg_views: Sort by average views  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",   \"params\": {},   \"data\": {     \"audience_country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"creator_country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_creator_filters_api_v1_tiktok_ads_get_creator_filters_get_with_http_info(async_req=True)
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
                    " to method get_creator_filters_api_v1_tiktok_ads_get_creator_filters_get" % key
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
            '/api/v1/tiktok/ads/get_creator_filters', 'GET',
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

    def get_creator_list_api_v1_tiktok_ads_get_creator_list_get(self, **kwargs):  # noqa: E501
        """获取创作者列表/Get creator list  # noqa: E501

        # [中文] ### 用途: - 获取符合条件的创作者列表，包括粉丝数、互动率等数据 - 发现高质量的广告合作创作者 - 分析不同类型创作者的表现和特点  ### 参数: - page: 页码，默认1 - limit: 每页数量，默认20 - sort_by: 排序方式   - follower: 按粉丝数排序   - engagement: 按互动率排序   - avg_views: 按平均观看量排序 - creator_country: 创作者所在国家 - audience_country: 受众所在国家（可选） - audience_count: 受众数量筛选（可选）  ### 返回内容说明: - `creators`: 创作者列表   - `tcm_id`: TCM ID   - `user_id`: 用户ID   - `nick_name`: 昵称   - `avatar_url`: 头像URL   - `country_code`: 国家代码   - `follower_cnt`: 粉丝数   - `liked_cnt`: 获赞总数   - `tt_link`: TikTok链接   - `tcm_link`: TCM链接   - `items`: 作品列表     - `item_id`: 作品ID     - `cover_url`: 封面URL     - `tt_link`: TikTok链接     - `vv`: 观看量     - `liked_cnt`: 点赞数     - `create_time`: 创建时间 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creator_list\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"sort_by\": \"follower\",     \"creator_country\": \"US\",     \"audience_country\": \"\",     \"audience_count\": \"0\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"7414477993612935173\",           \"user_id\": \"62133858422239232\",           \"nick_name\": \"Fernanda\",           \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",           \"country_code\": \"US\",           \"follower_cnt\": 9135515,           \"liked_cnt\": 668294555,           \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",           \"items\": [             {               \"item_id\": \"7444674312784645432\",               \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",               \"vv\": 13733332,               \"liked_cnt\": 516217,               \"create_time\": 1733348322             }           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 459,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get a list of creators matching criteria, including follower count, engagement rate, etc. - Discover high-quality creators for ad collaboration - Analyze performance and characteristics of different creator types  ### Parameters: - page: Page number, default 1 - limit: Items per page, default 20 - sort_by: Sorting method   - follower: Sort by follower count   - engagement: Sort by engagement rate   - avg_views: Sort by average views - creator_country: Creator's country - audience_country: Audience country (optional) - audience_count: Audience count filter (optional)  ### Return Description: - `creators`: Creator list   - `tcm_id`: TikTok Creator Marketplace ID   - `user_id`: User ID   - `nick_name`: Nickname   - `avatar_url`: Avatar URL   - `country_code`: Country code   - `follower_cnt`: Follower count   - `liked_cnt`: Total likes count   - `tt_link`: TikTok profile link   - `tcm_link`: Creator marketplace link   - `items`: Video list     - `item_id`: Video ID     - `cover_url`: Cover image URL     - `tt_link`: Video link     - `vv`: View count     - `liked_cnt`: Like count     - `create_time`: Creation timestamp - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Has more pages  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creator_list\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"sort_by\": \"follower\",     \"creator_country\": \"US\",     \"audience_country\": \"\",     \"audience_count\": \"0\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"7414477993612935173\",           \"user_id\": \"62133858422239232\",           \"nick_name\": \"Fernanda\",           \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",           \"country_code\": \"US\",           \"follower_cnt\": 9135515,           \"liked_cnt\": 668294555,           \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",           \"items\": [             {               \"item_id\": \"7444674312784645432\",               \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",               \"vv\": 13733332,               \"liked_cnt\": 516217,               \"create_time\": 1733348322             }           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 459,         \"has_more\": true       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_creator_list_api_v1_tiktok_ads_get_creator_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object sort_by: 排序方式/Sort by (follower, engagement, avg_views)
        :param object creator_country: 创作者国家/Creator country
        :param object audience_country: 受众国家/Audience country
        :param object audience_count: 受众数量筛选/Audience count filter
        :param object keyword: 关键词/Keyword
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_creator_list_api_v1_tiktok_ads_get_creator_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_creator_list_api_v1_tiktok_ads_get_creator_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_creator_list_api_v1_tiktok_ads_get_creator_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取创作者列表/Get creator list  # noqa: E501

        # [中文] ### 用途: - 获取符合条件的创作者列表，包括粉丝数、互动率等数据 - 发现高质量的广告合作创作者 - 分析不同类型创作者的表现和特点  ### 参数: - page: 页码，默认1 - limit: 每页数量，默认20 - sort_by: 排序方式   - follower: 按粉丝数排序   - engagement: 按互动率排序   - avg_views: 按平均观看量排序 - creator_country: 创作者所在国家 - audience_country: 受众所在国家（可选） - audience_count: 受众数量筛选（可选）  ### 返回内容说明: - `creators`: 创作者列表   - `tcm_id`: TCM ID   - `user_id`: 用户ID   - `nick_name`: 昵称   - `avatar_url`: 头像URL   - `country_code`: 国家代码   - `follower_cnt`: 粉丝数   - `liked_cnt`: 获赞总数   - `tt_link`: TikTok链接   - `tcm_link`: TCM链接   - `items`: 作品列表     - `item_id`: 作品ID     - `cover_url`: 封面URL     - `tt_link`: TikTok链接     - `vv`: 观看量     - `liked_cnt`: 点赞数     - `create_time`: 创建时间 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creator_list\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"sort_by\": \"follower\",     \"creator_country\": \"US\",     \"audience_country\": \"\",     \"audience_count\": \"0\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"7414477993612935173\",           \"user_id\": \"62133858422239232\",           \"nick_name\": \"Fernanda\",           \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",           \"country_code\": \"US\",           \"follower_cnt\": 9135515,           \"liked_cnt\": 668294555,           \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",           \"items\": [             {               \"item_id\": \"7444674312784645432\",               \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",               \"vv\": 13733332,               \"liked_cnt\": 516217,               \"create_time\": 1733348322             }           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 459,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get a list of creators matching criteria, including follower count, engagement rate, etc. - Discover high-quality creators for ad collaboration - Analyze performance and characteristics of different creator types  ### Parameters: - page: Page number, default 1 - limit: Items per page, default 20 - sort_by: Sorting method   - follower: Sort by follower count   - engagement: Sort by engagement rate   - avg_views: Sort by average views - creator_country: Creator's country - audience_country: Audience country (optional) - audience_count: Audience count filter (optional)  ### Return Description: - `creators`: Creator list   - `tcm_id`: TikTok Creator Marketplace ID   - `user_id`: User ID   - `nick_name`: Nickname   - `avatar_url`: Avatar URL   - `country_code`: Country code   - `follower_cnt`: Follower count   - `liked_cnt`: Total likes count   - `tt_link`: TikTok profile link   - `tcm_link`: Creator marketplace link   - `items`: Video list     - `item_id`: Video ID     - `cover_url`: Cover image URL     - `tt_link`: Video link     - `vv`: View count     - `liked_cnt`: Like count     - `create_time`: Creation timestamp - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Has more pages  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_creator_list\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"sort_by\": \"follower\",     \"creator_country\": \"US\",     \"audience_country\": \"\",     \"audience_count\": \"0\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"7414477993612935173\",           \"user_id\": \"62133858422239232\",           \"nick_name\": \"Fernanda\",           \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",           \"country_code\": \"US\",           \"follower_cnt\": 9135515,           \"liked_cnt\": 668294555,           \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",           \"items\": [             {               \"item_id\": \"7444674312784645432\",               \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",               \"vv\": 13733332,               \"liked_cnt\": 516217,               \"create_time\": 1733348322             }           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 459,         \"has_more\": true       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_creator_list_api_v1_tiktok_ads_get_creator_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object sort_by: 排序方式/Sort by (follower, engagement, avg_views)
        :param object creator_country: 创作者国家/Creator country
        :param object audience_country: 受众国家/Audience country
        :param object audience_count: 受众数量筛选/Audience count filter
        :param object keyword: 关键词/Keyword
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'sort_by', 'creator_country', 'audience_country', 'audience_count', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_creator_list_api_v1_tiktok_ads_get_creator_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'creator_country' in params:
            query_params.append(('creator_country', params['creator_country']))  # noqa: E501
        if 'audience_country' in params:
            query_params.append(('audience_country', params['audience_country']))  # noqa: E501
        if 'audience_count' in params:
            query_params.append(('audience_count', params['audience_count']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_creator_list', 'GET',
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

    def get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get(self, hashtag, **kwargs):  # noqa: E501
        """获取标签创作者信息/Get hashtag creator info  # noqa: E501

        # [中文] ### 用途: - 获取特定标签的创作者信息和相关数据 - 了解标签的来源、创建者和使用情况 - 分析标签的影响力和传播路径  ### 参数: - hashtag_name: 标签名称，不需要包含#号  ### 返回内容说明: - `creators`: 创作者列表   - `tcm_id`: TCM ID   - `user_id`: 用户ID   - `nick_name`: 昵称   - `avatar_url`: 头像URL   - `follower_cnt`: 粉丝数   - `liked_cnt`: 获赞总数   - `tt_link`: TikTok链接   - `tcm_link`: TCM链接   - `items`: 作品列表     - `item_id`: 作品ID     - `cover_url`: 封面URL     - `tt_link`: TikTok链接     - `vv`: 观看量     - `liked_cnt`: 点赞数     - `create_time`: 创建时间  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",   \"params\": {     \"hashtag_name\": \"blowup\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"7153957957875531782\",           \"user_id\": \"7137978712880088065\",           \"nick_name\": \"Ben🎧\",           \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",           \"follower_cnt\": 1123490,           \"liked_cnt\": 45506383,           \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",           \"items\": [             {               \"item_id\": \"7484029831462522119\",               \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",               \"vv\": 1068946,               \"liked_cnt\": 124292,               \"create_time\": 1742511489             },             {               \"item_id\": \"7483385475252751623\",               \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0037/oUew2qzADECItXAWFYGeoPQftQEZYPjUKLyIuM~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7483385475252751623\",               \"vv\": 239239,               \"liked_cnt\": 16919,               \"create_time\": 1742361463             }           ]         }       ]     }   } } ```  # [English] ### Purpose: - Get creator information and related data for specific hashtags - Understand hashtag origin, creator and usage - Analyze hashtag influence and spread path  ### Parameters: - hashtag_name: Hashtag name without # symbol  ### Return Description: - `creators`: Creator list   - `tcm_id`: TCM ID   - `user_id`: User ID   - `nick_name`: Nickname   - `avatar_url`: Avatar URL   - `follower_cnt`: Follower count   - `liked_cnt`: Total likes received   - `tt_link`: TikTok link   - `tcm_link`: TCM link   - `items`: Items list     - `item_id`: Item ID     - `cover_url`: Cover URL     - `tt_link`: TikTok link     - `vv`: View count     - `liked_cnt`: Like count     - `create_time`: Creation time  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",   \"params\": {     \"hashtag_name\": \"blowup\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"7153957957875531782\",           \"user_id\": \"7137978712880088065\",           \"nick_name\": \"Ben🎧\",           \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",           \"follower_cnt\": 1123490,           \"liked_cnt\": 45506383,           \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",           \"items\": [             {               \"item_id\": \"7484029831462522119\",               \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",               \"vv\": 1068946,               \"liked_cnt\": 124292,               \"create_time\": 1742511489             }           ]         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get(hashtag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object hashtag: 标签名称，不包含#符号/Hashtag name (without # symbol) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get_with_http_info(hashtag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get_with_http_info(hashtag, **kwargs)  # noqa: E501
            return data

    def get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get_with_http_info(self, hashtag, **kwargs):  # noqa: E501
        """获取标签创作者信息/Get hashtag creator info  # noqa: E501

        # [中文] ### 用途: - 获取特定标签的创作者信息和相关数据 - 了解标签的来源、创建者和使用情况 - 分析标签的影响力和传播路径  ### 参数: - hashtag_name: 标签名称，不需要包含#号  ### 返回内容说明: - `creators`: 创作者列表   - `tcm_id`: TCM ID   - `user_id`: 用户ID   - `nick_name`: 昵称   - `avatar_url`: 头像URL   - `follower_cnt`: 粉丝数   - `liked_cnt`: 获赞总数   - `tt_link`: TikTok链接   - `tcm_link`: TCM链接   - `items`: 作品列表     - `item_id`: 作品ID     - `cover_url`: 封面URL     - `tt_link`: TikTok链接     - `vv`: 观看量     - `liked_cnt`: 点赞数     - `create_time`: 创建时间  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",   \"params\": {     \"hashtag_name\": \"blowup\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"7153957957875531782\",           \"user_id\": \"7137978712880088065\",           \"nick_name\": \"Ben🎧\",           \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",           \"follower_cnt\": 1123490,           \"liked_cnt\": 45506383,           \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",           \"items\": [             {               \"item_id\": \"7484029831462522119\",               \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",               \"vv\": 1068946,               \"liked_cnt\": 124292,               \"create_time\": 1742511489             },             {               \"item_id\": \"7483385475252751623\",               \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0037/oUew2qzADECItXAWFYGeoPQftQEZYPjUKLyIuM~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7483385475252751623\",               \"vv\": 239239,               \"liked_cnt\": 16919,               \"create_time\": 1742361463             }           ]         }       ]     }   } } ```  # [English] ### Purpose: - Get creator information and related data for specific hashtags - Understand hashtag origin, creator and usage - Analyze hashtag influence and spread path  ### Parameters: - hashtag_name: Hashtag name without # symbol  ### Return Description: - `creators`: Creator list   - `tcm_id`: TCM ID   - `user_id`: User ID   - `nick_name`: Nickname   - `avatar_url`: Avatar URL   - `follower_cnt`: Follower count   - `liked_cnt`: Total likes received   - `tt_link`: TikTok link   - `tcm_link`: TCM link   - `items`: Items list     - `item_id`: Item ID     - `cover_url`: Cover URL     - `tt_link`: TikTok link     - `vv`: View count     - `liked_cnt`: Like count     - `create_time`: Creation time  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",   \"params\": {     \"hashtag_name\": \"blowup\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"7153957957875531782\",           \"user_id\": \"7137978712880088065\",           \"nick_name\": \"Ben🎧\",           \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",           \"follower_cnt\": 1123490,           \"liked_cnt\": 45506383,           \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",           \"items\": [             {               \"item_id\": \"7484029831462522119\",               \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",               \"vv\": 1068946,               \"liked_cnt\": 124292,               \"create_time\": 1742511489             }           ]         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get_with_http_info(hashtag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object hashtag: 标签名称，不包含#符号/Hashtag name (without # symbol) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hashtag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hashtag' is set
        if self.api_client.client_side_validation and ('hashtag' not in params or
                                                       params['hashtag'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `hashtag` when calling `get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hashtag' in params:
            query_params.append(('hashtag', params['hashtag']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_hashtag_creator', 'GET',
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

    def get_hashtag_filters_api_v1_tiktok_ads_get_hashtag_filters_get(self, **kwargs):  # noqa: E501
        """获取标签筛选器/Get hashtag filters  # noqa: E501

        # [中文] ### 用途: - 获取热门标签功能的可用筛选选项 - 了解支持的国家/地区、行业等筛选维度 - 为标签分析提供筛选参数参考  ### 返回内容说明: - `country`: 支持的国家/地区列表   - `id`: 国家代码   - `value`: 国家名称 - `industry`: 支持的行业列表   - `id`: 行业ID   - `value`: 行业名称  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",   \"params\": {},   \"data\": {     \"country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"},       {\"id\": \"JP\", \"value\": \"Japan\"}     ],     \"industry\": [       {\"id\": \"27000000000\", \"value\": \"Games\"},       {\"id\": \"19000000000\", \"value\": \"E-commerce\"},       {\"id\": \"10000000000\", \"value\": \"Education\"}     ]   } } ```  # [English] ### Purpose: - Get available filter options for popular hashtag functionality - Understand supported countries/regions, industries and other filter dimensions - Provide filter parameter reference for hashtag analysis  ### Return Description: - `country`: List of supported countries/regions   - `id`: Country code   - `value`: Country name - `industry`: List of supported industries   - `id`: Industry ID   - `value`: Industry name  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",   \"params\": {},   \"data\": {     \"country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"},       {\"id\": \"JP\", \"value\": \"Japan\"}     ],     \"industry\": [       {\"id\": \"27000000000\", \"value\": \"Games\"},       {\"id\": \"19000000000\", \"value\": \"E-commerce\"},       {\"id\": \"10000000000\", \"value\": \"Education\"}     ]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hashtag_filters_api_v1_tiktok_ads_get_hashtag_filters_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_hashtag_filters_api_v1_tiktok_ads_get_hashtag_filters_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_hashtag_filters_api_v1_tiktok_ads_get_hashtag_filters_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_hashtag_filters_api_v1_tiktok_ads_get_hashtag_filters_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取标签筛选器/Get hashtag filters  # noqa: E501

        # [中文] ### 用途: - 获取热门标签功能的可用筛选选项 - 了解支持的国家/地区、行业等筛选维度 - 为标签分析提供筛选参数参考  ### 返回内容说明: - `country`: 支持的国家/地区列表   - `id`: 国家代码   - `value`: 国家名称 - `industry`: 支持的行业列表   - `id`: 行业ID   - `value`: 行业名称  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",   \"params\": {},   \"data\": {     \"country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"},       {\"id\": \"JP\", \"value\": \"Japan\"}     ],     \"industry\": [       {\"id\": \"27000000000\", \"value\": \"Games\"},       {\"id\": \"19000000000\", \"value\": \"E-commerce\"},       {\"id\": \"10000000000\", \"value\": \"Education\"}     ]   } } ```  # [English] ### Purpose: - Get available filter options for popular hashtag functionality - Understand supported countries/regions, industries and other filter dimensions - Provide filter parameter reference for hashtag analysis  ### Return Description: - `country`: List of supported countries/regions   - `id`: Country code   - `value`: Country name - `industry`: List of supported industries   - `id`: Industry ID   - `value`: Industry name  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",   \"params\": {},   \"data\": {     \"country\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"},       {\"id\": \"JP\", \"value\": \"Japan\"}     ],     \"industry\": [       {\"id\": \"27000000000\", \"value\": \"Games\"},       {\"id\": \"19000000000\", \"value\": \"E-commerce\"},       {\"id\": \"10000000000\", \"value\": \"Education\"}     ]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hashtag_filters_api_v1_tiktok_ads_get_hashtag_filters_get_with_http_info(async_req=True)
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
                    " to method get_hashtag_filters_api_v1_tiktok_ads_get_hashtag_filters_get" % key
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
            '/api/v1/tiktok/ads/get_hashtag_filters', 'GET',
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

    def get_hashtag_list_api_v1_tiktok_ads_get_hashtag_list_get(self, **kwargs):  # noqa: E501
        """获取热门标签列表/Get popular hashtags list  # noqa: E501

        # [中文] ### 用途: - 获取TikTok广告中的热门标签排行榜，了解当前流行的话题标签 - 分析标签的使用量、观看量等数据，发现潜力标签 - 帮助广告主选择合适的标签，提升广告曝光和互动率  ### 参数: - page: 页码，默认1 - limit: 每页数量，默认20 - period: 时间范围（天），如7、30、120天 - country_code: 国家代码，如US、UK、JP等 - sort_by: 排序方式，\"popular\"=热门，\"new\"=最新 - industry_id: 行业ID，留空返回所有行业 - filter_by: 筛选条件，\"new_on_board\"=新上榜标签  ### 返回内容说明: - `list`: 标签列表   - `hashtag_id`: 标签ID   - `hashtag_name`: 标签名称   - `country_info`: 国家信息     - `id`: 国家ID     - `value`: 国家名称     - `label`: 国家标签   - `industry_info`: 行业信息     - `id`: 行业ID     - `value`: 行业名称     - `label`: 行业标签   - `is_promoted`: 是否推广   - `trend`: 趋势数据列表     - `time`: 时间戳     - `value`: 该时间点的值   - `creators`: 创作者列表     - `nick_name`: 昵称     - `avatar_url`: 头像URL   - `publish_cnt`: 发布数量   - `video_views`: 视频观看量   - `rank`: 排名   - `rank_diff`: 排名变化   - `rank_diff_type`: 排名变化类型 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"120\",     \"country_code\": \"US\",     \"sort_by\": \"popular\",     \"industry_id\": \"\",     \"filter_by\": \"\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"list\": [         {           \"hashtag_id\": \"4100\",           \"hashtag_name\": \"summer\",           \"country_info\": {             \"id\": \"US\",             \"value\": \"United States\",             \"label\": \"US\"           },           \"industry_info\": {             \"id\": 28000000000,             \"value\": \"Sports & Outdoor\",             \"label\": \"label_28000000000\"           },           \"is_promoted\": false,           \"trend\": [             {               \"time\": 1740787200,               \"value\": 0.38             },             {               \"time\": 1741392000,               \"value\": 0.37             },             {               \"time\": 1741996800,               \"value\": 0.43             },             {               \"time\": 1749254400,               \"value\": 1             }           ],           \"creators\": [             {               \"nick_name\": \"Mark Broze\",               \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/28bb3ad309c2165f9579a67515d17ca9~tplv-tiktokx-cropcenter:100:100.png\"             },             {               \"nick_name\": \"Liam 🤠\",               \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/a27b40671c78f8af17cdd2618ad8ba20~tplv-tiktokx-cropcenter:100:100.png\"             }           ],           \"publish_cnt\": 2886791,           \"video_views\": 19583705445,           \"rank\": 1,           \"rank_diff\": 1,           \"rank_diff_type\": 1         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 100,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get popular hashtag rankings in TikTok ads to understand current trending topics - Analyze usage and view data for hashtags to discover potential tags - Help advertisers choose appropriate hashtags to increase ad exposure and engagement  ### Parameters: - page: Page number, default 1 - limit: Items per page, default 20 - period: Time period in days, e.g., 7, 30, 120 days - country_code: Country code, e.g., US, UK, JP - sort_by: Sort method, \"popular\"=Popular, \"new\"=Latest - industry_id: Industry ID, empty returns all industries - filter_by: Filter condition, \"new_on_board\"=Newly trending hashtags  ### Return Description: - `list`: Hashtag list   - `hashtag_id`: Hashtag ID   - `hashtag_name`: Hashtag name   - `country_info`: Country information     - `id`: Country ID     - `value`: Country name     - `label`: Country label   - `industry_info`: Industry information     - `id`: Industry ID     - `value`: Industry name     - `label`: Industry label   - `is_promoted`: Whether promoted   - `trend`: Trend data list     - `time`: Timestamp     - `value`: Value at that time point   - `creators`: Creator list     - `nick_name`: Nickname     - `avatar_url`: Avatar URL   - `publish_cnt`: Publish count   - `video_views`: Video views   - `rank`: Ranking   - `rank_diff`: Rank difference   - `rank_diff_type`: Rank difference type - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"120\",     \"country_code\": \"US\",     \"sort_by\": \"popular\",     \"industry_id\": \"\",     \"filter_by\": \"\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"list\": [         {           \"hashtag_id\": \"4100\",           \"hashtag_name\": \"summer\",           \"country_info\": {             \"id\": \"US\",             \"value\": \"United States\",             \"label\": \"US\"           },           \"industry_info\": {             \"id\": 28000000000,             \"value\": \"Sports & Outdoor\",             \"label\": \"label_28000000000\"           },           \"is_promoted\": false,           \"trend\": [             {               \"time\": 1740787200,               \"value\": 0.38             },             {               \"time\": 1741392000,               \"value\": 0.37             }           ],           \"creators\": [             {               \"nick_name\": \"creator1\",               \"avatar_url\": \"https://example.com/avatar1.jpg\"             }           ],           \"publish_cnt\": 45678,           \"video_views\": 123456789,           \"rank\": 1,           \"rank_diff\": 2,           \"rank_diff_type\": 1         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 500,         \"has_more\": true       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hashtag_list_api_v1_tiktok_ads_get_hashtag_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object period: 时间范围（天）/Time period (days)
        :param object country_code: 国家代码/Country code
        :param object sort_by: 排序方式/Sort by (popular, new)
        :param object industry_id: 行业ID/Industry ID
        :param object filter_by: 筛选条件/Filter (new_on_board)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_hashtag_list_api_v1_tiktok_ads_get_hashtag_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_hashtag_list_api_v1_tiktok_ads_get_hashtag_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_hashtag_list_api_v1_tiktok_ads_get_hashtag_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热门标签列表/Get popular hashtags list  # noqa: E501

        # [中文] ### 用途: - 获取TikTok广告中的热门标签排行榜，了解当前流行的话题标签 - 分析标签的使用量、观看量等数据，发现潜力标签 - 帮助广告主选择合适的标签，提升广告曝光和互动率  ### 参数: - page: 页码，默认1 - limit: 每页数量，默认20 - period: 时间范围（天），如7、30、120天 - country_code: 国家代码，如US、UK、JP等 - sort_by: 排序方式，\"popular\"=热门，\"new\"=最新 - industry_id: 行业ID，留空返回所有行业 - filter_by: 筛选条件，\"new_on_board\"=新上榜标签  ### 返回内容说明: - `list`: 标签列表   - `hashtag_id`: 标签ID   - `hashtag_name`: 标签名称   - `country_info`: 国家信息     - `id`: 国家ID     - `value`: 国家名称     - `label`: 国家标签   - `industry_info`: 行业信息     - `id`: 行业ID     - `value`: 行业名称     - `label`: 行业标签   - `is_promoted`: 是否推广   - `trend`: 趋势数据列表     - `time`: 时间戳     - `value`: 该时间点的值   - `creators`: 创作者列表     - `nick_name`: 昵称     - `avatar_url`: 头像URL   - `publish_cnt`: 发布数量   - `video_views`: 视频观看量   - `rank`: 排名   - `rank_diff`: 排名变化   - `rank_diff_type`: 排名变化类型 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"120\",     \"country_code\": \"US\",     \"sort_by\": \"popular\",     \"industry_id\": \"\",     \"filter_by\": \"\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"list\": [         {           \"hashtag_id\": \"4100\",           \"hashtag_name\": \"summer\",           \"country_info\": {             \"id\": \"US\",             \"value\": \"United States\",             \"label\": \"US\"           },           \"industry_info\": {             \"id\": 28000000000,             \"value\": \"Sports & Outdoor\",             \"label\": \"label_28000000000\"           },           \"is_promoted\": false,           \"trend\": [             {               \"time\": 1740787200,               \"value\": 0.38             },             {               \"time\": 1741392000,               \"value\": 0.37             },             {               \"time\": 1741996800,               \"value\": 0.43             },             {               \"time\": 1749254400,               \"value\": 1             }           ],           \"creators\": [             {               \"nick_name\": \"Mark Broze\",               \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/28bb3ad309c2165f9579a67515d17ca9~tplv-tiktokx-cropcenter:100:100.png\"             },             {               \"nick_name\": \"Liam 🤠\",               \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/a27b40671c78f8af17cdd2618ad8ba20~tplv-tiktokx-cropcenter:100:100.png\"             }           ],           \"publish_cnt\": 2886791,           \"video_views\": 19583705445,           \"rank\": 1,           \"rank_diff\": 1,           \"rank_diff_type\": 1         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 100,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get popular hashtag rankings in TikTok ads to understand current trending topics - Analyze usage and view data for hashtags to discover potential tags - Help advertisers choose appropriate hashtags to increase ad exposure and engagement  ### Parameters: - page: Page number, default 1 - limit: Items per page, default 20 - period: Time period in days, e.g., 7, 30, 120 days - country_code: Country code, e.g., US, UK, JP - sort_by: Sort method, \"popular\"=Popular, \"new\"=Latest - industry_id: Industry ID, empty returns all industries - filter_by: Filter condition, \"new_on_board\"=Newly trending hashtags  ### Return Description: - `list`: Hashtag list   - `hashtag_id`: Hashtag ID   - `hashtag_name`: Hashtag name   - `country_info`: Country information     - `id`: Country ID     - `value`: Country name     - `label`: Country label   - `industry_info`: Industry information     - `id`: Industry ID     - `value`: Industry name     - `label`: Industry label   - `is_promoted`: Whether promoted   - `trend`: Trend data list     - `time`: Timestamp     - `value`: Value at that time point   - `creators`: Creator list     - `nick_name`: Nickname     - `avatar_url`: Avatar URL   - `publish_cnt`: Publish count   - `video_views`: Video views   - `rank`: Ranking   - `rank_diff`: Rank difference   - `rank_diff_type`: Rank difference type - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"120\",     \"country_code\": \"US\",     \"sort_by\": \"popular\",     \"industry_id\": \"\",     \"filter_by\": \"\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"list\": [         {           \"hashtag_id\": \"4100\",           \"hashtag_name\": \"summer\",           \"country_info\": {             \"id\": \"US\",             \"value\": \"United States\",             \"label\": \"US\"           },           \"industry_info\": {             \"id\": 28000000000,             \"value\": \"Sports & Outdoor\",             \"label\": \"label_28000000000\"           },           \"is_promoted\": false,           \"trend\": [             {               \"time\": 1740787200,               \"value\": 0.38             },             {               \"time\": 1741392000,               \"value\": 0.37             }           ],           \"creators\": [             {               \"nick_name\": \"creator1\",               \"avatar_url\": \"https://example.com/avatar1.jpg\"             }           ],           \"publish_cnt\": 45678,           \"video_views\": 123456789,           \"rank\": 1,           \"rank_diff\": 2,           \"rank_diff_type\": 1         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 500,         \"has_more\": true       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hashtag_list_api_v1_tiktok_ads_get_hashtag_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object period: 时间范围（天）/Time period (days)
        :param object country_code: 国家代码/Country code
        :param object sort_by: 排序方式/Sort by (popular, new)
        :param object industry_id: 行业ID/Industry ID
        :param object filter_by: 筛选条件/Filter (new_on_board)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'period', 'country_code', 'sort_by', 'industry_id', 'filter_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hashtag_list_api_v1_tiktok_ads_get_hashtag_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'industry_id' in params:
            query_params.append(('industry_id', params['industry_id']))  # noqa: E501
        if 'filter_by' in params:
            query_params.append(('filter_by', params['filter_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_hashtag_list', 'GET',
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

    def get_keyword_details_api_v1_tiktok_ads_get_keyword_details_get(self, **kwargs):  # noqa: E501
        """获取关键词详细信息/Get keyword details  # noqa: E501

        # [中文] ### 用途: - 获取特定关键词的详细数据，包括发布量、示例视频等 - 不提供关键词时，返回热门关键词排名列表 - 深入分析关键词的使用情况和效果  ### 参数: - keyword: 关键词，可选。不提供时返回排名列表 - page: 页码，默认1 - limit: 每页数量，默认20 - period: 时间范围（天），如7、30天 - country_code: 国家代码，如US、UK、JP等 - order_by: 排序字段，如\"post\"（发布量） - order_type: 排序方式，desc（降序）或asc（升序）  ### 返回内容说明: - `keyword_list`: 关键词详情列表   - `comment`: 评论数   - `cost`: 花费金额   - `cpa`: 每次转化成本   - `ctr`: 点击率   - `cvr`: 转化率   - `impression`: 展示量   - `keyword`: 关键词文本   - `like`: 点赞数   - `play_six_rate`: 6秒播放率   - `post`: 发布量   - `post_change`: 发布量变化率   - `share`: 分享数   - `video_list`: 视频ID列表 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_details\",   \"params\": {     \"keyword\": \"\",     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"7\",     \"country_code\": \"US\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"keyword_list\": [         {           \"comment\": 4785,           \"cost\": 756000,           \"cpa\": 20.2,           \"ctr\": 0.53,           \"cvr\": 9.75,           \"impression\": 164000000,           \"keyword\": \"summer\",           \"like\": 475734,           \"play_six_rate\": 6.43,           \"post\": 14200,           \"post_change\": 111.21,           \"share\": 5754,           \"video_list\": [             \"7504060523021896977\",             \"7512164952346529031\"           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 484,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get detailed data for specific keywords, including post volume, example videos, etc. - When no keyword is provided, returns a ranked list of popular keywords - Deep analysis of keyword usage and effectiveness  ### Parameters: - keyword: Keyword, optional. Returns ranking list when not provided - page: Page number, default 1 - limit: Items per page, default 20 - period: Time period in days, e.g., 7, 30 days - country_code: Country code, e.g., US, UK, JP - order_by: Sort field, e.g., \"post\" (post volume) - order_type: Sort order, desc (descending) or asc (ascending)  ### Return Description: - `keyword_list`: Keyword details list   - `comment`: Comment count   - `cost`: Cost amount   - `cpa`: Cost per acquisition   - `ctr`: Click-through rate   - `cvr`: Conversion rate   - `impression`: Impression count   - `keyword`: Keyword text   - `like`: Like count   - `play_six_rate`: 6-second play rate   - `post`: Post volume   - `post_change`: Post volume change rate   - `share`: Share count   - `video_list`: Video ID list - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_details\",   \"params\": {     \"keyword\": \"\",     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"7\",     \"country_code\": \"US\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"keyword_list\": [         {           \"comment\": 4785,           \"cost\": 756000,           \"cpa\": 20.2,           \"ctr\": 0.53,           \"cvr\": 9.75,           \"impression\": 164000000,           \"keyword\": \"summer\",           \"like\": 475734,           \"play_six_rate\": 6.43,           \"post\": 14200,           \"post_change\": 111.21,           \"share\": 5754,           \"video_list\": [             \"7504060523021896977\",             \"7512164952346529031\"           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 484,         \"has_more\": true       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_keyword_details_api_v1_tiktok_ads_get_keyword_details_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词（可选）/Keyword (optional)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object period: 时间范围（天）/Time period (days)
        :param object country_code: 国家代码/Country code
        :param object order_by: 排序字段/Sort field
        :param object order_type: 排序方式/Sort order (desc, asc)
        :param object industry: 行业ID/Industry ID
        :param object objective: 广告目标/Ad objective
        :param object keyword_type: 关键词类型/Keyword type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_keyword_details_api_v1_tiktok_ads_get_keyword_details_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_keyword_details_api_v1_tiktok_ads_get_keyword_details_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_keyword_details_api_v1_tiktok_ads_get_keyword_details_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取关键词详细信息/Get keyword details  # noqa: E501

        # [中文] ### 用途: - 获取特定关键词的详细数据，包括发布量、示例视频等 - 不提供关键词时，返回热门关键词排名列表 - 深入分析关键词的使用情况和效果  ### 参数: - keyword: 关键词，可选。不提供时返回排名列表 - page: 页码，默认1 - limit: 每页数量，默认20 - period: 时间范围（天），如7、30天 - country_code: 国家代码，如US、UK、JP等 - order_by: 排序字段，如\"post\"（发布量） - order_type: 排序方式，desc（降序）或asc（升序）  ### 返回内容说明: - `keyword_list`: 关键词详情列表   - `comment`: 评论数   - `cost`: 花费金额   - `cpa`: 每次转化成本   - `ctr`: 点击率   - `cvr`: 转化率   - `impression`: 展示量   - `keyword`: 关键词文本   - `like`: 点赞数   - `play_six_rate`: 6秒播放率   - `post`: 发布量   - `post_change`: 发布量变化率   - `share`: 分享数   - `video_list`: 视频ID列表 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_details\",   \"params\": {     \"keyword\": \"\",     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"7\",     \"country_code\": \"US\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"keyword_list\": [         {           \"comment\": 4785,           \"cost\": 756000,           \"cpa\": 20.2,           \"ctr\": 0.53,           \"cvr\": 9.75,           \"impression\": 164000000,           \"keyword\": \"summer\",           \"like\": 475734,           \"play_six_rate\": 6.43,           \"post\": 14200,           \"post_change\": 111.21,           \"share\": 5754,           \"video_list\": [             \"7504060523021896977\",             \"7512164952346529031\"           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 484,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get detailed data for specific keywords, including post volume, example videos, etc. - When no keyword is provided, returns a ranked list of popular keywords - Deep analysis of keyword usage and effectiveness  ### Parameters: - keyword: Keyword, optional. Returns ranking list when not provided - page: Page number, default 1 - limit: Items per page, default 20 - period: Time period in days, e.g., 7, 30 days - country_code: Country code, e.g., US, UK, JP - order_by: Sort field, e.g., \"post\" (post volume) - order_type: Sort order, desc (descending) or asc (ascending)  ### Return Description: - `keyword_list`: Keyword details list   - `comment`: Comment count   - `cost`: Cost amount   - `cpa`: Cost per acquisition   - `ctr`: Click-through rate   - `cvr`: Conversion rate   - `impression`: Impression count   - `keyword`: Keyword text   - `like`: Like count   - `play_six_rate`: 6-second play rate   - `post`: Post volume   - `post_change`: Post volume change rate   - `share`: Share count   - `video_list`: Video ID list - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_details\",   \"params\": {     \"keyword\": \"\",     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"7\",     \"country_code\": \"US\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"keyword_list\": [         {           \"comment\": 4785,           \"cost\": 756000,           \"cpa\": 20.2,           \"ctr\": 0.53,           \"cvr\": 9.75,           \"impression\": 164000000,           \"keyword\": \"summer\",           \"like\": 475734,           \"play_six_rate\": 6.43,           \"post\": 14200,           \"post_change\": 111.21,           \"share\": 5754,           \"video_list\": [             \"7504060523021896977\",             \"7512164952346529031\"           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 484,         \"has_more\": true       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_keyword_details_api_v1_tiktok_ads_get_keyword_details_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词（可选）/Keyword (optional)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object period: 时间范围（天）/Time period (days)
        :param object country_code: 国家代码/Country code
        :param object order_by: 排序字段/Sort field
        :param object order_type: 排序方式/Sort order (desc, asc)
        :param object industry: 行业ID/Industry ID
        :param object objective: 广告目标/Ad objective
        :param object keyword_type: 关键词类型/Keyword type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page', 'limit', 'period', 'country_code', 'order_by', 'order_type', 'industry', 'objective', 'keyword_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_keyword_details_api_v1_tiktok_ads_get_keyword_details_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'order_type' in params:
            query_params.append(('order_type', params['order_type']))  # noqa: E501
        if 'industry' in params:
            query_params.append(('industry', params['industry']))  # noqa: E501
        if 'objective' in params:
            query_params.append(('objective', params['objective']))  # noqa: E501
        if 'keyword_type' in params:
            query_params.append(('keyword_type', params['keyword_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_keyword_details', 'GET',
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

    def get_keyword_filters_api_v1_tiktok_ads_get_keyword_filters_get(self, **kwargs):  # noqa: E501
        """获取关键词筛选器/Get keyword filters  # noqa: E501

        # [中文] ### 用途: - 获取关键词洞察功能的可用筛选选项 - 了解支持的国家/地区、行业、关键词类型等筛选维度 - 为关键词分析提供筛选参数参考  ### 返回内容说明: - `country_list`: 支持的国家/地区列表   - `id`: 国家代码   - `value`: 国家名称 - `industry_list`: 支持的行业列表   - `id`: 行业ID   - `value`: 行业名称 - `keyword_type`: 支持的关键词类型 - `objective_list`: 支持的广告目标列表  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",   \"params\": {},   \"data\": {     \"country_list\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"industry_list\": [       {\"id\": \"27000000000\", \"value\": \"Games\"},       {\"id\": \"19000000000\", \"value\": \"E-commerce\"}     ],     \"keyword_type\": [\"general\", \"brand\", \"product\"],     \"objective_list\": [       {\"id\": \"1\", \"value\": \"Traffic\"},       {\"id\": \"2\", \"value\": \"Conversions\"}     ]   } } ```  # [English] ### Purpose: - Get available filter options for keyword insights functionality - Understand supported countries/regions, industries, keyword types and other filter dimensions - Provide filter parameter reference for keyword analysis  ### Return Description: - `country_list`: List of supported countries/regions   - `id`: Country code   - `value`: Country name - `industry_list`: List of supported industries   - `id`: Industry ID   - `value`: Industry name - `keyword_type`: Supported keyword types - `objective_list`: List of supported ad objectives  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",   \"params\": {},   \"data\": {     \"country_list\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"industry_list\": [       {\"id\": \"27000000000\", \"value\": \"Games\"},       {\"id\": \"19000000000\", \"value\": \"E-commerce\"}     ],     \"keyword_type\": [\"general\", \"brand\", \"product\"],     \"objective_list\": [       {\"id\": \"1\", \"value\": \"Traffic\"},       {\"id\": \"2\", \"value\": \"Conversions\"}     ]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_keyword_filters_api_v1_tiktok_ads_get_keyword_filters_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_keyword_filters_api_v1_tiktok_ads_get_keyword_filters_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_keyword_filters_api_v1_tiktok_ads_get_keyword_filters_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_keyword_filters_api_v1_tiktok_ads_get_keyword_filters_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取关键词筛选器/Get keyword filters  # noqa: E501

        # [中文] ### 用途: - 获取关键词洞察功能的可用筛选选项 - 了解支持的国家/地区、行业、关键词类型等筛选维度 - 为关键词分析提供筛选参数参考  ### 返回内容说明: - `country_list`: 支持的国家/地区列表   - `id`: 国家代码   - `value`: 国家名称 - `industry_list`: 支持的行业列表   - `id`: 行业ID   - `value`: 行业名称 - `keyword_type`: 支持的关键词类型 - `objective_list`: 支持的广告目标列表  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",   \"params\": {},   \"data\": {     \"country_list\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"industry_list\": [       {\"id\": \"27000000000\", \"value\": \"Games\"},       {\"id\": \"19000000000\", \"value\": \"E-commerce\"}     ],     \"keyword_type\": [\"general\", \"brand\", \"product\"],     \"objective_list\": [       {\"id\": \"1\", \"value\": \"Traffic\"},       {\"id\": \"2\", \"value\": \"Conversions\"}     ]   } } ```  # [English] ### Purpose: - Get available filter options for keyword insights functionality - Understand supported countries/regions, industries, keyword types and other filter dimensions - Provide filter parameter reference for keyword analysis  ### Return Description: - `country_list`: List of supported countries/regions   - `id`: Country code   - `value`: Country name - `industry_list`: List of supported industries   - `id`: Industry ID   - `value`: Industry name - `keyword_type`: Supported keyword types - `objective_list`: List of supported ad objectives  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",   \"params\": {},   \"data\": {     \"country_list\": [       {\"id\": \"US\", \"value\": \"United States\"},       {\"id\": \"UK\", \"value\": \"United Kingdom\"}     ],     \"industry_list\": [       {\"id\": \"27000000000\", \"value\": \"Games\"},       {\"id\": \"19000000000\", \"value\": \"E-commerce\"}     ],     \"keyword_type\": [\"general\", \"brand\", \"product\"],     \"objective_list\": [       {\"id\": \"1\", \"value\": \"Traffic\"},       {\"id\": \"2\", \"value\": \"Conversions\"}     ]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_keyword_filters_api_v1_tiktok_ads_get_keyword_filters_get_with_http_info(async_req=True)
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
                    " to method get_keyword_filters_api_v1_tiktok_ads_get_keyword_filters_get" % key
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
            '/api/v1/tiktok/ads/get_keyword_filters', 'GET',
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

    def get_keyword_insights_api_v1_tiktok_ads_get_keyword_insights_get(self, **kwargs):  # noqa: E501
        """获取关键词洞察数据/Get keyword insights data  # noqa: E501

        # [中文] ### 用途: - 获取TikTok广告关键词洞察数据，了解热门关键词的表现指标 - 分析不同关键词的点击率、发布量、增长趋势等核心数据 - 帮助广告主优化关键词策略，提升广告投放效果  ### 参数: - page: 页码，默认1 - limit: 每页数量，默认20 - period: 时间范围（天），如7、30、120天 - country_code: 国家代码，如US、UK、JP等 - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、click_rate（点击率）、trend（趋势） - order_type: 排序方式，desc（降序）或asc（升序） - industry: 行业ID，多个用逗号分隔 - objective: 广告目标 - keyword_type: 关键词类型  ### 返回内容说明: - `keyword_list`: 关键词列表   - `comment`: 评论数   - `cost`: 花费金额   - `cpa`: 每次转化成本   - `ctr`: 点击率（百分比）   - `cvr`: 转化率（百分比）   - `impression`: 展示量   - `keyword`: 关键词文本   - `like`: 点赞数   - `play_six_rate`: 6秒播放率（百分比）   - `post`: 发布量   - `post_change`: 发布量变化率（百分比）   - `share`: 分享数   - `video_list`: 视频ID列表 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"7\",     \"country_code\": \"US\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"keyword_list\": [         {           \"comment\": 4785,           \"cost\": 756000,           \"cpa\": 20.2,           \"ctr\": 0.53,           \"cvr\": 9.75,           \"impression\": 164000000,           \"keyword\": \"summer\",           \"like\": 475734,           \"play_six_rate\": 6.43,           \"post\": 14200,           \"post_change\": 111.21,           \"share\": 5754,           \"video_list\": [             \"7504060523021896977\",             \"7512164952346529031\",             \"7511370341621435679\",             \"7511483560939785514\",             \"7506971390613015854\"           ]         },         {           \"comment\": 2151,           \"cost\": 264000,           \"cpa\": 17.8,           \"ctr\": 1.38,           \"cvr\": 6.15,           \"impression\": 38100000,           \"keyword\": \"free shipping\",           \"like\": 84131,           \"play_six_rate\": 8.64,           \"post\": 7810,           \"post_change\": 91.91,           \"share\": 3707,           \"video_list\": [             \"7471433861654727943\",             \"7515178617568070930\",             \"7502578466194312456\",             \"7513186274711244054\",             \"7514776490123201810\"           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 484,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get TikTok ad keyword insights data to understand performance metrics of popular keywords - Analyze CTR, post volume, growth trends and other core data for different keywords - Help advertisers optimize keyword strategies and improve ad delivery effectiveness  ### Parameters: - page: Page number, default 1 - limit: Items per page, default 20 - period: Time period in days, e.g., 7, 30, 120 days - country_code: Country code, e.g., US, UK, JP - order_by: Sort field, options: post (post volume), ctr (click-through rate), click_rate, trend - order_type: Sort order, desc (descending) or asc (ascending) - industry: Industry IDs, multiple separated by commas - objective: Ad objectives - keyword_type: Keyword type  ### Return Description: - `keyword_list`: List of keywords   - `comment`: Comment count   - `cost`: Cost amount   - `cpa`: Cost per acquisition   - `ctr`: Click-through rate (percentage)   - `cvr`: Conversion rate (percentage)   - `impression`: Impression count   - `keyword`: Keyword text   - `like`: Like count   - `play_six_rate`: 6-second play rate (percentage)   - `post`: Post volume   - `post_change`: Post volume change rate (percentage)   - `share`: Share count   - `video_list`: List of video IDs - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"7\",     \"country_code\": \"US\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"keyword_list\": [         {           \"comment\": 4785,           \"cost\": 756000,           \"cpa\": 20.2,           \"ctr\": 0.53,           \"cvr\": 9.75,           \"impression\": 164000000,           \"keyword\": \"summer\",           \"like\": 475734,           \"play_six_rate\": 6.43,           \"post\": 14200,           \"post_change\": 111.21,           \"share\": 5754,           \"video_list\": [             \"7504060523021896977\",             \"7512164952346529031\",             \"7511370341621435679\",             \"7511483560939785514\",             \"7506971390613015854\"           ]         },         {           \"comment\": 2151,           \"cost\": 264000,           \"cpa\": 17.8,           \"ctr\": 1.38,           \"cvr\": 6.15,           \"impression\": 38100000,           \"keyword\": \"free shipping\",           \"like\": 84131,           \"play_six_rate\": 8.64,           \"post\": 7810,           \"post_change\": 91.91,           \"share\": 3707,           \"video_list\": [             \"7471433861654727943\",             \"7515178617568070930\",             \"7502578466194312456\",             \"7513186274711244054\",             \"7514776490123201810\"           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 484,         \"has_more\": true       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_keyword_insights_api_v1_tiktok_ads_get_keyword_insights_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object period: 时间段（天）/Time period (days, 7/30/120/180)
        :param object country_code: 国家代码/Country code
        :param object order_by: 排序字段/Sort field (post, ctr, click_rate, etc.)
        :param object order_type: 排序方式/Sort order (desc, asc)
        :param object industry: 行业ID/Industry ID
        :param object objective: 广告目标/Ad objective
        :param object keyword_type: 关键词类型/Keyword type
        :param object keyword: 关键词/Keyword
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_keyword_insights_api_v1_tiktok_ads_get_keyword_insights_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_keyword_insights_api_v1_tiktok_ads_get_keyword_insights_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_keyword_insights_api_v1_tiktok_ads_get_keyword_insights_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取关键词洞察数据/Get keyword insights data  # noqa: E501

        # [中文] ### 用途: - 获取TikTok广告关键词洞察数据，了解热门关键词的表现指标 - 分析不同关键词的点击率、发布量、增长趋势等核心数据 - 帮助广告主优化关键词策略，提升广告投放效果  ### 参数: - page: 页码，默认1 - limit: 每页数量，默认20 - period: 时间范围（天），如7、30、120天 - country_code: 国家代码，如US、UK、JP等 - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、click_rate（点击率）、trend（趋势） - order_type: 排序方式，desc（降序）或asc（升序） - industry: 行业ID，多个用逗号分隔 - objective: 广告目标 - keyword_type: 关键词类型  ### 返回内容说明: - `keyword_list`: 关键词列表   - `comment`: 评论数   - `cost`: 花费金额   - `cpa`: 每次转化成本   - `ctr`: 点击率（百分比）   - `cvr`: 转化率（百分比）   - `impression`: 展示量   - `keyword`: 关键词文本   - `like`: 点赞数   - `play_six_rate`: 6秒播放率（百分比）   - `post`: 发布量   - `post_change`: 发布量变化率（百分比）   - `share`: 分享数   - `video_list`: 视频ID列表 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"7\",     \"country_code\": \"US\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"keyword_list\": [         {           \"comment\": 4785,           \"cost\": 756000,           \"cpa\": 20.2,           \"ctr\": 0.53,           \"cvr\": 9.75,           \"impression\": 164000000,           \"keyword\": \"summer\",           \"like\": 475734,           \"play_six_rate\": 6.43,           \"post\": 14200,           \"post_change\": 111.21,           \"share\": 5754,           \"video_list\": [             \"7504060523021896977\",             \"7512164952346529031\",             \"7511370341621435679\",             \"7511483560939785514\",             \"7506971390613015854\"           ]         },         {           \"comment\": 2151,           \"cost\": 264000,           \"cpa\": 17.8,           \"ctr\": 1.38,           \"cvr\": 6.15,           \"impression\": 38100000,           \"keyword\": \"free shipping\",           \"like\": 84131,           \"play_six_rate\": 8.64,           \"post\": 7810,           \"post_change\": 91.91,           \"share\": 3707,           \"video_list\": [             \"7471433861654727943\",             \"7515178617568070930\",             \"7502578466194312456\",             \"7513186274711244054\",             \"7514776490123201810\"           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 484,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get TikTok ad keyword insights data to understand performance metrics of popular keywords - Analyze CTR, post volume, growth trends and other core data for different keywords - Help advertisers optimize keyword strategies and improve ad delivery effectiveness  ### Parameters: - page: Page number, default 1 - limit: Items per page, default 20 - period: Time period in days, e.g., 7, 30, 120 days - country_code: Country code, e.g., US, UK, JP - order_by: Sort field, options: post (post volume), ctr (click-through rate), click_rate, trend - order_type: Sort order, desc (descending) or asc (ascending) - industry: Industry IDs, multiple separated by commas - objective: Ad objectives - keyword_type: Keyword type  ### Return Description: - `keyword_list`: List of keywords   - `comment`: Comment count   - `cost`: Cost amount   - `cpa`: Cost per acquisition   - `ctr`: Click-through rate (percentage)   - `cvr`: Conversion rate (percentage)   - `impression`: Impression count   - `keyword`: Keyword text   - `like`: Like count   - `play_six_rate`: 6-second play rate (percentage)   - `post`: Post volume   - `post_change`: Post volume change rate (percentage)   - `share`: Share count   - `video_list`: List of video IDs - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",   \"params\": {     \"page\": \"1\",     \"limit\": \"20\",     \"period\": \"7\",     \"country_code\": \"US\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"keyword_list\": [         {           \"comment\": 4785,           \"cost\": 756000,           \"cpa\": 20.2,           \"ctr\": 0.53,           \"cvr\": 9.75,           \"impression\": 164000000,           \"keyword\": \"summer\",           \"like\": 475734,           \"play_six_rate\": 6.43,           \"post\": 14200,           \"post_change\": 111.21,           \"share\": 5754,           \"video_list\": [             \"7504060523021896977\",             \"7512164952346529031\",             \"7511370341621435679\",             \"7511483560939785514\",             \"7506971390613015854\"           ]         },         {           \"comment\": 2151,           \"cost\": 264000,           \"cpa\": 17.8,           \"ctr\": 1.38,           \"cvr\": 6.15,           \"impression\": 38100000,           \"keyword\": \"free shipping\",           \"like\": 84131,           \"play_six_rate\": 8.64,           \"post\": 7810,           \"post_change\": 91.91,           \"share\": 3707,           \"video_list\": [             \"7471433861654727943\",             \"7515178617568070930\",             \"7502578466194312456\",             \"7513186274711244054\",             \"7514776490123201810\"           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 484,         \"has_more\": true       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_keyword_insights_api_v1_tiktok_ads_get_keyword_insights_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object period: 时间段（天）/Time period (days, 7/30/120/180)
        :param object country_code: 国家代码/Country code
        :param object order_by: 排序字段/Sort field (post, ctr, click_rate, etc.)
        :param object order_type: 排序方式/Sort order (desc, asc)
        :param object industry: 行业ID/Industry ID
        :param object objective: 广告目标/Ad objective
        :param object keyword_type: 关键词类型/Keyword type
        :param object keyword: 关键词/Keyword
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'period', 'country_code', 'order_by', 'order_type', 'industry', 'objective', 'keyword_type', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_keyword_insights_api_v1_tiktok_ads_get_keyword_insights_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'order_type' in params:
            query_params.append(('order_type', params['order_type']))  # noqa: E501
        if 'industry' in params:
            query_params.append(('industry', params['industry']))  # noqa: E501
        if 'objective' in params:
            query_params.append(('objective', params['objective']))  # noqa: E501
        if 'keyword_type' in params:
            query_params.append(('keyword_type', params['keyword_type']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_keyword_insights', 'GET',
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

    def get_keyword_list_api_v1_tiktok_ads_get_keyword_list_get(self, **kwargs):  # noqa: E501
        """获取关键词列表/Get keyword list  # noqa: E501

        # [中文] ### 用途: - 获取特定关键词的广告投放数据，了解关键词在TikTok广告中的使用情况 - 分析关键词的发布量趋势、相关视频等信息 - 帮助广告主发现有效的广告关键词  ### 参数: - keyword: 搜索关键词，必填参数 - period: 时间范围（天），如7、30、120天 - page: 页码，默认1 - limit: 每页数量，默认6 - country_code: 国家代码，如US、UK、JP等 - industry: 行业ID列表，多个ID用逗号分隔  ### 返回内容说明: - `keyword_info_list`: 关键词信息列表   - `keyword`: 关键词文本   - `post`: 使用该关键词的广告发布数量   - `video_list`: 使用该关键词的示例视频ID列表 - `pagination`: 分页信息  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",   \"params\": {     \"keyword\": \"cat toy\",     \"period\": 120,     \"page\": 1,     \"limit\": 6   },   \"data\": {     \"keyword_info_list\": [       {         \"keyword\": \"cat toy\",         \"post\": 12345,         \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]       }     ],     \"pagination\": {       \"page\": 1,       \"limit\": 6,       \"total\": 50,       \"has_more\": true     }   } } ```  # [English] ### Purpose: - Get ad placement data for specific keywords to understand keyword usage in TikTok ads - Analyze keyword post trends, related videos, and other information - Help advertisers discover effective ad keywords  ### Parameters: - keyword: Search keyword, required parameter - period: Time period in days, e.g., 7, 30, 120 days - page: Page number, default 1 - limit: Items per page, default 6 - country_code: Country code, e.g., US, UK, JP - industry: Industry ID list, multiple IDs separated by commas  ### Return Description: - `keyword_info_list`: Keyword information list   - `keyword`: Keyword text   - `post`: Number of ads using this keyword   - `video_list`: List of example video IDs using this keyword - `pagination`: Pagination info  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",   \"params\": {     \"keyword\": \"cat toy\",     \"period\": 120,     \"page\": 1,     \"limit\": 6   },   \"data\": {     \"keyword_info_list\": [       {         \"keyword\": \"cat toy\",         \"post\": 12345,         \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]       }     ],     \"pagination\": {       \"page\": 1,       \"limit\": 6,       \"total\": 50,       \"has_more\": true     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_keyword_list_api_v1_tiktok_ads_get_keyword_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword
        :param object period: 时间范围（天）/Time period (days)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object country_code: 国家代码/Country code
        :param object industry: 行业ID列表，逗号分隔/Industry IDs, comma separated
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_keyword_list_api_v1_tiktok_ads_get_keyword_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_keyword_list_api_v1_tiktok_ads_get_keyword_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_keyword_list_api_v1_tiktok_ads_get_keyword_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取关键词列表/Get keyword list  # noqa: E501

        # [中文] ### 用途: - 获取特定关键词的广告投放数据，了解关键词在TikTok广告中的使用情况 - 分析关键词的发布量趋势、相关视频等信息 - 帮助广告主发现有效的广告关键词  ### 参数: - keyword: 搜索关键词，必填参数 - period: 时间范围（天），如7、30、120天 - page: 页码，默认1 - limit: 每页数量，默认6 - country_code: 国家代码，如US、UK、JP等 - industry: 行业ID列表，多个ID用逗号分隔  ### 返回内容说明: - `keyword_info_list`: 关键词信息列表   - `keyword`: 关键词文本   - `post`: 使用该关键词的广告发布数量   - `video_list`: 使用该关键词的示例视频ID列表 - `pagination`: 分页信息  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",   \"params\": {     \"keyword\": \"cat toy\",     \"period\": 120,     \"page\": 1,     \"limit\": 6   },   \"data\": {     \"keyword_info_list\": [       {         \"keyword\": \"cat toy\",         \"post\": 12345,         \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]       }     ],     \"pagination\": {       \"page\": 1,       \"limit\": 6,       \"total\": 50,       \"has_more\": true     }   } } ```  # [English] ### Purpose: - Get ad placement data for specific keywords to understand keyword usage in TikTok ads - Analyze keyword post trends, related videos, and other information - Help advertisers discover effective ad keywords  ### Parameters: - keyword: Search keyword, required parameter - period: Time period in days, e.g., 7, 30, 120 days - page: Page number, default 1 - limit: Items per page, default 6 - country_code: Country code, e.g., US, UK, JP - industry: Industry ID list, multiple IDs separated by commas  ### Return Description: - `keyword_info_list`: Keyword information list   - `keyword`: Keyword text   - `post`: Number of ads using this keyword   - `video_list`: List of example video IDs using this keyword - `pagination`: Pagination info  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",   \"params\": {     \"keyword\": \"cat toy\",     \"period\": 120,     \"page\": 1,     \"limit\": 6   },   \"data\": {     \"keyword_info_list\": [       {         \"keyword\": \"cat toy\",         \"post\": 12345,         \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]       }     ],     \"pagination\": {       \"page\": 1,       \"limit\": 6,       \"total\": 50,       \"has_more\": true     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_keyword_list_api_v1_tiktok_ads_get_keyword_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword
        :param object period: 时间范围（天）/Time period (days)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object country_code: 国家代码/Country code
        :param object industry: 行业ID列表，逗号分隔/Industry IDs, comma separated
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'period', 'page', 'limit', 'country_code', 'industry']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_keyword_list_api_v1_tiktok_ads_get_keyword_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'industry' in params:
            query_params.append(('industry', params['industry']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_keyword_list', 'GET',
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

    def get_popular_trends_api_v1_tiktok_ads_get_popular_trends_get(self, **kwargs):  # noqa: E501
        """获取流行趋势视频/Get popular trend videos  # noqa: E501

        # [中文] ### 用途: - 获取指定时间段内的流行趋势视频 - 了解当前热门内容的特点和趋势 - 为广告创意提供灵感和参考  ### 参数: - period: 时间范围（天），如7、30天 - page: 页码，默认1 - limit: 每页数量，默认10 - order_by: 排序字段   - vv: 按观看量排序   - like: 按点赞数排序   - comment: 按评论数排序   - repost: 按转发数排序 - country_code: 国家代码  ### 返回内容说明: - `pagination`: 分页信息   - `has_more`: 是否有更多   - `limit`: 每页数量   - `page`: 当前页   - `total_count`: 总数量 - `videos`: 趋势视频列表   - `country_code`: 国家代码   - `cover`: 封面图URL   - `duration`: 时长（秒）   - `id`: 视频ID   - `item_id`: 视频项目ID   - `item_url`: 视频链接   - `region`: 地区   - `title`: 视频标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",   \"params\": {     \"period\": \"7\",     \"page\": \"1\",     \"limit\": \"10\",     \"order_by\": \"vv\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"pagination\": {         \"has_more\": true,         \"limit\": 10,         \"page\": 1,         \"total_count\": 500       },       \"videos\": [         {           \"country_code\": \"US\",           \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",           \"duration\": 15,           \"id\": \"7512918118663081262\",           \"item_id\": \"7512918118663081262\",           \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",           \"region\": \"United States\",           \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"         },         {           \"country_code\": \"US\",           \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",           \"duration\": 15,           \"id\": \"7514018454932835615\",           \"item_id\": \"7514018454932835615\",           \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",           \"region\": \"United States\",           \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"         }       ]     }   } } ```  # [English] ### Purpose: - Get popular trend videos for specified time period - Understand characteristics and trends of current hot content - Provide inspiration and reference for ad creativity  ### Parameters: - period: Time period in days, e.g., 7, 30 days - page: Page number, default 1 - limit: Items per page, default 10 - order_by: Sort field   - vv: Sort by view count   - like: Sort by like count   - comment: Sort by comment count   - repost: Sort by repost count - country_code: Country code  ### Return Description: - `pagination`: Pagination info   - `has_more`: Has more pages   - `limit`: Items per page   - `page`: Current page   - `total_count`: Total count - `videos`: Trend video list   - `country_code`: Country code   - `cover`: Cover image URL   - `duration`: Duration in seconds   - `id`: Video ID   - `item_id`: Video item ID   - `item_url`: Video link   - `region`: Region name   - `title`: Video title  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",   \"params\": {     \"period\": \"7\",     \"page\": \"1\",     \"limit\": \"10\",     \"order_by\": \"vv\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"pagination\": {         \"has_more\": true,         \"limit\": 10,         \"page\": 1,         \"total_count\": 500       },       \"videos\": [         {           \"country_code\": \"US\",           \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",           \"duration\": 15,           \"id\": \"7512918118663081262\",           \"item_id\": \"7512918118663081262\",           \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",           \"region\": \"United States\",           \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"         },         {           \"country_code\": \"US\",           \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",           \"duration\": 15,           \"id\": \"7514018454932835615\",           \"item_id\": \"7514018454932835615\",           \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",           \"region\": \"United States\",           \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_popular_trends_api_v1_tiktok_ads_get_popular_trends_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object period: 时间范围（天）/Time period (days)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object order_by: 排序字段/Order by (vv, like, comment, repost)
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_popular_trends_api_v1_tiktok_ads_get_popular_trends_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_popular_trends_api_v1_tiktok_ads_get_popular_trends_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_popular_trends_api_v1_tiktok_ads_get_popular_trends_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取流行趋势视频/Get popular trend videos  # noqa: E501

        # [中文] ### 用途: - 获取指定时间段内的流行趋势视频 - 了解当前热门内容的特点和趋势 - 为广告创意提供灵感和参考  ### 参数: - period: 时间范围（天），如7、30天 - page: 页码，默认1 - limit: 每页数量，默认10 - order_by: 排序字段   - vv: 按观看量排序   - like: 按点赞数排序   - comment: 按评论数排序   - repost: 按转发数排序 - country_code: 国家代码  ### 返回内容说明: - `pagination`: 分页信息   - `has_more`: 是否有更多   - `limit`: 每页数量   - `page`: 当前页   - `total_count`: 总数量 - `videos`: 趋势视频列表   - `country_code`: 国家代码   - `cover`: 封面图URL   - `duration`: 时长（秒）   - `id`: 视频ID   - `item_id`: 视频项目ID   - `item_url`: 视频链接   - `region`: 地区   - `title`: 视频标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",   \"params\": {     \"period\": \"7\",     \"page\": \"1\",     \"limit\": \"10\",     \"order_by\": \"vv\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"pagination\": {         \"has_more\": true,         \"limit\": 10,         \"page\": 1,         \"total_count\": 500       },       \"videos\": [         {           \"country_code\": \"US\",           \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",           \"duration\": 15,           \"id\": \"7512918118663081262\",           \"item_id\": \"7512918118663081262\",           \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",           \"region\": \"United States\",           \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"         },         {           \"country_code\": \"US\",           \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",           \"duration\": 15,           \"id\": \"7514018454932835615\",           \"item_id\": \"7514018454932835615\",           \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",           \"region\": \"United States\",           \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"         }       ]     }   } } ```  # [English] ### Purpose: - Get popular trend videos for specified time period - Understand characteristics and trends of current hot content - Provide inspiration and reference for ad creativity  ### Parameters: - period: Time period in days, e.g., 7, 30 days - page: Page number, default 1 - limit: Items per page, default 10 - order_by: Sort field   - vv: Sort by view count   - like: Sort by like count   - comment: Sort by comment count   - repost: Sort by repost count - country_code: Country code  ### Return Description: - `pagination`: Pagination info   - `has_more`: Has more pages   - `limit`: Items per page   - `page`: Current page   - `total_count`: Total count - `videos`: Trend video list   - `country_code`: Country code   - `cover`: Cover image URL   - `duration`: Duration in seconds   - `id`: Video ID   - `item_id`: Video item ID   - `item_url`: Video link   - `region`: Region name   - `title`: Video title  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",   \"params\": {     \"period\": \"7\",     \"page\": \"1\",     \"limit\": \"10\",     \"order_by\": \"vv\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"pagination\": {         \"has_more\": true,         \"limit\": 10,         \"page\": 1,         \"total_count\": 500       },       \"videos\": [         {           \"country_code\": \"US\",           \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",           \"duration\": 15,           \"id\": \"7512918118663081262\",           \"item_id\": \"7512918118663081262\",           \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",           \"region\": \"United States\",           \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"         },         {           \"country_code\": \"US\",           \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",           \"duration\": 15,           \"id\": \"7514018454932835615\",           \"item_id\": \"7514018454932835615\",           \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",           \"region\": \"United States\",           \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_popular_trends_api_v1_tiktok_ads_get_popular_trends_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object period: 时间范围（天）/Time period (days)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object order_by: 排序字段/Order by (vv, like, comment, repost)
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['period', 'page', 'limit', 'order_by', 'country_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_popular_trends_api_v1_tiktok_ads_get_popular_trends_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_popular_trends', 'GET',
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

    def get_product_detail_api_v1_tiktok_ads_get_product_detail_get(self, id, **kwargs):  # noqa: E501
        """获取产品详细信息/Get product detail  # noqa: E501

        # [中文] ### 用途: - 获取特定产品类目的完整详细信息 - 包括受众分析、热门标签、相关帖子等多维度数据 - 为产品营销策略提供全面的数据支持  ### 参数: - id: 产品类目ID，如香水：601583 - last: 最近天数，如7、30天 - ecom_type: 电商类型，默认\"l3\" - period_type: 时间类型，默认\"last\"  ### 返回内容说明: - `info`: 产品详细信息   - `audience_ages`: 受众年龄分布     - `age_level`: 年龄数值     - `score`: 占比分数   - `audience_interests`: 受众兴趣分布     - `interest_info`: 兴趣信息       - `id`: 兴趣ID       - `label`: 兴趣标签       - `value`: 兴趣名称     - `score`: 占比分数   - `cover_url`: 封面图URL（可能为null）   - `ecom_type`: 电商类型   - `first_ecom_category`: 一级电商类目     - `id`: 类目ID     - `label`: 类目标签     - `value`: 类目名称   - `hashtags`: 热门标签列表   - `posts`: 相关帖子列表   - `second_ecom_category`: 二级电商类目   - `third_ecom_category`: 三级电商类目   - `url_title`: URL标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_detail\",   \"params\": {     \"id\": \"601583\",     \"last\": \"30\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"info\": {         \"audience_ages\": [           {             \"age_level\": 35,             \"score\": 27           },           {             \"age_level\": 25,             \"score\": 22           },           {             \"age_level\": 18,             \"score\": 22           },           {             \"age_level\": 45,             \"score\": 18           },           {             \"age_level\": 55,             \"score\": 11           }         ],         \"audience_interests\": [           {             \"interest_info\": {               \"id\": \"13105000000\",               \"label\": \"label_13105000000\",               \"value\": \"Pawn Shops\"             },             \"score\": 135           },           {             \"interest_info\": {               \"id\": \"24104000000\",               \"label\": \"label_24104000000\",               \"value\": \"Electronics & Electrical\"             },             \"score\": 127           }         ],         \"cover_url\": null,         \"ecom_type\": \"l3\",         \"first_ecom_category\": {           \"id\": \"601450\",           \"label\": \"category_601450\",           \"value\": \"Beauty & Personal Care\"         },         \"hashtags\": [           \"vlog\",           \"perfumetiktok\",           \"perfume\",           \"fragrance\",           \"fragrancetiktok\"         ],         \"posts\": [           \"7436474042036522248\",           \"7486253493716536584\",           \"7503974461725740295\"         ],         \"url_title\": \"Perfume\"       }     }   } } ```  # [English] ### Purpose: - Get complete detailed information for specific product categories - Includes multi-dimensional data like audience analysis, popular hashtags, related posts - Provide comprehensive data support for product marketing strategies  ### Parameters: - id: Product category ID, e.g., Perfume: 601583 - last: Number of recent days, e.g., 7, 30 days - ecom_type: E-commerce type, default \"l3\" - period_type: Period type, default \"last\"  ### Return Description: - `info`: Product detailed information   - `audience_ages`: Audience age distribution     - `age_level`: Age value     - `score`: Score value   - `audience_interests`: Audience interest distribution     - `interest_info`: Interest information       - `id`: Interest ID       - `label`: Interest label       - `value`: Interest name     - `score`: Score value   - `cover_url`: Cover image URL (may be null)   - `ecom_type`: E-commerce type   - `first_ecom_category`: First-level e-commerce category     - `id`: Category ID     - `label`: Category label     - `value`: Category name   - `hashtags`: Popular hashtags list   - `posts`: Related posts list   - `second_ecom_category`: Second-level e-commerce category   - `third_ecom_category`: Third-level e-commerce category   - `url_title`: URL title  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_detail\",   \"params\": {     \"id\": \"601583\",     \"last\": \"30\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"info\": {         \"audience_ages\": [           {             \"age_level\": 35,             \"score\": 27           },           {             \"age_level\": 25,             \"score\": 22           },           {             \"age_level\": 18,             \"score\": 22           },           {             \"age_level\": 45,             \"score\": 18           },           {             \"age_level\": 55,             \"score\": 11           }         ],         \"audience_interests\": [           {             \"interest_info\": {               \"id\": \"13105000000\",               \"label\": \"label_13105000000\",               \"value\": \"Pawn Shops\"             },             \"score\": 135           },           {             \"interest_info\": {               \"id\": \"24104000000\",               \"label\": \"label_24104000000\",               \"value\": \"Electronics & Electrical\"             },             \"score\": 127           }         ],         \"cover_url\": null,         \"ecom_type\": \"l3\",         \"first_ecom_category\": {           \"id\": \"601450\",           \"label\": \"category_601450\",           \"value\": \"Beauty & Personal Care\"         },         \"hashtags\": [           \"vlog\",           \"perfumetiktok\",           \"perfume\",           \"fragrance\",           \"fragrancetiktok\"         ],         \"posts\": [           \"7436474042036522248\",           \"7486253493716536584\",           \"7503974461725740295\"         ],         \"url_title\": \"Perfume\"       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_detail_api_v1_tiktok_ads_get_product_detail_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 产品类目ID/Product category ID (required)
        :param object last: 最近天数/Last days
        :param object ecom_type: 电商类型/E-commerce type
        :param object period_type: 时间类型/Period type
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_product_detail_api_v1_tiktok_ads_get_product_detail_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_product_detail_api_v1_tiktok_ads_get_product_detail_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_product_detail_api_v1_tiktok_ads_get_product_detail_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """获取产品详细信息/Get product detail  # noqa: E501

        # [中文] ### 用途: - 获取特定产品类目的完整详细信息 - 包括受众分析、热门标签、相关帖子等多维度数据 - 为产品营销策略提供全面的数据支持  ### 参数: - id: 产品类目ID，如香水：601583 - last: 最近天数，如7、30天 - ecom_type: 电商类型，默认\"l3\" - period_type: 时间类型，默认\"last\"  ### 返回内容说明: - `info`: 产品详细信息   - `audience_ages`: 受众年龄分布     - `age_level`: 年龄数值     - `score`: 占比分数   - `audience_interests`: 受众兴趣分布     - `interest_info`: 兴趣信息       - `id`: 兴趣ID       - `label`: 兴趣标签       - `value`: 兴趣名称     - `score`: 占比分数   - `cover_url`: 封面图URL（可能为null）   - `ecom_type`: 电商类型   - `first_ecom_category`: 一级电商类目     - `id`: 类目ID     - `label`: 类目标签     - `value`: 类目名称   - `hashtags`: 热门标签列表   - `posts`: 相关帖子列表   - `second_ecom_category`: 二级电商类目   - `third_ecom_category`: 三级电商类目   - `url_title`: URL标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_detail\",   \"params\": {     \"id\": \"601583\",     \"last\": \"30\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"info\": {         \"audience_ages\": [           {             \"age_level\": 35,             \"score\": 27           },           {             \"age_level\": 25,             \"score\": 22           },           {             \"age_level\": 18,             \"score\": 22           },           {             \"age_level\": 45,             \"score\": 18           },           {             \"age_level\": 55,             \"score\": 11           }         ],         \"audience_interests\": [           {             \"interest_info\": {               \"id\": \"13105000000\",               \"label\": \"label_13105000000\",               \"value\": \"Pawn Shops\"             },             \"score\": 135           },           {             \"interest_info\": {               \"id\": \"24104000000\",               \"label\": \"label_24104000000\",               \"value\": \"Electronics & Electrical\"             },             \"score\": 127           }         ],         \"cover_url\": null,         \"ecom_type\": \"l3\",         \"first_ecom_category\": {           \"id\": \"601450\",           \"label\": \"category_601450\",           \"value\": \"Beauty & Personal Care\"         },         \"hashtags\": [           \"vlog\",           \"perfumetiktok\",           \"perfume\",           \"fragrance\",           \"fragrancetiktok\"         ],         \"posts\": [           \"7436474042036522248\",           \"7486253493716536584\",           \"7503974461725740295\"         ],         \"url_title\": \"Perfume\"       }     }   } } ```  # [English] ### Purpose: - Get complete detailed information for specific product categories - Includes multi-dimensional data like audience analysis, popular hashtags, related posts - Provide comprehensive data support for product marketing strategies  ### Parameters: - id: Product category ID, e.g., Perfume: 601583 - last: Number of recent days, e.g., 7, 30 days - ecom_type: E-commerce type, default \"l3\" - period_type: Period type, default \"last\"  ### Return Description: - `info`: Product detailed information   - `audience_ages`: Audience age distribution     - `age_level`: Age value     - `score`: Score value   - `audience_interests`: Audience interest distribution     - `interest_info`: Interest information       - `id`: Interest ID       - `label`: Interest label       - `value`: Interest name     - `score`: Score value   - `cover_url`: Cover image URL (may be null)   - `ecom_type`: E-commerce type   - `first_ecom_category`: First-level e-commerce category     - `id`: Category ID     - `label`: Category label     - `value`: Category name   - `hashtags`: Popular hashtags list   - `posts`: Related posts list   - `second_ecom_category`: Second-level e-commerce category   - `third_ecom_category`: Third-level e-commerce category   - `url_title`: URL title  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_detail\",   \"params\": {     \"id\": \"601583\",     \"last\": \"30\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"info\": {         \"audience_ages\": [           {             \"age_level\": 35,             \"score\": 27           },           {             \"age_level\": 25,             \"score\": 22           },           {             \"age_level\": 18,             \"score\": 22           },           {             \"age_level\": 45,             \"score\": 18           },           {             \"age_level\": 55,             \"score\": 11           }         ],         \"audience_interests\": [           {             \"interest_info\": {               \"id\": \"13105000000\",               \"label\": \"label_13105000000\",               \"value\": \"Pawn Shops\"             },             \"score\": 135           },           {             \"interest_info\": {               \"id\": \"24104000000\",               \"label\": \"label_24104000000\",               \"value\": \"Electronics & Electrical\"             },             \"score\": 127           }         ],         \"cover_url\": null,         \"ecom_type\": \"l3\",         \"first_ecom_category\": {           \"id\": \"601450\",           \"label\": \"category_601450\",           \"value\": \"Beauty & Personal Care\"         },         \"hashtags\": [           \"vlog\",           \"perfumetiktok\",           \"perfume\",           \"fragrance\",           \"fragrancetiktok\"         ],         \"posts\": [           \"7436474042036522248\",           \"7486253493716536584\",           \"7503974461725740295\"         ],         \"url_title\": \"Perfume\"       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_detail_api_v1_tiktok_ads_get_product_detail_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 产品类目ID/Product category ID (required)
        :param object last: 最近天数/Last days
        :param object ecom_type: 电商类型/E-commerce type
        :param object period_type: 时间类型/Period type
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'last', 'ecom_type', 'period_type', 'country_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_detail_api_v1_tiktok_ads_get_product_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_product_detail_api_v1_tiktok_ads_get_product_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'last' in params:
            query_params.append(('last', params['last']))  # noqa: E501
        if 'ecom_type' in params:
            query_params.append(('ecom_type', params['ecom_type']))  # noqa: E501
        if 'period_type' in params:
            query_params.append(('period_type', params['period_type']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_product_detail', 'GET',
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

    def get_product_filters_api_v1_tiktok_ads_get_product_filters_get(self, **kwargs):  # noqa: E501
        """获取产品筛选器/Get product filters  # noqa: E501

        # [中文] ### 用途: - 获取产品分析功能的可用筛选选项 - 了解支持的电商类目、时间类型等筛选维度 - 为产品数据分析提供筛选参数参考  ### 返回内容说明: - `country`: 国家列表   - `id`: 国家ID   - `value`: 国家名称   - `label`: 国家标签 - `ecom_category`: 电商类目列表   - `id`: 类目ID   - `value`: 类目名称   - `label`: 类目标签 - `latest_month`: 最新月份 - `latest_week`: 最新周  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_filters\",   \"params\": {},   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"country\": [         {           \"id\": \"AR\",           \"value\": \"Argentina\",           \"label\": \"AR\"         },         {           \"id\": \"AU\",           \"value\": \"Australia\",           \"label\": \"AU\"         }       ],       \"ecom_category\": [         {           \"id\": 605196,           \"value\": \"Automotive & Motorbike\",           \"label\": \"category_605196\"         },         {           \"id\": 602284,           \"value\": \"Baby & Maternity\",           \"label\": \"category_602284\"         }       ],       \"latest_month\": \"2025-05\",       \"latest_week\": \"2025-06-07\"     }   } } ```  # [English] ### Purpose: - Get available filter options for product analysis functionality - Understand supported e-commerce categories, time types and other filter dimensions - Provide filter parameter reference for product data analysis  ### Return Description: - `country`: Country list   - `id`: Country ID   - `value`: Country name   - `label`: Country label - `ecom_category`: E-commerce category list   - `id`: Category ID   - `value`: Category name   - `label`: Category label - `latest_month`: Latest month - `latest_week`: Latest week  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_filters\",   \"params\": {},   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"country\": [         {           \"id\": \"AR\",           \"value\": \"Argentina\",           \"label\": \"AR\"         },         {           \"id\": \"AU\",           \"value\": \"Australia\",           \"label\": \"AU\"         }       ],       \"ecom_category\": [         {           \"id\": 605196,           \"value\": \"Automotive & Motorbike\",           \"label\": \"category_605196\"         },         {           \"id\": 602284,           \"value\": \"Baby & Maternity\",           \"label\": \"category_602284\"         }       ],       \"latest_month\": \"2025-05\",       \"latest_week\": \"2025-06-07\"     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_filters_api_v1_tiktok_ads_get_product_filters_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_product_filters_api_v1_tiktok_ads_get_product_filters_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_product_filters_api_v1_tiktok_ads_get_product_filters_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_product_filters_api_v1_tiktok_ads_get_product_filters_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取产品筛选器/Get product filters  # noqa: E501

        # [中文] ### 用途: - 获取产品分析功能的可用筛选选项 - 了解支持的电商类目、时间类型等筛选维度 - 为产品数据分析提供筛选参数参考  ### 返回内容说明: - `country`: 国家列表   - `id`: 国家ID   - `value`: 国家名称   - `label`: 国家标签 - `ecom_category`: 电商类目列表   - `id`: 类目ID   - `value`: 类目名称   - `label`: 类目标签 - `latest_month`: 最新月份 - `latest_week`: 最新周  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_filters\",   \"params\": {},   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"country\": [         {           \"id\": \"AR\",           \"value\": \"Argentina\",           \"label\": \"AR\"         },         {           \"id\": \"AU\",           \"value\": \"Australia\",           \"label\": \"AU\"         }       ],       \"ecom_category\": [         {           \"id\": 605196,           \"value\": \"Automotive & Motorbike\",           \"label\": \"category_605196\"         },         {           \"id\": 602284,           \"value\": \"Baby & Maternity\",           \"label\": \"category_602284\"         }       ],       \"latest_month\": \"2025-05\",       \"latest_week\": \"2025-06-07\"     }   } } ```  # [English] ### Purpose: - Get available filter options for product analysis functionality - Understand supported e-commerce categories, time types and other filter dimensions - Provide filter parameter reference for product data analysis  ### Return Description: - `country`: Country list   - `id`: Country ID   - `value`: Country name   - `label`: Country label - `ecom_category`: E-commerce category list   - `id`: Category ID   - `value`: Category name   - `label`: Category label - `latest_month`: Latest month - `latest_week`: Latest week  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_filters\",   \"params\": {},   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"country\": [         {           \"id\": \"AR\",           \"value\": \"Argentina\",           \"label\": \"AR\"         },         {           \"id\": \"AU\",           \"value\": \"Australia\",           \"label\": \"AU\"         }       ],       \"ecom_category\": [         {           \"id\": 605196,           \"value\": \"Automotive & Motorbike\",           \"label\": \"category_605196\"         },         {           \"id\": 602284,           \"value\": \"Baby & Maternity\",           \"label\": \"category_602284\"         }       ],       \"latest_month\": \"2025-05\",       \"latest_week\": \"2025-06-07\"     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_filters_api_v1_tiktok_ads_get_product_filters_get_with_http_info(async_req=True)
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
                    " to method get_product_filters_api_v1_tiktok_ads_get_product_filters_get" % key
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
            '/api/v1/tiktok/ads/get_product_filters', 'GET',
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

    def get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get(self, id, **kwargs):  # noqa: E501
        """获取产品指标数据/Get product metrics  # noqa: E501

        # [中文] ### 用途: - 获取特定产品类目的详细指标数据和时间趋势 - 分析产品的发布量、点击率、转化率等核心指标变化 - 帮助了解产品类目的市场表现和发展趋势  ### 参数: - id: 产品类目ID，如香水：601583 - last: 最近天数，如7、30天 - metrics: 指标类型，多个用逗号分隔，如\"post,ctr,cvr\" - ecom_type: 电商类型，默认\"l3\" - period_type: 时间类型，默认\"last\"  ### 返回内容说明: - `info`: 产品指标信息   - `comment`: 评论数   - `cost`: 花费金额   - `cover_url`: 封面图URL（可能为null）   - `cpa`: 每次转化成本   - `ctr`: 点击率   - `ctr_metrics`: 点击率时间序列数据     - `time`: 时间戳     - `value`: 对应时间的点击率   - `cvr`: 转化率   - `ecom_type`: 电商类型   - `first_ecom_category`: 一级电商类目   - `impression`: 展示量   - `like`: 点赞数   - `play_six_rate`: 6秒播放率   - `post`: 发布量   - `post_change`: 发布量变化率   - `post_metrics`: 发布量时间序列数据     - `time`: 时间戳     - `value`: 对应时间的发布量   - `second_ecom_category`: 二级电商类目   - `share`: 分享数   - `third_ecom_category`: 三级电商类目   - `url_title`: URL标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",   \"params\": {     \"id\": \"601583\",     \"last\": \"30\",     \"metrics\": \"post,ctr\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"info\": {         \"comment\": 13559,         \"cost\": 2330000,         \"cover_url\": null,         \"cpa\": 12.4,         \"ctr\": 1.04,         \"ctr_metrics\": [           {             \"time\": 1747267200,             \"value\": 0.88           },           {             \"time\": 1747353600,             \"value\": 0.99           }         ],         \"cvr\": 15.2,         \"ecom_type\": \"l3\",         \"post\": 52300,         \"post_change\": -8.12,         \"post_metrics\": [           {             \"time\": 1747267200,             \"value\": 1800           }         ]       }     }   } } ```  # [English] ### Purpose: - Get detailed metric data and time trends for specific product categories - Analyze changes in core metrics like post volume, CTR, CVR for products - Help understand market performance and development trends of product categories  ### Parameters: - id: Product category ID, e.g., Perfume: 601583 - last: Number of recent days, e.g., 7, 30 days - metrics: Metric types, multiple separated by commas, e.g., \"post,ctr,cvr\" - ecom_type: E-commerce type, default \"l3\" - period_type: Period type, default \"last\"  ### Return Description: - `info`: Product metric information   - `comment`: Comment count   - `cost`: Cost amount   - `cover_url`: Cover image URL (may be null)   - `cpa`: Cost per acquisition   - `ctr`: Click-through rate   - `ctr_metrics`: CTR time series data     - `time`: Timestamp     - `value`: CTR at that time   - `cvr`: Conversion rate   - `ecom_type`: E-commerce type   - `first_ecom_category`: First-level e-commerce category   - `impression`: Impression count   - `like`: Like count   - `play_six_rate`: 6-second play rate   - `post`: Post volume   - `post_change`: Post volume change rate   - `post_metrics`: Post volume time series data     - `time`: Timestamp     - `value`: Post volume at that time   - `second_ecom_category`: Second-level e-commerce category   - `share`: Share count   - `third_ecom_category`: Third-level e-commerce category   - `url_title`: URL title  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",   \"params\": {     \"id\": \"601583\",     \"last\": \"30\",     \"metrics\": \"post,ctr\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"info\": {         \"comment\": 13559,         \"cost\": 2330000,         \"cover_url\": null,         \"cpa\": 12.4,         \"ctr\": 1.04,         \"ctr_metrics\": [           {             \"time\": 1747267200,             \"value\": 0.88           },           {             \"time\": 1747353600,             \"value\": 0.99           }         ],         \"cvr\": 15.2,         \"ecom_type\": \"l3\",         \"post\": 52300,         \"post_change\": -8.12,         \"post_metrics\": [           {             \"time\": 1747267200,             \"value\": 1800           }         ]       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 产品类目ID/Product category ID (required)
        :param object last: 最近天数/Last days
        :param object metrics: 指标类型，逗号分隔/Metrics types, comma separated
        :param object ecom_type: 电商类型/E-commerce type
        :param object period_type: 时间类型/Period type
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """获取产品指标数据/Get product metrics  # noqa: E501

        # [中文] ### 用途: - 获取特定产品类目的详细指标数据和时间趋势 - 分析产品的发布量、点击率、转化率等核心指标变化 - 帮助了解产品类目的市场表现和发展趋势  ### 参数: - id: 产品类目ID，如香水：601583 - last: 最近天数，如7、30天 - metrics: 指标类型，多个用逗号分隔，如\"post,ctr,cvr\" - ecom_type: 电商类型，默认\"l3\" - period_type: 时间类型，默认\"last\"  ### 返回内容说明: - `info`: 产品指标信息   - `comment`: 评论数   - `cost`: 花费金额   - `cover_url`: 封面图URL（可能为null）   - `cpa`: 每次转化成本   - `ctr`: 点击率   - `ctr_metrics`: 点击率时间序列数据     - `time`: 时间戳     - `value`: 对应时间的点击率   - `cvr`: 转化率   - `ecom_type`: 电商类型   - `first_ecom_category`: 一级电商类目   - `impression`: 展示量   - `like`: 点赞数   - `play_six_rate`: 6秒播放率   - `post`: 发布量   - `post_change`: 发布量变化率   - `post_metrics`: 发布量时间序列数据     - `time`: 时间戳     - `value`: 对应时间的发布量   - `second_ecom_category`: 二级电商类目   - `share`: 分享数   - `third_ecom_category`: 三级电商类目   - `url_title`: URL标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",   \"params\": {     \"id\": \"601583\",     \"last\": \"30\",     \"metrics\": \"post,ctr\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"info\": {         \"comment\": 13559,         \"cost\": 2330000,         \"cover_url\": null,         \"cpa\": 12.4,         \"ctr\": 1.04,         \"ctr_metrics\": [           {             \"time\": 1747267200,             \"value\": 0.88           },           {             \"time\": 1747353600,             \"value\": 0.99           }         ],         \"cvr\": 15.2,         \"ecom_type\": \"l3\",         \"post\": 52300,         \"post_change\": -8.12,         \"post_metrics\": [           {             \"time\": 1747267200,             \"value\": 1800           }         ]       }     }   } } ```  # [English] ### Purpose: - Get detailed metric data and time trends for specific product categories - Analyze changes in core metrics like post volume, CTR, CVR for products - Help understand market performance and development trends of product categories  ### Parameters: - id: Product category ID, e.g., Perfume: 601583 - last: Number of recent days, e.g., 7, 30 days - metrics: Metric types, multiple separated by commas, e.g., \"post,ctr,cvr\" - ecom_type: E-commerce type, default \"l3\" - period_type: Period type, default \"last\"  ### Return Description: - `info`: Product metric information   - `comment`: Comment count   - `cost`: Cost amount   - `cover_url`: Cover image URL (may be null)   - `cpa`: Cost per acquisition   - `ctr`: Click-through rate   - `ctr_metrics`: CTR time series data     - `time`: Timestamp     - `value`: CTR at that time   - `cvr`: Conversion rate   - `ecom_type`: E-commerce type   - `first_ecom_category`: First-level e-commerce category   - `impression`: Impression count   - `like`: Like count   - `play_six_rate`: 6-second play rate   - `post`: Post volume   - `post_change`: Post volume change rate   - `post_metrics`: Post volume time series data     - `time`: Timestamp     - `value`: Post volume at that time   - `second_ecom_category`: Second-level e-commerce category   - `share`: Share count   - `third_ecom_category`: Third-level e-commerce category   - `url_title`: URL title  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",   \"params\": {     \"id\": \"601583\",     \"last\": \"30\",     \"metrics\": \"post,ctr\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"info\": {         \"comment\": 13559,         \"cost\": 2330000,         \"cover_url\": null,         \"cpa\": 12.4,         \"ctr\": 1.04,         \"ctr_metrics\": [           {             \"time\": 1747267200,             \"value\": 0.88           },           {             \"time\": 1747353600,             \"value\": 0.99           }         ],         \"cvr\": 15.2,         \"ecom_type\": \"l3\",         \"post\": 52300,         \"post_change\": -8.12,         \"post_metrics\": [           {             \"time\": 1747267200,             \"value\": 1800           }         ]       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 产品类目ID/Product category ID (required)
        :param object last: 最近天数/Last days
        :param object metrics: 指标类型，逗号分隔/Metrics types, comma separated
        :param object ecom_type: 电商类型/E-commerce type
        :param object period_type: 时间类型/Period type
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'last', 'metrics', 'ecom_type', 'period_type', 'country_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'last' in params:
            query_params.append(('last', params['last']))  # noqa: E501
        if 'metrics' in params:
            query_params.append(('metrics', params['metrics']))  # noqa: E501
        if 'ecom_type' in params:
            query_params.append(('ecom_type', params['ecom_type']))  # noqa: E501
        if 'period_type' in params:
            query_params.append(('period_type', params['period_type']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_product_metrics', 'GET',
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

    def get_query_suggestions_api_v1_tiktok_ads_get_query_suggestions_get(self, **kwargs):  # noqa: E501
        """获取查询建议/Get query suggestions  # noqa: E501

        # [中文] ### 用途: - 获取广告搜索的热门查询建议 - 了解当前流行的广告搜索关键词和趋势 - 帮助发现新的广告创意方向和热点话题  ### 参数: - count: 返回的建议数量，默认50 - scenario: 场景类型，默认1  ### 返回内容说明: - `query`: 查询建议列表（字符串数组）  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",   \"params\": {     \"count\": \"50\",     \"scenario\": \"1\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"query\": [         \"shop now\",         \"50% off\"       ]     }   } } ```  # [English] ### Purpose: - Get popular query suggestions for ad search - Understand current popular ad search keywords and trends - Help discover new creative directions and hot topics  ### Parameters: - count: Number of suggestions to return, default 50 - scenario: Scenario type, default 1  ### Return Description: - `query`: Query suggestions list (string array)  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",   \"params\": {     \"count\": \"50\",     \"scenario\": \"1\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"query\": [         \"shop now\",         \"50% off\"       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_query_suggestions_api_v1_tiktok_ads_get_query_suggestions_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 建议数量/Suggestion count
        :param object scenario: 场景类型/Scenario type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_query_suggestions_api_v1_tiktok_ads_get_query_suggestions_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_query_suggestions_api_v1_tiktok_ads_get_query_suggestions_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_query_suggestions_api_v1_tiktok_ads_get_query_suggestions_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取查询建议/Get query suggestions  # noqa: E501

        # [中文] ### 用途: - 获取广告搜索的热门查询建议 - 了解当前流行的广告搜索关键词和趋势 - 帮助发现新的广告创意方向和热点话题  ### 参数: - count: 返回的建议数量，默认50 - scenario: 场景类型，默认1  ### 返回内容说明: - `query`: 查询建议列表（字符串数组）  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",   \"params\": {     \"count\": \"50\",     \"scenario\": \"1\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"query\": [         \"shop now\",         \"50% off\"       ]     }   } } ```  # [English] ### Purpose: - Get popular query suggestions for ad search - Understand current popular ad search keywords and trends - Help discover new creative directions and hot topics  ### Parameters: - count: Number of suggestions to return, default 50 - scenario: Scenario type, default 1  ### Return Description: - `query`: Query suggestions list (string array)  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",   \"params\": {     \"count\": \"50\",     \"scenario\": \"1\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"query\": [         \"shop now\",         \"50% off\"       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_query_suggestions_api_v1_tiktok_ads_get_query_suggestions_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object count: 建议数量/Suggestion count
        :param object scenario: 场景类型/Scenario type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'scenario']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_query_suggestions_api_v1_tiktok_ads_get_query_suggestions_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'scenario' in params:
            query_params.append(('scenario', params['scenario']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_query_suggestions', 'GET',
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

    def get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get(self, material_id, **kwargs):  # noqa: E501
        """获取推荐广告/Get recommended ads  # noqa: E501

        # [中文] ### 用途: - 基于指定广告获取相似的推荐广告列表 - 发现同行业或相似风格的优秀广告案例 - 为广告创意提供更多参考和灵感  ### 参数: - material_id: 参考广告素材ID，必填参数 - industry: 行业ID，如游戏行业：25308000000 - country_code: 国家代码，如US、UK、JP等  ### 返回内容说明: - `materials`: 推荐广告素材列表   - `ad_title`: 广告标题   - `brand_name`: 品牌名称   - `cost`: 花费等级   - `ctr`: 点击率   - `favorite`: 是否收藏   - `id`: 广告ID   - `industry_key`: 行业键值   - `is_search`: 是否搜索结果   - `like`: 点赞数   - `objective_key`: 广告目标键值   - `tag`: 标签   - `video_info`: 视频信息     - `vid`: 视频ID     - `duration`: 时长（秒）     - `cover`: 封面图URL     - `video_url`: 视频播放地址       - `360p`: 360p画质       - `480p`: 480p画质       - `540p`: 540p画质       - `720p`: 720p画质     - `width`: 视频宽度     - `height`: 视频高度  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",   \"params\": {     \"material_id\": \"7213258221116751874\",     \"industry\": \"25308000000\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"materials\": [         {           \"ad_title\": \"What will you decide?\",           \"brand_name\": \"Eatventure\",           \"cost\": 2,           \"ctr\": 0.07,           \"favorite\": false,           \"id\": \"7164756134804979714\",           \"industry_key\": \"label_25308000000\",           \"is_search\": false,           \"like\": 1009024,           \"objective_key\": \"campaign_objective_conversion\",           \"tag\": 3,           \"video_info\": {             \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",             \"duration\": 30.016,             \"cover\": \"https://p16-sign-sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",             \"video_url\": {               \"360p\": \"https://v16m-default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",               \"480p\": \"https://v16m-default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",               \"540p\": \"https://v16m-default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",               \"720p\": \"https://v16m-default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"             },             \"width\": 720,             \"height\": 1280           }         }       ]     }   } } ```  # [English] ### Purpose: - Get similar recommended ads based on a specified ad - Discover excellent ad cases in the same industry or with similar styles - Provide more references and inspiration for ad creativity  ### Parameters: - material_id: Reference ad material ID, required parameter - industry: Industry ID, e.g., Games: 25308000000 - country_code: Country code, e.g., US, UK, JP  ### Return Description: - `materials`: Recommended ad materials list   - `ad_title`: Ad title   - `brand_name`: Brand name   - `cost`: Cost level   - `ctr`: Click-through rate   - `favorite`: Whether favorited   - `id`: Ad ID   - `industry_key`: Industry key   - `is_search`: Whether search result   - `like`: Like count   - `objective_key`: Ad objective key   - `tag`: Tag   - `video_info`: Video information     - `vid`: Video ID     - `duration`: Duration in seconds     - `cover`: Cover image URL     - `video_url`: Video playback URLs       - `360p`: 360p quality       - `480p`: 480p quality       - `540p`: 540p quality       - `720p`: 720p quality     - `width`: Video width     - `height`: Video height  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",   \"params\": {     \"material_id\": \"7213258221116751874\",     \"industry\": \"25308000000\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"materials\": [         {           \"ad_title\": \"What will you decide?\",           \"brand_name\": \"Eatventure\",           \"cost\": 2,           \"ctr\": 0.07,           \"favorite\": false,           \"id\": \"7164756134804979714\",           \"industry_key\": \"label_25308000000\",           \"is_search\": false,           \"like\": 1009024,           \"objective_key\": \"campaign_objective_conversion\",           \"tag\": 3,           \"video_info\": {             \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",             \"duration\": 30.016,             \"cover\": \"https://p16-sign-sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",             \"video_url\": {               \"360p\": \"https://v16m-default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",               \"480p\": \"https://v16m-default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",               \"540p\": \"https://v16m-default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",               \"720p\": \"https://v16m-default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"             },             \"width\": 720,             \"height\": 1280           }         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get(material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object material_id: 广告素材ID/Ad material ID (required)
        :param object industry: 行业ID/Industry ID
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get_with_http_info(material_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get_with_http_info(material_id, **kwargs)  # noqa: E501
            return data

    def get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get_with_http_info(self, material_id, **kwargs):  # noqa: E501
        """获取推荐广告/Get recommended ads  # noqa: E501

        # [中文] ### 用途: - 基于指定广告获取相似的推荐广告列表 - 发现同行业或相似风格的优秀广告案例 - 为广告创意提供更多参考和灵感  ### 参数: - material_id: 参考广告素材ID，必填参数 - industry: 行业ID，如游戏行业：25308000000 - country_code: 国家代码，如US、UK、JP等  ### 返回内容说明: - `materials`: 推荐广告素材列表   - `ad_title`: 广告标题   - `brand_name`: 品牌名称   - `cost`: 花费等级   - `ctr`: 点击率   - `favorite`: 是否收藏   - `id`: 广告ID   - `industry_key`: 行业键值   - `is_search`: 是否搜索结果   - `like`: 点赞数   - `objective_key`: 广告目标键值   - `tag`: 标签   - `video_info`: 视频信息     - `vid`: 视频ID     - `duration`: 时长（秒）     - `cover`: 封面图URL     - `video_url`: 视频播放地址       - `360p`: 360p画质       - `480p`: 480p画质       - `540p`: 540p画质       - `720p`: 720p画质     - `width`: 视频宽度     - `height`: 视频高度  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",   \"params\": {     \"material_id\": \"7213258221116751874\",     \"industry\": \"25308000000\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"materials\": [         {           \"ad_title\": \"What will you decide?\",           \"brand_name\": \"Eatventure\",           \"cost\": 2,           \"ctr\": 0.07,           \"favorite\": false,           \"id\": \"7164756134804979714\",           \"industry_key\": \"label_25308000000\",           \"is_search\": false,           \"like\": 1009024,           \"objective_key\": \"campaign_objective_conversion\",           \"tag\": 3,           \"video_info\": {             \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",             \"duration\": 30.016,             \"cover\": \"https://p16-sign-sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",             \"video_url\": {               \"360p\": \"https://v16m-default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",               \"480p\": \"https://v16m-default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",               \"540p\": \"https://v16m-default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",               \"720p\": \"https://v16m-default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"             },             \"width\": 720,             \"height\": 1280           }         }       ]     }   } } ```  # [English] ### Purpose: - Get similar recommended ads based on a specified ad - Discover excellent ad cases in the same industry or with similar styles - Provide more references and inspiration for ad creativity  ### Parameters: - material_id: Reference ad material ID, required parameter - industry: Industry ID, e.g., Games: 25308000000 - country_code: Country code, e.g., US, UK, JP  ### Return Description: - `materials`: Recommended ad materials list   - `ad_title`: Ad title   - `brand_name`: Brand name   - `cost`: Cost level   - `ctr`: Click-through rate   - `favorite`: Whether favorited   - `id`: Ad ID   - `industry_key`: Industry key   - `is_search`: Whether search result   - `like`: Like count   - `objective_key`: Ad objective key   - `tag`: Tag   - `video_info`: Video information     - `vid`: Video ID     - `duration`: Duration in seconds     - `cover`: Cover image URL     - `video_url`: Video playback URLs       - `360p`: 360p quality       - `480p`: 480p quality       - `540p`: 540p quality       - `720p`: 720p quality     - `width`: Video width     - `height`: Video height  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",   \"params\": {     \"material_id\": \"7213258221116751874\",     \"industry\": \"25308000000\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"materials\": [         {           \"ad_title\": \"What will you decide?\",           \"brand_name\": \"Eatventure\",           \"cost\": 2,           \"ctr\": 0.07,           \"favorite\": false,           \"id\": \"7164756134804979714\",           \"industry_key\": \"label_25308000000\",           \"is_search\": false,           \"like\": 1009024,           \"objective_key\": \"campaign_objective_conversion\",           \"tag\": 3,           \"video_info\": {             \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",             \"duration\": 30.016,             \"cover\": \"https://p16-sign-sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",             \"video_url\": {               \"360p\": \"https://v16m-default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",               \"480p\": \"https://v16m-default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",               \"540p\": \"https://v16m-default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",               \"720p\": \"https://v16m-default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"             },             \"width\": 720,             \"height\": 1280           }         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get_with_http_info(material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object material_id: 广告素材ID/Ad material ID (required)
        :param object industry: 行业ID/Industry ID
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['material_id', 'industry', 'country_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'material_id' is set
        if self.api_client.client_side_validation and ('material_id' not in params or
                                                       params['material_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `material_id` when calling `get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'material_id' in params:
            query_params.append(('material_id', params['material_id']))  # noqa: E501
        if 'industry' in params:
            query_params.append(('industry', params['industry']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_recommended_ads', 'GET',
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

    def get_related_keywords_api_v1_tiktok_ads_get_related_keywords_get(self, **kwargs):  # noqa: E501
        """获取相关关键词/Get related keywords  # noqa: E501

        # [中文] ### 用途: - 获取与指定关键词相关的其他关键词或标签 - 发现关键词的相关搜索词，扩展广告投放词库 - 分析突破性关键词，抓住新兴趋势  ### 参数: - keyword: 主关键词，必填参数 - period: 时间范围（天），如7、30天 - country_code: 国家代码，如US、UK、JP等 - rank_type: 排序类型，\"popular\"=热门，\"breakout\"=突破性 - content_type: 内容类型，\"keyword\"=关键词，\"hashtag\"=标签  ### 返回内容说明: - `list`: 相关关键词列表   - `keyword`: 相关关键词文本   - `relevance_score`: 相关性评分   - `search_volume`: 搜索量级别   - `growth_rate`: 增长率（突破性关键词）   - `post_count`: 使用该词的广告数量  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",   \"params\": {     \"keyword\": \"free shipping\",     \"period\": 7,     \"rank_type\": \"popular\"   },   \"data\": {     \"list\": [       {         \"keyword\": \"fast delivery\",         \"relevance_score\": 95,         \"search_volume\": \"high\",         \"post_count\": 8934       },       {         \"keyword\": \"discount code\",         \"relevance_score\": 88,         \"search_volume\": \"medium\",         \"post_count\": 5621       }     ]   } } ```  # [English] ### Purpose: - Get other keywords or hashtags related to a specified keyword - Discover related search terms to expand ad keyword library - Analyze breakout keywords to capture emerging trends  ### Parameters: - keyword: Main keyword, required parameter - period: Time period in days, e.g., 7, 30 days - country_code: Country code, e.g., US, UK, JP - rank_type: Ranking type, \"popular\"=Popular, \"breakout\"=Breakout - content_type: Content type, \"keyword\"=Keywords, \"hashtag\"=Hashtags  ### Return Description: - `list`: Related keywords list   - `keyword`: Related keyword text   - `relevance_score`: Relevance score   - `search_volume`: Search volume level   - `growth_rate`: Growth rate (for breakout keywords)   - `post_count`: Number of ads using this term  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",   \"params\": {     \"keyword\": \"free shipping\",     \"period\": 7,     \"rank_type\": \"popular\"   },   \"data\": {     \"list\": [       {         \"keyword\": \"fast delivery\",         \"relevance_score\": 95,         \"search_volume\": \"high\",         \"post_count\": 8934       },       {         \"keyword\": \"discount code\",         \"relevance_score\": 88,         \"search_volume\": \"medium\",         \"post_count\": 5621       }     ]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_related_keywords_api_v1_tiktok_ads_get_related_keywords_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 目标关键词/Target keyword
        :param object period: 时间段（天）/Time period (days, 7/30/120)
        :param object country_code: 国家/地区代码/Country code
        :param object rank_type: 排名类型/Rank type (popular: 热门, breakout: 突破性)
        :param object content_type: 内容类型/Content type (keyword, hashtag)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_related_keywords_api_v1_tiktok_ads_get_related_keywords_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_related_keywords_api_v1_tiktok_ads_get_related_keywords_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_related_keywords_api_v1_tiktok_ads_get_related_keywords_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取相关关键词/Get related keywords  # noqa: E501

        # [中文] ### 用途: - 获取与指定关键词相关的其他关键词或标签 - 发现关键词的相关搜索词，扩展广告投放词库 - 分析突破性关键词，抓住新兴趋势  ### 参数: - keyword: 主关键词，必填参数 - period: 时间范围（天），如7、30天 - country_code: 国家代码，如US、UK、JP等 - rank_type: 排序类型，\"popular\"=热门，\"breakout\"=突破性 - content_type: 内容类型，\"keyword\"=关键词，\"hashtag\"=标签  ### 返回内容说明: - `list`: 相关关键词列表   - `keyword`: 相关关键词文本   - `relevance_score`: 相关性评分   - `search_volume`: 搜索量级别   - `growth_rate`: 增长率（突破性关键词）   - `post_count`: 使用该词的广告数量  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",   \"params\": {     \"keyword\": \"free shipping\",     \"period\": 7,     \"rank_type\": \"popular\"   },   \"data\": {     \"list\": [       {         \"keyword\": \"fast delivery\",         \"relevance_score\": 95,         \"search_volume\": \"high\",         \"post_count\": 8934       },       {         \"keyword\": \"discount code\",         \"relevance_score\": 88,         \"search_volume\": \"medium\",         \"post_count\": 5621       }     ]   } } ```  # [English] ### Purpose: - Get other keywords or hashtags related to a specified keyword - Discover related search terms to expand ad keyword library - Analyze breakout keywords to capture emerging trends  ### Parameters: - keyword: Main keyword, required parameter - period: Time period in days, e.g., 7, 30 days - country_code: Country code, e.g., US, UK, JP - rank_type: Ranking type, \"popular\"=Popular, \"breakout\"=Breakout - content_type: Content type, \"keyword\"=Keywords, \"hashtag\"=Hashtags  ### Return Description: - `list`: Related keywords list   - `keyword`: Related keyword text   - `relevance_score`: Relevance score   - `search_volume`: Search volume level   - `growth_rate`: Growth rate (for breakout keywords)   - `post_count`: Number of ads using this term  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",   \"params\": {     \"keyword\": \"free shipping\",     \"period\": 7,     \"rank_type\": \"popular\"   },   \"data\": {     \"list\": [       {         \"keyword\": \"fast delivery\",         \"relevance_score\": 95,         \"search_volume\": \"high\",         \"post_count\": 8934       },       {         \"keyword\": \"discount code\",         \"relevance_score\": 88,         \"search_volume\": \"medium\",         \"post_count\": 5621       }     ]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_related_keywords_api_v1_tiktok_ads_get_related_keywords_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 目标关键词/Target keyword
        :param object period: 时间段（天）/Time period (days, 7/30/120)
        :param object country_code: 国家/地区代码/Country code
        :param object rank_type: 排名类型/Rank type (popular: 热门, breakout: 突破性)
        :param object content_type: 内容类型/Content type (keyword, hashtag)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'period', 'country_code', 'rank_type', 'content_type', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_related_keywords_api_v1_tiktok_ads_get_related_keywords_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'rank_type' in params:
            query_params.append(('rank_type', params['rank_type']))  # noqa: E501
        if 'content_type' in params:
            query_params.append(('content_type', params['content_type']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_related_keywords', 'GET',
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

    def get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get(self, clip_id, **kwargs):  # noqa: E501
        """获取音乐详情/Get sound detail  # noqa: E501

        # [中文] ### 用途: - 获取特定音乐的详细信息和使用数据 - 分析音乐的受众分布、使用趋势等多维度数据 - 帮助选择合适的背景音乐提升广告效果  ### 参数: - clip_id: 音乐ID，必填参数 - period: 时间范围（天），如7、30、120天 - country_code: 国家代码，如US、UK、JP等  ### 返回内容说明: - `disliked`: 是否不喜欢（可能为null） - `like_count`: 点赞数（可能为null） - `liked`: 是否点赞（可能为null） - `sound`: 音乐详细信息   - `audience_ages`: 受众年龄分布     - `age_level`: 年龄级别     - `score`: 分数   - `audience_countries`: 受众国家分布     - `country_info`: 国家信息       - `id`: 国家ID       - `label`: 国家标签       - `value`: 国家名称     - `score`: 分数   - `audience_interests`: 受众兴趣分布     - `interest_info`: 兴趣信息     - `score`: 分数   - `author`: 音乐作者   - `clip_id`: 片段ID   - `country_code`: 国家代码   - `cover`: 封面图URL   - `duration`: 时长（秒）   - `if_cml`: 是否商业音乐   - `is_search`: 是否搜索结果   - `link`: 音乐链接   - `longevity`: 持久度信息     - `popular_days`: 流行天数     - `current_popularity`: 当前流行度   - `music_url`: 音乐播放URL（可能为null）   - `on_list_times`: 上榜次数（可能为null）   - `promoted`: 是否推广   - `rank`: 排名（可能为null）   - `rank_diff`: 排名变化（可能为null）   - `related_items`: 相关视频列表     - `item_id`: 视频ID     - `cover_uri`: 封面URI   - `song_id`: 歌曲ID   - `title`: 音乐标题   - `trend`: 趋势数据     - `time`: 时间戳     - `value`: 数值   - `url_title`: URL标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",   \"params\": {     \"clip_id\": \"7251810329461147649\",     \"period\": 120,     \"country_code\": \"US\"   },   \"data\": {     \"sound\": {       \"title\": \"Upbeat Summer Vibes\",       \"author\": \"Music Producer\",       \"duration\": 30,       \"music_url\": \"https://music.tiktok.com/xxx\",       \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",       \"audience_ages\": [         {\"age_level\": \"18-24\", \"percentage\": 45.2},         {\"age_level\": \"25-34\", \"percentage\": 32.8}       ],       \"audience_countries\": [         {\"country\": \"US\", \"percentage\": 35.6},         {\"country\": \"UK\", \"percentage\": 18.4}       ],       \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],       \"usage_trend\": [         {\"date\": \"2025-01-01\", \"count\": 1234},         {\"date\": \"2025-01-02\", \"count\": 1456}       ]     }   } } ```  # [English] ### Purpose: - Get detailed information and usage data for specific music - Analyze multi-dimensional data like audience distribution and usage trends - Help select appropriate background music to enhance ad effectiveness  ### Parameters: - clip_id: Sound clip ID, required parameter - period: Time period in days, e.g., 7, 30, 120 days - country_code: Country code, e.g., US, UK, JP  ### Return Description: - `sound`: Sound detailed information   - `title`: Music title   - `author`: Music author/artist   - `duration`: Duration in seconds   - `music_url`: Music playback URL   - `cover_url`: Cover image URL   - `audience_ages`: Audience age distribution     - `age_level`: Age range     - `percentage`: Share percentage   - `audience_countries`: Audience country distribution     - `country`: Country code     - `percentage`: Share percentage   - `related_items`: List of popular video IDs using this music   - `usage_trend`: Usage trend data  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",   \"params\": {     \"clip_id\": \"7251810329461147649\",     \"period\": 120,     \"country_code\": \"US\"   },   \"data\": {     \"sound\": {       \"title\": \"Upbeat Summer Vibes\",       \"author\": \"Music Producer\",       \"duration\": 30,       \"music_url\": \"https://music.tiktok.com/xxx\",       \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",       \"audience_ages\": [         {\"age_level\": \"18-24\", \"percentage\": 45.2},         {\"age_level\": \"25-34\", \"percentage\": 32.8}       ],       \"audience_countries\": [         {\"country\": \"US\", \"percentage\": 35.6},         {\"country\": \"UK\", \"percentage\": 18.4}       ],       \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],       \"usage_trend\": [         {\"date\": \"2025-01-01\", \"count\": 1234},         {\"date\": \"2025-01-02\", \"count\": 1456}       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get(clip_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object clip_id: 音乐ID/Sound clip ID (required)
        :param object period: 时间范围（天）/Time period (days)
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get_with_http_info(clip_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get_with_http_info(clip_id, **kwargs)  # noqa: E501
            return data

    def get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get_with_http_info(self, clip_id, **kwargs):  # noqa: E501
        """获取音乐详情/Get sound detail  # noqa: E501

        # [中文] ### 用途: - 获取特定音乐的详细信息和使用数据 - 分析音乐的受众分布、使用趋势等多维度数据 - 帮助选择合适的背景音乐提升广告效果  ### 参数: - clip_id: 音乐ID，必填参数 - period: 时间范围（天），如7、30、120天 - country_code: 国家代码，如US、UK、JP等  ### 返回内容说明: - `disliked`: 是否不喜欢（可能为null） - `like_count`: 点赞数（可能为null） - `liked`: 是否点赞（可能为null） - `sound`: 音乐详细信息   - `audience_ages`: 受众年龄分布     - `age_level`: 年龄级别     - `score`: 分数   - `audience_countries`: 受众国家分布     - `country_info`: 国家信息       - `id`: 国家ID       - `label`: 国家标签       - `value`: 国家名称     - `score`: 分数   - `audience_interests`: 受众兴趣分布     - `interest_info`: 兴趣信息     - `score`: 分数   - `author`: 音乐作者   - `clip_id`: 片段ID   - `country_code`: 国家代码   - `cover`: 封面图URL   - `duration`: 时长（秒）   - `if_cml`: 是否商业音乐   - `is_search`: 是否搜索结果   - `link`: 音乐链接   - `longevity`: 持久度信息     - `popular_days`: 流行天数     - `current_popularity`: 当前流行度   - `music_url`: 音乐播放URL（可能为null）   - `on_list_times`: 上榜次数（可能为null）   - `promoted`: 是否推广   - `rank`: 排名（可能为null）   - `rank_diff`: 排名变化（可能为null）   - `related_items`: 相关视频列表     - `item_id`: 视频ID     - `cover_uri`: 封面URI   - `song_id`: 歌曲ID   - `title`: 音乐标题   - `trend`: 趋势数据     - `time`: 时间戳     - `value`: 数值   - `url_title`: URL标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",   \"params\": {     \"clip_id\": \"7251810329461147649\",     \"period\": 120,     \"country_code\": \"US\"   },   \"data\": {     \"sound\": {       \"title\": \"Upbeat Summer Vibes\",       \"author\": \"Music Producer\",       \"duration\": 30,       \"music_url\": \"https://music.tiktok.com/xxx\",       \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",       \"audience_ages\": [         {\"age_level\": \"18-24\", \"percentage\": 45.2},         {\"age_level\": \"25-34\", \"percentage\": 32.8}       ],       \"audience_countries\": [         {\"country\": \"US\", \"percentage\": 35.6},         {\"country\": \"UK\", \"percentage\": 18.4}       ],       \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],       \"usage_trend\": [         {\"date\": \"2025-01-01\", \"count\": 1234},         {\"date\": \"2025-01-02\", \"count\": 1456}       ]     }   } } ```  # [English] ### Purpose: - Get detailed information and usage data for specific music - Analyze multi-dimensional data like audience distribution and usage trends - Help select appropriate background music to enhance ad effectiveness  ### Parameters: - clip_id: Sound clip ID, required parameter - period: Time period in days, e.g., 7, 30, 120 days - country_code: Country code, e.g., US, UK, JP  ### Return Description: - `sound`: Sound detailed information   - `title`: Music title   - `author`: Music author/artist   - `duration`: Duration in seconds   - `music_url`: Music playback URL   - `cover_url`: Cover image URL   - `audience_ages`: Audience age distribution     - `age_level`: Age range     - `percentage`: Share percentage   - `audience_countries`: Audience country distribution     - `country`: Country code     - `percentage`: Share percentage   - `related_items`: List of popular video IDs using this music   - `usage_trend`: Usage trend data  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",   \"params\": {     \"clip_id\": \"7251810329461147649\",     \"period\": 120,     \"country_code\": \"US\"   },   \"data\": {     \"sound\": {       \"title\": \"Upbeat Summer Vibes\",       \"author\": \"Music Producer\",       \"duration\": 30,       \"music_url\": \"https://music.tiktok.com/xxx\",       \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",       \"audience_ages\": [         {\"age_level\": \"18-24\", \"percentage\": 45.2},         {\"age_level\": \"25-34\", \"percentage\": 32.8}       ],       \"audience_countries\": [         {\"country\": \"US\", \"percentage\": 35.6},         {\"country\": \"UK\", \"percentage\": 18.4}       ],       \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],       \"usage_trend\": [         {\"date\": \"2025-01-01\", \"count\": 1234},         {\"date\": \"2025-01-02\", \"count\": 1456}       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get_with_http_info(clip_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object clip_id: 音乐ID/Sound clip ID (required)
        :param object period: 时间范围（天）/Time period (days)
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['clip_id', 'period', 'country_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'clip_id' is set
        if self.api_client.client_side_validation and ('clip_id' not in params or
                                                       params['clip_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `clip_id` when calling `get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'clip_id' in params:
            query_params.append(('clip_id', params['clip_id']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_sound_detail', 'GET',
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

    def get_sound_filters_api_v1_tiktok_ads_get_sound_filters_get(self, **kwargs):  # noqa: E501
        """获取音乐筛选器/Get sound filters  # noqa: E501

        # [中文] ### 用途: - 获取热门音乐功能的可用筛选选项 - 了解不同排行类型下的筛选维度 - 为音乐选择提供参数参考  ### 参数: - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快  ### 返回内容说明: - `country`: 国家列表   - `id`: 国家ID   - `value`: 国家名称   - `label`: 国家标签  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",   \"params\": {     \"rank_type\": \"popular\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"country\": [         {           \"id\": \"AR\",           \"value\": \"Argentina\",           \"label\": \"AR\"         },         {           \"id\": \"AU\",           \"value\": \"Australia\",           \"label\": \"AU\"         }       ]     }   } } ```  # [English] ### Purpose: - Get available filter options for popular music functionality - Understand filter dimensions for different ranking types - Provide parameter reference for music selection  ### Parameters: - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising  ### Return Description: - `country`: Country list   - `id`: Country ID   - `value`: Country name   - `label`: Country label  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",   \"params\": {     \"rank_type\": \"popular\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"country\": [         {           \"id\": \"AR\",           \"value\": \"Argentina\",           \"label\": \"AR\"         },         {           \"id\": \"AU\",           \"value\": \"Australia\",           \"label\": \"AU\"         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sound_filters_api_v1_tiktok_ads_get_sound_filters_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object rank_type: 排行类型/Rank type (popular, surging)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sound_filters_api_v1_tiktok_ads_get_sound_filters_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sound_filters_api_v1_tiktok_ads_get_sound_filters_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sound_filters_api_v1_tiktok_ads_get_sound_filters_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取音乐筛选器/Get sound filters  # noqa: E501

        # [中文] ### 用途: - 获取热门音乐功能的可用筛选选项 - 了解不同排行类型下的筛选维度 - 为音乐选择提供参数参考  ### 参数: - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快  ### 返回内容说明: - `country`: 国家列表   - `id`: 国家ID   - `value`: 国家名称   - `label`: 国家标签  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",   \"params\": {     \"rank_type\": \"popular\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"country\": [         {           \"id\": \"AR\",           \"value\": \"Argentina\",           \"label\": \"AR\"         },         {           \"id\": \"AU\",           \"value\": \"Australia\",           \"label\": \"AU\"         }       ]     }   } } ```  # [English] ### Purpose: - Get available filter options for popular music functionality - Understand filter dimensions for different ranking types - Provide parameter reference for music selection  ### Parameters: - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising  ### Return Description: - `country`: Country list   - `id`: Country ID   - `value`: Country name   - `label`: Country label  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",   \"params\": {     \"rank_type\": \"popular\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"country\": [         {           \"id\": \"AR\",           \"value\": \"Argentina\",           \"label\": \"AR\"         },         {           \"id\": \"AU\",           \"value\": \"Australia\",           \"label\": \"AU\"         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sound_filters_api_v1_tiktok_ads_get_sound_filters_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object rank_type: 排行类型/Rank type (popular, surging)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rank_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sound_filters_api_v1_tiktok_ads_get_sound_filters_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rank_type' in params:
            query_params.append(('rank_type', params['rank_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_sound_filters', 'GET',
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

    def get_sound_rank_list_api_v1_tiktok_ads_get_sound_rank_list_get(self, **kwargs):  # noqa: E501
        """获取热门音乐排行榜/Get popular sound rankings  # noqa: E501

        # [中文] ### 用途: - 获取TikTok广告中的热门音乐排行榜，了解当前流行的音乐素材 - 分析音乐的使用量、增长趋势等数据，发现潜力音乐 - 帮助广告主选择合适的背景音乐，提升广告吸引力和传播效果  ### 参数: - period: 时间范围（天），如7、30、120天 - page: 页码，默认1 - limit: 每页数量，默认20 - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快 - new_on_board: 是否只看新上榜音乐，默认False - commercial_music: 是否只看商业音乐，默认False - country_code: 国家代码，如US、UK、JP等  ### 返回内容说明: - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多 - `sound_list`: 音乐列表   - `author`: 音乐作者   - `clip_id`: 片段ID   - `cml_mid`: 商业音乐ID   - `country_code`: 国家代码   - `cover`: 封面图URL   - `duration`: 时长（秒）   - `if_cml`: 是否商业音乐   - `is_search`: 是否搜索结果   - `link`: 音乐链接   - `music_url`: 音乐播放URL   - `on_list_times`: 上榜次数（可能为null）   - `promoted`: 是否推广   - `rank`: 排名   - `rank_diff`: 排名变化   - `rank_diff_type`: 排名变化类型   - `related_items`: 相关视频列表     - `item_id`: 视频ID     - `cover_uri`: 封面URI   - `song_id`: 歌曲ID   - `title`: 音乐标题   - `trend`: 趋势数据     - `time`: 时间戳     - `value`: 该时间点的值   - `url_title`: URL标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",   \"params\": {     \"period\": \"30\",     \"page\": \"1\",     \"limit\": \"20\",     \"rank_type\": \"popular\",     \"new_on_board\": \"false\",     \"commercial_music\": \"false\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 99,         \"has_more\": true       },       \"sound_list\": [         {           \"author\": \"CYRIL & MOONLGHT & The La's\",           \"clip_id\": \"7424014547218565904\",           \"cml_mid\": \"7512350022513852432\",           \"country_code\": \"US\",           \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",           \"duration\": 22,           \"if_cml\": true,           \"is_search\": false,           \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",           \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",           \"on_list_times\": null,           \"promoted\": false,           \"rank\": 1,           \"rank_diff\": 0,           \"rank_diff_type\": 2,           \"related_items\": [             {               \"item_id\": 7512619474084711723,               \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"             }           ],           \"song_id\": \"7503950818010335233\",           \"title\": \"There She Goes\",           \"trend\": [             {               \"time\": 1740787200,               \"value\": 0.15             }           ],           \"url_title\": \"There She Goes (CYRIL Remix)\"         }       ]     }   } } ```  # [English] ### Purpose: - Get popular music rankings in TikTok ads to understand current trending audio materials - Analyze usage and growth trend data for music to discover potential sounds - Help advertisers choose appropriate background music to enhance ad appeal and virality  ### Parameters: - period: Time period in days, e.g., 7, 30, 120 days - page: Page number, default 1 - limit: Items per page, default 20 - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising - new_on_board: Only show newly trending music, default False - commercial_music: Only show commercial music, default False - country_code: Country code, e.g., US, UK, JP  ### Return Description: - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items - `sound_list`: Music list   - `author`: Music author   - `clip_id`: Clip ID   - `cml_mid`: Commercial music ID   - `country_code`: Country code   - `cover`: Cover image URL   - `duration`: Duration in seconds   - `if_cml`: Whether commercial music   - `is_search`: Whether search result   - `link`: Music link   - `music_url`: Music playback URL   - `on_list_times`: Times on list (may be null)   - `promoted`: Whether promoted   - `rank`: Ranking   - `rank_diff`: Rank difference   - `rank_diff_type`: Rank difference type   - `related_items`: Related video list     - `item_id`: Video ID     - `cover_uri`: Cover URI   - `song_id`: Song ID   - `title`: Music title   - `trend`: Trend data     - `time`: Timestamp     - `value`: Value at that time point   - `url_title`: URL title  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",   \"params\": {     \"period\": \"30\",     \"page\": \"1\",     \"limit\": \"20\",     \"rank_type\": \"popular\",     \"new_on_board\": \"false\",     \"commercial_music\": \"false\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 99,         \"has_more\": true       },       \"sound_list\": [         {           \"author\": \"CYRIL & MOONLGHT & The La's\",           \"clip_id\": \"7424014547218565904\",           \"cml_mid\": \"7512350022513852432\",           \"country_code\": \"US\",           \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",           \"duration\": 22,           \"if_cml\": true,           \"is_search\": false,           \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",           \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",           \"on_list_times\": null,           \"promoted\": false,           \"rank\": 1,           \"rank_diff\": 0,           \"rank_diff_type\": 2,           \"related_items\": [             {               \"item_id\": 7512619474084711723,               \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"             }           ],           \"song_id\": \"7503950818010335233\",           \"title\": \"There She Goes\",           \"trend\": [             {               \"time\": 1740787200,               \"value\": 0.15             }           ],           \"url_title\": \"There She Goes (CYRIL Remix)\"         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sound_rank_list_api_v1_tiktok_ads_get_sound_rank_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object period: 时间范围（天）/Time period (days)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object rank_type: 排行类型/Rank type (popular, surging)
        :param object new_on_board: 是否只看新上榜/Only new on board
        :param object commercial_music: 是否商业音乐/Commercial music only
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sound_rank_list_api_v1_tiktok_ads_get_sound_rank_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sound_rank_list_api_v1_tiktok_ads_get_sound_rank_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sound_rank_list_api_v1_tiktok_ads_get_sound_rank_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热门音乐排行榜/Get popular sound rankings  # noqa: E501

        # [中文] ### 用途: - 获取TikTok广告中的热门音乐排行榜，了解当前流行的音乐素材 - 分析音乐的使用量、增长趋势等数据，发现潜力音乐 - 帮助广告主选择合适的背景音乐，提升广告吸引力和传播效果  ### 参数: - period: 时间范围（天），如7、30、120天 - page: 页码，默认1 - limit: 每页数量，默认20 - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快 - new_on_board: 是否只看新上榜音乐，默认False - commercial_music: 是否只看商业音乐，默认False - country_code: 国家代码，如US、UK、JP等  ### 返回内容说明: - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多 - `sound_list`: 音乐列表   - `author`: 音乐作者   - `clip_id`: 片段ID   - `cml_mid`: 商业音乐ID   - `country_code`: 国家代码   - `cover`: 封面图URL   - `duration`: 时长（秒）   - `if_cml`: 是否商业音乐   - `is_search`: 是否搜索结果   - `link`: 音乐链接   - `music_url`: 音乐播放URL   - `on_list_times`: 上榜次数（可能为null）   - `promoted`: 是否推广   - `rank`: 排名   - `rank_diff`: 排名变化   - `rank_diff_type`: 排名变化类型   - `related_items`: 相关视频列表     - `item_id`: 视频ID     - `cover_uri`: 封面URI   - `song_id`: 歌曲ID   - `title`: 音乐标题   - `trend`: 趋势数据     - `time`: 时间戳     - `value`: 该时间点的值   - `url_title`: URL标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",   \"params\": {     \"period\": \"30\",     \"page\": \"1\",     \"limit\": \"20\",     \"rank_type\": \"popular\",     \"new_on_board\": \"false\",     \"commercial_music\": \"false\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 99,         \"has_more\": true       },       \"sound_list\": [         {           \"author\": \"CYRIL & MOONLGHT & The La's\",           \"clip_id\": \"7424014547218565904\",           \"cml_mid\": \"7512350022513852432\",           \"country_code\": \"US\",           \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",           \"duration\": 22,           \"if_cml\": true,           \"is_search\": false,           \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",           \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",           \"on_list_times\": null,           \"promoted\": false,           \"rank\": 1,           \"rank_diff\": 0,           \"rank_diff_type\": 2,           \"related_items\": [             {               \"item_id\": 7512619474084711723,               \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"             }           ],           \"song_id\": \"7503950818010335233\",           \"title\": \"There She Goes\",           \"trend\": [             {               \"time\": 1740787200,               \"value\": 0.15             }           ],           \"url_title\": \"There She Goes (CYRIL Remix)\"         }       ]     }   } } ```  # [English] ### Purpose: - Get popular music rankings in TikTok ads to understand current trending audio materials - Analyze usage and growth trend data for music to discover potential sounds - Help advertisers choose appropriate background music to enhance ad appeal and virality  ### Parameters: - period: Time period in days, e.g., 7, 30, 120 days - page: Page number, default 1 - limit: Items per page, default 20 - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising - new_on_board: Only show newly trending music, default False - commercial_music: Only show commercial music, default False - country_code: Country code, e.g., US, UK, JP  ### Return Description: - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items - `sound_list`: Music list   - `author`: Music author   - `clip_id`: Clip ID   - `cml_mid`: Commercial music ID   - `country_code`: Country code   - `cover`: Cover image URL   - `duration`: Duration in seconds   - `if_cml`: Whether commercial music   - `is_search`: Whether search result   - `link`: Music link   - `music_url`: Music playback URL   - `on_list_times`: Times on list (may be null)   - `promoted`: Whether promoted   - `rank`: Ranking   - `rank_diff`: Rank difference   - `rank_diff_type`: Rank difference type   - `related_items`: Related video list     - `item_id`: Video ID     - `cover_uri`: Cover URI   - `song_id`: Song ID   - `title`: Music title   - `trend`: Trend data     - `time`: Timestamp     - `value`: Value at that time point   - `url_title`: URL title  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",   \"params\": {     \"period\": \"30\",     \"page\": \"1\",     \"limit\": \"20\",     \"rank_type\": \"popular\",     \"new_on_board\": \"false\",     \"commercial_music\": \"false\",     \"country_code\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 99,         \"has_more\": true       },       \"sound_list\": [         {           \"author\": \"CYRIL & MOONLGHT & The La's\",           \"clip_id\": \"7424014547218565904\",           \"cml_mid\": \"7512350022513852432\",           \"country_code\": \"US\",           \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",           \"duration\": 22,           \"if_cml\": true,           \"is_search\": false,           \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",           \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",           \"on_list_times\": null,           \"promoted\": false,           \"rank\": 1,           \"rank_diff\": 0,           \"rank_diff_type\": 2,           \"related_items\": [             {               \"item_id\": 7512619474084711723,               \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"             }           ],           \"song_id\": \"7503950818010335233\",           \"title\": \"There She Goes\",           \"trend\": [             {               \"time\": 1740787200,               \"value\": 0.15             }           ],           \"url_title\": \"There She Goes (CYRIL Remix)\"         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sound_rank_list_api_v1_tiktok_ads_get_sound_rank_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object period: 时间范围（天）/Time period (days)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object rank_type: 排行类型/Rank type (popular, surging)
        :param object new_on_board: 是否只看新上榜/Only new on board
        :param object commercial_music: 是否商业音乐/Commercial music only
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['period', 'page', 'limit', 'rank_type', 'new_on_board', 'commercial_music', 'country_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sound_rank_list_api_v1_tiktok_ads_get_sound_rank_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'rank_type' in params:
            query_params.append(('rank_type', params['rank_type']))  # noqa: E501
        if 'new_on_board' in params:
            query_params.append(('new_on_board', params['new_on_board']))  # noqa: E501
        if 'commercial_music' in params:
            query_params.append(('commercial_music', params['commercial_music']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_sound_rank_list', 'GET',
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

    def get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get(self, clip_id, **kwargs):  # noqa: E501
        """获取音乐推荐/Get sound recommendations  # noqa: E501

        # [中文] ### 用途: - 基于指定音乐获取相似的推荐音乐 - 发现风格相近或使用场景类似的音乐 - 扩展音乐选择范围，找到更多合适的配乐  ### 参数: - clip_id: 参考音乐ID，必填参数 - limit: 推荐数量，默认6  ### 返回内容说明: - `musics`: 推荐音乐列表   - `author`: 音乐作者   - `cover`: 封面图URL   - `music_id`: 音乐ID   - `music_url`: 音乐播放URL   - `title`: 音乐标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",   \"params\": {     \"clip_id\": \"7156826385225353217\",     \"limit\": \"6\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"musics\": [         {           \"author\": \"zomap\",           \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",           \"music_id\": \"6949146013727653889\",           \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-obj/d0d0dca4400886718099898494b7e31b.mp3\",           \"title\": \"Relaxed and gentle fashionable chillout(810161)\"         },         {           \"author\": \"zomap\",           \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",           \"music_id\": \"6949294080044843010\",           \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-obj/451acbadd83a76748a99878ccfef2df5.mp3\",           \"title\": \"Relaxed and gentle fashionable chillout(816672)\"         }       ]     }   } } ```  # [English] ### Purpose: - Get similar music recommendations based on specified music - Discover music with similar styles or usage scenarios - Expand music selection range to find more suitable soundtracks  ### Parameters: - clip_id: Reference sound clip ID, required parameter - limit: Number of recommendations, default 6  ### Return Description: - `musics`: Recommended music list   - `author`: Music author   - `cover`: Cover image URL   - `music_id`: Music ID   - `music_url`: Music playback URL   - `title`: Music title  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",   \"params\": {     \"clip_id\": \"7156826385225353217\",     \"limit\": 6   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"musics\": [         {           \"author\": \"zomap\",           \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",           \"music_id\": \"6949146013727653889\",           \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-obj/d0d0dca4400886718099898494b7e31b.mp3\",           \"title\": \"Relaxed and gentle fashionable chillout(810161)\"         },         {           \"author\": \"zomap\",           \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",           \"music_id\": \"6949294080044843010\",           \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-obj/451acbadd83a76748a99878ccfef2df5.mp3\",           \"title\": \"Relaxed and gentle fashionable chillout(816672)\"         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get(clip_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object clip_id: 参考音乐ID/Reference sound clip ID (required)
        :param object limit: 推荐数量/Number of recommendations
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get_with_http_info(clip_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get_with_http_info(clip_id, **kwargs)  # noqa: E501
            return data

    def get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get_with_http_info(self, clip_id, **kwargs):  # noqa: E501
        """获取音乐推荐/Get sound recommendations  # noqa: E501

        # [中文] ### 用途: - 基于指定音乐获取相似的推荐音乐 - 发现风格相近或使用场景类似的音乐 - 扩展音乐选择范围，找到更多合适的配乐  ### 参数: - clip_id: 参考音乐ID，必填参数 - limit: 推荐数量，默认6  ### 返回内容说明: - `musics`: 推荐音乐列表   - `author`: 音乐作者   - `cover`: 封面图URL   - `music_id`: 音乐ID   - `music_url`: 音乐播放URL   - `title`: 音乐标题  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",   \"params\": {     \"clip_id\": \"7156826385225353217\",     \"limit\": \"6\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"musics\": [         {           \"author\": \"zomap\",           \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",           \"music_id\": \"6949146013727653889\",           \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-obj/d0d0dca4400886718099898494b7e31b.mp3\",           \"title\": \"Relaxed and gentle fashionable chillout(810161)\"         },         {           \"author\": \"zomap\",           \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",           \"music_id\": \"6949294080044843010\",           \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-obj/451acbadd83a76748a99878ccfef2df5.mp3\",           \"title\": \"Relaxed and gentle fashionable chillout(816672)\"         }       ]     }   } } ```  # [English] ### Purpose: - Get similar music recommendations based on specified music - Discover music with similar styles or usage scenarios - Expand music selection range to find more suitable soundtracks  ### Parameters: - clip_id: Reference sound clip ID, required parameter - limit: Number of recommendations, default 6  ### Return Description: - `musics`: Recommended music list   - `author`: Music author   - `cover`: Cover image URL   - `music_id`: Music ID   - `music_url`: Music playback URL   - `title`: Music title  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",   \"params\": {     \"clip_id\": \"7156826385225353217\",     \"limit\": 6   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"musics\": [         {           \"author\": \"zomap\",           \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",           \"music_id\": \"6949146013727653889\",           \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-obj/d0d0dca4400886718099898494b7e31b.mp3\",           \"title\": \"Relaxed and gentle fashionable chillout(810161)\"         },         {           \"author\": \"zomap\",           \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",           \"music_id\": \"6949294080044843010\",           \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-obj/451acbadd83a76748a99878ccfef2df5.mp3\",           \"title\": \"Relaxed and gentle fashionable chillout(816672)\"         }       ]     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get_with_http_info(clip_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object clip_id: 参考音乐ID/Reference sound clip ID (required)
        :param object limit: 推荐数量/Number of recommendations
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['clip_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'clip_id' is set
        if self.api_client.client_side_validation and ('clip_id' not in params or
                                                       params['clip_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `clip_id` when calling `get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'clip_id' in params:
            query_params.append(('clip_id', params['clip_id']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_sound_recommendations', 'GET',
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

    def get_top_ads_spotlight_api_v1_tiktok_ads_get_top_ads_spotlight_get(self, **kwargs):  # noqa: E501
        """获取热门广告聚光灯/Get top ads spotlight  # noqa: E501

        # [中文] ### 用途: - 获取特定行业的热门广告聚光灯，展示行业内最受关注的广告案例 - 分析行业内的广告创意趋势和优秀案例 - 为广告创意制作提供灵感和参考  ### 参数: - industry: 行业ID，必填参数，如教育行业：25000000000 - page: 页码，默认1 - limit: 每页数量，默认20  ### 返回内容说明: - `materials`: 广告素材列表   - `cost`: 花费等级   - `ctr`: 点击率   - `highlight`: 亮点描述   - `id`: 广告ID   - `like`: 点赞数   - `video_info`: 视频信息     - `vid`: 视频ID     - `duration`: 时长（秒）     - `cover`: 封面图片URL     - `video_url`: 多种画质的视频播放URL       - `360p`: 360p画质视频URL       - `480p`: 480p画质视频URL       - `540p`: 540p画质视频URL       - `720p`: 720p画质视频URL     - `width`: 视频宽度     - `height`: 视频高度 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",   \"params\": {     \"industry\": \"25000000000\",     \"page\": \"1\",     \"limit\": \"20\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"materials\": [         {           \"cost\": 2,           \"ctr\": 0.14,           \"highlight\": \"Through the lens of a real person talking his way through the game, the video appears credible with commentary that sounds trustworthy.\",           \"id\": \"7165768841499066370\",           \"like\": 377333,           \"video_info\": {             \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",             \"duration\": 19.156,             \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",             \"video_url\": {               \"360p\": \"https://v16m-default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",               \"480p\": \"https://v16m-default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",               \"540p\": \"https://v16m-default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",               \"720p\": \"https://v16m-default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"             },             \"width\": 720,             \"height\": 1280           }         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 100,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get top ads spotlight for specific industries, showcasing the most popular ad cases - Analyze creative trends and excellent cases within the industry - Provide inspiration and reference for ad creative production  ### Parameters: - industry: Industry ID, required parameter, e.g., Education: 25000000000 - page: Page number, default 1 - limit: Items per page, default 20  ### Return Description: - `materials`: Ad materials list   - `cost`: Cost level   - `ctr`: Click-through rate   - `highlight`: Highlight description   - `id`: Ad ID   - `like`: Like count   - `video_info`: Video information     - `vid`: Video ID     - `duration`: Duration in seconds     - `cover`: Cover image URL     - `video_url`: Video playback URLs in multiple qualities       - `360p`: 360p quality video URL       - `480p`: 480p quality video URL       - `540p`: 540p quality video URL       - `720p`: 720p quality video URL     - `width`: Video width     - `height`: Video height - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",   \"params\": {     \"industry\": \"25000000000\",     \"page\": \"1\",     \"limit\": \"20\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"materials\": [         {           \"cost\": 2,           \"ctr\": 0.14,           \"highlight\": \"Through the lens of a real person talking his way through the game, the video appears credible with commentary that sounds trustworthy.\",           \"id\": \"7165768841499066370\",           \"like\": 377333,           \"video_info\": {             \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",             \"duration\": 19.156,             \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",             \"video_url\": {               \"360p\": \"https://v16m-default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",               \"480p\": \"https://v16m-default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",               \"540p\": \"https://v16m-default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",               \"720p\": \"https://v16m-default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"             },             \"width\": 720,             \"height\": 1280           }         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 100,       \"has_more\": true     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_top_ads_spotlight_api_v1_tiktok_ads_get_top_ads_spotlight_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object industry: 行业ID/Industry ID
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_top_ads_spotlight_api_v1_tiktok_ads_get_top_ads_spotlight_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_top_ads_spotlight_api_v1_tiktok_ads_get_top_ads_spotlight_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_top_ads_spotlight_api_v1_tiktok_ads_get_top_ads_spotlight_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热门广告聚光灯/Get top ads spotlight  # noqa: E501

        # [中文] ### 用途: - 获取特定行业的热门广告聚光灯，展示行业内最受关注的广告案例 - 分析行业内的广告创意趋势和优秀案例 - 为广告创意制作提供灵感和参考  ### 参数: - industry: 行业ID，必填参数，如教育行业：25000000000 - page: 页码，默认1 - limit: 每页数量，默认20  ### 返回内容说明: - `materials`: 广告素材列表   - `cost`: 花费等级   - `ctr`: 点击率   - `highlight`: 亮点描述   - `id`: 广告ID   - `like`: 点赞数   - `video_info`: 视频信息     - `vid`: 视频ID     - `duration`: 时长（秒）     - `cover`: 封面图片URL     - `video_url`: 多种画质的视频播放URL       - `360p`: 360p画质视频URL       - `480p`: 480p画质视频URL       - `540p`: 540p画质视频URL       - `720p`: 720p画质视频URL     - `width`: 视频宽度     - `height`: 视频高度 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",   \"params\": {     \"industry\": \"25000000000\",     \"page\": \"1\",     \"limit\": \"20\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"materials\": [         {           \"cost\": 2,           \"ctr\": 0.14,           \"highlight\": \"Through the lens of a real person talking his way through the game, the video appears credible with commentary that sounds trustworthy.\",           \"id\": \"7165768841499066370\",           \"like\": 377333,           \"video_info\": {             \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",             \"duration\": 19.156,             \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",             \"video_url\": {               \"360p\": \"https://v16m-default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",               \"480p\": \"https://v16m-default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",               \"540p\": \"https://v16m-default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",               \"720p\": \"https://v16m-default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"             },             \"width\": 720,             \"height\": 1280           }         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 100,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get top ads spotlight for specific industries, showcasing the most popular ad cases - Analyze creative trends and excellent cases within the industry - Provide inspiration and reference for ad creative production  ### Parameters: - industry: Industry ID, required parameter, e.g., Education: 25000000000 - page: Page number, default 1 - limit: Items per page, default 20  ### Return Description: - `materials`: Ad materials list   - `cost`: Cost level   - `ctr`: Click-through rate   - `highlight`: Highlight description   - `id`: Ad ID   - `like`: Like count   - `video_info`: Video information     - `vid`: Video ID     - `duration`: Duration in seconds     - `cover`: Cover image URL     - `video_url`: Video playback URLs in multiple qualities       - `360p`: 360p quality video URL       - `480p`: 480p quality video URL       - `540p`: 540p quality video URL       - `720p`: 720p quality video URL     - `width`: Video width     - `height`: Video height - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",   \"params\": {     \"industry\": \"25000000000\",     \"page\": \"1\",     \"limit\": \"20\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"materials\": [         {           \"cost\": 2,           \"ctr\": 0.14,           \"highlight\": \"Through the lens of a real person talking his way through the game, the video appears credible with commentary that sounds trustworthy.\",           \"id\": \"7165768841499066370\",           \"like\": 377333,           \"video_info\": {             \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",             \"duration\": 19.156,             \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",             \"video_url\": {               \"360p\": \"https://v16m-default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",               \"480p\": \"https://v16m-default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",               \"540p\": \"https://v16m-default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",               \"720p\": \"https://v16m-default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"             },             \"width\": 720,             \"height\": 1280           }         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 100,       \"has_more\": true     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_top_ads_spotlight_api_v1_tiktok_ads_get_top_ads_spotlight_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object industry: 行业ID/Industry ID
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['industry', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_top_ads_spotlight_api_v1_tiktok_ads_get_top_ads_spotlight_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'industry' in params:
            query_params.append(('industry', params['industry']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_top_ads_spotlight', 'GET',
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

    def get_top_products_api_v1_tiktok_ads_get_top_products_get(self, **kwargs):  # noqa: E501
        """获取热门产品列表/Get top products list  # noqa: E501

        # [中文] ### 用途: - 获取TikTok广告中的热门产品排行榜，了解各类目下的爆款产品 - 分析产品的广告投放量、点击率、转化率等核心指标 - 帮助电商卖家发现潜力产品，优化选品和营销策略  ### 参数: - last: 最近天数，如7、30天 - page: 页码，默认1 - limit: 每页数量，默认20 - country_code: 国家代码，如US、UK、JP等 - first_ecom_category_id: 电商类目ID，多个用逗号分隔 - ecom_type: 电商类型，默认\"l3\" - period_type: 时间类型，默认\"last\" - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、cvr（转化率） - order_type: 排序方式，desc（降序）或asc（升序）  ### 常用电商类目ID: - 美妆个护: 605196 - 女装女内衣: 602284 - 时尚配饰: 601450 - 手机电子: 801928 - 健康产品: 951432 - 家居用品: 601755 - 男装男内衣: 605248 - 香水: 601583  ### 返回内容说明: - `list`: 产品列表   - `comment`: 评论数   - `cost`: 花费金额   - `cover_url`: 封面图URL（可能为null）   - `cpa`: 每次转化成本   - `ctr`: 点击率（百分比）   - `cvr`: 转化率（百分比）   - `ecom_type`: 电商类型   - `first_ecom_category`: 一级电商类目     - `id`: 类目ID     - `label`: 类目标签     - `value`: 类目名称   - `impression`: 展示量   - `like`: 点赞数   - `play_six_rate`: 6秒播放率（百分比）   - `post`: 发布量   - `post_change`: 发布量变化率（百分比）   - `second_ecom_category`: 二级电商类目     - `id`: 类目ID     - `label`: 类目标签     - `parent_id`: 父类目ID     - `value`: 类目名称   - `share`: 分享数   - `third_ecom_category`: 三级电商类目     - `id`: 类目ID     - `label`: 类目标签     - `parent_id`: 父类目ID     - `value`: 类目名称   - `url_title`: URL标题 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_top_products\",   \"params\": {     \"last\": \"7\",     \"page\": \"1\",     \"limit\": \"20\",     \"country_code\": \"US\",     \"first_ecom_category_id\": \"\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"list\": [         {           \"comment\": 3449,           \"cost\": 477000,           \"cover_url\": null,           \"cpa\": 9.21,           \"ctr\": 1.29,           \"cvr\": 12.94,           \"ecom_type\": \"l3\",           \"first_ecom_category\": {             \"id\": \"601450\",             \"label\": \"category_601450\",             \"value\": \"Beauty & Personal Care\"           },           \"impression\": 65000000,           \"like\": 166618,           \"play_six_rate\": 7.62,           \"post\": 10600,           \"post_change\": -10.16,           \"second_ecom_category\": {             \"id\": \"848648\",             \"label\": \"category_848648\",             \"parent_id\": \"601450\",             \"value\": \"Makeup & Perfume\"           },           \"share\": 2359,           \"third_ecom_category\": {             \"id\": \"601583\",             \"label\": \"category_601583\",             \"parent_id\": \"848648\",             \"value\": \"Perfume\"           },           \"url_title\": \"Perfume\"         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 156,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get top product rankings in TikTok ads to understand popular products in various categories - Analyze core metrics like ad post volume, CTR, and conversion rate for products - Help e-commerce sellers discover potential products and optimize product selection and marketing strategies  ### Parameters: - last: Number of recent days, e.g., 7, 30 days - page: Page number, default 1 - limit: Items per page, default 20 - country_code: Country code, e.g., US, UK, JP - first_ecom_category_id: E-commerce category IDs, multiple separated by commas - ecom_type: E-commerce type, default \"l3\" - period_type: Period type, default \"last\" - order_by: Sort field, options: post (post volume), ctr (click-through rate), cvr (conversion rate) - order_type: Sort order, desc (descending) or asc (ascending)  ### Common E-commerce Category IDs: - Beauty & Personal Care: 605196 - Women's Clothing & Underwear: 602284 - Fashion Accessories: 601450 - Mobile & Electronics: 801928 - Health Products: 951432 - Home & Living: 601755 - Men's Clothing & Underwear: 605248 - Perfume: 601583  ### Return Description: - `list`: Product list   - `comment`: Comment count   - `cost`: Cost amount   - `cover_url`: Cover image URL (may be null)   - `cpa`: Cost per acquisition   - `ctr`: Click-through rate (percentage)   - `cvr`: Conversion rate (percentage)   - `ecom_type`: E-commerce type   - `first_ecom_category`: First-level e-commerce category     - `id`: Category ID     - `label`: Category label     - `value`: Category name   - `impression`: Impression count   - `like`: Like count   - `play_six_rate`: 6-second play rate (percentage)   - `post`: Post volume   - `post_change`: Post volume change rate (percentage)   - `second_ecom_category`: Second-level e-commerce category     - `id`: Category ID     - `label`: Category label     - `parent_id`: Parent category ID     - `value`: Category name   - `share`: Share count   - `third_ecom_category`: Third-level e-commerce category     - `id`: Category ID     - `label`: Category label     - `parent_id`: Parent category ID     - `value`: Category name   - `url_title`: URL title - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_top_products\",   \"params\": {     \"last\": \"7\",     \"page\": \"1\",     \"limit\": \"20\",     \"country_code\": \"US\",     \"first_ecom_category_id\": \"\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"list\": [         {           \"comment\": 3449,           \"cost\": 477000,           \"cover_url\": null,           \"cpa\": 9.21,           \"ctr\": 1.29,           \"cvr\": 12.94,           \"ecom_type\": \"l3\",           \"first_ecom_category\": {             \"id\": \"601450\",             \"label\": \"category_601450\",             \"value\": \"Beauty & Personal Care\"           },           \"impression\": 65000000,           \"like\": 166618,           \"play_six_rate\": 7.62,           \"post\": 10600,           \"post_change\": -10.16,           \"second_ecom_category\": {             \"id\": \"848648\",             \"label\": \"category_848648\",             \"parent_id\": \"601450\",             \"value\": \"Makeup & Perfume\"           },           \"share\": 2359,           \"third_ecom_category\": {             \"id\": \"601583\",             \"label\": \"category_601583\",             \"parent_id\": \"848648\",             \"value\": \"Perfume\"           },           \"url_title\": \"Perfume\"         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 156,         \"has_more\": true       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_top_products_api_v1_tiktok_ads_get_top_products_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object last: 最近天数/Last days
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object country_code: 国家代码/Country code
        :param object first_ecom_category_id: 电商类目ID，多个用逗号分隔/E-commerce category IDs, comma separated
        :param object ecom_type: 电商类型/E-commerce type (l3)
        :param object period_type: 时间类型/Period type (last)
        :param object order_by: 排序字段/Sort field (post, ctr, cvr)
        :param object order_type: 排序方式/Sort order (desc, asc)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_top_products_api_v1_tiktok_ads_get_top_products_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_top_products_api_v1_tiktok_ads_get_top_products_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_top_products_api_v1_tiktok_ads_get_top_products_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热门产品列表/Get top products list  # noqa: E501

        # [中文] ### 用途: - 获取TikTok广告中的热门产品排行榜，了解各类目下的爆款产品 - 分析产品的广告投放量、点击率、转化率等核心指标 - 帮助电商卖家发现潜力产品，优化选品和营销策略  ### 参数: - last: 最近天数，如7、30天 - page: 页码，默认1 - limit: 每页数量，默认20 - country_code: 国家代码，如US、UK、JP等 - first_ecom_category_id: 电商类目ID，多个用逗号分隔 - ecom_type: 电商类型，默认\"l3\" - period_type: 时间类型，默认\"last\" - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、cvr（转化率） - order_type: 排序方式，desc（降序）或asc（升序）  ### 常用电商类目ID: - 美妆个护: 605196 - 女装女内衣: 602284 - 时尚配饰: 601450 - 手机电子: 801928 - 健康产品: 951432 - 家居用品: 601755 - 男装男内衣: 605248 - 香水: 601583  ### 返回内容说明: - `list`: 产品列表   - `comment`: 评论数   - `cost`: 花费金额   - `cover_url`: 封面图URL（可能为null）   - `cpa`: 每次转化成本   - `ctr`: 点击率（百分比）   - `cvr`: 转化率（百分比）   - `ecom_type`: 电商类型   - `first_ecom_category`: 一级电商类目     - `id`: 类目ID     - `label`: 类目标签     - `value`: 类目名称   - `impression`: 展示量   - `like`: 点赞数   - `play_six_rate`: 6秒播放率（百分比）   - `post`: 发布量   - `post_change`: 发布量变化率（百分比）   - `second_ecom_category`: 二级电商类目     - `id`: 类目ID     - `label`: 类目标签     - `parent_id`: 父类目ID     - `value`: 类目名称   - `share`: 分享数   - `third_ecom_category`: 三级电商类目     - `id`: 类目ID     - `label`: 类目标签     - `parent_id`: 父类目ID     - `value`: 类目名称   - `url_title`: URL标题 - `pagination`: 分页信息   - `page`: 当前页   - `size`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_top_products\",   \"params\": {     \"last\": \"7\",     \"page\": \"1\",     \"limit\": \"20\",     \"country_code\": \"US\",     \"first_ecom_category_id\": \"\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"list\": [         {           \"comment\": 3449,           \"cost\": 477000,           \"cover_url\": null,           \"cpa\": 9.21,           \"ctr\": 1.29,           \"cvr\": 12.94,           \"ecom_type\": \"l3\",           \"first_ecom_category\": {             \"id\": \"601450\",             \"label\": \"category_601450\",             \"value\": \"Beauty & Personal Care\"           },           \"impression\": 65000000,           \"like\": 166618,           \"play_six_rate\": 7.62,           \"post\": 10600,           \"post_change\": -10.16,           \"second_ecom_category\": {             \"id\": \"848648\",             \"label\": \"category_848648\",             \"parent_id\": \"601450\",             \"value\": \"Makeup & Perfume\"           },           \"share\": 2359,           \"third_ecom_category\": {             \"id\": \"601583\",             \"label\": \"category_601583\",             \"parent_id\": \"848648\",             \"value\": \"Perfume\"           },           \"url_title\": \"Perfume\"         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 156,         \"has_more\": true       }     }   } } ```  # [English] ### Purpose: - Get top product rankings in TikTok ads to understand popular products in various categories - Analyze core metrics like ad post volume, CTR, and conversion rate for products - Help e-commerce sellers discover potential products and optimize product selection and marketing strategies  ### Parameters: - last: Number of recent days, e.g., 7, 30 days - page: Page number, default 1 - limit: Items per page, default 20 - country_code: Country code, e.g., US, UK, JP - first_ecom_category_id: E-commerce category IDs, multiple separated by commas - ecom_type: E-commerce type, default \"l3\" - period_type: Period type, default \"last\" - order_by: Sort field, options: post (post volume), ctr (click-through rate), cvr (conversion rate) - order_type: Sort order, desc (descending) or asc (ascending)  ### Common E-commerce Category IDs: - Beauty & Personal Care: 605196 - Women's Clothing & Underwear: 602284 - Fashion Accessories: 601450 - Mobile & Electronics: 801928 - Health Products: 951432 - Home & Living: 601755 - Men's Clothing & Underwear: 605248 - Perfume: 601583  ### Return Description: - `list`: Product list   - `comment`: Comment count   - `cost`: Cost amount   - `cover_url`: Cover image URL (may be null)   - `cpa`: Cost per acquisition   - `ctr`: Click-through rate (percentage)   - `cvr`: Conversion rate (percentage)   - `ecom_type`: E-commerce type   - `first_ecom_category`: First-level e-commerce category     - `id`: Category ID     - `label`: Category label     - `value`: Category name   - `impression`: Impression count   - `like`: Like count   - `play_six_rate`: 6-second play rate (percentage)   - `post`: Post volume   - `post_change`: Post volume change rate (percentage)   - `second_ecom_category`: Second-level e-commerce category     - `id`: Category ID     - `label`: Category label     - `parent_id`: Parent category ID     - `value`: Category name   - `share`: Share count   - `third_ecom_category`: Third-level e-commerce category     - `id`: Category ID     - `label`: Category label     - `parent_id`: Parent category ID     - `value`: Category name   - `url_title`: URL title - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/get_top_products\",   \"params\": {     \"last\": \"7\",     \"page\": \"1\",     \"limit\": \"20\",     \"country_code\": \"US\",     \"first_ecom_category_id\": \"\",     \"ecom_type\": \"l3\",     \"period_type\": \"last\",     \"order_by\": \"post\",     \"order_type\": \"desc\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"list\": [         {           \"comment\": 3449,           \"cost\": 477000,           \"cover_url\": null,           \"cpa\": 9.21,           \"ctr\": 1.29,           \"cvr\": 12.94,           \"ecom_type\": \"l3\",           \"first_ecom_category\": {             \"id\": \"601450\",             \"label\": \"category_601450\",             \"value\": \"Beauty & Personal Care\"           },           \"impression\": 65000000,           \"like\": 166618,           \"play_six_rate\": 7.62,           \"post\": 10600,           \"post_change\": -10.16,           \"second_ecom_category\": {             \"id\": \"848648\",             \"label\": \"category_848648\",             \"parent_id\": \"601450\",             \"value\": \"Makeup & Perfume\"           },           \"share\": 2359,           \"third_ecom_category\": {             \"id\": \"601583\",             \"label\": \"category_601583\",             \"parent_id\": \"848648\",             \"value\": \"Perfume\"           },           \"url_title\": \"Perfume\"         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 156,         \"has_more\": true       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_top_products_api_v1_tiktok_ads_get_top_products_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object last: 最近天数/Last days
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object country_code: 国家代码/Country code
        :param object first_ecom_category_id: 电商类目ID，多个用逗号分隔/E-commerce category IDs, comma separated
        :param object ecom_type: 电商类型/E-commerce type (l3)
        :param object period_type: 时间类型/Period type (last)
        :param object order_by: 排序字段/Sort field (post, ctr, cvr)
        :param object order_type: 排序方式/Sort order (desc, asc)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['last', 'page', 'limit', 'country_code', 'first_ecom_category_id', 'ecom_type', 'period_type', 'order_by', 'order_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_top_products_api_v1_tiktok_ads_get_top_products_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'last' in params:
            query_params.append(('last', params['last']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'first_ecom_category_id' in params:
            query_params.append(('first_ecom_category_id', params['first_ecom_category_id']))  # noqa: E501
        if 'ecom_type' in params:
            query_params.append(('ecom_type', params['ecom_type']))  # noqa: E501
        if 'period_type' in params:
            query_params.append(('period_type', params['period_type']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'order_type' in params:
            query_params.append(('order_type', params['order_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/get_top_products', 'GET',
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

    def search_ads_api_v1_tiktok_ads_search_ads_get(self, **kwargs):  # noqa: E501
        """搜索广告/Search ads  # noqa: E501

        # [中文] ### 用途: - 搜索TikTok广告创意库中的广告，支持多维度筛选和排序 - 发现特定行业、关键词或目标相关的高效广告案例 - 为广告策划和创意制作提供参考和灵感  ### 参数: - keyword: 搜索关键词，可选参数，留空返回所有广告 - objective: 广告目标，1=全部 - like: 点赞数筛选，1=全部 - period: 时间范围（天），如7、30、120、180天 - industry: 行业ID列表，多个ID用逗号分隔。完整行业ID列表见: https://github.com/TikHub/TikTok-Ads-Industry-Code - page: 页码，默认1 - limit: 每页数量，默认20，最大50 - order_by: 排序方式，\"for_you\"=为你推荐，\"likes\"=按点赞数排序 - country_code: 国家代码，如US、UK、JP等 - ad_format: 广告格式，1=视频广告 - ad_language: 广告语言代码，如en、zh等  ### 常用行业ID示例: - 游戏: 27000000000 - 电子商务: 19000000000 - 金融服务: 30000000000 - 教育: 10000000000 - 美妆个护: 22000000000 - 食品饮料: 16000000000  ### 返回内容说明: - `materials`: 广告素材列表   - `id`: 广告素材ID   - `aweme_id`: 广告视频ID   - `desc`: 广告描述   - `create_time`: 创建时间   - `video_info`: 视频信息     - `cover`: 封面图URL     - `duration`: 时长（秒）   - `statistics`: 统计数据     - `digg_count`: 点赞数     - `comment_count`: 评论数     - `share_count`: 分享数   - `ads_info`: 广告信息     - `advertiser_name`: 广告主名称     - `landing_page`: 落地页URL - `pagination`: 分页信息   - `page`: 当前页   - `limit`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_ads\",   \"params\": {     \"keyword\": \"cat toy\",     \"period\": 180,     \"industry\": \"27000000000\",     \"page\": 1,     \"limit\": 20   },   \"data\": {     \"materials\": [       {         \"id\": \"7213258221116751874\",         \"aweme_id\": \"7213258221116751874\",         \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",         \"create_time\": 1680234567,         \"video_info\": {           \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",           \"duration\": 15         },         \"statistics\": {           \"digg_count\": 128456,           \"comment_count\": 3421,           \"share_count\": 892         },         \"ads_info\": {           \"advertiser_name\": \"PetToys Inc.\",           \"landing_page\": \"https://example.com/cat-toys\"         }       }     ],     \"pagination\": {       \"page\": 1,       \"limit\": 20,       \"total\": 1523,       \"has_more\": true     }   } } ```  # [English] ### Purpose: - Search ads in TikTok's Creative Center with multi-dimensional filtering and sorting - Discover effective ad cases related to specific industries, keywords, or objectives - Provide reference and inspiration for ad planning and creative production  ### Parameters: - keyword: Search keyword, optional, returns all ads if empty - objective: Ad objective, 1=All - like: Like count filter, 1=All - period: Time period in days, e.g., 7, 30, 120, 180 days - industry: Industry ID list, multiple IDs separated by commas. Full industry ID list: https://github.com/TikHub/TikTok-Ads-Industry-Code - page: Page number, default 1 - limit: Items per page, default 20, max 50 - order_by: Sort method, \"for_you\"=Recommended, \"likes\"=Sort by likes - country_code: Country code, e.g., US, UK, JP - ad_format: Ad format, 1=Video ads - ad_language: Ad language code, e.g., en, zh  ### Common Industry ID Examples: - Games: 27000000000 - E-commerce: 19000000000 - Financial Services: 30000000000 - Education: 10000000000 - Beauty & Personal Care: 22000000000 - Food & Beverage: 16000000000  ### Return Description: - `materials`: List of ad materials   - `id`: Ad material ID   - `aweme_id`: Ad video ID   - `desc`: Ad description   - `create_time`: Creation time   - `video_info`: Video information     - `cover`: Cover image URL     - `duration`: Duration in seconds   - `statistics`: Statistics     - `digg_count`: Number of likes     - `comment_count`: Number of comments     - `share_count`: Number of shares   - `ads_info`: Ad information     - `advertiser_name`: Advertiser name     - `landing_page`: Landing page URL - `pagination`: Pagination info   - `page`: Current page   - `limit`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_ads\",   \"params\": {     \"keyword\": \"cat toy\",     \"period\": 180,     \"industry\": \"27000000000\",     \"page\": 1,     \"limit\": 20   },   \"data\": {     \"materials\": [       {         \"id\": \"7213258221116751874\",         \"aweme_id\": \"7213258221116751874\",         \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",         \"create_time\": 1680234567,         \"video_info\": {           \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",           \"duration\": 15         },         \"statistics\": {           \"digg_count\": 128456,           \"comment_count\": 3421,           \"share_count\": 892         },         \"ads_info\": {           \"advertiser_name\": \"PetToys Inc.\",           \"landing_page\": \"https://example.com/cat-toys\"         }       }     ],     \"pagination\": {       \"page\": 1,       \"limit\": 20,       \"total\": 1523,       \"has_more\": true     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_ads_api_v1_tiktok_ads_search_ads_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object objective: 广告目标类型/Ad objective (1:流量 2:应用安装 3:转化 4:视频浏览 5:触达 6:潜在客户 7:产品销售)
        :param object like: 表现排名/Performance rank (1:前1-20% 2:前21-40% 3:前41-60% 4:前61-80%)
        :param object period: 时间段/Time period (days)
        :param object industry: 行业ID/Industry ID
        :param object keyword: 搜索关键词/Search keyword
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object order_by: 排序方式/Sort by (for_you, likes)
        :param object country_code: 国家代码/Country code
        :param object ad_format: 广告格式/Ad format (1:视频)
        :param object ad_language: 广告语言/Ad language
        :param object search_id: 搜索ID（可选）/Search ID (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_ads_api_v1_tiktok_ads_search_ads_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_ads_api_v1_tiktok_ads_search_ads_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_ads_api_v1_tiktok_ads_search_ads_get_with_http_info(self, **kwargs):  # noqa: E501
        """搜索广告/Search ads  # noqa: E501

        # [中文] ### 用途: - 搜索TikTok广告创意库中的广告，支持多维度筛选和排序 - 发现特定行业、关键词或目标相关的高效广告案例 - 为广告策划和创意制作提供参考和灵感  ### 参数: - keyword: 搜索关键词，可选参数，留空返回所有广告 - objective: 广告目标，1=全部 - like: 点赞数筛选，1=全部 - period: 时间范围（天），如7、30、120、180天 - industry: 行业ID列表，多个ID用逗号分隔。完整行业ID列表见: https://github.com/TikHub/TikTok-Ads-Industry-Code - page: 页码，默认1 - limit: 每页数量，默认20，最大50 - order_by: 排序方式，\"for_you\"=为你推荐，\"likes\"=按点赞数排序 - country_code: 国家代码，如US、UK、JP等 - ad_format: 广告格式，1=视频广告 - ad_language: 广告语言代码，如en、zh等  ### 常用行业ID示例: - 游戏: 27000000000 - 电子商务: 19000000000 - 金融服务: 30000000000 - 教育: 10000000000 - 美妆个护: 22000000000 - 食品饮料: 16000000000  ### 返回内容说明: - `materials`: 广告素材列表   - `id`: 广告素材ID   - `aweme_id`: 广告视频ID   - `desc`: 广告描述   - `create_time`: 创建时间   - `video_info`: 视频信息     - `cover`: 封面图URL     - `duration`: 时长（秒）   - `statistics`: 统计数据     - `digg_count`: 点赞数     - `comment_count`: 评论数     - `share_count`: 分享数   - `ads_info`: 广告信息     - `advertiser_name`: 广告主名称     - `landing_page`: 落地页URL - `pagination`: 分页信息   - `page`: 当前页   - `limit`: 每页数量   - `total`: 总数量   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_ads\",   \"params\": {     \"keyword\": \"cat toy\",     \"period\": 180,     \"industry\": \"27000000000\",     \"page\": 1,     \"limit\": 20   },   \"data\": {     \"materials\": [       {         \"id\": \"7213258221116751874\",         \"aweme_id\": \"7213258221116751874\",         \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",         \"create_time\": 1680234567,         \"video_info\": {           \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",           \"duration\": 15         },         \"statistics\": {           \"digg_count\": 128456,           \"comment_count\": 3421,           \"share_count\": 892         },         \"ads_info\": {           \"advertiser_name\": \"PetToys Inc.\",           \"landing_page\": \"https://example.com/cat-toys\"         }       }     ],     \"pagination\": {       \"page\": 1,       \"limit\": 20,       \"total\": 1523,       \"has_more\": true     }   } } ```  # [English] ### Purpose: - Search ads in TikTok's Creative Center with multi-dimensional filtering and sorting - Discover effective ad cases related to specific industries, keywords, or objectives - Provide reference and inspiration for ad planning and creative production  ### Parameters: - keyword: Search keyword, optional, returns all ads if empty - objective: Ad objective, 1=All - like: Like count filter, 1=All - period: Time period in days, e.g., 7, 30, 120, 180 days - industry: Industry ID list, multiple IDs separated by commas. Full industry ID list: https://github.com/TikHub/TikTok-Ads-Industry-Code - page: Page number, default 1 - limit: Items per page, default 20, max 50 - order_by: Sort method, \"for_you\"=Recommended, \"likes\"=Sort by likes - country_code: Country code, e.g., US, UK, JP - ad_format: Ad format, 1=Video ads - ad_language: Ad language code, e.g., en, zh  ### Common Industry ID Examples: - Games: 27000000000 - E-commerce: 19000000000 - Financial Services: 30000000000 - Education: 10000000000 - Beauty & Personal Care: 22000000000 - Food & Beverage: 16000000000  ### Return Description: - `materials`: List of ad materials   - `id`: Ad material ID   - `aweme_id`: Ad video ID   - `desc`: Ad description   - `create_time`: Creation time   - `video_info`: Video information     - `cover`: Cover image URL     - `duration`: Duration in seconds   - `statistics`: Statistics     - `digg_count`: Number of likes     - `comment_count`: Number of comments     - `share_count`: Number of shares   - `ads_info`: Ad information     - `advertiser_name`: Advertiser name     - `landing_page`: Landing page URL - `pagination`: Pagination info   - `page`: Current page   - `limit`: Items per page   - `total`: Total count   - `has_more`: Whether there are more items  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_ads\",   \"params\": {     \"keyword\": \"cat toy\",     \"period\": 180,     \"industry\": \"27000000000\",     \"page\": 1,     \"limit\": 20   },   \"data\": {     \"materials\": [       {         \"id\": \"7213258221116751874\",         \"aweme_id\": \"7213258221116751874\",         \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",         \"create_time\": 1680234567,         \"video_info\": {           \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",           \"duration\": 15         },         \"statistics\": {           \"digg_count\": 128456,           \"comment_count\": 3421,           \"share_count\": 892         },         \"ads_info\": {           \"advertiser_name\": \"PetToys Inc.\",           \"landing_page\": \"https://example.com/cat-toys\"         }       }     ],     \"pagination\": {       \"page\": 1,       \"limit\": 20,       \"total\": 1523,       \"has_more\": true     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_ads_api_v1_tiktok_ads_search_ads_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object objective: 广告目标类型/Ad objective (1:流量 2:应用安装 3:转化 4:视频浏览 5:触达 6:潜在客户 7:产品销售)
        :param object like: 表现排名/Performance rank (1:前1-20% 2:前21-40% 3:前41-60% 4:前61-80%)
        :param object period: 时间段/Time period (days)
        :param object industry: 行业ID/Industry ID
        :param object keyword: 搜索关键词/Search keyword
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object order_by: 排序方式/Sort by (for_you, likes)
        :param object country_code: 国家代码/Country code
        :param object ad_format: 广告格式/Ad format (1:视频)
        :param object ad_language: 广告语言/Ad language
        :param object search_id: 搜索ID（可选）/Search ID (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['objective', 'like', 'period', 'industry', 'keyword', 'page', 'limit', 'order_by', 'country_code', 'ad_format', 'ad_language', 'search_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_ads_api_v1_tiktok_ads_search_ads_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'objective' in params:
            query_params.append(('objective', params['objective']))  # noqa: E501
        if 'like' in params:
            query_params.append(('like', params['like']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'industry' in params:
            query_params.append(('industry', params['industry']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'ad_format' in params:
            query_params.append(('ad_format', params['ad_format']))  # noqa: E501
        if 'ad_language' in params:
            query_params.append(('ad_language', params['ad_language']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/search_ads', 'GET',
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

    def search_creators_api_v1_tiktok_ads_search_creators_get(self, keyword, **kwargs):  # noqa: E501
        """搜索创作者/Search creators  # noqa: E501

        # [中文] ### 用途: - 通过关键词搜索创作者 - 快速找到特定领域或名称的创作者 - 支持按粉丝数或平均观看量排序  ### 参数: - keyword: 搜索关键词，可以是用户名、昵称的一部分 - page: 页码，默认1 - limit: 每页数量，默认20 - sort_by: 排序方式   - follower: 按粉丝数排序   - avg_views: 按平均观看量排序 - creator_country: 创作者所在国家  ### 返回内容说明: - `creators`: 创作者列表   - `tcm_id`: 创作者市场ID   - `user_id`: 用户ID   - `nick_name`: 昵称   - `avatar_url`: 头像URL   - `country_code`: 国家代码   - `follower_cnt`: 粉丝数   - `liked_cnt`: 总点赞数   - `tt_link`: TikTok个人主页链接   - `tcm_link`: 创作者市场链接   - `items`: 作品列表     - `item_id`: 作品ID     - `cover_url`: 封面URL     - `tt_link`: 作品链接     - `vv`: 观看量     - `liked_cnt`: 点赞数     - `create_time`: 创建时间戳 - `pagination`: 分页信息   - `page`: 当前页码   - `size`: 每页数量   - `total`: 总数   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_creators\",   \"params\": {     \"keyword\": \"jo\",     \"page\": \"1\",     \"limit\": \"20\",     \"sort_by\": \"follower\",     \"creator_country\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"6894787532572065797\",           \"user_id\": \"6684747467718820870\",           \"nick_name\": \"Josh Zilberberg\",           \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",           \"country_code\": \"US\",           \"follower_cnt\": 3048368,           \"liked_cnt\": 130131619,           \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",           \"items\": [             {               \"item_id\": \"7406005139112283397\",               \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",               \"vv\": 3266905,               \"liked_cnt\": 4057,               \"create_time\": 1724344950             }           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 6,         \"has_more\": false       }     }   } } ```  # [English] ### Purpose: - Search creators by keyword - Quickly find creators in specific fields or with specific names - Support sorting by follower count or average views  ### Parameters: - keyword: Search keyword, can be part of username or nickname - page: Page number, default 1 - limit: Items per page, default 20 - sort_by: Sorting method   - follower: Sort by follower count   - avg_views: Sort by average views - creator_country: Creator's country  ### Return Description: - `creators`: Creator list   - `tcm_id`: TikTok Creator Marketplace ID   - `user_id`: User ID   - `nick_name`: Nickname   - `avatar_url`: Avatar URL   - `country_code`: Country code   - `follower_cnt`: Follower count   - `liked_cnt`: Total likes count   - `tt_link`: TikTok profile link   - `tcm_link`: Creator marketplace link   - `items`: Video list     - `item_id`: Video ID     - `cover_url`: Cover image URL     - `tt_link`: Video link     - `vv`: View count     - `liked_cnt`: Like count     - `create_time`: Creation timestamp - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Has more pages  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_creators\",   \"params\": {     \"keyword\": \"jo\",     \"page\": \"1\",     \"limit\": \"20\",     \"sort_by\": \"follower\",     \"creator_country\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"6894787532572065797\",           \"user_id\": \"6684747467718820870\",           \"nick_name\": \"Josh Zilberberg\",           \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",           \"country_code\": \"US\",           \"follower_cnt\": 3048368,           \"liked_cnt\": 130131619,           \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",           \"items\": [             {               \"item_id\": \"7406005139112283397\",               \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",               \"vv\": 3266905,               \"liked_cnt\": 4057,               \"create_time\": 1724344950             }           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 6,         \"has_more\": false       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_creators_api_v1_tiktok_ads_search_creators_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object sort_by: 排序方式/Sort by (follower, avg_views)
        :param object creator_country: 创作者国家/Creator country
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_creators_api_v1_tiktok_ads_search_creators_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_creators_api_v1_tiktok_ads_search_creators_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_creators_api_v1_tiktok_ads_search_creators_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索创作者/Search creators  # noqa: E501

        # [中文] ### 用途: - 通过关键词搜索创作者 - 快速找到特定领域或名称的创作者 - 支持按粉丝数或平均观看量排序  ### 参数: - keyword: 搜索关键词，可以是用户名、昵称的一部分 - page: 页码，默认1 - limit: 每页数量，默认20 - sort_by: 排序方式   - follower: 按粉丝数排序   - avg_views: 按平均观看量排序 - creator_country: 创作者所在国家  ### 返回内容说明: - `creators`: 创作者列表   - `tcm_id`: 创作者市场ID   - `user_id`: 用户ID   - `nick_name`: 昵称   - `avatar_url`: 头像URL   - `country_code`: 国家代码   - `follower_cnt`: 粉丝数   - `liked_cnt`: 总点赞数   - `tt_link`: TikTok个人主页链接   - `tcm_link`: 创作者市场链接   - `items`: 作品列表     - `item_id`: 作品ID     - `cover_url`: 封面URL     - `tt_link`: 作品链接     - `vv`: 观看量     - `liked_cnt`: 点赞数     - `create_time`: 创建时间戳 - `pagination`: 分页信息   - `page`: 当前页码   - `size`: 每页数量   - `total`: 总数   - `has_more`: 是否有更多  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_creators\",   \"params\": {     \"keyword\": \"jo\",     \"page\": \"1\",     \"limit\": \"20\",     \"sort_by\": \"follower\",     \"creator_country\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"6894787532572065797\",           \"user_id\": \"6684747467718820870\",           \"nick_name\": \"Josh Zilberberg\",           \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",           \"country_code\": \"US\",           \"follower_cnt\": 3048368,           \"liked_cnt\": 130131619,           \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",           \"items\": [             {               \"item_id\": \"7406005139112283397\",               \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",               \"vv\": 3266905,               \"liked_cnt\": 4057,               \"create_time\": 1724344950             }           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 6,         \"has_more\": false       }     }   } } ```  # [English] ### Purpose: - Search creators by keyword - Quickly find creators in specific fields or with specific names - Support sorting by follower count or average views  ### Parameters: - keyword: Search keyword, can be part of username or nickname - page: Page number, default 1 - limit: Items per page, default 20 - sort_by: Sorting method   - follower: Sort by follower count   - avg_views: Sort by average views - creator_country: Creator's country  ### Return Description: - `creators`: Creator list   - `tcm_id`: TikTok Creator Marketplace ID   - `user_id`: User ID   - `nick_name`: Nickname   - `avatar_url`: Avatar URL   - `country_code`: Country code   - `follower_cnt`: Follower count   - `liked_cnt`: Total likes count   - `tt_link`: TikTok profile link   - `tcm_link`: Creator marketplace link   - `items`: Video list     - `item_id`: Video ID     - `cover_url`: Cover image URL     - `tt_link`: Video link     - `vv`: View count     - `liked_cnt`: Like count     - `create_time`: Creation timestamp - `pagination`: Pagination info   - `page`: Current page   - `size`: Items per page   - `total`: Total count   - `has_more`: Has more pages  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_creators\",   \"params\": {     \"keyword\": \"jo\",     \"page\": \"1\",     \"limit\": \"20\",     \"sort_by\": \"follower\",     \"creator_country\": \"US\"   },   \"data\": {     \"code\": 0,     \"msg\": \"OK\",     \"data\": {       \"creators\": [         {           \"tcm_id\": \"6894787532572065797\",           \"user_id\": \"6684747467718820870\",           \"nick_name\": \"Josh Zilberberg\",           \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",           \"country_code\": \"US\",           \"follower_cnt\": 3048368,           \"liked_cnt\": 130131619,           \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",           \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",           \"items\": [             {               \"item_id\": \"7406005139112283397\",               \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",               \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",               \"vv\": 3266905,               \"liked_cnt\": 4057,               \"create_time\": 1724344950             }           ]         }       ],       \"pagination\": {         \"page\": 1,         \"size\": 20,         \"total\": 6,         \"has_more\": false       }     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_creators_api_v1_tiktok_ads_search_creators_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object sort_by: 排序方式/Sort by (follower, avg_views)
        :param object creator_country: 创作者国家/Creator country
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page', 'limit', 'sort_by', 'creator_country']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_creators_api_v1_tiktok_ads_search_creators_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_creators_api_v1_tiktok_ads_search_creators_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'creator_country' in params:
            query_params.append(('creator_country', params['creator_country']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/search_creators', 'GET',
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

    def search_sound_api_v1_tiktok_ads_search_sound_get(self, keyword, **kwargs):  # noqa: E501
        """搜索音乐/Search sounds  # noqa: E501

        # [中文] ### 用途: - 搜索符合条件的音乐列表 - 支持按关键词、热度、商业类型等多维度筛选 - 为广告配乐选择提供全面的搜索功能  ### 参数: - keyword: 搜索关键词 - period: 时间范围（天），如7、30、120天 - page: 页码，默认1 - limit: 每页数量，默认20 - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快 - new_on_board: 是否只看新上榜音乐 - commercial_music: 是否只看商业音乐 - country_code: 国家代码  ### 返回内容说明: - `sound_list`: 音乐列表   - `id`: 音乐ID   - `title`: 音乐标题   - `author`: 音乐作者   - `duration`: 时长（秒）   - `trend`: 趋势数据   - `related_items`: 使用该音乐的视频数量   - `is_commercial`: 是否商业音乐 - `pagination`: 分页信息  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_sound\",   \"params\": {     \"keyword\": \"taylor swift\",     \"period\": 7,     \"page\": 1   },   \"data\": {     \"sound_list\": [       {         \"id\": \"7156826385225353217\",         \"title\": \"Karma\",         \"author\": \"Taylor Swift\",         \"duration\": 30,         \"trend\": [           {\"time\": 1746000000, \"value\": 15000}         ],         \"related_items\": 5678,         \"is_commercial\": true       }     ],     \"pagination\": {       \"page\": 1,       \"size\": 20,       \"total\": 156,       \"has_more\": true     }   } } ```  # [English] ### Purpose: - Search for music lists matching criteria - Support multi-dimensional filtering by keyword, popularity, commercial type, etc. - Provide comprehensive search functionality for ad soundtrack selection  ### Parameters: - keyword: Search keyword - period: Time period in days, e.g., 7, 30, 120 days - page: Page number, default 1 - limit: Items per page, default 20 - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising - new_on_board: Only show newly trending music - commercial_music: Only show commercial music - country_code: Country code  ### Return Description: - `sound_list`: Music list   - `id`: Music ID   - `title`: Music title   - `author`: Music author   - `duration`: Duration in seconds   - `trend`: Trend data   - `related_items`: Number of videos using this music   - `is_commercial`: Whether commercial music - `pagination`: Pagination info  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_sound\",   \"params\": {     \"keyword\": \"taylor swift\",     \"period\": 7,     \"page\": 1   },   \"data\": {     \"sound_list\": [       {         \"id\": \"7156826385225353217\",         \"title\": \"Karma\",         \"author\": \"Taylor Swift\",         \"duration\": 30,         \"trend\": [           {\"time\": 1746000000, \"value\": 15000}         ],         \"related_items\": 5678,         \"is_commercial\": true       }     ],     \"pagination\": {       \"page\": 1,       \"size\": 20,       \"total\": 156,       \"has_more\": true     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_sound_api_v1_tiktok_ads_search_sound_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object period: 时间范围（天）/Time period (days)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object rank_type: 排行类型/Rank type (popular, surging)
        :param object new_on_board: 是否只看新上榜/Only new on board
        :param object commercial_music: 是否商业音乐/Commercial music only
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_sound_api_v1_tiktok_ads_search_sound_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_sound_api_v1_tiktok_ads_search_sound_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_sound_api_v1_tiktok_ads_search_sound_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索音乐/Search sounds  # noqa: E501

        # [中文] ### 用途: - 搜索符合条件的音乐列表 - 支持按关键词、热度、商业类型等多维度筛选 - 为广告配乐选择提供全面的搜索功能  ### 参数: - keyword: 搜索关键词 - period: 时间范围（天），如7、30、120天 - page: 页码，默认1 - limit: 每页数量，默认20 - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快 - new_on_board: 是否只看新上榜音乐 - commercial_music: 是否只看商业音乐 - country_code: 国家代码  ### 返回内容说明: - `sound_list`: 音乐列表   - `id`: 音乐ID   - `title`: 音乐标题   - `author`: 音乐作者   - `duration`: 时长（秒）   - `trend`: 趋势数据   - `related_items`: 使用该音乐的视频数量   - `is_commercial`: 是否商业音乐 - `pagination`: 分页信息  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_sound\",   \"params\": {     \"keyword\": \"taylor swift\",     \"period\": 7,     \"page\": 1   },   \"data\": {     \"sound_list\": [       {         \"id\": \"7156826385225353217\",         \"title\": \"Karma\",         \"author\": \"Taylor Swift\",         \"duration\": 30,         \"trend\": [           {\"time\": 1746000000, \"value\": 15000}         ],         \"related_items\": 5678,         \"is_commercial\": true       }     ],     \"pagination\": {       \"page\": 1,       \"size\": 20,       \"total\": 156,       \"has_more\": true     }   } } ```  # [English] ### Purpose: - Search for music lists matching criteria - Support multi-dimensional filtering by keyword, popularity, commercial type, etc. - Provide comprehensive search functionality for ad soundtrack selection  ### Parameters: - keyword: Search keyword - period: Time period in days, e.g., 7, 30, 120 days - page: Page number, default 1 - limit: Items per page, default 20 - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising - new_on_board: Only show newly trending music - commercial_music: Only show commercial music - country_code: Country code  ### Return Description: - `sound_list`: Music list   - `id`: Music ID   - `title`: Music title   - `author`: Music author   - `duration`: Duration in seconds   - `trend`: Trend data   - `related_items`: Number of videos using this music   - `is_commercial`: Whether commercial music - `pagination`: Pagination info  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_sound\",   \"params\": {     \"keyword\": \"taylor swift\",     \"period\": 7,     \"page\": 1   },   \"data\": {     \"sound_list\": [       {         \"id\": \"7156826385225353217\",         \"title\": \"Karma\",         \"author\": \"Taylor Swift\",         \"duration\": 30,         \"trend\": [           {\"time\": 1746000000, \"value\": 15000}         ],         \"related_items\": 5678,         \"is_commercial\": true       }     ],     \"pagination\": {       \"page\": 1,       \"size\": 20,       \"total\": 156,       \"has_more\": true     }   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_sound_api_v1_tiktok_ads_search_sound_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object period: 时间范围（天）/Time period (days)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object rank_type: 排行类型/Rank type (popular, surging)
        :param object new_on_board: 是否只看新上榜/Only new on board
        :param object commercial_music: 是否商业音乐/Commercial music only
        :param object country_code: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'period', 'page', 'limit', 'rank_type', 'new_on_board', 'commercial_music', 'country_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_sound_api_v1_tiktok_ads_search_sound_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_sound_api_v1_tiktok_ads_search_sound_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'rank_type' in params:
            query_params.append(('rank_type', params['rank_type']))  # noqa: E501
        if 'new_on_board' in params:
            query_params.append(('new_on_board', params['new_on_board']))  # noqa: E501
        if 'commercial_music' in params:
            query_params.append(('commercial_music', params['commercial_music']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/search_sound', 'GET',
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

    def search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get(self, keyword, **kwargs):  # noqa: E501
        """搜索音乐提示/Search sound hints  # noqa: E501

        # [中文] ### 用途: - 获取音乐搜索的自动完成提示和推荐 - 帮助用户快速找到相关音乐 - 提供搜索建议优化音乐选择  ### 参数: - keyword: 搜索关键词 - period: 时间范围（天） - page: 页码，默认1 - limit: 每页数量，默认5 - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快 - country_code: 国家代码 - filter_by_checked: 是否只看已验证音乐 - commercial_music: 是否只看商业音乐  ### 返回内容说明: - `sound_list`: 音乐提示列表   - `title`: 音乐标题   - `author`: 音乐作者   - `match_type`: 匹配类型（标题/作者/标签）   - `popularity`: 热度评分  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",   \"params\": {     \"keyword\": \"taylor swift\",     \"limit\": 5   },   \"data\": {     \"sound_list\": [       {         \"title\": \"Anti-Hero\",         \"author\": \"Taylor Swift\",         \"match_type\": \"artist\",         \"popularity\": 98       },       {         \"title\": \"Blank Space\",         \"author\": \"Taylor Swift\",         \"match_type\": \"artist\",         \"popularity\": 95       }     ]   } } ```  # [English] ### Purpose: - Get auto-complete hints and recommendations for music search - Help users quickly find relevant music - Provide search suggestions to optimize music selection  ### Parameters: - keyword: Search keyword - period: Time period in days - page: Page number, default 1 - limit: Items per page, default 5 - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising - country_code: Country code - filter_by_checked: Only show verified music - commercial_music: Only show commercial music  ### Return Description: - `sound_list`: Music hint list   - `title`: Music title   - `author`: Music author   - `match_type`: Match type (title/artist/tag)   - `popularity`: Popularity score  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",   \"params\": {     \"keyword\": \"taylor swift\",     \"limit\": 5   },   \"data\": {     \"sound_list\": [       {         \"title\": \"Anti-Hero\",         \"author\": \"Taylor Swift\",         \"match_type\": \"artist\",         \"popularity\": 98       },       {         \"title\": \"Blank Space\",         \"author\": \"Taylor Swift\",         \"match_type\": \"artist\",         \"popularity\": 95       }     ]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object period: 时间范围（天）/Time period (days)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object rank_type: 排行类型/Rank type (popular, surging)
        :param object country_code: 国家代码/Country code
        :param object filter_by_checked: 是否只看已验证/Only verified
        :param object commercial_music: 是否商业音乐/Commercial music only
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索音乐提示/Search sound hints  # noqa: E501

        # [中文] ### 用途: - 获取音乐搜索的自动完成提示和推荐 - 帮助用户快速找到相关音乐 - 提供搜索建议优化音乐选择  ### 参数: - keyword: 搜索关键词 - period: 时间范围（天） - page: 页码，默认1 - limit: 每页数量，默认5 - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快 - country_code: 国家代码 - filter_by_checked: 是否只看已验证音乐 - commercial_music: 是否只看商业音乐  ### 返回内容说明: - `sound_list`: 音乐提示列表   - `title`: 音乐标题   - `author`: 音乐作者   - `match_type`: 匹配类型（标题/作者/标签）   - `popularity`: 热度评分  ### 示例响应: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",   \"params\": {     \"keyword\": \"taylor swift\",     \"limit\": 5   },   \"data\": {     \"sound_list\": [       {         \"title\": \"Anti-Hero\",         \"author\": \"Taylor Swift\",         \"match_type\": \"artist\",         \"popularity\": 98       },       {         \"title\": \"Blank Space\",         \"author\": \"Taylor Swift\",         \"match_type\": \"artist\",         \"popularity\": 95       }     ]   } } ```  # [English] ### Purpose: - Get auto-complete hints and recommendations for music search - Help users quickly find relevant music - Provide search suggestions to optimize music selection  ### Parameters: - keyword: Search keyword - period: Time period in days - page: Page number, default 1 - limit: Items per page, default 5 - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising - country_code: Country code - filter_by_checked: Only show verified music - commercial_music: Only show commercial music  ### Return Description: - `sound_list`: Music hint list   - `title`: Music title   - `author`: Music author   - `match_type`: Match type (title/artist/tag)   - `popularity`: Popularity score  ### Example Response: ```json {   \"code\": 200,   \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",   \"params\": {     \"keyword\": \"taylor swift\",     \"limit\": 5   },   \"data\": {     \"sound_list\": [       {         \"title\": \"Anti-Hero\",         \"author\": \"Taylor Swift\",         \"match_type\": \"artist\",         \"popularity\": 98       },       {         \"title\": \"Blank Space\",         \"author\": \"Taylor Swift\",         \"match_type\": \"artist\",         \"popularity\": 95       }     ]   } } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object period: 时间范围（天）/Time period (days)
        :param object page: 页码/Page number
        :param object limit: 每页数量/Items per page
        :param object rank_type: 排行类型/Rank type (popular, surging)
        :param object country_code: 国家代码/Country code
        :param object filter_by_checked: 是否只看已验证/Only verified
        :param object commercial_music: 是否商业音乐/Commercial music only
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'period', 'page', 'limit', 'rank_type', 'country_code', 'filter_by_checked', 'commercial_music']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'rank_type' in params:
            query_params.append(('rank_type', params['rank_type']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'filter_by_checked' in params:
            query_params.append(('filter_by_checked', params['filter_by_checked']))  # noqa: E501
        if 'commercial_music' in params:
            query_params.append(('commercial_music', params['commercial_music']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/ads/search_sound_hint', 'GET',
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
