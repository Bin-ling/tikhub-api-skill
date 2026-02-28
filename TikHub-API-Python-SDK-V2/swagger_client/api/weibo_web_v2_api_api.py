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


class WeiboWebV2APIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get(self, id, **kwargs):  # noqa: E501
        """检查微博是否允许带图评论/Check if Weibo allows image comments  # noqa: E501

        # [中文] ### 用途: - 检查指定微博是否允许用户在评论时上传图片。 ### 参数: - id: 微博ID（必填） ### 返回: - result: true表示允许带图评论，false表示不允许 ### 注意: - 不同微博的图片评论权限可能不同  # [English] ### Purpose: - Check if a specific Weibo post allows image comments. ### Parameters: - id: Weibo post ID (required) ### Return: - result: true means image comments allowed, false means not allowed ### Note: - Different posts may have different image comment permissions  # [示例/Example] id = \"5092682368025584\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 微博ID/Weibo ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """检查微博是否允许带图评论/Check if Weibo allows image comments  # noqa: E501

        # [中文] ### 用途: - 检查指定微博是否允许用户在评论时上传图片。 ### 参数: - id: 微博ID（必填） ### 返回: - result: true表示允许带图评论，false表示不允许 ### 注意: - 不同微博的图片评论权限可能不同  # [English] ### Purpose: - Check if a specific Weibo post allows image comments. ### Parameters: - id: Weibo post ID (required) ### Return: - result: true means image comments allowed, false means not allowed ### Note: - Different posts may have different image comment permissions  # [示例/Example] id = \"5092682368025584\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 微博ID/Weibo ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/check_allow_comment_with_pic', 'GET',
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

    def fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get(self, q, **kwargs):  # noqa: E501
        """微博高级搜索/Weibo Advanced Search  # noqa: E501

        # [中文] ### 用途: - 微博高级搜索，支持多维度筛选。 ### 参数: - q: 搜索关键词（必填） - search_type: 搜索类型（all/hot/original/verified/media/viewpoint） - include_type: 包含类型（all/pic/video/music/link） - timescope: 时间范围（格式: custom:开始日期:结束日期，如 custom:2025-09-01-0:2025-09-08-23） - page: 页码（默认1） ### 返回: - 搜索结果列表，包含微博内容、作者信息、图片、视频、互动数据等 ### 注意: - 视频播放需设置请求头 Referer=https://weibo.com/  # [English] ### Purpose: - Weibo advanced search with multi-dimensional filtering. ### Parameters: - q: Search keyword (required) - search_type: Search type (all/hot/original/verified/media/viewpoint) - include_type: Include type (all/pic/video/music/link) - timescope: Time scope (format: custom:start_date:end_date, e.g. custom:2025-09-01-0:2025-09-08-23) - page: Page number (default 1) ### Return: - Search result list, including post content, author info, images, videos, interaction data ### Note: - Video playback requires setting header Referer=https://weibo.com/  # [示例/Example] q = \"python\" search_type = \"hot\" include_type = \"pic\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object q: 搜索关键词/Search keyword (required)
        :param object search_type: 搜索类型/Search type: all(全部), hot(热门), original(原创), verified(认证用户), media(媒体), viewpoint(观点)
        :param object include_type: 包含类型/Include type: all(全部), pic(含图片), video(含视频), music(含音乐), link(含短链)
        :param object timescope: 时间范围/Time scope (custom:start:end)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get_with_http_info(self, q, **kwargs):  # noqa: E501
        """微博高级搜索/Weibo Advanced Search  # noqa: E501

        # [中文] ### 用途: - 微博高级搜索，支持多维度筛选。 ### 参数: - q: 搜索关键词（必填） - search_type: 搜索类型（all/hot/original/verified/media/viewpoint） - include_type: 包含类型（all/pic/video/music/link） - timescope: 时间范围（格式: custom:开始日期:结束日期，如 custom:2025-09-01-0:2025-09-08-23） - page: 页码（默认1） ### 返回: - 搜索结果列表，包含微博内容、作者信息、图片、视频、互动数据等 ### 注意: - 视频播放需设置请求头 Referer=https://weibo.com/  # [English] ### Purpose: - Weibo advanced search with multi-dimensional filtering. ### Parameters: - q: Search keyword (required) - search_type: Search type (all/hot/original/verified/media/viewpoint) - include_type: Include type (all/pic/video/music/link) - timescope: Time scope (format: custom:start_date:end_date, e.g. custom:2025-09-01-0:2025-09-08-23) - page: Page number (default 1) ### Return: - Search result list, including post content, author info, images, videos, interaction data ### Note: - Video playback requires setting header Referer=https://weibo.com/  # [示例/Example] q = \"python\" search_type = \"hot\" include_type = \"pic\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object q: 搜索关键词/Search keyword (required)
        :param object search_type: 搜索类型/Search type: all(全部), hot(热门), original(原创), verified(认证用户), media(媒体), viewpoint(观点)
        :param object include_type: 包含类型/Include type: all(全部), pic(含图片), video(含视频), music(含音乐), link(含短链)
        :param object timescope: 时间范围/Time scope (custom:start:end)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'search_type', 'include_type', 'timescope', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if self.api_client.client_side_validation and ('q' not in params or
                                                       params['q'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `q` when calling `fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'search_type' in params:
            query_params.append(('search_type', params['search_type']))  # noqa: E501
        if 'include_type' in params:
            query_params.append(('include_type', params['include_type']))  # noqa: E501
        if 'timescope' in params:
            query_params.append(('timescope', params['timescope']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_advanced_search', 'GET',
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

    def fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get(self, keyword, **kwargs):  # noqa: E501
        """微博AI搜索内容扩展/Weibo AI Search Content Extension  # noqa: E501

        # [中文] ### 用途: - 获取与关键词相关的内容扩展（相关问题、博主推荐、参考博文等）。 ### 参数: - keyword: 搜索关键词（必填，建议使用话题格式#话题名#） ### 返回: - HTML格式的扩展内容，包含相关问题、博主推荐、参考博文等 ### 注意: - 返回内容为HTML格式，需要进行HTML解析处理 - HTML结构可能会发生变化，需要做好容错处理  # [English] ### Purpose: - Get content extensions related to keyword (related questions, blogger recommendations, reference posts). ### Parameters: - keyword: Search keyword (required, recommend using topic format #TopicName#) ### Return: - HTML format extension content, including related questions, blogger recommendations, reference posts ### Note: - Returned content is in HTML format, requires HTML parsing - HTML structure may change, need proper error handling  # [示例/Example] keyword = \"#微博奇遇记#\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """微博AI搜索内容扩展/Weibo AI Search Content Extension  # noqa: E501

        # [中文] ### 用途: - 获取与关键词相关的内容扩展（相关问题、博主推荐、参考博文等）。 ### 参数: - keyword: 搜索关键词（必填，建议使用话题格式#话题名#） ### 返回: - HTML格式的扩展内容，包含相关问题、博主推荐、参考博文等 ### 注意: - 返回内容为HTML格式，需要进行HTML解析处理 - HTML结构可能会发生变化，需要做好容错处理  # [English] ### Purpose: - Get content extensions related to keyword (related questions, blogger recommendations, reference posts). ### Parameters: - keyword: Search keyword (required, recommend using topic format #TopicName#) ### Return: - HTML format extension content, including related questions, blogger recommendations, reference posts ### Note: - Returned content is in HTML format, requires HTML parsing - HTML structure may change, need proper error handling  # [示例/Example] keyword = \"#微博奇遇记#\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get_with_http_info(keyword, async_req=True)
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
                    " to method fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_ai_related_search', 'GET',
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

    def fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get(self, query, **kwargs):  # noqa: E501
        """微博智能搜索/Weibo AI Search  # noqa: E501

        # [中文] ### 用途: - 通过微博AI智能搜索获取搜索结果。 ### 参数: - query: 搜索关键词（必填，建议使用话题格式#话题名#） ### 返回: - AI搜索结果，包含推荐内容、相关话题等 ### 注意: - AI搜索结果会根据用户行为进行个性化调整  # [English] ### Purpose: - Get search results through Weibo AI intelligent search. ### Parameters: - query: Search keyword (required, recommend using topic format #TopicName#) ### Return: - AI search results, including recommended content, related topics ### Note: - AI search results are personalized based on user behavior  # [示例/Example] query = \"#法国#\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """微博智能搜索/Weibo AI Search  # noqa: E501

        # [中文] ### 用途: - 通过微博AI智能搜索获取搜索结果。 ### 参数: - query: 搜索关键词（必填，建议使用话题格式#话题名#） ### 返回: - AI搜索结果，包含推荐内容、相关话题等 ### 注意: - AI搜索结果会根据用户行为进行个性化调整  # [English] ### Purpose: - Get search results through Weibo AI intelligent search. ### Parameters: - query: Search keyword (required, recommend using topic format #TopicName#) ### Return: - AI search results, including recommended content, related topics ### Note: - AI search results are personalized based on user behavior  # [示例/Example] query = \"#法国#\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
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
                    " to method fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_ai_search', 'GET',
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

    def fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get(self, **kwargs):  # noqa: E501
        """获取所有分组信息/Get all groups information  # noqa: E501

        # [中文] ### 用途: - 获取微博平台的所有分组信息，包括默认分组和用户自定义分组。 ### 参数: - 无需额外参数 ### 返回: - 分组列表，包含分组ID、名称、容器ID等 ### 注意: - 返回的gid和containerid可用于时间轴接口的参数 - 分组信息变化不频繁，建议缓存  # [English] ### Purpose: - Get all group information on Weibo platform, including default and user-defined groups. ### Parameters: - No additional parameters required ### Return: - Group list, including group ID, name, container ID, etc. ### Note: - Returned gid and containerid can be used as parameters for timeline API - Group information changes infrequently, recommend caching  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取所有分组信息/Get all groups information  # noqa: E501

        # [中文] ### 用途: - 获取微博平台的所有分组信息，包括默认分组和用户自定义分组。 ### 参数: - 无需额外参数 ### 返回: - 分组列表，包含分组ID、名称、容器ID等 ### 注意: - 返回的gid和containerid可用于时间轴接口的参数 - 分组信息变化不频繁，建议缓存  # [English] ### Purpose: - Get all group information on Weibo platform, including default and user-defined groups. ### Parameters: - No additional parameters required ### Return: - Group list, including group ID, name, container ID, etc. ### Note: - Returned gid and containerid can be used as parameters for timeline API - Group information changes infrequently, recommend caching  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get_with_http_info(async_req=True)
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
                    " to method fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get" % key
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
            '/api/v1/weibo/web_v2/fetch_all_groups', 'GET',
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

    def fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get(self, **kwargs):  # noqa: E501
        """地区省市映射/Region City List  # noqa: E501

        # [中文] ### 用途: - 获取地区省市映射数据，用于用户搜索等接口的地区筛选参数。 ### 参数: - normalized: 是否返回标准化结构（默认True） ### 返回: - 省市映射数据，用于fetch_user_search等接口的region参数 ### 注意: - 返回的编码格式为 custom:省代码:市代码，如 custom:11:1  # [English] ### Purpose: - Get region city mapping data for region filter parameter in user search APIs. ### Parameters: - normalized: Whether to return normalized structure (default True) ### Return: - Province-city mapping data, for region parameter in fetch_user_search and other APIs ### Note: - Returned code format is custom:province_code:city_code, e.g. custom:11:1  # [示例/Example] normalized = True  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object normalized: 是否返回标准化结构（省份列表+城市数组）/Whether to return normalized structure
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """地区省市映射/Region City List  # noqa: E501

        # [中文] ### 用途: - 获取地区省市映射数据，用于用户搜索等接口的地区筛选参数。 ### 参数: - normalized: 是否返回标准化结构（默认True） ### 返回: - 省市映射数据，用于fetch_user_search等接口的region参数 ### 注意: - 返回的编码格式为 custom:省代码:市代码，如 custom:11:1  # [English] ### Purpose: - Get region city mapping data for region filter parameter in user search APIs. ### Parameters: - normalized: Whether to return normalized structure (default True) ### Return: - Province-city mapping data, for region parameter in fetch_user_search and other APIs ### Note: - Returned code format is custom:province_code:city_code, e.g. custom:11:1  # [示例/Example] normalized = True  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object normalized: 是否返回标准化结构（省份列表+城市数组）/Whether to return normalized structure
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['normalized']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'normalized' in params:
            query_params.append(('normalized', params['normalized']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_city_list', 'GET',
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

    def fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get(self, **kwargs):  # noqa: E501
        """获取微博文娱榜单/Get Weibo entertainment ranking  # noqa: E501

        # [中文] ### 用途: - 获取微博文娱榜单数据（娱乐圈、影视、综艺等）。 ### 参数: - 无需额外参数 ### 返回: - 文娱话题列表，包含话题、热度值、排名、分类等 ### 注意: - 建议缓存5-10分钟  # [English] ### Purpose: - Get Weibo entertainment ranking data (entertainment, film & TV, variety shows). ### Parameters: - No additional parameters required ### Return: - Entertainment topic list, including topic, heat value, rank, category ### Note: - Recommend caching for 5-10 minutes  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取微博文娱榜单/Get Weibo entertainment ranking  # noqa: E501

        # [中文] ### 用途: - 获取微博文娱榜单数据（娱乐圈、影视、综艺等）。 ### 参数: - 无需额外参数 ### 返回: - 文娱话题列表，包含话题、热度值、排名、分类等 ### 注意: - 建议缓存5-10分钟  # [English] ### Purpose: - Get Weibo entertainment ranking data (entertainment, film & TV, variety shows). ### Parameters: - No additional parameters required ### Return: - Entertainment topic list, including topic, heat value, rank, category ### Note: - Recommend caching for 5-10 minutes  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get_with_http_info(async_req=True)
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
                    " to method fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get" % key
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
            '/api/v1/weibo/web_v2/fetch_entertainment_ranking', 'GET',
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

    def fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get(self, ranking_type, **kwargs):  # noqa: E501
        """获取微博热门榜单时间轴/Get hot ranking timeline  # noqa: E501

        # [中文] ### 用途: - 获取微博平台各种类型的热门榜单内容。 ### 参数: - ranking_type: 榜单类型（必填）     - hour: 小时榜     - yesterday: 昨日榜     - day_before: 前日榜     - week: 周榜     - male: 男榜     - female: 女榜 - max_id: 翻页游标，首次请求传\"0\" - count: 获取数量（默认10） ### 返回: - 热门微博列表，包含微博内容、作者信息、互动数据等 ### 注意: - 不同榜单更新频率不同：小时榜实时性最强，周榜影响力较大  # [English] ### Purpose: - Get various types of hot ranking content from Weibo platform. ### Parameters: - ranking_type: Ranking type (required)     - hour: Hourly ranking     - yesterday: Yesterday ranking     - day_before: Day before ranking     - week: Weekly ranking     - male: Male ranking     - female: Female ranking - max_id: Pagination cursor, pass \"0\" for first request - count: Count (default 10) ### Return: - Hot post list, including post content, author info, interaction data ### Note: - Different rankings have different update frequencies: hourly has highest real-time relevance, weekly has high influence  # [示例/Example] ranking_type = \"hour\" max_id = \"0\" count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get(ranking_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ranking_type: 榜单类型：hour=小时榜，yesterday=昨日榜，day_before=前日榜，week=周榜，male=男榜，female=女榜/Ranking type: hour=hourly, yesterday=yesterday, day_before=day before, week=weekly, male=male ranking, female=female ranking (required)
        :param object since_id: 分页标识，默认为0/Pagination identifier, default is 0
        :param object max_id: 最大ID，默认为0/Max ID, default is 0
        :param object count: 获取数量，默认10/Count, default is 10
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get_with_http_info(ranking_type, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get_with_http_info(ranking_type, **kwargs)  # noqa: E501
            return data

    def fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get_with_http_info(self, ranking_type, **kwargs):  # noqa: E501
        """获取微博热门榜单时间轴/Get hot ranking timeline  # noqa: E501

        # [中文] ### 用途: - 获取微博平台各种类型的热门榜单内容。 ### 参数: - ranking_type: 榜单类型（必填）     - hour: 小时榜     - yesterday: 昨日榜     - day_before: 前日榜     - week: 周榜     - male: 男榜     - female: 女榜 - max_id: 翻页游标，首次请求传\"0\" - count: 获取数量（默认10） ### 返回: - 热门微博列表，包含微博内容、作者信息、互动数据等 ### 注意: - 不同榜单更新频率不同：小时榜实时性最强，周榜影响力较大  # [English] ### Purpose: - Get various types of hot ranking content from Weibo platform. ### Parameters: - ranking_type: Ranking type (required)     - hour: Hourly ranking     - yesterday: Yesterday ranking     - day_before: Day before ranking     - week: Weekly ranking     - male: Male ranking     - female: Female ranking - max_id: Pagination cursor, pass \"0\" for first request - count: Count (default 10) ### Return: - Hot post list, including post content, author info, interaction data ### Note: - Different rankings have different update frequencies: hourly has highest real-time relevance, weekly has high influence  # [示例/Example] ranking_type = \"hour\" max_id = \"0\" count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get_with_http_info(ranking_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object ranking_type: 榜单类型：hour=小时榜，yesterday=昨日榜，day_before=前日榜，week=周榜，male=男榜，female=女榜/Ranking type: hour=hourly, yesterday=yesterday, day_before=day before, week=weekly, male=male ranking, female=female ranking (required)
        :param object since_id: 分页标识，默认为0/Pagination identifier, default is 0
        :param object max_id: 最大ID，默认为0/Max ID, default is 0
        :param object count: 获取数量，默认10/Count, default is 10
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ranking_type', 'since_id', 'max_id', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ranking_type' is set
        if self.api_client.client_side_validation and ('ranking_type' not in params or
                                                       params['ranking_type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ranking_type` when calling `fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ranking_type' in params:
            query_params.append(('ranking_type', params['ranking_type']))  # noqa: E501
        if 'since_id' in params:
            query_params.append(('since_id', params['since_id']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_hot_ranking_timeline', 'GET',
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

    def fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get(self, **kwargs):  # noqa: E501
        """获取微博热搜榜单/Get Weibo hot search ranking  # noqa: E501

        # [中文] ### 用途: - 获取微博实时热搜榜单数据。 ### 参数: - 无需额外参数 ### 返回: - 热搜数据，包含realtime（实时热搜）、hotgov等多个板块 ### 注意: - 热搜更新频繁，建议缓存2-5分钟  # [English] ### Purpose: - Get Weibo real-time hot search ranking data. ### Parameters: - No additional parameters required ### Return: - Hot search data, including realtime (real-time hot search), hotgov and other sections ### Note: - Hot search updates frequently, recommend caching for 2-5 minutes  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取微博热搜榜单/Get Weibo hot search ranking  # noqa: E501

        # [中文] ### 用途: - 获取微博实时热搜榜单数据。 ### 参数: - 无需额外参数 ### 返回: - 热搜数据，包含realtime（实时热搜）、hotgov等多个板块 ### 注意: - 热搜更新频繁，建议缓存2-5分钟  # [English] ### Purpose: - Get Weibo real-time hot search ranking data. ### Parameters: - No additional parameters required ### Return: - Hot search data, including realtime (real-time hot search), hotgov and other sections ### Note: - Hot search updates frequently, recommend caching for 2-5 minutes  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get" % key
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
            '/api/v1/weibo/web_v2/fetch_hot_search', 'GET',
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

    def fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get(self, **kwargs):  # noqa: E501
        """获取微博热搜词条(10条)/Get Weibo hot search index (10 items)  # noqa: E501

        # [中文] ### 用途: - 快速获取微博热搜前10条。 ### 参数: - 无需额外参数 ### 返回: - 热搜词条列表，包含关键词、热度值、排名等 ### 注意: - 只返回前10条热搜 - 热搜更新频繁，建议缓存2-5分钟 - 如需完整热搜，使用fetch_hot_search_summary  # [English] ### Purpose: - Quickly get top 10 Weibo hot search items. ### Parameters: - No additional parameters required ### Return: - Hot search term list, including keyword, popularity value, rank ### Note: - Only returns top 10 hot search items - Hot search updates frequently, recommend caching for 2-5 minutes - For complete hot search, use fetch_hot_search_summary  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取微博热搜词条(10条)/Get Weibo hot search index (10 items)  # noqa: E501

        # [中文] ### 用途: - 快速获取微博热搜前10条。 ### 参数: - 无需额外参数 ### 返回: - 热搜词条列表，包含关键词、热度值、排名等 ### 注意: - 只返回前10条热搜 - 热搜更新频繁，建议缓存2-5分钟 - 如需完整热搜，使用fetch_hot_search_summary  # [English] ### Purpose: - Quickly get top 10 Weibo hot search items. ### Parameters: - No additional parameters required ### Return: - Hot search term list, including keyword, popularity value, rank ### Note: - Only returns top 10 hot search items - Hot search updates frequently, recommend caching for 2-5 minutes - For complete hot search, use fetch_hot_search_summary  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get" % key
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
            '/api/v1/weibo/web_v2/fetch_hot_search_index', 'GET',
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

    def fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get(self, **kwargs):  # noqa: E501
        """获取微博完整热搜榜单(50条)/Get Weibo complete hot search ranking (50 items)  # noqa: E501

        # [中文] ### 用途: - 获取微博完整热搜榜单（50条）。 ### 参数: - 无需额外参数 ### 返回: - 完整热搜列表，包含排名、关键词、标签（热点/沸点/官宣/新）、热度值 ### 注意: - 与fetch_hot_search_index的区别：本接口返回50条，fetch_hot_search_index返回10条 - rank为0表示置顶内容 - 建议缓存5-10分钟  # [English] ### Purpose: - Get complete Weibo hot search ranking (50 items). ### Parameters: - No additional parameters required ### Return: - Complete hot search list, including rank, keyword, tag (Hot/Boiling/Official/New), heat value ### Note: - Difference from fetch_hot_search_index: this API returns 50 items, fetch_hot_search_index returns 10 items - rank 0 indicates pinned content - Recommend caching for 5-10 minutes  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取微博完整热搜榜单(50条)/Get Weibo complete hot search ranking (50 items)  # noqa: E501

        # [中文] ### 用途: - 获取微博完整热搜榜单（50条）。 ### 参数: - 无需额外参数 ### 返回: - 完整热搜列表，包含排名、关键词、标签（热点/沸点/官宣/新）、热度值 ### 注意: - 与fetch_hot_search_index的区别：本接口返回50条，fetch_hot_search_index返回10条 - rank为0表示置顶内容 - 建议缓存5-10分钟  # [English] ### Purpose: - Get complete Weibo hot search ranking (50 items). ### Parameters: - No additional parameters required ### Return: - Complete hot search list, including rank, keyword, tag (Hot/Boiling/Official/New), heat value ### Note: - Difference from fetch_hot_search_index: this API returns 50 items, fetch_hot_search_index returns 10 items - rank 0 indicates pinned content - Recommend caching for 5-10 minutes  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get" % key
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
            '/api/v1/weibo/web_v2/fetch_hot_search_summary', 'GET',
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

    def fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get(self, **kwargs):  # noqa: E501
        """获取微博生活榜单/Get Weibo life ranking  # noqa: E501

        # [中文] ### 用途: - 获取微博生活榜单数据（美食、旅游、健康、时尚等）。 ### 参数: - 无需额外参数 ### 返回: - 生活话题列表，包含话题、热度值、排名、分类等 ### 注意: - 建议缓存5-10分钟  # [English] ### Purpose: - Get Weibo life ranking data (food, travel, health, fashion). ### Parameters: - No additional parameters required ### Return: - Life topic list, including topic, heat value, rank, category ### Note: - Recommend caching for 5-10 minutes  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取微博生活榜单/Get Weibo life ranking  # noqa: E501

        # [中文] ### 用途: - 获取微博生活榜单数据（美食、旅游、健康、时尚等）。 ### 参数: - 无需额外参数 ### 返回: - 生活话题列表，包含话题、热度值、排名、分类等 ### 注意: - 建议缓存5-10分钟  # [English] ### Purpose: - Get Weibo life ranking data (food, travel, health, fashion). ### Parameters: - No additional parameters required ### Return: - Life topic list, including topic, heat value, rank, category ### Note: - Recommend caching for 5-10 minutes  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get_with_http_info(async_req=True)
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
                    " to method fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get" % key
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
            '/api/v1/weibo/web_v2/fetch_life_ranking', 'GET',
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

    def fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get(self, query, **kwargs):  # noqa: E501
        """图片搜索/Weibo picture search  # noqa: E501

        # [中文] ### 用途: - 搜索微博图片内容，按微博ID聚合多图。 ### 参数: - query: 搜索关键词（必填） - page: 页码（默认1） ### 返回: - 图片列表，包含微博ID、缩略图、原图链接、作者信息、图片数量 ### 注意: - 缩略图会自动转换为原图链接  # [English] ### Purpose: - Search Weibo picture content, aggregated by weibo ID. ### Parameters: - query: Search keyword (required) - page: Page number (default 1) ### Return: - Image list with weibo ID, thumbnail, large image URL, author info, image count ### Note: - Thumbnails are automatically converted to large image URLs  # [示例/Example] query = \"yu7\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """图片搜索/Weibo picture search  # noqa: E501

        # [中文] ### 用途: - 搜索微博图片内容，按微博ID聚合多图。 ### 参数: - query: 搜索关键词（必填） - page: 页码（默认1） ### 返回: - 图片列表，包含微博ID、缩略图、原图链接、作者信息、图片数量 ### 注意: - 缩略图会自动转换为原图链接  # [English] ### Purpose: - Search Weibo picture content, aggregated by weibo ID. ### Parameters: - query: Search keyword (required) - page: Page number (default 1) ### Return: - Image list with weibo ID, thumbnail, large image URL, author info, image count ### Note: - Thumbnails are automatically converted to large image URLs  # [示例/Example] query = \"yu7\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
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
                    " to method fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_pic_search', 'GET',
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

    def fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get(self, id, **kwargs):  # noqa: E501
        """获取微博评论/Get Weibo comments  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的一级评论列表。 ### 参数: - id: 微博ID（必填） - count: 评论数量（默认10） - max_id: 翻页游标，首次请求传空，后续请求使用返回的max_id值 ### 返回: - 评论列表数据，包含评论内容、评论者信息、点赞数等 - 包含 max_id 字段用于翻页 ### 注意: - 当没有更多评论时，max_id 为空  # [English] ### Purpose: - Get the first-level comment list of specified post. ### Parameters: - id: Weibo post ID (required) - count: Number of comments (default 10) - max_id: Pagination cursor, pass empty for first request, use returned max_id for subsequent requests ### Return: - Comment list data, including comment content, commenter info, likes count - Contains max_id field for pagination ### Note: - When no more comments, max_id is empty  # [示例/Example] id = \"5188973773455957\" count = 10 max_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 微博ID/Weibo ID (required)
        :param object count: 评论数量/Number of comments
        :param object max_id: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """获取微博评论/Get Weibo comments  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的一级评论列表。 ### 参数: - id: 微博ID（必填） - count: 评论数量（默认10） - max_id: 翻页游标，首次请求传空，后续请求使用返回的max_id值 ### 返回: - 评论列表数据，包含评论内容、评论者信息、点赞数等 - 包含 max_id 字段用于翻页 ### 注意: - 当没有更多评论时，max_id 为空  # [English] ### Purpose: - Get the first-level comment list of specified post. ### Parameters: - id: Weibo post ID (required) - count: Number of comments (default 10) - max_id: Pagination cursor, pass empty for first request, use returned max_id for subsequent requests ### Return: - Comment list data, including comment content, commenter info, likes count - Contains max_id field for pagination ### Note: - When no more comments, max_id is empty  # [示例/Example] id = \"5188973773455957\" count = 10 max_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 微博ID/Weibo ID (required)
        :param object count: 评论数量/Number of comments
        :param object max_id: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'count', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_post_comments', 'GET',
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

    def fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get(self, id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single post data  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的详细信息，包括内容、作者、互动数据等。 ### 参数: - id: 微博ID（必填） - is_get_long_text: 是否获取长微博全文（默认\"true\"） ### 返回: - 微博详细数据，包含完整文本、图片、视频、点赞数、评论数、转发数等  # [English] ### Purpose: - Get detailed information of a specific Weibo post, including content, author, interaction data. ### Parameters: - id: Weibo post ID (required) - is_get_long_text: Whether to get full text of long posts (default \"true\") ### Return: - Post detailed data, including full text, images, videos, likes, comments, reposts count  # [示例/Example] id = \"5092682368025584\" is_get_long_text = \"true\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 作品id/Post id (required)
        :param object is_get_long_text: 是否获取长微博全文/Whether to get the full text of long Weibo posts (true/false)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """获取单个作品数据/Get single post data  # noqa: E501

        # [中文] ### 用途: - 获取指定微博的详细信息，包括内容、作者、互动数据等。 ### 参数: - id: 微博ID（必填） - is_get_long_text: 是否获取长微博全文（默认\"true\"） ### 返回: - 微博详细数据，包含完整文本、图片、视频、点赞数、评论数、转发数等  # [English] ### Purpose: - Get detailed information of a specific Weibo post, including content, author, interaction data. ### Parameters: - id: Weibo post ID (required) - is_get_long_text: Whether to get full text of long posts (default \"true\") ### Return: - Post detailed data, including full text, images, videos, likes, comments, reposts count  # [示例/Example] id = \"5092682368025584\" is_get_long_text = \"true\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 作品id/Post id (required)
        :param object is_get_long_text: 是否获取长微博全文/Whether to get the full text of long Weibo posts (true/false)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'is_get_long_text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'is_get_long_text' in params:
            query_params.append(('is_get_long_text', params['is_get_long_text']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_post_detail', 'GET',
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

    def fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get(self, id, **kwargs):  # noqa: E501
        """获取微博子评论/Get Weibo sub-comments  # noqa: E501

        # [中文] ### 用途: - 获取指定评论的回复（子评论）列表。 ### 参数: - id: 主评论ID（必填） - count: 子评论数量（默认10） - max_id: 翻页游标，首次请求传空，后续请求使用返回的max_id值 ### 返回: - 子评论列表数据，包含回复内容、回复者信息、点赞数等 - 包含 max_id 字段用于翻页 ### 注意: - 与fetch_post_comments的区别：本接口获取的是评论的回复，而非微博的主评论  # [English] ### Purpose: - Get the reply (sub-comment) list of a specified comment. ### Parameters: - id: Main comment ID (required) - count: Number of sub-comments (default 10) - max_id: Pagination cursor, pass empty for first request, use returned max_id for subsequent requests ### Return: - Sub-comment list data, including reply content, replier info, likes count - Contains max_id field for pagination ### Note: - Difference from fetch_post_comments: this API gets replies to comments, not main comments of posts  # [示例/Example] id = \"5201793550385562\" count = 10 max_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 主评论ID/Comment ID (required)
        :param object count: 子评论数量/Number of sub-comments
        :param object max_id: 分页标识/Page identifier
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """获取微博子评论/Get Weibo sub-comments  # noqa: E501

        # [中文] ### 用途: - 获取指定评论的回复（子评论）列表。 ### 参数: - id: 主评论ID（必填） - count: 子评论数量（默认10） - max_id: 翻页游标，首次请求传空，后续请求使用返回的max_id值 ### 返回: - 子评论列表数据，包含回复内容、回复者信息、点赞数等 - 包含 max_id 字段用于翻页 ### 注意: - 与fetch_post_comments的区别：本接口获取的是评论的回复，而非微博的主评论  # [English] ### Purpose: - Get the reply (sub-comment) list of a specified comment. ### Parameters: - id: Main comment ID (required) - count: Number of sub-comments (default 10) - max_id: Pagination cursor, pass empty for first request, use returned max_id for subsequent requests ### Return: - Sub-comment list data, including reply content, replier info, likes count - Contains max_id field for pagination ### Note: - Difference from fetch_post_comments: this API gets replies to comments, not main comments of posts  # [示例/Example] id = \"5201793550385562\" count = 10 max_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: 主评论ID/Comment ID (required)
        :param object count: 子评论数量/Number of sub-comments
        :param object max_id: 分页标识/Page identifier
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'count', 'max_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_post_sub_comments', 'GET',
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

    def fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get(self, query, **kwargs):  # noqa: E501
        """实时搜索/Weibo Realtime Search  # noqa: E501

        # [中文] ### 用途: - 获取微博实时搜索结果（按时间排序的最新微博）。 ### 参数: - query: 搜索关键词（必填） - page: 页码（默认1） ### 返回: - 实时搜索结果列表，包含微博内容、作者信息、图片、视频、互动数据等 ### 注意: - 视频播放需设置请求头 Referer=https://weibo.com/ - 返回结构与高级搜索一致  # [English] ### Purpose: - Get Weibo realtime search results (latest posts sorted by time). ### Parameters: - query: Search keyword (required) - page: Page number (default 1) ### Return: - Realtime search result list, including post content, author info, images, videos, interaction data ### Note: - Video playback requires setting header Referer=https://weibo.com/ - Return structure is same as advanced search  # [示例/Example] query = \"苹果发布会\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """实时搜索/Weibo Realtime Search  # noqa: E501

        # [中文] ### 用途: - 获取微博实时搜索结果（按时间排序的最新微博）。 ### 参数: - query: 搜索关键词（必填） - page: 页码（默认1） ### 返回: - 实时搜索结果列表，包含微博内容、作者信息、图片、视频、互动数据等 ### 注意: - 视频播放需设置请求头 Referer=https://weibo.com/ - 返回结构与高级搜索一致  # [English] ### Purpose: - Get Weibo realtime search results (latest posts sorted by time). ### Parameters: - query: Search keyword (required) - page: Page number (default 1) ### Return: - Realtime search result list, including post content, author info, images, videos, interaction data ### Note: - Video playback requires setting header Referer=https://weibo.com/ - Return structure is same as advanced search  # [示例/Example] query = \"苹果发布会\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
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
                    " to method fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_realtime_search', 'GET',
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

    def fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get(self, keyword, **kwargs):  # noqa: E501
        """获取微博相似搜索词推荐/Get Weibo similar search recommendations  # noqa: E501

        # [中文] ### 用途: - 根据关键词获取微博推荐的相似搜索词。 ### 参数: - keyword: 搜索关键词（必填，支持话题标签格式如#话题名#） ### 返回: - 相似搜索词列表，包含推荐词、搜索次数等 ### 注意: - 相似词推荐相对稳定，可缓存15-30分钟  # [English] ### Purpose: - Get similar search word recommendations based on keyword. ### Parameters: - keyword: Search keyword (required, supports topic tag format like #TopicName#) ### Return: - Similar search term list, including suggestion, search count ### Note: - Similar word recommendations are relatively stable, can cache for 15-30 minutes  # [示例/Example] keyword = \"#微博奇遇记#\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取微博相似搜索词推荐/Get Weibo similar search recommendations  # noqa: E501

        # [中文] ### 用途: - 根据关键词获取微博推荐的相似搜索词。 ### 参数: - keyword: 搜索关键词（必填，支持话题标签格式如#话题名#） ### 返回: - 相似搜索词列表，包含推荐词、搜索次数等 ### 注意: - 相似词推荐相对稳定，可缓存15-30分钟  # [English] ### Purpose: - Get similar search word recommendations based on keyword. ### Parameters: - keyword: Search keyword (required, supports topic tag format like #TopicName#) ### Return: - Similar search term list, including suggestion, search count ### Note: - Similar word recommendations are relatively stable, can cache for 15-30 minutes  # [示例/Example] keyword = \"#微博奇遇记#\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get_with_http_info(keyword, async_req=True)
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
                    " to method fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_similar_search', 'GET',
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

    def fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get(self, **kwargs):  # noqa: E501
        """获取微博社会榜单/Get Weibo social ranking  # noqa: E501

        # [中文] ### 用途: - 获取微博社会榜单数据（时事新闻、社会热点、民生话题等）。 ### 参数: - 无需额外参数 ### 返回: - 社会话题列表，包含话题、热度值、排名、分类等 ### 注意: - 社会热点变化较快，建议缓存2-5分钟  # [English] ### Purpose: - Get Weibo social ranking data (current affairs, social hotspots, livelihood topics). ### Parameters: - No additional parameters required ### Return: - Social topic list, including topic, heat value, rank, category ### Note: - Social hotspots change rapidly, recommend caching for 2-5 minutes  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取微博社会榜单/Get Weibo social ranking  # noqa: E501

        # [中文] ### 用途: - 获取微博社会榜单数据（时事新闻、社会热点、民生话题等）。 ### 参数: - 无需额外参数 ### 返回: - 社会话题列表，包含话题、热度值、排名、分类等 ### 注意: - 社会热点变化较快，建议缓存2-5分钟  # [English] ### Purpose: - Get Weibo social ranking data (current affairs, social hotspots, livelihood topics). ### Parameters: - No additional parameters required ### Return: - Social topic list, including topic, heat value, rank, category ### Note: - Social hotspots change rapidly, recommend caching for 2-5 minutes  # [示例/Example] # No parameters needed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get_with_http_info(async_req=True)
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
                    " to method fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get" % key
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
            '/api/v1/weibo/web_v2/fetch_social_ranking', 'GET',
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

    def fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get(self, query, **kwargs):  # noqa: E501
        """话题搜索/Weibo topic search  # noqa: E501

        # [中文] ### 用途: - 搜索微博话题，获取话题名称、封面、讨论量、阅读量。 ### 参数: - query: 搜索关键词（必填） - page: 页码（默认1） ### 返回: - 话题列表，包含话题名、封面图、讨论数、阅读数 ### 注意: - 数量单位（万/亿）已转换为整数  # [English] ### Purpose: - Search Weibo topics, get topic name, cover, discussion count, read count. ### Parameters: - query: Search keyword (required) - page: Page number (default 1) ### Return: - Topic list with topic name, cover image, discussion count, read count ### Note: - Count units (万/亿) are converted to integers  # [示例/Example] query = \"yu7\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """话题搜索/Weibo topic search  # noqa: E501

        # [中文] ### 用途: - 搜索微博话题，获取话题名称、封面、讨论量、阅读量。 ### 参数: - query: 搜索关键词（必填） - page: 页码（默认1） ### 返回: - 话题列表，包含话题名、封面图、讨论数、阅读数 ### 注意: - 数量单位（万/亿）已转换为整数  # [English] ### Purpose: - Search Weibo topics, get topic name, cover, discussion count, read count. ### Parameters: - query: Search keyword (required) - page: Page number (default 1) ### Return: - Topic list with topic name, cover image, discussion count, read count ### Note: - Count units (万/亿) are converted to integers  # [示例/Example] query = \"yu7\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object page: 页码/Page number
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
                    " to method fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_topic_search', 'GET',
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

    def fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get(self, uid, **kwargs):  # noqa: E501
        """获取用户基本信息/Get user basic information  # noqa: E501

        # [中文] ### 用途: - 获取微博用户的基本信息（轻量级接口）。 ### 参数: - uid: 用户ID（必填） ### 返回: - 用户基本信息，包括用户ID、用户名、头像、简介、认证信息 ### 注意: - 与fetch_user_info相比，本接口返回数据更少，响应更快 - 适合批量用户信息获取和用户卡片展示  # [English] ### Purpose: - Get basic information of Weibo users (lightweight API). ### Parameters: - uid: User ID (required) ### Return: - User basic info, including user ID, username, avatar, bio, verification ### Note: - Compared to fetch_user_info, this API returns less data with faster response - Suitable for batch user info retrieval and user card display  # [示例/Example] uid = \"7277477906\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户基本信息/Get user basic information  # noqa: E501

        # [中文] ### 用途: - 获取微博用户的基本信息（轻量级接口）。 ### 参数: - uid: 用户ID（必填） ### 返回: - 用户基本信息，包括用户ID、用户名、头像、简介、认证信息 ### 注意: - 与fetch_user_info相比，本接口返回数据更少，响应更快 - 适合批量用户信息获取和用户卡片展示  # [English] ### Purpose: - Get basic information of Weibo users (lightweight API). ### Parameters: - uid: User ID (required) ### Return: - User basic info, including user ID, username, avatar, bio, verification ### Note: - Compared to fetch_user_info, this API returns less data with faster response - Suitable for batch user info retrieval and user card display  # [示例/Example] uid = \"7277477906\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get_with_http_info(uid, async_req=True)
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
                    " to method fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_user_basic_info', 'GET',
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

    def fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get(self, uid, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Get user fans list  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的粉丝列表（谁关注了该用户）。 ### 参数: - uid: 用户ID（必填） - page: 页码，从0开始（默认0） ### 返回: - 粉丝用户列表，包含用户名、头像、简介、粉丝数等 ### 注意: - 粉丝列表受用户隐私设置影响 - page参数从0开始，而不是1 - 与fetch_user_following的区别：本接口获取谁关注了该用户，fetch_user_following获取用户关注了谁  # [English] ### Purpose: - Get the fans list of specified user (who follows the user). ### Parameters: - uid: User ID (required) - page: Page number, starts from 0 (default 0) ### Return: - Fans user list, including username, avatar, bio, followers count ### Note: - Fans list affected by user privacy settings - page parameter starts from 0, not 1 - Difference from fetch_user_following: this API gets who follows the user, fetch_user_following gets who user follows  # [示例/Example] uid = \"1722594714\" page = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Get user fans list  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的粉丝列表（谁关注了该用户）。 ### 参数: - uid: 用户ID（必填） - page: 页码，从0开始（默认0） ### 返回: - 粉丝用户列表，包含用户名、头像、简介、粉丝数等 ### 注意: - 粉丝列表受用户隐私设置影响 - page参数从0开始，而不是1 - 与fetch_user_following的区别：本接口获取谁关注了该用户，fetch_user_following获取用户关注了谁  # [English] ### Purpose: - Get the fans list of specified user (who follows the user). ### Parameters: - uid: User ID (required) - page: Page number, starts from 0 (default 0) ### Return: - Fans user list, including username, avatar, bio, followers count ### Note: - Fans list affected by user privacy settings - page parameter starts from 0, not 1 - Difference from fetch_user_following: this API gets who follows the user, fetch_user_following gets who user follows  # [示例/Example] uid = \"1722594714\" page = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :param object page: 页码/Page number
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
                    " to method fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_user_fans', 'GET',
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

    def fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get(self, uid, **kwargs):  # noqa: E501
        """获取用户关注列表/Get user following list  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的关注列表（该用户关注了谁）。 ### 参数: - uid: 用户ID（必填） - page: 页码，从0开始（默认0） ### 返回: - 关注用户列表，包含用户名、头像、简介、粉丝数等 ### 注意: - 关注列表受用户隐私设置影响 - page参数从0开始，而不是1 - 与fetch_user_fans的区别：本接口获取用户关注了谁，fetch_user_fans获取谁关注了该用户  # [English] ### Purpose: - Get the following list of specified user (who the user follows). ### Parameters: - uid: User ID (required) - page: Page number, starts from 0 (default 0) ### Return: - Following user list, including username, avatar, bio, followers count ### Note: - Following list affected by user privacy settings - page parameter starts from 0, not 1 - Difference from fetch_user_fans: this API gets who user follows, fetch_user_fans gets who follows the user  # [示例/Example] uid = \"1722594714\" page = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户关注列表/Get user following list  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的关注列表（该用户关注了谁）。 ### 参数: - uid: 用户ID（必填） - page: 页码，从0开始（默认0） ### 返回: - 关注用户列表，包含用户名、头像、简介、粉丝数等 ### 注意: - 关注列表受用户隐私设置影响 - page参数从0开始，而不是1 - 与fetch_user_fans的区别：本接口获取用户关注了谁，fetch_user_fans获取谁关注了该用户  # [English] ### Purpose: - Get the following list of specified user (who the user follows). ### Parameters: - uid: User ID (required) - page: Page number, starts from 0 (default 0) ### Return: - Following user list, including username, avatar, bio, followers count ### Note: - Following list affected by user privacy settings - page parameter starts from 0, not 1 - Difference from fetch_user_fans: this API gets who user follows, fetch_user_fans gets who follows the user  # [示例/Example] uid = \"1722594714\" page = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :param object page: 页码/Page number
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
                    " to method fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_user_following', 'GET',
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

    def fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get(self, **kwargs):  # noqa: E501
        """获取用户信息/Get user information  # noqa: E501

        # [中文] ### 用途: - 获取微博用户的详细信息，包括昵称、头像、简介、关注数、粉丝数等。 ### 参数: - uid: 用户ID（可选，与custom二选一） - custom: 自定义用户名（可选，与uid二选一） ### 返回: - 用户详细信息数据 ### 注意: - uid和custom参数至少需要提供一个 - 如果同时提供，优先使用uid - 建议优先使用uid参数  # [English] ### Purpose: - Get detailed information of Weibo users, including nickname, avatar, bio, following count, followers count. ### Parameters: - uid: User ID (optional, choose one with custom) - custom: Custom username (optional, choose one with uid) ### Return: - User detailed information data ### Note: - At least one of uid and custom must be provided - If both provided, uid takes priority - It's recommended to use uid parameter first  # [示例/Example] uid = \"1722594714\" # or custom = \"shuqi\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id
        :param object custom: 自定义微博用户名/Custom Weibo username
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户信息/Get user information  # noqa: E501

        # [中文] ### 用途: - 获取微博用户的详细信息，包括昵称、头像、简介、关注数、粉丝数等。 ### 参数: - uid: 用户ID（可选，与custom二选一） - custom: 自定义用户名（可选，与uid二选一） ### 返回: - 用户详细信息数据 ### 注意: - uid和custom参数至少需要提供一个 - 如果同时提供，优先使用uid - 建议优先使用uid参数  # [English] ### Purpose: - Get detailed information of Weibo users, including nickname, avatar, bio, following count, followers count. ### Parameters: - uid: User ID (optional, choose one with custom) - custom: Custom username (optional, choose one with uid) ### Return: - User detailed information data ### Note: - At least one of uid and custom must be provided - If both provided, uid takes priority - It's recommended to use uid parameter first  # [示例/Example] uid = \"1722594714\" # or custom = \"shuqi\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id
        :param object custom: 自定义微博用户名/Custom Weibo username
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'custom']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'custom' in params:
            query_params.append(('custom', params['custom']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_user_info', 'GET',
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

    def fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get(self, uid, **kwargs):  # noqa: E501
        """获取微博用户原创微博数据/Get Weibo user original posts  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的原创微博列表（排除转发内容）。 ### 参数: - uid: 用户ID（必填） - page: 页码，从1开始（默认1） - since_id: 翻页标识（第一页必须从fetch_user_posts接口获取） ### 返回: - 原创微博列表，包含微博内容、图片、视频、互动数据等 ### 注意: - 与fetch_user_posts的区别：本接口只返回原创微博，排除转发 - since_id必须先调用fetch_user_posts获取，第一页必传，后续页面不传  # [English] ### Purpose: - Get original posts published by specified user (excluding reposts). ### Parameters: - uid: User ID (required) - page: Page number, starts from 1 (default 1) - since_id: Pagination identifier (first page must get from fetch_user_posts) ### Return: - Original post list, including content, images, videos, interaction data ### Note: - Difference from fetch_user_posts: this API only returns original posts, excludes reposts - since_id must be obtained from fetch_user_posts first, required for first page, not needed for subsequent pages  # [示例/Example] uid = \"7277477906\" page = 1 since_id = \"4924526881242703\"  # from fetch_user_posts response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :param object page: 页数/Page number
        :param object since_id: 翻页标识，用于获取下一页数据/Pagination identifier for getting next page data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取微博用户原创微博数据/Get Weibo user original posts  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的原创微博列表（排除转发内容）。 ### 参数: - uid: 用户ID（必填） - page: 页码，从1开始（默认1） - since_id: 翻页标识（第一页必须从fetch_user_posts接口获取） ### 返回: - 原创微博列表，包含微博内容、图片、视频、互动数据等 ### 注意: - 与fetch_user_posts的区别：本接口只返回原创微博，排除转发 - since_id必须先调用fetch_user_posts获取，第一页必传，后续页面不传  # [English] ### Purpose: - Get original posts published by specified user (excluding reposts). ### Parameters: - uid: User ID (required) - page: Page number, starts from 1 (default 1) - since_id: Pagination identifier (first page must get from fetch_user_posts) ### Return: - Original post list, including content, images, videos, interaction data ### Note: - Difference from fetch_user_posts: this API only returns original posts, excludes reposts - since_id must be obtained from fetch_user_posts first, required for first page, not needed for subsequent pages  # [示例/Example] uid = \"7277477906\" page = 1 since_id = \"4924526881242703\"  # from fetch_user_posts response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :param object page: 页数/Page number
        :param object since_id: 翻页标识，用于获取下一页数据/Pagination identifier for getting next page data
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
                    " to method fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_user_original_posts', 'GET',
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

    def fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get(self, uid, **kwargs):  # noqa: E501
        """获取微博用户文章数据/Get Weibo user posts  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的微博列表，支持分页和多种数据详细程度。 ### 参数: - uid: 用户ID（必填） - page: 页码，从1开始（默认1） - feature: 数据特征值（默认0）     - 0: 返回10条基础数据     - 1: 返回20条扩展数据     - 2: 返回20条图片相关数据     - 3: 返回20条完整数据 - since_id: 翻页标识，用于获取下一页数据 ### 返回: - 微博列表数据，包含微博内容、图片、视频等信息 - 包含 since_id 字段用于翻页 ### 注意: - feature=0性能最佳，feature=3数据最全  # [English] ### Purpose: - Get the list of posts published by specified user, support pagination and multiple data detail levels. ### Parameters: - uid: User ID (required) - page: Page number, starts from 1 (default 1) - feature: Data feature value (default 0)     - 0: Return 10 basic posts     - 1: Return 20 extended posts     - 2: Return 20 image-related posts     - 3: Return 20 complete posts - since_id: Pagination identifier for next page ### Return: - Post list data, including post content, images, videos, etc. - Contains since_id field for pagination ### Note: - feature=0 has best performance, feature=3 has most complete data  # [示例/Example] uid = \"7277477906\" page = 1 feature = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :param object page: 页数/Page number
        :param object feature: 特征值，控制返回数据的数量和字段：0=返回10条基础数据，1=返回20条扩展数据，2=返回20条图片相关数据，3=返回20条视频相关数据，字段逐级增加/Feature type: 0=10 basic posts, 1=20 extended posts, 2=20 image-related posts, 3=20 video-related posts, fields increase progressively
        :param object since_id: 翻页标识，用于获取下一页数据/Pagination identifier for getting next page data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取微博用户文章数据/Get Weibo user posts  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的微博列表，支持分页和多种数据详细程度。 ### 参数: - uid: 用户ID（必填） - page: 页码，从1开始（默认1） - feature: 数据特征值（默认0）     - 0: 返回10条基础数据     - 1: 返回20条扩展数据     - 2: 返回20条图片相关数据     - 3: 返回20条完整数据 - since_id: 翻页标识，用于获取下一页数据 ### 返回: - 微博列表数据，包含微博内容、图片、视频等信息 - 包含 since_id 字段用于翻页 ### 注意: - feature=0性能最佳，feature=3数据最全  # [English] ### Purpose: - Get the list of posts published by specified user, support pagination and multiple data detail levels. ### Parameters: - uid: User ID (required) - page: Page number, starts from 1 (default 1) - feature: Data feature value (default 0)     - 0: Return 10 basic posts     - 1: Return 20 extended posts     - 2: Return 20 image-related posts     - 3: Return 20 complete posts - since_id: Pagination identifier for next page ### Return: - Post list data, including post content, images, videos, etc. - Contains since_id field for pagination ### Note: - feature=0 has best performance, feature=3 has most complete data  # [示例/Example] uid = \"7277477906\" page = 1 feature = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户id/User id (required)
        :param object page: 页数/Page number
        :param object feature: 特征值，控制返回数据的数量和字段：0=返回10条基础数据，1=返回20条扩展数据，2=返回20条图片相关数据，3=返回20条视频相关数据，字段逐级增加/Feature type: 0=10 basic posts, 1=20 extended posts, 2=20 image-related posts, 3=20 video-related posts, fields increase progressively
        :param object since_id: 翻页标识，用于获取下一页数据/Pagination identifier for getting next page data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'page', 'feature', 'since_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'feature' in params:
            query_params.append(('feature', params['feature']))  # noqa: E501
        if 'since_id' in params:
            query_params.append(('since_id', params['since_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_user_posts', 'GET',
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

    def fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get(self, **kwargs):  # noqa: E501
        """获取微博主页推荐时间轴/Get user recommend timeline  # noqa: E501

        # [中文] ### 用途: - 获取微博主页的推荐时间轴内容，基于用户兴趣展示个性化推荐。 ### 参数: - refresh: 刷新类型（0=正常刷新，1=强制刷新） - group_id: 分组ID（可通过fetch_all_groups获取） - containerid: 容器ID（通常与group_id相同） - extparam: 扩展参数（默认\"discover|new_feed\"） - max_id: 翻页游标，首次请求传\"0\" - count: 获取数量（默认10，建议5-20） ### 返回: - 推荐微博列表，包含微博内容、作者信息、互动数据等 - 包含 max_id 字段用于翻页 ### 注意: - 建议先调用fetch_all_groups获取可用分组  # [English] ### Purpose: - Get recommended timeline content from Weibo homepage, displaying personalized recommendations based on user interests. ### Parameters: - refresh: Refresh type (0=normal refresh, 1=force refresh) - group_id: Group ID (can be obtained through fetch_all_groups) - containerid: Container ID (usually same as group_id) - extparam: Extended parameters (default \"discover|new_feed\") - max_id: Pagination cursor, pass \"0\" for first request - count: Count (default 10, suggested 5-20) ### Return: - Recommended post list, including post content, author info, interaction data - Contains max_id field for pagination ### Note: - Recommend calling fetch_all_groups first to get available groups  # [示例/Example] refresh = 0 group_id = \"102803\" containerid = \"102803\" max_id = \"0\" count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object refresh: 刷新类型，0=正常刷新，1=强制刷新/Refresh type, 0=normal refresh, 1=force refresh
        :param object group_id: 分组ID/Group ID
        :param object containerid: 容器ID/Container ID
        :param object extparam: 扩展参数/Extended parameters
        :param object max_id: 最大ID/Max ID
        :param object count: 获取数量/Count
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取微博主页推荐时间轴/Get user recommend timeline  # noqa: E501

        # [中文] ### 用途: - 获取微博主页的推荐时间轴内容，基于用户兴趣展示个性化推荐。 ### 参数: - refresh: 刷新类型（0=正常刷新，1=强制刷新） - group_id: 分组ID（可通过fetch_all_groups获取） - containerid: 容器ID（通常与group_id相同） - extparam: 扩展参数（默认\"discover|new_feed\"） - max_id: 翻页游标，首次请求传\"0\" - count: 获取数量（默认10，建议5-20） ### 返回: - 推荐微博列表，包含微博内容、作者信息、互动数据等 - 包含 max_id 字段用于翻页 ### 注意: - 建议先调用fetch_all_groups获取可用分组  # [English] ### Purpose: - Get recommended timeline content from Weibo homepage, displaying personalized recommendations based on user interests. ### Parameters: - refresh: Refresh type (0=normal refresh, 1=force refresh) - group_id: Group ID (can be obtained through fetch_all_groups) - containerid: Container ID (usually same as group_id) - extparam: Extended parameters (default \"discover|new_feed\") - max_id: Pagination cursor, pass \"0\" for first request - count: Count (default 10, suggested 5-20) ### Return: - Recommended post list, including post content, author info, interaction data - Contains max_id field for pagination ### Note: - Recommend calling fetch_all_groups first to get available groups  # [示例/Example] refresh = 0 group_id = \"102803\" containerid = \"102803\" max_id = \"0\" count = 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object refresh: 刷新类型，0=正常刷新，1=强制刷新/Refresh type, 0=normal refresh, 1=force refresh
        :param object group_id: 分组ID/Group ID
        :param object containerid: 容器ID/Container ID
        :param object extparam: 扩展参数/Extended parameters
        :param object max_id: 最大ID/Max ID
        :param object count: 获取数量/Count
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['refresh', 'group_id', 'containerid', 'extparam', 'max_id', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'refresh' in params:
            query_params.append(('refresh', params['refresh']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'containerid' in params:
            query_params.append(('containerid', params['containerid']))  # noqa: E501
        if 'extparam' in params:
            query_params.append(('extparam', params['extparam']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('max_id', params['max_id']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_user_recommend_timeline', 'GET',
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

    def fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get(self, **kwargs):  # noqa: E501
        """用户搜索/User search  # noqa: E501

        # [中文] ### 用途: - 搜索微博用户，支持多种筛选条件。 ### 参数: - query: 搜索关键词（可选） - page: 页码（默认1） - region: 地区编码，从/fetch_city_list获取（可选） - auth: 认证类型 org_vip/per_vip/ord（可选） - gender: 性别 man/women（可选） - age: 年龄段 18y/22y/29y/39y/40y（可选） - nickname: 昵称筛选（可选） - tag: 标签筛选（可选） - school: 学校筛选（可选） - work: 公司筛选（可选） ### 返回: - 用户列表，包含uid、昵称、头像、粉丝数、主页链接 ### 注意: - 筛选参数过多可能导致无结果  # [English] ### Purpose: - Search Weibo users with multiple filter options. ### Parameters: - query: Search keyword (optional) - page: Page number (default 1) - region: Region code from /fetch_city_list (optional) - auth: Auth type org_vip/per_vip/ord (optional) - gender: Gender man/women (optional) - age: Age bucket 18y/22y/29y/39y/40y (optional) - nickname: Nickname filter (optional) - tag: Tag filter (optional) - school: School filter (optional) - work: Company filter (optional) ### Return: - User list with uid, nickname, avatar, fans count, profile URL ### Note: - Too many filters may result in no results  # [示例/Example] query = \"yu7\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Query（提供则视为“全部”搜索；留空则仅应用高级筛选参数）
        :param object page: 页码/Page
        :param object region: 地区编码，从 /city_list 获取/Region code from /city_list
        :param object auth: 认证类型 org_vip(机构)/per_vip(个人)/ord(普通)/Auth type
        :param object gender: 性别 man / women / Gender
        :param object age: 年龄段 18y/22y/29y/39y/40y / Age bucket
        :param object nickname: 昵称筛选/Nickname filter
        :param object tag: 标签筛选/Tag filter
        :param object school: 学校筛选/School filter
        :param object work: 公司筛选/Company filter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get_with_http_info(self, **kwargs):  # noqa: E501
        """用户搜索/User search  # noqa: E501

        # [中文] ### 用途: - 搜索微博用户，支持多种筛选条件。 ### 参数: - query: 搜索关键词（可选） - page: 页码（默认1） - region: 地区编码，从/fetch_city_list获取（可选） - auth: 认证类型 org_vip/per_vip/ord（可选） - gender: 性别 man/women（可选） - age: 年龄段 18y/22y/29y/39y/40y（可选） - nickname: 昵称筛选（可选） - tag: 标签筛选（可选） - school: 学校筛选（可选） - work: 公司筛选（可选） ### 返回: - 用户列表，包含uid、昵称、头像、粉丝数、主页链接 ### 注意: - 筛选参数过多可能导致无结果  # [English] ### Purpose: - Search Weibo users with multiple filter options. ### Parameters: - query: Search keyword (optional) - page: Page number (default 1) - region: Region code from /fetch_city_list (optional) - auth: Auth type org_vip/per_vip/ord (optional) - gender: Gender man/women (optional) - age: Age bucket 18y/22y/29y/39y/40y (optional) - nickname: Nickname filter (optional) - tag: Tag filter (optional) - school: School filter (optional) - work: Company filter (optional) ### Return: - User list with uid, nickname, avatar, fans count, profile URL ### Note: - Too many filters may result in no results  # [示例/Example] query = \"yu7\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Query（提供则视为“全部”搜索；留空则仅应用高级筛选参数）
        :param object page: 页码/Page
        :param object region: 地区编码，从 /city_list 获取/Region code from /city_list
        :param object auth: 认证类型 org_vip(机构)/per_vip(个人)/ord(普通)/Auth type
        :param object gender: 性别 man / women / Gender
        :param object age: 年龄段 18y/22y/29y/39y/40y / Age bucket
        :param object nickname: 昵称筛选/Nickname filter
        :param object tag: 标签筛选/Tag filter
        :param object school: 学校筛选/School filter
        :param object work: 公司筛选/Company filter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'page', 'region', 'auth', 'gender', 'age', 'nickname', 'tag', 'school', 'work']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'auth' in params:
            query_params.append(('auth', params['auth']))  # noqa: E501
        if 'gender' in params:
            query_params.append(('gender', params['gender']))  # noqa: E501
        if 'age' in params:
            query_params.append(('age', params['age']))  # noqa: E501
        if 'nickname' in params:
            query_params.append(('nickname', params['nickname']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
        if 'school' in params:
            query_params.append(('school', params['school']))  # noqa: E501
        if 'work' in params:
            query_params.append(('work', params['work']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_user_search', 'GET',
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

    def fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get(self, cid, **kwargs):  # noqa: E501
        """获取用户微博视频收藏夹详情/Get user video collection detail  # noqa: E501

        # [中文] ### 用途: - 获取指定收藏夹的详细内容，包括视频列表。 ### 参数: - cid: 收藏夹ID（必填，从fetch_user_video_collection_list获取） - cursor: 分页游标，首次请求传空，后续使用返回的cursor - tab_code: 排序方式（0=默认，1=最热，2=最新） ### 返回: - 收藏夹信息和视频列表，包含视频标题、封面、时长、播放数等 - 包含 next_cursor 和 has_more 字段用于翻页 ### 注意: - 不同排序方式的cursor不通用，切换排序需重新开始分页  # [English] ### Purpose: - Get detailed content of specified collection, including video list. ### Parameters: - cid: Collection ID (required, get from fetch_user_video_collection_list) - cursor: Pagination cursor, pass empty for first request, use returned cursor for subsequent - tab_code: Sort type (0=default, 1=hottest, 2=latest) ### Return: - Collection info and video list, including video title, cover, duration, views - Contains next_cursor and has_more fields for pagination ### Note: - Cursors for different sorting methods are not universal, switching sorting requires restarting pagination  # [示例/Example] cid = \"4883992307236954\" cursor = \"\" tab_code = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cid: 收藏夹ID/Collection ID (required)
        :param object cursor: 分页游标/Pagination cursor
        :param object tab_code: 排序方式：0=默认，1=最热，2=最新/Sort type: 0=default, 1=hottest, 2=latest
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get_with_http_info(cid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get_with_http_info(cid, **kwargs)  # noqa: E501
            return data

    def fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get_with_http_info(self, cid, **kwargs):  # noqa: E501
        """获取用户微博视频收藏夹详情/Get user video collection detail  # noqa: E501

        # [中文] ### 用途: - 获取指定收藏夹的详细内容，包括视频列表。 ### 参数: - cid: 收藏夹ID（必填，从fetch_user_video_collection_list获取） - cursor: 分页游标，首次请求传空，后续使用返回的cursor - tab_code: 排序方式（0=默认，1=最热，2=最新） ### 返回: - 收藏夹信息和视频列表，包含视频标题、封面、时长、播放数等 - 包含 next_cursor 和 has_more 字段用于翻页 ### 注意: - 不同排序方式的cursor不通用，切换排序需重新开始分页  # [English] ### Purpose: - Get detailed content of specified collection, including video list. ### Parameters: - cid: Collection ID (required, get from fetch_user_video_collection_list) - cursor: Pagination cursor, pass empty for first request, use returned cursor for subsequent - tab_code: Sort type (0=default, 1=hottest, 2=latest) ### Return: - Collection info and video list, including video title, cover, duration, views - Contains next_cursor and has_more fields for pagination ### Note: - Cursors for different sorting methods are not universal, switching sorting requires restarting pagination  # [示例/Example] cid = \"4883992307236954\" cursor = \"\" tab_code = 0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get_with_http_info(cid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object cid: 收藏夹ID/Collection ID (required)
        :param object cursor: 分页游标/Pagination cursor
        :param object tab_code: 排序方式：0=默认，1=最热，2=最新/Sort type: 0=default, 1=hottest, 2=latest
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cid', 'cursor', 'tab_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cid' is set
        if self.api_client.client_side_validation and ('cid' not in params or
                                                       params['cid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cid` when calling `fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cid' in params:
            query_params.append(('cid', params['cid']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'tab_code' in params:
            query_params.append(('tab_code', params['tab_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_user_video_collection_detail', 'GET',
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

    def fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get(self, uid, **kwargs):  # noqa: E501
        """获取用户微博视频收藏夹列表/Get user video collection list  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的视频收藏夹列表。 ### 参数: - uid: 用户ID（必填） ### 返回: - 收藏夹列表，包含收藏夹ID、名称、描述、视频数量等 ### 注意: - 收藏夹列表受用户隐私设置影响 - 部分用户可能没有创建视频收藏夹  # [English] ### Purpose: - Get video collection list of specified user. ### Parameters: - uid: User ID (required) ### Return: - Collection list, including collection ID, name, description, video count ### Note: - Collection list affected by user privacy settings - Some users may not have created video collections  # [示例/Example] uid = \"7277477906\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取用户微博视频收藏夹列表/Get user video collection list  # noqa: E501

        # [中文] ### 用途: - 获取指定用户的视频收藏夹列表。 ### 参数: - uid: 用户ID（必填） ### 返回: - 收藏夹列表，包含收藏夹ID、名称、描述、视频数量等 ### 注意: - 收藏夹列表受用户隐私设置影响 - 部分用户可能没有创建视频收藏夹  # [English] ### Purpose: - Get video collection list of specified user. ### Parameters: - uid: User ID (required) ### Return: - Collection list, including collection ID, name, description, video count ### Note: - Collection list affected by user privacy settings - Some users may not have created video collections  # [示例/Example] uid = \"7277477906\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get_with_http_info(uid, async_req=True)
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
                    " to method fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get`")  # noqa: E501

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
            '/api/v1/weibo/web_v2/fetch_user_video_collection_list', 'GET',
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

    def fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get(self, uid, **kwargs):  # noqa: E501
        """获取微博用户全部视频/Get user all videos  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的所有视频内容（瀑布流展示）。 ### 参数: - uid: 用户ID（必填） - cursor: 翻页游标，初次请求传\"0\"，后续请求使用返回的next_cursor值 ### 返回: - 视频列表数据，包含视频标题、封面、播放量等信息 - 包含 next_cursor 和 has_more 字段用于翻页 ### 注意: - 与收藏夹接口的区别：本接口获取用户发布的视频，收藏夹接口获取用户收藏的视频  # [English] ### Purpose: - Get all videos published by specified user (waterfall layout). ### Parameters: - uid: User ID (required) - cursor: Pagination cursor, pass \"0\" for first request, use returned next_cursor for subsequent requests ### Return: - Video list data, including video title, cover, views, etc. - Contains next_cursor and has_more fields for pagination ### Note: - Difference from collection APIs: this API gets user published videos, collection APIs get user collected videos  # [示例/Example] uid = \"7277477906\" cursor = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :param object cursor: 分页游标/Pagination cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get_with_http_info(self, uid, **kwargs):  # noqa: E501
        """获取微博用户全部视频/Get user all videos  # noqa: E501

        # [中文] ### 用途: - 获取指定用户发布的所有视频内容（瀑布流展示）。 ### 参数: - uid: 用户ID（必填） - cursor: 翻页游标，初次请求传\"0\"，后续请求使用返回的next_cursor值 ### 返回: - 视频列表数据，包含视频标题、封面、播放量等信息 - 包含 next_cursor 和 has_more 字段用于翻页 ### 注意: - 与收藏夹接口的区别：本接口获取用户发布的视频，收藏夹接口获取用户收藏的视频  # [English] ### Purpose: - Get all videos published by specified user (waterfall layout). ### Parameters: - uid: User ID (required) - cursor: Pagination cursor, pass \"0\" for first request, use returned next_cursor for subsequent requests ### Return: - Video list data, including video title, cover, views, etc. - Contains next_cursor and has_more fields for pagination ### Note: - Difference from collection APIs: this API gets user published videos, collection APIs get user collected videos  # [示例/Example] uid = \"7277477906\" cursor = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :param object cursor: 分页游标/Pagination cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_user_video_list', 'GET',
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

    def fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get(self, query, **kwargs):  # noqa: E501
        """视频搜索（热门/全部）/Weibo video search (hot/all)  # noqa: E501

        # [中文] ### 用途: - 搜索微博视频内容，支持热门和全部模式。 ### 参数: - query: 搜索关键词（必填） - mode: 搜索模式 hot=热门 / all=全部（默认hot） - page: 页码（默认1） ### 返回: - 视频列表，包含微博ID、作者、内容、视频链接、互动数据 ### 注意: - 播放视频需设置Referer=https://weibo.com/  # [English] ### Purpose: - Search Weibo video content, supports hot and all modes. ### Parameters: - query: Search keyword (required) - mode: Search mode hot=popular / all=all (default hot) - page: Page number (default 1) ### Return: - Video list with weibo ID, author, content, video URL, interaction data ### Note: - Video playback requires setting Referer=https://weibo.com/  # [示例/Example] query = \"yu7\" mode = \"hot\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object mode: 搜索模式：hot=热门 / all=全部
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """视频搜索（热门/全部）/Weibo video search (hot/all)  # noqa: E501

        # [中文] ### 用途: - 搜索微博视频内容，支持热门和全部模式。 ### 参数: - query: 搜索关键词（必填） - mode: 搜索模式 hot=热门 / all=全部（默认hot） - page: 页码（默认1） ### 返回: - 视频列表，包含微博ID、作者、内容、视频链接、互动数据 ### 注意: - 播放视频需设置Referer=https://weibo.com/  # [English] ### Purpose: - Search Weibo video content, supports hot and all modes. ### Parameters: - query: Search keyword (required) - mode: Search mode hot=popular / all=all (default hot) - page: Page number (default 1) ### Return: - Video list with weibo ID, author, content, video URL, interaction data ### Note: - Video playback requires setting Referer=https://weibo.com/  # [示例/Example] query = \"yu7\" mode = \"hot\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object query: 搜索关键词/Search keyword (required)
        :param object mode: 搜索模式：hot=热门 / all=全部
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'mode', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'mode' in params:
            query_params.append(('mode', params['mode']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/fetch_video_search', 'GET',
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

    def search_user_posts_api_v1_weibo_web_v2_search_user_posts_get(self, uid, q, starttime, endtime, **kwargs):  # noqa: E501
        """搜索用户微博/Search user posts  # noqa: E501

        # [中文] ### 用途: - 在指定用户的微博中搜索包含特定关键词的内容。 ### 参数: - uid: 用户ID（必填） - q: 搜索关键词（必填） - page: 页码，从1开始（默认1） - starttime: 开始时间戳（可选，Unix时间戳格式） - endtime: 结束时间戳（可选，Unix时间戳格式） - hasori: 是否包含原创（默认1包含） - hasret: 是否包含转发（默认1包含） - hastext: 是否包含文字（默认1包含） - haspic: 是否包含图片（默认1包含） - hasvideo: 是否包含视频（默认1包含） - hasmusic: 是否包含音乐（默认1包含） ### 返回: - 搜索结果列表，包含微博内容、作者信息、互动数据等 ### 注意: - 搜索结果受用户隐私设置影响 - 时间戳参数使用Unix时间戳格式  # [English] ### Purpose: - Search for content containing specific keywords in a specified user's posts. ### Parameters: - uid: User ID (required) - q: Search keyword (required) - page: Page number, starts from 1 (default 1) - starttime: Start timestamp (optional, Unix timestamp format) - endtime: End timestamp (optional, Unix timestamp format) - hasori: Include original posts (default 1 include) - hasret: Include retweets (default 1 include) - hastext: Include text posts (default 1 include) - haspic: Include image posts (default 1 include) - hasvideo: Include video posts (default 1 include) - hasmusic: Include music posts (default 1 include) ### Return: - Search result list, including post content, author info, interaction data ### Note: - Search results affected by user privacy settings - Timestamp parameters use Unix timestamp format  # [示例/Example] uid = \"7277477906\" q = \"python\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_user_posts_api_v1_weibo_web_v2_search_user_posts_get(uid, q, starttime, endtime, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :param object q: 搜索关键词/Search keyword (required)
        :param object starttime: 开始时间戳/Start timestamp (required)
        :param object endtime: 结束时间戳/End timestamp (required)
        :param object page: 页数/Page number
        :param object hasori: 是否包含原创微博，1=包含，0=不包含/Include original posts, 1=include, 0=exclude
        :param object hasret: 是否包含转发微博，1=包含，0=不包含/Include retweets, 1=include, 0=exclude
        :param object hastext: 是否包含文字微博，1=包含，0=不包含/Include text posts, 1=include, 0=exclude
        :param object haspic: 是否包含图片微博，1=包含，0=不包含/Include image posts, 1=include, 0=exclude
        :param object hasvideo: 是否包含视频微博，1=包含，0=不包含/Include video posts, 1=include, 0=exclude
        :param object hasmusic: 是否包含音乐微博，1=包含，0=不包含/Include music posts, 1=include, 0=exclude
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_user_posts_api_v1_weibo_web_v2_search_user_posts_get_with_http_info(uid, q, starttime, endtime, **kwargs)  # noqa: E501
        else:
            (data) = self.search_user_posts_api_v1_weibo_web_v2_search_user_posts_get_with_http_info(uid, q, starttime, endtime, **kwargs)  # noqa: E501
            return data

    def search_user_posts_api_v1_weibo_web_v2_search_user_posts_get_with_http_info(self, uid, q, starttime, endtime, **kwargs):  # noqa: E501
        """搜索用户微博/Search user posts  # noqa: E501

        # [中文] ### 用途: - 在指定用户的微博中搜索包含特定关键词的内容。 ### 参数: - uid: 用户ID（必填） - q: 搜索关键词（必填） - page: 页码，从1开始（默认1） - starttime: 开始时间戳（可选，Unix时间戳格式） - endtime: 结束时间戳（可选，Unix时间戳格式） - hasori: 是否包含原创（默认1包含） - hasret: 是否包含转发（默认1包含） - hastext: 是否包含文字（默认1包含） - haspic: 是否包含图片（默认1包含） - hasvideo: 是否包含视频（默认1包含） - hasmusic: 是否包含音乐（默认1包含） ### 返回: - 搜索结果列表，包含微博内容、作者信息、互动数据等 ### 注意: - 搜索结果受用户隐私设置影响 - 时间戳参数使用Unix时间戳格式  # [English] ### Purpose: - Search for content containing specific keywords in a specified user's posts. ### Parameters: - uid: User ID (required) - q: Search keyword (required) - page: Page number, starts from 1 (default 1) - starttime: Start timestamp (optional, Unix timestamp format) - endtime: End timestamp (optional, Unix timestamp format) - hasori: Include original posts (default 1 include) - hasret: Include retweets (default 1 include) - hastext: Include text posts (default 1 include) - haspic: Include image posts (default 1 include) - hasvideo: Include video posts (default 1 include) - hasmusic: Include music posts (default 1 include) ### Return: - Search result list, including post content, author info, interaction data ### Note: - Search results affected by user privacy settings - Timestamp parameters use Unix timestamp format  # [示例/Example] uid = \"7277477906\" q = \"python\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_user_posts_api_v1_weibo_web_v2_search_user_posts_get_with_http_info(uid, q, starttime, endtime, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object uid: 用户ID/User ID (required)
        :param object q: 搜索关键词/Search keyword (required)
        :param object starttime: 开始时间戳/Start timestamp (required)
        :param object endtime: 结束时间戳/End timestamp (required)
        :param object page: 页数/Page number
        :param object hasori: 是否包含原创微博，1=包含，0=不包含/Include original posts, 1=include, 0=exclude
        :param object hasret: 是否包含转发微博，1=包含，0=不包含/Include retweets, 1=include, 0=exclude
        :param object hastext: 是否包含文字微博，1=包含，0=不包含/Include text posts, 1=include, 0=exclude
        :param object haspic: 是否包含图片微博，1=包含，0=不包含/Include image posts, 1=include, 0=exclude
        :param object hasvideo: 是否包含视频微博，1=包含，0=不包含/Include video posts, 1=include, 0=exclude
        :param object hasmusic: 是否包含音乐微博，1=包含，0=不包含/Include music posts, 1=include, 0=exclude
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'q', 'starttime', 'endtime', 'page', 'hasori', 'hasret', 'hastext', 'haspic', 'hasvideo', 'hasmusic']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_user_posts_api_v1_weibo_web_v2_search_user_posts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in params or
                                                       params['uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `uid` when calling `search_user_posts_api_v1_weibo_web_v2_search_user_posts_get`")  # noqa: E501
        # verify the required parameter 'q' is set
        if self.api_client.client_side_validation and ('q' not in params or
                                                       params['q'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `q` when calling `search_user_posts_api_v1_weibo_web_v2_search_user_posts_get`")  # noqa: E501
        # verify the required parameter 'starttime' is set
        if self.api_client.client_side_validation and ('starttime' not in params or
                                                       params['starttime'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `starttime` when calling `search_user_posts_api_v1_weibo_web_v2_search_user_posts_get`")  # noqa: E501
        # verify the required parameter 'endtime' is set
        if self.api_client.client_side_validation and ('endtime' not in params or
                                                       params['endtime'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `endtime` when calling `search_user_posts_api_v1_weibo_web_v2_search_user_posts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'starttime' in params:
            query_params.append(('starttime', params['starttime']))  # noqa: E501
        if 'endtime' in params:
            query_params.append(('endtime', params['endtime']))  # noqa: E501
        if 'hasori' in params:
            query_params.append(('hasori', params['hasori']))  # noqa: E501
        if 'hasret' in params:
            query_params.append(('hasret', params['hasret']))  # noqa: E501
        if 'hastext' in params:
            query_params.append(('hastext', params['hastext']))  # noqa: E501
        if 'haspic' in params:
            query_params.append(('haspic', params['haspic']))  # noqa: E501
        if 'hasvideo' in params:
            query_params.append(('hasvideo', params['hasvideo']))  # noqa: E501
        if 'hasmusic' in params:
            query_params.append(('hasmusic', params['hasmusic']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/weibo/web_v2/search_user_posts', 'GET',
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
