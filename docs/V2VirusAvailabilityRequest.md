# V2VirusAvailabilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_virus_availability_request import V2VirusAvailabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2VirusAvailabilityRequest from a JSON string
v2_virus_availability_request_instance = V2VirusAvailabilityRequest.from_json(json)
# print the JSON string representation of the object
print(V2VirusAvailabilityRequest.to_json())

# convert the object into a dict
v2_virus_availability_request_dict = v2_virus_availability_request_instance.to_dict()
# create an instance of V2VirusAvailabilityRequest from a dict
v2_virus_availability_request_from_dict = V2VirusAvailabilityRequest.from_dict(v2_virus_availability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


