# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.user import User

from .._utils import maybe_transform, async_maybe_transform

from ..types.user_list import UserList

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
from ..types import user_retrieve_params
from ..types import user_list_params

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        include_role: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """Retrieve a user from your instance.

        Only available for the instance owner.

        Args:
          include_role: Whether to include the user's role or not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/users/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_role": include_role}, user_retrieve_params.UserRetrieveParams),
            ),
            cast_to=User,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        include_role: bool | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserList:
        """Retrieve all users from your instance.

        Only available for the instance owner.

        Args:
          cursor: Paginate by setting the cursor parameter to the nextCursor attribute returned by
              the previous request's response. Default value fetches the first "page" of the
              collection. See pagination for more detail.

          include_role: Whether to include the user's role or not.

          limit: The maximum number of items to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_role": include_role,
                        "limit": limit,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserList,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        include_role: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """Retrieve a user from your instance.

        Only available for the instance owner.

        Args:
          include_role: Whether to include the user's role or not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/users/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_role": include_role}, user_retrieve_params.UserRetrieveParams
                ),
            ),
            cast_to=User,
        )

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        include_role: bool | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserList:
        """Retrieve all users from your instance.

        Only available for the instance owner.

        Args:
          cursor: Paginate by setting the cursor parameter to the nextCursor attribute returned by
              the previous request's response. Default value fetches the first "page" of the
              collection. See pagination for more detail.

          include_role: Whether to include the user's role or not.

          limit: The maximum number of items to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "include_role": include_role,
                        "limit": limit,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserList,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
