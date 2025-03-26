# ncbi.datasets.openapi.TaxonomyApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_taxonomy_package**](TaxonomyApi.md#download_taxonomy_package) | **GET** /taxonomy/taxon/{tax_ids}/download | Get a taxonomy data package by tax ID
[**download_taxonomy_package_by_post**](TaxonomyApi.md#download_taxonomy_package_by_post) | **POST** /taxonomy/download | Get a taxonomy data package by tax_id
[**tax_name_query**](TaxonomyApi.md#tax_name_query) | **GET** /taxonomy/taxon_suggest/{taxon_query} | Get a list of taxonomy names and IDs given a partial taxonomic name
[**tax_name_query_by_post**](TaxonomyApi.md#tax_name_query_by_post) | **POST** /taxonomy/taxon_suggest | Get a list of taxonomy names and IDs given a partial taxonomic name
[**taxonomy_data_report**](TaxonomyApi.md#taxonomy_data_report) | **GET** /taxonomy/taxon/{taxons}/dataset_report | Use taxonomic identifiers to get taxonomic data report
[**taxonomy_data_report_post**](TaxonomyApi.md#taxonomy_data_report_post) | **POST** /taxonomy/dataset_report | Use taxonomic identifiers to get taxonomic names data report by post
[**taxonomy_filtered_subtree**](TaxonomyApi.md#taxonomy_filtered_subtree) | **GET** /taxonomy/taxon/{taxons}/filtered_subtree | Use taxonomic identifiers to get a filtered taxonomic subtree
[**taxonomy_filtered_subtree_post**](TaxonomyApi.md#taxonomy_filtered_subtree_post) | **POST** /taxonomy/filtered_subtree | Use taxonomic identifiers to get a filtered taxonomic subtree by post
[**taxonomy_image**](TaxonomyApi.md#taxonomy_image) | **GET** /taxonomy/taxon/{taxon}/image | Retrieve image associated with a taxonomic identifier
[**taxonomy_image_metadata**](TaxonomyApi.md#taxonomy_image_metadata) | **GET** /taxonomy/taxon/{taxon}/image/metadata | Retrieve image metadata associated with a taxonomic identifier
[**taxonomy_image_metadata_post**](TaxonomyApi.md#taxonomy_image_metadata_post) | **POST** /taxonomy/image/metadata | Retrieve image metadata associated with a taxonomic identifier by post
[**taxonomy_image_post**](TaxonomyApi.md#taxonomy_image_post) | **POST** /taxonomy/image | Retrieve image associated with a taxonomic identifier by post
[**taxonomy_links**](TaxonomyApi.md#taxonomy_links) | **GET** /taxonomy/taxon/{taxon}/links | Retrieve external links associated with a taxonomic identifier.
[**taxonomy_links_by_post**](TaxonomyApi.md#taxonomy_links_by_post) | **POST** /taxonomy/links | Retrieve external links associated with a taxonomic identifier.
[**taxonomy_metadata**](TaxonomyApi.md#taxonomy_metadata) | **GET** /taxonomy/taxon/{taxons} | Use taxonomic identifiers to get taxonomic metadata
[**taxonomy_metadata_post**](TaxonomyApi.md#taxonomy_metadata_post) | **POST** /taxonomy | Use taxonomic identifiers to get taxonomic metadata by post
[**taxonomy_names**](TaxonomyApi.md#taxonomy_names) | **GET** /taxonomy/taxon/{taxons}/name_report | Use taxonomic identifiers to get taxonomic names data report
[**taxonomy_names_post**](TaxonomyApi.md#taxonomy_names_post) | **POST** /taxonomy/name_report | Use taxonomic identifiers to get taxonomic names data report by post
[**taxonomy_related_ids**](TaxonomyApi.md#taxonomy_related_ids) | **GET** /taxonomy/taxon/{tax_id}/related_ids | Use taxonomic identifier to get related taxonomic identifiers, such as children
[**taxonomy_related_ids_post**](TaxonomyApi.md#taxonomy_related_ids_post) | **POST** /taxonomy/related_ids | Use taxonomic identifier to get related taxonomic identifiers, such as children


# **download_taxonomy_package**
> bytearray download_taxonomy_package(tax_ids, aux_reports=aux_reports, filename=filename)

Get a taxonomy data package by tax ID

Download a taxonomy report and names data package.

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
    tax_ids = [[9606]] # List[int] | 
    aux_reports = [ncbi.datasets.openapi.V2TaxonomyDatasetRequestTaxonomyReportType()] # List[V2TaxonomyDatasetRequestTaxonomyReportType] | list additional reports to include with download. TAXONOMY_REPORT is included by default. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a taxonomy data package by tax ID
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
 **aux_reports** | [**List[V2TaxonomyDatasetRequestTaxonomyReportType]**](V2TaxonomyDatasetRequestTaxonomyReportType.md)| list additional reports to include with download. TAXONOMY_REPORT is included by default. | [optional] 
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

Get a taxonomy data package by tax_id

Download a taxonomy report and names data package.

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
    v2_taxonomy_dataset_request = {"tax_ids":[9606,10090]} # V2TaxonomyDatasetRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a taxonomy data package by tax_id
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

Get a list of taxonomy names and IDs given a partial taxonomic name

This endpoint retrieves a list of taxonomy names and IDs given a possibly partial taxonomic name of any rank.

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
    taxon_query = 'hum' # str | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank
    tax_rank_filter = ncbi.datasets.openapi.V2OrganismQueryRequestTaxRankFilter() # V2OrganismQueryRequestTaxRankFilter | Set the scope of searched tax ranks when filtering by gene or genome.  Not used for 'all' (optional)
    taxon_resource_filter = ncbi.datasets.openapi.V2OrganismQueryRequestTaxonResourceFilter() # V2OrganismQueryRequestTaxonResourceFilter | Limit results to those with gene or genome counts (no filter by default) (optional)
    exact_match = False # bool | If true, only return results that exactly match the provided name or tax-id (optional) (default to False)

    try:
        # Get a list of taxonomy names and IDs given a partial taxonomic name
        api_response = api_instance.tax_name_query(taxon_query, tax_rank_filter=tax_rank_filter, taxon_resource_filter=taxon_resource_filter, exact_match=exact_match)
        print("The response of TaxonomyApi->tax_name_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->tax_name_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon_query** | **str**| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank | 
 **tax_rank_filter** | [**V2OrganismQueryRequestTaxRankFilter**](.md)| Set the scope of searched tax ranks when filtering by gene or genome.  Not used for &#39;all&#39; | [optional] 
 **taxon_resource_filter** | [**V2OrganismQueryRequestTaxonResourceFilter**](.md)| Limit results to those with gene or genome counts (no filter by default) | [optional] 
 **exact_match** | **bool**| If true, only return results that exactly match the provided name or tax-id | [optional] [default to False]

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

Get a list of taxonomy names and IDs given a partial taxonomic name

This endpoint retrieves a list of taxonomy names and IDs given a possibly partial taxonomic name of any rank, by post.

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
        # Get a list of taxonomy names and IDs given a partial taxonomic name
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

Use taxonomic identifiers to get taxonomic data report

Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get metadata about a taxonomic node including taxonomic identifiers, lineage information, child nodes, and gene and genome counts in JSON format.

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
    taxons = ['[\"9606\"]'] # List[str] | 
    returned_content = ncbi.datasets.openapi.V2TaxonomyMetadataRequestContentType() # V2TaxonomyMetadataRequestContentType | Return either tax-ids alone, or entire taxononmy-metadata records (optional)
    page_size = 20 # int | The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_token = 'page_token_example' # str | A page token is returned from `GetTaxonomyDataReportFor` and `GetTaxonomyNamesDataReportFor` calls with more than `page_size` results. When `page_token` is empty, all results have been retrieved. (optional)
    table_format = ncbi.datasets.openapi.V2TaxonomyMetadataRequestTableFormat() # V2TaxonomyMetadataRequestTableFormat |  (optional)
    children = True # bool | Flag for tax explosion. (optional)
    ranks = [ncbi.datasets.openapi.V2reportsRankType()] # List[V2reportsRankType] | Only include taxons of the provided ranks. If empty, return all ranks. (optional)

    try:
        # Use taxonomic identifiers to get taxonomic data report
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
 **returned_content** | [**V2TaxonomyMetadataRequestContentType**](.md)| Return either tax-ids alone, or entire taxononmy-metadata records | [optional] 
 **page_size** | **int**| The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_token** | **str**| A page token is returned from &#x60;GetTaxonomyDataReportFor&#x60; and &#x60;GetTaxonomyNamesDataReportFor&#x60; calls with more than &#x60;page_size&#x60; results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **table_format** | [**V2TaxonomyMetadataRequestTableFormat**](.md)|  | [optional] 
 **children** | **bool**| Flag for tax explosion. | [optional] 
 **ranks** | [**List[V2reportsRankType]**](V2reportsRankType.md)| Only include taxons of the provided ranks. If empty, return all ranks. | [optional] 

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

Use taxonomic identifiers to get taxonomic names data report by post

Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get metadata about a taxonomic node including taxonomic identifiers, lineage information, child nodes, and gene and genome counts in JSON format.

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
        # Use taxonomic identifiers to get taxonomic names data report by post
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
> V2TaxonomyFilteredSubtreeResponse taxonomy_filtered_subtree(taxons, specified_limit=specified_limit, rank_limits=rank_limits)

Use taxonomic identifiers to get a filtered taxonomic subtree

Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get a filtered taxonomic subtree that includes the full parent lineage and all immediate children from the selected taxonomic ranks in JSON format.

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
    taxons = ['[\"9606\"]'] # List[str] | 
    specified_limit = True # bool | Limit to specified species (optional)
    rank_limits = [ncbi.datasets.openapi.V2reportsRankType()] # List[V2reportsRankType] | Limit to the provided ranks.  If empty, accept any rank. (optional)

    try:
        # Use taxonomic identifiers to get a filtered taxonomic subtree
        api_response = api_instance.taxonomy_filtered_subtree(taxons, specified_limit=specified_limit, rank_limits=rank_limits)
        print("The response of TaxonomyApi->taxonomy_filtered_subtree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_filtered_subtree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxons** | [**List[str]**](str.md)|  | 
 **specified_limit** | **bool**| Limit to specified species | [optional] 
 **rank_limits** | [**List[V2reportsRankType]**](V2reportsRankType.md)| Limit to the provided ranks.  If empty, accept any rank. | [optional] 

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

Use taxonomic identifiers to get a filtered taxonomic subtree by post

Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get a filtered taxonomic subtree that includes the full parent lineage and all immediate children from the selected taxonomic ranks in JSON format.

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
        # Use taxonomic identifiers to get a filtered taxonomic subtree by post
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

Retrieve image associated with a taxonomic identifier

Using an NCBI Taxonomy ID or a name (common or scientific) at any rank, get the image associated with the taxon.

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
    image_size = ncbi.datasets.openapi.V2ImageSize() # V2ImageSize |  (optional)

    try:
        # Retrieve image associated with a taxonomic identifier
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
 **image_size** | [**V2ImageSize**](.md)|  | [optional] 

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

Retrieve image metadata associated with a taxonomic identifier

Using an NCBI Taxonomy ID or a name (common or scientific) at any rank, get the image metadata associated with the taxon.

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
        # Retrieve image metadata associated with a taxonomic identifier
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

Retrieve image metadata associated with a taxonomic identifier by post

Using an NCBI Taxonomy ID or a name (common or scientific) at any rank, get the image metadata associated with the taxon.

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
        # Retrieve image metadata associated with a taxonomic identifier by post
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

Retrieve image associated with a taxonomic identifier by post

Using an NCBI Taxonomy ID or a name (common or scientific) at any rank, get the image associated with the taxon.

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
        # Retrieve image associated with a taxonomic identifier by post
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

Retrieve external links associated with a taxonomic identifier.

Using an NCBI Taxonomy ID at any rank, get the external links associated with the taxon.

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
        # Retrieve external links associated with a taxonomic identifier.
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

Retrieve external links associated with a taxonomic identifier.

Using an NCBI Taxonomy ID at any rank, get the external links associated with the taxon.

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
        # Retrieve external links associated with a taxonomic identifier.
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

Use taxonomic identifiers to get taxonomic metadata

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
    taxons = ['[\"9606\"]'] # List[str] | 
    returned_content = ncbi.datasets.openapi.V2TaxonomyMetadataRequestContentType() # V2TaxonomyMetadataRequestContentType | Return either tax-ids alone, or entire taxononmy-metadata records (optional)
    page_size = 20 # int | The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_token = 'page_token_example' # str | A page token is returned from `GetTaxonomyDataReportFor` and `GetTaxonomyNamesDataReportFor` calls with more than `page_size` results. When `page_token` is empty, all results have been retrieved. (optional)
    table_format = ncbi.datasets.openapi.V2TaxonomyMetadataRequestTableFormat() # V2TaxonomyMetadataRequestTableFormat |  (optional)
    children = True # bool | Flag for tax explosion. (optional)
    ranks = [ncbi.datasets.openapi.V2reportsRankType()] # List[V2reportsRankType] | Only include taxons of the provided ranks. If empty, return all ranks. (optional)

    try:
        # Use taxonomic identifiers to get taxonomic metadata
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
 **returned_content** | [**V2TaxonomyMetadataRequestContentType**](.md)| Return either tax-ids alone, or entire taxononmy-metadata records | [optional] 
 **page_size** | **int**| The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_token** | **str**| A page token is returned from &#x60;GetTaxonomyDataReportFor&#x60; and &#x60;GetTaxonomyNamesDataReportFor&#x60; calls with more than &#x60;page_size&#x60; results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **table_format** | [**V2TaxonomyMetadataRequestTableFormat**](.md)|  | [optional] 
 **children** | **bool**| Flag for tax explosion. | [optional] 
 **ranks** | [**List[V2reportsRankType]**](V2reportsRankType.md)| Only include taxons of the provided ranks. If empty, return all ranks. | [optional] 

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

Use taxonomic identifiers to get taxonomic metadata by post

Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get metadata about a taxonomic node including taxonomic identifiers, lineage information, child nodes, and gene and genome counts in JSON format.

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
        # Use taxonomic identifiers to get taxonomic metadata by post
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
> V2reportsTaxonomyNamesDataReportPage taxonomy_names(taxons, returned_content=returned_content, page_size=page_size, include_tabular_header=include_tabular_header, page_token=page_token, table_format=table_format, children=children, ranks=ranks)

Use taxonomic identifiers to get taxonomic names data report

Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get metadata about associated taxonomic names.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request_content_type import V2TaxonomyMetadataRequestContentType
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request_table_format import V2TaxonomyMetadataRequestTableFormat
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
    taxons = ['[\"9606\"]'] # List[str] | 
    returned_content = ncbi.datasets.openapi.V2TaxonomyMetadataRequestContentType() # V2TaxonomyMetadataRequestContentType | Return either tax-ids alone, or entire taxononmy-metadata records (optional)
    page_size = 20 # int | The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_token = 'page_token_example' # str | A page token is returned from `GetTaxonomyDataReportFor` and `GetTaxonomyNamesDataReportFor` calls with more than `page_size` results. When `page_token` is empty, all results have been retrieved. (optional)
    table_format = ncbi.datasets.openapi.V2TaxonomyMetadataRequestTableFormat() # V2TaxonomyMetadataRequestTableFormat |  (optional)
    children = True # bool | Flag for tax explosion. (optional)
    ranks = [ncbi.datasets.openapi.V2reportsRankType()] # List[V2reportsRankType] | Only include taxons of the provided ranks. If empty, return all ranks. (optional)

    try:
        # Use taxonomic identifiers to get taxonomic names data report
        api_response = api_instance.taxonomy_names(taxons, returned_content=returned_content, page_size=page_size, include_tabular_header=include_tabular_header, page_token=page_token, table_format=table_format, children=children, ranks=ranks)
        print("The response of TaxonomyApi->taxonomy_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxons** | [**List[str]**](str.md)|  | 
 **returned_content** | [**V2TaxonomyMetadataRequestContentType**](.md)| Return either tax-ids alone, or entire taxononmy-metadata records | [optional] 
 **page_size** | **int**| The maximum number of taxons to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_token** | **str**| A page token is returned from &#x60;GetTaxonomyDataReportFor&#x60; and &#x60;GetTaxonomyNamesDataReportFor&#x60; calls with more than &#x60;page_size&#x60; results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **table_format** | [**V2TaxonomyMetadataRequestTableFormat**](.md)|  | [optional] 
 **children** | **bool**| Flag for tax explosion. | [optional] 
 **ranks** | [**List[V2reportsRankType]**](V2reportsRankType.md)| Only include taxons of the provided ranks. If empty, return all ranks. | [optional] 

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

Use taxonomic identifiers to get taxonomic names data report by post

Using NCBI Taxonomy IDs or names (common or scientific) at any rank, get metadata about associated taxonomic names.

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
        # Use taxonomic identifiers to get taxonomic names data report by post
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
> V2TaxonomyTaxIdsPage taxonomy_related_ids(tax_id, include_lineage=include_lineage, include_subtree=include_subtree, ranks=ranks, page_size=page_size, page_token=page_token)

Use taxonomic identifier to get related taxonomic identifiers, such as children

Using a single NCBI Taxonomy ID at any rank, get a list of related taxonomic IDs in JSON format.

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
    include_lineage = False # bool | If true, return reports for all taxonomy nodes in the lineages of the requested tax_id (optional) (default to False)
    include_subtree = False # bool | This field is deprecated because all requests include the subtree, so it has no effect (optional) (default to False)
    ranks = [ncbi.datasets.openapi.V2reportsRankType()] # List[V2reportsRankType] | Only include taxons of the provided ranks. If empty, return all ranks. (optional)
    page_size = 20 # int | The maximum number of taxids to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from a `GetRelatedTaxids` call with more than `page_size` results. Use this token, along with the previous `TaxonomyRelatedIdRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)

    try:
        # Use taxonomic identifier to get related taxonomic identifiers, such as children
        api_response = api_instance.taxonomy_related_ids(tax_id, include_lineage=include_lineage, include_subtree=include_subtree, ranks=ranks, page_size=page_size, page_token=page_token)
        print("The response of TaxonomyApi->taxonomy_related_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyApi->taxonomy_related_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_id** | **int**|  | 
 **include_lineage** | **bool**| If true, return reports for all taxonomy nodes in the lineages of the requested tax_id | [optional] [default to False]
 **include_subtree** | **bool**| This field is deprecated because all requests include the subtree, so it has no effect | [optional] [default to False]
 **ranks** | [**List[V2reportsRankType]**](V2reportsRankType.md)| Only include taxons of the provided ranks. If empty, return all ranks. | [optional] 
 **page_size** | **int**| The maximum number of taxids to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from a &#x60;GetRelatedTaxids&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;TaxonomyRelatedIdRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 

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

Use taxonomic identifier to get related taxonomic identifiers, such as children

Using a single NCBI Taxonomy ID at any rank, get a list of related taxonomic IDs in JSON format.

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
    v2_taxonomy_related_id_request = {"tax_id":9606} # V2TaxonomyRelatedIdRequest | 

    try:
        # Use taxonomic identifier to get related taxonomic identifiers, such as children
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

