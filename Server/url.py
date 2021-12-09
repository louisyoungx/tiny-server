from Server.api import serverLog, serverConfig, signIn

URL_TABLE = {
    "/log": serverLog,
    "/config": serverConfig,
    "/sign-in": signIn,
}
