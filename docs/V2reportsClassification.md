# V2reportsClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**superkingdom** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 
**kingdom** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 
**phylum** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 
**var_class** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 
**order** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 
**family** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 
**genus** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 
**species** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 
**domain** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 
**realm** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 
**acellular_root** | [**V2reportsTaxData**](V2reportsTaxData.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_classification import V2reportsClassification

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsClassification from a JSON string
v2reports_classification_instance = V2reportsClassification.from_json(json)
# print the JSON string representation of the object
print(V2reportsClassification.to_json())

# convert the object into a dict
v2reports_classification_dict = v2reports_classification_instance.to_dict()
# create an instance of V2reportsClassification from a dict
v2reports_classification_from_dict = V2reportsClassification.from_dict(v2reports_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


