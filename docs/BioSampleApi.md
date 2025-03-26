# ncbi.datasets.openapi.BioSampleApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bio_sample_dataset_report**](BioSampleApi.md#bio_sample_dataset_report) | **GET** /biosample/accession/{accessions}/biosample_report | Get BioSample dataset reports by accession(s)


# **bio_sample_dataset_report**
> V2reportsBioSampleDataReportPage bio_sample_dataset_report(accessions)

Get BioSample dataset reports by accession(s)

Get BioSample dataset reports by accession(s).  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2reports_bio_sample_data_report_page import V2reportsBioSampleDataReportPage
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
    api_instance = ncbi.datasets.openapi.BioSampleApi(api_client)
    accessions = ['[\"SAMN15960293\"]'] # List[str] | 

    try:
        # Get BioSample dataset reports by accession(s)
        api_response = api_instance.bio_sample_dataset_report(accessions)
        print("The response of BioSampleApi->bio_sample_dataset_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BioSampleApi->bio_sample_dataset_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)|  | 

### Return type

[**V2reportsBioSampleDataReportPage**](V2reportsBioSampleDataReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/x-ndjson, text/tab-separated-values

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

