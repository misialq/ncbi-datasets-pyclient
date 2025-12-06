# ncbi.datasets.openapi.GenomeApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotation_report_facets_by_accession**](GenomeApi.md#annotation_report_facets_by_accession) | **GET** /genome/accession/{accession}/annotation_summary | Get genome annotation report summary information by genome assembly accession
[**annotation_report_facets_by_post**](GenomeApi.md#annotation_report_facets_by_post) | **POST** /genome/annotation_summary | Get genome annotation report summary information by genome assembly accession
[**assembly_accessions_for_sequence_accession**](GenomeApi.md#assembly_accessions_for_sequence_accession) | **GET** /genome/sequence_accession/{accession}/sequence_assemblies | Get a genome assembly accession for a nucleotide sequence accession
[**assembly_accessions_for_sequence_accession_by_post**](GenomeApi.md#assembly_accessions_for_sequence_accession_by_post) | **POST** /genome/sequence_assemblies | Get a genome assembly accession for a nucleotide sequence accession
[**assembly_revision_history_by_get**](GenomeApi.md#assembly_revision_history_by_get) | **GET** /genome/accession/{accession}/revision_history | Get a revision history for a genome assembly by genome assembly accession
[**assembly_revision_history_by_post**](GenomeApi.md#assembly_revision_history_by_post) | **POST** /genome/revision_history | Get a revision history for a genome assembly by genome assembly accession
[**check_assembly_availability**](GenomeApi.md#check_assembly_availability) | **GET** /genome/accession/{accessions}/check | Check the validity of a genome assembly accession
[**check_assembly_availability_post**](GenomeApi.md#check_assembly_availability_post) | **POST** /genome/check | Check the validity of a genome assembly accession
[**checkm_histogram_by_taxon**](GenomeApi.md#checkm_histogram_by_taxon) | **GET** /genome/taxon/{species_taxon}/checkm_histogram | Get CheckM histogram data by species taxon
[**checkm_histogram_by_taxon_by_post**](GenomeApi.md#checkm_histogram_by_taxon_by_post) | **POST** /genome/checkm_histogram | Get CheckM histogram data by species taxon
[**download_assembly_package**](GenomeApi.md#download_assembly_package) | **GET** /genome/accession/{accessions}/download | Get a genome data package by genome assembly accession
[**download_assembly_package_post**](GenomeApi.md#download_assembly_package_post) | **POST** /genome/download | Get a genome data package by genome assembly accession
[**download_genome_annotation_package**](GenomeApi.md#download_genome_annotation_package) | **GET** /genome/accession/{accession}/annotation_report/download | Get a genome annotation data package by genome assembly accession
[**download_genome_annotation_package_by_post**](GenomeApi.md#download_genome_annotation_package_by_post) | **POST** /genome/annotation_report/download | Get a genome annotation data package by genome assembly accession
[**genome_annotation_download_summary**](GenomeApi.md#genome_annotation_download_summary) | **GET** /genome/accession/{accession}/annotation_report/download_summary | Get a download summary (preview) of a genome annotation data package by genome assembly accession
[**genome_annotation_download_summary_by_post**](GenomeApi.md#genome_annotation_download_summary_by_post) | **POST** /genome/annotation_report/download_summary | Get a download summary (preview) of a genome annotation data package by genome assembly accession
[**genome_annotation_report**](GenomeApi.md#genome_annotation_report) | **GET** /genome/accession/{accession}/annotation_report | Get genome annotation reports by genome assembly accession
[**genome_annotation_report_by_post**](GenomeApi.md#genome_annotation_report_by_post) | **POST** /genome/annotation_report | Get genome annotation reports by genome assembly accession
[**genome_dataset_report**](GenomeApi.md#genome_dataset_report) | **GET** /genome/accession/{accessions}/dataset_report | Get a genome assembly report by genome assembly accession
[**genome_dataset_report_by_post**](GenomeApi.md#genome_dataset_report_by_post) | **POST** /genome/dataset_report | Get a genome assembly report
[**genome_dataset_reports_by_assembly_name**](GenomeApi.md#genome_dataset_reports_by_assembly_name) | **GET** /genome/assembly_name/{assembly_names}/dataset_report | Get genome assembly reports by assembly name
[**genome_dataset_reports_by_bioproject**](GenomeApi.md#genome_dataset_reports_by_bioproject) | **GET** /genome/bioproject/{bioprojects}/dataset_report | Get genome assembly reports by BioProject accession
[**genome_dataset_reports_by_biosample_id**](GenomeApi.md#genome_dataset_reports_by_biosample_id) | **GET** /genome/biosample/{biosample_ids}/dataset_report | Get genome assembly reports by BioSample accession
[**genome_dataset_reports_by_taxon**](GenomeApi.md#genome_dataset_reports_by_taxon) | **GET** /genome/taxon/{taxons}/dataset_report | Get a genome assembly report by taxon
[**genome_dataset_reports_by_wgs**](GenomeApi.md#genome_dataset_reports_by_wgs) | **GET** /genome/wgs/{wgs_accessions}/dataset_report | Get a genome assembly data report by WGS accession
[**genome_download_summary**](GenomeApi.md#genome_download_summary) | **GET** /genome/accession/{accessions}/download_summary | Get a download summary (preview) of a genome data package by genome assembly accession
[**genome_download_summary_by_post**](GenomeApi.md#genome_download_summary_by_post) | **POST** /genome/download_summary | Get a download summary (preview) of a genome data package by genome assembly accession
[**genome_links_by_accession**](GenomeApi.md#genome_links_by_accession) | **GET** /genome/accession/{accessions}/links | Get assembly links by genome assembly accession
[**genome_links_by_accession_by_post**](GenomeApi.md#genome_links_by_accession_by_post) | **POST** /genome/links | Get assembly links by genome assembly accession
[**genome_sequence_report**](GenomeApi.md#genome_sequence_report) | **GET** /genome/accession/{accession}/sequence_reports | Get a genome sequence report by genome assembly accession
[**genome_sequence_report_by_post**](GenomeApi.md#genome_sequence_report_by_post) | **POST** /genome/sequence_reports | Get a genome sequence report by genome assembly accession


# **annotation_report_facets_by_accession**
> V2GenomeAnnotationTableSummaryReply annotation_report_facets_by_accession(accession, sort_field=sort_field, sort_direction=sort_direction)

Get genome annotation report summary information by genome assembly accession

Get genome annotation report summary information by genome assembly accession in JSON format, including chromosome names and gene types.

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
    accession = 'GCF_000001635.27' # str | One or more genome assembly accessions, limited to 100
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)

    try:
        # Get genome annotation report summary information by genome assembly accession
        api_response = api_instance.annotation_report_facets_by_accession(accession, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of GenomeApi->annotation_report_facets_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->annotation_report_facets_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**| One or more genome assembly accessions, limited to 100 | 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]

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

Get genome annotation report summary information by genome assembly accession

Get genome annotation report summary information by genome assembly accession in JSON format, including chromosome names and gene types.

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
        # Get genome annotation report summary information by genome assembly accession
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

Get a genome assembly accession for a nucleotide sequence accession

Get a genome assembly accession for a nucleotide sequence accession in JSON format.

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
    accession = 'NC_000001.11' # str | Nucleotide sequence accession associated with a genome assembly

    try:
        # Get a genome assembly accession for a nucleotide sequence accession
        api_response = api_instance.assembly_accessions_for_sequence_accession(accession)
        print("The response of GenomeApi->assembly_accessions_for_sequence_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->assembly_accessions_for_sequence_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**| Nucleotide sequence accession associated with a genome assembly | 

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

Get a genome assembly accession for a nucleotide sequence accession

Get a genome assembly accession for a nucleotide sequence accession in JSON format.

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
        # Get a genome assembly accession for a nucleotide sequence accession
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

Get a revision history for a genome assembly by genome assembly accession

Get a revision history, or list of all versions of a genome assembly, in JSON format.

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
    accession = 'GCF_000001405.40' # str | One genome assembly accession

    try:
        # Get a revision history for a genome assembly by genome assembly accession
        api_response = api_instance.assembly_revision_history_by_get(accession)
        print("The response of GenomeApi->assembly_revision_history_by_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->assembly_revision_history_by_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**| One genome assembly accession | 

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

Get a revision history for a genome assembly by genome assembly accession

Get a revision history, or list of all versions of a genome assembly, in JSON format.

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
        # Get a revision history for a genome assembly by genome assembly accession
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

Check the validity of a genome assembly accession

Check the validity of a genome assembly accession. Output in JSON format.

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
    accessions = ['GCF_000001405.40'] # List[str] | One or more genome assembly accessions, limited to 100

    try:
        # Check the validity of a genome assembly accession
        api_response = api_instance.check_assembly_availability(accessions)
        print("The response of GenomeApi->check_assembly_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->check_assembly_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more genome assembly accessions, limited to 100 | 

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

Check the validity of a genome assembly accession

Check the validity of a genome assembly accession. Output in JSON format.

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
    v2_assembly_dataset_request = {"accessions":["GCF_031307605.1"],"include_annotation_type":["GENOME_FASTA","GENOME_GFF","SEQUENCE_REPORT"]} # V2AssemblyDatasetRequest | 

    try:
        # Check the validity of a genome assembly accession
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

Get CheckM histogram data by species taxon

Get CheckM histogram data by species taxon. This data is used for rendering CheckM histograms on bacterial genome pages.

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
    species_taxon = '202956' # str | Bacterial species taxonomy ID or taxonomic name

    try:
        # Get CheckM histogram data by species taxon
        api_response = api_instance.checkm_histogram_by_taxon(species_taxon)
        print("The response of GenomeApi->checkm_histogram_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->checkm_histogram_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **species_taxon** | **str**| Bacterial species taxonomy ID or taxonomic name | 

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

Get CheckM histogram data by species taxon

Get CheckM histogram data by species taxon. This data is used for rendering CheckM histograms on bacterial genome pages.

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
        # Get CheckM histogram data by species taxon
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

Get a genome data package by genome assembly accession

Download a genome data package including sequence, annotation, and a detailed data report by genome assembly accession.

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
    accessions = ['GCF_000001405.40'] # List[str] | One or more genome assembly accessions, limited to 100
    chromosomes = ['[\"1\",\"MT\"]'] # List[str] | Only return genomic fasta sequence for the specified chromosomes. (optional)
    include_annotation_type = [ncbi.datasets.openapi.V2AnnotationForAssemblyType()] # List[V2AnnotationForAssemblyType] | Specify which sequence, annotation, and report files to include in the data package. The assembly data report is always included, and its inclusion is not affected by this parameter. (optional)
    hydrated = FULLY_HYDRATED # V2AssemblyDatasetRequestResolution | Specify whether to download a hydrated (with sequence and annotation files included) or dehydrated data package. A dehydrated data package includes the assembly data report and `fetch.txt`, which includes paths to the requested data files on NCBI servers. (optional) (default to FULLY_HYDRATED)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a genome data package by genome assembly accession
        api_response = api_instance.download_assembly_package(accessions, chromosomes=chromosomes, include_annotation_type=include_annotation_type, hydrated=hydrated, filename=filename)
        print("The response of GenomeApi->download_assembly_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->download_assembly_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more genome assembly accessions, limited to 100 | 
 **chromosomes** | [**List[str]**](str.md)| Only return genomic fasta sequence for the specified chromosomes. | [optional] 
 **include_annotation_type** | [**List[V2AnnotationForAssemblyType]**](V2AnnotationForAssemblyType.md)| Specify which sequence, annotation, and report files to include in the data package. The assembly data report is always included, and its inclusion is not affected by this parameter. | [optional] 
 **hydrated** | [**V2AssemblyDatasetRequestResolution**](.md)| Specify whether to download a hydrated (with sequence and annotation files included) or dehydrated data package. A dehydrated data package includes the assembly data report and &#x60;fetch.txt&#x60;, which includes paths to the requested data files on NCBI servers. | [optional] [default to FULLY_HYDRATED]
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

Get a genome data package by genome assembly accession

Download a genome data package including sequence, annotation, and a detailed data report by genome assembly accession.

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
    v2_assembly_dataset_request = {"accessions":["GCF_031307605.1"],"include_annotation_type":["GENOME_FASTA","GENOME_GFF","SEQUENCE_REPORT"]} # V2AssemblyDatasetRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a genome data package by genome assembly accession
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
> bytearray download_genome_annotation_package(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, include_annotation_type=include_annotation_type, filename=filename)

Get a genome annotation data package by genome assembly accession

Download an annotation data package including sequence and a detailed annotation report by genome assembly accession.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_genome_annotation_request_annotation_type import V2GenomeAnnotationRequestAnnotationType
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
    accession = 'GCF_000001635.27' # str | One or more genome assembly accessions, limited to 100
    annotation_ids = ['1'] # List[str] | Limit to one or more features annotated on the genome by specifying a number corresponding to a row_id (unstable). (optional)
    symbols = ['Qsox1'] # List[str] | Limit to annotated features matching the given gene symbol (case-sensitive). (optional)
    locations = ['1:1-1000'] # List[str] | Limit to features annotated at a specific location on the genome, by specifying a chromosome name or accession and optional start-stop range. (optional)
    gene_types = ['protein-coding'] # List[str] | Limit to features of a specified gene locus type. (optional)
    search_text = ['kinase'] # List[str] | Limit to features that match the specified gene symbol, gene name or protein name. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    include_annotation_type = [ncbi.datasets.openapi.V2GenomeAnnotationRequestAnnotationType()] # List[V2GenomeAnnotationRequestAnnotationType] | Specify which sequence files to include in the data package. Options include gene (GENOME_FASTA), transcript (RNA_FASTA), and protein (PROT_FASTA) sequences. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a genome annotation data package by genome assembly accession
        api_response = api_instance.download_genome_annotation_package(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, include_annotation_type=include_annotation_type, filename=filename)
        print("The response of GenomeApi->download_genome_annotation_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->download_genome_annotation_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**| One or more genome assembly accessions, limited to 100 | 
 **annotation_ids** | [**List[str]**](str.md)| Limit to one or more features annotated on the genome by specifying a number corresponding to a row_id (unstable). | [optional] 
 **symbols** | [**List[str]**](str.md)| Limit to annotated features matching the given gene symbol (case-sensitive). | [optional] 
 **locations** | [**List[str]**](str.md)| Limit to features annotated at a specific location on the genome, by specifying a chromosome name or accession and optional start-stop range. | [optional] 
 **gene_types** | [**List[str]**](str.md)| Limit to features of a specified gene locus type. | [optional] 
 **search_text** | [**List[str]**](str.md)| Limit to features that match the specified gene symbol, gene name or protein name. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **include_annotation_type** | [**List[V2GenomeAnnotationRequestAnnotationType]**](V2GenomeAnnotationRequestAnnotationType.md)| Specify which sequence files to include in the data package. Options include gene (GENOME_FASTA), transcript (RNA_FASTA), and protein (PROT_FASTA) sequences. | [optional] 
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

Get a genome annotation data package by genome assembly accession

Download an annotation data package including sequence and a detailed annotation report by genome assembly accession.

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
        # Get a genome annotation data package by genome assembly accession
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
> V2DownloadSummary genome_annotation_download_summary(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, include_annotation_type=include_annotation_type)

Get a download summary (preview) of a genome annotation data package by genome assembly accession

Get a downlaod summary (preview) of a genome annotation data package, including counts and file sizes, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
from ncbi.datasets.openapi.models.v2_genome_annotation_request_annotation_type import V2GenomeAnnotationRequestAnnotationType
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
    accession = 'GCF_000001635.27' # str | One or more genome assembly accessions, limited to 100
    annotation_ids = ['1'] # List[str] | Limit to one or more features annotated on the genome by specifying a number corresponding to a row_id (unstable). (optional)
    symbols = ['Qsox1'] # List[str] | Limit to annotated features matching the given gene symbol (case-sensitive). (optional)
    locations = ['1:1-1000'] # List[str] | Limit to features annotated at a specific location on the genome, by specifying a chromosome name or accession and optional start-stop range. (optional)
    gene_types = ['protein-coding'] # List[str] | Limit to features of a specified gene locus type. (optional)
    search_text = ['kinase'] # List[str] | Limit to features that match the specified gene symbol, gene name or protein name. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    include_annotation_type = [ncbi.datasets.openapi.V2GenomeAnnotationRequestAnnotationType()] # List[V2GenomeAnnotationRequestAnnotationType] | Specify which sequence files to include in the data package. Options include gene (GENOME_FASTA), transcript (RNA_FASTA), and protein (PROT_FASTA) sequences. (optional)

    try:
        # Get a download summary (preview) of a genome annotation data package by genome assembly accession
        api_response = api_instance.genome_annotation_download_summary(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, include_annotation_type=include_annotation_type)
        print("The response of GenomeApi->genome_annotation_download_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_annotation_download_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**| One or more genome assembly accessions, limited to 100 | 
 **annotation_ids** | [**List[str]**](str.md)| Limit to one or more features annotated on the genome by specifying a number corresponding to a row_id (unstable). | [optional] 
 **symbols** | [**List[str]**](str.md)| Limit to annotated features matching the given gene symbol (case-sensitive). | [optional] 
 **locations** | [**List[str]**](str.md)| Limit to features annotated at a specific location on the genome, by specifying a chromosome name or accession and optional start-stop range. | [optional] 
 **gene_types** | [**List[str]**](str.md)| Limit to features of a specified gene locus type. | [optional] 
 **search_text** | [**List[str]**](str.md)| Limit to features that match the specified gene symbol, gene name or protein name. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **include_annotation_type** | [**List[V2GenomeAnnotationRequestAnnotationType]**](V2GenomeAnnotationRequestAnnotationType.md)| Specify which sequence files to include in the data package. Options include gene (GENOME_FASTA), transcript (RNA_FASTA), and protein (PROT_FASTA) sequences. | [optional] 

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

Get a download summary (preview) of a genome annotation data package by genome assembly accession

Get a download summary (preview) of a genome annotation data package, including counts and file sizes, by genome assembly accession, in JSON format.

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
        # Get a download summary (preview) of a genome annotation data package by genome assembly accession
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
> V2reportsGenomeAnnotationReportPage genome_annotation_report(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, page_size=page_size, table_format=table_format, include_tabular_header=include_tabular_header, page_token=page_token)

Get genome annotation reports by genome assembly accession

Get genome annotation reports by genome assembly accession, where each report represents a single feature annotated on the genome.  By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
    accession = 'GCF_000001635.27' # str | One or more genome assembly accessions, limited to 100
    annotation_ids = ['1'] # List[str] | Limit to one or more features annotated on the genome by specifying a number corresponding to a row_id (unstable). (optional)
    symbols = ['Qsox1'] # List[str] | Limit to annotated features matching the given gene symbol (case-sensitive). (optional)
    locations = ['1:1-1000'] # List[str] | Limit to features annotated at a specific location on the genome, by specifying a chromosome name or accession and optional start-stop range. (optional)
    gene_types = ['protein-coding'] # List[str] | Limit to features of a specified gene locus type. (optional)
    search_text = ['kinase'] # List[str] | Limit to features that match the specified gene symbol, gene name or protein name. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    page_size = 20 # int | The maximum number of features to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    table_format = NO_TABLE # V2GenomeAnnotationRequestGenomeAnnotationTableFormat | Optional pre-defined template for processing a tabular data request (optional) (default to NO_TABLE)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)

    try:
        # Get genome annotation reports by genome assembly accession
        api_response = api_instance.genome_annotation_report(accession, annotation_ids=annotation_ids, symbols=symbols, locations=locations, gene_types=gene_types, search_text=search_text, sort_field=sort_field, sort_direction=sort_direction, page_size=page_size, table_format=table_format, include_tabular_header=include_tabular_header, page_token=page_token)
        print("The response of GenomeApi->genome_annotation_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_annotation_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**| One or more genome assembly accessions, limited to 100 | 
 **annotation_ids** | [**List[str]**](str.md)| Limit to one or more features annotated on the genome by specifying a number corresponding to a row_id (unstable). | [optional] 
 **symbols** | [**List[str]**](str.md)| Limit to annotated features matching the given gene symbol (case-sensitive). | [optional] 
 **locations** | [**List[str]**](str.md)| Limit to features annotated at a specific location on the genome, by specifying a chromosome name or accession and optional start-stop range. | [optional] 
 **gene_types** | [**List[str]**](str.md)| Limit to features of a specified gene locus type. | [optional] 
 **search_text** | [**List[str]**](str.md)| Limit to features that match the specified gene symbol, gene name or protein name. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **page_size** | **int**| The maximum number of features to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **table_format** | [**V2GenomeAnnotationRequestGenomeAnnotationTableFormat**](.md)| Optional pre-defined template for processing a tabular data request | [optional] [default to NO_TABLE]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 

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

Get genome annotation reports by genome assembly accession

Get genome annotation reports by genome assembly accession, where each report represents a single feature annotated on the genome.  By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
        # Get genome annotation reports by genome assembly accession
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
> V2reportsAssemblyDataReportPage genome_dataset_report(accessions, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)

Get a genome assembly report by genome assembly accession

Get a genome assembly report by assembly accession. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
    accessions = ['GCF_000001405.40'] # List[str] | One or more genome assembly accessions, limited to 100
    filters_reference_only = False # bool | If true, limit to reference genome assemblies. (optional) (default to False)
    filters_assembly_source = all # V2AssemblyDatasetDescriptorsFilterAssemblySource | Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. (optional) (default to all)
    filters_has_annotation = False # bool | Limit to annotated genome assemblies. (optional) (default to False)
    filters_exclude_paired_reports = False # bool | If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. (optional) (default to False)
    filters_assembly_version = current # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Limit to the most recent (current) version of a genome assembly. (optional) (default to current)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) (optional)
    filters_first_release_date = '2024-01-10' # datetime | Limit to genomes released on or after the specified date (optional)
    filters_last_release_date = '2025-01-10' # datetime | Limit to genomes released on or before the specified date (optional)
    filters_search_text = ['Genome Reference Consortium'] # List[str] | Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. (optional)
    filters_is_metagenome_derived = METAGENOME_DERIVED_UNSET # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter | Exclude or limit to metagenome-assembled genomes (MAGs). (optional) (default to METAGENOME_DERIVED_UNSET)
    filters_is_type_material = False # bool | If true, limit to genomes derived from type material. (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude genomes that were sequenced as part of large multi-isolate projects. (optional) (default to False)
    filters_type_material_category = NONE # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory | Limit to genomes derived from specific type material categories. (optional) (default to NONE)
    table_fields = ['accession'] # List[str] |  (optional)
    returned_content = COMPLETE # V2AssemblyDatasetReportsRequestContentType | Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. (optional) (default to COMPLETE)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)

    try:
        # Get a genome assembly report by genome assembly accession
        api_response = api_instance.genome_dataset_report(accessions, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_dataset_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_dataset_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more genome assembly accessions, limited to 100 | 
 **filters_reference_only** | **bool**| If true, limit to reference genome assemblies. | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. | [optional] [default to all]
 **filters_has_annotation** | **bool**| Limit to annotated genome assemblies. | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Limit to the most recent (current) version of a genome assembly. | [optional] [default to current]
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) | [optional] 
 **filters_first_release_date** | **datetime**| Limit to genomes released on or after the specified date | [optional] 
 **filters_last_release_date** | **datetime**| Limit to genomes released on or before the specified date | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)| Exclude or limit to metagenome-assembled genomes (MAGs). | [optional] [default to METAGENOME_DERIVED_UNSET]
 **filters_is_type_material** | **bool**| If true, limit to genomes derived from type material. | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude genomes that were sequenced as part of large multi-isolate projects. | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)| Limit to genomes derived from specific type material categories. | [optional] [default to NONE]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. | [optional] [default to COMPLETE]
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]

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

Get a genome assembly report

Get a genome assembly report. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
        # Get a genome assembly report
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

Get genome assembly reports by assembly name

Get genome assembly reports by assembly name (exact matches only).  By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
    assembly_names = ['HanXRQr2.0-SUNRISE'] # List[str] | One or more assembly names (exact match only)
    filters_reference_only = False # bool | If true, limit to reference genome assemblies. (optional) (default to False)
    filters_assembly_source = all # V2AssemblyDatasetDescriptorsFilterAssemblySource | Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. (optional) (default to all)
    filters_has_annotation = False # bool | Limit to annotated genome assemblies. (optional) (default to False)
    filters_exclude_paired_reports = False # bool | If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. (optional) (default to False)
    filters_assembly_version = current # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Limit to the most recent (current) version of a genome assembly. (optional) (default to current)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) (optional)
    filters_first_release_date = '2024-01-10' # datetime | Limit to genomes released on or after the specified date (optional)
    filters_last_release_date = '2025-01-10' # datetime | Limit to genomes released on or before the specified date (optional)
    filters_search_text = ['Genome Reference Consortium'] # List[str] | Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. (optional)
    filters_is_metagenome_derived = METAGENOME_DERIVED_UNSET # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter | Exclude or limit to metagenome-assembled genomes (MAGs). (optional) (default to METAGENOME_DERIVED_UNSET)
    filters_is_type_material = False # bool | If true, limit to genomes derived from type material. (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude genomes that were sequenced as part of large multi-isolate projects. (optional) (default to False)
    filters_type_material_category = NONE # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory | Limit to genomes derived from specific type material categories. (optional) (default to NONE)
    tax_exact_match = False # bool | If true, only return assemblies matching the specified taxon, but not child taxa. For example, if querying by \"Canis lupus\", return Canis lupus but not Canis lupus familiaris genomes. (optional) (default to False)
    table_fields = ['accession'] # List[str] |  (optional)
    returned_content = COMPLETE # V2AssemblyDatasetReportsRequestContentType | Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. (optional) (default to COMPLETE)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)

    try:
        # Get genome assembly reports by assembly name
        api_response = api_instance.genome_dataset_reports_by_assembly_name(assembly_names, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_dataset_reports_by_assembly_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_dataset_reports_by_assembly_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembly_names** | [**List[str]**](str.md)| One or more assembly names (exact match only) | 
 **filters_reference_only** | **bool**| If true, limit to reference genome assemblies. | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. | [optional] [default to all]
 **filters_has_annotation** | **bool**| Limit to annotated genome assemblies. | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Limit to the most recent (current) version of a genome assembly. | [optional] [default to current]
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) | [optional] 
 **filters_first_release_date** | **datetime**| Limit to genomes released on or after the specified date | [optional] 
 **filters_last_release_date** | **datetime**| Limit to genomes released on or before the specified date | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)| Exclude or limit to metagenome-assembled genomes (MAGs). | [optional] [default to METAGENOME_DERIVED_UNSET]
 **filters_is_type_material** | **bool**| If true, limit to genomes derived from type material. | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude genomes that were sequenced as part of large multi-isolate projects. | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)| Limit to genomes derived from specific type material categories. | [optional] [default to NONE]
 **tax_exact_match** | **bool**| If true, only return assemblies matching the specified taxon, but not child taxa. For example, if querying by \&quot;Canis lupus\&quot;, return Canis lupus but not Canis lupus familiaris genomes. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. | [optional] [default to COMPLETE]
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]

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

Get genome assembly reports by BioProject accession

Get genome assembly reports by BioProject accession.  By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
    bioprojects = ['PRJNA489243'] # List[str] | 
    filters_reference_only = False # bool | If true, limit to reference genome assemblies. (optional) (default to False)
    filters_assembly_source = all # V2AssemblyDatasetDescriptorsFilterAssemblySource | Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. (optional) (default to all)
    filters_has_annotation = False # bool | Limit to annotated genome assemblies. (optional) (default to False)
    filters_exclude_paired_reports = False # bool | If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. (optional) (default to False)
    filters_assembly_version = current # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Limit to the most recent (current) version of a genome assembly. (optional) (default to current)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) (optional)
    filters_first_release_date = '2024-01-10' # datetime | Limit to genomes released on or after the specified date (optional)
    filters_last_release_date = '2025-01-10' # datetime | Limit to genomes released on or before the specified date (optional)
    filters_search_text = ['Genome Reference Consortium'] # List[str] | Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. (optional)
    filters_is_metagenome_derived = METAGENOME_DERIVED_UNSET # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter | Exclude or limit to metagenome-assembled genomes (MAGs). (optional) (default to METAGENOME_DERIVED_UNSET)
    filters_is_type_material = False # bool | If true, limit to genomes derived from type material. (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude genomes that were sequenced as part of large multi-isolate projects. (optional) (default to False)
    filters_type_material_category = NONE # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory | Limit to genomes derived from specific type material categories. (optional) (default to NONE)
    tax_exact_match = False # bool | If true, only return assemblies matching the specified taxon, but not child taxa. For example, if querying by \"Canis lupus\", return Canis lupus but not Canis lupus familiaris genomes. (optional) (default to False)
    table_fields = ['accession'] # List[str] |  (optional)
    returned_content = COMPLETE # V2AssemblyDatasetReportsRequestContentType | Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. (optional) (default to COMPLETE)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)

    try:
        # Get genome assembly reports by BioProject accession
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
 **filters_reference_only** | **bool**| If true, limit to reference genome assemblies. | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. | [optional] [default to all]
 **filters_has_annotation** | **bool**| Limit to annotated genome assemblies. | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Limit to the most recent (current) version of a genome assembly. | [optional] [default to current]
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) | [optional] 
 **filters_first_release_date** | **datetime**| Limit to genomes released on or after the specified date | [optional] 
 **filters_last_release_date** | **datetime**| Limit to genomes released on or before the specified date | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)| Exclude or limit to metagenome-assembled genomes (MAGs). | [optional] [default to METAGENOME_DERIVED_UNSET]
 **filters_is_type_material** | **bool**| If true, limit to genomes derived from type material. | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude genomes that were sequenced as part of large multi-isolate projects. | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)| Limit to genomes derived from specific type material categories. | [optional] [default to NONE]
 **tax_exact_match** | **bool**| If true, only return assemblies matching the specified taxon, but not child taxa. For example, if querying by \&quot;Canis lupus\&quot;, return Canis lupus but not Canis lupus familiaris genomes. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. | [optional] [default to COMPLETE]
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]

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

Get genome assembly reports by BioSample accession

Get genome assembly reports by BioSample accession.  By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
    biosample_ids = ['SAMN15960293'] # List[str] | 
    filters_reference_only = False # bool | If true, limit to reference genome assemblies. (optional) (default to False)
    filters_assembly_source = all # V2AssemblyDatasetDescriptorsFilterAssemblySource | Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. (optional) (default to all)
    filters_has_annotation = False # bool | Limit to annotated genome assemblies. (optional) (default to False)
    filters_exclude_paired_reports = False # bool | If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. (optional) (default to False)
    filters_assembly_version = current # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Limit to the most recent (current) version of a genome assembly. (optional) (default to current)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) (optional)
    filters_first_release_date = '2024-01-10' # datetime | Limit to genomes released on or after the specified date (optional)
    filters_last_release_date = '2025-01-10' # datetime | Limit to genomes released on or before the specified date (optional)
    filters_search_text = ['Genome Reference Consortium'] # List[str] | Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. (optional)
    filters_is_metagenome_derived = METAGENOME_DERIVED_UNSET # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter | Exclude or limit to metagenome-assembled genomes (MAGs). (optional) (default to METAGENOME_DERIVED_UNSET)
    filters_is_type_material = False # bool | If true, limit to genomes derived from type material. (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude genomes that were sequenced as part of large multi-isolate projects. (optional) (default to False)
    filters_type_material_category = NONE # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory | Limit to genomes derived from specific type material categories. (optional) (default to NONE)
    tax_exact_match = False # bool | If true, only return assemblies matching the specified taxon, but not child taxa. For example, if querying by \"Canis lupus\", return Canis lupus but not Canis lupus familiaris genomes. (optional) (default to False)
    table_fields = ['accession'] # List[str] |  (optional)
    returned_content = COMPLETE # V2AssemblyDatasetReportsRequestContentType | Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. (optional) (default to COMPLETE)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)

    try:
        # Get genome assembly reports by BioSample accession
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
 **filters_reference_only** | **bool**| If true, limit to reference genome assemblies. | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. | [optional] [default to all]
 **filters_has_annotation** | **bool**| Limit to annotated genome assemblies. | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Limit to the most recent (current) version of a genome assembly. | [optional] [default to current]
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) | [optional] 
 **filters_first_release_date** | **datetime**| Limit to genomes released on or after the specified date | [optional] 
 **filters_last_release_date** | **datetime**| Limit to genomes released on or before the specified date | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)| Exclude or limit to metagenome-assembled genomes (MAGs). | [optional] [default to METAGENOME_DERIVED_UNSET]
 **filters_is_type_material** | **bool**| If true, limit to genomes derived from type material. | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude genomes that were sequenced as part of large multi-isolate projects. | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)| Limit to genomes derived from specific type material categories. | [optional] [default to NONE]
 **tax_exact_match** | **bool**| If true, only return assemblies matching the specified taxon, but not child taxa. For example, if querying by \&quot;Canis lupus\&quot;, return Canis lupus but not Canis lupus familiaris genomes. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. | [optional] [default to COMPLETE]
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]

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

Get a genome assembly report by taxon

Get a genome assembly report by taxon.  By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
    taxons = ['9606'] # List[str] | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank
    filters_reference_only = False # bool | If true, limit to reference genome assemblies. (optional) (default to False)
    filters_assembly_source = all # V2AssemblyDatasetDescriptorsFilterAssemblySource | Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. (optional) (default to all)
    filters_has_annotation = False # bool | Limit to annotated genome assemblies. (optional) (default to False)
    filters_exclude_paired_reports = False # bool | If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. (optional) (default to False)
    filters_assembly_version = current # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Limit to the most recent (current) version of a genome assembly. (optional) (default to current)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) (optional)
    filters_first_release_date = '2024-01-10' # datetime | Limit to genomes released on or after the specified date (optional)
    filters_last_release_date = '2025-01-10' # datetime | Limit to genomes released on or before the specified date (optional)
    filters_search_text = ['Genome Reference Consortium'] # List[str] | Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. (optional)
    filters_is_metagenome_derived = METAGENOME_DERIVED_UNSET # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter | Exclude or limit to metagenome-assembled genomes (MAGs). (optional) (default to METAGENOME_DERIVED_UNSET)
    filters_is_type_material = False # bool | If true, limit to genomes derived from type material. (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude genomes that were sequenced as part of large multi-isolate projects. (optional) (default to False)
    filters_type_material_category = NONE # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory | Limit to genomes derived from specific type material categories. (optional) (default to NONE)
    tax_exact_match = False # bool | If true, only return assemblies matching the specified taxon, but not child taxa. For example, if querying by \"Canis lupus\", return Canis lupus but not Canis lupus familiaris genomes. (optional) (default to False)
    table_fields = ['accession'] # List[str] |  (optional)
    returned_content = COMPLETE # V2AssemblyDatasetReportsRequestContentType | Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. (optional) (default to COMPLETE)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)

    try:
        # Get a genome assembly report by taxon
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
 **filters_reference_only** | **bool**| If true, limit to reference genome assemblies. | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. | [optional] [default to all]
 **filters_has_annotation** | **bool**| Limit to annotated genome assemblies. | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Limit to the most recent (current) version of a genome assembly. | [optional] [default to current]
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) | [optional] 
 **filters_first_release_date** | **datetime**| Limit to genomes released on or after the specified date | [optional] 
 **filters_last_release_date** | **datetime**| Limit to genomes released on or before the specified date | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)| Exclude or limit to metagenome-assembled genomes (MAGs). | [optional] [default to METAGENOME_DERIVED_UNSET]
 **filters_is_type_material** | **bool**| If true, limit to genomes derived from type material. | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude genomes that were sequenced as part of large multi-isolate projects. | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)| Limit to genomes derived from specific type material categories. | [optional] [default to NONE]
 **tax_exact_match** | **bool**| If true, only return assemblies matching the specified taxon, but not child taxa. For example, if querying by \&quot;Canis lupus\&quot;, return Canis lupus but not Canis lupus familiaris genomes. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. | [optional] [default to COMPLETE]
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]

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

Get a genome assembly data report by WGS accession

Get a genome assembly data report by WGS (whole genome shotgun) accession.  By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
    wgs_accessions = ['JAXUCZ01'] # List[str] | One or more WGS accessions associated with a genome assembly
    filters_reference_only = False # bool | If true, limit to reference genome assemblies. (optional) (default to False)
    filters_assembly_source = all # V2AssemblyDatasetDescriptorsFilterAssemblySource | Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. (optional) (default to all)
    filters_has_annotation = False # bool | Limit to annotated genome assemblies. (optional) (default to False)
    filters_exclude_paired_reports = False # bool | If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. (optional) (default to False)
    filters_exclude_atypical = False # bool | If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. (optional) (default to False)
    filters_assembly_version = current # V2AssemblyDatasetDescriptorsFilterAssemblyVersion | Limit to the most recent (current) version of a genome assembly. (optional) (default to current)
    filters_assembly_level = [ncbi.datasets.openapi.V2reportsAssemblyLevel()] # List[V2reportsAssemblyLevel] | Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) (optional)
    filters_first_release_date = '2024-01-10' # datetime | Limit to genomes released on or after the specified date (optional)
    filters_last_release_date = '2025-01-10' # datetime | Limit to genomes released on or before the specified date (optional)
    filters_search_text = ['Genome Reference Consortium'] # List[str] | Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. (optional)
    filters_is_metagenome_derived = METAGENOME_DERIVED_UNSET # V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter | Exclude or limit to metagenome-assembled genomes (MAGs). (optional) (default to METAGENOME_DERIVED_UNSET)
    filters_is_type_material = False # bool | If true, limit to genomes derived from type material. (optional) (default to False)
    filters_is_ictv_exemplar = False # bool | If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). (optional) (default to False)
    filters_exclude_multi_isolate = False # bool | If true, exclude genomes that were sequenced as part of large multi-isolate projects. (optional) (default to False)
    filters_type_material_category = NONE # V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory | Limit to genomes derived from specific type material categories. (optional) (default to NONE)
    tax_exact_match = False # bool | If true, only return assemblies matching the specified taxon, but not child taxa. For example, if querying by \"Canis lupus\", return Canis lupus but not Canis lupus familiaris genomes. (optional) (default to False)
    table_fields = ['accession'] # List[str] |  (optional)
    returned_content = COMPLETE # V2AssemblyDatasetReportsRequestContentType | Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. (optional) (default to COMPLETE)
    page_size = 20 # int | The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)

    try:
        # Get a genome assembly data report by WGS accession
        api_response = api_instance.genome_dataset_reports_by_wgs(wgs_accessions, filters_reference_only=filters_reference_only, filters_assembly_source=filters_assembly_source, filters_has_annotation=filters_has_annotation, filters_exclude_paired_reports=filters_exclude_paired_reports, filters_exclude_atypical=filters_exclude_atypical, filters_assembly_version=filters_assembly_version, filters_assembly_level=filters_assembly_level, filters_first_release_date=filters_first_release_date, filters_last_release_date=filters_last_release_date, filters_search_text=filters_search_text, filters_is_metagenome_derived=filters_is_metagenome_derived, filters_is_type_material=filters_is_type_material, filters_is_ictv_exemplar=filters_is_ictv_exemplar, filters_exclude_multi_isolate=filters_exclude_multi_isolate, filters_type_material_category=filters_type_material_category, tax_exact_match=tax_exact_match, table_fields=table_fields, returned_content=returned_content, page_size=page_size, page_token=page_token, sort_field=sort_field, sort_direction=sort_direction, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_dataset_reports_by_wgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_dataset_reports_by_wgs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wgs_accessions** | [**List[str]**](str.md)| One or more WGS accessions associated with a genome assembly | 
 **filters_reference_only** | **bool**| If true, limit to reference genome assemblies. | [optional] [default to False]
 **filters_assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](.md)| Limit to either RefSeq (GCF_) or GenBank (GCA_) genome assemblies. | [optional] [default to all]
 **filters_has_annotation** | **bool**| Limit to annotated genome assemblies. | [optional] [default to False]
 **filters_exclude_paired_reports** | **bool**| If true, for GenBank (GCA_)/RefSeq (GCF_) pairs, returns the RefSeq copy. When no RefSeq copy exists, the GenBank assembly is returned. | [optional] [default to False]
 **filters_exclude_atypical** | **bool**| If true, exclude [atypical genome assemblies](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/genome_notes/#atypical-assemblies), i.e., genomes that have assembly issues or are otherwise atypical. | [optional] [default to False]
 **filters_assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](.md)| Limit to the most recent (current) version of a genome assembly. | [optional] [default to current]
 **filters_assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md)| Limit to genomes at the specified [assembly level](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/glossary/#assembly-level) | [optional] 
 **filters_first_release_date** | **datetime**| Limit to genomes released on or after the specified date | [optional] 
 **filters_last_release_date** | **datetime**| Limit to genomes released on or before the specified date | [optional] 
 **filters_search_text** | [**List[str]**](str.md)| Limit to genomes that match the specified submitter name, assembly name, infraspecific name (or modifier), or organism name. | [optional] 
 **filters_is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](.md)| Exclude or limit to metagenome-assembled genomes (MAGs). | [optional] [default to METAGENOME_DERIVED_UNSET]
 **filters_is_type_material** | **bool**| If true, limit to genomes derived from type material. | [optional] [default to False]
 **filters_is_ictv_exemplar** | **bool**| If true, limit to genomes derived from an ICTV exemplar (only applies to virus genomes). | [optional] [default to False]
 **filters_exclude_multi_isolate** | **bool**| If true, exclude genomes that were sequenced as part of large multi-isolate projects. | [optional] [default to False]
 **filters_type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](.md)| Limit to genomes derived from specific type material categories. | [optional] [default to NONE]
 **tax_exact_match** | **bool**| If true, only return assemblies matching the specified taxon, but not child taxa. For example, if querying by \&quot;Canis lupus\&quot;, return Canis lupus but not Canis lupus familiaris genomes. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](.md)| Return complete genome assembly reports, or abbreviated reports with assembly accessions with or without paired assembly information. | [optional] [default to COMPLETE]
 **page_size** | **int**| The maximum number of genome assembly reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]

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

Get a download summary (preview) of a genome data package by genome assembly accession

Get a download summary (preview) of a genome data package, including counts and file sizes, in JSON format.

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
    accessions = ['GCF_000001405.40'] # List[str] | One or more genome assembly accessions, limited to 100
    chromosomes = ['[\"1\",\"MT\"]'] # List[str] | Only return genomic fasta sequence for the specified chromosomes. (optional)
    include_annotation_type = [ncbi.datasets.openapi.V2AnnotationForAssemblyType()] # List[V2AnnotationForAssemblyType] | Specify which sequence, annotation, and report files to include in the data package. The assembly data report is always included, and its inclusion is not affected by this parameter. (optional)

    try:
        # Get a download summary (preview) of a genome data package by genome assembly accession
        api_response = api_instance.genome_download_summary(accessions, chromosomes=chromosomes, include_annotation_type=include_annotation_type)
        print("The response of GenomeApi->genome_download_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_download_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more genome assembly accessions, limited to 100 | 
 **chromosomes** | [**List[str]**](str.md)| Only return genomic fasta sequence for the specified chromosomes. | [optional] 
 **include_annotation_type** | [**List[V2AnnotationForAssemblyType]**](V2AnnotationForAssemblyType.md)| Specify which sequence, annotation, and report files to include in the data package. The assembly data report is always included, and its inclusion is not affected by this parameter. | [optional] 

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

Get a download summary (preview) of a genome data package by genome assembly accession

Get a downlaod summary (preview) of a genome data package, including counts and file sizes, in JSON format.

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
    v2_assembly_dataset_request = {"accessions":["GCF_031307605.1"],"include_annotation_type":["GENOME_FASTA","GENOME_GFF","SEQUENCE_REPORT"]} # V2AssemblyDatasetRequest | 

    try:
        # Get a download summary (preview) of a genome data package by genome assembly accession
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

Get assembly links by genome assembly accession

Get links to assembly resources by genome assembly accession in JSON format.

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
    accessions = ['GCF_000001405.40'] # List[str] | One or more genome assembly accessions, limited to 100

    try:
        # Get assembly links by genome assembly accession
        api_response = api_instance.genome_links_by_accession(accessions)
        print("The response of GenomeApi->genome_links_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_links_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more genome assembly accessions, limited to 100 | 

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

Get assembly links by genome assembly accession

Get links to assembly resources by genome assembly accession in JSON format.

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
        # Get assembly links by genome assembly accession
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

Get a genome sequence report by genome assembly accession

Get a genome sequence report by genome assembly accession. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
    accession = 'GCF_000001635.27' # str | One or more genome assembly accessions, limited to 100
    chromosomes = ['[\"1\",\"MT\"]'] # List[str] | Limit to sequences with the specified chromosome names (optional)
    role_filters = ['assembled-molecule'] # List[str] | Limit to sequences with the specified \"role\", where possible roles are `assembled-molecule`, `unlocalized-scaffold`, or `unplaced-scaffold` (optional)
    table_fields = ['[\"accession\",\"chr-name\"]'] # List[str] |  (optional)
    count_assembly_unplaced = False # bool | Include the count of unplaced scaffold sequences (optional) (default to False)
    page_size = 56 # int | The maximum number of genome assemblies to return. Maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader |  (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)

    try:
        # Get a genome sequence report by genome assembly accession
        api_response = api_instance.genome_sequence_report(accession, chromosomes=chromosomes, role_filters=role_filters, table_fields=table_fields, count_assembly_unplaced=count_assembly_unplaced, page_size=page_size, page_token=page_token, include_tabular_header=include_tabular_header)
        print("The response of GenomeApi->genome_sequence_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenomeApi->genome_sequence_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession** | **str**| One or more genome assembly accessions, limited to 100 | 
 **chromosomes** | [**List[str]**](str.md)| Limit to sequences with the specified chromosome names | [optional] 
 **role_filters** | [**List[str]**](str.md)| Limit to sequences with the specified \&quot;role\&quot;, where possible roles are &#x60;assembled-molecule&#x60;, &#x60;unlocalized-scaffold&#x60;, or &#x60;unplaced-scaffold&#x60; | [optional] 
 **table_fields** | [**List[str]**](str.md)|  | [optional] 
 **count_assembly_unplaced** | **bool**| Include the count of unplaced scaffold sequences | [optional] [default to False]
 **page_size** | **int**| The maximum number of genome assemblies to return. Maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] 
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)|  | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]

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

Get a genome sequence report by genome assembly accession

Get a genome sequence report by genome assembly accession. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

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
        # Get a genome sequence report by genome assembly accession
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

