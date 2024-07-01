# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

import os

from ._streaming import AsyncStream as AsyncStream, Stream as Stream

from typing_extensions import override, Self

from typing import Any

from ._exceptions import APIStatusError

from ._utils import get_async_library

from . import _exceptions

import os
import asyncio
import warnings
from typing import Optional, Union, Dict, Any, Mapping, overload, cast
from typing_extensions import Literal

import httpx

from ._version import __version__
from ._qs import Querystring
from .types import shared_params
from ._utils import (
    extract_files,
    maybe_transform,
    required_args,
    deepcopy_minimal,
    maybe_coerce_integer,
    maybe_coerce_float,
    maybe_coerce_boolean,
    is_given,
)
from ._types import (
    Omit,
    NotGiven,
    Timeout,
    Transport,
    ProxiesTypes,
    RequestOptions,
    Headers,
    NoneType,
    Query,
    Body,
    NOT_GIVEN,
)
from ._base_client import (
    DEFAULT_CONNECTION_LIMITS,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    ResponseT,
    SyncHttpxClientWrapper,
    AsyncHttpxClientWrapper,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from . import resources

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "N8n",
    "AsyncN8n",
    "Client",
    "AsyncClient",
]


class N8n(SyncAPIClient):
    audits: resources.AuditsResource
    credentials: resources.CredentialsResource
    executions: resources.ExecutionsResource
    tags: resources.TagsResource
    workflows: resources.WorkflowsResource
    users: resources.UsersResource
    source_control: resources.SourceControlResource
    with_raw_response: N8nWithRawResponse
    with_streaming_response: N8nWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous n8n client instance."""
        if base_url is None:
            base_url = os.environ.get("N8N_BASE_URL")
        if base_url is None:
            base_url = f"/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.audits = resources.AuditsResource(self)
        self.credentials = resources.CredentialsResource(self)
        self.executions = resources.ExecutionsResource(self)
        self.tags = resources.TagsResource(self)
        self.workflows = resources.WorkflowsResource(self)
        self.users = resources.UsersResource(self)
        self.source_control = resources.SourceControlResource(self)
        self.with_raw_response = N8nWithRawResponse(self)
        self.with_streaming_response = N8nWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncN8n(AsyncAPIClient):
    audits: resources.AsyncAuditsResource
    credentials: resources.AsyncCredentialsResource
    executions: resources.AsyncExecutionsResource
    tags: resources.AsyncTagsResource
    workflows: resources.AsyncWorkflowsResource
    users: resources.AsyncUsersResource
    source_control: resources.AsyncSourceControlResource
    with_raw_response: AsyncN8nWithRawResponse
    with_streaming_response: AsyncN8nWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async n8n client instance."""
        if base_url is None:
            base_url = os.environ.get("N8N_BASE_URL")
        if base_url is None:
            base_url = f"/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.audits = resources.AsyncAuditsResource(self)
        self.credentials = resources.AsyncCredentialsResource(self)
        self.executions = resources.AsyncExecutionsResource(self)
        self.tags = resources.AsyncTagsResource(self)
        self.workflows = resources.AsyncWorkflowsResource(self)
        self.users = resources.AsyncUsersResource(self)
        self.source_control = resources.AsyncSourceControlResource(self)
        self.with_raw_response = AsyncN8nWithRawResponse(self)
        self.with_streaming_response = AsyncN8nWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class N8nWithRawResponse:
    def __init__(self, client: N8n) -> None:
        self.audits = resources.AuditsResourceWithRawResponse(client.audits)
        self.credentials = resources.CredentialsResourceWithRawResponse(client.credentials)
        self.executions = resources.ExecutionsResourceWithRawResponse(client.executions)
        self.tags = resources.TagsResourceWithRawResponse(client.tags)
        self.workflows = resources.WorkflowsResourceWithRawResponse(client.workflows)
        self.users = resources.UsersResourceWithRawResponse(client.users)
        self.source_control = resources.SourceControlResourceWithRawResponse(client.source_control)


class AsyncN8nWithRawResponse:
    def __init__(self, client: AsyncN8n) -> None:
        self.audits = resources.AsyncAuditsResourceWithRawResponse(client.audits)
        self.credentials = resources.AsyncCredentialsResourceWithRawResponse(client.credentials)
        self.executions = resources.AsyncExecutionsResourceWithRawResponse(client.executions)
        self.tags = resources.AsyncTagsResourceWithRawResponse(client.tags)
        self.workflows = resources.AsyncWorkflowsResourceWithRawResponse(client.workflows)
        self.users = resources.AsyncUsersResourceWithRawResponse(client.users)
        self.source_control = resources.AsyncSourceControlResourceWithRawResponse(client.source_control)


class N8nWithStreamedResponse:
    def __init__(self, client: N8n) -> None:
        self.audits = resources.AuditsResourceWithStreamingResponse(client.audits)
        self.credentials = resources.CredentialsResourceWithStreamingResponse(client.credentials)
        self.executions = resources.ExecutionsResourceWithStreamingResponse(client.executions)
        self.tags = resources.TagsResourceWithStreamingResponse(client.tags)
        self.workflows = resources.WorkflowsResourceWithStreamingResponse(client.workflows)
        self.users = resources.UsersResourceWithStreamingResponse(client.users)
        self.source_control = resources.SourceControlResourceWithStreamingResponse(client.source_control)


class AsyncN8nWithStreamedResponse:
    def __init__(self, client: AsyncN8n) -> None:
        self.audits = resources.AsyncAuditsResourceWithStreamingResponse(client.audits)
        self.credentials = resources.AsyncCredentialsResourceWithStreamingResponse(client.credentials)
        self.executions = resources.AsyncExecutionsResourceWithStreamingResponse(client.executions)
        self.tags = resources.AsyncTagsResourceWithStreamingResponse(client.tags)
        self.workflows = resources.AsyncWorkflowsResourceWithStreamingResponse(client.workflows)
        self.users = resources.AsyncUsersResourceWithStreamingResponse(client.users)
        self.source_control = resources.AsyncSourceControlResourceWithStreamingResponse(client.source_control)


Client = N8n

AsyncClient = AsyncN8n
