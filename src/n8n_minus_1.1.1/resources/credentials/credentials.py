# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .schema import SchemaResource, AsyncSchemaResource

from ..._compat import cached_property

from ...types.credential import Credential

from ..._utils import maybe_transform, async_maybe_transform

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types import credential_create_params
from .schema import (
    SchemaResource,
    AsyncSchemaResource,
    SchemaResourceWithRawResponse,
    AsyncSchemaResourceWithRawResponse,
    SchemaResourceWithStreamingResponse,
    AsyncSchemaResourceWithStreamingResponse,
)

__all__ = ["CredentialsResource", "AsyncCredentialsResource"]


class CredentialsResource(SyncAPIResource):
    @cached_property
    def schema(self) -> SchemaResource:
        return SchemaResource(self._client)

    @cached_property
    def with_raw_response(self) -> CredentialsResourceWithRawResponse:
        return CredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CredentialsResourceWithStreamingResponse:
        return CredentialsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        data: object,
        name: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """
        Creates a credential that can be used by nodes of the specified type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/credentials",
            body=maybe_transform(
                {
                    "data": data,
                    "name": name,
                    "type": type,
                },
                credential_create_params.CredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Credential,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """Deletes a credential from your instance.

        You must be the owner of the
        credentials

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/credentials/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Credential,
        )


class AsyncCredentialsResource(AsyncAPIResource):
    @cached_property
    def schema(self) -> AsyncSchemaResource:
        return AsyncSchemaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCredentialsResourceWithRawResponse:
        return AsyncCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCredentialsResourceWithStreamingResponse:
        return AsyncCredentialsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        data: object,
        name: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """
        Creates a credential that can be used by nodes of the specified type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/credentials",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "name": name,
                    "type": type,
                },
                credential_create_params.CredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Credential,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """Deletes a credential from your instance.

        You must be the owner of the
        credentials

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/credentials/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Credential,
        )


class CredentialsResourceWithRawResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.create = to_raw_response_wrapper(
            credentials.create,
        )
        self.delete = to_raw_response_wrapper(
            credentials.delete,
        )

    @cached_property
    def schema(self) -> SchemaResourceWithRawResponse:
        return SchemaResourceWithRawResponse(self._credentials.schema)


class AsyncCredentialsResourceWithRawResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.create = async_to_raw_response_wrapper(
            credentials.create,
        )
        self.delete = async_to_raw_response_wrapper(
            credentials.delete,
        )

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithRawResponse:
        return AsyncSchemaResourceWithRawResponse(self._credentials.schema)


class CredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.create = to_streamed_response_wrapper(
            credentials.create,
        )
        self.delete = to_streamed_response_wrapper(
            credentials.delete,
        )

    @cached_property
    def schema(self) -> SchemaResourceWithStreamingResponse:
        return SchemaResourceWithStreamingResponse(self._credentials.schema)


class AsyncCredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.create = async_to_streamed_response_wrapper(
            credentials.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            credentials.delete,
        )

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithStreamingResponse:
        return AsyncSchemaResourceWithStreamingResponse(self._credentials.schema)
