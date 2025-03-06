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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from notehub_py.models.contact import Contact
from notehub_py.models.device_tower_info import DeviceTowerInfo
from notehub_py.models.dfu_env import DFUEnv
from notehub_py.models.location import Location
from typing import Optional, Set
from typing_extensions import Self

class Device(BaseModel):
    """
    Device
    """ # noqa: E501
    uid: StrictStr
    serial_number: Optional[StrictStr] = None
    provisioned: datetime
    last_activity: Optional[datetime] = None
    contact: Optional[Contact] = None
    product_uid: StrictStr
    fleet_uids: List[StrictStr]
    tower_info: Optional[DeviceTowerInfo] = None
    tower_location: Optional[Location] = None
    gps_location: Optional[Location] = None
    triangulated_location: Optional[Location] = None
    voltage: Union[StrictFloat, StrictInt]
    temperature: Union[StrictFloat, StrictInt]
    dfu: Optional[DFUEnv] = None
    firmware_host: Optional[StrictStr] = None
    firmware_notecard: Optional[StrictStr] = None
    sku: Optional[StrictStr] = None
    disabled: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["uid", "serial_number", "provisioned", "last_activity", "contact", "product_uid", "fleet_uids", "tower_info", "tower_location", "gps_location", "triangulated_location", "voltage", "temperature", "dfu", "firmware_host", "firmware_notecard", "sku", "disabled"]

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
        """Create an instance of Device from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tower_info
        if self.tower_info:
            _dict['tower_info'] = self.tower_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tower_location
        if self.tower_location:
            _dict['tower_location'] = self.tower_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gps_location
        if self.gps_location:
            _dict['gps_location'] = self.gps_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of triangulated_location
        if self.triangulated_location:
            _dict['triangulated_location'] = self.triangulated_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dfu
        if self.dfu:
            _dict['dfu'] = self.dfu.to_dict()
        # set to None if contact (nullable) is None
        # and model_fields_set contains the field
        if self.contact is None and "contact" in self.model_fields_set:
            _dict['contact'] = None

        # set to None if tower_location (nullable) is None
        # and model_fields_set contains the field
        if self.tower_location is None and "tower_location" in self.model_fields_set:
            _dict['tower_location'] = None

        # set to None if gps_location (nullable) is None
        # and model_fields_set contains the field
        if self.gps_location is None and "gps_location" in self.model_fields_set:
            _dict['gps_location'] = None

        # set to None if triangulated_location (nullable) is None
        # and model_fields_set contains the field
        if self.triangulated_location is None and "triangulated_location" in self.model_fields_set:
            _dict['triangulated_location'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uid": obj.get("uid"),
            "serial_number": obj.get("serial_number"),
            "provisioned": obj.get("provisioned"),
            "last_activity": obj.get("last_activity"),
            "contact": Contact.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "product_uid": obj.get("product_uid"),
            "fleet_uids": obj.get("fleet_uids"),
            "tower_info": DeviceTowerInfo.from_dict(obj["tower_info"]) if obj.get("tower_info") is not None else None,
            "tower_location": Location.from_dict(obj["tower_location"]) if obj.get("tower_location") is not None else None,
            "gps_location": Location.from_dict(obj["gps_location"]) if obj.get("gps_location") is not None else None,
            "triangulated_location": Location.from_dict(obj["triangulated_location"]) if obj.get("triangulated_location") is not None else None,
            "voltage": obj.get("voltage"),
            "temperature": obj.get("temperature"),
            "dfu": DFUEnv.from_dict(obj["dfu"]) if obj.get("dfu") is not None else None,
            "firmware_host": obj.get("firmware_host"),
            "firmware_notecard": obj.get("firmware_notecard"),
            "sku": obj.get("sku"),
            "disabled": obj.get("disabled")
        })
        return _obj


