# V2reportsSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_name** | **str** |  | [optional] 
**aggregate_expression_value** | [**V2reportsAggregateExpressionValue**](V2reportsAggregateExpressionValue.md) |  | [optional] 
**biosamples** | [**List[V2reportsBioSample]**](V2reportsBioSample.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sample import V2reportsSample

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSample from a JSON string
v2reports_sample_instance = V2reportsSample.from_json(json)
# print the JSON string representation of the object
print(V2reportsSample.to_json())

# convert the object into a dict
v2reports_sample_dict = v2reports_sample_instance.to_dict()
# create an instance of V2reportsSample from a dict
v2reports_sample_from_dict = V2reportsSample.from_dict(v2reports_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


