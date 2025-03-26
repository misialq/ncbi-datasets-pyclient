# ncbi.datasets.openapi.GenomeApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotation_report_facets_by_accession**](GenomeApi.md#annotation_report_facets_by_accession) | **GET** /genome/accession/{accession}/annotation_summary | Get genome annotation report summary information
[**annotation_report_facets_by_post**](GenomeApi.md#annotation_report_facets_by_post) | **POST** /genome/annotation_summary | Get genome annotation report summary information
[**assembly_accessions_for_sequence_accession**](GenomeApi.md#assembly_accessions_for_sequence_accession) | **GET** /genome/sequence_accession/{accession}/sequence_assemblies | Get assembly accessions for a sequence accession
[**assembly_accessions_for_sequence_accession_by_post**](GenomeApi.md#assembly_accessions_for_sequence_accession_by_post) | **POST** /genome/sequence_assemblies | Get assembly accessions for a sequence accession
[**assembly_revision_history_by_get**](GenomeApi.md#assembly_revision_history_by_get) | **GET** /genome/accession/{accession}/revision_history | Get revision history for assembly by accession
[**assembly_revision_history_by_post**](GenomeApi.md#assembly_revision_history_by_post) | **POST** /genome/revision_history | Get revision history for assembly by accession
[**check_assembly_availability**](GenomeApi.md#check_assembly_availability) | **GET** /genome/accession/{accessions}/check | Check the validity of genome accessions
[**check_assembly_availability_post**](GenomeApi.md#check_assembly_availability_post) | **POST** /genome/check | Check the validity of many genome accessions in a single request
[**checkm_histogram_by_taxon**](GenomeApi.md#checkm_histogram_by_taxon) | **GET** /genome/taxon/{species_taxon}/checkm_histogram | Get CheckM histogram by species taxon
[**checkm_histogram_by_taxon_by_post**](GenomeApi.md#checkm_histogram_by_taxon_by_post) | **POST** /genome/checkm_histogram | Get CheckM histogram by species taxon
[**download_assembly_package**](GenomeApi.md#download_assembly_package) | **GET** /genome/accession/{accessions}/download | Get a genome dataset by accession
[**download_assembly_package_post**](GenomeApi.md#download_assembly_package_post) | **POST** /genome/download | Get a genome dataset by post
[**download_genome_annotation_package**](GenomeApi.md#download_genome_annotation_package) | **GET** /genome/accession/{accession}/annotation_report/download | Get an annotation report dataset by accession
[**download_genome_annotation_package_by_post**](GenomeApi.md#download_genome_annotation_package_by_post) | **POST** /genome/annotation_report/download | Get an annotation report dataset by accession
[**genome_annotation_download_summary**](GenomeApi.md#genome_annotation_download_summary) | **GET** /genome/accession/{accession}/annotation_report/download_summary | Preview feature dataset download
[**genome_annotation_download_summary_by_post**](GenomeApi.md#genome_annotation_download_summary_by_post) | **POST** /genome/annotation_report/download_summary | Preview feature download by POST
[**genome_annotation_report**](GenomeApi.md#genome_annotation_report) | **GET** /genome/accession/{accession}/annotation_report | Get genome annotation reports by genome accession
[**genome_annotation_report_by_post**](GenomeApi.md#genome_annotation_report_by_post) | **POST** /genome/annotation_report | Get genome annotation reports by genome accession
[**genome_dataset_report**](GenomeApi.md#genome_dataset_report) | **GET** /genome/accession/{accessions}/dataset_report | Get dataset reports by accessions
[**genome_dataset_report_by_post**](GenomeApi.md#genome_dataset_report_by_post) | **POST** /genome/dataset_report | Get dataset reports by accessions
[**genome_dataset_reports_by_assembly_name**](GenomeApi.md#genome_dataset_reports_by_assembly_name) | **GET** /genome/assembly_name/{assembly_names}/dataset_report | Get dataset reports by assembly name (exact)
[**genome_dataset_reports_by_bioproject**](GenomeApi.md#genome_dataset_reports_by_bioproject) | **GET** /genome/bioproject/{bioprojects}/dataset_report | Get dataset reports by bioproject
[**genome_dataset_reports_by_biosample_id**](GenomeApi.md#genome_dataset_reports_by_biosample_id) | **GET** /genome/biosample/{biosample_ids}/dataset_report | Get dataset reports by biosample id
[**genome_dataset_reports_by_taxon**](GenomeApi.md#genome_dataset_reports_by_taxon) | **GET** /genome/taxon/{taxons}/dataset_report | Get dataset reports by taxons
[**genome_dataset_reports_by_wgs**](GenomeApi.md#genome_dataset_reports_by_wgs) | **GET** /genome/wgs/{wgs_accessions}/dataset_report | Get dataset reports by wgs accession
[**genome_download_summary**](GenomeApi.md#genome_download_summary) | **GET** /genome/accession/{accessions}/download_summary | Preview genome dataset download
[**genome_download_summary_by_post**](GenomeApi.md#genome_download_summary_by_post) | **POST** /genome/download_summary | Preview genome dataset download by POST
[**genome_links_by_accession**](GenomeApi.md#genome_links_by_accession) | **GET** /genome/accession/{accessions}/links | Get assembly links by accessions
[**genome_links_by_accession_by_post**](GenomeApi.md#genome_links_by_accession_by_post) | **POST** /genome/links | Get assembly links by accessions
[**genome_sequence_report**](GenomeApi.md#genome_sequence_report) | **GET** /genome/accession/{accession}/sequence_reports | Get sequence reports by accessions
[**genome_sequence_report_by_post**](GenomeApi.md#genome_sequence_report_by_post) | **POST** /genome/sequence_reports | Get sequence reports by accessions


# **annotation_report_facets_by_accession**
> V2GenomeAnnotationTableSummaryReply annotation_report_facets_by_accession(accession, sort_field=sort_field, sort_direction=sort_direction)

Get genome annotation report summary information

Get genome annotation report summary information by genome accession. The return facets can be used in subsequent queries.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_genome_annotation_table_summary_reply import V2GenomeAnnotationTableSummaryReply
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accession = 'GCF_000001635.27' # str | 
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = ncbi.datasets.openapi.V2SortDirection() # V2SortDirection |  (optional)

    try:
        # Get genome annotation report summary information
        api_response = api_instance.annotation_report_facets_by_accession(accession, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of GenomeApi->annotation_report_facets_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->annotation_report_facets_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**|  | 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] 

### Return type

[**V2GenomeAnnotationTableSummaryReply**](V2GenomeAnnotationTableSummaryReply.md)

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

# **annotation_report_facets_by_post**
> V2GenomeAnnotationTableSummaryReply annotation_report_facets_by_post(v2_genome_annotation_request)

Get genome annotation report summary information

Get genome annotation report summary information by genome accession. The return facets can be used in subsequent queries.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_genome_annotation_request import V2GenomeAnnotationRequest
from ncbi.datasets.openapi.models.v2_genome_annotation_table_summary_reply import V2GenomeAnnotationTableSummaryReply
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_genome_annotation_request = {"accession":"GCF_000001635.27"} # V2GenomeAnnotationRequest | 

    try:
        # Get genome annotation report summary information
        api_response = api_instance.annotation_report_facets_by_post(v2_genome_annotation_request)
        print("The response of GenomeApi->annotation_report_facets_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->annotation_report_facets_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_genome_annotation_request** | [**V2GenomeAnnotationRequest**](V2GenomeAnnotationRequest.md)|  | 

### Return type

[**V2GenomeAnnotationTableSummaryReply**](V2GenomeAnnotationTableSummaryReply.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assembly_accessions_for_sequence_accession**
> V2AssemblyAccessions assembly_accessions_for_sequence_accession(accession)

Get assembly accessions for a sequence accession

Get assembly accessions for a sequence (nucleotide) accession

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_accessions import V2AssemblyAccessions
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accession = 'NC_000001.11' # str | 

    try:
        # Get assembly accessions for a sequence accession
        api_response = api_instance.assembly_accessions_for_sequence_accession(accession)
        print("The response of GenomeApi->assembly_accessions_for_sequence_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->assembly_accessions_for_sequence_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**|  | 

### Return type

[**V2AssemblyAccessions**](V2AssemblyAccessions.md)

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

# **assembly_accessions_for_sequence_accession_by_post**
> V2AssemblyAccessions assembly_accessions_for_sequence_accession_by_post(v2_sequence_accession_request)

Get assembly accessions for a sequence accession

Get assembly accessions for a sequence (nucleotide) accession

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_accessions import V2AssemblyAccessions
from ncbi.datasets.openapi.models.v2_sequence_accession_request import V2SequenceAccessionRequest
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_sequence_accession_request = {"accession":"NC_000001.11"} # V2SequenceAccessionRequest | 

    try:
        # Get assembly accessions for a sequence accession
        api_response = api_instance.assembly_accessions_for_sequence_accession_by_post(v2_sequence_accession_request)
        print("The response of GenomeApi->assembly_accessions_for_sequence_accession_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->assembly_accessions_for_sequence_accession_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_sequence_accession_request** | [**V2SequenceAccessionRequest**](V2SequenceAccessionRequest.md)|  | 

### Return type

[**V2AssemblyAccessions**](V2AssemblyAccessions.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assembly_revision_history_by_get**
> V2AssemblyRevisionHistory assembly_revision_history_by_get(accession)

Get revision history for assembly by accession

Get revision history for assembly by accession

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_revision_history import V2AssemblyRevisionHistory
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accession = 'GCF_000001405.40' # str | 

    try:
        # Get revision history for assembly by accession
        api_response = api_instance.assembly_revision_history_by_get(accession)
        print("The response of GenomeApi->assembly_revision_history_by_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->assembly_revision_history_by_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**|  | 

### Return type

[**V2AssemblyRevisionHistory**](V2AssemblyRevisionHistory.md)

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

# **assembly_revision_history_by_post**
> V2AssemblyRevisionHistory assembly_revision_history_by_post(v2_assembly_revision_history_request)

Get revision history for assembly by accession

Get revision history for assembly by accession

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_revision_history import V2AssemblyRevisionHistory
from ncbi.datasets.openapi.models.v2_assembly_revision_history_request import V2AssemblyRevisionHistoryRequest
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_assembly_revision_history_request = {"accession":"GCF_000001405.40"} # V2AssemblyRevisionHistoryRequest | 

    try:
        # Get revision history for assembly by accession
        api_response = api_instance.assembly_revision_history_by_post(v2_assembly_revision_history_request)
        print("The response of GenomeApi->assembly_revision_history_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->assembly_revision_history_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_assembly_revision_history_request** | [**V2AssemblyRevisionHistoryRequest**](V2AssemblyRevisionHistoryRequest.md)|  | 

### Return type

[**V2AssemblyRevisionHistory**](V2AssemblyRevisionHistory.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_assembly_availability**
> V2AssemblyDatasetAvailability check_assembly_availability(accessions)

Check the validity of genome accessions

The 'GET' version of check is limited by the size of the GET URL (2KB, which works out to about 140 genomic accessions).  The POST operation is provided to allow users to supply a larger number of accessions in a single request.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_availability import V2AssemblyDatasetAvailability
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accessions = ['[\"GCF_000001405.40\"]'] # List[str] | NCBI genome assembly accessions

    try:
        # Check the validity of genome accessions
        api_response = api_instance.check_assembly_availability(accessions)
        print("The response of GenomeApi->check_assembly_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->check_assembly_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| NCBI genome assembly accessions | 

### Return type

[**V2AssemblyDatasetAvailability**](V2AssemblyDatasetAvailability.md)

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

# **check_assembly_availability_post**
> V2AssemblyDatasetAvailability check_assembly_availability_post(v2_assembly_dataset_request)

Check the validity of many genome accessions in a single request

The 'GET' version of check is limited by the size of the GET URL (2KB, which works out to about 140 genomic accessions).  The POST operation is provided to allow users to supply a larger number of accessions in a single request.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_availability import V2AssemblyDatasetAvailability
from ncbi.datasets.openapi.models.v2_assembly_dataset_request import V2AssemblyDatasetRequest
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_assembly_dataset_request = {"accessions":["GCF_000001405.40"]} # V2AssemblyDatasetRequest | 

    try:
        # Check the validity of many genome accessions in a single request
        api_response = api_instance.check_assembly_availability_post(v2_assembly_dataset_request)
        print("The response of GenomeApi->check_assembly_availability_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->check_assembly_availability_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_assembly_dataset_request** | [**V2AssemblyDatasetRequest**](V2AssemblyDatasetRequest.md)|  | 

### Return type

[**V2AssemblyDatasetAvailability**](V2AssemblyDatasetAvailability.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkm_histogram_by_taxon**
> V2AssemblyCheckMHistogramReply checkm_histogram_by_taxon(species_taxon)

Get CheckM histogram by species taxon

Get CheckM histogram by species taxon. CheckM histograms are only available for certain bacterial species.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_check_m_histogram_reply import V2AssemblyCheckMHistogramReply
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    species_taxon = '202956' # str | 

    try:
        # Get CheckM histogram by species taxon
        api_response = api_instance.checkm_histogram_by_taxon(species_taxon)
        print("The response of GenomeApi->checkm_histogram_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->checkm_histogram_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **species_taxon** | **str**|  | 

### Return type

[**V2AssemblyCheckMHistogramReply**](V2AssemblyCheckMHistogramReply.md)

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

# **checkm_histogram_by_taxon_by_post**
> V2AssemblyCheckMHistogramReply checkm_histogram_by_taxon_by_post(v2_assembly_check_m_histogram_request)

Get CheckM histogram by species taxon

Get CheckM histogram by species taxon. CheckM histograms are only available for certain bacterial species.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_check_m_histogram_reply import V2AssemblyCheckMHistogramReply
from ncbi.datasets.openapi.models.v2_assembly_check_m_histogram_request import V2AssemblyCheckMHistogramRequest
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_assembly_check_m_histogram_request = {"species_taxon":"202956"} # V2AssemblyCheckMHistogramRequest | 

    try:
        # Get CheckM histogram by species taxon
        api_response = api_instance.checkm_histogram_by_taxon_by_post(v2_assembly_check_m_histogram_request)
        print("The response of GenomeApi->checkm_histogram_by_taxon_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->checkm_histogram_by_taxon_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_assembly_check_m_histogram_request** | [**V2AssemblyCheckMHistogramRequest**](V2AssemblyCheckMHistogramRequest.md)|  | 

### Return type

[**V2AssemblyCheckMHistogramReply**](V2AssemblyCheckMHistogramReply.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_assembly_package**
> bytearray download_assembly_package(accessions, chromosomes=chromosomes, include_annotation_type=include_annotation_type, hydrated=hydrated, filename=filename)

Get a genome dataset by accession

Download a genome dataset including fasta sequence, annotation and a detailed data report by accession.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_annotation_for_assembly_type import V2AnnotationForAssemblyType
from ncbi.datasets.openapi.models.v2_assembly_dataset_request_resolution import V2AssemblyDatasetRequestResolution
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accessions = ['[\"GCF_000001405.40\"]'] # List[str] | NCBI genome assembly accessions
    chromosomes = ['[\"1\",\"2\",\"3\",\"X\",\"Y\",\"MT\"]'] # List[str] | The default setting is all chromosome. Specify individual chromosome by string (1,2,MT or chr1,chr2.chrMT). Unplaced sequences are treated like their own chromosome ('Un'). The filter only applies to fasta sequence. (optional)
    include_annotation_type = [ncbi.datasets.openapi.V2AnnotationForAssemblyType()] # List[V2AnnotationForAssemblyType] | Select additional types of annotation to include in the data package.  If unset, no annotation is provided. (optional)
    hydrated = ncbi.datasets.openapi.V2AssemblyDatasetRequestResolution() # V2AssemblyDatasetRequestResolution | Set to DATA_REPORT_ONLY, to only retrieve data-reports. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a genome dataset by accession
        api_response = api_instance.download_assembly_package(accessions, chromosomes=chromosomes, include_annotation_type=include_annotation_type, hydrated=hydrated, filename=filename)
        print("The response of GenomeApi->download_assembly_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->download_assembly_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| NCBI genome assembly accessions | 
 **chromosomes** | [**List[str]**](str.md)| The default setting is all chromosome. Specify individual chromosome by string (1,2,MT or chr1,chr2.chrMT). Unplaced sequences are treated like their own chromosome (&#39;Un&#39;). The filter only applies to fasta sequence. | [optional] 
 **include_annotation_type** | [**List[V2AnnotationForAssemblyType]**](V2AnnotationForAssemblyType.md)| Select additional types of annotation to include in the data package.  If unset, no annotation is provided. | [optional] 
 **hydrated** | [**V2AssemblyDatasetRequestResolution**](.md)| Set to DATA_REPORT_ONLY, to only retrieve data-reports. | [optional] 
 **filename** | **str**| Output file name. | [optional] [default to &#39;ncbi_dataset.zip&#39;]

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_assembly_package_post**
> bytearray download_assembly_package_post(v2_assembly_dataset_request, filename=filename)

Get a genome dataset by post

The 'GET' version of download is limited by the size of the GET URL (2KB, which works out to about 140 genomic accessions).  The POST operation is provided to allow users to supply a larger number of accessions in a single request.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_request import V2AssemblyDatasetRequest
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_assembly_dataset_request = {"accessions":["GCF_000001405.40"]} # V2AssemblyDatasetRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a genome dataset by post
        api_response = api_instance.download_assembly_package_post(v2_assembly_dataset_request, filename=filename)
        print("The response of GenomeApi->download_assembly_package_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->download_assembly_package_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_assembly_dataset_request** | [**V2AssemblyDatasetRequest**](V2AssemblyDatasetRequest.md)|  | 
 **filename** | **str**| Output file name. | [optional] [default to &#39;ncbi_dataset.zip&#39;]

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_genome_annotation_package**
> bytearray download_genome_annotation_package(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, include_annotation_type=include_annotation_type, page_size=page_size, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_token=page_token, filename=filename)

Get an annotation report dataset by accession

Download an annotation report including fasta sequence and a detailed annotation report by genomic accession.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_genome_annotation_request_annotation_type import V2GenomeAnnotationRequestAnnotationType
from ncbi.datasets.openapi.models.v2_genome_annotation_request_genome_annotation_table_format import V2GenomeAnnotationRequestGenomeAnnotationTableFormat
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accession = 'GCF_000001635.27' # str | 
    annotation_ids = ['annotation_ids_example'] # List[str] | Limit the reports by internal, unstable annotation ids. (optional)
    symbols = ['symbols_example'] # List[str] | Filter parameters (optional)
    locations = ['locations_example'] # List[str] | Locations with a chromosome or accession and optional start-stop range: chromosome|accession[:start-end] (optional)
    gene_types = ['gene_types_example'] # List[str] | granular gene_types (optional)
    search_text = ['search_text_example'] # List[str] |  (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = ncbi.datasets.openapi.V2SortDirection() # V2SortDirection |  (optional)
    include_annotation_type = [ncbi.datasets.openapi.V2GenomeAnnotationRequestAnnotationType()] # List[V2GenomeAnnotationRequestAnnotationType] |  (optional)
    page_size = 20 # int | The maximum number of features to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    table_fields = ['table_fields_example'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = ncbi.datasets.openapi.V2GenomeAnnotationRequestGenomeAnnotationTableFormat() # V2GenomeAnnotationRequestGenomeAnnotationTableFormat | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_token = 'page_token_example' # str | A page token is returned from a `GetFeatures` call with more than `page_size` results. Use this token, along with the previous `FeatureRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get an annotation report dataset by accession
        api_response = api_instance.download_genome_annotation_package(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, include_annotation_type=include_annotation_type, page_size=page_size, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_token=page_token, filename=filename)
        print("The response of GenomeApi->download_genome_annotation_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->download_genome_annotation_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**|  | 
 **annotation_ids** | [**List[str]**](str.md)| Limit the reports by internal, unstable annotation ids. | [optional] 
 **symbols** | [**List[str]**](str.md)| Filter parameters | [optional] 
 **locations** | [**List[str]**](str.md)| Locations with a chromosome or accession and optional start-stop range: chromosome|accession[:start-end] | [optional] 
 **gene_types** | [**List[str]**](str.md)| granular gene_types | [optional] 
 **search_text** | [**List[str]**](str.md)|  | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] 
 **include_annotation_type** | [**List[V2GenomeAnnotationRequestAnnotationType]**](V2GenomeAnnotationRequestAnnotationType.md)|  | [optional] 
 **page_size** | **int**| The maximum number of features to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | [**V2GenomeAnnotationRequestGenomeAnnotationTableFormat**](.md)| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_token** | **str**| A page token is returned from a &#x60;GetFeatures&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;FeatureRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **filename** | **str**| Output file name. | [optional] [default to &#39;ncbi_dataset.zip&#39;]

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_genome_annotation_package_by_post**
> bytearray download_genome_annotation_package_by_post(v2_genome_annotation_request, filename=filename)

Get an annotation report dataset by accession

Download an annotation report including fasta sequence and a detailed annotation report by genomic accession.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_genome_annotation_request import V2GenomeAnnotationRequest
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_genome_annotation_request = {"accession":"GCF_000001635.27"} # V2GenomeAnnotationRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get an annotation report dataset by accession
        api_response = api_instance.download_genome_annotation_package_by_post(v2_genome_annotation_request, filename=filename)
        print("The response of GenomeApi->download_genome_annotation_package_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->download_genome_annotation_package_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_genome_annotation_request** | [**V2GenomeAnnotationRequest**](V2GenomeAnnotationRequest.md)|  | 
 **filename** | **str**| Output file name. | [optional] [default to &#39;ncbi_dataset.zip&#39;]

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genome_annotation_download_summary**
> V2DownloadSummary genome_annotation_download_summary(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, include_annotation_type=include_annotation_type, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header)

Preview feature dataset download

Get a download feature summary by accession in a JSON output format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
from ncbi.datasets.openapi.models.v2_genome_annotation_request_annotation_type import V2GenomeAnnotationRequestAnnotationType
from ncbi.datasets.openapi.models.v2_genome_annotation_request_genome_annotation_table_format import V2GenomeAnnotationRequestGenomeAnnotationTableFormat
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accession = 'GCF_000001635.27' # str | 
    annotation_ids = ['annotation_ids_example'] # List[str] | Limit the reports by internal, unstable annotation ids. (optional)
    symbols = ['symbols_example'] # List[str] | Filter parameters (optional)
    locations = ['locations_example'] # List[str] | Locations with a chromosome or accession and optional start-stop range: chromosome|accession[:start-end] (optional)
    gene_types = ['gene_types_example'] # List[str] | granular gene_types (optional)
    search_text = ['search_text_example'] # List[str] |  (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = ncbi.datasets.openapi.V2SortDirection() # V2SortDirection |  (optional)
    include_annotation_type = [ncbi.datasets.openapi.V2GenomeAnnotationRequestAnnotationType()] # List[V2GenomeAnnotationRequestAnnotationType] |  (optional)
    table_fields = ['table_fields_example'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = ncbi.datasets.openapi.V2GenomeAnnotationRequestGenomeAnnotationTableFormat() # V2GenomeAnnotationRequestGenomeAnnotationTableFormat | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)

    try:
        # Preview feature dataset download
        api_response = api_instance.genome_annotation_download_summary(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, include_annotation_type=include_annotation_type, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_annotation_download_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_annotation_download_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**|  | 
 **annotation_ids** | [**List[str]**](str.md)| Limit the reports by internal, unstable annotation ids. | [optional] 
 **symbols** | [**List[str]**](str.md)| Filter parameters | [optional] 
 **locations** | [**List[str]**](str.md)| Locations with a chromosome or accession and optional start-stop range: chromosome|accession[:start-end] | [optional] 
 **gene_types** | [**List[str]**](str.md)| granular gene_types | [optional] 
 **search_text** | [**List[str]**](str.md)|  | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] 
 **include_annotation_type** | [**List[V2GenomeAnnotationRequestAnnotationType]**](V2GenomeAnnotationRequestAnnotationType.md)|  | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | [**V2GenomeAnnotationRequestGenomeAnnotationTableFormat**](.md)| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 

### Return type

[**V2DownloadSummary**](V2DownloadSummary.md)

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

# **genome_annotation_download_summary_by_post**
> V2DownloadSummary genome_annotation_download_summary_by_post(v2_genome_annotation_request)

Preview feature download by POST

The 'GET' version of feature download summary is limited by the size of the GET URL (2KB).  The POST operation is provided to allow users to supply a larger number of annotation_ids in a single request.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
from ncbi.datasets.openapi.models.v2_genome_annotation_request import V2GenomeAnnotationRequest
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_genome_annotation_request = {"accession":"GCF_000001635.27"} # V2GenomeAnnotationRequest | 

    try:
        # Preview feature download by POST
        api_response = api_instance.genome_annotation_download_summary_by_post(v2_genome_annotation_request)
        print("The response of GenomeApi->genome_annotation_download_summary_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_annotation_download_summary_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_genome_annotation_request** | [**V2GenomeAnnotationRequest**](V2GenomeAnnotationRequest.md)|  | 

### Return type

[**V2DownloadSummary**](V2DownloadSummary.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genome_annotation_report**
> V2reportsGenomeAnnotationReportPage genome_annotation_report(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, page_size=page_size, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_token=page_token)

Get genome annotation reports by genome accession

Get genome annotation reports by genome accession.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_genome_annotation_request_genome_annotation_table_format import V2GenomeAnnotationRequestGenomeAnnotationTableFormat
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_genome_annotation_report_page import V2reportsGenomeAnnotationReportPage
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accession = 'GCF_000001635.27' # str | 
    annotation_ids = ['annotation_ids_example'] # List[str] | Limit the reports by internal, unstable annotation ids. (optional)
    symbols = ['symbols_example'] # List[str] | Filter parameters (optional)
    locations = ['locations_example'] # List[str] | Locations with a chromosome or accession and optional start-stop range: chromosome|accession[:start-end] (optional)
    gene_types = ['gene_types_example'] # List[str] | granular gene_types (optional)
    search_text = ['search_text_example'] # List[str] |  (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = ncbi.datasets.openapi.V2SortDirection() # V2SortDirection |  (optional)
    page_size = 20 # int | The maximum number of features to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    table_fields = ['table_fields_example'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = ncbi.datasets.openapi.V2GenomeAnnotationRequestGenomeAnnotationTableFormat() # V2GenomeAnnotationRequestGenomeAnnotationTableFormat | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_token = 'page_token_example' # str | A page token is returned from a `GetFeatures` call with more than `page_size` results. Use this token, along with the previous `FeatureRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)

    try:
        # Get genome annotation reports by genome accession
        api_response = api_instance.genome_annotation_report(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, page_size=page_size, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_token=page_token)
        print("The response of GenomeApi->genome_annotation_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_annotation_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**|  | 
 **annotation_ids** | [**List[str]**](str.md)| Limit the reports by internal, unstable annotation ids. | [optional] 
 **symbols** | [**List[str]**](str.md)| Filter parameters | [optional] 
 **locations** | [**List[str]**](str.md)| Locations with a chromosome or accession and optional start-stop range: chromosome|accession[:start-end] | [optional] 
 **gene_types** | [**List[str]**](str.md)| granular gene_types | [optional] 
 **search_text** | [**List[str]**](str.md)|  | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] 
 **page_size** | **int**| The maximum number of features to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | [**V2GenomeAnnotationRequestGenomeAnnotationTableFormat**](.md)| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_token** | **str**| A page token is returned from a &#x60;GetFeatures&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;FeatureRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 

### Return type

[**V2reportsGenomeAnnotationReportPage**](V2reportsGenomeAnnotationReportPage.md)

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

# **genome_annotation_report_by_post**
> V2reportsGenomeAnnotationReportPage genome_annotation_report_by_post(v2_genome_annotation_request)

Get genome annotation reports by genome accession

Get genome annotation reports by genome accession.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_genome_annotation_request import V2GenomeAnnotationRequest
from ncbi.datasets.openapi.models.v2reports_genome_annotation_report_page import V2reportsGenomeAnnotationReportPage
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_genome_annotation_request = {"accession":"GCF_000001635.27"} # V2GenomeAnnotationRequest | 

    try:
        # Get genome annotation reports by genome accession
        api_response = api_instance.genome_annotation_report_by_post(v2_genome_annotation_request)
        print("The response of GenomeApi->genome_annotation_report_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_annotation_report_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_genome_annotation_request** | [**V2GenomeAnnotationRequest**](V2GenomeAnnotationRequest.md)|  | 

### Return type

[**V2reportsGenomeAnnotationReportPage**](V2reportsGenomeAnnotationReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, application/x-ndjson, text/tab-separated-values

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genome_dataset_report**
> V2reportsAssemblyDataReportPage genome_dataset_report(accessions, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)

Get dataset reports by accessions

Get dataset reports by accessions.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_source import V2AssemblyDatasetDescriptorsFilterAssemblySource
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_version import V2AssemblyDatasetDescriptorsFilterAssemblyVersion
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_metagenome_derived_filter import V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_type_material_category import V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request_content_type import V2AssemblyDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_assembly_data_report_page import V2reportsAssemblyDataReportPage
from ncbi.datasets.openapi.models.v2reports_assembly_level import V2reportsAssemblyLevel
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accessions = ['[\"GCF_000001405.40\"]'] # List[str] | 
    filters_reference_only = False # bool | If true, only return reference genome assemblies (optional) (default to False)
    filters_assembly_source = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblySource() # V2AssemblyDatasetDescriptorsFilterAssemblySource | Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies (optional)
    filters_has_annotation = False # bool | Return only annotated genome assemblies (optional) (default to False)
    filters_exclude_paired_reports = False # bool | For paired (GCA/GCF) records, only return the primary record (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical (optional) (default to False)
    filters_assembly_version = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblyVersion() # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Return all assemblies, including replaced and suppressed, or only current assemblies (optional)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. (optional)
    filters_first_release_date = '2015-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or after the specified date By default, do not filter. (optional)
    filters_last_release_date = '2021-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or before to the specified date By default, do not filter. (optional)
    filters_search_text = ['[\"Genome Reference Consortium\"]'] # List[str] | Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter (optional)
    filters_is_metagenome_derived = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter() # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter |  (optional)
    filters_is_type_material = False # bool | If true, include only type materials (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, include only ICTV Exemplars (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude large multi-isolate projects (optional) (default to False)
    filters_type_material_category = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory() # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory |  (optional)
    tax_exact_match = False # bool | If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. (optional) (default to False)
    table_fields = ['[\"assminfo-accession\",\"assminfo-name\"]'] # List[str] |  (optional)
    returned_content = ncbi.datasets.openapi.V2AssemblyDatasetReportsRequestContentType() # V2AssemblyDatasetReportsRequestContentType | Return either assembly accessions, or complete assembly reports (optional)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = ncbi.datasets.openapi.V2SortDirection() # V2SortDirection |  (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)

    try:
        # Get dataset reports by accessions
        api_response = api_instance.genome_dataset_report(accessions, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_dataset_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_dataset_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)|  | 
 **filters_reference_only** | **bool**| If true, only return reference genome assemblies | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies | [optional] 
 **filters_has_annotation** | **bool**| Return only annotated genome assemblies | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| For paired (GCA/GCF) records, only return the primary record | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Return all assemblies, including replaced and suppressed, or only current assemblies | [optional] 
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. | [optional] 
 **filters_first_release_date** | **datetime**| Only return genome assemblies that were released on or after the specified date By default, do not filter. | [optional] 
 **filters_last_release_date** | **datetime**| Only return genome assemblies that were released on or before to the specified date By default, do not filter. | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)|  | [optional] 
 **filters_is_type_material** | **bool**| If true, include only type materials | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, include only ICTV Exemplars | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude large multi-isolate projects | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)|  | [optional] 
 **tax_exact_match** | **bool**| If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return either assembly accessions, or complete assembly reports | [optional] 
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 

### Return type

[**V2reportsAssemblyDataReportPage**](V2reportsAssemblyDataReportPage.md)

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

# **genome_dataset_report_by_post**
> V2reportsAssemblyDataReportPage genome_dataset_report_by_post(v2_assembly_dataset_reports_request)

Get dataset reports by accessions

Get a dataset report by accession.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request import V2AssemblyDatasetReportsRequest
from ncbi.datasets.openapi.models.v2reports_assembly_data_report_page import V2reportsAssemblyDataReportPage
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_assembly_dataset_reports_request = {"accessions":["GCF_000001405.40"]} # V2AssemblyDatasetReportsRequest | 

    try:
        # Get dataset reports by accessions
        api_response = api_instance.genome_dataset_report_by_post(v2_assembly_dataset_reports_request)
        print("The response of GenomeApi->genome_dataset_report_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_dataset_report_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_assembly_dataset_reports_request** | [**V2AssemblyDatasetReportsRequest**](V2AssemblyDatasetReportsRequest.md)|  | 

### Return type

[**V2reportsAssemblyDataReportPage**](V2reportsAssemblyDataReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, application/x-ndjson, text/tab-separated-values

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genome_dataset_reports_by_assembly_name**
> V2reportsAssemblyDataReportPage genome_dataset_reports_by_assembly_name(assembly_names, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)

Get dataset reports by assembly name (exact)

Get dataset reports by assembly name (exact).  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_source import V2AssemblyDatasetDescriptorsFilterAssemblySource
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_version import V2AssemblyDatasetDescriptorsFilterAssemblyVersion
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_metagenome_derived_filter import V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_type_material_category import V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request_content_type import V2AssemblyDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_assembly_data_report_page import V2reportsAssemblyDataReportPage
from ncbi.datasets.openapi.models.v2reports_assembly_level import V2reportsAssemblyLevel
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    assembly_names = ['[\"HanXRQr2.0-SUNRISE\"]'] # List[str] | 
    filters_reference_only = False # bool | If true, only return reference genome assemblies (optional) (default to False)
    filters_assembly_source = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblySource() # V2AssemblyDatasetDescriptorsFilterAssemblySource | Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies (optional)
    filters_has_annotation = False # bool | Return only annotated genome assemblies (optional) (default to False)
    filters_exclude_paired_reports = False # bool | For paired (GCA/GCF) records, only return the primary record (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical (optional) (default to False)
    filters_assembly_version = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblyVersion() # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Return all assemblies, including replaced and suppressed, or only current assemblies (optional)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. (optional)
    filters_first_release_date = '2015-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or after the specified date By default, do not filter. (optional)
    filters_last_release_date = '2021-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or before to the specified date By default, do not filter. (optional)
    filters_search_text = ['[\"Genome Reference Consortium\"]'] # List[str] | Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter (optional)
    filters_is_metagenome_derived = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter() # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter |  (optional)
    filters_is_type_material = False # bool | If true, include only type materials (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, include only ICTV Exemplars (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude large multi-isolate projects (optional) (default to False)
    filters_type_material_category = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory() # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory |  (optional)
    tax_exact_match = False # bool | If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. (optional) (default to False)
    table_fields = ['[\"assminfo-accession\",\"assminfo-name\"]'] # List[str] |  (optional)
    returned_content = ncbi.datasets.openapi.V2AssemblyDatasetReportsRequestContentType() # V2AssemblyDatasetReportsRequestContentType | Return either assembly accessions, or complete assembly reports (optional)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = ncbi.datasets.openapi.V2SortDirection() # V2SortDirection |  (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)

    try:
        # Get dataset reports by assembly name (exact)
        api_response = api_instance.genome_dataset_reports_by_assembly_name(assembly_names, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_dataset_reports_by_assembly_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_dataset_reports_by_assembly_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembly_names** | [**List[str]**](str.md)|  | 
 **filters_reference_only** | **bool**| If true, only return reference genome assemblies | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies | [optional] 
 **filters_has_annotation** | **bool**| Return only annotated genome assemblies | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| For paired (GCA/GCF) records, only return the primary record | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Return all assemblies, including replaced and suppressed, or only current assemblies | [optional] 
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. | [optional] 
 **filters_first_release_date** | **datetime**| Only return genome assemblies that were released on or after the specified date By default, do not filter. | [optional] 
 **filters_last_release_date** | **datetime**| Only return genome assemblies that were released on or before to the specified date By default, do not filter. | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)|  | [optional] 
 **filters_is_type_material** | **bool**| If true, include only type materials | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, include only ICTV Exemplars | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude large multi-isolate projects | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)|  | [optional] 
 **tax_exact_match** | **bool**| If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return either assembly accessions, or complete assembly reports | [optional] 
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 

### Return type

[**V2reportsAssemblyDataReportPage**](V2reportsAssemblyDataReportPage.md)

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

# **genome_dataset_reports_by_bioproject**
> V2reportsAssemblyDataReportPage genome_dataset_reports_by_bioproject(bioprojects, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)

Get dataset reports by bioproject

Get dataset reports by bioprojects.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_source import V2AssemblyDatasetDescriptorsFilterAssemblySource
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_version import V2AssemblyDatasetDescriptorsFilterAssemblyVersion
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_metagenome_derived_filter import V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_type_material_category import V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request_content_type import V2AssemblyDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_assembly_data_report_page import V2reportsAssemblyDataReportPage
from ncbi.datasets.openapi.models.v2reports_assembly_level import V2reportsAssemblyLevel
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    bioprojects = ['[\"PRJNA489243\"]'] # List[str] | 
    filters_reference_only = False # bool | If true, only return reference genome assemblies (optional) (default to False)
    filters_assembly_source = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblySource() # V2AssemblyDatasetDescriptorsFilterAssemblySource | Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies (optional)
    filters_has_annotation = False # bool | Return only annotated genome assemblies (optional) (default to False)
    filters_exclude_paired_reports = False # bool | For paired (GCA/GCF) records, only return the primary record (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical (optional) (default to False)
    filters_assembly_version = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblyVersion() # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Return all assemblies, including replaced and suppressed, or only current assemblies (optional)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. (optional)
    filters_first_release_date = '2015-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or after the specified date By default, do not filter. (optional)
    filters_last_release_date = '2021-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or before to the specified date By default, do not filter. (optional)
    filters_search_text = ['[\"Genome Reference Consortium\"]'] # List[str] | Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter (optional)
    filters_is_metagenome_derived = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter() # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter |  (optional)
    filters_is_type_material = False # bool | If true, include only type materials (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, include only ICTV Exemplars (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude large multi-isolate projects (optional) (default to False)
    filters_type_material_category = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory() # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory |  (optional)
    tax_exact_match = False # bool | If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. (optional) (default to False)
    table_fields = ['[\"assminfo-accession\",\"assminfo-name\"]'] # List[str] |  (optional)
    returned_content = ncbi.datasets.openapi.V2AssemblyDatasetReportsRequestContentType() # V2AssemblyDatasetReportsRequestContentType | Return either assembly accessions, or complete assembly reports (optional)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = ncbi.datasets.openapi.V2SortDirection() # V2SortDirection |  (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)

    try:
        # Get dataset reports by bioproject
        api_response = api_instance.genome_dataset_reports_by_bioproject(bioprojects, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_dataset_reports_by_bioproject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_dataset_reports_by_bioproject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bioprojects** | [**List[str]**](str.md)|  | 
 **filters_reference_only** | **bool**| If true, only return reference genome assemblies | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies | [optional] 
 **filters_has_annotation** | **bool**| Return only annotated genome assemblies | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| For paired (GCA/GCF) records, only return the primary record | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Return all assemblies, including replaced and suppressed, or only current assemblies | [optional] 
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. | [optional] 
 **filters_first_release_date** | **datetime**| Only return genome assemblies that were released on or after the specified date By default, do not filter. | [optional] 
 **filters_last_release_date** | **datetime**| Only return genome assemblies that were released on or before to the specified date By default, do not filter. | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)|  | [optional] 
 **filters_is_type_material** | **bool**| If true, include only type materials | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, include only ICTV Exemplars | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude large multi-isolate projects | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)|  | [optional] 
 **tax_exact_match** | **bool**| If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return either assembly accessions, or complete assembly reports | [optional] 
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 

### Return type

[**V2reportsAssemblyDataReportPage**](V2reportsAssemblyDataReportPage.md)

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

# **genome_dataset_reports_by_biosample_id**
> V2reportsAssemblyDataReportPage genome_dataset_reports_by_biosample_id(biosample_ids, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)

Get dataset reports by biosample id

Get dataset reports by biosample id.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_source import V2AssemblyDatasetDescriptorsFilterAssemblySource
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_version import V2AssemblyDatasetDescriptorsFilterAssemblyVersion
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_metagenome_derived_filter import V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_type_material_category import V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request_content_type import V2AssemblyDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_assembly_data_report_page import V2reportsAssemblyDataReportPage
from ncbi.datasets.openapi.models.v2reports_assembly_level import V2reportsAssemblyLevel
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    biosample_ids = ['[\"SAMN15960293\"]'] # List[str] | 
    filters_reference_only = False # bool | If true, only return reference genome assemblies (optional) (default to False)
    filters_assembly_source = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblySource() # V2AssemblyDatasetDescriptorsFilterAssemblySource | Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies (optional)
    filters_has_annotation = False # bool | Return only annotated genome assemblies (optional) (default to False)
    filters_exclude_paired_reports = False # bool | For paired (GCA/GCF) records, only return the primary record (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical (optional) (default to False)
    filters_assembly_version = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblyVersion() # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Return all assemblies, including replaced and suppressed, or only current assemblies (optional)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. (optional)
    filters_first_release_date = '2015-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or after the specified date By default, do not filter. (optional)
    filters_last_release_date = '2021-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or before to the specified date By default, do not filter. (optional)
    filters_search_text = ['[\"Genome Reference Consortium\"]'] # List[str] | Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter (optional)
    filters_is_metagenome_derived = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter() # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter |  (optional)
    filters_is_type_material = False # bool | If true, include only type materials (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, include only ICTV Exemplars (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude large multi-isolate projects (optional) (default to False)
    filters_type_material_category = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory() # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory |  (optional)
    tax_exact_match = False # bool | If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. (optional) (default to False)
    table_fields = ['[\"assminfo-accession\",\"assminfo-name\"]'] # List[str] |  (optional)
    returned_content = ncbi.datasets.openapi.V2AssemblyDatasetReportsRequestContentType() # V2AssemblyDatasetReportsRequestContentType | Return either assembly accessions, or complete assembly reports (optional)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = ncbi.datasets.openapi.V2SortDirection() # V2SortDirection |  (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)

    try:
        # Get dataset reports by biosample id
        api_response = api_instance.genome_dataset_reports_by_biosample_id(biosample_ids, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_dataset_reports_by_biosample_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_dataset_reports_by_biosample_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biosample_ids** | [**List[str]**](str.md)|  | 
 **filters_reference_only** | **bool**| If true, only return reference genome assemblies | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies | [optional] 
 **filters_has_annotation** | **bool**| Return only annotated genome assemblies | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| For paired (GCA/GCF) records, only return the primary record | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Return all assemblies, including replaced and suppressed, or only current assemblies | [optional] 
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. | [optional] 
 **filters_first_release_date** | **datetime**| Only return genome assemblies that were released on or after the specified date By default, do not filter. | [optional] 
 **filters_last_release_date** | **datetime**| Only return genome assemblies that were released on or before to the specified date By default, do not filter. | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)|  | [optional] 
 **filters_is_type_material** | **bool**| If true, include only type materials | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, include only ICTV Exemplars | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude large multi-isolate projects | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)|  | [optional] 
 **tax_exact_match** | **bool**| If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return either assembly accessions, or complete assembly reports | [optional] 
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 

### Return type

[**V2reportsAssemblyDataReportPage**](V2reportsAssemblyDataReportPage.md)

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

# **genome_dataset_reports_by_taxon**
> V2reportsAssemblyDataReportPage genome_dataset_reports_by_taxon(taxons, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)

Get dataset reports by taxons

Get dataset reports by taxons.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_source import V2AssemblyDatasetDescriptorsFilterAssemblySource
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_version import V2AssemblyDatasetDescriptorsFilterAssemblyVersion
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_metagenome_derived_filter import V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_type_material_category import V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request_content_type import V2AssemblyDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_assembly_data_report_page import V2reportsAssemblyDataReportPage
from ncbi.datasets.openapi.models.v2reports_assembly_level import V2reportsAssemblyLevel
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    taxons = ['[\"9606\"]'] # List[str] | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank
    filters_reference_only = False # bool | If true, only return reference genome assemblies (optional) (default to False)
    filters_assembly_source = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblySource() # V2AssemblyDatasetDescriptorsFilterAssemblySource | Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies (optional)
    filters_has_annotation = False # bool | Return only annotated genome assemblies (optional) (default to False)
    filters_exclude_paired_reports = False # bool | For paired (GCA/GCF) records, only return the primary record (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical (optional) (default to False)
    filters_assembly_version = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblyVersion() # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Return all assemblies, including replaced and suppressed, or only current assemblies (optional)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. (optional)
    filters_first_release_date = '2015-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or after the specified date By default, do not filter. (optional)
    filters_last_release_date = '2021-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or before to the specified date By default, do not filter. (optional)
    filters_search_text = ['[\"Genome Reference Consortium\"]'] # List[str] | Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter (optional)
    filters_is_metagenome_derived = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter() # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter |  (optional)
    filters_is_type_material = False # bool | If true, include only type materials (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, include only ICTV Exemplars (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude large multi-isolate projects (optional) (default to False)
    filters_type_material_category = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory() # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory |  (optional)
    tax_exact_match = False # bool | If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. (optional) (default to False)
    table_fields = ['[\"assminfo-accession\",\"assminfo-name\"]'] # List[str] |  (optional)
    returned_content = ncbi.datasets.openapi.V2AssemblyDatasetReportsRequestContentType() # V2AssemblyDatasetReportsRequestContentType | Return either assembly accessions, or complete assembly reports (optional)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = ncbi.datasets.openapi.V2SortDirection() # V2SortDirection |  (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)

    try:
        # Get dataset reports by taxons
        api_response = api_instance.genome_dataset_reports_by_taxon(taxons, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_dataset_reports_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_dataset_reports_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxons** | [**List[str]**](str.md)| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank | 
 **filters_reference_only** | **bool**| If true, only return reference genome assemblies | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies | [optional] 
 **filters_has_annotation** | **bool**| Return only annotated genome assemblies | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| For paired (GCA/GCF) records, only return the primary record | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Return all assemblies, including replaced and suppressed, or only current assemblies | [optional] 
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. | [optional] 
 **filters_first_release_date** | **datetime**| Only return genome assemblies that were released on or after the specified date By default, do not filter. | [optional] 
 **filters_last_release_date** | **datetime**| Only return genome assemblies that were released on or before to the specified date By default, do not filter. | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)|  | [optional] 
 **filters_is_type_material** | **bool**| If true, include only type materials | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, include only ICTV Exemplars | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude large multi-isolate projects | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)|  | [optional] 
 **tax_exact_match** | **bool**| If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return either assembly accessions, or complete assembly reports | [optional] 
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 

### Return type

[**V2reportsAssemblyDataReportPage**](V2reportsAssemblyDataReportPage.md)

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

# **genome_dataset_reports_by_wgs**
> V2reportsAssemblyDataReportPage genome_dataset_reports_by_wgs(wgs_accessions, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)

Get dataset reports by wgs accession

Get dataset reports by wgs accession.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_source import V2AssemblyDatasetDescriptorsFilterAssemblySource
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_version import V2AssemblyDatasetDescriptorsFilterAssemblyVersion
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_metagenome_derived_filter import V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_type_material_category import V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request_content_type import V2AssemblyDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_assembly_data_report_page import V2reportsAssemblyDataReportPage
from ncbi.datasets.openapi.models.v2reports_assembly_level import V2reportsAssemblyLevel
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    wgs_accessions = ['[\"JAXUCZ01\"]'] # List[str] | 
    filters_reference_only = False # bool | If true, only return reference genome assemblies (optional) (default to False)
    filters_assembly_source = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblySource() # V2AssemblyDatasetDescriptorsFilterAssemblySource | Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies (optional)
    filters_has_annotation = False # bool | Return only annotated genome assemblies (optional) (default to False)
    filters_exclude_paired_reports = False # bool | For paired (GCA/GCF) records, only return the primary record (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical (optional) (default to False)
    filters_assembly_version = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterAssemblyVersion() # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Return all assemblies, including replaced and suppressed, or only current assemblies (optional)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. (optional)
    filters_first_release_date = '2015-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or after the specified date By default, do not filter. (optional)
    filters_last_release_date = '2021-01-10T00:00:00Z' # datetime | Only return genome assemblies that were released on or before to the specified date By default, do not filter. (optional)
    filters_search_text = ['[\"Genome Reference Consortium\"]'] # List[str] | Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter (optional)
    filters_is_metagenome_derived = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter() # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter |  (optional)
    filters_is_type_material = False # bool | If true, include only type materials (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, include only ICTV Exemplars (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude large multi-isolate projects (optional) (default to False)
    filters_type_material_category = ncbi.datasets.openapi.V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory() # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory |  (optional)
    tax_exact_match = False # bool | If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. (optional) (default to False)
    table_fields = ['[\"assminfo-accession\",\"assminfo-name\"]'] # List[str] |  (optional)
    returned_content = ncbi.datasets.openapi.V2AssemblyDatasetReportsRequestContentType() # V2AssemblyDatasetReportsRequestContentType | Return either assembly accessions, or complete assembly reports (optional)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = ncbi.datasets.openapi.V2SortDirection() # V2SortDirection |  (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)

    try:
        # Get dataset reports by wgs accession
        api_response = api_instance.genome_dataset_reports_by_wgs(wgs_accessions, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_dataset_reports_by_wgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_dataset_reports_by_wgs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wgs_accessions** | [**List[str]**](str.md)|  | 
 **filters_reference_only** | **bool**| If true, only return reference genome assemblies | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Return only RefSeq (GCF_) or GenBank (GCA_) genome assemblies | [optional] 
 **filters_has_annotation** | **bool**| Return only annotated genome assemblies | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| For paired (GCA/GCF) records, only return the primary record | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude atypical genomes, i.e. genomes that have assembly issues or are otherwise atypical | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Return all assemblies, including replaced and suppressed, or only current assemblies | [optional] 
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Only return genome assemblies that have one of the specified assembly levels. By default, do not filter. | [optional] 
 **filters_first_release_date** | **datetime**| Only return genome assemblies that were released on or after the specified date By default, do not filter. | [optional] 
 **filters_last_release_date** | **datetime**| Only return genome assemblies that were released on or before to the specified date By default, do not filter. | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Only return results whose fields contain the specified search terms in their taxon, infraspecific, assembly name or submitter fields By default, do not filter | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)|  | [optional] 
 **filters_is_type_material** | **bool**| If true, include only type materials | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, include only ICTV Exemplars | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude large multi-isolate projects | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)|  | [optional] 
 **tax_exact_match** | **bool**| If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return either assembly accessions, or complete assembly reports | [optional] 
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 

### Return type

[**V2reportsAssemblyDataReportPage**](V2reportsAssemblyDataReportPage.md)

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

# **genome_download_summary**
> V2DownloadSummary genome_download_summary(accessions, chromosomes=chromosomes, include_annotation_type=include_annotation_type)

Preview genome dataset download

Get a download summary by accession in a JSON output format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_annotation_for_assembly_type import V2AnnotationForAssemblyType
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accessions = ['[\"GCF_000001405.40\"]'] # List[str] | NCBI genome assembly accessions
    chromosomes = ['[\"1\",\"2\",\"3\",\"X\",\"Y\",\"MT\"]'] # List[str] | The default setting is all chromosome. Specify individual chromosome by string (1,2,MT or chr1,chr2.chrMT). Unplaced sequences are treated like their own chromosome ('Un'). The filter only applies to fasta sequence. (optional)
    include_annotation_type = [ncbi.datasets.openapi.V2AnnotationForAssemblyType()] # List[V2AnnotationForAssemblyType] | Select additional types of annotation to include in the data package.  If unset, no annotation is provided. (optional)

    try:
        # Preview genome dataset download
        api_response = api_instance.genome_download_summary(accessions, chromosomes=chromosomes, include_annotation_type=include_annotation_type)
        print("The response of GenomeApi->genome_download_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_download_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| NCBI genome assembly accessions | 
 **chromosomes** | [**List[str]**](str.md)| The default setting is all chromosome. Specify individual chromosome by string (1,2,MT or chr1,chr2.chrMT). Unplaced sequences are treated like their own chromosome (&#39;Un&#39;). The filter only applies to fasta sequence. | [optional] 
 **include_annotation_type** | [**List[V2AnnotationForAssemblyType]**](V2AnnotationForAssemblyType.md)| Select additional types of annotation to include in the data package.  If unset, no annotation is provided. | [optional] 

### Return type

[**V2DownloadSummary**](V2DownloadSummary.md)

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

# **genome_download_summary_by_post**
> V2DownloadSummary genome_download_summary_by_post(v2_assembly_dataset_request)

Preview genome dataset download by POST

The 'GET' version of download summary is limited by the size of the GET URL (2KB, which works out to about 140 genomic accessions).  The POST operation is provided to allow users to supply a larger number of accessions in a single request.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_dataset_request import V2AssemblyDatasetRequest
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_assembly_dataset_request = {"accessions":["GCF_000001405.40"]} # V2AssemblyDatasetRequest | 

    try:
        # Preview genome dataset download by POST
        api_response = api_instance.genome_download_summary_by_post(v2_assembly_dataset_request)
        print("The response of GenomeApi->genome_download_summary_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_download_summary_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_assembly_dataset_request** | [**V2AssemblyDatasetRequest**](V2AssemblyDatasetRequest.md)|  | 

### Return type

[**V2DownloadSummary**](V2DownloadSummary.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genome_links_by_accession**
> V2AssemblyLinksReply genome_links_by_accession(accessions)

Get assembly links by accessions

Get links to available assembly resources by accessions.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_links_reply import V2AssemblyLinksReply
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accessions = ['[\"GCF_000001405.40\"]'] # List[str] | NCBI genome assembly accessions, limited to 1000

    try:
        # Get assembly links by accessions
        api_response = api_instance.genome_links_by_accession(accessions)
        print("The response of GenomeApi->genome_links_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_links_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| NCBI genome assembly accessions, limited to 1000 | 

### Return type

[**V2AssemblyLinksReply**](V2AssemblyLinksReply.md)

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

# **genome_links_by_accession_by_post**
> V2AssemblyLinksReply genome_links_by_accession_by_post(v2_assembly_links_request)

Get assembly links by accessions

Get links to available assembly resources by accessions.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_links_reply import V2AssemblyLinksReply
from ncbi.datasets.openapi.models.v2_assembly_links_request import V2AssemblyLinksRequest
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_assembly_links_request = {"accessions":["GCF_000001405.40"]} # V2AssemblyLinksRequest | 

    try:
        # Get assembly links by accessions
        api_response = api_instance.genome_links_by_accession_by_post(v2_assembly_links_request)
        print("The response of GenomeApi->genome_links_by_accession_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_links_by_accession_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_assembly_links_request** | [**V2AssemblyLinksRequest**](V2AssemblyLinksRequest.md)|  | 

### Return type

[**V2AssemblyLinksReply**](V2AssemblyLinksReply.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genome_sequence_report**
> V2SequenceReportPage genome_sequence_report(accession, chromosomes=chromosomes, role_filters=role_filters, table_fields=table_fields, count_assembly_unplaced=count_assembly_unplaced, page_size=page_size, page_token=page_token, include_tabular_header=include_tabular_header)

Get sequence reports by accessions

Get a sequence report by accession.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sequence_report_page import V2SequenceReportPage
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    accession = 'GCF_000001635.27' # str | 
    chromosomes = ['[\"1\",\"2\",\"3\",\"X\",\"Y\",\"MT\"]'] # List[str] |  (optional)
    role_filters = ['[\"assembled-molecule\",\"unlocalized-scaffold\",\"unplaced-scaffold\"]'] # List[str] |  (optional)
    table_fields = ['[\"accession\",\"chr-name\"]'] # List[str] |  (optional)
    count_assembly_unplaced = False # bool |  (optional) (default to False)
    page_size = 20 # int | The maximum number of genome assemblies to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `GetSequenceReports` call with more than `page_size` results. Use this token, along with the previous `AssemblyMetadataRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader |  (optional)

    try:
        # Get sequence reports by accessions
        api_response = api_instance.genome_sequence_report(accession, chromosomes=chromosomes, role_filters=role_filters, table_fields=table_fields, count_assembly_unplaced=count_assembly_unplaced, page_size=page_size, page_token=page_token, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_sequence_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_sequence_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**|  | 
 **chromosomes** | [**List[str]**](str.md)|  | [optional] 
 **role_filters** | [**List[str]**](str.md)|  | [optional] 
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **count_assembly_unplaced** | **bool**|  | [optional] [default to False]
 **page_size** | **int**| The maximum number of genome assemblies to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;GetSequenceReports&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyMetadataRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)|  | [optional] 

### Return type

[**V2SequenceReportPage**](V2SequenceReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, text/tab-separated-values, application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genome_sequence_report_by_post**
> V2SequenceReportPage genome_sequence_report_by_post(v2_assembly_sequence_reports_request)

Get sequence reports by accessions

Get a sequence report by accession.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_assembly_sequence_reports_request import V2AssemblySequenceReportsRequest
from ncbi.datasets.openapi.models.v2_sequence_report_page import V2SequenceReportPage
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
    api_instance = ncbi.datasets.openapi.GenomeApi(api_client)
    v2_assembly_sequence_reports_request = {"accession":"GCF_000001405.40"} # V2AssemblySequenceReportsRequest | 

    try:
        # Get sequence reports by accessions
        api_response = api_instance.genome_sequence_report_by_post(v2_assembly_sequence_reports_request)
        print("The response of GenomeApi->genome_sequence_report_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_sequence_report_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_assembly_sequence_reports_request** | [**V2AssemblySequenceReportsRequest**](V2AssemblySequenceReportsRequest.md)|  | 

### Return type

[**V2SequenceReportPage**](V2SequenceReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, text/tab-separated-values, application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

