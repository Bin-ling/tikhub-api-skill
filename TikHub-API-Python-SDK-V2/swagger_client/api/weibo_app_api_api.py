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


class WeiboAppAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_ai_smart_search_api_v1_weibo_app_fetch_ai_smart_search_get(self, query, **kwargs):  # noqa: E501
        """AI智搜/AI Smart Search  # noqa: E501

        # [中文] ### 用途: - 使用微博AI智搜功能进行搜索，返回AI增强的搜索结果。 ### 参数: - query: 搜索关键词（必填） - page: 页码，从1开始（默认1） ### 返回: - AI智搜结果，包含AI增强的搜索内容 ### 注意: - 此接口为AI增强搜索，返回结果经过AI处理  # [English] ### Purpose: - Use Weibo AI Smart Search to search, return AI-enhanced search results. ### Parameters: - query: Search keyword (required) - page: Page number, starts from 1 (default 1) ### Return: - AI smart search results, including AI-enhanced search content ### Note: - This is AI-enhanced search, results are processed by AI  # [示例/Example] query = \"人工智能\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ai_smart_search_api_v1_weibo_app_fetch_ai_smart_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词 (required)
        :param object page: 页码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_ai_smart_search_api_v1_weibo_app_fetch_ai_smart_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_ai_smart_search_api_v1_weibo_app_fetch_ai_smart_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_ai_smart_search_api_v1_weibo_app_fetch_ai_smart_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """AI智搜/AI Smart Search  # noqa: E501

        # [中文] ### 用途: - 使用微博AI智搜功能进行搜索，返回AI增强的搜索结果。 ### 参数: - query: 搜索关键词（必填） - page: 页码，从1开始（默认1） ### 返回: - AI智搜结果，包含AI增强的搜索内容 ### 注意: - 此接口为AI增强搜索，返回结果经过AI处理  # [English] ### Purpose: - Use Weibo AI Smart Search to search, return AI-enhanced search results. ### Parameters: - query: Search keyword (required) - page: Page number, starts from 1 (default 1) ### Return: - AI smart search results, including AI-enhanced search content ### Note: - This is AI-enhanced search, results are processed by AI  # [示例/Example] query = \"人工智能\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ai_smart_search_api_v1_weibo_app_fetch_ai_smart_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词 (required)
        :param object page: 页码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_ai_smart_search_api_v1_weibo_app_fetch_ai_smart_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_ai_smart_search_api_v1_weibo_app_fetch_ai_smart_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_ai_smart_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_home_recommend_feed_api_v1_weibo_app_fetch_home_recommend_feed_get(self, **kwargs):  # noqa: E501
        """获取首页推荐Feed流/Get home recommend feed  # noqa: E501

        # [中文] ### 用途: - 获取微博首页推荐Feed流。 ### 参数: - page: 页码，首页不传或传空，第二页传\"2\"，依次递增 - count: 每页数量，默认15，最大50 ### 返回: - 首页推荐Feed流数据 ### 注意: - 推荐内容基于热门话题和热点事件  # [English] ### Purpose: - Get the home recommend feed from Weibo. ### Parameters: - page: Page number, don't pass for first page, pass \"2\" for second page, and so on - count: Items per page, default 15, max 50 ### Return: - Home recommend feed data ### Note: - Recommended content based on hot topics and trending events  # [示例/Example] page = None  # First page count = 15  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_recommend_feed_api_v1_weibo_app_fetch_home_recommend_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码，首页不传，第二页传2
        :param object count: 每页数量
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_recommend_feed_api_v1_weibo_app_fetch_home_recommend_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_recommend_feed_api_v1_weibo_app_fetch_home_recommend_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_home_recommend_feed_api_v1_weibo_app_fetch_home_recommend_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取首页推荐Feed流/Get home recommend feed  # noqa: E501

        # [中文] ### 用途: - 获取微博首页推荐Feed流。 ### 参数: - page: 页码，首页不传或传空，第二页传\"2\"，依次递增 - count: 每页数量，默认15，最大50 ### 返回: - 首页推荐Feed流数据 ### 注意: - 推荐内容基于热门话题和热点事件  # [English] ### Purpose: - Get the home recommend feed from Weibo. ### Parameters: - page: Page number, don't pass for first page, pass \"2\" for second page, and so on - count: Items per page, default 15, max 50 ### Return: - Home recommend feed data ### Note: - Recommended content based on hot topics and trending events  # [示例/Example] page = None  # First page count = 15  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_recommend_feed_api_v1_weibo_app_fetch_home_recommend_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码，首页不传，第二页传2
        :param object count: 每页数量
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_home_recommend_feed_api_v1_weibo_app_fetch_home_recommend_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_home_recommend_feed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hot_search_api_v1_weibo_app_fetch_hot_search_get(self, **kwargs):  # noqa: E501
        """获取热搜榜/Get hot search  # noqa: E501

        # [中文] ### 用途: - 获取微博热搜榜，支持多个分类。 ### 参数: - category: 热搜分类     - mineband: 我的热搜     - realtimehot: 实时热搜（默认）     - social: 社会热搜     - fun: 文娱热搜     - technologynav: 科技热搜     - lifenav: 生活热搜     - region: 同城热搜     - sportnav: 体育热搜     - gamenav: ACG热搜 - page: 页码，从1开始（默认1） - count: 每页数量，默认20，最大50 ### 返回: - 热搜榜数据，包含热搜词条、热度等 ### 注意: - 热搜榜实时更新  # [English] ### Purpose: - Get Weibo hot search ranking, supports multiple categories. ### Parameters: - category: Hot search category     - mineband: My hot search     - realtimehot: Realtime hot search (default)     - social: Social hot search     - fun: Entertainment hot search     - technologynav: Technology hot search     - lifenav: Life hot search     - region: Local hot search     - sportnav: Sports hot search     - gamenav: ACG hot search - page: Page number, starts from 1 (default 1) - count: Items per page, default 20, max 50 ### Return: - Hot search ranking data, including search terms, popularity, etc. ### Note: - Hot search ranking updates in real-time  # [示例/Example] category = \"realtimehot\" page = 1 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_api_v1_weibo_app_fetch_hot_search_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category: 热搜分类: mineband=我的, realtimehot=热搜, social=社会, fun=文娱, technologynav=科技, lifenav=生活, region=同城, sportnav=体育, gamenav=ACG
        :param object page: 页码
        :param object count: 每页数量
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_api_v1_weibo_app_fetch_hot_search_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_api_v1_weibo_app_fetch_hot_search_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_api_v1_weibo_app_fetch_hot_search_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热搜榜/Get hot search  # noqa: E501

        # [中文] ### 用途: - 获取微博热搜榜，支持多个分类。 ### 参数: - category: 热搜分类     - mineband: 我的热搜     - realtimehot: 实时热搜（默认）     - social: 社会热搜     - fun: 文娱热搜     - technologynav: 科技热搜     - lifenav: 生活热搜     - region: 同城热搜     - sportnav: 体育热搜     - gamenav: ACG热搜 - page: 页码，从1开始（默认1） - count: 每页数量，默认20，最大50 ### 返回: - 热搜榜数据，包含热搜词条、热度等 ### 注意: - 热搜榜实时更新  # [English] ### Purpose: - Get Weibo hot search ranking, supports multiple categories. ### Parameters: - category: Hot search category     - mineband: My hot search     - realtimehot: Realtime hot search (default)     - social: Social hot search     - fun: Entertainment hot search     - technologynav: Technology hot search     - lifenav: Life hot search     - region: Local hot search     - sportnav: Sports hot search     - gamenav: ACG hot search - page: Page number, starts from 1 (default 1) - count: Items per page, default 20, max 50 ### Return: - Hot search ranking data, including search terms, popularity, etc. ### Note: - Hot search ranking updates in real-time  # [示例/Example] category = \"realtimehot\" page = 1 count = 20  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_api_v1_weibo_app_fetch_hot_search_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object category: 热搜分类: mineband=我的, realtimehot=热搜, social=社会, fun=文娱, technologynav=科技, lifenav=生活, region=同城, sportnav=体育, gamenav=ACG
        :param object page: 页码
        :param object count: 每页数量
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category', 'page', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_search_api_v1_weibo_app_fetch_hot_search_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category' in params:
            query_params.append(('category', params['category']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_hot_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_hot_search_categories_api_v1_weibo_app_fetch_hot_search_categories_get(self, **kwargs):  # noqa: E501
        """获取热搜分类列表/Get hot search categories  # noqa: E501

        # [中文] ### 用途: - 获取微博热搜榜的所有可用分类列表。 ### 参数: - 无 ### 返回: - 热搜分类列表数据，包含各分类名称和标识 ### 注意: - 返回的分类可用于 fetch_hot_search 接口的 category 参数  # [English] ### Purpose: - Get all available hot search category list from Weibo. ### Parameters: - None ### Return: - Hot search category list data, including category names and identifiers ### Note: - Returned categories can be used for category parameter in fetch_hot_search endpoint  # [示例/Example] # No parameters required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_categories_api_v1_weibo_app_fetch_hot_search_categories_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_categories_api_v1_weibo_app_fetch_hot_search_categories_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_categories_api_v1_weibo_app_fetch_hot_search_categories_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_categories_api_v1_weibo_app_fetch_hot_search_categories_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热搜分类列表/Get hot search categories  # noqa: E501

        # [中文] ### 用途: - 获取微博热搜榜的所有可用分类列表。 ### 参数: - 无 ### 返回: - 热搜分类列表数据，包含各分类名称和标识 ### 注意: - 返回的分类可用于 fetch_hot_search 接口的 category 参数  # [English] ### Purpose: - Get all available hot search category list from Weibo. ### Parameters: - None ### Return: - Hot search category list data, including category names and identifiers ### Note: - Returned categories can be used for category parameter in fetch_hot_search endpoint  # [示例/Example] # No parameters required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_categories_api_v1_weibo_app_fetch_hot_search_categories_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_search_categories_api_v1_weibo_app_fetch_hot_search_categories_get" % key
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
            '/api/v1/weibo/app/fetch_hot_search_categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_search_all_api_v1_weibo_app_fetch_search_all_get(self, query, **kwargs):  # noqa: E501
        """综合搜索/Comprehensive search  # noqa: E501

        # [中文] ### 用途: - 在微博中进行综合搜索，返回相关内容。支持多种搜索类型。 ### 参数: - query: 搜索关键词（必填） - page: 页码，从1开始（默认1） - search_type: 搜索类型     - 1: 综合（默认）     - 61: 实时     - 3: 用户     - 64: 视频     - 63: 图片     - 62: 关注     - 60: 热门     - 21: 全网     - 38: 话题     - 98: 超话     - 92: 地点     - 97: 商品 ### 返回: - 搜索结果列表，包含微博内容、作者信息、图片、视频等 ### 注意: - 搜索结果按相关度排序 - 仅使用 page 参数进行翻页  # [English] ### Purpose: - Comprehensive search in Weibo, return related content. Supports multiple search types. ### Parameters: - query: Search keyword (required) - page: Page number, starts from 1 (default 1) - search_type: Search type     - 1: General/All (default)     - 61: Realtime     - 3: Users     - 64: Videos     - 63: Images     - 62: Following     - 60: Hot     - 21: Whole network     - 38: Topics     - 98: Super topics     - 92: Places/Locations     - 97: Products/Goods ### Return: - Search result list, including post content, author info, images, videos, etc. ### Note: - Search results sorted by relevance - Only use page parameter for pagination  # [示例/Example] query = \"NVIDIA\" page = 1 search_type = 1  # General search # search_type = 3  # Search users # search_type = 64  # Search videos  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_all_api_v1_weibo_app_fetch_search_all_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词 (required)
        :param object page: 页码
        :param object search_type: 搜索类型: 1=综合, 61=实时, 3=用户, 64=视频, 63=图片, 62=关注, 60=热门, 21=全网, 38=话题, 98=超话, 92=地点, 97=商品
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_all_api_v1_weibo_app_fetch_search_all_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_all_api_v1_weibo_app_fetch_search_all_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_search_all_api_v1_weibo_app_fetch_search_all_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """综合搜索/Comprehensive search  # noqa: E501

        # [中文] ### 用途: - 在微博中进行综合搜索，返回相关内容。支持多种搜索类型。 ### 参数: - query: 搜索关键词（必填） - page: 页码，从1开始（默认1） - search_type: 搜索类型     - 1: 综合（默认）     - 61: 实时     - 3: 用户     - 64: 视频     - 63: 图片     - 62: 关注     - 60: 热门     - 21: 全网     - 38: 话题     - 98: 超话     - 92: 地点     - 97: 商品 ### 返回: - 搜索结果列表，包含微博内容、作者信息、图片、视频等 ### 注意: - 搜索结果按相关度排序 - 仅使用 page 参数进行翻页  # [English] ### Purpose: - Comprehensive search in Weibo, return related content. Supports multiple search types. ### Parameters: - query: Search keyword (required) - page: Page number, starts from 1 (default 1) - search_type: Search type     - 1: General/All (default)     - 61: Realtime     - 3: Users     - 64: Videos     - 63: Images     - 62: Following     - 60: Hot     - 21: Whole network     - 38: Topics     - 98: Super topics     - 92: Places/Locations     - 97: Products/Goods ### Return: - Search result list, including post content, author info, images, videos, etc. ### Note: - Search results sorted by relevance - Only use page parameter for pagination  # [示例/Example] query = \"NVIDIA\" page = 1 search_type = 1  # General search # search_type = 3  # Search users # search_type = 64  # Search videos  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_all_api_v1_weibo_app_fetch_search_all_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词 (required)
        :param object page: 页码
        :param object search_type: 搜索类型: 1=综合, 61=实时, 3=用户, 64=视频, 63=图片, 62=关注, 60=热门, 21=全网, 38=话题, 98=超话, 92=地点, 97=商品
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'page', 'search_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_all_api_v1_weibo_app_fetch_search_all_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_search_all_api_v1_weibo_app_fetch_search_all_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'search_type' in params:
            query_params.append(('search_type', params['search_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_search_all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_status_comments_api_v1_weibo_app_fetch_status_comments_get(self, status_id, **kwargs):  # noqa: E501
        """获取微博评论/Get post comments  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的一级评论列表（也适用于视频评论）。 ### 参数: - status_id: 微博ID或视频ID（必填） - max_id: 翻页游标，首次请求不传，后续请求使用返回的max_id值 - sort_type: 评论排序类型     - 0: 按热度排序（默认）     - 1: 按时间排序 ### 返回: - 评论列表数据，包含评论内容、评论者信息、点赞数等 - 包含 max_id 字段用于翻页 ### 注意: - 每次返回约20条评论 - 当没有更多评论时，max_id 为空或相同  # [English] ### Purpose: - Get the first-level comment list of specified post (also works for video comments). ### Parameters: - status_id: Post ID or Video ID (required) - max_id: Pagination cursor, don't pass for first request, use returned max_id for subsequent requests - sort_type: Comment sort type     - 0: Sort by popularity (default)     - 1: Sort by time ### Return: - Comment list data, including comment content, commenter info, likes count, etc. - Contains max_id field for pagination ### Note: - About 20 comments per page - When no more comments, max_id is empty or same  # [示例/Example] status_id = \"5258708168476831\" max_id = None  # First page sort_type = \"0\"  # Sort by popularity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_status_comments_api_v1_weibo_app_fetch_status_comments_get(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object status_id: 微博ID (required)
        :param object max_id: 翻页游标
        :param object sort_type: 排序类型: 0=按热度排序, 1=按时间排序
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_status_comments_api_v1_weibo_app_fetch_status_comments_get_with_http_info(status_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_status_comments_api_v1_weibo_app_fetch_status_comments_get_with_http_info(status_id, **kwargs)  # noqa: E501
            return data

    def fetch_status_comments_api_v1_weibo_app_fetch_status_comments_get_with_http_info(self, status_id, **kwargs):  # noqa: E501
        """获取微博评论/Get post comments  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的一级评论列表（也适用于视频评论）。 ### 参数: - status_id: 微博ID或视频ID（必填） - max_id: 翻页游标，首次请求不传，后续请求使用返回的max_id值 - sort_type: 评论排序类型     - 0: 按热度排序（默认）     - 1: 按时间排序 ### 返回: - 评论列表数据，包含评论内容、评论者信息、点赞数等 - 包含 max_id 字段用于翻页 ### 注意: - 每次返回约20条评论 - 当没有更多评论时，max_id 为空或相同  # [English] ### Purpose: - Get the first-level comment list of specified post (also works for video comments). ### Parameters: - status_id: Post ID or Video ID (required) - max_id: Pagination cursor, don't pass for first request, use returned max_id for subsequent requests - sort_type: Comment sort type     - 0: Sort by popularity (default)     - 1: Sort by time ### Return: - Comment list data, including comment content, commenter info, likes count, etc. - Contains max_id field for pagination ### Note: - About 20 comments per page - When no more comments, max_id is empty or same  # [示例/Example] status_id = \"5258708168476831\" max_id = None  # First page sort_type = \"0\"  # Sort by popularity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_status_comments_api_v1_weibo_app_fetch_status_comments_get_with_http_info(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object status_id: 微博ID (required)
        :param object max_id: 翻页游标
        :param object sort_type: 排序类型: 0=按热度排序, 1=按时间排序
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status_id', 'max_id', 'sort_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_status_comments_api_v1_weibo_app_fetch_status_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status_id' is set
        if self.api_client.client_side_validation and ('status_id' not in params or
                                                       params['status_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `status_id` when calling `fetch_status_comments_api_v1_weibo_app_fetch_status_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status_id' in params:
            query_params.append(('status_id', params['status_id']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_status_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_status_detail_api_v1_weibo_app_fetch_status_detail_get(self, status_id, **kwargs):  # noqa: E501
        """获取微博详情/Get post detail  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的详细信息。 ### 参数: - status_id: 微博ID（必填） ### 返回: - 微博详细数据，包含完整文本、图片、视频、点赞数、评论数、转发数等 ### 注意: - 如果微博已被删除或设置为私密，可能无法获取  # [English] ### Purpose: - Get detailed information of specified post. ### Parameters: - status_id: Post ID (required) ### Return: - Post detailed data, including full text, images, videos, likes, comments, reposts count, etc. ### Note: - May not be available if post has been deleted or set to private  # [示例/Example] status_id = \"5016922058656962\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_status_detail_api_v1_weibo_app_fetch_status_detail_get(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object status_id: 微博ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_status_detail_api_v1_weibo_app_fetch_status_detail_get_with_http_info(status_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_status_detail_api_v1_weibo_app_fetch_status_detail_get_with_http_info(status_id, **kwargs)  # noqa: E501
            return data

    def fetch_status_detail_api_v1_weibo_app_fetch_status_detail_get_with_http_info(self, status_id, **kwargs):  # noqa: E501
        """获取微博详情/Get post detail  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的详细信息。 ### 参数: - status_id: 微博ID（必填） ### 返回: - 微博详细数据，包含完整文本、图片、视频、点赞数、评论数、转发数等 ### 注意: - 如果微博已被删除或设置为私密，可能无法获取  # [English] ### Purpose: - Get detailed information of specified post. ### Parameters: - status_id: Post ID (required) ### Return: - Post detailed data, including full text, images, videos, likes, comments, reposts count, etc. ### Note: - May not be available if post has been deleted or set to private  # [示例/Example] status_id = \"5016922058656962\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_status_detail_api_v1_weibo_app_fetch_status_detail_get_with_http_info(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object status_id: 微博ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_status_detail_api_v1_weibo_app_fetch_status_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status_id' is set
        if self.api_client.client_side_validation and ('status_id' not in params or
                                                       params['status_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `status_id` when calling `fetch_status_detail_api_v1_weibo_app_fetch_status_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status_id' in params:
            query_params.append(('status_id', params['status_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_status_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_status_likes_api_v1_weibo_app_fetch_status_likes_get(self, status_id, **kwargs):  # noqa: E501
        """获取微博点赞列表/Get post likes  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的点赞列表（也适用于视频点赞）。 ### 参数: - status_id: 微博ID或视频ID（必填） - attitude_type: 点赞类型筛选     - 0: 全部（默认）     - 1: 点赞     - 2: 开心     - 3: 惊讶     - 4: 伤心     - 5: 愤怒     - 6: 打赏     - 8: 抱抱 ### 返回: - 点赞列表数据，包含点赞者信息、点赞类型等 ### 注意: - 每次返回约50条点赞记录  # [English] ### Purpose: - Get the like list of specified post (also works for video likes). ### Parameters: - status_id: Post ID or Video ID (required) - attitude_type: Like type filter     - 0: All (default)     - 1: Like     - 2: Happy     - 3: Surprise     - 4: Sad     - 5: Angry     - 6: Reward     - 8: Hug ### Return: - Like list data, including liker info, like type, etc. ### Note: - About 50 likes per page  # [示例/Example] status_id = \"5016922058656962\" attitude_type = \"0\"  # All types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_status_likes_api_v1_weibo_app_fetch_status_likes_get(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object status_id: 微博ID (required)
        :param object attitude_type: 点赞类型: 0=全部, 1=点赞, 2=开心, 3=惊讶, 4=伤心, 5=愤怒, 6=打赏, 8=抱抱
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_status_likes_api_v1_weibo_app_fetch_status_likes_get_with_http_info(status_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_status_likes_api_v1_weibo_app_fetch_status_likes_get_with_http_info(status_id, **kwargs)  # noqa: E501
            return data

    def fetch_status_likes_api_v1_weibo_app_fetch_status_likes_get_with_http_info(self, status_id, **kwargs):  # noqa: E501
        """获取微博点赞列表/Get post likes  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的点赞列表（也适用于视频点赞）。 ### 参数: - status_id: 微博ID或视频ID（必填） - attitude_type: 点赞类型筛选     - 0: 全部（默认）     - 1: 点赞     - 2: 开心     - 3: 惊讶     - 4: 伤心     - 5: 愤怒     - 6: 打赏     - 8: 抱抱 ### 返回: - 点赞列表数据，包含点赞者信息、点赞类型等 ### 注意: - 每次返回约50条点赞记录  # [English] ### Purpose: - Get the like list of specified post (also works for video likes). ### Parameters: - status_id: Post ID or Video ID (required) - attitude_type: Like type filter     - 0: All (default)     - 1: Like     - 2: Happy     - 3: Surprise     - 4: Sad     - 5: Angry     - 6: Reward     - 8: Hug ### Return: - Like list data, including liker info, like type, etc. ### Note: - About 50 likes per page  # [示例/Example] status_id = \"5016922058656962\" attitude_type = \"0\"  # All types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_status_likes_api_v1_weibo_app_fetch_status_likes_get_with_http_info(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object status_id: 微博ID (required)
        :param object attitude_type: 点赞类型: 0=全部, 1=点赞, 2=开心, 3=惊讶, 4=伤心, 5=愤怒, 6=打赏, 8=抱抱
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status_id', 'attitude_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_status_likes_api_v1_weibo_app_fetch_status_likes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status_id' is set
        if self.api_client.client_side_validation and ('status_id' not in params or
                                                       params['status_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `status_id` when calling `fetch_status_likes_api_v1_weibo_app_fetch_status_likes_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status_id' in params:
            query_params.append(('status_id', params['status_id']))  # noqa: E501
        if 'attitude_type' in params:
            query_params.append(('attitude_type', params['attitude_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_status_likes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_status_reposts_api_v1_weibo_app_fetch_status_reposts_get(self, status_id, **kwargs):  # noqa: E501
        """获取微博转发列表/Get post reposts  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的转发列表（也适用于视频转发）。 ### 参数: - status_id: 微博ID或视频ID（必填） - max_id: 翻页游标，首次请求不传，后续请求使用返回的max_id值 ### 返回: - 转发列表数据，包含转发内容、转发者信息等 - 包含 max_id 字段用于翻页 ### 注意: - 每次返回约20条转发 - 当没有更多转发时，max_id 为空或相同  # [English] ### Purpose: - Get the repost list of specified post (also works for video reposts). ### Parameters: - status_id: Post ID or Video ID (required) - max_id: Pagination cursor, don't pass for first request, use returned max_id for subsequent requests ### Return: - Repost list data, including repost content, reposter info, etc. - Contains max_id field for pagination ### Note: - About 20 reposts per page - When no more reposts, max_id is empty or same  # [示例/Example] status_id = \"5016922058656962\" max_id = None  # First page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_status_reposts_api_v1_weibo_app_fetch_status_reposts_get(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object status_id: 微博ID (required)
        :param object max_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_status_reposts_api_v1_weibo_app_fetch_status_reposts_get_with_http_info(status_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_status_reposts_api_v1_weibo_app_fetch_status_reposts_get_with_http_info(status_id, **kwargs)  # noqa: E501
            return data

    def fetch_status_reposts_api_v1_weibo_app_fetch_status_reposts_get_with_http_info(self, status_id, **kwargs):  # noqa: E501
        """获取微博转发列表/Get post reposts  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的转发列表（也适用于视频转发）。 ### 参数: - status_id: 微博ID或视频ID（必填） - max_id: 翻页游标，首次请求不传，后续请求使用返回的max_id值 ### 返回: - 转发列表数据，包含转发内容、转发者信息等 - 包含 max_id 字段用于翻页 ### 注意: - 每次返回约20条转发 - 当没有更多转发时，max_id 为空或相同  # [English] ### Purpose: - Get the repost list of specified post (also works for video reposts). ### Parameters: - status_id: Post ID or Video ID (required) - max_id: Pagination cursor, don't pass for first request, use returned max_id for subsequent requests ### Return: - Repost list data, including repost content, reposter info, etc. - Contains max_id field for pagination ### Note: - About 20 reposts per page - When no more reposts, max_id is empty or same  # [示例/Example] status_id = \"5016922058656962\" max_id = None  # First page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_status_reposts_api_v1_weibo_app_fetch_status_reposts_get_with_http_info(status_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object status_id: 微博ID (required)
        :param object max_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status_id', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_status_reposts_api_v1_weibo_app_fetch_status_reposts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status_id' is set
        if self.api_client.client_side_validation and ('status_id' not in params or
                                                       params['status_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `status_id` when calling `fetch_status_reposts_api_v1_weibo_app_fetch_status_reposts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status_id' in params:
            query_params.append(('status_id', params['status_id']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_status_reposts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_album_api_v1_weibo_app_fetch_user_album_get(self, uid, **kwargs):  # noqa: E501
        """获取用户相册/Get user album  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的相册内容。 ### 参数: - uid: 用户ID（必填） - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值 ### 返回: - 用户相册数据，包含图片列表等信息 ### 注意: - 如果用户设置了隐私保护，可能无法获取相册 - 使用游标翻页（since_id），不使用页码翻页  # [English] ### Purpose: - Get the album content of specified user. ### Parameters: - uid: User ID (required) - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests ### Return: - User album data, including image list, etc. ### Note: - If user has set privacy protection, album may not be available - Uses cursor pagination (since_id), not page numbers  # [示例/Example] uid = \"7648703289\" since_id = None  # First page # since_id = \"5012154263666753_4990205358511630|1034:4990204960768042_20240328_-1\"  # Next page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_album_api_v1_weibo_app_fetch_user_album_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object since_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_album_api_v1_weibo_app_fetch_user_album_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_album_api_v1_weibo_app_fetch_user_album_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_album_api_v1_weibo_app_fetch_user_album_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户相册/Get user album  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的相册内容。 ### 参数: - uid: 用户ID（必填） - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值 ### 返回: - 用户相册数据，包含图片列表等信息 ### 注意: - 如果用户设置了隐私保护，可能无法获取相册 - 使用游标翻页（since_id），不使用页码翻页  # [English] ### Purpose: - Get the album content of specified user. ### Parameters: - uid: User ID (required) - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests ### Return: - User album data, including image list, etc. ### Note: - If user has set privacy protection, album may not be available - Uses cursor pagination (since_id), not page numbers  # [示例/Example] uid = \"7648703289\" since_id = None  # First page # since_id = \"5012154263666753_4990205358511630|1034:4990204960768042_20240328_-1\"  # Next page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_album_api_v1_weibo_app_fetch_user_album_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object since_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'since_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_album_api_v1_weibo_app_fetch_user_album_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_album_api_v1_weibo_app_fetch_user_album_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'since_id' in params:
            query_params.append(('since_id', params['since_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_user_album', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_articles_api_v1_weibo_app_fetch_user_articles_get(self, uid, **kwargs):  # noqa: E501
        """获取用户文章列表/Get user articles  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的文章列表。 ### 参数: - uid: 用户ID（必填） - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值 ### 返回: - 用户文章列表数据 ### 注意: - 如果用户没有发布过文章，返回空列表 - 使用游标翻页（since_id），不使用页码翻页  # [English] ### Purpose: - Get the article list published by specified user. ### Parameters: - uid: User ID (required) - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests ### Return: - User article list data ### Note: - If user has not published any articles, returns empty list - Uses cursor pagination (since_id), not page numbers  # [示例/Example] uid = \"1725941200\" since_id = None  # First page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_articles_api_v1_weibo_app_fetch_user_articles_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object since_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_articles_api_v1_weibo_app_fetch_user_articles_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_articles_api_v1_weibo_app_fetch_user_articles_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_articles_api_v1_weibo_app_fetch_user_articles_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户文章列表/Get user articles  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的文章列表。 ### 参数: - uid: 用户ID（必填） - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值 ### 返回: - 用户文章列表数据 ### 注意: - 如果用户没有发布过文章，返回空列表 - 使用游标翻页（since_id），不使用页码翻页  # [English] ### Purpose: - Get the article list published by specified user. ### Parameters: - uid: User ID (required) - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests ### Return: - User article list data ### Note: - If user has not published any articles, returns empty list - Uses cursor pagination (since_id), not page numbers  # [示例/Example] uid = \"1725941200\" since_id = None  # First page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_articles_api_v1_weibo_app_fetch_user_articles_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object since_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'since_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_articles_api_v1_weibo_app_fetch_user_articles_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_articles_api_v1_weibo_app_fetch_user_articles_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'since_id' in params:
            query_params.append(('since_id', params['since_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_user_articles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_audios_api_v1_weibo_app_fetch_user_audios_get(self, uid, **kwargs):  # noqa: E501
        """获取用户音频列表/Get user audios  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的音频列表。 ### 参数: - uid: 用户ID（必填） - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值 ### 返回: - 用户音频列表数据 ### 注意: - 如果用户没有发布过音频，返回空列表 - 使用游标翻页（since_id），不使用页码翻页  # [English] ### Purpose: - Get the audio list published by specified user. ### Parameters: - uid: User ID (required) - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests ### Return: - User audio list data ### Note: - If user has not published any audios, returns empty list - Uses cursor pagination (since_id), not page numbers  # [示例/Example] uid = \"1725941200\" since_id = None  # First page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_audios_api_v1_weibo_app_fetch_user_audios_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object since_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_audios_api_v1_weibo_app_fetch_user_audios_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_audios_api_v1_weibo_app_fetch_user_audios_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_audios_api_v1_weibo_app_fetch_user_audios_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户音频列表/Get user audios  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的音频列表。 ### 参数: - uid: 用户ID（必填） - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值 ### 返回: - 用户音频列表数据 ### 注意: - 如果用户没有发布过音频，返回空列表 - 使用游标翻页（since_id），不使用页码翻页  # [English] ### Purpose: - Get the audio list published by specified user. ### Parameters: - uid: User ID (required) - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests ### Return: - User audio list data ### Note: - If user has not published any audios, returns empty list - Uses cursor pagination (since_id), not page numbers  # [示例/Example] uid = \"1725941200\" since_id = None  # First page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_audios_api_v1_weibo_app_fetch_user_audios_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object since_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'since_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_audios_api_v1_weibo_app_fetch_user_audios_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_audios_api_v1_weibo_app_fetch_user_audios_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'since_id' in params:
            query_params.append(('since_id', params['since_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_user_audios', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_api_v1_weibo_app_fetch_user_info_get(self, uid, **kwargs):  # noqa: E501
        """获取用户信息/Get user information  # noqa: E501

        # [中文] ### 用途: - 获取微博用户的基本信息，包括昵称、头像、简介、关注数、粉丝数等。 ### 参数: - uid: 用户ID（必填） ### 返回: - 用户基本信息数据 ### 注意: - 如果用户设置了隐私保护，部分信息可能无法获取  # [English] ### Purpose: - Get basic information of Weibo users, including nickname, avatar, bio, following count, followers count, etc. ### Parameters: - uid: User ID (required) ### Return: - User basic information data ### Note: - Some information may not be available if user has set privacy protection  # [示例/Example] uid = \"7648703289\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_weibo_app_fetch_user_info_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_weibo_app_fetch_user_info_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_weibo_app_fetch_user_info_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_weibo_app_fetch_user_info_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户信息/Get user information  # noqa: E501

        # [中文] ### 用途: - 获取微博用户的基本信息，包括昵称、头像、简介、关注数、粉丝数等。 ### 参数: - uid: 用户ID（必填） ### 返回: - 用户基本信息数据 ### 注意: - 如果用户设置了隐私保护，部分信息可能无法获取  # [English] ### Purpose: - Get basic information of Weibo users, including nickname, avatar, bio, following count, followers count, etc. ### Parameters: - uid: User ID (required) ### Return: - User basic information data ### Note: - Some information may not be available if user has set privacy protection  # [示例/Example] uid = \"7648703289\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_weibo_app_fetch_user_info_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
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
                    " to method fetch_user_info_api_v1_weibo_app_fetch_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_info_api_v1_weibo_app_fetch_user_info_get`")  # noqa: E501

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
            '/api/v1/weibo/app/fetch_user_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_info_detail_api_v1_weibo_app_fetch_user_info_detail_get(self, uid, **kwargs):  # noqa: E501
        """获取用户详细信息/Get user detail information  # noqa: E501

        # [中文] ### 用途: - 获取微博用户的详细信息，比基本信息更加完整，包括认证信息、标签、等级等。 ### 参数: - uid: 用户ID（必填） ### 返回: - 用户详细信息数据 ### 注意: - 如果用户设置了隐私保护，部分信息可能无法获取  # [English] ### Purpose: - Get detailed information of Weibo users, more complete than basic info, including verification info, tags, level, etc. ### Parameters: - uid: User ID (required) ### Return: - User detailed information data ### Note: - Some information may not be available if user has set privacy protection  # [示例/Example] uid = \"7648703289\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_detail_api_v1_weibo_app_fetch_user_info_detail_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_detail_api_v1_weibo_app_fetch_user_info_detail_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_detail_api_v1_weibo_app_fetch_user_info_detail_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_detail_api_v1_weibo_app_fetch_user_info_detail_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户详细信息/Get user detail information  # noqa: E501

        # [中文] ### 用途: - 获取微博用户的详细信息，比基本信息更加完整，包括认证信息、标签、等级等。 ### 参数: - uid: 用户ID（必填） ### 返回: - 用户详细信息数据 ### 注意: - 如果用户设置了隐私保护，部分信息可能无法获取  # [English] ### Purpose: - Get detailed information of Weibo users, more complete than basic info, including verification info, tags, level, etc. ### Parameters: - uid: User ID (required) ### Return: - User detailed information data ### Note: - Some information may not be available if user has set privacy protection  # [示例/Example] uid = \"7648703289\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_detail_api_v1_weibo_app_fetch_user_info_detail_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
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
                    " to method fetch_user_info_detail_api_v1_weibo_app_fetch_user_info_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_info_detail_api_v1_weibo_app_fetch_user_info_detail_get`")  # noqa: E501

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
            '/api/v1/weibo/app/fetch_user_info_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_profile_feed_api_v1_weibo_app_fetch_user_profile_feed_get(self, uid, **kwargs):  # noqa: E501
        """获取用户主页动态/Get user profile feed  # noqa: E501

        # [中文] ### 用途: - 获取指定用户主页的动态流。 ### 参数: - uid: 用户ID（必填） - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值 ### 返回: - 用户主页动态数据 ### 注意: - 如果用户设置了隐私保护，可能无法获取动态 - 使用游标翻页（since_id），不使用页码翻页  # [English] ### Purpose: - Get the profile feed of specified user. ### Parameters: - uid: User ID (required) - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests ### Return: - User profile feed data ### Note: - If user has set privacy protection, feed may not be available - Uses cursor pagination (since_id), not page numbers  # [示例/Example] uid = \"6580994757\" since_id = None  # First page # since_id = \"2|1769360821762|5258923930289595,,,,,,1768788000,,,,,-1,-1\"  # Next page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_feed_api_v1_weibo_app_fetch_user_profile_feed_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object since_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_profile_feed_api_v1_weibo_app_fetch_user_profile_feed_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_profile_feed_api_v1_weibo_app_fetch_user_profile_feed_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_profile_feed_api_v1_weibo_app_fetch_user_profile_feed_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户主页动态/Get user profile feed  # noqa: E501

        # [中文] ### 用途: - 获取指定用户主页的动态流。 ### 参数: - uid: 用户ID（必填） - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值 ### 返回: - 用户主页动态数据 ### 注意: - 如果用户设置了隐私保护，可能无法获取动态 - 使用游标翻页（since_id），不使用页码翻页  # [English] ### Purpose: - Get the profile feed of specified user. ### Parameters: - uid: User ID (required) - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests ### Return: - User profile feed data ### Note: - If user has set privacy protection, feed may not be available - Uses cursor pagination (since_id), not page numbers  # [示例/Example] uid = \"6580994757\" since_id = None  # First page # since_id = \"2|1769360821762|5258923930289595,,,,,,1768788000,,,,,-1,-1\"  # Next page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_profile_feed_api_v1_weibo_app_fetch_user_profile_feed_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object since_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'since_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_profile_feed_api_v1_weibo_app_fetch_user_profile_feed_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_profile_feed_api_v1_weibo_app_fetch_user_profile_feed_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'since_id' in params:
            query_params.append(('since_id', params['since_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_user_profile_feed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_super_topics_api_v1_weibo_app_fetch_user_super_topics_get(self, uid, **kwargs):  # noqa: E501
        """获取用户参与的超话列表/Get user super topics  # noqa: E501

        # [中文] ### 用途: - 获取指定用户参与的超话列表。 ### 参数: - uid: 用户ID（必填） - page: 页码，从1开始（默认1） ### 返回: - 用户参与的超话列表数据 ### 注意: - 如果用户设置了隐私保护，可能无法获取超话列表  # [English] ### Purpose: - Get the super topics list that user participated in. ### Parameters: - uid: User ID (required) - page: Page number, starts from 1 (default 1) ### Return: - User's super topics list data ### Note: - If user has set privacy protection, super topics list may not be available  # [示例/Example] uid = \"7648703289\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_super_topics_api_v1_weibo_app_fetch_user_super_topics_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object page: 页码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_super_topics_api_v1_weibo_app_fetch_user_super_topics_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_super_topics_api_v1_weibo_app_fetch_user_super_topics_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_super_topics_api_v1_weibo_app_fetch_user_super_topics_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户参与的超话列表/Get user super topics  # noqa: E501

        # [中文] ### 用途: - 获取指定用户参与的超话列表。 ### 参数: - uid: 用户ID（必填） - page: 页码，从1开始（默认1） ### 返回: - 用户参与的超话列表数据 ### 注意: - 如果用户设置了隐私保护，可能无法获取超话列表  # [English] ### Purpose: - Get the super topics list that user participated in. ### Parameters: - uid: User ID (required) - page: Page number, starts from 1 (default 1) ### Return: - User's super topics list data ### Note: - If user has set privacy protection, super topics list may not be available  # [示例/Example] uid = \"7648703289\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_super_topics_api_v1_weibo_app_fetch_user_super_topics_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object page: 页码
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_super_topics_api_v1_weibo_app_fetch_user_super_topics_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_super_topics_api_v1_weibo_app_fetch_user_super_topics_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_user_super_topics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_timeline_api_v1_weibo_app_fetch_user_timeline_get(self, uid, **kwargs):  # noqa: E501
        """获取用户发布的微博/Get user timeline  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的微博列表，支持分页和多种内容筛选。 ### 参数: - uid: 用户ID（必填） - page: 页码，从1开始（默认1） - filter_type: 筛选类型（默认\"all\"）     - all: 全部微博     - original: 原创微博     - likes: 她/他的赞     - video: 视频微博     - pic: 图片微博     - location: 签到足迹     - month: 按时间筛选（需要同时传入month参数） - month: 时间筛选参数，格式YYYYMMDD（仅当filter_type=month时使用） ### 返回: - 微博列表数据，包含微博内容、图片、视频等信息 ### 注意: - 如果用户设置了隐私保护，可能无法获取微博列表 - 每页返回数量约为20条微博 - 使用时间筛选时必须同时指定filter_type=month和month参数  # [English] ### Purpose: - Get the list of posts published by specified user, support pagination and multiple content filters. ### Parameters: - uid: User ID (required) - page: Page number, starts from 1 (default 1) - filter_type: Filter type (default \"all\")     - all: All posts     - original: Original posts     - likes: Liked posts     - video: Video posts     - pic: Picture posts     - location: Location check-in posts     - month: Filter by time (must pass month parameter) - month: Time filter parameter, format YYYYMMDD (only used when filter_type=month) ### Return: - Post list data, including post content, images, videos, etc. ### Note: - If user has set privacy protection, post list may not be available - About 20 posts per page - When using time filter, must specify both filter_type=month and month parameter  # [示例/Example] uid = \"7648703289\" page = 1 filter_type = \"all\" # or filter_type = \"video\" for videos only # or filter_type = \"month\" with month = \"20251010\" for time filter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_timeline_api_v1_weibo_app_fetch_user_timeline_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object page: 页码
        :param object filter_type: 筛选类型
        :param object month: 时间筛选(YYYYMMDD格式)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_timeline_api_v1_weibo_app_fetch_user_timeline_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_timeline_api_v1_weibo_app_fetch_user_timeline_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_timeline_api_v1_weibo_app_fetch_user_timeline_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户发布的微博/Get user timeline  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的微博列表，支持分页和多种内容筛选。 ### 参数: - uid: 用户ID（必填） - page: 页码，从1开始（默认1） - filter_type: 筛选类型（默认\"all\"）     - all: 全部微博     - original: 原创微博     - likes: 她/他的赞     - video: 视频微博     - pic: 图片微博     - location: 签到足迹     - month: 按时间筛选（需要同时传入month参数） - month: 时间筛选参数，格式YYYYMMDD（仅当filter_type=month时使用） ### 返回: - 微博列表数据，包含微博内容、图片、视频等信息 ### 注意: - 如果用户设置了隐私保护，可能无法获取微博列表 - 每页返回数量约为20条微博 - 使用时间筛选时必须同时指定filter_type=month和month参数  # [English] ### Purpose: - Get the list of posts published by specified user, support pagination and multiple content filters. ### Parameters: - uid: User ID (required) - page: Page number, starts from 1 (default 1) - filter_type: Filter type (default \"all\")     - all: All posts     - original: Original posts     - likes: Liked posts     - video: Video posts     - pic: Picture posts     - location: Location check-in posts     - month: Filter by time (must pass month parameter) - month: Time filter parameter, format YYYYMMDD (only used when filter_type=month) ### Return: - Post list data, including post content, images, videos, etc. ### Note: - If user has set privacy protection, post list may not be available - About 20 posts per page - When using time filter, must specify both filter_type=month and month parameter  # [示例/Example] uid = \"7648703289\" page = 1 filter_type = \"all\" # or filter_type = \"video\" for videos only # or filter_type = \"month\" with month = \"20251010\" for time filter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_timeline_api_v1_weibo_app_fetch_user_timeline_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object page: 页码
        :param object filter_type: 筛选类型
        :param object month: 时间筛选(YYYYMMDD格式)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'page', 'filter_type', 'month']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_timeline_api_v1_weibo_app_fetch_user_timeline_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_timeline_api_v1_weibo_app_fetch_user_timeline_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'filter_type' in params:
            query_params.append(('filter_type', params['filter_type']))  # noqa: E501
        if 'month' in params:
            query_params.append(('month', params['month']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_user_timeline', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_user_videos_api_v1_weibo_app_fetch_user_videos_get(self, uid, **kwargs):  # noqa: E501
        """获取用户视频列表/Get user videos  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的视频列表（瀑布流展示）。 ### 参数: - uid: 用户ID（必填） - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值 ### 返回: - 视频列表数据，包含视频标题、封面、播放量等信息 - 包含 moreInfo.params.since_id 字段用于翻页 ### 注意: - 只返回包含视频的微博 - 使用游标翻页（since_id），不使用页码翻页  # [English] ### Purpose: - Get the video list published by specified user (waterfall layout). ### Parameters: - uid: User ID (required) - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests ### Return: - Video list data, including video title, cover, views, etc. - Contains moreInfo.params.since_id field for pagination ### Note: - Only returns posts with videos - Uses cursor pagination (since_id), not page numbers  # [示例/Example] # First page uid = \"7648703289\" since_id = None  # Next page (use since_id from previous response) # since_id = \"4763250669650541\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_videos_api_v1_weibo_app_fetch_user_videos_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object since_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_videos_api_v1_weibo_app_fetch_user_videos_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_videos_api_v1_weibo_app_fetch_user_videos_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_videos_api_v1_weibo_app_fetch_user_videos_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户视频列表/Get user videos  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的视频列表（瀑布流展示）。 ### 参数: - uid: 用户ID（必填） - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值 ### 返回: - 视频列表数据，包含视频标题、封面、播放量等信息 - 包含 moreInfo.params.since_id 字段用于翻页 ### 注意: - 只返回包含视频的微博 - 使用游标翻页（since_id），不使用页码翻页  # [English] ### Purpose: - Get the video list published by specified user (waterfall layout). ### Parameters: - uid: User ID (required) - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests ### Return: - Video list data, including video title, cover, views, etc. - Contains moreInfo.params.since_id field for pagination ### Note: - Only returns posts with videos - Uses cursor pagination (since_id), not page numbers  # [示例/Example] # First page uid = \"7648703289\" since_id = None  # Next page (use since_id from previous response) # since_id = \"4763250669650541\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_videos_api_v1_weibo_app_fetch_user_videos_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID (required)
        :param object since_id: 翻页游标
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'since_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_videos_api_v1_weibo_app_fetch_user_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_videos_api_v1_weibo_app_fetch_user_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'since_id' in params:
            query_params.append(('since_id', params['since_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_user_videos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_video_detail_api_v1_weibo_app_fetch_video_detail_get(self, mid, **kwargs):  # noqa: E501
        """获取视频详情/Get video detail  # noqa: E501

        # [中文] ### 用途: - 获取单个视频的详细信息，包括视频播放地址。 - **重要**: 从微博视频链接（如 https://weibo.com/tv/show/1034:5232127105761312）获取真实视频ID的必需步骤 ### 参数: - mid: 视频微博ID或链接中的ID（必填） ### 返回: - 视频详细数据，包含视频播放地址、封面、时长、标题等 - **items[0].data.idstr**: 真实的视频微博ID，可用于获取评论等操作 ### 注意: - 返回的视频地址可能有时效性 - 支持获取高清视频地址 - **获取评论前必须先调用此接口**: 链接中的ID不能直接用于获取评论，需要先通过此接口获取 items[0].data.idstr 中的真实ID  # [English] ### Purpose: - Get detailed information of single video, including video play URL. - **Important**: Required step to get real video ID from Weibo video link (e.g., https://weibo.com/tv/show/1034:5232127105761312) ### Parameters: - mid: Video post ID or ID from link (required) ### Return: - Video detailed data, including video play URL, cover, duration, title, etc. - **items[0].data.idstr**: Real video post ID, can be used for fetching comments ### Note: - Returned video URL may have expiration time - Support getting HD video URL - **Must call this API before fetching comments**: ID from link cannot be used directly for comments, must get real ID from items[0].data.idstr first  # [示例/Example] mid = \"5242977759006596\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_detail_api_v1_weibo_app_fetch_video_detail_get(mid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mid: 视频微博ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_detail_api_v1_weibo_app_fetch_video_detail_get_with_http_info(mid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_detail_api_v1_weibo_app_fetch_video_detail_get_with_http_info(mid, **kwargs)  # noqa: E501
            return data

    def fetch_video_detail_api_v1_weibo_app_fetch_video_detail_get_with_http_info(self, mid, **kwargs):  # noqa: E501
        """获取视频详情/Get video detail  # noqa: E501

        # [中文] ### 用途: - 获取单个视频的详细信息，包括视频播放地址。 - **重要**: 从微博视频链接（如 https://weibo.com/tv/show/1034:5232127105761312）获取真实视频ID的必需步骤 ### 参数: - mid: 视频微博ID或链接中的ID（必填） ### 返回: - 视频详细数据，包含视频播放地址、封面、时长、标题等 - **items[0].data.idstr**: 真实的视频微博ID，可用于获取评论等操作 ### 注意: - 返回的视频地址可能有时效性 - 支持获取高清视频地址 - **获取评论前必须先调用此接口**: 链接中的ID不能直接用于获取评论，需要先通过此接口获取 items[0].data.idstr 中的真实ID  # [English] ### Purpose: - Get detailed information of single video, including video play URL. - **Important**: Required step to get real video ID from Weibo video link (e.g., https://weibo.com/tv/show/1034:5232127105761312) ### Parameters: - mid: Video post ID or ID from link (required) ### Return: - Video detailed data, including video play URL, cover, duration, title, etc. - **items[0].data.idstr**: Real video post ID, can be used for fetching comments ### Note: - Returned video URL may have expiration time - Support getting HD video URL - **Must call this API before fetching comments**: ID from link cannot be used directly for comments, must get real ID from items[0].data.idstr first  # [示例/Example] mid = \"5242977759006596\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_detail_api_v1_weibo_app_fetch_video_detail_get_with_http_info(mid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object mid: 视频微博ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_detail_api_v1_weibo_app_fetch_video_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mid' is set
        if self.api_client.client_side_validation and ('mid' not in params or
                                                       params['mid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `mid` when calling `fetch_video_detail_api_v1_weibo_app_fetch_video_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mid' in params:
            query_params.append(('mid', params['mid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_video_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_video_featured_feed_api_v1_weibo_app_fetch_video_featured_feed_get(self, **kwargs):  # noqa: E501
        """获取短视频精选Feed流/Get video featured feed  # noqa: E501

        # [中文] ### 用途: - 获取微博短视频精选页的Feed流。 ### 参数: - page: 页码，首页不传或传空，第二页传\"2\"，依次递增 ### 返回: - 短视频精选Feed流数据，包含视频列表等 ### 注意: - 每页返回约20条视频  # [English] ### Purpose: - Get the featured video feed from Weibo video section. ### Parameters: - page: Page number, don't pass for first page, pass \"2\" for second page, and so on ### Return: - Featured video feed data, including video list, etc. ### Note: - About 20 videos per page  # [示例/Example] page = None  # First page # page = \"2\"  # Second page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_featured_feed_api_v1_weibo_app_fetch_video_featured_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码，首页不传，第二页传2
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_featured_feed_api_v1_weibo_app_fetch_video_featured_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_featured_feed_api_v1_weibo_app_fetch_video_featured_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_video_featured_feed_api_v1_weibo_app_fetch_video_featured_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取短视频精选Feed流/Get video featured feed  # noqa: E501

        # [中文] ### 用途: - 获取微博短视频精选页的Feed流。 ### 参数: - page: 页码，首页不传或传空，第二页传\"2\"，依次递增 ### 返回: - 短视频精选Feed流数据，包含视频列表等 ### 注意: - 每页返回约20条视频  # [English] ### Purpose: - Get the featured video feed from Weibo video section. ### Parameters: - page: Page number, don't pass for first page, pass \"2\" for second page, and so on ### Return: - Featured video feed data, including video list, etc. ### Note: - About 20 videos per page  # [示例/Example] page = None  # First page # page = \"2\"  # Second page  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_featured_feed_api_v1_weibo_app_fetch_video_featured_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: 页码，首页不传，第二页传2
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_featured_feed_api_v1_weibo_app_fetch_video_featured_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/app/fetch_video_featured_feed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
