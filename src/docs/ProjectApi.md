# notehub_py.ProjectApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                                       | HTTP request                                                                                | Description                                              |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| [**add_device_to_fleets**](ProjectApi.md#add_device_to_fleets)                               | **PUT** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/fleets                       | Add a device to fleets                                   |
| [**clone_project**](ProjectApi.md#clone_project)                                             | **POST** /v1/projects/{projectOrProductUID}/clone                                           | Clone a project                                          |
| [**create_fleet**](ProjectApi.md#create_fleet)                                               | **POST** /v1/projects/{projectOrProductUID}/fleets                                          | Create a fleet                                           |
| [**create_product**](ProjectApi.md#create_product)                                           | **POST** /v1/projects/{projectOrProductUID}/products                                        | Create a product                                         |
| [**create_project**](ProjectApi.md#create_project)                                           | **POST** /v1/projects                                                                       | Create a project                                         |
| [**create_project_secret**](ProjectApi.md#create_project_secret)                             | **POST** /v1/projects/{projectOrProductUID}/secrets                                         | Create a project secret                                  |
| [**delete_device_from_fleets**](ProjectApi.md#delete_device_from_fleets)                     | **DELETE** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/fleets                    | Remove a device from fleets                              |
| [**delete_firmware**](ProjectApi.md#delete_firmware)                                         | **DELETE** /v1/projects/{projectOrProductUID}/firmware/{firmwareType}/{filename}            | Delete host firmware                                     |
| [**delete_fleet**](ProjectApi.md#delete_fleet)                                               | **DELETE** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}                             | Delete a fleet                                           |
| [**delete_fleet_environment_variable**](ProjectApi.md#delete_fleet_environment_variable)     | **DELETE** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}/environment_variables/{key} | Delete a fleet environment variable                      |
| [**delete_product**](ProjectApi.md#delete_product)                                           | **DELETE** /v1/projects/{projectOrProductUID}/products/{productUID}                         | Delete a product                                         |
| [**delete_project**](ProjectApi.md#delete_project)                                           | **DELETE** /v1/projects/{projectOrProductUID}                                               | Delete a project                                         |
| [**delete_project_environment_variable**](ProjectApi.md#delete_project_environment_variable) | **DELETE** /v1/projects/{projectOrProductUID}/environment_variables/{key}                   | Delete a project environment variable                    |
| [**delete_project_secret**](ProjectApi.md#delete_project_secret)                             | **DELETE** /v1/projects/{projectOrProductUID}/secrets/{secretName}                          | Delete a project secret                                  |
| [**disable_global_event_transformation**](ProjectApi.md#disable_global_event_transformation) | **POST** /v1/projects/{projectOrProductUID}/global-transformation/disable                   | Disable the global event transformation                  |
| [**download_firmware**](ProjectApi.md#download_firmware)                                     | **GET** /v1/projects/{projectOrProductUID}/firmware/{firmwareType}/{filename}               | Download host firmware                                   |
| [**enable_global_event_transformation**](ProjectApi.md#enable_global_event_transformation)   | **POST** /v1/projects/{projectOrProductUID}/global-transformation/enable                    | Enable the global event transformation                   |
| [**get_aws_role_config**](ProjectApi.md#get_aws_role_config)                                 | **GET** /v1/projects/{projectOrProductUID}/aws-role-config                                  | Get AWS role configuration for role-based authentication |
| [**get_device_dfu_history**](ProjectApi.md#get_device_dfu_history)                           | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/dfu/{firmwareType}/history   | Get a device&#39;s firmware update history               |
| [**get_device_dfu_status**](ProjectApi.md#get_device_dfu_status)                             | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/dfu/{firmwareType}/status    | Get a device&#39;s firmware update status                |
| [**get_device_fleets**](ProjectApi.md#get_device_fleets)                                     | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/fleets                       | List a device&#39;s fleets                               |
| [**get_devices_dfu_history**](ProjectApi.md#get_devices_dfu_history)                         | **GET** /v1/projects/{projectOrProductUID}/dfu/{firmwareType}/history                       | List devices&#39; firmware update history                |
| [**get_devices_dfu_status**](ProjectApi.md#get_devices_dfu_status)                           | **GET** /v1/projects/{projectOrProductUID}/dfu/{firmwareType}/status                        | List devices&#39; firmware status                        |
| [**get_firmware_info**](ProjectApi.md#get_firmware_info)                                     | **GET** /v1/projects/{projectOrProductUID}/firmware                                         | List firmware                                            |
| [**get_fleet**](ProjectApi.md#get_fleet)                                                     | **GET** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}                                | Get a fleet                                              |
| [**get_fleet_environment_hierarchy**](ProjectApi.md#get_fleet_environment_hierarchy)         | **GET** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}/environment_hierarchy          | Get a fleet&#39;s environment hierarchy                  |
| [**get_fleet_environment_variables**](ProjectApi.md#get_fleet_environment_variables)         | **GET** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}/environment_variables          | Get fleet environment variables                          |
| [**get_fleets**](ProjectApi.md#get_fleets)                                                   | **GET** /v1/projects/{projectOrProductUID}/fleets                                           | List fleets                                              |
| [**get_notefile_schemas**](ProjectApi.md#get_notefile_schemas)                               | **GET** /v1/projects/{projectOrProductUID}/schemas                                          | List Notefile schemas                                    |
| [**get_products**](ProjectApi.md#get_products)                                               | **GET** /v1/projects/{projectOrProductUID}/products                                         | List a project&#39;s products                            |
| [**get_project**](ProjectApi.md#get_project)                                                 | **GET** /v1/projects/{projectOrProductUID}                                                  | Get a project                                            |
| [**get_project_by_product**](ProjectApi.md#get_project_by_product)                           | **GET** /v1/products/{productUID}/project                                                   | Get the project for a ProductUID                         |
| [**get_project_environment_hierarchy**](ProjectApi.md#get_project_environment_hierarchy)     | **GET** /v1/projects/{projectOrProductUID}/environment_hierarchy                            | Get the project environment hierarchy                    |
| [**get_project_environment_variables**](ProjectApi.md#get_project_environment_variables)     | **GET** /v1/projects/{projectOrProductUID}/environment_variables                            | Get project environment variables                        |
| [**get_project_members**](ProjectApi.md#get_project_members)                                 | **GET** /v1/projects/{projectOrProductUID}/members                                          | List project members                                     |
| [**get_project_secrets**](ProjectApi.md#get_project_secrets)                                 | **GET** /v1/projects/{projectOrProductUID}/secrets                                          | List project secrets                                     |
| [**get_projects**](ProjectApi.md#get_projects)                                               | **GET** /v1/projects                                                                        | List projects                                            |
| [**perform_dfu_action**](ProjectApi.md#perform_dfu_action)                                   | **POST** /v1/projects/{projectOrProductUID}/dfu/{firmwareType}/{action}                     | Start or cancel firmware updates                         |
| [**set_fleet_environment_variables**](ProjectApi.md#set_fleet_environment_variables)         | **PUT** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}/environment_variables          | Set fleet environment variables                          |
| [**set_global_event_transformation**](ProjectApi.md#set_global_event_transformation)         | **POST** /v1/projects/{projectOrProductUID}/global-transformation                           | Set the global event transformation                      |
| [**set_project_environment_variables**](ProjectApi.md#set_project_environment_variables)     | **PUT** /v1/projects/{projectOrProductUID}/environment_variables                            | Set project environment variables                        |
| [**update_firmware**](ProjectApi.md#update_firmware)                                         | **POST** /v1/projects/{projectOrProductUID}/firmware/{firmwareType}/{filename}              | Update host firmware metadata                            |
| [**update_fleet**](ProjectApi.md#update_fleet)                                               | **PUT** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}                                | Update a fleet                                           |
| [**update_project_secret**](ProjectApi.md#update_project_secret)                             | **PUT** /v1/projects/{projectOrProductUID}/secrets/{secretName}                             | Update a project secret                                  |
| [**upload_firmware**](ProjectApi.md#upload_firmware)                                         | **PUT** /v1/projects/{projectOrProductUID}/firmware/{firmwareType}/{filename}               | Upload firmware                                          |

## add_device_to_fleets

> GetDeviceFleets200Response add_device_to_fleets(project_or_product_uid, device_uid, add_device_to_fleets_request)

Add a device to fleets

Add a device to one or more fleets, keeping the fleets it's already in, and return all its fleets. Fleets it's already in are skipped, so a retry is safe. Requires the Owner or Developer role. Returns 400 if a fleet doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.add_device_to_fleets_request import AddDeviceToFleetsRequest
from notehub_py.models.get_device_fleets200_response import GetDeviceFleets200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    add_device_to_fleets_request = (
        notehub_py.AddDeviceToFleetsRequest()
    )  # AddDeviceToFleetsRequest | The fleets to add the device to.

    try:
        # Add a device to fleets
        api_response = api_instance.add_device_to_fleets(
            project_or_product_uid, device_uid, add_device_to_fleets_request
        )
        print("The response of ProjectApi->add_device_to_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->add_device_to_fleets: %s\n" % e)
```

### Parameters

| Name                             | Type                                                        | Description                      | Notes |
| -------------------------------- | ----------------------------------------------------------- | -------------------------------- | ----- |
| **project_or_product_uid**       | **str**                                                     |                                  |
| **device_uid**                   | **str**                                                     |                                  |
| **add_device_to_fleets_request** | [**AddDeviceToFleetsRequest**](AddDeviceToFleetsRequest.md) | The fleets to add the device to. |

### Return type

[**GetDeviceFleets200Response**](GetDeviceFleets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## clone_project

> Project clone_project(project_or_product_uid, clone_project_request)

Clone a project

Create a new project as a copy of this one. Settings, environment variables, transformation, fleets, routes and host firmware are copied; devices, products and members aren't. Copied fleets get new FleetUIDs. Requires the Owner role (400 otherwise), a verified email address (401 otherwise), and permission to create projects in the target organization (403 otherwise).

### Example

```python
import notehub_py
from notehub_py.models.clone_project_request import CloneProjectRequest
from notehub_py.models.project import Project
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    clone_project_request = (
        notehub_py.CloneProjectRequest()
    )  # CloneProjectRequest | The new project's name and organization, and what to leave out of the copy.

    try:
        # Clone a project
        api_response = api_instance.clone_project(
            project_or_product_uid, clone_project_request
        )
        print("The response of ProjectApi->clone_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->clone_project: %s\n" % e)
```

### Parameters

| Name                       | Type                                              | Description                                                                     | Notes |
| -------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                                           |                                                                                 |
| **clone_project_request**  | [**CloneProjectRequest**](CloneProjectRequest.md) | The new project&#39;s name and organization, and what to leave out of the copy. |

### Return type

[**Project**](Project.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## create_fleet

> Fleet create_fleet(project_or_product_uid, create_fleet_request)

Create a fleet

Create a fleet in the project. Connectivity assurance is on unless `connectivity_assurance.enabled` is `false`. A second call creates another fleet. Requires the Owner or Developer role. Returns 400 if `label` is missing or empty.

### Example

```python
import notehub_py
from notehub_py.models.create_fleet_request import CreateFleetRequest
from notehub_py.models.fleet import Fleet
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    create_fleet_request = (
        notehub_py.CreateFleetRequest()
    )  # CreateFleetRequest | The new fleet's name and settings.

    try:
        # Create a fleet
        api_response = api_instance.create_fleet(
            project_or_product_uid, create_fleet_request
        )
        print("The response of ProjectApi->create_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_fleet: %s\n" % e)
```

### Parameters

| Name                       | Type                                            | Description                            | Notes |
| -------------------------- | ----------------------------------------------- | -------------------------------------- | ----- |
| **project_or_product_uid** | **str**                                         |                                        |
| **create_fleet_request**   | [**CreateFleetRequest**](CreateFleetRequest.md) | The new fleet&#39;s name and settings. |

### Return type

[**Fleet**](Fleet.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## create_product

> Product create_product(project_or_product_uid, create_product_request)

Create a product

Add a ProductUID to the project, formed from the caller's reversed email and `product_uid`. For `jane@acme.com` and `sensors` it is `com.acme.jane:sensors`. Requires the Owner or Developer role and a verified email address (400 otherwise). Returns 404 if an `auto_provision_fleets` entry isn't a fleet in this project, and 500 if `product_uid` is invalid or already taken.

### Example

```python
import notehub_py
from notehub_py.models.create_product_request import CreateProductRequest
from notehub_py.models.product import Product
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    create_product_request = (
        notehub_py.CreateProductRequest()
    )  # CreateProductRequest | The new product's UID suffix, name and provisioning settings.

    try:
        # Create a product
        api_response = api_instance.create_product(
            project_or_product_uid, create_product_request
        )
        print("The response of ProjectApi->create_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_product: %s\n" % e)
```

### Parameters

| Name                       | Type                                                | Description                                                       | Notes |
| -------------------------- | --------------------------------------------------- | ----------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                                             |                                                                   |
| **create_product_request** | [**CreateProductRequest**](CreateProductRequest.md) | The new product&#39;s UID suffix, name and provisioning settings. |

### Return type

[**Product**](Product.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## create_project

> Project create_project(create_project_request)

Create a project

Create a project in an organization, with one default fleet, no products, and the caller as its Owner. A second call creates another project. Requires a verified email address (401 otherwise) and permission to create projects in the organization (403 otherwise).

### Example

```python
import notehub_py
from notehub_py.models.create_project_request import CreateProjectRequest
from notehub_py.models.project import Project
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    create_project_request = (
        notehub_py.CreateProjectRequest()
    )  # CreateProjectRequest | The new project's name and organization.

    try:
        # Create a project
        api_response = api_instance.create_project(create_project_request)
        print("The response of ProjectApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

| Name                       | Type                                                | Description                                  | Notes |
| -------------------------- | --------------------------------------------------- | -------------------------------------------- | ----- |
| **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md) | The new project&#39;s name and organization. |

### Return type

[**Project**](Project.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## create_project_secret

> ProjectSecret create_project_secret(project_or_product_uid, create_project_secret_request)

Create a project secret

Store a secret value that routes and alerts can reference as `[$$name]` without exposing it. The value can't be read back. Requires the Owner or Developer role. Returns 409 if the name is taken, and 400 if it's invalid.

### Example

```python
import notehub_py
from notehub_py.models.create_project_secret_request import CreateProjectSecretRequest
from notehub_py.models.project_secret import ProjectSecret
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    create_project_secret_request = (
        notehub_py.CreateProjectSecretRequest()
    )  # CreateProjectSecretRequest |

    try:
        # Create a project secret
        api_response = api_instance.create_project_secret(
            project_or_product_uid, create_project_secret_request
        )
        print("The response of ProjectApi->create_project_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project_secret: %s\n" % e)
```

### Parameters

| Name                              | Type                                                            | Description | Notes |
| --------------------------------- | --------------------------------------------------------------- | ----------- | ----- |
| **project_or_product_uid**        | **str**                                                         |             |
| **create_project_secret_request** | [**CreateProjectSecretRequest**](CreateProjectSecretRequest.md) |             |

### Return type

[**ProjectSecret**](ProjectSecret.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## delete_device_from_fleets

> GetDeviceFleets200Response delete_device_from_fleets(project_or_product_uid, device_uid, delete_device_from_fleets_request)

Remove a device from fleets

Remove a device from one or more fleets and return the fleets it's still in. Fleets it isn't in are ignored, so a retry is safe. Requires the Owner or Developer role.

### Example

```python
import notehub_py
from notehub_py.models.delete_device_from_fleets_request import (
    DeleteDeviceFromFleetsRequest,
)
from notehub_py.models.get_device_fleets200_response import GetDeviceFleets200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    delete_device_from_fleets_request = (
        notehub_py.DeleteDeviceFromFleetsRequest()
    )  # DeleteDeviceFromFleetsRequest | The fleets to remove the device from.

    try:
        # Remove a device from fleets
        api_response = api_instance.delete_device_from_fleets(
            project_or_product_uid, device_uid, delete_device_from_fleets_request
        )
        print("The response of ProjectApi->delete_device_from_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_device_from_fleets: %s\n" % e)
```

### Parameters

| Name                                  | Type                                                                  | Description                           | Notes |
| ------------------------------------- | --------------------------------------------------------------------- | ------------------------------------- | ----- |
| **project_or_product_uid**            | **str**                                                               |                                       |
| **device_uid**                        | **str**                                                               |                                       |
| **delete_device_from_fleets_request** | [**DeleteDeviceFromFleetsRequest**](DeleteDeviceFromFleetsRequest.md) | The fleets to remove the device from. |

### Return type

[**GetDeviceFleets200Response**](GetDeviceFleets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## delete_firmware

> delete_firmware(project_or_product_uid, firmware_type, filename)

Delete host firmware

Delete a host firmware file by its stored filename, including its `$` timestamp suffix. Notecard firmware can't be deleted. Requires the Owner or Developer role. Returns 404 if the file doesn't exist, and 400 for a sub-project, whose parent manages host firmware.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    firmware_type = "firmware_type_example"  # str |
    filename = "filename_example"  # str |

    try:
        # Delete host firmware
        api_instance.delete_firmware(project_or_product_uid, firmware_type, filename)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_firmware: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **firmware_type**          | **str** |             |
| **filename**               | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_fleet

> delete_fleet(project_or_product_uid, fleet_uid)

Delete a fleet

Delete a fleet and remove it from all its devices. The devices stay in the project; the fleet's environment variables are deleted. To remove one device from a fleet, use `DeleteDeviceFromFleets`. Requires the Owner or Developer role. Returns 400 if the fleet does not exist, including on a retry.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    fleet_uid = "fleet_uid_example"  # str |

    try:
        # Delete a fleet
        api_instance.delete_fleet(project_or_product_uid, fleet_uid)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_fleet: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **fleet_uid**              | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_fleet_environment_variable

> EnvironmentVariables delete_fleet_environment_variable(project_or_product_uid, fleet_uid, key)

Delete a fleet environment variable

Delete one fleet environment variable and return the ones left. Requires the Owner or Developer role. Returns 404 if the fleet or the variable doesn't exist.

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    fleet_uid = "fleet_uid_example"  # str |
    key = "key_example"  # str | Name of the environment variable to delete.

    try:
        # Delete a fleet environment variable
        api_response = api_instance.delete_fleet_environment_variable(
            project_or_product_uid, fleet_uid, key
        )
        print("The response of ProjectApi->delete_fleet_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->delete_fleet_environment_variable: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description                                 | Notes |
| -------------------------- | ------- | ------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                             |
| **fleet_uid**              | **str** |                                             |
| **key**                    | **str** | Name of the environment variable to delete. |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_product

> delete_product(project_or_product_uid, product_uid)

Delete a product

Remove a ProductUID from the project. Accepts the UID with or without the `product:` prefix. Requires the Owner or Developer role. Returns 404 if the project has no such ProductUID.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    product_uid = "com.blues.bridge:sensors"  # str |

    try:
        # Delete a product
        api_instance.delete_product(project_or_product_uid, product_uid)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_product: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **product_uid**            | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_project

> delete_project(project_or_product_uid)

Delete a project

Delete a project, its ProductUIDs, and every member's access to it. Can't be undone through the API. Requires the Owner or Developer role. Returns 200 with no body.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # Delete a project
        api_instance.delete_project(project_or_product_uid)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_project_environment_variable

> EnvironmentVariables delete_project_environment_variable(project_or_product_uid, key)

Delete a project environment variable

Delete one project environment variable and return the ones left. Deleting a variable that doesn't exist still succeeds. Requires the Owner or Developer role.

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    key = "key_example"  # str | Name of the environment variable to delete.

    try:
        # Delete a project environment variable
        api_response = api_instance.delete_project_environment_variable(
            project_or_product_uid, key
        )
        print("The response of ProjectApi->delete_project_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->delete_project_environment_variable: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description                                 | Notes |
| -------------------------- | ------- | ------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                             |
| **key**                    | **str** | Name of the environment variable to delete. |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_project_secret

> delete_project_secret(project_or_product_uid, secret_name)

Delete a project secret

Delete a project secret. Routes and alerts that still reference it can no longer resolve it. Requires the Owner or Developer role. Returns 404 if the secret doesn't exist.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    secret_name = "secret_name_example"  # str | Name of the secret, as listed by `GetProjectSecrets`.

    try:
        # Delete a project secret
        api_instance.delete_project_secret(project_or_product_uid, secret_name)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_project_secret: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                     | Notes |
| -------------------------- | ------- | --------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                 |
| **secret_name**            | **str** | Name of the secret, as listed by &#x60;GetProjectSecrets&#x60;. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## disable_global_event_transformation

> disable_global_event_transformation(project_or_product_uid)

Disable the global event transformation

Stop applying the project's global event transformation to new events. The expression is kept, so `EnableGlobalEventTransformation` can turn it back on. Requires the Owner or Developer role. Returns 400 for a sub-project, whose parent's transformation applies.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # Disable the global event transformation
        api_instance.disable_global_event_transformation(project_or_product_uid)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->disable_global_event_transformation: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## download_firmware

> bytearray download_firmware(project_or_product_uid, firmware_type, filename)

Download host firmware

Download a host firmware binary by its stored filename, including its `$` timestamp suffix. Notecard firmware can't be downloaded (400). Requires the Owner or Developer role. Returns 404 if the file doesn't exist.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    firmware_type = "firmware_type_example"  # str | Which firmware: `host` (the host microcontroller's) or `notecard`.
    filename = "filename_example"  # str |

    try:
        # Download host firmware
        api_response = api_instance.download_firmware(
            project_or_product_uid, firmware_type, filename
        )
        print("The response of ProjectApi->download_firmware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->download_firmware: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                | Notes |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------ | ----- |
| **project_or_product_uid** | **str** |                                                                                            |
| **firmware_type**          | **str** | Which firmware: &#x60;host&#x60; (the host microcontroller&#39;s) or &#x60;notecard&#x60;. |
| **filename**               | **str** |                                                                                            |

### Return type

**bytearray**

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

## enable_global_event_transformation

> enable_global_event_transformation(project_or_product_uid)

Enable the global event transformation

Resume applying the project's global event transformation to new events, without changing the expression. Undoes `DisableGlobalEventTransformation`. Requires the Owner or Developer role. Returns 400 for a sub-project, whose parent's transformation applies.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # Enable the global event transformation
        api_instance.enable_global_event_transformation(project_or_product_uid)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->enable_global_event_transformation: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_aws_role_config

> AWSRoleConfig get_aws_role_config(project_or_product_uid)

Get AWS role configuration for role-based authentication

Get the AWS account ID and External ID for the IAM role trust policy used by AWS routes with role-based authentication. The External ID is created on the first call and stays the same after that.

### Example

```python
import notehub_py
from notehub_py.models.aws_role_config import AWSRoleConfig
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # Get AWS role configuration for role-based authentication
        api_response = api_instance.get_aws_role_config(project_or_product_uid)
        print("The response of ProjectApi->get_aws_role_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_aws_role_config: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**AWSRoleConfig**](AWSRoleConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_dfu_history

> DeviceDfuHistory get_device_dfu_history(project_or_product_uid, device_uid, firmware_type)

Get a device's firmware update history

Get a device's current host or Notecard firmware version and every firmware update requested for it, newest first. For just the latest update, use `GetDeviceDfuStatus`. Returns 400 if the device isn't in the project.

### Example

```python
import notehub_py
from notehub_py.models.device_dfu_history import DeviceDfuHistory
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    firmware_type = "firmware_type_example"  # str | Which firmware: `host` (the host microcontroller's) or `notecard`.

    try:
        # Get a device's firmware update history
        api_response = api_instance.get_device_dfu_history(
            project_or_product_uid, device_uid, firmware_type
        )
        print("The response of ProjectApi->get_device_dfu_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_device_dfu_history: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                | Notes |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------ | ----- |
| **project_or_product_uid** | **str** |                                                                                            |
| **device_uid**             | **str** |                                                                                            |
| **firmware_type**          | **str** | Which firmware: &#x60;host&#x60; (the host microcontroller&#39;s) or &#x60;notecard&#x60;. |

### Return type

[**DeviceDfuHistory**](DeviceDfuHistory.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_dfu_status

> DeviceDfuStatus get_device_dfu_status(project_or_product_uid, device_uid, firmware_type)

Get a device's firmware update status

Get a device's current host or Notecard firmware version and its latest firmware update. Includes whether an update is in progress. For every past update, use `GetDeviceDfuHistory`. Returns 400 if the device isn't in the project.

### Example

```python
import notehub_py
from notehub_py.models.device_dfu_status import DeviceDfuStatus
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |
    firmware_type = "firmware_type_example"  # str | Which firmware: `host` (the host microcontroller's) or `notecard`.

    try:
        # Get a device's firmware update status
        api_response = api_instance.get_device_dfu_status(
            project_or_product_uid, device_uid, firmware_type
        )
        print("The response of ProjectApi->get_device_dfu_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_device_dfu_status: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                | Notes |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------ | ----- |
| **project_or_product_uid** | **str** |                                                                                            |
| **device_uid**             | **str** |                                                                                            |
| **firmware_type**          | **str** | Which firmware: &#x60;host&#x60; (the host microcontroller&#39;s) or &#x60;notecard&#x60;. |

### Return type

[**DeviceDfuStatus**](DeviceDfuStatus.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_device_fleets

> GetDeviceFleets200Response get_device_fleets(project_or_product_uid, device_uid)

List a device's fleets

List the fleets a device belongs to, with only each fleet's UID, label and creation time. For a fleet's full details use `GetFleet`. Returns 404 if the device isn't in the project.

### Example

```python
import notehub_py
from notehub_py.models.get_device_fleets200_response import GetDeviceFleets200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    device_uid = "dev:000000000000000"  # str |

    try:
        # List a device's fleets
        api_response = api_instance.get_device_fleets(
            project_or_product_uid, device_uid
        )
        print("The response of ProjectApi->get_device_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_device_fleets: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**GetDeviceFleets200Response**](GetDeviceFleets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_devices_dfu_history

> DeviceDfuHistoryPage get_devices_dfu_history(project_or_product_uid, firmware_type, page_size=page_size, page_num=page_num, cursor=cursor, sort_by=sort_by, sort_order=sort_order, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)

List devices' firmware update history

List every host or Notecard firmware update requested for each matching device, newest first. Includes each device's current firmware version. For just the latest update, use `GetDevicesDfuStatus`. Paginated, by page or `cursor`. With a `cursor`, changes made through fleet or project firmware settings don't appear until the device itself is next updated.

### Example

```python
import notehub_py
from notehub_py.models.device_dfu_history_page import DeviceDfuHistoryPage
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    firmware_type = "firmware_type_example"  # str | Which firmware: `host` (the host microcontroller's) or `notecard`.
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)
    cursor = "cursor_example"  # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)
    sort_by = "captured"  # str |  (optional) (default to 'captured')
    sort_order = "asc"  # str |  (optional) (default to 'asc')
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    tag = [
        "tag_example"
    ]  # List[str] | Tag filter. Matches the whole tag, case-insensitive. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. For example, `51*` matches tags starting with `51`. (optional)
    serial_number = [
        "serial_number_example"
    ]  # List[str] | Serial number filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    fleet_uid = "fleet_uid_example"  # str |  (optional)
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
        # List devices' firmware update history
        api_response = api_instance.get_devices_dfu_history(
            project_or_product_uid,
            firmware_type,
            page_size=page_size,
            page_num=page_num,
            cursor=cursor,
            sort_by=sort_by,
            sort_order=sort_order,
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
        print("The response of ProjectApi->get_devices_dfu_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_devices_dfu_history: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                                      |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **firmware_type**          | **str**                 | Which firmware: &#x60;host&#x60; (the host microcontroller&#39;s) or &#x60;notecard&#x60;.                                                                                                                                                                                                                                                                                                                                                                              |
| **page_size**              | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000]               |
| **page_num**               | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]                  |
| **cursor**                 | **str**                 | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                                 |
| **sort_by**                | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to &#39;captured&#39;] |
| **sort_order**             | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to &#39;asc&#39;]      |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [optional]                                 |
| **tag**                    | [**List[str]**](str.md) | Tag filter. Matches the whole tag, case-insensitive. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;_&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally. For example, &#x60;51_&#x60; matches tags starting with &#x60;51&#x60;.                                                                                                                                                                   | [optional]                                 |
| **serial_number**          | [**List[str]**](str.md) | Serial number filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                           | [optional]                                 |
| **fleet_uid**              | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional]                                 |
| **notecard_firmware**      | [**List[str]**](str.md) | Firmware version filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                        | [optional]                                 |
| **location**               | [**List[str]**](str.md) | Location filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                                | [optional]                                 |
| **host_firmware**          | [**List[str]**](str.md) | Host firmware filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                           | [optional]                                 |
| **product_uid**            | [**List[str]**](str.md) | ProductUID filter. Matches any value containing the filter text, case-insensitive. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                            | [optional]                                 |
| **sku**                    | [**List[str]**](str.md) | SKU filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                                     | [optional]                                 |

### Return type

[**DeviceDfuHistoryPage**](DeviceDfuHistoryPage.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_devices_dfu_status

> DeviceDfuStatusPage get_devices_dfu_status(project_or_product_uid, firmware_type, page_size=page_size, page_num=page_num, cursor=cursor, sort_by=sort_by, sort_order=sort_order, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)

List devices' firmware status

List the host or Notecard firmware version each matching device runs now, with its latest firmware update. Use this to find which firmware devices run. Paginated, by page or `cursor`. With a `cursor`, changes made through fleet or project firmware settings don't appear until the device itself is next updated.

### Example

```python
import notehub_py
from notehub_py.models.device_dfu_status_page import DeviceDfuStatusPage
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    firmware_type = "firmware_type_example"  # str | Which firmware: `host` (the host microcontroller's) or `notecard`.
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)
    cursor = "cursor_example"  # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)
    sort_by = "captured"  # str |  (optional) (default to 'captured')
    sort_order = "asc"  # str |  (optional) (default to 'asc')
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    tag = [
        "tag_example"
    ]  # List[str] | Tag filter. Matches the whole tag, case-insensitive. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. For example, `51*` matches tags starting with `51`. (optional)
    serial_number = [
        "serial_number_example"
    ]  # List[str] | Serial number filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    fleet_uid = "fleet_uid_example"  # str |  (optional)
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
        # List devices' firmware status
        api_response = api_instance.get_devices_dfu_status(
            project_or_product_uid,
            firmware_type,
            page_size=page_size,
            page_num=page_num,
            cursor=cursor,
            sort_by=sort_by,
            sort_order=sort_order,
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
        print("The response of ProjectApi->get_devices_dfu_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_devices_dfu_status: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                                      |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **firmware_type**          | **str**                 | Which firmware: &#x60;host&#x60; (the host microcontroller&#39;s) or &#x60;notecard&#x60;.                                                                                                                                                                                                                                                                                                                                                                              |
| **page_size**              | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000]               |
| **page_num**               | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]                  |
| **cursor**                 | **str**                 | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                                 |
| **sort_by**                | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to &#39;captured&#39;] |
| **sort_order**             | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to &#39;asc&#39;]      |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [optional]                                 |
| **tag**                    | [**List[str]**](str.md) | Tag filter. Matches the whole tag, case-insensitive. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;_&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally. For example, &#x60;51_&#x60; matches tags starting with &#x60;51&#x60;.                                                                                                                                                                   | [optional]                                 |
| **serial_number**          | [**List[str]**](str.md) | Serial number filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                           | [optional]                                 |
| **fleet_uid**              | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional]                                 |
| **notecard_firmware**      | [**List[str]**](str.md) | Firmware version filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                        | [optional]                                 |
| **location**               | [**List[str]**](str.md) | Location filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                                | [optional]                                 |
| **host_firmware**          | [**List[str]**](str.md) | Host firmware filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                           | [optional]                                 |
| **product_uid**            | [**List[str]**](str.md) | ProductUID filter. Matches any value containing the filter text, case-insensitive. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                            | [optional]                                 |
| **sku**                    | [**List[str]**](str.md) | SKU filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                                                                                                                                                                                     | [optional]                                 |

### Return type

[**DeviceDfuStatusPage**](DeviceDfuStatusPage.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_firmware_info

> List[FirmwareInfo] get_firmware_info(project_or_product_uid, product=product, firmware_type=firmware_type, version=version, target=target, filename=filename, md5=md5, unpublished=unpublished, sort_by=sort_by, sort_order=sort_order)

List firmware

List the host firmware uploaded to the project and the Notecard firmware available to it. Text filters match substrings, and unpublished Notecard builds are left out unless `unpublished` is `true`. Not paginated.

### Example

```python
import notehub_py
from notehub_py.models.firmware_info import FirmwareInfo
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    product = "product_example"  # str | Only firmware whose product contains this text. (optional)
    firmware_type = "firmware_type_example"  # str | Only list `host` or `notecard` firmware. Omit for both. (optional)
    version = "version_example"  # str | Only firmware whose version contains this text. (optional)
    target = "target_example"  # str | Only firmware whose target contains this text. (optional)
    filename = "notecard-7.2.2.16518$20240410043100.bin"  # str | Only firmware whose stored filename contains this text. (optional)
    md5 = "md5_example"  # str | Only firmware whose MD5 hash contains this text. (optional)
    unpublished = (
        True  # bool | If `true`, also list unpublished Notecard firmware. (optional)
    )
    sort_by = "created"  # str | Field to sort by (optional) (default to 'created')
    sort_order = "desc"  # str | Sort order (asc for ascending, desc for descending) (optional) (default to 'desc')

    try:
        # List firmware
        api_response = api_instance.get_firmware_info(
            project_or_product_uid,
            product=product,
            firmware_type=firmware_type,
            version=version,
            target=target,
            filename=filename,
            md5=md5,
            unpublished=unpublished,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        print("The response of ProjectApi->get_firmware_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_firmware_info: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                                                                 | Notes                                     |
| -------------------------- | -------- | --------------------------------------------------------------------------- | ----------------------------------------- |
| **project_or_product_uid** | **str**  |                                                                             |
| **product**                | **str**  | Only firmware whose product contains this text.                             | [optional]                                |
| **firmware_type**          | **str**  | Only list &#x60;host&#x60; or &#x60;notecard&#x60; firmware. Omit for both. | [optional]                                |
| **version**                | **str**  | Only firmware whose version contains this text.                             | [optional]                                |
| **target**                 | **str**  | Only firmware whose target contains this text.                              | [optional]                                |
| **filename**               | **str**  | Only firmware whose stored filename contains this text.                     | [optional]                                |
| **md5**                    | **str**  | Only firmware whose MD5 hash contains this text.                            | [optional]                                |
| **unpublished**            | **bool** | If &#x60;true&#x60;, also list unpublished Notecard firmware.               | [optional]                                |
| **sort_by**                | **str**  | Field to sort by                                                            | [optional] [default to &#39;created&#39;] |
| **sort_order**             | **str**  | Sort order (asc for ascending, desc for descending)                         | [optional] [default to &#39;desc&#39;]    |

### Return type

[**List[FirmwareInfo]**](FirmwareInfo.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_fleet

> Fleet get_fleet(project_or_product_uid, fleet_uid)

Get a fleet

Get one fleet's label, smart rule, watchdog and environment variables. Doesn't include `smart_rule_enabled`. Returns 404 if the fleet doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.fleet import Fleet
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    fleet_uid = "fleet_uid_example"  # str |

    try:
        # Get a fleet
        api_response = api_instance.get_fleet(project_or_product_uid, fleet_uid)
        print("The response of ProjectApi->get_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_fleet: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **fleet_uid**              | **str** |             |

### Return type

[**Fleet**](Fleet.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_fleet_environment_hierarchy

> EnvTreeJsonNode get_fleet_environment_hierarchy(project_or_product_uid, fleet_uid)

Get a fleet's environment hierarchy

Get a fleet's environment variables and the project variables it inherits, as a tree. Each variable has its precedence and whether it is used or overridden. Returns 500 if the fleet doesn't exist.

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    fleet_uid = "fleet_uid_example"  # str |

    try:
        # Get a fleet's environment hierarchy
        api_response = api_instance.get_fleet_environment_hierarchy(
            project_or_product_uid, fleet_uid
        )
        print("The response of ProjectApi->get_fleet_environment_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->get_fleet_environment_hierarchy: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **fleet_uid**              | **str** |             |

### Return type

[**EnvTreeJsonNode**](EnvTreeJsonNode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_fleet_environment_variables

> EnvironmentVariables get_fleet_environment_variables(project_or_product_uid, fleet_uid)

Get fleet environment variables

Get the environment variables set on a fleet, with their notes. They override project variables, and device variables override them. Returns 404 if the fleet doesn't exist.

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    fleet_uid = "fleet_uid_example"  # str |

    try:
        # Get fleet environment variables
        api_response = api_instance.get_fleet_environment_variables(
            project_or_product_uid, fleet_uid
        )
        print("The response of ProjectApi->get_fleet_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->get_fleet_environment_variables: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **fleet_uid**              | **str** |             |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_fleets

> GetDeviceFleets200Response get_fleets(project_or_product_uid)

List fleets

List the project's fleets with each one's label, smart rule, watchdog and environment variables. Doesn't include `smart_rule_enabled`. Not paginated.

### Example

```python
import notehub_py
from notehub_py.models.get_device_fleets200_response import GetDeviceFleets200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # List fleets
        api_response = api_instance.get_fleets(project_or_product_uid)
        print("The response of ProjectApi->get_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_fleets: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**GetDeviceFleets200Response**](GetDeviceFleets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_notefile_schemas

> List[NotefileSchema] get_notefile_schemas(project_or_product_uid)

List Notefile schemas

List the project's Notefiles, each with the event `body` fields Notehub has seen in it and their JSON types. Inferred from received events.

### Example

```python
import notehub_py
from notehub_py.models.notefile_schema import NotefileSchema
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # List Notefile schemas
        api_response = api_instance.get_notefile_schemas(project_or_product_uid)
        print("The response of ProjectApi->get_notefile_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_notefile_schemas: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**List[NotefileSchema]**](NotefileSchema.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_products

> GetProducts200Response get_products(project_or_product_uid)

List a project's products

List the project's ProductUIDs, each with its label, auto-provision fleets, and whether new devices start disabled. UIDs here include the `product:` prefix; `CreateProduct` returns them without it. Not paginated.

### Example

```python
import notehub_py
from notehub_py.models.get_products200_response import GetProducts200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # List a project's products
        api_response = api_instance.get_products(project_or_product_uid)
        print("The response of ProjectApi->get_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_products: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**GetProducts200Response**](GetProducts200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_project

> Project get_project(project_or_product_uid)

Get a project

Get a project's label, creation time, contacts, and the caller's `role` in it. Accepts a ProductUID in place of the ProjectUID.

### Example

```python
import notehub_py
from notehub_py.models.project import Project
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # Get a project
        api_response = api_instance.get_project(project_or_product_uid)
        print("The response of ProjectApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**Project**](Project.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_project_by_product

> Project get_project_by_product(product_uid)

Get the project for a ProductUID

Get the project that a ProductUID belongs to. Returns the same object as `GetProject`, which also accepts a ProductUID in place of a ProjectUID.

### Example

```python
import notehub_py
from notehub_py.models.project import Project
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    product_uid = "com.blues.airnote"  # str | ProductUID, e.g. `com.blues.airnote`, with or without the `product:` prefix.

    try:
        # Get the project for a ProductUID
        api_response = api_instance.get_project_by_product(product_uid)
        print("The response of ProjectApi->get_project_by_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_by_product: %s\n" % e)
```

### Parameters

| Name            | Type    | Description                                                                                      | Notes |
| --------------- | ------- | ------------------------------------------------------------------------------------------------ | ----- |
| **product_uid** | **str** | ProductUID, e.g. &#x60;com.blues.airnote&#x60;, with or without the &#x60;product:&#x60; prefix. |

### Return type

[**Project**](Project.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_project_environment_hierarchy

> EnvTreeJsonNode get_project_environment_hierarchy(project_or_product_uid)

Get the project environment hierarchy

Get the project's environment variables as a one-node environment hierarchy tree. The fleet and device hierarchy operations use the same format; for plain key/value pairs, use `GetProjectEnvironmentVariables`.

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # Get the project environment hierarchy
        api_response = api_instance.get_project_environment_hierarchy(
            project_or_product_uid
        )
        print("The response of ProjectApi->get_project_environment_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->get_project_environment_hierarchy: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**EnvTreeJsonNode**](EnvTreeJsonNode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_project_environment_variables

> EnvironmentVariables get_project_environment_variables(project_or_product_uid)

Get project environment variables

Get the environment variables set on the project, with their notes. Fleet and device variables override these; for what a device actually sees, use `GetDeviceEnvironmentVariables`.

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # Get project environment variables
        api_response = api_instance.get_project_environment_variables(
            project_or_product_uid
        )
        print("The response of ProjectApi->get_project_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->get_project_environment_variables: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_project_members

> GetProjectMembers200Response get_project_members(project_or_product_uid)

List project members

List the project's members with each one's name and role. Emails are filled in only when the caller is an Owner. Not paginated.

### Example

```python
import notehub_py
from notehub_py.models.get_project_members200_response import (
    GetProjectMembers200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # List project members
        api_response = api_instance.get_project_members(project_or_product_uid)
        print("The response of ProjectApi->get_project_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_members: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**GetProjectMembers200Response**](GetProjectMembers200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_project_secrets

> GetProjectSecretsResponse get_project_secrets(project_or_product_uid)

List project secrets

List the project's secrets by name, with who created and last changed each one and when. Values are never returned.

### Example

```python
import notehub_py
from notehub_py.models.get_project_secrets_response import GetProjectSecretsResponse
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # List project secrets
        api_response = api_instance.get_project_secrets(project_or_product_uid)
        print("The response of ProjectApi->get_project_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_secrets: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**GetProjectSecretsResponse**](GetProjectSecretsResponse.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_projects

> GetProjects200Response get_projects()

List projects

List every project the caller is a member of, with the caller's `role` in each. Not paginated.

### Example

```python
import notehub_py
from notehub_py.models.get_projects200_response import GetProjects200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)

    try:
        # List projects
        api_response = api_instance.get_projects()
        print("The response of ProjectApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_projects: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetProjects200Response**](GetProjects200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## perform_dfu_action

> perform_dfu_action(project_or_product_uid, firmware_type, action, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku, dfu_action_request=dfu_action_request)

Start or cancel firmware updates

Start or cancel a host or Notecard firmware update on every device matching the filters. With no filters, that is every device in the project. `update` sets each device's `_fw` or `_fwc` variable to `filename`. Requires the Owner or Developer role. `update` returns 404 if the file isn't found, and can return 400 if a matching device already has an update in progress.

### Example

```python
import notehub_py
from notehub_py.models.dfu_action_request import DfuActionRequest
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    firmware_type = "firmware_type_example"  # str | Which firmware: `host` (the host microcontroller's) or `notecard`.
    action = "action_example"  # str | - `update`: start updating to the firmware in `filename` - `cancel`: cancel any update in progress
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    tag = [
        "tag_example"
    ]  # List[str] | Tag filter. Matches the whole tag, case-insensitive. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. For example, `51*` matches tags starting with `51`. (optional)
    serial_number = [
        "serial_number_example"
    ]  # List[str] | Serial number filter. Matches any value containing the filter text. Use `*` as a wildcard and `\\*` to match a literal `*`; all other characters, including `%` and `_`, match literally. (optional)
    fleet_uid = "fleet_uid_example"  # str |  (optional)
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
    dfu_action_request = (
        notehub_py.DfuActionRequest()
    )  # DfuActionRequest | Which firmware in the case of an update action (optional)

    try:
        # Start or cancel firmware updates
        api_instance.perform_dfu_action(
            project_or_product_uid,
            firmware_type,
            action,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
            dfu_action_request=dfu_action_request,
        )
    except Exception as e:
        print("Exception when calling ProjectApi->perform_dfu_action: %s\n" % e)
```

### Parameters

| Name                       | Type                                        | Description                                                                                                                                                                                                                                                                                           | Notes      |
| -------------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**                                     |                                                                                                                                                                                                                                                                                                       |
| **firmware_type**          | **str**                                     | Which firmware: &#x60;host&#x60; (the host microcontroller&#39;s) or &#x60;notecard&#x60;.                                                                                                                                                                                                            |
| **action**                 | **str**                                     | - &#x60;update&#x60;: start updating to the firmware in &#x60;filename&#x60; - &#x60;cancel&#x60;: cancel any update in progress                                                                                                                                                                      |
| **device_uid**             | [**List[str]**](str.md)                     | A DeviceUID.                                                                                                                                                                                                                                                                                          | [optional] |
| **tag**                    | [**List[str]**](str.md)                     | Tag filter. Matches the whole tag, case-insensitive. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;_&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally. For example, &#x60;51_&#x60; matches tags starting with &#x60;51&#x60;. | [optional] |
| **serial_number**          | [**List[str]**](str.md)                     | Serial number filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                         | [optional] |
| **fleet_uid**              | **str**                                     |                                                                                                                                                                                                                                                                                                       | [optional] |
| **notecard_firmware**      | [**List[str]**](str.md)                     | Firmware version filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                      | [optional] |
| **location**               | [**List[str]**](str.md)                     | Location filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                              | [optional] |
| **host_firmware**          | [**List[str]**](str.md)                     | Host firmware filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                         | [optional] |
| **product_uid**            | [**List[str]**](str.md)                     | ProductUID filter. Matches any value containing the filter text, case-insensitive. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                          | [optional] |
| **sku**                    | [**List[str]**](str.md)                     | SKU filter. Matches any value containing the filter text. Use &#x60;_&#x60; as a wildcard and &#x60;\\_&#x60; to match a literal &#x60;\*&#x60;; all other characters, including &#x60;%&#x60; and &#x60;\_&#x60;, match literally.                                                                   | [optional] |
| **dfu_action_request**     | [**DfuActionRequest**](DfuActionRequest.md) | Which firmware in the case of an update action                                                                                                                                                                                                                                                        | [optional] |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## set_fleet_environment_variables

> EnvironmentVariables set_fleet_environment_variables(project_or_product_uid, fleet_uid, environment_variables)

Set fleet environment variables

Add or change a fleet's environment variables; variables you don't send keep their values. A value of `\"\"` or `-` deletes that variable. Setting `_fw`, `_fwc` or `_fwm` starts a host, Notecard or modem firmware update. Requires the Owner or Developer role. Returns 404 if the fleet doesn't exist, and 400 if a note's key isn't a variable.

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    fleet_uid = "fleet_uid_example"  # str |
    environment_variables = (
        notehub_py.EnvironmentVariables()
    )  # EnvironmentVariables | The variables to add or change, and optional notes.

    try:
        # Set fleet environment variables
        api_response = api_instance.set_fleet_environment_variables(
            project_or_product_uid, fleet_uid, environment_variables
        )
        print("The response of ProjectApi->set_fleet_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->set_fleet_environment_variables: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type                                                | Description                                         | Notes |
| -------------------------- | --------------------------------------------------- | --------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                                             |                                                     |
| **fleet_uid**              | **str**                                             |                                                     |
| **environment_variables**  | [**EnvironmentVariables**](EnvironmentVariables.md) | The variables to add or change, and optional notes. |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## set_global_event_transformation

> set_global_event_transformation(project_or_product_uid, body)

Set the global event transformation

Set the project's JSONata expression that rewrites each new event before it's stored and routed. It can change `body`, `payload`, `details`, `file` and `note`, or drop the event with `$doNotRoute()`; an event it fails on is kept with `error` set. Doesn't enable or disable it. Requires the Owner or Developer role. Returns 400 if it doesn't compile, or for a sub-project, which uses its parent's.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    body = "body_example"  # str | JSONata expression as plain text. An empty body clears the transformation.

    try:
        # Set the global event transformation
        api_instance.set_global_event_transformation(project_or_product_uid, body)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->set_global_event_transformation: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description                                                                | Notes |
| -------------------------- | ------- | -------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                            |
| **body**                   | **str** | JSONata expression as plain text. An empty body clears the transformation. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

## set_project_environment_variables

> EnvironmentVariables set_project_environment_variables(project_or_product_uid, environment_variables=environment_variables)

Set project environment variables

Add or change project environment variables; variables you don't send keep their values. A value of `\"\"` or `-` deletes that variable. Setting `_fw`, `_fwc` or `_fwm` starts a host, Notecard or modem firmware update. Requires the Owner or Developer role. Returns 400 if a note's key isn't a variable.

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
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    environment_variables = (
        notehub_py.EnvironmentVariables()
    )  # EnvironmentVariables |  (optional)

    try:
        # Set project environment variables
        api_response = api_instance.set_project_environment_variables(
            project_or_product_uid, environment_variables=environment_variables
        )
        print("The response of ProjectApi->set_project_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling ProjectApi->set_project_environment_variables: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type                                                | Description | Notes      |
| -------------------------- | --------------------------------------------------- | ----------- | ---------- |
| **project_or_product_uid** | **str**                                             |             |
| **environment_variables**  | [**EnvironmentVariables**](EnvironmentVariables.md) |             | [optional] |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## update_firmware

> FirmwareInfo update_firmware(project_or_product_uid, firmware_type, filename, update_host_firmware_request)

Update host firmware metadata

Change a host firmware file's `version`, `notes` or `info`; fields you leave out or send empty keep their values. Use the stored filename, including its `$` timestamp suffix. Requires the Owner or Developer role. Returns 400 for a sub-project, whose parent manages host firmware, and 404 if the file doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.firmware_info import FirmwareInfo
from notehub_py.models.update_host_firmware_request import UpdateHostFirmwareRequest
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    firmware_type = "firmware_type_example"  # str |
    filename = "filename_example"  # str |
    update_host_firmware_request = (
        notehub_py.UpdateHostFirmwareRequest()
    )  # UpdateHostFirmwareRequest | Firmware metadata fields to update. All fields are optional; only provided fields will be updated.

    try:
        # Update host firmware metadata
        api_response = api_instance.update_firmware(
            project_or_product_uid,
            firmware_type,
            filename,
            update_host_firmware_request,
        )
        print("The response of ProjectApi->update_firmware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_firmware: %s\n" % e)
```

### Parameters

| Name                             | Type                                                          | Description                                                                                        | Notes |
| -------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid**       | **str**                                                       |                                                                                                    |
| **firmware_type**                | **str**                                                       |                                                                                                    |
| **filename**                     | **str**                                                       |                                                                                                    |
| **update_host_firmware_request** | [**UpdateHostFirmwareRequest**](UpdateHostFirmwareRequest.md) | Firmware metadata fields to update. All fields are optional; only provided fields will be updated. |

### Return type

[**FirmwareInfo**](FirmwareInfo.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## update_fleet

> Fleet update_fleet(project_or_product_uid, fleet_uid, update_fleet_request)

Update a fleet

Change a fleet's label, smart rule, watchdog or connectivity assurance, or add and remove devices. Always send `smart_rule_enabled`; leaving it out turns the smart rule off. Empty `label` or `smart_rule` keeps the current value; `-` clears `smart_rule`. Requires the Owner or Developer role. Returns 400 for an unknown fleet or `label` of `-`, and for a bad DeviceUID after saving the other changes.

### Example

```python
import notehub_py
from notehub_py.models.fleet import Fleet
from notehub_py.models.update_fleet_request import UpdateFleetRequest
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    fleet_uid = "fleet_uid_example"  # str |
    update_fleet_request = (
        notehub_py.UpdateFleetRequest()
    )  # UpdateFleetRequest | The fields to change. Fields left out keep their values, except `smart_rule_enabled`.

    try:
        # Update a fleet
        api_response = api_instance.update_fleet(
            project_or_product_uid, fleet_uid, update_fleet_request
        )
        print("The response of ProjectApi->update_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_fleet: %s\n" % e)
```

### Parameters

| Name                       | Type                                            | Description                                                                                     | Notes |
| -------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                                         |                                                                                                 |
| **fleet_uid**              | **str**                                         |                                                                                                 |
| **update_fleet_request**   | [**UpdateFleetRequest**](UpdateFleetRequest.md) | The fields to change. Fields left out keep their values, except &#x60;smart_rule_enabled&#x60;. |

### Return type

[**Fleet**](Fleet.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## update_project_secret

> ProjectSecret update_project_secret(project_or_product_uid, secret_name, update_project_secret_request)

Update a project secret

Replace the value of an existing project secret. Routes and alerts that reference it use the new value from then on. Requires the Owner or Developer role. Returns 404 if the secret doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.project_secret import ProjectSecret
from notehub_py.models.update_project_secret_request import UpdateProjectSecretRequest
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    secret_name = "secret_name_example"  # str | Name of the secret, as listed by `GetProjectSecrets`.
    update_project_secret_request = (
        notehub_py.UpdateProjectSecretRequest()
    )  # UpdateProjectSecretRequest |

    try:
        # Update a project secret
        api_response = api_instance.update_project_secret(
            project_or_product_uid, secret_name, update_project_secret_request
        )
        print("The response of ProjectApi->update_project_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_project_secret: %s\n" % e)
```

### Parameters

| Name                              | Type                                                            | Description                                                     | Notes |
| --------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | ----- |
| **project_or_product_uid**        | **str**                                                         |                                                                 |
| **secret_name**                   | **str**                                                         | Name of the secret, as listed by &#x60;GetProjectSecrets&#x60;. |
| **update_project_secret_request** | [**UpdateProjectSecretRequest**](UpdateProjectSecretRequest.md) |                                                                 |

### Return type

[**ProjectSecret**](ProjectSecret.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## upload_firmware

> FirmwareInfo upload_firmware(project_or_product_uid, firmware_type, filename, body, version=version, notes=notes)

Upload firmware

Upload a host or Notecard firmware binary. Notehub usually adds a timestamp to `filename`; use the returned `filename` from then on. Requires the Owner or Developer role. Returns 400 for host firmware on a sub-project, whose parent manages it, and 500 for a wrong file type or a file over the limit: 1.5 MB for host firmware, 2 MB for `notecard-s3-*` and 1 MB for other Notecard firmware.

### Example

```python
import notehub_py
from notehub_py.models.firmware_info import FirmwareInfo
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ProjectApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    firmware_type = "firmware_type_example"  # str | Which firmware: `host` (the host microcontroller's) or `notecard`.
    filename = "filename_example"  # str | Name to store the file under. Notehub adds `$` and a timestamp before the extension, except for a Notecard firmware name that already contains `$`.
    body = None  # bytearray | contents of the firmware binary
    version = "version_example"  # str | Firmware version (optional). If not provided, the version will be extracted from firmware binary if available, otherwise left empty (optional)
    notes = "notes_example"  # str | Optional notes describing what's different about this firmware version (optional)

    try:
        # Upload firmware
        api_response = api_instance.upload_firmware(
            project_or_product_uid,
            firmware_type,
            filename,
            body,
            version=version,
            notes=notes,
        )
        print("The response of ProjectApi->upload_firmware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->upload_firmware: %s\n" % e)
```

### Parameters

| Name                       | Type          | Description                                                                                                                                                             | Notes      |
| -------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**       |                                                                                                                                                                         |
| **firmware_type**          | **str**       | Which firmware: &#x60;host&#x60; (the host microcontroller&#39;s) or &#x60;notecard&#x60;.                                                                              |
| **filename**               | **str**       | Name to store the file under. Notehub adds &#x60;$&#x60; and a timestamp before the extension, except for a Notecard firmware name that already contains &#x60;$&#x60;. |
| **body**                   | **bytearray** | contents of the firmware binary                                                                                                                                         |
| **version**                | **str**       | Firmware version (optional). If not provided, the version will be extracted from firmware binary if available, otherwise left empty                                     | [optional] |
| **notes**                  | **str**       | Optional notes describing what&#39;s different about this firmware version                                                                                              | [optional] |

### Return type

[**FirmwareInfo**](FirmwareInfo.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json
