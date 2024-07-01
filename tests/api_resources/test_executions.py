# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from n8n_minus_1.1.1 import N8n, AsyncN8n

from n8n_minus_1.1.1.types import Execution, ExecutionList

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from n8n_minus_1.1.1 import N8n, AsyncN8n
from tests.utils import assert_matches_type
from n8n_minus_1.1.1.types import execution_retrieve_params
from n8n_minus_1.1.1.types import execution_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_retrieve(self, client: N8n) -> None:
        execution = client.executions.retrieve(
            0,
        )
        assert_matches_type(Execution, execution, path=['response'])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: N8n) -> None:
        execution = client.executions.retrieve(
            0,
            include_data=True,
        )
        assert_matches_type(Execution, execution, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: N8n) -> None:

        response = client.executions.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        execution = response.parse()
        assert_matches_type(Execution, execution, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: N8n) -> None:
        with client.executions.with_streaming_response.retrieve(
            0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            execution = response.parse()
            assert_matches_type(Execution, execution, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: N8n) -> None:
        execution = client.executions.list()
        assert_matches_type(ExecutionList, execution, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: N8n) -> None:
        execution = client.executions.list(
            cursor="string",
            include_data=True,
            limit=100,
            status="error",
            workflow_id="1000",
        )
        assert_matches_type(ExecutionList, execution, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: N8n) -> None:

        response = client.executions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        execution = response.parse()
        assert_matches_type(ExecutionList, execution, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: N8n) -> None:
        with client.executions.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            execution = response.parse()
            assert_matches_type(ExecutionList, execution, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: N8n) -> None:
        execution = client.executions.delete(
            0,
        )
        assert_matches_type(Execution, execution, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: N8n) -> None:

        response = client.executions.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        execution = response.parse()
        assert_matches_type(Execution, execution, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: N8n) -> None:
        with client.executions.with_streaming_response.delete(
            0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            execution = response.parse()
            assert_matches_type(Execution, execution, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_retrieve(self, async_client: AsyncN8n) -> None:
        execution = await async_client.executions.retrieve(
            0,
        )
        assert_matches_type(Execution, execution, path=['response'])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncN8n) -> None:
        execution = await async_client.executions.retrieve(
            0,
            include_data=True,
        )
        assert_matches_type(Execution, execution, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncN8n) -> None:

        response = await async_client.executions.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        execution = await response.parse()
        assert_matches_type(Execution, execution, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncN8n) -> None:
        async with async_client.executions.with_streaming_response.retrieve(
            0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            execution = await response.parse()
            assert_matches_type(Execution, execution, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncN8n) -> None:
        execution = await async_client.executions.list()
        assert_matches_type(ExecutionList, execution, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncN8n) -> None:
        execution = await async_client.executions.list(
            cursor="string",
            include_data=True,
            limit=100,
            status="error",
            workflow_id="1000",
        )
        assert_matches_type(ExecutionList, execution, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncN8n) -> None:

        response = await async_client.executions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        execution = await response.parse()
        assert_matches_type(ExecutionList, execution, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncN8n) -> None:
        async with async_client.executions.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            execution = await response.parse()
            assert_matches_type(ExecutionList, execution, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncN8n) -> None:
        execution = await async_client.executions.delete(
            0,
        )
        assert_matches_type(Execution, execution, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncN8n) -> None:

        response = await async_client.executions.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        execution = await response.parse()
        assert_matches_type(Execution, execution, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncN8n) -> None:
        async with async_client.executions.with_streaming_response.delete(
            0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            execution = await response.parse()
            assert_matches_type(Execution, execution, path=['response'])

        assert cast(Any, response.is_closed) is True