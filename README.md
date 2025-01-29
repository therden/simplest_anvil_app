# Simplest Anvil App

This app was built to test installation of [Anvil Runtime Server](https://github.com/anvil-works/anvil-runtime).

It doesn't use forms, data tables, or any add-in services (email, users, etc.)

It contains what I believe to be the minimum files and structure necessary for an app.  

The server code simply supports a couple of routes, all of which return plain text responses.

0.  Install the Anvil runtime (see link above)...
1.  Clone this app to a subdirectory of the one where you've installed the runtime server
2.  Start the server with the default settings (`anvil-app-server --app simplest_anvil_app`)
3.  From the same computer that the server's running on, use `curl` or a browser to hit `http://localhost:3030`.

This should produce the following output:

```
Anvil Runtime Server 'Simplest App' is working...

Try the following routes:
    /ping
    /hello
    /hello/{your name here}
```
