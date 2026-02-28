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


class XiaohongshuWebV2APIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get(self, note_id, **kwargs):  # noqa: E501
        """获取单一笔记和推荐笔记 V1 (已弃用)/Fetch one note and feed notes V1 (deprecated)  # noqa: E501

        # [中文] ### 用途: - 获取单一笔记和推荐笔记 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get_with_http_info(note_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get_with_http_info(note_id, **kwargs)  # noqa: E501
            return data

    def fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get_with_http_info(self, note_id, **kwargs):  # noqa: E501
        """获取单一笔记和推荐笔记 V1 (已弃用)/Fetch one note and feed notes V1 (deprecated)  # noqa: E501

        # [中文] ### 用途: - 获取单一笔记和推荐笔记 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get_with_http_info(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web_v2/fetch_feed_notes', 'GET',
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

    def fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get(self, note_id, **kwargs):  # noqa: E501
        """获取单一笔记和推荐笔记 V2/Fetch one note and feed notes V2(v2稳定, 推荐使用此接口)  # noqa: E501

        # [中文] ### 用途: - 获取单一笔记和推荐笔记 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get_with_http_info(note_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get_with_http_info(note_id, **kwargs)  # noqa: E501
            return data

    def fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get_with_http_info(self, note_id, **kwargs):  # noqa: E501
        """获取单一笔记和推荐笔记 V2/Fetch one note and feed notes V2(v2稳定, 推荐使用此接口)  # noqa: E501

        # [中文] ### 用途: - 获取单一笔记和推荐笔记 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get_with_http_info(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web_v2/fetch_feed_notes_v2', 'GET',
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

    def fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get(self, short_url, **kwargs):  # noqa: E501
        """获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)  # noqa: E501

        # [中文] ### 用途: - 获取单一笔记和推荐笔记 ### 参数: - short_url: 短链，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes ### Parameters: - short_url: Short URL, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] short_url = \"http://xhslink.com/a/tyoREa3ciaAeb\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get(short_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object short_url: 短链/Short URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get_with_http_info(short_url, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get_with_http_info(short_url, **kwargs)  # noqa: E501
            return data

    def fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get_with_http_info(self, short_url, **kwargs):  # noqa: E501
        """获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)  # noqa: E501

        # [中文] ### 用途: - 获取单一笔记和推荐笔记 ### 参数: - short_url: 短链，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes ### Parameters: - short_url: Short URL, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] short_url = \"http://xhslink.com/a/tyoREa3ciaAeb\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get_with_http_info(short_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object short_url: 短链/Short URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['short_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'short_url' is set
        if self.api_client.client_side_validation and ('short_url' not in params or
                                                       params['short_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `short_url` when calling `fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'short_url' in params:
            query_params.append(('short_url', params['short_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web_v2/fetch_feed_notes_v3', 'GET',
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

    def fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get(self, note_id, **kwargs):  # noqa: E501
        """获取单一笔记和推荐笔记 V4 (互动量有延迟)/Fetch one note and feed notes V4 (interaction volume has a delay)  # noqa: E501

        # [中文] ### 用途: - 获取单一笔记和推荐笔记，结构不同互动量有延时 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes, the structure is different and the interaction volume has a delay ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get_with_http_info(note_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get_with_http_info(note_id, **kwargs)  # noqa: E501
            return data

    def fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get_with_http_info(self, note_id, **kwargs):  # noqa: E501
        """获取单一笔记和推荐笔记 V4 (互动量有延迟)/Fetch one note and feed notes V4 (interaction volume has a delay)  # noqa: E501

        # [中文] ### 用途: - 获取单一笔记和推荐笔记，结构不同互动量有延时 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记  # [English] ### Purpose: - Get one note and feed notes, the structure is different and the interaction volume has a delay ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get_with_http_info(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web_v2/fetch_feed_notes_v4', 'GET',
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

    def fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get(self, note_id, **kwargs):  # noqa: E501
        """获取单一笔记和推荐笔记 V5 (互动量有缺失)/Fetch one note and feed notes V5 (interaction volume has a missing)  # noqa: E501

        # [中文] ### 用途: - 获取单一笔记和推荐笔记，结构不同互动量有缺失 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记 ### 备注: - 互动数据仅有点赞数，没有评论数与收藏数  # [English] ### Purpose: - Get one note and feed notes, the structure is different and the interaction volume has a missing ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes ### Notes: - Interaction data only includes likes, without comments and favorites.  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get_with_http_info(note_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get_with_http_info(note_id, **kwargs)  # noqa: E501
            return data

    def fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get_with_http_info(self, note_id, **kwargs):  # noqa: E501
        """获取单一笔记和推荐笔记 V5 (互动量有缺失)/Fetch one note and feed notes V5 (interaction volume has a missing)  # noqa: E501

        # [中文] ### 用途: - 获取单一笔记和推荐笔记，结构不同互动量有缺失 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 单一笔记和推荐笔记 ### 备注: - 互动数据仅有点赞数，没有评论数与收藏数  # [English] ### Purpose: - Get one note and feed notes, the structure is different and the interaction volume has a missing ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - One note and feed notes ### Notes: - Interaction data only includes likes, without comments and favorites.  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get_with_http_info(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web_v2/fetch_feed_notes_v5', 'GET',
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

    def fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Fetch follower list  # noqa: E501

        # [中文] ### 用途: - 获取用户粉丝列表 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 用户粉丝列表  # [English] ### Purpose: - Get follower list ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Follower list  # [示例/Example] user_id = \"604a28420000000001005211\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户粉丝列表/Fetch follower list  # noqa: E501

        # [中文] ### 用途: - 获取用户粉丝列表 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 用户粉丝列表  # [English] ### Purpose: - Get follower list ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Follower list  # [示例/Example] user_id = \"604a28420000000001005211\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 游标/Cursor
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
                    " to method fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web_v2/fetch_follower_list', 'GET',
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

    def fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户关注列表/Fetch following list  # noqa: E501

        # [中文] ### 用途: - 获取用户关注列表 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 用户关注列表  # [English] ### Purpose: - Get following list ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Following list  # [示例/Example] user_id = \"604a28420000000001005211\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户关注列表/Fetch following list  # noqa: E501

        # [中文] ### 用途: - 获取用户关注列表 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 用户关注列表  # [English] ### Purpose: - Get following list ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Following list  # [示例/Example] user_id = \"604a28420000000001005211\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 游标/Cursor
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
                    " to method fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web_v2/fetch_following_list', 'GET',
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

    def fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get(self, user_id, **kwargs):  # noqa: E501
        """获取Web用户主页笔记/Fetch web user profile notes  # noqa: E501

        # [中文] ### 用途: - 获取主页笔记 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 主页笔记  # [English] ### Purpose: - Get home notes ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Home notes  # [示例/Example] user_id = \"5f3e0d00000000001f03a4bc\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取Web用户主页笔记/Fetch web user profile notes  # noqa: E501

        # [中文] ### 用途: - 获取主页笔记 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 主页笔记  # [English] ### Purpose: - Get home notes ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Home notes  # [示例/Example] user_id = \"5f3e0d00000000001f03a4bc\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 游标/Cursor
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
                    " to method fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web_v2/fetch_home_notes', 'GET',
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

    def fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get(self, user_id, **kwargs):  # noqa: E501
        """获取App用户主页笔记/Fetch App user home notes  # noqa: E501

        # [中文] ### 用途: - 获取App主页笔记 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 主页笔记  # [English] ### Purpose: - Get home notes ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Home notes  # [示例/Example] user_id = \"5f3e0d00000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取App用户主页笔记/Fetch App user home notes  # noqa: E501

        # [中文] ### 用途: - 获取App主页笔记 ### 参数: - user_id: 用户ID - cursor: 游标 ### 返回: - 主页笔记  # [English] ### Purpose: - Get home notes ### Parameters: - user_id: User ID - cursor: Cursor ### Return: - Home notes  # [示例/Example] user_id = \"5f3e0d00000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object cursor: 游标/Cursor
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
                    " to method fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web_v2/fetch_home_notes_app', 'GET',
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

    def fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get(self, **kwargs):  # noqa: E501
        """获取小红书热榜/Fetch Xiaohongshu hot list  # noqa: E501

        # [中文] ### 用途: - 获取小红书热榜 ### 返回: - 小红书热榜  # [English] ### Purpose: - Get Xiaohongshu hot list ### Return: - Xiaohongshu hot list  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取小红书热榜/Fetch Xiaohongshu hot list  # noqa: E501

        # [中文] ### 用途: - 获取小红书热榜 ### 返回: - 小红书热榜  # [English] ### Purpose: - Get Xiaohongshu hot list ### Return: - Xiaohongshu hot list  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get_with_http_info(async_req=True)
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
                    " to method fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get" % key
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
            '/api/v1/xiaohongshu/web_v2/fetch_hot_list', 'GET',
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

    def fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get(self, note_id, **kwargs):  # noqa: E501
        """获取笔记评论/Fetch note comments  # noqa: E501

        # [中文] ### 用途: - 获取笔记评论 ### 参数: - note_id: 笔记ID - cursor: 游标 ### 返回: - 笔记评论  # [English] ### Purpose: - Get note comments ### Parameters: - note_id: Note ID - cursor: Cursor ### Return: - Note comments  # [示例/Example] note_id = \"651ccaa9000000001f03d7f7\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get_with_http_info(note_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get_with_http_info(note_id, **kwargs)  # noqa: E501
            return data

    def fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get_with_http_info(self, note_id, **kwargs):  # noqa: E501
        """获取笔记评论/Fetch note comments  # noqa: E501

        # [中文] ### 用途: - 获取笔记评论 ### 参数: - note_id: 笔记ID - cursor: 游标 ### 返回: - 笔记评论  # [English] ### Purpose: - Get note comments ### Parameters: - note_id: Note ID - cursor: Cursor ### Return: - Note comments  # [示例/Example] note_id = \"651ccaa9000000001f03d7f7\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get_with_http_info(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web_v2/fetch_note_comments', 'GET',
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

    def fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get(self, note_id, **kwargs):  # noqa: E501
        """获取小红书笔记图片/Fetch Xiaohongshu note image  # noqa: E501

        # [中文] ### 用途: - 获取小红书笔记图片 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 小红书笔记图片  # [English] ### Purpose: - Get Xiaohongshu note image ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - Xiaohongshu note image  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get_with_http_info(note_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get_with_http_info(note_id, **kwargs)  # noqa: E501
            return data

    def fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get_with_http_info(self, note_id, **kwargs):  # noqa: E501
        """获取小红书笔记图片/Fetch Xiaohongshu note image  # noqa: E501

        # [中文] ### 用途: - 获取小红书笔记图片 ### 参数: - note_id: 笔记ID，可以从小红书的分享链接中获取 ### 返回: - 小红书笔记图片  # [English] ### Purpose: - Get Xiaohongshu note image ### Parameters: - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website. ### Return: - Xiaohongshu note image  # [示例/Example] note_id = \"66c9cc31000000001f03a4bc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get_with_http_info(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web_v2/fetch_note_image', 'GET',
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

    def fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get(self, user_id, **kwargs):  # noqa: E501
        """获取小红书商品列表/Fetch Xiaohongshu product list  # noqa: E501

        # [中文] ### 用途: - 获取小红书商品列表 ### 参数: - user_id: 用户ID - page: 页码 ### 返回: - 小红书商品列表  # [English] ### Purpose: - Get Xiaohongshu product list ### Parameters: - user_id: User ID - page: Page number ### Return: - Xiaohongshu product list  # [示例/Example] user_id = \"627e35aa00000000210275ae\" page = \"1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取小红书商品列表/Fetch Xiaohongshu product list  # noqa: E501

        # [中文] ### 用途: - 获取小红书商品列表 ### 参数: - user_id: 用户ID - page: 页码 ### 返回: - 小红书商品列表  # [English] ### Purpose: - Get Xiaohongshu product list ### Parameters: - user_id: User ID - page: Page number ### Return: - Xiaohongshu product list  # [示例/Example] user_id = \"627e35aa00000000210275ae\" page = \"1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :param object page: 页码/Page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web_v2/fetch_product_list', 'GET',
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

    def fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get(self, keywords, **kwargs):  # noqa: E501
        """获取搜索笔记/Fetch search notes  # noqa: E501

        # [中文] ### 用途: - 获取搜索笔记 ### 参数: - keywords：搜索关键词 - sort_type：排序方式     - general：综合     - time_descending：最新     - popularity_descending：最热 - note_type: 笔记类型     - 0：全部     - 1：视频     - 2：图文 ### 返回: - 搜索笔记  # [English] ### Purpose: - Get search notes ### Parameters: - keywords: Search keywords - sort_type: Sort type     - general: General     - time_descending: Latest     - popularity_descending: Popular - note_type: Note type     - 0: All     - 1: Video     - 2: Note ### Return: - Search notes  # [示例/Example] keywords = \"口红\" page = 1 sort_type = \"general\" note_type = \"1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get(keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keywords: 搜索关键词/Search keywords (required)
        :param object page: 页码/Page number
        :param object sort_type: 排序方式/Sort type
        :param object note_type: 笔记类型/Note type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get_with_http_info(keywords, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get_with_http_info(keywords, **kwargs)  # noqa: E501
            return data

    def fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get_with_http_info(self, keywords, **kwargs):  # noqa: E501
        """获取搜索笔记/Fetch search notes  # noqa: E501

        # [中文] ### 用途: - 获取搜索笔记 ### 参数: - keywords：搜索关键词 - sort_type：排序方式     - general：综合     - time_descending：最新     - popularity_descending：最热 - note_type: 笔记类型     - 0：全部     - 1：视频     - 2：图文 ### 返回: - 搜索笔记  # [English] ### Purpose: - Get search notes ### Parameters: - keywords: Search keywords - sort_type: Sort type     - general: General     - time_descending: Latest     - popularity_descending: Popular - note_type: Note type     - 0: All     - 1: Video     - 2: Note ### Return: - Search notes  # [示例/Example] keywords = \"口红\" page = 1 sort_type = \"general\" note_type = \"1\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get_with_http_info(keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keywords: 搜索关键词/Search keywords (required)
        :param object page: 页码/Page number
        :param object sort_type: 排序方式/Sort type
        :param object note_type: 笔记类型/Note type
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keywords', 'page', 'sort_type', 'note_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keywords' is set
        if self.api_client.client_side_validation and ('keywords' not in params or
                                                       params['keywords'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keywords` when calling `fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'sort_type' in params:
            query_params.append(('sort_type', params['sort_type']))  # noqa: E501
        if 'note_type' in params:
            query_params.append(('note_type', params['note_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web_v2/fetch_search_notes', 'GET',
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

    def fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get(self, keywords, **kwargs):  # noqa: E501
        """获取搜索用户/Fetch search users  # noqa: E501

        # [中文] ### 用途: - 获取搜索用户 ### 参数: - keywords：搜索关键词 - page：页码 ### 返回: - 搜索用户  # [English] ### Purpose: - Get search users ### Parameters: - keywords: Search keywords - page: Page number ### Return: - Search users  # [示例/Example] keywords = \"口红\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get(keywords, async_req=True)
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
            return self.fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get_with_http_info(keywords, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get_with_http_info(keywords, **kwargs)  # noqa: E501
            return data

    def fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get_with_http_info(self, keywords, **kwargs):  # noqa: E501
        """获取搜索用户/Fetch search users  # noqa: E501

        # [中文] ### 用途: - 获取搜索用户 ### 参数: - keywords：搜索关键词 - page：页码 ### 返回: - 搜索用户  # [English] ### Purpose: - Get search users ### Parameters: - keywords: Search keywords - page: Page number ### Return: - Search users  # [示例/Example] keywords = \"口红\" page = 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get_with_http_info(keywords, async_req=True)
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
                    " to method fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keywords' is set
        if self.api_client.client_side_validation and ('keywords' not in params or
                                                       params['keywords'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keywords` when calling `fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web_v2/fetch_search_users', 'GET',
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

    def fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get(self, note_id, comment_id, **kwargs):  # noqa: E501
        """获取子评论/Fetch sub comments  # noqa: E501

        # [中文] ### 用途: - 获取子评论 ### 参数: - note_id: 笔记ID - comment_id: 评论ID - cursor: 游标 ### 返回: - 子评论  # [English] ### Purpose: - Get sub comments ### Parameters: - note_id: Note ID - comment_id: Comment ID - cursor: Cursor ### Return: - Sub comments  # [示例/Example] note_id = \"673c894c0000000007033f92\" comment_id = \"673ecdfc000000001503bf8b\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get(note_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object comment_id: 评论ID/Comment ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get_with_http_info(note_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get_with_http_info(note_id, comment_id, **kwargs)  # noqa: E501
            return data

    def fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get_with_http_info(self, note_id, comment_id, **kwargs):  # noqa: E501
        """获取子评论/Fetch sub comments  # noqa: E501

        # [中文] ### 用途: - 获取子评论 ### 参数: - note_id: 笔记ID - comment_id: 评论ID - cursor: 游标 ### 返回: - 子评论  # [English] ### Purpose: - Get sub comments ### Parameters: - note_id: Note ID - comment_id: Comment ID - cursor: Cursor ### Return: - Sub comments  # [示例/Example] note_id = \"673c894c0000000007033f92\" comment_id = \"673ecdfc000000001503bf8b\" cursor = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get_with_http_info(note_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object note_id: 笔记ID/Note ID (required)
        :param object comment_id: 评论ID/Comment ID (required)
        :param object cursor: 游标/Cursor
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id', 'comment_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if self.api_client.client_side_validation and ('note_id' not in params or
                                                       params['note_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `note_id` when calling `fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'note_id' in params:
            query_params.append(('note_id', params['note_id']))  # noqa: E501
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/xiaohongshu/web_v2/fetch_sub_comments', 'GET',
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

    def fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get(self, user_id, **kwargs):  # noqa: E501
        """获取App用户信息/Fetch App user info  # noqa: E501

        # [中文] ### 用途: - 获取用户信息 ### 参数: - user_id: 用户ID ### 返回: - 用户信息  # [English] ### Purpose: - Get user info ### Parameters: - user_id: User ID ### Return: - User info  # [示例/Example] user_id = \"5e3a8ee700000000010070c6\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取App用户信息/Fetch App user info  # noqa: E501

        # [中文] ### 用途: - 获取用户信息 ### 参数: - user_id: 用户ID ### 返回: - 用户信息  # [English] ### Purpose: - Get user info ### Parameters: - user_id: User ID ### Return: - User info  # [示例/Example] user_id = \"5e3a8ee700000000010070c6\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get_with_http_info(user_id, async_req=True)
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
                    " to method fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web_v2/fetch_user_info_app', 'GET',
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

    def fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息/Fetch user info  # noqa: E501

        # [中文] ### 用途: - 获取用户信息 ### 参数: - user_id: 用户ID ### 返回: - 用户信息  # [English] ### Purpose: - Get user info ### Parameters: - user_id: User ID ### Return: - User info  # [示例/Example] user_id = \"5e3a8ee700000000010070c6\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_id: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """获取用户信息/Fetch user info  # noqa: E501

        # [中文] ### 用途: - 获取用户信息 ### 参数: - user_id: 用户ID ### 返回: - 用户信息  # [English] ### Purpose: - Get user info ### Parameters: - user_id: User ID ### Return: - User info  # [示例/Example] user_id = \"5e3a8ee700000000010070c6\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get_with_http_info(user_id, async_req=True)
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
                    " to method fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in params or
                                                       params['user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_id` when calling `fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get`")  # noqa: E501

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
            '/api/v1/xiaohongshu/web_v2/fetch_user_info', 'GET',
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
