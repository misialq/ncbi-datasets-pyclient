# V2reportsExpressionRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_name** | **str** |  | [optional] 
**assembly_accession** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_expression_release import V2reportsExpressionRelease

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsExpressionRelease from a JSON string
v2reports_expression_release_instance = V2reportsExpressionRelease.from_json(json)
# print the JSON string representation of the object
print(V2reportsExpressionRelease.to_json())

# convert the object into a dict
v2reports_expression_release_dict = v2reports_expression_release_instance.to_dict()
# create an instance of V2reportsExpressionRelease from a dict
v2reports_expression_release_from_dict = V2reportsExpressionRelease.from_dict(v2reports_expression_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


