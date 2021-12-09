# Turbon

**Turbon** 本地Python项目运行基础框架，无需安装第三方库，
内置纯Python原生实现的多进程http服务器，可通过内置restful web api或网页查看本地日志，可自定义web模版,
可定时执行代码，可动态加载依赖包，可进行消息通知，可定义服务器api查看运行状态，可进行持久化存储，有完善的日志与配置系统。

## 主要功能
- 配置模块
  - 通过yaml文件配置
  - 通过`config.Module.item`即可取出配置数据
- 日志模块
  - 日志大小，文件个数等详细配置
  - 时间，函数，日志类型等详细输出信息
  - 命令行彩色输出
  - 可以对服务器日志开关进行控制
  - 可调用内置进度条
- 定时执行模块
  - 通过配置开关模块
  - 根据开始结束时间，定期执行核心代码
  - 可自动跳过周末
  - 可配置多个执行时间
- 消息通知模块
  - 通过配置开关模块
  - 发送邮件
  - 配合`mirai`框架发送QQ信息
- 服务器模块
  - 内置静态文件服务器
  - 可自定义API与url
  - API支持`GET`与`POST`方法
  - 可通过内置API查询程序日志与配置
- 状态持久化模块
  - 响应式对象持久化
  - 对需要持久化的数据进行实时存储
  - 一键调用模块
- 依赖管理模块
  - 可动态加载依赖包
  - 缺失依赖包可自动下载

## 模块功能

- `Config`
  - `config.yaml` - 配置信息
  - `config` - 对config.ini中数据进行读取与初始化
  - `direct` - 字典转对象，通过点直接访问配置属性
- `Core`
  - `core` - 程序执行的入口
- `Depend`
  - `load_depend` - 导入依赖
  - `import_lib` - 动态加载依赖
- `Logger`
  - `Log_Files` - 存储日志文件
  - `logger` - 日志模块
  - `progress` - 进度条模块
- `Message`
  - `message` - 消息传递接口，可通过QQ机器人与邮箱发送信息
- `Scheduler`
  - `scheduler` - 批量执行任务模块
  - `task` - 单任务定时执行模块
- `Server`
  - `api` - 自定义api
  - `handler` - 包含主要的HTTP请求处理
  - `router` - api路由函数
  - `server` - 用于配置并启动服务器线程
  - `url` - 用于路由配置
- `Static`
  - 静态文件存放目录
- `Storage`
  - `storage` - 数据持久化存储
  - `reactive` - 实现数据响应式
- `TEST`
  - 一些测试文件
- `runserver`
  - `Turbon`启动入口

## 安装教程

拉取仓库到本地
```shell
git clone https://github.com/louisyoungx/turbon.git
```

进入项目目录
```shell
cd turbon
```

修改配置 - `/Config/config.yaml`

修改主函数中代码 - `/Core/core.py`

通过如下命令运行`Turbon`
```shell
python3 runserver
```

> Windows系统下通过
> ```python
> py runserver # 或者 python runserver
> ```