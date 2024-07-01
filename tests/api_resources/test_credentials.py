# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from n8n_minus_1.1.1 import N8n, AsyncN8n

from n8n_minus_1.1.1.types import Credential

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from n8n_minus_1.1.1 import N8n, AsyncN8n
from tests.utils import assert_matches_type
from n8n_minus_1.1.1.types import credential_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: N8n) -> None:
        credential = client.credentials.create(
            data={
                "token": "ada612vad6fa5df4adf5a5dsf4389adsf76da7s"
            },
            name="Joe's Github Credentials",
            type="github",
        )
        assert_matches_type(Credential, credential, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: N8n) -> None:

        response = client.credentials.with_raw_response.create(
            data={
                "token": "ada612vad6fa5df4adf5a5dsf4389adsf76da7s"
            },
            name="Joe's Github Credentials",
            type="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        credential = response.parse()
        assert_matches_type(Credential, credential, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: N8n) -> None:
        with client.credentials.with_streaming_response.create(
            data={
                "token": "ada612vad6fa5df4adf5a5dsf4389adsf76da7s"
            },
            name="Joe's Github Credentials",
            type="github",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            credential = response.parse()
            assert_matches_type(Credential, credential, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: N8n) -> None:
        credential = client.credentials.delete(
            "string",
        )
        assert_matches_type(Credential, credential, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: N8n) -> None:

        response = client.credentials.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        credential = response.parse()
        assert_matches_type(Credential, credential, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: N8n) -> None:
        with client.credentials.with_streaming_response.delete(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            credential = response.parse()
            assert_matches_type(Credential, credential, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.credentials.with_raw_response.delete(
              "",
          )
class TestAsyncCredentials:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncN8n) -> None:
        credential = await async_client.credentials.create(
            data={
                "token": "ada612vad6fa5df4adf5a5dsf4389adsf76da7s"
            },
            name="Joe's Github Credentials",
            type="github",
        )
        assert_matches_type(Credential, credential, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncN8n) -> None:

        response = await async_client.credentials.with_raw_response.create(
            data={
                "token": "ada612vad6fa5df4adf5a5dsf4389adsf76da7s"
            },
            name="Joe's Github Credentials",
            type="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        credential = await response.parse()
        assert_matches_type(Credential, credential, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncN8n) -> None:
        async with async_client.credentials.with_streaming_response.create(
            data={
                "token": "ada612vad6fa5df4adf5a5dsf4389adsf76da7s"
            },
            name="Joe's Github Credentials",
            type="github",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            credential = await response.parse()
            assert_matches_type(Credential, credential, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncN8n) -> None:
        credential = await async_client.credentials.delete(
            "string",
        )
        assert_matches_type(Credential, credential, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncN8n) -> None:

        response = await async_client.credentials.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        credential = await response.parse()
        assert_matches_type(Credential, credential, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncN8n) -> None:
        async with async_client.credentials.with_streaming_response.delete(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            credential = await response.parse()
            assert_matches_type(Credential, credential, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.credentials.with_raw_response.delete(
              "",
          )