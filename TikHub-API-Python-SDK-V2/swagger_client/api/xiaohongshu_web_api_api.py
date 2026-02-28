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


class XiaohongshuWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_home_recommend_api_v1_xiaohongshu_web_get_home_recommend_post(self, **kwargs):  # noqa: E501
        """获取首页推荐/Get home recommend  # noqa: E501

        # [中文] ### 用途: - 获取首页推荐 ### 参数: - feed_type: 推荐类型     - 全部: 0     - 穿搭: 1     - 美食: 2     - 彩妆: 3     - 影视: 4     - 职场: 5     - 情感: 6     - 家居: 7     - 游戏: 8     - 旅行: 9     - 健身: 10 - need_filter_image: 是否只看图文笔记，默认为 False - cookie: 可选参数，用户自行提供的已登录的网页Cookie获取个性化推荐，如果不提供，则使用游客模式 - proxy: 可选参数，网络代理，可降低封号概率，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port ### 返回: - 推荐列表  # [English] ### Purpose: - Get home recommend ### Parameters: - feed_type: Feed type     - Dress: 1     - Food: 2     - Makeup: 3     - Film: 4     - Workplace: 5     - Emotion: 6     - Home: 7     - Game: 8     - Travel: 9     - Fitness: 10 - need_filter_image: Whether to view only image notes, default is False - cookie: Optional parameter, user-provided logged-in web Cookie to get personalized recommendations, if not provided, use visitor mode - proxy: Optional parameter, network proxy, can reduce the probability of account ban, format: http://username:password@IP:port ### Return: - Recommend list  # [示例/Example] feed_type=\"0\" need_filter_image=False  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_home_recommend_api_v1_xiaohongshu_web_get_home_recommend_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_home_recommend_api_v1_xiaohongshu_web_get_home_recommend_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_home_recommend_api_v1_xiaohongshu_web_get_home_recommend_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_home_recommend_api_v1_xiaohongshu_web_get_home_recommend_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取首页推荐/Get home recommend  # noqa: E501

        # [中文] ### 用途: - 获取首页推荐 ### 参数: - feed_type: 推荐类型     - 全部: 0     - 穿搭: 1     - 美食: 2     - 彩妆: 3     - 影视: 4     - 职场: 5     - 情感: 6     - 家居: 7     - 游戏: 8     - 旅行: 9     - 健身: 10 - need_filter_image: 是否只看图文笔记，默认为 False - cookie: 可选参数，用户自行提供的已登录的网页Cookie获取个性化推荐，如果不提供，则使用游客模式 - proxy: 可选参数，网络代理，可降低封号概率，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port ### 返回: - 推荐列表  # [English] ### Purpose: - Get home recommend ### Parameters: - feed_type: Feed type     - Dress: 1     - Food: 2     - Makeup: 3     - Film: 4     - Workplace: 5     - Emotion: 6     - Home: 7     - Game: 8     - Travel: 9     - Fitness: 10 - need_filter_image: Whether to view only image notes, default is False - cookie: Optional parameter, user-provided logged-in web Cookie to get personalized recommendations, if not provided, use visitor mode - proxy: Optional parameter, network proxy, can reduce the probability of account ban, format: http://username:password@IP:port ### Return: - Recommend list  # [示例/Example] feed_type=\"0\" need_filter_image=False  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_home_recommend_api_v1_xiaohongshu_web_get_home_recommend_post_with_http_info(async_req=True)
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
                    " to method get_home_recommend_api_v1_xiaohongshu_web_get_home_recommend_post" % key
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
            '/api/v1/xiaohongshu/web/get_home_recommend', 'POST',
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

    def get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get(self, note_id, comment_id, **kwargs):  # noqa: E501
        """获取笔记评论回复 V1/Get note comment replies V1  # noqa: E501

        # [中文] ### 用途: - 获取笔记评论回复 V1 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - comment_id: 评论ID - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的游标 ### 返回: - 笔记评论回复列表  # [English] ### Purpose: - Get note comment replies V1 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - comment_id: Comment ID - lastCursor: Last cursor, empty for the first request, use the cursor returned in the last response for subsequent requests ### Return: - Note comment replies list  # [示例/Example] note_id=\"6683b283000000001f0052bf\" comment_id=\"6683ec5b000000000303b91a\" lastCursor=None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get(note_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object comment_id: 评论ID/Comment ID (required)
        :param object last_cursor: 上一页的游标/Last cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get_with_http_info(note_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get_with_http_info(note_id, comment_id, **kwargs)  # noqa: E501
            return data

    def get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get_with_http_info(self, note_id, comment_id, **kwargs):  # noqa: E501
        """获取笔记评论回复 V1/Get note comment replies V1  # noqa: E501

        # [中文] ### 用途: - 获取笔记评论回复 V1 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - comment_id: 评论ID - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的游标 ### 返回: - 笔记评论回复列表  # [English] ### Purpose: - Get note comment replies V1 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - comment_id: Comment ID - lastCursor: Last cursor, empty for the first request, use the cursor returned in the last response for subsequent requests ### Return: - Note comment replies list  # [示例/Example] note_id=\"6683b283000000001f0052bf\" comment_id=\"6683ec5b000000000303b91a\" lastCursor=None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get_with_http_info(note_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object comment_id: 评论ID/Comment ID (required)
        :param object last_cursor: 上一页的游标/Last cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id', 'comment_id', 'last_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'last_cursor' in params:
            query_params.append(('lastCursor', params['last_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web/get_note_comment_replies', 'GET',
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

    def get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get(self, note_id, **kwargs):  # noqa: E501
        """获取笔记评论 V1/Get note comments V1  # noqa: E501

        # [中文] ### 用途: - 获取笔记评论 V1 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的游标 ### 返回: - 笔记评论列表  # [English] ### Purpose: - Get note comments V1 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - lastCursor: Last cursor, empty for the first request, use the cursor returned in the last response for subsequent requests ### Return: - Note comments list  # [示例/Example] note_id=\"6683b283000000001f0052bf\" lastCursor=None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object last_cursor: 上一页的游标/Last cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get_with_http_info(note_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get_with_http_info(note_id, **kwargs)  # noqa: E501
            return data

    def get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get_with_http_info(self, note_id, **kwargs):  # noqa: E501
        """获取笔记评论 V1/Get note comments V1  # noqa: E501

        # [中文] ### 用途: - 获取笔记评论 V1 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的游标 ### 返回: - 笔记评论列表  # [English] ### Purpose: - Get note comments V1 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - lastCursor: Last cursor, empty for the first request, use the cursor returned in the last response for subsequent requests ### Return: - Note comments list  # [示例/Example] note_id=\"6683b283000000001f0052bf\" lastCursor=None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get_with_http_info(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object last_cursor: 上一页的游标/Last cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id', 'last_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501
        if 'last_cursor' in params:
            query_params.append(('lastCursor', params['last_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web/get_note_comments', 'GET',
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

    def get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get(self, share_text, **kwargs):  # noqa: E501
        """通过分享链接获取小红书的Note ID 和 xsec_token/Get Xiaohongshu Note ID and xsec_token by share link  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取小红书的Note ID 和 xsec_token ### 参数: - share_text: 小红书分享链接（支持APP和Web端分享链接） ### 返回: - Note ID 和 xsec_token  # [English] ### Purpose: - Get Xiaohongshu Note ID and xsec_token by share link ### Parameters: - share_text: Xiaohongshu sharing link (support APP and Web sharing link) ### Return: - Note ID and xsec_token  # [示例/Example] share_text=\"https://xhslink.com/a/EZ4M9TwMA6c3\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get(share_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get_with_http_info(share_text, **kwargs)  # noqa: E501
        else:
            (data) = self.get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get_with_http_info(share_text, **kwargs)  # noqa: E501
            return data

    def get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get_with_http_info(self, share_text, **kwargs):  # noqa: E501
        """通过分享链接获取小红书的Note ID 和 xsec_token/Get Xiaohongshu Note ID and xsec_token by share link  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取小红书的Note ID 和 xsec_token ### 参数: - share_text: 小红书分享链接（支持APP和Web端分享链接） ### 返回: - Note ID 和 xsec_token  # [English] ### Purpose: - Get Xiaohongshu Note ID and xsec_token by share link ### Parameters: - share_text: Xiaohongshu sharing link (support APP and Web sharing link) ### Return: - Note ID and xsec_token  # [示例/Example] share_text=\"https://xhslink.com/a/EZ4M9TwMA6c3\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get_with_http_info(share_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: 分享链接/Share link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['share_text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'share_text' is set
        if self.api_client.client_side_validation and ('share_text' not in params or
                                                       params['share_text'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `share_text` when calling `get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_text' in params:
            query_params.append(('share_text', params['share_text']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web/get_note_id_and_xsec_token', 'GET',
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

    def get_note_info_v2_api_v1_xiaohongshu_web_get_note_info_v2_get(self, **kwargs):  # noqa: E501
        """获取笔记信息 V2/Get note info V2  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息 V2 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记信息  # [English] ### Purpose: - Get note info V2 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note info  # [示例/Example] note_id=\"665f95200000000006005624\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v2_api_v1_xiaohongshu_web_get_note_info_v2_get(async_req=True)
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
            return self.get_note_info_v2_api_v1_xiaohongshu_web_get_note_info_v2_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_note_info_v2_api_v1_xiaohongshu_web_get_note_info_v2_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_note_info_v2_api_v1_xiaohongshu_web_get_note_info_v2_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取笔记信息 V2/Get note info V2  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息 V2 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记信息  # [English] ### Purpose: - Get note info V2 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note info  # [示例/Example] note_id=\"665f95200000000006005624\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v2_api_v1_xiaohongshu_web_get_note_info_v2_get_with_http_info(async_req=True)
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
                    " to method get_note_info_v2_api_v1_xiaohongshu_web_get_note_info_v2_get" % key
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
            '/api/v1/xiaohongshu/web/get_note_info_v2', 'GET',
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

    def get_note_info_v4_api_v1_xiaohongshu_web_get_note_info_v4_get(self, **kwargs):  # noqa: E501
        """获取笔记信息 V4/Get note info V4  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息V4 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记信息  # [English] ### Purpose: - Get note info V4 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note info  # [示例/Example] note_id=\"665f95200000000006005624\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v4_api_v1_xiaohongshu_web_get_note_info_v4_get(async_req=True)
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
            return self.get_note_info_v4_api_v1_xiaohongshu_web_get_note_info_v4_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_note_info_v4_api_v1_xiaohongshu_web_get_note_info_v4_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_note_info_v4_api_v1_xiaohongshu_web_get_note_info_v4_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取笔记信息 V4/Get note info V4  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息V4 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记信息  # [English] ### Purpose: - Get note info V4 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note info  # [示例/Example] note_id=\"665f95200000000006005624\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v4_api_v1_xiaohongshu_web_get_note_info_v4_get_with_http_info(async_req=True)
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
                    " to method get_note_info_v4_api_v1_xiaohongshu_web_get_note_info_v4_get" % key
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
            '/api/v1/xiaohongshu/web/get_note_info_v4', 'GET',
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

    def get_note_info_v5_api_v1_xiaohongshu_web_get_note_info_v5_post(self, **kwargs):  # noqa: E501
        """获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie)  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息V5，用户自行提供Cookie来获取笔记信息 - 此接口收费0.001$ ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - xsec_token: X-Sec-Token，可以从搜索接口中获取，分享链接中也有/X-Sec-Token, can be obtained from the search interface, also in the sharing link - cookie: 用户自行提供的已登录的网页Cookie - proxy: 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port - 最好使用代理，避免被封号或其他未知问题。  ### 返回: - 笔记信息  # [English] ### Purpose: - Get note info V5, user provides Cookie to get note info - This interface charges 0.001$ ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - xsec_token: X-Sec-Token, can be obtained from the search interface, also in the sharing link - cookie: User provided logged-in web Cookie - proxy: Proxy, format: http://username:password@IP:port - It is recommended to use a proxy to avoid being banned or other unknown issues. ### Return: - Note info  # [示例/Example] note_id = \"67855d09000000001703d449\" xsec_token = \"ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo=\" cookie = \"Your Cookie\" proxy = \"http://username:password@IP:port\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v5_api_v1_xiaohongshu_web_get_note_info_v5_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_note_info_v5_api_v1_xiaohongshu_web_get_note_info_v5_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_note_info_v5_api_v1_xiaohongshu_web_get_note_info_v5_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_note_info_v5_api_v1_xiaohongshu_web_get_note_info_v5_post_with_http_info(self, **kwargs):  # noqa: E501
        """获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie)  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息V5，用户自行提供Cookie来获取笔记信息 - 此接口收费0.001$ ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - xsec_token: X-Sec-Token，可以从搜索接口中获取，分享链接中也有/X-Sec-Token, can be obtained from the search interface, also in the sharing link - cookie: 用户自行提供的已登录的网页Cookie - proxy: 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port - 最好使用代理，避免被封号或其他未知问题。  ### 返回: - 笔记信息  # [English] ### Purpose: - Get note info V5, user provides Cookie to get note info - This interface charges 0.001$ ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - xsec_token: X-Sec-Token, can be obtained from the search interface, also in the sharing link - cookie: User provided logged-in web Cookie - proxy: Proxy, format: http://username:password@IP:port - It is recommended to use a proxy to avoid being banned or other unknown issues. ### Return: - Note info  # [示例/Example] note_id = \"67855d09000000001703d449\" xsec_token = \"ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo=\" cookie = \"Your Cookie\" proxy = \"http://username:password@IP:port\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v5_api_v1_xiaohongshu_web_get_note_info_v5_post_with_http_info(async_req=True)
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
                    " to method get_note_info_v5_api_v1_xiaohongshu_web_get_note_info_v5_post" % key
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
            '/api/v1/xiaohongshu/web/get_note_info_v5', 'POST',
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

    def get_note_info_v7_api_v1_xiaohongshu_web_get_note_info_v7_get(self, **kwargs):  # noqa: E501
        """获取笔记信息 V7/Get note info V7  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息V7 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记信息  # [English] ### Purpose: - Get note info V7 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note info  # [示例/Example] note_id=\"665f95200000000006005624\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v7_api_v1_xiaohongshu_web_get_note_info_v7_get(async_req=True)
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
            return self.get_note_info_v7_api_v1_xiaohongshu_web_get_note_info_v7_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_note_info_v7_api_v1_xiaohongshu_web_get_note_info_v7_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_note_info_v7_api_v1_xiaohongshu_web_get_note_info_v7_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取笔记信息 V7/Get note info V7  # noqa: E501

        # [中文] ### 用途: - 获取笔记信息V7 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 - share_text: 小红书分享链接（支持APP和Web端分享链接） - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。 ### 返回: - 笔记信息  # [English] ### Purpose: - Get note info V7 ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail. ### Return: - Note info  # [示例/Example] note_id=\"665f95200000000006005624\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_info_v7_api_v1_xiaohongshu_web_get_note_info_v7_get_with_http_info(async_req=True)
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
                    " to method get_note_info_v7_api_v1_xiaohongshu_web_get_note_info_v7_get" % key
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
            '/api/v1/xiaohongshu/web/get_note_info_v7', 'GET',
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

    def get_product_info_api_v1_xiaohongshu_web_get_product_info_get(self, **kwargs):  # noqa: E501
        """获取小红书商品信息/Get Xiaohongshu product info  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取小红书的商品信息 ### 参数: - share_text: 小红书分享链接（支持APP和Web端分享链接） - item_id: 商品ID - xsec_token: X-Sec-Token - 如果share_text不为空，则item_id和xsec_token会被忽略 - 如果share_text为空，则item_id和xsec_token不能为空 ### 返回: - 商品信息  # [English] ### Purpose: - Get Xiaohongshu product info by share link ### Parameters: - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - item_id: Item ID - xsec_token: X-Sec-Token - If share_text is not empty, item_id and xsec_token will be ignored - If share_text is empty, item_id and xsec_token cannot be empty ### Return: - Product info  # [示例/Example] item_id=\"65fc2e6d6b92310001d24efb\" xsec_token=\"XBC6LTqeaEDeJETMoXo436Eg-74GxFemVnNHeONYobv7k=\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_info_api_v1_xiaohongshu_web_get_product_info_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: 分享链接/Share link
        :param object item_id: 商品ID/Item ID
        :param object xsec_token: X-Sec-Token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_product_info_api_v1_xiaohongshu_web_get_product_info_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_product_info_api_v1_xiaohongshu_web_get_product_info_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_product_info_api_v1_xiaohongshu_web_get_product_info_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取小红书商品信息/Get Xiaohongshu product info  # noqa: E501

        # [中文] ### 用途: - 通过分享链接获取小红书的商品信息 ### 参数: - share_text: 小红书分享链接（支持APP和Web端分享链接） - item_id: 商品ID - xsec_token: X-Sec-Token - 如果share_text不为空，则item_id和xsec_token会被忽略 - 如果share_text为空，则item_id和xsec_token不能为空 ### 返回: - 商品信息  # [English] ### Purpose: - Get Xiaohongshu product info by share link ### Parameters: - share_text: Xiaohongshu sharing link (support APP and Web sharing link) - item_id: Item ID - xsec_token: X-Sec-Token - If share_text is not empty, item_id and xsec_token will be ignored - If share_text is empty, item_id and xsec_token cannot be empty ### Return: - Product info  # [示例/Example] item_id=\"65fc2e6d6b92310001d24efb\" xsec_token=\"XBC6LTqeaEDeJETMoXo436Eg-74GxFemVnNHeONYobv7k=\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_info_api_v1_xiaohongshu_web_get_product_info_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object share_text: 分享链接/Share link
        :param object item_id: 商品ID/Item ID
        :param object xsec_token: X-Sec-Token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['share_text', 'item_id', 'xsec_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_info_api_v1_xiaohongshu_web_get_product_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'share_text' in params:
            query_params.append(('share_text', params['share_text']))  # noqa: E501
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))  # noqa: E501
        if 'xsec_token' in params:
            query_params.append(('xsec_token', params['xsec_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web/get_product_info', 'GET',
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

    def get_user_info_api_v1_xiaohongshu_web_get_user_info_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息 V1/Get user info V1  # noqa: E501

        # [中文] ### 用途: - 获取用户信息 V1 ### 参数: - user_id: 用户ID，可以从小红书的分享链接中获取 ### 返回: - 用户信息  # [English] ### Purpose: - Get user info V1 ### Parameters: - user_id: User ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - User info  # [示例/Example] user_id=\"5f4a10070000000001006fc7\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_info_api_v1_xiaohongshu_web_get_user_info_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_info_api_v1_xiaohongshu_web_get_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_info_api_v1_xiaohongshu_web_get_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_info_api_v1_xiaohongshu_web_get_user_info_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息 V1/Get user info V1  # noqa: E501

        # [中文] ### 用途: - 获取用户信息 V1 ### 参数: - user_id: 用户ID，可以从小红书的分享链接中获取 ### 返回: - 用户信息  # [English] ### Purpose: - Get user info V1 ### Parameters: - user_id: User ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - User info  # [示例/Example] user_id=\"5f4a10070000000001006fc7\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_info_api_v1_xiaohongshu_web_get_user_info_get_with_http_info(user_id, async_req=True)
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
                    " to method get_user_info_api_v1_xiaohongshu_web_get_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_info_api_v1_xiaohongshu_web_get_user_info_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web/get_user_info', 'GET',
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

    def get_user_info_v2_api_v1_xiaohongshu_web_get_user_info_v2_get(self, **kwargs):  # noqa: E501
        """获取用户信息 V2/Get user info V2  # noqa: E501

        # [中文] ### 用途: - 获取用户信息 V2 ### 参数: - user_id: 用户ID，可以从小红书的分享链接中获取 - share_text: 小红书分享文本或链接（支持APP和Web端分享链接） - 优先使用`user_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`user_id`为准。 ### 返回: - 用户信息  # [English] ### Purpose: - Get user info V2 ### Parameters: - user_id: User ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing text or link (support APP and Web sharing link) - Prefer to use `user_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `user_id` shall prevail. ### Return: - User info  # [示例/Example] user_id = \"5f4a10070000000001006fc7\" share_text = \"@Noo 在小红书收获了15.3万次赞与收藏，查看Ta的主页>> https://xhslink.com/m/7XkrlCXbL38\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_info_v2_api_v1_xiaohongshu_web_get_user_info_v2_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object share_text: 分享文本或链接/Share text or link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_info_v2_api_v1_xiaohongshu_web_get_user_info_v2_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_info_v2_api_v1_xiaohongshu_web_get_user_info_v2_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_info_v2_api_v1_xiaohongshu_web_get_user_info_v2_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取用户信息 V2/Get user info V2  # noqa: E501

        # [中文] ### 用途: - 获取用户信息 V2 ### 参数: - user_id: 用户ID，可以从小红书的分享链接中获取 - share_text: 小红书分享文本或链接（支持APP和Web端分享链接） - 优先使用`user_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`user_id`为准。 ### 返回: - 用户信息  # [English] ### Purpose: - Get user info V2 ### Parameters: - user_id: User ID, can be obtained from the sharing link of Xiaohongshu website. - share_text: Xiaohongshu sharing text or link (support APP and Web sharing link) - Prefer to use `user_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `user_id` shall prevail. ### Return: - User info  # [示例/Example] user_id = \"5f4a10070000000001006fc7\" share_text = \"@Noo 在小红书收获了15.3万次赞与收藏，查看Ta的主页>> https://xhslink.com/m/7XkrlCXbL38\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_info_v2_api_v1_xiaohongshu_web_get_user_info_v2_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID
        :param object share_text: 分享文本或链接/Share text or link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'share_text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_info_v2_api_v1_xiaohongshu_web_get_user_info_v2_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'share_text' in params:
            query_params.append(('share_text', params['share_text']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web/get_user_info_v2', 'GET',
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

    def get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户的笔记 V2/Get user notes V2  # noqa: E501

        # [中文] ### 用途: - 获取用户的笔记 ### 参数: - user_id: 用户ID，可以从小红书的分享链接中获取 - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的最后一个NoteID     - 例如: \"662908190000000001007366\"     - JSON Path: $.data.data.notes.[-1].id ### 返回: - 用户的笔记列表  # [English] ### Purpose: - Get user notes ### Parameters: - user_id: User ID, can be obtained from the sharing link of Xiaohongshu website. - lastCursor: Last cursor, empty for the first request, use the last NoteID returned in the last response for subsequent requests     - Example: \"662908190000000001007366\"     - JSON Path: $.data.data.notes.[-1].id ### Return: - User notes list  # [示例/Example] user_id=\"5f4a10070000000001006fc7\" lastCursor=None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object last_cursor: 上一页的游标/Last cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户的笔记 V2/Get user notes V2  # noqa: E501

        # [中文] ### 用途: - 获取用户的笔记 ### 参数: - user_id: 用户ID，可以从小红书的分享链接中获取 - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的最后一个NoteID     - 例如: \"662908190000000001007366\"     - JSON Path: $.data.data.notes.[-1].id ### 返回: - 用户的笔记列表  # [English] ### Purpose: - Get user notes ### Parameters: - user_id: User ID, can be obtained from the sharing link of Xiaohongshu website. - lastCursor: Last cursor, empty for the first request, use the last NoteID returned in the last response for subsequent requests     - Example: \"662908190000000001007366\"     - JSON Path: $.data.data.notes.[-1].id ### Return: - User notes list  # [示例/Example] user_id=\"5f4a10070000000001006fc7\" lastCursor=None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object last_cursor: 上一页的游标/Last cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'last_cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'last_cursor' in params:
            query_params.append(('lastCursor', params['last_cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web/get_user_notes_v2', 'GET',
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

    def get_visitor_cookie_api_v1_xiaohongshu_web_get_visitor_cookie_get(self, **kwargs):  # noqa: E501
        """获取游客Cookie/Get visitor cookie  # noqa: E501

        # [中文] ### 用途: - 获取小红书网页版的游客Cookie，可以用于爬取小红书的一些数据。 ### 参数: - proxy: 代理，例如: http://username:password@host:port - 代理格式支持HTTP和SOCKS5，若不需要代理则留空 ### 返回: - 游客Cookie  # [English] ### Purpose: - Get Xiaohongshu web visitor cookie, which can be used to crawl some data of Xiaohongshu. ### Parameters: - proxy: Proxy, e.g. http://username:password@host:port ### Return: - Visitor cookie  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_visitor_cookie_api_v1_xiaohongshu_web_get_visitor_cookie_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object proxy: 代理/Proxy
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_visitor_cookie_api_v1_xiaohongshu_web_get_visitor_cookie_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_visitor_cookie_api_v1_xiaohongshu_web_get_visitor_cookie_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_visitor_cookie_api_v1_xiaohongshu_web_get_visitor_cookie_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取游客Cookie/Get visitor cookie  # noqa: E501

        # [中文] ### 用途: - 获取小红书网页版的游客Cookie，可以用于爬取小红书的一些数据。 ### 参数: - proxy: 代理，例如: http://username:password@host:port - 代理格式支持HTTP和SOCKS5，若不需要代理则留空 ### 返回: - 游客Cookie  # [English] ### Purpose: - Get Xiaohongshu web visitor cookie, which can be used to crawl some data of Xiaohongshu. ### Parameters: - proxy: Proxy, e.g. http://username:password@host:port ### Return: - Visitor cookie  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_visitor_cookie_api_v1_xiaohongshu_web_get_visitor_cookie_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object proxy: 代理/Proxy
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['proxy']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_visitor_cookie_api_v1_xiaohongshu_web_get_visitor_cookie_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'proxy' in params:
            query_params.append(('proxy', params['proxy']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web/get_visitor_cookie', 'GET',
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

    def search_notes_api_v1_xiaohongshu_web_search_notes_get(self, keyword, **kwargs):  # noqa: E501
        """搜索笔记/Search notes  # noqa: E501

        # [中文] ### 用途: - 搜索笔记 ### 参数: - keyword: 搜索关键词 - page: 页码，默认为1 - sort: 排序方式     - 综合排序（默认参数）: general     - 最热排序: popularity_descending     - 最新排序: time_descending     - 最多评论: comment_descending     - 最多收藏: collect_descending - noteType: 笔记类型     - 综合笔记（默认参数）: _0     - 视频笔记: _1     - 图文笔记: _2     - 直播: _3 - noteTime: 发布时间     - 不限: \"\"     - 一天内 :一天内     - 一周内 :一周内     - 半年内 :半年内 ### 返回: - 笔记列表  # [English] ### Purpose: - Search notes ### Parameters: - keyword: Keyword - page: Page, default is 1 - sort: Sort     - General sort (default): general     - Popularity sort: popularity_descending     - Latest sort: time_descending     - Most comments: comment_descending     - Most favorites: collect_descending - noteType: Note type     - General note (default): _0     - Video note: _1     - Image note: _2     - Live: _3 - noteTime: Release time     - No limit: \"\"     - Within one day: 一天内     - Within one week: 一周内     - Within half a year: 半年内 ### Return: - Note list  # [示例/Example] keyword=\"美食\" page=1 sort=\"general\" noteType=\"_0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_notes_api_v1_xiaohongshu_web_search_notes_get(keyword, async_req=True)
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
            return self.search_notes_api_v1_xiaohongshu_web_search_notes_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_notes_api_v1_xiaohongshu_web_search_notes_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_notes_api_v1_xiaohongshu_web_search_notes_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索笔记/Search notes  # noqa: E501

        # [中文] ### 用途: - 搜索笔记 ### 参数: - keyword: 搜索关键词 - page: 页码，默认为1 - sort: 排序方式     - 综合排序（默认参数）: general     - 最热排序: popularity_descending     - 最新排序: time_descending     - 最多评论: comment_descending     - 最多收藏: collect_descending - noteType: 笔记类型     - 综合笔记（默认参数）: _0     - 视频笔记: _1     - 图文笔记: _2     - 直播: _3 - noteTime: 发布时间     - 不限: \"\"     - 一天内 :一天内     - 一周内 :一周内     - 半年内 :半年内 ### 返回: - 笔记列表  # [English] ### Purpose: - Search notes ### Parameters: - keyword: Keyword - page: Page, default is 1 - sort: Sort     - General sort (default): general     - Popularity sort: popularity_descending     - Latest sort: time_descending     - Most comments: comment_descending     - Most favorites: collect_descending - noteType: Note type     - General note (default): _0     - Video note: _1     - Image note: _2     - Live: _3 - noteTime: Release time     - No limit: \"\"     - Within one day: 一天内     - Within one week: 一周内     - Within half a year: 半年内 ### Return: - Note list  # [示例/Example] keyword=\"美食\" page=1 sort=\"general\" noteType=\"_0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_notes_api_v1_xiaohongshu_web_search_notes_get_with_http_info(keyword, async_req=True)
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
                    " to method search_notes_api_v1_xiaohongshu_web_search_notes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_notes_api_v1_xiaohongshu_web_search_notes_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web/search_notes', 'GET',
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

    def search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get(self, keyword, **kwargs):  # noqa: E501
        """搜索笔记 V3/Search notes V3  # noqa: E501

        # [中文] ### 用途: - 搜索笔记 V3 ### 参数: - keyword: 搜索关键词 - page: 页码，默认为1 - sort: 排序方式     - 综合排序（默认参数）: general     - 最热排序: popularity_descending     - 最新排序: time_descending     - 最多评论: comment_descending     - 最多收藏: collect_descending - noteType: 笔记类型     - 综合笔记（默认参数）: _0     - 视频笔记: _1     - 图文笔记: _2     - 直播: _3 - noteTime: 发布时间     - 不限: \"\"     - 一天内 :一天内     - 一周内 :一周内     - 半年内 :半年内 ### 返回: - 笔记列表  # [English] ### Purpose: - Search notes V3 ### Parameters: - keyword: Keyword - page: Page, default is 1 - sort: Sort     - General sort (default): general     - Popularity sort: popularity_descending     - Latest sort: time_descending     - Most comments: comment_descending     - Most favorites: collect_descending - noteType: Note type     - General note (default): _0     - Video note: _1     - Image note: _2     - Live: _3 - noteTime: Release time     - No limit: \"\"     - Within one day: 一天内     - Within one week: 一周内     - Within half a year: 半年内 ### Return: - Note list  # [示例/Example] keyword=\"美食\" page=1 sort=\"general\" noteType=\"_0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get(keyword, async_req=True)
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
            return self.search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索笔记 V3/Search notes V3  # noqa: E501

        # [中文] ### 用途: - 搜索笔记 V3 ### 参数: - keyword: 搜索关键词 - page: 页码，默认为1 - sort: 排序方式     - 综合排序（默认参数）: general     - 最热排序: popularity_descending     - 最新排序: time_descending     - 最多评论: comment_descending     - 最多收藏: collect_descending - noteType: 笔记类型     - 综合笔记（默认参数）: _0     - 视频笔记: _1     - 图文笔记: _2     - 直播: _3 - noteTime: 发布时间     - 不限: \"\"     - 一天内 :一天内     - 一周内 :一周内     - 半年内 :半年内 ### 返回: - 笔记列表  # [English] ### Purpose: - Search notes V3 ### Parameters: - keyword: Keyword - page: Page, default is 1 - sort: Sort     - General sort (default): general     - Popularity sort: popularity_descending     - Latest sort: time_descending     - Most comments: comment_descending     - Most favorites: collect_descending - noteType: Note type     - General note (default): _0     - Video note: _1     - Image note: _2     - Live: _3 - noteTime: Release time     - No limit: \"\"     - Within one day: 一天内     - Within one week: 一周内     - Within half a year: 半年内 ### Return: - Note list  # [示例/Example] keyword=\"美食\" page=1 sort=\"general\" noteType=\"_0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get_with_http_info(keyword, async_req=True)
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
                    " to method search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web/search_notes_v3', 'GET',
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

    def search_users_api_v1_xiaohongshu_web_search_users_get(self, keyword, **kwargs):  # noqa: E501
        """搜索用户/Search users  # noqa: E501

        # [中文] ### 用途: - 搜索用户 ### 参数: - keyword: 搜索关键词 - page: 页码，默认为1 ### 返回: - 用户列表  # [English] ### Purpose: - Search users ### Parameters: - keyword: Keyword - page: Page, default is 1 ### Return: - User list  # [示例/Example] keyword=\"美食\" page=1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_api_v1_xiaohongshu_web_search_users_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Keyword (required)
        :param object page: 页码/Page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_users_api_v1_xiaohongshu_web_search_users_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.search_users_api_v1_xiaohongshu_web_search_users_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def search_users_api_v1_xiaohongshu_web_search_users_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """搜索用户/Search users  # noqa: E501

        # [中文] ### 用途: - 搜索用户 ### 参数: - keyword: 搜索关键词 - page: 页码，默认为1 ### 返回: - 用户列表  # [English] ### Purpose: - Search users ### Parameters: - keyword: Keyword - page: Page, default is 1 ### Return: - User list  # [示例/Example] keyword=\"美食\" page=1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_users_api_v1_xiaohongshu_web_search_users_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Keyword (required)
        :param object page: 页码/Page
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
                    " to method search_users_api_v1_xiaohongshu_web_search_users_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `search_users_api_v1_xiaohongshu_web_search_users_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web/search_users', 'GET',
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

    def sign_api_v1_xiaohongshu_web_sign_post(self, **kwargs):  # noqa: E501
        """小红书Web签名/Xiaohongshu Web sign  # noqa: E501

        # [中文] ### 用途: - 小红书Web签名，用于获取小红书的一些数据。 - 生成 `X-s`, `X-t`, `X-s-common` 等签名参数。 - 价格：0.001$/次 ### 参数: - sign_request: 签名请求模型     - path: 请求接口的路径，例如: `/api/sns/web/v1/homefeed`     - data: 请求API的荷载数据     - cookie: 请求接口的Cookie ### 返回: - 签名参数(X-s, X-t, X-s-common等)  # [English] ### Purpose: - Xiaohongshu Web sign, used to get some data of Xiaohongshu. - Generate `X-s`, `X-t`, `X-s-common` and other signature parameters. - Price: 0.001$/time ### Parameters: - sign_request: Sign request model     - path: Request API path, e.g. `/api/sns/web/v1/homefeed`     - data: Payload data of request API     - cookie: Request API cookie ### Return: - Signature parameters(X-s, X-t, X-s-common, etc.)  # [示例/Example] {     \"path\": \"/api/sns/web/v1/homefeed\",     \"data\": {         \"cursor_score\": \"\",         \"num\": 35,         \"refresh_type\": 1,         \"note_index\": 35,         \"unread_begin_note_id\": \"\",         \"unread_end_note_id\": \"\",         \"unread_note_count\": 0,         \"category\": \"homefeed_recommend\",         \"search_key\": \"\",         \"need_num\": 10,         \"image_formats\": [             \"jpg\",             \"webp\",             \"avif\"         ],         \"need_filter_image\": False     },     \"cookie\": \"web_session=030037a04eafd37791e6e4bd05204a8cf2af05;acw_tc=0a00d79f17363096679345838efb77751cc087fb039dd1691dc954824410f6;abRequestId=384480ae-5196-5818-a835-42e6278de9f0;webBuild=4.47.1;xsecappid=xhs-pc-web;a1=194441ef694PayUbdUvgp0dSHfIcACsNsLud0Lgru50000354513;webId=6cf10a564b9b07d129729b65e0d1785a;sec_poison_id=32964532-d414-4beb-914f-98811853b75f\" }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sign_api_v1_xiaohongshu_web_sign_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sign_api_v1_xiaohongshu_web_sign_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.sign_api_v1_xiaohongshu_web_sign_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def sign_api_v1_xiaohongshu_web_sign_post_with_http_info(self, **kwargs):  # noqa: E501
        """小红书Web签名/Xiaohongshu Web sign  # noqa: E501

        # [中文] ### 用途: - 小红书Web签名，用于获取小红书的一些数据。 - 生成 `X-s`, `X-t`, `X-s-common` 等签名参数。 - 价格：0.001$/次 ### 参数: - sign_request: 签名请求模型     - path: 请求接口的路径，例如: `/api/sns/web/v1/homefeed`     - data: 请求API的荷载数据     - cookie: 请求接口的Cookie ### 返回: - 签名参数(X-s, X-t, X-s-common等)  # [English] ### Purpose: - Xiaohongshu Web sign, used to get some data of Xiaohongshu. - Generate `X-s`, `X-t`, `X-s-common` and other signature parameters. - Price: 0.001$/time ### Parameters: - sign_request: Sign request model     - path: Request API path, e.g. `/api/sns/web/v1/homefeed`     - data: Payload data of request API     - cookie: Request API cookie ### Return: - Signature parameters(X-s, X-t, X-s-common, etc.)  # [示例/Example] {     \"path\": \"/api/sns/web/v1/homefeed\",     \"data\": {         \"cursor_score\": \"\",         \"num\": 35,         \"refresh_type\": 1,         \"note_index\": 35,         \"unread_begin_note_id\": \"\",         \"unread_end_note_id\": \"\",         \"unread_note_count\": 0,         \"category\": \"homefeed_recommend\",         \"search_key\": \"\",         \"need_num\": 10,         \"image_formats\": [             \"jpg\",             \"webp\",             \"avif\"         ],         \"need_filter_image\": False     },     \"cookie\": \"web_session=030037a04eafd37791e6e4bd05204a8cf2af05;acw_tc=0a00d79f17363096679345838efb77751cc087fb039dd1691dc954824410f6;abRequestId=384480ae-5196-5818-a835-42e6278de9f0;webBuild=4.47.1;xsecappid=xhs-pc-web;a1=194441ef694PayUbdUvgp0dSHfIcACsNsLud0Lgru50000354513;webId=6cf10a564b9b07d129729b65e0d1785a;sec_poison_id=32964532-d414-4beb-914f-98811853b75f\" }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sign_api_v1_xiaohongshu_web_sign_post_with_http_info(async_req=True)
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
                    " to method sign_api_v1_xiaohongshu_web_sign_post" % key
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
            '/api/v1/xiaohongshu/web/sign', 'POST',
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
