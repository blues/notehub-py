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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class Radresponder(BaseModel):
    """
    Route settings specific to RadResponder routes.  Only used for RadResponder route types
    """  # noqa: E501

    fleets: Optional[Annotated[List[StrictStr], Field(min_length=0)]] = Field(
        default=None,
        description="list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets",
    )
    test_api: Optional[StrictBool] = False
    data_feed_key: Optional[StrictStr] = None
    client_id: Optional[StrictStr] = None
    client_secret: Optional[StrictStr] = Field(
        default=None,
        description="This value is input-only and will be omitted from the response and replaced with a placeholder",
    )
    __properties: ClassVar[List[str]] = [
        "fleets",
        "test_api",
        "data_feed_key",
        "client_id",
        "client_secret",
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
        """Create an instance of Radresponder from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Radresponder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "fleets": obj.get("fleets"),
                "test_api": (
                    obj.get("test_api") if obj.get("test_api") is not None else False
                ),
                "data_feed_key": obj.get("data_feed_key"),
                "client_id": obj.get("client_id"),
                "client_secret": obj.get("client_secret"),
            }
        )
        return _obj
