# V2reportsAggregateExpressionValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mean** | **float** |  | [optional] 
**stddev** | **float** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_aggregate_expression_value import V2reportsAggregateExpressionValue

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAggregateExpressionValue from a JSON string
v2reports_aggregate_expression_value_instance = V2reportsAggregateExpressionValue.from_json(json)
# print the JSON string representation of the object
print(V2reportsAggregateExpressionValue.to_json())

# convert the object into a dict
v2reports_aggregate_expression_value_dict = v2reports_aggregate_expression_value_instance.to_dict()
# create an instance of V2reportsAggregateExpressionValue from a dict
v2reports_aggregate_expression_value_from_dict = V2reportsAggregateExpressionValue.from_dict(v2reports_aggregate_expression_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


