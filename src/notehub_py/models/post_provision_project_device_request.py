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
from typing import Optional, Set
from typing_extensions import Self

class PostProvisionProjectDeviceRequest(BaseModel):
    """
    PostProvisionProjectDeviceRequest
    """ # noqa: E501
    product_uid: StrictStr = Field(description="The ProductUID that the device should use.")
    device_sn: Optional[StrictStr] = Field(default=None, description="The serial number to assign to the device.")
    fleet_uids: Optional[List[StrictStr]] = Field(default=None, description="The fleetUIDs to provision the device to.")
    __properties: ClassVar[List[str]] = ["product_uid", "device_sn", "fleet_uids"]

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
        """Create an instance of PostProvisionProjectDeviceRequest from a JSON string"""
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
        # set to None if fleet_uids (nullable) is None
        # and model_fields_set contains the field
        if self.fleet_uids is None and "fleet_uids" in self.model_fields_set:
            _dict['fleet_uids'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostProvisionProjectDeviceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "product_uid": obj.get("product_uid"),
            "device_sn": obj.get("device_sn"),
            "fleet_uids": obj.get("fleet_uids")
        })
        return _obj


