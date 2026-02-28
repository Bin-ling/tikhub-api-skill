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


class TikTokAppV3APIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get(self, aweme_type, item_id, **kwargs):  # noqa: E501
        """根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID  # noqa: E501

        # [中文] ### 用途: - 根据视频ID来增加作品的播放数 ### 参数: - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。 - item_id: 作品id，别名为aweme_id - invite_code: 邀请码，此接口需要邀请码才能使用。 ### 返回: - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。  # [English] ### Purpose: - Increase the number of plays of the work according to the video ID ### Parameters: - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data interface. - item_id: Video id, alias aweme_id - invite_code: Invite code, this interface requires an invite code to use. ### Return: - The current timestamp and status code. When the status code is 200, it means success, otherwise it is a failure. You can try to change another work id and call it again, or wait for a period of time and call it again.  # [示例/Example] aweme_type = 0 item_id = \"7419966340443819295\" cookie = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get(aweme_type, item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_type: 作品类型/Video type (required)
        :param object item_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get_with_http_info(aweme_type, item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get_with_http_info(aweme_type, item_id, **kwargs)  # noqa: E501
            return data

    def add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get_with_http_info(self, aweme_type, item_id, **kwargs):  # noqa: E501
        """根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID  # noqa: E501

        # [中文] ### 用途: - 根据视频ID来增加作品的播放数 ### 参数: - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。 - item_id: 作品id，别名为aweme_id - invite_code: 邀请码，此接口需要邀请码才能使用。 ### 返回: - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。  # [English] ### Purpose: - Increase the number of plays of the work according to the video ID ### Parameters: - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data interface. - item_id: Video id, alias aweme_id - invite_code: Invite code, this interface requires an invite code to use. ### Return: - The current timestamp and status code. When the status code is 200, it means success, otherwise it is a failure. You can try to change another work id and call it again, or wait for a period of time and call it again.  # [示例/Example] aweme_type = 0 item_id = \"7419966340443819295\" cookie = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get_with_http_info(aweme_type, item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_type: 作品类型/Video type (required)
        :param object item_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_type', 'item_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_type' is set
        if self.api_client.client_side_validation and ('aweme_type' not in params or
                                                       params['aweme_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_type` when calling `add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get`")  # noqa: E501
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_type' in params:
            query_params.append(('aweme_type', params['aweme_type']))  # noqa: E501
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/add_video_play_count', 'GET',
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

    def check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get(self, room_id, **kwargs):  # noqa: E501
        """检测直播间是否在线/Check if live room is online  # noqa: E501

        # [中文] ### 用途: - 检测直播间是否在线 - 直播间的Room ID可以通过直播间链接从`/api/v1/tiktok/web/get_live_room_id`接口获取 ### 参数: - room_id: 直播间id ### 返回: - 是否在线  # [English] ### Purpose: - Check if live room is online - The Room ID of the live room can be obtained from the `/api/v1/tiktok/web/get_live_room_id` interface through the live room link ### Parameters: - room_id: Live room id ### Return: - Whether online  # [示例/Example] room_id = \"7358603858249009962\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间id/Live room id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get_with_http_info(room_id, **kwargs)  # noqa: E501
        else:
            (data) = self.check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get_with_http_info(room_id, **kwargs)  # noqa: E501
            return data

    def check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get_with_http_info(self, room_id, **kwargs):  # noqa: E501
        """检测直播间是否在线/Check if live room is online  # noqa: E501

        # [中文] ### 用途: - 检测直播间是否在线 - 直播间的Room ID可以通过直播间链接从`/api/v1/tiktok/web/get_live_room_id`接口获取 ### 参数: - room_id: 直播间id ### 返回: - 是否在线  # [English] ### Purpose: - Check if live room is online - The Room ID of the live room can be obtained from the `/api/v1/tiktok/web/get_live_room_id` interface through the live room link ### Parameters: - room_id: Live room id ### Return: - Whether online  # [示例/Example] room_id = \"7358603858249009962\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get_with_http_info(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间id/Live room id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/check_live_room_online', 'GET',
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

    def check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post(self, **kwargs):  # noqa: E501
        """批量检测直播间是否在线/Batch check if live rooms are online  # noqa: E501

        # [中文] ### 用途: - 批量检测多个 TikTok 直播间是否在线，最大支持50个直播间ID - Room ID 可以通过 `/api/v1/tiktok/web/get_live_room_id` 获取 ### 参数: - room_ids: 多个直播间 ID 的数组 ### 返回: - 每个直播间的在线状态  # [English] ### Purpose: - Batch check TikTok live rooms' online status, supports up to 50 room IDs - Room IDs can be retrieved from `/api/v1/tiktok/web/get_live_room_id` ### Parameters: - room_ids: List of TikTok live room IDs ### Return: - Online status per room  # [示例/Example] ``` payload = {     \"room_ids\": [         \"7494491933781003054\",         \"7494514925034113835\"     ] } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post_with_http_info(self, **kwargs):  # noqa: E501
        """批量检测直播间是否在线/Batch check if live rooms are online  # noqa: E501

        # [中文] ### 用途: - 批量检测多个 TikTok 直播间是否在线，最大支持50个直播间ID - Room ID 可以通过 `/api/v1/tiktok/web/get_live_room_id` 获取 ### 参数: - room_ids: 多个直播间 ID 的数组 ### 返回: - 每个直播间的在线状态  # [English] ### Purpose: - Batch check TikTok live rooms' online status, supports up to 50 room IDs - Room IDs can be retrieved from `/api/v1/tiktok/web/get_live_room_id` ### Parameters: - room_ids: List of TikTok live room IDs ### Return: - Online status per room  # [示例/Example] ``` payload = {     \"room_ids\": [         \"7494491933781003054\",         \"7494514925034113835\"     ] } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post_with_http_info(async_req=True)
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
                    " to method check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post" % key
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
            '/api/v1/tiktok/app/v3/check_live_room_online_batch', 'POST',
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

    def encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post(self, **kwargs):  # noqa: E501
        """加密或解密 TikTok APP 登录请求体/Encrypt or Decrypt TikTok APP login request body  # noqa: E501

        # [中文] ### 用途: - 加密/解密 TikTok APP 登录请求体，用于登录接口的请求体加密和解密。 ### 参数: - username: 用户名，可以是密文或明文。 - password: 密码，可以是密文或明文。 - mode: 模式     - `encrypt`: 加密     - `decrypt`: 解密 ### 返回: - 加密/解密后的请求体  # [English] ### Purpose: - Encrypt/decrypt the TikTok APP login request body, used for encrypting and decrypting the request body of the login interface. ### Parameters: - username: Username, can be ciphertext or plaintext. - password: Password, can be ciphertext or plaintext. - mode: Mode     - `encrypt`: Encrypt     - `decrypt`: Decrypt ### Return: - Encrypted/decrypted request body  # [示例/Example] ```json {     \"username\": \"example_username\",     \"password\": \"example_password\",     \"mode\": \"encrypt\" } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post_with_http_info(self, **kwargs):  # noqa: E501
        """加密或解密 TikTok APP 登录请求体/Encrypt or Decrypt TikTok APP login request body  # noqa: E501

        # [中文] ### 用途: - 加密/解密 TikTok APP 登录请求体，用于登录接口的请求体加密和解密。 ### 参数: - username: 用户名，可以是密文或明文。 - password: 密码，可以是密文或明文。 - mode: 模式     - `encrypt`: 加密     - `decrypt`: 解密 ### 返回: - 加密/解密后的请求体  # [English] ### Purpose: - Encrypt/decrypt the TikTok APP login request body, used for encrypting and decrypting the request body of the login interface. ### Parameters: - username: Username, can be ciphertext or plaintext. - password: Password, can be ciphertext or plaintext. - mode: Mode     - `encrypt`: Encrypt     - `decrypt`: Decrypt ### Return: - Encrypted/decrypted request body  # [示例/Example] ```json {     \"username\": \"example_username\",     \"password\": \"example_password\",     \"mode\": \"encrypt\" } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post_with_http_info(async_req=True)
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
                    " to method encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post" % key
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
            '/api/v1/tiktok/app/v3/encrypt_decrypt_login_request', 'POST',
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

    def fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post(self, **kwargs):  # noqa: E501
        """获取内容翻译数据/Get content translation data  # noqa: E501

        # [中文] ### 用途: - 获取内容翻译数据 ### 参数: - trg_lang: 目标语言     - zh-Hans: 简体中文     - zh-Hant: 繁体中文     - en: 英语     - ja: 日语     - ko: 韩语     - fr: 法语     - de: 德语     - ru: 俄语     - es: 西班牙语     - pt: 葡萄牙语     - vi: 越南语     - th: 泰语     - id: 印尼语     - ar: 阿拉伯语     - it: 意大利语     - tr: 土耳其语     - he: 希伯来语     - pl: 波兰语     - nl: 荷兰语     - sv: 瑞典语     - da: 丹麦语     - fi: 芬兰语     - no: 挪威语     - cs: 捷克语     - hu: 匈牙利语 - src_content: 源内容，也就是需要翻译的内容，长度不超过5000个字符，如果超过5000个字符，只会翻译前5000个字符。 ### 返回: - 内容翻译数据  # [English] ### Purpose: - Get content translation data ### Parameters: - trg_lang: Target language     - zh-Hans: Simplified Chinese     - zh-Hant: Traditional Chinese     - en: English     - ja: Japanese     - ko: Korean     - fr: French     - de: German     - ru: Russian     - es: Spanish     - pt: Portuguese     - vi: Vietnamese     - th: Thai     - id: Indonesian     - ar: Arabic     - it: Italian     - tr: Turkish     - he: Hebrew     - pl: Polish     - nl: Dutch     - sv: Swedish     - da: Danish     - fi: Finnish     - no: Norwegian     - cs: Czech     - hu: Hungarian - src_content: Source content, that is, the content that needs to be translated, the length does not exceed 5000 characters, if it exceeds 5000 characters, only the first 5000 characters will be translated. ### Return: - Content translation data  # [示例/Example] trg_lang = \"zh-Hans\" src_content = \"Hello, welcome to TikHub!\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取内容翻译数据/Get content translation data  # noqa: E501

        # [中文] ### 用途: - 获取内容翻译数据 ### 参数: - trg_lang: 目标语言     - zh-Hans: 简体中文     - zh-Hant: 繁体中文     - en: 英语     - ja: 日语     - ko: 韩语     - fr: 法语     - de: 德语     - ru: 俄语     - es: 西班牙语     - pt: 葡萄牙语     - vi: 越南语     - th: 泰语     - id: 印尼语     - ar: 阿拉伯语     - it: 意大利语     - tr: 土耳其语     - he: 希伯来语     - pl: 波兰语     - nl: 荷兰语     - sv: 瑞典语     - da: 丹麦语     - fi: 芬兰语     - no: 挪威语     - cs: 捷克语     - hu: 匈牙利语 - src_content: 源内容，也就是需要翻译的内容，长度不超过5000个字符，如果超过5000个字符，只会翻译前5000个字符。 ### 返回: - 内容翻译数据  # [English] ### Purpose: - Get content translation data ### Parameters: - trg_lang: Target language     - zh-Hans: Simplified Chinese     - zh-Hant: Traditional Chinese     - en: English     - ja: Japanese     - ko: Korean     - fr: French     - de: German     - ru: Russian     - es: Spanish     - pt: Portuguese     - vi: Vietnamese     - th: Thai     - id: Indonesian     - ar: Arabic     - it: Italian     - tr: Turkish     - he: Hebrew     - pl: Polish     - nl: Dutch     - sv: Swedish     - da: Danish     - fi: Finnish     - no: Norwegian     - cs: Czech     - hu: Hungarian - src_content: Source content, that is, the content that needs to be translated, the length does not exceed 5000 characters, if it exceeds 5000 characters, only the first 5000 characters will be translated. ### Return: - Content translation data  # [示例/Example] trg_lang = \"zh-Hans\" src_content = \"Hello, welcome to TikHub!\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post_with_http_info(async_req=True)
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
                    " to method fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post" % key
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
            '/api/v1/tiktok/app/v3/fetch_content_translate', 'POST',
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

    def fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get(self, creator_uid, **kwargs):  # noqa: E501
        """获取带货创作者信息/Get shopping creator information  # noqa: E501

        # [中文] ### 用途: - 获取创作者信息，包括创作者的基本信息、粉丝数、橱窗商品数量、带货直播间等信息。 ### 参数: - creator_uid: 创作者uid ### 返回: - 创作者信息  # [English] ### Purpose: - Get creator information, including the creator's basic information, number of fans, number of storefront products, shop live room and other information. ### Parameters: - creator_uid: Creator uid ### Return: - Creator information  # [示例/Example] creator_uid = \"6555451606845243393\"  # [示例响应/Example Response] response = {     \"code\": 200,     \"request_id\": \"d5575d80-a8cc-44ab-a46a-b62c2e967829\",     \"router\": \"/api/v1/tiktok/app/v3/fetch_creator_info\",     \"params\": {         \"creator_uid\": \"6555451606845243393\"     },     \"data\": {         \"code\": 0,         \"data\": {             \"creator_info\": {                 \"creator_id\": \"6555451606845243393\",                 \"creator_name\": \"louissescarlettFamily's showcase\",                 \"avatar\": {                     \"uri\": \"720x720/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248\",                     \"url_list\": [                         \"https://p19-common-sign-sg.tiktokcdn-us.com/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248~tplv-tiktokx-cropcenter:720:720.webp?dr=9640&refresh_token=fd81a69e&x-expires=1756022400&x-signature=neQwNv%2BxfA4YPnLFb51270Zi8Ps%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=85ba3243&idc=useast5\",                         \"https://p16-common-sign-sg.tiktokcdn-us.com/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248~tplv-tiktokx-cropcenter:720:720.webp?dr=9640&refresh_token=723df957&x-expires=1756022400&x-signature=9q4A2SUIO%2B42lqTsrVkkpks54dI%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=85ba3243&idc=useast5\",                         \"https://p19-common-sign-sg.tiktokcdn-us.com/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=d63d422b&x-expires=1756022400&x-signature=sycMEH0640dpjl%2BK0nDy1ZPbtxs%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=85ba3243&idc=useast5\"                     ]                 },                 \"followers_info\": {                     \"count\": \"18017938\",                     \"count_info\": \"18.0M followers\",                     \"value\": 18017938,                     \"count_format\": \"18.0M\"                 },                 \"sold_count_info\": {                     \"count\": \"0\",                     \"value\": 0                 },                 \"bg_pic\": {                     \"uri\": \"tos-alisg-i-aphluv4xwc-sg/72edb551d7c77636678a5518cdddfd1c.jpg\",                     \"url_list\": [                         \"https://p19-oec-general.ttcdn-us.com/tos-alisg-i-aphluv4xwc-sg/72edb551d7c77636678a5518cdddfd1c.jpg~tplv-fhlh96nyum-resize-jpeg:1600:1600.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\",                         \"https://p16-oec-general.ttcdn-us.com/tos-alisg-i-aphluv4xwc-sg/72edb551d7c77636678a5518cdddfd1c.jpg~tplv-fhlh96nyum-resize-jpeg:1600:1600.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\"                     ]                 },                 \"is_banned\": false,                 \"sec_user_id\": \"MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux\",                 \"follow_status_extended\": 0,                 \"show_follow_button\": false,                 \"can_share\": false,                 \"show_commission_paid\": \"Creator earns commission\",                 \"product_count_info\": {                     \"count\": \"713\",                     \"count_info\": \"713 products\",                     \"value\": 713,                     \"count_format\": \"713\"                 },                 \"dark_bg_pic_new\": {                     \"uri\": \"tos-maliva-i-acgf4d7es9-us/showcase_header_v2_dark.png\",                     \"url_list\": [                         \"https://p16-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_dark.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\",                         \"https://p19-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_dark.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\"                     ]                 },                 \"light_bg_pic_new\": {                     \"uri\": \"tos-maliva-i-acgf4d7es9-us/showcase_header_v2_light.png\",                     \"url_list\": [                         \"https://p16-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_light.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\",                         \"https://p19-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_light.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\"                     ]                 },                 \"is_new_header\": true,                 \"dynamic_header\": {                     \"is_dynamic\": false,                     \"delay_time\": 0                 },                 \"extra_val\": {                     \"showcase_no_product_show_less_screen\": \"0\",                     \"us_uk_show_voucher_info\": \"0\"                 }             },             \"live_info\": {                 \"room_id\": \"7541231942331566853\",                 \"upcoming_event_time\": \"1756141200\"             },             \"diversion_module\": 0         },         \"message\": \"success\"     } }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get(creator_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object creator_uid: 创作者uid/Creator uid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get_with_http_info(creator_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get_with_http_info(creator_uid, **kwargs)  # noqa: E501
            return data

    def fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get_with_http_info(self, creator_uid, **kwargs):  # noqa: E501
        """获取带货创作者信息/Get shopping creator information  # noqa: E501

        # [中文] ### 用途: - 获取创作者信息，包括创作者的基本信息、粉丝数、橱窗商品数量、带货直播间等信息。 ### 参数: - creator_uid: 创作者uid ### 返回: - 创作者信息  # [English] ### Purpose: - Get creator information, including the creator's basic information, number of fans, number of storefront products, shop live room and other information. ### Parameters: - creator_uid: Creator uid ### Return: - Creator information  # [示例/Example] creator_uid = \"6555451606845243393\"  # [示例响应/Example Response] response = {     \"code\": 200,     \"request_id\": \"d5575d80-a8cc-44ab-a46a-b62c2e967829\",     \"router\": \"/api/v1/tiktok/app/v3/fetch_creator_info\",     \"params\": {         \"creator_uid\": \"6555451606845243393\"     },     \"data\": {         \"code\": 0,         \"data\": {             \"creator_info\": {                 \"creator_id\": \"6555451606845243393\",                 \"creator_name\": \"louissescarlettFamily's showcase\",                 \"avatar\": {                     \"uri\": \"720x720/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248\",                     \"url_list\": [                         \"https://p19-common-sign-sg.tiktokcdn-us.com/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248~tplv-tiktokx-cropcenter:720:720.webp?dr=9640&refresh_token=fd81a69e&x-expires=1756022400&x-signature=neQwNv%2BxfA4YPnLFb51270Zi8Ps%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=85ba3243&idc=useast5\",                         \"https://p16-common-sign-sg.tiktokcdn-us.com/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248~tplv-tiktokx-cropcenter:720:720.webp?dr=9640&refresh_token=723df957&x-expires=1756022400&x-signature=9q4A2SUIO%2B42lqTsrVkkpks54dI%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=85ba3243&idc=useast5\",                         \"https://p19-common-sign-sg.tiktokcdn-us.com/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=d63d422b&x-expires=1756022400&x-signature=sycMEH0640dpjl%2BK0nDy1ZPbtxs%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=85ba3243&idc=useast5\"                     ]                 },                 \"followers_info\": {                     \"count\": \"18017938\",                     \"count_info\": \"18.0M followers\",                     \"value\": 18017938,                     \"count_format\": \"18.0M\"                 },                 \"sold_count_info\": {                     \"count\": \"0\",                     \"value\": 0                 },                 \"bg_pic\": {                     \"uri\": \"tos-alisg-i-aphluv4xwc-sg/72edb551d7c77636678a5518cdddfd1c.jpg\",                     \"url_list\": [                         \"https://p19-oec-general.ttcdn-us.com/tos-alisg-i-aphluv4xwc-sg/72edb551d7c77636678a5518cdddfd1c.jpg~tplv-fhlh96nyum-resize-jpeg:1600:1600.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\",                         \"https://p16-oec-general.ttcdn-us.com/tos-alisg-i-aphluv4xwc-sg/72edb551d7c77636678a5518cdddfd1c.jpg~tplv-fhlh96nyum-resize-jpeg:1600:1600.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\"                     ]                 },                 \"is_banned\": false,                 \"sec_user_id\": \"MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux\",                 \"follow_status_extended\": 0,                 \"show_follow_button\": false,                 \"can_share\": false,                 \"show_commission_paid\": \"Creator earns commission\",                 \"product_count_info\": {                     \"count\": \"713\",                     \"count_info\": \"713 products\",                     \"value\": 713,                     \"count_format\": \"713\"                 },                 \"dark_bg_pic_new\": {                     \"uri\": \"tos-maliva-i-acgf4d7es9-us/showcase_header_v2_dark.png\",                     \"url_list\": [                         \"https://p16-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_dark.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\",                         \"https://p19-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_dark.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\"                     ]                 },                 \"light_bg_pic_new\": {                     \"uri\": \"tos-maliva-i-acgf4d7es9-us/showcase_header_v2_light.png\",                     \"url_list\": [                         \"https://p16-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_light.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\",                         \"https://p19-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_light.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398\"                     ]                 },                 \"is_new_header\": true,                 \"dynamic_header\": {                     \"is_dynamic\": false,                     \"delay_time\": 0                 },                 \"extra_val\": {                     \"showcase_no_product_show_less_screen\": \"0\",                     \"us_uk_show_voucher_info\": \"0\"                 }             },             \"live_info\": {                 \"room_id\": \"7541231942331566853\",                 \"upcoming_event_time\": \"1756141200\"             },             \"diversion_module\": 0         },         \"message\": \"success\"     } }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get_with_http_info(creator_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object creator_uid: 创作者uid/Creator uid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['creator_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'creator_uid' is set
        if self.api_client.client_side_validation and ('creator_uid' not in params or
                                                       params['creator_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `creator_uid` when calling `fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'creator_uid' in params:
            query_params.append(('creator_uid', params['creator_uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_creator_info', 'GET',
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

    def fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get(self, **kwargs):  # noqa: E501
        """创作者搜索洞察/Creator Search Insights  # noqa: E501

        # [中文] ### 用途: - 获取创作者搜索洞察数据，用于了解热门搜索趋势和创作灵感 ### 参数: - offset: 分页偏移量，默认0 - limit: 每页数量，默认20 - tab: 标签页类型，可选值:     - all: 全部     - content_gap: 内容差距     - follower_searched: 粉丝常搜     - life_style: 生活方式     - topics: 话题     - challenges: 挑战     - sounds: 声音     - hashtags: 标签 - language_filters: 语言过滤器，多个用逗号分隔，可选值: id, de, en, es, fr, pt, vi, tr, ar, th, ja, ko - category_filters: 分类过滤器，多个用逗号分隔，可选值: Gaming, Fashion, Tourism, Science, Food, Sports - creator_source: 创作者来源，默认 \"general_search\" - force_refresh: 是否强制刷新，默认 False ### 返回: - 创作者搜索洞察数据  # [English] ### Purpose: - Get creator search insights data, used to understand trending search topics and creative inspiration ### Parameters: - offset: Pagination offset, default 0 - limit: Number per page, default 20 - tab: Tab type, options:     - all: All     - content_gap: Content gap     - follower_searched: Follower searched     - life_style: Life style     - topics: Topics     - challenges: Challenges     - sounds: Sounds     - hashtags: Hashtags - language_filters: Language filters, separated by comma, options: id, de, en, es, fr, pt, vi, tr, ar, th, ja, ko - category_filters: Category filters, separated by comma, options: Gaming, Fashion, Tourism, Science, Food, Sports - creator_source: Creator source, default \"general_search\" - force_refresh: Force refresh, default False ### Return: - Creator search insights data  # [示例/Example] offset = 0 limit = 20 tab = \"all\" language_filters = \"en\" category_filters = \"Gaming\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object offset: 分页偏移量/Pagination offset
        :param object limit: 每页数量/Number per page
        :param object tab: 标签页类型/Tab type (all/content_gap/follower_searched/life_style/topics/challenges/sounds/hashtags)
        :param object language_filters: 语言过滤器，多个用逗号分隔/Language filters (id/de/en/es/fr/pt/vi/tr/ar/th/ja/ko)
        :param object category_filters: 分类过滤器，多个用逗号分隔/Category filters (Gaming/Fashion/Tourism/Science/Food/Sports)
        :param object creator_source: 创作者来源/Creator source
        :param object force_refresh: 是否强制刷新/Force refresh
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get_with_http_info(self, **kwargs):  # noqa: E501
        """创作者搜索洞察/Creator Search Insights  # noqa: E501

        # [中文] ### 用途: - 获取创作者搜索洞察数据，用于了解热门搜索趋势和创作灵感 ### 参数: - offset: 分页偏移量，默认0 - limit: 每页数量，默认20 - tab: 标签页类型，可选值:     - all: 全部     - content_gap: 内容差距     - follower_searched: 粉丝常搜     - life_style: 生活方式     - topics: 话题     - challenges: 挑战     - sounds: 声音     - hashtags: 标签 - language_filters: 语言过滤器，多个用逗号分隔，可选值: id, de, en, es, fr, pt, vi, tr, ar, th, ja, ko - category_filters: 分类过滤器，多个用逗号分隔，可选值: Gaming, Fashion, Tourism, Science, Food, Sports - creator_source: 创作者来源，默认 \"general_search\" - force_refresh: 是否强制刷新，默认 False ### 返回: - 创作者搜索洞察数据  # [English] ### Purpose: - Get creator search insights data, used to understand trending search topics and creative inspiration ### Parameters: - offset: Pagination offset, default 0 - limit: Number per page, default 20 - tab: Tab type, options:     - all: All     - content_gap: Content gap     - follower_searched: Follower searched     - life_style: Life style     - topics: Topics     - challenges: Challenges     - sounds: Sounds     - hashtags: Hashtags - language_filters: Language filters, separated by comma, options: id, de, en, es, fr, pt, vi, tr, ar, th, ja, ko - category_filters: Category filters, separated by comma, options: Gaming, Fashion, Tourism, Science, Food, Sports - creator_source: Creator source, default \"general_search\" - force_refresh: Force refresh, default False ### Return: - Creator search insights data  # [示例/Example] offset = 0 limit = 20 tab = \"all\" language_filters = \"en\" category_filters = \"Gaming\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object offset: 分页偏移量/Pagination offset
        :param object limit: 每页数量/Number per page
        :param object tab: 标签页类型/Tab type (all/content_gap/follower_searched/life_style/topics/challenges/sounds/hashtags)
        :param object language_filters: 语言过滤器，多个用逗号分隔/Language filters (id/de/en/es/fr/pt/vi/tr/ar/th/ja/ko)
        :param object category_filters: 分类过滤器，多个用逗号分隔/Category filters (Gaming/Fashion/Tourism/Science/Food/Sports)
        :param object creator_source: 创作者来源/Creator source
        :param object force_refresh: 是否强制刷新/Force refresh
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'tab', 'language_filters', 'category_filters', 'creator_source', 'force_refresh']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'tab' in params:
            query_params.append(('tab', params['tab']))  # noqa: E501
        if 'language_filters' in params:
            query_params.append(('language_filters', params['language_filters']))  # noqa: E501
        if 'category_filters' in params:
            query_params.append(('category_filters', params['category_filters']))  # noqa: E501
        if 'creator_source' in params:
            query_params.append(('creator_source', params['creator_source']))  # noqa: E501
        if 'force_refresh' in params:
            query_params.append(('force_refresh', params['force_refresh']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_creator_search_insights', 'GET',
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

    def fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get(self, query_id_str, **kwargs):  # noqa: E501
        """创作者搜索洞察详情/Creator Search Insights Detail  # noqa: E501

        # [中文] ### 用途: - 获取创作者搜索洞察详情数据，用于查询特定搜索词条的搜索统计数据 ### 参数: - query_id_str: 搜索词条ID，从 fetch_creator_search_insights 接口返回的数据中获取 - time_range: 时间范围，可选值:     - past_7_days: 过去7天     - past_30_days: 过去30天（默认）     - past_60_days: 过去60天     - past_6_months: 过去6个月     - custom: 自定义时间（需配合 start_date 和 end_date 使用，不能超过6个月） - start_date: 开始时间戳（秒），仅当 time_range=custom 时生效 - end_date: 结束时间戳（秒），仅当 time_range=custom 时生效 - dimension_list: 维度列表，多个用逗号分隔，可选值: gender（性别）, age（年龄）, country（国家） ### 返回: - 搜索洞察详情数据，包含搜索趋势、用户画像等  # [English] ### Purpose: - Get creator search insights detail data, used to query search statistics for specific query ### Parameters: - query_id_str: Query ID, obtained from fetch_creator_search_insights response - time_range: Time range, options:     - past_7_days: Past 7 days     - past_30_days: Past 30 days (default)     - past_60_days: Past 60 days     - past_6_months: Past 6 months     - custom: Custom range (requires start_date and end_date, cannot exceed 6 months) - start_date: Start timestamp (seconds), only for custom range - end_date: End timestamp (seconds), only for custom range - dimension_list: Dimension list, separated by comma, options: gender, age, country ### Return: - Search insights detail data, including search trends, user demographics, etc.  # [示例/Example] query_id_str = \"122991006\" time_range = \"past_30_days\" dimension_list = \"gender,age,country\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get(query_id_str, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query_id_str: 搜索词条ID，从 fetch_creator_search_insights 接口获取/Query ID from fetch_creator_search_insights (required)
        :param object time_range: 时间范围/Time range (past_7_days/past_30_days/past_60_days/past_6_months/custom)
        :param object start_date: 开始时间戳（秒），仅当 time_range=custom 时生效/Start timestamp (seconds), only for custom range
        :param object end_date: 结束时间戳（秒），仅当 time_range=custom 时生效/End timestamp (seconds), only for custom range
        :param object dimension_list: 维度列表，多个用逗号分隔/Dimension list (gender/age/country)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get_with_http_info(query_id_str, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get_with_http_info(query_id_str, **kwargs)  # noqa: E501
            return data

    def fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get_with_http_info(self, query_id_str, **kwargs):  # noqa: E501
        """创作者搜索洞察详情/Creator Search Insights Detail  # noqa: E501

        # [中文] ### 用途: - 获取创作者搜索洞察详情数据，用于查询特定搜索词条的搜索统计数据 ### 参数: - query_id_str: 搜索词条ID，从 fetch_creator_search_insights 接口返回的数据中获取 - time_range: 时间范围，可选值:     - past_7_days: 过去7天     - past_30_days: 过去30天（默认）     - past_60_days: 过去60天     - past_6_months: 过去6个月     - custom: 自定义时间（需配合 start_date 和 end_date 使用，不能超过6个月） - start_date: 开始时间戳（秒），仅当 time_range=custom 时生效 - end_date: 结束时间戳（秒），仅当 time_range=custom 时生效 - dimension_list: 维度列表，多个用逗号分隔，可选值: gender（性别）, age（年龄）, country（国家） ### 返回: - 搜索洞察详情数据，包含搜索趋势、用户画像等  # [English] ### Purpose: - Get creator search insights detail data, used to query search statistics for specific query ### Parameters: - query_id_str: Query ID, obtained from fetch_creator_search_insights response - time_range: Time range, options:     - past_7_days: Past 7 days     - past_30_days: Past 30 days (default)     - past_60_days: Past 60 days     - past_6_months: Past 6 months     - custom: Custom range (requires start_date and end_date, cannot exceed 6 months) - start_date: Start timestamp (seconds), only for custom range - end_date: End timestamp (seconds), only for custom range - dimension_list: Dimension list, separated by comma, options: gender, age, country ### Return: - Search insights detail data, including search trends, user demographics, etc.  # [示例/Example] query_id_str = \"122991006\" time_range = \"past_30_days\" dimension_list = \"gender,age,country\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get_with_http_info(query_id_str, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query_id_str: 搜索词条ID，从 fetch_creator_search_insights 接口获取/Query ID from fetch_creator_search_insights (required)
        :param object time_range: 时间范围/Time range (past_7_days/past_30_days/past_60_days/past_6_months/custom)
        :param object start_date: 开始时间戳（秒），仅当 time_range=custom 时生效/Start timestamp (seconds), only for custom range
        :param object end_date: 结束时间戳（秒），仅当 time_range=custom 时生效/End timestamp (seconds), only for custom range
        :param object dimension_list: 维度列表，多个用逗号分隔/Dimension list (gender/age/country)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id_str', 'time_range', 'start_date', 'end_date', 'dimension_list']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id_str' is set
        if self.api_client.client_side_validation and ('query_id_str' not in params or
                                                       params['query_id_str'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query_id_str` when calling `fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query_id_str' in params:
            query_params.append(('query_id_str', params['query_id_str']))  # noqa: E501
        if 'time_range' in params:
            query_params.append(('time_range', params['time_range']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'dimension_list' in params:
            query_params.append(('dimension_list', params['dimension_list']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_creator_search_insights_detail', 'GET',
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

    def fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get(self, query_id_str, **kwargs):  # noqa: E501
        """创作者搜索洞察趋势/Creator Search Insights Trend  # noqa: E501

        # [中文] ### 用途: - 获取创作者搜索洞察趋势数据，包含地区和时间维度的搜索热度 ### 参数: - query_id_str: 搜索词条ID，从 fetch_creator_search_insights 接口返回的数据中获取 - from_tab_path: 来源标签路径，默认 \"TRENDING,TOPICS\" - query_analysis_required: 是否需要查询分析，默认 True ### 返回: - 搜索趋势数据，包含地区热度、时间趋势等  # [English] ### Purpose: - Get creator search insights trend data, including search popularity by region and time ### Parameters: - query_id_str: Query ID, obtained from fetch_creator_search_insights response - from_tab_path: From tab path, default \"TRENDING,TOPICS\" - query_analysis_required: Whether query analysis is required, default True ### Return: - Search trend data, including regional popularity, time trends, etc.  # [示例/Example] query_id_str = \"7555720035176562699\" from_tab_path = \"TRENDING,TOPICS\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get(query_id_str, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query_id_str: 搜索词条ID，从 fetch_creator_search_insights 接口获取/Query ID from fetch_creator_search_insights (required)
        :param object from_tab_path: 来源标签路径/From tab path
        :param object query_analysis_required: 是否需要查询分析/Whether query analysis is required
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get_with_http_info(query_id_str, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get_with_http_info(query_id_str, **kwargs)  # noqa: E501
            return data

    def fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get_with_http_info(self, query_id_str, **kwargs):  # noqa: E501
        """创作者搜索洞察趋势/Creator Search Insights Trend  # noqa: E501

        # [中文] ### 用途: - 获取创作者搜索洞察趋势数据，包含地区和时间维度的搜索热度 ### 参数: - query_id_str: 搜索词条ID，从 fetch_creator_search_insights 接口返回的数据中获取 - from_tab_path: 来源标签路径，默认 \"TRENDING,TOPICS\" - query_analysis_required: 是否需要查询分析，默认 True ### 返回: - 搜索趋势数据，包含地区热度、时间趋势等  # [English] ### Purpose: - Get creator search insights trend data, including search popularity by region and time ### Parameters: - query_id_str: Query ID, obtained from fetch_creator_search_insights response - from_tab_path: From tab path, default \"TRENDING,TOPICS\" - query_analysis_required: Whether query analysis is required, default True ### Return: - Search trend data, including regional popularity, time trends, etc.  # [示例/Example] query_id_str = \"7555720035176562699\" from_tab_path = \"TRENDING,TOPICS\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get_with_http_info(query_id_str, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query_id_str: 搜索词条ID，从 fetch_creator_search_insights 接口获取/Query ID from fetch_creator_search_insights (required)
        :param object from_tab_path: 来源标签路径/From tab path
        :param object query_analysis_required: 是否需要查询分析/Whether query analysis is required
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id_str', 'from_tab_path', 'query_analysis_required']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id_str' is set
        if self.api_client.client_side_validation and ('query_id_str' not in params or
                                                       params['query_id_str'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query_id_str` when calling `fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query_id_str' in params:
            query_params.append(('query_id_str', params['query_id_str']))  # noqa: E501
        if 'from_tab_path' in params:
            query_params.append(('from_tab_path', params['from_tab_path']))  # noqa: E501
        if 'query_analysis_required' in params:
            query_params.append(('query_analysis_required', params['query_analysis_required']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_creator_search_insights_trend', 'GET',
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

    def fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get(self, keyword, **kwargs):  # noqa: E501
        """创作者搜索洞察相关视频/Creator Search Insights Videos  # noqa: E501

        # [中文] ### 用途: - 获取创作者搜索洞察相关视频，查询该搜索词条下比较火的相关视频 ### 参数: - keyword: 搜索关键词，从 fetch_creator_search_insights 或 fetch_creator_search_insights_trend 接口获取 - offset: 分页偏移量，默认0 - count: 每页数量，默认20 ### 返回: - 相关热门视频列表  # [English] ### Purpose: - Get creator search insights related videos, query popular related videos for the search term ### Parameters: - keyword: Search keyword, obtained from fetch_creator_search_insights or fetch_creator_search_insights_trend - offset: Pagination offset, default 0 - count: Number per page, default 20 ### Return: - Related popular videos list  # [示例/Example] keyword = \"headshots 2 2 3\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object offset: 分页偏移量/Pagination offset
        :param object count: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """创作者搜索洞察相关视频/Creator Search Insights Videos  # noqa: E501

        # [中文] ### 用途: - 获取创作者搜索洞察相关视频，查询该搜索词条下比较火的相关视频 ### 参数: - keyword: 搜索关键词，从 fetch_creator_search_insights 或 fetch_creator_search_insights_trend 接口获取 - offset: 分页偏移量，默认0 - count: 每页数量，默认20 ### 返回: - 相关热门视频列表  # [English] ### Purpose: - Get creator search insights related videos, query popular related videos for the search term ### Parameters: - keyword: Search keyword, obtained from fetch_creator_search_insights or fetch_creator_search_insights_trend - offset: Pagination offset, default 0 - count: Number per page, default 20 ### Return: - Related popular videos list  # [示例/Example] keyword = \"headshots 2 2 3\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object offset: 分页偏移量/Pagination offset
        :param object count: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_creator_search_insights_videos', 'GET',
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

    def fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get(self, kol_id, **kwargs):  # noqa: E501
        """获取创作者橱窗商品列表/Get creator showcase product list  # noqa: E501

        # [中文] ### 用途: - 获取创作者橱窗商品列表 ### 参数: - kol_id: 创作者的sec_user_id - count: 数量 - next_scroll_param: 翻页参数，第一页为空字符串，后续请求使用上一次请求返回的next_scroll_param值。 ### 返回: - 创作者橱窗商品列表  # [English] ### Purpose: - Get creator showcase product list ### Parameters: - kol_id: Creator's sec_user_id - count: Number - next_scroll_param: Page parameter, empty string for the first page, use the next_scroll_param value returned by the last request for subsequent requests. ### Return: - Creator showcase product list  # [示例/Example] kol_id = \"MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux\" count = 20 next_scroll_param = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 创作者的sec_user_id/Creator's sec_user_id (required)
        :param object count: 数量/Number
        :param object next_scroll_param: 翻页参数/Page parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get_with_http_info(kol_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get_with_http_info(kol_id, **kwargs)  # noqa: E501
            return data

    def fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get_with_http_info(self, kol_id, **kwargs):  # noqa: E501
        """获取创作者橱窗商品列表/Get creator showcase product list  # noqa: E501

        # [中文] ### 用途: - 获取创作者橱窗商品列表 ### 参数: - kol_id: 创作者的sec_user_id - count: 数量 - next_scroll_param: 翻页参数，第一页为空字符串，后续请求使用上一次请求返回的next_scroll_param值。 ### 返回: - 创作者橱窗商品列表  # [English] ### Purpose: - Get creator showcase product list ### Parameters: - kol_id: Creator's sec_user_id - count: Number - next_scroll_param: Page parameter, empty string for the first page, use the next_scroll_param value returned by the last request for subsequent requests. ### Return: - Creator showcase product list  # [示例/Example] kol_id = \"MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux\" count = 20 next_scroll_param = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get_with_http_info(kol_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object kol_id: 创作者的sec_user_id/Creator's sec_user_id (required)
        :param object count: 数量/Number
        :param object next_scroll_param: 翻页参数/Page parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kol_id', 'count', 'next_scroll_param']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kol_id' is set
        if self.api_client.client_side_validation and ('kol_id' not in params or
                                                       params['kol_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `kol_id` when calling `fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kol_id' in params:
            query_params.append(('kol_id', params['kol_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'next_scroll_param' in params:
            query_params.append(('next_scroll_param', params['next_scroll_param']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_creator_showcase_product_list', 'GET',
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

    def fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的综合搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 - sort_type: 0-相关度，1-最多点赞 - publish_time: 0-不限制，1-最近一天，7-最近一周，30-最近一个月，90-最近三个月，180-最近半年 ### 返回: - 综合搜索结果  # [English] ### Purpose: - Get comprehensive search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset - count: Number - sort_type: 0-Relatedness, 1-Most likes - publish_time: 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year ### Return: - Comprehensive search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = 0 publish_time = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的综合搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 - sort_type: 0-相关度，1-最多点赞 - publish_time: 0-不限制，1-最近一天，7-最近一周，30-最近一个月，90-最近三个月，180-最近半年 ### 返回: - 综合搜索结果  # [English] ### Purpose: - Get comprehensive search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset - count: Number - sort_type: 0-Relatedness, 1-Most likes - publish_time: 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year ### Return: - Comprehensive search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = 0 publish_time = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'sort_type', 'publish_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'publish_time' in params:
            query_params.append(('publish_time', params['publish_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_general_search_result', 'GET',
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

    def fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get(self, ch_id, **kwargs):  # noqa: E501
        """获取指定话题的详情数据/Get details of specified hashtag  # noqa: E501

        # [中文] ### 用途: - 获取指定话题的详情数据 ### 参数: - ch_id: 话题id ### 返回: - 话题详情数据  # [English] ### Purpose: - Get details of specified hashtag ### Parameters: - ch_id: Hashtag id ### Return: - Hashtag details data  # [示例/Example] ch_id = \"7551\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get(ch_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ch_id: 话题id/Hashtag id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get_with_http_info(ch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get_with_http_info(ch_id, **kwargs)  # noqa: E501
            return data

    def fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get_with_http_info(self, ch_id, **kwargs):  # noqa: E501
        """获取指定话题的详情数据/Get details of specified hashtag  # noqa: E501

        # [中文] ### 用途: - 获取指定话题的详情数据 ### 参数: - ch_id: 话题id ### 返回: - 话题详情数据  # [English] ### Purpose: - Get details of specified hashtag ### Parameters: - ch_id: Hashtag id ### Return: - Hashtag details data  # [示例/Example] ch_id = \"7551\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get_with_http_info(ch_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ch_id: 话题id/Hashtag id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ch_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ch_id' is set
        if self.api_client.client_side_validation and ('ch_id' not in params or
                                                       params['ch_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ch_id` when calling `fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ch_id' in params:
            query_params.append(('ch_id', params['ch_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_hashtag_detail', 'GET',
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

    def fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的话题搜索结果/Get hashtag search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的话题搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 ### 返回: - 话题搜索结果  # [English] ### Purpose: - Get hashtag search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset - count: Number ### Return: - Hashtag search results  # [示例/Example] keyword = \"Cat\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的话题搜索结果/Get hashtag search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的话题搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 ### 返回: - 话题搜索结果  # [English] ### Purpose: - Get hashtag search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset - count: Number ### Return: - Hashtag search results  # [示例/Example] keyword = \"Cat\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_hashtag_search_result', 'GET',
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

    def fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get(self, ch_id, **kwargs):  # noqa: E501
        """获取指定话题的作品数据/Get video list of specified hashtag  # noqa: E501

        # [中文] ### 用途: - 获取指定话题的作品数据 ### 参数: - ch_id: 话题id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 ### 返回: - 话题作品数据  # [English] ### Purpose: - Get video list of specified hashtag ### Parameters: - ch_id: Hashtag id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number ### Return: - Hashtag video list data  # [示例/Example] ch_id = \"7551\" cursor = 0 sort_type = 0 count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get(ch_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ch_id: 话题id/Hashtag id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get_with_http_info(ch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get_with_http_info(ch_id, **kwargs)  # noqa: E501
            return data

    def fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get_with_http_info(self, ch_id, **kwargs):  # noqa: E501
        """获取指定话题的作品数据/Get video list of specified hashtag  # noqa: E501

        # [中文] ### 用途: - 获取指定话题的作品数据 ### 参数: - ch_id: 话题id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 ### 返回: - 话题作品数据  # [English] ### Purpose: - Get video list of specified hashtag ### Parameters: - ch_id: Hashtag id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number ### Return: - Hashtag video list data  # [示例/Example] ch_id = \"7551\" cursor = 0 sort_type = 0 count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get_with_http_info(ch_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ch_id: 话题id/Hashtag id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ch_id', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ch_id' is set
        if self.api_client.client_side_validation and ('ch_id' not in params or
                                                       params['ch_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ch_id` when calling `fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ch_id' in params:
            query_params.append(('ch_id', params['ch_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_hashtag_video_list', 'GET',
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

    def fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post(self, **kwargs):  # noqa: E501
        """获取主页视频推荐数据/Get home feed(recommend) video data  # noqa: E501

        # [中文] ### 用途: - 获取主页视频推荐数据 ### 参数: - cookie: 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。 ### 返回: - 视频推荐数据  # [English] ### Purpose: - Get home feed(recommend) video data ### Parameters: - cookie: User's own cookie, optional parameter, used for personalized recommendation of interface returned data. ### Return: - Video recommend data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取主页视频推荐数据/Get home feed(recommend) video data  # noqa: E501

        # [中文] ### 用途: - 获取主页视频推荐数据 ### 参数: - cookie: 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。 ### 返回: - 视频推荐数据  # [English] ### Purpose: - Get home feed(recommend) video data ### Parameters: - cookie: User's own cookie, optional parameter, used for personalized recommendation of interface returned data. ### Return: - Video recommend data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post_with_http_info(async_req=True)
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
                    " to method fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post" % key
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
            '/api/v1/tiktok/app/v3/fetch_home_feed', 'POST',
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

    def fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get(self, **kwargs):  # noqa: E501
        """获取直播每日榜单数据/Get live daily rank data  # noqa: E501

        # [中文] ### 用途: - 获取直播每日榜单数据 ### 参数: - anchor_id: 主播id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的主播id。 - room_id: 直播间id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的id。 - rank_type: 榜单类型，参数值如下表：      | type | rankName | 分组类型 | 说明 |     |------|----------|----------|------|     | 0 | `hourly_rank` | GIFT_RANK | 小时榜 |     | 1 | `weekly_rank` | GIFT_RANK | 周榜 |     | 5 | `rookie_star_rank` | GIFT_RANK | 新星榜 |     | 6 | `sale_rank` | E_COMMERCE | 带货榜 |     | 8 | `daily_rank` | GIFT_RANK | 日榜 |     | 10 | `weekly_game_rank` | GAME_RANK | 周游戏榜 |     | 11 | `daily_game_rank` | GAME_RANK | 日游戏榜 |     | 12 | `hall_of_fame_rank` | GIFT_RANK | 名人堂 |     | 13 | `champion_tournament` | GIFT_RANK | 冠军赛（含phase_one/two/three） |     | 14 | `daily_rookie_star_rank` | GIFT_RANK | 日新星榜 |     | 15 | `fans_team_rank` | GIFT_RANK | 粉丝团榜 |     | 16 | `ranking_league` | GIFT_RANK | 排位联赛（App内显示: D5段位榜） |     | 20 | `pubg` | GAME_RANK | PUBG游戏榜 |     | 21 | `mlbb` | GAME_RANK | MLBB游戏榜（Mobile Legends: Bang Bang） |     | 22 | `free_fire` | GAME_RANK | Free Fire游戏榜 |     | 23 | `sub_weekly_game_rank1` | GAME_RANK | 子周游戏榜1 |     | 24 | `sub_weekly_game_rank2` | GAME_RANK | 子周游戏榜2 |     | 25 | `sub_weekly_game_rank3` | GAME_RANK | 子周游戏榜3 |     | 26 | `collectibles` | E_COMMERCE | 收藏品榜 |     | 27 | `beauty` | E_COMMERCE | 美妆榜 |     | 28 | `women_wear` | E_COMMERCE | 女装榜 |     | 29 | `sale_rank_daily` | E_COMMERCE | 日带货榜 |     | 1001 | `league_campaign_rank` | GIFT_RANK | 联赛活动榜 |     | -1 | `unknown` | DEFAULT | 未知 |  - region_type: 地区类型，使用默认值即可，具体含义不明。 - gap_interval: 时间间隔，使用默认值代表当天，使用-1代表排名记录。 - cookie: 用户自己的cookie，可选参数，用于接口不可用时使用。 ### 返回: - 直播每日榜单数据  # [English] ### Purpose: - Get live daily rank data ### Parameters: - anchor_id: Anchor id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different anchor ids of different live rooms. - room_id: Live room id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different room ids of different live rooms. - rank_type: Rank type, parameter values are as follows:      | type | rankName | Group Type | Description |     |------|----------|------------|-------------|     | 0 | `hourly_rank` | GIFT_RANK | Hourly Rank |     | 1 | `weekly_rank` | GIFT_RANK | Weekly Rank |     | 5 | `rookie_star_rank` | GIFT_RANK | Rookie Star Rank |     | 6 | `sale_rank` | E_COMMERCE | Sale Rank |     | 8 | `daily_rank` | GIFT_RANK | Daily Rank |     | 10 | `weekly_game_rank` | GAME_RANK | Weekly Game Rank |     | 11 | `daily_game_rank` | GAME_RANK | Daily Game Rank |     | 12 | `hall_of_fame_rank` | GIFT_RANK | Hall of Fame Rank |     | 13 | `champion_tournament` | GIFT_RANK | Champion Tournament (includes phase_one/two/three) |     | 14 | `daily_rookie_star_rank` | GIFT_RANK | Daily Rookie Star Rank |     | 15 | `fans_team_rank` | GIFT_RANK | Fans Team Rank |     | 16 | `ranking_league` | GIFT_RANK | Ranking League (App display: D5 Level Rank) |     | 20 | `pubg` | GAME_RANK | PUBG Rank |     | 21 | `mlbb` | GAME_RANK | MLBB Rank (Mobile Legends: Bang Bang) |     | 22 | `free_fire` | GAME_RANK | Free Fire Rank |     | 23 | `sub_weekly_game_rank1` | GAME_RANK | Sub Weekly Game Rank 1 |     | 24 | `sub_weekly_game_rank2` | GAME_RANK | Sub Weekly Game Rank 2 |     | 25 | `sub_weekly_game_rank3` | GAME_RANK | Sub Weekly Game Rank 3 |     | 26 | `collectibles` | E_COMMERCE | Collectibles Rank |     | 27 | `beauty` | E_COMMERCE | Beauty Rank |     | 28 | `women_wear` | E_COMMERCE | Women Wear Rank |     | 29 | `sale_rank_daily` | E_COMMERCE | Daily Sale Rank |     | 1001 | `league_campaign_rank` | GIFT_RANK | League Campaign Rank |     | -1 | `unknown` | DEFAULT | Unknown |  - region_type: Region type, use the default value, the specific meaning is unknown. - gap_interval: Time interval, use the default value to represent the current day, use -1 to represent the ranking record. - cookie: User's own cookie, optional parameter, used when the interface is not available. ### Return: - Live daily rank data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object anchor_id: 主播id/Anchor id
        :param object room_id: 直播间id/Live room id
        :param object rank_type: 榜单类型/Rank type
        :param object region_type: 地区类型/Region type
        :param object gap_interval: 时间间隔/Time interval
        :param object cookie: 用户自己的cookie/User's own cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取直播每日榜单数据/Get live daily rank data  # noqa: E501

        # [中文] ### 用途: - 获取直播每日榜单数据 ### 参数: - anchor_id: 主播id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的主播id。 - room_id: 直播间id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的id。 - rank_type: 榜单类型，参数值如下表：      | type | rankName | 分组类型 | 说明 |     |------|----------|----------|------|     | 0 | `hourly_rank` | GIFT_RANK | 小时榜 |     | 1 | `weekly_rank` | GIFT_RANK | 周榜 |     | 5 | `rookie_star_rank` | GIFT_RANK | 新星榜 |     | 6 | `sale_rank` | E_COMMERCE | 带货榜 |     | 8 | `daily_rank` | GIFT_RANK | 日榜 |     | 10 | `weekly_game_rank` | GAME_RANK | 周游戏榜 |     | 11 | `daily_game_rank` | GAME_RANK | 日游戏榜 |     | 12 | `hall_of_fame_rank` | GIFT_RANK | 名人堂 |     | 13 | `champion_tournament` | GIFT_RANK | 冠军赛（含phase_one/two/three） |     | 14 | `daily_rookie_star_rank` | GIFT_RANK | 日新星榜 |     | 15 | `fans_team_rank` | GIFT_RANK | 粉丝团榜 |     | 16 | `ranking_league` | GIFT_RANK | 排位联赛（App内显示: D5段位榜） |     | 20 | `pubg` | GAME_RANK | PUBG游戏榜 |     | 21 | `mlbb` | GAME_RANK | MLBB游戏榜（Mobile Legends: Bang Bang） |     | 22 | `free_fire` | GAME_RANK | Free Fire游戏榜 |     | 23 | `sub_weekly_game_rank1` | GAME_RANK | 子周游戏榜1 |     | 24 | `sub_weekly_game_rank2` | GAME_RANK | 子周游戏榜2 |     | 25 | `sub_weekly_game_rank3` | GAME_RANK | 子周游戏榜3 |     | 26 | `collectibles` | E_COMMERCE | 收藏品榜 |     | 27 | `beauty` | E_COMMERCE | 美妆榜 |     | 28 | `women_wear` | E_COMMERCE | 女装榜 |     | 29 | `sale_rank_daily` | E_COMMERCE | 日带货榜 |     | 1001 | `league_campaign_rank` | GIFT_RANK | 联赛活动榜 |     | -1 | `unknown` | DEFAULT | 未知 |  - region_type: 地区类型，使用默认值即可，具体含义不明。 - gap_interval: 时间间隔，使用默认值代表当天，使用-1代表排名记录。 - cookie: 用户自己的cookie，可选参数，用于接口不可用时使用。 ### 返回: - 直播每日榜单数据  # [English] ### Purpose: - Get live daily rank data ### Parameters: - anchor_id: Anchor id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different anchor ids of different live rooms. - room_id: Live room id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different room ids of different live rooms. - rank_type: Rank type, parameter values are as follows:      | type | rankName | Group Type | Description |     |------|----------|------------|-------------|     | 0 | `hourly_rank` | GIFT_RANK | Hourly Rank |     | 1 | `weekly_rank` | GIFT_RANK | Weekly Rank |     | 5 | `rookie_star_rank` | GIFT_RANK | Rookie Star Rank |     | 6 | `sale_rank` | E_COMMERCE | Sale Rank |     | 8 | `daily_rank` | GIFT_RANK | Daily Rank |     | 10 | `weekly_game_rank` | GAME_RANK | Weekly Game Rank |     | 11 | `daily_game_rank` | GAME_RANK | Daily Game Rank |     | 12 | `hall_of_fame_rank` | GIFT_RANK | Hall of Fame Rank |     | 13 | `champion_tournament` | GIFT_RANK | Champion Tournament (includes phase_one/two/three) |     | 14 | `daily_rookie_star_rank` | GIFT_RANK | Daily Rookie Star Rank |     | 15 | `fans_team_rank` | GIFT_RANK | Fans Team Rank |     | 16 | `ranking_league` | GIFT_RANK | Ranking League (App display: D5 Level Rank) |     | 20 | `pubg` | GAME_RANK | PUBG Rank |     | 21 | `mlbb` | GAME_RANK | MLBB Rank (Mobile Legends: Bang Bang) |     | 22 | `free_fire` | GAME_RANK | Free Fire Rank |     | 23 | `sub_weekly_game_rank1` | GAME_RANK | Sub Weekly Game Rank 1 |     | 24 | `sub_weekly_game_rank2` | GAME_RANK | Sub Weekly Game Rank 2 |     | 25 | `sub_weekly_game_rank3` | GAME_RANK | Sub Weekly Game Rank 3 |     | 26 | `collectibles` | E_COMMERCE | Collectibles Rank |     | 27 | `beauty` | E_COMMERCE | Beauty Rank |     | 28 | `women_wear` | E_COMMERCE | Women Wear Rank |     | 29 | `sale_rank_daily` | E_COMMERCE | Daily Sale Rank |     | 1001 | `league_campaign_rank` | GIFT_RANK | League Campaign Rank |     | -1 | `unknown` | DEFAULT | Unknown |  - region_type: Region type, use the default value, the specific meaning is unknown. - gap_interval: Time interval, use the default value to represent the current day, use -1 to represent the ranking record. - cookie: User's own cookie, optional parameter, used when the interface is not available. ### Return: - Live daily rank data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object anchor_id: 主播id/Anchor id
        :param object room_id: 直播间id/Live room id
        :param object rank_type: 榜单类型/Rank type
        :param object region_type: 地区类型/Region type
        :param object gap_interval: 时间间隔/Time interval
        :param object cookie: 用户自己的cookie/User's own cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['anchor_id', 'room_id', 'rank_type', 'region_type', 'gap_interval', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'anchor_id' in params:
            query_params.append(('anchor_id', params['anchor_id']))  # noqa: E501
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501
        if 'rank_type' in params:
            query_params.append(('rank_type', params['rank_type']))  # noqa: E501
        if 'region_type' in params:
            query_params.append(('region_type', params['region_type']))  # noqa: E501
        if 'gap_interval' in params:
            query_params.append(('gap_interval', params['gap_interval']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_live_daily_rank', 'GET',
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

    def fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get(self, room_id, anchor_id, **kwargs):  # noqa: E501
        """获取直播间排行榜数据/Get live room ranking list  # noqa: E501

        # [中文] ### 用途: - 获取直播间内观众的排行榜数据 ### 参数: - room_id: 直播间id - anchor_id: 主播id ### 返回: - 排行榜数据  # [English] ### Purpose: - Get ranking list of audience in live room ### Parameters: - room_id: Live room id - anchor_id: Anchor id ### Return: - Ranking list data  # [示例/Example] room_id = \"7358603858249009962\" anchor_id = \"7222941468722758702\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get(room_id, anchor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间id/Live room id (required)
        :param object anchor_id: 主播id/Anchor id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get_with_http_info(room_id, anchor_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get_with_http_info(room_id, anchor_id, **kwargs)  # noqa: E501
            return data

    def fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get_with_http_info(self, room_id, anchor_id, **kwargs):  # noqa: E501
        """获取直播间排行榜数据/Get live room ranking list  # noqa: E501

        # [中文] ### 用途: - 获取直播间内观众的排行榜数据 ### 参数: - room_id: 直播间id - anchor_id: 主播id ### 返回: - 排行榜数据  # [English] ### Purpose: - Get ranking list of audience in live room ### Parameters: - room_id: Live room id - anchor_id: Anchor id ### Return: - Ranking list data  # [示例/Example] room_id = \"7358603858249009962\" anchor_id = \"7222941468722758702\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get_with_http_info(room_id, anchor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间id/Live room id (required)
        :param object anchor_id: 主播id/Anchor id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id', 'anchor_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get`")  # noqa: E501
        # verify the required parameter 'anchor_id' is set
        if self.api_client.client_side_validation and ('anchor_id' not in params or
                                                       params['anchor_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `anchor_id` when calling `fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501
        if 'anchor_id' in params:
            query_params.append(('anchor_id', params['anchor_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_live_ranking_list', 'GET',
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

    def fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get(self, room_id, **kwargs):  # noqa: E501
        """获取指定直播间的数据/Get data of specified live room  # noqa: E501

        # [中文] ### 用途: - 获取指定直播间的数据 ### 参数: - room_id: 直播间id ### 返回: - 直播间数据  # [English] ### Purpose: - Get data of specified live room ### Parameters: - room_id: Live room id ### Return: - Live room data  # [示例/Example] room_id = \"7385461256746060575\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间id/Live room id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get_with_http_info(room_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get_with_http_info(room_id, **kwargs)  # noqa: E501
            return data

    def fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get_with_http_info(self, room_id, **kwargs):  # noqa: E501
        """获取指定直播间的数据/Get data of specified live room  # noqa: E501

        # [中文] ### 用途: - 获取指定直播间的数据 ### 参数: - room_id: 直播间id ### 返回: - 直播间数据  # [English] ### Purpose: - Get data of specified live room ### Parameters: - room_id: Live room id ### Return: - Live room data  # [示例/Example] room_id = \"7385461256746060575\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get_with_http_info(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间id/Live room id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_live_room_info', 'GET',
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

    def fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get(self, room_id, author_id, **kwargs):  # noqa: E501
        """获取直播间商品列表数据/Get live room product list data  # noqa: E501

        # [中文] ### 用途: - 获取直播间商品列表数据 ### 参数: - room_id: 直播间id，必填参数。 - author_id: 主播id，必填参数。 - page_size: 每页数量，可选参数，默认为15。 - offset: 翻页游标，可选参数，默认为0，每次翻页增加15。 - region: 地区，可选参数，默认为`US`，如果使用其他地区，如：`VN`，请自行携带Cookie，否则无法获取数据。 - cookie: 用户自己的cookie，可选参数，用于爬取除`US`以外的地区数据。 ### 参数获取: - 第一步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"`接口获取直播间id（room_id）。 - 第二步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"`接口获取直播间信息。 - 第三步：使用第二步返回的JSON数据中使用JSONPATH获取`$.data.data.owner.id_str`字段的值作为主播id（author_id）。 ### 返回: - 直播间商品列表数据  # [English] ### Purpose: - Get live room product list data ### Parameters: - room_id: Live room id, required parameter. - author_id: Anchor id, required parameter. - page_size: Number per page, optional parameter, default is 15. - offset: Page turning cursor, optional parameter, default is 0, increasing by 15 each time. - region: Region, optional parameter, default is `US`, if you use other regions, such as: `VN`, please bring your own Cookie, otherwise you will not be able to get data. - cookie: User's own cookie, optional parameter, used to crawl data from regions other than `US`. ### Get Parameters: - Step 1: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"` to get the live room id (room_id). - Step 2: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"` to get the live room information. - Step 3: Use the JSONPATH in the JSON data returned in the second step to get the value of the field `$.data.data.owner.id_str` as the anchor id (author_id). ### Return: - Live room product list data  # [示例/Example] room_id = \"7420741353250507562\" author_id = \"7408859677050274859\" page_size = 15 offset = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get(room_id, author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间id/Live room id (required)
        :param object author_id: 主播id/Anchor id (required)
        :param object page_size: 数量/Number
        :param object offset: 数量/Number
        :param object region: 地区/Region
        :param object cookie: 用户自己的cookie/User's own cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get_with_http_info(room_id, author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get_with_http_info(room_id, author_id, **kwargs)  # noqa: E501
            return data

    def fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get_with_http_info(self, room_id, author_id, **kwargs):  # noqa: E501
        """获取直播间商品列表数据/Get live room product list data  # noqa: E501

        # [中文] ### 用途: - 获取直播间商品列表数据 ### 参数: - room_id: 直播间id，必填参数。 - author_id: 主播id，必填参数。 - page_size: 每页数量，可选参数，默认为15。 - offset: 翻页游标，可选参数，默认为0，每次翻页增加15。 - region: 地区，可选参数，默认为`US`，如果使用其他地区，如：`VN`，请自行携带Cookie，否则无法获取数据。 - cookie: 用户自己的cookie，可选参数，用于爬取除`US`以外的地区数据。 ### 参数获取: - 第一步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"`接口获取直播间id（room_id）。 - 第二步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"`接口获取直播间信息。 - 第三步：使用第二步返回的JSON数据中使用JSONPATH获取`$.data.data.owner.id_str`字段的值作为主播id（author_id）。 ### 返回: - 直播间商品列表数据  # [English] ### Purpose: - Get live room product list data ### Parameters: - room_id: Live room id, required parameter. - author_id: Anchor id, required parameter. - page_size: Number per page, optional parameter, default is 15. - offset: Page turning cursor, optional parameter, default is 0, increasing by 15 each time. - region: Region, optional parameter, default is `US`, if you use other regions, such as: `VN`, please bring your own Cookie, otherwise you will not be able to get data. - cookie: User's own cookie, optional parameter, used to crawl data from regions other than `US`. ### Get Parameters: - Step 1: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"` to get the live room id (room_id). - Step 2: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"` to get the live room information. - Step 3: Use the JSONPATH in the JSON data returned in the second step to get the value of the field `$.data.data.owner.id_str` as the anchor id (author_id). ### Return: - Live room product list data  # [示例/Example] room_id = \"7420741353250507562\" author_id = \"7408859677050274859\" page_size = 15 offset = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get_with_http_info(room_id, author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间id/Live room id (required)
        :param object author_id: 主播id/Anchor id (required)
        :param object page_size: 数量/Number
        :param object offset: 数量/Number
        :param object region: 地区/Region
        :param object cookie: 用户自己的cookie/User's own cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id', 'author_id', 'page_size', 'offset', 'region', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get`")  # noqa: E501
        # verify the required parameter 'author_id' is set
        if self.api_client.client_side_validation and ('author_id' not in params or
                                                       params['author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `author_id` when calling `fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501
        if 'author_id' in params:
            query_params.append(('author_id', params['author_id']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_live_room_product_list', 'GET',
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

    def fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get(self, room_id, author_id, **kwargs):  # noqa: E501
        """获取直播间商品列表数据 V2 /Get live room product list data V2  # noqa: E501

        # [中文] ### 用途: - 获取直播间商品列表数据 V2 ### 参数: - room_id: 直播间id，必填参数。 - author_id: 主播id，必填参数。 - page_size: 每页数量，可选参数，默认为15。 - offset: 翻页游标，可选参数，默认为0，每次翻页增加15。 - region: 地区，可选参数，默认为`US`，如果使用其他地区，如：`VN`，请自行携带Cookie，否则无法获取数据。 - cookie: 用户自己的cookie，可选参数，用于爬取除`US`以外的地区数据。 ### 参数获取: - 第一步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"`接口获取直播间id（room_id）。 - 第二步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"`接口获取直播间信息。 - 第三步：使用第二步返回的JSON数据中使用JSONPATH获取`$.data.data.owner.id_str`字段的值作为主播id（author_id）。 ### 返回: - 直播间商品列表数据  # [English] ### Purpose: - Get live room product list data V2 ### Parameters: - room_id: Live room id, required parameter. - author_id: Anchor id, required parameter. - page_size: Number per page, optional parameter, default is 15. - offset: Page turning cursor, optional parameter, default is 0, increasing by 15 each time. - region: Region, optional parameter, default is `US`, if you use other regions, such as: `VN`, please bring your own Cookie, otherwise you will not be able to get data. - cookie: User's own cookie, optional parameter, used to crawl data from regions other than `US`. ### Get Parameters: - Step 1: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"` to get the live room id (room_id). - Step 2: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"` to get the live room information. - Step 3: Use the JSONPATH in the JSON data returned in the second step to get the value of the field `$.data.data.owner.id_str` as the anchor id (author_id). ### Return: - Live room product list data  # [示例/Example] room_id = \"7420741353250507562\" author_id = \"7408859677050274859\" page_size = 15 offset = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get(room_id, author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间id/Live room id (required)
        :param object author_id: 主播id/Anchor id (required)
        :param object page_size: 数量/Number
        :param object offset: 数量/Number
        :param object region: 地区/Region
        :param object cookie: 用户自己的cookie/User's own cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get_with_http_info(room_id, author_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get_with_http_info(room_id, author_id, **kwargs)  # noqa: E501
            return data

    def fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get_with_http_info(self, room_id, author_id, **kwargs):  # noqa: E501
        """获取直播间商品列表数据 V2 /Get live room product list data V2  # noqa: E501

        # [中文] ### 用途: - 获取直播间商品列表数据 V2 ### 参数: - room_id: 直播间id，必填参数。 - author_id: 主播id，必填参数。 - page_size: 每页数量，可选参数，默认为15。 - offset: 翻页游标，可选参数，默认为0，每次翻页增加15。 - region: 地区，可选参数，默认为`US`，如果使用其他地区，如：`VN`，请自行携带Cookie，否则无法获取数据。 - cookie: 用户自己的cookie，可选参数，用于爬取除`US`以外的地区数据。 ### 参数获取: - 第一步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"`接口获取直播间id（room_id）。 - 第二步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"`接口获取直播间信息。 - 第三步：使用第二步返回的JSON数据中使用JSONPATH获取`$.data.data.owner.id_str`字段的值作为主播id（author_id）。 ### 返回: - 直播间商品列表数据  # [English] ### Purpose: - Get live room product list data V2 ### Parameters: - room_id: Live room id, required parameter. - author_id: Anchor id, required parameter. - page_size: Number per page, optional parameter, default is 15. - offset: Page turning cursor, optional parameter, default is 0, increasing by 15 each time. - region: Region, optional parameter, default is `US`, if you use other regions, such as: `VN`, please bring your own Cookie, otherwise you will not be able to get data. - cookie: User's own cookie, optional parameter, used to crawl data from regions other than `US`. ### Get Parameters: - Step 1: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"` to get the live room id (room_id). - Step 2: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"` to get the live room information. - Step 3: Use the JSONPATH in the JSON data returned in the second step to get the value of the field `$.data.data.owner.id_str` as the anchor id (author_id). ### Return: - Live room product list data  # [示例/Example] room_id = \"7420741353250507562\" author_id = \"7408859677050274859\" page_size = 15 offset = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get_with_http_info(room_id, author_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间id/Live room id (required)
        :param object author_id: 主播id/Anchor id (required)
        :param object page_size: 数量/Number
        :param object offset: 数量/Number
        :param object region: 地区/Region
        :param object cookie: 用户自己的cookie/User's own cookie
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id', 'author_id', 'page_size', 'offset', 'region', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get`")  # noqa: E501
        # verify the required parameter 'author_id' is set
        if self.api_client.client_side_validation and ('author_id' not in params or
                                                       params['author_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `author_id` when calling `fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501
        if 'author_id' in params:
            query_params.append(('author_id', params['author_id']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_live_room_product_list_v2', 'GET',
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

    def fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的直播搜索结果/Get live search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的直播搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量，从0开始，第二页从响应中获取cursor的值作为offset继续请求。 - count: 数量，不要超过20 - region: 地区，默认为US-美国，可选值请参考TikTok地区代码或ISO 3166-1 alpha-2国家代码。 ### 返回: - 直播搜索结果  # [English] ### Purpose: - Get live search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. - count: Number, do not exceed 20 - region: Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. ### Return: - Live search results  # [示例/Example] keyword = \"Cat\" offset = 0 count = 20 region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object region: 地区/Region
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的直播搜索结果/Get live search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的直播搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量，从0开始，第二页从响应中获取cursor的值作为offset继续请求。 - count: 数量，不要超过20 - region: 地区，默认为US-美国，可选值请参考TikTok地区代码或ISO 3166-1 alpha-2国家代码。 ### 返回: - 直播搜索结果  # [English] ### Purpose: - Get live search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. - count: Number, do not exceed 20 - region: Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. ### Return: - Live search results  # [示例/Example] keyword = \"Cat\" offset = 0 count = 20 region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object region: 地区/Region
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_live_search_result', 'GET',
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

    def fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get(self, keyword, **kwargs):  # noqa: E501
        """获取地点搜索结果/Get location search results  # noqa: E501

        # [中文] ### 用途: - 获取地点搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 ### 返回: - 地点搜索结果  # [English] ### Purpose: - Get location search results ### Parameters: - keyword: Keyword - offset: Offset - count: Number ### Return: - Location search results  # [示例/Example] keyword = \"Shanghai\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取地点搜索结果/Get location search results  # noqa: E501

        # [中文] ### 用途: - 获取地点搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 ### 返回: - 地点搜索结果  # [English] ### Purpose: - Get location search results ### Parameters: - keyword: Keyword - offset: Offset - count: Number ### Return: - Location search results  # [示例/Example] keyword = \"Shanghai\" offset = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_location_search', 'GET',
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

    def fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post(self, **kwargs):  # noqa: E501
        """批量获取视频信息/Batch Get Video Information  # noqa: E501

        # [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。 - 如果本接口报错，请使用 fetch_multi_video_v3 接口。 ### 参数: - aweme_ids: 作品id列表，最多支持10个作品id。 ### 返回: - 作品数据  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface charges a fixed price of 0.001$ * 10 = 0.01$ each time. - If this interface reports an error, please use the fetch_multi_video_v3 interface. ### Parameters: - aweme_ids: List of video ids, up to 10 video ids are supported. ### Return: - Video data  # [示例/Example] aweme_ids = [         \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",         \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",     ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post_with_http_info(self, **kwargs):  # noqa: E501
        """批量获取视频信息/Batch Get Video Information  # noqa: E501

        # [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。 - 如果本接口报错，请使用 fetch_multi_video_v3 接口。 ### 参数: - aweme_ids: 作品id列表，最多支持10个作品id。 ### 返回: - 作品数据  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface charges a fixed price of 0.001$ * 10 = 0.01$ each time. - If this interface reports an error, please use the fetch_multi_video_v3 interface. ### Parameters: - aweme_ids: List of video ids, up to 10 video ids are supported. ### Return: - Video data  # [示例/Example] aweme_ids = [         \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",         \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",     ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post_with_http_info(async_req=True)
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
                    " to method fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post" % key
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
            '/api/v1/tiktok/app/v3/fetch_multi_video', 'POST',
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

    def fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post(self, **kwargs):  # noqa: E501
        """批量获取视频信息 V2/Batch Get Video Information V2  # noqa: E501

        # [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持25个视频，此接口收费固定价格为0.001$ * 25 = 0.025$一次。 - 注意：此接口为V2版本，支持更多功能和更高效的数据获取，一秒可以获取25个视频数据。 - 如果本接口报错，请使用 fetch_multi_video_v3 接口。 ### 参数: - aweme_ids: 作品id列表，最多支持25个作品id。 ### 返回: - 作品数据  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 25 videos at a time, this interface charges a fixed price of 0.001$ * 25 = 0.025$ each time. - Note: This interface is the V2 version, which supports more features and more efficient data retrieval, can retrieve 25 video data per second. - If this interface reports an error, please use the fetch_multi_video_v3 interface. ### Parameters: - aweme_ids: List of video ids, up to 25 video ids are supported. ### Return: - Video data  # [示例/Example] aweme_ids = [         \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",         \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",     ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post_with_http_info(self, **kwargs):  # noqa: E501
        """批量获取视频信息 V2/Batch Get Video Information V2  # noqa: E501

        # [中文] ### 用途: - 批量获取视频信息，支持图文、视频等，一次性最多支持25个视频，此接口收费固定价格为0.001$ * 25 = 0.025$一次。 - 注意：此接口为V2版本，支持更多功能和更高效的数据获取，一秒可以获取25个视频数据。 - 如果本接口报错，请使用 fetch_multi_video_v3 接口。 ### 参数: - aweme_ids: 作品id列表，最多支持25个作品id。 ### 返回: - 作品数据  # [English] ### Purpose: - Batch Get Video Information, support photo, video, etc., up to 25 videos at a time, this interface charges a fixed price of 0.001$ * 25 = 0.025$ each time. - Note: This interface is the V2 version, which supports more features and more efficient data retrieval, can retrieve 25 video data per second. - If this interface reports an error, please use the fetch_multi_video_v3 interface. ### Parameters: - aweme_ids: List of video ids, up to 25 video ids are supported. ### Return: - Video data  # [示例/Example] aweme_ids = [         \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",         \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",     ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post_with_http_info(async_req=True)
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
                    " to method fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post" % key
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
            '/api/v1/tiktok/app/v3/fetch_multi_video_v2', 'POST',
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

    def fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get(self, **kwargs):  # noqa: E501
        """音乐排行榜/Music Chart List  # noqa: E501

        # [中文] ### 用途: - 获取TikTok音乐排行榜数据 ### 参数: - scene: 排行榜类型     - 0: Top 50 (热门前50)     - 1: Viral 50 (病毒式传播前50) - cursor: 分页游标，默认0 - count: 每页数量，默认50，最大50 ### 返回: - 音乐排行榜数据，包含歌曲信息、排名变化等  # [English] ### Purpose: - Get TikTok music chart list data ### Parameters: - scene: Chart type     - 0: Top 50 (Popular top 50)     - 1: Viral 50 (Viral top 50) - cursor: Pagination cursor, default 0 - count: Number per page, default 50, max 50 ### Return: - Music chart data, including song info, ranking changes, etc.  # [示例/Example] scene = 0  # Top 50 cursor = 0 count = 50  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object scene: 排行榜类型/Chart type (0: Top 50, 1: Viral 50)
        :param object cursor: 分页游标/Pagination cursor
        :param object count: 每页数量/Number per page (max 50)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """音乐排行榜/Music Chart List  # noqa: E501

        # [中文] ### 用途: - 获取TikTok音乐排行榜数据 ### 参数: - scene: 排行榜类型     - 0: Top 50 (热门前50)     - 1: Viral 50 (病毒式传播前50) - cursor: 分页游标，默认0 - count: 每页数量，默认50，最大50 ### 返回: - 音乐排行榜数据，包含歌曲信息、排名变化等  # [English] ### Purpose: - Get TikTok music chart list data ### Parameters: - scene: Chart type     - 0: Top 50 (Popular top 50)     - 1: Viral 50 (Viral top 50) - cursor: Pagination cursor, default 0 - count: Number per page, default 50, max 50 ### Return: - Music chart data, including song info, ranking changes, etc.  # [示例/Example] scene = 0  # Top 50 cursor = 0 count = 50  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object scene: 排行榜类型/Chart type (0: Top 50, 1: Viral 50)
        :param object cursor: 分页游标/Pagination cursor
        :param object count: 每页数量/Number per page (max 50)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scene', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scene' in params:
            query_params.append(('scene', params['scene']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_music_chart_list', 'GET',
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

    def fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get(self, music_id, **kwargs):  # noqa: E501
        """获取指定音乐的详情数据/Get details of specified music  # noqa: E501

        # [中文] ### 用途: - 获取指定音乐的详情数据 ### 参数: - music_id: 音乐id ### 返回: - 音乐详情数据  # [English] ### Purpose: - Get details of specified music ### Parameters: - music_id: Music id ### Return: - Music details data  # [示例/Example] music_id = \"6943027371519772674\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get(music_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object music_id: 音乐id/Music id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get_with_http_info(music_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get_with_http_info(music_id, **kwargs)  # noqa: E501
            return data

    def fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get_with_http_info(self, music_id, **kwargs):  # noqa: E501
        """获取指定音乐的详情数据/Get details of specified music  # noqa: E501

        # [中文] ### 用途: - 获取指定音乐的详情数据 ### 参数: - music_id: 音乐id ### 返回: - 音乐详情数据  # [English] ### Purpose: - Get details of specified music ### Parameters: - music_id: Music id ### Return: - Music details data  # [示例/Example] music_id = \"6943027371519772674\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get_with_http_info(music_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object music_id: 音乐id/Music id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['music_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'music_id' is set
        if self.api_client.client_side_validation and ('music_id' not in params or
                                                       params['music_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `music_id` when calling `fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'music_id' in params:
            query_params.append(('music_id', params['music_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_music_detail', 'GET',
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

    def fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的音乐搜索结果/Get music search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的音乐搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量，从0开始，第二页从响应中获取cursor的值作为offset继续请求。 - count: 数量，不要超过20 - filter_by: 过滤类型，0-全部，1-标题，2-作者，默认为0-全部 - sort_type: 排序类型，0-相关度，1-最多使用，2-最新，3-时长最短，4-时长最长，默认为0-相关度 - region: 地区，默认为US-美国，可选值请参考TikTok地区代码或ISO 3166-1 alpha-2国家代码。 ### 返回: - 音乐搜索结果  # [English] ### Purpose: - Get music search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. - count: Number, do not exceed 20 - filter_by: Filter type, 0-All, 1-Title, 2-Author, default is 0-All - sort_type: Sort type, 0-Relatedness, 1-Most used, 2-Latest, 3-Shortest duration, 4-Longest duration, default is 0-Relatedness - region: Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. ### Return: - Music search results  # [示例/Example] keyword = \"Cat\" offset = 0 count = 20 filter_by = 0 sort_type = 0 region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object filter_by: 过滤类型/Filter type
        :param object sort_type: 排序类型/Sort type
        :param object region: 地区/Region
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的音乐搜索结果/Get music search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的音乐搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量，从0开始，第二页从响应中获取cursor的值作为offset继续请求。 - count: 数量，不要超过20 - filter_by: 过滤类型，0-全部，1-标题，2-作者，默认为0-全部 - sort_type: 排序类型，0-相关度，1-最多使用，2-最新，3-时长最短，4-时长最长，默认为0-相关度 - region: 地区，默认为US-美国，可选值请参考TikTok地区代码或ISO 3166-1 alpha-2国家代码。 ### 返回: - 音乐搜索结果  # [English] ### Purpose: - Get music search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. - count: Number, do not exceed 20 - filter_by: Filter type, 0-All, 1-Title, 2-Author, default is 0-All - sort_type: Sort type, 0-Relatedness, 1-Most used, 2-Latest, 3-Shortest duration, 4-Longest duration, default is 0-Relatedness - region: Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. ### Return: - Music search results  # [示例/Example] keyword = \"Cat\" offset = 0 count = 20 filter_by = 0 sort_type = 0 region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object filter_by: 过滤类型/Filter type
        :param object sort_type: 排序类型/Sort type
        :param object region: 地区/Region
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'filter_by', 'sort_type', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'filter_by' in params:
            query_params.append(('filter_by', params['filter_by']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_music_search_result', 'GET',
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

    def fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get(self, music_id, **kwargs):  # noqa: E501
        """获取指定音乐的视频列表数据/Get video list of specified music  # noqa: E501

        # [中文] ### 用途: - 获取指定音乐的视频列表数据 ### 参数: - music_id: 音乐id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 ### 返回: - 音乐视频列表数据  # [English] ### Purpose: - Get video list of specified music ### Parameters: - music_id: Music id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number ### Return: - Music video list data  # [示例/Example] music_id = \"6943027371519772674\" cursor = 0 count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get(music_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object music_id: 音乐id/Music id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get_with_http_info(music_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get_with_http_info(music_id, **kwargs)  # noqa: E501
            return data

    def fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get_with_http_info(self, music_id, **kwargs):  # noqa: E501
        """获取指定音乐的视频列表数据/Get video list of specified music  # noqa: E501

        # [中文] ### 用途: - 获取指定音乐的视频列表数据 ### 参数: - music_id: 音乐id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 ### 返回: - 音乐视频列表数据  # [English] ### Purpose: - Get video list of specified music ### Parameters: - music_id: Music id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number ### Return: - Music video list data  # [示例/Example] music_id = \"6943027371519772674\" cursor = 0 count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get_with_http_info(music_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object music_id: 音乐id/Music id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['music_id', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'music_id' is set
        if self.api_client.client_side_validation and ('music_id' not in params or
                                                       params['music_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `music_id` when calling `fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'music_id' in params:
            query_params.append(('music_id', params['music_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_music_video_list', 'GET',
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

    def fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data ### Parameters: - aweme_id: Video id ### Return: - Video data  # [示例/Example] aweme_id = \"7350810998023949599\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data ### Parameters: - aweme_id: Video id ### Return: - Video data  # [示例/Example] aweme_id = \"7350810998023949599\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_one_video', 'GET',
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

    def fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get(self, share_url, **kwargs):  # noqa: E501
        """根据分享链接获取单个作品数据/Get single video data by sharing link  # noqa: E501

        # [中文] ### 用途: - 根据分享链接获取单个作品数据 ### 参数: - share_url: 分享链接 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data by sharing link ### Parameters: - share_url: Share link ### Return: - Video data  # [示例/Example] share_url = \"https://www.tiktok.com/t/ZTFNEj8Hk/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get(share_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_url: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get_with_http_info(share_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get_with_http_info(share_url, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get_with_http_info(self, share_url, **kwargs):  # noqa: E501
        """根据分享链接获取单个作品数据/Get single video data by sharing link  # noqa: E501

        # [中文] ### 用途: - 根据分享链接获取单个作品数据 ### 参数: - share_url: 分享链接 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data by sharing link ### Parameters: - share_url: Share link ### Return: - Video data  # [示例/Example] share_url = \"https://www.tiktok.com/t/ZTFNEj8Hk/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get_with_http_info(share_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_url: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['share_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_url' is set
        if self.api_client.client_side_validation and ('share_url' not in params or
                                                       params['share_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_url` when calling `fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_url' in params:
            query_params.append(('share_url', params['share_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_one_video_by_share_url', 'GET',
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

    def fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get(self, share_url, **kwargs):  # noqa: E501
        """根据分享链接获取单个作品数据/Get single video data by sharing link  # noqa: E501

        # [中文] ### 用途: - 根据分享链接获取单个作品数据 V2，数据结构会有些不一样，会返回region字段。 ### 参数: - share_url: 分享链接 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data by sharing link V2, the data structure will be a bit different, and the region field will be returned. ### Parameters: - share_url: Share link ### Return: - Video data  # [示例/Example] share_url = \"https://www.tiktok.com/t/ZTFNEj8Hk/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get(share_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_url: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get_with_http_info(share_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get_with_http_info(share_url, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get_with_http_info(self, share_url, **kwargs):  # noqa: E501
        """根据分享链接获取单个作品数据/Get single video data by sharing link  # noqa: E501

        # [中文] ### 用途: - 根据分享链接获取单个作品数据 V2，数据结构会有些不一样，会返回region字段。 ### 参数: - share_url: 分享链接 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data by sharing link V2, the data structure will be a bit different, and the region field will be returned. ### Parameters: - share_url: Share link ### Return: - Video data  # [示例/Example] share_url = \"https://www.tiktok.com/t/ZTFNEj8Hk/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get_with_http_info(share_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_url: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['share_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_url' is set
        if self.api_client.client_side_validation and ('share_url' not in params or
                                                       params['share_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_url` when calling `fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_url' in params:
            query_params.append(('share_url', params['share_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_one_video_by_share_url_v2', 'GET',
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

    def fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 V2 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data V2 ### Parameters: - aweme_id: Video id ### Return: - Video data  # [示例/Example] aweme_id = \"7350810998023949599\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 V2 ### 参数: - aweme_id: 作品id ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data V2 ### Parameters: - aweme_id: Video id ### Return: - Video data  # [示例/Example] aweme_id = \"7350810998023949599\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_one_video_v2', 'GET',
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

    def fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V3(支持国家参数)/Get single video data V3 (support country parameter)  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 V3 ### 参数: - aweme_id: 作品id - region: 国家代码，默认US，支持ISO 3166-1 alpha-2国家代码，例如：US、GB、FR、DE、IN、JP等。 - 备注：某些视频可能在特定国家/地区不可用，设置region参数可以尝试获取该国家/地区的视频数据。 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data V3 ### Parameters: - aweme_id: Video id - region: Country code, default is US, supports ISO 3166-1 alpha-2 country codes, such as: US, GB, FR, DE, IN, JP, etc. - Note: Some videos may not be available in certain countries/regions, setting the region parameter can try to get the video data for that country/region. ### Return: - Video data  # [示例/Example] aweme_id = \"7350810998023949599\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object region: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V3(支持国家参数)/Get single video data V3 (support country parameter)  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 V3 ### 参数: - aweme_id: 作品id - region: 国家代码，默认US，支持ISO 3166-1 alpha-2国家代码，例如：US、GB、FR、DE、IN、JP等。 - 备注：某些视频可能在特定国家/地区不可用，设置region参数可以尝试获取该国家/地区的视频数据。 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data V3 ### Parameters: - aweme_id: Video id - region: Country code, default is US, supports ISO 3166-1 alpha-2 country codes, such as: US, GB, FR, DE, IN, JP, etc. - Note: Some videos may not be available in certain countries/regions, setting the region parameter can try to get the video data for that country/region. ### Return: - Video data  # [示例/Example] aweme_id = \"7350810998023949599\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object region: 国家代码/Country code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_one_video_v3', 'GET',
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

    def fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情数据（即将弃用，使用 fetch_product_detail_v2 代替）/Get product detail data (will be deprecated, use fetch_product_detail_v2 instead)  # noqa: E501

        # [中文] ### 用途: - 获取商品详情数据 - 即将弃用，使用 fetch_product_detail_v2 代替 ### 参数: - product_id: 商品id，有时候需要从product_id_str字段中获取。 ### 返回: - 商品详情数据  # [English] ### Purpose: - Get product detail data - Will be deprecated, use fetch_product_detail_v2 instead ### Parameters: - product_id: Product id, sometimes need to get from the product_id_str field. ### Return: - Product detail data  # [示例/Example] product_id = \"1729385239712731370\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品id/Product id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情数据（即将弃用，使用 fetch_product_detail_v2 代替）/Get product detail data (will be deprecated, use fetch_product_detail_v2 instead)  # noqa: E501

        # [中文] ### 用途: - 获取商品详情数据 - 即将弃用，使用 fetch_product_detail_v2 代替 ### 参数: - product_id: 商品id，有时候需要从product_id_str字段中获取。 ### 返回: - 商品详情数据  # [English] ### Purpose: - Get product detail data - Will be deprecated, use fetch_product_detail_v2 instead ### Parameters: - product_id: Product id, sometimes need to get from the product_id_str field. ### Return: - Product detail data  # [示例/Example] product_id = \"1729385239712731370\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品id/Product id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_product_detail', 'GET',
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

    def fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情数据V2/Get product detail data V2  # noqa: E501

        # [中文] ### 用途: - 获取商品详情数据V2 ### 参数: - product_id: 商品id，有时候需要从product_id_str字段中获取。 ### 返回: - 商品详情数据V2  # [English] ### Purpose: - Get product detail data V2 ### Parameters: - product_id: Product id, sometimes need to get from the product_id_str field. ### Return: - Product detail data V2  # [示例/Example] product_id = \"1729385239712731370\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品id/Product id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情数据V2/Get product detail data V2  # noqa: E501

        # [中文] ### 用途: - 获取商品详情数据V2 ### 参数: - product_id: 商品id，有时候需要从product_id_str字段中获取。 ### 返回: - 商品详情数据V2  # [English] ### Purpose: - Get product detail data V2 ### Parameters: - product_id: Product id, sometimes need to get from the product_id_str field. ### Return: - Product detail data V2  # [示例/Example] product_id = \"1729385239712731370\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品id/Product id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_product_detail_v2', 'GET',
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

    def fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情数据V3 / Get product detail data V3  # noqa: E501

        # [中文] ### 用途: - 获取商品详情数据V3。如果商品详情数据V2无法获取，可以尝试使用此接口。  ### 参数: - product_id: 商品id，有时候需要从 `product_id_str` 字段中获取，也可以从商品分享链接中获取。 - region: 商品的国家/地区代码，默认值为 \"US\"。  ### 支持的国家/地区代码（按区域分组）： - 东南亚 Southeast Asia:   ID（印度尼西亚）, SG（新加坡）, MY（马来西亚）, PH（菲律宾）, TH（泰国） - 北美 North America:   US（美国）, MX（墨西哥） - 欧洲 Europe:   IE（爱尔兰）, GB（英国）, ES（西班牙） - 越南 Vietnam:   VN（越南）  ### 返回: - 商品详情数据V3  # [English] ### Purpose: - Get product detail data V3. If product detail data V2 cannot be retrieved, try this version.  ### Parameters: - product_id: Product ID. Sometimes needs to be extracted from `product_id_str` field, or can be obtained from the product share link. - region: Country code of the product, default is \"US\".  ### Supported region codes (grouped by area): - Southeast Asia:   ID (Indonesia), SG (Singapore), MY (Malaysia), PH (Philippines), TH (Thailand) - North America:   US (United States), MX (Mexico) - Europe:   IE (Ireland), GB (United Kingdom), ES (Spain) - Vietnam:   VN (Vietnam)  ### Return: - Product detail data V3  # [示例 / Example] product_id = \"1729385239712731370\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品id / Product ID (required)
        :param object region: 商品的国家/地区代码/ Country/region code of the product
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情数据V3 / Get product detail data V3  # noqa: E501

        # [中文] ### 用途: - 获取商品详情数据V3。如果商品详情数据V2无法获取，可以尝试使用此接口。  ### 参数: - product_id: 商品id，有时候需要从 `product_id_str` 字段中获取，也可以从商品分享链接中获取。 - region: 商品的国家/地区代码，默认值为 \"US\"。  ### 支持的国家/地区代码（按区域分组）： - 东南亚 Southeast Asia:   ID（印度尼西亚）, SG（新加坡）, MY（马来西亚）, PH（菲律宾）, TH（泰国） - 北美 North America:   US（美国）, MX（墨西哥） - 欧洲 Europe:   IE（爱尔兰）, GB（英国）, ES（西班牙） - 越南 Vietnam:   VN（越南）  ### 返回: - 商品详情数据V3  # [English] ### Purpose: - Get product detail data V3. If product detail data V2 cannot be retrieved, try this version.  ### Parameters: - product_id: Product ID. Sometimes needs to be extracted from `product_id_str` field, or can be obtained from the product share link. - region: Country code of the product, default is \"US\".  ### Supported region codes (grouped by area): - Southeast Asia:   ID (Indonesia), SG (Singapore), MY (Malaysia), PH (Philippines), TH (Thailand) - North America:   US (United States), MX (Mexico) - Europe:   IE (Ireland), GB (United Kingdom), ES (Spain) - Vietnam:   VN (Vietnam)  ### Return: - Product detail data V3  # [示例 / Example] product_id = \"1729385239712731370\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品id / Product ID (required)
        :param object region: 商品的国家/地区代码/ Country/region code of the product
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_product_detail_v3', 'GET',
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

    def fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情数据V4 / Get product detail data V4  # noqa: E501

        # [中文] ### 用途: - 获取商品详情数据V4。如果商品详情数据V3无法获取，可以尝试使用此接口。  ### 参数: - product_id: 商品id，有时候需要从 `product_id_str` 字段中获取，也可以从商品分享链接中获取。 - region: 商品的国家/地区代码，默认值为 \"US\"。  ### 支持的国家/地区代码（按区域分组）： - 东南亚 Southeast Asia:   ID（印度尼西亚）, SG（新加坡）, MY（马来西亚）, PH（菲律宾）, TH（泰国） - 北美 North America:   US（美国）, MX（墨西哥） - 欧洲 Europe:   IE（爱尔兰）, GB（英国）, ES（西班牙） - 越南 Vietnam:   VN（越南）  ### 返回: - 商品详情数据V4  # [English] ### Purpose: - Get product detail data V4. If product detail data V3 cannot be retrieved, try this version.  ### Parameters: - product_id: Product ID. Sometimes needs to be extracted from `product_id_str` field, or can be obtained from the product share link. - region: Country code of the product, default is \"US\".  ### Supported region codes (grouped by area): - Southeast Asia:   ID (Indonesia), SG (Singapore), MY (Malaysia), PH (Philippines), TH (Thailand) - North America:   US (United States), MX (Mexico) - Europe:   IE (Ireland), GB (United Kingdom), ES (Spain) - Vietnam:   VN (Vietnam)  ### Return: - Product detail data V4  # [示例 / Example] seller_id = \"8646929864612614278\" product_id = \"1729385239712731370\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品id / Product ID (required)
        :param object region: 商品的国家/地区代码/ Country/region code of the product
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情数据V4 / Get product detail data V4  # noqa: E501

        # [中文] ### 用途: - 获取商品详情数据V4。如果商品详情数据V3无法获取，可以尝试使用此接口。  ### 参数: - product_id: 商品id，有时候需要从 `product_id_str` 字段中获取，也可以从商品分享链接中获取。 - region: 商品的国家/地区代码，默认值为 \"US\"。  ### 支持的国家/地区代码（按区域分组）： - 东南亚 Southeast Asia:   ID（印度尼西亚）, SG（新加坡）, MY（马来西亚）, PH（菲律宾）, TH（泰国） - 北美 North America:   US（美国）, MX（墨西哥） - 欧洲 Europe:   IE（爱尔兰）, GB（英国）, ES（西班牙） - 越南 Vietnam:   VN（越南）  ### 返回: - 商品详情数据V4  # [English] ### Purpose: - Get product detail data V4. If product detail data V3 cannot be retrieved, try this version.  ### Parameters: - product_id: Product ID. Sometimes needs to be extracted from `product_id_str` field, or can be obtained from the product share link. - region: Country code of the product, default is \"US\".  ### Supported region codes (grouped by area): - Southeast Asia:   ID (Indonesia), SG (Singapore), MY (Malaysia), PH (Philippines), TH (Thailand) - North America:   US (United States), MX (Mexico) - Europe:   IE (Ireland), GB (United Kingdom), ES (Spain) - Vietnam:   VN (Vietnam)  ### Return: - Product detail data V4  # [示例 / Example] seller_id = \"8646929864612614278\" product_id = \"1729385239712731370\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品id / Product ID (required)
        :param object region: 商品的国家/地区代码/ Country/region code of the product
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_product_detail_v4', 'GET',
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

    def fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get(self, share_link, **kwargs):  # noqa: E501
        """通过分享链接获取商品ID/Get Product ID by Share Link  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取商品ID ### 参数: - share_link: 分享链接 ### 返回: - 商品ID  # [English] ### Purpose: - Get Product ID by Share Link ### Parameters: - share_link: Share link ### Return: - Product ID  # [示例/Example] share_link = \"https://www.tiktok.com/t/ZT2A9N1kw/\" share_link2 = \"https://affiliate-us.tiktok.com/api/v1/share/AJ4hS3OdXmSg\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get_with_http_info(share_link, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get_with_http_info(share_link, **kwargs)  # noqa: E501
            return data

    def fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get_with_http_info(self, share_link, **kwargs):  # noqa: E501
        """通过分享链接获取商品ID/Get Product ID by Share Link  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取商品ID ### 参数: - share_link: 分享链接 ### 返回: - 商品ID  # [English] ### Purpose: - Get Product ID by Share Link ### Parameters: - share_link: Share link ### Return: - Product ID  # [示例/Example] share_link = \"https://www.tiktok.com/t/ZT2A9N1kw/\" share_link2 = \"https://affiliate-us.tiktok.com/api/v1/share/AJ4hS3OdXmSg\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get_with_http_info(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: 分享链接/Share link (required)
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
                    " to method fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_link' is set
        if self.api_client.client_side_validation and ('share_link' not in params or
                                                       params['share_link'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_link` when calling `fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get`")  # noqa: E501

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
            '/api/v1/tiktok/app/v3/fetch_product_id_by_share_link', 'GET',
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

    def fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品评价数据/Get product review data  # noqa: E501

        # [中文] ### 用途: - 获取商品评价数据 ### 参数: - product_id: 商品id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - size: 数量 - filter_id: 筛选条件     - 0: 全部评价     - 1: 1星评价     - 2: 2星评价     - 3: 3星评价     - 4: 4星评价     - 5: 5星评价     - 102: 有图评价     - 104: 已购买的评价 - sort_type: 排序条件     - 1: 相关度     - 2: 从新到旧 ### 返回: - 商品评价数据  # [English] ### Purpose: - Get product review data ### Parameters: - product_id: Product id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - size: Count number - filter_id: Filter condition     - 0: All reviews     - 1: 1-star review     - 2: 2-star review     - 3: 3-star review     - 4: 4-star review     - 5: 5-star review     - 102: Reviews with pictures     - 104: Reviews of purchased products - sort_type: Sorting conditions     - 1: Relevance     - 2: New to old ### Return: - Product review data  # [示例/Example] product_id = \"1729448812983194615\" cursor = 0 size = 10 filter_id = 0 sort_type = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品id/Product id (required)
        :param object cursor: 游标/Cursor
        :param object size: 数量/Number
        :param object filter_id: 筛选条件/Filter condition
        :param object sort_type: 排序条件/Sorting conditions
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品评价数据/Get product review data  # noqa: E501

        # [中文] ### 用途: - 获取商品评价数据 ### 参数: - product_id: 商品id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - size: 数量 - filter_id: 筛选条件     - 0: 全部评价     - 1: 1星评价     - 2: 2星评价     - 3: 3星评价     - 4: 4星评价     - 5: 5星评价     - 102: 有图评价     - 104: 已购买的评价 - sort_type: 排序条件     - 1: 相关度     - 2: 从新到旧 ### 返回: - 商品评价数据  # [English] ### Purpose: - Get product review data ### Parameters: - product_id: Product id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - size: Count number - filter_id: Filter condition     - 0: All reviews     - 1: 1-star review     - 2: 2-star review     - 3: 3-star review     - 4: 4-star review     - 5: 5-star review     - 102: Reviews with pictures     - 104: Reviews of purchased products - sort_type: Sorting conditions     - 1: Relevance     - 2: New to old ### Return: - Product review data  # [示例/Example] product_id = \"1729448812983194615\" cursor = 0 size = 10 filter_id = 0 sort_type = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品id/Product id (required)
        :param object cursor: 游标/Cursor
        :param object size: 数量/Number
        :param object filter_id: 筛选条件/Filter condition
        :param object sort_type: 排序条件/Sorting conditions
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'cursor', 'size', 'filter_id', 'sort_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'filter_id' in params:
            query_params.append(('filter_id', params['filter_id']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_product_review', 'GET',
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

    def fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get(self, keyword, **kwargs):  # noqa: E501
        """获取商品搜索结果/Get product search results  # noqa: E501

        # [中文] ### 用途: - 获取商品搜索结果 ### 参数: - keyword: 关键词 - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 - sort_type: 商品排序条件     - 1: 综合排序     - 2: 销量排序     - 3: 价格从高到低     - 4: 价格从低到高     - 5: 最新发布 - customer_review_four_star: 四星以上评价 - have_discount: 有优惠 - min_price: 最低价格 - max_price: 最高价格 ### 返回: - 商品搜索结果  # [English] ### Purpose: - Get product search results ### Parameters: - keyword: Keyword - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number - sort_type: Product sorting conditions     - 1: Comprehensive sorting     - 2: Sales volume sorting     - 3: Price high to low     - 4: Price low to high     - 5: Latest release - customer_review_four_star: Four-star or more reviews - have_discount: Having discount - min_price: Minimum price - max_price: Maximum price ### Return: - Product search results  # [示例/Example] keyword = \"Cat Toy\" cursor = 0 count = 12 sort_type = 1 customer_review_four_star = False have_discount = False min_price = \"10\" max_price = \"25\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :param object sort_type: 商品排序条件/Product sorting conditions
        :param object customer_review_four_star: 四星以上评价/Four-star or more reviews
        :param object have_discount: 有优惠/Having discount
        :param object min_price: 最低价格/Minimum price
        :param object max_price: 最高价格/Maximum price
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取商品搜索结果/Get product search results  # noqa: E501

        # [中文] ### 用途: - 获取商品搜索结果 ### 参数: - keyword: 关键词 - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 - sort_type: 商品排序条件     - 1: 综合排序     - 2: 销量排序     - 3: 价格从高到低     - 4: 价格从低到高     - 5: 最新发布 - customer_review_four_star: 四星以上评价 - have_discount: 有优惠 - min_price: 最低价格 - max_price: 最高价格 ### 返回: - 商品搜索结果  # [English] ### Purpose: - Get product search results ### Parameters: - keyword: Keyword - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number - sort_type: Product sorting conditions     - 1: Comprehensive sorting     - 2: Sales volume sorting     - 3: Price high to low     - 4: Price low to high     - 5: Latest release - customer_review_four_star: Four-star or more reviews - have_discount: Having discount - min_price: Minimum price - max_price: Maximum price ### Return: - Product search results  # [示例/Example] keyword = \"Cat Toy\" cursor = 0 count = 12 sort_type = 1 customer_review_four_star = False have_discount = False min_price = \"10\" max_price = \"25\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :param object sort_type: 商品排序条件/Product sorting conditions
        :param object customer_review_four_star: 四星以上评价/Four-star or more reviews
        :param object have_discount: 有优惠/Having discount
        :param object min_price: 最低价格/Minimum price
        :param object max_price: 最高价格/Maximum price
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'cursor', 'count', 'sort_type', 'customer_review_four_star', 'have_discount', 'min_price', 'max_price']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'customer_review_four_star' in params:
            query_params.append(('customer_review_four_star', params['customer_review_four_star']))  # noqa: E501
        if 'have_discount' in params:
            query_params.append(('have_discount', params['have_discount']))  # noqa: E501
        if 'min_price' in params:
            query_params.append(('min_price', params['min_price']))  # noqa: E501
        if 'max_price' in params:
            query_params.append(('max_price', params['max_price']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_product_search', 'GET',
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

    def fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get(self, object_id, **kwargs):  # noqa: E501
        """获取分享二维码/Get share QR code  # noqa: E501

        # [中文] ### 用途: - 获取分享二维码 ### 参数: - object_id: 对象id，当前支持个人主页接口响应中的uid作为参数。 ### 返回: - 二维码图片  # [English] ### Purpose: - Get share QR code ### Parameters: - object_id: Object id, currently supports the uid in the response of the personal homepage interface as a parameter. ### Return: - QR code image  # [示例/Example] url = \"6762244951259661318\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get(object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object object_id: 对象id/Object id (required)
        :param object schema_type: 模式类型/Schema type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get_with_http_info(object_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get_with_http_info(object_id, **kwargs)  # noqa: E501
            return data

    def fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get_with_http_info(self, object_id, **kwargs):  # noqa: E501
        """获取分享二维码/Get share QR code  # noqa: E501

        # [中文] ### 用途: - 获取分享二维码 ### 参数: - object_id: 对象id，当前支持个人主页接口响应中的uid作为参数。 ### 返回: - 二维码图片  # [English] ### Purpose: - Get share QR code ### Parameters: - object_id: Object id, currently supports the uid in the response of the personal homepage interface as a parameter. ### Return: - QR code image  # [示例/Example] url = \"6762244951259661318\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get_with_http_info(object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object object_id: 对象id/Object id (required)
        :param object schema_type: 模式类型/Schema type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['object_id', 'schema_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'object_id' is set
        if self.api_client.client_side_validation and ('object_id' not in params or
                                                       params['object_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `object_id` when calling `fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in params:
            query_params.append(('object_id', params['object_id']))  # noqa: E501
        if 'schema_type' in params:
            query_params.append(('schema_type', params['schema_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_share_qr_code', 'GET',
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

    def fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get(self, url, **kwargs):  # noqa: E501
        """获取分享短链接/Get share short link  # noqa: E501

        # [中文] ### 用途: - 获取分享短链接 ### 参数: - url: 长链接或想要转换的链接 ### 返回: - 短链接  # [English] ### Purpose: - Get share short link ### Parameters: - url: Long link or link to convert ### Return: - Short link  # [示例/Example] url = \"https://www.tiktok.com/passport/web/logout/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """获取分享短链接/Get share short link  # noqa: E501

        # [中文] ### 用途: - 获取分享短链接 ### 参数: - url: 长链接或想要转换的链接 ### 返回: - 短链接  # [English] ### Purpose: - Get share short link ### Parameters: - url: Long link or link to convert ### Return: - Short link  # [示例/Example] url = \"https://www.tiktok.com/passport/web/logout/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 分享链接/Share link (required)
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
                    " to method fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get`")  # noqa: E501

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
            '/api/v1/tiktok/app/v3/fetch_share_short_link', 'GET',
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

    def fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get(self, page_id, seller_id, **kwargs):  # noqa: E501
        """获取商家主页数据/Get shop home page data  # noqa: E501

        # [中文] ### 用途: - 获取商家主页的商品数据 ### 参数: - page_id: 爬取的商家主页Page id，可以从`fetch_shop_home_page_list`这个接口获取 - seller_id: 商家id,店铺id ### 返回: - 商家主页数据  # [English] ### Purpose: - Get product data of the shop home page ### Parameters: - page_id: Page id of the crawled shop home page, which can be obtained from the interface `fetch_shop_home_page_list` - seller_id: Seller id, shop id ### Return: - Shop home page data  # [示例/Example] page_id = \"7314705727611930410\" seller_id = \"8646929864612614278\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get(page_id, seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page_id: 爬取的商家主页Page id/Page id of the crawled shop home page (required)
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get_with_http_info(page_id, seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get_with_http_info(page_id, seller_id, **kwargs)  # noqa: E501
            return data

    def fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get_with_http_info(self, page_id, seller_id, **kwargs):  # noqa: E501
        """获取商家主页数据/Get shop home page data  # noqa: E501

        # [中文] ### 用途: - 获取商家主页的商品数据 ### 参数: - page_id: 爬取的商家主页Page id，可以从`fetch_shop_home_page_list`这个接口获取 - seller_id: 商家id,店铺id ### 返回: - 商家主页数据  # [English] ### Purpose: - Get product data of the shop home page ### Parameters: - page_id: Page id of the crawled shop home page, which can be obtained from the interface `fetch_shop_home_page_list` - seller_id: Seller id, shop id ### Return: - Shop home page data  # [示例/Example] page_id = \"7314705727611930410\" seller_id = \"8646929864612614278\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get_with_http_info(page_id, seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page_id: 爬取的商家主页Page id/Page id of the crawled shop home page (required)
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_id', 'seller_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_id' is set
        if self.api_client.client_side_validation and ('page_id' not in params or
                                                       params['page_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page_id` when calling `fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get`")  # noqa: E501
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in params or
                                                       params['seller_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `seller_id` when calling `fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_id' in params:
            query_params.append(('page_id', params['page_id']))  # noqa: E501
        if 'seller_id' in params:
            query_params.append(('seller_id', params['seller_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_shop_home', 'GET',
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

    def fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get(self, seller_id, **kwargs):  # noqa: E501
        """获取商家主页Page列表数据/Get shop home page list data  # noqa: E501

        # [中文] ### 用途: - 获取商家主页Page列表数据, 用于商家主页展示，以及爬取商家主页的商品数据 ### 参数: - seller_id: 商家id,店铺id ### 返回: - 商家主页Page列表数据  # [English] ### Purpose: - Get shop home page list data, used for shop home page display, and crawling shop home page product data ### Parameters: - seller_id: Seller id, shop id ### Return: - Shop home page list data  # [示例/Example] seller_id = \"8646929864612614278\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get_with_http_info(seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get_with_http_info(seller_id, **kwargs)  # noqa: E501
            return data

    def fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """获取商家主页Page列表数据/Get shop home page list data  # noqa: E501

        # [中文] ### 用途: - 获取商家主页Page列表数据, 用于商家主页展示，以及爬取商家主页的商品数据 ### 参数: - seller_id: 商家id,店铺id ### 返回: - 商家主页Page列表数据  # [English] ### Purpose: - Get shop home page list data, used for shop home page display, and crawling shop home page product data ### Parameters: - seller_id: Seller id, shop id ### Return: - Shop home page list data  # [示例/Example] seller_id = \"8646929864612614278\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['seller_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in params or
                                                       params['seller_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `seller_id` when calling `fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in params:
            query_params.append(('seller_id', params['seller_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_shop_home_page_list', 'GET',
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

    def fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get(self, share_link, **kwargs):  # noqa: E501
        """通过分享链接获取店铺ID/Get Shop ID by Share Link  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取店铺ID ### 参数: - share_link: 分享链接 ### 返回: - 店铺ID  # [English] ### Purpose: - Get Shop ID by Share Link ### Parameters: - share_link: Share link ### Return: - Shop ID  # [示例/Example] share_link = \"https://vt.tiktok.com/ZT2AHoGsE/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get_with_http_info(share_link, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get_with_http_info(share_link, **kwargs)  # noqa: E501
            return data

    def fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get_with_http_info(self, share_link, **kwargs):  # noqa: E501
        """通过分享链接获取店铺ID/Get Shop ID by Share Link  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取店铺ID ### 参数: - share_link: 分享链接 ### 返回: - 店铺ID  # [English] ### Purpose: - Get Shop ID by Share Link ### Parameters: - share_link: Share link ### Return: - Shop ID  # [示例/Example] share_link = \"https://vt.tiktok.com/ZT2AHoGsE/\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get_with_http_info(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: 分享链接/Share link (required)
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
                    " to method fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_link' is set
        if self.api_client.client_side_validation and ('share_link' not in params or
                                                       params['share_link'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_link` when calling `fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get`")  # noqa: E501

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
            '/api/v1/tiktok/app/v3/fetch_shop_id_by_share_link', 'GET',
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

    def fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get(self, shop_id, **kwargs):  # noqa: E501
        """获取商家信息数据/Get shop information data  # noqa: E501

        # [中文] ### 用途: - 获取商家信息数据 ### 参数: - shop_id: 商家id,店铺id ### 返回: - 商家信息数据  # [English] ### Purpose: - Get shop information data ### Parameters: - shop_id: Seller id, shop id ### Return: - Shop information data  # [示例/Example] shop_id = \"8646942781241463007\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get(shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object shop_id: 商家id,店铺id/Seller id, shop id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get_with_http_info(shop_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get_with_http_info(shop_id, **kwargs)  # noqa: E501
            return data

    def fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get_with_http_info(self, shop_id, **kwargs):  # noqa: E501
        """获取商家信息数据/Get shop information data  # noqa: E501

        # [中文] ### 用途: - 获取商家信息数据 ### 参数: - shop_id: 商家id,店铺id ### 返回: - 商家信息数据  # [English] ### Purpose: - Get shop information data ### Parameters: - shop_id: Seller id, shop id ### Return: - Shop information data  # [示例/Example] shop_id = \"8646942781241463007\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get_with_http_info(shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object shop_id: 商家id,店铺id/Seller id, shop id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shop_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shop_id' is set
        if self.api_client.client_side_validation and ('shop_id' not in params or
                                                       params['shop_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `shop_id` when calling `fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'shop_id' in params:
            query_params.append(('shop_id', params['shop_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_shop_info', 'GET',
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

    def fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get(self, seller_id, **kwargs):  # noqa: E501
        """获取商家产品分类数据/Get shop product category data  # noqa: E501

        # [中文] ### 用途: - 获取商家产品分类数据 ### 参数: - seller_id: 商家id,店铺id ### 返回: - 商家产品分类数据  # [English] ### Purpose: - Get shop product category data ### Parameters: - seller_id: Seller id, shop id ### Return: - Shop product category data  # [示例/Example] seller_id = \"7495294980909468039\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get_with_http_info(seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get_with_http_info(seller_id, **kwargs)  # noqa: E501
            return data

    def fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """获取商家产品分类数据/Get shop product category data  # noqa: E501

        # [中文] ### 用途: - 获取商家产品分类数据 ### 参数: - seller_id: 商家id,店铺id ### 返回: - 商家产品分类数据  # [English] ### Purpose: - Get shop product category data ### Parameters: - seller_id: Seller id, shop id ### Return: - Shop product category data  # [示例/Example] seller_id = \"7495294980909468039\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['seller_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in params or
                                                       params['seller_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `seller_id` when calling `fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in params:
            query_params.append(('seller_id', params['seller_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_shop_product_category', 'GET',
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

    def fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get(self, seller_id, **kwargs):  # noqa: E501
        """获取商家商品列表数据/Get shop product list data  # noqa: E501

        # [中文] ### 用途: - 获取商家商品列表数据 ### 参数: - seller_id: 商家id,店铺id - scroll_params: 滚动参数，用于加载更多商品数据 - page_size: 每页数量 - sort_field: 排序字段     - 1: 综合排序     - 3: 最新发布     - 4: 销量最好     - 5: 价格排序 - sort_order: 排序方式     - 0: 默认价格排序     - 1: 价格从高到低     - 2: 价格从低到高 ### 返回: - 商家商品列表数据  # [English] ### Purpose: - Get shop product list data ### Parameters: - seller_id: Seller id, shop id - scroll_params: Scroll parameter, used to load more product data - page_size: Number per page - sort_field: Sorting field     - 1: Comprehensive sorting     - 3: Latest release     - 4: Best sales     - 5: Price sorting - sort_order: Sorting method     - 0: Default price sorting     - 1: Price high to low     - 2: Price low to high ### Return: - Shop product list data  # [示例/Example] seller_id = \"8646929864612614278\" scroll_params = \"\" page_size = 10 sort_field = 1 sort_order = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :param object scroll_params: 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data
        :param object page_size: 每页数量/Number per page
        :param object sort_field: 排序字段/Sorting field
        :param object sort_order: 排序方式/Sorting method
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get_with_http_info(seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get_with_http_info(seller_id, **kwargs)  # noqa: E501
            return data

    def fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """获取商家商品列表数据/Get shop product list data  # noqa: E501

        # [中文] ### 用途: - 获取商家商品列表数据 ### 参数: - seller_id: 商家id,店铺id - scroll_params: 滚动参数，用于加载更多商品数据 - page_size: 每页数量 - sort_field: 排序字段     - 1: 综合排序     - 3: 最新发布     - 4: 销量最好     - 5: 价格排序 - sort_order: 排序方式     - 0: 默认价格排序     - 1: 价格从高到低     - 2: 价格从低到高 ### 返回: - 商家商品列表数据  # [English] ### Purpose: - Get shop product list data ### Parameters: - seller_id: Seller id, shop id - scroll_params: Scroll parameter, used to load more product data - page_size: Number per page - sort_field: Sorting field     - 1: Comprehensive sorting     - 3: Latest release     - 4: Best sales     - 5: Price sorting - sort_order: Sorting method     - 0: Default price sorting     - 1: Price high to low     - 2: Price low to high ### Return: - Shop product list data  # [示例/Example] seller_id = \"8646929864612614278\" scroll_params = \"\" page_size = 10 sort_field = 1 sort_order = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :param object scroll_params: 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data
        :param object page_size: 每页数量/Number per page
        :param object sort_field: 排序字段/Sorting field
        :param object sort_order: 排序方式/Sorting method
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['seller_id', 'scroll_params', 'page_size', 'sort_field', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in params or
                                                       params['seller_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `seller_id` when calling `fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in params:
            query_params.append(('seller_id', params['seller_id']))  # noqa: E501
        if 'scroll_params' in params:
            query_params.append(('scroll_params', params['scroll_params']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('sort_field', params['sort_field']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_shop_product_list', 'GET',
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

    def fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get(self, seller_id, **kwargs):  # noqa: E501
        """获取商家商品列表数据 V2/Get shop product list data V2  # noqa: E501

        # [中文] ### 用途: - 获取商家商品列表数据 ### 参数: - seller_id: 商家id,店铺id - scroll_params: 滚动参数，用于加载更多商品数据 - page_size: 每页数量 - sort_field: 排序字段     - 1: 综合排序     - 3: 最新发布     - 4: 销量最好     - 5: 价格排序 - sort_order: 排序方式     - 0: 默认价格排序     - 1: 价格从高到低     - 2: 价格从低到高 ### 返回: - 商家商品列表数据  # [English] ### Purpose: - Get shop product list data ### Parameters: - seller_id: Seller id, shop id - scroll_params: Scroll parameter, used to load more product data - page_size: Number per page - sort_field: Sorting field     - 1: Comprehensive sorting     - 3: Latest release     - 4: Best sales     - 5: Price sorting - sort_order: Sorting method     - 0: Default price sorting     - 1: Price high to low     - 2: Price low to high ### Return: - Shop product list data  # [示例/Example] seller_id = \"8646929864612614278\" scroll_params = \"\" page_size = 10 sort_field = 1 sort_order = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :param object scroll_params: 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data
        :param object page_size: 每页数量/Number per page
        :param object sort_field: 排序字段/Sorting field
        :param object sort_order: 排序方式/Sorting method
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get_with_http_info(seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get_with_http_info(seller_id, **kwargs)  # noqa: E501
            return data

    def fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """获取商家商品列表数据 V2/Get shop product list data V2  # noqa: E501

        # [中文] ### 用途: - 获取商家商品列表数据 ### 参数: - seller_id: 商家id,店铺id - scroll_params: 滚动参数，用于加载更多商品数据 - page_size: 每页数量 - sort_field: 排序字段     - 1: 综合排序     - 3: 最新发布     - 4: 销量最好     - 5: 价格排序 - sort_order: 排序方式     - 0: 默认价格排序     - 1: 价格从高到低     - 2: 价格从低到高 ### 返回: - 商家商品列表数据  # [English] ### Purpose: - Get shop product list data ### Parameters: - seller_id: Seller id, shop id - scroll_params: Scroll parameter, used to load more product data - page_size: Number per page - sort_field: Sorting field     - 1: Comprehensive sorting     - 3: Latest release     - 4: Best sales     - 5: Price sorting - sort_order: Sorting method     - 0: Default price sorting     - 1: Price high to low     - 2: Price low to high ### Return: - Shop product list data  # [示例/Example] seller_id = \"8646929864612614278\" scroll_params = \"\" page_size = 10 sort_field = 1 sort_order = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :param object scroll_params: 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data
        :param object page_size: 每页数量/Number per page
        :param object sort_field: 排序字段/Sorting field
        :param object sort_order: 排序方式/Sorting method
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['seller_id', 'scroll_params', 'page_size', 'sort_field', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in params or
                                                       params['seller_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `seller_id` when calling `fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in params:
            query_params.append(('seller_id', params['seller_id']))  # noqa: E501
        if 'scroll_params' in params:
            query_params.append(('scroll_params', params['scroll_params']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('sort_field', params['sort_field']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_shop_product_list_v2', 'GET',
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

    def fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get(self, seller_id, **kwargs):  # noqa: E501
        """获取商家商品推荐数据/Get shop product recommend data  # noqa: E501

        # [中文] ### 用途: - 获取商家商品推荐数据 ### 参数: - seller_id: 商家id,店铺id - scroll_param: 滚动参数，用于加载更多商品数据 - page_size: 每页数量 ### 返回: - 商家商品推荐数据  # [English] ### Purpose: - Get shop product recommend data ### Parameters: - seller_id: Seller id, shop id - scroll_param: Scroll parameter, used to load more product data - page_size: Number per page ### Return: - Shop product recommend data  # [示例/Example] seller_id = \"8646929864612614278\" scroll_param = \"\" page_size = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :param object scroll_param: 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data
        :param object page_size: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get_with_http_info(seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get_with_http_info(seller_id, **kwargs)  # noqa: E501
            return data

    def fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """获取商家商品推荐数据/Get shop product recommend data  # noqa: E501

        # [中文] ### 用途: - 获取商家商品推荐数据 ### 参数: - seller_id: 商家id,店铺id - scroll_param: 滚动参数，用于加载更多商品数据 - page_size: 每页数量 ### 返回: - 商家商品推荐数据  # [English] ### Purpose: - Get shop product recommend data ### Parameters: - seller_id: Seller id, shop id - scroll_param: Scroll parameter, used to load more product data - page_size: Number per page ### Return: - Shop product recommend data  # [示例/Example] seller_id = \"8646929864612614278\" scroll_param = \"\" page_size = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 商家id,店铺id/Seller id, shop id (required)
        :param object scroll_param: 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data
        :param object page_size: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['seller_id', 'scroll_param', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in params or
                                                       params['seller_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `seller_id` when calling `fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in params:
            query_params.append(('seller_id', params['seller_id']))  # noqa: E501
        if 'scroll_param' in params:
            query_params.append(('scroll_param', params['scroll_param']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_shop_product_recommend', 'GET',
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

    def fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取类似用户推荐/Similar User Recommendations  # noqa: E501

        # [中文] ### 用途: - 获取类似用户推荐 ### 参数: - sec_uid: 用户sec_uid - page_token: 分页标记，第一次请求时不需要传递，后续请求时传递上一次响应中的next_page_token值。 ### 返回: - 类似用户推荐  # [English] ### Purpose: - Similar User Recommendations ### Parameters: - sec_uid: User sec_uid - page_token: Page token, not required for the first request, for subsequent requests, pass the next_page_token value from the previous response. ### Return: - Similar User Recommendations  # [示例/Example] sec_uid = \"MS4wLjABAAAA2_YTgxz3kLb2XoyC3xOXnosim3gdiqMtFHnjRvckabZJFQ40XBOVttDCiB5cwa3b\" page_token = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_uid/User sec_uid (required)
        :param object page_token: 分页标记/Page token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取类似用户推荐/Similar User Recommendations  # noqa: E501

        # [中文] ### 用途: - 获取类似用户推荐 ### 参数: - sec_uid: 用户sec_uid - page_token: 分页标记，第一次请求时不需要传递，后续请求时传递上一次响应中的next_page_token值。 ### 返回: - 类似用户推荐  # [English] ### Purpose: - Similar User Recommendations ### Parameters: - sec_uid: User sec_uid - page_token: Page token, not required for the first request, for subsequent requests, pass the next_page_token value from the previous response. ### Return: - Similar User Recommendations  # [示例/Example] sec_uid = \"MS4wLjABAAAA2_YTgxz3kLb2XoyC3xOXnosim3gdiqMtFHnjRvckabZJFQ40XBOVttDCiB5cwa3b\" page_token = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_uid/User sec_uid (required)
        :param object page_token: 分页标记/Page token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_similar_user_recommendations', 'GET',
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

    def fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get(self, username, **kwargs):  # noqa: E501
        """通过用户名获取用户账号国家地区/Get user account country by username  # noqa: E501

        # [中文] ### 用途: - 通过用户名获取用户账号国家地区 ### 参数: - username: 用户名，可以从用户主页链接中获取，例如：https://www.tiktok.com/@tiktok，用户名即为tiktok。 ### 返回: - 用户账号国家地区  # [English] ### Purpose: - Get user account country by username ### Parameters: - username: Username, which can be obtained from the user's homepage link, for example: https://www.tiktok.com/@tiktok, the username is tiktok. ### Return: - User account country  # [示例/Example] username = \"tiktok\"  # 响应示例/Response Example ```json {'username': 'tiktok', 'username_modify_time': 1760985494, 'user_id': '107955', 'sec_user_id': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM', 'country': 'US', 'api_version': 'v1'} ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """通过用户名获取用户账号国家地区/Get user account country by username  # noqa: E501

        # [中文] ### 用途: - 通过用户名获取用户账号国家地区 ### 参数: - username: 用户名，可以从用户主页链接中获取，例如：https://www.tiktok.com/@tiktok，用户名即为tiktok。 ### 返回: - 用户账号国家地区  # [English] ### Purpose: - Get user account country by username ### Parameters: - username: Username, which can be obtained from the user's homepage link, for example: https://www.tiktok.com/@tiktok, the username is tiktok. ### Return: - User account country  # [示例/Example] username = \"tiktok\"  # 响应示例/Response Example ```json {'username': 'tiktok', 'username_modify_time': 1760985494, 'user_id': '107955', 'sec_user_id': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM', 'country': 'US', 'api_version': 'v1'} ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get_with_http_info(username, async_req=True)
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
                    " to method fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get`")  # noqa: E501

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
            '/api/v1/tiktok/app/v3/fetch_user_country_by_username', 'GET',
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

    def fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get(self, **kwargs):  # noqa: E501
        """获取指定用户的粉丝列表数据/Get follower list of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的粉丝列表数据 ### 参数: - user_id: 用户ID，这是一个纯数字版本的用户ID (与sec_user_id二选一/One of user_id and sec_user_id) - sec_user_id: 用户sec_user_id，这是一个混合字母和数字的版本ID (与user_id二选一/One of user_id and sec_user_id) - count: 数量，不要超过20，保持固定。 - min_time: 最小时间，用于翻页，第一次请求使用默认值0，后续请求使用上一次请求返回的min_time值。 - page_token: 翻页token，第一次请求使用默认值\"\"，后续请求使用上一次请求返回的page_token值。 ### 返回: - 粉丝列表数据  # [English] ### Purpose: - Get follower list of specified user ### Parameters: - user_id: User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id) - sec_user_id: User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id) - count: Number, do not exceed 20, keep it fixed. - min_time: Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests. - page_token: Page token, use default value \"\" for the first request, and use the page_token value returned by the last request for subsequent requests. ### Return: - Follower list data  # [示例/Example] user_id = \"7486586574684881927\" sec_user_id = \"MS4wLjABAAAA0lKrE0cVLLZCnVil-n-YEZlOoik9oeO3zOYQ08dqOEOw2pRSXWJdcSFw7lZeZcSP\" count = 20 min_time = 0 page_token = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (与sec_user_id二选一/One of user_id and sec_user_id)
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (与user_id二选一/One of user_id and sec_user_id)
        :param object count: 数量/Number
        :param object min_time: 最小时间，用于翻页/Minimum time for paging
        :param object page_token: 翻页token/Page token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取指定用户的粉丝列表数据/Get follower list of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的粉丝列表数据 ### 参数: - user_id: 用户ID，这是一个纯数字版本的用户ID (与sec_user_id二选一/One of user_id and sec_user_id) - sec_user_id: 用户sec_user_id，这是一个混合字母和数字的版本ID (与user_id二选一/One of user_id and sec_user_id) - count: 数量，不要超过20，保持固定。 - min_time: 最小时间，用于翻页，第一次请求使用默认值0，后续请求使用上一次请求返回的min_time值。 - page_token: 翻页token，第一次请求使用默认值\"\"，后续请求使用上一次请求返回的page_token值。 ### 返回: - 粉丝列表数据  # [English] ### Purpose: - Get follower list of specified user ### Parameters: - user_id: User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id) - sec_user_id: User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id) - count: Number, do not exceed 20, keep it fixed. - min_time: Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests. - page_token: Page token, use default value \"\" for the first request, and use the page_token value returned by the last request for subsequent requests. ### Return: - Follower list data  # [示例/Example] user_id = \"7486586574684881927\" sec_user_id = \"MS4wLjABAAAA0lKrE0cVLLZCnVil-n-YEZlOoik9oeO3zOYQ08dqOEOw2pRSXWJdcSFw7lZeZcSP\" count = 20 min_time = 0 page_token = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (与sec_user_id二选一/One of user_id and sec_user_id)
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (与user_id二选一/One of user_id and sec_user_id)
        :param object count: 数量/Number
        :param object min_time: 最小时间，用于翻页/Minimum time for paging
        :param object page_token: 翻页token/Page token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'sec_user_id', 'count', 'min_time', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'min_time' in params:
            query_params.append(('min_time', params['min_time']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_user_follower_list', 'GET',
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

    def fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get(self, **kwargs):  # noqa: E501
        """获取指定用户的关注列表数据/Get following list of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的关注列表数据 ### 参数: - user_id: 用户ID，这是一个纯数字版本的用户ID (与sec_user_id二选一/One of user_id and sec_user_id) - sec_user_id: 用户sec_user_id，这是一个混合字母和数字的版本ID (与user_id二选一/One of user_id and sec_user_id) - count: 数量，不要超过20，保持固定。 - min_time: 最小时间，用于翻页，第一次请求使用默认值0，后续请求使用上一次请求返回的min_time值。 - page_token: 翻页token，第一次请求使用默认值\"\"，后续请求使用上一次请求返回的page_token值。 ### 返回: - 关注列表数据  # [English] ### Purpose: - Get following list of specified user ### Parameters: - user_id: User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id) - sec_user_id: User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id) - count: Number, do not exceed 20, keep it fixed. - min_time: Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests. - page_token: Page token, use default value \"\" for the first request, and use the page_token value returned by the last request for subsequent requests. ### Return: - Following list data  # [示例/Example] user_id = \"7486586574684881927\" sec_user_id = \"MS4wLjABAAAA0lKrE0cVLLZCnVil-n-YEZlOoik9oeO3zOYQ08dqOEOw2pRSXWJdcSFw7lZeZcSP\" count = 20 min_time = 0 page_token = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (与sec_user_id二选一/One of user_id and sec_user_id)
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (与user_id二选一/One of user_id and sec_user_id)
        :param object count: 数量/Number
        :param object min_time: 最小时间，用于翻页/Minimum time for paging
        :param object page_token: 翻页token/Page token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取指定用户的关注列表数据/Get following list of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的关注列表数据 ### 参数: - user_id: 用户ID，这是一个纯数字版本的用户ID (与sec_user_id二选一/One of user_id and sec_user_id) - sec_user_id: 用户sec_user_id，这是一个混合字母和数字的版本ID (与user_id二选一/One of user_id and sec_user_id) - count: 数量，不要超过20，保持固定。 - min_time: 最小时间，用于翻页，第一次请求使用默认值0，后续请求使用上一次请求返回的min_time值。 - page_token: 翻页token，第一次请求使用默认值\"\"，后续请求使用上一次请求返回的page_token值。 ### 返回: - 关注列表数据  # [English] ### Purpose: - Get following list of specified user ### Parameters: - user_id: User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id) - sec_user_id: User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id) - count: Number, do not exceed 20, keep it fixed. - min_time: Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests. - page_token: Page token, use default value \"\" for the first request, and use the page_token value returned by the last request for subsequent requests. ### Return: - Following list data  # [示例/Example] user_id = \"7486586574684881927\" sec_user_id = \"MS4wLjABAAAA0lKrE0cVLLZCnVil-n-YEZlOoik9oeO3zOYQ08dqOEOw2pRSXWJdcSFw7lZeZcSP\" count = 20 min_time = 0 page_token = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (与sec_user_id二选一/One of user_id and sec_user_id)
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (与user_id二选一/One of user_id and sec_user_id)
        :param object count: 数量/Number
        :param object min_time: 最小时间，用于翻页/Minimum time for paging
        :param object page_token: 翻页token/Page token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'sec_user_id', 'count', 'min_time', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'min_time' in params:
            query_params.append(('min_time', params['min_time']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_user_following_list', 'GET',
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

    def fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get(self, sec_user_id, **kwargs):  # noqa: E501
        """获取用户喜欢作品数据/Get user like video data  # noqa: E501

        # [中文] ### 用途: - 获取用户喜欢作品数据 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user like video data ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAA-RkTGCGXLuLKRM5Xcuuwm7Mclg51I2ECO1RqOA7mJHuXFz99nztdi077Z2XmYHZV\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object counts: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get_with_http_info(sec_user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get_with_http_info(self, sec_user_id, **kwargs):  # noqa: E501
        """获取用户喜欢作品数据/Get user like video data  # noqa: E501

        # [中文] ### 用途: - 获取用户喜欢作品数据 ### 参数: - sec_user_id: 用户sec_user_id - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user like video data ### Parameters: - sec_user_id: User sec_user_id - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAA-RkTGCGXLuLKRM5Xcuuwm7Mclg51I2ECO1RqOA7mJHuXFz99nztdi077Z2XmYHZV\" max_cursor = 0 counts = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get_with_http_info(sec_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id (required)
        :param object max_cursor: 最大游标/Maximum cursor
        :param object counts: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'max_cursor', 'counts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_user_id' is set
        if self.api_client.client_side_validation and ('sec_user_id' not in params or
                                                       params['sec_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_user_id` when calling `fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'max_cursor' in params:
            query_params.append(('max_cursor', params['max_cursor']))  # noqa: E501
        if 'counts' in params:
            query_params.append(('counts', params['counts']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_user_like_videos', 'GET',
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

    def fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户音乐列表数据/Get user music list data  # noqa: E501

        # [中文] ### 用途: - 获取用户音乐列表数据 ### 参数: - sec_uid: 用户sec_uid - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 ### 返回: - 用户音乐列表数据  # [English] ### Purpose: - Get user music list data ### Parameters: - sec_uid: User sec_uid - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number  # [示例/Example] sec_uid = \"MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6\" cursor = 0 count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_uid/User sec_uid (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户音乐列表数据/Get user music list data  # noqa: E501

        # [中文] ### 用途: - 获取用户音乐列表数据 ### 参数: - sec_uid: 用户sec_uid - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 ### 返回: - 用户音乐列表数据  # [English] ### Purpose: - Get user music list data ### Parameters: - sec_uid: User sec_uid - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number  # [示例/Example] sec_uid = \"MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6\" cursor = 0 count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户sec_uid/User sec_uid (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('sec_uid', params['sec_uid']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_user_music_list', 'GET',
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

    def fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get(self, **kwargs):  # noqa: E501
        """获取用户主页作品数据 V1/Get user homepage video data V1  # noqa: E501

        # [中文] ### 用途: - 获取用户主页作品数据 ### 参数: - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。 - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量，建议保持默认值20。 - sort_type: 排序类型，0-最新，1-热门 - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。 - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data ### Parameters: - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number - sort_type: Sort type, 0-Latest, 1-Hot - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority, the faster the speed, and it is recommended to use only sec_user_id to get user data. ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS\" max_cursor = 0 counts = 20 sort_type = 0 unique_id = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object unique_id: 用户unique_id/User unique_id
        :param object max_cursor: 最大游标/Maximum cursor
        :param object count: 每页数量/Number per page
        :param object sort_type: 排序类型/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户主页作品数据 V1/Get user homepage video data V1  # noqa: E501

        # [中文] ### 用途: - 获取用户主页作品数据 ### 参数: - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。 - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量，建议保持默认值20。 - sort_type: 排序类型，0-最新，1-热门 - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。 - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data ### Parameters: - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number - sort_type: Sort type, 0-Latest, 1-Hot - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority, the faster the speed, and it is recommended to use only sec_user_id to get user data. ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS\" max_cursor = 0 counts = 20 sort_type = 0 unique_id = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object unique_id: 用户unique_id/User unique_id
        :param object max_cursor: 最大游标/Maximum cursor
        :param object count: 每页数量/Number per page
        :param object sort_type: 排序类型/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'unique_id', 'max_cursor', 'count', 'sort_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'unique_id' in params:
            query_params.append(('unique_id', params['unique_id']))  # noqa: E501
        if 'max_cursor' in params:
            query_params.append(('max_cursor', params['max_cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_user_post_videos', 'GET',
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

    def fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get(self, **kwargs):  # noqa: E501
        """获取用户主页作品数据 V2/Get user homepage video data V2  # noqa: E501

        # [中文] ### 用途: - 获取用户主页作品数据 ### 参数: - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。 - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量，建议保持默认值20。 - sort_type: 排序类型，0-最新，1-热门 - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。 - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data ### Parameters: - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number - sort_type: Sort type, 0-Latest, 1-Hot - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority, the faster the speed, and it is recommended to use only sec_user_id to get user data. ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS\" max_cursor = 0 counts = 20 sort_type = 0 unique_id = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object unique_id: 用户unique_id/User unique_id
        :param object max_cursor: 最大游标/Maximum cursor
        :param object count: 每页数量/Number per page
        :param object sort_type: 排序类型/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户主页作品数据 V2/Get user homepage video data V2  # noqa: E501

        # [中文] ### 用途: - 获取用户主页作品数据 ### 参数: - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。 - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量，建议保持默认值20。 - sort_type: 排序类型，0-最新，1-热门 - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。 - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data ### Parameters: - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number - sort_type: Sort type, 0-Latest, 1-Hot - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority, the faster the speed, and it is recommended to use only sec_user_id to get user data. ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS\" max_cursor = 0 counts = 20 sort_type = 0 unique_id = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object unique_id: 用户unique_id/User unique_id
        :param object max_cursor: 最大游标/Maximum cursor
        :param object count: 每页数量/Number per page
        :param object sort_type: 排序类型/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'unique_id', 'max_cursor', 'count', 'sort_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'unique_id' in params:
            query_params.append(('unique_id', params['unique_id']))  # noqa: E501
        if 'max_cursor' in params:
            query_params.append(('max_cursor', params['max_cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_user_post_videos_v2', 'GET',
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

    def fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get(self, **kwargs):  # noqa: E501
        """获取用户主页作品数据 V3（精简数据-更快速）/Get user homepage video data V3 (simplified data - faster)  # noqa: E501

        # [中文] ### 用途: - 获取用户主页作品数据 ### 参数: - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。 - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量，建议保持默认值20。 - sort_type: 排序类型，0-最新，1-热门 - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。 - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data ### Parameters: - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number - sort_type: Sort type, 0-Latest, 1-Hot - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority, the faster the speed, and it is recommended to use only sec_user_id to get user data. ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS\" max_cursor = 0 counts = 20 sort_type = 0 unique_id = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object unique_id: 用户unique_id/User unique_id
        :param object max_cursor: 最大游标/Maximum cursor
        :param object count: 每页数量/Number per page
        :param object sort_type: 排序类型/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户主页作品数据 V3（精简数据-更快速）/Get user homepage video data V3 (simplified data - faster)  # noqa: E501

        # [中文] ### 用途: - 获取用户主页作品数据 ### 参数: - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。 - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。 - count: 最大数量，建议保持默认值20。 - sort_type: 排序类型，0-最新，1-热门 - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。 - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。 ### 返回: - 用户作品数据  # [English] ### Purpose: - Get user homepage video data ### Parameters: - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data. - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. - count: Maximum count number - sort_type: Sort type, 0-Latest, 1-Hot - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username. - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority, the faster the speed, and it is recommended to use only sec_user_id to get user data. ### Return: - User video data  # [示例/Example] sec_user_id = \"MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS\" max_cursor = 0 counts = 20 sort_type = 0 unique_id = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object unique_id: 用户unique_id/User unique_id
        :param object max_cursor: 最大游标/Maximum cursor
        :param object count: 每页数量/Number per page
        :param object sort_type: 排序类型/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_user_id', 'unique_id', 'max_cursor', 'count', 'sort_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'unique_id' in params:
            query_params.append(('unique_id', params['unique_id']))  # noqa: E501
        if 'max_cursor' in params:
            query_params.append(('max_cursor', params['max_cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_user_post_videos_v3', 'GET',
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

    def fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户转发的作品数据/Get user repost video data  # noqa: E501

        # [中文] ### 用途: - 获取用户转发的作品数据 ### 参数: - user_id: 用户id，可以通过 handler_user_profile 端点获取，响应中的关键字为uid。 - offset: 偏移量 - count: 数量 ### 返回: - 用户转发作品数据  # [English] ### Purpose: - Get user repost video data ### Parameters: - user_id: User id, which can be obtained through the handler_user_profile endpoint, with the keyword uid in the response. - offset: Offset - count: Number ### Return: - User repost video data  # [示例/Example] user_id = 107955 offset = 0 count = 21  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户转发的作品数据/Get user repost video data  # noqa: E501

        # [中文] ### 用途: - 获取用户转发的作品数据 ### 参数: - user_id: 用户id，可以通过 handler_user_profile 端点获取，响应中的关键字为uid。 - offset: 偏移量 - count: 数量 ### 返回: - 用户转发作品数据  # [English] ### Purpose: - Get user repost video data ### Parameters: - user_id: User id, which can be obtained through the handler_user_profile endpoint, with the keyword uid in the response. - offset: Offset - count: Number ### Return: - User repost video data  # [示例/Example] user_id = 107955 offset = 0 count = 21  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户id/User id (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'offset', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_user_repost_videos', 'GET',
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

    def fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的用户搜索结果/Get user search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的用户搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 - user_search_follower_count（根据粉丝数排序）:     - 空-不限制，     - ZERO_TO_ONE_K = 0-1K，     - ONE_K_TO_TEN_K-1K = 1K-10K，     - TEN_K_TO_ONE_H_K = 10K-100K，     - ONE_H_K_PLUS = 100K以上 - user_search_profile_type（根据账号类型排序）:     - 空-不限制，     - VERIFIED = 认证用户 - user_search_other_pref（根据其他偏好排序）:     - USERNAME = 根据用户名相关性 ### 返回: - 用户搜索结果  # [English] ### Purpose: - Get user search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset - count: Number - user_search_follower_count（Sort by number of followers）:     - Empty-Unlimited,     - ZERO_TO_ONE_K = 0-1K,     - ONE_K_TO_TEN_K-1K = 1K-10K,     - TEN_K_TO_ONE_H_K = 10K-100K,     - ONE_H_K_PLUS = 100K and above - user_search_profile_type（Sort by account type）:     - Empty-Unlimited,     - VERIFIED = Verified user - user_search_other_pref（Sort by other preferences）:     - USERNAME = Sort by username relevance ### Return: - User search results  # [示例/Example] keyword = \"Cat\" offset = 0 count = 20 user_search_follower_count = \"\" user_search_profile_type = \"\" user_search_other_pref = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object user_search_follower_count: 根据粉丝数排序/Sort by number of followers
        :param object user_search_profile_type: 根据账号类型排序/Sort by account type
        :param object user_search_other_pref: 根据其他偏好排序/Sort by other preferences
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的用户搜索结果/Get user search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的用户搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 - user_search_follower_count（根据粉丝数排序）:     - 空-不限制，     - ZERO_TO_ONE_K = 0-1K，     - ONE_K_TO_TEN_K-1K = 1K-10K，     - TEN_K_TO_ONE_H_K = 10K-100K，     - ONE_H_K_PLUS = 100K以上 - user_search_profile_type（根据账号类型排序）:     - 空-不限制，     - VERIFIED = 认证用户 - user_search_other_pref（根据其他偏好排序）:     - USERNAME = 根据用户名相关性 ### 返回: - 用户搜索结果  # [English] ### Purpose: - Get user search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset - count: Number - user_search_follower_count（Sort by number of followers）:     - Empty-Unlimited,     - ZERO_TO_ONE_K = 0-1K,     - ONE_K_TO_TEN_K-1K = 1K-10K,     - TEN_K_TO_ONE_H_K = 10K-100K,     - ONE_H_K_PLUS = 100K and above - user_search_profile_type（Sort by account type）:     - Empty-Unlimited,     - VERIFIED = Verified user - user_search_other_pref（Sort by other preferences）:     - USERNAME = Sort by username relevance ### Return: - User search results  # [示例/Example] keyword = \"Cat\" offset = 0 count = 20 user_search_follower_count = \"\" user_search_profile_type = \"\" user_search_other_pref = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object user_search_follower_count: 根据粉丝数排序/Sort by number of followers
        :param object user_search_profile_type: 根据账号类型排序/Sort by account type
        :param object user_search_other_pref: 根据其他偏好排序/Sort by other preferences
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'user_search_follower_count', 'user_search_profile_type', 'user_search_other_pref']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'user_search_follower_count' in params:
            query_params.append(('user_search_follower_count', params['user_search_follower_count']))  # noqa: E501
        if 'user_search_profile_type' in params:
            query_params.append(('user_search_profile_type', params['user_search_profile_type']))  # noqa: E501
        if 'user_search_other_pref' in params:
            query_params.append(('user_search_other_pref', params['user_search_other_pref']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_user_search_result', 'GET',
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

    def fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个视频评论数据/Get single video comments data  # noqa: E501

        # [中文] ### 用途: - 获取单个视频评论数据 ### 参数: - aweme_id: 作品id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 ### 返回: - 评论数据  # [English] ### Purpose: - Get single video comments data ### Parameters: - aweme_id: Video id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number ### Return: - Comments data  # [示例/Example] aweme_id = \"7326156045968067873\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取单个视频评论数据/Get single video comments data  # noqa: E501

        # [中文] ### 用途: - 获取单个视频评论数据 ### 参数: - aweme_id: 作品id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 ### 返回: - 评论数据  # [English] ### Purpose: - Get single video comments data ### Parameters: - aweme_id: Video id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number ### Return: - Comments data  # [示例/Example] aweme_id = \"7326156045968067873\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_video_comments', 'GET',
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

    def fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get(self, item_id, comment_id, **kwargs):  # noqa: E501
        """获取指定视频的评论回复数据/Get comment replies data of specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的评论回复数据 ### 参数: - item_id: 作品id - comment_id: 评论id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 ### 返回: - 评论回复数据  # [English] ### Purpose: - Get comment replies data of specified video ### Parameters: - item_id: Video id - comment_id: Comment id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number ### Return: - Comment replies data  # [示例/Example] aweme_id = \"7326156045968067873\" comment_id = \"7327061675382260482\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
        :param object comment_id: 评论id/Comment id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
            return data

    def fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get_with_http_info(self, item_id, comment_id, **kwargs):  # noqa: E501
        """获取指定视频的评论回复数据/Get comment replies data of specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的评论回复数据 ### 参数: - item_id: 作品id - comment_id: 评论id - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。 - count: 数量 ### 返回: - 评论回复数据  # [English] ### Purpose: - Get comment replies data of specified video ### Parameters: - item_id: Video id - comment_id: Comment id - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. - count: Number ### Return: - Comment replies data  # [示例/Example] aweme_id = \"7326156045968067873\" comment_id = \"7327061675382260482\" cursor = 0 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get_with_http_info(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
        :param object comment_id: 评论id/Comment id (required)
        :param object cursor: 游标/Cursor
        :param object count: 数量/Number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'comment_id', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_video_comment_replies', 'GET',
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

    def fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的视频搜索结果/Get video search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的视频搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 - sort_type: 0-相关度，1-最多点赞 - publish_time: 0-不限制，1-最近一天，7-最近一周，30-最近一个月，90-最近三个月，180-最近半年 - region: 地区，默认为US-美国，可选值请参考TikTok地区代码或ISO 3166-1 alpha-2国家代码。 ### 返回: - 视频搜索结果  # [English] ### Purpose: - Get video search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset - count: Number - sort_type: 0-Relatedness, 1-Most likes - publish_time: 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year - region: Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. ### Return: - Video search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = 0 publish_time = 0 region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object region: 地区/Region
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取指定关键词的视频搜索结果/Get video search results of specified keywords  # noqa: E501

        # [中文] ### 用途: - 获取指定关键词的视频搜索结果 ### 参数: - keyword: 关键词 - offset: 偏移量 - count: 数量 - sort_type: 0-相关度，1-最多点赞 - publish_time: 0-不限制，1-最近一天，7-最近一周，30-最近一个月，90-最近三个月，180-最近半年 - region: 地区，默认为US-美国，可选值请参考TikTok地区代码或ISO 3166-1 alpha-2国家代码。 ### 返回: - 视频搜索结果  # [English] ### Purpose: - Get video search results of specified keywords ### Parameters: - keyword: Keyword - offset: Offset - count: Number - sort_type: 0-Relatedness, 1-Most likes - publish_time: 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year - region: Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. ### Return: - Video search results  # [示例/Example] keyword = \"中华娘\" offset = 0 count = 20 sort_type = 0 publish_time = 0 region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :param object offset: 偏移量/Offset
        :param object count: 数量/Number
        :param object sort_type: 排序类型/Sort type
        :param object publish_time: 发布时间/Publish time
        :param object region: 地区/Region
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'count', 'sort_type', 'publish_time', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'publish_time' in params:
            query_params.append(('publish_time', params['publish_time']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_video_search_result', 'GET',
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

    def fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get(self, **kwargs):  # noqa: E501
        """获取指定 Webcast 用户的信息/Get information of specified Webcast user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户信息。 - user_id: 用户uid，可选参数，纯数字，如果使用请保持sec_user_id以及unique_id为空。 - 以上参数必须至少填写一个，优先级为sec_user_id > user_id，优先级越高速度越快。 ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id - user_id: User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. - At least one of the above parameters must be filled in, the priority is sec_user_id > user_id, the higher the priority, the faster the speed. ### Return: - User information  # [示例/Example] user_id = \"107955\" sec_user_id = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户uid （可选，纯数字）/User uid (optional, pure number)
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取指定 Webcast 用户的信息/Get information of specified Webcast user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户信息。 - user_id: 用户uid，可选参数，纯数字，如果使用请保持sec_user_id以及unique_id为空。 - 以上参数必须至少填写一个，优先级为sec_user_id > user_id，优先级越高速度越快。 ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id - user_id: User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. - At least one of the above parameters must be filled in, the priority is sec_user_id > user_id, the higher the priority, the faster the speed. ### Return: - User information  # [示例/Example] user_id = \"107955\" sec_user_id = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户uid （可选，纯数字）/User uid (optional, pure number)
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'sec_user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/fetch_webcast_user_info', 'GET',
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

    def get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get(self, username, **kwargs):  # noqa: E501
        """使用用户名获取用户 user_id 和 sec_user_id/Get user_id and sec_user_id by Username  # noqa: E501

        # [中文] ### 用途: - 使用用户名获取用户 user_id 和 sec_user_id ### 参数: - username: 用户名 ### 返回: - 用户 user_id 和 sec_user_id  # [English] ### Purpose: - Get user_id and sec_user_id by Username ### Parameters: - username: Username ### Return: - User user_id and sec_user_id  # [示例/Example] username = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """使用用户名获取用户 user_id 和 sec_user_id/Get user_id and sec_user_id by Username  # noqa: E501

        # [中文] ### 用途: - 使用用户名获取用户 user_id 和 sec_user_id ### 参数: - username: 用户名 ### 返回: - 用户 user_id 和 sec_user_id  # [English] ### Purpose: - Get user_id and sec_user_id by Username ### Parameters: - username: Username ### Return: - User user_id and sec_user_id  # [示例/Example] username = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get_with_http_info(username, async_req=True)
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
                    " to method get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get`")  # noqa: E501

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
            '/api/v1/tiktok/app/v3/get_user_id_and_sec_user_id_by_username', 'GET',
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

    def handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get(self, **kwargs):  # noqa: E501
        """获取指定用户的信息/Get information of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户信息。 - user_id: 用户uid，可选参数，纯数字，如果使用请保持sec_user_id以及unique_id为空。 - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户信息，unique_id也是用户的用户名，如果使用请保持sec_user_id以及user_id为空。 - 以上参数必须至少填写一个，优先级为sec_user_id > user_id > unique_id，优先级越高速度越快。 ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id - user_id: User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user information, unique_id is also the user's username, if used, please keep sec_user_id and user_id empty. - At least one of the above parameters must be filled in, the priority is sec_user_id > user_id > unique_id, the higher the priority, the faster the speed. ### Return: - User information  # [示例/Example] user_id = \"107955\" sec_user_id = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" unique_id = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户uid （可选，纯数字）/User uid (optional, pure number)
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object unique_id: 用户unique_id （用户名）/User unique_id (username)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取指定用户的信息/Get information of specified user  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的信息 ### 参数: - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户信息。 - user_id: 用户uid，可选参数，纯数字，如果使用请保持sec_user_id以及unique_id为空。 - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户信息，unique_id也是用户的用户名，如果使用请保持sec_user_id以及user_id为空。 - 以上参数必须至少填写一个，优先级为sec_user_id > user_id > unique_id，优先级越高速度越快。 ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - sec_user_id: User sec_user_id - user_id: User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty. - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user information, unique_id is also the user's username, if used, please keep sec_user_id and user_id empty. - At least one of the above parameters must be filled in, the priority is sec_user_id > user_id > unique_id, the higher the priority, the faster the speed. ### Return: - User information  # [示例/Example] user_id = \"107955\" sec_user_id = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" unique_id = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户uid （可选，纯数字）/User uid (optional, pure number)
        :param object sec_user_id: 用户sec_user_id/User sec_user_id
        :param object unique_id: 用户unique_id （用户名）/User unique_id (username)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'sec_user_id', 'unique_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'sec_user_id' in params:
            query_params.append(('sec_user_id', params['sec_user_id']))  # noqa: E501
        if 'unique_id' in params:
            query_params.append(('unique_id', params['unique_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/handler_user_profile', 'GET',
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

    def open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get(self, keyword, **kwargs):  # noqa: E501
        """生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果/Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result  # noqa: E501

        # [中文] ### 用途: - 生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果。  ### 参数: - keyword: 关键词 - 注意: 如果未能跳转，请确保APP已经在后台运行。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result  ### Parameters: - keyword: Keyword - Note: If you cannot jump, please make sure that the APP is running in the background  ### Return: - Share link  # [示例/Example] keyword = \"Evil0ctal\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果/Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result  # noqa: E501

        # [中文] ### 用途: - 生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果。  ### 参数: - keyword: 关键词 - 注意: 如果未能跳转，请确保APP已经在后台运行。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result  ### Parameters: - keyword: Keyword - Note: If you cannot jump, please make sure that the APP is running in the background  ### Return: - Share link  # [示例/Example] keyword = \"Evil0ctal\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 关键词/Keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/open_tiktok_app_to_keyword_search', 'GET',
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

    def open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get(self, uid, **kwargs):  # noqa: E501
        """生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信/Generate TikTok share link, call TikTok APP, and send private messages to specified users  # noqa: E501

        # [中文] ### 用途: - 生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信。  ### 参数: - uid: 用户id，从用户主页接口中获取。 - 注意: 如果未能跳转，请确保APP已经在后台运行。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate TikTok share link, call TikTok APP, and send private messages to specified users  ### Parameters: - uid: User id, obtained from the user profile interface. - Note: If you cannot jump, please make sure that the APP is running in the background.  ### Return: - Share link  # [示例/Example] uid = \"7059867056504407087\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信/Generate TikTok share link, call TikTok APP, and send private messages to specified users  # noqa: E501

        # [中文] ### 用途: - 生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信。  ### 参数: - uid: 用户id，从用户主页接口中获取。 - 注意: 如果未能跳转，请确保APP已经在后台运行。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate TikTok share link, call TikTok APP, and send private messages to specified users  ### Parameters: - uid: User id, obtained from the user profile interface. - Note: If you cannot jump, please make sure that the APP is running in the background.  ### Return: - Share link  # [示例/Example] uid = \"7059867056504407087\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/open_tiktok_app_to_send_private_message', 'GET',
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

    def open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get(self, uid, **kwargs):  # noqa: E501
        """生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页/Generate TikTok share link, call TikTok APP, and jump to the specified user profile  # noqa: E501

        # [中文] ### 用途: - 生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页。  ### 参数: - uid: 用户id，从用户主页接口中获取。 - 注意: 如果未能跳转，请确保APP已经在后台运行。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate TikTok share link, call TikTok APP, and jump to the specified user profile  ### Parameters: - uid: User id, obtained from the user profile interface. - Note: If you cannot jump, please make sure that the APP is running in the background.  ### Return: - Share link  # [示例/Example] uid = \"7059867056504407087\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页/Generate TikTok share link, call TikTok APP, and jump to the specified user profile  # noqa: E501

        # [中文] ### 用途: - 生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页。  ### 参数: - uid: 用户id，从用户主页接口中获取。 - 注意: 如果未能跳转，请确保APP已经在后台运行。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate TikTok share link, call TikTok APP, and jump to the specified user profile  ### Parameters: - uid: User id, obtained from the user profile interface. - Note: If you cannot jump, please make sure that the APP is running in the background.  ### Return: - Share link  # [示例/Example] uid = \"7059867056504407087\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/open_tiktok_app_to_user_profile', 'GET',
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

    def open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get(self, aweme_id, **kwargs):  # noqa: E501
        """生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页/Generate TikTok share link, call TikTok APP, and jump to the specified video details page  # noqa: E501

        # [中文] ### 用途: - 生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页。  ### 参数: - aweme_id: 作品id - 注意: 如果未能跳转，请确保APP已经在后台运行。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate TikTok share link, call TikTok APP, and jump to the specified video  ### Parameters: - aweme_id: Video id - Note: If you cannot jump, please make sure that the APP is running in the background  ### Return: - Share link  # [示例/Example] aweme_id = \"7440436579409153311\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页/Generate TikTok share link, call TikTok APP, and jump to the specified video details page  # noqa: E501

        # [中文] ### 用途: - 生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页。  ### 参数: - aweme_id: 作品id - 注意: 如果未能跳转，请确保APP已经在后台运行。  ### 返回: - 分享链接  # [English] ### Purpose: - Generate TikTok share link, call TikTok APP, and jump to the specified video  ### Parameters: - aweme_id: Video id - Note: If you cannot jump, please make sure that the APP is running in the background  ### Return: - Share link  # [示例/Example] aweme_id = \"7440436579409153311\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/open_tiktok_app_to_video_detail', 'GET',
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

    def search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get(self, user_id, keyword, **kwargs):  # noqa: E501
        """搜索粉丝列表/Search follower list  # noqa: E501

        # [中文] ### 用途: - 搜索指定用户的粉丝列表，可以用于查找某个用户的粉丝中是否有特定昵称的用户。 ### 参数: - user_id: 用户ID，这是一个纯数字版本的用户ID，可以先通过获取用户信息接口获取。 - keyword: 搜索关键词，用户的昵称中包含该关键词即可匹配 ### 返回: - 搜索结果列表  # [English] ### Purpose: - Search follower list of specified user, can be used to find whether there is a user with a specific nickname in the followers of a certain user. ### Parameters: - user_id: User ID, this is a pure numeric version of the user ID, which can be obtained through the get user info API. - keyword: Search keyword, the user's nickname contains the keyword to match. ### Return: - Search result list  # [示例/Example] user_id = \"7540849481009988663\" keyword = \"a\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get(user_id, keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get_with_http_info(user_id, keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get_with_http_info(user_id, keyword, **kwargs)  # noqa: E501
            return data

    def search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get_with_http_info(self, user_id, keyword, **kwargs):  # noqa: E501
        """搜索粉丝列表/Search follower list  # noqa: E501

        # [中文] ### 用途: - 搜索指定用户的粉丝列表，可以用于查找某个用户的粉丝中是否有特定昵称的用户。 ### 参数: - user_id: 用户ID，这是一个纯数字版本的用户ID，可以先通过获取用户信息接口获取。 - keyword: 搜索关键词，用户的昵称中包含该关键词即可匹配 ### 返回: - 搜索结果列表  # [English] ### Purpose: - Search follower list of specified user, can be used to find whether there is a user with a specific nickname in the followers of a certain user. ### Parameters: - user_id: User ID, this is a pure numeric version of the user ID, which can be obtained through the get user info API. - keyword: Search keyword, the user's nickname contains the keyword to match. ### Return: - Search result list  # [示例/Example] user_id = \"7540849481009988663\" keyword = \"a\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get_with_http_info(user_id, keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get`")  # noqa: E501
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/search_follower_list', 'GET',
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

    def search_following_list_api_v1_tiktok_app_v3_search_following_list_get(self, user_id, keyword, **kwargs):  # noqa: E501
        """搜索关注列表/Search following list  # noqa: E501

        # [中文] ### 用途: - 搜索指定用户的关注列表，可以用于查找某个用户的关注中是否有特定昵称的用户。 ### 参数: - user_id: 用户ID，这是一个纯数字版本的用户ID，可以先通过获取用户信息接口获取。 - keyword: 搜索关键词，用户的昵称中包含该关键词即可匹配。 ### 返回: - 搜索结果列表  # [English] ### Purpose: - Search following list of specified user, can be used to find whether there is a user with a specific nickname in the following of a certain user. ### Parameters: - user_id: User ID, this is a pure numeric version of the user ID, which can be obtained through the get user info API. - keyword: Search keyword, the user's nickname contains the keyword to match. ### Return: - Search result list  # [示例/Example] user_id = \"7540849481009988663\" keyword = \"a\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_following_list_api_v1_tiktok_app_v3_search_following_list_get(user_id, keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_following_list_api_v1_tiktok_app_v3_search_following_list_get_with_http_info(user_id, keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_following_list_api_v1_tiktok_app_v3_search_following_list_get_with_http_info(user_id, keyword, **kwargs)  # noqa: E501
            return data

    def search_following_list_api_v1_tiktok_app_v3_search_following_list_get_with_http_info(self, user_id, keyword, **kwargs):  # noqa: E501
        """搜索关注列表/Search following list  # noqa: E501

        # [中文] ### 用途: - 搜索指定用户的关注列表，可以用于查找某个用户的关注中是否有特定昵称的用户。 ### 参数: - user_id: 用户ID，这是一个纯数字版本的用户ID，可以先通过获取用户信息接口获取。 - keyword: 搜索关键词，用户的昵称中包含该关键词即可匹配。 ### 返回: - 搜索结果列表  # [English] ### Purpose: - Search following list of specified user, can be used to find whether there is a user with a specific nickname in the following of a certain user. ### Parameters: - user_id: User ID, this is a pure numeric version of the user ID, which can be obtained through the get user info API. - keyword: Search keyword, the user's nickname contains the keyword to match. ### Return: - Search result list  # [示例/Example] user_id = \"7540849481009988663\" keyword = \"a\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_following_list_api_v1_tiktok_app_v3_search_following_list_get_with_http_info(user_id, keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_following_list_api_v1_tiktok_app_v3_search_following_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `search_following_list_api_v1_tiktok_app_v3_search_following_list_get`")  # noqa: E501
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_following_list_api_v1_tiktok_app_v3_search_following_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/app/v3/search_following_list', 'GET',
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

    def t_tencrypt_algorithm_api_v1_tiktok_app_v3_t_tencrypt_algorithm_post(self, **kwargs):  # noqa: E501
        """TikTok APP加密算法/TikTok APP encryption algorithm  # noqa: E501

        # [中文] ### 用途: - TikTok APP加密算法，用于生成请求头中的加密参数。 - 生成的加密参数列表：     - `x-ladon`     - `x-khronos`     - `x-argus`     - `x-gorgon` （8404）  ### 参数: - url: 需要加密的完整URL - data: 如果接口是POST请求，请填写POST请求的数据参与加密计算，GET请求时传入空字符串即可。 - device_info: 设备信息，可选参数，如果不填写则使用默认设备信息，设备信息会修改传入的URL中的参数。  ### 返回: - 加密参数列表  # [English] ### Purpose: - TikTok APP encryption algorithm, used to generate encrypted parameters in the request header. - The generated encrypted parameter list:     - `x-ladon`     - `x-khronos`     - `x-argus`     - `x-gorgon` (8404)  ### Parameters: - url: Full URL to be encrypted - data: If the interface is a POST request, please fill in the data of the POST request to participate in the encryption calculation. For GET requests, pass an empty string. - device_info: Device information, optional parameter, if not filled in, the default device information will be used, and the device information will modify the parameters in the URL passed in.  ### Return: - Encrypted parameter list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.t_tencrypt_algorithm_api_v1_tiktok_app_v3_t_tencrypt_algorithm_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.t_tencrypt_algorithm_api_v1_tiktok_app_v3_t_tencrypt_algorithm_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.t_tencrypt_algorithm_api_v1_tiktok_app_v3_t_tencrypt_algorithm_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def t_tencrypt_algorithm_api_v1_tiktok_app_v3_t_tencrypt_algorithm_post_with_http_info(self, **kwargs):  # noqa: E501
        """TikTok APP加密算法/TikTok APP encryption algorithm  # noqa: E501

        # [中文] ### 用途: - TikTok APP加密算法，用于生成请求头中的加密参数。 - 生成的加密参数列表：     - `x-ladon`     - `x-khronos`     - `x-argus`     - `x-gorgon` （8404）  ### 参数: - url: 需要加密的完整URL - data: 如果接口是POST请求，请填写POST请求的数据参与加密计算，GET请求时传入空字符串即可。 - device_info: 设备信息，可选参数，如果不填写则使用默认设备信息，设备信息会修改传入的URL中的参数。  ### 返回: - 加密参数列表  # [English] ### Purpose: - TikTok APP encryption algorithm, used to generate encrypted parameters in the request header. - The generated encrypted parameter list:     - `x-ladon`     - `x-khronos`     - `x-argus`     - `x-gorgon` (8404)  ### Parameters: - url: Full URL to be encrypted - data: If the interface is a POST request, please fill in the data of the POST request to participate in the encryption calculation. For GET requests, pass an empty string. - device_info: Device information, optional parameter, if not filled in, the default device information will be used, and the device information will modify the parameters in the URL passed in.  ### Return: - Encrypted parameter list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.t_tencrypt_algorithm_api_v1_tiktok_app_v3_t_tencrypt_algorithm_post_with_http_info(async_req=True)
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
                    " to method t_tencrypt_algorithm_api_v1_tiktok_app_v3_t_tencrypt_algorithm_post" % key
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
            '/api/v1/tiktok/app/v3/TTencrypt_algorithm', 'POST',
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
