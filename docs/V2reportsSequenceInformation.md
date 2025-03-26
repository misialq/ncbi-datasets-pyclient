# V2reportsSequenceInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**submission_date** | **str** |  | [optional] 
**submitter** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_information import V2reportsSequenceInformation

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceInformation from a JSON string
v2reports_sequence_information_instance = V2reportsSequenceInformation.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceInformation.to_json())

# convert the object into a dict
v2reports_sequence_information_dict = v2reports_sequence_information_instance.to_dict()
# create an instance of V2reportsSequenceInformation from a dict
v2reports_sequence_information_from_dict = V2reportsSequenceInformation.from_dict(v2reports_sequence_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


