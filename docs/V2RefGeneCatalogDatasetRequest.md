# V2RefGeneCatalogDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opaque_solr_query** | **str** |  | [optional] 
**files** | [**List[V2RefGeneCatalogDatasetRequestFileType]**](V2RefGeneCatalogDatasetRequestFileType.md) |  | [optional] 
**element_flank_config** | [**V2ElementFlankConfig**](V2ElementFlankConfig.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_ref_gene_catalog_dataset_request import V2RefGeneCatalogDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2RefGeneCatalogDatasetRequest from a JSON string
v2_ref_gene_catalog_dataset_request_instance = V2RefGeneCatalogDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(V2RefGeneCatalogDatasetRequest.to_json())

# convert the object into a dict
v2_ref_gene_catalog_dataset_request_dict = v2_ref_gene_catalog_dataset_request_instance.to_dict()
# create an instance of V2RefGeneCatalogDatasetRequest from a dict
v2_ref_gene_catalog_dataset_request_from_dict = V2RefGeneCatalogDatasetRequest.from_dict(v2_ref_gene_catalog_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


