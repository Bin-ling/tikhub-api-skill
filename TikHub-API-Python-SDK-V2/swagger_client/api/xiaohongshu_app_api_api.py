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


class XiaohongshuAppAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get(self, share_link, **kwargs):  # noqa: E501
        """提取分享链接信息/Extract share link info  # noqa: E501

        # [中文] ### 用途: - 从分享链接中提取笔记ID和xsec_token ### 参数: - share_link: 小红书分享链接，支持短链接和长链接 ### 返回: - 提取的信息对象，包含：     - note_id: 笔记ID     - xsec_token: 安全令牌（如果URL中包含）  ### 使用说明: - 支持短链接格式：https://xhslink.com/a/xxxxx - 支持长链接格式：     - https://www.xiaohongshu.com/discovery/item/xxxxx     - https://www.xiaohongshu.com/explore/xxxxx - 短链接会自动重定向获取真实链接 - 提取的note_id可用于get_note_info接口  # [English] ### Purpose: - Extract note ID and xsec_token from share link ### Parameters: - share_link: Xiaohongshu share link, support short and long links ### Return: - Extracted info object containing:     - note_id: Note ID     - xsec_token: Security token (if exists in URL)  ### Usage Guide: - Supports short link format: https://xhslink.com/a/xxxxx - Supports long link formats:     - https://www.xiaohongshu.com/discovery/item/xxxxx     - https://www.xiaohongshu.com/explore/xxxxx - Short links will be auto-redirected to get real link - Extracted note_id can be used in get_note_info endpoint  # [示例/Example] share_link=\"https://xhslink.com/a/EZ4M9TwMA6c3\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get_with_http_info(share_link, **kwargs)  # noqa: E501
        else:
            (data) = self.extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get_with_http_info(share_link, **kwargs)  # noqa: E501
            return data

    def extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get_with_http_info(self, share_link, **kwargs):  # noqa: E501
        """提取分享链接信息/Extract share link info  # noqa: E501

        # [中文] ### 用途: - 从分享链接中提取笔记ID和xsec_token ### 参数: - share_link: 小红书分享链接，支持短链接和长链接 ### 返回: - 提取的信息对象，包含：     - note_id: 笔记ID     - xsec_token: 安全令牌（如果URL中包含）  ### 使用说明: - 支持短链接格式：https://xhslink.com/a/xxxxx - 支持长链接格式：     - https://www.xiaohongshu.com/discovery/item/xxxxx     - https://www.xiaohongshu.com/explore/xxxxx - 短链接会自动重定向获取真实链接 - 提取的note_id可用于get_note_info接口  # [English] ### Purpose: - Extract note ID and xsec_token from share link ### Parameters: - share_link: Xiaohongshu share link, support short and long links ### Return: - Extracted info object containing:     - note_id: Note ID     - xsec_token: Security token (if exists in URL)  ### Usage Guide: - Supports short link format: https://xhslink.com/a/xxxxx - Supports long link formats:     - https://www.xiaohongshu.com/discovery/item/xxxxx     - https://www.xiaohongshu.com/explore/xxxxx - Short links will be auto-redirected to get real link - Extracted note_id can be used in get_note_info endpoint  # [示例/Example] share_link=\"https://xhslink.com/a/EZ4M9TwMA6c3\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get_with_http_info(share_link, async_req=True)
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
                    " to method extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_link' is set
        if self.api_client.client_side_validation and ('share_link' not in params or
                                                       params['share_link'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_link` when calling `extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/app/extract_share_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get(self, note_id, **kwargs):  # noqa: E501
        """获取笔记评论/Get note comments  # noqa: E501

        # [中文] ### 用途: - 获取笔记的评论列表 ### 参数: - note_id: 笔记ID（必需） - start: 翻页游标，从上一次请求的响应中获取，支持两种格式：     1. 简单格式: \"682b0133000000001c03618d\"     2. JSON格式: {\"cursor\":\"682b0133000000001c03618d\",\"index\":2,\"pageArea\":\"ALL\"} - sort_strategy: 排序策略     - 1: 默认排序（默认值）     - 2: 按最新评论排序 ### 返回: - 评论数据对象，包含：     - comments: 评论列表数组，每个评论包含：         - id: 评论ID         - content: 评论内容         - create_time: 创建时间戳         - user_info: 评论者信息             - user_id: 用户ID             - nickname: 昵称             - image: 头像URL         - interact_info: 互动数据             - liked_count: 点赞数         - sub_comment_count: 子评论数量         - sub_comment_cursor: 子评论翻页游标（如有子评论）     - cursor: 翻页游标，用于获取下一页     - has_more: 是否有更多数据（布尔值）     - total: 总评论数  ### 翻页说明: - 首次请求不传start参数 - 获取下一页时，将上一次返回的cursor作为start参数传入 - 当has_more为false时，表示没有更多数据  # [English] ### Purpose: - Get note comments list ### Parameters: - note_id: Note ID (required) - start: Pagination cursor from previous response, supports two formats:     1. Simple format: \"682b0133000000001c03618d\"     2. JSON format: {\"cursor\":\"682b0133000000001c03618d\",\"index\":2,\"pageArea\":\"ALL\"} - sort_strategy: Sort strategy     - 1: Default sort (default)     - 2: Sort by latest comments ### Return: - Comments data object containing:     - comments: Comment list array, each comment includes:         - id: Comment ID         - content: Comment content         - create_time: Creation timestamp         - user_info: Commenter info             - user_id: User ID             - nickname: Nickname             - image: Avatar URL         - interact_info: Interaction data             - liked_count: Like count         - sub_comment_count: Sub-comment count         - sub_comment_cursor: Sub-comment pagination cursor (if has sub-comments)     - cursor: Pagination cursor for next page     - has_more: Whether has more data (boolean)     - total: Total comment count  ### Pagination Guide: - Don't pass start parameter for first request - For next page, pass cursor from previous response as start parameter - When has_more is false, no more data available  # [示例/Example] note_id=\"677d1909000000002002a892\" sort_strategy=1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object start: 翻页游标/Pagination cursor
        :param object sort_strategy: 排序策略：1-默认排序，2-最新评论/Sort strategy: 1-default, 2-latest
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get_with_http_info(note_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get_with_http_info(note_id, **kwargs)  # noqa: E501
            return data

    def get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get_with_http_info(self, note_id, **kwargs):  # noqa: E501
        """获取笔记评论/Get note comments  # noqa: E501

        # [中文] ### 用途: - 获取笔记的评论列表 ### 参数: - note_id: 笔记ID（必需） - start: 翻页游标，从上一次请求的响应中获取，支持两种格式：     1. 简单格式: \"682b0133000000001c03618d\"     2. JSON格式: {\"cursor\":\"682b0133000000001c03618d\",\"index\":2,\"pageArea\":\"ALL\"} - sort_strategy: 排序策略     - 1: 默认排序（默认值）     - 2: 按最新评论排序 ### 返回: - 评论数据对象，包含：     - comments: 评论列表数组，每个评论包含：         - id: 评论ID         - content: 评论内容         - create_time: 创建时间戳         - user_info: 评论者信息             - user_id: 用户ID             - nickname: 昵称             - image: 头像URL         - interact_info: 互动数据             - liked_count: 点赞数         - sub_comment_count: 子评论数量         - sub_comment_cursor: 子评论翻页游标（如有子评论）     - cursor: 翻页游标，用于获取下一页     - has_more: 是否有更多数据（布尔值）     - total: 总评论数  ### 翻页说明: - 首次请求不传start参数 - 获取下一页时，将上一次返回的cursor作为start参数传入 - 当has_more为false时，表示没有更多数据  # [English] ### Purpose: - Get note comments list ### Parameters: - note_id: Note ID (required) - start: Pagination cursor from previous response, supports two formats:     1. Simple format: \"682b0133000000001c03618d\"     2. JSON format: {\"cursor\":\"682b0133000000001c03618d\",\"index\":2,\"pageArea\":\"ALL\"} - sort_strategy: Sort strategy     - 1: Default sort (default)     - 2: Sort by latest comments ### Return: - Comments data object containing:     - comments: Comment list array, each comment includes:         - id: Comment ID         - content: Comment content         - create_time: Creation timestamp         - user_info: Commenter info             - user_id: User ID             - nickname: Nickname             - image: Avatar URL         - interact_info: Interaction data             - liked_count: Like count         - sub_comment_count: Sub-comment count         - sub_comment_cursor: Sub-comment pagination cursor (if has sub-comments)     - cursor: Pagination cursor for next page     - has_more: Whether has more data (boolean)     - total: Total comment count  ### Pagination Guide: - Don't pass start parameter for first request - For next page, pass cursor from previous response as start parameter - When has_more is false, no more data available  # [示例/Example] note_id=\"677d1909000000002002a892\" sort_strategy=1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get_with_http_info(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object start: 翻页游标/Pagination cursor
        :param object sort_strategy: 排序策略：1-默认排序，2-最新评论/Sort strategy: 1-default, 2-latest
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id', 'start', 'sort_strategy']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'sort_strategy' in params:
            query_params.append(('sort_strategy', params['sort_strategy']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/get_note_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_note_info_v1_api_v1_xiaohongshu_app_get_note_info_get(self, **kwargs):  # noqa: E501
        """获取笔记信息 V1/Get note info V1  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息 V1 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记详情数据，包含以下主要字段：     - note_id: 笔记ID     - title: 笔记标题     - desc: 笔记内容描述     - type: 笔记类型（normal=图文笔记，video=视频笔记）     - user: 作者信息对象         - user_id: 用户ID         - nickname: 用户昵称         - avatar: 用户头像URL     - image_list: 图片列表（图文笔记）     - video_info: 视频信息（视频笔记）     - interact_info: 互动数据         - liked_count: 点赞数         - collected_count: 收藏数         - comment_count: 评论数         - share_count: 分享数     - tag_list: 话题标签列表     - time: 发布时间戳     - ip_location: IP属地  # [English] ### Purpose: - Get note info V1 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note detail data with main fields:     - note_id: Note ID     - title: Note title     - desc: Note content description     - type: Note type (normal=image note, video=video note)     - user: Author info object         - user_id: User ID         - nickname: User nickname         - avatar: User avatar URL     - image_list: Image list (for image notes)     - video_info: Video info (for video notes)     - interact_info: Interaction data         - liked_count: Like count         - collected_count: Collect count         - comment_count: Comment count         - share_count: Share count     - tag_list: Topic tag list     - time: Publish timestamp     - ip_location: IP location  # [示例/Example] note_id=\"665f95200000000006005624\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v1_api_v1_xiaohongshu_app_get_note_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID
        :param object share_text: 分享链接/Share link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_note_info_v1_api_v1_xiaohongshu_app_get_note_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_note_info_v1_api_v1_xiaohongshu_app_get_note_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_note_info_v1_api_v1_xiaohongshu_app_get_note_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取笔记信息 V1/Get note info V1  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息 V1 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记详情数据，包含以下主要字段：     - note_id: 笔记ID     - title: 笔记标题     - desc: 笔记内容描述     - type: 笔记类型（normal=图文笔记，video=视频笔记）     - user: 作者信息对象         - user_id: 用户ID         - nickname: 用户昵称         - avatar: 用户头像URL     - image_list: 图片列表（图文笔记）     - video_info: 视频信息（视频笔记）     - interact_info: 互动数据         - liked_count: 点赞数         - collected_count: 收藏数         - comment_count: 评论数         - share_count: 分享数     - tag_list: 话题标签列表     - time: 发布时间戳     - ip_location: IP属地  # [English] ### Purpose: - Get note info V1 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note detail data with main fields:     - note_id: Note ID     - title: Note title     - desc: Note content description     - type: Note type (normal=image note, video=video note)     - user: Author info object         - user_id: User ID         - nickname: User nickname         - avatar: User avatar URL     - image_list: Image list (for image notes)     - video_info: Video info (for video notes)     - interact_info: Interaction data         - liked_count: Like count         - collected_count: Collect count         - comment_count: Comment count         - share_count: Share count     - tag_list: Topic tag list     - time: Publish timestamp     - ip_location: IP location  # [示例/Example] note_id=\"665f95200000000006005624\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v1_api_v1_xiaohongshu_app_get_note_info_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID
        :param object share_text: 分享链接/Share link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id', 'share_text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_note_info_v1_api_v1_xiaohongshu_app_get_note_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501
        if 'share_text' in params:
            query_params.append(('share_text', params['share_text']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/get_note_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_note_info_v2_api_v1_xiaohongshu_app_get_note_info_v2_get(self, **kwargs):  # noqa: E501
        """获取笔记信息 V2 (蒲公英商家后台)/Get note info V2 (Pugongying Business Backend)  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息 V2 - 除赞、评、藏数据之外此接口能获取到笔记的曝光量（impNum）、阅读量（readNum）、关注量（followCnt）。 - 但是不是每一篇都有，如果是没有被小红书后台收录的笔记，赞评藏数据返回为0，但是笔记内容是完整的。 - 通过作者userId，可以去作品列表接口拿到赞、评、藏数据 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记详情数据，包含以下主要字段：     - note_id: 笔记ID     - title: 笔记标题     - desc: 笔记内容描述     - type: 笔记类型（normal=图文笔记，video=视频笔记）     - user: 作者信息对象         - user_id: 用户ID         - nickname: 用户昵称         - avatar: 用户头像URL     - image_list: 图片列表（图文笔记）     - video_info: 视频信息（视频笔记）     - interact_info: 互动数据         - liked_count: 点赞数         - collected_count: 收藏数         - comment_count: 评论数         - share_count: 分享数     - tag_list: 话题标签列表     - time: 发布时间戳     - ip_location: IP属地  # [English] ### Purpose: - Get note info V2 - This interface can get note exposure (impNum), read count (readNum), and follow count (followCnt) in addition to like, comment, and collect data. - However, not every note has this data. If the note is not indexed by Xiaohongshu backend, like, comment, and collect data will return 0, but the note content is complete. - You can get like, comment, and collect data from the note list interface using the author's userId. ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note detail data with main fields:     - note_id: Note ID     - title: Note title     - desc: Note content description     - type: Note type (normal=image note, video=video note)     - user: Author info object         - user_id: User ID         - nickname: User nickname         - avatar: User avatar URL     - image_list: Image list (for image notes)     - video_info: Video info (for video notes)     - interact_info: Interaction data         - liked_count: Like count         - collected_count: Collect count         - comment_count: Comment count         - share_count: Share count     - tag_list: Topic tag list     - time: Publish timestamp     - ip_location: IP location  # [示例/Example] note_id=\"665f95200000000006005624\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v2_api_v1_xiaohongshu_app_get_note_info_v2_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID
        :param object share_text: 分享链接/Share link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_note_info_v2_api_v1_xiaohongshu_app_get_note_info_v2_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_note_info_v2_api_v1_xiaohongshu_app_get_note_info_v2_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_note_info_v2_api_v1_xiaohongshu_app_get_note_info_v2_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取笔记信息 V2 (蒲公英商家后台)/Get note info V2 (Pugongying Business Backend)  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息 V2 - 除赞、评、藏数据之外此接口能获取到笔记的曝光量（impNum）、阅读量（readNum）、关注量（followCnt）。 - 但是不是每一篇都有，如果是没有被小红书后台收录的笔记，赞评藏数据返回为0，但是笔记内容是完整的。 - 通过作者userId，可以去作品列表接口拿到赞、评、藏数据 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记详情数据，包含以下主要字段：     - note_id: 笔记ID     - title: 笔记标题     - desc: 笔记内容描述     - type: 笔记类型（normal=图文笔记，video=视频笔记）     - user: 作者信息对象         - user_id: 用户ID         - nickname: 用户昵称         - avatar: 用户头像URL     - image_list: 图片列表（图文笔记）     - video_info: 视频信息（视频笔记）     - interact_info: 互动数据         - liked_count: 点赞数         - collected_count: 收藏数         - comment_count: 评论数         - share_count: 分享数     - tag_list: 话题标签列表     - time: 发布时间戳     - ip_location: IP属地  # [English] ### Purpose: - Get note info V2 - This interface can get note exposure (impNum), read count (readNum), and follow count (followCnt) in addition to like, comment, and collect data. - However, not every note has this data. If the note is not indexed by Xiaohongshu backend, like, comment, and collect data will return 0, but the note content is complete. - You can get like, comment, and collect data from the note list interface using the author's userId. ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note detail data with main fields:     - note_id: Note ID     - title: Note title     - desc: Note content description     - type: Note type (normal=image note, video=video note)     - user: Author info object         - user_id: User ID         - nickname: User nickname         - avatar: User avatar URL     - image_list: Image list (for image notes)     - video_info: Video info (for video notes)     - interact_info: Interaction data         - liked_count: Like count         - collected_count: Collect count         - comment_count: Comment count         - share_count: Share count     - tag_list: Topic tag list     - time: Publish timestamp     - ip_location: IP location  # [示例/Example] note_id=\"665f95200000000006005624\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v2_api_v1_xiaohongshu_app_get_note_info_v2_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID
        :param object share_text: 分享链接/Share link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id', 'share_text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_note_info_v2_api_v1_xiaohongshu_app_get_note_info_v2_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501
        if 'share_text' in params:
            query_params.append(('share_text', params['share_text']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/get_note_info_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get(self, page_id, first_load_time, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 根据话题标签获取作品/Get notes by topic  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。 ### 用途: - 根据话题标签获取相关笔记 ### 参数: - page_id: 话题标签ID（必需） - first_load_time: 首次请求的时间戳，毫秒级时间戳（必需）     - 例子: 1698647850000     - Python获取当前时间戳: `int(time.time() * 1000)` - sort: 排序方式     - \"hot\": 综合排序（默认）     - \"time\": 最新发布     - \"trend\": 最热门 - session_id: 会话ID，首次不传，由服务端生成，翻页时传入 - last_note_ct: 最后一条笔记的create_time字段，首次不传，翻页时传入 - last_note_id: 最后一条笔记的ID，首次不传，翻页时传入 - cursor_score: 最后一条笔记的cursor_score字段，首次不传，翻页时传入 ### 返回: - 话题笔记数据，包含：     - notes: 笔记列表数组，每个元素包含：         - id: 元素ID         - model_type: 模型类型（通常为\"note\"）         - note: 笔记详情对象             - note_id: 笔记ID             - title: 标题             - desc: 描述             - type: 类型（normal/video）             - user: 作者信息             - interact_info: 互动数据             - cover: 封面图             - create_time: 创建时间戳             - cursor_score: 游标分数（用于翻页）     - session_id: 会话ID（翻页必需）     - has_more: 是否有更多数据  ### 翻页说明: - 首次请求：只传page_id和first_load_time - 翻页请求：需要传入     1. 上一次返回的session_id     2. 最后一条笔记的last_note_ct（create_time）     3. 最后一条笔记的last_note_id（id）     4. 最后一条笔记的cursor_score  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. ### Purpose: - Get notes by topic tag ### Parameters: - page_id: Topic tag ID (required) - first_load_time: First load timestamp in milliseconds (required)     - Example: 1698647850000     - Get current timestamp in Python: `int(time.time() * 1000)` - sort: Sort method     - \"hot\": Comprehensive (default)     - \"time\": Latest published     - \"trend\": Trending - session_id: Session ID, not required for first request, use returned value for pagination - last_note_ct: Last note create_time field for pagination - last_note_id: Last note ID for pagination - cursor_score: Last note cursor_score field for pagination ### Return: - Topic notes data containing:     - notes: Notes list array, each element includes:         - id: Element ID         - model_type: Model type (usually \"note\")         - note: Note detail object             - note_id: Note ID             - title: Title             - desc: Description             - type: Type (normal/video)             - user: Author info             - interact_info: Interaction data             - cover: Cover image             - create_time: Creation timestamp             - cursor_score: Cursor score (for pagination)     - session_id: Session ID (required for pagination)     - has_more: Whether has more data  ### Pagination Guide: - First request: Only pass page_id and first_load_time - Next requests: Need to pass     1. session_id from previous response     2. last_note_ct (create_time of last note)     3. last_note_id (id of last note)     4. cursor_score of last note  # [示例/Example] page_id=\"5c014b045b29cb0001ead530\" first_load_time=\"1698647850000\" sort=\"hot\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get(page_id, first_load_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page_id: 话题标签ID/Topic tag ID (required)
        :param object first_load_time: 首次请求时间戳（毫秒）/First load timestamp (ms) (required)
        :param object sort: 排序方式：hot-综合，time-最新，trend-最热/Sort: hot-comprehensive, time-latest, trend-trending
        :param object session_id: 会话ID/Session ID
        :param object last_note_ct: 最后一条笔记创建时间/Last note create time
        :param object last_note_id: 最后一条笔记ID/Last note ID
        :param object cursor_score: 游标分数/Cursor score
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get_with_http_info(page_id, first_load_time, **kwargs)  # noqa: E501
        else:
            (data) = self.get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get_with_http_info(page_id, first_load_time, **kwargs)  # noqa: E501
            return data

    def get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get_with_http_info(self, page_id, first_load_time, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 根据话题标签获取作品/Get notes by topic  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。 ### 用途: - 根据话题标签获取相关笔记 ### 参数: - page_id: 话题标签ID（必需） - first_load_time: 首次请求的时间戳，毫秒级时间戳（必需）     - 例子: 1698647850000     - Python获取当前时间戳: `int(time.time() * 1000)` - sort: 排序方式     - \"hot\": 综合排序（默认）     - \"time\": 最新发布     - \"trend\": 最热门 - session_id: 会话ID，首次不传，由服务端生成，翻页时传入 - last_note_ct: 最后一条笔记的create_time字段，首次不传，翻页时传入 - last_note_id: 最后一条笔记的ID，首次不传，翻页时传入 - cursor_score: 最后一条笔记的cursor_score字段，首次不传，翻页时传入 ### 返回: - 话题笔记数据，包含：     - notes: 笔记列表数组，每个元素包含：         - id: 元素ID         - model_type: 模型类型（通常为\"note\"）         - note: 笔记详情对象             - note_id: 笔记ID             - title: 标题             - desc: 描述             - type: 类型（normal/video）             - user: 作者信息             - interact_info: 互动数据             - cover: 封面图             - create_time: 创建时间戳             - cursor_score: 游标分数（用于翻页）     - session_id: 会话ID（翻页必需）     - has_more: 是否有更多数据  ### 翻页说明: - 首次请求：只传page_id和first_load_time - 翻页请求：需要传入     1. 上一次返回的session_id     2. 最后一条笔记的last_note_ct（create_time）     3. 最后一条笔记的last_note_id（id）     4. 最后一条笔记的cursor_score  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. ### Purpose: - Get notes by topic tag ### Parameters: - page_id: Topic tag ID (required) - first_load_time: First load timestamp in milliseconds (required)     - Example: 1698647850000     - Get current timestamp in Python: `int(time.time() * 1000)` - sort: Sort method     - \"hot\": Comprehensive (default)     - \"time\": Latest published     - \"trend\": Trending - session_id: Session ID, not required for first request, use returned value for pagination - last_note_ct: Last note create_time field for pagination - last_note_id: Last note ID for pagination - cursor_score: Last note cursor_score field for pagination ### Return: - Topic notes data containing:     - notes: Notes list array, each element includes:         - id: Element ID         - model_type: Model type (usually \"note\")         - note: Note detail object             - note_id: Note ID             - title: Title             - desc: Description             - type: Type (normal/video)             - user: Author info             - interact_info: Interaction data             - cover: Cover image             - create_time: Creation timestamp             - cursor_score: Cursor score (for pagination)     - session_id: Session ID (required for pagination)     - has_more: Whether has more data  ### Pagination Guide: - First request: Only pass page_id and first_load_time - Next requests: Need to pass     1. session_id from previous response     2. last_note_ct (create_time of last note)     3. last_note_id (id of last note)     4. cursor_score of last note  # [示例/Example] page_id=\"5c014b045b29cb0001ead530\" first_load_time=\"1698647850000\" sort=\"hot\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get_with_http_info(page_id, first_load_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page_id: 话题标签ID/Topic tag ID (required)
        :param object first_load_time: 首次请求时间戳（毫秒）/First load timestamp (ms) (required)
        :param object sort: 排序方式：hot-综合，time-最新，trend-最热/Sort: hot-comprehensive, time-latest, trend-trending
        :param object session_id: 会话ID/Session ID
        :param object last_note_ct: 最后一条笔记创建时间/Last note create time
        :param object last_note_id: 最后一条笔记ID/Last note ID
        :param object cursor_score: 游标分数/Cursor score
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_id', 'first_load_time', 'sort', 'session_id', 'last_note_ct', 'last_note_id', 'cursor_score']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_id' is set
        if self.api_client.client_side_validation and ('page_id' not in params or
                                                       params['page_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page_id` when calling `get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get`")  # noqa: E501
        # verify the required parameter 'first_load_time' is set
        if self.api_client.client_side_validation and ('first_load_time' not in params or
                                                       params['first_load_time'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `first_load_time` when calling `get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_id' in params:
            query_params.append(('page_id', params['page_id']))  # noqa: E501
        if 'first_load_time' in params:
            query_params.append(('first_load_time', params['first_load_time']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501
        if 'last_note_ct' in params:
            query_params.append(('last_note_ct', params['last_note_ct']))  # noqa: E501
        if 'last_note_id' in params:
            query_params.append(('last_note_id', params['last_note_id']))  # noqa: E501
        if 'cursor_score' in params:
            query_params.append(('cursor_score', params['cursor_score']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/get_notes_by_topic', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get(self, sku_id, **kwargs):  # noqa: E501
        """获取商品详情/Get product detail  # noqa: E501

        # [中文] ### 用途: - 获取小红书商品详情信息 ### 参数: - sku_id: 商品skuId（必需） ### 返回: - 商品详情数据  # [English] ### Purpose: - Get Xiaohongshu product detail info ### Parameters: - sku_id: Product SKU ID (required) ### Return: - Product detail data  # [示例/Example] sku_id=\"68be7cbc8c331700011f89d1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get(sku_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sku_id: 商品skuId/Product SKU ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get_with_http_info(sku_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get_with_http_info(sku_id, **kwargs)  # noqa: E501
            return data

    def get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get_with_http_info(self, sku_id, **kwargs):  # noqa: E501
        """获取商品详情/Get product detail  # noqa: E501

        # [中文] ### 用途: - 获取小红书商品详情信息 ### 参数: - sku_id: 商品skuId（必需） ### 返回: - 商品详情数据  # [English] ### Purpose: - Get Xiaohongshu product detail info ### Parameters: - sku_id: Product SKU ID (required) ### Return: - Product detail data  # [示例/Example] sku_id=\"68be7cbc8c331700011f89d1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get_with_http_info(sku_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object sku_id: 商品skuId/Product SKU ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sku_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku_id' is set
        if self.api_client.client_side_validation and ('sku_id' not in params or
                                                       params['sku_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sku_id` when calling `get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sku_id' in params:
            query_params.append(('sku_id', params['sku_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/get_product_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get(self, note_id, comment_id, **kwargs):  # noqa: E501
        """获取子评论/Get sub comments  # noqa: E501

        # [中文] ### 用途: - 获取评论的子评论（回复）列表 ### 参数: - note_id: 笔记ID（必需） - comment_id: 一级评论ID，要查看哪条评论的子评论（必需） - start: 翻页游标，从上一次请求的响应中获取，从评论列表的最后一条子评论ID获取：     格式如下: \"6806642d000000001f01991b\" ### 返回: - 子评论列表数组，每个子评论包含：     - id: 子评论ID     - content: 评论内容     - create_time: 创建时间戳     - user_info: 评论者信息         - user_id: 用户ID         - nickname: 昵称         - image: 头像URL     - target_comment: 被回复的评论信息（如果是回复其他子评论）         - id: 被回复评论ID         - user_info: 被回复者信息             - nickname: 被回复者昵称  ### 翻页说明: - 首次请求不传start参数 - 获取更多时，将上一次请求返回的最后一条子评论ID作为start参数  # [English] ### Purpose: - Get sub comments (replies) list ### Parameters: - note_id: Note ID (required) - comment_id: Parent comment ID to get sub comments (required) - start: Pagination cursor from previous response, obtained from the last sub-comment ID in the comment list:     Format: \"6806642d000000001f01991b\" ### Return: - Sub comments array list, each sub-comment includes:     - id: Sub-comment ID     - content: Comment content     - create_time: Creation timestamp     - user_info: Commenter info         - user_id: User ID         - nickname: Nickname         - image: Avatar URL     - target_comment: Replied comment info (if replying to other sub-comment)         - id: Replied comment ID         - user_info: Replied user info             - nickname: Replied user nickname  ### Pagination Guide: - Don't pass start parameter for first request - For more data, pass last sub-comment ID from previous response as start parameter  # [示例/Example] note_id=\"677d1909000000002002a892\" comment_id=\"677f67e400000000220013f3\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get(note_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object comment_id: 一级评论ID/Parent comment ID (required)
        :param object start: 翻页游标/Pagination cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get_with_http_info(note_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get_with_http_info(note_id, comment_id, **kwargs)  # noqa: E501
            return data

    def get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get_with_http_info(self, note_id, comment_id, **kwargs):  # noqa: E501
        """获取子评论/Get sub comments  # noqa: E501

        # [中文] ### 用途: - 获取评论的子评论（回复）列表 ### 参数: - note_id: 笔记ID（必需） - comment_id: 一级评论ID，要查看哪条评论的子评论（必需） - start: 翻页游标，从上一次请求的响应中获取，从评论列表的最后一条子评论ID获取：     格式如下: \"6806642d000000001f01991b\" ### 返回: - 子评论列表数组，每个子评论包含：     - id: 子评论ID     - content: 评论内容     - create_time: 创建时间戳     - user_info: 评论者信息         - user_id: 用户ID         - nickname: 昵称         - image: 头像URL     - target_comment: 被回复的评论信息（如果是回复其他子评论）         - id: 被回复评论ID         - user_info: 被回复者信息             - nickname: 被回复者昵称  ### 翻页说明: - 首次请求不传start参数 - 获取更多时，将上一次请求返回的最后一条子评论ID作为start参数  # [English] ### Purpose: - Get sub comments (replies) list ### Parameters: - note_id: Note ID (required) - comment_id: Parent comment ID to get sub comments (required) - start: Pagination cursor from previous response, obtained from the last sub-comment ID in the comment list:     Format: \"6806642d000000001f01991b\" ### Return: - Sub comments array list, each sub-comment includes:     - id: Sub-comment ID     - content: Comment content     - create_time: Creation timestamp     - user_info: Commenter info         - user_id: User ID         - nickname: Nickname         - image: Avatar URL     - target_comment: Replied comment info (if replying to other sub-comment)         - id: Replied comment ID         - user_info: Replied user info             - nickname: Replied user nickname  ### Pagination Guide: - Don't pass start parameter for first request - For more data, pass last sub-comment ID from previous response as start parameter  # [示例/Example] note_id=\"677d1909000000002002a892\" comment_id=\"677f67e400000000220013f3\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get_with_http_info(note_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object comment_id: 一级评论ID/Parent comment ID (required)
        :param object start: 翻页游标/Pagination cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id', 'comment_id', 'start']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/get_sub_comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get(self, share_link, **kwargs):  # noqa: E501
        """从分享链接中提取用户ID和xsec_token/Extract user ID and xsec_token from share link  # noqa: E501

        # [中文] ### 用途: - 从用户分享链接中提取用户ID和xsec_token ### 参数: - share_link: 小红书用户分享链接，支持短链接和长链接 ### 返回: - 提取的信息对象，包含：     - user_id: 用户ID     - xsec_token: 安全令牌（如果URL中包含）  ### 使用说明: - 支持短链接格式：https://xhslink.com/m/xxxxx - 支持长链接格式：https://www.xiaohongshu.com/user/profile/xxxxx - 提取的user_id可用于get_user_info接口  # [English] ### Purpose: - Extract user ID and xsec_token from user share link ### Parameters: - share_link: Xiaohongshu user share link, support short and long links ### Return: - Extracted info object containing:     - user_id: User ID     - xsec_token: Security token (if exists in URL)  ### Usage Guide: - Supports short link format: https://xhslink.com/m/xxxxx - Supports long link format: https://www.xiaohongshu.com/user/profile/xxxxx - Extracted user_id can be used in get_user_info endpoint # [示例/Example] share_link=\"https://xhslink.com/m/Ap1vXtgAixh\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: 用户分享链接/User share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get_with_http_info(share_link, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get_with_http_info(share_link, **kwargs)  # noqa: E501
            return data

    def get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get_with_http_info(self, share_link, **kwargs):  # noqa: E501
        """从分享链接中提取用户ID和xsec_token/Extract user ID and xsec_token from share link  # noqa: E501

        # [中文] ### 用途: - 从用户分享链接中提取用户ID和xsec_token ### 参数: - share_link: 小红书用户分享链接，支持短链接和长链接 ### 返回: - 提取的信息对象，包含：     - user_id: 用户ID     - xsec_token: 安全令牌（如果URL中包含）  ### 使用说明: - 支持短链接格式：https://xhslink.com/m/xxxxx - 支持长链接格式：https://www.xiaohongshu.com/user/profile/xxxxx - 提取的user_id可用于get_user_info接口  # [English] ### Purpose: - Extract user ID and xsec_token from user share link ### Parameters: - share_link: Xiaohongshu user share link, support short and long links ### Return: - Extracted info object containing:     - user_id: User ID     - xsec_token: Security token (if exists in URL)  ### Usage Guide: - Supports short link format: https://xhslink.com/m/xxxxx - Supports long link format: https://www.xiaohongshu.com/user/profile/xxxxx - Extracted user_id can be used in get_user_info endpoint # [示例/Example] share_link=\"https://xhslink.com/m/Ap1vXtgAixh\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get_with_http_info(share_link, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_link: 用户分享链接/User share link (required)
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
                    " to method get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_link' is set
        if self.api_client.client_side_validation and ('share_link' not in params or
                                                       params['share_link'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_link` when calling `get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/app/get_user_id_and_xsec_token', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_info_api_v1_xiaohongshu_app_get_user_info_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息/Get user info  # noqa: E501

        # [中文] ### 用途: - 获取用户详情信息 ### 参数: - user_id: 用户ID（必需） ### 返回: - 用户详情数据，包含：     - user_id: 用户ID     - nickname: 昵称     - desc: 个人简介     - gender: 性别（0=女，1=男，2=未知）     - images: 头像URL     - imageb: 背景图URL     - red_official_verify_type: 官方认证类型（0=无，1=个人，2=机构）     - red_official_verify_show: 是否显示认证标识     - level: 等级信息         - image: 等级图标URL         - name: 等级名称     - follows: 关注数     - fans: 粉丝数     - interaction: 获赞与收藏总数     - notes: 笔记数     - boards: 专辑数     - location: 所在地     - collected: 收藏数     - liked: 点赞数  # [English] ### Purpose: - Get user detail info ### Parameters: - user_id: User ID (required) ### Return: - User detail data including:     - user_id: User ID     - nickname: Nickname     - desc: Personal bio     - gender: Gender (0=female, 1=male, 2=unknown)     - images: Avatar URL     - imageb: Background image URL     - red_official_verify_type: Official verify type (0=none, 1=personal, 2=organization)     - red_official_verify_show: Whether show verify badge     - level: Level info         - image: Level icon URL         - name: Level name     - follows: Following count     - fans: Fans count     - interaction: Total likes & collects     - notes: Notes count     - boards: Album count     - location: Location     - collected: Collect count     - liked: Like count  # [示例/Example] user_id=\"5c2f338a000000000701e1c6\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_info_api_v1_xiaohongshu_app_get_user_info_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_info_api_v1_xiaohongshu_app_get_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_info_api_v1_xiaohongshu_app_get_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_info_api_v1_xiaohongshu_app_get_user_info_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息/Get user info  # noqa: E501

        # [中文] ### 用途: - 获取用户详情信息 ### 参数: - user_id: 用户ID（必需） ### 返回: - 用户详情数据，包含：     - user_id: 用户ID     - nickname: 昵称     - desc: 个人简介     - gender: 性别（0=女，1=男，2=未知）     - images: 头像URL     - imageb: 背景图URL     - red_official_verify_type: 官方认证类型（0=无，1=个人，2=机构）     - red_official_verify_show: 是否显示认证标识     - level: 等级信息         - image: 等级图标URL         - name: 等级名称     - follows: 关注数     - fans: 粉丝数     - interaction: 获赞与收藏总数     - notes: 笔记数     - boards: 专辑数     - location: 所在地     - collected: 收藏数     - liked: 点赞数  # [English] ### Purpose: - Get user detail info ### Parameters: - user_id: User ID (required) ### Return: - User detail data including:     - user_id: User ID     - nickname: Nickname     - desc: Personal bio     - gender: Gender (0=female, 1=male, 2=unknown)     - images: Avatar URL     - imageb: Background image URL     - red_official_verify_type: Official verify type (0=none, 1=personal, 2=organization)     - red_official_verify_show: Whether show verify badge     - level: Level info         - image: Level icon URL         - name: Level name     - follows: Following count     - fans: Fans count     - interaction: Total likes & collects     - notes: Notes count     - boards: Album count     - location: Location     - collected: Collect count     - liked: Like count  # [示例/Example] user_id=\"5c2f338a000000000701e1c6\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_info_api_v1_xiaohongshu_app_get_user_info_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_info_api_v1_xiaohongshu_app_get_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_info_api_v1_xiaohongshu_app_get_user_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/get_user_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户作品列表/Get user notes  # noqa: E501

        # [中文] ### 用途: - 获取用户发布的笔记列表 ### 参数: - user_id: 用户ID（必需） - cursor: 翻页索引，上一次请求返回的cursor字段，不传默认请求第一页 - cursor取值方式为notes列表的最后一条笔记的note_id ### 返回: - 用户笔记列表数据，包含：     - notes: 笔记数组，每个笔记包含：         - note_id: 笔记ID         - type: 类型（normal=图文，video=视频）         - display_title: 标题         - desc: 描述         - liked_count: 点赞数         - cover: 封面图信息             - url: 图片URL             - width: 宽度             - height: 高度         - user: 作者信息（通常与查询用户相同）     - cursor: 翻页游标     - has_more: 是否有更多数据  ### 翻页说明: - 首次请求：只传user_id - 翻页请求：传入上一次返回的cursor - 当has_more为false时，表示没有更多笔记  # [English] ### Purpose: - Get user's published notes list ### Parameters: - user_id: User ID (required) - cursor: Pagination cursor from previous response, omit for first page - Cursor value is the note_id of the last note in the notes list ### Return: - User notes data including:     - notes: Notes array, each note contains:         - note_id: Note ID         - type: Type (normal=image, video=video)         - display_title: Title         - desc: Description         - liked_count: Like count         - cover: Cover image info             - url: Image URL             - width: Width             - height: Height         - user: Author info (usually same as queried user)     - cursor: Pagination cursor     - has_more: Whether has more data  ### Pagination Guide: - First request: Only pass user_id - Next pages: Pass cursor from previous response - When has_more is false, no more notes available  # [示例/Example] user_id=\"5c57e6a4000000001802a013\" cursor=\"67ee399f000000001c02f36f\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页游标/Pagination cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户作品列表/Get user notes  # noqa: E501

        # [中文] ### 用途: - 获取用户发布的笔记列表 ### 参数: - user_id: 用户ID（必需） - cursor: 翻页索引，上一次请求返回的cursor字段，不传默认请求第一页 - cursor取值方式为notes列表的最后一条笔记的note_id ### 返回: - 用户笔记列表数据，包含：     - notes: 笔记数组，每个笔记包含：         - note_id: 笔记ID         - type: 类型（normal=图文，video=视频）         - display_title: 标题         - desc: 描述         - liked_count: 点赞数         - cover: 封面图信息             - url: 图片URL             - width: 宽度             - height: 高度         - user: 作者信息（通常与查询用户相同）     - cursor: 翻页游标     - has_more: 是否有更多数据  ### 翻页说明: - 首次请求：只传user_id - 翻页请求：传入上一次返回的cursor - 当has_more为false时，表示没有更多笔记  # [English] ### Purpose: - Get user's published notes list ### Parameters: - user_id: User ID (required) - cursor: Pagination cursor from previous response, omit for first page - Cursor value is the note_id of the last note in the notes list ### Return: - User notes data including:     - notes: Notes array, each note contains:         - note_id: Note ID         - type: Type (normal=image, video=video)         - display_title: Title         - desc: Description         - liked_count: Like count         - cover: Cover image info             - url: Image URL             - width: Width             - height: Height         - user: Author info (usually same as queried user)     - cursor: Pagination cursor     - has_more: Whether has more data  ### Pagination Guide: - First request: Only pass user_id - Next pages: Pass cursor from previous response - When has_more is false, no more notes available  # [示例/Example] user_id=\"5c57e6a4000000001802a013\" cursor=\"67ee399f000000001c02f36f\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 翻页游标/Pagination cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/get_user_notes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_video_note_info_api_v1_xiaohongshu_app_get_video_note_info_get(self, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 获取视频笔记信息 V1/ Get video note info V1  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用 `get_note_info` 接口替代。 ### 用途: - 获取视频笔记信息 V1 - 视频笔记用这个接口，成功率高。 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记详情数据，包含以下主要字段：     - note_id: 笔记ID     - title: 笔记标题     - desc: 笔记内容描述     - type: 笔记类型（normal=图文笔记，video=视频笔记）     - user: 作者信息对象         - user_id: 用户ID         - nickname: 用户昵称         - avatar: 用户头像URL     - image_list: 图片列表（图文笔记）     - video_info: 视频信息（视频笔记）     - interact_info: 互动数据         - liked_count: 点赞数         - collected_count: 收藏数         - comment_count: 评论数         - share_count: 分享数     - tag_list: 话题标签列表     - time: 发布时间戳     - ip_location: IP属地  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the `get_note_info` endpoint instead. ### Purpose: - Get video note info V1 - Use this interface for video notes, higher success rate. ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note detail data with main fields:     - note_id: Note ID     - title: Note title     - desc: Note content description     - type: Note type (normal=image note, video=video note)     - user: Author info object         - user_id: User ID         - nickname: User nickname         - avatar: User avatar URL     - image_list: Image list (for image notes)     - video_info: Video info (for video notes)     - interact_info: Interaction data         - liked_count: Like count         - collected_count: Collect count         - comment_count: Comment count         - share_count: Share count     - tag_list: Topic tag list     - time: Publish timestamp     - ip_location: IP location  # [示例/Example] note_id=\"681b87cd0000000022027853\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_note_info_api_v1_xiaohongshu_app_get_video_note_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID
        :param object share_text: 分享链接/Share link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_video_note_info_api_v1_xiaohongshu_app_get_video_note_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_video_note_info_api_v1_xiaohongshu_app_get_video_note_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_video_note_info_api_v1_xiaohongshu_app_get_video_note_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 获取视频笔记信息 V1/ Get video note info V1  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用 `get_note_info` 接口替代。 ### 用途: - 获取视频笔记信息 V1 - 视频笔记用这个接口，成功率高。 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记详情数据，包含以下主要字段：     - note_id: 笔记ID     - title: 笔记标题     - desc: 笔记内容描述     - type: 笔记类型（normal=图文笔记，video=视频笔记）     - user: 作者信息对象         - user_id: 用户ID         - nickname: 用户昵称         - avatar: 用户头像URL     - image_list: 图片列表（图文笔记）     - video_info: 视频信息（视频笔记）     - interact_info: 互动数据         - liked_count: 点赞数         - collected_count: 收藏数         - comment_count: 评论数         - share_count: 分享数     - tag_list: 话题标签列表     - time: 发布时间戳     - ip_location: IP属地  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the `get_note_info` endpoint instead. ### Purpose: - Get video note info V1 - Use this interface for video notes, higher success rate. ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note detail data with main fields:     - note_id: Note ID     - title: Note title     - desc: Note content description     - type: Note type (normal=image note, video=video note)     - user: Author info object         - user_id: User ID         - nickname: User nickname         - avatar: User avatar URL     - image_list: Image list (for image notes)     - video_info: Video info (for video notes)     - interact_info: Interaction data         - liked_count: Like count         - collected_count: Collect count         - comment_count: Comment count         - share_count: Share count     - tag_list: Topic tag list     - time: Publish timestamp     - ip_location: IP location  # [示例/Example] note_id=\"681b87cd0000000022027853\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_note_info_api_v1_xiaohongshu_app_get_video_note_info_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID
        :param object share_text: 分享链接/Share link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id', 'share_text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_note_info_api_v1_xiaohongshu_app_get_video_note_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501
        if 'share_text' in params:
            query_params.append(('share_text', params['share_text']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/get_video_note_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_notes_api_v1_xiaohongshu_app_search_notes_get(self, keyword, page, **kwargs):  # noqa: E501
        """搜索笔记/Search notes  # noqa: E501

        # [中文] ### 用途: - 搜索小红书笔记 ### 参数: - keyword: 要搜索的关键词（必需） - page: 第几页，从1开始（必需） - search_id: 搜索ID，第一次请求可不传，服务端会生成searchId，翻页时需要携带服务端返回的searchId - session_id: 会话ID，第一次请求可不传，服务端会生成sessionId，翻页时携带服务端返回的sessionId - sort_type: 排序规则     - \"general\": 综合排序（默认）     - \"time_descending\": 最新发布     - \"popularity_descending\": 最多点赞     - \"comment_descending\": 最多评论     - \"collect_descending\": 最多收藏 - filter_note_type: 筛选笔记类型     - \"不限\": 所有类型（默认）     - \"视频笔记\": 仅视频     - \"普通笔记\": 仅图文 - filter_note_time: 筛选笔记发布时间     - \"不限\": 所有时间（默认）     - \"一天内\": 24小时内     - \"一周内\": 7天内     - \"半年内\": 6个月内 ### 返回: - 搜索结果数据，包含：     - items: 搜索结果列表，每个元素包含：         - id: 元素ID         - model_type: 模型类型（通常为\"note\"）         - note: 笔记详情             - note_id: 笔记ID             - type: 类型（normal=图文，video=视频）             - display_title: 标题（关键词会高亮）             - desc: 内容描述（搜索接口无法返回完整的 desc，仅部分内容，请使用笔记详情接口获取完整内容）             - user: 作者信息             - interact_info: 互动数据                 - liked_count: 点赞数             - cover: 封面图信息     - searchId: 搜索ID（翻页必需，不同关键词不要复用）     - sessionId: 会话ID（翻页必需）     - has_more: 是否有更多数据     - total_count: 搜索结果总数  ### 翻页说明: - 首次搜索：只传keyword和page=1 - 翻页搜索：传入相同keyword，递增page，并携带首次返回的searchId和sessionId - 注意：更换关键词时不要复用之前的searchId  # [English] ### Purpose: - Search Xiaohongshu notes ### Parameters: - keyword: Search keyword (required) - page: Page number, start from 1 (required) - search_id: Search ID, optional for first request, required for pagination - session_id: Session ID, optional for first request, required for pagination - sort_type: Sort method     - \"general\": Comprehensive (default)     - \"time_descending\": Latest published     - \"popularity_descending\": Most liked     - \"comment_descending\": Most commented     - \"collect_descending\": Most collected - filter_note_type: Note type filter     - \"不限\": All types (default)     - \"视频笔记\": Video only     - \"普通笔记\": Image & text only - filter_note_time: Time filter     - \"不限\": All time (default)     - \"一天内\": Within 24 hours     - \"一周内\": Within 7 days     - \"半年内\": Within 6 months ### Return: - Search results data containing:     - items: Search results list, each element includes:         - id: Element ID         - model_type: Model type (usually \"note\")         - note: Note details             - note_id: Note ID             - type: Type (normal=image, video=video)             - display_title: Title (keywords highlighted)             - desc: Content description (incomplete in search results, use note detail API for full content)             - user: Author info             - interact_info: Interaction data                 - liked_count: Like count             - cover: Cover image info     - searchId: Search ID (required for pagination, don't reuse for different keywords)     - sessionId: Session ID (required for pagination)     - has_more: Whether has more data     - total_count: Total search results count  ### Pagination Guide: - First search: Only pass keyword and page=1 - Next pages: Pass same keyword, increment page, include searchId and sessionId from first response - Note: Don't reuse searchId when changing keywords  # [示例/Example] keyword=\"猫粮\" page=1 sort_type=\"general\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_notes_api_v1_xiaohongshu_app_search_notes_get(keyword, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码（从1开始）/Page number (start from 1) (required)
        :param object search_id: 搜索ID，翻页时使用/Search ID for pagination
        :param object session_id: 会话ID，翻页时使用/Session ID for pagination
        :param object sort_type: 排序方式/Sort type
        :param object filter_note_type: 笔记类型筛选：不限、视频笔记、普通笔记/Note type filter
        :param object filter_note_time: 发布时间筛选：不限、一天内、一周内、半年内/Time filter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_notes_api_v1_xiaohongshu_app_search_notes_get_with_http_info(keyword, page, **kwargs)  # noqa: E501
        else:
            (data) = self.search_notes_api_v1_xiaohongshu_app_search_notes_get_with_http_info(keyword, page, **kwargs)  # noqa: E501
            return data

    def search_notes_api_v1_xiaohongshu_app_search_notes_get_with_http_info(self, keyword, page, **kwargs):  # noqa: E501
        """搜索笔记/Search notes  # noqa: E501

        # [中文] ### 用途: - 搜索小红书笔记 ### 参数: - keyword: 要搜索的关键词（必需） - page: 第几页，从1开始（必需） - search_id: 搜索ID，第一次请求可不传，服务端会生成searchId，翻页时需要携带服务端返回的searchId - session_id: 会话ID，第一次请求可不传，服务端会生成sessionId，翻页时携带服务端返回的sessionId - sort_type: 排序规则     - \"general\": 综合排序（默认）     - \"time_descending\": 最新发布     - \"popularity_descending\": 最多点赞     - \"comment_descending\": 最多评论     - \"collect_descending\": 最多收藏 - filter_note_type: 筛选笔记类型     - \"不限\": 所有类型（默认）     - \"视频笔记\": 仅视频     - \"普通笔记\": 仅图文 - filter_note_time: 筛选笔记发布时间     - \"不限\": 所有时间（默认）     - \"一天内\": 24小时内     - \"一周内\": 7天内     - \"半年内\": 6个月内 ### 返回: - 搜索结果数据，包含：     - items: 搜索结果列表，每个元素包含：         - id: 元素ID         - model_type: 模型类型（通常为\"note\"）         - note: 笔记详情             - note_id: 笔记ID             - type: 类型（normal=图文，video=视频）             - display_title: 标题（关键词会高亮）             - desc: 内容描述（搜索接口无法返回完整的 desc，仅部分内容，请使用笔记详情接口获取完整内容）             - user: 作者信息             - interact_info: 互动数据                 - liked_count: 点赞数             - cover: 封面图信息     - searchId: 搜索ID（翻页必需，不同关键词不要复用）     - sessionId: 会话ID（翻页必需）     - has_more: 是否有更多数据     - total_count: 搜索结果总数  ### 翻页说明: - 首次搜索：只传keyword和page=1 - 翻页搜索：传入相同keyword，递增page，并携带首次返回的searchId和sessionId - 注意：更换关键词时不要复用之前的searchId  # [English] ### Purpose: - Search Xiaohongshu notes ### Parameters: - keyword: Search keyword (required) - page: Page number, start from 1 (required) - search_id: Search ID, optional for first request, required for pagination - session_id: Session ID, optional for first request, required for pagination - sort_type: Sort method     - \"general\": Comprehensive (default)     - \"time_descending\": Latest published     - \"popularity_descending\": Most liked     - \"comment_descending\": Most commented     - \"collect_descending\": Most collected - filter_note_type: Note type filter     - \"不限\": All types (default)     - \"视频笔记\": Video only     - \"普通笔记\": Image & text only - filter_note_time: Time filter     - \"不限\": All time (default)     - \"一天内\": Within 24 hours     - \"一周内\": Within 7 days     - \"半年内\": Within 6 months ### Return: - Search results data containing:     - items: Search results list, each element includes:         - id: Element ID         - model_type: Model type (usually \"note\")         - note: Note details             - note_id: Note ID             - type: Type (normal=image, video=video)             - display_title: Title (keywords highlighted)             - desc: Content description (incomplete in search results, use note detail API for full content)             - user: Author info             - interact_info: Interaction data                 - liked_count: Like count             - cover: Cover image info     - searchId: Search ID (required for pagination, don't reuse for different keywords)     - sessionId: Session ID (required for pagination)     - has_more: Whether has more data     - total_count: Total search results count  ### Pagination Guide: - First search: Only pass keyword and page=1 - Next pages: Pass same keyword, increment page, include searchId and sessionId from first response - Note: Don't reuse searchId when changing keywords  # [示例/Example] keyword=\"猫粮\" page=1 sort_type=\"general\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_notes_api_v1_xiaohongshu_app_search_notes_get_with_http_info(keyword, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码（从1开始）/Page number (start from 1) (required)
        :param object search_id: 搜索ID，翻页时使用/Search ID for pagination
        :param object session_id: 会话ID，翻页时使用/Session ID for pagination
        :param object sort_type: 排序方式/Sort type
        :param object filter_note_type: 笔记类型筛选：不限、视频笔记、普通笔记/Note type filter
        :param object filter_note_time: 发布时间筛选：不限、一天内、一周内、半年内/Time filter
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page', 'search_id', 'session_id', 'sort_type', 'filter_note_type', 'filter_note_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_notes_api_v1_xiaohongshu_app_search_notes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_notes_api_v1_xiaohongshu_app_search_notes_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if self.api_client.client_side_validation and ('page' not in params or
                                                       params['page'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page` when calling `search_notes_api_v1_xiaohongshu_app_search_notes_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'filter_note_type' in params:
            query_params.append(('filter_note_type', params['filter_note_type']))  # noqa: E501
        if 'filter_note_time' in params:
            query_params.append(('filter_note_time', params['filter_note_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/search_notes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_notes_v2_api_v1_xiaohongshu_app_search_notes_v2_get(self, keyword, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 搜索笔记 V2/Search notes V2  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用 `search_notes` 接口替代。 ### 用途: - 搜索笔记 ### 参数: - keyword: 搜索关键词 - page: 页码，默认为1 - sort: 排序方式     - 综合排序（默认参数）: general     - 最热排序: popularity_descending     - 最新排序: time_descending     - 最多评论: comment_descending     - 最多收藏: collect_descending - noteType: 笔记类型     - 综合笔记（默认参数）: _0     - 视频笔记: _1     - 图文笔记: _2     - 直播: _3 - noteTime: 发布时间     - 不限: \"\"     - 一天内 :一天内     - 一周内 :一周内     - 半年内 :半年内 ### 返回: - 笔记列表  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the `search_notes` endpoint instead. ### Purpose: - Search notes ### Parameters: - keyword: Keyword - page: Page, default is 1 - sort: Sort     - General sort (default): general     - Popularity sort: popularity_descending     - Latest sort: time_descending     - Most comments: comment_descending     - Most favorites: collect_descending - noteType: Note type     - General note (default): _0     - Video note: _1     - Image note: _2     - Live: _3 - noteTime: Release time     - No limit: \"\"     - Within one day: 一天内     - Within one week: 一周内     - Within half a year: 半年内 ### Return: - Note list  # [示例/Example] keyword=\"美食\" page=1 sort=\"general\" noteType=\"_0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_notes_v2_api_v1_xiaohongshu_app_search_notes_v2_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Keyword (required)
        :param object page: 页码/Page
        :param object sort: 排序方式/Sort
        :param object note_type: 笔记类型/Note type
        :param object note_time: 发布时间/Release time
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_notes_v2_api_v1_xiaohongshu_app_search_notes_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_notes_v2_api_v1_xiaohongshu_app_search_notes_v2_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_notes_v2_api_v1_xiaohongshu_app_search_notes_v2_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 搜索笔记 V2/Search notes V2  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用 `search_notes` 接口替代。 ### 用途: - 搜索笔记 ### 参数: - keyword: 搜索关键词 - page: 页码，默认为1 - sort: 排序方式     - 综合排序（默认参数）: general     - 最热排序: popularity_descending     - 最新排序: time_descending     - 最多评论: comment_descending     - 最多收藏: collect_descending - noteType: 笔记类型     - 综合笔记（默认参数）: _0     - 视频笔记: _1     - 图文笔记: _2     - 直播: _3 - noteTime: 发布时间     - 不限: \"\"     - 一天内 :一天内     - 一周内 :一周内     - 半年内 :半年内 ### 返回: - 笔记列表  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the `search_notes` endpoint instead. ### Purpose: - Search notes ### Parameters: - keyword: Keyword - page: Page, default is 1 - sort: Sort     - General sort (default): general     - Popularity sort: popularity_descending     - Latest sort: time_descending     - Most comments: comment_descending     - Most favorites: collect_descending - noteType: Note type     - General note (default): _0     - Video note: _1     - Image note: _2     - Live: _3 - noteTime: Release time     - No limit: \"\"     - Within one day: 一天内     - Within one week: 一周内     - Within half a year: 半年内 ### Return: - Note list  # [示例/Example] keyword=\"美食\" page=1 sort=\"general\" noteType=\"_0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_notes_v2_api_v1_xiaohongshu_app_search_notes_v2_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Keyword (required)
        :param object page: 页码/Page
        :param object sort: 排序方式/Sort
        :param object note_type: 笔记类型/Note type
        :param object note_time: 发布时间/Release time
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page', 'sort', 'note_type', 'note_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_notes_v2_api_v1_xiaohongshu_app_search_notes_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_notes_v2_api_v1_xiaohongshu_app_search_notes_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'note_type' in params:
            query_params.append(('noteType', params['note_type']))  # noqa: E501
        if 'note_time' in params:
            query_params.append(('noteTime', params['note_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/search_notes_v2', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_products_api_v1_xiaohongshu_app_search_products_get(self, keyword, page, **kwargs):  # noqa: E501
        """搜索商品/Search products  # noqa: E501

        # [中文] ### 用途: - 搜索小红书商品 ### 参数: - keyword: 搜索关键词（必需） - page: 页码，从1开始（必需） - search_id: 搜索ID，第一次请求可不传，翻页时需要携带服务端返回的searchId - session_id: 会话ID，第一次请求可不传，翻页时携带服务端返回的sessionId - sort: 排序规则，默认综合     - \"sales_qty\": 销量     - \"price_asc\": 价格升序     - \"price_desc\": 价格降序 - scope: 搜索范围，默认不限     - \"purchased\": 买过的店     - \"following\": 关注的店 - service_guarantee: 物流权益，多选用英文逗号分割     - 可选值: \"24小时发货\", \"七天无理由\", \"现货\", \"退货包运费\" - min_price: 最低价 - max_price: 最高价 - super_promotion: 标签ID ### 返回: - 搜索结果数据，包含：     - items: 商品列表     - searchId: 搜索ID（翻页必需）     - sessionId: 会话ID（翻页必需）     - has_more: 是否有更多数据  ### 翻页说明: - 首次搜索：只传keyword和page=1 - 翻页搜索：传入相同keyword，递增page，并携带首次返回的searchId和sessionId - 注意：更换关键词时不要复用之前的searchId  # [English] ### Purpose: - Search Xiaohongshu products ### Parameters: - keyword: Search keyword (required) - page: Page number, start from 1 (required) - search_id: Search ID, optional for first request, required for pagination - session_id: Session ID, optional for first request, required for pagination - sort: Sort method     - \"sales_qty\": By sales     - \"price_asc\": Price ascending     - \"price_desc\": Price descending - scope: Search scope     - \"purchased\": Shops you've bought from     - \"following\": Shops you follow - service_guarantee: Service guarantees, comma separated     - Options: \"24小时发货\", \"七天无理由\", \"现货\", \"退货包运费\" - min_price: Minimum price - max_price: Maximum price - super_promotion: Promotion tag ID ### 返回: - Search results containing:     - items: Product list     - searchId: Search ID (required for pagination)     - sessionId: Session ID (required for pagination)     - has_more: Whether has more data  ### Pagination Guide: - First search: Only pass keyword and page=1 - Next pages: Pass same keyword, increment page, include searchId and sessionId - Note: Don't reuse searchId when changing keywords  # [示例/Example] keyword=\"充电宝\" page=1 sort=\"sales_qty\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_products_api_v1_xiaohongshu_app_search_products_get(keyword, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码（从1开始）/Page number (start from 1) (required)
        :param object search_id: 搜索ID，翻页时使用/Search ID for pagination
        :param object session_id: 会话ID，翻页时使用/Session ID for pagination
        :param object sort: 排序规则：sales_qty-销量、price_asc-价格升序、price_desc-价格降序/Sort: sales_qty, price_asc, price_desc
        :param object scope: 搜索范围：purchased-买过的店、following-关注的店/Scope: purchased, following
        :param object service_guarantee: 物流权益，多选用英文逗号分割/Service guarantee, comma separated
        :param object min_price: 最低价/Min price
        :param object max_price: 最高价/Max price
        :param object super_promotion: 标签ID/Promotion tag ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_products_api_v1_xiaohongshu_app_search_products_get_with_http_info(keyword, page, **kwargs)  # noqa: E501
        else:
            (data) = self.search_products_api_v1_xiaohongshu_app_search_products_get_with_http_info(keyword, page, **kwargs)  # noqa: E501
            return data

    def search_products_api_v1_xiaohongshu_app_search_products_get_with_http_info(self, keyword, page, **kwargs):  # noqa: E501
        """搜索商品/Search products  # noqa: E501

        # [中文] ### 用途: - 搜索小红书商品 ### 参数: - keyword: 搜索关键词（必需） - page: 页码，从1开始（必需） - search_id: 搜索ID，第一次请求可不传，翻页时需要携带服务端返回的searchId - session_id: 会话ID，第一次请求可不传，翻页时携带服务端返回的sessionId - sort: 排序规则，默认综合     - \"sales_qty\": 销量     - \"price_asc\": 价格升序     - \"price_desc\": 价格降序 - scope: 搜索范围，默认不限     - \"purchased\": 买过的店     - \"following\": 关注的店 - service_guarantee: 物流权益，多选用英文逗号分割     - 可选值: \"24小时发货\", \"七天无理由\", \"现货\", \"退货包运费\" - min_price: 最低价 - max_price: 最高价 - super_promotion: 标签ID ### 返回: - 搜索结果数据，包含：     - items: 商品列表     - searchId: 搜索ID（翻页必需）     - sessionId: 会话ID（翻页必需）     - has_more: 是否有更多数据  ### 翻页说明: - 首次搜索：只传keyword和page=1 - 翻页搜索：传入相同keyword，递增page，并携带首次返回的searchId和sessionId - 注意：更换关键词时不要复用之前的searchId  # [English] ### Purpose: - Search Xiaohongshu products ### Parameters: - keyword: Search keyword (required) - page: Page number, start from 1 (required) - search_id: Search ID, optional for first request, required for pagination - session_id: Session ID, optional for first request, required for pagination - sort: Sort method     - \"sales_qty\": By sales     - \"price_asc\": Price ascending     - \"price_desc\": Price descending - scope: Search scope     - \"purchased\": Shops you've bought from     - \"following\": Shops you follow - service_guarantee: Service guarantees, comma separated     - Options: \"24小时发货\", \"七天无理由\", \"现货\", \"退货包运费\" - min_price: Minimum price - max_price: Maximum price - super_promotion: Promotion tag ID ### 返回: - Search results containing:     - items: Product list     - searchId: Search ID (required for pagination)     - sessionId: Session ID (required for pagination)     - has_more: Whether has more data  ### Pagination Guide: - First search: Only pass keyword and page=1 - Next pages: Pass same keyword, increment page, include searchId and sessionId - Note: Don't reuse searchId when changing keywords  # [示例/Example] keyword=\"充电宝\" page=1 sort=\"sales_qty\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_products_api_v1_xiaohongshu_app_search_products_get_with_http_info(keyword, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码（从1开始）/Page number (start from 1) (required)
        :param object search_id: 搜索ID，翻页时使用/Search ID for pagination
        :param object session_id: 会话ID，翻页时使用/Session ID for pagination
        :param object sort: 排序规则：sales_qty-销量、price_asc-价格升序、price_desc-价格降序/Sort: sales_qty, price_asc, price_desc
        :param object scope: 搜索范围：purchased-买过的店、following-关注的店/Scope: purchased, following
        :param object service_guarantee: 物流权益，多选用英文逗号分割/Service guarantee, comma separated
        :param object min_price: 最低价/Min price
        :param object max_price: 最高价/Max price
        :param object super_promotion: 标签ID/Promotion tag ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page', 'search_id', 'session_id', 'sort', 'scope', 'service_guarantee', 'min_price', 'max_price', 'super_promotion']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_products_api_v1_xiaohongshu_app_search_products_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_products_api_v1_xiaohongshu_app_search_products_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if self.api_client.client_side_validation and ('page' not in params or
                                                       params['page'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page` when calling `search_products_api_v1_xiaohongshu_app_search_products_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'search_id' in params:
            query_params.append(('search_id', params['search_id']))  # noqa: E501
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501
        if 'service_guarantee' in params:
            query_params.append(('service_guarantee', params['service_guarantee']))  # noqa: E501
        if 'min_price' in params:
            query_params.append(('min_price', params['min_price']))  # noqa: E501
        if 'max_price' in params:
            query_params.append(('max_price', params['max_price']))  # noqa: E501
        if 'super_promotion' in params:
            query_params.append(('super_promotion', params['super_promotion']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/search_products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_users_api_v1_xiaohongshu_app_search_users_get(self, keyword, page, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 搜索用户/Search users  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。 ### 用途: - 搜索小红书用户 ### 参数: - keyword: 要搜索的关键词（必需） - page: 第几页，从1开始（必需） ### 返回: - 用户搜索结果，包含：     - users: 用户列表数组，每个元素包含：         - user: 用户信息对象             - user_id: 用户ID             - nickname: 昵称             - images: 头像URL             - desc: 个人简介             - red_official_verify_type: 官方认证类型（0=无，1=个人，2=机构）             - follows: 关注数             - fans: 粉丝数             - interaction: 获赞与收藏总数             - notes: 笔记数     - has_more: 是否有更多数据  ### 翻页说明: - 首次搜索：只传keyword和page=1 - 翻页搜索：传入相同keyword，递增page  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. ### Purpose: - Search Xiaohongshu users ### Parameters: - keyword: Search keyword (required) - page: Page number, start from 1 (required) ### Return: - User search results containing:     - users: Users list array, each element includes:         - user: User info object             - user_id: User ID             - nickname: Nickname             - images: Avatar URL             - desc: Personal bio             - red_official_verify_type: Official verify type (0=none, 1=personal, 2=organization)             - follows: Following count             - fans: Fans count             - interaction: Total likes & collects             - notes: Notes count     - has_more: Whether has more data  ### Pagination Guide: - First search: Only pass keyword and page=1 - Next pages: Pass same keyword, increment page, include searchId from first response  # [示例/Example] keyword=\"美食博主\" page=1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_api_v1_xiaohongshu_app_search_users_get(keyword, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码（从1开始）/Page number (start from 1) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_users_api_v1_xiaohongshu_app_search_users_get_with_http_info(keyword, page, **kwargs)  # noqa: E501
        else:
            (data) = self.search_users_api_v1_xiaohongshu_app_search_users_get_with_http_info(keyword, page, **kwargs)  # noqa: E501
            return data

    def search_users_api_v1_xiaohongshu_app_search_users_get_with_http_info(self, keyword, page, **kwargs):  # noqa: E501
        """[已弃用/Deprecated] 搜索用户/Search users  # noqa: E501

        # [中文] ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。 ### 用途: - 搜索小红书用户 ### 参数: - keyword: 要搜索的关键词（必需） - page: 第几页，从1开始（必需） ### 返回: - 用户搜索结果，包含：     - users: 用户列表数组，每个元素包含：         - user: 用户信息对象             - user_id: 用户ID             - nickname: 昵称             - images: 头像URL             - desc: 个人简介             - red_official_verify_type: 官方认证类型（0=无，1=个人，2=机构）             - follows: 关注数             - fans: 粉丝数             - interaction: 获赞与收藏总数             - notes: 笔记数     - has_more: 是否有更多数据  ### 翻页说明: - 首次搜索：只传keyword和page=1 - 翻页搜索：传入相同keyword，递增page  # [English] ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. ### Purpose: - Search Xiaohongshu users ### Parameters: - keyword: Search keyword (required) - page: Page number, start from 1 (required) ### Return: - User search results containing:     - users: Users list array, each element includes:         - user: User info object             - user_id: User ID             - nickname: Nickname             - images: Avatar URL             - desc: Personal bio             - red_official_verify_type: Official verify type (0=none, 1=personal, 2=organization)             - follows: Following count             - fans: Fans count             - interaction: Total likes & collects             - notes: Notes count     - has_more: Whether has more data  ### Pagination Guide: - First search: Only pass keyword and page=1 - Next pages: Pass same keyword, increment page, include searchId from first response  # [示例/Example] keyword=\"美食博主\" page=1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_api_v1_xiaohongshu_app_search_users_get_with_http_info(keyword, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search keyword (required)
        :param object page: 页码（从1开始）/Page number (start from 1) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_users_api_v1_xiaohongshu_app_search_users_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_users_api_v1_xiaohongshu_app_search_users_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if self.api_client.client_side_validation and ('page' not in params or
                                                       params['page'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `page` when calling `search_users_api_v1_xiaohongshu_app_search_users_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/app/search_users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
