# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from n8n_minus_1.1.1 import N8n, AsyncN8n

from n8n_minus_1.1.1.types import Workflow, WorkflowList

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from n8n_minus_1.1.1 import N8n, AsyncN8n
from tests.utils import assert_matches_type
from n8n_minus_1.1.1.types import workflow_create_params
from n8n_minus_1.1.1.types import workflow_update_params
from n8n_minus_1.1.1.types import workflow_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: N8n) -> None:
        workflow = client.workflows.create(
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_method_create_with_all_params(self, client: N8n) -> None:
        workflow = client.workflows.create(
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }, {
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }, {
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }],
            settings={
                "save_execution_progress": True,
                "save_manual_executions": True,
                "save_data_error_execution": "all",
                "save_data_success_execution": "all",
                "execution_timeout": 3600,
                "error_workflow": "VzqKEW0ShTXA5vPj",
                "timezone": "America/New_York",
                "execution_order": "v1",
            },
            static_data={
                "lastId": 1
            },
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: N8n) -> None:

        response = client.workflows.with_raw_response.create(
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: N8n) -> None:
        with client.workflows.with_streaming_response.create(
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: N8n) -> None:
        workflow = client.workflows.retrieve(
            "string",
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: N8n) -> None:

        response = client.workflows.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: N8n) -> None:
        with client.workflows.with_streaming_response.retrieve(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.workflows.with_raw_response.retrieve(
              "",
          )

    @parametrize
    def test_method_update(self, client: N8n) -> None:
        workflow = client.workflows.update(
            "string",
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_method_update_with_all_params(self, client: N8n) -> None:
        workflow = client.workflows.update(
            "string",
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }, {
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }, {
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }],
            settings={
                "save_execution_progress": True,
                "save_manual_executions": True,
                "save_data_error_execution": "all",
                "save_data_success_execution": "all",
                "execution_timeout": 3600,
                "error_workflow": "VzqKEW0ShTXA5vPj",
                "timezone": "America/New_York",
                "execution_order": "v1",
            },
            static_data={
                "lastId": 1
            },
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: N8n) -> None:

        response = client.workflows.with_raw_response.update(
            "string",
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: N8n) -> None:
        with client.workflows.with_streaming_response.update(
            "string",
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.workflows.with_raw_response.update(
              "",
              connections={
                  "main": [{
                      "node": "Jira",
                      "type": "main",
                      "index": 0,
                  }]
              },
              name="Workflow 1",
              nodes=[{}, {}, {}],
              settings={},
          )

    @parametrize
    def test_method_list(self, client: N8n) -> None:
        workflow = client.workflows.list()
        assert_matches_type(WorkflowList, workflow, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: N8n) -> None:
        workflow = client.workflows.list(
            active=True,
            cursor="string",
            limit=100,
            name="My Workflow",
            tags="test,production",
        )
        assert_matches_type(WorkflowList, workflow, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: N8n) -> None:

        response = client.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = response.parse()
        assert_matches_type(WorkflowList, workflow, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: N8n) -> None:
        with client.workflows.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = response.parse()
            assert_matches_type(WorkflowList, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: N8n) -> None:
        workflow = client.workflows.delete(
            "string",
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: N8n) -> None:

        response = client.workflows.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: N8n) -> None:
        with client.workflows.with_streaming_response.delete(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.workflows.with_raw_response.delete(
              "",
          )

    @parametrize
    def test_method_activate(self, client: N8n) -> None:
        workflow = client.workflows.activate(
            "string",
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_raw_response_activate(self, client: N8n) -> None:

        response = client.workflows.with_raw_response.activate(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_streaming_response_activate(self, client: N8n) -> None:
        with client.workflows.with_streaming_response.activate(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_activate(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.workflows.with_raw_response.activate(
              "",
          )

    @parametrize
    def test_method_deactivate(self, client: N8n) -> None:
        workflow = client.workflows.deactivate(
            "string",
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_raw_response_deactivate(self, client: N8n) -> None:

        response = client.workflows.with_raw_response.deactivate(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    def test_streaming_response_deactivate(self, client: N8n) -> None:
        with client.workflows.with_streaming_response.deactivate(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deactivate(self, client: N8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.workflows.with_raw_response.deactivate(
              "",
          )
class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncN8n) -> None:
        workflow = await async_client.workflows.create(
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncN8n) -> None:
        workflow = await async_client.workflows.create(
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }, {
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }, {
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }],
            settings={
                "save_execution_progress": True,
                "save_manual_executions": True,
                "save_data_error_execution": "all",
                "save_data_success_execution": "all",
                "execution_timeout": 3600,
                "error_workflow": "VzqKEW0ShTXA5vPj",
                "timezone": "America/New_York",
                "execution_order": "v1",
            },
            static_data={
                "lastId": 1
            },
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncN8n) -> None:

        response = await async_client.workflows.with_raw_response.create(
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = await response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncN8n) -> None:
        async with async_client.workflows.with_streaming_response.create(
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = await response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncN8n) -> None:
        workflow = await async_client.workflows.retrieve(
            "string",
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncN8n) -> None:

        response = await async_client.workflows.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = await response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncN8n) -> None:
        async with async_client.workflows.with_streaming_response.retrieve(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = await response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.workflows.with_raw_response.retrieve(
              "",
          )

    @parametrize
    async def test_method_update(self, async_client: AsyncN8n) -> None:
        workflow = await async_client.workflows.update(
            "string",
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncN8n) -> None:
        workflow = await async_client.workflows.update(
            "string",
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }, {
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }, {
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
                "name": "Jira",
                "webhook_id": "string",
                "disabled": True,
                "notes_in_flow": True,
                "notes": "string",
                "type": "n8n-nodes-base.Jira",
                "type_version": 1,
                "execute_once": False,
                "always_output_data": False,
                "retry_on_fail": False,
                "max_tries": 0,
                "wait_between_tries": 0,
                "continue_on_fail": False,
                "on_error": "stopWorkflow",
                "position": [-100, 80],
                "parameters": {
                    "additionalProperties": {}
                },
                "credentials": {
                    "jiraSoftwareCloudApi": {
                        "id": "35",
                        "name": "jiraApi",
                    }
                },
            }],
            settings={
                "save_execution_progress": True,
                "save_manual_executions": True,
                "save_data_error_execution": "all",
                "save_data_success_execution": "all",
                "execution_timeout": 3600,
                "error_workflow": "VzqKEW0ShTXA5vPj",
                "timezone": "America/New_York",
                "execution_order": "v1",
            },
            static_data={
                "lastId": 1
            },
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncN8n) -> None:

        response = await async_client.workflows.with_raw_response.update(
            "string",
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = await response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncN8n) -> None:
        async with async_client.workflows.with_streaming_response.update(
            "string",
            connections={
                "main": [{
                    "node": "Jira",
                    "type": "main",
                    "index": 0,
                }]
            },
            name="Workflow 1",
            nodes=[{}, {}, {}],
            settings={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = await response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.workflows.with_raw_response.update(
              "",
              connections={
                  "main": [{
                      "node": "Jira",
                      "type": "main",
                      "index": 0,
                  }]
              },
              name="Workflow 1",
              nodes=[{}, {}, {}],
              settings={},
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncN8n) -> None:
        workflow = await async_client.workflows.list()
        assert_matches_type(WorkflowList, workflow, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncN8n) -> None:
        workflow = await async_client.workflows.list(
            active=True,
            cursor="string",
            limit=100,
            name="My Workflow",
            tags="test,production",
        )
        assert_matches_type(WorkflowList, workflow, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncN8n) -> None:

        response = await async_client.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = await response.parse()
        assert_matches_type(WorkflowList, workflow, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncN8n) -> None:
        async with async_client.workflows.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = await response.parse()
            assert_matches_type(WorkflowList, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncN8n) -> None:
        workflow = await async_client.workflows.delete(
            "string",
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncN8n) -> None:

        response = await async_client.workflows.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = await response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncN8n) -> None:
        async with async_client.workflows.with_streaming_response.delete(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = await response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.workflows.with_raw_response.delete(
              "",
          )

    @parametrize
    async def test_method_activate(self, async_client: AsyncN8n) -> None:
        workflow = await async_client.workflows.activate(
            "string",
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncN8n) -> None:

        response = await async_client.workflows.with_raw_response.activate(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = await response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncN8n) -> None:
        async with async_client.workflows.with_streaming_response.activate(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = await response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_activate(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.workflows.with_raw_response.activate(
              "",
          )

    @parametrize
    async def test_method_deactivate(self, async_client: AsyncN8n) -> None:
        workflow = await async_client.workflows.deactivate(
            "string",
        )
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncN8n) -> None:

        response = await async_client.workflows.with_raw_response.deactivate(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        workflow = await response.parse()
        assert_matches_type(Workflow, workflow, path=['response'])

    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncN8n) -> None:
        async with async_client.workflows.with_streaming_response.deactivate(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            workflow = await response.parse()
            assert_matches_type(Workflow, workflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncN8n) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.workflows.with_raw_response.deactivate(
              "",
          )