# Turbon

**Turbon** native Python project powerful framework , 
no need to install third-party libraries
built-in pure Python native implementation of multi-process http server , 
built-in restful web api and web pages to view local logs , custom web templates ,
can be timed to execute code , can dynamically load dependency packages ,
can be message notification ,
can define the server api to view the running state , 
can be persistent storage , there is a perfect logging and configuration system .

## Main Functions
- Configuration module
  - Configuration via yaml file
  - Configuration data can be retrieved via `config.Module.item`.
- Logging module
  - Detailed configuration of log size, number of files, etc.
  - Detailed output information such as time, function, log type, etc.
  - Command line color output
  - Control of server logging switches
  - Built-in progress bar can be invoked
- Timed execution module
  - By configuring the switch module
  - Periodic execution of core code based on start and end times
  - Automatic skipping of weekends
  - Multiple execution times can be configured
- Message notification module
  - Configurable switch module
  - Sending emails
  - Sending QQ messages with `mirai` framework
- Server module
  - Built-in static file server
  - Customizable API and url
  - API support `GET` and `POST` methods
  - Built-in API to query the program logs and configuration
- State persistence module
  - Responsive object persistence
  - Real-time storage of data that needs to be persisted
  - One-click call module
- Dependency management module
  - Dynamic loading of dependency packages
  - Automatic download of missing dependency packages

## Module Functions

- `Config`
  - `config.yaml` - configuration information
  - `config` - read and initialize data in config.ini
  - `direct` - dictionary to object, direct access to configuration properties via point
- `Core`
  - `core` - entry point for program execution
- `Depend`
  - `load_depend` - importing dependencies
  - `import_lib` - dynamic loading of dependencies
- `Logger`
  - `Log_Files` - store log files
  - `logger` - logging module
  - `progress` - progress bar module
- `Message`
  - `message` - messaging interface for sending messages through QQ bots and mailboxes
- `Scheduler`
  - `scheduler` - Batch execution task module
  - `task` - single-task timing module
- `Server`
  - `api` - custom api
  - `handler` - contains the main HTTP request handling
  - `router` - api routing functions
  - `server` - used to configure and start server threads
  - `url` - used for routing configuration
- `Static`
  - Static file storage directory
- `Storage`
  - `storage` - persistent data storage
  - `reactive` - implements data responsive
- `TEST`
  - Some test files
- `runserver`
  - `Turbon` startup portal

## Installation Tutorial

Pull the repository locally
```shell
git clone https://github.com/louisyoungx/turbon.git
```

Go to the project directory
```shell
cd turbon
```

Modify the configuration - `/Config/config.yaml`

Modify the code in the main function - ``/Core/core.py``

Run `Turbon` with the following command
```shell
python3 runserver
```

> Windows via
> ``python
> py runserver # or python runserver
> ```