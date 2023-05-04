# HelloFlask

HelloFlask 的 Meta 仓库，包含 HelloFlask 相关文档和示例程序。


## Links

- 文档：<https://docs.helloflask.com>
- 主站：<https://helloflask.com>
- 论坛：<https://discuss.helloflask.com>


## Books

- Flask Web 开发实战：<https://helloflask.com/book/1>
- Python Web API 设计与开发：<https://helloflask.com/book/2>
- Flask 入门教程：<https://helloflask.com/book/3>
- Flask Web 开发实战（第 2 版）：<https://helloflask.com/book/4>


## Feedbacks

- 勘误和建议：创建 [issue](https://github.com/greyli/helloflask/issues) 或发送邮件到 withlihui@gmail.com
- 问题求助 & 讨论：在[论坛](https://discuss.helloflask.com)、[GitHub Discussion](https://github.com/greyli/helloflask/discussions) 或[群聊](https://helloflask.com#discuss)创建讨论


## Docs

一些快速链接：

- [《Flask Web 开发实战》示例程序索引](https://docs.helloflask.com/examples/)
- [《Flask Web 开发实战》勘误](https://docs.helloflask.com/book/1/errata/)
- [《Flask Web 开发实战（第 2 版）》代码片段](https://docs.helloflask.com/book/4/snippets/)

## 笔记
- 如果程序主模块是其他名称 比如hello.py那么需要设置环境变量FLASK_APP，将包含程序实例的模块名赋值给
这个变量set FLASK_APP=hello
- app.config['ADMIN_NAME'] = 'Peter' 配置的名称必须是全大写形式，小写的变量将不会被读取
- url_for url_for()函数接收两个及以上的参数，他接收函数名作为第一个参数， 接收对应URL规则的命名参数，如果还出现其他的参数，则会添加到URL的后面作为查询参数
- url_for('static1', filename='favicon.ico') 访问静态文件
- urlparse 将url解析为6部分：ParseResult(scheme='http', netloc='127.0.0.1:5000', path='/', params='', query='', fragment='')
- 当我们调用render_template（）函数渲染任意一个模板时，所有使用app.context_processor装饰器注册的模板上下文处理函数（包括Flask内置的上下文处理函数）都会被执行，这些函数的返回值会被添加到模板中，因此我们可以在模板中直接使用foo变量
- 