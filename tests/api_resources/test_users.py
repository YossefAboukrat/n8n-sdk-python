# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from n8n_minus_1.1.1 import N8n, AsyncN8n

from n8n_minus_1.1.1.types import User, UserList

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from n8n_minus_1.1.1 import N8n, AsyncN8n
from tests.utils import assert_matches_type
from n8n_minus_1.1.1.types import user_retrieve_params
from n8n_minus_1.1.1.types import user_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_retrieve(self, client: N8n) -> None:
        user = client.users.retrieve(
            "string",
        )
        assert_matches_type(User, user, path=['response'])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: N8n) -> None:
        user = client.users.retrieve(
            "string",
            include_role=True,
        )
        assert_matches_type(User, user, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: N8n) -> None:

        response = client.users.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user = response.parse()
        assert_matches_type(User, user, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: N8n) -> None:
        with client.users.with_streaming_response.retrieve(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user = response.parse()
            assert_matches_type(User, user, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.users.with_raw_response.retrieve(
              "",
          )

    @parametrize
    def test_method_list(self, client: N8n) -> None:
        user = client.users.list()
        assert_matches_type(UserList, user, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: N8n) -> None:
        user = client.users.list(
            cursor="string",
            include_role=True,
            limit=100,
        )
        assert_matches_type(UserList, user, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: N8n) -> None:

        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user = response.parse()
        assert_matches_type(UserList, user, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: N8n) -> None:
        with client.users.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user = response.parse()
            assert_matches_type(UserList, user, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_retrieve(self, async_client: AsyncN8n) -> None:
        user = await async_client.users.retrieve(
            "string",
        )
        assert_matches_type(User, user, path=['response'])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncN8n) -> None:
        user = await async_client.users.retrieve(
            "string",
            include_role=True,
        )
        assert_matches_type(User, user, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncN8n) -> None:

        response = await async_client.users.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user = await response.parse()
        assert_matches_type(User, user, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncN8n) -> None:
        async with async_client.users.with_streaming_response.retrieve(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user = await response.parse()
            assert_matches_type(User, user, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.users.with_raw_response.retrieve(
              "",
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncN8n) -> None:
        user = await async_client.users.list()
        assert_matches_type(UserList, user, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncN8n) -> None:
        user = await async_client.users.list(
            cursor="string",
            include_role=True,
            limit=100,
        )
        assert_matches_type(UserList, user, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncN8n) -> None:

        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user = await response.parse()
        assert_matches_type(UserList, user, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncN8n) -> None:
        async with async_client.users.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user = await response.parse()
            assert_matches_type(UserList, user, path=['response'])

        assert cast(Any, response.is_closed) is True