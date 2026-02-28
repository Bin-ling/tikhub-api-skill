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


class TikTokShopWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get(self, **kwargs):  # noqa: E501
        """获取热卖商品列表/Get hot selling products list  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop的热卖商品列表 - 返回当前最受欢迎的商品 ### 参数: - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // 热卖商品列表(最多1000个)             {                 \"product_id\": \"xxx\",                 \"title\": \"商品标题\",                 \"image\": \"商品图片\",                 \"price\": {},              // 价格信息                 \"rating\": {},             // 评分信息                 \"sales\": {},              // 销量信息                 \"rank\": 1                 // 热卖排名             }         ]     } } ```  # [English] ### Purpose: - Get TikTok Shop hot selling products list - Returns currently most popular products ### Parameters: - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // Hot selling products (up to 1000)             {                 \"product_id\": \"xxx\",                 \"title\": \"Product title\",                 \"image\": \"Product image\",                 \"price\": {},              // Price info                 \"rating\": {},             // Rating info                 \"sales\": {},              // Sales info                 \"rank\": 1                 // Hot selling rank             }         ]     } } ```  # [示例/Example] region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热卖商品列表/Get hot selling products list  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop的热卖商品列表 - 返回当前最受欢迎的商品 ### 参数: - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // 热卖商品列表(最多1000个)             {                 \"product_id\": \"xxx\",                 \"title\": \"商品标题\",                 \"image\": \"商品图片\",                 \"price\": {},              // 价格信息                 \"rating\": {},             // 评分信息                 \"sales\": {},              // 销量信息                 \"rank\": 1                 // 热卖排名             }         ]     } } ```  # [English] ### Purpose: - Get TikTok Shop hot selling products list - Returns currently most popular products ### Parameters: - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // Hot selling products (up to 1000)             {                 \"product_id\": \"xxx\",                 \"title\": \"Product title\",                 \"image\": \"Product image\",                 \"price\": {},              // Price info                 \"rating\": {},             // Rating info                 \"sales\": {},              // Sales info                 \"rank\": 1                 // Hot selling rank             }         ]     } } ```  # [示例/Example] region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_hot_selling_products_list', 'GET',
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

    def fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情V1(桌面端-数据完整)/Get product detail V1(Full data)  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop商品的详细信息 - 包含商品基本信息、价格、库存、评价、推荐商品等完整数据 - 某些特殊地区的商品可能无法获取到数据（如：泰国），如果遇到此情况请尝试使用 `fetch_product_detail_v3` 接口 ### 参数: - seller_id: 卖家ID (可传空字符串) - product_id: 商品ID (必填) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"global_fe_config\": {},      // 全局前端配置         \"components_map\": [],         // 组件映射列表         \"global_data\": {              // 全局数据             \"product_info\": {},       // 商品信息             \"seller_info\": {},        // 卖家信息             \"shipping_info\": {},      // 物流信息             \"review_info\": {}         // 评价信息         }     } } ```  # [English] ### Purpose: - Get detailed information of TikTok Shop products - Contains complete data including basic info, price, stock, reviews, recommendations - Some products from specific regions may not be accessible (e.g., Thailand); if so, try using `fetch_product_detail_v3` ### Parameters: - seller_id: Seller ID (can be empty string) - product_id: Product ID (required) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"global_fe_config\": {},      // Global frontend config         \"components_map\": [],         // Component mapping list         \"global_data\": {              // Global data             \"product_info\": {},       // Product information             \"seller_info\": {},        // Seller information             \"shipping_info\": {},      // Shipping information             \"review_info\": {}         // Review information         }     } } ```  # [示例/Example] seller_id = \"7495150558072178725\" product_id = \"1731088507416187562\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object seller_id: 卖家ID(可选)/Seller ID (optional)
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情V1(桌面端-数据完整)/Get product detail V1(Full data)  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop商品的详细信息 - 包含商品基本信息、价格、库存、评价、推荐商品等完整数据 - 某些特殊地区的商品可能无法获取到数据（如：泰国），如果遇到此情况请尝试使用 `fetch_product_detail_v3` 接口 ### 参数: - seller_id: 卖家ID (可传空字符串) - product_id: 商品ID (必填) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"global_fe_config\": {},      // 全局前端配置         \"components_map\": [],         // 组件映射列表         \"global_data\": {              // 全局数据             \"product_info\": {},       // 商品信息             \"seller_info\": {},        // 卖家信息             \"shipping_info\": {},      // 物流信息             \"review_info\": {}         // 评价信息         }     } } ```  # [English] ### Purpose: - Get detailed information of TikTok Shop products - Contains complete data including basic info, price, stock, reviews, recommendations - Some products from specific regions may not be accessible (e.g., Thailand); if so, try using `fetch_product_detail_v3` ### Parameters: - seller_id: Seller ID (can be empty string) - product_id: Product ID (required) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"global_fe_config\": {},      // Global frontend config         \"components_map\": [],         // Component mapping list         \"global_data\": {              // Global data             \"product_info\": {},       // Product information             \"seller_info\": {},        // Seller information             \"shipping_info\": {},      // Shipping information             \"review_info\": {}         // Review information         }     } } ```  # [示例/Example] seller_id = \"7495150558072178725\" product_id = \"1731088507416187562\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object seller_id: 卖家ID(可选)/Seller ID (optional)
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'seller_id', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'seller_id' in params:
            query_params.append(('seller_id', params['seller_id']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_product_detail', 'GET',
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

    def fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情V2(移动端-数据少)/Get product detail V2 (Less Data)  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop商品详情(移动端接口) - 数据结构更精简，响应速度更快 - 此接口返回的数据更少，如果需要更完整的数据请使用 `fetch_product_detail` 或 `fetch_product_detail_v3` 接口 ### 参数: - seller_id: 卖家ID (可传空字符串) - product_id: 商品ID (必填) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"productDetailSchema\": {},    // 商品详细信息         \"productCategoryInfoSchema\": {}, // 分类信息         \"pdpRelatedKwSchema\": [],     // 相关关键词         \"productsForComponentListSchema\": [] // 推荐商品组件     } } ```  # [English] ### Purpose: - Get TikTok Shop product details (Mobile API) - More streamlined data structure with faster response - This API returns less data; for more complete data, use `fetch_product_detail` or `fetch_product_detail_v3` ### Parameters: - seller_id: Seller ID (can be empty string) - product_id: Product ID (required) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"productDetailSchema\": {},    // Product details         \"productCategoryInfoSchema\": {}, // Category info         \"pdpRelatedKwSchema\": [],     // Related keywords         \"productsForComponentListSchema\": [] // Recommended product components     } } ```  # [示例/Example] seller_id = \"7495150558072178725\" product_id = \"1731088507416187562\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object seller_id: 卖家ID(可选)/Seller ID (optional)
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情V2(移动端-数据少)/Get product detail V2 (Less Data)  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop商品详情(移动端接口) - 数据结构更精简，响应速度更快 - 此接口返回的数据更少，如果需要更完整的数据请使用 `fetch_product_detail` 或 `fetch_product_detail_v3` 接口 ### 参数: - seller_id: 卖家ID (可传空字符串) - product_id: 商品ID (必填) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"productDetailSchema\": {},    // 商品详细信息         \"productCategoryInfoSchema\": {}, // 分类信息         \"pdpRelatedKwSchema\": [],     // 相关关键词         \"productsForComponentListSchema\": [] // 推荐商品组件     } } ```  # [English] ### Purpose: - Get TikTok Shop product details (Mobile API) - More streamlined data structure with faster response - This API returns less data; for more complete data, use `fetch_product_detail` or `fetch_product_detail_v3` ### Parameters: - seller_id: Seller ID (can be empty string) - product_id: Product ID (required) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"productDetailSchema\": {},    // Product details         \"productCategoryInfoSchema\": {}, // Category info         \"pdpRelatedKwSchema\": [],     // Related keywords         \"productsForComponentListSchema\": [] // Recommended product components     } } ```  # [示例/Example] seller_id = \"7495150558072178725\" product_id = \"1731088507416187562\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object seller_id: 卖家ID(可选)/Seller ID (optional)
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'seller_id', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'seller_id' in params:
            query_params.append(('seller_id', params['seller_id']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_product_detail_v2', 'GET',
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

    def fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情V3(移动端-数据完整)/Get product detail V3 (Full Data)  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop商品详情 - 提供最完整的商品信息，包括推荐商品、相关视频、店铺信息等 - 适用于所有地区的商品 ### 参数: - product_id: 商品ID (必填) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 200,     \"data\": {         \"productInfo\": {},                           // 商品详细信息         \"frequentlyBoughtTogether\": [],              // 经常一起购买的商品         \"similarProductsInCategory\": [],             // 同类别相似商品         \"exploreMoreFromShop\": [],                   // 店铺更多商品         \"brandInCategoryRecommendedProducts\": [],    // 品牌分类推荐商品         \"customersAlsoBought\": [],                   // 顾客还购买了         \"moreInThisColorStyle\": [],                  // 更多颜色款式         \"relatedVideos\": [],                         // 相关视频         \"shopPerformance\": {},                       // 店铺表现         \"categoryInfo\": {},                          // 分类信息         \"searchRecommendWords\": [],                  // 搜索推荐词         \"randomSearchWord\": \"\",                      // 随机搜索词         \"shopInfo\": {},                              // 店铺信息         \"shopHotReviews\": []                         // 店铺热门评论     } } ```  # [English] ### Purpose: - Get TikTok Shop product details - Provides the most complete product information including recommendations, videos, shop info, etc. - Suitable for products from all regions ### Parameters: - product_id: Product ID (required) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 200,     \"data\": {         \"productInfo\": {},                           // Product details         \"frequentlyBoughtTogether\": [],              // Frequently bought together         \"similarProductsInCategory\": [],             // Similar products in category         \"exploreMoreFromShop\": [],                   // More from shop         \"brandInCategoryRecommendedProducts\": [],    // Brand category recommendations         \"customersAlsoBought\": [],                   // Customers also bought         \"moreInThisColorStyle\": [],                  // More colors/styles         \"relatedVideos\": [],                         // Related videos         \"shopPerformance\": {},                       // Shop performance         \"categoryInfo\": {},                          // Category info         \"searchRecommendWords\": [],                  // Search recommendation words         \"randomSearchWord\": \"\",                      // Random search word         \"shopInfo\": {},                              // Shop information         \"shopHotReviews\": []                         // Shop hot reviews     } } ```  # [示例/Example] product_id = \"1731434108723499596\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品详情V3(移动端-数据完整)/Get product detail V3 (Full Data)  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop商品详情 - 提供最完整的商品信息，包括推荐商品、相关视频、店铺信息等 - 适用于所有地区的商品 ### 参数: - product_id: 商品ID (必填) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 200,     \"data\": {         \"productInfo\": {},                           // 商品详细信息         \"frequentlyBoughtTogether\": [],              // 经常一起购买的商品         \"similarProductsInCategory\": [],             // 同类别相似商品         \"exploreMoreFromShop\": [],                   // 店铺更多商品         \"brandInCategoryRecommendedProducts\": [],    // 品牌分类推荐商品         \"customersAlsoBought\": [],                   // 顾客还购买了         \"moreInThisColorStyle\": [],                  // 更多颜色款式         \"relatedVideos\": [],                         // 相关视频         \"shopPerformance\": {},                       // 店铺表现         \"categoryInfo\": {},                          // 分类信息         \"searchRecommendWords\": [],                  // 搜索推荐词         \"randomSearchWord\": \"\",                      // 随机搜索词         \"shopInfo\": {},                              // 店铺信息         \"shopHotReviews\": []                         // 店铺热门评论     } } ```  # [English] ### Purpose: - Get TikTok Shop product details - Provides the most complete product information including recommendations, videos, shop info, etc. - Suitable for products from all regions ### Parameters: - product_id: Product ID (required) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 200,     \"data\": {         \"productInfo\": {},                           // Product details         \"frequentlyBoughtTogether\": [],              // Frequently bought together         \"similarProductsInCategory\": [],             // Similar products in category         \"exploreMoreFromShop\": [],                   // More from shop         \"brandInCategoryRecommendedProducts\": [],    // Brand category recommendations         \"customersAlsoBought\": [],                   // Customers also bought         \"moreInThisColorStyle\": [],                  // More colors/styles         \"relatedVideos\": [],                         // Related videos         \"shopPerformance\": {},                       // Shop performance         \"categoryInfo\": {},                          // Category info         \"searchRecommendWords\": [],                  // Search recommendation words         \"randomSearchWord\": \"\",                      // Random search word         \"shopInfo\": {},                              // Shop information         \"shopHotReviews\": []                         // Shop hot reviews     } } ```  # [示例/Example] product_id = \"1731434108723499596\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object region: 地区代码/Region code
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
                    " to method fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get`")  # noqa: E501

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
            '/api/v1/tiktok/shop/web/fetch_product_detail_v3', 'GET',
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

    def fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品评论V1/Get product reviews V1  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop商品的评论列表（支持所有国家区域的商品，无需指定地区代码） - 支持按相关性或时间排序 - 支持评论筛选和分页加载 ### 参数: - product_id: 商品ID (必填) - sort_type: 排序方式     - 1: 按相关性排序     - 2: 按时间排序(最新)，默认值 - filter_id: 评论筛选ID (可选)     - 可从首次响应的 review_filters 列表中获取 - offset: 分页偏移量，默认1     - 如果响应中 has_more=1，使用 next_cursor 值进行下一页请求 ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 200,     \"data\": {         \"reviews\": [                      // 评论列表(每页20条)             {                 \"review_id\": \"xxx\",                 \"user_info\": {},          // 用户信息                 \"rating\": 5,              // 评分(1-5星)                 \"review_content\": \"...\",  // 评论内容                 \"images\": [],             // 评论图片                 \"videos\": [],             // 评论视频                 \"create_time\": 0,         // 创建时间戳                 \"is_verified_buyer\": true // 是否认证买家             }         ],         \"has_more\": 1,                    // 是否有更多: 1=有, 0=无         \"next_cursor\": \"xxx\",             // 下一页游标         \"review_filters\": [               // 可用的筛选器             {                 \"filter_id\": \"xxx\",                 \"filter_name\": \"所有评论\"             }         ],         \"statistics\": {                   // 统计信息             \"total_count\": 1000,             \"average_rating\": 4.5,             \"rating_distribution\": {}     // 星级分布         }     } } ```  # [English] ### Purpose: - Get TikTok Shop product reviews list (supports products from all countries/regions without specifying region code) - Support sorting by relevance or time - Support review filtering and pagination ### Parameters: - product_id: Product ID (required) - sort_type: Sort type     - 1: Sort by relevance     - 2: Sort by recent (default) - filter_id: Review filter ID (optional)     - Can be obtained from review_filters list in first response - offset: Offset for pagination, default 1     - If has_more=1 in response, use next_cursor value for next page ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 200,     \"data\": {         \"reviews\": [                      // Review list (20 per page)             {                 \"review_id\": \"xxx\",                 \"user_info\": {},          // User info                 \"rating\": 5,              // Rating (1-5 stars)                 \"review_content\": \"...\",  // Review content                 \"images\": [],             // Review images                 \"videos\": [],             // Review videos                 \"create_time\": 0,         // Create timestamp                 \"is_verified_buyer\": true // Is verified buyer             }         ],         \"has_more\": 1,                    // Has more: 1=yes, 0=no         \"next_cursor\": \"xxx\",             // Next page cursor         \"review_filters\": [               // Available filters             {                 \"filter_id\": \"xxx\",                 \"filter_name\": \"All reviews\"             }         ],         \"statistics\": {                   // Statistics             \"total_count\": 1000,             \"average_rating\": 4.5,             \"rating_distribution\": {}     // Rating distribution         }     } } ```  # [示例/Example] product_id = \"1731677627342753961\" sort_type = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object sort_type: 排序方式/Sort type: 1=相关性/Relevance, 2=最新/Recent
        :param object filter_id: 筛选ID/Filter ID
        :param object offset: 分页偏移量/Offset for pagination
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品评论V1/Get product reviews V1  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop商品的评论列表（支持所有国家区域的商品，无需指定地区代码） - 支持按相关性或时间排序 - 支持评论筛选和分页加载 ### 参数: - product_id: 商品ID (必填) - sort_type: 排序方式     - 1: 按相关性排序     - 2: 按时间排序(最新)，默认值 - filter_id: 评论筛选ID (可选)     - 可从首次响应的 review_filters 列表中获取 - offset: 分页偏移量，默认1     - 如果响应中 has_more=1，使用 next_cursor 值进行下一页请求 ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 200,     \"data\": {         \"reviews\": [                      // 评论列表(每页20条)             {                 \"review_id\": \"xxx\",                 \"user_info\": {},          // 用户信息                 \"rating\": 5,              // 评分(1-5星)                 \"review_content\": \"...\",  // 评论内容                 \"images\": [],             // 评论图片                 \"videos\": [],             // 评论视频                 \"create_time\": 0,         // 创建时间戳                 \"is_verified_buyer\": true // 是否认证买家             }         ],         \"has_more\": 1,                    // 是否有更多: 1=有, 0=无         \"next_cursor\": \"xxx\",             // 下一页游标         \"review_filters\": [               // 可用的筛选器             {                 \"filter_id\": \"xxx\",                 \"filter_name\": \"所有评论\"             }         ],         \"statistics\": {                   // 统计信息             \"total_count\": 1000,             \"average_rating\": 4.5,             \"rating_distribution\": {}     // 星级分布         }     } } ```  # [English] ### Purpose: - Get TikTok Shop product reviews list (supports products from all countries/regions without specifying region code) - Support sorting by relevance or time - Support review filtering and pagination ### Parameters: - product_id: Product ID (required) - sort_type: Sort type     - 1: Sort by relevance     - 2: Sort by recent (default) - filter_id: Review filter ID (optional)     - Can be obtained from review_filters list in first response - offset: Offset for pagination, default 1     - If has_more=1 in response, use next_cursor value for next page ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 200,     \"data\": {         \"reviews\": [                      // Review list (20 per page)             {                 \"review_id\": \"xxx\",                 \"user_info\": {},          // User info                 \"rating\": 5,              // Rating (1-5 stars)                 \"review_content\": \"...\",  // Review content                 \"images\": [],             // Review images                 \"videos\": [],             // Review videos                 \"create_time\": 0,         // Create timestamp                 \"is_verified_buyer\": true // Is verified buyer             }         ],         \"has_more\": 1,                    // Has more: 1=yes, 0=no         \"next_cursor\": \"xxx\",             // Next page cursor         \"review_filters\": [               // Available filters             {                 \"filter_id\": \"xxx\",                 \"filter_name\": \"All reviews\"             }         ],         \"statistics\": {                   // Statistics             \"total_count\": 1000,             \"average_rating\": 4.5,             \"rating_distribution\": {}     // Rating distribution         }     } } ```  # [示例/Example] product_id = \"1731677627342753961\" sort_type = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object sort_type: 排序方式/Sort type: 1=相关性/Relevance, 2=最新/Recent
        :param object filter_id: 筛选ID/Filter ID
        :param object offset: 分页偏移量/Offset for pagination
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'sort_type', 'filter_id', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'filter_id' in params:
            query_params.append(('filter_id', params['filter_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_product_reviews_v1', 'GET',
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

    def fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get(self, product_id, **kwargs):  # noqa: E501
        """获取商品评论V2/Get product reviews V2  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop商品评论（仅支持美洲，欧洲，地区的商品，东南亚地区商品请使用 `fetch_product_reviews_v1` 接口） - 支持多种筛选和排序方式 - 数据结构更完整，包含更多评论详情 ### 参数: - product_id: 商品ID (必填) - page_start: 起始页码，默认1     - 当响应中 has_more=1 时，使用当前页码 +1 进行下一页请求 - sort_rule: 排序规则，默认2 - filter_type: 筛选类型     - 1: 默认不选择任何过滤     - 2: 包含图片或视频     - 3: 真实购买过滤 - filter_value: 星级筛选     - 6: 所有星级的评论(默认)     - 5: 5星评价     - 4: 4星评价     - 3: 3星评价     - 2: 2星评价     - 1: 1星评价 - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"reviews\": [                      // 评论列表(每页20条)             {                 \"review_id\": \"xxx\",                 \"user\": {                 // 用户信息                     \"user_id\": \"xxx\",                     \"nickname\": \"用户昵称\",                     \"avatar\": \"头像URL\"                 },                 \"rating\": 5,              // 评分(1-5星)                 \"content\": \"评论内容\",                 \"medias\": [               // 媒体文件(图片/视频)                     {                         \"type\": \"image\",                         \"url\": \"媒体URL\"                     }                 ],                 \"create_time\": 0,         // 创建时间戳                 \"verified_purchase\": true, // 是否认证购买                 \"product_info\": {},       // 商品信息                 \"likes_count\": 10,        // 点赞数                 \"seller_reply\": {}        // 卖家回复             }         ],         \"has_more\": 1,                    // 是否有更多: 1=有, 0=无         \"page_start\": 1,                  // 当前页码         \"total_count\": 500,               // 总评论数         \"review_summary\": {               // 评论摘要             \"average_rating\": 4.8,             \"star_distribution\": {        // 星级分布                 \"5\": 400,                 \"4\": 80,                 \"3\": 15,                 \"2\": 3,                 \"1\": 2             }         }     } } ```  # [English] ### Purpose: - Get TikTok Shop product reviews (only supports products from Americas, Europe; for Southeast Asia products, use `fetch_product_reviews_v1`) - Support multiple filtering and sorting options - More complete data structure with detailed review information ### Parameters: - product_id: Product ID (required) - page_start: Starting page number, default 1     - When has_more=1 in response, use current page +1 for next page - sort_rule: Sort rule, default 2 - filter_type: Filter type     - 1: Default, no filter     - 2: Contains images or videos     - 3: Verified purchase filter - filter_value: Star filter     - 6: All star ratings (default)     - 5: 5-star reviews     - 4: 4-star reviews     - 3: 3-star reviews     - 2: 2-star reviews     - 1: 1-star reviews - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"reviews\": [                      // Review list (20 per page)             {                 \"review_id\": \"xxx\",                 \"user\": {                 // User info                     \"user_id\": \"xxx\",                     \"nickname\": \"Username\",                     \"avatar\": \"Avatar URL\"                 },                 \"rating\": 5,              // Rating (1-5 stars)                 \"content\": \"Review content\",                 \"medias\": [               // Media files (images/videos)                     {                         \"type\": \"image\",                         \"url\": \"Media URL\"                     }                 ],                 \"create_time\": 0,         // Create timestamp                 \"verified_purchase\": true, // Is verified purchase                 \"product_info\": {},       // Product info                 \"likes_count\": 10,        // Likes count                 \"seller_reply\": {}        // Seller reply             }         ],         \"has_more\": 1,                    // Has more: 1=yes, 0=no         \"page_start\": 1,                  // Current page         \"total_count\": 500,               // Total review count         \"review_summary\": {               // Review summary             \"average_rating\": 4.8,             \"star_distribution\": {        // Star distribution                 \"5\": 400,                 \"4\": 80,                 \"3\": 15,                 \"2\": 3,                 \"1\": 2             }         }     } } ```  # [示例/Example] product_id = \"1731677627342753961\" page_start = 1 sort_rule = 2 filter_type = 1 filter_value = 6 region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object page_start: 起始页码/Page start
        :param object sort_rule: 排序规则/Sort rule
        :param object filter_type: 筛选类型/Filter type: 1=默认, 2=有图片/视频, 3=真实购买
        :param object filter_value: 星级筛选/Star filter: 6=全部, 5-1=对应星级
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """获取商品评论V2/Get product reviews V2  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop商品评论（仅支持美洲，欧洲，地区的商品，东南亚地区商品请使用 `fetch_product_reviews_v1` 接口） - 支持多种筛选和排序方式 - 数据结构更完整，包含更多评论详情 ### 参数: - product_id: 商品ID (必填) - page_start: 起始页码，默认1     - 当响应中 has_more=1 时，使用当前页码 +1 进行下一页请求 - sort_rule: 排序规则，默认2 - filter_type: 筛选类型     - 1: 默认不选择任何过滤     - 2: 包含图片或视频     - 3: 真实购买过滤 - filter_value: 星级筛选     - 6: 所有星级的评论(默认)     - 5: 5星评价     - 4: 4星评价     - 3: 3星评价     - 2: 2星评价     - 1: 1星评价 - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"reviews\": [                      // 评论列表(每页20条)             {                 \"review_id\": \"xxx\",                 \"user\": {                 // 用户信息                     \"user_id\": \"xxx\",                     \"nickname\": \"用户昵称\",                     \"avatar\": \"头像URL\"                 },                 \"rating\": 5,              // 评分(1-5星)                 \"content\": \"评论内容\",                 \"medias\": [               // 媒体文件(图片/视频)                     {                         \"type\": \"image\",                         \"url\": \"媒体URL\"                     }                 ],                 \"create_time\": 0,         // 创建时间戳                 \"verified_purchase\": true, // 是否认证购买                 \"product_info\": {},       // 商品信息                 \"likes_count\": 10,        // 点赞数                 \"seller_reply\": {}        // 卖家回复             }         ],         \"has_more\": 1,                    // 是否有更多: 1=有, 0=无         \"page_start\": 1,                  // 当前页码         \"total_count\": 500,               // 总评论数         \"review_summary\": {               // 评论摘要             \"average_rating\": 4.8,             \"star_distribution\": {        // 星级分布                 \"5\": 400,                 \"4\": 80,                 \"3\": 15,                 \"2\": 3,                 \"1\": 2             }         }     } } ```  # [English] ### Purpose: - Get TikTok Shop product reviews (only supports products from Americas, Europe; for Southeast Asia products, use `fetch_product_reviews_v1`) - Support multiple filtering and sorting options - More complete data structure with detailed review information ### Parameters: - product_id: Product ID (required) - page_start: Starting page number, default 1     - When has_more=1 in response, use current page +1 for next page - sort_rule: Sort rule, default 2 - filter_type: Filter type     - 1: Default, no filter     - 2: Contains images or videos     - 3: Verified purchase filter - filter_value: Star filter     - 6: All star ratings (default)     - 5: 5-star reviews     - 4: 4-star reviews     - 3: 3-star reviews     - 2: 2-star reviews     - 1: 1-star reviews - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"reviews\": [                      // Review list (20 per page)             {                 \"review_id\": \"xxx\",                 \"user\": {                 // User info                     \"user_id\": \"xxx\",                     \"nickname\": \"Username\",                     \"avatar\": \"Avatar URL\"                 },                 \"rating\": 5,              // Rating (1-5 stars)                 \"content\": \"Review content\",                 \"medias\": [               // Media files (images/videos)                     {                         \"type\": \"image\",                         \"url\": \"Media URL\"                     }                 ],                 \"create_time\": 0,         // Create timestamp                 \"verified_purchase\": true, // Is verified purchase                 \"product_info\": {},       // Product info                 \"likes_count\": 10,        // Likes count                 \"seller_reply\": {}        // Seller reply             }         ],         \"has_more\": 1,                    // Has more: 1=yes, 0=no         \"page_start\": 1,                  // Current page         \"total_count\": 500,               // Total review count         \"review_summary\": {               // Review summary             \"average_rating\": 4.8,             \"star_distribution\": {        // Star distribution                 \"5\": 400,                 \"4\": 80,                 \"3\": 15,                 \"2\": 3,                 \"1\": 2             }         }     } } ```  # [示例/Example] product_id = \"1731677627342753961\" page_start = 1 sort_rule = 2 filter_type = 1 filter_value = 6 region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object product_id: 商品ID/Product ID (required)
        :param object page_start: 起始页码/Page start
        :param object sort_rule: 排序规则/Sort rule
        :param object filter_type: 筛选类型/Filter type: 1=默认, 2=有图片/视频, 3=真实购买
        :param object filter_value: 星级筛选/Star filter: 6=全部, 5-1=对应星级
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'page_start', 'sort_rule', 'filter_type', 'filter_value', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if self.api_client.client_side_validation and ('product_id' not in params or
                                                       params['product_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `product_id` when calling `fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in params:
            query_params.append(('product_id', params['product_id']))  # noqa: E501
        if 'page_start' in params:
            query_params.append(('page_start', params['page_start']))  # noqa: E501
        if 'sort_rule' in params:
            query_params.append(('sort_rule', params['sort_rule']))  # noqa: E501
        if 'filter_type' in params:
            query_params.append(('filter_type', params['filter_type']))  # noqa: E501
        if 'filter_value' in params:
            query_params.append(('filter_value', params['filter_value']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_product_reviews_v2', 'GET',
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

    def fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get(self, category_id, **kwargs):  # noqa: E501
        """根据分类ID获取商品列表/Get products by category ID  # noqa: E501

        # [中文] ### 用途: - 根据商品分类ID获取该分类下的商品列表 - 可用于构建分类浏览功能 ### 参数: - category_id: 分类ID (必填，从fetch_products_category_list接口获取) - offset: 翻页偏移量 (默认0)     - 每页默认20个商品，每次请求增加20，当响应中的 `hasMore` 为true时可继续请求下一页，否则已到最后一页。     - 例如: 第1页offset=0，第2页offset=20，第3页offset=40，以此类推。 - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // 商品列表(最多20个)             {                 \"product_id\": \"xxx\",                 \"title\": \"商品标题\",                 \"image\": \"商品图片\",                 \"price\": {},              // 价格信息                 \"rating\": {},             // 评分信息                 \"sales\": {}               // 销量信息             }         ]     } } ```  # [English] ### Purpose: - Get product list by category ID - Can be used to build category browsing feature ### Parameters: - category_id: Category ID (required, from fetch_products_category_list API) - offset: Offset for pagination (default 0)     - Default 20 products per page, increase by 20 for each request. If `hasMore` in response is true, can request next page, otherwise reached last page.     - Example: Page 1 offset=0, Page 2 offset=20, Page 3 offset=40, and so on. - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // Product list (up to 20)             {                 \"product_id\": \"xxx\",                 \"title\": \"Product title\",                 \"image\": \"Product image\",                 \"price\": {},              // Price info                 \"rating\": {},             // Rating info                 \"sales\": {}               // Sales info             }         ]     } } ```  # [示例/Example] category_id = 963976 region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category_id: 分类ID/Category ID (required)
        :param object offset: 翻页偏移量/Offset for pagination
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get_with_http_info(category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get_with_http_info(category_id, **kwargs)  # noqa: E501
            return data

    def fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get_with_http_info(self, category_id, **kwargs):  # noqa: E501
        """根据分类ID获取商品列表/Get products by category ID  # noqa: E501

        # [中文] ### 用途: - 根据商品分类ID获取该分类下的商品列表 - 可用于构建分类浏览功能 ### 参数: - category_id: 分类ID (必填，从fetch_products_category_list接口获取) - offset: 翻页偏移量 (默认0)     - 每页默认20个商品，每次请求增加20，当响应中的 `hasMore` 为true时可继续请求下一页，否则已到最后一页。     - 例如: 第1页offset=0，第2页offset=20，第3页offset=40，以此类推。 - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // 商品列表(最多20个)             {                 \"product_id\": \"xxx\",                 \"title\": \"商品标题\",                 \"image\": \"商品图片\",                 \"price\": {},              // 价格信息                 \"rating\": {},             // 评分信息                 \"sales\": {}               // 销量信息             }         ]     } } ```  # [English] ### Purpose: - Get product list by category ID - Can be used to build category browsing feature ### Parameters: - category_id: Category ID (required, from fetch_products_category_list API) - offset: Offset for pagination (default 0)     - Default 20 products per page, increase by 20 for each request. If `hasMore` in response is true, can request next page, otherwise reached last page.     - Example: Page 1 offset=0, Page 2 offset=20, Page 3 offset=40, and so on. - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // Product list (up to 20)             {                 \"product_id\": \"xxx\",                 \"title\": \"Product title\",                 \"image\": \"Product image\",                 \"price\": {},              // Price info                 \"rating\": {},             // Rating info                 \"sales\": {}               // Sales info             }         ]     } } ```  # [示例/Example] category_id = 963976 region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get_with_http_info(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category_id: 分类ID/Category ID (required)
        :param object offset: 翻页偏移量/Offset for pagination
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'offset', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if self.api_client.client_side_validation and ('category_id' not in params or
                                                       params['category_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `category_id` when calling `fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category_id' in params:
            query_params.append(('category_id', params['category_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_products_by_category_id', 'GET',
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

    def fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get(self, **kwargs):  # noqa: E501
        """获取商品分类列表/Get product category list  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop的商品分类目录 - 返回完整的分类树结构 ### 参数: - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 返回数据结构: ```json [     {         \"self\": {                     // 分类自身信息             \"category_id\": \"xxx\",             \"category_level\": 1,             \"is_leaf\": false,             \"parent_category_id\": \"0\",             \"category_name\": \"分类名称\",             \"category_name_en\": \"Category Name\",             \"image_url\": \"分类图片URL\"         },         \"children\": [                 // 子分类列表             {                 \"self\": {...},                 \"children\": [...]             }         ]     } ] ``` - 总共约28个主分类  # [English] ### Purpose: - Get TikTok Shop product category directory - Returns complete category tree structure ### Parameters: - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Response Structure: ```json [     {         \"self\": {                     // Category info             \"category_id\": \"xxx\",             \"category_level\": 1,             \"is_leaf\": false,             \"parent_category_id\": \"0\",             \"category_name\": \"Category Name\",             \"category_name_en\": \"Category Name\",             \"image_url\": \"Category image URL\"         },         \"children\": [                 // Sub-categories             {                 \"self\": {...},                 \"children\": [...]             }         ]     } ] ``` - Total about 28 main categories  # [示例/Example] region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取商品分类列表/Get product category list  # noqa: E501

        # [中文] ### 用途: - 获取TikTok Shop的商品分类目录 - 返回完整的分类树结构 ### 参数: - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 返回数据结构: ```json [     {         \"self\": {                     // 分类自身信息             \"category_id\": \"xxx\",             \"category_level\": 1,             \"is_leaf\": false,             \"parent_category_id\": \"0\",             \"category_name\": \"分类名称\",             \"category_name_en\": \"Category Name\",             \"image_url\": \"分类图片URL\"         },         \"children\": [                 // 子分类列表             {                 \"self\": {...},                 \"children\": [...]             }         ]     } ] ``` - 总共约28个主分类  # [English] ### Purpose: - Get TikTok Shop product category directory - Returns complete category tree structure ### Parameters: - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Response Structure: ```json [     {         \"self\": {                     // Category info             \"category_id\": \"xxx\",             \"category_level\": 1,             \"is_leaf\": false,             \"parent_category_id\": \"0\",             \"category_name\": \"Category Name\",             \"category_name_en\": \"Category Name\",             \"image_url\": \"Category image URL\"         },         \"children\": [                 // Sub-categories             {                 \"self\": {...},                 \"children\": [...]             }         ]     } ] ``` - Total about 28 main categories  # [示例/Example] region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_products_category_list', 'GET',
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

    def fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get(self, search_word, **kwargs):  # noqa: E501
        """搜索商品列表V1/Search products list V1  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索商品 - 支持分页加载更多结果 ### 参数: - search_word: 搜索关键词 (必填) - offset: 偏移量，用于分页 (默认0) - page_token: 分页标记，用于获取下一页 - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // 商品列表(每页30个)             {                 \"product_id\": \"xxx\",                 \"title\": \"商品标题\",                 \"image\": \"商品图片URL\",                 \"product_price_info\": {},  // 价格信息                 \"rate_info\": {},           // 评分信息                 \"sold_info\": {},           // 销量信息                 \"seller_info\": {},         // 卖家信息                 \"seo_url\": \"商品SEO链接\",                 \"product_marketing_info\": {} // 营销信息             }         ],         \"has_more\": true,             // 是否有更多         \"load_more_params\": {         // 分页参数             \"offset\": 30,             \"page_token\": \"xxx\",             \"api_source\": 2         }     } } ```  # [English] ### Purpose: - Search products by keyword - Support pagination to load more results ### Parameters: - search_word: Search keyword (required) - offset: Offset for pagination (default 0) - page_token: Page token for next page - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // Product list (30 per page)             {                 \"product_id\": \"xxx\",                 \"title\": \"Product title\",                 \"image\": \"Product image URL\",                 \"product_price_info\": {},  // Price info                 \"rate_info\": {},           // Rating info                 \"sold_info\": {},           // Sales info                 \"seller_info\": {},         // Seller info                 \"seo_url\": \"Product SEO URL\",                 \"product_marketing_info\": {} // Marketing info             }         ],         \"has_more\": true,             // Has more         \"load_more_params\": {         // Pagination params             \"offset\": 30,             \"page_token\": \"xxx\",             \"api_source\": 2         }     } } ```  # [示例/Example] search_word = \"labubu\" offset = 0 page_token = \"\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get(search_word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_word: 搜索关键词/Search keyword (required)
        :param object offset: 偏移量/Offset
        :param object page_token: 分页标记/Page token
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get_with_http_info(search_word, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get_with_http_info(search_word, **kwargs)  # noqa: E501
            return data

    def fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get_with_http_info(self, search_word, **kwargs):  # noqa: E501
        """搜索商品列表V1/Search products list V1  # noqa: E501

        # [中文] ### 用途: - 根据关键词搜索商品 - 支持分页加载更多结果 ### 参数: - search_word: 搜索关键词 (必填) - offset: 偏移量，用于分页 (默认0) - page_token: 分页标记，用于获取下一页 - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // 商品列表(每页30个)             {                 \"product_id\": \"xxx\",                 \"title\": \"商品标题\",                 \"image\": \"商品图片URL\",                 \"product_price_info\": {},  // 价格信息                 \"rate_info\": {},           // 评分信息                 \"sold_info\": {},           // 销量信息                 \"seller_info\": {},         // 卖家信息                 \"seo_url\": \"商品SEO链接\",                 \"product_marketing_info\": {} // 营销信息             }         ],         \"has_more\": true,             // 是否有更多         \"load_more_params\": {         // 分页参数             \"offset\": 30,             \"page_token\": \"xxx\",             \"api_source\": 2         }     } } ```  # [English] ### Purpose: - Search products by keyword - Support pagination to load more results ### Parameters: - search_word: Search keyword (required) - offset: Offset for pagination (default 0) - page_token: Page token for next page - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // Product list (30 per page)             {                 \"product_id\": \"xxx\",                 \"title\": \"Product title\",                 \"image\": \"Product image URL\",                 \"product_price_info\": {},  // Price info                 \"rate_info\": {},           // Rating info                 \"sold_info\": {},           // Sales info                 \"seller_info\": {},         // Seller info                 \"seo_url\": \"Product SEO URL\",                 \"product_marketing_info\": {} // Marketing info             }         ],         \"has_more\": true,             // Has more         \"load_more_params\": {         // Pagination params             \"offset\": 30,             \"page_token\": \"xxx\",             \"api_source\": 2         }     } } ```  # [示例/Example] search_word = \"labubu\" offset = 0 page_token = \"\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get_with_http_info(search_word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_word: 搜索关键词/Search keyword (required)
        :param object offset: 偏移量/Offset
        :param object page_token: 分页标记/Page token
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_word', 'offset', 'page_token', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_word' is set
        if self.api_client.client_side_validation and ('search_word' not in params or
                                                       params['search_word'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_word` when calling `fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_word' in params:
            query_params.append(('search_word', params['search_word']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_search_products_list', 'GET',
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

    def fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get(self, search_word, **kwargs):  # noqa: E501
        """搜索商品列表V2(移动端)/Search products list V2 (Mobile)  # noqa: E501

        # [中文] ### 用途: - 搜索商品(移动端接口) - 数据结构更精简，响应更快 ### 参数: - search_word: 搜索关键词 (必填) - offset: 偏移量 (默认0) - page_token: 分页标记 - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [...],            // 商品列表         \"has_more\": true,             // 是否有更多         \"load_more_params\": {}        // 加载更多参数     } } ```  # [English] ### Purpose: - Search products (Mobile API) - More streamlined data, faster response ### Parameters: - search_word: Search keyword (required) - offset: Offset (default 0) - page_token: Page token - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [...],            // Product list         \"has_more\": true,             // Has more         \"load_more_params\": {}        // Load more params     } } ```  # [示例/Example] search_word = \"labubu\" offset = 0 page_token = \"\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get(search_word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_word: 搜索关键词/Search keyword (required)
        :param object offset: 偏移量/Offset
        :param object page_token: 分页标记/Page token
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get_with_http_info(search_word, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get_with_http_info(search_word, **kwargs)  # noqa: E501
            return data

    def fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get_with_http_info(self, search_word, **kwargs):  # noqa: E501
        """搜索商品列表V2(移动端)/Search products list V2 (Mobile)  # noqa: E501

        # [中文] ### 用途: - 搜索商品(移动端接口) - 数据结构更精简，响应更快 ### 参数: - search_word: 搜索关键词 (必填) - offset: 偏移量 (默认0) - page_token: 分页标记 - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [...],            // 商品列表         \"has_more\": true,             // 是否有更多         \"load_more_params\": {}        // 加载更多参数     } } ```  # [English] ### Purpose: - Search products (Mobile API) - More streamlined data, faster response ### Parameters: - search_word: Search keyword (required) - offset: Offset (default 0) - page_token: Page token - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [...],            // Product list         \"has_more\": true,             // Has more         \"load_more_params\": {}        // Load more params     } } ```  # [示例/Example] search_word = \"labubu\" offset = 0 page_token = \"\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get_with_http_info(search_word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_word: 搜索关键词/Search keyword (required)
        :param object offset: 偏移量/Offset
        :param object page_token: 分页标记/Page token
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_word', 'offset', 'page_token', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_word' is set
        if self.api_client.client_side_validation and ('search_word' not in params or
                                                       params['search_word'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_word` when calling `fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_word' in params:
            query_params.append(('search_word', params['search_word']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_search_products_list_v2', 'GET',
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

    def fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get(self, keyword, **kwargs):  # noqa: E501
        """搜索商品列表V3/Search products list V3  # noqa: E501

        # [中文] ### 用途: - 搜索TikTok Shop商品，支持高级筛选和排序 - 提供更多的筛选选项和排序方式 - 适合需要精细化筛选的场景 ### 参数: - keyword: 搜索关键词 (必填) - offset: 分页偏移量，默认0     - 每页固定返回20个商品     - 如果响应中 has_more=1，使用 cursor 值进行下一页请求 - region: 地区代码，Alpha-2 国家代码 (必填) - sort_by: 排序方式，默认 RELEVANCE     - RELEVANCE: 按相关性排序（默认）     - PRICE_ASC: 价格从低到高     - PRICE_DESC: 价格从高到低     - BEST_SELLERS: 最畅销 - filters_data: 筛选数据，JSON数组格式字符串（可选）     - 可从首次响应的 filter_groups 字段获取可用筛选器     - 格式示例：         - 简单筛选按钮: {\"type\": 2, \"value\": \"true\"}         - 范围/多选: {\"type\": 8, \"value_list\": [\"1,1000\"]}         - 完整示例（价格和4星及以上）: [{\"type\": 2, \"value\": \"true\"},{\"type\": 8, \"value_list\": [\"1,1000\"]}] ### 重要提示: - 每页固定返回20个商品 - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 200,     \"data\": {         \"products\": [                  // 商品列表             {                 \"product_id\": \"xxx\",                 \"title\": \"商品标题\",                 \"image\": \"商品图片URL\",                 \"price\": {             // 价格信息                     \"current_price\": 19.99,                     \"original_price\": 29.99,                     \"discount\": \"33% OFF\"                 },                 \"rating\": {            // 评分信息                     \"average\": 4.8,                     \"count\": 1234                 },                 \"sales\": 5000,         // 销量                 \"seller_info\": {},     // 卖家信息                 \"url\": \"商品链接\"             }         ],         \"has_more\": 1,                 // 是否有更多: 1=有, 0=无         \"cursor\": \"xxx\",               // 下一页游标         \"filter_groups\": [             // 可用的筛选器组             {                 \"group_name\": \"价格\",                 \"filters\": [                     {                         \"type\": 8,                         \"name\": \"价格区间\",                         \"options\": [...]                     }                 ]             },             {                 \"group_name\": \"评分\",                 \"filters\": [                     {                         \"type\": 2,                         \"name\": \"4星及以上\",                         \"value\": \"true\"                     }                 ]             }         ],         \"total_count\": 10000           // 总商品数     } } ```  # [English] ### Purpose: - Search TikTok Shop products with advanced filtering and sorting - Provides more filter options and sort methods - Suitable for scenarios requiring fine-grained filtering ### Parameters: - keyword: Search keyword (required) - offset: Offset for pagination, default 0     - Fixed 20 products per page     - If has_more=1 in response, use cursor value for next page - region: Region code, Alpha-2 country code (required) - sort_by: Sort method, default RELEVANCE     - RELEVANCE: Sort by relevance (default)     - PRICE_ASC: Price low to high     - PRICE_DESC: Price high to low     - BEST_SELLERS: Best sellers - filters_data: Filter data, JSON array format string (optional)     - Available filters can be obtained from filter_groups field in first response     - Format examples:         - Simple filter button: {\"type\": 2, \"value\": \"true\"}         - Range/multiple select: {\"type\": 8, \"value_list\": [\"1,1000\"]}         - Complete example (price and 4+ stars): [{\"type\": 2, \"value\": \"true\"},{\"type\": 8, \"value_list\": [\"1,1000\"]}] ### Important Notice: - Fixed 20 products per page - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 200,     \"data\": {         \"products\": [                  // Product list             {                 \"product_id\": \"xxx\",                 \"title\": \"Product title\",                 \"image\": \"Product image URL\",                 \"price\": {             // Price info                     \"current_price\": 19.99,                     \"original_price\": 29.99,                     \"discount\": \"33% OFF\"                 },                 \"rating\": {            // Rating info                     \"average\": 4.8,                     \"count\": 1234                 },                 \"sales\": 5000,         // Sales count                 \"seller_info\": {},     // Seller info                 \"url\": \"Product URL\"             }         ],         \"has_more\": 1,                 // Has more: 1=yes, 0=no         \"cursor\": \"xxx\",               // Next page cursor         \"filter_groups\": [             // Available filter groups             {                 \"group_name\": \"Price\",                 \"filters\": [                     {                         \"type\": 8,                         \"name\": \"Price range\",                         \"options\": [...]                     }                 ]             },             {                 \"group_name\": \"Rating\",                 \"filters\": [                     {                         \"type\": 2,                         \"name\": \"4 Stars & Up\",                         \"value\": \"true\"                     }                 ]             }         ],         \"total_count\": 10000           // Total product count     } } ```  # [示例/Example] keyword = \"baby\" offset = 0 region = \"US\" sort_by = \"PRICE_ASC\" filters_data = '[{\"type\": 2, \"value\": \"true\"},{\"type\": 8, \"value_list\": [\"1,1000\"]}]'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object offset: 偏移量/Offset
        :param object region: 地区代码/Region code (Alpha-2)
        :param object sort_by: 排序方式/Sort by: RELEVANCE, PRICE_ASC, PRICE_DESC, BEST_SELLERS
        :param object filters_data: 筛选数据JSON/Filters data JSON
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索商品列表V3/Search products list V3  # noqa: E501

        # [中文] ### 用途: - 搜索TikTok Shop商品，支持高级筛选和排序 - 提供更多的筛选选项和排序方式 - 适合需要精细化筛选的场景 ### 参数: - keyword: 搜索关键词 (必填) - offset: 分页偏移量，默认0     - 每页固定返回20个商品     - 如果响应中 has_more=1，使用 cursor 值进行下一页请求 - region: 地区代码，Alpha-2 国家代码 (必填) - sort_by: 排序方式，默认 RELEVANCE     - RELEVANCE: 按相关性排序（默认）     - PRICE_ASC: 价格从低到高     - PRICE_DESC: 价格从高到低     - BEST_SELLERS: 最畅销 - filters_data: 筛选数据，JSON数组格式字符串（可选）     - 可从首次响应的 filter_groups 字段获取可用筛选器     - 格式示例：         - 简单筛选按钮: {\"type\": 2, \"value\": \"true\"}         - 范围/多选: {\"type\": 8, \"value_list\": [\"1,1000\"]}         - 完整示例（价格和4星及以上）: [{\"type\": 2, \"value\": \"true\"},{\"type\": 8, \"value_list\": [\"1,1000\"]}] ### 重要提示: - 每页固定返回20个商品 - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 200,     \"data\": {         \"products\": [                  // 商品列表             {                 \"product_id\": \"xxx\",                 \"title\": \"商品标题\",                 \"image\": \"商品图片URL\",                 \"price\": {             // 价格信息                     \"current_price\": 19.99,                     \"original_price\": 29.99,                     \"discount\": \"33% OFF\"                 },                 \"rating\": {            // 评分信息                     \"average\": 4.8,                     \"count\": 1234                 },                 \"sales\": 5000,         // 销量                 \"seller_info\": {},     // 卖家信息                 \"url\": \"商品链接\"             }         ],         \"has_more\": 1,                 // 是否有更多: 1=有, 0=无         \"cursor\": \"xxx\",               // 下一页游标         \"filter_groups\": [             // 可用的筛选器组             {                 \"group_name\": \"价格\",                 \"filters\": [                     {                         \"type\": 8,                         \"name\": \"价格区间\",                         \"options\": [...]                     }                 ]             },             {                 \"group_name\": \"评分\",                 \"filters\": [                     {                         \"type\": 2,                         \"name\": \"4星及以上\",                         \"value\": \"true\"                     }                 ]             }         ],         \"total_count\": 10000           // 总商品数     } } ```  # [English] ### Purpose: - Search TikTok Shop products with advanced filtering and sorting - Provides more filter options and sort methods - Suitable for scenarios requiring fine-grained filtering ### Parameters: - keyword: Search keyword (required) - offset: Offset for pagination, default 0     - Fixed 20 products per page     - If has_more=1 in response, use cursor value for next page - region: Region code, Alpha-2 country code (required) - sort_by: Sort method, default RELEVANCE     - RELEVANCE: Sort by relevance (default)     - PRICE_ASC: Price low to high     - PRICE_DESC: Price high to low     - BEST_SELLERS: Best sellers - filters_data: Filter data, JSON array format string (optional)     - Available filters can be obtained from filter_groups field in first response     - Format examples:         - Simple filter button: {\"type\": 2, \"value\": \"true\"}         - Range/multiple select: {\"type\": 8, \"value_list\": [\"1,1000\"]}         - Complete example (price and 4+ stars): [{\"type\": 2, \"value\": \"true\"},{\"type\": 8, \"value_list\": [\"1,1000\"]}] ### Important Notice: - Fixed 20 products per page - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 200,     \"data\": {         \"products\": [                  // Product list             {                 \"product_id\": \"xxx\",                 \"title\": \"Product title\",                 \"image\": \"Product image URL\",                 \"price\": {             // Price info                     \"current_price\": 19.99,                     \"original_price\": 29.99,                     \"discount\": \"33% OFF\"                 },                 \"rating\": {            // Rating info                     \"average\": 4.8,                     \"count\": 1234                 },                 \"sales\": 5000,         // Sales count                 \"seller_info\": {},     // Seller info                 \"url\": \"Product URL\"             }         ],         \"has_more\": 1,                 // Has more: 1=yes, 0=no         \"cursor\": \"xxx\",               // Next page cursor         \"filter_groups\": [             // Available filter groups             {                 \"group_name\": \"Price\",                 \"filters\": [                     {                         \"type\": 8,                         \"name\": \"Price range\",                         \"options\": [...]                     }                 ]             },             {                 \"group_name\": \"Rating\",                 \"filters\": [                     {                         \"type\": 2,                         \"name\": \"4 Stars & Up\",                         \"value\": \"true\"                     }                 ]             }         ],         \"total_count\": 10000           // Total product count     } } ```  # [示例/Example] keyword = \"baby\" offset = 0 region = \"US\" sort_by = \"PRICE_ASC\" filters_data = '[{\"type\": 2, \"value\": \"true\"},{\"type\": 8, \"value_list\": [\"1,1000\"]}]'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object offset: 偏移量/Offset
        :param object region: 地区代码/Region code (Alpha-2)
        :param object sort_by: 排序方式/Sort by: RELEVANCE, PRICE_ASC, PRICE_DESC, BEST_SELLERS
        :param object filters_data: 筛选数据JSON/Filters data JSON
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'region', 'sort_by', 'filters_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'filters_data' in params:
            query_params.append(('filters_data', params['filters_data']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_search_products_list_v3', 'GET',
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

    def fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get(self, search_word, **kwargs):  # noqa: E501
        """获取搜索关键词建议V1/Get search keyword suggestions V1  # noqa: E501

        # [中文] ### 用途: - 获取搜索关键词的自动补全建议 - 用于搜索框的智能提示功能 ### 参数: - search_word: 搜索关键词 (必填) - lang: 语言代码 (en/zh等) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"\",     \"data\": [                        // 建议列表(最多50个)         \"phone case\",         \"phone mount\",         \"phone holder for car\",         \"...\"     ] } ```  # [English] ### Purpose: - Get auto-complete suggestions for search keywords - Used for search box smart suggestions ### Parameters: - search_word: Search keyword (required) - lang: Language code (en/zh etc.) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"\",     \"data\": [                        // Suggestion list (up to 50)         \"phone case\",         \"phone mount\",         \"phone holder for car\",         \"...\"     ] } ```  # [示例/Example] search_word = \"labubu\" lang = \"en\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get(search_word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_word: 搜索关键词/Search keyword (required)
        :param object lang: 语言/Language
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get_with_http_info(search_word, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get_with_http_info(search_word, **kwargs)  # noqa: E501
            return data

    def fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get_with_http_info(self, search_word, **kwargs):  # noqa: E501
        """获取搜索关键词建议V1/Get search keyword suggestions V1  # noqa: E501

        # [中文] ### 用途: - 获取搜索关键词的自动补全建议 - 用于搜索框的智能提示功能 ### 参数: - search_word: 搜索关键词 (必填) - lang: 语言代码 (en/zh等) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"\",     \"data\": [                        // 建议列表(最多50个)         \"phone case\",         \"phone mount\",         \"phone holder for car\",         \"...\"     ] } ```  # [English] ### Purpose: - Get auto-complete suggestions for search keywords - Used for search box smart suggestions ### Parameters: - search_word: Search keyword (required) - lang: Language code (en/zh etc.) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"\",     \"data\": [                        // Suggestion list (up to 50)         \"phone case\",         \"phone mount\",         \"phone holder for car\",         \"...\"     ] } ```  # [示例/Example] search_word = \"labubu\" lang = \"en\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get_with_http_info(search_word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_word: 搜索关键词/Search keyword (required)
        :param object lang: 语言/Language
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_word', 'lang', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_word' is set
        if self.api_client.client_side_validation and ('search_word' not in params or
                                                       params['search_word'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_word` when calling `fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_word' in params:
            query_params.append(('search_word', params['search_word']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_search_word_suggestion', 'GET',
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

    def fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get(self, search_word, **kwargs):  # noqa: E501
        """获取搜索关键词建议V2(移动端)/Get search keyword suggestions V2 (Mobile)  # noqa: E501

        # [中文] ### 用途: - 获取搜索关键词建议(移动端接口) - 专为电商搜索结果优化 ### 参数: - search_word: 搜索关键词 (必填) - lang: 语言代码 (en/zh等) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"\",     \"data\": [                        // 建议列表(最多50个)         \"关键词1\",         \"关键词2\",         \"...\"     ] } ```  # [English] ### Purpose: - Get search keyword suggestions (Mobile API) - Optimized for e-commerce search results ### Parameters: - search_word: Search keyword (required) - lang: Language code (en/zh etc.) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"\",     \"data\": [                        // Suggestion list (up to 50)         \"keyword1\",         \"keyword2\",         \"...\"     ] } ```  # [示例/Example] search_word = \"labubu\" lang = \"en\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get(search_word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_word: 搜索关键词/Search keyword (required)
        :param object lang: 语言/Language
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get_with_http_info(search_word, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get_with_http_info(search_word, **kwargs)  # noqa: E501
            return data

    def fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get_with_http_info(self, search_word, **kwargs):  # noqa: E501
        """获取搜索关键词建议V2(移动端)/Get search keyword suggestions V2 (Mobile)  # noqa: E501

        # [中文] ### 用途: - 获取搜索关键词建议(移动端接口) - 专为电商搜索结果优化 ### 参数: - search_word: 搜索关键词 (必填) - lang: 语言代码 (en/zh等) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"\",     \"data\": [                        // 建议列表(最多50个)         \"关键词1\",         \"关键词2\",         \"...\"     ] } ```  # [English] ### Purpose: - Get search keyword suggestions (Mobile API) - Optimized for e-commerce search results ### Parameters: - search_word: Search keyword (required) - lang: Language code (en/zh etc.) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"\",     \"data\": [                        // Suggestion list (up to 50)         \"keyword1\",         \"keyword2\",         \"...\"     ] } ```  # [示例/Example] search_word = \"labubu\" lang = \"en\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get_with_http_info(search_word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_word: 搜索关键词/Search keyword (required)
        :param object lang: 语言/Language
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_word', 'lang', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_word' is set
        if self.api_client.client_side_validation and ('search_word' not in params or
                                                       params['search_word'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_word` when calling `fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_word' in params:
            query_params.append(('search_word', params['search_word']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_search_word_suggestion_v2', 'GET',
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

    def fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get(self, seller_id, **kwargs):  # noqa: E501
        """获取商家商品列表V1/Get seller products list V1  # noqa: E501

        # [中文] ### 用途: - 获取指定商家的商品列表 - 支持分页加载更多商品 ### 参数: - seller_id: 卖家ID (必填) - search_params: 搜索参数，用于分页加载(可选) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // 商品列表(每页30个)             {                 \"product_id\": \"xxx\",                 \"title\": \"商品标题\",                 \"image\": \"商品图片URL\",                 \"product_price_info\": {},  // 价格信息                 \"rate_info\": {},           // 评分信息                 \"sold_info\": {},           // 销量信息                 \"seller_info\": {},         // 卖家信息                 \"seo_url\": \"商品SEO链接\"             }         ],         \"has_more\": true,             // 是否有更多商品         \"load_more_params\": {}        // 加载更多参数(用于下一页)     } } ```  # [English] ### Purpose: - Get product list from specified seller - Support pagination to load more products ### Parameters: - seller_id: Seller ID (required) - search_params: Search parameters for pagination (optional) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // Product list (30 per page)             {                 \"product_id\": \"xxx\",                 \"title\": \"Product title\",                 \"image\": \"Product image URL\",                 \"product_price_info\": {},  // Price info                 \"rate_info\": {},           // Rating info                 \"sold_info\": {},           // Sales info                 \"seller_info\": {},         // Seller info                 \"seo_url\": \"Product SEO URL\"             }         ],         \"has_more\": true,             // Has more products         \"load_more_params\": {}        // Load more params (for next page)     } } ```  # [示例/Example] seller_id = \"7495150558072178725\" search_params = \"\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 卖家ID/Seller ID (required)
        :param object search_params: 搜索参数(用于分页)/Search params (for pagination)
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get_with_http_info(seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get_with_http_info(seller_id, **kwargs)  # noqa: E501
            return data

    def fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """获取商家商品列表V1/Get seller products list V1  # noqa: E501

        # [中文] ### 用途: - 获取指定商家的商品列表 - 支持分页加载更多商品 ### 参数: - seller_id: 卖家ID (必填) - search_params: 搜索参数，用于分页加载(可选) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // 商品列表(每页30个)             {                 \"product_id\": \"xxx\",                 \"title\": \"商品标题\",                 \"image\": \"商品图片URL\",                 \"product_price_info\": {},  // 价格信息                 \"rate_info\": {},           // 评分信息                 \"sold_info\": {},           // 销量信息                 \"seller_info\": {},         // 卖家信息                 \"seo_url\": \"商品SEO链接\"             }         ],         \"has_more\": true,             // 是否有更多商品         \"load_more_params\": {}        // 加载更多参数(用于下一页)     } } ```  # [English] ### Purpose: - Get product list from specified seller - Support pagination to load more products ### Parameters: - seller_id: Seller ID (required) - search_params: Search parameters for pagination (optional) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [                // Product list (30 per page)             {                 \"product_id\": \"xxx\",                 \"title\": \"Product title\",                 \"image\": \"Product image URL\",                 \"product_price_info\": {},  // Price info                 \"rate_info\": {},           // Rating info                 \"sold_info\": {},           // Sales info                 \"seller_info\": {},         // Seller info                 \"seo_url\": \"Product SEO URL\"             }         ],         \"has_more\": true,             // Has more products         \"load_more_params\": {}        // Load more params (for next page)     } } ```  # [示例/Example] seller_id = \"7495150558072178725\" search_params = \"\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 卖家ID/Seller ID (required)
        :param object search_params: 搜索参数(用于分页)/Search params (for pagination)
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['seller_id', 'search_params', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in params or
                                                       params['seller_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `seller_id` when calling `fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in params:
            query_params.append(('seller_id', params['seller_id']))  # noqa: E501
        if 'search_params' in params:
            query_params.append(('search_params', params['search_params']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_seller_products_list', 'GET',
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

    def fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get(self, seller_id, **kwargs):  # noqa: E501
        """获取商家商品列表V2(移动端)/Get seller products list V2 (Mobile)  # noqa: E501

        # [中文] ### 用途: - 获取商家商品列表(移动端接口) - 数据结构更精简 ### 参数: - seller_id: 卖家ID (必填) - searchParams: 搜索参数(可选) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [...],            // 商品列表         \"has_more\": true,             // 是否有更多         \"load_more_params\": {}        // 加载更多参数     } } ```  # [English] ### Purpose: - Get seller product list (Mobile API) - More streamlined data structure ### Parameters: - seller_id: Seller ID (required) - searchParams: Search parameters (optional) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [...],            // Product list         \"has_more\": true,             // Has more         \"load_more_params\": {}        // Load more params     } } ```  # [示例/Example] seller_id = \"7495150558072178725\" searchParams = \"\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 卖家ID/Seller ID (required)
        :param object search_params: 搜索参数/Search params
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get_with_http_info(seller_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get_with_http_info(seller_id, **kwargs)  # noqa: E501
            return data

    def fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get_with_http_info(self, seller_id, **kwargs):  # noqa: E501
        """获取商家商品列表V2(移动端)/Get seller products list V2 (Mobile)  # noqa: E501

        # [中文] ### 用途: - 获取商家商品列表(移动端接口) - 数据结构更精简 ### 参数: - seller_id: 卖家ID (必填) - searchParams: 搜索参数(可选) - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID) ### 重要提示: - 由于接口风控原因，请务必将请求timeout设置为30秒 - 如遇到400错误代码，请重试请求3次 ### 返回数据结构: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [...],            // 商品列表         \"has_more\": true,             // 是否有更多         \"load_more_params\": {}        // 加载更多参数     } } ```  # [English] ### Purpose: - Get seller product list (Mobile API) - More streamlined data structure ### Parameters: - seller_id: Seller ID (required) - searchParams: Search parameters (optional) - region: Region code (US/GB/SG/MY/PH/TH/VN/ID) ### Important Notice: - Due to API rate limiting, please set request timeout to 30 seconds - If you encounter error code 400, please retry the request 3 times ### Response Structure: ```json {     \"code\": 0,     \"message\": \"success\",     \"data\": {         \"products\": [...],            // Product list         \"has_more\": true,             // Has more         \"load_more_params\": {}        // Load more params     } } ```  # [示例/Example] seller_id = \"7495150558072178725\" searchParams = \"\" region = \"US\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get_with_http_info(seller_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object seller_id: 卖家ID/Seller ID (required)
        :param object search_params: 搜索参数/Search params
        :param object region: 地区代码/Region code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['seller_id', 'search_params', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'seller_id' is set
        if self.api_client.client_side_validation and ('seller_id' not in params or
                                                       params['seller_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `seller_id` when calling `fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'seller_id' in params:
            query_params.append(('seller_id', params['seller_id']))  # noqa: E501
        if 'search_params' in params:
            query_params.append(('searchParams', params['search_params']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/shop/web/fetch_seller_products_list_v2', 'GET',
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
