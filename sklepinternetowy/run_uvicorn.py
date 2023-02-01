import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "SklepInternetowy.asgi:application", 
        host="0.0.0.0",
        port=8080, 
        log_level="debug",
        reload=True, 
        ssl_keyfile="/etc/letsencrypt/live/sklep-internetowy.morskyi.dev/privkey.pem",
        ssl_certfile="/etc/letsencrypt/live/sklep-internetowy.morskyi.dev/fullchain.pem"
        )
