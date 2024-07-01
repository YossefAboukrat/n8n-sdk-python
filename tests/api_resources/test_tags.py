# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from n8n_minus_1.1.1 import N8n, AsyncN8n

from n8n_minus_1.1.1.types import Tag, TagList

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from n8n_minus_1.1.1 import N8n, AsyncN8n
from tests.utils import assert_matches_type
from n8n_minus_1.1.1.types import tag_create_params
from n8n_minus_1.1.1.types import tag_update_params
from n8n_minus_1.1.1.types import tag_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: N8n) -> None:
        tag = client.tags.create(
            name="Production",
        )
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: N8n) -> None:

        response = client.tags.with_raw_response.create(
            name="Production",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = response.parse()
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: N8n) -> None:
        with client.tags.with_streaming_response.create(
            name="Production",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = response.parse()
            assert_matches_type(Tag, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: N8n) -> None:
        tag = client.tags.retrieve(
            "string",
        )
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: N8n) -> None:

        response = client.tags.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = response.parse()
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: N8n) -> None:
        with client.tags.with_streaming_response.retrieve(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = response.parse()
            assert_matches_type(Tag, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.tags.with_raw_response.retrieve(
              "",
          )

    @parametrize
    def test_method_update(self, client: N8n) -> None:
        tag = client.tags.update(
            "string",
            name="Production",
        )
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: N8n) -> None:

        response = client.tags.with_raw_response.update(
            "string",
            name="Production",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = response.parse()
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: N8n) -> None:
        with client.tags.with_streaming_response.update(
            "string",
            name="Production",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = response.parse()
            assert_matches_type(Tag, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.tags.with_raw_response.update(
              "",
              name="Production",
          )

    @parametrize
    def test_method_list(self, client: N8n) -> None:
        tag = client.tags.list()
        assert_matches_type(TagList, tag, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: N8n) -> None:
        tag = client.tags.list(
            cursor="string",
            limit=100,
        )
        assert_matches_type(TagList, tag, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: N8n) -> None:

        response = client.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = response.parse()
        assert_matches_type(TagList, tag, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: N8n) -> None:
        with client.tags.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = response.parse()
            assert_matches_type(TagList, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: N8n) -> None:
        tag = client.tags.delete(
            "string",
        )
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: N8n) -> None:

        response = client.tags.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = response.parse()
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: N8n) -> None:
        with client.tags.with_streaming_response.delete(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = response.parse()
            assert_matches_type(Tag, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.tags.with_raw_response.delete(
              "",
          )
class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncN8n) -> None:
        tag = await async_client.tags.create(
            name="Production",
        )
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncN8n) -> None:

        response = await async_client.tags.with_raw_response.create(
            name="Production",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncN8n) -> None:
        async with async_client.tags.with_streaming_response.create(
            name="Production",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncN8n) -> None:
        tag = await async_client.tags.retrieve(
            "string",
        )
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncN8n) -> None:

        response = await async_client.tags.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncN8n) -> None:
        async with async_client.tags.with_streaming_response.retrieve(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.tags.with_raw_response.retrieve(
              "",
          )

    @parametrize
    async def test_method_update(self, async_client: AsyncN8n) -> None:
        tag = await async_client.tags.update(
            "string",
            name="Production",
        )
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncN8n) -> None:

        response = await async_client.tags.with_raw_response.update(
            "string",
            name="Production",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncN8n) -> None:
        async with async_client.tags.with_streaming_response.update(
            "string",
            name="Production",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.tags.with_raw_response.update(
              "",
              name="Production",
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncN8n) -> None:
        tag = await async_client.tags.list()
        assert_matches_type(TagList, tag, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncN8n) -> None:
        tag = await async_client.tags.list(
            cursor="string",
            limit=100,
        )
        assert_matches_type(TagList, tag, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncN8n) -> None:

        response = await async_client.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = await response.parse()
        assert_matches_type(TagList, tag, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncN8n) -> None:
        async with async_client.tags.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = await response.parse()
            assert_matches_type(TagList, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncN8n) -> None:
        tag = await async_client.tags.delete(
            "string",
        )
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncN8n) -> None:

        response = await async_client.tags.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncN8n) -> None:
        async with async_client.tags.with_streaming_response.delete(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.tags.with_raw_response.delete(
              "",
          )