# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["User"]


class User(BaseModel):
    email: str

    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the user was created."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """User's first name"""

    is_pending: Optional[bool] = FieldInfo(alias="isPending", default=None)
    """
    Whether the user finished setting up their account in response to the invitation
    (true) or not (false).
    """

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """User's last name"""

    role: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Last time the user was updated."""
