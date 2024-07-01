# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from n8n_minus_1.1.1 import N8n, AsyncN8n

from n8n_minus_1.1.1.types import Audit

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from n8n_minus_1.1.1 import N8n, AsyncN8n
from tests.utils import assert_matches_type
from n8n_minus_1.1.1.types import audit_generate_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestAudits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_generate(self, client: N8n) -> None:
        audit = client.audits.generate()
        assert_matches_type(Audit, audit, path=['response'])

    @parametrize
    def test_method_generate_with_all_params(self, client: N8n) -> None:
        audit = client.audits.generate(
            additional_options={
                "days_abandoned_workflow": 0,
                "categories": ["credentials", "database", "nodes"],
            },
        )
        assert_matches_type(Audit, audit, path=['response'])

    @parametrize
    def test_raw_response_generate(self, client: N8n) -> None:

        response = client.audits.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        audit = response.parse()
        assert_matches_type(Audit, audit, path=['response'])

    @parametrize
    def test_streaming_response_generate(self, client: N8n) -> None:
        with client.audits.with_streaming_response.generate() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            audit = response.parse()
            assert_matches_type(Audit, audit, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncAudits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_generate(self, async_client: AsyncN8n) -> None:
        audit = await async_client.audits.generate()
        assert_matches_type(Audit, audit, path=['response'])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncN8n) -> None:
        audit = await async_client.audits.generate(
            additional_options={
                "days_abandoned_workflow": 0,
                "categories": ["credentials", "database", "nodes"],
            },
        )
        assert_matches_type(Audit, audit, path=['response'])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncN8n) -> None:

        response = await async_client.audits.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        audit = await response.parse()
        assert_matches_type(Audit, audit, path=['response'])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncN8n) -> None:
        async with async_client.audits.with_streaming_response.generate() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            audit = await response.parse()
            assert_matches_type(Audit, audit, path=['response'])

        assert cast(Any, response.is_closed) is True