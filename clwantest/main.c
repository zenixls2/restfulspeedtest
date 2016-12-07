#include "lwan.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static lwan_http_status_t
hello_world(lwan_request_t *request,
            lwan_response_t *response, void *data)
{
    static const char message[] = "Hello";

    response->mime_type = "text/plain";
    /*const char *name = lwan_request_get_query_param(request, "name");
    static lwan_key_value_t headers[] = {
        { .key = "Test", .value = "xddd" },
        { NULL, NULL}
    };
    if (name) {
        headers[0].value = (char*)name;
    }
    response->headers = headers;*/
    strbuf_set_static(response->buffer, message, sizeof(message) - 1);

    return HTTP_OK;
}

static void
lwan_module_shutdown(lwan_t *l)
{
    hash_free(l->module_registry);
}

void
custom_shutdown(lwan_t *l)
{
    extern void lwan_job_thread_shutdown(void);
    extern void lwan_thread_shutdown(void);
    extern void lwan_response_shutdown(lwan_t *l);
    extern void lwan_tables_shutdown(void);
    extern void lwan_status_shutdown(lwan_t *l);
    extern void lwan_http_authorize_shutdown(void);
    extern void lwan_module_shutdown(lwan_t *l);
    lwan_job_thread_shutdown();
    lwan_thread_shutdown();
    free(l->config.error_template);
    free(l->config.config_file_path);
    free(l->conns);
    lwan_response_shutdown(l);
    lwan_tables_shutdown();
    lwan_status_shutdown(l);
    lwan_http_authorize_shutdown();
    lwan_module_shutdown(l);
}

int
main(void)
{
    const lwan_url_map_t default_map[] = {
        { .prefix = "/", .handler = hello_world },
        { .prefix = NULL }
    };
    lwan_t l;
    static const lwan_config_t config = {
        .listener = "0.0.0.0:8080",
        .keep_alive_timeout = 15,
        .quiet = false,
        .reuse_port = true,
        .proxy_protocol = false,
        .expires = 1 * ONE_WEEK,
        .n_threads = 0,
        .max_post_data_size = 10 * DEFAULT_BUFFER_SIZE
    };

    lwan_init_with_config(&l, &config);

    lwan_set_url_map(&l, default_map);
    lwan_main_loop(&l);

    custom_shutdown(&l);

    return 0;
}
