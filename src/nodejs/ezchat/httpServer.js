// 引入核心模块
var ezHttpPort = 8886
var http = require('http')

// 创建服务器(API返回的是一个实例)
var server = http.createServer()

// 绑定端口号(3000)
server.listen(ezHttpPort, () => {
    console.log(`服务器启动成功,等待客户端请求...`)
})

// 监听客户端发起的请求
server.on('request', (request, response) => {
    
    // 客户端请求路径
    console.log(`客户端请求路径为：${request.url}`)

    // 响应给客户端
    switch(request.url){
        
        case '/': {//浏览器默认行为
            response.write(`/`)
            break;
        }

        case '/index': {//首页
            response.write(`/index`)
            break;
        }

        case '/loging': {//登录页
            response.write(`/loging`)
            break;
        }
        case '/yw': {//登录页
            response.write(`hello yw server.`)
            break;
        }
        
    }

    // 响应完成
    response.end()
    
})

