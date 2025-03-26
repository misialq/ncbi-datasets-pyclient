# V2DatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genome_v2** | [**V2AssemblyDatasetRequest**](V2AssemblyDatasetRequest.md) |  | [optional] 
**gene_v2** | [**V2GeneDatasetRequest**](V2GeneDatasetRequest.md) |  | [optional] 
**virus_v2** | [**V2VirusDatasetRequest**](V2VirusDatasetRequest.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_dataset_request import V2DatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DatasetRequest from a JSON string
v2_dataset_request_instance = V2DatasetRequest.from_json(json)
# print the JSON string representation of the object
print(V2DatasetRequest.to_json())

# convert the object into a dict
v2_dataset_request_dict = v2_dataset_request_instance.to_dict()
# create an instance of V2DatasetRequest from a dict
v2_dataset_request_from_dict = V2DatasetRequest.from_dict(v2_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


