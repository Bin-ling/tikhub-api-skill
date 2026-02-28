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


class WeChatChannelsAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_comments_api_v1_wechat_channels_fetch_comments_get(self, id, **kwargs):  # noqa: E501
        """微信视频号评论/WeChat Channels Comments  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号视频评论 - 支持分页获取更多评论 - 价格：0.01$/次 ### 参数: - id: 视频ID - lastBuffer: 分页参数，首次请求可为空 - comment_id: 评论ID，默认不传，传入则获取该评论下的子评论 ### 返回: - 视频评论列表  # [English] ### Purpose: - Get WeChat Channels video comments - Support pagination for more comments - Price: $0.01 per request ### Parameters: - id: Video ID - lastBuffer: Pagination parameter, can be empty for first request - comment_id: Comment ID, if provided, fetches replies to that comment ### Return: - Video comment list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comments_api_v1_wechat_channels_fetch_comments_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 视频ID/Video ID (required)
        :param object last_buffer: 分页参数/Pagination parameter
        :param object comment_id: 评论ID，默认不传，传入则获取该评论下的子评论/Comment ID, if provided, fetches replies to that comment
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_comments_api_v1_wechat_channels_fetch_comments_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_comments_api_v1_wechat_channels_fetch_comments_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def fetch_comments_api_v1_wechat_channels_fetch_comments_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """微信视频号评论/WeChat Channels Comments  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号视频评论 - 支持分页获取更多评论 - 价格：0.01$/次 ### 参数: - id: 视频ID - lastBuffer: 分页参数，首次请求可为空 - comment_id: 评论ID，默认不传，传入则获取该评论下的子评论 ### 返回: - 视频评论列表  # [English] ### Purpose: - Get WeChat Channels video comments - Support pagination for more comments - Price: $0.01 per request ### Parameters: - id: Video ID - lastBuffer: Pagination parameter, can be empty for first request - comment_id: Comment ID, if provided, fetches replies to that comment ### Return: - Video comment list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comments_api_v1_wechat_channels_fetch_comments_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 视频ID/Video ID (required)
        :param object last_buffer: 分页参数/Pagination parameter
        :param object comment_id: 评论ID，默认不传，传入则获取该评论下的子评论/Comment ID, if provided, fetches replies to that comment
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'last_buffer', 'comment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_comments_api_v1_wechat_channels_fetch_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `fetch_comments_api_v1_wechat_channels_fetch_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'last_buffer' in params:
            query_params.append(('lastBuffer', params['last_buffer']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/wechat_channels/fetch_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_default_search_api_v1_wechat_channels_fetch_default_search_get(self, keywords, **kwargs):  # noqa: E501
        """微信视频号默认搜索/WeChat Channels Default Search  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号默认搜索结果 - 支持分页获取更多结果 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 - session_buffer:     - 分页参数，首次请求可为空，后续使用响应中的 `last_buff` 进行分页请求     - JSON Path： `$.data.last_buff` ### 返回: - 搜索结果列表，包含视频信息  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取翻页参数 `last_buff`: `$.data.last_buff`     - 获取视频列表: `$.data.media_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.media_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.media_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.media_list[*].object_desc.media[0].url + $.data.media_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.media_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels default search results - Support pagination for more results - Price: $0.01 per request ### Parameters: - keywords: Search keywords - session_buffer: Pagination parameter, can be empty for first request     - For subsequent requests, use `last_buff` from the response for pagination     - JSON Path: `$.data.last_buff`  ### Return: - Search result list with video information ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the pagination parameter `last_buff`: `$.data.last_buff`     - To get the video list: `$.data.media_list[*]`     - To get the video CDN link (without Token): `$.data.media_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.media_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.media_list[*].object_desc.media[0].url + $.data.media_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.media_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_default_search_api_v1_wechat_channels_fetch_default_search_get(keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keywords: 搜索关键词/Search keywords (required)
        :param object session_buffer: 分页参数/Pagination parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_default_search_api_v1_wechat_channels_fetch_default_search_get_with_http_info(keywords, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_default_search_api_v1_wechat_channels_fetch_default_search_get_with_http_info(keywords, **kwargs)  # noqa: E501
            return data

    def fetch_default_search_api_v1_wechat_channels_fetch_default_search_get_with_http_info(self, keywords, **kwargs):  # noqa: E501
        """微信视频号默认搜索/WeChat Channels Default Search  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号默认搜索结果 - 支持分页获取更多结果 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 - session_buffer:     - 分页参数，首次请求可为空，后续使用响应中的 `last_buff` 进行分页请求     - JSON Path： `$.data.last_buff` ### 返回: - 搜索结果列表，包含视频信息  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取翻页参数 `last_buff`: `$.data.last_buff`     - 获取视频列表: `$.data.media_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.media_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.media_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.media_list[*].object_desc.media[0].url + $.data.media_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.media_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels default search results - Support pagination for more results - Price: $0.01 per request ### Parameters: - keywords: Search keywords - session_buffer: Pagination parameter, can be empty for first request     - For subsequent requests, use `last_buff` from the response for pagination     - JSON Path: `$.data.last_buff`  ### Return: - Search result list with video information ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the pagination parameter `last_buff`: `$.data.last_buff`     - To get the video list: `$.data.media_list[*]`     - To get the video CDN link (without Token): `$.data.media_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.media_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.media_list[*].object_desc.media[0].url + $.data.media_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.media_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_default_search_api_v1_wechat_channels_fetch_default_search_get_with_http_info(keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keywords: 搜索关键词/Search keywords (required)
        :param object session_buffer: 分页参数/Pagination parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keywords', 'session_buffer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_default_search_api_v1_wechat_channels_fetch_default_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keywords' is set
        if self.api_client.client_side_validation and ('keywords' not in params or
                                                       params['keywords'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keywords` when calling `fetch_default_search_api_v1_wechat_channels_fetch_default_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501
        if 'session_buffer' in params:
            query_params.append(('session_buffer', params['session_buffer']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/wechat_channels/fetch_default_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_home_page_api_v1_wechat_channels_fetch_home_page_get(self, username, **kwargs):  # noqa: E501
        """微信视频号主页/WeChat Channels Home Page  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号用户主页信息 - 包含用户发布的视频列表 - 支持分页获取更多视频 - 价格：0.01$/次 ### 参数: - username: 用户名 - last_buffer:     - 分页参数，首次请求可为空，后续使用 `object_list` 最后一个 item 的 `last_buffer` 进行分页请求     - JSON Path: `$.data.object_list[-1].last_buffer` ### 返回: - 用户主页信息和视频列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取翻页参数 `last_buffer`: `$.data.object_list[-1].last_buffer`     - 获取视频列表: `$.data.object_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.object_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels user homepage information - Including list of videos published by user - Support pagination for more videos - Price: $0.01 per request ### Parameters: - username: Username - last_buffer:     - Pagination parameter, can be empty for first request     - For subsequent requests, use the `last_buffer` of the last item in `object_list`     - JSON Path: `$.data.object_list[-1].last_buffer` ### Return: - User homepage information and video list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the pagination parameter `last_buffer`: `$.data.object_list[-1].last_buffer`     - To get the video list: `$.data.object_list[*]`     - To get the video CDN link (without Token): `$.data.object_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_page_api_v1_wechat_channels_fetch_home_page_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object last_buffer: 分页参数/Pagination parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_page_api_v1_wechat_channels_fetch_home_page_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_page_api_v1_wechat_channels_fetch_home_page_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_home_page_api_v1_wechat_channels_fetch_home_page_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """微信视频号主页/WeChat Channels Home Page  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号用户主页信息 - 包含用户发布的视频列表 - 支持分页获取更多视频 - 价格：0.01$/次 ### 参数: - username: 用户名 - last_buffer:     - 分页参数，首次请求可为空，后续使用 `object_list` 最后一个 item 的 `last_buffer` 进行分页请求     - JSON Path: `$.data.object_list[-1].last_buffer` ### 返回: - 用户主页信息和视频列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取翻页参数 `last_buffer`: `$.data.object_list[-1].last_buffer`     - 获取视频列表: `$.data.object_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.object_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels user homepage information - Including list of videos published by user - Support pagination for more videos - Price: $0.01 per request ### Parameters: - username: Username - last_buffer:     - Pagination parameter, can be empty for first request     - For subsequent requests, use the `last_buffer` of the last item in `object_list`     - JSON Path: `$.data.object_list[-1].last_buffer` ### Return: - User homepage information and video list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the pagination parameter `last_buffer`: `$.data.object_list[-1].last_buffer`     - To get the video list: `$.data.object_list[*]`     - To get the video CDN link (without Token): `$.data.object_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_page_api_v1_wechat_channels_fetch_home_page_get_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :param object last_buffer: 分页参数/Pagination parameter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'last_buffer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_home_page_api_v1_wechat_channels_fetch_home_page_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_home_page_api_v1_wechat_channels_fetch_home_page_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'last_buffer' in params:
            query_params.append(('last_buffer', params['last_buffer']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/wechat_channels/fetch_home_page', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get(self, **kwargs):  # noqa: E501
        """微信视频号热门话题/WeChat Channels Hot Topics  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号当前热门话题 - 可用于发现热门内容和趋势 - 价格：0.01$/次 ### 参数: - 无需额外参数 ### 返回: - 热门话题列表  # [English] ### Purpose: - Get current hot topics in WeChat Channels - Can be used to discover popular content and trends - Price: $0.01 per request ### Parameters: - No additional parameters required ### Return: - Hot topic list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get_with_http_info(self, **kwargs):  # noqa: E501
        """微信视频号热门话题/WeChat Channels Hot Topics  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号当前热门话题 - 可用于发现热门内容和趋势 - 价格：0.01$/次 ### 参数: - 无需额外参数 ### 返回: - 热门话题列表  # [English] ### Purpose: - Get current hot topics in WeChat Channels - Can be used to discover popular content and trends - Price: $0.01 per request ### Parameters: - No additional parameters required ### Return: - Hot topic list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get" % key
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
            '/api/v1/wechat_channels/fetch_hot_words', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_live_history_api_v1_wechat_channels_fetch_live_history_get(self, username, **kwargs):  # noqa: E501
        """微信视频号直播回放/WeChat Channels Live History  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号用户的直播回放列表 - 价格：0.01$/次 ### 参数: - username: 用户名 ### 返回: - 直播回放列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取直播回放列表: `$.data.live_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.live_list[*].media.url`     - 获取视频 CDN 链接的 Token: `$.data.live_list[*].media.url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.live_list[*].media.url + $.data.live_list[*].media.url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.live_list[*].media.decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels user's live replay list - Price: $0.01 per request ### Parameters: - username: Username ### Return: - Live replay list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the live replay list: `$.data.live_list[*]`     - To get the video CDN link (without Token): `$.data.live_list[*].media.url`     - To get the Token for the video CDN link: `$.data.live_list[*].media.url_token`     - How to concatenate the complete URL of the video CDN: `$.data.live_list[*].media.url + $.data.live_list[*].media.url_token`     - To get the video decryption key (different for each request): `$.data.live_list[*].media.decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_history_api_v1_wechat_channels_fetch_live_history_get(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object username: 用户名/Username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_live_history_api_v1_wechat_channels_fetch_live_history_get_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_live_history_api_v1_wechat_channels_fetch_live_history_get_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def fetch_live_history_api_v1_wechat_channels_fetch_live_history_get_with_http_info(self, username, **kwargs):  # noqa: E501
        """微信视频号直播回放/WeChat Channels Live History  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号用户的直播回放列表 - 价格：0.01$/次 ### 参数: - username: 用户名 ### 返回: - 直播回放列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取直播回放列表: `$.data.live_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.live_list[*].media.url`     - 获取视频 CDN 链接的 Token: `$.data.live_list[*].media.url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.live_list[*].media.url + $.data.live_list[*].media.url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.live_list[*].media.decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels user's live replay list - Price: $0.01 per request ### Parameters: - username: Username ### Return: - Live replay list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the live replay list: `$.data.live_list[*]`     - To get the video CDN link (without Token): `$.data.live_list[*].media.url`     - To get the Token for the video CDN link: `$.data.live_list[*].media.url_token`     - How to concatenate the complete URL of the video CDN: `$.data.live_list[*].media.url + $.data.live_list[*].media.url_token`     - To get the video decryption key (different for each request): `$.data.live_list[*].media.decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_live_history_api_v1_wechat_channels_fetch_live_history_get_with_http_info(username, async_req=True)
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
                    " to method fetch_live_history_api_v1_wechat_channels_fetch_live_history_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `fetch_live_history_api_v1_wechat_channels_fetch_live_history_get`")  # noqa: E501

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
            '/api/v1/wechat_channels/fetch_live_history', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get(self, keywords, **kwargs):  # noqa: E501
        """微信视频号搜索最新视频/WeChat Channels Search Latest Videos  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号最新视频搜索结果 - 按时间倒序排列 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 ### 返回: - 最新视频搜索结果列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取视频列表: `$.data.object_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.object_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels latest video search results - Sorted by time in descending order - Price: $0.01 per request ### Parameters: - keywords: Search keywords ### Return: - Latest video search result list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the video list: `$.data.object_list[*]`     - To get the video CDN link (without Token): `$.data.object_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get(keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keywords: 搜索关键词/Search keywords (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get_with_http_info(keywords, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get_with_http_info(keywords, **kwargs)  # noqa: E501
            return data

    def fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get_with_http_info(self, keywords, **kwargs):  # noqa: E501
        """微信视频号搜索最新视频/WeChat Channels Search Latest Videos  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号最新视频搜索结果 - 按时间倒序排列 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 ### 返回: - 最新视频搜索结果列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取视频列表: `$.data.object_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.object_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels latest video search results - Sorted by time in descending order - Price: $0.01 per request ### Parameters: - keywords: Search keywords ### Return: - Latest video search result list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the video list: `$.data.object_list[*]`     - To get the video CDN link (without Token): `$.data.object_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get_with_http_info(keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keywords: 搜索关键词/Search keywords (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keywords']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keywords' is set
        if self.api_client.client_side_validation and ('keywords' not in params or
                                                       params['keywords'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keywords` when calling `fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/wechat_channels/fetch_search_latest', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get(self, keywords, **kwargs):  # noqa: E501
        """微信视频号综合搜索/WeChat Channels Comprehensive Search  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号综合搜索结果 - 按相关性排序 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 ### 返回: - 综合搜索结果列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取视频列表: `$.data.object_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.object_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels comprehensive search results - Sorted by relevance - Price: $0.01 per request ### Parameters: - keywords: Search keywords ### Return: - Comprehensive search result list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the video list: `$.data.object_list[*]`     - To get the video CDN link (without Token): `$.data.object_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get(keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keywords: 搜索关键词/Search keywords (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get_with_http_info(keywords, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get_with_http_info(keywords, **kwargs)  # noqa: E501
            return data

    def fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get_with_http_info(self, keywords, **kwargs):  # noqa: E501
        """微信视频号综合搜索/WeChat Channels Comprehensive Search  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号综合搜索结果 - 按相关性排序 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 ### 返回: - 综合搜索结果列表  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取视频列表: `$.data.object_list[*]`     - 获取视频 CDN 链接（不带Token）: `$.data.object_list[*].object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_list[*].object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_list[*].object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels comprehensive search results - Sorted by relevance - Price: $0.01 per request ### Parameters: - keywords: Search keywords ### Return: - Comprehensive search result list ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the video list: `$.data.object_list[*]`     - To get the video CDN link (without Token): `$.data.object_list[*].object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_list[*].object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_list[*].object_desc.media[0].url + $.data.object_list[*].object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_list[*].object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get_with_http_info(keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keywords: 搜索关键词/Search keywords (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keywords']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keywords' is set
        if self.api_client.client_side_validation and ('keywords' not in params or
                                                       params['keywords'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keywords` when calling `fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/wechat_channels/fetch_search_ordinary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_search_api_v1_wechat_channels_fetch_user_search_get(self, keywords, **kwargs):  # noqa: E501
        """微信视频号用户搜索/WeChat Channels User Search  # noqa: E501

        # [中文] ### 用途: - 搜索微信视频号用户 - 按关键词查找相关用户 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 - page: 页码，从1开始 ### 返回: - 用户搜索结果列表  # [English] ### Purpose: - Search WeChat Channels users - Find related users by keywords - Price: $0.01 per request ### Parameters: - keywords: Search keywords - page: Page number, starting from 1 ### Return: - User search result list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_api_v1_wechat_channels_fetch_user_search_get(keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keywords: 搜索关键词/Search keywords (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_search_api_v1_wechat_channels_fetch_user_search_get_with_http_info(keywords, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_search_api_v1_wechat_channels_fetch_user_search_get_with_http_info(keywords, **kwargs)  # noqa: E501
            return data

    def fetch_user_search_api_v1_wechat_channels_fetch_user_search_get_with_http_info(self, keywords, **kwargs):  # noqa: E501
        """微信视频号用户搜索/WeChat Channels User Search  # noqa: E501

        # [中文] ### 用途: - 搜索微信视频号用户 - 按关键词查找相关用户 - 价格：0.01$/次 ### 参数: - keywords: 搜索关键词 - page: 页码，从1开始 ### 返回: - 用户搜索结果列表  # [English] ### Purpose: - Search WeChat Channels users - Find related users by keywords - Price: $0.01 per request ### Parameters: - keywords: Search keywords - page: Page number, starting from 1 ### Return: - User search result list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_api_v1_wechat_channels_fetch_user_search_get_with_http_info(keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keywords: 搜索关键词/Search keywords (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keywords', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_search_api_v1_wechat_channels_fetch_user_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keywords' is set
        if self.api_client.client_side_validation and ('keywords' not in params or
                                                       params['keywords'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keywords` when calling `fetch_user_search_api_v1_wechat_channels_fetch_user_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/wechat_channels/fetch_user_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get(self, **kwargs):  # noqa: E501
        """微信视频号视频详情/WeChat Channels Video Detail  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号视频详细信息 - 可通过视频ID或导出ID获取 - 价格：0.01$/次 ### 参数: - id: 视频ID（二选一） - exportId: 导出ID（会过期，二选一，使用时可不传id） ### 返回: - 视频详细信息  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取视频 CDN 链接（不带Token）: `$.data.object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_desc.media[0].url + $.data.object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels video detailed information - Can be obtained through video ID or export ID - Price: $0.01 per request ### Parameters: - id: Video ID (choose one) - exportId: Export ID (may expire, choose one, can be used without id) ### Return: - Video detailed information ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the video CDN link (without Token): `$.data.object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_desc.media[0].url + $.data.object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 视频ID/Video ID
        :param object export_id: 导出ID会过期，优先用视频ID，使用时可不传id/Export ID may expire, prefer to use Video ID, can be used without id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get_with_http_info(self, **kwargs):  # noqa: E501
        """微信视频号视频详情/WeChat Channels Video Detail  # noqa: E501

        # [中文] ### 用途: - 获取微信视频号视频详细信息 - 可通过视频ID或导出ID获取 - 价格：0.01$/次 ### 参数: - id: 视频ID（二选一） - exportId: 导出ID（会过期，二选一，使用时可不传id） ### 返回: - 视频详细信息  ### 重要提示: - 如果你访问响应返回的 `url` 字段，可能会发现无法正确打开视频页面，这是因为微信对视频号页面做了防盗链处理。 - 解决方法是将 `url` 字段和 `url_token` 字段拼接成一个完整的 URL，然后在浏览器中打开。（注明：可以打开的意思是HTTP响应代码200，不代表视频能正常播放，因为视频文件是加密的） - 使用上面拼接好的链接通过任意 HTTP 客户端下载视频文件，下载后如果发现 MP4 文件无法正常播放，说明该视频文件是加密的。 请使用接口返回的 `decode_key` 字段和加密视频文件，通过下面的工具进行解密。 - ⚠️ **视频文件加密说明**: 如果下载的 MP4 文件无法正常播放，说明该视频文件是加密的。请使用接口返回的 `decode_key` 字段和加密视频文件，通过此工具进行解密：https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **重要**: 微信接口每次请求都会返回新的加密文件链接和 `decode_key`，即使是同一个视频。请确保使用的 `decode_key` 与下载的加密视频文件是同一次 API 响应中获取的，否则解密将会失败。 - JSON Path 和相关说明:     - 获取视频 CDN 链接（不带Token）: `$.data.object_desc.media[0].url`     - 获取视频 CDN 链接的 Token: `$.data.object_desc.media[0].url_token`     - 拼接视频 CDN 的完整 URL 方式: `$.data.object_desc.media[0].url + $.data.object_desc.media[0].url_token`     - 获取视频解密密钥（每次请求都不一样）: `$.data.object_desc.media[0].decode_key`     - 在线解密工具: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - 可自行部署的解密 API（Docker一键部署）：https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # [English] ### Purpose: - Get WeChat Channels video detailed information - Can be obtained through video ID or export ID - Price: $0.01 per request ### Parameters: - id: Video ID (choose one) - exportId: Export ID (may expire, choose one, can be used without id) ### Return: - Video detailed information ### Important Note: - If you try to access the `url` field in the response, you may find that the video page cannot be opened correctly. This is because WeChat has implemented anti-hotlinking protection for video pages. - The solution is to concatenate the `url` field and the `url_token` field into a complete URL, and then open it in a browser. (Note: \"can be opened\" means HTTP response code 200, does not mean the video can be played normally, as the video file is encrypted) - Use the concatenated link above to download the video file through any HTTP client. If you find that the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using the tool below. - ⚠️ **Video Encryption Notice**: If the downloaded MP4 file cannot be played normally, it means the video file is encrypted. Please use the `decode_key` field returned by the API along with the encrypted video file, and decrypt it using this tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/ - ⚠️ **Important**: WeChat API returns a new encrypted file link and `decode_key` with each request, even for the same video. Please ensure that the `decode_key` used matches the encrypted video file obtained from the same API response, otherwise decryption will fail. - JSON Path and related instructions:     - To get the video CDN link (without Token): `$.data.object_desc.media[0].url`     - To get the Token for the video CDN link: `$.data.object_desc.media[0].url_token`     - How to concatenate the complete URL of the video CDN: `$.data.object_desc.media[0].url + $.data.object_desc.media[0].url_token`     - To get the video decryption key (different for each request): `$.data.object_desc.media[0].decode_key`     - Online decryption tool: https://evil0ctal.github.io/WeChat-Channels-Video-File-Decryption/     - Self-deployable decryption API (one-click Docker deployment): https://github.com/Evil0ctal/WeChat-Channels-Video-File-Decryption  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 视频ID/Video ID
        :param object export_id: 导出ID会过期，优先用视频ID，使用时可不传id/Export ID may expire, prefer to use Video ID, can be used without id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'export_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'export_id' in params:
            query_params.append(('exportId', params['export_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/wechat_channels/fetch_video_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
