# coding: utf-8

"""
    Notehub API

    The OpenAPI definition for the Notehub.io API. 

    The version of the OpenAPI document: 1.0.0
    Contact: engineering@blues.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from notehub_py.models.monitor_alert_routes_inner import MonitorAlertRoutesInner
from notehub_py.models.monitor_thresholds import MonitorThresholds
from typing import Optional, Set
from typing_extensions import Self

class CreateMonitor(BaseModel):
    """
    CreateMonitor
    """ # noqa: E501
    uid: Optional[StrictStr] = None
    name: StrictStr
    description: StrictStr
    source_type: Optional[StrictStr] = Field(default=None, description="The type of source to monitor. Currently only \"event\" is supported.")
    disabled: Optional[StrictBool] = Field(default=None, description="If true, the monitor will not be evaluated.")
    alert: Optional[StrictBool] = Field(default=None, description="If true, the monitor is in alert state.")
    notefile_filter: List[StrictStr]
    fleet_filter: Optional[List[StrictStr]] = None
    source_selector: Optional[StrictStr] = Field(default=None, description="A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.")
    condition_type: Optional[StrictStr] = Field(default=None, description="The type of condition to apply to the value selected by the source_selector")
    thresholds: Optional[MonitorThresholds] = None
    alert_routes: List[MonitorAlertRoutesInner]
    last_routed_at: Optional[StrictStr] = Field(default=None, description="The last time the monitor was evaluated and routed.")
    silenced: Optional[StrictBool] = Field(default=None, description="If true, alerts will be created, but no notifications will be sent.")
    routing_cooldown_period: Optional[StrictStr] = Field(default=None, description="The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.")
    __properties: ClassVar[List[str]] = ["uid", "name", "description", "source_type", "disabled", "alert", "notefile_filter", "fleet_filter", "source_selector", "condition_type", "thresholds", "alert_routes", "last_routed_at", "silenced", "routing_cooldown_period"]

    @field_validator('source_type')
    def source_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['event']):
            raise ValueError("must be one of enum values ('event')")
        return value

    @field_validator('condition_type')
    def condition_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['greater_than', 'greater_than_or_equal_to', 'less_than', 'less_than_or_equal_to', 'equal_to', 'not_equal_to']):
            raise ValueError("must be one of enum values ('greater_than', 'greater_than_or_equal_to', 'less_than', 'less_than_or_equal_to', 'equal_to', 'not_equal_to')")
        return value

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
        """Create an instance of CreateMonitor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of thresholds
        if self.thresholds:
            _dict['thresholds'] = self.thresholds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in alert_routes (list)
        _items = []
        if self.alert_routes:
            for _item in self.alert_routes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alert_routes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateMonitor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uid": obj.get("uid"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "source_type": obj.get("source_type"),
            "disabled": obj.get("disabled"),
            "alert": obj.get("alert"),
            "notefile_filter": obj.get("notefile_filter"),
            "fleet_filter": obj.get("fleet_filter"),
            "source_selector": obj.get("source_selector"),
            "condition_type": obj.get("condition_type"),
            "thresholds": MonitorThresholds.from_dict(obj["thresholds"]) if obj.get("thresholds") is not None else None,
            "alert_routes": [MonitorAlertRoutesInner.from_dict(_item) for _item in obj["alert_routes"]] if obj.get("alert_routes") is not None else None,
            "last_routed_at": obj.get("last_routed_at"),
            "silenced": obj.get("silenced"),
            "routing_cooldown_period": obj.get("routing_cooldown_period")
        })
        return _obj


