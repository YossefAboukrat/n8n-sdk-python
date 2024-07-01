# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from typing import Iterable, Union, Optional

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["WorkflowCreateParams", "Node", "Settings"]


class WorkflowCreateParams(TypedDict, total=False):
    connections: Required[object]

    name: Required[str]

    nodes: Required[Iterable[Node]]

    settings: Required[Settings]

    static_data: Annotated[Union[Optional[str], Optional[object]], PropertyInfo(alias="staticData")]


class Node(TypedDict, total=False):
    id: str

    always_output_data: Annotated[bool, PropertyInfo(alias="alwaysOutputData")]

    continue_on_fail: Annotated[bool, PropertyInfo(alias="continueOnFail")]
    """use onError instead"""

    credentials: object

    disabled: bool

    execute_once: Annotated[bool, PropertyInfo(alias="executeOnce")]

    max_tries: Annotated[float, PropertyInfo(alias="maxTries")]

    name: str

    notes: str

    notes_in_flow: Annotated[bool, PropertyInfo(alias="notesInFlow")]

    on_error: Annotated[str, PropertyInfo(alias="onError")]

    parameters: object

    position: Iterable[float]

    retry_on_fail: Annotated[bool, PropertyInfo(alias="retryOnFail")]

    type: str

    type_version: Annotated[float, PropertyInfo(alias="typeVersion")]

    wait_between_tries: Annotated[float, PropertyInfo(alias="waitBetweenTries")]

    webhook_id: Annotated[str, PropertyInfo(alias="webhookId")]


class Settings(TypedDict, total=False):
    error_workflow: Annotated[str, PropertyInfo(alias="errorWorkflow")]
    """The ID of the workflow that contains the error trigger node."""

    execution_order: Annotated[str, PropertyInfo(alias="executionOrder")]

    execution_timeout: Annotated[float, PropertyInfo(alias="executionTimeout")]

    save_data_error_execution: Annotated[Literal["all", "none"], PropertyInfo(alias="saveDataErrorExecution")]

    save_data_success_execution: Annotated[Literal["all", "none"], PropertyInfo(alias="saveDataSuccessExecution")]

    save_execution_progress: Annotated[bool, PropertyInfo(alias="saveExecutionProgress")]

    save_manual_executions: Annotated[bool, PropertyInfo(alias="saveManualExecutions")]

    timezone: str
