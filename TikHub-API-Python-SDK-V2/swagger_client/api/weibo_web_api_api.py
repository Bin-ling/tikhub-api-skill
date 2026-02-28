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


class WeiboWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get(self, **kwargs):  # noqa: E501
        """根据频道名称获取热门内容/Get channel feed by name  # noqa: E501

        # [中文] ### 用途: - 根据频道名称获取热门内容（便捷接口） ### 参数: - channel_name: 频道名称，如 \"热门\"、\"榜单\"、\"社会\" 等，不传则使用默认频道 - page: 页码，默认1 ### 返回: - 热门微博列表 ### 说明: - 此接口会自动调用 fetch_config_list 获取频道配置，然后获取对应频道的热门内容 - 如果指定的频道名称不存在，会返回错误信息 - 可用频道：热门、榜单、同城、社会、科技、明星、电影、音乐、数码、汽车、游戏  # [English] ### Purpose: - Get trending content by channel name (convenience endpoint) ### Parameters: - channel_name: Channel name, such as \"热门\", \"榜单\", \"社会\", etc. Use default if not provided - page: Page number, default 1 ### Return: - Trending Weibo list ### Note: - This endpoint will automatically call fetch_config_list to get channel config, then fetch trending content - Returns error if the specified channel name does not exist - Available channels: 热门, 榜单, 同城, 社会, 科技, 明星, 电影, 音乐, 数码, 汽车, 游戏  # [示例/Example] channel_name = \"热门\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_name: 频道名称，不传则使用默认频道/Channel name, use default if not provided
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get_with_http_info(self, **kwargs):  # noqa: E501
        """根据频道名称获取热门内容/Get channel feed by name  # noqa: E501

        # [中文] ### 用途: - 根据频道名称获取热门内容（便捷接口） ### 参数: - channel_name: 频道名称，如 \"热门\"、\"榜单\"、\"社会\" 等，不传则使用默认频道 - page: 页码，默认1 ### 返回: - 热门微博列表 ### 说明: - 此接口会自动调用 fetch_config_list 获取频道配置，然后获取对应频道的热门内容 - 如果指定的频道名称不存在，会返回错误信息 - 可用频道：热门、榜单、同城、社会、科技、明星、电影、音乐、数码、汽车、游戏  # [English] ### Purpose: - Get trending content by channel name (convenience endpoint) ### Parameters: - channel_name: Channel name, such as \"热门\", \"榜单\", \"社会\", etc. Use default if not provided - page: Page number, default 1 ### Return: - Trending Weibo list ### Note: - This endpoint will automatically call fetch_config_list to get channel config, then fetch trending content - Returns error if the specified channel name does not exist - Available channels: 热门, 榜单, 同城, 社会, 科技, 明星, 电影, 音乐, 数码, 汽车, 游戏  # [示例/Example] channel_name = \"热门\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_name: 频道名称，不传则使用默认频道/Channel name, use default if not provided
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_name', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_name' in params:
            query_params.append(('channel_name', params['channel_name']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web/fetch_channel_feed', 'GET',
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

    def fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get(self, cid, **kwargs):  # noqa: E501
        """获取评论子评论/Get comment replies  # noqa: E501

        # [中文] ### 用途: - 获取评论的子评论（回复） ### 参数: - cid: 根评论ID（从 fetch_post_comments 返回的评论中获取） - max_id: 翻页用的ID，默认0为第一页，从上一页返回结果中获取下一页的max_id ### 返回: - 子评论列表  # [English] ### Purpose: - Get comment replies (sub-comments) ### Parameters: - cid: Root comment ID (from fetch_post_comments response) - max_id: Pagination ID, default 0 for first page, get next page max_id from previous response ### Return: - Sub-comments list  # [示例/Example] cid = \"5100663573318494\" max_id = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cid: 根评论ID/Root comment ID (required)
        :param object max_id: 翻页ID，默认0为第一页/Pagination ID, default 0 for first page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get_with_http_info(cid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get_with_http_info(cid, **kwargs)  # noqa: E501
            return data

    def fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get_with_http_info(self, cid, **kwargs):  # noqa: E501
        """获取评论子评论/Get comment replies  # noqa: E501

        # [中文] ### 用途: - 获取评论的子评论（回复） ### 参数: - cid: 根评论ID（从 fetch_post_comments 返回的评论中获取） - max_id: 翻页用的ID，默认0为第一页，从上一页返回结果中获取下一页的max_id ### 返回: - 子评论列表  # [English] ### Purpose: - Get comment replies (sub-comments) ### Parameters: - cid: Root comment ID (from fetch_post_comments response) - max_id: Pagination ID, default 0 for first page, get next page max_id from previous response ### Return: - Sub-comments list  # [示例/Example] cid = \"5100663573318494\" max_id = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get_with_http_info(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cid: 根评论ID/Root comment ID (required)
        :param object max_id: 翻页ID，默认0为第一页/Pagination ID, default 0 for first page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cid' is set
        if self.api_client.client_side_validation and ('cid' not in params or
                                                       params['cid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cid` when calling `fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cid' in params:
            query_params.append(('cid', params['cid']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web/fetch_comment_replies', 'GET',
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

    def fetch_config_list_api_v1_weibo_web_fetch_config_list_get(self, **kwargs):  # noqa: E501
        """获取频道配置列表/Get channel config list  # noqa: E501

        # [中文] ### 用途: - 获取微博移动端所有频道的配置信息 ### 返回: - 频道列表，包含频道名称和 containerid ### 说明: - 返回的 containerid 可用于 fetch_trend_top 接口获取对应频道的热门内容  # [English] ### Purpose: - Get all channel configuration information from Weibo mobile ### Return: - Channel list, including channel name and containerid ### Note: - The returned containerid can be used in fetch_trend_top endpoint to get trending content of the corresponding channel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_config_list_api_v1_weibo_web_fetch_config_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_config_list_api_v1_weibo_web_fetch_config_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_config_list_api_v1_weibo_web_fetch_config_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_config_list_api_v1_weibo_web_fetch_config_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取频道配置列表/Get channel config list  # noqa: E501

        # [中文] ### 用途: - 获取微博移动端所有频道的配置信息 ### 返回: - 频道列表，包含频道名称和 containerid ### 说明: - 返回的 containerid 可用于 fetch_trend_top 接口获取对应频道的热门内容  # [English] ### Purpose: - Get all channel configuration information from Weibo mobile ### Return: - Channel list, including channel name and containerid ### Note: - The returned containerid can be used in fetch_trend_top endpoint to get trending content of the corresponding channel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_config_list_api_v1_weibo_web_fetch_config_list_get_with_http_info(async_req=True)
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
                    " to method fetch_config_list_api_v1_weibo_web_fetch_config_list_get" % key
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
            '/api/v1/weibo/web/fetch_config_list', 'GET',
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

    def fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get(self, **kwargs):  # noqa: E501
        """获取热搜榜/Get hot search ranking  # noqa: E501

        # [中文] ### 用途: - 获取微博实时热搜榜（Top 50）和实时上升热点 ### 返回: - 热搜榜列表，包含：     - **实时热搜榜**: 当前最热门的50个话题，按热度排序     - **实时上升热点**: 正在快速上升的热门话题 ### 说明: - 这是微博官方热搜榜数据 - 每个热搜包含：排名、话题名、热度值、标签（如：新、热、沸）等 - 与 `fetch_search_topics` 不同，此接口返回的是完整的热搜排行榜  # [English] ### Purpose: - Get Weibo real-time hot search ranking (Top 50) and rising trends ### Return: - Hot search list, including:     - **Real-time Hot Search**: Top 50 hottest topics, sorted by popularity     - **Rising Trends**: Topics that are rapidly gaining attention ### Note: - This is official Weibo hot search data - Each entry includes: rank, topic name, heat value, tags (new, hot, trending), etc. - Different from `fetch_search_topics`, this returns the complete hot search ranking  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取热搜榜/Get hot search ranking  # noqa: E501

        # [中文] ### 用途: - 获取微博实时热搜榜（Top 50）和实时上升热点 ### 返回: - 热搜榜列表，包含：     - **实时热搜榜**: 当前最热门的50个话题，按热度排序     - **实时上升热点**: 正在快速上升的热门话题 ### 说明: - 这是微博官方热搜榜数据 - 每个热搜包含：排名、话题名、热度值、标签（如：新、热、沸）等 - 与 `fetch_search_topics` 不同，此接口返回的是完整的热搜排行榜  # [English] ### Purpose: - Get Weibo real-time hot search ranking (Top 50) and rising trends ### Return: - Hot search list, including:     - **Real-time Hot Search**: Top 50 hottest topics, sorted by popularity     - **Rising Trends**: Topics that are rapidly gaining attention ### Note: - This is official Weibo hot search data - Each entry includes: rank, topic name, heat value, tags (new, hot, trending), etc. - Different from `fetch_search_topics`, this returns the complete hot search ranking  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get" % key
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
            '/api/v1/weibo/web/fetch_hot_search', 'GET',
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

    def fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get(self, post_id, mid, **kwargs):  # noqa: E501
        """获取微博评论/Get post comments  # noqa: E501

        # [中文] ### 用途: - 获取微博的评论列表（热门评论流） ### 参数: - post_id: 微博ID - mid: 微博MID - max_id: 翻页用的ID，从上一页返回结果中获取 - max_id_type: max_id类型，默认0 ### 返回: - 评论列表  # [English] ### Purpose: - Get Weibo post comments (hot comments flow) ### Parameters: - post_id: Post ID - mid: Post MID - max_id: Pagination ID from previous page result - max_id_type: max_id type, default 0 ### Return: - Comments list  # [示例/Example] post_id = \"5100663548412324\" mid = \"5100663548412324\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get(post_id, mid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 微博ID/Post ID (required)
        :param object mid: 微博MID/Post MID (required)
        :param object max_id: 翻页ID/Pagination ID
        :param object max_id_type: 翻页ID类型/Pagination ID type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get_with_http_info(post_id, mid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get_with_http_info(post_id, mid, **kwargs)  # noqa: E501
            return data

    def fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get_with_http_info(self, post_id, mid, **kwargs):  # noqa: E501
        """获取微博评论/Get post comments  # noqa: E501

        # [中文] ### 用途: - 获取微博的评论列表（热门评论流） ### 参数: - post_id: 微博ID - mid: 微博MID - max_id: 翻页用的ID，从上一页返回结果中获取 - max_id_type: max_id类型，默认0 ### 返回: - 评论列表  # [English] ### Purpose: - Get Weibo post comments (hot comments flow) ### Parameters: - post_id: Post ID - mid: Post MID - max_id: Pagination ID from previous page result - max_id_type: max_id type, default 0 ### Return: - Comments list  # [示例/Example] post_id = \"5100663548412324\" mid = \"5100663548412324\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get_with_http_info(post_id, mid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 微博ID/Post ID (required)
        :param object mid: 微博MID/Post MID (required)
        :param object max_id: 翻页ID/Pagination ID
        :param object max_id_type: 翻页ID类型/Pagination ID type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_id', 'mid', 'max_id', 'max_id_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_id' is set
        if self.api_client.client_side_validation and ('post_id' not in params or
                                                       params['post_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_id` when calling `fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get`")  # noqa: E501
        # verify the required parameter 'mid' is set
        if self.api_client.client_side_validation and ('mid' not in params or
                                                       params['mid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `mid` when calling `fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'post_id' in params:
            query_params.append(('post_id', params['post_id']))  # noqa: E501
        if 'mid' in params:
            query_params.append(('mid', params['mid']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501
        if 'max_id_type' in params:
            query_params.append(('max_id_type', params['max_id_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web/fetch_post_comments', 'GET',
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

    def fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get(self, post_id, **kwargs):  # noqa: E501
        """获取微博详情/Get post detail  # noqa: E501

        # [中文] ### 用途: - 获取单条微博的详情 ### 参数: - post_id: 微博ID ### 返回: - 微博详情  # [English] ### Purpose: - Get single Weibo post detail ### Parameters: - post_id: Post ID ### Return: - Post detail  # [示例/Example] post_id = \"5092682368025584\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 微博ID/Post ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get_with_http_info(post_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get_with_http_info(post_id, **kwargs)  # noqa: E501
            return data

    def fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get_with_http_info(self, post_id, **kwargs):  # noqa: E501
        """获取微博详情/Get post detail  # noqa: E501

        # [中文] ### 用途: - 获取单条微博的详情 ### 参数: - post_id: 微博ID ### 返回: - 微博详情  # [English] ### Purpose: - Get single Weibo post detail ### Parameters: - post_id: Post ID ### Return: - Post detail  # [示例/Example] post_id = \"5092682368025584\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get_with_http_info(post_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object post_id: 微博ID/Post ID (required)
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
                    " to method fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_id' is set
        if self.api_client.client_side_validation and ('post_id' not in params or
                                                       params['post_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `post_id` when calling `fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get`")  # noqa: E501

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
            '/api/v1/weibo/web/fetch_post_detail', 'GET',
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

    def fetch_search_api_v1_weibo_web_fetch_search_get(self, keyword, **kwargs):  # noqa: E501
        """搜索微博/Search Weibo  # noqa: E501

        # [中文] ### 用途: - 搜索微博内容 ### 参数: - **keyword**: 搜索关键词     - 普通搜索: `游戏`、`新闻`     - 话题搜索: `#话题名#`（如 `#大冰建议女生不要找老登#`） - **page**: 页码     - 从 **1** 开始递增: 1, 2, 3, 4...     - 每页约返回 10-20 条结果     - **不是** 1, 10, 20 这种偏移量模式 - **search_type**: 搜索类型     - **1**: 综合（默认，按相关性排序）     - **61**: 实时（按时间排序，最新优先）     - **3**: 用户（搜索用户账号）     - **60**: 热门（按热度排序）     - **64**: 视频（仅视频内容）     - **63**: 图片（仅图片内容）     - **21**: 文章（仅长文章） - **time_scope**: 时间范围筛选     - **null/不传**: 不限时间（默认）     - **hour**: 一小时内     - **day**: 一天内（24小时）     - **week**: 一周内     - **month**: 一个月内 ### 返回: - 搜索结果列表 ### 注意: - 此接口会自动生成游客Cookie，无需登录即可使用 - 如遇到 432 错误，系统会自动重试  # [English] ### Purpose: - Search Weibo content ### Parameters: - **keyword**: Search keyword     - Normal search: `game`, `news`     - Hashtag search: `#topic#` (e.g., `#TopicName#`) - **page**: Page number     - Starts from **1** and increments: 1, 2, 3, 4...     - Returns ~10-20 results per page     - **NOT** offset mode like 1, 10, 20 - **search_type**: Search type     - **1**: Comprehensive (default, sorted by relevance)     - **61**: Real-time (sorted by time, newest first)     - **3**: Users (search user accounts)     - **60**: Hot (sorted by popularity)     - **64**: Video (video content only)     - **63**: Pictures (image content only)     - **21**: Articles (long articles only) - **time_scope**: Time range filter     - **null/empty**: No time limit (default)     - **hour**: Within one hour     - **day**: Within one day (24 hours)     - **week**: Within one week     - **month**: Within one month ### Return: - Search results list ### Note: - This endpoint auto-generates visitor cookies, no login required - Auto-retry on 432 error  # [示例/Example] keyword = \"游戏\" page = 1 search_type = \"1\" time_scope = null  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_api_v1_weibo_web_fetch_search_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词，支持话题搜索如 #话题名#/Search keyword, supports hashtag like #topic# (required)
        :param object page: 页码，从1开始递增(1,2,3...)，每页约10-20条/Page number, starts from 1 (1,2,3...), ~10-20 results per page
        :param object search_type: 搜索类型/Search type: 1=综合, 61=实时, 3=用户, 60=热门, 64=视频, 63=图片, 21=文章
        :param object time_scope: 时间范围/Time scope: hour=一小时内, day=一天内, week=一周内, month=一个月内, null=不限
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_api_v1_weibo_web_fetch_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_api_v1_weibo_web_fetch_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_api_v1_weibo_web_fetch_search_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索微博/Search Weibo  # noqa: E501

        # [中文] ### 用途: - 搜索微博内容 ### 参数: - **keyword**: 搜索关键词     - 普通搜索: `游戏`、`新闻`     - 话题搜索: `#话题名#`（如 `#大冰建议女生不要找老登#`） - **page**: 页码     - 从 **1** 开始递增: 1, 2, 3, 4...     - 每页约返回 10-20 条结果     - **不是** 1, 10, 20 这种偏移量模式 - **search_type**: 搜索类型     - **1**: 综合（默认，按相关性排序）     - **61**: 实时（按时间排序，最新优先）     - **3**: 用户（搜索用户账号）     - **60**: 热门（按热度排序）     - **64**: 视频（仅视频内容）     - **63**: 图片（仅图片内容）     - **21**: 文章（仅长文章） - **time_scope**: 时间范围筛选     - **null/不传**: 不限时间（默认）     - **hour**: 一小时内     - **day**: 一天内（24小时）     - **week**: 一周内     - **month**: 一个月内 ### 返回: - 搜索结果列表 ### 注意: - 此接口会自动生成游客Cookie，无需登录即可使用 - 如遇到 432 错误，系统会自动重试  # [English] ### Purpose: - Search Weibo content ### Parameters: - **keyword**: Search keyword     - Normal search: `game`, `news`     - Hashtag search: `#topic#` (e.g., `#TopicName#`) - **page**: Page number     - Starts from **1** and increments: 1, 2, 3, 4...     - Returns ~10-20 results per page     - **NOT** offset mode like 1, 10, 20 - **search_type**: Search type     - **1**: Comprehensive (default, sorted by relevance)     - **61**: Real-time (sorted by time, newest first)     - **3**: Users (search user accounts)     - **60**: Hot (sorted by popularity)     - **64**: Video (video content only)     - **63**: Pictures (image content only)     - **21**: Articles (long articles only) - **time_scope**: Time range filter     - **null/empty**: No time limit (default)     - **hour**: Within one hour     - **day**: Within one day (24 hours)     - **week**: Within one week     - **month**: Within one month ### Return: - Search results list ### Note: - This endpoint auto-generates visitor cookies, no login required - Auto-retry on 432 error  # [示例/Example] keyword = \"游戏\" page = 1 search_type = \"1\" time_scope = null  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_api_v1_weibo_web_fetch_search_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词，支持话题搜索如 #话题名#/Search keyword, supports hashtag like #topic# (required)
        :param object page: 页码，从1开始递增(1,2,3...)，每页约10-20条/Page number, starts from 1 (1,2,3...), ~10-20 results per page
        :param object search_type: 搜索类型/Search type: 1=综合, 61=实时, 3=用户, 60=热门, 64=视频, 63=图片, 21=文章
        :param object time_scope: 时间范围/Time scope: hour=一小时内, day=一天内, week=一周内, month=一个月内, null=不限
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page', 'search_type', 'time_scope']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_api_v1_weibo_web_fetch_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_api_v1_weibo_web_fetch_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'search_type' in params:
            query_params.append(('search_type', params['search_type']))  # noqa: E501
        if 'time_scope' in params:
            query_params.append(('time_scope', params['time_scope']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web/fetch_search', 'GET',
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

    def fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get(self, **kwargs):  # noqa: E501
        """获取搜索页热搜词/Get search page hot topics  # noqa: E501

        # [中文] ### 用途: - 获取搜索页的热搜词列表（搜索建议/热门话题） ### 返回: - 搜索热词列表 ### 说明: - 这是搜索页面展示的热门搜索词 - 通常用于搜索框下方的热门推荐 - 与 `fetch_hot_search` 不同，此接口返回的是搜索建议词  # [English] ### Purpose: - Get search page hot topics list (search suggestions/trending topics) ### Return: - Search hot topics list ### Note: - These are hot search terms displayed on the search page - Usually used for trending recommendations below the search box - Different from `fetch_hot_search`, this returns search suggestion terms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取搜索页热搜词/Get search page hot topics  # noqa: E501

        # [中文] ### 用途: - 获取搜索页的热搜词列表（搜索建议/热门话题） ### 返回: - 搜索热词列表 ### 说明: - 这是搜索页面展示的热门搜索词 - 通常用于搜索框下方的热门推荐 - 与 `fetch_hot_search` 不同，此接口返回的是搜索建议词  # [English] ### Purpose: - Get search page hot topics list (search suggestions/trending topics) ### Return: - Search hot topics list ### Note: - These are hot search terms displayed on the search page - Usually used for trending recommendations below the search box - Different from `fetch_hot_search`, this returns search suggestion terms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get_with_http_info(async_req=True)
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
                    " to method fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get" % key
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
            '/api/v1/weibo/web/fetch_search_topics', 'GET',
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

    def fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get(self, containerid, **kwargs):  # noqa: E501
        """获取频道热门趋势/Get channel trend top  # noqa: E501

        # [中文] ### 用途: - 获取指定频道的热门趋势内容 ### 参数: - containerid: 频道容器ID，可从 fetch_config_list 接口获取 - page: 页码，默认1 ### 返回: - 热门微博列表 ### 说明: - containerid 示例: 102803_ctg1_8999_-_ctg1_8999_home - 可通过 fetch_config_list 获取所有可用的 containerid  # [English] ### Purpose: - Get trending content of the specified channel ### Parameters: - containerid: Channel container ID, can be obtained from fetch_config_list endpoint - page: Page number, default 1 ### Return: - Trending Weibo list ### Note: - containerid example: 102803_ctg1_8999_-_ctg1_8999_home - You can get all available containerids from fetch_config_list  # [示例/Example] containerid = \"102803_ctg1_8999_-_ctg1_8999_home\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get(containerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object containerid: 频道容器ID/Channel container ID (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get_with_http_info(containerid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get_with_http_info(containerid, **kwargs)  # noqa: E501
            return data

    def fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get_with_http_info(self, containerid, **kwargs):  # noqa: E501
        """获取频道热门趋势/Get channel trend top  # noqa: E501

        # [中文] ### 用途: - 获取指定频道的热门趋势内容 ### 参数: - containerid: 频道容器ID，可从 fetch_config_list 接口获取 - page: 页码，默认1 ### 返回: - 热门微博列表 ### 说明: - containerid 示例: 102803_ctg1_8999_-_ctg1_8999_home - 可通过 fetch_config_list 获取所有可用的 containerid  # [English] ### Purpose: - Get trending content of the specified channel ### Parameters: - containerid: Channel container ID, can be obtained from fetch_config_list endpoint - page: Page number, default 1 ### Return: - Trending Weibo list ### Note: - containerid example: 102803_ctg1_8999_-_ctg1_8999_home - You can get all available containerids from fetch_config_list  # [示例/Example] containerid = \"102803_ctg1_8999_-_ctg1_8999_home\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get_with_http_info(containerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object containerid: 频道容器ID/Channel container ID (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['containerid', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'containerid' is set
        if self.api_client.client_side_validation and ('containerid' not in params or
                                                       params['containerid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `containerid` when calling `fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'containerid' in params:
            query_params.append(('containerid', params['containerid']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web/fetch_trend_top', 'GET',
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

    def fetch_user_info_api_v1_weibo_web_fetch_user_info_get(self, uid, **kwargs):  # noqa: E501
        """获取用户信息/Get user information  # noqa: E501

        # [中文] ### 用途: - 获取微博用户信息 ### 参数: - uid: 用户ID ### 返回: - 用户信息  # [English] ### Purpose: - Get Weibo user information ### Parameters: - uid: User ID ### Return: - User information  # [示例/Example] uid = \"2992978081\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_weibo_web_fetch_user_info_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_weibo_web_fetch_user_info_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_weibo_web_fetch_user_info_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_weibo_web_fetch_user_info_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户信息/Get user information  # noqa: E501

        # [中文] ### 用途: - 获取微博用户信息 ### 参数: - uid: 用户ID ### 返回: - 用户信息  # [English] ### Purpose: - Get Weibo user information ### Parameters: - uid: User ID ### Return: - User information  # [示例/Example] uid = \"2992978081\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_weibo_web_fetch_user_info_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
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
                    " to method fetch_user_info_api_v1_weibo_web_fetch_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_info_api_v1_weibo_web_fetch_user_info_get`")  # noqa: E501

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
            '/api/v1/weibo/web/fetch_user_info', 'GET',
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

    def fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get(self, uid, **kwargs):  # noqa: E501
        """获取用户微博列表/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取微博用户的微博列表 ### 参数: - uid: 用户ID - page: 页码，默认1 - since_id: 翻页用的ID，从上一页返回结果中获取 ### 返回: - 用户微博列表  # [English] ### Purpose: - Get Weibo user's posts list ### Parameters: - uid: User ID - page: Page number, default 1 - since_id: Pagination ID from previous page result ### Return: - User posts list  # [示例/Example] uid = \"7277477906\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :param object page: 页码/Page number
        :param object since_id: 翻页ID，从上一页结果获取/Pagination ID from previous page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户微博列表/Get user posts  # noqa: E501

        # [中文] ### 用途: - 获取微博用户的微博列表 ### 参数: - uid: 用户ID - page: 页码，默认1 - since_id: 翻页用的ID，从上一页返回结果中获取 ### 返回: - 用户微博列表  # [English] ### Purpose: - Get Weibo user's posts list ### Parameters: - uid: User ID - page: Page number, default 1 - since_id: Pagination ID from previous page result ### Return: - User posts list  # [示例/Example] uid = \"7277477906\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :param object page: 页码/Page number
        :param object since_id: 翻页ID，从上一页结果获取/Pagination ID from previous page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'page', 'since_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'since_id' in params:
            query_params.append(('since_id', params['since_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web/fetch_user_posts', 'GET',
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
