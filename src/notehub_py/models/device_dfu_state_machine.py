# coding: utf-8

"""
Notehub API

The OpenAPI definition for the Notehub.io API.

The version of the OpenAPI document: 1.2.0
Contact: engineering@blues.io
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from notehub_py.models.device_dfu_state_machine_node import DeviceDfuStateMachineNode
from typing import Optional, Set
from typing_extensions import Self


class DeviceDfuStateMachine(BaseModel):
    """
    Represents a single request to update the host or Notecard firmware
    """  # noqa: E501

    requested_version: Optional[StrictStr] = Field(
        default=None,
        description="Version of the firmware that was requested to be installed",
    )
    current_version: Optional[StrictStr] = Field(
        default=None,
        description="Version of the firmware that was installed prior to this request",
    )
    initiated: Optional[StrictStr] = Field(
        default=None, description="RFC3339 datetime of when this update was requested"
    )
    updates: Optional[List[DeviceDfuStateMachineNode]] = None
    __properties: ClassVar[List[str]] = [
        "requested_version",
        "current_version",
        "initiated",
        "updates",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DeviceDfuStateMachine from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in updates (list)
        _items = []
        if self.updates:
            for _item in self.updates:
                if _item:
                    _items.append(_item.to_dict())
            _dict["updates"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceDfuStateMachine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "requested_version": obj.get("requested_version"),
                "current_version": obj.get("current_version"),
                "initiated": obj.get("initiated"),
                "updates": (
                    [
                        DeviceDfuStateMachineNode.from_dict(_item)
                        for _item in obj["updates"]
                    ]
                    if obj.get("updates") is not None
                    else None
                ),
            }
        )
        return _obj
