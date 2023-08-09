# LightNovelReaderBackground
 项目 [LightNovelReader](https://github.com/dmzz-yyhyy/LightNovelReader) 的服务端, 利用爬虫整合数据后返回至客户端
 使用Python编写, 后期会视情况改为Java编写
 主要使用FastAPI
# 进度
 - [x] 获取书本API
 - [x] 获取章节API
 - [x] 搜索书本API
 - [x] 获取书本各项信息API
 - [x] 数据缓存
 - [ ] 缓存优化
# 未来
- [ ] 用户数据库
- [ ] 用户数据云端同步
# 爬虫
 目前计划爬取网站 [轻小说文库](https://www.wenku8.net/index.php) 的内容(如网站管理员有意见可以联系我, 我会立刻换源)
 使用cloudflare-scrape库绕过CloudFlare获取数据
