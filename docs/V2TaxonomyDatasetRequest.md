# V2TaxonomyDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_ids** | **List[int]** |  | [optional] 
**aux_reports** | [**List[V2TaxonomyDatasetRequestTaxonomyReportType]**](V2TaxonomyDatasetRequestTaxonomyReportType.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_dataset_request import V2TaxonomyDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyDatasetRequest from a JSON string
v2_taxonomy_dataset_request_instance = V2TaxonomyDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyDatasetRequest.to_json())

# convert the object into a dict
v2_taxonomy_dataset_request_dict = v2_taxonomy_dataset_request_instance.to_dict()
# create an instance of V2TaxonomyDatasetRequest from a dict
v2_taxonomy_dataset_request_from_dict = V2TaxonomyDatasetRequest.from_dict(v2_taxonomy_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


