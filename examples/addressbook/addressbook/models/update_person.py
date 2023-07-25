# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class UpdatePerson(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UpdatePerson - a model defined in OpenAPI

        age: The age of this UpdatePerson [Optional].
        first_name: The first_name of this UpdatePerson [Optional].
        hobbies: The hobbies of this UpdatePerson [Optional].
        last_name: The last_name of this UpdatePerson [Optional].
    """

    age: Optional[int] = Field(alias="age", default=None)
    first_name: Optional[str] = Field(alias="first_name", default=None)
    hobbies: Optional[List[str]] = Field(alias="hobbies", default=None)
    last_name: Optional[str] = Field(alias="last_name", default=None)


UpdatePerson.update_forward_refs()