# notehub_py.DeviceApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                                              | HTTP request                                                                                  | Description                                  |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [**add_db_note**](DeviceApi.md#add_db_note)                                                         | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}/{noteID}   | Add a note to a .db notefile                 |
| [**add_qi_note**](DeviceApi.md#add_qi_note)                                                         | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}            | Queue a note for a Notecard                  |
| [**create_notefile**](DeviceApi.md#create_notefile)                                                 | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notefiles/{notefileID}        | Create an empty notefile                     |
| [**delete_device**](DeviceApi.md#delete_device)                                                     | **DELETE** /v1/projects/{projectOrProductUID}/devices/{deviceUID}                             | Delete a device                              |
| [**delete_device_environment_variable**](DeviceApi.md#delete_device_environment_variable)           | **DELETE** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/environment_variables/{key} | Delete a device environment variable         |
| [**delete_note**](DeviceApi.md#delete_note)                                                         | **DELETE** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}/{noteID} | Delete a note                                |
| [**delete_notefiles**](DeviceApi.md#delete_notefiles)                                               | **DELETE** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/files                       | Delete notefiles                             |
| [**disable_device**](DeviceApi.md#disable_device)                                                   | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/disable                       | Disable a device                             |
| [**enable_device**](DeviceApi.md#enable_device)                                                     | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/enable                        | Enable a device                              |
| [**get_db_note**](DeviceApi.md#get_db_note)                                                         | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}/{noteID}    | Get a note                                   |
| [**get_device**](DeviceApi.md#get_device)                                                           | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}                                | Get a device                                 |
| [**get_device_environment_hierarchy**](DeviceApi.md#get_device_environment_hierarchy)               | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/environment_hierarchy          | Get a device&#39;s environment hierarchy     |
| [**get_device_environment_variables**](DeviceApi.md#get_device_environment_variables)               | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/environment_variables          | Get device environment variables             |
| [**get_device_environment_variables_by_pin**](DeviceApi.md#get_device_environment_variables_by_pin) | **GET** /v1/products/{productUID}/devices/{deviceUID}/environment_variables_with_pin          | Get device environment variables using a PIN |
| [**get_device_health_log**](DeviceApi.md#get_device_health_log)                                     | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/health-log                     | Get a device&#39;s health log                |
| [**get_device_journey**](DeviceApi.md#get_device_journey)                                           | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/journeys/{journeyID}           | Get a journey and its events                 |
| [**get_device_journeys**](DeviceApi.md#get_device_journeys)                                         | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/journeys                       | List a device&#39;s journeys                 |
| [**get_device_latest_events**](DeviceApi.md#get_device_latest_events)                               | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/latest                         | Get a device&#39;s latest event per notefile |
| [**get_device_plans**](DeviceApi.md#get_device_plans)                                               | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/plans                          | Get a device&#39;s cellular data plans       |
| [**get_device_public_key**](DeviceApi.md#get_device_public_key)                                     | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/public-key                     | Get a device&#39;s public key                |
| [**get_device_public_keys**](DeviceApi.md#get_device_public_keys)                                   | **GET** /v1/projects/{projectOrProductUID}/devices/public-keys                                | List public keys of all devices              |
| [**get_device_sessions**](DeviceApi.md#get_device_sessions)                                         | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/sessions                       | List a device&#39;s sessions                 |
| [**get_devices**](DeviceApi.md#get_devices)                                                         | **GET** /v1/projects/{projectOrProductUID}/devices                                            | List devices in a project                    |
| [**get_fleet_devices**](DeviceApi.md#get_fleet_devices)                                             | **GET** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}/devices                          | List devices in a fleet                      |
| [**get_notefile**](DeviceApi.md#get_notefile)                                                       | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}             | Get the notes in a notefile                  |
| [**get_sessions**](DeviceApi.md#get_sessions)                                                       | **GET** /v1/projects/{projectOrProductUID}/sessions                                           | List sessions in a project                   |
| [**list_notefiles**](DeviceApi.md#list_notefiles)                                                   | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/files                          | List a device&#39;s notefiles and notes      |
| [**provision_device**](DeviceApi.md#provision_device)                                               | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/provision                     | Provision a Notecard                         |
| [**set_device_environment_variables**](DeviceApi.md#set_device_environment_variables)               | **PUT** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/environment_variables          | Set device environment variables             |
| [**set_device_environment_variables_by_pin**](DeviceApi.md#set_device_environment_variables_by_pin) | **PUT** /v1/products/{productUID}/devices/{deviceUID}/environment_variables_with_pin          | Set device environment variables using a PIN |
| [**signal_device**](DeviceApi.md#signal_device)                                                     | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/signal                        | Send a signal to a connected Notecard        |
| [**update_db_note**](DeviceApi.md#update_db_note)                                                   | **PUT** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}/{noteID}    | Update a note in a .db notefile              |

## add_db_note

> add_db_note(project_or_product_uid, device_uid, notefile_id, note_id, note_input)

Add a note to a .db notefile

Add a note with the given ID to a database notefile on a device, synced to the Notecard on its next sync. To change an existing note, use `UpdateDbNote`; to queue a note in a `.qi` notefile, use `AddQiNote`. Requires the Owner or Developer role. Returns 400 unless the notefile ends in `.db` or `.dbs`, or if `payload` isn't valid base64.

### Example

```python
import notehub_py
from notehub_py.models.note_input import NoteInput
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    notefile_id = "notefile_id_example"  # str | Notefile name, including its extension, e.g. `config.db` or `commands.qi`.
    note_id = "note_id_example"  # str | Note ID within the notefile, e.g. `my_note`. Notes in a `.qi` notefile have IDs like `1:435`.
    note_input = (
        notehub_py.NoteInput()
    )  # NoteInput | Body or payload of note to be added to the device

    try:
        # Add a note to a .db notefile
        api_instance.add_db_note(
            project_or_product_uid, device_uid, notefile_id, note_id, note_input
        )
    except Exception as e:
        print("Exception when calling DeviceApi->add_db_note: %s\n" % e)
```

### Parameters

| Name                       | Type                          | Description                                                                                                                 | Notes |
| -------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                       |                                                                                                                             |
| **device_uid**             | **str**                       |                                                                                                                             |
| **notefile_id**            | **str**                       | Notefile name, including its extension, e.g. &#x60;config.db&#x60; or &#x60;commands.qi&#x60;.                              |
| **note_id**                | **str**                       | Note ID within the notefile, e.g. &#x60;my_note&#x60;. Notes in a &#x60;.qi&#x60; notefile have IDs like &#x60;1:435&#x60;. |
| **note_input**             | [**NoteInput**](NoteInput.md) | Body or payload of note to be added to the device                                                                           |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## add_qi_note

> add_qi_note(project_or_product_uid, device_uid, notefile_id, note_input)

Queue a note for a Notecard

Add a note to an inbound queue (`.qi`) notefile on a device, creating the notefile if needed. The Notecard receives it on its next sync. For a `.db` notefile, use `AddDbNote`; to reach a connected Notecard immediately, use `SignalDevice`. Requires the Owner or Developer role. Returns 400 unless the notefile ends in `.qi` or `.qis`, or if `payload` isn't valid base64.

### Example

```python
import notehub_py
from notehub_py.models.note_input import NoteInput
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    notefile_id = "notefile_id_example"  # str | Notefile name, including its extension, e.g. `config.db` or `commands.qi`.
    note_input = (
        notehub_py.NoteInput()
    )  # NoteInput | Body or payload of note to be added to the device

    try:
        # Queue a note for a Notecard
        api_instance.add_qi_note(
            project_or_product_uid, device_uid, notefile_id, note_input
        )
    except Exception as e:
        print("Exception when calling DeviceApi->add_qi_note: %s\n" % e)
```

### Parameters

| Name                       | Type                          | Description                                                                                    | Notes |
| -------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                       |                                                                                                |
| **device_uid**             | **str**                       |                                                                                                |
| **notefile_id**            | **str**                       | Notefile name, including its extension, e.g. &#x60;config.db&#x60; or &#x60;commands.qi&#x60;. |
| **note_input**             | [**NoteInput**](NoteInput.md) | Body or payload of note to be added to the device                                              |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## create_notefile

> create_notefile(project_or_product_uid, device_uid, notefile_id)

Create an empty notefile

Create an empty notefile on a device. `AddQiNote` creates a notefile when needed, so this is only required for an empty one. Requires the Owner or Developer role. Returns 400 if the notefile already exists.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    notefile_id = "notefile_id_example"  # str | Notefile name, including its extension, e.g. `config.db` or `commands.qi`.

    try:
        # Create an empty notefile
        api_instance.create_notefile(project_or_product_uid, device_uid, notefile_id)
    except Exception as e:
        print("Exception when calling DeviceApi->create_notefile: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                    | Notes |
| -------------------------- | ------- | ---------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                                |
| **device_uid**             | **str** |                                                                                                |
| **notefile_id**            | **str** | Notefile name, including its extension, e.g. &#x60;config.db&#x60; or &#x60;commands.qi&#x60;. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_device

> delete_device(project_or_product_uid, device_uid)

Delete a device

Delete a device and its notefiles from a project. Its events are kept. A Notecard that syncs again is added back as a new device; to block it instead, use `DisableDevice`. Requires the Owner or Developer role.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |

    try:
        # Delete a device
        api_instance.delete_device(project_or_product_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_device: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_device_environment_variable

> EnvironmentVariables delete_device_environment_variable(project_or_product_uid, device_uid, key)

Delete a device environment variable

Delete one device environment variable and return the ones left. Fleet and project variables with the same name then apply. Deleting a variable that doesn't exist succeeds. Requires the Owner or Developer role.

### Example

```python
import notehub_py
from notehub_py.models.environment_variables import EnvironmentVariables
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    key = "key_example"  # str | The environment variable key to delete.

    try:
        # Delete a device environment variable
        api_response = api_instance.delete_device_environment_variable(
            project_or_product_uid, device_uid, key
        )
        print("The response of DeviceApi->delete_device_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling DeviceApi->delete_device_environment_variable: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description                             | Notes |
| -------------------------- | ------- | --------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                         |
| **device_uid**             | **str** |                                         |
| **key**                    | **str** | The environment variable key to delete. |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_note

> delete_note(project_or_product_uid, device_uid, notefile_id, note_id)

Delete a note

Delete one note from a notefile on a device. To delete whole notefiles, use `DeleteNotefiles`. Requires the Owner or Developer role.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    notefile_id = "notefile_id_example"  # str | Notefile name, including its extension, e.g. `config.db` or `commands.qi`.
    note_id = "note_id_example"  # str | Note ID within the notefile, e.g. `my_note`. Notes in a `.qi` notefile have IDs like `1:435`.

    try:
        # Delete a note
        api_instance.delete_note(
            project_or_product_uid, device_uid, notefile_id, note_id
        )
    except Exception as e:
        print("Exception when calling DeviceApi->delete_note: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                                                 | Notes |
| -------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                                                             |
| **device_uid**             | **str** |                                                                                                                             |
| **notefile_id**            | **str** | Notefile name, including its extension, e.g. &#x60;config.db&#x60; or &#x60;commands.qi&#x60;.                              |
| **note_id**                | **str** | Note ID within the notefile, e.g. &#x60;my_note&#x60;. Notes in a &#x60;.qi&#x60; notefile have IDs like &#x60;1:435&#x60;. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_notefiles

> delete_notefiles(project_or_product_uid, device_uid, delete_notefiles_request)

Delete notefiles

Delete notefiles and all their notes from a device. To delete one note, use `DeleteNote`. Requires the Owner or Developer role. Returns 400 if `files` is empty.

### Example

```python
import notehub_py
from notehub_py.models.delete_notefiles_request import DeleteNotefilesRequest
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    delete_notefiles_request = (
        notehub_py.DeleteNotefilesRequest()
    )  # DeleteNotefilesRequest | The notefiles to delete.

    try:
        # Delete notefiles
        api_instance.delete_notefiles(
            project_or_product_uid, device_uid, delete_notefiles_request
        )
    except Exception as e:
        print("Exception when calling DeviceApi->delete_notefiles: %s\n" % e)
```

### Parameters

| Name                         | Type                                                    | Description              | Notes |
| ---------------------------- | ------------------------------------------------------- | ------------------------ | ----- |
| **project_or_product_uid**   | **str**                                                 |                          |
| **device_uid**               | **str**                                                 |                          |
| **delete_notefiles_request** | [**DeleteNotefilesRequest**](DeleteNotefilesRequest.md) | The notefiles to delete. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## disable_device

> disable_device(project_or_product_uid, device_uid)

Disable a device

Stop a device from connecting to Notehub, ending any open session. The device and its data stay in the project; undo with `EnableDevice`. Does nothing if it's already disabled. Requires the Owner or Developer role.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |

    try:
        # Disable a device
        api_instance.disable_device(project_or_product_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->disable_device: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## enable_device

> enable_device(project_or_product_uid, device_uid)

Enable a device

Re-enable a device turned off with `DisableDevice`, so it can connect to Notehub again. Does nothing if the device is already enabled. Requires the Owner or Developer role. Returns 409 if the device's cellular service was deactivated; it must be reactivated instead.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |

    try:
        # Enable a device
        api_instance.enable_device(project_or_product_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->enable_device: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_db_note

> GetDbNote200Response get_db_note(project_or_product_uid, device_uid, notefile_id, note_id, delete=delete, deleted=deleted)

Get a note

Get one note's body, payload and time from a notefile on a device. To get every note in a notefile, use `GetNotefile`. With `delete=true`, the note is deleted after it is read, which requires the Owner or Developer role.

### Example

```python
import notehub_py
from notehub_py.models.get_db_note200_response import GetDbNote200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    notefile_id = "notefile_id_example"  # str | Notefile name, including its extension, e.g. `config.db` or `commands.qi`.
    note_id = "note_id_example"  # str | Note ID within the notefile, e.g. `my_note`. Notes in a `.qi` notefile have IDs like `1:435`.
    delete = True  # bool | If true, delete the note after returning it. Requires the Owner or Developer role. (optional)
    deleted = (
        True  # bool | If true, also return the note if it has been deleted. (optional)
    )

    try:
        # Get a note
        api_response = api_instance.get_db_note(
            project_or_product_uid,
            device_uid,
            notefile_id,
            note_id,
            delete=delete,
            deleted=deleted,
        )
        print("The response of DeviceApi->get_db_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_db_note: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                                                                                                                 | Notes      |
| -------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**  |                                                                                                                             |
| **device_uid**             | **str**  |                                                                                                                             |
| **notefile_id**            | **str**  | Notefile name, including its extension, e.g. &#x60;config.db&#x60; or &#x60;commands.qi&#x60;.                              |
| **note_id**                | **str**  | Note ID within the notefile, e.g. &#x60;my_note&#x60;. Notes in a &#x60;.qi&#x60; notefile have IDs like &#x60;1:435&#x60;. |
| **delete**                 | **bool** | If true, delete the note after returning it. Requires the Owner or Developer role.                                          | [optional] |
| **deleted**                | **bool** | If true, also return the note if it has been deleted.                                                                       | [optional] |

### Return type

[**GetDbNote200Response**](GetDbNote200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device

> Device get_device(project_or_product_uid, device_uid)

Get a device

Get one device's details: serial number, product, fleets, locations, firmware versions, SIM usage and DFU state. To find devices by tag, serial number or other fields, use `GetDevices`.

### Example

```python
import notehub_py
from notehub_py.models.device import Device
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |

    try:
        # Get a device
        api_response = api_instance.get_device(project_or_product_uid, device_uid)
        print("The response of DeviceApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**Device**](Device.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_environment_hierarchy

> EnvTreeJsonNode get_device_environment_hierarchy(project_or_product_uid, device_uid)

Get a device's environment hierarchy

Get a device's environment variables and the fleet and project variables it inherits, as a tree. Each variable has its precedence and whether it is used or overridden. For just the resolved values, use `GetDeviceEnvironmentVariables`.

### Example

```python
import notehub_py
from notehub_py.models.env_tree_json_node import EnvTreeJsonNode
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |

    try:
        # Get a device's environment hierarchy
        api_response = api_instance.get_device_environment_hierarchy(
            project_or_product_uid, device_uid
        )
        print("The response of DeviceApi->get_device_environment_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling DeviceApi->get_device_environment_hierarchy: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**EnvTreeJsonNode**](EnvTreeJsonNode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_environment_variables

> GetDeviceEnvironmentVariablesByPin200Response get_device_environment_variables(project_or_product_uid, device_uid)

Get device environment variables

Get a device's own environment variables, its `env.default` values, and its effective values. Effective values merge in project and fleet variables, which device variables override. To see where each value comes from, use `GetDeviceEnvironmentHierarchy`.

### Example

```python
import notehub_py
from notehub_py.models.get_device_environment_variables_by_pin200_response import (
    GetDeviceEnvironmentVariablesByPin200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |

    try:
        # Get device environment variables
        api_response = api_instance.get_device_environment_variables(
            project_or_product_uid, device_uid
        )
        print("The response of DeviceApi->get_device_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling DeviceApi->get_device_environment_variables: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**GetDeviceEnvironmentVariablesByPin200Response**](GetDeviceEnvironmentVariablesByPin200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_environment_variables_by_pin

> GetDeviceEnvironmentVariablesByPin200Response get_device_environment_variables_by_pin(product_uid, device_uid, x_auth_token)

Get device environment variables using a PIN

Get a device's environment variables using its PIN instead of an API token. Pass the PIN in `X-Auth-Token`. Made for device dashboard pages; with a token, use `GetDeviceEnvironmentVariables`, which also returns effective values. Returns 401 if the project's device dashboard URL has no `[pin]`, or the PIN is wrong.

### Example

```python
import notehub_py
from notehub_py.models.get_device_environment_variables_by_pin200_response import (
    GetDeviceEnvironmentVariablesByPin200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    device_uid = "dev:000000000000000"  # str |
    x_auth_token = (
        "x_auth_token_example"  # str | The device's PIN, used instead of an API token.
    )

    try:
        # Get device environment variables using a PIN
        api_response = api_instance.get_device_environment_variables_by_pin(
            product_uid, device_uid, x_auth_token
        )
        print("The response of DeviceApi->get_device_environment_variables_by_pin:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling DeviceApi->get_device_environment_variables_by_pin: %s\n"
            % e
        )
```

### Parameters

| Name             | Type    | Description                                         | Notes |
| ---------------- | ------- | --------------------------------------------------- | ----- |
| **product_uid**  | **str** |                                                     |
| **device_uid**   | **str** |                                                     |
| **x_auth_token** | **str** | The device&#39;s PIN, used instead of an API token. |

### Return type

[**GetDeviceEnvironmentVariablesByPin200Response**](GetDeviceEnvironmentVariablesByPin200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_health_log

> GetDeviceHealthLog200Response get_device_health_log(project_or_product_uid, device_uid, start_date=start_date, end_date=end_date, log_type=log_type)

Get a device's health log

Get a device's health log: timestamped status messages such as restarts and completed firmware updates. Only the latest 100 entries are kept. To filter by date, pass both `startDate` and `endDate`; `startDate` alone returns 400, and the same value for both returns every entry.

### Example

```python
import notehub_py
from notehub_py.models.get_device_health_log200_response import (
    GetDeviceHealthLog200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)
    log_type = [
        "log_type_example"
    ]  # List[str] | Return only these kinds of entry. If omitted, all entries are returned. - `boot`: the device restarted - `dfu_completed`: a host firmware update finished  (optional)

    try:
        # Get a device's health log
        api_response = api_instance.get_device_health_log(
            project_or_product_uid,
            device_uid,
            start_date=start_date,
            end_date=end_date,
            log_type=log_type,
        )
        print("The response of DeviceApi->get_device_health_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_health_log: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                   | Notes      |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                               |
| **device_uid**             | **str**                 |                                                                                                                                                                               |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                                                                                               | [optional] |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                                                                                                 | [optional] |
| **log_type**               | [**List[str]**](str.md) | Return only these kinds of entry. If omitted, all entries are returned. - &#x60;boot&#x60;: the device restarted - &#x60;dfu_completed&#x60;: a host firmware update finished | [optional] |

### Return type

[**GetDeviceHealthLog200Response**](GetDeviceHealthLog200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_journey

> GetDeviceJourney200Response get_device_journey(project_or_product_uid, device_uid, journey_id, page_size=page_size, page_num=page_num)

Get a journey and its events

Get one journey's start and end time and its events, oldest first. Only events with a location are included, and a run of events at the same location is reduced to the first. The events are paginated; `journey.has_more` is true if there are more. Returns 404 if the journey doesn't exist, and 403 if the organization is suspended.

### Example

```python
import notehub_py
from notehub_py.models.get_device_journey200_response import GetDeviceJourney200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    journey_id = 56  # int | Identifier of the journey, taken from the numeric `journey` field in the event body (a Unix timestamp marking the start of the journey).
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)

    try:
        # Get a journey and its events
        api_response = api_instance.get_device_journey(
            project_or_product_uid,
            device_uid,
            journey_id,
            page_size=page_size,
            page_num=page_num,
        )
        print("The response of DeviceApi->get_device_journey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_journey: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                                                                        | Notes                        |
| -------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **project_or_product_uid** | **str** |                                                                                                                                                    |
| **device_uid**             | **str** |                                                                                                                                                    |
| **journey_id**             | **int** | Identifier of the journey, taken from the numeric &#x60;journey&#x60; field in the event body (a Unix timestamp marking the start of the journey). |
| **page_size**              | **int** |                                                                                                                                                    | [optional] [default to 1000] |
| **page_num**               | **int** |                                                                                                                                                    | [optional] [default to 1]    |

### Return type

[**GetDeviceJourney200Response**](GetDeviceJourney200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_journeys

> GetDeviceJourneys200Response get_device_journeys(project_or_product_uid, device_uid, start_date=start_date, end_date=end_date)

List a device's journeys

List a device's journeys, newest first, without their events. A journey is the events whose body has the same `journey` value and a `jcount` field; one-event journeys are left out. For a journey's events, use `GetDeviceJourney`. Returns at most 100; `has_more` is true if there are more. `startDate` and `endDate` filter on the journey's start. Returns 403 if the organization is suspended.

### Example

```python
import notehub_py
from notehub_py.models.get_device_journeys200_response import (
    GetDeviceJourneys200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)

    try:
        # List a device's journeys
        api_response = api_instance.get_device_journeys(
            project_or_product_uid, device_uid, start_date=start_date, end_date=end_date
        )
        print("The response of DeviceApi->get_device_journeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_journeys: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                     | Notes      |
| -------------------------- | ------- | --------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str** |                                                                 |
| **device_uid**             | **str** |                                                                 |
| **start_date**             | **int** | Start date for filtering results, specified as a Unix timestamp | [optional] |
| **end_date**               | **int** | End date for filtering results, specified as a Unix timestamp   | [optional] |

### Return type

[**GetDeviceJourneys200Response**](GetDeviceJourneys200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_latest_events

> GetDeviceLatestEvents200Response get_device_latest_events(project_or_product_uid, device_uid)

Get a device's latest event per notefile

Get the most recent event from each of a device's notefiles, sorted by notefile name. `_env.qo` is left out. To search a device's event history, use `GetEvents`. Returns 403 if the organization is suspended.

### Example

```python
import notehub_py
from notehub_py.models.get_device_latest_events200_response import (
    GetDeviceLatestEvents200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |

    try:
        # Get a device's latest event per notefile
        api_response = api_instance.get_device_latest_events(
            project_or_product_uid, device_uid
        )
        print("The response of DeviceApi->get_device_latest_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_latest_events: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**GetDeviceLatestEvents200Response**](GetDeviceLatestEvents200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_plans

> GetDevicePlans200Response get_device_plans(project_or_product_uid, device_uid)

Get a device's cellular data plans

Get the data plan of each cellular SIM in a device: plan type, data used and remaining, and expiry. Covers the built-in SIM and any external SIM, but not satellite plans. Returns 404 if the device has no cellular or satellite SIM.

### Example

```python
import notehub_py
from notehub_py.models.get_device_plans200_response import GetDevicePlans200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |

    try:
        # Get a device's cellular data plans
        api_response = api_instance.get_device_plans(project_or_product_uid, device_uid)
        print("The response of DeviceApi->get_device_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_plans: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**GetDevicePlans200Response**](GetDevicePlans200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_public_key

> GetDevicePublicKey200Response get_device_public_key(project_or_product_uid, device_uid)

Get a device's public key

Get one Notecard's public key, in PEM format. For every device in the project, use `GetDevicePublicKeys`.

### Example

```python
import notehub_py
from notehub_py.models.get_device_public_key200_response import (
    GetDevicePublicKey200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |

    try:
        # Get a device's public key
        api_response = api_instance.get_device_public_key(
            project_or_product_uid, device_uid
        )
        print("The response of DeviceApi->get_device_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_public_key: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**GetDevicePublicKey200Response**](GetDevicePublicKey200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_public_keys

> GetDevicePublicKeys200Response get_device_public_keys(project_or_product_uid, page_size=page_size, page_num=page_num, cursor=cursor)

List public keys of all devices

List the public key of every device in a project. For one device, use `GetDevicePublicKey`. Paginated. Deleted devices are included only when reading with a `cursor`.

### Example

```python
import notehub_py
from notehub_py.models.get_device_public_keys200_response import (
    GetDevicePublicKeys200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)
    cursor = "cursor_example"  # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)

    try:
        # List public keys of all devices
        api_response = api_instance.get_device_public_keys(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
            cursor=cursor,
        )
        print("The response of DeviceApi->get_device_public_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_public_keys: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                        |
| -------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **project_or_product_uid** | **str** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **page_size**              | **int** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000] |
| **page_num**               | **int** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]    |
| **cursor**                 | **str** | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                   |

### Return type

[**GetDevicePublicKeys200Response**](GetDevicePublicKeys200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_sessions

> GetDeviceSessions200Response get_device_sessions(project_or_product_uid, device_uid, page_size=page_size, page_num=page_num, cursor=cursor, start_date=start_date, end_date=end_date, first_sync=first_sync)

List a device's sessions

List a device's sessions, its connections to Notehub. Each shows why it opened and closed, signal strength, location and data usage. `startDate` and `endDate` filter on when the session began. For every device's sessions, use `GetSessions`. Paginated.

### Example

```python
import notehub_py
from notehub_py.models.get_device_sessions200_response import (
    GetDeviceSessions200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)
    cursor = "cursor_example"  # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)
    first_sync = False  # bool | If true, return only sessions whose `why_session_opened` begins with \"first sync\". (optional) (default to False)

    try:
        # List a device's sessions
        api_response = api_instance.get_device_sessions(
            project_or_product_uid,
            device_uid,
            page_size=page_size,
            page_num=page_num,
            cursor=cursor,
            start_date=start_date,
            end_date=end_date,
            first_sync=first_sync,
        )
        print("The response of DeviceApi->get_device_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_sessions: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                         |
| -------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **project_or_product_uid** | **str**  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **device_uid**             | **str**  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **page_size**              | **int**  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000]  |
| **page_num**               | **int**  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]     |
| **cursor**                 | **str**  | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                    |
| **start_date**             | **int**  | Start date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                                                                                                                         | [optional]                    |
| **end_date**               | **int**  | End date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                                                                                                                           | [optional]                    |
| **first_sync**             | **bool** | If true, return only sessions whose &#x60;why_session_opened&#x60; begins with \&quot;first sync\&quot;.                                                                                                                                                                                                                                                                                                                                                                | [optional] [default to False] |

### Return type

[**GetDeviceSessions200Response**](GetDeviceSessions200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_devices

> GetDevices200Response get_devices(project_or_product_uid, page_size=page_size, page_num=page_num, cursor=cursor, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)

List devices in a project

List the devices in a project, with optional filters such as tag, serial number, fleet, location and firmware version. For one fleet's devices, use `GetFleetDevices`. Paginated.

### Example

```python
import notehub_py
from notehub_py.models.get_devices200_response import GetDevices200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)
    cursor = "cursor_example"  # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    tag = [
        "tag_example"
    ]  # List[str] | Tag filter. Matches the whole tag, case-insensitive. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. For example, `51*` matches tags starting with `51`. (optional)
    serial_number = [
        "serial_number_example"
    ]  # List[str] | Serial number filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    fleet_uid = ["fleet_uid_example"]  # List[str] |  (optional)
    notecard_firmware = [
        "notecard_firmware_example"
    ]  # List[str] | Firmware version filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    location = [
        "location_example"
    ]  # List[str] | Location filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    host_firmware = [
        "host_firmware_example"
    ]  # List[str] | Host firmware filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    product_uid = [
        "product_uid_example"
    ]  # List[str] | ProductUID filter. Matches any value containing the filter text, case-insensitive. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    sku = [
        "sku_example"
    ]  # List[str] | SKU filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)

    try:
        # List devices in a project
        api_response = api_instance.get_devices(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
            cursor=cursor,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
        )
        print("The response of DeviceApi->get_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_devices: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                        |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **page_size**              | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000] |
| **page_num**               | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]    |
| **cursor**                 | **str**                 | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                   |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [optional]                   |
| **tag**                    | [**List[str]**](str.md) | Tag filter. Matches the whole tag, case-insensitive. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;_&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally. For example, &#x60;51_&#x60; matches tags starting with &#x60;51&#x60;.                                                                                                                                                                   | [optional]                   |
| **serial_number**          | [**List[str]**](str.md) | Serial number filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                           | [optional]                   |
| **fleet_uid**              | [**List[str]**](str.md) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional]                   |
| **notecard_firmware**      | [**List[str]**](str.md) | Firmware version filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                        | [optional]                   |
| **location**               | [**List[str]**](str.md) | Location filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                                | [optional]                   |
| **host_firmware**          | [**List[str]**](str.md) | Host firmware filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                           | [optional]                   |
| **product_uid**            | [**List[str]**](str.md) | ProductUID filter. Matches any value containing the filter text, case-insensitive. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                            | [optional]                   |
| **sku**                    | [**List[str]**](str.md) | SKU filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                                     | [optional]                   |

### Return type

[**GetDevices200Response**](GetDevices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_fleet_devices

> GetDevices200Response get_fleet_devices(project_or_product_uid, fleet_uid, page_size=page_size, page_num=page_num, cursor=cursor, device_uid=device_uid, tag=tag, serial_number=serial_number, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)

List devices in a fleet

List the devices in one fleet, with the same filters as `GetDevices`. To list a device's fleets instead, use `GetDeviceFleets`. Paginated. Returns 404 if the fleet doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.get_devices200_response import GetDevices200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    fleet_uid = "fleet_uid_example"  # str |
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)
    cursor = "cursor_example"  # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    tag = [
        "tag_example"
    ]  # List[str] | Tag filter. Matches the whole tag, case-insensitive. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. For example, `51*` matches tags starting with `51`. (optional)
    serial_number = [
        "serial_number_example"
    ]  # List[str] | Serial number filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    notecard_firmware = [
        "notecard_firmware_example"
    ]  # List[str] | Firmware version filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    location = [
        "location_example"
    ]  # List[str] | Location filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    host_firmware = [
        "host_firmware_example"
    ]  # List[str] | Host firmware filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    product_uid = [
        "product_uid_example"
    ]  # List[str] | ProductUID filter. Matches any value containing the filter text, case-insensitive. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    sku = [
        "sku_example"
    ]  # List[str] | SKU filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)

    try:
        # List devices in a fleet
        api_response = api_instance.get_fleet_devices(
            project_or_product_uid,
            fleet_uid,
            page_size=page_size,
            page_num=page_num,
            cursor=cursor,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
        )
        print("The response of DeviceApi->get_fleet_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_fleet_devices: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                        |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **fleet_uid**              | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **page_size**              | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000] |
| **page_num**               | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]    |
| **cursor**                 | **str**                 | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                   |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [optional]                   |
| **tag**                    | [**List[str]**](str.md) | Tag filter. Matches the whole tag, case-insensitive. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;_&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally. For example, &#x60;51_&#x60; matches tags starting with &#x60;51&#x60;.                                                                                                                                                                   | [optional]                   |
| **serial_number**          | [**List[str]**](str.md) | Serial number filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                           | [optional]                   |
| **notecard_firmware**      | [**List[str]**](str.md) | Firmware version filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                        | [optional]                   |
| **location**               | [**List[str]**](str.md) | Location filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                                | [optional]                   |
| **host_firmware**          | [**List[str]**](str.md) | Host firmware filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                           | [optional]                   |
| **product_uid**            | [**List[str]**](str.md) | ProductUID filter. Matches any value containing the filter text, case-insensitive. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                            | [optional]                   |
| **sku**                    | [**List[str]**](str.md) | SKU filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                                     | [optional]                   |

### Return type

[**GetDevices200Response**](GetDevices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_notefile

> GetNotefile200Response get_notefile(project_or_product_uid, device_uid, notefile_id, max=max, deleted=deleted, delete=delete)

Get the notes in a notefile

Get the notes in one notefile on a device. For a `.qi` notefile, that's the notes still queued; for a `.db` notefile, every note. To list all of a device's notefiles with their notes, use `ListNotefiles`. With `delete=true`, the returned notes are deleted, which requires the Owner or Developer role. Returns 400 if `notefileID` has no valid notefile extension.

### Example

```python
import notehub_py
from notehub_py.models.get_notefile200_response import GetNotefile200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    notefile_id = "notefile_id_example"  # str | Notefile name, including its extension, e.g. `config.db` or `commands.qi`.
    max = 56  # int | The most notes to return. (optional)
    deleted = True  # bool | If true, also return deleted notes. (optional)
    delete = True  # bool | If true, delete the notes this request returns. Requires the Owner or Developer role. (optional)

    try:
        # Get the notes in a notefile
        api_response = api_instance.get_notefile(
            project_or_product_uid,
            device_uid,
            notefile_id,
            max=max,
            deleted=deleted,
            delete=delete,
        )
        print("The response of DeviceApi->get_notefile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_notefile: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                                                                                    | Notes      |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**  |                                                                                                |
| **device_uid**             | **str**  |                                                                                                |
| **notefile_id**            | **str**  | Notefile name, including its extension, e.g. &#x60;config.db&#x60; or &#x60;commands.qi&#x60;. |
| **max**                    | **int**  | The most notes to return.                                                                      | [optional] |
| **deleted**                | **bool** | If true, also return deleted notes.                                                            | [optional] |
| **delete**                 | **bool** | If true, delete the notes this request returns. Requires the Owner or Developer role.          | [optional] |

### Return type

[**GetNotefile200Response**](GetNotefile200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_sessions

> GetDeviceSessions200Response get_sessions(project_or_product_uid, page_size=page_size, page_num=page_num, cursor=cursor, start_date=start_date, end_date=end_date, first_sync=first_sync, device_uid=device_uid, fleet_uid=fleet_uid)

List sessions in a project

List the sessions of every device in a project, as `GetDeviceSessions` does for one device. `startDate` and `endDate` filter on when the session began. `deviceUID` and `fleetUID` each match any of their values; `fleetUID` matches the fleets recorded on the session. Paginated.

### Example

```python
import notehub_py
from notehub_py.models.get_device_sessions200_response import (
    GetDeviceSessions200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)
    cursor = "cursor_example"  # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)
    first_sync = False  # bool | If true, return only sessions whose `why_session_opened` begins with \"first sync\". (optional) (default to False)
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    fleet_uid = ["fleet_uid_example"]  # List[str] |  (optional)

    try:
        # List sessions in a project
        api_response = api_instance.get_sessions(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
            cursor=cursor,
            start_date=start_date,
            end_date=end_date,
            first_sync=first_sync,
            device_uid=device_uid,
            fleet_uid=fleet_uid,
        )
        print("The response of DeviceApi->get_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_sessions: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                         |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **page_size**              | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000]  |
| **page_num**               | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]     |
| **cursor**                 | **str**                 | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                    |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                                                                                                                         | [optional]                    |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                                                                                                                           | [optional]                    |
| **first_sync**             | **bool**                | If true, return only sessions whose &#x60;why_session_opened&#x60; begins with \&quot;first sync\&quot;.                                                                                                                                                                                                                                                                                                                                                                | [optional] [default to False] |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [optional]                    |
| **fleet_uid**              | [**List[str]**](str.md) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional]                    |

### Return type

[**GetDeviceSessions200Response**](GetDeviceSessions200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## list_notefiles

> List[Notefile] list_notefiles(project_or_product_uid, device_uid, files=files, pending=pending)

List a device's notefiles and notes

List a device's notefiles with the notes in each, sorted `.qo`, then `.qi`, then `.db`. `.qo` notefiles are listed without notes, since Notehub empties them as it processes them. Most system notefiles (names starting with `_`) are left out. For one notefile, use `GetNotefile`.

### Example

```python
import notehub_py
from notehub_py.models.notefile import Notefile
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    files = [
        "files_example"
    ]  # List[str] | Notefiles to include, e.g. `config.db`. If omitted, all are listed. (optional)
    pending = (
        True  # bool | show only files that are pending sync to the Notecard (optional)
    )

    try:
        # List a device's notefiles and notes
        api_response = api_instance.list_notefiles(
            project_or_product_uid, device_uid, files=files, pending=pending
        )
        print("The response of DeviceApi->list_notefiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->list_notefiles: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                   | Notes      |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**                 |                                                                               |
| **device_uid**             | **str**                 |                                                                               |
| **files**                  | [**List[str]**](str.md) | Notefiles to include, e.g. &#x60;config.db&#x60;. If omitted, all are listed. | [optional] |
| **pending**                | **bool**                | show only files that are pending sync to the Notecard                         | [optional] |

### Return type

[**List[Notefile]**](Notefile.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## provision_device

> object provision_device(project_or_product_uid, device_uid, provision_device_request)

Provision a Notecard

Add a Notecard to a project before it first connects, with its product, serial number and fleets. A device that already exists isn't reset and keeps its fleets. Requires the Owner or Developer role. Returns 404 if `product_uid` doesn't exist, and 400 if it belongs to another project or `deviceUID` isn't a valid Notecard DeviceUID.

### Example

```python
import notehub_py
from notehub_py.models.provision_device_request import ProvisionDeviceRequest
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    provision_device_request = (
        notehub_py.ProvisionDeviceRequest()
    )  # ProvisionDeviceRequest | The product, serial number and fleets for the device.

    try:
        # Provision a Notecard
        api_response = api_instance.provision_device(
            project_or_product_uid, device_uid, provision_device_request
        )
        print("The response of DeviceApi->provision_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->provision_device: %s\n" % e)
```

### Parameters

| Name                         | Type                                                    | Description                                           | Notes |
| ---------------------------- | ------------------------------------------------------- | ----------------------------------------------------- | ----- |
| **project_or_product_uid**   | **str**                                                 |                                                       |
| **device_uid**               | **str**                                                 |                                                       |
| **provision_device_request** | [**ProvisionDeviceRequest**](ProvisionDeviceRequest.md) | The product, serial number and fleets for the device. |

### Return type

**object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## set_device_environment_variables

> EnvironmentVariables set_device_environment_variables(project_or_product_uid, device_uid, environment_variables)

Set device environment variables

Add or change a device's environment variables; variables you don't send keep their values. A value of `\"\"` or `-` deletes that variable. Setting `_fw`, `_fwc` or `_fwm` starts a host, Notecard or modem firmware update. Requires the Owner or Developer role. Returns 400 if a note's key isn't a variable.

### Example

```python
import notehub_py
from notehub_py.models.environment_variables import EnvironmentVariables
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    environment_variables = (
        notehub_py.EnvironmentVariables()
    )  # EnvironmentVariables | The variables to add or change, and optional notes.

    try:
        # Set device environment variables
        api_response = api_instance.set_device_environment_variables(
            project_or_product_uid, device_uid, environment_variables
        )
        print("The response of DeviceApi->set_device_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling DeviceApi->set_device_environment_variables: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type                                                | Description                                         | Notes |
| -------------------------- | --------------------------------------------------- | --------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                                             |                                                     |
| **device_uid**             | **str**                                             |                                                     |
| **environment_variables**  | [**EnvironmentVariables**](EnvironmentVariables.md) | The variables to add or change, and optional notes. |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## set_device_environment_variables_by_pin

> EnvironmentVariables set_device_environment_variables_by_pin(product_uid, device_uid, x_auth_token, environment_variables)

Set device environment variables using a PIN

Add or change a device's environment variables using its PIN instead of an API token. Pass the PIN in `X-Auth-Token`. Works like `SetDeviceEnvironmentVariables`: a value of `\"\"` or `-` deletes that variable. Returns 401 if the project's device dashboard URL has no `[pin]`, or the PIN is wrong.

### Example

```python
import notehub_py
from notehub_py.models.environment_variables import EnvironmentVariables
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    device_uid = "dev:000000000000000"  # str |
    x_auth_token = (
        "x_auth_token_example"  # str | The device's PIN, used instead of an API token.
    )
    environment_variables = (
        notehub_py.EnvironmentVariables()
    )  # EnvironmentVariables | The variables to add or change, and optional notes.

    try:
        # Set device environment variables using a PIN
        api_response = api_instance.set_device_environment_variables_by_pin(
            product_uid, device_uid, x_auth_token, environment_variables
        )
        print("The response of DeviceApi->set_device_environment_variables_by_pin:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling DeviceApi->set_device_environment_variables_by_pin: %s\n"
            % e
        )
```

### Parameters

| Name                      | Type                                                | Description                                         | Notes |
| ------------------------- | --------------------------------------------------- | --------------------------------------------------- | ----- |
| **product_uid**           | **str**                                             |                                                     |
| **device_uid**            | **str**                                             |                                                     |
| **x_auth_token**          | **str**                                             | The device&#39;s PIN, used instead of an API token. |
| **environment_variables** | [**EnvironmentVariables**](EnvironmentVariables.md) | The variables to add or change, and optional notes. |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## signal_device

> SignalDevice200Response signal_device(project_or_product_uid, device_uid, body)

Send a signal to a connected Notecard

Send a JSON object straight to a Notecard, which the host can read with `hub.signal`. It's delivered only if the Notecard is connected to Notehub at that moment, and is never queued; `connected` in the response says whether it was. To queue data for the next sync, use `AddQiNote` instead. Requires the Owner or Developer role. Returns 400 if the body has a `type` field.

### Example

```python
import notehub_py
from notehub_py.models.body import Body
from notehub_py.models.signal_device200_response import SignalDevice200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    body = notehub_py.Body()  # Body | The signal to send.

    try:
        # Send a signal to a connected Notecard
        api_response = api_instance.signal_device(
            project_or_product_uid, device_uid, body
        )
        print("The response of DeviceApi->signal_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->signal_device: %s\n" % e)
```

### Parameters

| Name                       | Type                | Description         | Notes |
| -------------------------- | ------------------- | ------------------- | ----- |
| **project_or_product_uid** | **str**             |                     |
| **device_uid**             | **str**             |                     |
| **body**                   | [**Body**](Body.md) | The signal to send. |

### Return type

[**SignalDevice200Response**](SignalDevice200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## update_db_note

> update_db_note(project_or_product_uid, device_uid, notefile_id, note_id, note_input)

Update a note in a .db notefile

Replace the body and payload of a note in a database notefile on a device, synced to the Notecard on its next sync. To add a new note, use `AddDbNote`. Requires the Owner or Developer role. Returns 400 unless the notefile ends in `.db` or `.dbs`, or if `payload` isn't valid base64.

### Example

```python
import notehub_py
from notehub_py.models.note_input import NoteInput
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    notefile_id = "notefile_id_example"  # str | Notefile name, including its extension, e.g. `config.db` or `commands.qi`.
    note_id = "note_id_example"  # str | Note ID within the notefile, e.g. `my_note`. Notes in a `.qi` notefile have IDs like `1:435`.
    note_input = (
        notehub_py.NoteInput()
    )  # NoteInput | Body or payload of note to be added to the device

    try:
        # Update a note in a .db notefile
        api_instance.update_db_note(
            project_or_product_uid, device_uid, notefile_id, note_id, note_input
        )
    except Exception as e:
        print("Exception when calling DeviceApi->update_db_note: %s\n" % e)
```

### Parameters

| Name                       | Type                          | Description                                                                                                                 | Notes |
| -------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                       |                                                                                                                             |
| **device_uid**             | **str**                       |                                                                                                                             |
| **notefile_id**            | **str**                       | Notefile name, including its extension, e.g. &#x60;config.db&#x60; or &#x60;commands.qi&#x60;.                              |
| **note_id**                | **str**                       | Note ID within the notefile, e.g. &#x60;my_note&#x60;. Notes in a &#x60;.qi&#x60; notefile have IDs like &#x60;1:435&#x60;. |
| **note_input**             | [**NoteInput**](NoteInput.md) | Body or payload of note to be added to the device                                                                           |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json
