# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from n8n_minus_1.1.1 import N8n, AsyncN8n

from n8n_minus_1.1.1.types import ImportResult

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from n8n_minus_1.1.1 import N8n, AsyncN8n
from tests.utils import assert_matches_type
from n8n_minus_1.1.1.types import source_control_pull_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestSourceControl:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_pull(self, client: N8n) -> None:
        source_control = client.source_control.pull()
        assert_matches_type(ImportResult, source_control, path=['response'])

    @parametrize
    def test_method_pull_with_all_params(self, client: N8n) -> None:
        source_control = client.source_control.pull(
            force=True,
            variables={
                "foo": "bar"
            },
        )
        assert_matches_type(ImportResult, source_control, path=['response'])

    @parametrize
    def test_raw_response_pull(self, client: N8n) -> None:

        response = client.source_control.with_raw_response.pull()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        source_control = response.parse()
        assert_matches_type(ImportResult, source_control, path=['response'])

    @parametrize
    def test_streaming_response_pull(self, client: N8n) -> None:
        with client.source_control.with_streaming_response.pull() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            source_control = response.parse()
            assert_matches_type(ImportResult, source_control, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncSourceControl:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_pull(self, async_client: AsyncN8n) -> None:
        source_control = await async_client.source_control.pull()
        assert_matches_type(ImportResult, source_control, path=['response'])

    @parametrize
    async def test_method_pull_with_all_params(self, async_client: AsyncN8n) -> None:
        source_control = await async_client.source_control.pull(
            force=True,
            variables={
                "foo": "bar"
            },
        )
        assert_matches_type(ImportResult, source_control, path=['response'])

    @parametrize
    async def test_raw_response_pull(self, async_client: AsyncN8n) -> None:

        response = await async_client.source_control.with_raw_response.pull()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        source_control = await response.parse()
        assert_matches_type(ImportResult, source_control, path=['response'])

    @parametrize
    async def test_streaming_response_pull(self, async_client: AsyncN8n) -> None:
        async with async_client.source_control.with_streaming_response.pull() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            source_control = await response.parse()
            assert_matches_type(ImportResult, source_control, path=['response'])

        assert cast(Any, response.is_closed) is True