# ncbi.datasets.openapi.VersionApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version**](VersionApi.md#version) | **GET** /version | Retrieve service version


# **version**
> V2VersionReply version()

Retrieve service version

Retrieve the latest version of the Datasets services.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_version_reply import V2VersionReply
from ncbi.datasets.openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ncbi.nlm.nih.gov/datasets/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ncbi.datasets.openapi.Configuration(
    host = "https://api.ncbi.nlm.nih.gov/datasets/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuthHeader
configuration.api_key['ApiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuthHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with ncbi.datasets.openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ncbi.datasets.openapi.VersionApi(api_client)

    try:
        # Retrieve service version
        api_response = api_instance.version()
        print("The response of VersionApi->version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionApi->version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V2VersionReply**](V2VersionReply.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

