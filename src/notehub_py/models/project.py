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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from notehub_py.models.contact import Contact
from notehub_py.models.role import Role
from typing import Optional, Set
from typing_extensions import Self

class Project(BaseModel):
    """
    Project
    """ # noqa: E501
    uid: StrictStr
    label: StrictStr
    created: datetime
    role: Optional[Role] = None
    administrative_contact: Optional[Contact] = None
    technical_contact: Optional[Contact] = None
    __properties: ClassVar[List[str]] = ["uid", "label", "created", "role", "administrative_contact", "technical_contact"]

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
        """Create an instance of Project from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of administrative_contact
        if self.administrative_contact:
            _dict['administrative_contact'] = self.administrative_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of technical_contact
        if self.technical_contact:
            _dict['technical_contact'] = self.technical_contact.to_dict()
        # set to None if role (nullable) is None
        # and model_fields_set contains the field
        if self.role is None and "role" in self.model_fields_set:
            _dict['role'] = None

        # set to None if administrative_contact (nullable) is None
        # and model_fields_set contains the field
        if self.administrative_contact is None and "administrative_contact" in self.model_fields_set:
            _dict['administrative_contact'] = None

        # set to None if technical_contact (nullable) is None
        # and model_fields_set contains the field
        if self.technical_contact is None and "technical_contact" in self.model_fields_set:
            _dict['technical_contact'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Project from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uid": obj.get("uid"),
            "label": obj.get("label"),
            "created": obj.get("created"),
            "role": obj.get("role"),
            "administrative_contact": Contact.from_dict(obj["administrative_contact"]) if obj.get("administrative_contact") is not None else None,
            "technical_contact": Contact.from_dict(obj["technical_contact"]) if obj.get("technical_contact") is not None else None
        })
        return _obj


