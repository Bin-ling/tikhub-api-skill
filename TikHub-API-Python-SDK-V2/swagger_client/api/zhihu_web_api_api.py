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


class ZhihuWebAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_ai_search_api_v1_zhihu_web_fetch_ai_search_get(self, message_content, **kwargs):  # noqa: E501
        """获取知乎AI搜索/Get Zhihu AI Search  # noqa: E501

        # [中文] ### 用途: - 获取知乎AI搜索 ### 参数: - message_content: 搜索内容 ### 返回: - 知乎AI搜索消息ID，用于请求搜索结果  # [English] ### Purpose: - Get Zhihu AI Search ### Parameters: - message_content: Search Content ### Returns: - Zhihu AI Search Message ID for requesting search results  # [示例/Example] message_content = \"deepseek\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ai_search_api_v1_zhihu_web_fetch_ai_search_get(message_content, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object message_content: 搜索内容/Search Content (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_ai_search_api_v1_zhihu_web_fetch_ai_search_get_with_http_info(message_content, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_ai_search_api_v1_zhihu_web_fetch_ai_search_get_with_http_info(message_content, **kwargs)  # noqa: E501
            return data

    def fetch_ai_search_api_v1_zhihu_web_fetch_ai_search_get_with_http_info(self, message_content, **kwargs):  # noqa: E501
        """获取知乎AI搜索/Get Zhihu AI Search  # noqa: E501

        # [中文] ### 用途: - 获取知乎AI搜索 ### 参数: - message_content: 搜索内容 ### 返回: - 知乎AI搜索消息ID，用于请求搜索结果  # [English] ### Purpose: - Get Zhihu AI Search ### Parameters: - message_content: Search Content ### Returns: - Zhihu AI Search Message ID for requesting search results  # [示例/Example] message_content = \"deepseek\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ai_search_api_v1_zhihu_web_fetch_ai_search_get_with_http_info(message_content, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object message_content: 搜索内容/Search Content (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_content']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_ai_search_api_v1_zhihu_web_fetch_ai_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_content' is set
        if self.api_client.client_side_validation and ('message_content' not in params or
                                                       params['message_content'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `message_content` when calling `fetch_ai_search_api_v1_zhihu_web_fetch_ai_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'message_content' in params:
            query_params.append(('message_content', params['message_content']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_ai_search', 'GET',
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

    def fetch_ai_search_result_api_v1_zhihu_web_fetch_ai_search_result_get(self, message_id, **kwargs):  # noqa: E501
        """获取知乎AI搜索结果/Get Zhihu AI Search Result  # noqa: E501

        # [中文] ### 用途: - 获取知乎AI搜索结果 ### 参数: - message_id: 消息ID ### 返回: - 知乎AI搜索结果  # [English] ### Purpose: - Get Zhihu AI Search Result ### Parameters: - message_id: Message ID ### Returns: - Zhihu AI Search Result  # [示例/Example] message_id = \"5f8b4f4a-0b7c-4d1b-8c4f-2e5c0d6c1b9d\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ai_search_result_api_v1_zhihu_web_fetch_ai_search_result_get(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object message_id: 消息ID/Message ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_ai_search_result_api_v1_zhihu_web_fetch_ai_search_result_get_with_http_info(message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_ai_search_result_api_v1_zhihu_web_fetch_ai_search_result_get_with_http_info(message_id, **kwargs)  # noqa: E501
            return data

    def fetch_ai_search_result_api_v1_zhihu_web_fetch_ai_search_result_get_with_http_info(self, message_id, **kwargs):  # noqa: E501
        """获取知乎AI搜索结果/Get Zhihu AI Search Result  # noqa: E501

        # [中文] ### 用途: - 获取知乎AI搜索结果 ### 参数: - message_id: 消息ID ### 返回: - 知乎AI搜索结果  # [English] ### Purpose: - Get Zhihu AI Search Result ### Parameters: - message_id: Message ID ### Returns: - Zhihu AI Search Result  # [示例/Example] message_id = \"5f8b4f4a-0b7c-4d1b-8c4f-2e5c0d6c1b9d\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ai_search_result_api_v1_zhihu_web_fetch_ai_search_result_get_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object message_id: 消息ID/Message ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_ai_search_result_api_v1_zhihu_web_fetch_ai_search_result_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_id' is set
        if self.api_client.client_side_validation and ('message_id' not in params or
                                                       params['message_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `message_id` when calling `fetch_ai_search_result_api_v1_zhihu_web_fetch_ai_search_result_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'message_id' in params:
            query_params.append(('message_id', params['message_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_ai_search_result', 'GET',
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

    def fetch_article_search_v3_api_v1_zhihu_web_fetch_article_search_v3_get(self, keyword, **kwargs):  # noqa: E501
        """获取知乎文章搜索V3/Get Zhihu Article Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎文章搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页文章数量 - show_all_topics: 显示所有主题，     - 0 不显示话题     - 1 显示话题 - search_source: 搜索来源     - Filter 过滤参数生效     - Normal 为普通结果 - search_hash_id: 搜索哈希ID，用于过滤重复搜索结果 - vertical: 空 不限类型     - answer 只看回答     - article 只看文章     - zvideo 只看视频 - sort: 空 综合排序     - upvoted_count 最多赞同     - created_time 最新发布 - time_interval: 时间间隔     - 空 不限时间     - a_day 一天内     - a_week 一周内     - a_month 一个月内     - three_months 三个月内     - half_a_year 半年内     - a_year 一年内 - vertical_info: 垂类信息     - 0,0,0,0,0,0,0,0,0,0,0,0 不限类型，不会设置勿填 ### 返回: - 知乎文章搜索V3  # [English] ### Purpose: - Get Zhihu Article Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of articles per page - show_all_topics: Show all topics     - 0 Do not show topics     - 1 Show topics - search_source: Search Source     - Filter parameter takes effect     - Normal is normal result - search_hash_id: Search Hash ID, used to filter duplicate search results - vertical: Empty unlimited type     - answer only see answers     - article only see articles     - zvideo only see videos - sort: Empty comprehensive sorting     - upvoted_count most upvoted     - created_time latest release - time_interval: Time interval     - Empty unlimited time     - a_day within a day     - a_week within a week     - a_month within a month     - three_months within three months     - half_a_year within half a year     - a_year within a year - vertical_info: Vertical information     - 0,0,0,0,0,0,0,0,0,0,0,0 unlimited type, do not set do not fill ### Returns: - Zhihu Article Search V3  # [示例/Example] # 默认搜索，综合排序，不限时间 keyword = \"deepseek\" offset = \"0\" limit = \"20\" show_all_topics = 0 search_source = \"Normal\" search_hash_id = \"\" vertical = \"\" sort = \"\" time_interval = \"\" vertical_info = \"\"  # 只看回答，最多赞同，三月内 keyword = \"deepseek\" offset = \"0\" limit = \"20\" show_all_topics = 0 search_source = \"Filter\" search_hash_id = \"\" vertical = \"answer\" sort = \"upvoted_count\" time_interval = \"three_months\" vertical_info = \"0,0,0,0,0,0,0,0,0,0,0,0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_article_search_v3_api_v1_zhihu_web_fetch_article_search_v3_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页文章数量/Number of articles per page
        :param object show_all_topics: 显示所有主题/Show all topics
        :param object search_source: 搜索来源/Search Source
        :param object search_hash_id: 搜索哈希ID/Search Hash ID
        :param object vertical: 垂类/Vertical Type
        :param object sort: 排序/Sort
        :param object time_interval: 时间间隔/Time Interval
        :param object vertical_info: 垂类信息/Vertical Info
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_article_search_v3_api_v1_zhihu_web_fetch_article_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_article_search_v3_api_v1_zhihu_web_fetch_article_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_article_search_v3_api_v1_zhihu_web_fetch_article_search_v3_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取知乎文章搜索V3/Get Zhihu Article Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎文章搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页文章数量 - show_all_topics: 显示所有主题，     - 0 不显示话题     - 1 显示话题 - search_source: 搜索来源     - Filter 过滤参数生效     - Normal 为普通结果 - search_hash_id: 搜索哈希ID，用于过滤重复搜索结果 - vertical: 空 不限类型     - answer 只看回答     - article 只看文章     - zvideo 只看视频 - sort: 空 综合排序     - upvoted_count 最多赞同     - created_time 最新发布 - time_interval: 时间间隔     - 空 不限时间     - a_day 一天内     - a_week 一周内     - a_month 一个月内     - three_months 三个月内     - half_a_year 半年内     - a_year 一年内 - vertical_info: 垂类信息     - 0,0,0,0,0,0,0,0,0,0,0,0 不限类型，不会设置勿填 ### 返回: - 知乎文章搜索V3  # [English] ### Purpose: - Get Zhihu Article Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of articles per page - show_all_topics: Show all topics     - 0 Do not show topics     - 1 Show topics - search_source: Search Source     - Filter parameter takes effect     - Normal is normal result - search_hash_id: Search Hash ID, used to filter duplicate search results - vertical: Empty unlimited type     - answer only see answers     - article only see articles     - zvideo only see videos - sort: Empty comprehensive sorting     - upvoted_count most upvoted     - created_time latest release - time_interval: Time interval     - Empty unlimited time     - a_day within a day     - a_week within a week     - a_month within a month     - three_months within three months     - half_a_year within half a year     - a_year within a year - vertical_info: Vertical information     - 0,0,0,0,0,0,0,0,0,0,0,0 unlimited type, do not set do not fill ### Returns: - Zhihu Article Search V3  # [示例/Example] # 默认搜索，综合排序，不限时间 keyword = \"deepseek\" offset = \"0\" limit = \"20\" show_all_topics = 0 search_source = \"Normal\" search_hash_id = \"\" vertical = \"\" sort = \"\" time_interval = \"\" vertical_info = \"\"  # 只看回答，最多赞同，三月内 keyword = \"deepseek\" offset = \"0\" limit = \"20\" show_all_topics = 0 search_source = \"Filter\" search_hash_id = \"\" vertical = \"answer\" sort = \"upvoted_count\" time_interval = \"three_months\" vertical_info = \"0,0,0,0,0,0,0,0,0,0,0,0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_article_search_v3_api_v1_zhihu_web_fetch_article_search_v3_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页文章数量/Number of articles per page
        :param object show_all_topics: 显示所有主题/Show all topics
        :param object search_source: 搜索来源/Search Source
        :param object search_hash_id: 搜索哈希ID/Search Hash ID
        :param object vertical: 垂类/Vertical Type
        :param object sort: 排序/Sort
        :param object time_interval: 时间间隔/Time Interval
        :param object vertical_info: 垂类信息/Vertical Info
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'limit', 'show_all_topics', 'search_source', 'search_hash_id', 'vertical', 'sort', 'time_interval', 'vertical_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_article_search_v3_api_v1_zhihu_web_fetch_article_search_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_article_search_v3_api_v1_zhihu_web_fetch_article_search_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'show_all_topics' in params:
            query_params.append(('show_all_topics', params['show_all_topics']))  # noqa: E501
        if 'search_source' in params:
            query_params.append(('search_source', params['search_source']))  # noqa: E501
        if 'search_hash_id' in params:
            query_params.append(('search_hash_id', params['search_hash_id']))  # noqa: E501
        if 'vertical' in params:
            query_params.append(('vertical', params['vertical']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'time_interval' in params:
            query_params.append(('time_interval', params['time_interval']))  # noqa: E501
        if 'vertical_info' in params:
            query_params.append(('vertical_info', params['vertical_info']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_article_search_v3', 'GET',
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

    def fetch_column_article_detail_api_v1_zhihu_web_fetch_column_article_detail_get(self, article_id, **kwargs):  # noqa: E501
        """获取知乎专栏文章详情/Get Zhihu Column Article Detail  # noqa: E501

        # [中文] ### 用途: - 获取知乎专栏文章详情 ### 参数: - article_id: 文章ID ### 返回: - 知乎专栏文章详情  # [English] ### Purpose: - Get Zhihu Column Article Detail ### Parameters: - article_id: Article ID ### Returns: - Zhihu Column Article Detail  # [示例/Example] article_id = \"669214677\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_article_detail_api_v1_zhihu_web_fetch_column_article_detail_get(article_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object article_id: 文章ID/Article ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_column_article_detail_api_v1_zhihu_web_fetch_column_article_detail_get_with_http_info(article_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_column_article_detail_api_v1_zhihu_web_fetch_column_article_detail_get_with_http_info(article_id, **kwargs)  # noqa: E501
            return data

    def fetch_column_article_detail_api_v1_zhihu_web_fetch_column_article_detail_get_with_http_info(self, article_id, **kwargs):  # noqa: E501
        """获取知乎专栏文章详情/Get Zhihu Column Article Detail  # noqa: E501

        # [中文] ### 用途: - 获取知乎专栏文章详情 ### 参数: - article_id: 文章ID ### 返回: - 知乎专栏文章详情  # [English] ### Purpose: - Get Zhihu Column Article Detail ### Parameters: - article_id: Article ID ### Returns: - Zhihu Column Article Detail  # [示例/Example] article_id = \"669214677\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_article_detail_api_v1_zhihu_web_fetch_column_article_detail_get_with_http_info(article_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object article_id: 文章ID/Article ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['article_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_column_article_detail_api_v1_zhihu_web_fetch_column_article_detail_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'article_id' is set
        if self.api_client.client_side_validation and ('article_id' not in params or
                                                       params['article_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `article_id` when calling `fetch_column_article_detail_api_v1_zhihu_web_fetch_column_article_detail_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'article_id' in params:
            query_params.append(('article_id', params['article_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_column_article_detail', 'GET',
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

    def fetch_column_articles_api_v1_zhihu_web_fetch_column_articles_get(self, column_id, **kwargs):  # noqa: E501
        """获取知乎专栏文章列表/Get Zhihu Column Articles  # noqa: E501

        # [中文] ### 用途: - 获取知乎专栏文章列表 ### 参数: - column_id: 专栏ID - limit: 每页文章数量 - offset: 偏移量 ### 返回: - 知乎专栏文章列表  # [English] ### Purpose: - Get Zhihu Column Articles ### Parameters: - column_id: Column ID - limit: Number of articles per page - offset: Offset ### Returns: - Zhihu Column Articles  # [示例/Example] column_id = \"zhangjiawei\" limit = \"10\" offset = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_articles_api_v1_zhihu_web_fetch_column_articles_get(column_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object column_id: 专栏ID/Column ID (required)
        :param object limit: 每页文章数量/Number of articles per page
        :param object offset: 偏移量/Offset
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_column_articles_api_v1_zhihu_web_fetch_column_articles_get_with_http_info(column_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_column_articles_api_v1_zhihu_web_fetch_column_articles_get_with_http_info(column_id, **kwargs)  # noqa: E501
            return data

    def fetch_column_articles_api_v1_zhihu_web_fetch_column_articles_get_with_http_info(self, column_id, **kwargs):  # noqa: E501
        """获取知乎专栏文章列表/Get Zhihu Column Articles  # noqa: E501

        # [中文] ### 用途: - 获取知乎专栏文章列表 ### 参数: - column_id: 专栏ID - limit: 每页文章数量 - offset: 偏移量 ### 返回: - 知乎专栏文章列表  # [English] ### Purpose: - Get Zhihu Column Articles ### Parameters: - column_id: Column ID - limit: Number of articles per page - offset: Offset ### Returns: - Zhihu Column Articles  # [示例/Example] column_id = \"zhangjiawei\" limit = \"10\" offset = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_articles_api_v1_zhihu_web_fetch_column_articles_get_with_http_info(column_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object column_id: 专栏ID/Column ID (required)
        :param object limit: 每页文章数量/Number of articles per page
        :param object offset: 偏移量/Offset
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['column_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_column_articles_api_v1_zhihu_web_fetch_column_articles_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'column_id' is set
        if self.api_client.client_side_validation and ('column_id' not in params or
                                                       params['column_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `column_id` when calling `fetch_column_articles_api_v1_zhihu_web_fetch_column_articles_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'column_id' in params:
            query_params.append(('column_id', params['column_id']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_column_articles', 'GET',
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

    def fetch_column_comment_config_api_v1_zhihu_web_fetch_column_comment_config_get(self, article_id, **kwargs):  # noqa: E501
        """获取知乎专栏评论区配置/Get Zhihu Column Comment Config  # noqa: E501

        # [中文] ### 用途: - 获取知乎专栏评论区配置 ### 参数: - article_id: 文章ID ### 返回: - 知乎专栏评论区配置  # [English] ### Purpose: - Get Zhihu Column Comment Config ### Parameters: - article_id: Article ID ### Returns: - Zhihu Column Comment Config  # [示例/Example] article_id = \"669214677\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_comment_config_api_v1_zhihu_web_fetch_column_comment_config_get(article_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object article_id: 文章ID/Article ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_column_comment_config_api_v1_zhihu_web_fetch_column_comment_config_get_with_http_info(article_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_column_comment_config_api_v1_zhihu_web_fetch_column_comment_config_get_with_http_info(article_id, **kwargs)  # noqa: E501
            return data

    def fetch_column_comment_config_api_v1_zhihu_web_fetch_column_comment_config_get_with_http_info(self, article_id, **kwargs):  # noqa: E501
        """获取知乎专栏评论区配置/Get Zhihu Column Comment Config  # noqa: E501

        # [中文] ### 用途: - 获取知乎专栏评论区配置 ### 参数: - article_id: 文章ID ### 返回: - 知乎专栏评论区配置  # [English] ### Purpose: - Get Zhihu Column Comment Config ### Parameters: - article_id: Article ID ### Returns: - Zhihu Column Comment Config  # [示例/Example] article_id = \"669214677\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_comment_config_api_v1_zhihu_web_fetch_column_comment_config_get_with_http_info(article_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object article_id: 文章ID/Article ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['article_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_column_comment_config_api_v1_zhihu_web_fetch_column_comment_config_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'article_id' is set
        if self.api_client.client_side_validation and ('article_id' not in params or
                                                       params['article_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `article_id` when calling `fetch_column_comment_config_api_v1_zhihu_web_fetch_column_comment_config_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'article_id' in params:
            query_params.append(('article_id', params['article_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_column_comment_config', 'GET',
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

    def fetch_column_recommend_api_v1_zhihu_web_fetch_column_recommend_get(self, article_id, **kwargs):  # noqa: E501
        """获取知乎相似专栏推荐/Get Zhihu Similar Column Recommend  # noqa: E501

        # [中文] ### 用途: - 获取知乎相似专栏推荐 ### 参数: - article_id: 文章ID - limit: 每页专栏数量 - offset: 偏移量 ### 返回: - 知乎相似专栏推荐  # [English] ### Purpose: - Get Zhihu Similar Column Recommend ### Parameters: - article_id: Article ID - limit: Number of columns per page - offset: Offset ### Returns: - Zhihu Similar Column Recommend  # [示例/Example] article_id = \"669214677\" limit = \"12\" offset = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_recommend_api_v1_zhihu_web_fetch_column_recommend_get(article_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object article_id: 文章ID/Article ID (required)
        :param object limit: 每页专栏数量/Number of columns per page
        :param object offset: 偏移量/Offset
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_column_recommend_api_v1_zhihu_web_fetch_column_recommend_get_with_http_info(article_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_column_recommend_api_v1_zhihu_web_fetch_column_recommend_get_with_http_info(article_id, **kwargs)  # noqa: E501
            return data

    def fetch_column_recommend_api_v1_zhihu_web_fetch_column_recommend_get_with_http_info(self, article_id, **kwargs):  # noqa: E501
        """获取知乎相似专栏推荐/Get Zhihu Similar Column Recommend  # noqa: E501

        # [中文] ### 用途: - 获取知乎相似专栏推荐 ### 参数: - article_id: 文章ID - limit: 每页专栏数量 - offset: 偏移量 ### 返回: - 知乎相似专栏推荐  # [English] ### Purpose: - Get Zhihu Similar Column Recommend ### Parameters: - article_id: Article ID - limit: Number of columns per page - offset: Offset ### Returns: - Zhihu Similar Column Recommend  # [示例/Example] article_id = \"669214677\" limit = \"12\" offset = \"0\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_recommend_api_v1_zhihu_web_fetch_column_recommend_get_with_http_info(article_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object article_id: 文章ID/Article ID (required)
        :param object limit: 每页专栏数量/Number of columns per page
        :param object offset: 偏移量/Offset
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['article_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_column_recommend_api_v1_zhihu_web_fetch_column_recommend_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'article_id' is set
        if self.api_client.client_side_validation and ('article_id' not in params or
                                                       params['article_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `article_id` when calling `fetch_column_recommend_api_v1_zhihu_web_fetch_column_recommend_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'article_id' in params:
            query_params.append(('article_id', params['article_id']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_column_recommend', 'GET',
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

    def fetch_column_relationship_api_v1_zhihu_web_fetch_column_relationship_get(self, article_id, **kwargs):  # noqa: E501
        """获取知乎专栏文章互动关系/Get Zhihu Column Article Relationship  # noqa: E501

        # [中文] ### 用途: - 获取知乎专栏文章互动关系 ### 参数: - article_id: 文章ID ### 返回: - 知乎专栏互动关系  # [English] ### Purpose: - Get Zhihu Column Relationship ### Parameters: - article_id: Article ID ### Returns: - Zhihu Column Relationship  # [示例/Example] article_id = \"669214677\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_relationship_api_v1_zhihu_web_fetch_column_relationship_get(article_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object article_id: 文章ID/Article ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_column_relationship_api_v1_zhihu_web_fetch_column_relationship_get_with_http_info(article_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_column_relationship_api_v1_zhihu_web_fetch_column_relationship_get_with_http_info(article_id, **kwargs)  # noqa: E501
            return data

    def fetch_column_relationship_api_v1_zhihu_web_fetch_column_relationship_get_with_http_info(self, article_id, **kwargs):  # noqa: E501
        """获取知乎专栏文章互动关系/Get Zhihu Column Article Relationship  # noqa: E501

        # [中文] ### 用途: - 获取知乎专栏文章互动关系 ### 参数: - article_id: 文章ID ### 返回: - 知乎专栏互动关系  # [English] ### Purpose: - Get Zhihu Column Relationship ### Parameters: - article_id: Article ID ### Returns: - Zhihu Column Relationship  # [示例/Example] article_id = \"669214677\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_relationship_api_v1_zhihu_web_fetch_column_relationship_get_with_http_info(article_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object article_id: 文章ID/Article ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['article_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_column_relationship_api_v1_zhihu_web_fetch_column_relationship_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'article_id' is set
        if self.api_client.client_side_validation and ('article_id' not in params or
                                                       params['article_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `article_id` when calling `fetch_column_relationship_api_v1_zhihu_web_fetch_column_relationship_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'article_id' in params:
            query_params.append(('article_id', params['article_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_column_relationship', 'GET',
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

    def fetch_column_search_v3_api_v1_zhihu_web_fetch_column_search_v3_get(self, keyword, **kwargs):  # noqa: E501
        """获取知乎专栏搜索V3/Get Zhihu Column Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎专栏搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页专栏数量 - search_hash_id: 搜索哈希ID ### 返回: - 知乎专栏搜索V3  # [English] ### Purpose: - Get Zhihu Column Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of columns per page - search_hash_id: Search Hash ID ### Returns: - Zhihu Column Search V3  # [示例/Example] keyword = \"deepseek\" limit = \"20\" offset = \"0\" search_hash_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_search_v3_api_v1_zhihu_web_fetch_column_search_v3_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页专栏数量/Number of columns per page
        :param object search_hash_id: 搜索哈希ID/Search Hash ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_column_search_v3_api_v1_zhihu_web_fetch_column_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_column_search_v3_api_v1_zhihu_web_fetch_column_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_column_search_v3_api_v1_zhihu_web_fetch_column_search_v3_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取知乎专栏搜索V3/Get Zhihu Column Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎专栏搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页专栏数量 - search_hash_id: 搜索哈希ID ### 返回: - 知乎专栏搜索V3  # [English] ### Purpose: - Get Zhihu Column Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of columns per page - search_hash_id: Search Hash ID ### Returns: - Zhihu Column Search V3  # [示例/Example] keyword = \"deepseek\" limit = \"20\" offset = \"0\" search_hash_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_column_search_v3_api_v1_zhihu_web_fetch_column_search_v3_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页专栏数量/Number of columns per page
        :param object search_hash_id: 搜索哈希ID/Search Hash ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'limit', 'search_hash_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_column_search_v3_api_v1_zhihu_web_fetch_column_search_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_column_search_v3_api_v1_zhihu_web_fetch_column_search_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'search_hash_id' in params:
            query_params.append(('search_hash_id', params['search_hash_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_column_search_v3', 'GET',
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

    def fetch_comment_v5_api_v1_zhihu_web_fetch_comment_v5_get(self, answer_id, **kwargs):  # noqa: E501
        """获取知乎评论区V5/Get Zhihu Comment V5  # noqa: E501

        # [中文] ### 用途: - 获取知乎评论区V5 ### 参数: - answer_id: 回答ID - order_by: 排序     - score 最热排序     - ts 最新排序 - limit: 每页评论数量 - offset: 偏移量/页码 ### 返回: - 知乎评论区V5  # [English] ### Purpose: - Get Zhihu Comment V5 ### Parameters: - answer_id: Answer ID - order_by: Sort     - score Hottest Sort     - ts Latest Sort - limit: Number of comments per page - offset: Offset/Page Number ### Returns: - Zhihu Comment V5  # [示例/Example] answer_id = \"89226347214\" order_by = \"score\" limit = \"20\" offset = \"\" # 1739257701_11108372663_0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comment_v5_api_v1_zhihu_web_fetch_comment_v5_get(answer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object answer_id: 回答ID/Answer ID (required)
        :param object order_by: 排序/Sort
        :param object limit: 每页评论数量/Number of comments per page
        :param object offset: 偏移量/Offset
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_comment_v5_api_v1_zhihu_web_fetch_comment_v5_get_with_http_info(answer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_comment_v5_api_v1_zhihu_web_fetch_comment_v5_get_with_http_info(answer_id, **kwargs)  # noqa: E501
            return data

    def fetch_comment_v5_api_v1_zhihu_web_fetch_comment_v5_get_with_http_info(self, answer_id, **kwargs):  # noqa: E501
        """获取知乎评论区V5/Get Zhihu Comment V5  # noqa: E501

        # [中文] ### 用途: - 获取知乎评论区V5 ### 参数: - answer_id: 回答ID - order_by: 排序     - score 最热排序     - ts 最新排序 - limit: 每页评论数量 - offset: 偏移量/页码 ### 返回: - 知乎评论区V5  # [English] ### Purpose: - Get Zhihu Comment V5 ### Parameters: - answer_id: Answer ID - order_by: Sort     - score Hottest Sort     - ts Latest Sort - limit: Number of comments per page - offset: Offset/Page Number ### Returns: - Zhihu Comment V5  # [示例/Example] answer_id = \"89226347214\" order_by = \"score\" limit = \"20\" offset = \"\" # 1739257701_11108372663_0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_comment_v5_api_v1_zhihu_web_fetch_comment_v5_get_with_http_info(answer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object answer_id: 回答ID/Answer ID (required)
        :param object order_by: 排序/Sort
        :param object limit: 每页评论数量/Number of comments per page
        :param object offset: 偏移量/Offset
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['answer_id', 'order_by', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_comment_v5_api_v1_zhihu_web_fetch_comment_v5_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'answer_id' is set
        if self.api_client.client_side_validation and ('answer_id' not in params or
                                                       params['answer_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `answer_id` when calling `fetch_comment_v5_api_v1_zhihu_web_fetch_comment_v5_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'answer_id' in params:
            query_params.append(('answer_id', params['answer_id']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_comment_v5', 'GET',
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

    def fetch_ebook_search_v3_api_v1_zhihu_web_fetch_ebook_search_v3_get(self, keyword, **kwargs):  # noqa: E501
        """获取知乎电子书搜索V3/Get Zhihu Ebook Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎电子书搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页电子书数量 - search_hash_id: 搜索哈希ID ### 返回: - 知乎电子书搜索V3  # [English] ### Purpose: - Get Zhihu Ebook Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of ebooks per page - search_hash_id: Search Hash ID ### Returns: - Zhihu Ebook Search V3  # [示例/Example] keyword = \"deepseek\" limit = \"20\" offset = \"0\" search_hash_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ebook_search_v3_api_v1_zhihu_web_fetch_ebook_search_v3_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页电子书数量/Number of ebooks per page
        :param object search_hash_id: 搜索哈希ID/Search Hash ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_ebook_search_v3_api_v1_zhihu_web_fetch_ebook_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_ebook_search_v3_api_v1_zhihu_web_fetch_ebook_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_ebook_search_v3_api_v1_zhihu_web_fetch_ebook_search_v3_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取知乎电子书搜索V3/Get Zhihu Ebook Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎电子书搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页电子书数量 - search_hash_id: 搜索哈希ID ### 返回: - 知乎电子书搜索V3  # [English] ### Purpose: - Get Zhihu Ebook Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of ebooks per page - search_hash_id: Search Hash ID ### Returns: - Zhihu Ebook Search V3  # [示例/Example] keyword = \"deepseek\" limit = \"20\" offset = \"0\" search_hash_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_ebook_search_v3_api_v1_zhihu_web_fetch_ebook_search_v3_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页电子书数量/Number of ebooks per page
        :param object search_hash_id: 搜索哈希ID/Search Hash ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'limit', 'search_hash_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_ebook_search_v3_api_v1_zhihu_web_fetch_ebook_search_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_ebook_search_v3_api_v1_zhihu_web_fetch_ebook_search_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'search_hash_id' in params:
            query_params.append(('search_hash_id', params['search_hash_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_ebook_search_v3', 'GET',
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

    def fetch_hot_list_api_v1_zhihu_web_fetch_hot_list_get(self, **kwargs):  # noqa: E501
        """获取知乎首页热榜/Get Zhihu Hot List  # noqa: E501

        # [中文] ### 用途: - 获取知乎首页热榜 ### 参数: - limit: 每页文章数量 - desktop: 是否为桌面端 ### 返回: - 知乎首页热榜  # [English] ### Purpose: - Get Zhihu Hot List ### Parameters: - limit: Number of articles per page - desktop: Is it a desktop ### Returns: - Zhihu Hot List  # [示例/Example] limit = \"50\" desktop = \"true\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_list_api_v1_zhihu_web_fetch_hot_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit: 每页文章数量/Number of articles per page
        :param object desktop: 是否为桌面端/Is it a desktop
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_list_api_v1_zhihu_web_fetch_hot_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_list_api_v1_zhihu_web_fetch_hot_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_list_api_v1_zhihu_web_fetch_hot_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取知乎首页热榜/Get Zhihu Hot List  # noqa: E501

        # [中文] ### 用途: - 获取知乎首页热榜 ### 参数: - limit: 每页文章数量 - desktop: 是否为桌面端 ### 返回: - 知乎首页热榜  # [English] ### Purpose: - Get Zhihu Hot List ### Parameters: - limit: Number of articles per page - desktop: Is it a desktop ### Returns: - Zhihu Hot List  # [示例/Example] limit = \"50\" desktop = \"true\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_list_api_v1_zhihu_web_fetch_hot_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit: 每页文章数量/Number of articles per page
        :param object desktop: 是否为桌面端/Is it a desktop
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'desktop']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_list_api_v1_zhihu_web_fetch_hot_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'desktop' in params:
            query_params.append(('desktop', params['desktop']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_hot_list', 'GET',
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

    def fetch_hot_recommend_api_v1_zhihu_web_fetch_hot_recommend_get(self, **kwargs):  # noqa: E501
        """获取知乎首页推荐/Get Zhihu Hot Recommend  # noqa: E501

        # [中文] ### 用途: - 获取知乎首页推荐 ### 参数: - offset: 偏移量 - page_number: 页码 - session_token: 会话令牌 ### 返回: - 知乎首页推荐  # [English] ### Purpose: - Get Zhihu Hot Recommend ### Parameters: - offset: Offset - page_number: Page Number - session_token: Session Token  # [示例/Example] offset = \"0\" page_number = \"1\" session_token = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_recommend_api_v1_zhihu_web_fetch_hot_recommend_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object offset: 偏移量/Offset
        :param object page_number: 页码/Page Number
        :param object session_token: 会话令牌/Session Token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_hot_recommend_api_v1_zhihu_web_fetch_hot_recommend_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_hot_recommend_api_v1_zhihu_web_fetch_hot_recommend_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_hot_recommend_api_v1_zhihu_web_fetch_hot_recommend_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取知乎首页推荐/Get Zhihu Hot Recommend  # noqa: E501

        # [中文] ### 用途: - 获取知乎首页推荐 ### 参数: - offset: 偏移量 - page_number: 页码 - session_token: 会话令牌 ### 返回: - 知乎首页推荐  # [English] ### Purpose: - Get Zhihu Hot Recommend ### Parameters: - offset: Offset - page_number: Page Number - session_token: Session Token  # [示例/Example] offset = \"0\" page_number = \"1\" session_token = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_hot_recommend_api_v1_zhihu_web_fetch_hot_recommend_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object offset: 偏移量/Offset
        :param object page_number: 页码/Page Number
        :param object session_token: 会话令牌/Session Token
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'page_number', 'session_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_hot_recommend_api_v1_zhihu_web_fetch_hot_recommend_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'session_token' in params:
            query_params.append(('session_token', params['session_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_hot_recommend', 'GET',
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

    def fetch_preset_search_api_v1_zhihu_web_fetch_preset_search_get(self, **kwargs):  # noqa: E501
        """获取知乎搜索预设词/Get Zhihu Preset Search  # noqa: E501

        # [中文] ### 用途: - 获取知乎搜索预设词 ### 参数: - 无 ### 返回: - 知乎搜索预设词  # [English] ### Purpose: - Get Zhihu Preset Search ### Parameters: - None ### Returns: - Zhihu Preset Search  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_preset_search_api_v1_zhihu_web_fetch_preset_search_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_preset_search_api_v1_zhihu_web_fetch_preset_search_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_preset_search_api_v1_zhihu_web_fetch_preset_search_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_preset_search_api_v1_zhihu_web_fetch_preset_search_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取知乎搜索预设词/Get Zhihu Preset Search  # noqa: E501

        # [中文] ### 用途: - 获取知乎搜索预设词 ### 参数: - 无 ### 返回: - 知乎搜索预设词  # [English] ### Purpose: - Get Zhihu Preset Search ### Parameters: - None ### Returns: - Zhihu Preset Search  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_preset_search_api_v1_zhihu_web_fetch_preset_search_get_with_http_info(async_req=True)
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
                    " to method fetch_preset_search_api_v1_zhihu_web_fetch_preset_search_get" % key
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
            '/api/v1/zhihu/web/fetch_preset_search', 'GET',
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

    def fetch_question_answers_api_v1_zhihu_web_fetch_question_answers_get(self, question_id, **kwargs):  # noqa: E501
        """获取知乎问题回答列表/Get Zhihu Question Answers  # noqa: E501

        # [中文] ### 用途: - 获取知乎问题的回答列表 ### 参数: - question_id: 问题ID - cursor: 分页游标，用于获取下一页数据，从返回的字段里提取 - limit: 每页回答数量，默认5 - offset: 偏移量，默认0 - order: 排序方式，default=默认排序，updated=按时间排序 - session_id: 会话ID，用于分页时保持状态，从返回的字段里提取 ### 返回: - 知乎问题回答列表数据  # [English] ### Purpose: - Get Zhihu Question Answers List ### Parameters: - question_id: Question ID - cursor: Pagination cursor for next page, extracted from response fields - limit: Number of answers per page, default 5 - offset: Offset, default 0 - order: Sort order, default=default sort, updated=sort by time - session_id: Session ID for pagination state, extracted from response fields ### Returns: - Zhihu Question Answers List Data  # [示例/Example] question_id = \"37811449\" cursor = \"\" limit = 5 offset = 0 order = \"default\"  # 或 \"updated\" 按时间排序 session_id = \"\"  # 获取下一页 (Get next page): cursor = \"d88f09569eba20b966bcf15076977430\" offset = 1 session_id = \"1757928778451769939\"  # 按时间排序 (Sort by time): order = \"updated\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_question_answers_api_v1_zhihu_web_fetch_question_answers_get(question_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object question_id: 问题ID/Question ID (required)
        :param object cursor: 分页游标/Pagination cursor
        :param object limit: 每页回答数量/Number of answers per page
        :param object offset: 偏移量/Offset
        :param object order: 排序方式：default=默认排序，updated=按时间排序/Sort order: default=default sort, updated=sort by time
        :param object session_id: 会话ID/Session ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_question_answers_api_v1_zhihu_web_fetch_question_answers_get_with_http_info(question_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_question_answers_api_v1_zhihu_web_fetch_question_answers_get_with_http_info(question_id, **kwargs)  # noqa: E501
            return data

    def fetch_question_answers_api_v1_zhihu_web_fetch_question_answers_get_with_http_info(self, question_id, **kwargs):  # noqa: E501
        """获取知乎问题回答列表/Get Zhihu Question Answers  # noqa: E501

        # [中文] ### 用途: - 获取知乎问题的回答列表 ### 参数: - question_id: 问题ID - cursor: 分页游标，用于获取下一页数据，从返回的字段里提取 - limit: 每页回答数量，默认5 - offset: 偏移量，默认0 - order: 排序方式，default=默认排序，updated=按时间排序 - session_id: 会话ID，用于分页时保持状态，从返回的字段里提取 ### 返回: - 知乎问题回答列表数据  # [English] ### Purpose: - Get Zhihu Question Answers List ### Parameters: - question_id: Question ID - cursor: Pagination cursor for next page, extracted from response fields - limit: Number of answers per page, default 5 - offset: Offset, default 0 - order: Sort order, default=default sort, updated=sort by time - session_id: Session ID for pagination state, extracted from response fields ### Returns: - Zhihu Question Answers List Data  # [示例/Example] question_id = \"37811449\" cursor = \"\" limit = 5 offset = 0 order = \"default\"  # 或 \"updated\" 按时间排序 session_id = \"\"  # 获取下一页 (Get next page): cursor = \"d88f09569eba20b966bcf15076977430\" offset = 1 session_id = \"1757928778451769939\"  # 按时间排序 (Sort by time): order = \"updated\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_question_answers_api_v1_zhihu_web_fetch_question_answers_get_with_http_info(question_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object question_id: 问题ID/Question ID (required)
        :param object cursor: 分页游标/Pagination cursor
        :param object limit: 每页回答数量/Number of answers per page
        :param object offset: 偏移量/Offset
        :param object order: 排序方式：default=默认排序，updated=按时间排序/Sort order: default=default sort, updated=sort by time
        :param object session_id: 会话ID/Session ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['question_id', 'cursor', 'limit', 'offset', 'order', 'session_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_question_answers_api_v1_zhihu_web_fetch_question_answers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'question_id' is set
        if self.api_client.client_side_validation and ('question_id' not in params or
                                                       params['question_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `question_id` when calling `fetch_question_answers_api_v1_zhihu_web_fetch_question_answers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'question_id' in params:
            query_params.append(('question_id', params['question_id']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_question_answers', 'GET',
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

    def fetch_recommend_followees_api_v1_zhihu_web_fetch_recommend_followees_get(self, **kwargs):  # noqa: E501
        """获取知乎推荐关注列表/Get Zhihu Recommend Followees  # noqa: E501

        # [中文] ### 用途: - 获取知乎推荐关注列表 ### 参数: - 无 ### 返回: - 知乎推荐关注列表  # [English] ### Purpose: - Get Zhihu Recommend Followees ### Parameters: - None ### Returns: - Zhihu Recommend Followees  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_recommend_followees_api_v1_zhihu_web_fetch_recommend_followees_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_recommend_followees_api_v1_zhihu_web_fetch_recommend_followees_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_recommend_followees_api_v1_zhihu_web_fetch_recommend_followees_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_recommend_followees_api_v1_zhihu_web_fetch_recommend_followees_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取知乎推荐关注列表/Get Zhihu Recommend Followees  # noqa: E501

        # [中文] ### 用途: - 获取知乎推荐关注列表 ### 参数: - 无 ### 返回: - 知乎推荐关注列表  # [English] ### Purpose: - Get Zhihu Recommend Followees ### Parameters: - None ### Returns: - Zhihu Recommend Followees  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_recommend_followees_api_v1_zhihu_web_fetch_recommend_followees_get_with_http_info(async_req=True)
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
                    " to method fetch_recommend_followees_api_v1_zhihu_web_fetch_recommend_followees_get" % key
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
            '/api/v1/zhihu/web/fetch_recommend_followees', 'GET',
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

    def fetch_salt_search_v3_api_v1_zhihu_web_fetch_salt_search_v3_get(self, keyword, **kwargs):  # noqa: E501
        """获取知乎盐选内容搜索V3/Get Zhihu Salt Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎盐选内容搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页内容数量 - search_hash_id: 搜索哈希ID ### 返回: - 知乎盐选内容搜索V3  # [English] ### Purpose: - Get Zhihu Salt Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of contents per page - search_hash_id: Search Hash ID ### Returns: - Zhihu Salt Search V3  # [示例/Example] keyword = \"deepseek\" limit = \"20\" offset = \"0\" search_hash_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_salt_search_v3_api_v1_zhihu_web_fetch_salt_search_v3_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页内容数量/Number of contents per page
        :param object search_hash_id: 搜索哈希ID/Search Hash ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_salt_search_v3_api_v1_zhihu_web_fetch_salt_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_salt_search_v3_api_v1_zhihu_web_fetch_salt_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_salt_search_v3_api_v1_zhihu_web_fetch_salt_search_v3_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取知乎盐选内容搜索V3/Get Zhihu Salt Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎盐选内容搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页内容数量 - search_hash_id: 搜索哈希ID ### 返回: - 知乎盐选内容搜索V3  # [English] ### Purpose: - Get Zhihu Salt Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of contents per page - search_hash_id: Search Hash ID ### Returns: - Zhihu Salt Search V3  # [示例/Example] keyword = \"deepseek\" limit = \"20\" offset = \"0\" search_hash_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_salt_search_v3_api_v1_zhihu_web_fetch_salt_search_v3_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页内容数量/Number of contents per page
        :param object search_hash_id: 搜索哈希ID/Search Hash ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'limit', 'search_hash_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_salt_search_v3_api_v1_zhihu_web_fetch_salt_search_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_salt_search_v3_api_v1_zhihu_web_fetch_salt_search_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'search_hash_id' in params:
            query_params.append(('search_hash_id', params['search_hash_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_salt_search_v3', 'GET',
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

    def fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post(self, keyword, **kwargs):  # noqa: E501
        """获取知乎论文搜索V3/Get Zhihu Scholar Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎论文搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页论文数量 - filter_fields: 过滤字段 ### 返回: - 知乎论文搜索V3  # [English] ### Purpose: - Get Zhihu Scholar Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of papers per page - filter_fields: Filter Fields ### Returns: - Zhihu Scholar Search V3  # [示例/Example] keyword = \"人工智能\" offset = \"0\" limit = \"25\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页论文数量/Number of papers per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取知乎论文搜索V3/Get Zhihu Scholar Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎论文搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页论文数量 - filter_fields: 过滤字段 ### 返回: - 知乎论文搜索V3  # [English] ### Purpose: - Get Zhihu Scholar Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of papers per page - filter_fields: Filter Fields ### Returns: - Zhihu Scholar Search V3  # [示例/Example] keyword = \"人工智能\" offset = \"0\" limit = \"25\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页论文数量/Number of papers per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_scholar_search_v3', 'POST',
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

    def fetch_search_recommend_api_v1_zhihu_web_fetch_search_recommend_get(self, **kwargs):  # noqa: E501
        """获取知乎搜索发现/Get Zhihu Search Recommend  # noqa: E501

        # [中文] ### 用途: - 获取知乎搜索发现 ### 参数: - 无 ### 返回: - 知乎搜索发现  # [English] ### Purpose: - Get Zhihu Search Recommend ### Parameters: - None ### Returns: - Zhihu Search Recommend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_recommend_api_v1_zhihu_web_fetch_search_recommend_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_recommend_api_v1_zhihu_web_fetch_search_recommend_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_recommend_api_v1_zhihu_web_fetch_search_recommend_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_search_recommend_api_v1_zhihu_web_fetch_search_recommend_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取知乎搜索发现/Get Zhihu Search Recommend  # noqa: E501

        # [中文] ### 用途: - 获取知乎搜索发现 ### 参数: - 无 ### 返回: - 知乎搜索发现  # [English] ### Purpose: - Get Zhihu Search Recommend ### Parameters: - None ### Returns: - Zhihu Search Recommend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_recommend_api_v1_zhihu_web_fetch_search_recommend_get_with_http_info(async_req=True)
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
                    " to method fetch_search_recommend_api_v1_zhihu_web_fetch_search_recommend_get" % key
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
            '/api/v1/zhihu/web/fetch_search_recommend', 'GET',
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

    def fetch_search_suggest_api_v1_zhihu_web_fetch_search_suggest_get(self, keyword, **kwargs):  # noqa: E501
        """知乎搜索预测词/Get Zhihu Search Suggest  # noqa: E501

        # [中文] ### 用途: - 知乎搜索预测词 ### 参数: - keyword: 搜索关键词 ### 返回: - 知乎搜索预测词  # [English] ### Purpose: - Get Zhihu Search Suggest ### Parameters: - keyword: Search Keywords ### Returns: - Zhihu Search Suggest  # [示例/Example] keyword = \"deepseek\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_suggest_api_v1_zhihu_web_fetch_search_suggest_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_search_suggest_api_v1_zhihu_web_fetch_search_suggest_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_search_suggest_api_v1_zhihu_web_fetch_search_suggest_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_search_suggest_api_v1_zhihu_web_fetch_search_suggest_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """知乎搜索预测词/Get Zhihu Search Suggest  # noqa: E501

        # [中文] ### 用途: - 知乎搜索预测词 ### 参数: - keyword: 搜索关键词 ### 返回: - 知乎搜索预测词  # [English] ### Purpose: - Get Zhihu Search Suggest ### Parameters: - keyword: Search Keywords ### Returns: - Zhihu Search Suggest  # [示例/Example] keyword = \"deepseek\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_search_suggest_api_v1_zhihu_web_fetch_search_suggest_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
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
                    " to method fetch_search_suggest_api_v1_zhihu_web_fetch_search_suggest_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_search_suggest_api_v1_zhihu_web_fetch_search_suggest_get`")  # noqa: E501

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
            '/api/v1/zhihu/web/fetch_search_suggest', 'GET',
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

    def fetch_sub_comment_v5_api_v1_zhihu_web_fetch_sub_comment_v5_get(self, comment_id, **kwargs):  # noqa: E501
        """获取知乎子评论区V5/Get Zhihu Sub Comment V5  # noqa: E501

        # [中文] ### 用途: - 获取知乎子评论区V5 ### 参数: - comment_id: 评论ID - order_by: 排序     - score 最热排序     - ts 最新排序 - limit: 每页评论数量 - offset: 偏移量/页码 ### 返回: - 知乎子评论区V5  # [English] ### Purpose: - Get Zhihu Sub Comment V5 ### Parameters: - comment_id: Comment ID - order_by: Sort     - score Hottest Sort     - ts Latest Sort - limit: Number of comments per page - offset: Offset/Page Number ### Returns: - Zhihu Sub Comment V5  # [示例/Example] comment_id = \"11100789728\" order_by = \"score\" limit = \"20\" offset = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_sub_comment_v5_api_v1_zhihu_web_fetch_sub_comment_v5_get(comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object comment_id: 评论ID/Comment ID (required)
        :param object order_by: 排序/Sort
        :param object limit: 每页评论数量/Number of comments per page
        :param object offset: 偏移量/Offset
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_sub_comment_v5_api_v1_zhihu_web_fetch_sub_comment_v5_get_with_http_info(comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_sub_comment_v5_api_v1_zhihu_web_fetch_sub_comment_v5_get_with_http_info(comment_id, **kwargs)  # noqa: E501
            return data

    def fetch_sub_comment_v5_api_v1_zhihu_web_fetch_sub_comment_v5_get_with_http_info(self, comment_id, **kwargs):  # noqa: E501
        """获取知乎子评论区V5/Get Zhihu Sub Comment V5  # noqa: E501

        # [中文] ### 用途: - 获取知乎子评论区V5 ### 参数: - comment_id: 评论ID - order_by: 排序     - score 最热排序     - ts 最新排序 - limit: 每页评论数量 - offset: 偏移量/页码 ### 返回: - 知乎子评论区V5  # [English] ### Purpose: - Get Zhihu Sub Comment V5 ### Parameters: - comment_id: Comment ID - order_by: Sort     - score Hottest Sort     - ts Latest Sort - limit: Number of comments per page - offset: Offset/Page Number ### Returns: - Zhihu Sub Comment V5  # [示例/Example] comment_id = \"11100789728\" order_by = \"score\" limit = \"20\" offset = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_sub_comment_v5_api_v1_zhihu_web_fetch_sub_comment_v5_get_with_http_info(comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object comment_id: 评论ID/Comment ID (required)
        :param object order_by: 排序/Sort
        :param object limit: 每页评论数量/Number of comments per page
        :param object offset: 偏移量/Offset
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['comment_id', 'order_by', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_sub_comment_v5_api_v1_zhihu_web_fetch_sub_comment_v5_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'comment_id' is set
        if self.api_client.client_side_validation and ('comment_id' not in params or
                                                       params['comment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `comment_id` when calling `fetch_sub_comment_v5_api_v1_zhihu_web_fetch_sub_comment_v5_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'comment_id' in params:
            query_params.append(('comment_id', params['comment_id']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_sub_comment_v5', 'GET',
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

    def fetch_topic_search_v3_api_v1_zhihu_web_fetch_topic_search_v3_get(self, keyword, **kwargs):  # noqa: E501
        """获取知乎话题搜索V3/Get Zhihu Topic Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎话题搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页话题数量 ### 返回: - 知乎话题搜索V3  # [English] ### Purpose: - Get Zhihu Topic Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of topics per page ### Returns: - Zhihu Topic Search V3  # [示例/Example] keyword = \"deepseek\" offset = \"0\" limit = \"25\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_topic_search_v3_api_v1_zhihu_web_fetch_topic_search_v3_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页话题数量/Number of topics per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_topic_search_v3_api_v1_zhihu_web_fetch_topic_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_topic_search_v3_api_v1_zhihu_web_fetch_topic_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_topic_search_v3_api_v1_zhihu_web_fetch_topic_search_v3_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取知乎话题搜索V3/Get Zhihu Topic Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎话题搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页话题数量 ### 返回: - 知乎话题搜索V3  # [English] ### Purpose: - Get Zhihu Topic Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of topics per page ### Returns: - Zhihu Topic Search V3  # [示例/Example] keyword = \"deepseek\" offset = \"0\" limit = \"25\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_topic_search_v3_api_v1_zhihu_web_fetch_topic_search_v3_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页话题数量/Number of topics per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_topic_search_v3_api_v1_zhihu_web_fetch_topic_search_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_topic_search_v3_api_v1_zhihu_web_fetch_topic_search_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_topic_search_v3', 'GET',
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

    def fetch_user_follow_collections_api_v1_zhihu_web_fetch_user_follow_collections_get(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户关注的收藏/Get Zhihu User Follow Collections  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户关注的收藏 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页收藏数量 ### 返回: - 知乎用户关注的收藏  # [English] ### Purpose: - Get Zhihu User Follow Collections ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of collections per page ### Returns: - Zhihu User Follow Collections  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follow_collections_api_v1_zhihu_web_fetch_user_follow_collections_get(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页收藏数量/Number of collections per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_follow_collections_api_v1_zhihu_web_fetch_user_follow_collections_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_follow_collections_api_v1_zhihu_web_fetch_user_follow_collections_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
            return data

    def fetch_user_follow_collections_api_v1_zhihu_web_fetch_user_follow_collections_get_with_http_info(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户关注的收藏/Get Zhihu User Follow Collections  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户关注的收藏 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页收藏数量 ### 返回: - 知乎用户关注的收藏  # [English] ### Purpose: - Get Zhihu User Follow Collections ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of collections per page ### Returns: - Zhihu User Follow Collections  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follow_collections_api_v1_zhihu_web_fetch_user_follow_collections_get_with_http_info(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页收藏数量/Number of collections per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_url_token', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_follow_collections_api_v1_zhihu_web_fetch_user_follow_collections_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_url_token' is set
        if self.api_client.client_side_validation and ('user_url_token' not in params or
                                                       params['user_url_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_url_token` when calling `fetch_user_follow_collections_api_v1_zhihu_web_fetch_user_follow_collections_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_url_token' in params:
            query_params.append(('user_url_token', params['user_url_token']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_user_follow_collections', 'GET',
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

    def fetch_user_follow_columns_api_v1_zhihu_web_fetch_user_follow_columns_get(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户订阅的专栏/Get Zhihu User Columns  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户订阅的专栏 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页专栏数量 ### 返回: - 知乎用户订阅的专栏  # [English] ### Purpose: - Get Zhihu User Columns ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of columns per page ### Returns: - Zhihu User Columns  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follow_columns_api_v1_zhihu_web_fetch_user_follow_columns_get(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页专栏数量/Number of columns per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_follow_columns_api_v1_zhihu_web_fetch_user_follow_columns_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_follow_columns_api_v1_zhihu_web_fetch_user_follow_columns_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
            return data

    def fetch_user_follow_columns_api_v1_zhihu_web_fetch_user_follow_columns_get_with_http_info(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户订阅的专栏/Get Zhihu User Columns  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户订阅的专栏 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页专栏数量 ### 返回: - 知乎用户订阅的专栏  # [English] ### Purpose: - Get Zhihu User Columns ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of columns per page ### Returns: - Zhihu User Columns  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follow_columns_api_v1_zhihu_web_fetch_user_follow_columns_get_with_http_info(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页专栏数量/Number of columns per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_url_token', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_follow_columns_api_v1_zhihu_web_fetch_user_follow_columns_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_url_token' is set
        if self.api_client.client_side_validation and ('user_url_token' not in params or
                                                       params['user_url_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_url_token` when calling `fetch_user_follow_columns_api_v1_zhihu_web_fetch_user_follow_columns_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_url_token' in params:
            query_params.append(('user_url_token', params['user_url_token']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_user_follow_columns', 'GET',
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

    def fetch_user_follow_questions_api_v1_zhihu_web_fetch_user_follow_questions_get(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户关注的问题/Get Zhihu User Follow Questions  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户关注的问题 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页问题数量 ### 返回: - 知乎用户关注的问题  # [English] ### Purpose: - Get Zhihu User Follow Questions ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of questions per page ### Returns: - Zhihu User Follow Questions  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follow_questions_api_v1_zhihu_web_fetch_user_follow_questions_get(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页问题数量/Number of questions per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_follow_questions_api_v1_zhihu_web_fetch_user_follow_questions_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_follow_questions_api_v1_zhihu_web_fetch_user_follow_questions_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
            return data

    def fetch_user_follow_questions_api_v1_zhihu_web_fetch_user_follow_questions_get_with_http_info(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户关注的问题/Get Zhihu User Follow Questions  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户关注的问题 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页问题数量 ### 返回: - 知乎用户关注的问题  # [English] ### Purpose: - Get Zhihu User Follow Questions ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of questions per page ### Returns: - Zhihu User Follow Questions  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follow_questions_api_v1_zhihu_web_fetch_user_follow_questions_get_with_http_info(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页问题数量/Number of questions per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_url_token', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_follow_questions_api_v1_zhihu_web_fetch_user_follow_questions_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_url_token' is set
        if self.api_client.client_side_validation and ('user_url_token' not in params or
                                                       params['user_url_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_url_token` when calling `fetch_user_follow_questions_api_v1_zhihu_web_fetch_user_follow_questions_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_url_token' in params:
            query_params.append(('user_url_token', params['user_url_token']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_user_follow_questions', 'GET',
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

    def fetch_user_follow_topics_api_v1_zhihu_web_fetch_user_follow_topics_get(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户关注的话题/Get Zhihu User Follow Topics  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户关注的话题 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页话题数量 ### 返回: - 知乎用户关注的话题  # [English] ### Purpose: - Get Zhihu User Follow Topics ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of topics per page ### Returns: - Zhihu User Follow Topics  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follow_topics_api_v1_zhihu_web_fetch_user_follow_topics_get(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页话题数量/Number of topics per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_follow_topics_api_v1_zhihu_web_fetch_user_follow_topics_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_follow_topics_api_v1_zhihu_web_fetch_user_follow_topics_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
            return data

    def fetch_user_follow_topics_api_v1_zhihu_web_fetch_user_follow_topics_get_with_http_info(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户关注的话题/Get Zhihu User Follow Topics  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户关注的话题 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页话题数量 ### 返回: - 知乎用户关注的话题  # [English] ### Purpose: - Get Zhihu User Follow Topics ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of topics per page ### Returns: - Zhihu User Follow Topics  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_follow_topics_api_v1_zhihu_web_fetch_user_follow_topics_get_with_http_info(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页话题数量/Number of topics per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_url_token', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_follow_topics_api_v1_zhihu_web_fetch_user_follow_topics_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_url_token' is set
        if self.api_client.client_side_validation and ('user_url_token' not in params or
                                                       params['user_url_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_url_token` when calling `fetch_user_follow_topics_api_v1_zhihu_web_fetch_user_follow_topics_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_url_token' in params:
            query_params.append(('user_url_token', params['user_url_token']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_user_follow_topics', 'GET',
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

    def fetch_user_followees_api_v1_zhihu_web_fetch_user_followees_get(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户关注列表/Get Zhihu User Following  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户关注列表 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页用户数量 ### 返回: - 知乎用户关注列表  # [English] ### Purpose: - Get Zhihu User Following ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of users per page ### Returns: - Zhihu User Following  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_followees_api_v1_zhihu_web_fetch_user_followees_get(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页用户数量/Number of users per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_followees_api_v1_zhihu_web_fetch_user_followees_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_followees_api_v1_zhihu_web_fetch_user_followees_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
            return data

    def fetch_user_followees_api_v1_zhihu_web_fetch_user_followees_get_with_http_info(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户关注列表/Get Zhihu User Following  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户关注列表 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页用户数量 ### 返回: - 知乎用户关注列表  # [English] ### Purpose: - Get Zhihu User Following ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of users per page ### Returns: - Zhihu User Following  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_followees_api_v1_zhihu_web_fetch_user_followees_get_with_http_info(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页用户数量/Number of users per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_url_token', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_followees_api_v1_zhihu_web_fetch_user_followees_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_url_token' is set
        if self.api_client.client_side_validation and ('user_url_token' not in params or
                                                       params['user_url_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_url_token` when calling `fetch_user_followees_api_v1_zhihu_web_fetch_user_followees_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_url_token' in params:
            query_params.append(('user_url_token', params['user_url_token']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_user_followees', 'GET',
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

    def fetch_user_followers_api_v1_zhihu_web_fetch_user_followers_get(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户粉丝列表/Get Zhihu User Followers  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户粉丝列表 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页用户数量 ### 返回: - 知乎用户粉丝列表  # [English] ### Purpose: - Get Zhihu User Followers ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of users per page ### Returns: - Zhihu User Followers  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_followers_api_v1_zhihu_web_fetch_user_followers_get(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页用户数量/Number of users per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_followers_api_v1_zhihu_web_fetch_user_followers_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_followers_api_v1_zhihu_web_fetch_user_followers_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
            return data

    def fetch_user_followers_api_v1_zhihu_web_fetch_user_followers_get_with_http_info(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户粉丝列表/Get Zhihu User Followers  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户粉丝列表 ### 参数: - user_url_token: 用户ID - offset: 偏移量 - limit: 每页用户数量 ### 返回: - 知乎用户粉丝列表  # [English] ### Purpose: - Get Zhihu User Followers ### Parameters: - user_url_token: User ID - offset: Offset - limit: Number of users per page ### Returns: - Zhihu User Followers  # [示例/Example] user_url_token = \"ming-he-43-93\" offset = \"0\" limit = \"20\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_followers_api_v1_zhihu_web_fetch_user_followers_get_with_http_info(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页用户数量/Number of users per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_url_token', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_followers_api_v1_zhihu_web_fetch_user_followers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_url_token' is set
        if self.api_client.client_side_validation and ('user_url_token' not in params or
                                                       params['user_url_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_url_token` when calling `fetch_user_followers_api_v1_zhihu_web_fetch_user_followers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_url_token' in params:
            query_params.append(('user_url_token', params['user_url_token']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_user_followers', 'GET',
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

    def fetch_user_info_api_v1_zhihu_web_fetch_user_info_get(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户信息/Get Zhihu User Info  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户信息 ### 参数: - user_url_token: 用户ID ### 返回: - 知乎用户信息  # [English] ### Purpose: - Get Zhihu User Info ### Parameters: - user_url_token: User ID ### Returns: - Zhihu User Info  # [示例/Example] user_url_token = \"ming-he-43-93\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_zhihu_web_fetch_user_info_get(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_info_api_v1_zhihu_web_fetch_user_info_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_info_api_v1_zhihu_web_fetch_user_info_get_with_http_info(user_url_token, **kwargs)  # noqa: E501
            return data

    def fetch_user_info_api_v1_zhihu_web_fetch_user_info_get_with_http_info(self, user_url_token, **kwargs):  # noqa: E501
        """获取知乎用户信息/Get Zhihu User Info  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户信息 ### 参数: - user_url_token: 用户ID ### 返回: - 知乎用户信息  # [English] ### Purpose: - Get Zhihu User Info ### Parameters: - user_url_token: User ID ### Returns: - Zhihu User Info  # [示例/Example] user_url_token = \"ming-he-43-93\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_info_api_v1_zhihu_web_fetch_user_info_get_with_http_info(user_url_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object user_url_token: 用户ID/User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_url_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_info_api_v1_zhihu_web_fetch_user_info_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_url_token' is set
        if self.api_client.client_side_validation and ('user_url_token' not in params or
                                                       params['user_url_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_url_token` when calling `fetch_user_info_api_v1_zhihu_web_fetch_user_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_url_token' in params:
            query_params.append(('user_url_token', params['user_url_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_user_info', 'GET',
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

    def fetch_user_search_v3_api_v1_zhihu_web_fetch_user_search_v3_get(self, keyword, **kwargs):  # noqa: E501
        """获取知乎用户搜索V3/Get Zhihu User Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页用户数量 ### 返回: - 知乎用户搜索V3  # [English] ### Purpose: - Get Zhihu User Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of users per page ### Returns: - Zhihu User Search V3  # [示例/Example] keyword = \"deepseek\" offset = \"0\" limit = \"25\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_v3_api_v1_zhihu_web_fetch_user_search_v3_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页用户数量/Number of users per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_user_search_v3_api_v1_zhihu_web_fetch_user_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_user_search_v3_api_v1_zhihu_web_fetch_user_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_user_search_v3_api_v1_zhihu_web_fetch_user_search_v3_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取知乎用户搜索V3/Get Zhihu User Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎用户搜索V3 ### 参数: - keyword: 搜索关键词 - offset: 偏移量 - limit: 每页用户数量 ### 返回: - 知乎用户搜索V3  # [English] ### Purpose: - Get Zhihu User Search V3 ### Parameters: - keyword: Search Keywords - offset: Offset - limit: Number of users per page ### Returns: - Zhihu User Search V3  # [示例/Example] keyword = \"deepseek\" offset = \"0\" limit = \"25\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_user_search_v3_api_v1_zhihu_web_fetch_user_search_v3_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object offset: 偏移量/Offset
        :param object limit: 每页用户数量/Number of users per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_user_search_v3_api_v1_zhihu_web_fetch_user_search_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_user_search_v3_api_v1_zhihu_web_fetch_user_search_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_user_search_v3', 'GET',
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

    def fetch_video_list_api_v1_zhihu_web_fetch_video_list_get(self, **kwargs):  # noqa: E501
        """获取知乎首页视频榜/Get Zhihu Video List  # noqa: E501

        # [中文] ### 用途: - 获取知乎首页视频榜 ### 参数: - offset: 偏移量 - limit: 每页视频数量 ### 返回: - 知乎首页视频榜  # [English] ### Purpose: - Get Zhihu Video List ### Parameters: - offset: Offset - limit: Number of videos per page ### Returns: - Zhihu Video List  # [示例/Example] offset = \"\" limit = \"12\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_list_api_v1_zhihu_web_fetch_video_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object offset: 偏移量/Offset
        :param object limit: 每页视频数量/Number of videos per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_list_api_v1_zhihu_web_fetch_video_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_list_api_v1_zhihu_web_fetch_video_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_video_list_api_v1_zhihu_web_fetch_video_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """获取知乎首页视频榜/Get Zhihu Video List  # noqa: E501

        # [中文] ### 用途: - 获取知乎首页视频榜 ### 参数: - offset: 偏移量 - limit: 每页视频数量 ### 返回: - 知乎首页视频榜  # [English] ### Purpose: - Get Zhihu Video List ### Parameters: - offset: Offset - limit: Number of videos per page ### Returns: - Zhihu Video List  # [示例/Example] offset = \"\" limit = \"12\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_list_api_v1_zhihu_web_fetch_video_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object offset: 偏移量/Offset
        :param object limit: 每页视频数量/Number of videos per page
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_list_api_v1_zhihu_web_fetch_video_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_video_list', 'GET',
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

    def fetch_video_search_v3_api_v1_zhihu_web_fetch_video_search_v3_get(self, keyword, **kwargs):  # noqa: E501
        """获取知乎视频搜索V3/Get Zhihu Video Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎视频搜索V3 ### 参数: - keyword: 搜索关键词 - limit: 每页视频数量 - offset: 偏移量 - search_hash_id: 搜索哈希ID ### 返回: - 知乎视频搜索V3  # [English] ### Purpose: - Get Zhihu Video Search V3 ### Parameters: - keyword: Search Keywords - limit: Number of videos per page - offset: Offset - search_hash_id: Search Hash ID ### Returns: - Zhihu Video Search V3  # [示例/Example] keyword = \"deepseek\" limit = \"20\" offset = \"0\" search_hash_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_v3_api_v1_zhihu_web_fetch_video_search_v3_get(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object limit: 每页视频数量/Number of videos per page
        :param object offset: 偏移量/Offset
        :param object search_hash_id: 搜索哈希ID/Search Hash ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_video_search_v3_api_v1_zhihu_web_fetch_video_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_video_search_v3_api_v1_zhihu_web_fetch_video_search_v3_get_with_http_info(keyword, **kwargs)  # noqa: E501
            return data

    def fetch_video_search_v3_api_v1_zhihu_web_fetch_video_search_v3_get_with_http_info(self, keyword, **kwargs):  # noqa: E501
        """获取知乎视频搜索V3/Get Zhihu Video Search V3  # noqa: E501

        # [中文] ### 用途: - 获取知乎视频搜索V3 ### 参数: - keyword: 搜索关键词 - limit: 每页视频数量 - offset: 偏移量 - search_hash_id: 搜索哈希ID ### 返回: - 知乎视频搜索V3  # [English] ### Purpose: - Get Zhihu Video Search V3 ### Parameters: - keyword: Search Keywords - limit: Number of videos per page - offset: Offset - search_hash_id: Search Hash ID ### Returns: - Zhihu Video Search V3  # [示例/Example] keyword = \"deepseek\" limit = \"20\" offset = \"0\" search_hash_id = \"\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_video_search_v3_api_v1_zhihu_web_fetch_video_search_v3_get_with_http_info(keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object keyword: 搜索关键词/Search Keywords (required)
        :param object limit: 每页视频数量/Number of videos per page
        :param object offset: 偏移量/Offset
        :param object search_hash_id: 搜索哈希ID/Search Hash ID
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'limit', 'offset', 'search_hash_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_video_search_v3_api_v1_zhihu_web_fetch_video_search_v3_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if self.api_client.client_side_validation and ('keyword' not in params or
                                                       params['keyword'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `keyword` when calling `fetch_video_search_v3_api_v1_zhihu_web_fetch_video_search_v3_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'search_hash_id' in params:
            query_params.append(('search_hash_id', params['search_hash_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/zhihu/web/fetch_video_search_v3', 'GET',
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
