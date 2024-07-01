# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from n8n_minus_1.1.1 import N8n, AsyncN8n

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from n8n_minus_1.1.1 import N8n, AsyncN8n
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestSchema:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_retrieve(self, client: N8n) -> None:
        schema = client.credentials.schema.retrieve(
            "string",
        )
        assert_matches_type(object, schema, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: N8n) -> None:

        response = client.credentials.schema.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        schema = response.parse()
        assert_matches_type(object, schema, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: N8n) -> None:
        with client.credentials.schema.with_streaming_response.retrieve(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            schema = response.parse()
            assert_matches_type(object, schema, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_type_name` but received ''"):
          client.credentials.schema.with_raw_response.retrieve(
              "",
          )
class TestAsyncSchema:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_retrieve(self, async_client: AsyncN8n) -> None:
        schema = await async_client.credentials.schema.retrieve(
            "string",
        )
        assert_matches_type(object, schema, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncN8n) -> None:

        response = await async_client.credentials.schema.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        schema = await response.parse()
        assert_matches_type(object, schema, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncN8n) -> None:
        async with async_client.credentials.schema.with_streaming_response.retrieve(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            schema = await response.parse()
            assert_matches_type(object, schema, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_type_name` but received ''"):
          await async_client.credentials.schema.with_raw_response.retrieve(
              "",
          )