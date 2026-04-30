# V2reportsSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**institution** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**names** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_submission import V2reportsSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSubmission from a JSON string
v2reports_submission_instance = V2reportsSubmission.from_json(json)
# print the JSON string representation of the object
print(V2reportsSubmission.to_json())

# convert the object into a dict
v2reports_submission_dict = v2reports_submission_instance.to_dict()
# create an instance of V2reportsSubmission from a dict
v2reports_submission_from_dict = V2reportsSubmission.from_dict(v2reports_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


