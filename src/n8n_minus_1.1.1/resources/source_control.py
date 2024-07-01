# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.import_result import ImportResult

from .._utils import maybe_transform, async_maybe_transform

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import source_control_pull_params

__all__ = ["SourceControlResource", "AsyncSourceControlResource"]


class SourceControlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SourceControlResourceWithRawResponse:
        return SourceControlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourceControlResourceWithStreamingResponse:
        return SourceControlResourceWithStreamingResponse(self)

    def pull(
        self,
        *,
        force: bool | NotGiven = NOT_GIVEN,
        variables: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImportResult:
        """
        Requires the Source Control feature to be licensed and connected to a
        repository.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/source-control/pull",
            body=maybe_transform(
                {
                    "force": force,
                    "variables": variables,
                },
                source_control_pull_params.SourceControlPullParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportResult,
        )


class AsyncSourceControlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSourceControlResourceWithRawResponse:
        return AsyncSourceControlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourceControlResourceWithStreamingResponse:
        return AsyncSourceControlResourceWithStreamingResponse(self)

    async def pull(
        self,
        *,
        force: bool | NotGiven = NOT_GIVEN,
        variables: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImportResult:
        """
        Requires the Source Control feature to be licensed and connected to a
        repository.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/source-control/pull",
            body=await async_maybe_transform(
                {
                    "force": force,
                    "variables": variables,
                },
                source_control_pull_params.SourceControlPullParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportResult,
        )


class SourceControlResourceWithRawResponse:
    def __init__(self, source_control: SourceControlResource) -> None:
        self._source_control = source_control

        self.pull = to_raw_response_wrapper(
            source_control.pull,
        )


class AsyncSourceControlResourceWithRawResponse:
    def __init__(self, source_control: AsyncSourceControlResource) -> None:
        self._source_control = source_control

        self.pull = async_to_raw_response_wrapper(
            source_control.pull,
        )


class SourceControlResourceWithStreamingResponse:
    def __init__(self, source_control: SourceControlResource) -> None:
        self._source_control = source_control

        self.pull = to_streamed_response_wrapper(
            source_control.pull,
        )


class AsyncSourceControlResourceWithStreamingResponse:
    def __init__(self, source_control: AsyncSourceControlResource) -> None:
        self._source_control = source_control

        self.pull = async_to_streamed_response_wrapper(
            source_control.pull,
        )
