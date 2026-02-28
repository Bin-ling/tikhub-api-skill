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


class TikTokWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def decrypt_str_data_api_v1_tiktok_web_decrypt_str_data_get(self, encrypted_data, **kwargs):  # noqa: E501
        """解密strData/Decrypt strData  # noqa: E501

        # [中文] ### 用途: - 解密strData指纹数据，用于分析msToken请求中的指纹信息 ### 参数: - encrypted_data: 加密后的strData字符串，从浏览器自行抓包获取 ### 返回: - 解密后的原始指纹数据，包含浏览器指纹信息和环境信息等。  # [English] ### Purpose: - Decrypt strData fingerprint data to analyze fingerprint info in msToken request ### Parameters: - encrypted_data: Encrypted strData string, obtained from browser packet capture ### Return: - Decrypted raw fingerprint data, including browser fingerprint info and environment info, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.decrypt_str_data_api_v1_tiktok_web_decrypt_str_data_get(encrypted_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object encrypted_data: 加密后的strData字符串/Encrypted strData string (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.decrypt_str_data_api_v1_tiktok_web_decrypt_str_data_get_with_http_info(encrypted_data, **kwargs)  # noqa: E501
        else:
            (data) = self.decrypt_str_data_api_v1_tiktok_web_decrypt_str_data_get_with_http_info(encrypted_data, **kwargs)  # noqa: E501
            return data

    def decrypt_str_data_api_v1_tiktok_web_decrypt_str_data_get_with_http_info(self, encrypted_data, **kwargs):  # noqa: E501
        """解密strData/Decrypt strData  # noqa: E501

        # [中文] ### 用途: - 解密strData指纹数据，用于分析msToken请求中的指纹信息 ### 参数: - encrypted_data: 加密后的strData字符串，从浏览器自行抓包获取 ### 返回: - 解密后的原始指纹数据，包含浏览器指纹信息和环境信息等。  # [English] ### Purpose: - Decrypt strData fingerprint data to analyze fingerprint info in msToken request ### Parameters: - encrypted_data: Encrypted strData string, obtained from browser packet capture ### Return: - Decrypted raw fingerprint data, including browser fingerprint info and environment info, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.decrypt_str_data_api_v1_tiktok_web_decrypt_str_data_get_with_http_info(encrypted_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object encrypted_data: 加密后的strData字符串/Encrypted strData string (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['encrypted_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method decrypt_str_data_api_v1_tiktok_web_decrypt_str_data_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'encrypted_data' is set
        if self.api_client.client_side_validation and ('encrypted_data' not in params or
                                                       params['encrypted_data'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `encrypted_data` when calling `decrypt_str_data_api_v1_tiktok_web_decrypt_str_data_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'encrypted_data' in params:
            query_params.append(('encrypted_data', params['encrypted_data']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/decrypt_strData', 'GET',
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

    def device_register_api_v1_tiktok_web_device_register_get(self, **kwargs):  # noqa: E501
        """设备注册/Register device for TikTok Web  # noqa: E501

        # [中文] ### 用途: - 设备注册，为TikTok Web生成设备ID和游客Cookie ### 参数: - 无 ### 返回: - 设备注册信息，包括设备ID和游客Cookie  # [English] ### Purpose: - Register device to generate device ID and guest Cookie for TikTok Web ### Parameters: - None ### Return: - Device registration information, including device ID and guest Cookie # [响应/Response]: ```json {     \"deviceId\": \"7556227929396708877\",     \"cookie\": \"tt_chain_token=wBqjjz5I8m1bt96uxA1s8A==\",     \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\" } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_register_api_v1_tiktok_web_device_register_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.device_register_api_v1_tiktok_web_device_register_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.device_register_api_v1_tiktok_web_device_register_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def device_register_api_v1_tiktok_web_device_register_get_with_http_info(self, **kwargs):  # noqa: E501
        """设备注册/Register device for TikTok Web  # noqa: E501

        # [中文] ### 用途: - 设备注册，为TikTok Web生成设备ID和游客Cookie ### 参数: - 无 ### 返回: - 设备注册信息，包括设备ID和游客Cookie  # [English] ### Purpose: - Register device to generate device ID and guest Cookie for TikTok Web ### Parameters: - None ### Return: - Device registration information, including device ID and guest Cookie # [响应/Response]: ```json {     \"deviceId\": \"7556227929396708877\",     \"cookie\": \"tt_chain_token=wBqjjz5I8m1bt96uxA1s8A==\",     \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\" } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.device_register_api_v1_tiktok_web_device_register_get_with_http_info(async_req=True)
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
                    " to method device_register_api_v1_tiktok_web_device_register_get" % key
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
            '/api/v1/tiktok/web/device_register', 'GET',
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

    def encrypt_str_data_api_v1_tiktok_web_encrypt_str_data_get(self, data, **kwargs):  # noqa: E501
        """加密strData/Encrypt strData  # noqa: E501

        # [中文] ### 用途: - 加密strData指纹数据，用于生成msToken请求 ### 参数: - data: 原始指纹数据字符串（请先将JSON格式然后转换成字符串进行请求） ### 返回: - 加密后的strData  # [English] ### Purpose: - Encrypt strData fingerprint data for msToken request ### Parameters: - data: Raw fingerprint data string (please convert JSON format to string before requesting) ### Return: - Encrypted strData  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.encrypt_str_data_api_v1_tiktok_web_encrypt_str_data_get(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object data: 原始指纹数据字符串（JSON格式或字典字符串）/Raw fingerprint data string (JSON format or dict string) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.encrypt_str_data_api_v1_tiktok_web_encrypt_str_data_get_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.encrypt_str_data_api_v1_tiktok_web_encrypt_str_data_get_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def encrypt_str_data_api_v1_tiktok_web_encrypt_str_data_get_with_http_info(self, data, **kwargs):  # noqa: E501
        """加密strData/Encrypt strData  # noqa: E501

        # [中文] ### 用途: - 加密strData指纹数据，用于生成msToken请求 ### 参数: - data: 原始指纹数据字符串（请先将JSON格式然后转换成字符串进行请求） ### 返回: - 加密后的strData  # [English] ### Purpose: - Encrypt strData fingerprint data for msToken request ### Parameters: - data: Raw fingerprint data string (please convert JSON format to string before requesting) ### Return: - Encrypted strData  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.encrypt_str_data_api_v1_tiktok_web_encrypt_str_data_get_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object data: 原始指纹数据字符串（JSON格式或字典字符串）/Raw fingerprint data string (JSON format or dict string) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method encrypt_str_data_api_v1_tiktok_web_encrypt_str_data_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in params or
                                                       params['data'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data` when calling `encrypt_str_data_api_v1_tiktok_web_encrypt_str_data_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'data' in params:
            query_params.append(('data', params['data']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/encrypt_strData', 'GET',
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

    def fetch_batch_check_live_alive_api_v1_tiktok_web_fetch_batch_check_live_alive_get(self, room_ids, **kwargs):  # noqa: E501
        """批量直播间开播状态检测/Batch live room start status check  # noqa: E501

        # [中文] ### 用途: - 批量直播间开播状态检测 - 最多支持50个直播间同时查询 - 如果某个直播间不存在或已下播，则对应位置返回空或null。 ### 参数: - room_ids: 直播间ID列表，用英文逗号分隔，如：7530611486784277278,7530633767468288782 ### 返回: - 批量直播间开播状态列表 ### 价格: - 定价0.025$，请尽量达到50个直播间查询，避免浪费API调用次数。 ### 说明: - 同一个room_id不会重复返回开播状态。  # [English] ### Purpose: - Batch live room start status check - Support up to 50 live rooms query at once - If a live room does not exist or has ended, the corresponding position will return empty or null. ### Parameters: - room_ids: Live room ID list separated by commas, e.g.: 7530611486784277278,7530633767468288782 ### Return: - Batch live room start status list ### Price: - Charged by the number of live rooms queried, 0.025$ per live room, please try to query 50 live rooms to avoid wasting API call counts. ### Note: - The same room_id will not return the start status repeatedly.  # [示例/Example] room_ids = \"7530611486784277278,7530633767468288782,7530636465034775310,7530604930088848142\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_batch_check_live_alive_api_v1_tiktok_web_fetch_batch_check_live_alive_get(room_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_ids: 直播间ID列表，用英文逗号分隔，最多支持50个/Live room ID list separated by commas, up to 50 IDs (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_batch_check_live_alive_api_v1_tiktok_web_fetch_batch_check_live_alive_get_with_http_info(room_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_batch_check_live_alive_api_v1_tiktok_web_fetch_batch_check_live_alive_get_with_http_info(room_ids, **kwargs)  # noqa: E501
            return data

    def fetch_batch_check_live_alive_api_v1_tiktok_web_fetch_batch_check_live_alive_get_with_http_info(self, room_ids, **kwargs):  # noqa: E501
        """批量直播间开播状态检测/Batch live room start status check  # noqa: E501

        # [中文] ### 用途: - 批量直播间开播状态检测 - 最多支持50个直播间同时查询 - 如果某个直播间不存在或已下播，则对应位置返回空或null。 ### 参数: - room_ids: 直播间ID列表，用英文逗号分隔，如：7530611486784277278,7530633767468288782 ### 返回: - 批量直播间开播状态列表 ### 价格: - 定价0.025$，请尽量达到50个直播间查询，避免浪费API调用次数。 ### 说明: - 同一个room_id不会重复返回开播状态。  # [English] ### Purpose: - Batch live room start status check - Support up to 50 live rooms query at once - If a live room does not exist or has ended, the corresponding position will return empty or null. ### Parameters: - room_ids: Live room ID list separated by commas, e.g.: 7530611486784277278,7530633767468288782 ### Return: - Batch live room start status list ### Price: - Charged by the number of live rooms queried, 0.025$ per live room, please try to query 50 live rooms to avoid wasting API call counts. ### Note: - The same room_id will not return the start status repeatedly.  # [示例/Example] room_ids = \"7530611486784277278,7530633767468288782,7530636465034775310,7530604930088848142\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_batch_check_live_alive_api_v1_tiktok_web_fetch_batch_check_live_alive_get_with_http_info(room_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_ids: 直播间ID列表，用英文逗号分隔，最多支持50个/Live room ID list separated by commas, up to 50 IDs (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_batch_check_live_alive_api_v1_tiktok_web_fetch_batch_check_live_alive_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_ids' is set
        if self.api_client.client_side_validation and ('room_ids' not in params or
                                                       params['room_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_ids` when calling `fetch_batch_check_live_alive_api_v1_tiktok_web_fetch_batch_check_live_alive_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_ids' in params:
            query_params.append(('room_ids', params['room_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_batch_check_live_alive', 'GET',
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

    def fetch_check_live_alive_api_v1_tiktok_web_fetch_check_live_alive_get(self, room_id, **kwargs):  # noqa: E501
        """直播间开播状态检测/Live room start status check  # noqa: E501

        # [中文] ### 用途: - 直播间开播状态检测 - 如果当前直播间不存在或已下播，则返回空。 ### 参数: - room_id: 直播间ID ### 返回: - 直播间开播状态  # [English] ### Purpose: - Live room start status check - If the current live room does not exist or has ended, it will return empty. ### Parameters: - room_id: Live room ID ### Return: - Live room start status  # [示例/Example] room_id = \"7381444193462078214\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_check_live_alive_api_v1_tiktok_web_fetch_check_live_alive_get(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间ID/Live room ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_check_live_alive_api_v1_tiktok_web_fetch_check_live_alive_get_with_http_info(room_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_check_live_alive_api_v1_tiktok_web_fetch_check_live_alive_get_with_http_info(room_id, **kwargs)  # noqa: E501
            return data

    def fetch_check_live_alive_api_v1_tiktok_web_fetch_check_live_alive_get_with_http_info(self, room_id, **kwargs):  # noqa: E501
        """直播间开播状态检测/Live room start status check  # noqa: E501

        # [中文] ### 用途: - 直播间开播状态检测 - 如果当前直播间不存在或已下播，则返回空。 ### 参数: - room_id: 直播间ID ### 返回: - 直播间开播状态  # [English] ### Purpose: - Live room start status check - If the current live room does not exist or has ended, it will return empty. ### Parameters: - room_id: Live room ID ### Return: - Live room start status  # [示例/Example] room_id = \"7381444193462078214\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_check_live_alive_api_v1_tiktok_web_fetch_check_live_alive_get_with_http_info(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间ID/Live room ID (required)
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
                    " to method fetch_check_live_alive_api_v1_tiktok_web_fetch_check_live_alive_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_check_live_alive_api_v1_tiktok_web_fetch_check_live_alive_get`")  # noqa: E501

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
            '/api/v1/tiktok/web/fetch_check_live_alive', 'GET',
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

    def fetch_explore_post_api_v1_tiktok_web_fetch_explore_post_get(self, **kwargs):  # noqa: E501
        """获取探索作品数据/Get explore video data  # noqa: E501

        # [中文] ### 用途: - 获取探索作品数据 ### 参数: - categoryType: 作品分类     - 100: 动画与漫画     - 101: 表演     - 102: 美容护理     - 103: 游戏     - 104: 喜剧     - 105: 日常生活     - 106: 家庭     - 107: 情感关系     - 108: 戏剧     - 109: 穿搭     - 110: 对口型     - 111: 美食     - 112: 运动     - 113: 动物     - 114: 社会     - 115: 汽车     - 116: 教育     - 117: 健身和健康     - 118: 科技     - 119: 唱歌跳舞     - 120: 全部 - count: 每页数量 ### 返回: - 作品数据 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get explore video data ### Parameters: - categoryType: Video category     - 100: Animation and comics     - 101: Performance     - 102: Beauty care     - 103: Game     - 104: Comedy     - 105: Daily life     - 106: Family     - 107: Emotional relationship     - 108: Drama     - 109: Dress up     - 110: Dubbing     - 111: Food     - 112: Sports     - 113: Animals     - 114: Society     - 115: Car     - 116: Education     - 117: Fitness and health     - 118: Technology     - 119: Singing and dancing     - 120: All - count: Number per page ### Return: - Video data ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] categoryType = \"120\" count = 16  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_explore_post_api_v1_tiktok_web_fetch_explore_post_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category_type: 作品分类/Video category
        :param object count: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_explore_post_api_v1_tiktok_web_fetch_explore_post_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_explore_post_api_v1_tiktok_web_fetch_explore_post_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_explore_post_api_v1_tiktok_web_fetch_explore_post_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取探索作品数据/Get explore video data  # noqa: E501

        # [中文] ### 用途: - 获取探索作品数据 ### 参数: - categoryType: 作品分类     - 100: 动画与漫画     - 101: 表演     - 102: 美容护理     - 103: 游戏     - 104: 喜剧     - 105: 日常生活     - 106: 家庭     - 107: 情感关系     - 108: 戏剧     - 109: 穿搭     - 110: 对口型     - 111: 美食     - 112: 运动     - 113: 动物     - 114: 社会     - 115: 汽车     - 116: 教育     - 117: 健身和健康     - 118: 科技     - 119: 唱歌跳舞     - 120: 全部 - count: 每页数量 ### 返回: - 作品数据 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get explore video data ### Parameters: - categoryType: Video category     - 100: Animation and comics     - 101: Performance     - 102: Beauty care     - 103: Game     - 104: Comedy     - 105: Daily life     - 106: Family     - 107: Emotional relationship     - 108: Drama     - 109: Dress up     - 110: Dubbing     - 111: Food     - 112: Sports     - 113: Animals     - 114: Society     - 115: Car     - 116: Education     - 117: Fitness and health     - 118: Technology     - 119: Singing and dancing     - 120: All - count: Number per page ### Return: - Video data ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] categoryType = \"120\" count = 16  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_explore_post_api_v1_tiktok_web_fetch_explore_post_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category_type: 作品分类/Video category
        :param object count: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_type', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_explore_post_api_v1_tiktok_web_fetch_explore_post_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category_type' in params:
            query_params.append(('categoryType', params['category_type']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_explore_post', 'GET',
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

    def fetch_general_search_api_v1_tiktok_web_fetch_general_search_get(self, keyword, **kwargs):  # noqa: E501
        """获取综合搜索列表/Get general search list  # noqa: E501

        # [中文] ### 用途: - 获取综合搜索列表 ### 参数: - keyword: 搜索关键词 - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供) ### 返回: - 综合搜索列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get general search list ### Parameters: - keyword: Search keyword - offset: Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required) ### Return: - General search list ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] keyword = \"TikTok\" offset = 0 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_general_search_api_v1_tiktok_web_fetch_general_search_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object offset: 翻页游标/Page cursor
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :param object cookie: 用户cookie(按需提供)/User cookie(if needed)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_general_search_api_v1_tiktok_web_fetch_general_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_general_search_api_v1_tiktok_web_fetch_general_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_general_search_api_v1_tiktok_web_fetch_general_search_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取综合搜索列表/Get general search list  # noqa: E501

        # [中文] ### 用途: - 获取综合搜索列表 ### 参数: - keyword: 搜索关键词 - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供) ### 返回: - 综合搜索列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get general search list ### Parameters: - keyword: Search keyword - offset: Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required) ### Return: - General search list ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] keyword = \"TikTok\" offset = 0 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_general_search_api_v1_tiktok_web_fetch_general_search_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object offset: 翻页游标/Page cursor
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :param object cookie: 用户cookie(按需提供)/User cookie(if needed)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'search_id', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_general_search_api_v1_tiktok_web_fetch_general_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_general_search_api_v1_tiktok_web_fetch_general_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_general_search', 'GET',
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

    def fetch_gift_name_by_id_api_v1_tiktok_web_fetch_gift_name_by_id_post(self, **kwargs):  # noqa: E501
        """根据Gift ID查询礼物名称/Get gift name by gift ID  # noqa: E501

        根据TikTok的Gift ID查询对应的礼物名称 | Get gift name by TikTok gift ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_gift_name_by_id_api_v1_tiktok_web_fetch_gift_name_by_id_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_gift_name_by_id_api_v1_tiktok_web_fetch_gift_name_by_id_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_gift_name_by_id_api_v1_tiktok_web_fetch_gift_name_by_id_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_gift_name_by_id_api_v1_tiktok_web_fetch_gift_name_by_id_post_with_http_info(self, **kwargs):  # noqa: E501
        """根据Gift ID查询礼物名称/Get gift name by gift ID  # noqa: E501

        根据TikTok的Gift ID查询对应的礼物名称 | Get gift name by TikTok gift ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_gift_name_by_id_api_v1_tiktok_web_fetch_gift_name_by_id_post_with_http_info(async_req=True)
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
                    " to method fetch_gift_name_by_id_api_v1_tiktok_web_fetch_gift_name_by_id_post" % key
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
            '/api/v1/tiktok/web/fetch_gift_name_by_id', 'POST',
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

    def fetch_gift_names_by_ids_api_v1_tiktok_web_fetch_gift_names_by_ids_post(self, **kwargs):  # noqa: E501
        """批量查询Gift ID对应的礼物名称($0.025/次,建议50个)/Batch get gift names by gift IDs ($0.025/call, suggest 50)  # noqa: E501

        批量查询多个TikTok Gift ID对应的礼物名称。计费：$0.025每次调用。建议每次查询50个ID以获得最佳性价比，超过50个时自动处理前50个 | Batch get gift names by multiple TikTok gift IDs. Pricing: $0.025 per call. Recommend querying 50 IDs at once for best value, auto-process first 50 IDs if more than 50  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_gift_names_by_ids_api_v1_tiktok_web_fetch_gift_names_by_ids_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_gift_names_by_ids_api_v1_tiktok_web_fetch_gift_names_by_ids_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_gift_names_by_ids_api_v1_tiktok_web_fetch_gift_names_by_ids_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_gift_names_by_ids_api_v1_tiktok_web_fetch_gift_names_by_ids_post_with_http_info(self, **kwargs):  # noqa: E501
        """批量查询Gift ID对应的礼物名称($0.025/次,建议50个)/Batch get gift names by gift IDs ($0.025/call, suggest 50)  # noqa: E501

        批量查询多个TikTok Gift ID对应的礼物名称。计费：$0.025每次调用。建议每次查询50个ID以获得最佳性价比，超过50个时自动处理前50个 | Batch get gift names by multiple TikTok gift IDs. Pricing: $0.025 per call. Recommend querying 50 IDs at once for best value, auto-process first 50 IDs if more than 50  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_gift_names_by_ids_api_v1_tiktok_web_fetch_gift_names_by_ids_post_with_http_info(async_req=True)
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
                    " to method fetch_gift_names_by_ids_api_v1_tiktok_web_fetch_gift_names_by_ids_post" % key
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
            '/api/v1/tiktok/web/fetch_gift_names_by_ids', 'POST',
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

    def fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post(self, **kwargs):  # noqa: E501
        """首页推荐作品/Home Feed  # noqa: E501

        # [中文] ### 用途: - 首页推荐作品 ### 参数: - count: 每页数量 - cookie: 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。 ### 返回: - 首页推荐作品 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Home Feed ### Parameters: - count: Number per page - cookie: User's own cookie, optional parameter, used for personalized recommendations of interface return data. ### Return: - Home Feed ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] count = 15 Cookie = \"Your_Cookie\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post_with_http_info(self, **kwargs):  # noqa: E501
        """首页推荐作品/Home Feed  # noqa: E501

        # [中文] ### 用途: - 首页推荐作品 ### 参数: - count: 每页数量 - cookie: 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。 ### 返回: - 首页推荐作品 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Home Feed ### Parameters: - count: Number per page - cookie: User's own cookie, optional parameter, used for personalized recommendations of interface return data. ### Return: - Home Feed ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] count = 15 Cookie = \"Your_Cookie\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post_with_http_info(async_req=True)
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
                    " to method fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post" % key
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
            '/api/v1/tiktok/web/fetch_home_feed', 'POST',
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

    def fetch_live_gift_list_api_v1_tiktok_web_fetch_live_gift_list_get(self, **kwargs):  # noqa: E501
        """获取直播间礼物列表/Get live room gift list  # noqa: E501

        # [中文] ### 用途: - 获取直播间礼物列表 - room_id为可选参数，不传则获取通用礼物列表（2025年08月15日统计是256种礼物） ### 参数: - room_id: 直播间ID（可选） ### 返回: - 直播间礼物列表数据 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get live room gift list - room_id is optional parameter, if not provided, will get general gift list (as of August 15, 2025, there are 256 types of gifts) ### Parameters: - room_id: Live room ID (optional) ### Return: - Live room gift list data ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] room_id = \"7381444193462078214\"  # 可选/Optional  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_gift_list_api_v1_tiktok_web_fetch_live_gift_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间ID，可选参数/Live room ID, optional parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_gift_list_api_v1_tiktok_web_fetch_live_gift_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_gift_list_api_v1_tiktok_web_fetch_live_gift_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_live_gift_list_api_v1_tiktok_web_fetch_live_gift_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取直播间礼物列表/Get live room gift list  # noqa: E501

        # [中文] ### 用途: - 获取直播间礼物列表 - room_id为可选参数，不传则获取通用礼物列表（2025年08月15日统计是256种礼物） ### 参数: - room_id: 直播间ID（可选） ### 返回: - 直播间礼物列表数据 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get live room gift list - room_id is optional parameter, if not provided, will get general gift list (as of August 15, 2025, there are 256 types of gifts) ### Parameters: - room_id: Live room ID (optional) ### Return: - Live room gift list data ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] room_id = \"7381444193462078214\"  # 可选/Optional  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_gift_list_api_v1_tiktok_web_fetch_live_gift_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间ID，可选参数/Live room ID, optional parameter
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
                    " to method fetch_live_gift_list_api_v1_tiktok_web_fetch_live_gift_list_get" % key
                )
            params[key] = val
        del params['kwargs']

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
            '/api/v1/tiktok/web/fetch_live_gift_list', 'GET',
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

    def fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get(self, room_id, user_unique_id, **kwargs):  # noqa: E501
        """TikTok直播间弹幕参数获取/tiktok live room danmaku parameters  # noqa: E501

        # [中文] ### 用途: - TikTok直播间弹幕参数获取 ### 参数: - room_id: 直播间号 - user_unique_id: 用户唯一ID  ### 返回: - 弹幕参数数据  # [English] ### Purpose: - TikTok live room danmaku parameters ### Parameters: - room_id: Live room id - user_unique_id: User unique ID  ### Return: - Danmaku parameter data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get(room_id, user_unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间号/Live room id (required)
        :param object user_unique_id: 用户唯一ID/User unique ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get_with_http_info(room_id, user_unique_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get_with_http_info(room_id, user_unique_id, **kwargs)  # noqa: E501
            return data

    def fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get_with_http_info(self, room_id, user_unique_id, **kwargs):  # noqa: E501
        """TikTok直播间弹幕参数获取/tiktok live room danmaku parameters  # noqa: E501

        # [中文] ### 用途: - TikTok直播间弹幕参数获取 ### 参数: - room_id: 直播间号 - user_unique_id: 用户唯一ID  ### 返回: - 弹幕参数数据  # [English] ### Purpose: - TikTok live room danmaku parameters ### Parameters: - room_id: Live room id - user_unique_id: User unique ID  ### Return: - Danmaku parameter data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get_with_http_info(room_id, user_unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object room_id: 直播间号/Live room id (required)
        :param object user_unique_id: 用户唯一ID/User unique ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id', 'user_unique_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if self.api_client.client_side_validation and ('room_id' not in params or
                                                       params['room_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `room_id` when calling `fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get`")  # noqa: E501
        # verify the required parameter 'user_unique_id' is set
        if self.api_client.client_side_validation and ('user_unique_id' not in params or
                                                       params['user_unique_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_unique_id` when calling `fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501
        if 'user_unique_id' in params:
            query_params.append(('user_unique_id', params['user_unique_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_live_im_fetch', 'GET',
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

    def fetch_live_recommend_api_v1_tiktok_web_fetch_live_recommend_get(self, related_live_tag, **kwargs):  # noqa: E501
        """获取直播间首页推荐列表/Get live room homepage recommendation list  # noqa: E501

        # [中文] ### 用途: - 获取直播间首页推荐列表 ### 参数: - related_live_tag: 相关直播标签 ### 返回: - 直播间首页推荐列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get live room homepage recommendation list ### Parameters: - related_live_tag: Related live tag ### Return: - Live room homepage recommendation list ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] related_live_tag = \"VALORANT\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_recommend_api_v1_tiktok_web_fetch_live_recommend_get(related_live_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object related_live_tag: 相关直播标签/Related live tag (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_recommend_api_v1_tiktok_web_fetch_live_recommend_get_with_http_info(related_live_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_recommend_api_v1_tiktok_web_fetch_live_recommend_get_with_http_info(related_live_tag, **kwargs)  # noqa: E501
            return data

    def fetch_live_recommend_api_v1_tiktok_web_fetch_live_recommend_get_with_http_info(self, related_live_tag, **kwargs):  # noqa: E501
        """获取直播间首页推荐列表/Get live room homepage recommendation list  # noqa: E501

        # [中文] ### 用途: - 获取直播间首页推荐列表 ### 参数: - related_live_tag: 相关直播标签 ### 返回: - 直播间首页推荐列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get live room homepage recommendation list ### Parameters: - related_live_tag: Related live tag ### Return: - Live room homepage recommendation list ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] related_live_tag = \"VALORANT\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_recommend_api_v1_tiktok_web_fetch_live_recommend_get_with_http_info(related_live_tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object related_live_tag: 相关直播标签/Related live tag (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['related_live_tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_live_recommend_api_v1_tiktok_web_fetch_live_recommend_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'related_live_tag' is set
        if self.api_client.client_side_validation and ('related_live_tag' not in params or
                                                       params['related_live_tag'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `related_live_tag` when calling `fetch_live_recommend_api_v1_tiktok_web_fetch_live_recommend_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'related_live_tag' in params:
            query_params.append(('related_live_tag', params['related_live_tag']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_live_recommend', 'GET',
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

    def fetch_post_comment_api_v1_tiktok_web_fetch_post_comment_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取作品的评论列表/Get video comments  # noqa: E501

        # [中文] ### 用途: - 获取作品的评论列表 ### 参数: - aweme_id: 作品id - cursor: 翻页游标 - count: 每页数量 - current_region: 当前地区，默认为空。 ### 返回: - 作品的评论列表  # [English] ### Purpose: - Get video comments ### Parameters: - aweme_id: Video id - cursor: Page cursor - count: Number per page - current_region: Current region, default is empty. ### Return: - Video comments  # [示例/Eample] aweme_id = \"7304809083817774382\" cursor = 0 count = 20 current_region = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comment_api_v1_tiktok_web_fetch_post_comment_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object current_region: 当前地区/Current region
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comment_api_v1_tiktok_web_fetch_post_comment_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comment_api_v1_tiktok_web_fetch_post_comment_get_with_http_info(aweme_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_comment_api_v1_tiktok_web_fetch_post_comment_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取作品的评论列表/Get video comments  # noqa: E501

        # [中文] ### 用途: - 获取作品的评论列表 ### 参数: - aweme_id: 作品id - cursor: 翻页游标 - count: 每页数量 - current_region: 当前地区，默认为空。 ### 返回: - 作品的评论列表  # [English] ### Purpose: - Get video comments ### Parameters: - aweme_id: Video id - cursor: Page cursor - count: Number per page - current_region: Current region, default is empty. ### Return: - Video comments  # [示例/Eample] aweme_id = \"7304809083817774382\" cursor = 0 count = 20 current_region = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comment_api_v1_tiktok_web_fetch_post_comment_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object aweme_id: 作品id/Video id (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object current_region: 当前地区/Current region
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aweme_id', 'cursor', 'count', 'current_region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comment_api_v1_tiktok_web_fetch_post_comment_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in params or
                                                       params['aweme_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `aweme_id` when calling `fetch_post_comment_api_v1_tiktok_web_fetch_post_comment_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in params:
            query_params.append(('aweme_id', params['aweme_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'current_region' in params:
            query_params.append(('current_region', params['current_region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_post_comment', 'GET',
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

    def fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get(self, item_id, comment_id, **kwargs):  # noqa: E501
        """获取作品的评论回复列表/Get video comment replies  # noqa: E501

        # [中文] ### 用途: - 获取作品的评论回复列表 ### 参数: - item_id: 作品id - comment_id: 评论id - cursor: 翻页游标 - count: 每页数量 - current_region: 当前地区，默认为空。 ### 返回: - 作品的评论回复列表  # [English] ### Purpose: - Get video comment replies ### Parameters: - item_id: Video id - comment_id: Comment id - cursor: Page cursor - count: Number per page - current_region: Current region, default is empty. ### Return: - Video comment replies  # [示例/Eample] item_id = \"7304809083817774382\" comment_id = \"7304877760886588191\" cursor = 0 count = 20 current_region = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
        :param object comment_id: 评论id/Comment id (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object current_region: 当前地区/Current region
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get_with_http_info(self, item_id, comment_id, **kwargs):  # noqa: E501
        """获取作品的评论回复列表/Get video comment replies  # noqa: E501

        # [中文] ### 用途: - 获取作品的评论回复列表 ### 参数: - item_id: 作品id - comment_id: 评论id - cursor: 翻页游标 - count: 每页数量 - current_region: 当前地区，默认为空。 ### 返回: - 作品的评论回复列表  # [English] ### Purpose: - Get video comment replies ### Parameters: - item_id: Video id - comment_id: Comment id - cursor: Page cursor - count: Number per page - current_region: Current region, default is empty. ### Return: - Video comment replies  # [示例/Eample] item_id = \"7304809083817774382\" comment_id = \"7304877760886588191\" cursor = 0 count = 20 current_region = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get_with_http_info(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
        :param object comment_id: 评论id/Comment id (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object current_region: 当前地区/Current region
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'comment_id', 'cursor', 'count', 'current_region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get`")  # noqa: E501

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
        if 'current_region' in params:
            query_params.append(('current_region', params['current_region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_post_comment_reply', 'GET',
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

    def fetch_post_detail_api_v1_tiktok_web_fetch_post_detail_get(self, item_id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 ### 参数: - itemId: 作品id ### 返回: - 作品数据 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get single video data ### Parameters: - itemId: Video id ### Return: - Video data ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] itemId = \"7339393672959757570\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_tiktok_web_fetch_post_detail_get(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_detail_api_v1_tiktok_web_fetch_post_detail_get_with_http_info(item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_detail_api_v1_tiktok_web_fetch_post_detail_get_with_http_info(item_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_detail_api_v1_tiktok_web_fetch_post_detail_get_with_http_info(self, item_id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single video data  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 ### 参数: - itemId: 作品id ### 返回: - 作品数据 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get single video data ### Parameters: - itemId: Video id ### Return: - Video data ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] itemId = \"7339393672959757570\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_tiktok_web_fetch_post_detail_get_with_http_info(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
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
                    " to method fetch_post_detail_api_v1_tiktok_web_fetch_post_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `fetch_post_detail_api_v1_tiktok_web_fetch_post_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item_id' in params:
            query_params.append(('itemId', params['item_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_post_detail', 'GET',
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

    def fetch_post_detail_v2_api_v1_tiktok_web_fetch_post_detail_v2_get(self, item_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 ### 参数: - itemId: 作品id ### 返回: - 作品数据 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get single video data ### Parameters: - itemId: Video id ### Return: - Video data ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] itemId = \"7339393672959757570\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_v2_api_v1_tiktok_web_fetch_post_detail_v2_get(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_detail_v2_api_v1_tiktok_web_fetch_post_detail_v2_get_with_http_info(item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_detail_v2_api_v1_tiktok_web_fetch_post_detail_v2_get_with_http_info(item_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_detail_v2_api_v1_tiktok_web_fetch_post_detail_v2_get_with_http_info(self, item_id, **kwargs):  # noqa: E501
        """获取单个作品数据 V2/Get single video data V2  # noqa: E501

        # [中文] ### 用途: - 获取单个作品数据 ### 参数: - itemId: 作品id ### 返回: - 作品数据 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get single video data ### Parameters: - itemId: Video id ### Return: - Video data ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] itemId = \"7339393672959757570\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_v2_api_v1_tiktok_web_fetch_post_detail_v2_get_with_http_info(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object item_id: 作品id/Video id (required)
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
                    " to method fetch_post_detail_v2_api_v1_tiktok_web_fetch_post_detail_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `fetch_post_detail_v2_api_v1_tiktok_web_fetch_post_detail_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item_id' in params:
            query_params.append(('itemId', params['item_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_post_detail_v2', 'GET',
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

    def fetch_search_keyword_suggest_api_v1_tiktok_web_fetch_search_keyword_suggest_get(self, keyword, **kwargs):  # noqa: E501
        """搜索关键字推荐/Search keyword suggest  # noqa: E501

        # [中文] ### 用途: - 搜索关键字推荐 ### 参数: - keyword: 搜索关键词 ### 返回: - 关键字推荐列表  # [English] ### Purpose: - Search keyword suggest ### Parameters: - keyword: Search keyword ### Return: - Keyword suggest list  # [示例/Example] keyword = \"TikTok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_keyword_suggest_api_v1_tiktok_web_fetch_search_keyword_suggest_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_keyword_suggest_api_v1_tiktok_web_fetch_search_keyword_suggest_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_keyword_suggest_api_v1_tiktok_web_fetch_search_keyword_suggest_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_keyword_suggest_api_v1_tiktok_web_fetch_search_keyword_suggest_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索关键字推荐/Search keyword suggest  # noqa: E501

        # [中文] ### 用途: - 搜索关键字推荐 ### 参数: - keyword: 搜索关键词 ### 返回: - 关键字推荐列表  # [English] ### Purpose: - Search keyword suggest ### Parameters: - keyword: Search keyword ### Return: - Keyword suggest list  # [示例/Example] keyword = \"TikTok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_keyword_suggest_api_v1_tiktok_web_fetch_search_keyword_suggest_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
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
                    " to method fetch_search_keyword_suggest_api_v1_tiktok_web_fetch_search_keyword_suggest_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_keyword_suggest_api_v1_tiktok_web_fetch_search_keyword_suggest_get`")  # noqa: E501

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
            '/api/v1/tiktok/web/fetch_search_keyword_suggest', 'GET',
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

    def fetch_search_live_api_v1_tiktok_web_fetch_search_live_get(self, keyword, **kwargs):  # noqa: E501
        """搜索直播/Search live  # noqa: E501

        # [中文] ### 用途: - 搜索直播 ### 参数: - keyword: 搜索关键词 - count: 每页数量 - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取。 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供) ### 返回: - 直播列表  # [English] ### Purpose: - Search live ### Parameters: - keyword: Search keyword - count: Number per page - offset: Page offset, 0 for the first request, need to provide for the second paging. - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required) ### Return: - Live list  # [示例/Example] keyword = \"TikTok\" count = 20 offset = 0 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_live_api_v1_tiktok_web_fetch_search_live_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object count: 每页数量/Number per page
        :param object offset: 翻页游标/Page cursor
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :param object cookie: 用户cookie(按需提供)/User cookie(if needed)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_live_api_v1_tiktok_web_fetch_search_live_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_live_api_v1_tiktok_web_fetch_search_live_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_live_api_v1_tiktok_web_fetch_search_live_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索直播/Search live  # noqa: E501

        # [中文] ### 用途: - 搜索直播 ### 参数: - keyword: 搜索关键词 - count: 每页数量 - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取。 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供) ### 返回: - 直播列表  # [English] ### Purpose: - Search live ### Parameters: - keyword: Search keyword - count: Number per page - offset: Page offset, 0 for the first request, need to provide for the second paging. - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required) ### Return: - Live list  # [示例/Example] keyword = \"TikTok\" count = 20 offset = 0 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_live_api_v1_tiktok_web_fetch_search_live_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object count: 每页数量/Number per page
        :param object offset: 翻页游标/Page cursor
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :param object cookie: 用户cookie(按需提供)/User cookie(if needed)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'count', 'offset', 'search_id', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_live_api_v1_tiktok_web_fetch_search_live_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_live_api_v1_tiktok_web_fetch_search_live_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_search_live', 'GET',
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

    def fetch_search_photo_api_v1_tiktok_web_fetch_search_photo_get(self, keyword, **kwargs):  # noqa: E501
        """搜索照片/Search photo  # noqa: E501

        # [中文] ### 用途: - 搜索照片 ### 参数: - keyword: 搜索关键词 - count: 每页数量，建议保持默认值20。 - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供) ### 返回: - 视频列表  # [English] ### Purpose: - Search photo ### Parameters: - keyword: Search keyword - count: Number per page, it is recommended to keep the default value 20. - offset: Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - offset: Page cursor - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required) ### Return: - Video list  # [示例/Example] keyword = \"TikTok\" count = 20 offset = 0 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_photo_api_v1_tiktok_web_fetch_search_photo_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object count: 每页数量/Number per page
        :param object offset: 翻页游标/Page offset
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :param object cookie: 用户cookie(按需提供)/User cookie(if needed)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_photo_api_v1_tiktok_web_fetch_search_photo_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_photo_api_v1_tiktok_web_fetch_search_photo_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_photo_api_v1_tiktok_web_fetch_search_photo_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索照片/Search photo  # noqa: E501

        # [中文] ### 用途: - 搜索照片 ### 参数: - keyword: 搜索关键词 - count: 每页数量，建议保持默认值20。 - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供) ### 返回: - 视频列表  # [English] ### Purpose: - Search photo ### Parameters: - keyword: Search keyword - count: Number per page, it is recommended to keep the default value 20. - offset: Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - offset: Page cursor - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required) ### Return: - Video list  # [示例/Example] keyword = \"TikTok\" count = 20 offset = 0 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_photo_api_v1_tiktok_web_fetch_search_photo_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object count: 每页数量/Number per page
        :param object offset: 翻页游标/Page offset
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :param object cookie: 用户cookie(按需提供)/User cookie(if needed)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'count', 'offset', 'search_id', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_photo_api_v1_tiktok_web_fetch_search_photo_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_photo_api_v1_tiktok_web_fetch_search_photo_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_search_photo', 'GET',
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

    def fetch_search_user_api_v1_tiktok_web_fetch_search_user_get(self, keyword, **kwargs):  # noqa: E501
        """搜索用户/Search user  # noqa: E501

        # [中文] ### 用途: - 搜索用户 ### 参数: - keyword: 搜索关键词 - cursor: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供) ### 返回: - 用户列表 ### 备注: - 如果接口响应的 `data` 字段中的 `status_code` 不为0，说明搜索请求未成功，此时请检查响应里的异常，有可能你在搜索 TikTok 不允许的关键词，或者搜索了敏感内容，请更换关键词重试。  # [English] ### Purpose: - Search user ### Parameters: - keyword: Search keyword - cursor: Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required) ### Return: - User list ### Note: - If the `status_code` in the `data` field of the interface response is not 0, it means that the search request was not successful. Please check the exceptions in the response. You may be searching for keywords that TikTok does not allow, or searching for sensitive content. Please change the keywords and try again.  # [示例/Example] keyword = \"TikTok\" cursor = 0 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_user_api_v1_tiktok_web_fetch_search_user_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object cursor: 翻页游标/Page cursor
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :param object cookie: 用户cookie(按需提供)/User cookie(if needed)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_user_api_v1_tiktok_web_fetch_search_user_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_user_api_v1_tiktok_web_fetch_search_user_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_user_api_v1_tiktok_web_fetch_search_user_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索用户/Search user  # noqa: E501

        # [中文] ### 用途: - 搜索用户 ### 参数: - keyword: 搜索关键词 - cursor: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供) ### 返回: - 用户列表 ### 备注: - 如果接口响应的 `data` 字段中的 `status_code` 不为0，说明搜索请求未成功，此时请检查响应里的异常，有可能你在搜索 TikTok 不允许的关键词，或者搜索了敏感内容，请更换关键词重试。  # [English] ### Purpose: - Search user ### Parameters: - keyword: Search keyword - cursor: Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor. - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required) ### Return: - User list ### Note: - If the `status_code` in the `data` field of the interface response is not 0, it means that the search request was not successful. Please check the exceptions in the response. You may be searching for keywords that TikTok does not allow, or searching for sensitive content. Please change the keywords and try again.  # [示例/Example] keyword = \"TikTok\" cursor = 0 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_user_api_v1_tiktok_web_fetch_search_user_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object cursor: 翻页游标/Page cursor
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :param object cookie: 用户cookie(按需提供)/User cookie(if needed)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'cursor', 'search_id', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_user_api_v1_tiktok_web_fetch_search_user_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_user_api_v1_tiktok_web_fetch_search_user_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_search_user', 'GET',
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

    def fetch_search_video_api_v1_tiktok_web_fetch_search_video_get(self, keyword, **kwargs):  # noqa: E501
        """搜索视频/Search video  # noqa: E501

        # [中文] ### 用途: - 搜索视频 ### 参数: - keyword: 搜索关键词 - count: 每页数量，建议保持默认值20。 - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取。 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供) ### 返回: - 视频列表  # [English] ### Purpose: - Search video ### Parameters: - keyword: Search keyword - count: Number per page, it is recommended to keep the default value 20. - offset: Page offset, 0 for the first request, need to provide for the second paging. - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required) ### Return: - Video list  # [示例/Example] keyword = \"TikTok\" count = 20 offset = 0 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_video_api_v1_tiktok_web_fetch_search_video_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object count: 每页数量/Number per page
        :param object offset: 翻页游标/Page cursor
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :param object cookie: 用户cookie(按需提供)/User cookie(if needed)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_video_api_v1_tiktok_web_fetch_search_video_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_video_api_v1_tiktok_web_fetch_search_video_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_video_api_v1_tiktok_web_fetch_search_video_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索视频/Search video  # noqa: E501

        # [中文] ### 用途: - 搜索视频 ### 参数: - keyword: 搜索关键词 - count: 每页数量，建议保持默认值20。 - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取。 - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。     - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供) ### 返回: - 视频列表  # [English] ### Purpose: - Search video ### Parameters: - keyword: Search keyword - count: Number per page, it is recommended to keep the default value 20. - offset: Page offset, 0 for the first request, need to provide for the second paging. - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.     - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"     - JSON Path-1 : $.data.extra.logid     - JSON Path-2 : $.data.log_pb.impr_id - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required) ### Return: - Video list  # [示例/Example] keyword = \"TikTok\" count = 20 offset = 0 search_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_video_api_v1_tiktok_web_fetch_search_video_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object count: 每页数量/Number per page
        :param object offset: 翻页游标/Page cursor
        :param object search_id: 搜索id，翻页时需要提供/Search id, need to provide when paging
        :param object cookie: 用户cookie(按需提供)/User cookie(if needed)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'count', 'offset', 'search_id', 'cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_video_api_v1_tiktok_web_fetch_search_video_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_video_api_v1_tiktok_web_fetch_search_video_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_search_video', 'GET',
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

    def fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get(self, device_id, verify_fp, region, proxy, **kwargs):  # noqa: E501
        """认证SSO登录/Authenticate SSO login  # noqa: E501

        # [中文] ### 用途: - 认证SSO登录 ### 参数: - device_id: 设备ID - verifyFp: verifyFp - region: 地区 - proxy: 代理 ### 返回: - SSO登录认证信息 ### 说明: - 认证需要保持参数一致，否则会认证失败。  # [English] ### Purpose: - Authenticate SSO login ### Parameters: - token: Login token - device_id: Device ID - verifyFp: verifyFp - region: Region - proxy: Proxy ### Return: - SSO login authentication information ### Description: - Please use the value obtained by the /fetch_sso_login_status interface for input. - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.  # [示例/Example] device_id = \"7481276116461831688\" verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\" region = \"US\" proxy = \"None\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get(device_id, verify_fp, region, proxy, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object device_id: 设备ID/Device ID (required)
        :param object verify_fp: verifyFp (required)
        :param object region: 地区/Region (required)
        :param object proxy: 代理/Proxy (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get_with_http_info(device_id, verify_fp, region, proxy, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get_with_http_info(device_id, verify_fp, region, proxy, **kwargs)  # noqa: E501
            return data

    def fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get_with_http_info(self, device_id, verify_fp, region, proxy, **kwargs):  # noqa: E501
        """认证SSO登录/Authenticate SSO login  # noqa: E501

        # [中文] ### 用途: - 认证SSO登录 ### 参数: - device_id: 设备ID - verifyFp: verifyFp - region: 地区 - proxy: 代理 ### 返回: - SSO登录认证信息 ### 说明: - 认证需要保持参数一致，否则会认证失败。  # [English] ### Purpose: - Authenticate SSO login ### Parameters: - token: Login token - device_id: Device ID - verifyFp: verifyFp - region: Region - proxy: Proxy ### Return: - SSO login authentication information ### Description: - Please use the value obtained by the /fetch_sso_login_status interface for input. - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.  # [示例/Example] device_id = \"7481276116461831688\" verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\" region = \"US\" proxy = \"None\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get_with_http_info(device_id, verify_fp, region, proxy, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object device_id: 设备ID/Device ID (required)
        :param object verify_fp: verifyFp (required)
        :param object region: 地区/Region (required)
        :param object proxy: 代理/Proxy (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'verify_fp', 'region', 'proxy']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if self.api_client.client_side_validation and ('device_id' not in params or
                                                       params['device_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_id` when calling `fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get`")  # noqa: E501
        # verify the required parameter 'verify_fp' is set
        if self.api_client.client_side_validation and ('verify_fp' not in params or
                                                       params['verify_fp'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `verify_fp` when calling `fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get`")  # noqa: E501
        # verify the required parameter 'region' is set
        if self.api_client.client_side_validation and ('region' not in params or
                                                       params['region'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `region` when calling `fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get`")  # noqa: E501
        # verify the required parameter 'proxy' is set
        if self.api_client.client_side_validation and ('proxy' not in params or
                                                       params['proxy'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `proxy` when calling `fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'device_id' in params:
            query_params.append(('device_id', params['device_id']))  # noqa: E501
        if 'verify_fp' in params:
            query_params.append(('verifyFp', params['verify_fp']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'proxy' in params:
            query_params.append(('proxy', params['proxy']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_sso_login_auth', 'GET',
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

    def fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get(self, device_id, region, proxy, **kwargs):  # noqa: E501
        """获取SSO登录二维码/Get SSO login QR code  # noqa: E501

        # [中文] ### 用途: - 获取SSO登录二维码 ### 参数: - device_id: 设备ID - region: 地区 - proxy: 代理 ### 返回: - SSO登录二维码 ### 说明: - 该接口返回的二维码需要使用手机扫描登录，登录成功后会返回登录信息。 - 不传入设备ID将由后端自动生成设备ID。 - 如果需要使用代理，请传入代理地址，否则传入None。 - 单次二维码有效期为一分钟。  # [English] ### Purpose: - Get SSO login QR code ### Parameters: - device_id: Device ID - region: Region - proxy: Proxy ### Return: - SSO login QR code ### Description: - The QR code returned by this interface needs to be scanned by the mobile phone for login, and the login information will be returned after successful login. - If the device ID is not passed in, the device ID will be automatically generated by the backend. - If you need to use a proxy, please pass in the proxy address, otherwise pass in None - The validity period of a single QR code is one minute.  # [示例/Example] device_id = \"7481276116461831688\" region = \"US\" proxy = \"None\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get(device_id, region, proxy, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object device_id: 设备ID/Device ID (required)
        :param object region: 地区/Region (required)
        :param object proxy: 代理/Proxy (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get_with_http_info(device_id, region, proxy, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get_with_http_info(device_id, region, proxy, **kwargs)  # noqa: E501
            return data

    def fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get_with_http_info(self, device_id, region, proxy, **kwargs):  # noqa: E501
        """获取SSO登录二维码/Get SSO login QR code  # noqa: E501

        # [中文] ### 用途: - 获取SSO登录二维码 ### 参数: - device_id: 设备ID - region: 地区 - proxy: 代理 ### 返回: - SSO登录二维码 ### 说明: - 该接口返回的二维码需要使用手机扫描登录，登录成功后会返回登录信息。 - 不传入设备ID将由后端自动生成设备ID。 - 如果需要使用代理，请传入代理地址，否则传入None。 - 单次二维码有效期为一分钟。  # [English] ### Purpose: - Get SSO login QR code ### Parameters: - device_id: Device ID - region: Region - proxy: Proxy ### Return: - SSO login QR code ### Description: - The QR code returned by this interface needs to be scanned by the mobile phone for login, and the login information will be returned after successful login. - If the device ID is not passed in, the device ID will be automatically generated by the backend. - If you need to use a proxy, please pass in the proxy address, otherwise pass in None - The validity period of a single QR code is one minute.  # [示例/Example] device_id = \"7481276116461831688\" region = \"US\" proxy = \"None\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get_with_http_info(device_id, region, proxy, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object device_id: 设备ID/Device ID (required)
        :param object region: 地区/Region (required)
        :param object proxy: 代理/Proxy (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'region', 'proxy']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if self.api_client.client_side_validation and ('device_id' not in params or
                                                       params['device_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_id` when calling `fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get`")  # noqa: E501
        # verify the required parameter 'region' is set
        if self.api_client.client_side_validation and ('region' not in params or
                                                       params['region'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `region` when calling `fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get`")  # noqa: E501
        # verify the required parameter 'proxy' is set
        if self.api_client.client_side_validation and ('proxy' not in params or
                                                       params['proxy'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `proxy` when calling `fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'device_id' in params:
            query_params.append(('device_id', params['device_id']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'proxy' in params:
            query_params.append(('proxy', params['proxy']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_sso_login_qrcode', 'GET',
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

    def fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get(self, token, device_id, verify_fp, region, proxy, **kwargs):  # noqa: E501
        """获取SSO登录状态/Get SSO login status  # noqa: E501

        # [中文] ### 用途: - 获取SSO登录状态 ### 参数: - token: 登录令牌 - device_id: 设备ID - verifyFp: verifyFp - region: 地区 - proxy: 代理 ### 返回: - SSO登录状态 ### 说明: - 该接口返回的登录状态需要轮询，建议2秒轮询一次。 - 请使用/fetch_sso_login_qrcode接口获取的值进行传入。 - 如果需要使用代理，请传入代理地址，否则传入None。 - 扫码状态：     - new: 未扫码     - expired: 二维码过期（需要重新请求/fetch_sso_login_qrcode）     - scanned: 已扫码     - confirmed: 已确认登录（需要请求/fetch_sso_login_auth认证）  # [English] ### Purpose: - Get SSO login status ### Parameters: - token: Login token - device_id: Device ID - verifyFp: verifyFp - region: Region - proxy: Proxy ### Return: - SSO login status ### Description: - The login status returned by this interface needs to be polled, and it is recommended to poll once every 2 seconds. - Please use the value obtained by the /fetch_sso_login_qrcode interface for input. - If you need to use a proxy, please pass in the proxy address, otherwise pass in None. - Scan status:     - new: Not scanned     - expired: QR code expired (need to request /fetch_sso_login_qrcode again)     - scanned: Scanned     - confirmed: Confirmed login (need to request /fetch_sso_login_auth for authentication  # [示例/Example] token = \"jiHRabSoJdwNrsvJvlRKj4hecTstR2xsn2NmtmKMN8o=_useast5\" device_id = \"7481276116461831688\" verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\" region = \"US\" proxy = \"None\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get(token, device_id, verify_fp, region, proxy, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object token: 登录令牌/Login token (required)
        :param object device_id: 设备ID/Device ID (required)
        :param object verify_fp: verifyFp (required)
        :param object region: 地区/Region (required)
        :param object proxy: 代理/Proxy (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get_with_http_info(token, device_id, verify_fp, region, proxy, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get_with_http_info(token, device_id, verify_fp, region, proxy, **kwargs)  # noqa: E501
            return data

    def fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get_with_http_info(self, token, device_id, verify_fp, region, proxy, **kwargs):  # noqa: E501
        """获取SSO登录状态/Get SSO login status  # noqa: E501

        # [中文] ### 用途: - 获取SSO登录状态 ### 参数: - token: 登录令牌 - device_id: 设备ID - verifyFp: verifyFp - region: 地区 - proxy: 代理 ### 返回: - SSO登录状态 ### 说明: - 该接口返回的登录状态需要轮询，建议2秒轮询一次。 - 请使用/fetch_sso_login_qrcode接口获取的值进行传入。 - 如果需要使用代理，请传入代理地址，否则传入None。 - 扫码状态：     - new: 未扫码     - expired: 二维码过期（需要重新请求/fetch_sso_login_qrcode）     - scanned: 已扫码     - confirmed: 已确认登录（需要请求/fetch_sso_login_auth认证）  # [English] ### Purpose: - Get SSO login status ### Parameters: - token: Login token - device_id: Device ID - verifyFp: verifyFp - region: Region - proxy: Proxy ### Return: - SSO login status ### Description: - The login status returned by this interface needs to be polled, and it is recommended to poll once every 2 seconds. - Please use the value obtained by the /fetch_sso_login_qrcode interface for input. - If you need to use a proxy, please pass in the proxy address, otherwise pass in None. - Scan status:     - new: Not scanned     - expired: QR code expired (need to request /fetch_sso_login_qrcode again)     - scanned: Scanned     - confirmed: Confirmed login (need to request /fetch_sso_login_auth for authentication  # [示例/Example] token = \"jiHRabSoJdwNrsvJvlRKj4hecTstR2xsn2NmtmKMN8o=_useast5\" device_id = \"7481276116461831688\" verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\" region = \"US\" proxy = \"None\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get_with_http_info(token, device_id, verify_fp, region, proxy, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object token: 登录令牌/Login token (required)
        :param object device_id: 设备ID/Device ID (required)
        :param object verify_fp: verifyFp (required)
        :param object region: 地区/Region (required)
        :param object proxy: 代理/Proxy (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'device_id', 'verify_fp', 'region', 'proxy']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in params or
                                                       params['token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `token` when calling `fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if self.api_client.client_side_validation and ('device_id' not in params or
                                                       params['device_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `device_id` when calling `fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get`")  # noqa: E501
        # verify the required parameter 'verify_fp' is set
        if self.api_client.client_side_validation and ('verify_fp' not in params or
                                                       params['verify_fp'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `verify_fp` when calling `fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get`")  # noqa: E501
        # verify the required parameter 'region' is set
        if self.api_client.client_side_validation and ('region' not in params or
                                                       params['region'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `region` when calling `fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get`")  # noqa: E501
        # verify the required parameter 'proxy' is set
        if self.api_client.client_side_validation and ('proxy' not in params or
                                                       params['proxy'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `proxy` when calling `fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501
        if 'device_id' in params:
            query_params.append(('device_id', params['device_id']))  # noqa: E501
        if 'verify_fp' in params:
            query_params.append(('verifyFp', params['verify_fp']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'proxy' in params:
            query_params.append(('proxy', params['proxy']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_sso_login_status', 'GET',
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

    def fetch_tag_detail_api_v1_tiktok_web_fetch_tag_detail_get(self, tag_name, **kwargs):  # noqa: E501
        """Tag详情/Tag Detail  # noqa: E501

        # [中文] ### 用途: - Tag详情 ### 参数: - tag_name: Tag名称 ### 返回: - Tag详情  # [English] ### Purpose: - Tag Detail ### Parameters: - tag_name: Tag name ### Return: - Tag Detail  # [示例/Example] tag_name = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_tag_detail_api_v1_tiktok_web_fetch_tag_detail_get(tag_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tag_name: Tag名称/Tag name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_tag_detail_api_v1_tiktok_web_fetch_tag_detail_get_with_http_info(tag_name, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_tag_detail_api_v1_tiktok_web_fetch_tag_detail_get_with_http_info(tag_name, **kwargs)  # noqa: E501
            return data

    def fetch_tag_detail_api_v1_tiktok_web_fetch_tag_detail_get_with_http_info(self, tag_name, **kwargs):  # noqa: E501
        """Tag详情/Tag Detail  # noqa: E501

        # [中文] ### 用途: - Tag详情 ### 参数: - tag_name: Tag名称 ### 返回: - Tag详情  # [English] ### Purpose: - Tag Detail ### Parameters: - tag_name: Tag name ### Return: - Tag Detail  # [示例/Example] tag_name = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_tag_detail_api_v1_tiktok_web_fetch_tag_detail_get_with_http_info(tag_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tag_name: Tag名称/Tag name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_tag_detail_api_v1_tiktok_web_fetch_tag_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_name' is set
        if self.api_client.client_side_validation and ('tag_name' not in params or
                                                       params['tag_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tag_name` when calling `fetch_tag_detail_api_v1_tiktok_web_fetch_tag_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag_name' in params:
            query_params.append(('tag_name', params['tag_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_tag_detail', 'GET',
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

    def fetch_tag_post_api_v1_tiktok_web_fetch_tag_post_get(self, challenge_id, **kwargs):  # noqa: E501
        """Tag作品/Tag Post  # noqa: E501

        # [中文] ### 用途: - Tag作品 ### 参数: - challengeID: Tag ID - count: 每页数量 - cursor: 翻页游标 ### 返回: - Tag作品 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Tag Post ### Parameters: - challengeID: Tag ID - count: Number per page - cursor: Page cursor ### Return: - Tag Post ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] challengeID = \"7551\" count = 30 cursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_tag_post_api_v1_tiktok_web_fetch_tag_post_get(challenge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object challenge_id: Tag ID (required)
        :param object count: 每页数量/Number per page
        :param object cursor: 翻页游标/Page cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_tag_post_api_v1_tiktok_web_fetch_tag_post_get_with_http_info(challenge_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_tag_post_api_v1_tiktok_web_fetch_tag_post_get_with_http_info(challenge_id, **kwargs)  # noqa: E501
            return data

    def fetch_tag_post_api_v1_tiktok_web_fetch_tag_post_get_with_http_info(self, challenge_id, **kwargs):  # noqa: E501
        """Tag作品/Tag Post  # noqa: E501

        # [中文] ### 用途: - Tag作品 ### 参数: - challengeID: Tag ID - count: 每页数量 - cursor: 翻页游标 ### 返回: - Tag作品 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Tag Post ### Parameters: - challengeID: Tag ID - count: Number per page - cursor: Page cursor ### Return: - Tag Post ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] challengeID = \"7551\" count = 30 cursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_tag_post_api_v1_tiktok_web_fetch_tag_post_get_with_http_info(challenge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object challenge_id: Tag ID (required)
        :param object count: 每页数量/Number per page
        :param object cursor: 翻页游标/Page cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['challenge_id', 'count', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_tag_post_api_v1_tiktok_web_fetch_tag_post_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'challenge_id' is set
        if self.api_client.client_side_validation and ('challenge_id' not in params or
                                                       params['challenge_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `challenge_id` when calling `fetch_tag_post_api_v1_tiktok_web_fetch_tag_post_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'challenge_id' in params:
            query_params.append(('challengeID', params['challenge_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_tag_post', 'GET',
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

    def fetch_tiktok_live_data_api_v1_tiktok_web_fetch_tiktok_live_data_get(self, live_room_url, **kwargs):  # noqa: E501
        """通过直播链接获取直播间信息/Get live room information via live link  # noqa: E501

        # [中文] ### 用途: - 通过直播链接获取直播间信息 - 此接口可获取离线直播间信息 ### 参数: - live_room_url: 直播间链接 ### 返回: - 直播间信息  # [English] ### Purpose: - Get live room information via live link - This interface can get offline live room information ### Parameters: - live_room_url: Live room link ### Return: - Live room information  # [示例/Example] live_room_url = \"https://www.tiktok.com/@.caseoh_daily/live\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_tiktok_live_data_api_v1_tiktok_web_fetch_tiktok_live_data_get(live_room_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object live_room_url: 直播间链接/Live room link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_tiktok_live_data_api_v1_tiktok_web_fetch_tiktok_live_data_get_with_http_info(live_room_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_tiktok_live_data_api_v1_tiktok_web_fetch_tiktok_live_data_get_with_http_info(live_room_url, **kwargs)  # noqa: E501
            return data

    def fetch_tiktok_live_data_api_v1_tiktok_web_fetch_tiktok_live_data_get_with_http_info(self, live_room_url, **kwargs):  # noqa: E501
        """通过直播链接获取直播间信息/Get live room information via live link  # noqa: E501

        # [中文] ### 用途: - 通过直播链接获取直播间信息 - 此接口可获取离线直播间信息 ### 参数: - live_room_url: 直播间链接 ### 返回: - 直播间信息  # [English] ### Purpose: - Get live room information via live link - This interface can get offline live room information ### Parameters: - live_room_url: Live room link ### Return: - Live room information  # [示例/Example] live_room_url = \"https://www.tiktok.com/@.caseoh_daily/live\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_tiktok_live_data_api_v1_tiktok_web_fetch_tiktok_live_data_get_with_http_info(live_room_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object live_room_url: 直播间链接/Live room link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['live_room_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_tiktok_live_data_api_v1_tiktok_web_fetch_tiktok_live_data_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'live_room_url' is set
        if self.api_client.client_side_validation and ('live_room_url' not in params or
                                                       params['live_room_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `live_room_url` when calling `fetch_tiktok_live_data_api_v1_tiktok_web_fetch_tiktok_live_data_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'live_room_url' in params:
            query_params.append(('live_room_url', params['live_room_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_tiktok_live_data', 'GET',
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

    def fetch_tiktok_web_guest_cookie_api_v1_tiktok_web_fetch_tiktok_web_guest_cookie_get(self, user_agent, **kwargs):  # noqa: E501
        """获取游客 Cookie/Get the guest Cookie  # noqa: E501

        # [中文] ### 用途: - 获取 TikTok Web的游客Cookie - 可以用于爬取 TikTok Web 的数据，如用户作品、合辑作品等。 - 可以固定身份避免部分接口重复数据。 - 请注意：游客Cookie无法爬取所有数据，有一定的限制。 - 可以配合开源项目使用此接口实现TikTok Web的数据爬取。 ### 参数: - user_agent: 用户浏览器代理 ### 返回: - 游客Cookie  # [English] ### Purpose: - Get the guest Cookie of TikTok Web - Can be used to crawl data of TikTok Web, such as user videos, mix videos, etc. - Can fix identity to avoid duplicate data for some interfaces. - Please note: Guest Cookie cannot crawl all data, there are certain restrictions. - Can be used with open source projects to implement data crawling of TikTok Web using this interface. ### Parameters: - user_agent: User browser agent ### Return: - Guest Cookie  # [示例/Example] user_agent = \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\"  # [响应/Response]: ```json {     \"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\",     \"Cookie\": \"ttwid=1%7Ck5lqyYxAq2wSmaEculMCk31ur4lkvy3DVwn6Phf45GQ%7C1759321284%7C6bac9a25e1f6b512aecad91a37167ad753b47f2306ffe0d70695001d6b4dd793;tt_csrf_token=tueWm0Fw-jL4Ie3Iu2z755XYPzAphhgJmHDA;tt_chain_token=drrbnMAs2A13tME+L6XbsA==\",     \"Referer\": \"https://www.tiktok.com/explore\" } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_tiktok_web_guest_cookie_api_v1_tiktok_web_fetch_tiktok_web_guest_cookie_get(user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_agent: 用户浏览器代理/User browser agent (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_tiktok_web_guest_cookie_api_v1_tiktok_web_fetch_tiktok_web_guest_cookie_get_with_http_info(user_agent, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_tiktok_web_guest_cookie_api_v1_tiktok_web_fetch_tiktok_web_guest_cookie_get_with_http_info(user_agent, **kwargs)  # noqa: E501
            return data

    def fetch_tiktok_web_guest_cookie_api_v1_tiktok_web_fetch_tiktok_web_guest_cookie_get_with_http_info(self, user_agent, **kwargs):  # noqa: E501
        """获取游客 Cookie/Get the guest Cookie  # noqa: E501

        # [中文] ### 用途: - 获取 TikTok Web的游客Cookie - 可以用于爬取 TikTok Web 的数据，如用户作品、合辑作品等。 - 可以固定身份避免部分接口重复数据。 - 请注意：游客Cookie无法爬取所有数据，有一定的限制。 - 可以配合开源项目使用此接口实现TikTok Web的数据爬取。 ### 参数: - user_agent: 用户浏览器代理 ### 返回: - 游客Cookie  # [English] ### Purpose: - Get the guest Cookie of TikTok Web - Can be used to crawl data of TikTok Web, such as user videos, mix videos, etc. - Can fix identity to avoid duplicate data for some interfaces. - Please note: Guest Cookie cannot crawl all data, there are certain restrictions. - Can be used with open source projects to implement data crawling of TikTok Web using this interface. ### Parameters: - user_agent: User browser agent ### Return: - Guest Cookie  # [示例/Example] user_agent = \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\"  # [响应/Response]: ```json {     \"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\",     \"Cookie\": \"ttwid=1%7Ck5lqyYxAq2wSmaEculMCk31ur4lkvy3DVwn6Phf45GQ%7C1759321284%7C6bac9a25e1f6b512aecad91a37167ad753b47f2306ffe0d70695001d6b4dd793;tt_csrf_token=tueWm0Fw-jL4Ie3Iu2z755XYPzAphhgJmHDA;tt_chain_token=drrbnMAs2A13tME+L6XbsA==\",     \"Referer\": \"https://www.tiktok.com/explore\" } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_tiktok_web_guest_cookie_api_v1_tiktok_web_fetch_tiktok_web_guest_cookie_get_with_http_info(user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_agent: 用户浏览器代理/User browser agent (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_tiktok_web_guest_cookie_api_v1_tiktok_web_fetch_tiktok_web_guest_cookie_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_agent' is set
        if self.api_client.client_side_validation and ('user_agent' not in params or
                                                       params['user_agent'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_agent` when calling `fetch_tiktok_web_guest_cookie_api_v1_tiktok_web_fetch_tiktok_web_guest_cookie_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_tiktok_web_guest_cookie', 'GET',
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

    def fetch_trending_post_api_v1_tiktok_web_fetch_trending_post_get(self, **kwargs):  # noqa: E501
        """获取每日热门内容作品数据/Get daily trending video data  # noqa: E501

        # [中文] ### 用途: - 获取每日热门内容作品数据 ### 返回: - 作品数据  # [English] ### Purpose: - Get daily trending video data ### Return: - Video data  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_trending_post_api_v1_tiktok_web_fetch_trending_post_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_trending_post_api_v1_tiktok_web_fetch_trending_post_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_trending_post_api_v1_tiktok_web_fetch_trending_post_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_trending_post_api_v1_tiktok_web_fetch_trending_post_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取每日热门内容作品数据/Get daily trending video data  # noqa: E501

        # [中文] ### 用途: - 获取每日热门内容作品数据 ### 返回: - 作品数据  # [English] ### Purpose: - Get daily trending video data ### Return: - Video data  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_trending_post_api_v1_tiktok_web_fetch_trending_post_get_with_http_info(async_req=True)
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
                    " to method fetch_trending_post_api_v1_tiktok_web_fetch_trending_post_get" % key
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
            '/api/v1/tiktok/web/fetch_trending_post', 'GET',
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

    def fetch_trending_searchwords_api_v1_tiktok_web_fetch_trending_searchwords_get(self, **kwargs):  # noqa: E501
        """获取每日趋势搜索关键词/Get daily trending search words  # noqa: E501

        # [中文] ### 用途: - 获取每日趋势搜索关键词 ### 返回: - 趋势搜索关键词  # [English] ### Purpose: - Get daily trending search words ### Return: - Trending search words  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_trending_searchwords_api_v1_tiktok_web_fetch_trending_searchwords_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_trending_searchwords_api_v1_tiktok_web_fetch_trending_searchwords_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_trending_searchwords_api_v1_tiktok_web_fetch_trending_searchwords_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_trending_searchwords_api_v1_tiktok_web_fetch_trending_searchwords_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取每日趋势搜索关键词/Get daily trending search words  # noqa: E501

        # [中文] ### 用途: - 获取每日趋势搜索关键词 ### 返回: - 趋势搜索关键词  # [English] ### Purpose: - Get daily trending search words ### Return: - Trending search words  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_trending_searchwords_api_v1_tiktok_web_fetch_trending_searchwords_get_with_http_info(async_req=True)
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
                    " to method fetch_trending_searchwords_api_v1_tiktok_web_fetch_trending_searchwords_get" % key
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
            '/api/v1/tiktok/web/fetch_trending_searchwords', 'GET',
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

    def fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get(self, cookie, sec_uid, **kwargs):  # noqa: E501
        """获取用户的收藏列表/Get user favorites  # noqa: E501

        # [中文] ### 用途: - 获取用户的收藏列表 - 注意: 该接口目前只能获取自己的收藏列表，需要提供自己账号的cookie。 ### 参数: - cookie: 用户cookie - secUid: 用户secUid - cursor: 翻页游标 - count: 每页数量 - coverFormat: 封面格式 ### 返回: - 用户的收藏列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user favorites - Note: This interface can currently only get your own favorites list, you need to provide your account cookie. ### Parameters: - cookie: User cookie - secUid: User secUid - cursor: Page cursor - count: Number per page - coverFormat: Cover format ### Return: - User favorites ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] cookie = \"Your_Cookie\" secUid = \"Your_SecUid\" cursor = 0 count = 30 coverFormat = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get(cookie, sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cookie: 用户cookie/User cookie (required)
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object cover_format: 封面格式/Cover format
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get_with_http_info(cookie, sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get_with_http_info(cookie, sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get_with_http_info(self, cookie, sec_uid, **kwargs):  # noqa: E501
        """获取用户的收藏列表/Get user favorites  # noqa: E501

        # [中文] ### 用途: - 获取用户的收藏列表 - 注意: 该接口目前只能获取自己的收藏列表，需要提供自己账号的cookie。 ### 参数: - cookie: 用户cookie - secUid: 用户secUid - cursor: 翻页游标 - count: 每页数量 - coverFormat: 封面格式 ### 返回: - 用户的收藏列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user favorites - Note: This interface can currently only get your own favorites list, you need to provide your account cookie. ### Parameters: - cookie: User cookie - secUid: User secUid - cursor: Page cursor - count: Number per page - coverFormat: Cover format ### Return: - User favorites ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] cookie = \"Your_Cookie\" secUid = \"Your_SecUid\" cursor = 0 count = 30 coverFormat = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get_with_http_info(cookie, sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cookie: 用户cookie/User cookie (required)
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object cover_format: 封面格式/Cover format
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cookie', 'sec_uid', 'cursor', 'count', 'cover_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cookie' is set
        if self.api_client.client_side_validation and ('cookie' not in params or
                                                       params['cookie'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cookie` when calling `fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get`")  # noqa: E501
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501
        if 'sec_uid' in params:
            query_params.append(('secUid', params['sec_uid']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'cover_format' in params:
            query_params.append(('coverFormat', params['cover_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_user_collect', 'GET',
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

    def fetch_user_fans_api_v1_tiktok_web_fetch_user_fans_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的粉丝列表/Get user followers  # noqa: E501

        # [中文] ### 用途: - 获取用户的粉丝列表 ### 参数: - secUid: 用户secUid - count: 每页数量 - maxCursor: 最大游标 - minCursor: 最小游标 ### 返回: - 用户的粉丝列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user followers ### Parameters: - secUid: User secUid - count: Number per page - maxCursor: Max cursor - minCursor: Min cursor ### Return: - User followers ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" count = 30 maxCursor = 0 minCursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_fans_api_v1_tiktok_web_fetch_user_fans_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object count: 每页数量/Number per page
        :param object max_cursor: 最大游标/Max cursor
        :param object min_cursor: 最小游标/Min cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_fans_api_v1_tiktok_web_fetch_user_fans_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_fans_api_v1_tiktok_web_fetch_user_fans_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_fans_api_v1_tiktok_web_fetch_user_fans_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的粉丝列表/Get user followers  # noqa: E501

        # [中文] ### 用途: - 获取用户的粉丝列表 ### 参数: - secUid: 用户secUid - count: 每页数量 - maxCursor: 最大游标 - minCursor: 最小游标 ### 返回: - 用户的粉丝列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user followers ### Parameters: - secUid: User secUid - count: Number per page - maxCursor: Max cursor - minCursor: Min cursor ### Return: - User followers ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" count = 30 maxCursor = 0 minCursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_fans_api_v1_tiktok_web_fetch_user_fans_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object count: 每页数量/Number per page
        :param object max_cursor: 最大游标/Max cursor
        :param object min_cursor: 最小游标/Min cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid', 'count', 'max_cursor', 'min_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_fans_api_v1_tiktok_web_fetch_user_fans_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_user_fans_api_v1_tiktok_web_fetch_user_fans_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('secUid', params['sec_uid']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'max_cursor' in params:
            query_params.append(('maxCursor', params['max_cursor']))  # noqa: E501
        if 'min_cursor' in params:
            query_params.append(('minCursor', params['min_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_user_fans', 'GET',
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

    def fetch_user_follow_api_v1_tiktok_web_fetch_user_follow_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的关注列表/Get user followings  # noqa: E501

        # [中文] ### 用途: - 获取用户的关注列表 ### 参数: - secUid: 用户secUid - count: 每页数量 - maxCursor: 最大游标 - minCursor: 最小游标 ### 返回: - 用户的关注列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user followings ### Parameters: - secUid: User secUid - count: Number per page - maxCursor: Max cursor - minCursor: Min cursor ### Return: - User followings ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" count = 30 maxCursor = 0 minCursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follow_api_v1_tiktok_web_fetch_user_follow_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object count: 每页数量/Number per page
        :param object max_cursor: 最大游标/Max cursor
        :param object min_cursor: 最小游标/Min cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_follow_api_v1_tiktok_web_fetch_user_follow_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_follow_api_v1_tiktok_web_fetch_user_follow_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_follow_api_v1_tiktok_web_fetch_user_follow_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的关注列表/Get user followings  # noqa: E501

        # [中文] ### 用途: - 获取用户的关注列表 ### 参数: - secUid: 用户secUid - count: 每页数量 - maxCursor: 最大游标 - minCursor: 最小游标 ### 返回: - 用户的关注列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user followings ### Parameters: - secUid: User secUid - count: Number per page - maxCursor: Max cursor - minCursor: Min cursor ### Return: - User followings ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" count = 30 maxCursor = 0 minCursor = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follow_api_v1_tiktok_web_fetch_user_follow_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object count: 每页数量/Number per page
        :param object max_cursor: 最大游标/Max cursor
        :param object min_cursor: 最小游标/Min cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid', 'count', 'max_cursor', 'min_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_follow_api_v1_tiktok_web_fetch_user_follow_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_user_follow_api_v1_tiktok_web_fetch_user_follow_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('secUid', params['sec_uid']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'max_cursor' in params:
            query_params.append(('maxCursor', params['max_cursor']))  # noqa: E501
        if 'min_cursor' in params:
            query_params.append(('minCursor', params['min_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_user_follow', 'GET',
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

    def fetch_user_like_api_v1_tiktok_web_fetch_user_like_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的点赞列表/Get user likes  # noqa: E501

        # [中文] ### 用途: - 获取用户的点赞列表 - 注意: 该接口需要用户点赞列表为公开状态 ### 参数: - secUid: 用户secUid - cursor: 翻页游标 - count: 每页数量，默认为20，不可变更。 - coverFormat: 封面格式 - post_item_list_request_type: 排序方式     - 0：默认排序     - 1：热门排序     - 2：最旧排序 ### 返回: - 用户的点赞列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user likes - Note: This interface requires that the user's like list be public ### Parameters: - secUid: User secUid - cursor: Page cursor - count: Number per page, default is 20, cannot be changed. - coverFormat: Cover format - post_item_list_request_type: Sort type     - 0: Default sort     - 1: Hot sort     - 2: Oldest sort ### Return: - User likes ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] secUid = \"MS4wLjABAAAAq1iRXNduFZpY301UkVpJ1eQT60_NiWS9QQSeNqmNQEDJp0pOF8cpleNEdiJx5_IU\" cursor = 0 count = 20 coverFormat = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_like_api_v1_tiktok_web_fetch_user_like_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object cover_format: 封面格式/Cover format
        :param object post_item_list_request_type: 排序方式/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_like_api_v1_tiktok_web_fetch_user_like_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_like_api_v1_tiktok_web_fetch_user_like_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_like_api_v1_tiktok_web_fetch_user_like_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的点赞列表/Get user likes  # noqa: E501

        # [中文] ### 用途: - 获取用户的点赞列表 - 注意: 该接口需要用户点赞列表为公开状态 ### 参数: - secUid: 用户secUid - cursor: 翻页游标 - count: 每页数量，默认为20，不可变更。 - coverFormat: 封面格式 - post_item_list_request_type: 排序方式     - 0：默认排序     - 1：热门排序     - 2：最旧排序 ### 返回: - 用户的点赞列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user likes - Note: This interface requires that the user's like list be public ### Parameters: - secUid: User secUid - cursor: Page cursor - count: Number per page, default is 20, cannot be changed. - coverFormat: Cover format - post_item_list_request_type: Sort type     - 0: Default sort     - 1: Hot sort     - 2: Oldest sort ### Return: - User likes ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] secUid = \"MS4wLjABAAAAq1iRXNduFZpY301UkVpJ1eQT60_NiWS9QQSeNqmNQEDJp0pOF8cpleNEdiJx5_IU\" cursor = 0 count = 20 coverFormat = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_like_api_v1_tiktok_web_fetch_user_like_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object cover_format: 封面格式/Cover format
        :param object post_item_list_request_type: 排序方式/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid', 'cursor', 'count', 'cover_format', 'post_item_list_request_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_like_api_v1_tiktok_web_fetch_user_like_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_user_like_api_v1_tiktok_web_fetch_user_like_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('secUid', params['sec_uid']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'cover_format' in params:
            query_params.append(('coverFormat', params['cover_format']))  # noqa: E501
        if 'post_item_list_request_type' in params:
            query_params.append(('post_item_list_request_type', params['post_item_list_request_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_user_like', 'GET',
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

    def fetch_user_live_detail_api_v1_tiktok_web_fetch_user_live_detail_get(self, unique_id, **kwargs):  # noqa: E501
        """获取用户的直播详情/Get user live details  # noqa: E501

        # [中文] ### 用途: - 获取用户的直播详情 ### 参数: - uniqueId: 用户uniqueId ### 返回: - 用户的直播详情 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user live details ### Parameters: - uniqueId: User uniqueId ### Return: - User live details ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] uniqueId = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_detail_api_v1_tiktok_web_fetch_user_live_detail_get(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object unique_id: 用户uniqueId/User uniqueId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_live_detail_api_v1_tiktok_web_fetch_user_live_detail_get_with_http_info(unique_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_live_detail_api_v1_tiktok_web_fetch_user_live_detail_get_with_http_info(unique_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_live_detail_api_v1_tiktok_web_fetch_user_live_detail_get_with_http_info(self, unique_id, **kwargs):  # noqa: E501
        """获取用户的直播详情/Get user live details  # noqa: E501

        # [中文] ### 用途: - 获取用户的直播详情 ### 参数: - uniqueId: 用户uniqueId ### 返回: - 用户的直播详情 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user live details ### Parameters: - uniqueId: User uniqueId ### Return: - User live details ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] uniqueId = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_live_detail_api_v1_tiktok_web_fetch_user_live_detail_get_with_http_info(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object unique_id: 用户uniqueId/User uniqueId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['unique_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_live_detail_api_v1_tiktok_web_fetch_user_live_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'unique_id' is set
        if self.api_client.client_side_validation and ('unique_id' not in params or
                                                       params['unique_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `unique_id` when calling `fetch_user_live_detail_api_v1_tiktok_web_fetch_user_live_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'unique_id' in params:
            query_params.append(('uniqueId', params['unique_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_user_live_detail', 'GET',
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

    def fetch_user_mix_api_v1_tiktok_web_fetch_user_mix_get(self, mix_id, **kwargs):  # noqa: E501
        """获取用户的合辑列表/Get user mix list  # noqa: E501

        # [中文] ### 用途: - 获取用户的合辑列表 ### 参数: - mixId: 合辑id - cursor: 翻页游标 - count: 每页数量 ### 返回: - 用户的合辑列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user mix list ### Parameters: - mixId: Mix id - cursor: Page cursor - count: Number per page ### Return: - User mix list ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Eample] mixId = \"7101538765474106158\" cursor = 0 count = 30  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_mix_api_v1_tiktok_web_fetch_user_mix_get(mix_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mix_id: 合辑id/Mix id (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_mix_api_v1_tiktok_web_fetch_user_mix_get_with_http_info(mix_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_mix_api_v1_tiktok_web_fetch_user_mix_get_with_http_info(mix_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_mix_api_v1_tiktok_web_fetch_user_mix_get_with_http_info(self, mix_id, **kwargs):  # noqa: E501
        """获取用户的合辑列表/Get user mix list  # noqa: E501

        # [中文] ### 用途: - 获取用户的合辑列表 ### 参数: - mixId: 合辑id - cursor: 翻页游标 - count: 每页数量 ### 返回: - 用户的合辑列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user mix list ### Parameters: - mixId: Mix id - cursor: Page cursor - count: Number per page ### Return: - User mix list ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Eample] mixId = \"7101538765474106158\" cursor = 0 count = 30  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_mix_api_v1_tiktok_web_fetch_user_mix_get_with_http_info(mix_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mix_id: 合辑id/Mix id (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mix_id', 'cursor', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_mix_api_v1_tiktok_web_fetch_user_mix_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mix_id' is set
        if self.api_client.client_side_validation and ('mix_id' not in params or
                                                       params['mix_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `mix_id` when calling `fetch_user_mix_api_v1_tiktok_web_fetch_user_mix_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mix_id' in params:
            query_params.append(('mixId', params['mix_id']))  # noqa: E501
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
            '/api/v1/tiktok/web/fetch_user_mix', 'GET',
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

    def fetch_user_play_list_api_v1_tiktok_web_fetch_user_play_list_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的播放列表/Get user play list  # noqa: E501

        # [中文] ### 用途: - 获取用户的播放列表 ### 参数: - secUid: 用户secUid - cursor: 翻页游标 - count: 每页数量 ### 返回: - 用户的播放列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user play list ### Parameters: - secUid: User secUid - cursor: Page cursor - count: Number per page ### Return: - User play list ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Eample] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" cursor = 0 count = 30  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_play_list_api_v1_tiktok_web_fetch_user_play_list_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_play_list_api_v1_tiktok_web_fetch_user_play_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_play_list_api_v1_tiktok_web_fetch_user_play_list_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_play_list_api_v1_tiktok_web_fetch_user_play_list_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的播放列表/Get user play list  # noqa: E501

        # [中文] ### 用途: - 获取用户的播放列表 ### 参数: - secUid: 用户secUid - cursor: 翻页游标 - count: 每页数量 ### 返回: - 用户的播放列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user play list ### Parameters: - secUid: User secUid - cursor: Page cursor - count: Number per page ### Return: - User play list ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Eample] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" cursor = 0 count = 30  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_play_list_api_v1_tiktok_web_fetch_user_play_list_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
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
                    " to method fetch_user_play_list_api_v1_tiktok_web_fetch_user_play_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_user_play_list_api_v1_tiktok_web_fetch_user_play_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('secUid', params['sec_uid']))  # noqa: E501
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
            '/api/v1/tiktok/web/fetch_user_play_list', 'GET',
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

    def fetch_user_post_api_v1_tiktok_web_fetch_user_post_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的作品列表/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取用户的作品列表 ### 参数: - secUid: 用户secUid - cursor: 翻页游标 - count: 每页数量，默认为20，不可变更。 - coverFormat: 封面格式，默认为2，可选值为1或2。 - post_item_list_request_type: 排序方式     - 0：默认排序     - 1：热门排序     - 2：最旧排序 ### 返回: - 用户的作品列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user posts ### Parameters: - secUid: User secUid - cursor: Page cursor - count: Number per page, default is 20, cannot be changed. - coverFormat: Cover format, default is 2, optional values are 1 or 2. - post_item_list_request_type: Sort type     - 0: Default sort     - 1: Hot sort     - 2: Oldest sort ### Return: - User posts ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" cursor = 0 post_item_list_request_type = 0 count = 20 coverFormat = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_api_v1_tiktok_web_fetch_user_post_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object cover_format: 封面格式/Cover format
        :param object post_item_list_request_type: 排序方式/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_post_api_v1_tiktok_web_fetch_user_post_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_api_v1_tiktok_web_fetch_user_post_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_post_api_v1_tiktok_web_fetch_user_post_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的作品列表/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取用户的作品列表 ### 参数: - secUid: 用户secUid - cursor: 翻页游标 - count: 每页数量，默认为20，不可变更。 - coverFormat: 封面格式，默认为2，可选值为1或2。 - post_item_list_request_type: 排序方式     - 0：默认排序     - 1：热门排序     - 2：最旧排序 ### 返回: - 用户的作品列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user posts ### Parameters: - secUid: User secUid - cursor: Page cursor - count: Number per page, default is 20, cannot be changed. - coverFormat: Cover format, default is 2, optional values are 1 or 2. - post_item_list_request_type: Sort type     - 0: Default sort     - 1: Hot sort     - 2: Oldest sort ### Return: - User posts ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" cursor = 0 post_item_list_request_type = 0 count = 20 coverFormat = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_api_v1_tiktok_web_fetch_user_post_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object cover_format: 封面格式/Cover format
        :param object post_item_list_request_type: 排序方式/Sort type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid', 'cursor', 'count', 'cover_format', 'post_item_list_request_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_post_api_v1_tiktok_web_fetch_user_post_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_user_post_api_v1_tiktok_web_fetch_user_post_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('secUid', params['sec_uid']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'cover_format' in params:
            query_params.append(('coverFormat', params['cover_format']))  # noqa: E501
        if 'post_item_list_request_type' in params:
            query_params.append(('post_item_list_request_type', params['post_item_list_request_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_user_post', 'GET',
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

    def fetch_user_profile_api_v1_tiktok_web_fetch_user_profile_get(self, **kwargs):  # noqa: E501
        """获取用户的个人信息/Get user profile  # noqa: E501

        # [中文] ### 用途: - 获取用户的个人信息 ### 参数: - secUid: 用户secUid - uniqueId: 用户uniqueId - secUid和uniqueId至少提供一个, 优先使用uniqueId, 也就是用户主页的链接中的用户名。 ### 返回: - 用户的个人信息  # [English] ### Purpose: - Get user profile ### Parameters: - secUid: User secUid - uniqueId: User uniqueId - At least one of secUid and uniqueId is provided, and uniqueId is preferred, that is, the username in the user's homepage link. ### Return: - User profile  # [示例/Example] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" uniqueId = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_api_v1_tiktok_web_fetch_user_profile_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object unique_id: 用户uniqueId/User uniqueId
        :param object sec_uid: 用户secUid/User secUid
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_profile_api_v1_tiktok_web_fetch_user_profile_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_profile_api_v1_tiktok_web_fetch_user_profile_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_profile_api_v1_tiktok_web_fetch_user_profile_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户的个人信息/Get user profile  # noqa: E501

        # [中文] ### 用途: - 获取用户的个人信息 ### 参数: - secUid: 用户secUid - uniqueId: 用户uniqueId - secUid和uniqueId至少提供一个, 优先使用uniqueId, 也就是用户主页的链接中的用户名。 ### 返回: - 用户的个人信息  # [English] ### Purpose: - Get user profile ### Parameters: - secUid: User secUid - uniqueId: User uniqueId - At least one of secUid and uniqueId is provided, and uniqueId is preferred, that is, the username in the user's homepage link. ### Return: - User profile  # [示例/Example] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" uniqueId = \"tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_api_v1_tiktok_web_fetch_user_profile_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object unique_id: 用户uniqueId/User uniqueId
        :param object sec_uid: 用户secUid/User secUid
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['unique_id', 'sec_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_profile_api_v1_tiktok_web_fetch_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'unique_id' in params:
            query_params.append(('uniqueId', params['unique_id']))  # noqa: E501
        if 'sec_uid' in params:
            query_params.append(('secUid', params['sec_uid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_user_profile', 'GET',
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

    def fetch_user_repost_api_v1_tiktok_web_fetch_user_repost_get(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的转发作品列表/Get user reposts  # noqa: E501

        # [中文] ### 用途: - 获取用户的转发作品列表 ### 参数: - secUid: 用户secUid - cursor: 翻页游标 - count: 每页数量，默认为20，不可变更。 - coverFormat: 封面格式，默认为2，可选值为1或2。 ### 返回: - 用户的转发作品列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user reposts ### Parameters: - secUid: User secUid - cursor: Page cursor - count: Number per page, default is 20, cannot be changed. - coverFormat: Cover format, default is 2, optional values are 1 or 2. ### Return: - User reposts ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" cursor = 0 count = 20 coverFormat = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_repost_api_v1_tiktok_web_fetch_user_repost_get(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object cover_format: 封面格式/Cover format
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_repost_api_v1_tiktok_web_fetch_user_repost_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_repost_api_v1_tiktok_web_fetch_user_repost_get_with_http_info(sec_uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_repost_api_v1_tiktok_web_fetch_user_repost_get_with_http_info(self, sec_uid, **kwargs):  # noqa: E501
        """获取用户的转发作品列表/Get user reposts  # noqa: E501

        # [中文] ### 用途: - 获取用户的转发作品列表 ### 参数: - secUid: 用户secUid - cursor: 翻页游标 - count: 每页数量，默认为20，不可变更。 - coverFormat: 封面格式，默认为2，可选值为1或2。 ### 返回: - 用户的转发作品列表 ### 备注: - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。 - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。 - **如果访问视频CDN链接时返回HTTP 403错误**:   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值   3. 示例请求头: `Cookie: tt_chain_token=xxx` - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。  # [English] ### Purpose: - Get user reposts ### Parameters: - secUid: User secUid - cursor: Page cursor - count: Number per page, default is 20, cannot be changed. - coverFormat: Cover format, default is 2, optional values are 1 or 2. ### Return: - User reposts ### Note: - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned. - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface. - **If you receive HTTP 403 error when accessing video CDN links**:   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API   3. Example request header: `Cookie: tt_chain_token=xxx` - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.  # [示例/Example] secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\" cursor = 0 count = 20 coverFormat = 2  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_repost_api_v1_tiktok_web_fetch_user_repost_get_with_http_info(sec_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sec_uid: 用户secUid/User secUid (required)
        :param object cursor: 翻页游标/Page cursor
        :param object count: 每页数量/Number per page
        :param object cover_format: 封面格式/Cover format
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sec_uid', 'cursor', 'count', 'cover_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_repost_api_v1_tiktok_web_fetch_user_repost_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sec_uid' is set
        if self.api_client.client_side_validation and ('sec_uid' not in params or
                                                       params['sec_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sec_uid` when calling `fetch_user_repost_api_v1_tiktok_web_fetch_user_repost_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sec_uid' in params:
            query_params.append(('secUid', params['sec_uid']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'cover_format' in params:
            query_params.append(('coverFormat', params['cover_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/fetch_user_repost', 'GET',
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

    def generate_fingerprint_api_v1_tiktok_web_generate_fingerprint_get(self, **kwargs):  # noqa: E501
        """生成浏览器指纹/Generate browser fingerprint  # noqa: E501

        # [中文] ### 用途: - 生成随机浏览器指纹数据，可用于自定义msToken请求 ### 参数: - browser_type: 指定浏览器类型，可选值:     - chrome_windows: Chrome + Windows     - chrome_mac: Chrome + macOS     - firefox_windows: Firefox + Windows     - firefox_mac: Firefox + macOS     - 不传则随机选择 ### 返回: - 浏览器指纹数据  # [English] ### Purpose: - Generate random browser fingerprint data for custom msToken request ### Parameters: - browser_type: Specify browser type, options:     - chrome_windows: Chrome + Windows     - chrome_mac: Chrome + macOS     - firefox_windows: Firefox + Windows     - firefox_mac: Firefox + macOS     - Leave empty for random selection ### Return: - Browser fingerprint data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_fingerprint_api_v1_tiktok_web_generate_fingerprint_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object browser_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_fingerprint_api_v1_tiktok_web_generate_fingerprint_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_fingerprint_api_v1_tiktok_web_generate_fingerprint_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_fingerprint_api_v1_tiktok_web_generate_fingerprint_get_with_http_info(self, **kwargs):  # noqa: E501
        """生成浏览器指纹/Generate browser fingerprint  # noqa: E501

        # [中文] ### 用途: - 生成随机浏览器指纹数据，可用于自定义msToken请求 ### 参数: - browser_type: 指定浏览器类型，可选值:     - chrome_windows: Chrome + Windows     - chrome_mac: Chrome + macOS     - firefox_windows: Firefox + Windows     - firefox_mac: Firefox + macOS     - 不传则随机选择 ### 返回: - 浏览器指纹数据  # [English] ### Purpose: - Generate random browser fingerprint data for custom msToken request ### Parameters: - browser_type: Specify browser type, options:     - chrome_windows: Chrome + Windows     - chrome_mac: Chrome + macOS     - firefox_windows: Firefox + Windows     - firefox_mac: Firefox + macOS     - Leave empty for random selection ### Return: - Browser fingerprint data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_fingerprint_api_v1_tiktok_web_generate_fingerprint_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object browser_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['browser_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_fingerprint_api_v1_tiktok_web_generate_fingerprint_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'browser_type' in params:
            query_params.append(('browser_type', params['browser_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/generate_fingerprint', 'GET',
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

    def generate_hashed_id_api_v1_tiktok_web_generate_hashed_id_get(self, email, **kwargs):  # noqa: E501
        """生成哈希ID/Generate hashed ID  # noqa: E501

        # [中文] ### 用途: - 生成TikTok Web的哈希ID ### 参数: - email: 邮箱地址 ### 返回: - 生成的哈希ID字符串  # [English] ### Purpose: - Generate hashed ID for TikTok Web ### Parameters: - email: Email address ### Return: - Generated hashed ID string  # [示例/Example] email = \"test@example.com\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_hashed_id_api_v1_tiktok_web_generate_hashed_id_get(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object email: 邮箱地址/Email address (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_hashed_id_api_v1_tiktok_web_generate_hashed_id_get_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_hashed_id_api_v1_tiktok_web_generate_hashed_id_get_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def generate_hashed_id_api_v1_tiktok_web_generate_hashed_id_get_with_http_info(self, email, **kwargs):  # noqa: E501
        """生成哈希ID/Generate hashed ID  # noqa: E501

        # [中文] ### 用途: - 生成TikTok Web的哈希ID ### 参数: - email: 邮箱地址 ### 返回: - 生成的哈希ID字符串  # [English] ### Purpose: - Generate hashed ID for TikTok Web ### Parameters: - email: Email address ### Return: - Generated hashed ID string  # [示例/Example] email = \"test@example.com\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_hashed_id_api_v1_tiktok_web_generate_hashed_id_get_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object email: 邮箱地址/Email address (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_hashed_id_api_v1_tiktok_web_generate_hashed_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if self.api_client.client_side_validation and ('email' not in params or
                                                       params['email'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `email` when calling `generate_hashed_id_api_v1_tiktok_web_generate_hashed_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'email' in params:
            query_params.append(('email', params['email']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/generate_hashed_id', 'GET',
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

    def generate_real_ms_token_api_v1_tiktok_web_generate_real_ms_token_get(self, **kwargs):  # noqa: E501
        """生成真实msToken/Generate real msToken  # noqa: E501

        # [中文] ### 用途: - 生成真实msToken ### 参数: - random_strData: 是否使用随机化的浏览器指纹数据（推荐开启以提高反爬虫能力） - browser_type: 指定浏览器类型，可选值:     - chrome_windows: Chrome + Windows     - chrome_mac: Chrome + macOS     - firefox_windows: Firefox + Windows     - firefox_mac: Firefox + macOS     - 不传则随机选择 ### 返回: - 真实msToken  # [English] ### Purpose: - Generate real msToken ### Parameters: - random_strData: Whether to use randomized browser fingerprint data (recommended for better anti-bot) - browser_type: Specify browser type, options:     - chrome_windows: Chrome + Windows     - chrome_mac: Chrome + macOS     - firefox_windows: Firefox + Windows     - firefox_mac: Firefox + macOS     - Leave empty for random selection ### Return: - Real msToken  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_real_ms_token_api_v1_tiktok_web_generate_real_ms_token_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object random_str_data:
        :param object browser_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_real_ms_token_api_v1_tiktok_web_generate_real_ms_token_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_real_ms_token_api_v1_tiktok_web_generate_real_ms_token_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_real_ms_token_api_v1_tiktok_web_generate_real_ms_token_get_with_http_info(self, **kwargs):  # noqa: E501
        """生成真实msToken/Generate real msToken  # noqa: E501

        # [中文] ### 用途: - 生成真实msToken ### 参数: - random_strData: 是否使用随机化的浏览器指纹数据（推荐开启以提高反爬虫能力） - browser_type: 指定浏览器类型，可选值:     - chrome_windows: Chrome + Windows     - chrome_mac: Chrome + macOS     - firefox_windows: Firefox + Windows     - firefox_mac: Firefox + macOS     - 不传则随机选择 ### 返回: - 真实msToken  # [English] ### Purpose: - Generate real msToken ### Parameters: - random_strData: Whether to use randomized browser fingerprint data (recommended for better anti-bot) - browser_type: Specify browser type, options:     - chrome_windows: Chrome + Windows     - chrome_mac: Chrome + macOS     - firefox_windows: Firefox + Windows     - firefox_mac: Firefox + macOS     - Leave empty for random selection ### Return: - Real msToken  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_real_ms_token_api_v1_tiktok_web_generate_real_ms_token_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object random_str_data:
        :param object browser_type:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['random_str_data', 'browser_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_real_ms_token_api_v1_tiktok_web_generate_real_ms_token_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'random_str_data' in params:
            query_params.append(('random_strData', params['random_str_data']))  # noqa: E501
        if 'browser_type' in params:
            query_params.append(('browser_type', params['browser_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/generate_real_msToken', 'GET',
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

    def generate_ttwid_api_v1_tiktok_web_generate_ttwid_get(self, **kwargs):  # noqa: E501
        """生成ttwid/Generate ttwid  # noqa: E501

        # [中文] ### 用途: - 生成ttwid ### 参数: - 无 ### 返回: - ttwid  # [English] ### Purpose: - Generate ttwid ### Parameters: - None ### Return: - ttwid  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_ttwid_api_v1_tiktok_web_generate_ttwid_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_agent:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_ttwid_api_v1_tiktok_web_generate_ttwid_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_ttwid_api_v1_tiktok_web_generate_ttwid_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_ttwid_api_v1_tiktok_web_generate_ttwid_get_with_http_info(self, **kwargs):  # noqa: E501
        """生成ttwid/Generate ttwid  # noqa: E501

        # [中文] ### 用途: - 生成ttwid ### 参数: - 无 ### 返回: - ttwid  # [English] ### Purpose: - Generate ttwid ### Parameters: - None ### Return: - ttwid  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_ttwid_api_v1_tiktok_web_generate_ttwid_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_agent:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_ttwid_api_v1_tiktok_web_generate_ttwid_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/generate_ttwid', 'GET',
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

    def generate_webid_api_v1_tiktok_web_generate_webid_get(self, **kwargs):  # noqa: E501
        """生成web_id/Generate web_id  # noqa: E501

        # [中文] ### 用途: - 生成 TikTok web_id （Web接口请求参数中的device_id） ### 参数: - cookie: 自定义 cookie（需包含 odin_tt），如不传则使用随机生成的游客Cookie值 - user_agent: 用户代理字符串 - url: 请求来源 URL - referer: 来源页面 - user_unique_id: 用户唯一 ID（可选） - app_id: 应用 ID，默认 1988，代表 TikTok Web 应用 ### 返回: - web_id: 生成的 web_id - e: 错误码 (0 表示成功) - ssid: 会话 ID  # [English] ### Purpose: - Generate TikTok web_id (device_id in Web API request parameters) ### Parameters: - cookie: Custom cookie (must contain odin_tt), uses default if not provided - user_agent: User agent string - url: Request source URL - referer: Referrer page - user_unique_id: User unique ID (optional) - app_id: Application ID, default 1988, represents TikTok Web app ### Return: - web_id: Generated web_id - e: Error code (0 means success) - ssid: Session ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_webid_api_v1_tiktok_web_generate_webid_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cookie:
        :param object user_agent:
        :param object url:
        :param object referer:
        :param object user_unique_id:
        :param object app_id:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_webid_api_v1_tiktok_web_generate_webid_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_webid_api_v1_tiktok_web_generate_webid_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_webid_api_v1_tiktok_web_generate_webid_get_with_http_info(self, **kwargs):  # noqa: E501
        """生成web_id/Generate web_id  # noqa: E501

        # [中文] ### 用途: - 生成 TikTok web_id （Web接口请求参数中的device_id） ### 参数: - cookie: 自定义 cookie（需包含 odin_tt），如不传则使用随机生成的游客Cookie值 - user_agent: 用户代理字符串 - url: 请求来源 URL - referer: 来源页面 - user_unique_id: 用户唯一 ID（可选） - app_id: 应用 ID，默认 1988，代表 TikTok Web 应用 ### 返回: - web_id: 生成的 web_id - e: 错误码 (0 表示成功) - ssid: 会话 ID  # [English] ### Purpose: - Generate TikTok web_id (device_id in Web API request parameters) ### Parameters: - cookie: Custom cookie (must contain odin_tt), uses default if not provided - user_agent: User agent string - url: Request source URL - referer: Referrer page - user_unique_id: User unique ID (optional) - app_id: Application ID, default 1988, represents TikTok Web app ### Return: - web_id: Generated web_id - e: Error code (0 means success) - ssid: Session ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_webid_api_v1_tiktok_web_generate_webid_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cookie:
        :param object user_agent:
        :param object url:
        :param object referer:
        :param object user_unique_id:
        :param object app_id:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cookie', 'user_agent', 'url', 'referer', 'user_unique_id', 'app_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_webid_api_v1_tiktok_web_generate_webid_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cookie' in params:
            query_params.append(('cookie', params['cookie']))  # noqa: E501
        if 'user_agent' in params:
            query_params.append(('user_agent', params['user_agent']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501
        if 'referer' in params:
            query_params.append(('referer', params['referer']))  # noqa: E501
        if 'user_unique_id' in params:
            query_params.append(('user_unique_id', params['user_unique_id']))  # noqa: E501
        if 'app_id' in params:
            query_params.append(('app_id', params['app_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/generate_webid', 'GET',
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

    def generate_xbogus_api_v1_tiktok_web_generate_xbogus_post(self, **kwargs):  # noqa: E501
        """生成 XBogus/Generate XBogus  # noqa: E501

        # [中文] ### 用途: - 生成xbogus ### 参数: - url: 未签名的API URL - user_agent: 用户浏览器User-Agent ### 返回: - xbogus  # [English] ### Purpose: - Generate xbogus ### Parameters: - url: Unsigned API URL - user_agent: User browser User-Agent ### Return: - xbogus  # [示例/Example]  ```json {     \"url\": \"https://www.tiktok.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=128&device_memory=10240&platform=PC&downlink=10&effective_type=4g&round_trip_time=100\",     \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\" }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_xbogus_api_v1_tiktok_web_generate_xbogus_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_xbogus_api_v1_tiktok_web_generate_xbogus_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_xbogus_api_v1_tiktok_web_generate_xbogus_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_xbogus_api_v1_tiktok_web_generate_xbogus_post_with_http_info(self, **kwargs):  # noqa: E501
        """生成 XBogus/Generate XBogus  # noqa: E501

        # [中文] ### 用途: - 生成xbogus ### 参数: - url: 未签名的API URL - user_agent: 用户浏览器User-Agent ### 返回: - xbogus  # [English] ### Purpose: - Generate xbogus ### Parameters: - url: Unsigned API URL - user_agent: User browser User-Agent ### Return: - xbogus  # [示例/Example]  ```json {     \"url\": \"https://www.tiktok.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=128&device_memory=10240&platform=PC&downlink=10&effective_type=4g&round_trip_time=100\",     \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36\" }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_xbogus_api_v1_tiktok_web_generate_xbogus_post_with_http_info(async_req=True)
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
                    " to method generate_xbogus_api_v1_tiktok_web_generate_xbogus_post" % key
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
            '/api/v1/tiktok/web/generate_xbogus', 'POST',
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

    def generate_xgnarly_and_xbogus_api_v1_tiktok_web_generate_xgnarly_and_xbogus_post(self, **kwargs):  # noqa: E501
        """生成 XGnarly 和 XBogus /Generate XGnarly and XBogus  # noqa: E501

        # [中文] ### 用途: - 生成 XGnarly 加密，用于 TikTok Web API 请求 - 用这个接口可以生成最新版本的加密参数 X-Bogus 和 X-Gnarly，不可自定义 User-Agent，会自动生成一个常见浏览器的User-Agent - 此接口为完美还原算法，无视除验证码外的一切风控，可以用于爬取商品，价格：0.005 美金/次 - 本接口生成的 X-Bogus 和 X-Gnarly 均为最新版本（2026年1月） ### 参数: - url (str): 不携带签名（X-Bogus 或 X-Gnarly）并且包含域名的请求URL，不需要进行URL编码 - body (str): 请求的API参数，适用于POST请求，如果是GET请求则不需要提供 ### 返回: - 最新版本的 X-Gnarly 加密 + 最新版本的 X-Bogus 加密 + 随机浏览器的 User-Agent  # [English] ### Purpose: - Generate XGnarly encryption, used for TikTok Web API requests - This interface can generate the latest version of encryption parameters X-Bogus and X-Gnarly, User-Agent cannot be customized, a common browser User-Agent will be automatically generated - This interface perfectly restores the algorithm, ignores all risk controls except for verification codes, and can be used to crawl products, price: $0.005/time - The X-Bogus and X-Gnarly generated by this interface are the latest versions (January 2026) ### Parameters: - url (str): The requested API URL without signature (X-Bogus or X-Gnarly) and including the domain name, no need to URL encode - body (str): The API parameters of the request, applicable for POST requests, not required for ### Return: - The latest version of X-Gnarly encryption + the latest version of X-Bogus encryption + User-Agent of a random browser  # [示例/Example]  ```json {     \"url\": \"https://www.tiktok.com/api/search/user/full/?WebIdLastTime=1756087650&aid=1988&app_language=zh-Hans&app_name=tiktok_web&browser_language=zh-CN&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=10&data_collection_enabled=false&device_id=7542339104672111234&device_platform=web_pc&focus_state=true&from_page=search&history_len=3&is_fullscreen=true&is_page_visible=true&keyword=musk&odinId=7542338997269211234&os=mac&priority_region&referer&region=US&screen_height=967&screen_width=1496&search_id&tz_name=America%2FLos_Angeles&user_is_login=false&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=zh-Hans\",     \"body\": \"\" }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_xgnarly_and_xbogus_api_v1_tiktok_web_generate_xgnarly_and_xbogus_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_xgnarly_and_xbogus_api_v1_tiktok_web_generate_xgnarly_and_xbogus_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_xgnarly_and_xbogus_api_v1_tiktok_web_generate_xgnarly_and_xbogus_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_xgnarly_and_xbogus_api_v1_tiktok_web_generate_xgnarly_and_xbogus_post_with_http_info(self, **kwargs):  # noqa: E501
        """生成 XGnarly 和 XBogus /Generate XGnarly and XBogus  # noqa: E501

        # [中文] ### 用途: - 生成 XGnarly 加密，用于 TikTok Web API 请求 - 用这个接口可以生成最新版本的加密参数 X-Bogus 和 X-Gnarly，不可自定义 User-Agent，会自动生成一个常见浏览器的User-Agent - 此接口为完美还原算法，无视除验证码外的一切风控，可以用于爬取商品，价格：0.005 美金/次 - 本接口生成的 X-Bogus 和 X-Gnarly 均为最新版本（2026年1月） ### 参数: - url (str): 不携带签名（X-Bogus 或 X-Gnarly）并且包含域名的请求URL，不需要进行URL编码 - body (str): 请求的API参数，适用于POST请求，如果是GET请求则不需要提供 ### 返回: - 最新版本的 X-Gnarly 加密 + 最新版本的 X-Bogus 加密 + 随机浏览器的 User-Agent  # [English] ### Purpose: - Generate XGnarly encryption, used for TikTok Web API requests - This interface can generate the latest version of encryption parameters X-Bogus and X-Gnarly, User-Agent cannot be customized, a common browser User-Agent will be automatically generated - This interface perfectly restores the algorithm, ignores all risk controls except for verification codes, and can be used to crawl products, price: $0.005/time - The X-Bogus and X-Gnarly generated by this interface are the latest versions (January 2026) ### Parameters: - url (str): The requested API URL without signature (X-Bogus or X-Gnarly) and including the domain name, no need to URL encode - body (str): The API parameters of the request, applicable for POST requests, not required for ### Return: - The latest version of X-Gnarly encryption + the latest version of X-Bogus encryption + User-Agent of a random browser  # [示例/Example]  ```json {     \"url\": \"https://www.tiktok.com/api/search/user/full/?WebIdLastTime=1756087650&aid=1988&app_language=zh-Hans&app_name=tiktok_web&browser_language=zh-CN&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=10&data_collection_enabled=false&device_id=7542339104672111234&device_platform=web_pc&focus_state=true&from_page=search&history_len=3&is_fullscreen=true&is_page_visible=true&keyword=musk&odinId=7542338997269211234&os=mac&priority_region&referer&region=US&screen_height=967&screen_width=1496&search_id&tz_name=America%2FLos_Angeles&user_is_login=false&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=zh-Hans\",     \"body\": \"\" }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_xgnarly_and_xbogus_api_v1_tiktok_web_generate_xgnarly_and_xbogus_post_with_http_info(async_req=True)
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
                    " to method generate_xgnarly_and_xbogus_api_v1_tiktok_web_generate_xgnarly_and_xbogus_post" % key
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
            '/api/v1/tiktok/web/generate_xgnarly_and_xbogus', 'POST',
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

    def generate_xgnarly_api_v1_tiktok_web_generate_xgnarly_post(self, **kwargs):  # noqa: E501
        """生成 XGnarly /Generate XGnarly  # noqa: E501

        # [中文] ### 用途: - 生成 XGnarly 加密，用于 TikTok Web API 请求 ### 参数: - url (str): 不携带签名（X-Bogus 或 X-Gnarly）的 原始 URL 字符串 或 查询参数字符串，不需要进行URL编码 - user_agent (str): 用户浏览器User-Agent，参与加密，请确保与请求时的User-Agent一致 - body (str): 请求的API参数，适用于POST请求，如果是GET请求则不需要提供 ### 返回: - X-Gnarly 加密字符串  # [English] ### Purpose: - Generate XGnarly encryption, used for TikTok Web API requests ### Parameters: - url (str): The original URL string or query parameter string without signature (X-Bogus or X-Gnarly), no need to URL encode - user_agent (str): User browser User-Agent, involved in encryption, please ensure it is consistent with the User-Agent when requesting - body (str): The API parameters of the request, applicable for POST requests, not required for ### Return: - X-Gnarly encryption string  # [示例/Example]  ```json {     \"url\": \"https://www.tiktok.com/api/search/user/full/?WebIdLastTime=1756087650&aid=1988&app_language=zh-Hans&app_name=tiktok_web&browser_language=zh-CN&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=10&data_collection_enabled=false&device_id=7542339104672111234&device_platform=web_pc&focus_state=true&from_page=search&history_len=3&is_fullscreen=true&is_page_visible=true&keyword=musk&odinId=7542338997269211234&os=mac&priority_region&referer&region=US&screen_height=967&screen_width=1496&search_id&tz_name=America%2FLos_Angeles&user_is_login=false&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=zh-Hans\",     \"user_agent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36\",     \"body\": \"\" }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_xgnarly_api_v1_tiktok_web_generate_xgnarly_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_xgnarly_api_v1_tiktok_web_generate_xgnarly_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.generate_xgnarly_api_v1_tiktok_web_generate_xgnarly_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def generate_xgnarly_api_v1_tiktok_web_generate_xgnarly_post_with_http_info(self, **kwargs):  # noqa: E501
        """生成 XGnarly /Generate XGnarly  # noqa: E501

        # [中文] ### 用途: - 生成 XGnarly 加密，用于 TikTok Web API 请求 ### 参数: - url (str): 不携带签名（X-Bogus 或 X-Gnarly）的 原始 URL 字符串 或 查询参数字符串，不需要进行URL编码 - user_agent (str): 用户浏览器User-Agent，参与加密，请确保与请求时的User-Agent一致 - body (str): 请求的API参数，适用于POST请求，如果是GET请求则不需要提供 ### 返回: - X-Gnarly 加密字符串  # [English] ### Purpose: - Generate XGnarly encryption, used for TikTok Web API requests ### Parameters: - url (str): The original URL string or query parameter string without signature (X-Bogus or X-Gnarly), no need to URL encode - user_agent (str): User browser User-Agent, involved in encryption, please ensure it is consistent with the User-Agent when requesting - body (str): The API parameters of the request, applicable for POST requests, not required for ### Return: - X-Gnarly encryption string  # [示例/Example]  ```json {     \"url\": \"https://www.tiktok.com/api/search/user/full/?WebIdLastTime=1756087650&aid=1988&app_language=zh-Hans&app_name=tiktok_web&browser_language=zh-CN&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=10&data_collection_enabled=false&device_id=7542339104672111234&device_platform=web_pc&focus_state=true&from_page=search&history_len=3&is_fullscreen=true&is_page_visible=true&keyword=musk&odinId=7542338997269211234&os=mac&priority_region&referer&region=US&screen_height=967&screen_width=1496&search_id&tz_name=America%2FLos_Angeles&user_is_login=false&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=zh-Hans\",     \"user_agent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36\",     \"body\": \"\" }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_xgnarly_api_v1_tiktok_web_generate_xgnarly_post_with_http_info(async_req=True)
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
                    " to method generate_xgnarly_api_v1_tiktok_web_generate_xgnarly_post" % key
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
            '/api/v1/tiktok/web/generate_xgnarly', 'POST',
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

    def get_all_aweme_id_api_v1_tiktok_web_get_all_aweme_id_post(self, **kwargs):  # noqa: E501
        """提取列表作品id/Extract list video id  # noqa: E501

        # [中文] ### 用途: - 提取列表作品id ### 参数: - url: 作品链接 (最多支持20个链接) ### 返回: - 作品id  # [English] ### Purpose: - Extract list video id ### Parameters: - url: Video link (Support up to 20 links) ### Return: - Video id  # [示例/Example] url = [\"https://www.tiktok.com/@owlcitymusic/video/7218694761253735723\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_aweme_id_api_v1_tiktok_web_get_all_aweme_id_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_aweme_id_api_v1_tiktok_web_get_all_aweme_id_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_aweme_id_api_v1_tiktok_web_get_all_aweme_id_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_aweme_id_api_v1_tiktok_web_get_all_aweme_id_post_with_http_info(self, **kwargs):  # noqa: E501
        """提取列表作品id/Extract list video id  # noqa: E501

        # [中文] ### 用途: - 提取列表作品id ### 参数: - url: 作品链接 (最多支持20个链接) ### 返回: - 作品id  # [English] ### Purpose: - Extract list video id ### Parameters: - url: Video link (Support up to 20 links) ### Return: - Video id  # [示例/Example] url = [\"https://www.tiktok.com/@owlcitymusic/video/7218694761253735723\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_aweme_id_api_v1_tiktok_web_get_all_aweme_id_post_with_http_info(async_req=True)
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
                    " to method get_all_aweme_id_api_v1_tiktok_web_get_all_aweme_id_post" % key
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
            '/api/v1/tiktok/web/get_all_aweme_id', 'POST',
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

    def get_all_sec_user_id_api_v1_tiktok_web_get_all_sec_user_id_post(self, **kwargs):  # noqa: E501
        """提取列表用户sec_user_id/Extract list user sec_user_id  # noqa: E501

        # [中文] ### 用途: - 提取列表用户id ### 参数: - url: 用户主页链接（最多支持10个链接）、 ### 返回: - 如果链接成功获取到sec_user_id，则返回sec_user_id，否则返回原始的输入链接，后续可以手动校验链接无法获取sec_user_id的原因。  # [English] ### Purpose: - Extract list user id ### Parameters: - url: User homepage link (Support up to 10 links) ### Return: - If the sec_user_id is successfully obtained, the sec_user_id is returned, otherwise the original input link is returned, and the reason why the sec_user_id cannot be obtained can be manually verified later.  # [示例/Example] url = [\"https://www.tiktok.com/@tiktok\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_sec_user_id_api_v1_tiktok_web_get_all_sec_user_id_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_sec_user_id_api_v1_tiktok_web_get_all_sec_user_id_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_sec_user_id_api_v1_tiktok_web_get_all_sec_user_id_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_sec_user_id_api_v1_tiktok_web_get_all_sec_user_id_post_with_http_info(self, **kwargs):  # noqa: E501
        """提取列表用户sec_user_id/Extract list user sec_user_id  # noqa: E501

        # [中文] ### 用途: - 提取列表用户id ### 参数: - url: 用户主页链接（最多支持10个链接）、 ### 返回: - 如果链接成功获取到sec_user_id，则返回sec_user_id，否则返回原始的输入链接，后续可以手动校验链接无法获取sec_user_id的原因。  # [English] ### Purpose: - Extract list user id ### Parameters: - url: User homepage link (Support up to 10 links) ### Return: - If the sec_user_id is successfully obtained, the sec_user_id is returned, otherwise the original input link is returned, and the reason why the sec_user_id cannot be obtained can be manually verified later.  # [示例/Example] url = [\"https://www.tiktok.com/@tiktok\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_sec_user_id_api_v1_tiktok_web_get_all_sec_user_id_post_with_http_info(async_req=True)
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
                    " to method get_all_sec_user_id_api_v1_tiktok_web_get_all_sec_user_id_post" % key
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
            '/api/v1/tiktok/web/get_all_sec_user_id', 'POST',
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

    def get_all_unique_id_api_v1_tiktok_web_get_all_unique_id_post(self, **kwargs):  # noqa: E501
        """获取列表unique_id/Get list unique_id  # noqa: E501

        # [中文] ### 用途: - 获取列表unique_id ### 参数: - url: 用户主页链接 (最多支持20个链接) ### 返回: - unique_id  # [English] ### Purpose: - Get list unique_id ### Parameters: - url: User homepage link (Support up to 20 links) ### Return: - unique_id  # [示例/Example] url = [\"https://www.tiktok.com/@tiktok\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_unique_id_api_v1_tiktok_web_get_all_unique_id_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_unique_id_api_v1_tiktok_web_get_all_unique_id_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_unique_id_api_v1_tiktok_web_get_all_unique_id_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_unique_id_api_v1_tiktok_web_get_all_unique_id_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取列表unique_id/Get list unique_id  # noqa: E501

        # [中文] ### 用途: - 获取列表unique_id ### 参数: - url: 用户主页链接 (最多支持20个链接) ### 返回: - unique_id  # [English] ### Purpose: - Get list unique_id ### Parameters: - url: User homepage link (Support up to 20 links) ### Return: - unique_id  # [示例/Example] url = [\"https://www.tiktok.com/@tiktok\"]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_unique_id_api_v1_tiktok_web_get_all_unique_id_post_with_http_info(async_req=True)
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
                    " to method get_all_unique_id_api_v1_tiktok_web_get_all_unique_id_post" % key
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
            '/api/v1/tiktok/web/get_all_unique_id', 'POST',
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

    def get_aweme_id_api_v1_tiktok_web_get_aweme_id_get(self, url, **kwargs):  # noqa: E501
        """提取单个作品id/Extract single video id  # noqa: E501

        # [中文] ### 用途: - 提取单个作品id ### 参数: - url: 作品链接 ### 返回: - 作品id  # [English] ### Purpose: - Extract single video id ### Parameters: - url: Video link ### Return: - Video id  # [示例/Example] url = \"https://www.tiktok.com/@owlcitymusic/video/7218694761253735723\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_aweme_id_api_v1_tiktok_web_get_aweme_id_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 作品链接/Video link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_aweme_id_api_v1_tiktok_web_get_aweme_id_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.get_aweme_id_api_v1_tiktok_web_get_aweme_id_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def get_aweme_id_api_v1_tiktok_web_get_aweme_id_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """提取单个作品id/Extract single video id  # noqa: E501

        # [中文] ### 用途: - 提取单个作品id ### 参数: - url: 作品链接 ### 返回: - 作品id  # [English] ### Purpose: - Extract single video id ### Parameters: - url: Video link ### Return: - Video id  # [示例/Example] url = \"https://www.tiktok.com/@owlcitymusic/video/7218694761253735723\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_aweme_id_api_v1_tiktok_web_get_aweme_id_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 作品链接/Video link (required)
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
                    " to method get_aweme_id_api_v1_tiktok_web_get_aweme_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `get_aweme_id_api_v1_tiktok_web_get_aweme_id_get`")  # noqa: E501

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
            '/api/v1/tiktok/web/get_aweme_id', 'GET',
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

    def get_live_room_id_api_v1_tiktok_web_get_live_room_id_get(self, live_room_url, **kwargs):  # noqa: E501
        """根据直播间链接提取直播间ID/Extract live room ID from live room link  # noqa: E501

        # [中文] ### 用途: - 根据直播间链接提取直播间Room ID - 支持短链接，如：https://vt.tiktok.com/ZSjuyJnWQ/ - 支持长链接，如：https://www.tiktok.com/@maksukaracun/live ### 参数: - live_room_url: 直播间链接 ### 返回: - 直播间Room ID  # [English] ### Purpose: - Extract live room Room ID from live room link - Support short links, such as: https://vt.tiktok.com/ZSjuyJnWQ/ - Support long links, such as: https://www.tiktok.com/@maksukaracun/live ### Parameters: - live_room_url: Live room link ### Return: - Live room Room ID  # [示例/Example] live_room_url = \"https://www.tiktok.com/@maksukaracun/live\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_live_room_id_api_v1_tiktok_web_get_live_room_id_get(live_room_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object live_room_url: 直播间链接/Live room link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_live_room_id_api_v1_tiktok_web_get_live_room_id_get_with_http_info(live_room_url, **kwargs)  # noqa: E501
        else:
            (data) = self.get_live_room_id_api_v1_tiktok_web_get_live_room_id_get_with_http_info(live_room_url, **kwargs)  # noqa: E501
            return data

    def get_live_room_id_api_v1_tiktok_web_get_live_room_id_get_with_http_info(self, live_room_url, **kwargs):  # noqa: E501
        """根据直播间链接提取直播间ID/Extract live room ID from live room link  # noqa: E501

        # [中文] ### 用途: - 根据直播间链接提取直播间Room ID - 支持短链接，如：https://vt.tiktok.com/ZSjuyJnWQ/ - 支持长链接，如：https://www.tiktok.com/@maksukaracun/live ### 参数: - live_room_url: 直播间链接 ### 返回: - 直播间Room ID  # [English] ### Purpose: - Extract live room Room ID from live room link - Support short links, such as: https://vt.tiktok.com/ZSjuyJnWQ/ - Support long links, such as: https://www.tiktok.com/@maksukaracun/live ### Parameters: - live_room_url: Live room link ### Return: - Live room Room ID  # [示例/Example] live_room_url = \"https://www.tiktok.com/@maksukaracun/live\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_live_room_id_api_v1_tiktok_web_get_live_room_id_get_with_http_info(live_room_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object live_room_url: 直播间链接/Live room link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['live_room_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_live_room_id_api_v1_tiktok_web_get_live_room_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'live_room_url' is set
        if self.api_client.client_side_validation and ('live_room_url' not in params or
                                                       params['live_room_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `live_room_url` when calling `get_live_room_id_api_v1_tiktok_web_get_live_room_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'live_room_url' in params:
            query_params.append(('live_room_url', params['live_room_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/get_live_room_id', 'GET',
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

    def get_sec_user_id_api_v1_tiktok_web_get_sec_user_id_get(self, url, **kwargs):  # noqa: E501
        """提取用户sec_user_id/Extract user sec_user_id  # noqa: E501

        # [中文] ### 用途: - 提取列表用户id ### 参数: - url: 用户主页链接 ### 返回: - 用户id  # [English] ### Purpose: - Extract list user id ### Parameters: - url: User homepage link ### Return: - User id  # [示例/Example] url = \"https://www.tiktok.com/@tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sec_user_id_api_v1_tiktok_web_get_sec_user_id_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 用户主页链接/User homepage link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sec_user_id_api_v1_tiktok_web_get_sec_user_id_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sec_user_id_api_v1_tiktok_web_get_sec_user_id_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def get_sec_user_id_api_v1_tiktok_web_get_sec_user_id_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """提取用户sec_user_id/Extract user sec_user_id  # noqa: E501

        # [中文] ### 用途: - 提取列表用户id ### 参数: - url: 用户主页链接 ### 返回: - 用户id  # [English] ### Purpose: - Extract list user id ### Parameters: - url: User homepage link ### Return: - User id  # [示例/Example] url = \"https://www.tiktok.com/@tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sec_user_id_api_v1_tiktok_web_get_sec_user_id_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 用户主页链接/User homepage link (required)
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
                    " to method get_sec_user_id_api_v1_tiktok_web_get_sec_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `get_sec_user_id_api_v1_tiktok_web_get_sec_user_id_get`")  # noqa: E501

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
            '/api/v1/tiktok/web/get_sec_user_id', 'GET',
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

    def get_unique_id_api_v1_tiktok_web_get_unique_id_get(self, url, **kwargs):  # noqa: E501
        """获取用户unique_id/Get user unique_id  # noqa: E501

        # [中文] ### 用途: - 获取用户unique_id ### 参数: - url: 用户主页链接 ### 返回: - unique_id  # [English] ### Purpose: - Get user unique_id ### Parameters: - url: User homepage link ### Return: - unique_id  # [示例/Example] url = \"https://www.tiktok.com/@tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_unique_id_api_v1_tiktok_web_get_unique_id_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 用户主页链接/User homepage link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_unique_id_api_v1_tiktok_web_get_unique_id_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.get_unique_id_api_v1_tiktok_web_get_unique_id_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def get_unique_id_api_v1_tiktok_web_get_unique_id_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """获取用户unique_id/Get user unique_id  # noqa: E501

        # [中文] ### 用途: - 获取用户unique_id ### 参数: - url: 用户主页链接 ### 返回: - unique_id  # [English] ### Purpose: - Get user unique_id ### Parameters: - url: User homepage link ### Return: - unique_id  # [示例/Example] url = \"https://www.tiktok.com/@tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_unique_id_api_v1_tiktok_web_get_unique_id_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 用户主页链接/User homepage link (required)
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
                    " to method get_unique_id_api_v1_tiktok_web_get_unique_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `get_unique_id_api_v1_tiktok_web_get_unique_id_get`")  # noqa: E501

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
            '/api/v1/tiktok/web/get_unique_id', 'GET',
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

    def get_user_id_api_v1_tiktok_web_get_user_id_get(self, url, **kwargs):  # noqa: E501
        """提取用户user_id/Extract user user_id  # noqa: E501

        # [中文] ### 用途: - 提取用户user_id ### 参数: - url: 用户主页链接 ### 返回: - 用户id  # [English] ### Purpose: - Extract list user id ### Parameters: - url: User homepage link ### Return: - User id  # [示例/Example] url = \"https://www.tiktok.com/@tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_id_api_v1_tiktok_web_get_user_id_get(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 用户主页链接/User homepage link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_id_api_v1_tiktok_web_get_user_id_get_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_id_api_v1_tiktok_web_get_user_id_get_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def get_user_id_api_v1_tiktok_web_get_user_id_get_with_http_info(self, url, **kwargs):  # noqa: E501
        """提取用户user_id/Extract user user_id  # noqa: E501

        # [中文] ### 用途: - 提取用户user_id ### 参数: - url: 用户主页链接 ### 返回: - 用户id  # [English] ### Purpose: - Extract list user id ### Parameters: - url: User homepage link ### Return: - User id  # [示例/Example] url = \"https://www.tiktok.com/@tiktok\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_id_api_v1_tiktok_web_get_user_id_get_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object url: 用户主页链接/User homepage link (required)
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
                    " to method get_user_id_api_v1_tiktok_web_get_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if self.api_client.client_side_validation and ('url' not in params or
                                                       params['url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `url` when calling `get_user_id_api_v1_tiktok_web_get_user_id_get`")  # noqa: E501

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
            '/api/v1/tiktok/web/get_user_id', 'GET',
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

    def tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get(self, live_room_url, danmaku_type, **kwargs):  # noqa: E501
        """提取直播间弹幕/Extract live room danmaku  # noqa: E501

        # [中文] ### 用途: - 提取直播间弹幕 - 该接口已不再提供线上服务，需要自行购买源代码后在本地部署使用，购买源代码请在Discord服务器联系管理员，Discord邀请链接：https://discord.gg/aMEAS8Xsvz #### 价格: - 每10条数据消耗0.001$，支持阶梯式计费折扣。 ### 参数: - live_room_url: 直播间链接 - danmaku_type: 消息类型     - WebcastChatMessage: 聊天消息     - WebcastMemberMessage: 成员消息     - WebcastRoomUserSeqMessage: 用户序列消息     - WebcastGiftMessage: 礼物消息     - WebcastSocialMessage: 社交消息     - WebcastLikeMessage: 点赞消息     - WebcastLinkMicFanTicketMethod: 连麦粉丝票方法     - WebcastLinkMicMethod: 连麦方法 ### 返回: - 弹幕数据的WebSocket连接信息，需要使用WebSocket连接获取弹幕数据，此接口不返回弹幕数据。  # [English] ### Purpose: - Extract live room danmaku - This interface is no longer available online, you need to purchase the source code and deploy it locally for use. To purchase the source code, please contact the administrator in the Discord server. Discord invite link: https://discord.gg/aMEAS8Xsvz #### Price: - 0.001$ per 10 data, support tiered billing discount. ### Parameters: - live_room_url: Live room link - danmaku_type: Message type     - WebcastChatMessage: Chat message     - WebcastMemberMessage: Member message     - WebcastRoomUserSeqMessage: User sequence message     - WebcastGiftMessage: Gift message     - WebcastSocialMessage: Social message     - WebcastLikeMessage: Like message     - WebcastLinkMicFanTicketMethod: Link Mic Fan Ticket Method     - WebcastLinkMicMethod: Link Mic Method ### Return: - WebSocket connection information of the danmaku data, you need to use WebSocket connection to get the danmaku data, this interface does not return the danmaku data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get(live_room_url, danmaku_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object live_room_url: 直播间链接/Live room link (required)
        :param object danmaku_type: 消息类型/Message type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get_with_http_info(live_room_url, danmaku_type, **kwargs)  # noqa: E501
        else:
            (data) = self.tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get_with_http_info(live_room_url, danmaku_type, **kwargs)  # noqa: E501
            return data

    def tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get_with_http_info(self, live_room_url, danmaku_type, **kwargs):  # noqa: E501
        """提取直播间弹幕/Extract live room danmaku  # noqa: E501

        # [中文] ### 用途: - 提取直播间弹幕 - 该接口已不再提供线上服务，需要自行购买源代码后在本地部署使用，购买源代码请在Discord服务器联系管理员，Discord邀请链接：https://discord.gg/aMEAS8Xsvz #### 价格: - 每10条数据消耗0.001$，支持阶梯式计费折扣。 ### 参数: - live_room_url: 直播间链接 - danmaku_type: 消息类型     - WebcastChatMessage: 聊天消息     - WebcastMemberMessage: 成员消息     - WebcastRoomUserSeqMessage: 用户序列消息     - WebcastGiftMessage: 礼物消息     - WebcastSocialMessage: 社交消息     - WebcastLikeMessage: 点赞消息     - WebcastLinkMicFanTicketMethod: 连麦粉丝票方法     - WebcastLinkMicMethod: 连麦方法 ### 返回: - 弹幕数据的WebSocket连接信息，需要使用WebSocket连接获取弹幕数据，此接口不返回弹幕数据。  # [English] ### Purpose: - Extract live room danmaku - This interface is no longer available online, you need to purchase the source code and deploy it locally for use. To purchase the source code, please contact the administrator in the Discord server. Discord invite link: https://discord.gg/aMEAS8Xsvz #### Price: - 0.001$ per 10 data, support tiered billing discount. ### Parameters: - live_room_url: Live room link - danmaku_type: Message type     - WebcastChatMessage: Chat message     - WebcastMemberMessage: Member message     - WebcastRoomUserSeqMessage: User sequence message     - WebcastGiftMessage: Gift message     - WebcastSocialMessage: Social message     - WebcastLikeMessage: Like message     - WebcastLinkMicFanTicketMethod: Link Mic Fan Ticket Method     - WebcastLinkMicMethod: Link Mic Method ### Return: - WebSocket connection information of the danmaku data, you need to use WebSocket connection to get the danmaku data, this interface does not return the danmaku data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get_with_http_info(live_room_url, danmaku_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object live_room_url: 直播间链接/Live room link (required)
        :param object danmaku_type: 消息类型/Message type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['live_room_url', 'danmaku_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'live_room_url' is set
        if self.api_client.client_side_validation and ('live_room_url' not in params or
                                                       params['live_room_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `live_room_url` when calling `tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get`")  # noqa: E501
        # verify the required parameter 'danmaku_type' is set
        if self.api_client.client_side_validation and ('danmaku_type' not in params or
                                                       params['danmaku_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `danmaku_type` when calling `tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'live_room_url' in params:
            query_params.append(('live_room_url', params['live_room_url']))  # noqa: E501
        if 'danmaku_type' in params:
            query_params.append(('danmaku_type', params['danmaku_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tiktok/web/tiktok_live_room', 'GET',
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
