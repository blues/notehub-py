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
import json
import pprint
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictStr,
    ValidationError,
    field_validator,
)
from typing import Any, List, Optional
from notehub_py.models.aws import Aws
from notehub_py.models.azure import Azure
from notehub_py.models.google import Google
from notehub_py.models.http import Http
from notehub_py.models.mqtt import Mqtt
from notehub_py.models.proxy import Proxy
from notehub_py.models.radresponder import Radresponder
from notehub_py.models.slack import Slack
from notehub_py.models.snowflake import Snowflake
from notehub_py.models.thingworx import Thingworx
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

NOTEHUBROUTESCHEMA_ONE_OF_SCHEMAS = [
    "Aws",
    "Azure",
    "Google",
    "Http",
    "Mqtt",
    "Proxy",
    "Radresponder",
    "Slack",
    "Snowflake",
    "Thingworx",
]


class NotehubRouteSchema(BaseModel):
    """
    NotehubRouteSchema
    """

    # data type: Http
    oneof_schema_1_validator: Optional[Http] = None
    # data type: Google
    oneof_schema_2_validator: Optional[Google] = None
    # data type: Proxy
    oneof_schema_3_validator: Optional[Proxy] = None
    # data type: Mqtt
    oneof_schema_4_validator: Optional[Mqtt] = None
    # data type: Aws
    oneof_schema_5_validator: Optional[Aws] = None
    # data type: Radresponder
    oneof_schema_6_validator: Optional[Radresponder] = None
    # data type: Azure
    oneof_schema_7_validator: Optional[Azure] = None
    # data type: Thingworx
    oneof_schema_8_validator: Optional[Thingworx] = None
    # data type: Snowflake
    oneof_schema_9_validator: Optional[Snowflake] = None
    # data type: Slack
    oneof_schema_10_validator: Optional[Slack] = None
    actual_instance: Optional[
        Union[
            Aws,
            Azure,
            Google,
            Http,
            Mqtt,
            Proxy,
            Radresponder,
            Slack,
            Snowflake,
            Thingworx,
        ]
    ] = None
    one_of_schemas: Set[str] = {
        "Aws",
        "Azure",
        "Google",
        "Http",
        "Mqtt",
        "Proxy",
        "Radresponder",
        "Slack",
        "Snowflake",
        "Thingworx",
    }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`"
                )
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used."
                )
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator("actual_instance")
    def actual_instance_must_validate_oneof(cls, v):
        instance = NotehubRouteSchema.model_construct()
        error_messages = []
        match = 0
        # validate data type: Http
        if not isinstance(v, Http):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Http`")
        else:
            match += 1
        # validate data type: Google
        if not isinstance(v, Google):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Google`")
        else:
            match += 1
        # validate data type: Proxy
        if not isinstance(v, Proxy):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Proxy`")
        else:
            match += 1
        # validate data type: Mqtt
        if not isinstance(v, Mqtt):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Mqtt`")
        else:
            match += 1
        # validate data type: Aws
        if not isinstance(v, Aws):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Aws`")
        else:
            match += 1
        # validate data type: Radresponder
        if not isinstance(v, Radresponder):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `Radresponder`"
            )
        else:
            match += 1
        # validate data type: Azure
        if not isinstance(v, Azure):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Azure`")
        else:
            match += 1
        # validate data type: Thingworx
        if not isinstance(v, Thingworx):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Thingworx`")
        else:
            match += 1
        # validate data type: Snowflake
        if not isinstance(v, Snowflake):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Snowflake`")
        else:
            match += 1
        # validate data type: Slack
        if not isinstance(v, Slack):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Slack`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError(
                "Multiple matches found when setting `actual_instance` in NotehubRouteSchema with oneOf schemas: Aws, Azure, Google, Http, Mqtt, Proxy, Radresponder, Slack, Snowflake, Thingworx. Details: "
                + ", ".join(error_messages)
            )
        elif match == 0:
            # no match
            raise ValueError(
                "No match found when setting `actual_instance` in NotehubRouteSchema with oneOf schemas: Aws, Azure, Google, Http, Mqtt, Proxy, Radresponder, Slack, Snowflake, Thingworx. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into Http
        try:
            instance.actual_instance = Http.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Google
        try:
            instance.actual_instance = Google.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Proxy
        try:
            instance.actual_instance = Proxy.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Mqtt
        try:
            instance.actual_instance = Mqtt.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Aws
        try:
            instance.actual_instance = Aws.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Radresponder
        try:
            instance.actual_instance = Radresponder.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Azure
        try:
            instance.actual_instance = Azure.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Thingworx
        try:
            instance.actual_instance = Thingworx.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Snowflake
        try:
            instance.actual_instance = Snowflake.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Slack
        try:
            instance.actual_instance = Slack.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError(
                "Multiple matches found when deserializing the JSON string into NotehubRouteSchema with oneOf schemas: Aws, Azure, Google, Http, Mqtt, Proxy, Radresponder, Slack, Snowflake, Thingworx. Details: "
                + ", ".join(error_messages)
            )
        elif match == 0:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into NotehubRouteSchema with oneOf schemas: Aws, Azure, Google, Http, Mqtt, Proxy, Radresponder, Slack, Snowflake, Thingworx. Details: "
                + ", ".join(error_messages)
            )
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(
            self.actual_instance.to_json
        ):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(
        self,
    ) -> Optional[
        Union[
            Dict[str, Any],
            Aws,
            Azure,
            Google,
            Http,
            Mqtt,
            Proxy,
            Radresponder,
            Slack,
            Snowflake,
            Thingworx,
        ]
    ]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(
            self.actual_instance.to_dict
        ):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
