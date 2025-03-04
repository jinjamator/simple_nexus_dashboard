import logging

from .decorators import handle_async_request_error, handle_request_error
from .models import Response
import json

logger = logging.getLogger(__name__)


@handle_request_error
def make_request(client, request):
    logger.debug("operation=request_started, request=%r", request)
    method = request.method
    client_method = getattr(client, method.lower())
    client_options = {
        "params": request.params,
        "headers": request.headers,
        "timeout": request.timeout,
        # "verify": request.ssl_verify,
        **request.kwargs,
    }
    if method.lower() in ("post", "put", "patch"):
        if request.headers.get("content-type") == "application/json":
            client_options["json"] = request.body
        else:
            client_options["data"] = request.body
    client_response = client_method(request.url, **client_options)
    content_type = client_response.headers.get(
        "content-type", client_response.headers.get("Content-Type", "")
    )
    if "text" in content_type:
        body = client_response.text
    elif "json" in content_type:
        if client_response.text:
            try:
                body = client_response.json()["response"]
            except KeyError:
                body = client_response.json()
    else:
        body = client_response.content

    response = Response(
        url=str(client_response.url),
        method=method,
        body=body,
        headers=client_response.headers,
        status_code=client_response.status_code,
        client_response=client_response,
    )
    logger.debug(
        "operation=request_finished, request=%r, response=%r", request, response
    )
    return response


@handle_async_request_error
async def make_async_request(client, request):
    logger.debug("operation=request_started, request=%r", request)
    method = request.method
    client_method = getattr(client, method.lower())
    client_options = {
        "params": request.params,
        "headers": request.headers,
        "timeout": request.timeout,
        "verify": request.ssl_verify,
        **request.kwargs,
    }
    if method.lower() in ("post", "put", "patch"):
        if request.headers.get("content-type") == "application/json":
            client_options["json"] = request.body
        else:
            client_options["data"] = request.body
    client_response = await client_method(request.url, **client_options)
    content_type = client_response.headers.get("content-type", "")

    if "text" in content_type:
        body = client_response.text
    elif "json" in content_type:
        body = client_response.text
        if body:
            body = client_response.json()
    else:
        body = client_response.content

    response = Response(
        url=str(client_response.url),
        method=method,
        body=body,
        headers=client_response.headers,
        status_code=client_response.status_code,
        client_response=client_response,
    )
    logger.debug(
        "operation=request_finished, request=%r, response=%r", request, response
    )
    return response
