# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.audit import Audit

from .._utils import maybe_transform, async_maybe_transform

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ..types import audit_generate_params

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
from ..types import audit_generate_params

__all__ = ["AuditsResource", "AsyncAuditsResource"]


class AuditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditsResourceWithRawResponse:
        return AuditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditsResourceWithStreamingResponse:
        return AuditsResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        additional_options: audit_generate_params.AdditionalOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Audit:
        """
        Generate a security audit for your n8n instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/audit",
            body=maybe_transform({"additional_options": additional_options}, audit_generate_params.AuditGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Audit,
        )


class AsyncAuditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditsResourceWithRawResponse:
        return AsyncAuditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditsResourceWithStreamingResponse:
        return AsyncAuditsResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        additional_options: audit_generate_params.AdditionalOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Audit:
        """
        Generate a security audit for your n8n instance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/audit",
            body=await async_maybe_transform(
                {"additional_options": additional_options}, audit_generate_params.AuditGenerateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Audit,
        )


class AuditsResourceWithRawResponse:
    def __init__(self, audits: AuditsResource) -> None:
        self._audits = audits

        self.generate = to_raw_response_wrapper(
            audits.generate,
        )


class AsyncAuditsResourceWithRawResponse:
    def __init__(self, audits: AsyncAuditsResource) -> None:
        self._audits = audits

        self.generate = async_to_raw_response_wrapper(
            audits.generate,
        )


class AuditsResourceWithStreamingResponse:
    def __init__(self, audits: AuditsResource) -> None:
        self._audits = audits

        self.generate = to_streamed_response_wrapper(
            audits.generate,
        )


class AsyncAuditsResourceWithStreamingResponse:
    def __init__(self, audits: AsyncAuditsResource) -> None:
        self._audits = audits

        self.generate = async_to_streamed_response_wrapper(
            audits.generate,
        )
