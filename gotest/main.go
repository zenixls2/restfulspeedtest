package main

import (
	fasthttprouter "github.com/buaazp/fasthttprouter"
	"github.com/valyala/fasthttp"
)

func Hello(ctx *fasthttp.RequestCtx) {
	ctx.WriteString("Hello")
}

func main() {
	router := fasthttprouter.New()
	router.GET("/", Hello)
	fasthttp.ListenAndServe(":8080", router.Handler)
}
