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


class TikTokInteractionAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def apply_for_scope_api_v1_tiktok_interaction_apply_get(self, api_key, invite_code, **kwargs):  # noqa: E501
        """申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)  # noqa: E501

        # [通知] - 此接口已经废弃，用户现在无需手动申请调用权限，只需要在用户后台更新API Key的对应权限即可，即API Key对应的的Scope。 # [中文] ### 接口用途: - 申请使用TikTok交互API的接口权限（Scope），请在使用交互类接口之前申请，否则将无法正常请求。 ### 申请流程: - 申请接口权限需要邀请码，如果你没有邀请码，可以在Discord服务器中联系管理员获取。 - Discord服务器链接: [TikHub Discord](https://discord.gg/aMEAS8Xsvz) ### 申请须知: - 此权限仅限于当前提交的API Key，不可跨API Key使用。 - 用户需要使用美国地区注册且有效的的TikTok账号进行登录，否则保证将无法正常请求。 - 用户需要使用美国地区的代理IP进行获取Cookie，否则将保证无法正常请求。 - 用户需要使用美国地区的代理IP进行请求，否则将无法保证正常请求。 ### 用户守则以及责任: - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 - 请不要将接口权限分享给他人，否则我们将会停止对你的服务。 - 接口请求目前暂时定为每秒5次请求。 ### 返回: - 申请结果以及申请的邀请码，请自行保留邀请码，以便后续使用。  # [Notice] - This interface has been deprecated, users no longer need to apply for permission to call the API, just update the corresponding permission of the API Key in the user background, that is, the Scope corresponding to the API Key. # [English] ### Purpose: - Apply for the interface permission (Scope) of TikTok Interaction API, please apply before using the interactive interface, otherwise the request will not be made normally. ### Application process: - Applying for interface permissions requires an invitation code, if you do not have an invitation code, you can contact the administrator on the Discord server. - Discord server link: [TikHub Discord](https://discord.gg/aMEAS8Xsvz) ### Application notes: - This permission is limited to the API Key submitted, and cannot be used across API Keys. - Users need to log in with a registered and valid TikTok account in the United States, otherwise the request will not be made normally. - Users need to use a proxy IP in the United States to obtain cookies, otherwise the request will not be made normally. - Users need to use a proxy IP in the United States for requests, otherwise the request will not be made normally. ### User guidelines and responsibilities: - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. - Please do not share the interface permission with others, otherwise we will stop providing services to you. - The interface request is currently set to 5 requests per second. ### Return: - Application results and the invitation code applied for, please keep the invitation code for subsequent use.  # [示例/Example] ```python # Python Code invite_code = \"Your_Invite_Code\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apply_for_scope_api_v1_tiktok_interaction_apply_get(api_key, invite_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object api_key: (required)
        :param object invite_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apply_for_scope_api_v1_tiktok_interaction_apply_get_with_http_info(api_key, invite_code, **kwargs)  # noqa: E501
        else:
            (data) = self.apply_for_scope_api_v1_tiktok_interaction_apply_get_with_http_info(api_key, invite_code, **kwargs)  # noqa: E501
            return data

    def apply_for_scope_api_v1_tiktok_interaction_apply_get_with_http_info(self, api_key, invite_code, **kwargs):  # noqa: E501
        """申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)  # noqa: E501

        # [通知] - 此接口已经废弃，用户现在无需手动申请调用权限，只需要在用户后台更新API Key的对应权限即可，即API Key对应的的Scope。 # [中文] ### 接口用途: - 申请使用TikTok交互API的接口权限（Scope），请在使用交互类接口之前申请，否则将无法正常请求。 ### 申请流程: - 申请接口权限需要邀请码，如果你没有邀请码，可以在Discord服务器中联系管理员获取。 - Discord服务器链接: [TikHub Discord](https://discord.gg/aMEAS8Xsvz) ### 申请须知: - 此权限仅限于当前提交的API Key，不可跨API Key使用。 - 用户需要使用美国地区注册且有效的的TikTok账号进行登录，否则保证将无法正常请求。 - 用户需要使用美国地区的代理IP进行获取Cookie，否则将保证无法正常请求。 - 用户需要使用美国地区的代理IP进行请求，否则将无法保证正常请求。 ### 用户守则以及责任: - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 - 请不要将接口权限分享给他人，否则我们将会停止对你的服务。 - 接口请求目前暂时定为每秒5次请求。 ### 返回: - 申请结果以及申请的邀请码，请自行保留邀请码，以便后续使用。  # [Notice] - This interface has been deprecated, users no longer need to apply for permission to call the API, just update the corresponding permission of the API Key in the user background, that is, the Scope corresponding to the API Key. # [English] ### Purpose: - Apply for the interface permission (Scope) of TikTok Interaction API, please apply before using the interactive interface, otherwise the request will not be made normally. ### Application process: - Applying for interface permissions requires an invitation code, if you do not have an invitation code, you can contact the administrator on the Discord server. - Discord server link: [TikHub Discord](https://discord.gg/aMEAS8Xsvz) ### Application notes: - This permission is limited to the API Key submitted, and cannot be used across API Keys. - Users need to log in with a registered and valid TikTok account in the United States, otherwise the request will not be made normally. - Users need to use a proxy IP in the United States to obtain cookies, otherwise the request will not be made normally. - Users need to use a proxy IP in the United States for requests, otherwise the request will not be made normally. ### User guidelines and responsibilities: - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. - Please do not share the interface permission with others, otherwise we will stop providing services to you. - The interface request is currently set to 5 requests per second. ### Return: - Application results and the invitation code applied for, please keep the invitation code for subsequent use.  # [示例/Example] ```python # Python Code invite_code = \"Your_Invite_Code\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apply_for_scope_api_v1_tiktok_interaction_apply_get_with_http_info(api_key, invite_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object api_key: (required)
        :param object invite_code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'invite_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apply_for_scope_api_v1_tiktok_interaction_apply_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in params or
                                                       params['api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `api_key` when calling `apply_for_scope_api_v1_tiktok_interaction_apply_get`")  # noqa: E501
        # verify the required parameter 'invite_code' is set
        if self.api_client.client_side_validation and ('invite_code' not in params or
                                                       params['invite_code'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `invite_code` when calling `apply_for_scope_api_v1_tiktok_interaction_apply_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))  # noqa: E501
        if 'invite_code' in params:
            query_params.append(('invite_code', params['invite_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/interaction/apply', 'GET',
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

    def collect_api_v1_tiktok_interaction_collect_post(self, **kwargs):  # noqa: E501
        """收藏/Collect  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie收藏指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Collect a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Like results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.collect_api_v1_tiktok_interaction_collect_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.collect_api_v1_tiktok_interaction_collect_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.collect_api_v1_tiktok_interaction_collect_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def collect_api_v1_tiktok_interaction_collect_post_with_http_info(self, **kwargs):  # noqa: E501
        """收藏/Collect  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie收藏指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Collect a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Like results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.collect_api_v1_tiktok_interaction_collect_post_with_http_info(async_req=True)
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
                    " to method collect_api_v1_tiktok_interaction_collect_post" % key
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
            '/api/v1/tiktok/interaction/collect', 'POST',
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

    def follow_api_v1_tiktok_interaction_follow_post(self, **kwargs):  # noqa: E501
        """关注/Follow  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie关注指定用户，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - user_id: 用户id，可以从接口`/api/v1/tiktok/app/v3/handler_user_profile`获取。 - sec_user_id: 用户sec_id，可以从分接口`/api/v1/tiktok/web/get_sec_user_id`获取。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 关注结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Follow a specified user using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - user_id: User id, which can be obtained from the sub-interface `/api/v1/tiktok/app/v3/handler_user_profile`. - sec_user_id: User sec_id, which can be obtained from the sub-interface `/api/v1/tiktok/web/get_sec_user_id`. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Follow results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"user_id\": \"6881290705605477381\",     \"sec_user_id\": \"MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6\",     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.follow_api_v1_tiktok_interaction_follow_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.follow_api_v1_tiktok_interaction_follow_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.follow_api_v1_tiktok_interaction_follow_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def follow_api_v1_tiktok_interaction_follow_post_with_http_info(self, **kwargs):  # noqa: E501
        """关注/Follow  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie关注指定用户，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - user_id: 用户id，可以从接口`/api/v1/tiktok/app/v3/handler_user_profile`获取。 - sec_user_id: 用户sec_id，可以从分接口`/api/v1/tiktok/web/get_sec_user_id`获取。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 关注结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Follow a specified user using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - user_id: User id, which can be obtained from the sub-interface `/api/v1/tiktok/app/v3/handler_user_profile`. - sec_user_id: User sec_id, which can be obtained from the sub-interface `/api/v1/tiktok/web/get_sec_user_id`. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Follow results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"user_id\": \"6881290705605477381\",     \"sec_user_id\": \"MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6\",     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.follow_api_v1_tiktok_interaction_follow_post_with_http_info(async_req=True)
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
                    " to method follow_api_v1_tiktok_interaction_follow_post" % key
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
            '/api/v1/tiktok/interaction/follow', 'POST',
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

    def forward_api_v1_tiktok_interaction_forward_post(self, **kwargs):  # noqa: E501
        """转发/Forward  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie转发指定作品，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 关注结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Forward a specified post using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - sec_user_id: User sec_id, which can be obtained from the sub-interface `/api/v1/tiktok/web/get_sec_user_id`. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Follow results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"user_id\": \"6881290705605477381\",     \"sec_user_id\": \"MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6\",     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forward_api_v1_tiktok_interaction_forward_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.forward_api_v1_tiktok_interaction_forward_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.forward_api_v1_tiktok_interaction_forward_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def forward_api_v1_tiktok_interaction_forward_post_with_http_info(self, **kwargs):  # noqa: E501
        """转发/Forward  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie转发指定作品，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 关注结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Forward a specified post using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - sec_user_id: User sec_id, which can be obtained from the sub-interface `/api/v1/tiktok/web/get_sec_user_id`. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Follow results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"user_id\": \"6881290705605477381\",     \"sec_user_id\": \"MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6\",     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forward_api_v1_tiktok_interaction_forward_post_with_http_info(async_req=True)
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
                    " to method forward_api_v1_tiktok_interaction_forward_post" % key
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
            '/api/v1/tiktok/interaction/forward', 'POST',
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

    def like_api_v1_tiktok_interaction_like_post(self, **kwargs):  # noqa: E501
        """点赞/Like  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie点赞指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Like a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Like results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.like_api_v1_tiktok_interaction_like_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.like_api_v1_tiktok_interaction_like_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.like_api_v1_tiktok_interaction_like_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def like_api_v1_tiktok_interaction_like_post_with_http_info(self, **kwargs):  # noqa: E501
        """点赞/Like  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie点赞指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Like a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Like results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.like_api_v1_tiktok_interaction_like_post_with_http_info(async_req=True)
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
                    " to method like_api_v1_tiktok_interaction_like_post" % key
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
            '/api/v1/tiktok/interaction/like', 'POST',
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

    def post_comment_api_v1_tiktok_interaction_post_comment_post(self, **kwargs):  # noqa: E501
        """发送评论/Post comment  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie发送评论到指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - text: 评论内容，TikTok评论内容需要符合规范，不要带有违规的关键词，否则即使请求成功也会被系统判定为垃圾评论从而不被展示，提交时请使用URL编码评论字符串。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 发送评论结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Post comments to the specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - text: Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, otherwise, even if the request is successful, it will be judged as spam comments by the system and will not be displayed, please use URL-encoded comment string when submitting. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Post comment results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code text = urllib.parse.quote(\"Hello, TikTok!\") cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"text\": text,     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_comment_api_v1_tiktok_interaction_post_comment_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_comment_api_v1_tiktok_interaction_post_comment_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_comment_api_v1_tiktok_interaction_post_comment_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_comment_api_v1_tiktok_interaction_post_comment_post_with_http_info(self, **kwargs):  # noqa: E501
        """发送评论/Post comment  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie发送评论到指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - text: 评论内容，TikTok评论内容需要符合规范，不要带有违规的关键词，否则即使请求成功也会被系统判定为垃圾评论从而不被展示，提交时请使用URL编码评论字符串。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 发送评论结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Post comments to the specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - text: Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, otherwise, even if the request is successful, it will be judged as spam comments by the system and will not be displayed, please use URL-encoded comment string when submitting. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Post comment results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code text = urllib.parse.quote(\"Hello, TikTok!\") cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"text\": text,     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_comment_api_v1_tiktok_interaction_post_comment_post_with_http_info(async_req=True)
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
                    " to method post_comment_api_v1_tiktok_interaction_post_comment_post" % key
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
            '/api/v1/tiktok/interaction/post_comment', 'POST',
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

    def reply_comment_api_v1_tiktok_interaction_reply_comment_post(self, **kwargs):  # noqa: E501
        """回复评论/Reply to comment  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie回复指定视频的一个评论，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - reply_id: 要回复的目标评论ID，可以从指定视频的评论数据接口中获取，通常关键字为`cid`或`comment_id`或`reply_id`。 - text: 评论内容，TikTok评论内容需要符合规范，不要带有违规的关键词，否则即使请求成功也会被系统判定为垃圾评论从而不被展示，提交时请使用URL编码评论字符串。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 回复评论结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Reply to a comment on a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - reply_id: The target comment ID to reply to, which can be obtained from the comment data interface of the specified video, usually the keyword is `cid` or `comment_id` or `reply_id`. - text: Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, otherwise, even if the request is successful, it will be judged as spam comments by the system and will not be displayed, please use URL-encoded comment string when submitting. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Reply comment results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code text = urllib.parse.quote(\"Hello, TikTok!\") cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"reply_id\": \"7420673787547419435\",     \"text\": text,     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reply_comment_api_v1_tiktok_interaction_reply_comment_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reply_comment_api_v1_tiktok_interaction_reply_comment_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.reply_comment_api_v1_tiktok_interaction_reply_comment_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def reply_comment_api_v1_tiktok_interaction_reply_comment_post_with_http_info(self, **kwargs):  # noqa: E501
        """回复评论/Reply to comment  # noqa: E501

        # [中文] ### 用途: - 使用用户Cookie回复指定视频的一个评论，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - reply_id: 要回复的目标评论ID，可以从指定视频的评论数据接口中获取，通常关键字为`cid`或`comment_id`或`reply_id`。 - text: 评论内容，TikTok评论内容需要符合规范，不要带有违规的关键词，否则即使请求成功也会被系统判定为垃圾评论从而不被展示，提交时请使用URL编码评论字符串。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 回复评论结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Reply to a comment on a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - reply_id: The target comment ID to reply to, which can be obtained from the comment data interface of the specified video, usually the keyword is `cid` or `comment_id` or `reply_id`. - text: Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, otherwise, even if the request is successful, it will be judged as spam comments by the system and will not be displayed, please use URL-encoded comment string when submitting. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Reply comment results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code text = urllib.parse.quote(\"Hello, TikTok!\") cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"reply_id\": \"7420673787547419435\",     \"text\": text,     \"cookie\": cookie,     \"proxy\": \"\", } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reply_comment_api_v1_tiktok_interaction_reply_comment_post_with_http_info(async_req=True)
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
                    " to method reply_comment_api_v1_tiktok_interaction_reply_comment_post" % key
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
            '/api/v1/tiktok/interaction/reply_comment', 'POST',
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
