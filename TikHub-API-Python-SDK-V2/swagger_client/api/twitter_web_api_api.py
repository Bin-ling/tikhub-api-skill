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


class TwitterWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get(self, tweet_id, **kwargs):  # noqa: E501
        """获取最新的推文评论/Get the latest tweet comments  # noqa: E501

        # [中文] ### 用途: - 获取最新的推文评论 ### 参数: - tweet_id: 推文ID - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 推文评论  # [English] ### Purpose: - Get the latest tweet comments ### Parameters: - tweet_id: Tweet ID - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - Tweet comments  # [示例/Example] tweet_id = \"1808168603721650364\" cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get(tweet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tweet_id: 推文ID/Tweet ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get_with_http_info(tweet_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get_with_http_info(tweet_id, **kwargs)  # noqa: E501
            return data

    def fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get_with_http_info(self, tweet_id, **kwargs):  # noqa: E501
        """获取最新的推文评论/Get the latest tweet comments  # noqa: E501

        # [中文] ### 用途: - 获取最新的推文评论 ### 参数: - tweet_id: 推文ID - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 推文评论  # [English] ### Purpose: - Get the latest tweet comments ### Parameters: - tweet_id: Tweet ID - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - Tweet comments  # [示例/Example] tweet_id = \"1808168603721650364\" cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get_with_http_info(tweet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tweet_id: 推文ID/Tweet ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tweet_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tweet_id' is set
        if self.api_client.client_side_validation and ('tweet_id' not in params or
                                                       params['tweet_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tweet_id` when calling `fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tweet_id' in params:
            query_params.append(('tweet_id', params['tweet_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_latest_post_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get(self, tweet_id, **kwargs):  # noqa: E501
        """获取评论/Get comments  # noqa: E501

        # [中文] ### 用途: - 获取推文下的评论 ### 参数: - tweet_id: 推文ID - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 评论  # [English] ### Purpose: - Get comments under the tweet ### Parameters: - tweet_id: Tweet ID - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - Comments  # [示例/Example] tweet_id = \"1808168603721650364\" cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get(tweet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tweet_id: 推文ID/Tweet ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get_with_http_info(tweet_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get_with_http_info(tweet_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get_with_http_info(self, tweet_id, **kwargs):  # noqa: E501
        """获取评论/Get comments  # noqa: E501

        # [中文] ### 用途: - 获取推文下的评论 ### 参数: - tweet_id: 推文ID - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 评论  # [English] ### Purpose: - Get comments under the tweet ### Parameters: - tweet_id: Tweet ID - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - Comments  # [示例/Example] tweet_id = \"1808168603721650364\" cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get_with_http_info(tweet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tweet_id: 推文ID/Tweet ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tweet_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tweet_id' is set
        if self.api_client.client_side_validation and ('tweet_id' not in params or
                                                       params['tweet_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tweet_id` when calling `fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tweet_id' in params:
            query_params.append(('tweet_id', params['tweet_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_post_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get(self, tweet_id, **kwargs):  # noqa: E501
        """转推用户列表/ReTweet User list  # noqa: E501

        # [中文] ### 用途: - 获取转推用户列表 ### 参数: - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的 1808168603721650364。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 转推用户列表  # [English] ### Purpose: - Get ReTweet User list ### Parameters: - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364 - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - ReTweet User list  # [示例/Example] tweet_id = \"1808168603721650364\" cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get(tweet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tweet_id: 推文ID/Tweet ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get_with_http_info(tweet_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get_with_http_info(tweet_id, **kwargs)  # noqa: E501
            return data

    def fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get_with_http_info(self, tweet_id, **kwargs):  # noqa: E501
        """转推用户列表/ReTweet User list  # noqa: E501

        # [中文] ### 用途: - 获取转推用户列表 ### 参数: - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的 1808168603721650364。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 转推用户列表  # [English] ### Purpose: - Get ReTweet User list ### Parameters: - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364 - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - ReTweet User list  # [示例/Example] tweet_id = \"1808168603721650364\" cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get_with_http_info(tweet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tweet_id: 推文ID/Tweet ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tweet_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tweet_id' is set
        if self.api_client.client_side_validation and ('tweet_id' not in params or
                                                       params['tweet_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tweet_id` when calling `fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tweet_id' in params:
            query_params.append(('tweet_id', params['tweet_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_retweet_user_list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get(self, keyword, **kwargs):  # noqa: E501
        """搜索/Search  # noqa: E501

        # [中文] ### 用途: - 搜索 ### 参数: - keyword: 搜索关键字 - search_type: 搜索类型，默认为Top，其他可选值为Latest，Media，People, Lists - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 搜索结果  # [English] ### Purpose: - Search ### Parameters: - keyword: Search keyword - search_type: Search type, default is Top, other optional values are Latest, Media, People, Lists - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - Search results  # [示例/Example] keyword = \"Elon Musk\" search_type = \"Top\" cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键字/Search Keyword (required)
        :param object search_type: 搜索类型/Search Type
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索/Search  # noqa: E501

        # [中文] ### 用途: - 搜索 ### 参数: - keyword: 搜索关键字 - search_type: 搜索类型，默认为Top，其他可选值为Latest，Media，People, Lists - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 搜索结果  # [English] ### Purpose: - Search ### Parameters: - keyword: Search keyword - search_type: Search type, default is Top, other optional values are Latest, Media, People, Lists - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - Search results  # [示例/Example] keyword = \"Elon Musk\" search_type = \"Top\" cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键字/Search Keyword (required)
        :param object search_type: 搜索类型/Search Type
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'search_type', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'search_type' in params:
            query_params.append(('search_type', params['search_type']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_search_timeline', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_trending_api_v1_twitter_web_fetch_trending_get(self, **kwargs):  # noqa: E501
        """趋势/Trending  # noqa: E501

        # [中文] ### 用途: - 获取趋势 ### 参数: - country: 国家，默认为UnitedStates，其他可选值见下方     - China     - India     - Japan     - Russia     - Germany     - Indonesia     - Brazil     - France     - UnitedKingdom     - Turkey     - Italy     - Mexico     - SouthKorea     - Canada     - Spain     - SaudiArabia     - Egypt     - Australia     - Poland     - Iran     - Pakistan     - Vietnam     - Nigeria     - Bangladesh     - Netherlands     - Argentina     - Philippines     - Malaysia     - Colombia     - UniteArabEmirates     - Romania     - Belgium     - Switzerland     - Singapore     - Sweden     - Norway     - Austria     - Kazakhstan     - Algeria     - Chile     - Czechia     - Peru     - Iraq     - Israel     - Ukraine     - Denmark     - Portugal     - Hungary     - Greece     - Finland     - NewZealand     - Belarus     - Slovakia     - Serbia     - Lithuania     - Luxembourg     - Estonia  ### 返回: - 趋势  # [English] ### Purpose: - Get Trending ### Parameters: - country: Country, default is UnitedStates, other optional values are as follows     - China     - India     - Japan     - Russia     - Germany     - Indonesia     - Brazil     - France     - UnitedKingdom     - Turkey     - Italy     - Mexico     - SouthKorea     - Canada     - Spain     - SaudiArabia     - Egypt     - Australia     - Poland     - Iran     - Pakistan     - Vietnam     - Nigeria     - Bangladesh     - Netherlands     - Argentina     - Philippines     - Malaysia     - Colombia     - UniteArabEmirates     - Romania     - Belgium     - Switzerland     - Singapore     - Sweden     - Norway     - Austria     - Kazakhstan     - Algeria     - Chile     - Czechia     - Peru  ### Return: - Trending  # [示例/Example] country = \"UnitedStates\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_trending_api_v1_twitter_web_fetch_trending_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object country: 国家/Country
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_trending_api_v1_twitter_web_fetch_trending_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_trending_api_v1_twitter_web_fetch_trending_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_trending_api_v1_twitter_web_fetch_trending_get_with_http_info(self, **kwargs):  # noqa: E501
        """趋势/Trending  # noqa: E501

        # [中文] ### 用途: - 获取趋势 ### 参数: - country: 国家，默认为UnitedStates，其他可选值见下方     - China     - India     - Japan     - Russia     - Germany     - Indonesia     - Brazil     - France     - UnitedKingdom     - Turkey     - Italy     - Mexico     - SouthKorea     - Canada     - Spain     - SaudiArabia     - Egypt     - Australia     - Poland     - Iran     - Pakistan     - Vietnam     - Nigeria     - Bangladesh     - Netherlands     - Argentina     - Philippines     - Malaysia     - Colombia     - UniteArabEmirates     - Romania     - Belgium     - Switzerland     - Singapore     - Sweden     - Norway     - Austria     - Kazakhstan     - Algeria     - Chile     - Czechia     - Peru     - Iraq     - Israel     - Ukraine     - Denmark     - Portugal     - Hungary     - Greece     - Finland     - NewZealand     - Belarus     - Slovakia     - Serbia     - Lithuania     - Luxembourg     - Estonia  ### 返回: - 趋势  # [English] ### Purpose: - Get Trending ### Parameters: - country: Country, default is UnitedStates, other optional values are as follows     - China     - India     - Japan     - Russia     - Germany     - Indonesia     - Brazil     - France     - UnitedKingdom     - Turkey     - Italy     - Mexico     - SouthKorea     - Canada     - Spain     - SaudiArabia     - Egypt     - Australia     - Poland     - Iran     - Pakistan     - Vietnam     - Nigeria     - Bangladesh     - Netherlands     - Argentina     - Philippines     - Malaysia     - Colombia     - UniteArabEmirates     - Romania     - Belgium     - Switzerland     - Singapore     - Sweden     - Norway     - Austria     - Kazakhstan     - Algeria     - Chile     - Czechia     - Peru  ### Return: - Trending  # [示例/Example] country = \"UnitedStates\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_trending_api_v1_twitter_web_fetch_trending_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object country: 国家/Country
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_trending_api_v1_twitter_web_fetch_trending_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_trending', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get(self, tweet_id, **kwargs):  # noqa: E501
        """获取单个推文数据/Get single tweet data  # noqa: E501

        # [中文] ### 用途: - 获取单个推文数据 ### 参数: - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的 1808168603721650364。 ### 返回: - 推文数据  # [English] ### Purpose: - Get single tweet data ### Parameters: - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364 ### Return: - Tweet data  # [示例/Example] tweet_id = \"1808168603721650364\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get(tweet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tweet_id: 推文ID/Tweet ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get_with_http_info(tweet_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get_with_http_info(tweet_id, **kwargs)  # noqa: E501
            return data

    def fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get_with_http_info(self, tweet_id, **kwargs):  # noqa: E501
        """获取单个推文数据/Get single tweet data  # noqa: E501

        # [中文] ### 用途: - 获取单个推文数据 ### 参数: - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的 1808168603721650364。 ### 返回: - 推文数据  # [English] ### Purpose: - Get single tweet data ### Parameters: - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364 ### Return: - Tweet data  # [示例/Example] tweet_id = \"1808168603721650364\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get_with_http_info(tweet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object tweet_id: 推文ID/Tweet ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tweet_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tweet_id' is set
        if self.api_client.client_side_validation and ('tweet_id' not in params or
                                                       params['tweet_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tweet_id` when calling `fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tweet_id' in params:
            query_params.append(('tweet_id', params['tweet_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_tweet_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get(self, screen_name, **kwargs):  # noqa: E501
        """用户粉丝/User Followers  # noqa: E501

        # [中文] ### 用途: - 获取用户粉丝 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 用户粉丝  # [English] ### Purpose: - Get User Followers ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - User Followers  # [示例/Example] screen_name = \"elonmusk\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get(screen_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get_with_http_info(screen_name, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get_with_http_info(screen_name, **kwargs)  # noqa: E501
            return data

    def fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get_with_http_info(self, screen_name, **kwargs):  # noqa: E501
        """用户粉丝/User Followers  # noqa: E501

        # [中文] ### 用途: - 获取用户粉丝 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 用户粉丝  # [English] ### Purpose: - Get User Followers ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - User Followers  # [示例/Example] screen_name = \"elonmusk\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get_with_http_info(screen_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['screen_name', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'screen_name' is set
        if self.api_client.client_side_validation and ('screen_name' not in params or
                                                       params['screen_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `screen_name` when calling `fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'screen_name' in params:
            query_params.append(('screen_name', params['screen_name']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_user_followers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get(self, screen_name, **kwargs):  # noqa: E501
        """用户关注/User Followings  # noqa: E501

        # [中文] ### 用途: - 获取用户关注 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 用户关注  # [English] ### Purpose: - Get User Followings ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - User Followings  # [示例/Example] screen_name = \"elonmusk\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get(screen_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get_with_http_info(screen_name, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get_with_http_info(screen_name, **kwargs)  # noqa: E501
            return data

    def fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get_with_http_info(self, screen_name, **kwargs):  # noqa: E501
        """用户关注/User Followings  # noqa: E501

        # [中文] ### 用途: - 获取用户关注 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 用户关注  # [English] ### Purpose: - Get User Followings ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - User Followings  # [示例/Example] screen_name = \"elonmusk\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get_with_http_info(screen_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['screen_name', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'screen_name' is set
        if self.api_client.client_side_validation and ('screen_name' not in params or
                                                       params['screen_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `screen_name` when calling `fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'screen_name' in params:
            query_params.append(('screen_name', params['screen_name']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_user_followings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户高光推文/Get user highlights tweets  # noqa: E501

        # [中文] ### 用途: - 获取用户高光推文 ### 参数: - userId: 用户ID - count: 数量，默认为20 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取     - JSONPath: $.data.data.user.result.timeline_v2.timeline.instructions.[1].entries.[-1].content.value ### 返回: - 用户高光推文  # [English] ### Purpose: - Get user highlights tweets ### Parameters: - userId: User ID - count: Count, default is 20 - cursor: Cursor, default is None, used for paging, obtained from the last request     - JSONPath: $.data.data.user.result.timeline_v2.timeline.instructions.[1].entries.[-1].content.value ### Return: - User highlights tweets  # [示例/Example] userId = \"44196397\" count = 20 cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object count: 数量/Count
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户高光推文/Get user highlights tweets  # noqa: E501

        # [中文] ### 用途: - 获取用户高光推文 ### 参数: - userId: 用户ID - count: 数量，默认为20 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取     - JSONPath: $.data.data.user.result.timeline_v2.timeline.instructions.[1].entries.[-1].content.value ### 返回: - 用户高光推文  # [English] ### Purpose: - Get user highlights tweets ### Parameters: - userId: User ID - count: Count, default is 20 - cursor: Cursor, default is None, used for paging, obtained from the last request     - JSONPath: $.data.data.user.result.timeline_v2.timeline.instructions.[1].entries.[-1].content.value ### Return: - User highlights tweets  # [示例/Example] userId = \"44196397\" count = 20 cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object count: 数量/Count
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'count', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('userId', params['user_id']))  # noqa: E501
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
            '/api/v1/twitter/web/fetch_user_highlights_tweets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_media_api_v1_twitter_web_fetch_user_media_get(self, screen_name, **kwargs):  # noqa: E501
        """获取用户媒体/Get user media  # noqa: E501

        # [中文] ### 用途: - 获取用户媒体 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中的 `next_cursor` 获取 ### 返回: - 用户媒体  # [English] ### Purpose: - Get user media ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. - cursor: Cursor, default is None, used for paging, obtained from the `next_cursor` in the last request ### Return: - User media  # [示例/Example] screen_name = \"elonmusk\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_media_api_v1_twitter_web_fetch_user_media_get(screen_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name (required)
        :param object rest_id: 用户ID/User ID
        :param object cursor: 翻页游标/Page Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_media_api_v1_twitter_web_fetch_user_media_get_with_http_info(screen_name, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_media_api_v1_twitter_web_fetch_user_media_get_with_http_info(screen_name, **kwargs)  # noqa: E501
            return data

    def fetch_user_media_api_v1_twitter_web_fetch_user_media_get_with_http_info(self, screen_name, **kwargs):  # noqa: E501
        """获取用户媒体/Get user media  # noqa: E501

        # [中文] ### 用途: - 获取用户媒体 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中的 `next_cursor` 获取 ### 返回: - 用户媒体  # [English] ### Purpose: - Get user media ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. - cursor: Cursor, default is None, used for paging, obtained from the `next_cursor` in the last request ### Return: - User media  # [示例/Example] screen_name = \"elonmusk\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_media_api_v1_twitter_web_fetch_user_media_get_with_http_info(screen_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name (required)
        :param object rest_id: 用户ID/User ID
        :param object cursor: 翻页游标/Page Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['screen_name', 'rest_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_media_api_v1_twitter_web_fetch_user_media_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'screen_name' is set
        if self.api_client.client_side_validation and ('screen_name' not in params or
                                                       params['screen_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `screen_name` when calling `fetch_user_media_api_v1_twitter_web_fetch_user_media_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'screen_name' in params:
            query_params.append(('screen_name', params['screen_name']))  # noqa: E501
        if 'rest_id' in params:
            query_params.append(('rest_id', params['rest_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_user_media', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get(self, **kwargs):  # noqa: E501
        """获取用户发帖/Get user post  # noqa: E501

        # [中文] ### 用途: - 获取用户发帖 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中的JSON中获取。 ### 返回: - 用户发帖  # [English] ### Purpose: - Get user post ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. - cursor: Cursor, default is None, used for paging, obtained from the JSON in the last request.  # [示例/Example] screen_name = \"elonmusk\" rest_id = 44196397 cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name
        :param object rest_id: 用户ID/User ID
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户发帖/Get user post  # noqa: E501

        # [中文] ### 用途: - 获取用户发帖 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中的JSON中获取。 ### 返回: - 用户发帖  # [English] ### Purpose: - Get user post ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. - cursor: Cursor, default is None, used for paging, obtained from the JSON in the last request.  # [示例/Example] screen_name = \"elonmusk\" rest_id = 44196397 cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name
        :param object rest_id: 用户ID/User ID
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['screen_name', 'rest_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'screen_name' in params:
            query_params.append(('screen_name', params['screen_name']))  # noqa: E501
        if 'rest_id' in params:
            query_params.append(('rest_id', params['rest_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_user_post_tweet', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get(self, **kwargs):  # noqa: E501
        """获取用户资料/Get user profile  # noqa: E501

        # [中文] ### 用途: - 获取用户资料 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。 ### 返回: - 用户资料  # [English] ### Purpose: - Get user profile ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. ### Return: - User profile  # [示例/Example] screen_name = \"elonmusk\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name
        :param object rest_id: 用户ID（如果使用用户ID则会忽略用户名）/User ID (If the user ID is used, the user name will be ignored)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户资料/Get user profile  # noqa: E501

        # [中文] ### 用途: - 获取用户资料 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。 ### 返回: - 用户资料  # [English] ### Purpose: - Get user profile ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. ### Return: - User profile  # [示例/Example] screen_name = \"elonmusk\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name
        :param object rest_id: 用户ID（如果使用用户ID则会忽略用户名）/User ID (If the user ID is used, the user name will be ignored)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['screen_name', 'rest_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'screen_name' in params:
            query_params.append(('screen_name', params['screen_name']))  # noqa: E501
        if 'rest_id' in params:
            query_params.append(('rest_id', params['rest_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_user_profile', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get(self, screen_name, **kwargs):  # noqa: E501
        """获取用户推文回复/Get user tweet replies  # noqa: E501

        # [中文] ### 用途: - 获取用户推文回复 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 用户推文回复  # [English] ### Purpose: - Get user tweet replies ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - User tweet replies  # [示例/Example] screen_name = \"elonmusk\" cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get(screen_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get_with_http_info(screen_name, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get_with_http_info(screen_name, **kwargs)  # noqa: E501
            return data

    def fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get_with_http_info(self, screen_name, **kwargs):  # noqa: E501
        """获取用户推文回复/Get user tweet replies  # noqa: E501

        # [中文] ### 用途: - 获取用户推文回复 ### 参数: - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。 - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取 ### 返回: - 用户推文回复  # [English] ### Purpose: - Get user tweet replies ### Parameters: - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk - cursor: Cursor, default is None, used for paging, obtained from the last request ### Return: - User tweet replies  # [示例/Example] screen_name = \"elonmusk\" cursor = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get_with_http_info(screen_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object screen_name: 用户名/Screen Name (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['screen_name', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'screen_name' is set
        if self.api_client.client_side_validation and ('screen_name' not in params or
                                                       params['screen_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `screen_name` when calling `fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'screen_name' in params:
            query_params.append(('screen_name', params['screen_name']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/twitter/web/fetch_user_tweet_replies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
