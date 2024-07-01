# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["Execution"]


class Execution(BaseModel):
    id: Optional[float] = None

    data: Optional[object] = None

    finished: Optional[bool] = None

    mode: Optional[Literal["cli", "error", "integrated", "internal", "manual", "retry", "trigger", "webhook"]] = None

    retry_of: Optional[float] = FieldInfo(alias="retryOf", default=None)

    retry_success_id: Optional[float] = FieldInfo(alias="retrySuccessId", default=None)

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    stopped_at: Optional[datetime] = FieldInfo(alias="stoppedAt", default=None)

    wait_till: Optional[datetime] = FieldInfo(alias="waitTill", default=None)

    workflow_id: Optional[float] = FieldInfo(alias="workflowId", default=None)
