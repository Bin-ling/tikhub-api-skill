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


class YouTubeWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_get_video_subtitles_api_v1_youtube_web_get_video_subtitles_get(self, subtitle_url, **kwargs):  # noqa: E501
        """获取视频字幕/Get video subtitles  # noqa: E501

        # [中文] ### 用途: - 获取视频字幕内容 ### 使用流程: 1. 先调用获取视频详情接口，从字幕数据中获取subtitleUrl 2. 使用该URL作为本接口参数 ### 参数说明: - fix_overlap: 特别适用于自动生成的字幕，会自动分割重叠的时间段  # [English] ### Purpose: - Get video subtitle content ### Workflow: 1. First call get_video_info to obtain subtitleUrl 2. Use that URL as parameter here ### Parameter Notes: - fix_overlap: Especially useful for auto-generated subtitles, will split overlapping time ranges  # [示例/Example] subtitle_url = \"https://www.youtube.com/api/timedtext?v=G33j5Qi4rE8...\" target_lang = \"zh-CN\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_get_video_subtitles_api_v1_youtube_web_get_video_subtitles_get(subtitle_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subtitle_url: 字幕URL（需先调用获取视频详情接口） / Subtitle URL from video details (required)
        :param object format: 字幕格式：srt/xml/vtt/txt / Subtitle format
        :param object fix_overlap: 修复重叠字幕（默认开启） / Fix overlapping subtitles
        :param object target_lang: 目标语言代码（留空保持原语言） / Target language code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_get_video_subtitles_api_v1_youtube_web_get_video_subtitles_get_with_http_info(subtitle_url, **kwargs)  # noqa: E501
        else:
            (data) = self.api_get_video_subtitles_api_v1_youtube_web_get_video_subtitles_get_with_http_info(subtitle_url, **kwargs)  # noqa: E501
            return data

    def api_get_video_subtitles_api_v1_youtube_web_get_video_subtitles_get_with_http_info(self, subtitle_url, **kwargs):  # noqa: E501
        """获取视频字幕/Get video subtitles  # noqa: E501

        # [中文] ### 用途: - 获取视频字幕内容 ### 使用流程: 1. 先调用获取视频详情接口，从字幕数据中获取subtitleUrl 2. 使用该URL作为本接口参数 ### 参数说明: - fix_overlap: 特别适用于自动生成的字幕，会自动分割重叠的时间段  # [English] ### Purpose: - Get video subtitle content ### Workflow: 1. First call get_video_info to obtain subtitleUrl 2. Use that URL as parameter here ### Parameter Notes: - fix_overlap: Especially useful for auto-generated subtitles, will split overlapping time ranges  # [示例/Example] subtitle_url = \"https://www.youtube.com/api/timedtext?v=G33j5Qi4rE8...\" target_lang = \"zh-CN\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_get_video_subtitles_api_v1_youtube_web_get_video_subtitles_get_with_http_info(subtitle_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object subtitle_url: 字幕URL（需先调用获取视频详情接口） / Subtitle URL from video details (required)
        :param object format: 字幕格式：srt/xml/vtt/txt / Subtitle format
        :param object fix_overlap: 修复重叠字幕（默认开启） / Fix overlapping subtitles
        :param object target_lang: 目标语言代码（留空保持原语言） / Target language code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subtitle_url', 'format', 'fix_overlap', 'target_lang']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_get_video_subtitles_api_v1_youtube_web_get_video_subtitles_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subtitle_url' is set
        if self.api_client.client_side_validation and ('subtitle_url' not in params or
                                                       params['subtitle_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subtitle_url` when calling `api_get_video_subtitles_api_v1_youtube_web_get_video_subtitles_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subtitle_url' in params:
            query_params.append(('subtitle_url', params['subtitle_url']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501
        if 'fix_overlap' in params:
            query_params.append(('fix_overlap', params['fix_overlap']))  # noqa: E501
        if 'target_lang' in params:
            query_params.append(('target_lang', params['target_lang']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_video_subtitles', 'GET',
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

    def get_channel_description_api_v1_youtube_web_get_channel_description_get(self, **kwargs):  # noqa: E501
        """获取频道描述信息/Get channel description  # noqa: E501

        # [中文] ### 用途: - 获取YouTube频道的介绍信息（订阅数、视频数、观看次数、注册时间、社交链接等）  ### 重要提示 - 需要两次请求获取完整数据: - **第一次请求**（使用channel_id）: 返回基本信息（频道名称、描述、订阅数、视频数、头像、横幅等） - **第二次请求**（使用continuation_token）: 返回高级信息（**注册时间、社交媒体链接、国家、观看次数**等）  ### 如何获取channel_id: - 如果你只有频道URL（如 `https://www.youtube.com/@CozyCraftYT`），请先调用 **get_channel_id_v2** 接口获取channel_id - 该接口会返回类似 `UCeu6U67OzJhV1KwBansH3Dg` 的频道ID  ### 参数详解:  #### 📌 必选参数（二选一）: **channel_id** (string) - **作用**: 频道ID，用于第一次请求获取频道基本信息 - **格式**: 通常以 `UC` 开头的24位字符串 - **示例**: `\"UCeu6U67OzJhV1KwBansH3Dg\"` - **获取方式**: 调用 **get_channel_id_v2** 接口，传入频道URL即可获取  **continuation_token** (string) - **作用**: 翻页标志，用于第二次请求获取频道的高级信息 - **获取方式**: 从第一次请求的响应中获取 `continuation_token` 字段 - **注意**: `channel_id` 和 `continuation_token` 必须提供其中一个  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置显示语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 使用流程（三步获取完整数据）: 1. **获取channel_id**: 如果只有频道URL，先调用 `get_channel_id_v2?channel_url=https://www.youtube.com/@CozyCraftYT` 2. **第一次请求**: 使用 `channel_id` 参数获取频道基本信息，同时获取 `continuation_token` 3. **第二次请求**: 使用 `continuation_token` 获取高级信息（注册时间、社交链接等）  ### 返回数据结构 (need_format=true):  #### 第一次请求返回（使用channel_id）: ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": \"CozyCraft\",   \"handle\": \"CozyCraftYT\",   \"description\": \"频道介绍...\",   \"subscriber_count\": \"9.84万位订阅者\",   \"video_count\": \"181 个视频\",   \"view_count\": null,   \"country\": null,   \"creation_date\": null,   \"links\": [],   \"avatar\": [{\"url\": \"...\", \"width\": 900, \"height\": 900}],   \"banner\": [{\"url\": \"...\", \"width\": 2560, \"height\": 424}],   \"keywords\": \"Minecraft Ambience...\",   \"channel_url\": \"https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg\",   \"vanity_url\": \"http://www.youtube.com/@CozyCraftYT\",   \"rss_url\": \"https://www.youtube.com/feeds/videos.xml?channel_id=UCeu6U67OzJhV1KwBansH3Dg\",   \"is_family_safe\": true,   \"verified\": false,   \"has_business_email\": false,   \"has_membership\": true,   \"continuation_token\": \"4qmFsgJg...\" } ```  #### 第二次请求返回（使用continuation_token）: ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": null,   \"handle\": \"CozyCraftYT\",   \"description\": \"完整频道介绍...\",   \"subscriber_count\": \"98.4K subscribers\",   \"video_count\": \"181 videos\",   \"view_count\": \"53,218,926 views\",   \"country\": \"United States\",   \"creation_date\": \"Oct 28, 2022\",   \"links\": [     {\"name\": \"Discord\", \"url\": \"https://discord.gg/tvuxxcsgSS\"},     {\"name\": \"Twitter\", \"url\": \"https://twitter.com/...\"}   ],   \"avatar\": [],   \"banner\": [],   \"verified\": false,   \"has_business_email\": true,   \"continuation_token\": null } ```  ### 注意事项: - **必须进行两次请求才能获取完整的频道信息** - 第一次请求: 获取基本信息（title、avatar、banner、keywords、rss_url等）和 continuation_token - 第二次请求: 获取高级信息（creation_date、links、view_count、country等） - 建议两次请求都设置 `need_format=true` 获取清洗后的数据 - 可以合并两次请求的结果来获得完整的频道信息  # [English] ### Purpose: - Get YouTube channel description information (subscribers, videos, views, creation date, social links, etc.)  ### Important - Two requests required for complete data: - **First request** (with channel_id): Returns basic info (title, description, subscribers, videos, avatar, banner, etc.) - **Second request** (with continuation_token): Returns advanced info (**creation date, social media links, country, view count**, etc.)  ### How to get channel_id: - If you only have channel URL (e.g., `https://www.youtube.com/@CozyCraftYT`), call **get_channel_id_v2** endpoint first - It will return channel_id like `UCeu6U67OzJhV1KwBansH3Dg`  ### Parameters:  #### 📌 Required (choose one): **channel_id** (string) - **Purpose**: Channel ID for first request to get basic channel info - **Format**: Usually starts with `UC`, 24 characters - **Example**: `\"UCeu6U67OzJhV1KwBansH3Dg\"` - **How to get**: Call **get_channel_id_v2** endpoint with channel URL  **continuation_token** (string) - **Purpose**: Pagination token for second request to get advanced info - **How to get**: Get `continuation_token` field from first request response - **Note**: Must provide either `channel_id` or `continuation_token`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  **country_code** (string, optional) - **Purpose**: Set region code - **Default**: `\"US\"` - **Values**: `\"US\"`, `\"JP\"`, `\"GB\"`, etc.  **need_format** (boolean, optional) - **Purpose**: Whether to return cleaned simplified data - **Default**: `false` - **Values**:   - `false` - Return raw complete data   - `true` - Return cleaned simplified data (recommended)  ### Usage Flow (3 steps for complete data): 1. **Get channel_id**: If you only have URL, call `get_channel_id_v2?channel_url=https://www.youtube.com/@CozyCraftYT` 2. **First request**: Use `channel_id` parameter to get basic info and `continuation_token` 3. **Second request**: Use `continuation_token` to get advanced info (creation date, social links, etc.)  ### Response Structure (need_format=true):  #### First request response (with channel_id): ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": \"CozyCraft\",   \"handle\": \"CozyCraftYT\",   \"description\": \"Channel description...\",   \"subscriber_count\": \"98.4K subscribers\",   \"video_count\": \"181 videos\",   \"view_count\": null,   \"country\": null,   \"creation_date\": null,   \"links\": [],   \"avatar\": [{\"url\": \"...\", \"width\": 900, \"height\": 900}],   \"banner\": [{\"url\": \"...\", \"width\": 2560, \"height\": 424}],   \"keywords\": \"Minecraft Ambience...\",   \"channel_url\": \"https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg\",   \"vanity_url\": \"http://www.youtube.com/@CozyCraftYT\",   \"rss_url\": \"https://www.youtube.com/feeds/videos.xml?channel_id=UCeu6U67OzJhV1KwBansH3Dg\",   \"is_family_safe\": true,   \"verified\": false,   \"has_business_email\": false,   \"has_membership\": true,   \"continuation_token\": \"4qmFsgJg...\" } ```  #### Second request response (with continuation_token): ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": null,   \"handle\": \"CozyCraftYT\",   \"description\": \"Full channel description...\",   \"subscriber_count\": \"98.4K subscribers\",   \"video_count\": \"181 videos\",   \"view_count\": \"53,218,926 views\",   \"country\": \"United States\",   \"creation_date\": \"Oct 28, 2022\",   \"links\": [     {\"name\": \"Discord\", \"url\": \"https://discord.gg/tvuxxcsgSS\"},     {\"name\": \"Twitter\", \"url\": \"https://twitter.com/...\"}   ],   \"avatar\": [],   \"banner\": [],   \"verified\": false,   \"has_business_email\": true,   \"continuation_token\": null } ```  ### Notes: - **Two requests are required to get complete channel information** - First request: Get basic info (title, avatar, banner, keywords, rss_url, etc.) and continuation_token - Second request: Get advanced info (creation_date, links, view_count, country, etc.) - Recommend setting `need_format=true` for both requests - You can merge results from both requests for complete channel info  # [示例/Examples] ## 步骤1 - 获取channel_id（如果只有URL） GET /youtube_web/get_channel_id_v2?channel_url=https://www.youtube.com/@CozyCraftYT  ## 步骤2 - 第一次请求获取基本信息和continuation_token GET /youtube_web/get_channel_description?channel_id=UCeu6U67OzJhV1KwBansH3Dg&need_format=true  ## 步骤3 - 第二次请求获取高级信息（使用返回的continuation_token） GET /youtube_web/get_channel_description?continuation_token=xxx&need_format=true  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_description_api_v1_youtube_web_get_channel_description_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID（格式如：UCeu6U67OzJhV1KwBansH3Dg），可通过get_channel_id_v2接口从频道URL获取/Channel ID, can be obtained from channel URL via get_channel_id_v2 endpoint
        :param object continuation_token: 翻页标志（用于获取频道注册时间等高级信息）/Continuation token for getting advanced info like channel creation date
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, JP等）/Country code
        :param object need_format: 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_channel_description_api_v1_youtube_web_get_channel_description_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_channel_description_api_v1_youtube_web_get_channel_description_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_channel_description_api_v1_youtube_web_get_channel_description_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取频道描述信息/Get channel description  # noqa: E501

        # [中文] ### 用途: - 获取YouTube频道的介绍信息（订阅数、视频数、观看次数、注册时间、社交链接等）  ### 重要提示 - 需要两次请求获取完整数据: - **第一次请求**（使用channel_id）: 返回基本信息（频道名称、描述、订阅数、视频数、头像、横幅等） - **第二次请求**（使用continuation_token）: 返回高级信息（**注册时间、社交媒体链接、国家、观看次数**等）  ### 如何获取channel_id: - 如果你只有频道URL（如 `https://www.youtube.com/@CozyCraftYT`），请先调用 **get_channel_id_v2** 接口获取channel_id - 该接口会返回类似 `UCeu6U67OzJhV1KwBansH3Dg` 的频道ID  ### 参数详解:  #### 📌 必选参数（二选一）: **channel_id** (string) - **作用**: 频道ID，用于第一次请求获取频道基本信息 - **格式**: 通常以 `UC` 开头的24位字符串 - **示例**: `\"UCeu6U67OzJhV1KwBansH3Dg\"` - **获取方式**: 调用 **get_channel_id_v2** 接口，传入频道URL即可获取  **continuation_token** (string) - **作用**: 翻页标志，用于第二次请求获取频道的高级信息 - **获取方式**: 从第一次请求的响应中获取 `continuation_token` 字段 - **注意**: `channel_id` 和 `continuation_token` 必须提供其中一个  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置显示语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 使用流程（三步获取完整数据）: 1. **获取channel_id**: 如果只有频道URL，先调用 `get_channel_id_v2?channel_url=https://www.youtube.com/@CozyCraftYT` 2. **第一次请求**: 使用 `channel_id` 参数获取频道基本信息，同时获取 `continuation_token` 3. **第二次请求**: 使用 `continuation_token` 获取高级信息（注册时间、社交链接等）  ### 返回数据结构 (need_format=true):  #### 第一次请求返回（使用channel_id）: ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": \"CozyCraft\",   \"handle\": \"CozyCraftYT\",   \"description\": \"频道介绍...\",   \"subscriber_count\": \"9.84万位订阅者\",   \"video_count\": \"181 个视频\",   \"view_count\": null,   \"country\": null,   \"creation_date\": null,   \"links\": [],   \"avatar\": [{\"url\": \"...\", \"width\": 900, \"height\": 900}],   \"banner\": [{\"url\": \"...\", \"width\": 2560, \"height\": 424}],   \"keywords\": \"Minecraft Ambience...\",   \"channel_url\": \"https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg\",   \"vanity_url\": \"http://www.youtube.com/@CozyCraftYT\",   \"rss_url\": \"https://www.youtube.com/feeds/videos.xml?channel_id=UCeu6U67OzJhV1KwBansH3Dg\",   \"is_family_safe\": true,   \"verified\": false,   \"has_business_email\": false,   \"has_membership\": true,   \"continuation_token\": \"4qmFsgJg...\" } ```  #### 第二次请求返回（使用continuation_token）: ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": null,   \"handle\": \"CozyCraftYT\",   \"description\": \"完整频道介绍...\",   \"subscriber_count\": \"98.4K subscribers\",   \"video_count\": \"181 videos\",   \"view_count\": \"53,218,926 views\",   \"country\": \"United States\",   \"creation_date\": \"Oct 28, 2022\",   \"links\": [     {\"name\": \"Discord\", \"url\": \"https://discord.gg/tvuxxcsgSS\"},     {\"name\": \"Twitter\", \"url\": \"https://twitter.com/...\"}   ],   \"avatar\": [],   \"banner\": [],   \"verified\": false,   \"has_business_email\": true,   \"continuation_token\": null } ```  ### 注意事项: - **必须进行两次请求才能获取完整的频道信息** - 第一次请求: 获取基本信息（title、avatar、banner、keywords、rss_url等）和 continuation_token - 第二次请求: 获取高级信息（creation_date、links、view_count、country等） - 建议两次请求都设置 `need_format=true` 获取清洗后的数据 - 可以合并两次请求的结果来获得完整的频道信息  # [English] ### Purpose: - Get YouTube channel description information (subscribers, videos, views, creation date, social links, etc.)  ### Important - Two requests required for complete data: - **First request** (with channel_id): Returns basic info (title, description, subscribers, videos, avatar, banner, etc.) - **Second request** (with continuation_token): Returns advanced info (**creation date, social media links, country, view count**, etc.)  ### How to get channel_id: - If you only have channel URL (e.g., `https://www.youtube.com/@CozyCraftYT`), call **get_channel_id_v2** endpoint first - It will return channel_id like `UCeu6U67OzJhV1KwBansH3Dg`  ### Parameters:  #### 📌 Required (choose one): **channel_id** (string) - **Purpose**: Channel ID for first request to get basic channel info - **Format**: Usually starts with `UC`, 24 characters - **Example**: `\"UCeu6U67OzJhV1KwBansH3Dg\"` - **How to get**: Call **get_channel_id_v2** endpoint with channel URL  **continuation_token** (string) - **Purpose**: Pagination token for second request to get advanced info - **How to get**: Get `continuation_token` field from first request response - **Note**: Must provide either `channel_id` or `continuation_token`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  **country_code** (string, optional) - **Purpose**: Set region code - **Default**: `\"US\"` - **Values**: `\"US\"`, `\"JP\"`, `\"GB\"`, etc.  **need_format** (boolean, optional) - **Purpose**: Whether to return cleaned simplified data - **Default**: `false` - **Values**:   - `false` - Return raw complete data   - `true` - Return cleaned simplified data (recommended)  ### Usage Flow (3 steps for complete data): 1. **Get channel_id**: If you only have URL, call `get_channel_id_v2?channel_url=https://www.youtube.com/@CozyCraftYT` 2. **First request**: Use `channel_id` parameter to get basic info and `continuation_token` 3. **Second request**: Use `continuation_token` to get advanced info (creation date, social links, etc.)  ### Response Structure (need_format=true):  #### First request response (with channel_id): ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": \"CozyCraft\",   \"handle\": \"CozyCraftYT\",   \"description\": \"Channel description...\",   \"subscriber_count\": \"98.4K subscribers\",   \"video_count\": \"181 videos\",   \"view_count\": null,   \"country\": null,   \"creation_date\": null,   \"links\": [],   \"avatar\": [{\"url\": \"...\", \"width\": 900, \"height\": 900}],   \"banner\": [{\"url\": \"...\", \"width\": 2560, \"height\": 424}],   \"keywords\": \"Minecraft Ambience...\",   \"channel_url\": \"https://www.youtube.com/channel/UCeu6U67OzJhV1KwBansH3Dg\",   \"vanity_url\": \"http://www.youtube.com/@CozyCraftYT\",   \"rss_url\": \"https://www.youtube.com/feeds/videos.xml?channel_id=UCeu6U67OzJhV1KwBansH3Dg\",   \"is_family_safe\": true,   \"verified\": false,   \"has_business_email\": false,   \"has_membership\": true,   \"continuation_token\": \"4qmFsgJg...\" } ```  #### Second request response (with continuation_token): ```json {   \"channel_id\": \"UCeu6U67OzJhV1KwBansH3Dg\",   \"title\": null,   \"handle\": \"CozyCraftYT\",   \"description\": \"Full channel description...\",   \"subscriber_count\": \"98.4K subscribers\",   \"video_count\": \"181 videos\",   \"view_count\": \"53,218,926 views\",   \"country\": \"United States\",   \"creation_date\": \"Oct 28, 2022\",   \"links\": [     {\"name\": \"Discord\", \"url\": \"https://discord.gg/tvuxxcsgSS\"},     {\"name\": \"Twitter\", \"url\": \"https://twitter.com/...\"}   ],   \"avatar\": [],   \"banner\": [],   \"verified\": false,   \"has_business_email\": true,   \"continuation_token\": null } ```  ### Notes: - **Two requests are required to get complete channel information** - First request: Get basic info (title, avatar, banner, keywords, rss_url, etc.) and continuation_token - Second request: Get advanced info (creation_date, links, view_count, country, etc.) - Recommend setting `need_format=true` for both requests - You can merge results from both requests for complete channel info  # [示例/Examples] ## 步骤1 - 获取channel_id（如果只有URL） GET /youtube_web/get_channel_id_v2?channel_url=https://www.youtube.com/@CozyCraftYT  ## 步骤2 - 第一次请求获取基本信息和continuation_token GET /youtube_web/get_channel_description?channel_id=UCeu6U67OzJhV1KwBansH3Dg&need_format=true  ## 步骤3 - 第二次请求获取高级信息（使用返回的continuation_token） GET /youtube_web/get_channel_description?continuation_token=xxx&need_format=true  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_description_api_v1_youtube_web_get_channel_description_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID（格式如：UCeu6U67OzJhV1KwBansH3Dg），可通过get_channel_id_v2接口从频道URL获取/Channel ID, can be obtained from channel URL via get_channel_id_v2 endpoint
        :param object continuation_token: 翻页标志（用于获取频道注册时间等高级信息）/Continuation token for getting advanced info like channel creation date
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, JP等）/Country code
        :param object need_format: 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id', 'continuation_token', 'language_code', 'country_code', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_channel_description_api_v1_youtube_web_get_channel_description_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in params:
            query_params.append(('channel_id', params['channel_id']))  # noqa: E501
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_channel_description', 'GET',
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

    def get_channel_id_api_v1_youtube_web_get_channel_id_get(self, channel_name, **kwargs):  # noqa: E501
        """获取频道ID/Get channel ID  # noqa: E501

        # [中文] ### 用途: - 获取频道ID。 ### 参数: - channel_name: 频道名称。 ### 返回: - 频道ID。  # [English] ### Purpose: - Get channel ID. ### Parameters: - channel_name: Channel name. ### Returns: - Channel ID.  # [示例/Example] channel_name = \"LinusTechTips\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_id_api_v1_youtube_web_get_channel_id_get(channel_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_name: 频道名称/Channel name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_channel_id_api_v1_youtube_web_get_channel_id_get_with_http_info(channel_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_channel_id_api_v1_youtube_web_get_channel_id_get_with_http_info(channel_name, **kwargs)  # noqa: E501
            return data

    def get_channel_id_api_v1_youtube_web_get_channel_id_get_with_http_info(self, channel_name, **kwargs):  # noqa: E501
        """获取频道ID/Get channel ID  # noqa: E501

        # [中文] ### 用途: - 获取频道ID。 ### 参数: - channel_name: 频道名称。 ### 返回: - 频道ID。  # [English] ### Purpose: - Get channel ID. ### Parameters: - channel_name: Channel name. ### Returns: - Channel ID.  # [示例/Example] channel_name = \"LinusTechTips\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_id_api_v1_youtube_web_get_channel_id_get_with_http_info(channel_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_name: 频道名称/Channel name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_channel_id_api_v1_youtube_web_get_channel_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_name' is set
        if self.api_client.client_side_validation and ('channel_name' not in params or
                                                       params['channel_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `channel_name` when calling `get_channel_id_api_v1_youtube_web_get_channel_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_name' in params:
            query_params.append(('channel_name', params['channel_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_channel_id', 'GET',
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

    def get_channel_id_v2_api_v1_youtube_web_get_channel_id_v2_get(self, channel_url, **kwargs):  # noqa: E501
        """从频道URL获取频道ID V2/Get channel ID from URL V2  # noqa: E501

        # [中文] ### 用途: - 从YouTube频道URL转换获取频道ID（channel_id）。 - 支持多种URL格式，包括@用户名格式、/channel/格式、/c/格式、/user/格式。 ### 参数: - channel_url: 频道URL。 ### 返回: - channel_id: 频道ID（如：UCeu6U67OzJhV1KwBansH3Dg） - channel_url: 标准化的频道URL - source: 数据来源（url_parse表示直接从URL解析，page_parse表示从页面解析）  # [English] ### Purpose: - Convert YouTube channel URL to channel ID. - Supports multiple URL formats including @username, /channel/, /c/, /user/ formats. ### Parameters: - channel_url: Channel URL. ### Returns: - channel_id: Channel ID (e.g., UCeu6U67OzJhV1KwBansH3Dg) - channel_url: Normalized channel URL - source: Data source (url_parse means parsed from URL directly, page_parse means parsed from page)  # [示例/Example] channel_url = \"https://www.youtube.com/@CozyCraftYT\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_id_v2_api_v1_youtube_web_get_channel_id_v2_get(channel_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_url: 频道URL/Channel URL，支持多种格式如：https://www.youtube.com/@username, https://www.youtube.com/channel/UCxxxxxx, https://www.youtube.com/c/channelname (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_channel_id_v2_api_v1_youtube_web_get_channel_id_v2_get_with_http_info(channel_url, **kwargs)  # noqa: E501
        else:
            (data) = self.get_channel_id_v2_api_v1_youtube_web_get_channel_id_v2_get_with_http_info(channel_url, **kwargs)  # noqa: E501
            return data

    def get_channel_id_v2_api_v1_youtube_web_get_channel_id_v2_get_with_http_info(self, channel_url, **kwargs):  # noqa: E501
        """从频道URL获取频道ID V2/Get channel ID from URL V2  # noqa: E501

        # [中文] ### 用途: - 从YouTube频道URL转换获取频道ID（channel_id）。 - 支持多种URL格式，包括@用户名格式、/channel/格式、/c/格式、/user/格式。 ### 参数: - channel_url: 频道URL。 ### 返回: - channel_id: 频道ID（如：UCeu6U67OzJhV1KwBansH3Dg） - channel_url: 标准化的频道URL - source: 数据来源（url_parse表示直接从URL解析，page_parse表示从页面解析）  # [English] ### Purpose: - Convert YouTube channel URL to channel ID. - Supports multiple URL formats including @username, /channel/, /c/, /user/ formats. ### Parameters: - channel_url: Channel URL. ### Returns: - channel_id: Channel ID (e.g., UCeu6U67OzJhV1KwBansH3Dg) - channel_url: Normalized channel URL - source: Data source (url_parse means parsed from URL directly, page_parse means parsed from page)  # [示例/Example] channel_url = \"https://www.youtube.com/@CozyCraftYT\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_id_v2_api_v1_youtube_web_get_channel_id_v2_get_with_http_info(channel_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_url: 频道URL/Channel URL，支持多种格式如：https://www.youtube.com/@username, https://www.youtube.com/channel/UCxxxxxx, https://www.youtube.com/c/channelname (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_channel_id_v2_api_v1_youtube_web_get_channel_id_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_url' is set
        if self.api_client.client_side_validation and ('channel_url' not in params or
                                                       params['channel_url'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `channel_url` when calling `get_channel_id_v2_api_v1_youtube_web_get_channel_id_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_url' in params:
            query_params.append(('channel_url', params['channel_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_channel_id_v2', 'GET',
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

    def get_channel_info_api_v1_youtube_web_get_channel_info_get(self, channel_id, **kwargs):  # noqa: E501
        """获取频道信息/Get channel information  # noqa: E501

        # [中文] ### 用途: - 获取频道信息。 ### 参数: - channel_id: 频道ID。 ### 返回: - 频道信息。  # [English] ### Purpose: - Get channel information. ### Parameters: - channel_id: Channel ID. ### Returns: - Channel information.  # [示例/Example] channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_info_api_v1_youtube_web_get_channel_info_get(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_channel_info_api_v1_youtube_web_get_channel_info_get_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_channel_info_api_v1_youtube_web_get_channel_info_get_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def get_channel_info_api_v1_youtube_web_get_channel_info_get_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """获取频道信息/Get channel information  # noqa: E501

        # [中文] ### 用途: - 获取频道信息。 ### 参数: - channel_id: 频道ID。 ### 返回: - 频道信息。  # [English] ### Purpose: - Get channel information. ### Parameters: - channel_id: Channel ID. ### Returns: - Channel information.  # [示例/Example] channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_info_api_v1_youtube_web_get_channel_info_get_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_channel_info_api_v1_youtube_web_get_channel_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if self.api_client.client_side_validation and ('channel_id' not in params or
                                                       params['channel_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `channel_id` when calling `get_channel_info_api_v1_youtube_web_get_channel_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in params:
            query_params.append(('channel_id', params['channel_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_channel_info', 'GET',
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

    def get_channel_short_videos_api_v1_youtube_web_get_channel_short_videos_get(self, channel_id, **kwargs):  # noqa: E501
        """获取频道短视频/Get channel short videos  # noqa: E501

        # [中文] ### 用途: - 获取频道短视频。 ### 参数: - channel_id: 频道ID。 - continuation_token: 用于继续获取频道短视频的令牌。默认为None。 ### 返回: - 频道短视频。  # [English] ### Purpose: - Get channel short videos. ### Parameters: - channel_id: Channel ID. - continuation_token: Token to continue fetching channel short videos. Default is None. ### Returns: - Channel short videos.  # [示例/Example] channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_short_videos_api_v1_youtube_web_get_channel_short_videos_get(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_channel_short_videos_api_v1_youtube_web_get_channel_short_videos_get_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_channel_short_videos_api_v1_youtube_web_get_channel_short_videos_get_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def get_channel_short_videos_api_v1_youtube_web_get_channel_short_videos_get_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """获取频道短视频/Get channel short videos  # noqa: E501

        # [中文] ### 用途: - 获取频道短视频。 ### 参数: - channel_id: 频道ID。 - continuation_token: 用于继续获取频道短视频的令牌。默认为None。 ### 返回: - 频道短视频。  # [English] ### Purpose: - Get channel short videos. ### Parameters: - channel_id: Channel ID. - continuation_token: Token to continue fetching channel short videos. Default is None. ### Returns: - Channel short videos.  # [示例/Example] channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_short_videos_api_v1_youtube_web_get_channel_short_videos_get_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id', 'continuation_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_channel_short_videos_api_v1_youtube_web_get_channel_short_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if self.api_client.client_side_validation and ('channel_id' not in params or
                                                       params['channel_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `channel_id` when calling `get_channel_short_videos_api_v1_youtube_web_get_channel_short_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in params:
            query_params.append(('channel_id', params['channel_id']))  # noqa: E501
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_channel_short_videos', 'GET',
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

    def get_channel_url_api_v1_youtube_web_get_channel_url_get(self, channel_id, **kwargs):  # noqa: E501
        """从频道ID获取频道URL/Get channel URL from channel ID  # noqa: E501

        # [中文] ### 用途: - 从YouTube频道ID转换获取频道Handle (@用户名) - 与 get_channel_id_v2 接口互为反向操作  ### 参数: - channel_id: 频道ID（如：UCeu6U67OzJhV1KwBansH3Dg）  ### 返回: - channel_id: 频道ID - handle: 频道Handle（如：CozyCraftYT） - title: 频道名称 - channel_url: 标准频道URL（/channel/格式） - vanity_url: 个性化URL（/@用户名格式）  ### 使用场景: - 当你有频道ID但需要获取@用户名格式的URL时 - 需要展示用户友好的频道链接时  # [English] ### Purpose: - Convert YouTube channel ID to channel handle (@username) - Reverse operation of get_channel_id_v2 endpoint  ### Parameters: - channel_id: Channel ID (e.g., UCeu6U67OzJhV1KwBansH3Dg)  ### Returns: - channel_id: Channel ID - handle: Channel handle (e.g., CozyCraftYT) - title: Channel name - channel_url: Standard channel URL (/channel/ format) - vanity_url: Vanity URL (/@username format)  ### Use Cases: - When you have channel ID but need @username format URL - When you need to display user-friendly channel links  # [示例/Example] channel_id = \"UCeu6U67OzJhV1KwBansH3Dg\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_url_api_v1_youtube_web_get_channel_url_get(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (格式如：UCeu6U67OzJhV1KwBansH3Dg) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_channel_url_api_v1_youtube_web_get_channel_url_get_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_channel_url_api_v1_youtube_web_get_channel_url_get_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def get_channel_url_api_v1_youtube_web_get_channel_url_get_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """从频道ID获取频道URL/Get channel URL from channel ID  # noqa: E501

        # [中文] ### 用途: - 从YouTube频道ID转换获取频道Handle (@用户名) - 与 get_channel_id_v2 接口互为反向操作  ### 参数: - channel_id: 频道ID（如：UCeu6U67OzJhV1KwBansH3Dg）  ### 返回: - channel_id: 频道ID - handle: 频道Handle（如：CozyCraftYT） - title: 频道名称 - channel_url: 标准频道URL（/channel/格式） - vanity_url: 个性化URL（/@用户名格式）  ### 使用场景: - 当你有频道ID但需要获取@用户名格式的URL时 - 需要展示用户友好的频道链接时  # [English] ### Purpose: - Convert YouTube channel ID to channel handle (@username) - Reverse operation of get_channel_id_v2 endpoint  ### Parameters: - channel_id: Channel ID (e.g., UCeu6U67OzJhV1KwBansH3Dg)  ### Returns: - channel_id: Channel ID - handle: Channel handle (e.g., CozyCraftYT) - title: Channel name - channel_url: Standard channel URL (/channel/ format) - vanity_url: Vanity URL (/@username format)  ### Use Cases: - When you have channel ID but need @username format URL - When you need to display user-friendly channel links  # [示例/Example] channel_id = \"UCeu6U67OzJhV1KwBansH3Dg\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_url_api_v1_youtube_web_get_channel_url_get_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (格式如：UCeu6U67OzJhV1KwBansH3Dg) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_channel_url_api_v1_youtube_web_get_channel_url_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if self.api_client.client_side_validation and ('channel_id' not in params or
                                                       params['channel_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `channel_id` when calling `get_channel_url_api_v1_youtube_web_get_channel_url_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in params:
            query_params.append(('channel_id', params['channel_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_channel_url', 'GET',
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

    def get_channel_videos_api_v1_youtube_web_get_channel_videos_get(self, channel_id, **kwargs):  # noqa: E501
        """获取频道视频 V1（即将过时，优先使用 V2）/Get channel videos V1 (deprecated soon, use V2 first)  # noqa: E501

        # [中文] ### 用途: - 获取频道视频。 ### 参数: - channel_id: 频道ID。 - continuation_token: 用于继续获取频道视频的令牌。默认为None。 ### 返回: - 频道视频。  # [English] ### Purpose: - Get channel videos. ### Parameters: - channel_id: Channel ID. - continuation_token: Token to continue fetching channel videos. Default is None. ### Returns: - Channel videos.  # [示例/Example] channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_videos_api_v1_youtube_web_get_channel_videos_get(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_channel_videos_api_v1_youtube_web_get_channel_videos_get_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_channel_videos_api_v1_youtube_web_get_channel_videos_get_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def get_channel_videos_api_v1_youtube_web_get_channel_videos_get_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """获取频道视频 V1（即将过时，优先使用 V2）/Get channel videos V1 (deprecated soon, use V2 first)  # noqa: E501

        # [中文] ### 用途: - 获取频道视频。 ### 参数: - channel_id: 频道ID。 - continuation_token: 用于继续获取频道视频的令牌。默认为None。 ### 返回: - 频道视频。  # [English] ### Purpose: - Get channel videos. ### Parameters: - channel_id: Channel ID. - continuation_token: Token to continue fetching channel videos. Default is None. ### Returns: - Channel videos.  # [示例/Example] channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_videos_api_v1_youtube_web_get_channel_videos_get_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id', 'continuation_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_channel_videos_api_v1_youtube_web_get_channel_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if self.api_client.client_side_validation and ('channel_id' not in params or
                                                       params['channel_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `channel_id` when calling `get_channel_videos_api_v1_youtube_web_get_channel_videos_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in params:
            query_params.append(('channel_id', params['channel_id']))  # noqa: E501
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_channel_videos', 'GET',
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

    def get_channel_videos_v2_api_v1_youtube_web_get_channel_videos_v2_get(self, channel_id, **kwargs):  # noqa: E501
        """获取频道视频 V2/Get channel videos V2  # noqa: E501

        # [中文]  ### 用途: - 获取频道视频 V2，支持获取频道视频列表，频道短视频列表，频道直播列表。  ### 参数: - channel_id: 频道ID或频道名称，如果是频道名称，则需要在前面加上 `@` 符号，例如：@LinusTechTips。 - lang: 视频结果语言代码，默认为 `en-US`，任何语言代码均可，当提交不支持的语言代码时，默认使用 `en-US` 作为语言代码。 - sortBy: 排序方式，默认为 `newest`，可选值为 `newest` 和 `oldest` 和 `mostPopular`：     - newest: 按照最新排序，默认值。     - oldest: 按照最旧排序。     - mostPopular: 按照最热排序。 - contentType: 内容类型，默认为 `videos`，可选值为 `videos` 和 `shorts` 和 `live`：     - videos: 视频列表，默认值。     - shorts: 短视频列表。     - live: 直播列表。 - nextToken: 用于继续获取视频的令牌。可选参数，默认值为空，从第一页开始获取。     - 如果获取第一页，则nextToken参数为None。     - 如果获取第二页，则nextToken参数为第一页请求返回的nextToken。  ### 返回: - 频道视频列表，包含视频ID、标题、缩略图、观看次数、点赞次数、评论数、视频时长等信息。  # [English]  ### Purpose: - Get channel videos V2, support getting channel video list, channel short video list, channel live list.  ### Parameters: - channel_id: Channel ID or channel name, if it is a channel name, add `@` symbol in front of it, for example: @LinusTechTips. - lang: Video result language code, default is `en-US`, any language code is supported, when submitting unsupported language code, default use `en-US` as language code. - sortBy: Sort by, default is `newest`, optional values are `newest` and `oldest` and `mostPopular`:     - newest: Sort by newest, default value.     - oldest: Sort by oldest.     - mostPopular: Sort by most popular. - contentType: Content type, default is `videos`, optional values are `videos`     - videos: Video list, default value.     - shorts: Short video list.     - live: Live list. - nextToken: Token to continue fetching videos. Optional parameter, default value is empty, start from the first page.     - If fetching the first page, the nextToken parameter is None.     - If fetching the second page, the nextToken parameter is the nextToken returned by the first page request. ### Returns: - Channel video list, including video ID, title, thumbnail, view count, like count, comment count, video duration and other information.  # [示例/Example] channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\" lang = \"en-US\" sortBy = \"newest\" contentType = \"videos\" nextToken = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_videos_v2_api_v1_youtube_web_get_channel_videos_v2_get(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :param object lang: 视频结果语言代码/Video result language code
        :param object sort_by: 排序方式/Sort by
        :param object content_type: 内容类型/Content type
        :param object next_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_channel_videos_v2_api_v1_youtube_web_get_channel_videos_v2_get_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_channel_videos_v2_api_v1_youtube_web_get_channel_videos_v2_get_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def get_channel_videos_v2_api_v1_youtube_web_get_channel_videos_v2_get_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """获取频道视频 V2/Get channel videos V2  # noqa: E501

        # [中文]  ### 用途: - 获取频道视频 V2，支持获取频道视频列表，频道短视频列表，频道直播列表。  ### 参数: - channel_id: 频道ID或频道名称，如果是频道名称，则需要在前面加上 `@` 符号，例如：@LinusTechTips。 - lang: 视频结果语言代码，默认为 `en-US`，任何语言代码均可，当提交不支持的语言代码时，默认使用 `en-US` 作为语言代码。 - sortBy: 排序方式，默认为 `newest`，可选值为 `newest` 和 `oldest` 和 `mostPopular`：     - newest: 按照最新排序，默认值。     - oldest: 按照最旧排序。     - mostPopular: 按照最热排序。 - contentType: 内容类型，默认为 `videos`，可选值为 `videos` 和 `shorts` 和 `live`：     - videos: 视频列表，默认值。     - shorts: 短视频列表。     - live: 直播列表。 - nextToken: 用于继续获取视频的令牌。可选参数，默认值为空，从第一页开始获取。     - 如果获取第一页，则nextToken参数为None。     - 如果获取第二页，则nextToken参数为第一页请求返回的nextToken。  ### 返回: - 频道视频列表，包含视频ID、标题、缩略图、观看次数、点赞次数、评论数、视频时长等信息。  # [English]  ### Purpose: - Get channel videos V2, support getting channel video list, channel short video list, channel live list.  ### Parameters: - channel_id: Channel ID or channel name, if it is a channel name, add `@` symbol in front of it, for example: @LinusTechTips. - lang: Video result language code, default is `en-US`, any language code is supported, when submitting unsupported language code, default use `en-US` as language code. - sortBy: Sort by, default is `newest`, optional values are `newest` and `oldest` and `mostPopular`:     - newest: Sort by newest, default value.     - oldest: Sort by oldest.     - mostPopular: Sort by most popular. - contentType: Content type, default is `videos`, optional values are `videos`     - videos: Video list, default value.     - shorts: Short video list.     - live: Live list. - nextToken: Token to continue fetching videos. Optional parameter, default value is empty, start from the first page.     - If fetching the first page, the nextToken parameter is None.     - If fetching the second page, the nextToken parameter is the nextToken returned by the first page request. ### Returns: - Channel video list, including video ID, title, thumbnail, view count, like count, comment count, video duration and other information.  # [示例/Example] channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\" lang = \"en-US\" sortBy = \"newest\" contentType = \"videos\" nextToken = None  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_videos_v2_api_v1_youtube_web_get_channel_videos_v2_get_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :param object lang: 视频结果语言代码/Video result language code
        :param object sort_by: 排序方式/Sort by
        :param object content_type: 内容类型/Content type
        :param object next_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id', 'lang', 'sort_by', 'content_type', 'next_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_channel_videos_v2_api_v1_youtube_web_get_channel_videos_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if self.api_client.client_side_validation and ('channel_id' not in params or
                                                       params['channel_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `channel_id` when calling `get_channel_videos_v2_api_v1_youtube_web_get_channel_videos_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in params:
            query_params.append(('channel_id', params['channel_id']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501
        if 'content_type' in params:
            query_params.append(('contentType', params['content_type']))  # noqa: E501
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_channel_videos_v2', 'GET',
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

    def get_channel_videos_v3_api_v1_youtube_web_get_channel_videos_v3_get(self, channel_id, **kwargs):  # noqa: E501
        """获取频道视频 V3/Get channel videos V3  # noqa: E501

        # [中文] ### 用途: - 获取YouTube频道的视频列表 V3 - 支持分页获取，可通过 continuation_token 获取更多视频  ### 参数详解:  #### 📌 必选参数: **channel_id** (string) - **作用**: 频道ID - **获取方式**:   - 从频道URL中提取，例如 `https://www.youtube.com/channel/UCJHBJ7F-nAIlMGolm0Hu4vg`   - 或从 `@用户名` 格式的URL中，先访问频道页面获取真实的频道ID - **示例**: `\"UCJHBJ7F-nAIlMGolm0Hu4vg\"`  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **continuation_token** (string, 可选) - **作用**: 分页token，用于获取下一页视频 - **获取方式**: 从上一次请求的响应中提取 - **首次请求**: 不传此参数或传 `null`  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 返回数据结构 (need_format=true): ```json {   \"videos\": [     {       \"video_id\": \"zd3yCa1bJCM\",       \"title\": \"Minecraft: DREAM! - Asleep Custom Map\",       \"thumbnail\": \"https://i.ytimg.com/vi/zd3yCa1bJCM/hqdefault.jpg\",       \"thumbnails\": [         {\"url\": \"...\", \"width\": 168, \"height\": 94},         {\"url\": \"...\", \"width\": 336, \"height\": 188}       ],       \"moving_thumbnail\": \"https://i.ytimg.com/an_webp/zd3yCa1bJCM/mqdefault_6s.webp?...\",       \"duration\": \"16:57\",       \"duration_accessibility\": \"16分钟57秒钟\",       \"view_count\": \"343,369次观看\",       \"short_view_count\": \"34万次观看\",       \"published_time\": \"18小时前\",       \"description\": \"Today, we're trapped in a super weird dream...\",       \"is_live\": false,       \"is_verified\": true,       \"url\": \"https://www.youtube.com/watch?v=zd3yCa1bJCM\",       \"playback_url\": \"https://rr5---sn-ogueln67.googlevideo.com/initplayback?...\"     }   ],   \"continuation_token\": \"下一页token\" } ```  ### 清洗后的字段说明: - `video_id`: 视频ID - `title`: 视频标题 - `thumbnail`: 最高清晰度缩略图URL - `thumbnails`: 所有分辨率的缩略图列表 - `moving_thumbnail`: 动态缩略图URL（webp格式，鼠标悬停预览） - `duration`: 视频时长（如\"16:57\"） - `duration_accessibility`: 时长无障碍文本（如\"16分钟57秒钟\"） - `view_count`: 完整观看次数（如\"343,369次观看\"） - `short_view_count`: 简短观看次数（如\"34万次观看\"） - `published_time`: 发布时间（如\"18小时前\"） - `description`: 视频描述片段 - `is_live`: 是否为直播 - `is_verified`: 频道是否已认证 - `url`: 视频播放页URL - `playback_url`: 视频播放初始化URL（googlevideo.com，可能为空） - `continuation_token`: 下一页的分页token  # [English] ### Purpose: - Get YouTube channel video list V3 - Supports pagination via continuation_token  ### Parameters:  #### 📌 Required: **channel_id** (string) - **Purpose**: Channel ID - **How to get**:   - Extract from channel URL, e.g., `https://www.youtube.com/channel/UCJHBJ7F-nAIlMGolm0Hu4vg`   - Or visit the channel page to get the real channel ID from `@username` format URLs - **Example**: `\"UCJHBJ7F-nAIlMGolm0Hu4vg\"`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  **country_code** (string, optional) - **Purpose**: Set region code - **Default**: `\"US\"` - **Values**: `\"US\"`, `\"JP\"`, `\"GB\"`, etc.  **continuation_token** (string, optional) - **Purpose**: Pagination token for next page - **How to get**: Extract from previous response - **First request**: Omit or set to `null`  **need_format** (boolean, optional) - **Purpose**: Whether to return cleaned simplified data - **Default**: `false` - **Values**:   - `false` - Return raw complete data   - `true` - Return cleaned simplified data (recommended)  ### Response Structure (need_format=true): ```json {   \"videos\": [     {       \"video_id\": \"zd3yCa1bJCM\",       \"title\": \"Minecraft: DREAM! - Asleep Custom Map\",       \"thumbnail\": \"https://i.ytimg.com/vi/zd3yCa1bJCM/hqdefault.jpg\",       \"thumbnails\": [         {\"url\": \"...\", \"width\": 168, \"height\": 94},         {\"url\": \"...\", \"width\": 336, \"height\": 188}       ],       \"moving_thumbnail\": \"https://i.ytimg.com/an_webp/zd3yCa1bJCM/mqdefault_6s.webp?...\",       \"duration\": \"16:57\",       \"duration_accessibility\": \"16 minutes, 57 seconds\",       \"view_count\": \"343,369 views\",       \"short_view_count\": \"343K views\",       \"published_time\": \"18 hours ago\",       \"description\": \"Today, we're trapped in a super weird dream...\",       \"is_live\": false,       \"is_verified\": true,       \"url\": \"https://www.youtube.com/watch?v=zd3yCa1bJCM\",       \"playback_url\": \"https://rr5---sn-ogueln67.googlevideo.com/initplayback?...\"     }   ],   \"continuation_token\": \"next page token\" } ```  ### Cleaned Data Field Descriptions: - `video_id`: Video ID - `title`: Video title - `thumbnail`: Highest resolution thumbnail URL - `thumbnails`: List of all resolution thumbnails - `moving_thumbnail`: Moving thumbnail URL (webp format, hover preview) - `duration`: Video duration (e.g., \"16:57\") - `duration_accessibility`: Duration accessibility text (e.g., \"16 minutes, 57 seconds\") - `view_count`: Full view count (e.g., \"343,369 views\") - `short_view_count`: Short view count (e.g., \"343K views\") - `published_time`: Published time (e.g., \"18 hours ago\") - `description`: Video description snippet - `is_live`: Whether it's a live stream - `is_verified`: Whether the channel is verified - `url`: Video playback page URL - `playback_url`: Video playback initialization URL (googlevideo.com, may be empty) - `continuation_token`: Pagination token for next page  # [示例/Examples] ## 获取频道首页视频 / Get first page of channel videos GET /youtube_web/get_channel_videos_v3?channel_id=UCJHBJ7F-nAIlMGolm0Hu4vg  ## 获取清洗后的数据（推荐）/ Get cleaned data (recommended) GET /youtube_web/get_channel_videos_v3?channel_id=UCJHBJ7F-nAIlMGolm0Hu4vg&need_format=true  ## 获取下一页 / Get next page GET /youtube_web/get_channel_videos_v3?channel_id=UCJHBJ7F-nAIlMGolm0Hu4vg&continuation_token=xxxxx&need_format=true  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_videos_v3_api_v1_youtube_web_get_channel_videos_v3_get(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, JP等）/Country code
        :param object continuation_token: 分页token，用于获取下一页/Pagination token for next page
        :param object need_format: 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_channel_videos_v3_api_v1_youtube_web_get_channel_videos_v3_get_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_channel_videos_v3_api_v1_youtube_web_get_channel_videos_v3_get_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def get_channel_videos_v3_api_v1_youtube_web_get_channel_videos_v3_get_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """获取频道视频 V3/Get channel videos V3  # noqa: E501

        # [中文] ### 用途: - 获取YouTube频道的视频列表 V3 - 支持分页获取，可通过 continuation_token 获取更多视频  ### 参数详解:  #### 📌 必选参数: **channel_id** (string) - **作用**: 频道ID - **获取方式**:   - 从频道URL中提取，例如 `https://www.youtube.com/channel/UCJHBJ7F-nAIlMGolm0Hu4vg`   - 或从 `@用户名` 格式的URL中，先访问频道页面获取真实的频道ID - **示例**: `\"UCJHBJ7F-nAIlMGolm0Hu4vg\"`  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **continuation_token** (string, 可选) - **作用**: 分页token，用于获取下一页视频 - **获取方式**: 从上一次请求的响应中提取 - **首次请求**: 不传此参数或传 `null`  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 返回数据结构 (need_format=true): ```json {   \"videos\": [     {       \"video_id\": \"zd3yCa1bJCM\",       \"title\": \"Minecraft: DREAM! - Asleep Custom Map\",       \"thumbnail\": \"https://i.ytimg.com/vi/zd3yCa1bJCM/hqdefault.jpg\",       \"thumbnails\": [         {\"url\": \"...\", \"width\": 168, \"height\": 94},         {\"url\": \"...\", \"width\": 336, \"height\": 188}       ],       \"moving_thumbnail\": \"https://i.ytimg.com/an_webp/zd3yCa1bJCM/mqdefault_6s.webp?...\",       \"duration\": \"16:57\",       \"duration_accessibility\": \"16分钟57秒钟\",       \"view_count\": \"343,369次观看\",       \"short_view_count\": \"34万次观看\",       \"published_time\": \"18小时前\",       \"description\": \"Today, we're trapped in a super weird dream...\",       \"is_live\": false,       \"is_verified\": true,       \"url\": \"https://www.youtube.com/watch?v=zd3yCa1bJCM\",       \"playback_url\": \"https://rr5---sn-ogueln67.googlevideo.com/initplayback?...\"     }   ],   \"continuation_token\": \"下一页token\" } ```  ### 清洗后的字段说明: - `video_id`: 视频ID - `title`: 视频标题 - `thumbnail`: 最高清晰度缩略图URL - `thumbnails`: 所有分辨率的缩略图列表 - `moving_thumbnail`: 动态缩略图URL（webp格式，鼠标悬停预览） - `duration`: 视频时长（如\"16:57\"） - `duration_accessibility`: 时长无障碍文本（如\"16分钟57秒钟\"） - `view_count`: 完整观看次数（如\"343,369次观看\"） - `short_view_count`: 简短观看次数（如\"34万次观看\"） - `published_time`: 发布时间（如\"18小时前\"） - `description`: 视频描述片段 - `is_live`: 是否为直播 - `is_verified`: 频道是否已认证 - `url`: 视频播放页URL - `playback_url`: 视频播放初始化URL（googlevideo.com，可能为空） - `continuation_token`: 下一页的分页token  # [English] ### Purpose: - Get YouTube channel video list V3 - Supports pagination via continuation_token  ### Parameters:  #### 📌 Required: **channel_id** (string) - **Purpose**: Channel ID - **How to get**:   - Extract from channel URL, e.g., `https://www.youtube.com/channel/UCJHBJ7F-nAIlMGolm0Hu4vg`   - Or visit the channel page to get the real channel ID from `@username` format URLs - **Example**: `\"UCJHBJ7F-nAIlMGolm0Hu4vg\"`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  **country_code** (string, optional) - **Purpose**: Set region code - **Default**: `\"US\"` - **Values**: `\"US\"`, `\"JP\"`, `\"GB\"`, etc.  **continuation_token** (string, optional) - **Purpose**: Pagination token for next page - **How to get**: Extract from previous response - **First request**: Omit or set to `null`  **need_format** (boolean, optional) - **Purpose**: Whether to return cleaned simplified data - **Default**: `false` - **Values**:   - `false` - Return raw complete data   - `true` - Return cleaned simplified data (recommended)  ### Response Structure (need_format=true): ```json {   \"videos\": [     {       \"video_id\": \"zd3yCa1bJCM\",       \"title\": \"Minecraft: DREAM! - Asleep Custom Map\",       \"thumbnail\": \"https://i.ytimg.com/vi/zd3yCa1bJCM/hqdefault.jpg\",       \"thumbnails\": [         {\"url\": \"...\", \"width\": 168, \"height\": 94},         {\"url\": \"...\", \"width\": 336, \"height\": 188}       ],       \"moving_thumbnail\": \"https://i.ytimg.com/an_webp/zd3yCa1bJCM/mqdefault_6s.webp?...\",       \"duration\": \"16:57\",       \"duration_accessibility\": \"16 minutes, 57 seconds\",       \"view_count\": \"343,369 views\",       \"short_view_count\": \"343K views\",       \"published_time\": \"18 hours ago\",       \"description\": \"Today, we're trapped in a super weird dream...\",       \"is_live\": false,       \"is_verified\": true,       \"url\": \"https://www.youtube.com/watch?v=zd3yCa1bJCM\",       \"playback_url\": \"https://rr5---sn-ogueln67.googlevideo.com/initplayback?...\"     }   ],   \"continuation_token\": \"next page token\" } ```  ### Cleaned Data Field Descriptions: - `video_id`: Video ID - `title`: Video title - `thumbnail`: Highest resolution thumbnail URL - `thumbnails`: List of all resolution thumbnails - `moving_thumbnail`: Moving thumbnail URL (webp format, hover preview) - `duration`: Video duration (e.g., \"16:57\") - `duration_accessibility`: Duration accessibility text (e.g., \"16 minutes, 57 seconds\") - `view_count`: Full view count (e.g., \"343,369 views\") - `short_view_count`: Short view count (e.g., \"343K views\") - `published_time`: Published time (e.g., \"18 hours ago\") - `description`: Video description snippet - `is_live`: Whether it's a live stream - `is_verified`: Whether the channel is verified - `url`: Video playback page URL - `playback_url`: Video playback initialization URL (googlevideo.com, may be empty) - `continuation_token`: Pagination token for next page  # [示例/Examples] ## 获取频道首页视频 / Get first page of channel videos GET /youtube_web/get_channel_videos_v3?channel_id=UCJHBJ7F-nAIlMGolm0Hu4vg  ## 获取清洗后的数据（推荐）/ Get cleaned data (recommended) GET /youtube_web/get_channel_videos_v3?channel_id=UCJHBJ7F-nAIlMGolm0Hu4vg&need_format=true  ## 获取下一页 / Get next page GET /youtube_web/get_channel_videos_v3?channel_id=UCJHBJ7F-nAIlMGolm0Hu4vg&continuation_token=xxxxx&need_format=true  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_channel_videos_v3_api_v1_youtube_web_get_channel_videos_v3_get_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, JP等）/Country code
        :param object continuation_token: 分页token，用于获取下一页/Pagination token for next page
        :param object need_format: 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id', 'language_code', 'country_code', 'continuation_token', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_channel_videos_v3_api_v1_youtube_web_get_channel_videos_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if self.api_client.client_side_validation and ('channel_id' not in params or
                                                       params['channel_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `channel_id` when calling `get_channel_videos_v3_api_v1_youtube_web_get_channel_videos_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in params:
            query_params.append(('channel_id', params['channel_id']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_channel_videos_v3', 'GET',
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

    def get_general_search_api_v1_youtube_web_get_general_search_get(self, search_query, **kwargs):  # noqa: E501
        """综合搜索（支持过滤条件）/General search with filters  # noqa: E501

        # [中文] ### 用途: - YouTube综合搜索，支持多种过滤条件，可以精确筛选搜索结果  ### 参数详解: - **search_query**: 搜索关键字 - **language_code**: 语言代码，推荐使用zh-CN（中文）或en-US（英文） - **country_code**: 国家代码，影响搜索结果的地区相关性 - **time_zone**: 时区设置  ### 过滤条件 (选择一个值即可): #### 上传时间 (upload_time): - `hour`: 过去1小时内上传 - `today`: 今天上传 - `week`: 本周上传 - `month`: 本月上传 - `year`: 今年上传  #### 视频时长 (duration): - `short`: 短视频（少于4分钟） - `medium`: 中等时长（4-20分钟） - `long`: 长视频（超过20分钟）  #### 内容类型 (content_type): - `video`: 视频 - `channel`: 频道 - `playlist`: 播放列表 - `movie`: 电影  #### 特征 (feature): - `hd`: 高清视频 - `4k`: 4K视频 - `subtitles`: 包含字幕 - `live`: 直播 - `creative_commons`: 知识共享许可 - `360`: 360度视频 - `vr180`: VR180视频 - `3d`: 3D视频 - `hdr`: HDR视频 - `location`: 包含位置信息 - `purchased`: 已购买内容  #### 排序方式 (sort_by): - `relevance`: 相关性（默认） - `upload_date`: 上传日期 - `view_count`: 观看次数 - `rating`: 评分  ### 返回: - 包含过滤条件的搜索结果  # [English] ### Purpose: - YouTube comprehensive search with multiple filter options for precise result filtering  ### Parameters: - **search_query**: Search keyword - **language_code**: Language code (zh-CN for Chinese, en-US for English) - **country_code**: Country code affecting regional relevance - **time_zone**: Time zone setting  ### Filter Options (select one value for each): #### Upload Time (upload_time): - `hour`: Uploaded in the past hour - `today`: Uploaded today - `week`: Uploaded this week - `month`: Uploaded this month - `year`: Uploaded this year  #### Duration (duration): - `short`: Short videos (under 4 minutes) - `medium`: Medium length (4-20 minutes) - `long`: Long videos (over 20 minutes)  #### Content Type (content_type): - `video`: Videos - `channel`: Channels - `playlist`: Playlists - `movie`: Movies  #### Features (feature): - `hd`: High definition - `4k`: 4K videos - `subtitles`: With subtitles - `live`: Live streams - `creative_commons`: Creative Commons licensed - `360`: 360-degree videos - `vr180`: VR180 videos - `3d`: 3D videos - `hdr`: HDR videos - `location`: With location info - `purchased`: Purchased content  #### Sort By (sort_by): - `relevance`: Relevance (default) - `upload_date`: Upload date - `view_count`: View count - `rating`: Rating  ### Returns: - Filtered search results  # [示例/Examples] ## 基础搜索 GET /youtube_web/get_general_search?search_query=Python编程  ## 搜索本周上传的Python编程短视频 GET /youtube_web/get_general_search?search_query=Python编程&upload_time=week&duration=short  ## 搜索高清的Python教程视频，按观看次数排序 GET /youtube_web/get_general_search?search_query=Python tutorial&feature=hd&sort_by=view_count  ## 搜索今天上传的4K编程直播 GET /youtube_web/get_general_search?search_query=programming&upload_time=today&feature=4k&content_type=video  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_general_search_api_v1_youtube_web_get_general_search_get(search_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_query: 搜索关键字/Search keyword (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, CN等）/Country code
        :param object time_zone: 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone
        :param object upload_time: 上传时间过滤 | Upload time filter
        :param object duration: 视频时长过滤 | Duration filter
        :param object content_type: 内容类型过滤 | Content type filter
        :param object feature: 特征过滤 | Feature filter
        :param object sort_by: 排序方式 | Sort by
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_general_search_api_v1_youtube_web_get_general_search_get_with_http_info(search_query, **kwargs)  # noqa: E501
        else:
            (data) = self.get_general_search_api_v1_youtube_web_get_general_search_get_with_http_info(search_query, **kwargs)  # noqa: E501
            return data

    def get_general_search_api_v1_youtube_web_get_general_search_get_with_http_info(self, search_query, **kwargs):  # noqa: E501
        """综合搜索（支持过滤条件）/General search with filters  # noqa: E501

        # [中文] ### 用途: - YouTube综合搜索，支持多种过滤条件，可以精确筛选搜索结果  ### 参数详解: - **search_query**: 搜索关键字 - **language_code**: 语言代码，推荐使用zh-CN（中文）或en-US（英文） - **country_code**: 国家代码，影响搜索结果的地区相关性 - **time_zone**: 时区设置  ### 过滤条件 (选择一个值即可): #### 上传时间 (upload_time): - `hour`: 过去1小时内上传 - `today`: 今天上传 - `week`: 本周上传 - `month`: 本月上传 - `year`: 今年上传  #### 视频时长 (duration): - `short`: 短视频（少于4分钟） - `medium`: 中等时长（4-20分钟） - `long`: 长视频（超过20分钟）  #### 内容类型 (content_type): - `video`: 视频 - `channel`: 频道 - `playlist`: 播放列表 - `movie`: 电影  #### 特征 (feature): - `hd`: 高清视频 - `4k`: 4K视频 - `subtitles`: 包含字幕 - `live`: 直播 - `creative_commons`: 知识共享许可 - `360`: 360度视频 - `vr180`: VR180视频 - `3d`: 3D视频 - `hdr`: HDR视频 - `location`: 包含位置信息 - `purchased`: 已购买内容  #### 排序方式 (sort_by): - `relevance`: 相关性（默认） - `upload_date`: 上传日期 - `view_count`: 观看次数 - `rating`: 评分  ### 返回: - 包含过滤条件的搜索结果  # [English] ### Purpose: - YouTube comprehensive search with multiple filter options for precise result filtering  ### Parameters: - **search_query**: Search keyword - **language_code**: Language code (zh-CN for Chinese, en-US for English) - **country_code**: Country code affecting regional relevance - **time_zone**: Time zone setting  ### Filter Options (select one value for each): #### Upload Time (upload_time): - `hour`: Uploaded in the past hour - `today`: Uploaded today - `week`: Uploaded this week - `month`: Uploaded this month - `year`: Uploaded this year  #### Duration (duration): - `short`: Short videos (under 4 minutes) - `medium`: Medium length (4-20 minutes) - `long`: Long videos (over 20 minutes)  #### Content Type (content_type): - `video`: Videos - `channel`: Channels - `playlist`: Playlists - `movie`: Movies  #### Features (feature): - `hd`: High definition - `4k`: 4K videos - `subtitles`: With subtitles - `live`: Live streams - `creative_commons`: Creative Commons licensed - `360`: 360-degree videos - `vr180`: VR180 videos - `3d`: 3D videos - `hdr`: HDR videos - `location`: With location info - `purchased`: Purchased content  #### Sort By (sort_by): - `relevance`: Relevance (default) - `upload_date`: Upload date - `view_count`: View count - `rating`: Rating  ### Returns: - Filtered search results  # [示例/Examples] ## 基础搜索 GET /youtube_web/get_general_search?search_query=Python编程  ## 搜索本周上传的Python编程短视频 GET /youtube_web/get_general_search?search_query=Python编程&upload_time=week&duration=short  ## 搜索高清的Python教程视频，按观看次数排序 GET /youtube_web/get_general_search?search_query=Python tutorial&feature=hd&sort_by=view_count  ## 搜索今天上传的4K编程直播 GET /youtube_web/get_general_search?search_query=programming&upload_time=today&feature=4k&content_type=video  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_general_search_api_v1_youtube_web_get_general_search_get_with_http_info(search_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_query: 搜索关键字/Search keyword (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, CN等）/Country code
        :param object time_zone: 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone
        :param object upload_time: 上传时间过滤 | Upload time filter
        :param object duration: 视频时长过滤 | Duration filter
        :param object content_type: 内容类型过滤 | Content type filter
        :param object feature: 特征过滤 | Feature filter
        :param object sort_by: 排序方式 | Sort by
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_query', 'language_code', 'country_code', 'time_zone', 'upload_time', 'duration', 'content_type', 'feature', 'sort_by', 'continuation_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_general_search_api_v1_youtube_web_get_general_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_query' is set
        if self.api_client.client_side_validation and ('search_query' not in params or
                                                       params['search_query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_query` when calling `get_general_search_api_v1_youtube_web_get_general_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_query' in params:
            query_params.append(('search_query', params['search_query']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'time_zone' in params:
            query_params.append(('time_zone', params['time_zone']))  # noqa: E501
        if 'upload_time' in params:
            query_params.append(('upload_time', params['upload_time']))  # noqa: E501
        if 'duration' in params:
            query_params.append(('duration', params['duration']))  # noqa: E501
        if 'content_type' in params:
            query_params.append(('content_type', params['content_type']))  # noqa: E501
        if 'feature' in params:
            query_params.append(('feature', params['feature']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_general_search', 'GET',
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

    def get_relate_video_api_v1_youtube_web_get_relate_video_get(self, video_id, **kwargs):  # noqa: E501
        """获取推荐视频/Get related videos  # noqa: E501

        # [中文] ### 用途: - 根据视频ID获取推荐视频数据。 ### 参数: - video_id: 视频ID，从URL中获取，例如：https://www.youtube.com/watch?v=LuIL5JATZsc，这里的video_id就是LuIL5JATZsc。 - continuation_token: 用于继续获取推荐视频的令牌。默认为None。 ### 返回: - 推荐视频数据。  # [English] ### Purpose: - Get related videos by video ID. ### Parameters: - video_id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc. - continuation_token: Token to continue fetching related videos. Default is None. ### Returns: - Related videos.  # [示例/Example] video_id = \"LuIL5JATZsc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_relate_video_api_v1_youtube_web_get_relate_video_get(video_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object video_id: 视频ID/Video ID (required)
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_relate_video_api_v1_youtube_web_get_relate_video_get_with_http_info(video_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_relate_video_api_v1_youtube_web_get_relate_video_get_with_http_info(video_id, **kwargs)  # noqa: E501
            return data

    def get_relate_video_api_v1_youtube_web_get_relate_video_get_with_http_info(self, video_id, **kwargs):  # noqa: E501
        """获取推荐视频/Get related videos  # noqa: E501

        # [中文] ### 用途: - 根据视频ID获取推荐视频数据。 ### 参数: - video_id: 视频ID，从URL中获取，例如：https://www.youtube.com/watch?v=LuIL5JATZsc，这里的video_id就是LuIL5JATZsc。 - continuation_token: 用于继续获取推荐视频的令牌。默认为None。 ### 返回: - 推荐视频数据。  # [English] ### Purpose: - Get related videos by video ID. ### Parameters: - video_id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc. - continuation_token: Token to continue fetching related videos. Default is None. ### Returns: - Related videos.  # [示例/Example] video_id = \"LuIL5JATZsc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_relate_video_api_v1_youtube_web_get_relate_video_get_with_http_info(video_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object video_id: 视频ID/Video ID (required)
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'continuation_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_relate_video_api_v1_youtube_web_get_relate_video_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if self.api_client.client_side_validation and ('video_id' not in params or
                                                       params['video_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `video_id` when calling `get_relate_video_api_v1_youtube_web_get_relate_video_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'video_id' in params:
            query_params.append(('video_id', params['video_id']))  # noqa: E501
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_relate_video', 'GET',
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

    def get_shorts_search_api_v1_youtube_web_get_shorts_search_get(self, search_query, **kwargs):  # noqa: E501
        """YouTube Shorts短视频搜索/YouTube Shorts search  # noqa: E501

        # [中文] ### 用途: - YouTube Shorts短视频专门搜索，使用原生YouTube API接口  ### 特点: - 🎬 专门搜索YouTube Shorts短视频（<60秒） - 🔍 支持多种过滤条件和排序方式 - 📱 优化的移动端短视频内容 - ⚡ 智能过滤：首次请求可能返回混合内容（长视频+短视频），默认自动过滤长视频  ### 重要说明 - YouTube Shorts搜索机制: 根据YouTube的搜索逻辑，Shorts搜索有以下特性： 1. **首次请求**（无continuation_token）：可能返回混合内容（部分长视频 + 部分短视频） 2. **后续请求**（有continuation_token）：仅返回纯短视频内容 3. **解决方案**：    - 方案A：使用 `filter_mixed_content=true`（默认），自动过滤掉长视频    - 方案B：使用第一次返回的 continuation_token 进行第二次请求，获取纯Shorts内容    - 方案C：设置 `filter_mixed_content=false`，获取原始混合内容  ### 参数详解:  #### 📌 必选参数 (Required Parameters):  **search_query** (string) - **作用**: 搜索关键字，用于匹配Shorts视频的标题、描述等内容 - **格式**: 任意字符串 - **示例**: `\"Python编程\"`, `\"gaming\"`, `\"cooking tutorial\"` - **注意**: 支持中英文及其他语言，空格会被自动处理  #### ⚙️ 可选参数 - 基础设置 (Optional Parameters - Basic Settings):  **language_code** (string, 可选) - **作用**: 设置搜索结果的显示语言，影响返回内容的语言偏好 - **默认值**: `\"en-US\"` - **可用值**:   - `\"zh-CN\"` - 简体中文   - `\"zh-TW\"` - 繁体中文   - `\"en-US\"` - 英语（美国）   - `\"en-GB\"` - 英语（英国）   - `\"ja-JP\"` - 日语   - `\"ko-KR\"` - 韩语   - `\"es-ES\"` - 西班牙语   - `\"fr-FR\"` - 法语   - `\"de-DE\"` - 德语   - 其他符合IETF BCP 47标准的语言代码 - **示例**: `language_code=zh-CN` - **影响**: 会影响搜索算法的语言匹配和结果排序  **country_code** (string, 可选) - **作用**: 设置地区/国家代码，影响搜索结果的地域相关性和内容可用性 - **默认值**: `\"US\"` - **可用值**:   - `\"US\"` - 美国   - `\"CN\"` - 中国   - `\"JP\"` - 日本   - `\"KR\"` - 韩国   - `\"GB\"` - 英国   - `\"DE\"` - 德国   - `\"FR\"` - 法国   - `\"CA\"` - 加拿大   - 其他符合ISO 3166-1 alpha-2标准的国家代码 - **示例**: `country_code=JP` - **影响**: 某些Shorts可能因地区限制而不可见  **time_zone** (string, 可选) - **作用**: 设置时区，影响时间相关过滤器（如\"今天\"、\"本周\"）的计算 - **默认值**: `\"America/Los_Angeles\"` - **可用值**: 符合IANA时区数据库的时区标识符   - `\"America/Los_Angeles\"` - 美国太平洋时区   - `\"America/New_York\"` - 美国东部时区   - `\"Asia/Shanghai\"` - 中国时区   - `\"Asia/Tokyo\"` - 日本时区   - `\"Europe/London\"` - 英国时区   - `\"Europe/Paris\"` - 法国时区 - **示例**: `time_zone=Asia/Shanghai` - **影响**: 结合upload_time参数使用时，决定\"今天\"等时间段的具体范围  **filter_mixed_content** (boolean, 可选) - **作用**: 控制是否自动过滤掉响应中的长视频（非Shorts内容） - **默认值**: `true` - **可用值**:   - `true` - 自动过滤长视频，只返回Shorts（推荐）   - `false` - 返回原始内容，可能包含长视频 - **示例**: `filter_mixed_content=true` - **使用场景**:   - `true`: 当你只需要纯Shorts内容时使用（推荐首次请求使用）   - `false`: 当你需要分析YouTube原始返回的混合内容时使用（调试用） - **注意**: 只影响首次请求，使用continuation_token的请求本身就只返回Shorts  #### 🎯 可选参数 - Shorts过滤条件 (Optional Parameters - Shorts Filters):  **upload_time** (string, 可选) - **作用**: 按上传时间过滤Shorts，只返回指定时间段内上传的视频 - **默认值**: `null` (不过滤) - **可用值**:   - `\"hour\"` - 过去1小时内上传   - `\"today\"` - 今天上传（基于time_zone参数）   - `\"week\"` - 本周上传（最近7天）   - `\"month\"` - 本月上传（最近30天）   - `\"year\"` - 今年上传（最近365天） - **示例**: `upload_time=week` - **使用场景**: 寻找最新、热门的Shorts内容 - **注意**: 与time_zone参数配合使用，时间计算基于设定的时区  **sort_by** (string, 可选) - **作用**: 设置搜索结果的排序方式 - **默认值**: `null` (YouTube默认相关性排序) - **可用值**:   - `\"relevance\"` - 按相关性排序（YouTube默认算法）   - `\"upload_date\"` - 按上传日期排序（最新优先）   - `\"view_count\"` - 按观看次数排序（最多观看优先）   - `\"rating\"` - 按评分排序（最高评分优先） - **示例**: `sort_by=view_count` - **使用场景**:   - `relevance`: 寻找最相关的内容   - `upload_date`: 寻找最新发布的Shorts   - `view_count`: 寻找最受欢迎的Shorts   - `rating`: 寻找质量最高的Shorts - **优先级**: sort_by的优先级高于upload_time，两者同时使用时以sort_by为准  #### 📄 可选参数 - 翻页控制 (Optional Parameters - Pagination):  **continuation_token** (string, 可选) - **作用**: 用于获取下一页搜索结果的翻页令牌 - **默认值**: `null` (获取第一页) - **格式**: YouTube返回的加密字符串 - **示例**: `continuation_token=EqcBEgPkuKzor4YybhmgGk...` - **获取方式**: 从上一次请求的响应中提取（见\"翻页机制详解\"部分） - **使用场景**:   - 首次搜索：不传此参数，获取第一页结果   - 后续翻页：传入上次返回的token，获取下一页结果 - **注意**:   - Token有时效性，通常在数小时内有效   - 使用continuation_token时，必须保持search_query等其他参数一致   - 使用token的请求会自动返回纯Shorts内容（无需过滤）  ### 翻页机制详解: #### 如何获取 continuation_token： 从响应JSON中提取，路径通常为以下之一： ```python # 路径1：在 onResponseReceivedCommands 中 response[\"data\"][\"onResponseReceivedCommands\"][0][\"appendContinuationItemsAction\"][\"continuationItems\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"]  # 路径2：在 contents 中 response[\"data\"][\"contents\"][\"twoColumnSearchResultsRenderer\"][\"primaryContents\"][\"sectionListRenderer\"][\"contents\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"] ```  #### 使用流程： 1. **首次请求**: 不传 continuation_token    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python    ``` 2. **提取token**: 从响应中找到 continuation_token 3. **后续请求**: 传入 continuation_token 获取下一页    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python&continuation_token=xxx    ```  ### 响应数据结构: ```json {   \"code\": 200,   \"data\": {     \"contents\": {       \"twoColumnSearchResultsRenderer\": {         \"primaryContents\": {           \"sectionListRenderer\": {             \"contents\": [               {                 \"itemSectionRenderer\": {                   \"contents\": [                     {                       \"gridShelfViewModel\": {                         // Shorts视频列表                         \"items\": [...]                       }                     }                   ]                 }               },               {                 \"continuationItemRenderer\": {                   \"continuationEndpoint\": {                     \"continuationCommand\": {                       \"token\": \"xxx\"  // 下一页的token                     }                   }                 }               }             ]           }         }       }     }   } } ```  ### 返回: - 专门针对Shorts的搜索结果，包含视频列表和翻页token  # [English] ### Purpose: - YouTube Shorts specialized search using native YouTube API  ### Features: - 🎬 Specialized search for YouTube Shorts (<60 seconds) - 🔍 Support for multiple filter conditions and sorting options - 📱 Optimized for mobile short-form content - ⚡ Smart filtering: First request may return mixed content (long+short videos), automatically filters long videos by default  ### Important - YouTube Shorts Search Mechanism: According to YouTube's search logic, Shorts search has these characteristics: 1. **First request** (no continuation_token): May return mixed content (some long videos + some short videos) 2. **Subsequent requests** (with continuation_token): Returns only pure Shorts content 3. **Solutions**:    - Solution A: Use `filter_mixed_content=true` (default) to automatically filter long videos    - Solution B: Use continuation_token from first response for second request to get pure Shorts    - Solution C: Set `filter_mixed_content=false` to get original mixed content  ### Parameters: - **search_query**: Search keyword - **language_code**: Language code (zh-CN for Chinese, en-US for English) - **country_code**: Country code affecting regional relevance - **time_zone**: Time zone (e.g., America/Los_Angeles, Asia/Shanghai) - **filter_mixed_content**: Whether to filter long videos from mixed content (default true)  ### Shorts-specific Filters: #### Upload Time (upload_time): - `hour`: Shorts uploaded in the past hour - `today`: Shorts uploaded today - `week`: Shorts uploaded this week - `month`: Shorts uploaded this month - `year`: Shorts uploaded this year  #### Sort By (sort_by): - `relevance`: Relevance (default) - `upload_date`: Upload date - `view_count`: View count - `rating`: Rating  ### Pagination Mechanism Explained: #### How to get continuation_token: Extract from response JSON, typically at one of these paths: ```python # Path 1: In onResponseReceivedCommands response[\"onResponseReceivedCommands\"][0][\"appendContinuationItemsAction\"][\"continuationItems\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"]  # Path 2: In contents response[\"contents\"][\"twoColumnSearchResultsRenderer\"][\"primaryContents\"][\"sectionListRenderer\"][\"contents\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"] ```  #### Usage Flow: 1. **First request**: Don't pass continuation_token    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python    ``` 2. **Extract token**: Find continuation_token in response 3. **Next requests**: Pass continuation_token to get next page    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python&continuation_token=xxx    ```  ### Response Data Structure: ```json {   \"code\": 200,   \"data\": {     \"contents\": {       \"twoColumnSearchResultsRenderer\": {         \"primaryContents\": {           \"sectionListRenderer\": {             \"contents\": [               {                 \"itemSectionRenderer\": {                   \"contents\": [                     {                       \"gridShelfViewModel\": {                         // Shorts video list                         \"items\": [...]                       }                     }                   ]                 }               },               {                 \"continuationItemRenderer\": {                   \"continuationEndpoint\": {                     \"continuationCommand\": {                       \"token\": \"xxx\"  // Token for next page                     }                   }                 }               }             ]           }         }       }     }   } } ```  ### Returns: - Shorts-specific search results with video list and pagination token  # [示例/Examples] ## 基础Shorts搜索（自动过滤长视频） GET /youtube_web/get_shorts_search?search_query=Python编程  ## 获取原始混合内容（包含长视频） GET /youtube_web/get_shorts_search?search_query=Python编程&filter_mixed_content=false  ## 搜索本周上传的Python相关Shorts GET /youtube_web/get_shorts_search?search_query=python&upload_time=week  ## 搜索观看次数最多的技术Shorts GET /youtube_web/get_shorts_search?search_query=技术&sort_by=view_count  ## 翻页获取更多Shorts GET /youtube_web/get_shorts_search?search_query=编程&continuation_token=EqcBEgPkuKzor4YybhmgGk...  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shorts_search_api_v1_youtube_web_get_shorts_search_get(search_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_query: 搜索关键字/Search keyword (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, CN等）/Country code
        :param object time_zone: 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone
        :param object upload_time: 上传时间过滤 | Upload time filter for Shorts
        :param object sort_by: 排序方式 | Sort by for Shorts
        :param object continuation_token: 翻页令牌/Pagination token
        :param object filter_mixed_content: 是否过滤混合内容（长视频），默认True / Filter mixed content (long videos), default True
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_shorts_search_api_v1_youtube_web_get_shorts_search_get_with_http_info(search_query, **kwargs)  # noqa: E501
        else:
            (data) = self.get_shorts_search_api_v1_youtube_web_get_shorts_search_get_with_http_info(search_query, **kwargs)  # noqa: E501
            return data

    def get_shorts_search_api_v1_youtube_web_get_shorts_search_get_with_http_info(self, search_query, **kwargs):  # noqa: E501
        """YouTube Shorts短视频搜索/YouTube Shorts search  # noqa: E501

        # [中文] ### 用途: - YouTube Shorts短视频专门搜索，使用原生YouTube API接口  ### 特点: - 🎬 专门搜索YouTube Shorts短视频（<60秒） - 🔍 支持多种过滤条件和排序方式 - 📱 优化的移动端短视频内容 - ⚡ 智能过滤：首次请求可能返回混合内容（长视频+短视频），默认自动过滤长视频  ### 重要说明 - YouTube Shorts搜索机制: 根据YouTube的搜索逻辑，Shorts搜索有以下特性： 1. **首次请求**（无continuation_token）：可能返回混合内容（部分长视频 + 部分短视频） 2. **后续请求**（有continuation_token）：仅返回纯短视频内容 3. **解决方案**：    - 方案A：使用 `filter_mixed_content=true`（默认），自动过滤掉长视频    - 方案B：使用第一次返回的 continuation_token 进行第二次请求，获取纯Shorts内容    - 方案C：设置 `filter_mixed_content=false`，获取原始混合内容  ### 参数详解:  #### 📌 必选参数 (Required Parameters):  **search_query** (string) - **作用**: 搜索关键字，用于匹配Shorts视频的标题、描述等内容 - **格式**: 任意字符串 - **示例**: `\"Python编程\"`, `\"gaming\"`, `\"cooking tutorial\"` - **注意**: 支持中英文及其他语言，空格会被自动处理  #### ⚙️ 可选参数 - 基础设置 (Optional Parameters - Basic Settings):  **language_code** (string, 可选) - **作用**: 设置搜索结果的显示语言，影响返回内容的语言偏好 - **默认值**: `\"en-US\"` - **可用值**:   - `\"zh-CN\"` - 简体中文   - `\"zh-TW\"` - 繁体中文   - `\"en-US\"` - 英语（美国）   - `\"en-GB\"` - 英语（英国）   - `\"ja-JP\"` - 日语   - `\"ko-KR\"` - 韩语   - `\"es-ES\"` - 西班牙语   - `\"fr-FR\"` - 法语   - `\"de-DE\"` - 德语   - 其他符合IETF BCP 47标准的语言代码 - **示例**: `language_code=zh-CN` - **影响**: 会影响搜索算法的语言匹配和结果排序  **country_code** (string, 可选) - **作用**: 设置地区/国家代码，影响搜索结果的地域相关性和内容可用性 - **默认值**: `\"US\"` - **可用值**:   - `\"US\"` - 美国   - `\"CN\"` - 中国   - `\"JP\"` - 日本   - `\"KR\"` - 韩国   - `\"GB\"` - 英国   - `\"DE\"` - 德国   - `\"FR\"` - 法国   - `\"CA\"` - 加拿大   - 其他符合ISO 3166-1 alpha-2标准的国家代码 - **示例**: `country_code=JP` - **影响**: 某些Shorts可能因地区限制而不可见  **time_zone** (string, 可选) - **作用**: 设置时区，影响时间相关过滤器（如\"今天\"、\"本周\"）的计算 - **默认值**: `\"America/Los_Angeles\"` - **可用值**: 符合IANA时区数据库的时区标识符   - `\"America/Los_Angeles\"` - 美国太平洋时区   - `\"America/New_York\"` - 美国东部时区   - `\"Asia/Shanghai\"` - 中国时区   - `\"Asia/Tokyo\"` - 日本时区   - `\"Europe/London\"` - 英国时区   - `\"Europe/Paris\"` - 法国时区 - **示例**: `time_zone=Asia/Shanghai` - **影响**: 结合upload_time参数使用时，决定\"今天\"等时间段的具体范围  **filter_mixed_content** (boolean, 可选) - **作用**: 控制是否自动过滤掉响应中的长视频（非Shorts内容） - **默认值**: `true` - **可用值**:   - `true` - 自动过滤长视频，只返回Shorts（推荐）   - `false` - 返回原始内容，可能包含长视频 - **示例**: `filter_mixed_content=true` - **使用场景**:   - `true`: 当你只需要纯Shorts内容时使用（推荐首次请求使用）   - `false`: 当你需要分析YouTube原始返回的混合内容时使用（调试用） - **注意**: 只影响首次请求，使用continuation_token的请求本身就只返回Shorts  #### 🎯 可选参数 - Shorts过滤条件 (Optional Parameters - Shorts Filters):  **upload_time** (string, 可选) - **作用**: 按上传时间过滤Shorts，只返回指定时间段内上传的视频 - **默认值**: `null` (不过滤) - **可用值**:   - `\"hour\"` - 过去1小时内上传   - `\"today\"` - 今天上传（基于time_zone参数）   - `\"week\"` - 本周上传（最近7天）   - `\"month\"` - 本月上传（最近30天）   - `\"year\"` - 今年上传（最近365天） - **示例**: `upload_time=week` - **使用场景**: 寻找最新、热门的Shorts内容 - **注意**: 与time_zone参数配合使用，时间计算基于设定的时区  **sort_by** (string, 可选) - **作用**: 设置搜索结果的排序方式 - **默认值**: `null` (YouTube默认相关性排序) - **可用值**:   - `\"relevance\"` - 按相关性排序（YouTube默认算法）   - `\"upload_date\"` - 按上传日期排序（最新优先）   - `\"view_count\"` - 按观看次数排序（最多观看优先）   - `\"rating\"` - 按评分排序（最高评分优先） - **示例**: `sort_by=view_count` - **使用场景**:   - `relevance`: 寻找最相关的内容   - `upload_date`: 寻找最新发布的Shorts   - `view_count`: 寻找最受欢迎的Shorts   - `rating`: 寻找质量最高的Shorts - **优先级**: sort_by的优先级高于upload_time，两者同时使用时以sort_by为准  #### 📄 可选参数 - 翻页控制 (Optional Parameters - Pagination):  **continuation_token** (string, 可选) - **作用**: 用于获取下一页搜索结果的翻页令牌 - **默认值**: `null` (获取第一页) - **格式**: YouTube返回的加密字符串 - **示例**: `continuation_token=EqcBEgPkuKzor4YybhmgGk...` - **获取方式**: 从上一次请求的响应中提取（见\"翻页机制详解\"部分） - **使用场景**:   - 首次搜索：不传此参数，获取第一页结果   - 后续翻页：传入上次返回的token，获取下一页结果 - **注意**:   - Token有时效性，通常在数小时内有效   - 使用continuation_token时，必须保持search_query等其他参数一致   - 使用token的请求会自动返回纯Shorts内容（无需过滤）  ### 翻页机制详解: #### 如何获取 continuation_token： 从响应JSON中提取，路径通常为以下之一： ```python # 路径1：在 onResponseReceivedCommands 中 response[\"data\"][\"onResponseReceivedCommands\"][0][\"appendContinuationItemsAction\"][\"continuationItems\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"]  # 路径2：在 contents 中 response[\"data\"][\"contents\"][\"twoColumnSearchResultsRenderer\"][\"primaryContents\"][\"sectionListRenderer\"][\"contents\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"] ```  #### 使用流程： 1. **首次请求**: 不传 continuation_token    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python    ``` 2. **提取token**: 从响应中找到 continuation_token 3. **后续请求**: 传入 continuation_token 获取下一页    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python&continuation_token=xxx    ```  ### 响应数据结构: ```json {   \"code\": 200,   \"data\": {     \"contents\": {       \"twoColumnSearchResultsRenderer\": {         \"primaryContents\": {           \"sectionListRenderer\": {             \"contents\": [               {                 \"itemSectionRenderer\": {                   \"contents\": [                     {                       \"gridShelfViewModel\": {                         // Shorts视频列表                         \"items\": [...]                       }                     }                   ]                 }               },               {                 \"continuationItemRenderer\": {                   \"continuationEndpoint\": {                     \"continuationCommand\": {                       \"token\": \"xxx\"  // 下一页的token                     }                   }                 }               }             ]           }         }       }     }   } } ```  ### 返回: - 专门针对Shorts的搜索结果，包含视频列表和翻页token  # [English] ### Purpose: - YouTube Shorts specialized search using native YouTube API  ### Features: - 🎬 Specialized search for YouTube Shorts (<60 seconds) - 🔍 Support for multiple filter conditions and sorting options - 📱 Optimized for mobile short-form content - ⚡ Smart filtering: First request may return mixed content (long+short videos), automatically filters long videos by default  ### Important - YouTube Shorts Search Mechanism: According to YouTube's search logic, Shorts search has these characteristics: 1. **First request** (no continuation_token): May return mixed content (some long videos + some short videos) 2. **Subsequent requests** (with continuation_token): Returns only pure Shorts content 3. **Solutions**:    - Solution A: Use `filter_mixed_content=true` (default) to automatically filter long videos    - Solution B: Use continuation_token from first response for second request to get pure Shorts    - Solution C: Set `filter_mixed_content=false` to get original mixed content  ### Parameters: - **search_query**: Search keyword - **language_code**: Language code (zh-CN for Chinese, en-US for English) - **country_code**: Country code affecting regional relevance - **time_zone**: Time zone (e.g., America/Los_Angeles, Asia/Shanghai) - **filter_mixed_content**: Whether to filter long videos from mixed content (default true)  ### Shorts-specific Filters: #### Upload Time (upload_time): - `hour`: Shorts uploaded in the past hour - `today`: Shorts uploaded today - `week`: Shorts uploaded this week - `month`: Shorts uploaded this month - `year`: Shorts uploaded this year  #### Sort By (sort_by): - `relevance`: Relevance (default) - `upload_date`: Upload date - `view_count`: View count - `rating`: Rating  ### Pagination Mechanism Explained: #### How to get continuation_token: Extract from response JSON, typically at one of these paths: ```python # Path 1: In onResponseReceivedCommands response[\"onResponseReceivedCommands\"][0][\"appendContinuationItemsAction\"][\"continuationItems\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"]  # Path 2: In contents response[\"contents\"][\"twoColumnSearchResultsRenderer\"][\"primaryContents\"][\"sectionListRenderer\"][\"contents\"][-1][\"continuationItemRenderer\"][\"continuationEndpoint\"][\"continuationCommand\"][\"token\"] ```  #### Usage Flow: 1. **First request**: Don't pass continuation_token    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python    ``` 2. **Extract token**: Find continuation_token in response 3. **Next requests**: Pass continuation_token to get next page    ```    GET /api/v1/youtube_web/get_shorts_search?search_query=python&continuation_token=xxx    ```  ### Response Data Structure: ```json {   \"code\": 200,   \"data\": {     \"contents\": {       \"twoColumnSearchResultsRenderer\": {         \"primaryContents\": {           \"sectionListRenderer\": {             \"contents\": [               {                 \"itemSectionRenderer\": {                   \"contents\": [                     {                       \"gridShelfViewModel\": {                         // Shorts video list                         \"items\": [...]                       }                     }                   ]                 }               },               {                 \"continuationItemRenderer\": {                   \"continuationEndpoint\": {                     \"continuationCommand\": {                       \"token\": \"xxx\"  // Token for next page                     }                   }                 }               }             ]           }         }       }     }   } } ```  ### Returns: - Shorts-specific search results with video list and pagination token  # [示例/Examples] ## 基础Shorts搜索（自动过滤长视频） GET /youtube_web/get_shorts_search?search_query=Python编程  ## 获取原始混合内容（包含长视频） GET /youtube_web/get_shorts_search?search_query=Python编程&filter_mixed_content=false  ## 搜索本周上传的Python相关Shorts GET /youtube_web/get_shorts_search?search_query=python&upload_time=week  ## 搜索观看次数最多的技术Shorts GET /youtube_web/get_shorts_search?search_query=技术&sort_by=view_count  ## 翻页获取更多Shorts GET /youtube_web/get_shorts_search?search_query=编程&continuation_token=EqcBEgPkuKzor4YybhmgGk...  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shorts_search_api_v1_youtube_web_get_shorts_search_get_with_http_info(search_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_query: 搜索关键字/Search keyword (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, CN等）/Country code
        :param object time_zone: 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone
        :param object upload_time: 上传时间过滤 | Upload time filter for Shorts
        :param object sort_by: 排序方式 | Sort by for Shorts
        :param object continuation_token: 翻页令牌/Pagination token
        :param object filter_mixed_content: 是否过滤混合内容（长视频），默认True / Filter mixed content (long videos), default True
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_query', 'language_code', 'country_code', 'time_zone', 'upload_time', 'sort_by', 'continuation_token', 'filter_mixed_content']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shorts_search_api_v1_youtube_web_get_shorts_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_query' is set
        if self.api_client.client_side_validation and ('search_query' not in params or
                                                       params['search_query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_query` when calling `get_shorts_search_api_v1_youtube_web_get_shorts_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_query' in params:
            query_params.append(('search_query', params['search_query']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'time_zone' in params:
            query_params.append(('time_zone', params['time_zone']))  # noqa: E501
        if 'upload_time' in params:
            query_params.append(('upload_time', params['upload_time']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501
        if 'filter_mixed_content' in params:
            query_params.append(('filter_mixed_content', params['filter_mixed_content']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_shorts_search', 'GET',
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

    def get_trending_videos_api_v1_youtube_web_get_trending_videos_get(self, **kwargs):  # noqa: E501
        """获取趋势视频/Get trending videos  # noqa: E501

        # [中文] ### 用途: - 获取趋势视频。 ### 参数: - language_code: 语言代码，默认为en。 - country_code: 国家代码，默认为us。 - section: 类型，默认为Now，可选值为Music, Gaming, Movies。 ### 返回: - 趋势视频。  # [English] ### Purpose: - Get trending videos. ### Parameters: - language_code: Language code, default is en. - country_code: Country code, default is us. - section: Section, default is Now, optional values are Music, Gaming, Movies. ### Returns: - Trending videos.  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trending_videos_api_v1_youtube_web_get_trending_videos_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object language_code: 语言代码/Language code
        :param object country_code: 国家代码/Country code
        :param object section: 类型/Section
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_trending_videos_api_v1_youtube_web_get_trending_videos_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_trending_videos_api_v1_youtube_web_get_trending_videos_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_trending_videos_api_v1_youtube_web_get_trending_videos_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取趋势视频/Get trending videos  # noqa: E501

        # [中文] ### 用途: - 获取趋势视频。 ### 参数: - language_code: 语言代码，默认为en。 - country_code: 国家代码，默认为us。 - section: 类型，默认为Now，可选值为Music, Gaming, Movies。 ### 返回: - 趋势视频。  # [English] ### Purpose: - Get trending videos. ### Parameters: - language_code: Language code, default is en. - country_code: Country code, default is us. - section: Section, default is Now, optional values are Music, Gaming, Movies. ### Returns: - Trending videos.  # [示例/Example]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trending_videos_api_v1_youtube_web_get_trending_videos_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object language_code: 语言代码/Language code
        :param object country_code: 国家代码/Country code
        :param object section: 类型/Section
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['language_code', 'country_code', 'section']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trending_videos_api_v1_youtube_web_get_trending_videos_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'section' in params:
            query_params.append(('section', params['section']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_trending_videos', 'GET',
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

    def get_video_comment_replies_api_v1_youtube_web_get_video_comment_replies_get(self, continuation_token, **kwargs):  # noqa: E501
        """获取视频二级评论/Get video sub comments  # noqa: E501

        # [中文] ### 用途: - 获取视频二级评论  ### 参数详解:  #### 📌 必选参数: **continuation_token** (string) - **作用**: 回复的continuation token - **获取方式**: 从一级评论的响应数据中获取 `reply_continuation_token` 字段 - **示例**: `\"Eg0SC29hU05CejRxTVFZGAYygwEaUBIaVWd3WmhjUXVGUmJZTlhkUV85VjRBYUFCQWciAggAKhhVQ0pIQko3Ri1uQUlsTUdvbG0wSHU0dmcyC29hU05CejRxTVFZQAFICoIBAggBQi9jb21tZW50LXJlcGxpZXMtaXRlbS1VZ3daaGNRdUZSYllOWGRRXzlWNEFhQUJBZw%3D%3D\"`  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置回复显示的语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 使用流程: 1. 先调用 `/get_video_comments` 接口获取一级评论 2. 从一级评论的响应中找到 `reply_continuation_token` 字段 3. 使用该 token 调用本接口获取该评论的所有回复  ### 返回数据结构 (need_format=true): ```json {   \"comments\": [     {       \"comment_id\": \"UgwZhcQuFRbYNXdQ_9V4AaABAg.A2B3C4D5E6F7G8H9I0J1\",       \"content\": \"回复内容文本\",       \"published_time\": \"2天前\",       \"reply_level\": 1,       \"like_count\": \"5\",       \"like_count_a11y\": \"5 次赞\",       \"reply_count\": \"0\",       \"author\": {         \"channel_id\": \"UCxxxxxx\",         \"display_name\": \"@username\",         \"channel_url\": \"https://www.youtube.com/@username\",         \"avatar_url\": \"https://yt3.ggpht.com/...\",         \"is_verified\": false,         \"is_creator\": true,         \"is_artist\": false       }     }   ],   \"continuation_token\": \"下一页token（如果有更多回复）\" } ```  ### 字段说明: - `reply_level`: 回复层级（1表示二级评论/回复） - `is_creator`: 是否为视频创作者（如果是创作者回复会标记为true） - 其他字段与一级评论相同  # [English] ### Purpose: - Get video second-level comments  ### Parameters: - id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc. - continuation_token: Token to continue fetching comments. Default is None. ### Returns: - Video comments.  # [示例/Example] id = \"LuIL5JATZsc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_comment_replies_api_v1_youtube_web_get_video_comment_replies_get(continuation_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object continuation_token: 回复的continuation token（从一级评论的reply_continuation_token字段获取）/Reply continuation token from first-level comment (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, JP等）/Country code
        :param object need_format: 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_video_comment_replies_api_v1_youtube_web_get_video_comment_replies_get_with_http_info(continuation_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_video_comment_replies_api_v1_youtube_web_get_video_comment_replies_get_with_http_info(continuation_token, **kwargs)  # noqa: E501
            return data

    def get_video_comment_replies_api_v1_youtube_web_get_video_comment_replies_get_with_http_info(self, continuation_token, **kwargs):  # noqa: E501
        """获取视频二级评论/Get video sub comments  # noqa: E501

        # [中文] ### 用途: - 获取视频二级评论  ### 参数详解:  #### 📌 必选参数: **continuation_token** (string) - **作用**: 回复的continuation token - **获取方式**: 从一级评论的响应数据中获取 `reply_continuation_token` 字段 - **示例**: `\"Eg0SC29hU05CejRxTVFZGAYygwEaUBIaVWd3WmhjUXVGUmJZTlhkUV85VjRBYUFCQWciAggAKhhVQ0pIQko3Ri1uQUlsTUdvbG0wSHU0dmcyC29hU05CejRxTVFZQAFICoIBAggBQi9jb21tZW50LXJlcGxpZXMtaXRlbS1VZ3daaGNRdUZSYllOWGRRXzlWNEFhQUJBZw%3D%3D\"`  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置回复显示的语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 使用流程: 1. 先调用 `/get_video_comments` 接口获取一级评论 2. 从一级评论的响应中找到 `reply_continuation_token` 字段 3. 使用该 token 调用本接口获取该评论的所有回复  ### 返回数据结构 (need_format=true): ```json {   \"comments\": [     {       \"comment_id\": \"UgwZhcQuFRbYNXdQ_9V4AaABAg.A2B3C4D5E6F7G8H9I0J1\",       \"content\": \"回复内容文本\",       \"published_time\": \"2天前\",       \"reply_level\": 1,       \"like_count\": \"5\",       \"like_count_a11y\": \"5 次赞\",       \"reply_count\": \"0\",       \"author\": {         \"channel_id\": \"UCxxxxxx\",         \"display_name\": \"@username\",         \"channel_url\": \"https://www.youtube.com/@username\",         \"avatar_url\": \"https://yt3.ggpht.com/...\",         \"is_verified\": false,         \"is_creator\": true,         \"is_artist\": false       }     }   ],   \"continuation_token\": \"下一页token（如果有更多回复）\" } ```  ### 字段说明: - `reply_level`: 回复层级（1表示二级评论/回复） - `is_creator`: 是否为视频创作者（如果是创作者回复会标记为true） - 其他字段与一级评论相同  # [English] ### Purpose: - Get video second-level comments  ### Parameters: - id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc. - continuation_token: Token to continue fetching comments. Default is None. ### Returns: - Video comments.  # [示例/Example] id = \"LuIL5JATZsc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_comment_replies_api_v1_youtube_web_get_video_comment_replies_get_with_http_info(continuation_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object continuation_token: 回复的continuation token（从一级评论的reply_continuation_token字段获取）/Reply continuation token from first-level comment (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, JP等）/Country code
        :param object need_format: 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['continuation_token', 'language_code', 'country_code', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_comment_replies_api_v1_youtube_web_get_video_comment_replies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'continuation_token' is set
        if self.api_client.client_side_validation and ('continuation_token' not in params or
                                                       params['continuation_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `continuation_token` when calling `get_video_comment_replies_api_v1_youtube_web_get_video_comment_replies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_video_comment_replies', 'GET',
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

    def get_video_comments_api_v1_youtube_web_get_video_comments_get(self, video_id, **kwargs):  # noqa: E501
        """获取视频评论/Get video comments  # noqa: E501

        # [中文] ### 用途: - 获取YouTube视频的一级评论  ### 参数详解:  #### 📌 必选参数: **video_id** (string) - **作用**: 视频ID - **格式**: YouTube视频ID字符串 - **示例**: `\"oaSNBz4qMQY\"` - **获取方式**: 从URL `https://www.youtube.com/watch?v=oaSNBz4qMQY` 中提取  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置评论显示的语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **sort_by** (string, 可选) - **作用**: 评论排序方式 - **默认值**: `\"top\"` - **可用值**:   - `\"top\"` - 热门评论（按点赞数排序）   - `\"newest\"` - 最新评论（按时间排序）  **continuation_token** (string, 可选) - **作用**: 翻页令牌，用于获取下一页评论 - **默认值**: `null` - **获取方式**: 从上一次请求的响应中提取  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 返回数据结构 (need_format=true): ```json {   \"comments\": [     {       \"comment_id\": \"UgzRDoUJAvDNn5_8i8p4AaABAg\",       \"content\": \"评论内容文本\",       \"published_time\": \"1天前\",       \"reply_level\": 0,       \"like_count\": \"2\",       \"like_count_a11y\": \"2 次赞\",       \"reply_count\": \"0\",       \"reply_count_a11y\": \"0 条回复\",       \"reply_count_text\": \"1 条回复\",       \"reply_continuation_token\": \"...\",       \"author\": {         \"channel_id\": \"UCzRzHrLFuH0lHZYnrI84I8Q\",         \"display_name\": \"@username\",         \"channel_url\": \"https://www.youtube.com/@username\",         \"avatar_url\": \"https://yt3.ggpht.com/...\",         \"avatar_thumbnails\": [           {\"url\": \"...\", \"width\": 88, \"height\": 88}         ],         \"is_verified\": false,         \"is_creator\": false,         \"is_artist\": false       },       \"creator_thumbnail_url\": \"https://yt3.ggpht.com/...\"     }   ],   \"continuation_token\": \"下一页token\" } ```  ### 字段说明: - `comment_id`: 评论唯一ID - `content`: 评论文本内容 - `published_time`: 发布时间（相对时间，如\"1天前\"） - `reply_level`: 回复层级（0表示一级评论） - `like_count`: 点赞数 - `reply_count`: 回复数 - `reply_count_text`: 回复数文本（如\"1 条回复\"） - `reply_continuation_token`: 获取该评论回复的token - `author`: 评论作者信息   - `channel_id`: 作者频道ID   - `display_name`: 显示名称   - `channel_url`: 频道URL   - `avatar_url`: 头像URL   - `is_verified`: 是否已认证   - `is_creator`: 是否为视频创作者   - `is_artist`: 是否为音乐人 - `creator_thumbnail_url`: 视频创作者头像URL  # [English] ### Purpose: - Get YouTube video first-level comments  ### Parameters:  #### 📌 Required: **video_id** (string) - **Purpose**: Video ID - **Format**: YouTube video ID string - **Example**: `\"oaSNBz4qMQY\"` - **How to get**: Extract from URL `https://www.youtube.com/watch?v=oaSNBz4qMQY`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference for comments - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  **country_code** (string, optional) - **Purpose**: Set region code - **Default**: `\"US\"` - **Values**: `\"US\"`, `\"JP\"`, `\"GB\"`, etc.  **sort_by** (string, optional) - **Purpose**: Comment sorting method - **Default**: `\"top\"` - **Values**:   - `\"top\"` - Top comments (sorted by likes)   - `\"newest\"` - Newest comments (sorted by time)  **continuation_token** (string, optional) - **Purpose**: Pagination token for next page - **Default**: `null` - **How to get**: Extract from previous response  **need_format** (boolean, optional) - **Purpose**: Whether to return cleaned simplified data - **Default**: `false` - **Values**:   - `false` - Return raw complete data   - `true` - Return cleaned simplified data (recommended)  ### Response Structure (need_format=true): ```json {   \"comments\": [     {       \"comment_id\": \"UgzRDoUJAvDNn5_8i8p4AaABAg\",       \"content\": \"Comment text content\",       \"published_time\": \"1 day ago\",       \"reply_level\": 0,       \"like_count\": \"2\",       \"like_count_a11y\": \"2 likes\",       \"reply_count\": \"0\",       \"reply_count_a11y\": \"0 replies\",       \"reply_count_text\": \"1 reply\",       \"reply_continuation_token\": \"...\",       \"author\": {         \"channel_id\": \"UCzRzHrLFuH0lHZYnrI84I8Q\",         \"display_name\": \"@username\",         \"channel_url\": \"https://www.youtube.com/@username\",         \"avatar_url\": \"https://yt3.ggpht.com/...\",         \"avatar_thumbnails\": [           {\"url\": \"...\", \"width\": 88, \"height\": 88}         ],         \"is_verified\": false,         \"is_creator\": false,         \"is_artist\": false       },       \"creator_thumbnail_url\": \"https://yt3.ggpht.com/...\"     }   ],   \"continuation_token\": \"next page token\" } ```  ### Field Descriptions: - `comment_id`: Unique comment ID - `content`: Comment text content - `published_time`: Published time (relative, e.g., \"1 day ago\") - `reply_level`: Reply level (0 for first-level comments) - `like_count`: Number of likes - `reply_count`: Number of replies - `reply_count_text`: Reply count text (e.g., \"1 reply\") - `reply_continuation_token`: Token to get replies for this comment - `author`: Comment author info   - `channel_id`: Author's channel ID   - `display_name`: Display name   - `channel_url`: Channel URL   - `avatar_url`: Avatar URL   - `is_verified`: Whether verified   - `is_creator`: Whether video creator   - `is_artist`: Whether artist - `creator_thumbnail_url`: Video creator's avatar URL  # [示例/Examples] ## 获取热门评论 GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&sort_by=top  ## 获取最新评论 GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&sort_by=newest  ## 获取清洗后的评论数据（推荐） GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&need_format=true  ## 翻页获取更多评论 GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&continuation_token=xxx&need_format=true  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_comments_api_v1_youtube_web_get_video_comments_get(video_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object video_id: 视频ID/Video ID (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, JP等）/Country code
        :param object sort_by: 排序方式 | Sort by
        :param object continuation_token: 翻页令牌/Pagination token
        :param object need_format: 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_video_comments_api_v1_youtube_web_get_video_comments_get_with_http_info(video_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_video_comments_api_v1_youtube_web_get_video_comments_get_with_http_info(video_id, **kwargs)  # noqa: E501
            return data

    def get_video_comments_api_v1_youtube_web_get_video_comments_get_with_http_info(self, video_id, **kwargs):  # noqa: E501
        """获取视频评论/Get video comments  # noqa: E501

        # [中文] ### 用途: - 获取YouTube视频的一级评论  ### 参数详解:  #### 📌 必选参数: **video_id** (string) - **作用**: 视频ID - **格式**: YouTube视频ID字符串 - **示例**: `\"oaSNBz4qMQY\"` - **获取方式**: 从URL `https://www.youtube.com/watch?v=oaSNBz4qMQY` 中提取  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置评论显示的语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  **country_code** (string, 可选) - **作用**: 设置地区代码 - **默认值**: `\"US\"` - **可用值**: `\"US\"`, `\"JP\"`, `\"GB\"` 等  **sort_by** (string, 可选) - **作用**: 评论排序方式 - **默认值**: `\"top\"` - **可用值**:   - `\"top\"` - 热门评论（按点赞数排序）   - `\"newest\"` - 最新评论（按时间排序）  **continuation_token** (string, 可选) - **作用**: 翻页令牌，用于获取下一页评论 - **默认值**: `null` - **获取方式**: 从上一次请求的响应中提取  **need_format** (boolean, 可选) - **作用**: 是否返回清洗后的精简数据 - **默认值**: `false` - **可用值**:   - `false` - 返回原始完整数据   - `true` - 返回清洗后的精简数据（推荐）  ### 返回数据结构 (need_format=true): ```json {   \"comments\": [     {       \"comment_id\": \"UgzRDoUJAvDNn5_8i8p4AaABAg\",       \"content\": \"评论内容文本\",       \"published_time\": \"1天前\",       \"reply_level\": 0,       \"like_count\": \"2\",       \"like_count_a11y\": \"2 次赞\",       \"reply_count\": \"0\",       \"reply_count_a11y\": \"0 条回复\",       \"reply_count_text\": \"1 条回复\",       \"reply_continuation_token\": \"...\",       \"author\": {         \"channel_id\": \"UCzRzHrLFuH0lHZYnrI84I8Q\",         \"display_name\": \"@username\",         \"channel_url\": \"https://www.youtube.com/@username\",         \"avatar_url\": \"https://yt3.ggpht.com/...\",         \"avatar_thumbnails\": [           {\"url\": \"...\", \"width\": 88, \"height\": 88}         ],         \"is_verified\": false,         \"is_creator\": false,         \"is_artist\": false       },       \"creator_thumbnail_url\": \"https://yt3.ggpht.com/...\"     }   ],   \"continuation_token\": \"下一页token\" } ```  ### 字段说明: - `comment_id`: 评论唯一ID - `content`: 评论文本内容 - `published_time`: 发布时间（相对时间，如\"1天前\"） - `reply_level`: 回复层级（0表示一级评论） - `like_count`: 点赞数 - `reply_count`: 回复数 - `reply_count_text`: 回复数文本（如\"1 条回复\"） - `reply_continuation_token`: 获取该评论回复的token - `author`: 评论作者信息   - `channel_id`: 作者频道ID   - `display_name`: 显示名称   - `channel_url`: 频道URL   - `avatar_url`: 头像URL   - `is_verified`: 是否已认证   - `is_creator`: 是否为视频创作者   - `is_artist`: 是否为音乐人 - `creator_thumbnail_url`: 视频创作者头像URL  # [English] ### Purpose: - Get YouTube video first-level comments  ### Parameters:  #### 📌 Required: **video_id** (string) - **Purpose**: Video ID - **Format**: YouTube video ID string - **Example**: `\"oaSNBz4qMQY\"` - **How to get**: Extract from URL `https://www.youtube.com/watch?v=oaSNBz4qMQY`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference for comments - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  **country_code** (string, optional) - **Purpose**: Set region code - **Default**: `\"US\"` - **Values**: `\"US\"`, `\"JP\"`, `\"GB\"`, etc.  **sort_by** (string, optional) - **Purpose**: Comment sorting method - **Default**: `\"top\"` - **Values**:   - `\"top\"` - Top comments (sorted by likes)   - `\"newest\"` - Newest comments (sorted by time)  **continuation_token** (string, optional) - **Purpose**: Pagination token for next page - **Default**: `null` - **How to get**: Extract from previous response  **need_format** (boolean, optional) - **Purpose**: Whether to return cleaned simplified data - **Default**: `false` - **Values**:   - `false` - Return raw complete data   - `true` - Return cleaned simplified data (recommended)  ### Response Structure (need_format=true): ```json {   \"comments\": [     {       \"comment_id\": \"UgzRDoUJAvDNn5_8i8p4AaABAg\",       \"content\": \"Comment text content\",       \"published_time\": \"1 day ago\",       \"reply_level\": 0,       \"like_count\": \"2\",       \"like_count_a11y\": \"2 likes\",       \"reply_count\": \"0\",       \"reply_count_a11y\": \"0 replies\",       \"reply_count_text\": \"1 reply\",       \"reply_continuation_token\": \"...\",       \"author\": {         \"channel_id\": \"UCzRzHrLFuH0lHZYnrI84I8Q\",         \"display_name\": \"@username\",         \"channel_url\": \"https://www.youtube.com/@username\",         \"avatar_url\": \"https://yt3.ggpht.com/...\",         \"avatar_thumbnails\": [           {\"url\": \"...\", \"width\": 88, \"height\": 88}         ],         \"is_verified\": false,         \"is_creator\": false,         \"is_artist\": false       },       \"creator_thumbnail_url\": \"https://yt3.ggpht.com/...\"     }   ],   \"continuation_token\": \"next page token\" } ```  ### Field Descriptions: - `comment_id`: Unique comment ID - `content`: Comment text content - `published_time`: Published time (relative, e.g., \"1 day ago\") - `reply_level`: Reply level (0 for first-level comments) - `like_count`: Number of likes - `reply_count`: Number of replies - `reply_count_text`: Reply count text (e.g., \"1 reply\") - `reply_continuation_token`: Token to get replies for this comment - `author`: Comment author info   - `channel_id`: Author's channel ID   - `display_name`: Display name   - `channel_url`: Channel URL   - `avatar_url`: Avatar URL   - `is_verified`: Whether verified   - `is_creator`: Whether video creator   - `is_artist`: Whether artist - `creator_thumbnail_url`: Video creator's avatar URL  # [示例/Examples] ## 获取热门评论 GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&sort_by=top  ## 获取最新评论 GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&sort_by=newest  ## 获取清洗后的评论数据（推荐） GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&need_format=true  ## 翻页获取更多评论 GET /youtube_web/get_video_comments?video_id=oaSNBz4qMQY&continuation_token=xxx&need_format=true  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_comments_api_v1_youtube_web_get_video_comments_get_with_http_info(video_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object video_id: 视频ID/Video ID (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :param object country_code: 国家代码（如US, JP等）/Country code
        :param object sort_by: 排序方式 | Sort by
        :param object continuation_token: 翻页令牌/Pagination token
        :param object need_format: 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'language_code', 'country_code', 'sort_by', 'continuation_token', 'need_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_comments_api_v1_youtube_web_get_video_comments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if self.api_client.client_side_validation and ('video_id' not in params or
                                                       params['video_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `video_id` when calling `get_video_comments_api_v1_youtube_web_get_video_comments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'video_id' in params:
            query_params.append(('video_id', params['video_id']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501
        if 'need_format' in params:
            query_params.append(('need_format', params['need_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_video_comments', 'GET',
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

    def get_video_info_api_v1_youtube_web_get_video_info_get(self, video_id, **kwargs):  # noqa: E501
        """获取视频信息 V1/Get video information V1  # noqa: E501

        # [中文] ### 用途: - 获取视频元数据及下载信息 - 此接口收费: 0.002$/次 - 如果需要节省成本，可以使用V2版本，V2版本是0.001$/次，但不保证稳定性。 ### 详细参数: - url_access:     - normal: 包含音视频直链     - blocked: 不包含直链 - videos/audios:     - auto: 根据url_access自动选择（normal→true，blocked→false）     - true: 返回简化格式信息     - raw: 返回原始格式信息     - false: 不包含该类型数据 ### 返回: - 视频元数据 + 请求参数对应的资源信息  # [English] ### Purpose: - Get video metadata and download information - This endpoint is charged: 0.002$/request - To save cost, you can use V2 version, which is 0.001$/request, but stability is not guaranteed. ### Parameters Detail: - url_access:     - normal: Include direct URLs     - blocked: Exclude direct URLs - videos/audios:     - auto: Auto-select based on url_access (normal→true，blocked→false)     - true: Simplified format     - raw: Original format     - false: Exclude this type ### Returns: - Video metadata + requested resource information  # [示例/Example] video_id = \"LuIL5JATZsc\" url_access = \"blocked\" lang = \"zh-CN\"  video_id = \"LuIL5JATZsc\" url_access = \"normal\" lang = \"en-US\" videos = \"auto\" audios = \"auto\" subtitles = True  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_info_api_v1_youtube_web_get_video_info_get(video_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object video_id: 视频ID/Video ID (required)
        :param object url_access: URL访问模式：normal（包含音视频URL）| blocked（不包含音视频URL） / URL access mode
        :param object lang: 语言代码（IETF标签），默认en-US / Language code
        :param object videos: 视频格式：auto（自动）| true（简化格式）| raw（原始格式）| false（不获取） / Video format selection
        :param object audios: 音频格式：auto（自动）| true（简化格式）| raw（原始格式）| false（不获取） / Audio format selection
        :param object subtitles: 是否获取字幕 / Include subtitles
        :param object related: 是否获取相关视频 / Include related content
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_video_info_api_v1_youtube_web_get_video_info_get_with_http_info(video_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_video_info_api_v1_youtube_web_get_video_info_get_with_http_info(video_id, **kwargs)  # noqa: E501
            return data

    def get_video_info_api_v1_youtube_web_get_video_info_get_with_http_info(self, video_id, **kwargs):  # noqa: E501
        """获取视频信息 V1/Get video information V1  # noqa: E501

        # [中文] ### 用途: - 获取视频元数据及下载信息 - 此接口收费: 0.002$/次 - 如果需要节省成本，可以使用V2版本，V2版本是0.001$/次，但不保证稳定性。 ### 详细参数: - url_access:     - normal: 包含音视频直链     - blocked: 不包含直链 - videos/audios:     - auto: 根据url_access自动选择（normal→true，blocked→false）     - true: 返回简化格式信息     - raw: 返回原始格式信息     - false: 不包含该类型数据 ### 返回: - 视频元数据 + 请求参数对应的资源信息  # [English] ### Purpose: - Get video metadata and download information - This endpoint is charged: 0.002$/request - To save cost, you can use V2 version, which is 0.001$/request, but stability is not guaranteed. ### Parameters Detail: - url_access:     - normal: Include direct URLs     - blocked: Exclude direct URLs - videos/audios:     - auto: Auto-select based on url_access (normal→true，blocked→false)     - true: Simplified format     - raw: Original format     - false: Exclude this type ### Returns: - Video metadata + requested resource information  # [示例/Example] video_id = \"LuIL5JATZsc\" url_access = \"blocked\" lang = \"zh-CN\"  video_id = \"LuIL5JATZsc\" url_access = \"normal\" lang = \"en-US\" videos = \"auto\" audios = \"auto\" subtitles = True  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_info_api_v1_youtube_web_get_video_info_get_with_http_info(video_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object video_id: 视频ID/Video ID (required)
        :param object url_access: URL访问模式：normal（包含音视频URL）| blocked（不包含音视频URL） / URL access mode
        :param object lang: 语言代码（IETF标签），默认en-US / Language code
        :param object videos: 视频格式：auto（自动）| true（简化格式）| raw（原始格式）| false（不获取） / Video format selection
        :param object audios: 音频格式：auto（自动）| true（简化格式）| raw（原始格式）| false（不获取） / Audio format selection
        :param object subtitles: 是否获取字幕 / Include subtitles
        :param object related: 是否获取相关视频 / Include related content
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'url_access', 'lang', 'videos', 'audios', 'subtitles', 'related']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_info_api_v1_youtube_web_get_video_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if self.api_client.client_side_validation and ('video_id' not in params or
                                                       params['video_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `video_id` when calling `get_video_info_api_v1_youtube_web_get_video_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'video_id' in params:
            query_params.append(('video_id', params['video_id']))  # noqa: E501
        if 'url_access' in params:
            query_params.append(('url_access', params['url_access']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'videos' in params:
            query_params.append(('videos', params['videos']))  # noqa: E501
        if 'audios' in params:
            query_params.append(('audios', params['audios']))  # noqa: E501
        if 'subtitles' in params:
            query_params.append(('subtitles', params['subtitles']))  # noqa: E501
        if 'related' in params:
            query_params.append(('related', params['related']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_video_info', 'GET',
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

    def get_video_info_v2_api_v1_youtube_web_get_video_info_v2_get(self, video_id, **kwargs):  # noqa: E501
        """获取视频信息 V2/Get video information V2  # noqa: E501

        # [中文] ### 用途: - 获取视频元数据及下载信息 - 此接口收费: 0.001$/次 ### 参数: - video_id: 视频ID，从URL中获取，例如：https://www.youtube.com/watch?v=LuIL5JATZsc，这里的video_id就是LuIL5JATZsc。 ### 返回: - 视频元数据 + 请求参数对应的资源信息  # [English] ### Purpose: - Get video metadata and download information - This endpoint is charged: 0.001$/request ### Parameters Detail: - video_id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc. ### Returns: - Video metadata + requested resource information  # [示例/Example] video_id = \"LuIL5JATZsc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_info_v2_api_v1_youtube_web_get_video_info_v2_get(video_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object video_id: 视频ID/Video ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_video_info_v2_api_v1_youtube_web_get_video_info_v2_get_with_http_info(video_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_video_info_v2_api_v1_youtube_web_get_video_info_v2_get_with_http_info(video_id, **kwargs)  # noqa: E501
            return data

    def get_video_info_v2_api_v1_youtube_web_get_video_info_v2_get_with_http_info(self, video_id, **kwargs):  # noqa: E501
        """获取视频信息 V2/Get video information V2  # noqa: E501

        # [中文] ### 用途: - 获取视频元数据及下载信息 - 此接口收费: 0.001$/次 ### 参数: - video_id: 视频ID，从URL中获取，例如：https://www.youtube.com/watch?v=LuIL5JATZsc，这里的video_id就是LuIL5JATZsc。 ### 返回: - 视频元数据 + 请求参数对应的资源信息  # [English] ### Purpose: - Get video metadata and download information - This endpoint is charged: 0.001$/request ### Parameters Detail: - video_id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the id is LuIL5JATZsc. ### Returns: - Video metadata + requested resource information  # [示例/Example] video_id = \"LuIL5JATZsc\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_info_v2_api_v1_youtube_web_get_video_info_v2_get_with_http_info(video_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object video_id: 视频ID/Video ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_info_v2_api_v1_youtube_web_get_video_info_v2_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if self.api_client.client_side_validation and ('video_id' not in params or
                                                       params['video_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `video_id` when calling `get_video_info_v2_api_v1_youtube_web_get_video_info_v2_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'video_id' in params:
            query_params.append(('video_id', params['video_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_video_info_v2', 'GET',
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

    def get_video_info_v3_api_v1_youtube_web_get_video_info_v3_get(self, video_id, **kwargs):  # noqa: E501
        """获取视频详情 V3/Get video information V3  # noqa: E501

        # [中文] ### 用途: - 获取YouTube视频详情信息 - 返回原始完整数据（包含 playerResponse 和 initialData）  ### 参数详解:  #### 📌 必选参数: **video_id** (string) - **作用**: 视频ID - **获取方式**: 从视频URL中提取，例如 `https://www.youtube.com/watch?v=oaSNBz4qMQY`，video_id 就是 `oaSNBz4qMQY` - **示例**: `\"oaSNBz4qMQY\"`  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  ### 返回数据结构: ```json {   \"playerResponse\": {     \"videoDetails\": {},     \"streamingData\": {       \"formats\": [],       \"adaptiveFormats\": []     },     \"microformat\": {},     ...   },   \"initialData\": {     \"contents\": {       \"twoColumnWatchNextResults\": {         \"results\": {           \"results\": {             \"contents\": [               {                 \"videoPrimaryInfoRenderer\": {...},                 \"videoSecondaryInfoRenderer\": {...}               }             ]           }         }       }     },     ...   } } ```  ### 主要字段说明: - `playerResponse`: YouTube 播放器响应数据   - `videoDetails`: 视频基本信息（可能为空，取决于YouTube的返回）   - `streamingData`: 视频流数据（包含 formats 和 adaptiveFormats，包含 googlevideo.com 的URL）   - `microformat`: 元数据信息 - `initialData`: YouTube 页面初始化数据   - `videoPrimaryInfoRenderer`: 主要信息（标题、观看次数、点赞数等）   - `videoSecondaryInfoRenderer`: 次要信息（频道信息、描述等）  # [English] ### Purpose: - Get YouTube video details - Returns raw complete data (includes playerResponse and initialData)  ### Parameters:  #### 📌 Required: **video_id** (string) - **Purpose**: Video ID - **How to get**: Extract from video URL, e.g., `https://www.youtube.com/watch?v=oaSNBz4qMQY`, video_id is `oaSNBz4qMQY` - **Example**: `\"oaSNBz4qMQY\"`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  ### Response Structure: ```json {   \"playerResponse\": {     \"videoDetails\": {},     \"streamingData\": {       \"formats\": [],       \"adaptiveFormats\": []     },     \"microformat\": {},     ...   },   \"initialData\": {     \"contents\": {       \"twoColumnWatchNextResults\": {         \"results\": {           \"results\": {             \"contents\": [               {                 \"videoPrimaryInfoRenderer\": {...},                 \"videoSecondaryInfoRenderer\": {...}               }             ]           }         }       }     },     ...   } } ```  ### Key Fields: - `playerResponse`: YouTube player response data   - `videoDetails`: Basic video info (may be empty depending on YouTube's response)   - `streamingData`: Video stream data (includes formats and adaptiveFormats with googlevideo.com URLs)   - `microformat`: Metadata information - `initialData`: YouTube page initialization data   - `videoPrimaryInfoRenderer`: Primary info (title, view count, like count, etc.)   - `videoSecondaryInfoRenderer`: Secondary info (channel info, description, etc.)  # [示例/Examples] ## 获取视频详情数据 / Get video details GET /youtube_web/get_video_info_v3?video_id=oaSNBz4qMQY  ## 指定语言 / Specify language GET /youtube_web/get_video_info_v3?video_id=oaSNBz4qMQY&language_code=en-US  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_info_v3_api_v1_youtube_web_get_video_info_v3_get(video_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object video_id: 视频ID/Video ID (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_video_info_v3_api_v1_youtube_web_get_video_info_v3_get_with_http_info(video_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_video_info_v3_api_v1_youtube_web_get_video_info_v3_get_with_http_info(video_id, **kwargs)  # noqa: E501
            return data

    def get_video_info_v3_api_v1_youtube_web_get_video_info_v3_get_with_http_info(self, video_id, **kwargs):  # noqa: E501
        """获取视频详情 V3/Get video information V3  # noqa: E501

        # [中文] ### 用途: - 获取YouTube视频详情信息 - 返回原始完整数据（包含 playerResponse 和 initialData）  ### 参数详解:  #### 📌 必选参数: **video_id** (string) - **作用**: 视频ID - **获取方式**: 从视频URL中提取，例如 `https://www.youtube.com/watch?v=oaSNBz4qMQY`，video_id 就是 `oaSNBz4qMQY` - **示例**: `\"oaSNBz4qMQY\"`  #### ⚙️ 可选参数: **language_code** (string, 可选) - **作用**: 设置语言偏好 - **默认值**: `\"zh-CN\"` - **可用值**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"` 等  ### 返回数据结构: ```json {   \"playerResponse\": {     \"videoDetails\": {},     \"streamingData\": {       \"formats\": [],       \"adaptiveFormats\": []     },     \"microformat\": {},     ...   },   \"initialData\": {     \"contents\": {       \"twoColumnWatchNextResults\": {         \"results\": {           \"results\": {             \"contents\": [               {                 \"videoPrimaryInfoRenderer\": {...},                 \"videoSecondaryInfoRenderer\": {...}               }             ]           }         }       }     },     ...   } } ```  ### 主要字段说明: - `playerResponse`: YouTube 播放器响应数据   - `videoDetails`: 视频基本信息（可能为空，取决于YouTube的返回）   - `streamingData`: 视频流数据（包含 formats 和 adaptiveFormats，包含 googlevideo.com 的URL）   - `microformat`: 元数据信息 - `initialData`: YouTube 页面初始化数据   - `videoPrimaryInfoRenderer`: 主要信息（标题、观看次数、点赞数等）   - `videoSecondaryInfoRenderer`: 次要信息（频道信息、描述等）  # [English] ### Purpose: - Get YouTube video details - Returns raw complete data (includes playerResponse and initialData)  ### Parameters:  #### 📌 Required: **video_id** (string) - **Purpose**: Video ID - **How to get**: Extract from video URL, e.g., `https://www.youtube.com/watch?v=oaSNBz4qMQY`, video_id is `oaSNBz4qMQY` - **Example**: `\"oaSNBz4qMQY\"`  #### ⚙️ Optional: **language_code** (string, optional) - **Purpose**: Set language preference - **Default**: `\"zh-CN\"` - **Values**: `\"zh-CN\"`, `\"en-US\"`, `\"ja-JP\"`, `\"ko-KR\"`, etc.  ### Response Structure: ```json {   \"playerResponse\": {     \"videoDetails\": {},     \"streamingData\": {       \"formats\": [],       \"adaptiveFormats\": []     },     \"microformat\": {},     ...   },   \"initialData\": {     \"contents\": {       \"twoColumnWatchNextResults\": {         \"results\": {           \"results\": {             \"contents\": [               {                 \"videoPrimaryInfoRenderer\": {...},                 \"videoSecondaryInfoRenderer\": {...}               }             ]           }         }       }     },     ...   } } ```  ### Key Fields: - `playerResponse`: YouTube player response data   - `videoDetails`: Basic video info (may be empty depending on YouTube's response)   - `streamingData`: Video stream data (includes formats and adaptiveFormats with googlevideo.com URLs)   - `microformat`: Metadata information - `initialData`: YouTube page initialization data   - `videoPrimaryInfoRenderer`: Primary info (title, view count, like count, etc.)   - `videoSecondaryInfoRenderer`: Secondary info (channel info, description, etc.)  # [示例/Examples] ## 获取视频详情数据 / Get video details GET /youtube_web/get_video_info_v3?video_id=oaSNBz4qMQY  ## 指定语言 / Specify language GET /youtube_web/get_video_info_v3?video_id=oaSNBz4qMQY&language_code=en-US  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_info_v3_api_v1_youtube_web_get_video_info_v3_get_with_http_info(video_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object video_id: 视频ID/Video ID (required)
        :param object language_code: 语言代码（如zh-CN, en-US等）/Language code
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'language_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_info_v3_api_v1_youtube_web_get_video_info_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if self.api_client.client_side_validation and ('video_id' not in params or
                                                       params['video_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `video_id` when calling `get_video_info_v3_api_v1_youtube_web_get_video_info_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'video_id' in params:
            query_params.append(('video_id', params['video_id']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/get_video_info_v3', 'GET',
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

    def search_channel_api_v1_youtube_web_search_channel_get(self, channel_id, search_query, **kwargs):  # noqa: E501
        """搜索频道/Search channel  # noqa: E501

        # [中文] ### 用途: - 搜索频道。 ### 参数: - search_query: 搜索关键字。 - language_code: 语言代码，默认为en。 - country_code: 国家代码，默认为us。 - continuation_token: 用于继续获取搜索结果的令牌。默认为None。 ### 返回: - 搜索结果。  # [English] ### Purpose: - Search channel. ### Parameters: - search_query: Search keyword. - language_code: Language code, default is en. - country_code: Country code, default is us. - continuation_token: Token to continue fetching search results. Default is None. ### Returns: - Search results.  # [示例/Example] channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\" search_query = \"AMD\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_channel_api_v1_youtube_web_search_channel_get(channel_id, search_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :param object search_query: 搜索关键字/Search keyword (required)
        :param object language_code: 语言代码/Language code
        :param object country_code: 国家代码/Country code
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_channel_api_v1_youtube_web_search_channel_get_with_http_info(channel_id, search_query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_channel_api_v1_youtube_web_search_channel_get_with_http_info(channel_id, search_query, **kwargs)  # noqa: E501
            return data

    def search_channel_api_v1_youtube_web_search_channel_get_with_http_info(self, channel_id, search_query, **kwargs):  # noqa: E501
        """搜索频道/Search channel  # noqa: E501

        # [中文] ### 用途: - 搜索频道。 ### 参数: - search_query: 搜索关键字。 - language_code: 语言代码，默认为en。 - country_code: 国家代码，默认为us。 - continuation_token: 用于继续获取搜索结果的令牌。默认为None。 ### 返回: - 搜索结果。  # [English] ### Purpose: - Search channel. ### Parameters: - search_query: Search keyword. - language_code: Language code, default is en. - country_code: Country code, default is us. - continuation_token: Token to continue fetching search results. Default is None. ### Returns: - Search results.  # [示例/Example] channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\" search_query = \"AMD\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_channel_api_v1_youtube_web_search_channel_get_with_http_info(channel_id, search_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object channel_id: 频道ID/Channel ID (required)
        :param object search_query: 搜索关键字/Search keyword (required)
        :param object language_code: 语言代码/Language code
        :param object country_code: 国家代码/Country code
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id', 'search_query', 'language_code', 'country_code', 'continuation_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_channel_api_v1_youtube_web_search_channel_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if self.api_client.client_side_validation and ('channel_id' not in params or
                                                       params['channel_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `channel_id` when calling `search_channel_api_v1_youtube_web_search_channel_get`")  # noqa: E501
        # verify the required parameter 'search_query' is set
        if self.api_client.client_side_validation and ('search_query' not in params or
                                                       params['search_query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_query` when calling `search_channel_api_v1_youtube_web_search_channel_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in params:
            query_params.append(('channel_id', params['channel_id']))  # noqa: E501
        if 'search_query' in params:
            query_params.append(('search_query', params['search_query']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/search_channel', 'GET',
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

    def search_video_api_v1_youtube_web_search_video_get(self, search_query, **kwargs):  # noqa: E501
        """搜索视频/Search video  # noqa: E501

        # [中文] ### 用途: - 搜索视频。 ### 参数: - search_query: 搜索关键字。 - language_code: 语言代码，默认为en。 - order_by: 排序方式，默认为this_month，可选值为this_week, this_month, this_year, last_hour, today。 - country_code: 国家代码，默认为us。 - continuation_token: 用于继续获取搜索结果的令牌。默认为None。 ### 返回: - 搜索结果。  # [English] ### Purpose: - Search video. ### Parameters: - search_query: Search keyword. - language_code: Language code, default is en. - order_by: Order by, default is this_month, optional values are this_week, this_month, this_year, last_hour, today. - country_code: Country code, default is us. - continuation_token: Token to continue fetching search results. Default is None. ### Returns: - Search results.  # [示例/Example] search_query = \"Minecraft\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_video_api_v1_youtube_web_search_video_get(search_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_query: 搜索关键字/Search keyword (required)
        :param object language_code: 语言代码/Language code
        :param object order_by: 排序方式/Order by
        :param object country_code: 国家代码/Country code
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_video_api_v1_youtube_web_search_video_get_with_http_info(search_query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_video_api_v1_youtube_web_search_video_get_with_http_info(search_query, **kwargs)  # noqa: E501
            return data

    def search_video_api_v1_youtube_web_search_video_get_with_http_info(self, search_query, **kwargs):  # noqa: E501
        """搜索视频/Search video  # noqa: E501

        # [中文] ### 用途: - 搜索视频。 ### 参数: - search_query: 搜索关键字。 - language_code: 语言代码，默认为en。 - order_by: 排序方式，默认为this_month，可选值为this_week, this_month, this_year, last_hour, today。 - country_code: 国家代码，默认为us。 - continuation_token: 用于继续获取搜索结果的令牌。默认为None。 ### 返回: - 搜索结果。  # [English] ### Purpose: - Search video. ### Parameters: - search_query: Search keyword. - language_code: Language code, default is en. - order_by: Order by, default is this_month, optional values are this_week, this_month, this_year, last_hour, today. - country_code: Country code, default is us. - continuation_token: Token to continue fetching search results. Default is None. ### Returns: - Search results.  # [示例/Example] search_query = \"Minecraft\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_video_api_v1_youtube_web_search_video_get_with_http_info(search_query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object search_query: 搜索关键字/Search keyword (required)
        :param object language_code: 语言代码/Language code
        :param object order_by: 排序方式/Order by
        :param object country_code: 国家代码/Country code
        :param object continuation_token: 翻页令牌/Pagination token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_query', 'language_code', 'order_by', 'country_code', 'continuation_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_video_api_v1_youtube_web_search_video_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_query' is set
        if self.api_client.client_side_validation and ('search_query' not in params or
                                                       params['search_query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_query` when calling `search_video_api_v1_youtube_web_search_video_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_query' in params:
            query_params.append(('search_query', params['search_query']))  # noqa: E501
        if 'language_code' in params:
            query_params.append(('language_code', params['language_code']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))  # noqa: E501
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/youtube/web/search_video', 'GET',
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
