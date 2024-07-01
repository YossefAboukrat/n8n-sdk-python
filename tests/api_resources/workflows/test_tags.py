# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from n8n_minus_1.1.1 import N8n, AsyncN8n

from n8n_minus_1.1.1.types.workflows import WorkflowTags

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from n8n_minus_1.1.1 import N8n, AsyncN8n
from tests.utils import assert_matches_type
from n8n_minus_1.1.1.types.workflows import tag_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_update(self, client: N8n) -> None:
        tag = client.workflows.tags.update(
            "string",
            body=[{
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }],
        )
        assert_matches_type(WorkflowTags, tag, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: N8n) -> None:

        response = client.workflows.tags.with_raw_response.update(
            "string",
            body=[{
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = response.parse()
        assert_matches_type(WorkflowTags, tag, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: N8n) -> None:
        with client.workflows.tags.with_streaming_response.update(
            "string",
            body=[{
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = response.parse()
            assert_matches_type(WorkflowTags, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.workflows.tags.with_raw_response.update(
              "",
              body=[{
                  "id": "2tUt1wbLX592XDdX"
              }, {
                  "id": "2tUt1wbLX592XDdX"
              }, {
                  "id": "2tUt1wbLX592XDdX"
              }],
          )

    @parametrize
    def test_method_list(self, client: N8n) -> None:
        tag = client.workflows.tags.list(
            "string",
        )
        assert_matches_type(WorkflowTags, tag, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: N8n) -> None:

        response = client.workflows.tags.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = response.parse()
        assert_matches_type(WorkflowTags, tag, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: N8n) -> None:
        with client.workflows.tags.with_streaming_response.list(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = response.parse()
            assert_matches_type(WorkflowTags, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.workflows.tags.with_raw_response.list(
              "",
          )
class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_update(self, async_client: AsyncN8n) -> None:
        tag = await async_client.workflows.tags.update(
            "string",
            body=[{
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }],
        )
        assert_matches_type(WorkflowTags, tag, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncN8n) -> None:

        response = await async_client.workflows.tags.with_raw_response.update(
            "string",
            body=[{
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = await response.parse()
        assert_matches_type(WorkflowTags, tag, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncN8n) -> None:
        async with async_client.workflows.tags.with_streaming_response.update(
            "string",
            body=[{
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }, {
                "id": "2tUt1wbLX592XDdX"
            }],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = await response.parse()
            assert_matches_type(WorkflowTags, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.workflows.tags.with_raw_response.update(
              "",
              body=[{
                  "id": "2tUt1wbLX592XDdX"
              }, {
                  "id": "2tUt1wbLX592XDdX"
              }, {
                  "id": "2tUt1wbLX592XDdX"
              }],
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncN8n) -> None:
        tag = await async_client.workflows.tags.list(
            "string",
        )
        assert_matches_type(WorkflowTags, tag, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncN8n) -> None:

        response = await async_client.workflows.tags.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        tag = await response.parse()
        assert_matches_type(WorkflowTags, tag, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncN8n) -> None:
        async with async_client.workflows.tags.with_streaming_response.list(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            tag = await response.parse()
            assert_matches_type(WorkflowTags, tag, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.workflows.tags.with_raw_response.list(
              "",
          )