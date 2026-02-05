# ncbi.datasets.openapi.OrganelleApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_organelle_package**](OrganelleApi.md#download_organelle_package) | **GET** /organelle/accession/{accessions}/download | Get a organelle data package by accesions
[**download_organelle_package_by_post**](OrganelleApi.md#download_organelle_package_by_post) | **POST** /organelle/download | Get a organelle data package by post
[**organelle_datareport_by_accession**](OrganelleApi.md#organelle_datareport_by_accession) | **GET** /organelle/accessions/{accessions}/dataset_report | Get Organelle dataset report by accession
[**organelle_datareport_by_post**](OrganelleApi.md#organelle_datareport_by_post) | **POST** /organelle/dataset_report | Get Organelle dataset report by http post
[**organelle_datareport_by_taxon**](OrganelleApi.md#organelle_datareport_by_taxon) | **GET** /organelle/taxon/{taxons}/dataset_report | Get Organelle dataset report by taxons


# **download_organelle_package**
> bytearray download_organelle_package(accessions, exclude_sequence=exclude_sequence, include_annotation_type=include_annotation_type, filename=filename)

Get a organelle data package by accesions

Download a organelle data report and annotation data package.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_annotation_for_organelle_type import V2AnnotationForOrganelleType
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
    api_instance = ncbi.datasets.openapi.OrganelleApi(api_client)
    accessions = ['NC_001643.1'] # List[str] | NCBI organelle assembly accessions
    exclude_sequence = True # bool | Set to true to omit the genomic sequence. (optional)
    include_annotation_type = [ncbi.datasets.openapi.V2AnnotationForOrganelleType()] # List[V2AnnotationForOrganelleType] | Select additional types of annotation to include in the data package.  If unset, no annotation is provided. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a organelle data package by accesions
        api_response = api_instance.download_organelle_package(accessions, exclude_sequence=exclude_sequence, include_annotation_type=include_annotation_type, filename=filename)
        print("The response of OrganelleApi->download_organelle_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganelleApi->download_organelle_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| NCBI organelle assembly accessions | 
 **exclude_sequence** | **bool**| Set to true to omit the genomic sequence. | [optional] 
 **include_annotation_type** | [**List[V2AnnotationForOrganelleType]**](V2AnnotationForOrganelleType.md)| Select additional types of annotation to include in the data package.  If unset, no annotation is provided. | [optional] 
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

# **download_organelle_package_by_post**
> bytearray download_organelle_package_by_post(v2_organelle_download_request, filename=filename)

Get a organelle data package by post

Download a organelle report and annotation data package by post.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_organelle_download_request import V2OrganelleDownloadRequest
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
    api_instance = ncbi.datasets.openapi.OrganelleApi(api_client)
    v2_organelle_download_request = {"accessions":["NC_001643.1"]} # V2OrganelleDownloadRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a organelle data package by post
        api_response = api_instance.download_organelle_package_by_post(v2_organelle_download_request, filename=filename)
        print("The response of OrganelleApi->download_organelle_package_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganelleApi->download_organelle_package_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_organelle_download_request** | [**V2OrganelleDownloadRequest**](V2OrganelleDownloadRequest.md)|  | 
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

# **organelle_datareport_by_accession**
> V2reportsOrganelleDataReports organelle_datareport_by_accession(accessions, taxons=taxons, organelle_types=organelle_types, first_release_date=first_release_date, last_release_date=last_release_date, tax_exact_match=tax_exact_match, sort_field=sort_field, sort_direction=sort_direction, returned_content=returned_content, table_format=table_format, include_tabular_header=include_tabular_header)

Get Organelle dataset report by accession

Get Organelle dataset report by accession.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_organelle_metadata_request_content_type import V2OrganelleMetadataRequestContentType
from ncbi.datasets.openapi.models.v2_organelle_metadata_request_organelle_table_format import V2OrganelleMetadataRequestOrganelleTableFormat
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_organelle_data_reports import V2reportsOrganelleDataReports
from ncbi.datasets.openapi.models.v2reports_organelle_type import V2reportsOrganelleType
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
    api_instance = ncbi.datasets.openapi.OrganelleApi(api_client)
    accessions = ['NC_001643.1'] # List[str] | NCBI assembly accession
    taxons = ['9443'] # List[str] | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank (optional)
    organelle_types = [ncbi.datasets.openapi.V2reportsOrganelleType()] # List[V2reportsOrganelleType] |  (optional)
    first_release_date = '2015-01-10' # datetime |  (optional)
    last_release_date = '2021-01-10' # datetime |  (optional)
    tax_exact_match = False # bool | If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. (optional) (default to False)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    returned_content = COMPLETE # V2OrganelleMetadataRequestContentType | Return either assembly accessions, or entire assembly-metadata records (optional) (default to COMPLETE)
    table_format = ORGANELLE_TABLE_FORMAT_NO_TABLE # V2OrganelleMetadataRequestOrganelleTableFormat | Optional pre-defined template for processing a tabular data request (optional) (default to ORGANELLE_TABLE_FORMAT_NO_TABLE)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)

    try:
        # Get Organelle dataset report by accession
        api_response = api_instance.organelle_datareport_by_accession(accessions, taxons=taxons, organelle_types=organelle_types, first_release_date=first_release_date, last_release_date=last_release_date, tax_exact_match=tax_exact_match, sort_field=sort_field, sort_direction=sort_direction, returned_content=returned_content, table_format=table_format, include_tabular_header=include_tabular_header)
        print("The response of OrganelleApi->organelle_datareport_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganelleApi->organelle_datareport_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| NCBI assembly accession | 
 **taxons** | [**List[str]**](str.md)| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank | [optional] 
 **organelle_types** | [**List[V2reportsOrganelleType]**](V2reportsOrganelleType.md)|  | [optional] 
 **first_release_date** | **datetime**|  | [optional] 
 **last_release_date** | **datetime**|  | [optional] 
 **tax_exact_match** | **bool**| If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. | [optional] [default to False]
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **returned_content** | [**V2OrganelleMetadataRequestContentType**](.md)| Return either assembly accessions, or entire assembly-metadata records | [optional] [default to COMPLETE]
 **table_format** | [**V2OrganelleMetadataRequestOrganelleTableFormat**](.md)| Optional pre-defined template for processing a tabular data request | [optional] [default to ORGANELLE_TABLE_FORMAT_NO_TABLE]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]

### Return type

[**V2reportsOrganelleDataReports**](V2reportsOrganelleDataReports.md)

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

# **organelle_datareport_by_post**
> V2reportsOrganelleDataReports organelle_datareport_by_post(v2_organelle_metadata_request)

Get Organelle dataset report by http post

Get Organelle dataset report by http post.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_organelle_metadata_request import V2OrganelleMetadataRequest
from ncbi.datasets.openapi.models.v2reports_organelle_data_reports import V2reportsOrganelleDataReports
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
    api_instance = ncbi.datasets.openapi.OrganelleApi(api_client)
    v2_organelle_metadata_request = {"taxons":["9443"]} # V2OrganelleMetadataRequest | 

    try:
        # Get Organelle dataset report by http post
        api_response = api_instance.organelle_datareport_by_post(v2_organelle_metadata_request)
        print("The response of OrganelleApi->organelle_datareport_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganelleApi->organelle_datareport_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_organelle_metadata_request** | [**V2OrganelleMetadataRequest**](V2OrganelleMetadataRequest.md)|  | 

### Return type

[**V2reportsOrganelleDataReports**](V2reportsOrganelleDataReports.md)

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

# **organelle_datareport_by_taxon**
> V2reportsOrganelleDataReports organelle_datareport_by_taxon(taxons, organelle_types=organelle_types, first_release_date=first_release_date, last_release_date=last_release_date, tax_exact_match=tax_exact_match, sort_field=sort_field, sort_direction=sort_direction, returned_content=returned_content, page_size=page_size, page_token=page_token, table_format=table_format, include_tabular_header=include_tabular_header)

Get Organelle dataset report by taxons

Get Organelle dataset report by taxons.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_organelle_metadata_request_content_type import V2OrganelleMetadataRequestContentType
from ncbi.datasets.openapi.models.v2_organelle_metadata_request_organelle_table_format import V2OrganelleMetadataRequestOrganelleTableFormat
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_organelle_data_reports import V2reportsOrganelleDataReports
from ncbi.datasets.openapi.models.v2reports_organelle_type import V2reportsOrganelleType
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
    api_instance = ncbi.datasets.openapi.OrganelleApi(api_client)
    taxons = ['9443'] # List[str] | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank
    organelle_types = [ncbi.datasets.openapi.V2reportsOrganelleType()] # List[V2reportsOrganelleType] |  (optional)
    first_release_date = '2015-01-10' # datetime |  (optional)
    last_release_date = '2021-01-10' # datetime |  (optional)
    tax_exact_match = False # bool | If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. (optional) (default to False)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)
    returned_content = COMPLETE # V2OrganelleMetadataRequestContentType | Return either assembly accessions, or entire assembly-metadata records (optional) (default to COMPLETE)
    page_size = 56 # int | The maximum number of organelle assemblies to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional)
    page_token = 'page_token_example' # str | A page token is returned from an `OrganelleMetadata` call with more than `page_size` results. Use this token, along with the previous `OrganelleMetadata` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    table_format = ORGANELLE_TABLE_FORMAT_NO_TABLE # V2OrganelleMetadataRequestOrganelleTableFormat | Optional pre-defined template for processing a tabular data request (optional) (default to ORGANELLE_TABLE_FORMAT_NO_TABLE)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)

    try:
        # Get Organelle dataset report by taxons
        api_response = api_instance.organelle_datareport_by_taxon(taxons, organelle_types=organelle_types, first_release_date=first_release_date, last_release_date=last_release_date, tax_exact_match=tax_exact_match, sort_field=sort_field, sort_direction=sort_direction, returned_content=returned_content, page_size=page_size, page_token=page_token, table_format=table_format, include_tabular_header=include_tabular_header)
        print("The response of OrganelleApi->organelle_datareport_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganelleApi->organelle_datareport_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxons** | [**List[str]**](str.md)| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank | 
 **organelle_types** | [**List[V2reportsOrganelleType]**](V2reportsOrganelleType.md)|  | [optional] 
 **first_release_date** | **datetime**|  | [optional] 
 **last_release_date** | **datetime**|  | [optional] 
 **tax_exact_match** | **bool**| If true, only return assemblies with the given NCBI Taxonomy ID, or name. Otherwise, assemblies from taxonomy subtree are included, too. | [optional] [default to False]
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]
 **returned_content** | [**V2OrganelleMetadataRequestContentType**](.md)| Return either assembly accessions, or entire assembly-metadata records | [optional] [default to COMPLETE]
 **page_size** | **int**| The maximum number of organelle assemblies to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] 
 **page_token** | **str**| A page token is returned from an &#x60;OrganelleMetadata&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;OrganelleMetadata&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **table_format** | [**V2OrganelleMetadataRequestOrganelleTableFormat**](.md)| Optional pre-defined template for processing a tabular data request | [optional] [default to ORGANELLE_TABLE_FORMAT_NO_TABLE]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]

### Return type

[**V2reportsOrganelleDataReports**](V2reportsOrganelleDataReports.md)

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

