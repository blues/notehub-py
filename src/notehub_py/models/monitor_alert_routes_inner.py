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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from notehub_py.models.email_notification import EmailNotification
from notehub_py.models.slack_bearer_notification import SlackBearerNotification
from notehub_py.models.slack_web_hook_notification import SlackWebHookNotification
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

MONITORALERTROUTESINNER_ONE_OF_SCHEMAS = ["EmailNotification", "SlackBearerNotification", "SlackWebHookNotification"]

class MonitorAlertRoutesInner(BaseModel):
    """
    MonitorAlertRoutesInner
    """
    # data type: SlackWebHookNotification
    oneof_schema_1_validator: Optional[SlackWebHookNotification] = None
    # data type: SlackBearerNotification
    oneof_schema_2_validator: Optional[SlackBearerNotification] = None
    # data type: EmailNotification
    oneof_schema_3_validator: Optional[EmailNotification] = None
    actual_instance: Optional[Union[EmailNotification, SlackBearerNotification, SlackWebHookNotification]] = None
    one_of_schemas: Set[str] = { "EmailNotification", "SlackBearerNotification", "SlackWebHookNotification" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = MonitorAlertRoutesInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: SlackWebHookNotification
        if not isinstance(v, SlackWebHookNotification):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SlackWebHookNotification`")
        else:
            match += 1
        # validate data type: SlackBearerNotification
        if not isinstance(v, SlackBearerNotification):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SlackBearerNotification`")
        else:
            match += 1
        # validate data type: EmailNotification
        if not isinstance(v, EmailNotification):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EmailNotification`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in MonitorAlertRoutesInner with oneOf schemas: EmailNotification, SlackBearerNotification, SlackWebHookNotification. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in MonitorAlertRoutesInner with oneOf schemas: EmailNotification, SlackBearerNotification, SlackWebHookNotification. Details: " + ", ".join(error_messages))
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

        # deserialize data into SlackWebHookNotification
        try:
            instance.actual_instance = SlackWebHookNotification.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SlackBearerNotification
        try:
            instance.actual_instance = SlackBearerNotification.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EmailNotification
        try:
            instance.actual_instance = EmailNotification.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into MonitorAlertRoutesInner with oneOf schemas: EmailNotification, SlackBearerNotification, SlackWebHookNotification. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into MonitorAlertRoutesInner with oneOf schemas: EmailNotification, SlackBearerNotification, SlackWebHookNotification. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], EmailNotification, SlackBearerNotification, SlackWebHookNotification]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


