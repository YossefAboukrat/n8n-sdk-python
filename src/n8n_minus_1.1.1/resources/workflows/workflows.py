# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .tags import TagsResource, AsyncTagsResource

from ..._compat import cached_property

from ...types.workflow import Workflow

from ..._utils import maybe_transform, async_maybe_transform

from typing import Iterable, Union, Optional

from ...types.workflow_list import WorkflowList

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ...types import workflow_create_params, workflow_update_params

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
from ...types import workflow_create_params
from ...types import workflow_update_params
from ...types import workflow_list_params
from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]


class WorkflowsResource(SyncAPIResource):
    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkflowsResourceWithRawResponse:
        return WorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowsResourceWithStreamingResponse:
        return WorkflowsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connections: object,
        name: str,
        nodes: Iterable[workflow_create_params.Node],
        settings: workflow_create_params.Settings,
        static_data: Union[Optional[str], Optional[object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Create a workflow in your instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/workflows",
            body=maybe_transform(
                {
                    "connections": connections,
                    "name": name,
                    "nodes": nodes,
                    "settings": settings,
                    "static_data": static_data,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Retrieves a workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/workflows/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )

    def update(
        self,
        id: str,
        *,
        connections: object,
        name: str,
        nodes: Iterable[workflow_update_params.Node],
        settings: workflow_update_params.Settings,
        static_data: Union[Optional[str], Optional[object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Update a workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/workflows/{id}",
            body=maybe_transform(
                {
                    "connections": connections,
                    "name": name,
                    "nodes": nodes,
                    "settings": settings,
                    "static_data": static_data,
                },
                workflow_update_params.WorkflowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )

    def list(
        self,
        *,
        active: bool | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowList:
        """
        Retrieve all workflows from your instance.

        Args:
          cursor: Paginate by setting the cursor parameter to the nextCursor attribute returned by
              the previous request's response. Default value fetches the first "page" of the
              collection. See pagination for more detail.

          limit: The maximum number of items to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/workflows",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "cursor": cursor,
                        "limit": limit,
                        "name": name,
                        "tags": tags,
                    },
                    workflow_list_params.WorkflowListParams,
                ),
            ),
            cast_to=WorkflowList,
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
    ) -> Workflow:
        """
        Deletes a workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/workflows/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )

    def activate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Active a workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/workflows/{id}/activate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )

    def deactivate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Deactivate a workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/workflows/{id}/deactivate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )


class AsyncWorkflowsResource(AsyncAPIResource):
    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkflowsResourceWithRawResponse:
        return AsyncWorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        return AsyncWorkflowsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connections: object,
        name: str,
        nodes: Iterable[workflow_create_params.Node],
        settings: workflow_create_params.Settings,
        static_data: Union[Optional[str], Optional[object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Create a workflow in your instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/workflows",
            body=await async_maybe_transform(
                {
                    "connections": connections,
                    "name": name,
                    "nodes": nodes,
                    "settings": settings,
                    "static_data": static_data,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Retrieves a workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/workflows/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )

    async def update(
        self,
        id: str,
        *,
        connections: object,
        name: str,
        nodes: Iterable[workflow_update_params.Node],
        settings: workflow_update_params.Settings,
        static_data: Union[Optional[str], Optional[object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Update a workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/workflows/{id}",
            body=await async_maybe_transform(
                {
                    "connections": connections,
                    "name": name,
                    "nodes": nodes,
                    "settings": settings,
                    "static_data": static_data,
                },
                workflow_update_params.WorkflowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )

    async def list(
        self,
        *,
        active: bool | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowList:
        """
        Retrieve all workflows from your instance.

        Args:
          cursor: Paginate by setting the cursor parameter to the nextCursor attribute returned by
              the previous request's response. Default value fetches the first "page" of the
              collection. See pagination for more detail.

          limit: The maximum number of items to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/workflows",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active": active,
                        "cursor": cursor,
                        "limit": limit,
                        "name": name,
                        "tags": tags,
                    },
                    workflow_list_params.WorkflowListParams,
                ),
            ),
            cast_to=WorkflowList,
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
    ) -> Workflow:
        """
        Deletes a workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/workflows/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )

    async def activate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Active a workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/workflows/{id}/activate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )

    async def deactivate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """
        Deactivate a workflow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/workflows/{id}/deactivate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workflow,
        )


class WorkflowsResourceWithRawResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.create = to_raw_response_wrapper(
            workflows.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workflows.update,
        )
        self.list = to_raw_response_wrapper(
            workflows.list,
        )
        self.delete = to_raw_response_wrapper(
            workflows.delete,
        )
        self.activate = to_raw_response_wrapper(
            workflows.activate,
        )
        self.deactivate = to_raw_response_wrapper(
            workflows.deactivate,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._workflows.tags)


class AsyncWorkflowsResourceWithRawResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.create = async_to_raw_response_wrapper(
            workflows.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workflows.update,
        )
        self.list = async_to_raw_response_wrapper(
            workflows.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workflows.delete,
        )
        self.activate = async_to_raw_response_wrapper(
            workflows.activate,
        )
        self.deactivate = async_to_raw_response_wrapper(
            workflows.deactivate,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._workflows.tags)


class WorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.create = to_streamed_response_wrapper(
            workflows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workflows.update,
        )
        self.list = to_streamed_response_wrapper(
            workflows.list,
        )
        self.delete = to_streamed_response_wrapper(
            workflows.delete,
        )
        self.activate = to_streamed_response_wrapper(
            workflows.activate,
        )
        self.deactivate = to_streamed_response_wrapper(
            workflows.deactivate,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._workflows.tags)


class AsyncWorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.create = async_to_streamed_response_wrapper(
            workflows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workflows.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workflows.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workflows.delete,
        )
        self.activate = async_to_streamed_response_wrapper(
            workflows.activate,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            workflows.deactivate,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._workflows.tags)
