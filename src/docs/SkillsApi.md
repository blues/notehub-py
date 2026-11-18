# notehub_py.SkillsApi

All URIs are relative to *https://api.notefile.net*

| Method                                        | HTTP request                                                     | Description                       |
| --------------------------------------------- | ---------------------------------------------------------------- | --------------------------------- |
| [**delete_skill**](SkillsApi.md#delete_skill) | **DELETE** /v1/projects/{projectOrProductUID}/skills/{skillName} | Delete a project skill            |
| [**get_skill**](SkillsApi.md#get_skill)       | **GET** /v1/projects/{projectOrProductUID}/skills/{skillName}    | Get a project skill               |
| [**get_skills**](SkillsApi.md#get_skills)     | **GET** /v1/projects/{projectOrProductUID}/skills                | List project skills               |
| [**put_skill**](SkillsApi.md#put_skill)       | **PUT** /v1/projects/{projectOrProductUID}/skills/{skillName}    | Create or replace a project skill |

## delete_skill

> delete_skill(project_or_product_uid, skill_name, if_match)

Delete a project skill

Delete a skill and all its stored versions. Requires `If-Match` set to the revision from `GetSkill`. Requires the Owner or Developer role. Subprojects must write to their parent project.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.SkillsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    skill_name = "references/devices.md"  # str | Relative .md name, case-insensitive, at most 512 UTF-8 bytes. In URLs, encode the whole name once: references/devices.md becomes references%2Fdevices.md; a literal % becomes %25. Pass the unencoded name to SDKs. Spaces, Unicode and punctuation are allowed. No absolute paths, dot segments, empty segments, backslashes, colons, control characters or surrounding segment whitespace.
    if_match = "if_match_example"  # str | Required; use one strong ETag or quoted skill revision. Wildcards and weak tags are rejected.

    try:
        # Delete a project skill
        api_instance.delete_skill(project_or_product_uid, skill_name, if_match)
    except Exception as e:
        print("Exception when calling SkillsApi->delete_skill: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                  | Notes |
| -------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                                                                                                                                                                                                                                                                                                                              |
| **skill_name**             | **str** | Relative .md name, case-insensitive, at most 512 UTF-8 bytes. In URLs, encode the whole name once: references/devices.md becomes references%2Fdevices.md; a literal % becomes %25. Pass the unencoded name to SDKs. Spaces, Unicode and punctuation are allowed. No absolute paths, dot segments, empty segments, backslashes, colons, control characters or surrounding segment whitespace. |
| **if_match**               | **str** | Required; use one strong ETag or quoted skill revision. Wildcards and weak tags are rejected.                                                                                                                                                                                                                                                                                                |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_skill

> Skill get_skill(project_or_product_uid, skill_name, if_match=if_match, if_none_match=if_none_match)

Get a project skill

Get one skill's metadata and exact Markdown content. Use `links.self` from `GetSkills`, or URL-encode the whole skill name as one path parameter. `If-Match` requires a revision; `If-None-Match` skips unchanged content. Any role can read it, and so can anonymous callers when the project's default access is Viewer.

### Example

```python
import notehub_py
from notehub_py.models.skill import Skill
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.SkillsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    skill_name = "references/devices.md"  # str | Relative .md name, case-insensitive, at most 512 UTF-8 bytes. In URLs, encode the whole name once: references/devices.md becomes references%2Fdevices.md; a literal % becomes %25. Pass the unencoded name to SDKs. Spaces, Unicode and punctuation are allowed. No absolute paths, dot segments, empty segments, backslashes, colons, control characters or surrounding segment whitespace.
    if_match = "if_match_example"  # str | Optionally require one strong ETag or quoted skill revision; wildcards and weak tags are rejected. (optional)
    if_none_match = "if_none_match_example"  # str | Return 304 if an ETag for this skill matches, or use * to match any existing skill at this name. (optional)

    try:
        # Get a project skill
        api_response = api_instance.get_skill(
            project_or_product_uid,
            skill_name,
            if_match=if_match,
            if_none_match=if_none_match,
        )
        print("The response of SkillsApi->get_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->get_skill: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                  | Notes      |
| -------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str** |                                                                                                                                                                                                                                                                                                                                                                                              |
| **skill_name**             | **str** | Relative .md name, case-insensitive, at most 512 UTF-8 bytes. In URLs, encode the whole name once: references/devices.md becomes references%2Fdevices.md; a literal % becomes %25. Pass the unencoded name to SDKs. Spaces, Unicode and punctuation are allowed. No absolute paths, dot segments, empty segments, backslashes, colons, control characters or surrounding segment whitespace. |
| **if_match**               | **str** | Optionally require one strong ETag or quoted skill revision; wildcards and weak tags are rejected.                                                                                                                                                                                                                                                                                           | [optional] |
| **if_none_match**          | **str** | Return 304 if an ETag for this skill matches, or use \* to match any existing skill at this name.                                                                                                                                                                                                                                                                                            | [optional] |

### Return type

[**Skill**](Skill.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_skills

> SkillSet get_skills(project_or_product_uid, include_content=include_content, if_none_match=if_none_match)

List project skills

List a project's skills, the Markdown guides agents read, with metadata only unless `includeContent=true`. Not paginated; a project with none returns `skills: []`. On 413, list metadata and use `GetSkill` for each document. Subprojects read their parent's skills. Any role can read them, and so can anonymous callers when the project's default access is Viewer.

### Example

```python
import notehub_py
from notehub_py.models.skill_set import SkillSet
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.SkillsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    include_content = False  # bool | Use true to include exact Markdown content. Omit or use false for metadata only. (optional) (default to False)
    if_none_match = "if_none_match_example"  # str | Return 304 if an ETag from GetSkills matches, or use * to match any current representation. (optional)

    try:
        # List project skills
        api_response = api_instance.get_skills(
            project_or_product_uid,
            include_content=include_content,
            if_none_match=if_none_match,
        )
        print("The response of SkillsApi->get_skills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->get_skills: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                                                                                  | Notes                         |
| -------------------------- | -------- | -------------------------------------------------------------------------------------------- | ----------------------------- |
| **project_or_product_uid** | **str**  |                                                                                              |
| **include_content**        | **bool** | Use true to include exact Markdown content. Omit or use false for metadata only.             | [optional] [default to False] |
| **if_none_match**          | **str**  | Return 304 if an ETag from GetSkills matches, or use \* to match any current representation. | [optional]                    |

### Return type

[**SkillSet**](SkillSet.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## put_skill

> SkillWriteResult put_skill(project_or_product_uid, skill_name, skill_write, if_match=if_match, if_none_match=if_none_match)

Create or replace a project skill

Create a skill with `If-None-Match: *`, or replace it with `If-Match` set to the revision from `GetSkill`. Send `content` and optional `kinds`; omit `kinds` to keep them, or send `[]` to clear them. An identical write returns unchanged. Requires the Owner or Developer role. Subprojects must write to their parent project.

### Example

```python
import notehub_py
from notehub_py.models.skill_write import SkillWrite
from notehub_py.models.skill_write_result import SkillWriteResult
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.SkillsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    skill_name = "references/devices.md"  # str | Relative .md name, case-insensitive, at most 512 UTF-8 bytes. In URLs, encode the whole name once: references/devices.md becomes references%2Fdevices.md; a literal % becomes %25. Pass the unencoded name to SDKs. Spaces, Unicode and punctuation are allowed. No absolute paths, dot segments, empty segments, backslashes, colons, control characters or surrounding segment whitespace.
    skill_write = {"content": "# Project guide\n", "kinds": ["index"]}  # SkillWrite |
    if_match = "if_match_example"  # str | Required for replacement; use one strong ETag or quoted skill revision. Wildcards and weak tags are rejected. (optional)
    if_none_match = "if_none_match_example"  # str | Use * to create only if the name is absent; cannot be combined with If-Match. (optional)

    try:
        # Create or replace a project skill
        api_response = api_instance.put_skill(
            project_or_product_uid,
            skill_name,
            skill_write,
            if_match=if_match,
            if_none_match=if_none_match,
        )
        print("The response of SkillsApi->put_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->put_skill: %s\n" % e)
```

### Parameters

| Name                       | Type                            | Description                                                                                                                                                                                                                                                                                                                                                                                  | Notes      |
| -------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**                         |                                                                                                                                                                                                                                                                                                                                                                                              |
| **skill_name**             | **str**                         | Relative .md name, case-insensitive, at most 512 UTF-8 bytes. In URLs, encode the whole name once: references/devices.md becomes references%2Fdevices.md; a literal % becomes %25. Pass the unencoded name to SDKs. Spaces, Unicode and punctuation are allowed. No absolute paths, dot segments, empty segments, backslashes, colons, control characters or surrounding segment whitespace. |
| **skill_write**            | [**SkillWrite**](SkillWrite.md) |                                                                                                                                                                                                                                                                                                                                                                                              |
| **if_match**               | **str**                         | Required for replacement; use one strong ETag or quoted skill revision. Wildcards and weak tags are rejected.                                                                                                                                                                                                                                                                                | [optional] |
| **if_none_match**          | **str**                         | Use \* to create only if the name is absent; cannot be combined with If-Match.                                                                                                                                                                                                                                                                                                               | [optional] |

### Return type

[**SkillWriteResult**](SkillWriteResult.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json
