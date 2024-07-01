# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.execution import Execution

from .._utils import maybe_transform, async_maybe_transform

from ..types.execution_list import ExecutionList

from typing_extensions import Literal

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
from ..types import execution_retrieve_params
from ..types import execution_list_params

__all__ = ["ExecutionsResource", "AsyncExecutionsResource"]


class ExecutionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExecutionsResourceWithRawResponse:
        return ExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecutionsResourceWithStreamingResponse:
        return ExecutionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: float,
        *,
        include_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Execution:
        """
        Retrieve an execution from your instance.

        Args:
          include_data: Whether or not to include the execution's detailed data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/executions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_data": include_data}, execution_retrieve_params.ExecutionRetrieveParams
                ),
            ),
            cast_to=Execution,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        include_data: bool | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        status: Literal["error", "success", "waiting"] | NotGiven = NOT_GIVEN,
        workflow_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionList:
        """
        Retrieve all executions from your instance.

        Args:
          cursor: Paginate by setting the cursor parameter to the nextCursor attribute returned by
              the previous request's response. Default value fetches the first "page" of the
              collection. See pagination for more detail.

          include_data: Whether or not to include the execution's detailed data.

          limit: The maximum number of items to return.

          status: Status to filter the executions by.

          workflow_id: Workflow to filter the executions by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/executions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_data": include_data,
                        "limit": limit,
                        "status": status,
                        "workflow_id": workflow_id,
                    },
                    execution_list_params.ExecutionListParams,
                ),
            ),
            cast_to=ExecutionList,
        )

    def delete(
        self,
        id: float,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Execution:
        """
        Deletes an execution from your instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/executions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Execution,
        )


class AsyncExecutionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExecutionsResourceWithRawResponse:
        return AsyncExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecutionsResourceWithStreamingResponse:
        return AsyncExecutionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: float,
        *,
        include_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Execution:
        """
        Retrieve an execution from your instance.

        Args:
          include_data: Whether or not to include the execution's detailed data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/executions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_data": include_data}, execution_retrieve_params.ExecutionRetrieveParams
                ),
            ),
            cast_to=Execution,
        )

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        include_data: bool | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        status: Literal["error", "success", "waiting"] | NotGiven = NOT_GIVEN,
        workflow_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionList:
        """
        Retrieve all executions from your instance.

        Args:
          cursor: Paginate by setting the cursor parameter to the nextCursor attribute returned by
              the previous request's response. Default value fetches the first "page" of the
              collection. See pagination for more detail.

          include_data: Whether or not to include the execution's detailed data.

          limit: The maximum number of items to return.

          status: Status to filter the executions by.

          workflow_id: Workflow to filter the executions by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/executions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "include_data": include_data,
                        "limit": limit,
                        "status": status,
                        "workflow_id": workflow_id,
                    },
                    execution_list_params.ExecutionListParams,
                ),
            ),
            cast_to=ExecutionList,
        )

    async def delete(
        self,
        id: float,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Execution:
        """
        Deletes an execution from your instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/executions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Execution,
        )


class ExecutionsResourceWithRawResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = to_raw_response_wrapper(
            executions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            executions.list,
        )
        self.delete = to_raw_response_wrapper(
            executions.delete,
        )


class AsyncExecutionsResourceWithRawResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = async_to_raw_response_wrapper(
            executions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            executions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            executions.delete,
        )


class ExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = to_streamed_response_wrapper(
            executions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            executions.list,
        )
        self.delete = to_streamed_response_wrapper(
            executions.delete,
        )


class AsyncExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = async_to_streamed_response_wrapper(
            executions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            executions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            executions.delete,
        )
