# ncbi.datasets.openapi.TaxonomyApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_taxonomy_package**](TaxonomyApi.md#download_taxonomy_package) | **GET** /taxonomy/taxon/{tax_ids}/download | Get a taxonomy data package by Taxonomy ID
[**download_taxonomy_package_by_post**](TaxonomyApi.md#download_taxonomy_package_by_post) | **POST** /taxonomy/download | Get a taxonomy data package by Taxonomy ID
[**tax_name_query**](TaxonomyApi.md#tax_name_query) | **GET** /taxonomy/taxon_suggest/{taxon_query} | Get a list of taxonomy names and IDs by partial taxonomic name
[**tax_name_query_by_post**](TaxonomyApi.md#tax_name_query_by_post) | **POST** /taxonomy/taxon_suggest | Get a list of taxonomy names and IDs by partial taxonomic name
[**taxonomy_data_report**](TaxonomyApi.md#taxonomy_data_report) | **GET** /taxonomy/taxon/{taxons}/dataset_report | Get a taxonomy data report by taxon
[**taxonomy_data_report_post**](TaxonomyApi.md#taxonomy_data_report_post) | **POST** /taxonomy/dataset_report | Get a taxonomy data report by taxon
[**taxonomy_filtered_subtree**](TaxonomyApi.md#taxonomy_filtered_subtree) | **GET** /taxonomy/taxon/{taxons}/filtered_subtree | Get a filtered taxonomic subtree by taxon
[**taxonomy_filtered_subtree_post**](TaxonomyApi.md#taxonomy_filtered_subtree_post) | **POST** /taxonomy/filtered_subtree | Get a filtered taxonomic subtree by taxon
[**taxonomy_image**](TaxonomyApi.md#taxonomy_image) | **GET** /taxonomy/taxon/{taxon}/image | Get a taxonomy image by taxon
[**taxonomy_image_metadata**](TaxonomyApi.md#taxonomy_image_metadata) | **GET** /taxonomy/taxon/{taxon}/image/metadata | Get taxonomy image metadata by Taxonomy ID
[**taxonomy_image_metadata_post**](TaxonomyApi.md#taxonomy_image_metadata_post) | **POST** /taxonomy/image/metadata | Get taxonomy image metadata by Taxonomy ID
[**taxonomy_image_post**](TaxonomyApi.md#taxonomy_image_post) | **POST** /taxonomy/image | Get a taxonomy image by taxon
[**taxonomy_links**](TaxonomyApi.md#taxonomy_links) | **GET** /taxonomy/taxon/{taxon}/links | Get external links by Taxonomy ID
[**taxonomy_links_by_post**](TaxonomyApi.md#taxonomy_links_by_post) | **POST** /taxonomy/links | Get external links by Taxonomy ID
[**taxonomy_metadata**](TaxonomyApi.md#taxonomy_metadata) | **GET** /taxonomy/taxon/{taxons} | Use taxonomic identifiers to get taxonomic metadata (deprecated)
[**taxonomy_metadata_post**](TaxonomyApi.md#taxonomy_metadata_post) | **POST** /taxonomy | Get taxonomy metadata by taxon (deprecated)
[**taxonomy_names**](TaxonomyApi.md#taxonomy_names) | **GET** /taxonomy/taxon/{taxons}/name_report | Get a taxonomy names report by taxon
[**taxonomy_names_post**](TaxonomyApi.md#taxonomy_names_post) | **POST** /taxonomy/name_report | Get a taxonomy names report by taxon
[**taxonomy_related_ids**](TaxonomyApi.md#taxonomy_related_ids) | **GET** /taxonomy/taxon/{tax_id}/related_ids | Get child nodes, and optionally parent nodes, for a given taxon by Taxonomy ID
[**taxonomy_related_ids_post**](TaxonomyApi.md#taxonomy_related_ids_post) | **POST** /taxonomy/related_ids | Get child nodes, and optionally parent nodes, for a given taxon by Taxonomy ID


# **download_taxonomy_package**
> bytearray download_taxonomy_package(tax_ids, aux_reports=aux_reports, filename=filename)

Get a taxonomy data package by Taxonomy ID

Download a taxonomy data package, including taxonomy and names reports, as a compressed zip archive.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_dataset_request_taxonomy_report_type import V2TaxonomyDatasetRequestTaxonomyReportType
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    tax_ids = [9606] # List[int] | 
    aux_reports = [ncbi.datasets.openapi.V2TaxonomyDatasetRequestTaxonomyReportType()] # List[V2TaxonomyDatasetRequestTaxonomyReportType] | Specify additional report files to include in the data package. The taxonomy report is always included, and its inclusion is not affected by this parameter. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a taxonomy data package by Taxonomy ID
        api_response = api_instance.download_taxonomy_package(tax_ids, aux_reports=aux_reports, filename=filename)
        print("The response of TaxonomyApi->download_taxonomy_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->download_taxonomy_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_ids** | [**List[int]**](int.md)|  | 
 **aux_reports** | [**List[V2TaxonomyDatasetRequestTaxonomyReportType]**](V2TaxonomyDatasetRequestTaxonomyReportType.md)| Specify additional report files to include in the data package. The taxonomy report is always included, and its inclusion is not affected by this parameter. | [optional] 
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

# **download_taxonomy_package_by_post**
> bytearray download_taxonomy_package_by_post(v2_taxonomy_dataset_request, filename=filename)

Get a taxonomy data package by Taxonomy ID

Download a taxonomy data package, including taxonomy and names reports, as a compressed zip archive.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_dataset_request import V2TaxonomyDatasetRequest
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    v2_taxonomy_dataset_request = {"tax_ids":[9606,10090],"aux_reports":["NAMES_REPORT","TAXONOMY_SUMMARY"]} # V2TaxonomyDatasetRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a taxonomy data package by Taxonomy ID
        api_response = api_instance.download_taxonomy_package_by_post(v2_taxonomy_dataset_request, filename=filename)
        print("The response of TaxonomyApi->download_taxonomy_package_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->download_taxonomy_package_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_taxonomy_dataset_request** | [**V2TaxonomyDatasetRequest**](V2TaxonomyDatasetRequest.md)|  | 
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

# **tax_name_query**
> V2SciNameAndIds tax_name_query(taxon_query, tax_rank_filter=tax_rank_filter, taxon_resource_filter=taxon_resource_filter, exact_match=exact_match)

Get a list of taxonomy names and IDs by partial taxonomic name

Get a list of taxonomy names and IDs in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_organism_query_request_tax_rank_filter import V2OrganismQueryRequestTaxRankFilter
from ncbi.datasets.openapi.models.v2_organism_query_request_taxon_resource_filter import V2OrganismQueryRequestTaxonResourceFilter
from ncbi.datasets.openapi.models.v2_sci_name_and_ids import V2SciNameAndIds
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    taxon_query = 'hum' # str | Taxonomy ID or name (common or scientific) at any taxonomic rank
    tax_rank_filter = species # V2OrganismQueryRequestTaxRankFilter | Optionally return results for taxonomic ranks above species using `higher_taxon` (optional) (default to species)
    taxon_resource_filter = TAXON_RESOURCE_FILTER_ALL # V2OrganismQueryRequestTaxonResourceFilter | Limit to taxonomy nodes with gene, genome or organelle data (optional) (default to TAXON_RESOURCE_FILTER_ALL)
    exact_match = False # bool | If true, only return results that exactly match the provided taxonomic name (optional) (default to False)

    try:
        # Get a list of taxonomy names and IDs by partial taxonomic name
        api_response = api_instance.tax_name_query(taxon_query, tax_rank_filter=tax_rank_filter, taxon_resource_filter=taxon_resource_filter, exact_match=exact_match)
        print("The response of TaxonomyApi->tax_name_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->tax_name_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon_query** | **str**| Taxonomy ID or name (common or scientific) at any taxonomic rank | 
 **tax_rank_filter** | [**V2OrganismQueryRequestTaxRankFilter**](.md)| Optionally return results for taxonomic ranks above species using &#x60;higher_taxon&#x60; | [optional] [default to species]
 **taxon_resource_filter** | [**V2OrganismQueryRequestTaxonResourceFilter**](.md)| Limit to taxonomy nodes with gene, genome or organelle data | [optional] [default to TAXON_RESOURCE_FILTER_ALL]
 **exact_match** | **bool**| If true, only return results that exactly match the provided taxonomic name | [optional] [default to False]

### Return type

[**V2SciNameAndIds**](V2SciNameAndIds.md)

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

# **tax_name_query_by_post**
> V2SciNameAndIds tax_name_query_by_post(v2_organism_query_request)

Get a list of taxonomy names and IDs by partial taxonomic name

Get a list of taxonomy names and IDs in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_organism_query_request import V2OrganismQueryRequest
from ncbi.datasets.openapi.models.v2_sci_name_and_ids import V2SciNameAndIds
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    v2_organism_query_request = {"taxon_query":"hum"} # V2OrganismQueryRequest | 

    try:
        # Get a list of taxonomy names and IDs by partial taxonomic name
        api_response = api_instance.tax_name_query_by_post(v2_organism_query_request)
        print("The response of TaxonomyApi->tax_name_query_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->tax_name_query_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_organism_query_request** | [**V2OrganismQueryRequest**](V2OrganismQueryRequest.md)|  | 

### Return type

[**V2SciNameAndIds**](V2SciNameAndIds.md)

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

# **taxonomy_data_report**
> V2reportsTaxonomyDataReportPage taxonomy_data_report(taxons, returned_content=returned_content, page_size=page_size, include_tabular_header=include_tabular_header, page_token=page_token, table_format=table_format, children=children, ranks=ranks)

Get a taxonomy data report by taxon

Get a taxonomy data report by taxon. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request_content_type import V2TaxonomyMetadataRequestContentType
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request_table_format import V2TaxonomyMetadataRequestTableFormat
from ncbi.datasets.openapi.models.v2reports_rank_type import V2reportsRankType
from ncbi.datasets.openapi.models.v2reports_taxonomy_data_report_page import V2reportsTaxonomyDataReportPage
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    taxons = ['9606'] # List[str] | 
    returned_content = COMPLETE # V2TaxonomyMetadataRequestContentType | Return complete taxonomy reports, Taxonomy IDs only, or reports without assembly and gene counts (metadata). (optional) (default to COMPLETE)
    page_size = 20 # int | The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    table_format = SUMMARY # V2TaxonomyMetadataRequestTableFormat | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional) (default to SUMMARY)
    children = True # bool | If true, return results for child taxa. (optional)
    ranks = [ncbi.datasets.openapi.V2reportsRankType()] # List[V2reportsRankType] | Limit results to taxa of the specified ranks. (optional)

    try:
        # Get a taxonomy data report by taxon
        api_response = api_instance.taxonomy_data_report(taxons, returned_content=returned_content, page_size=page_size, include_tabular_header=include_tabular_header, page_token=page_token, table_format=table_format, children=children, ranks=ranks)
        print("The response of TaxonomyApi->taxonomy_data_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_data_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxons** | [**List[str]**](str.md)|  | 
 **returned_content** | [**V2TaxonomyMetadataRequestContentType**](.md)| Return complete taxonomy reports, Taxonomy IDs only, or reports without assembly and gene counts (metadata). | [optional] [default to COMPLETE]
 **page_size** | **int**| The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **table_format** | [**V2TaxonomyMetadataRequestTableFormat**](.md)| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] [default to SUMMARY]
 **children** | **bool**| If true, return results for child taxa. | [optional] 
 **ranks** | [**List[V2reportsRankType]**](V2reportsRankType.md)| Limit results to taxa of the specified ranks. | [optional] 

### Return type

[**V2reportsTaxonomyDataReportPage**](V2reportsTaxonomyDataReportPage.md)

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

# **taxonomy_data_report_post**
> V2reportsTaxonomyDataReportPage taxonomy_data_report_post(v2_taxonomy_metadata_request)

Get a taxonomy data report by taxon

Get a taxonomy data report by taxon. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request import V2TaxonomyMetadataRequest
from ncbi.datasets.openapi.models.v2reports_taxonomy_data_report_page import V2reportsTaxonomyDataReportPage
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    v2_taxonomy_metadata_request = {"taxons":["9606","house mouse"]} # V2TaxonomyMetadataRequest | 

    try:
        # Get a taxonomy data report by taxon
        api_response = api_instance.taxonomy_data_report_post(v2_taxonomy_metadata_request)
        print("The response of TaxonomyApi->taxonomy_data_report_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_data_report_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_taxonomy_metadata_request** | [**V2TaxonomyMetadataRequest**](V2TaxonomyMetadataRequest.md)|  | 

### Return type

[**V2reportsTaxonomyDataReportPage**](V2reportsTaxonomyDataReportPage.md)

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

# **taxonomy_filtered_subtree**
> V2TaxonomyFilteredSubtreeResponse taxonomy_filtered_subtree(taxons, rank_limits=rank_limits, include_incertae_sedis=include_incertae_sedis)

Get a filtered taxonomic subtree by taxon

Get a filtered taxonomic subtree, including parent and child nodes, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_response import V2TaxonomyFilteredSubtreeResponse
from ncbi.datasets.openapi.models.v2reports_rank_type import V2reportsRankType
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    taxons = ['9606'] # List[str] | 
    rank_limits = [ncbi.datasets.openapi.V2reportsRankType()] # List[V2reportsRankType] | Limit to the provided ranks.  If empty, accept any rank. (optional)
    include_incertae_sedis = True # bool | Include nodes with ranks not in 'rank_limits' if their names meet criteria for incertae sedis (of unknown origin). (optional)

    try:
        # Get a filtered taxonomic subtree by taxon
        api_response = api_instance.taxonomy_filtered_subtree(taxons, rank_limits=rank_limits, include_incertae_sedis=include_incertae_sedis)
        print("The response of TaxonomyApi->taxonomy_filtered_subtree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_filtered_subtree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxons** | [**List[str]**](str.md)|  | 
 **rank_limits** | [**List[V2reportsRankType]**](V2reportsRankType.md)| Limit to the provided ranks.  If empty, accept any rank. | [optional] 
 **include_incertae_sedis** | **bool**| Include nodes with ranks not in &#39;rank_limits&#39; if their names meet criteria for incertae sedis (of unknown origin). | [optional] 

### Return type

[**V2TaxonomyFilteredSubtreeResponse**](V2TaxonomyFilteredSubtreeResponse.md)

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

# **taxonomy_filtered_subtree_post**
> V2TaxonomyFilteredSubtreeResponse taxonomy_filtered_subtree_post(v2_taxonomy_filtered_subtree_request)

Get a filtered taxonomic subtree by taxon

Get a filtered taxonomic subtree, including parent and child nodes, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_request import V2TaxonomyFilteredSubtreeRequest
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_response import V2TaxonomyFilteredSubtreeResponse
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    v2_taxonomy_filtered_subtree_request = {"taxons":["9606","10090"]} # V2TaxonomyFilteredSubtreeRequest | 

    try:
        # Get a filtered taxonomic subtree by taxon
        api_response = api_instance.taxonomy_filtered_subtree_post(v2_taxonomy_filtered_subtree_request)
        print("The response of TaxonomyApi->taxonomy_filtered_subtree_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_filtered_subtree_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_taxonomy_filtered_subtree_request** | [**V2TaxonomyFilteredSubtreeRequest**](V2TaxonomyFilteredSubtreeRequest.md)|  | 

### Return type

[**V2TaxonomyFilteredSubtreeResponse**](V2TaxonomyFilteredSubtreeResponse.md)

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

# **taxonomy_image**
> bytearray taxonomy_image(taxon, image_size=image_size)

Get a taxonomy image by taxon

Get an image associated with the specified taxon. By default, in JPEG format, but also available in PNG (accept: image/png), TIFF (accept: accept: image/tiff), and SVG+XML (accept: image/svg+xml) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_image_size import V2ImageSize
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    taxon = '9606' # str | 
    image_size = UNSPECIFIED # V2ImageSize |  (optional) (default to UNSPECIFIED)

    try:
        # Get a taxonomy image by taxon
        api_response = api_instance.taxonomy_image(taxon, image_size=image_size)
        print("The response of TaxonomyApi->taxonomy_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**|  | 
 **image_size** | [**V2ImageSize**](.md)|  | [optional] [default to UNSPECIFIED]

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, image/jpeg, image/png, image/gif, image/tiff, image/svg+xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taxonomy_image_metadata**
> V2TaxonomyImageMetadataResponse taxonomy_image_metadata(taxon)

Get taxonomy image metadata by Taxonomy ID

Get taxonomy image metadata, including the image URL and license information, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_image_metadata_response import V2TaxonomyImageMetadataResponse
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    taxon = '9606' # str | 

    try:
        # Get taxonomy image metadata by Taxonomy ID
        api_response = api_instance.taxonomy_image_metadata(taxon)
        print("The response of TaxonomyApi->taxonomy_image_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_image_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**|  | 

### Return type

[**V2TaxonomyImageMetadataResponse**](V2TaxonomyImageMetadataResponse.md)

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

# **taxonomy_image_metadata_post**
> V2TaxonomyImageMetadataResponse taxonomy_image_metadata_post(v2_taxonomy_image_metadata_request)

Get taxonomy image metadata by Taxonomy ID

Get taxonomy image metadata, including the image URL and license information, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_image_metadata_request import V2TaxonomyImageMetadataRequest
from ncbi.datasets.openapi.models.v2_taxonomy_image_metadata_response import V2TaxonomyImageMetadataResponse
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    v2_taxonomy_image_metadata_request = {"taxon":"9606"} # V2TaxonomyImageMetadataRequest | 

    try:
        # Get taxonomy image metadata by Taxonomy ID
        api_response = api_instance.taxonomy_image_metadata_post(v2_taxonomy_image_metadata_request)
        print("The response of TaxonomyApi->taxonomy_image_metadata_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_image_metadata_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_taxonomy_image_metadata_request** | [**V2TaxonomyImageMetadataRequest**](V2TaxonomyImageMetadataRequest.md)|  | 

### Return type

[**V2TaxonomyImageMetadataResponse**](V2TaxonomyImageMetadataResponse.md)

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

# **taxonomy_image_post**
> bytearray taxonomy_image_post(v2_taxonomy_image_request)

Get a taxonomy image by taxon

Get an image associated with the specified taxon. By default, in JPEG format, but also available in PNG (accept: image/png), TIFF (accept: accept: image/tiff), and SVG+XML (accept: image/svg+xml) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_image_request import V2TaxonomyImageRequest
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    v2_taxonomy_image_request = {"taxon":"9606"} # V2TaxonomyImageRequest | 

    try:
        # Get a taxonomy image by taxon
        api_response = api_instance.taxonomy_image_post(v2_taxonomy_image_request)
        print("The response of TaxonomyApi->taxonomy_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_taxonomy_image_request** | [**V2TaxonomyImageRequest**](V2TaxonomyImageRequest.md)|  | 

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, image/jpeg, image/png, image/tiff, image/svg+xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taxonomy_links**
> V2TaxonomyLinksResponse taxonomy_links(taxon)

Get external links by Taxonomy ID

Get external links associated with a given taxon in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_links_response import V2TaxonomyLinksResponse
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    taxon = '9606' # str | 

    try:
        # Get external links by Taxonomy ID
        api_response = api_instance.taxonomy_links(taxon)
        print("The response of TaxonomyApi->taxonomy_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**|  | 

### Return type

[**V2TaxonomyLinksResponse**](V2TaxonomyLinksResponse.md)

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

# **taxonomy_links_by_post**
> V2TaxonomyLinksResponse taxonomy_links_by_post(v2_taxonomy_links_request)

Get external links by Taxonomy ID

Get external links associated with a given taxon in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_links_request import V2TaxonomyLinksRequest
from ncbi.datasets.openapi.models.v2_taxonomy_links_response import V2TaxonomyLinksResponse
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    v2_taxonomy_links_request = {"taxon":"9606"} # V2TaxonomyLinksRequest | 

    try:
        # Get external links by Taxonomy ID
        api_response = api_instance.taxonomy_links_by_post(v2_taxonomy_links_request)
        print("The response of TaxonomyApi->taxonomy_links_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_links_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_taxonomy_links_request** | [**V2TaxonomyLinksRequest**](V2TaxonomyLinksRequest.md)|  | 

### Return type

[**V2TaxonomyLinksResponse**](V2TaxonomyLinksResponse.md)

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

# **taxonomy_metadata**
> V2TaxonomyMetadataResponse taxonomy_metadata(taxons, returned_content=returned_content, page_size=page_size, include_tabular_header=include_tabular_header, page_token=page_token, table_format=table_format, children=children, ranks=ranks)

Use taxonomic identifiers to get taxonomic metadata (deprecated)

Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get metadata about a taxonomic node including taxonomic identifiers, lineage information, child nodes, and gene and genome counts in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request_content_type import V2TaxonomyMetadataRequestContentType
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request_table_format import V2TaxonomyMetadataRequestTableFormat
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_response import V2TaxonomyMetadataResponse
from ncbi.datasets.openapi.models.v2reports_rank_type import V2reportsRankType
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    taxons = ['9606'] # List[str] | 
    returned_content = COMPLETE # V2TaxonomyMetadataRequestContentType | Return complete taxonomy reports, Taxonomy IDs only, or reports without assembly and gene counts (metadata). (optional) (default to COMPLETE)
    page_size = 20 # int | The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    table_format = SUMMARY # V2TaxonomyMetadataRequestTableFormat | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional) (default to SUMMARY)
    children = True # bool | If true, return results for child taxa. (optional)
    ranks = [ncbi.datasets.openapi.V2reportsRankType()] # List[V2reportsRankType] | Limit results to taxa of the specified ranks. (optional)

    try:
        # Use taxonomic identifiers to get taxonomic metadata (deprecated)
        api_response = api_instance.taxonomy_metadata(taxons, returned_content=returned_content, page_size=page_size, include_tabular_header=include_tabular_header, page_token=page_token, table_format=table_format, children=children, ranks=ranks)
        print("The response of TaxonomyApi->taxonomy_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxons** | [**List[str]**](str.md)|  | 
 **returned_content** | [**V2TaxonomyMetadataRequestContentType**](.md)| Return complete taxonomy reports, Taxonomy IDs only, or reports without assembly and gene counts (metadata). | [optional] [default to COMPLETE]
 **page_size** | **int**| The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **table_format** | [**V2TaxonomyMetadataRequestTableFormat**](.md)| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] [default to SUMMARY]
 **children** | **bool**| If true, return results for child taxa. | [optional] 
 **ranks** | [**List[V2reportsRankType]**](V2reportsRankType.md)| Limit results to taxa of the specified ranks. | [optional] 

### Return type

[**V2TaxonomyMetadataResponse**](V2TaxonomyMetadataResponse.md)

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

# **taxonomy_metadata_post**
> V2TaxonomyMetadataResponse taxonomy_metadata_post(v2_taxonomy_metadata_request)

Get taxonomy metadata by taxon (deprecated)

Get taxonomy metadata by taxon in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request import V2TaxonomyMetadataRequest
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_response import V2TaxonomyMetadataResponse
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    v2_taxonomy_metadata_request = {"taxons":["9606","house mouse"]} # V2TaxonomyMetadataRequest | 

    try:
        # Get taxonomy metadata by taxon (deprecated)
        api_response = api_instance.taxonomy_metadata_post(v2_taxonomy_metadata_request)
        print("The response of TaxonomyApi->taxonomy_metadata_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_metadata_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_taxonomy_metadata_request** | [**V2TaxonomyMetadataRequest**](V2TaxonomyMetadataRequest.md)|  | 

### Return type

[**V2TaxonomyMetadataResponse**](V2TaxonomyMetadataResponse.md)

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

# **taxonomy_names**
> V2reportsTaxonomyNamesDataReportPage taxonomy_names(taxons, page_size=page_size, page_token=page_token, children=children, ranks=ranks)

Get a taxonomy names report by taxon

Get a taxonomy names report, including common names and other synonyms, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2reports_rank_type import V2reportsRankType
from ncbi.datasets.openapi.models.v2reports_taxonomy_names_data_report_page import V2reportsTaxonomyNamesDataReportPage
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    taxons = ['9606'] # List[str] | 
    page_size = 20 # int | The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    children = True # bool | If true, return results for child taxa. (optional)
    ranks = [ncbi.datasets.openapi.V2reportsRankType()] # List[V2reportsRankType] | Limit results to taxa of the specified ranks. (optional)

    try:
        # Get a taxonomy names report by taxon
        api_response = api_instance.taxonomy_names(taxons, page_size=page_size, page_token=page_token, children=children, ranks=ranks)
        print("The response of TaxonomyApi->taxonomy_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxons** | [**List[str]**](str.md)|  | 
 **page_size** | **int**| The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **children** | **bool**| If true, return results for child taxa. | [optional] 
 **ranks** | [**List[V2reportsRankType]**](V2reportsRankType.md)| Limit results to taxa of the specified ranks. | [optional] 

### Return type

[**V2reportsTaxonomyNamesDataReportPage**](V2reportsTaxonomyNamesDataReportPage.md)

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

# **taxonomy_names_post**
> V2reportsTaxonomyNamesDataReportPage taxonomy_names_post(v2_taxonomy_metadata_request)

Get a taxonomy names report by taxon

Get a taxonomy names report, including common names and other synonyms, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request import V2TaxonomyMetadataRequest
from ncbi.datasets.openapi.models.v2reports_taxonomy_names_data_report_page import V2reportsTaxonomyNamesDataReportPage
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    v2_taxonomy_metadata_request = {"taxons":["9606","house mouse"]} # V2TaxonomyMetadataRequest | 

    try:
        # Get a taxonomy names report by taxon
        api_response = api_instance.taxonomy_names_post(v2_taxonomy_metadata_request)
        print("The response of TaxonomyApi->taxonomy_names_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_names_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_taxonomy_metadata_request** | [**V2TaxonomyMetadataRequest**](V2TaxonomyMetadataRequest.md)|  | 

### Return type

[**V2reportsTaxonomyNamesDataReportPage**](V2reportsTaxonomyNamesDataReportPage.md)

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

# **taxonomy_related_ids**
> V2TaxonomyTaxIdsPage taxonomy_related_ids(tax_id, include_lineage=include_lineage, ranks=ranks, page_size=page_size, page_token=page_token)

Get child nodes, and optionally parent nodes, for a given taxon by Taxonomy ID

Get child nodes, and optionally parent nodes, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_tax_ids_page import V2TaxonomyTaxIdsPage
from ncbi.datasets.openapi.models.v2reports_rank_type import V2reportsRankType
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    tax_id = 9606 # int | 
    include_lineage = False # bool | If true, include parent nodes (optional) (default to False)
    ranks = [ncbi.datasets.openapi.V2reportsRankType()] # List[V2reportsRankType] | Limit to taxonomic nodes from the given ranks. (optional)
    page_size = 20 # int | The maximum number of taxids to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)

    try:
        # Get child nodes, and optionally parent nodes, for a given taxon by Taxonomy ID
        api_response = api_instance.taxonomy_related_ids(tax_id, include_lineage=include_lineage, ranks=ranks, page_size=page_size, page_token=page_token)
        print("The response of TaxonomyApi->taxonomy_related_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_related_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_id** | **int**|  | 
 **include_lineage** | **bool**| If true, include parent nodes | [optional] [default to False]
 **ranks** | [**List[V2reportsRankType]**](V2reportsRankType.md)| Limit to taxonomic nodes from the given ranks. | [optional] 
 **page_size** | **int**| The maximum number of taxids to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 

### Return type

[**V2TaxonomyTaxIdsPage**](V2TaxonomyTaxIdsPage.md)

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

# **taxonomy_related_ids_post**
> V2TaxonomyTaxIdsPage taxonomy_related_ids_post(v2_taxonomy_related_id_request)

Get child nodes, and optionally parent nodes, for a given taxon by Taxonomy ID

Get child nodes, and optionally parent nodes, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_taxonomy_related_id_request import V2TaxonomyRelatedIdRequest
from ncbi.datasets.openapi.models.v2_taxonomy_tax_ids_page import V2TaxonomyTaxIdsPage
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
    api_instance = ncbi.datasets.openapi.TaxonomyApi(api_client)
    v2_taxonomy_related_id_request = {"tax_id":9606,"include_lineage":true} # V2TaxonomyRelatedIdRequest | 

    try:
        # Get child nodes, and optionally parent nodes, for a given taxon by Taxonomy ID
        api_response = api_instance.taxonomy_related_ids_post(v2_taxonomy_related_id_request)
        print("The response of TaxonomyApi->taxonomy_related_ids_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_related_ids_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_taxonomy_related_id_request** | [**V2TaxonomyRelatedIdRequest**](V2TaxonomyRelatedIdRequest.md)|  | 

### Return type

[**V2TaxonomyTaxIdsPage**](V2TaxonomyTaxIdsPage.md)

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

