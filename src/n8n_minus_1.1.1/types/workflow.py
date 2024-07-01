# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List, Union

from datetime import datetime

from typing_extensions import Literal

from .tag import Tag

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["Workflow", "Node", "Settings"]


class Node(BaseModel):
    id: Optional[str] = None

    always_output_data: Optional[bool] = FieldInfo(alias="alwaysOutputData", default=None)

    continue_on_fail: Optional[bool] = FieldInfo(alias="continueOnFail", default=None)
    """use onError instead"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    credentials: Optional[object] = None

    disabled: Optional[bool] = None

    execute_once: Optional[bool] = FieldInfo(alias="executeOnce", default=None)

    max_tries: Optional[float] = FieldInfo(alias="maxTries", default=None)

    name: Optional[str] = None

    notes: Optional[str] = None

    notes_in_flow: Optional[bool] = FieldInfo(alias="notesInFlow", default=None)

    on_error: Optional[str] = FieldInfo(alias="onError", default=None)

    parameters: Optional[object] = None

    position: Optional[List[float]] = None

    retry_on_fail: Optional[bool] = FieldInfo(alias="retryOnFail", default=None)

    type: Optional[str] = None

    type_version: Optional[float] = FieldInfo(alias="typeVersion", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    wait_between_tries: Optional[float] = FieldInfo(alias="waitBetweenTries", default=None)

    webhook_id: Optional[str] = FieldInfo(alias="webhookId", default=None)


class Settings(BaseModel):
    error_workflow: Optional[str] = FieldInfo(alias="errorWorkflow", default=None)
    """The ID of the workflow that contains the error trigger node."""

    execution_order: Optional[str] = FieldInfo(alias="executionOrder", default=None)

    execution_timeout: Optional[float] = FieldInfo(alias="executionTimeout", default=None)

    save_data_error_execution: Optional[Literal["all", "none"]] = FieldInfo(
        alias="saveDataErrorExecution", default=None
    )

    save_data_success_execution: Optional[Literal["all", "none"]] = FieldInfo(
        alias="saveDataSuccessExecution", default=None
    )

    save_execution_progress: Optional[bool] = FieldInfo(alias="saveExecutionProgress", default=None)

    save_manual_executions: Optional[bool] = FieldInfo(alias="saveManualExecutions", default=None)

    timezone: Optional[str] = None


class Workflow(BaseModel):
    connections: object

    name: str

    nodes: List[Node]

    settings: Settings

    id: Optional[str] = None

    active: Optional[bool] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    static_data: Union[Optional[str], Optional[object], None] = FieldInfo(alias="staticData", default=None)

    tags: Optional[List[Tag]] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
