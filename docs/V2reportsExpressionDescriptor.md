# V2reportsExpressionDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_id** | **str** |  | [optional] 
**expression_release** | [**V2reportsExpressionRelease**](V2reportsExpressionRelease.md) |  | [optional] 
**expression_method** | **str** |  | [optional] 
**bioprojects** | [**List[V2reportsExpressionBioProject]**](V2reportsExpressionBioProject.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_expression_descriptor import V2reportsExpressionDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsExpressionDescriptor from a JSON string
v2reports_expression_descriptor_instance = V2reportsExpressionDescriptor.from_json(json)
# print the JSON string representation of the object
print(V2reportsExpressionDescriptor.to_json())

# convert the object into a dict
v2reports_expression_descriptor_dict = v2reports_expression_descriptor_instance.to_dict()
# create an instance of V2reportsExpressionDescriptor from a dict
v2reports_expression_descriptor_from_dict = V2reportsExpressionDescriptor.from_dict(v2reports_expression_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


