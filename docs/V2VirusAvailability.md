# V2VirusAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_accessions** | **List[str]** |  | [optional] 
**invalid_accessions** | **List[str]** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_virus_availability import V2VirusAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of V2VirusAvailability from a JSON string
v2_virus_availability_instance = V2VirusAvailability.from_json(json)
# print the JSON string representation of the object
print(V2VirusAvailability.to_json())

# convert the object into a dict
v2_virus_availability_dict = v2_virus_availability_instance.to_dict()
# create an instance of V2VirusAvailability from a dict
v2_virus_availability_from_dict = V2VirusAvailability.from_dict(v2_virus_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


