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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from notehub_py.models.http_filter import HttpFilter
from notehub_py.models.snowflake_transform import SnowflakeTransform
from typing import Optional, Set
from typing_extensions import Self


class Slack(BaseModel):
    """
    Route settings specific to Slack routes.  Only used for Slack route types
    """  # noqa: E501

    fleets: Optional[Annotated[List[StrictStr], Field(min_length=0)]] = Field(
        default=None,
        description="list of Fleet UIDs to apply route to, if any.  If empty, applies to all Fleets",
    )
    filter: Optional[HttpFilter] = None
    transform: Optional[SnowflakeTransform] = None
    throttle_ms: Optional[StrictInt] = Field(
        default=None, description="Minimum time between requests in Miliseconds"
    )
    timeout: Optional[StrictInt] = Field(
        default=15, description="Timeout in seconds for each request"
    )
    slack_type: Optional[StrictStr] = Field(
        default=None,
        description='The type of Slack message.  Must be one of "slack-bearer" for Bearer Token or "slack-webhook" for Webhook messages',
    )
    bearer: Optional[StrictStr] = Field(
        default=None,
        description='The Bearer Token for Slack messaging, if the "slack-bearer" type is selected',
    )
    channel: Optional[StrictStr] = Field(
        default=None,
        description='The Channel ID for Bearer Token method, if the "slack-bearer" type is selected',
    )
    webhook_url: Optional[StrictStr] = Field(
        default=None,
        description='The Webhook URL for Slack Messaging if the "slack-webhook" type is selected',
    )
    text: Optional[StrictStr] = Field(
        default=None,
        description="The simple text message to be sent, if the blocks message field is not in use.  Placeholders are available for this field.",
    )
    blocks: Optional[StrictStr] = Field(
        default=None,
        description="The Blocks message to be sent.  If populated, this field overrides the text field within the Slack Messaging API.  Placeholders are available for this field.",
    )
    __properties: ClassVar[List[str]] = [
        "fleets",
        "filter",
        "transform",
        "throttle_ms",
        "timeout",
        "slack_type",
        "bearer",
        "channel",
        "webhook_url",
        "text",
        "blocks",
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
        """Create an instance of Slack from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict["filter"] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transform
        if self.transform:
            _dict["transform"] = self.transform.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Slack from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "fleets": obj.get("fleets"),
                "filter": (
                    HttpFilter.from_dict(obj["filter"])
                    if obj.get("filter") is not None
                    else None
                ),
                "transform": (
                    SnowflakeTransform.from_dict(obj["transform"])
                    if obj.get("transform") is not None
                    else None
                ),
                "throttle_ms": obj.get("throttle_ms"),
                "timeout": obj.get("timeout") if obj.get("timeout") is not None else 15,
                "slack_type": obj.get("slack_type"),
                "bearer": obj.get("bearer"),
                "channel": obj.get("channel"),
                "webhook_url": obj.get("webhook_url"),
                "text": obj.get("text"),
                "blocks": obj.get("blocks"),
            }
        )
        return _obj
