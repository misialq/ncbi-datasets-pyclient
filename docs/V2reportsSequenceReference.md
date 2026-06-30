# V2reportsSequenceReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article** | [**V2reportsArticle**](V2reportsArticle.md) |  | [optional] 
**journal** | [**V2reportsJournal**](V2reportsJournal.md) |  | [optional] 
**book** | [**V2reportsBook**](V2reportsBook.md) |  | [optional] 
**proceedings** | [**V2reportsProceedings**](V2reportsProceedings.md) |  | [optional] 
**thesis** | [**V2reportsThesis**](V2reportsThesis.md) |  | [optional] 
**patent** | [**V2reportsPatent**](V2reportsPatent.md) |  | [optional] 
**general** | [**V2reportsGeneral**](V2reportsGeneral.md) |  | [optional] 
**medline** | [**V2reportsMedline**](V2reportsMedline.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_reference import V2reportsSequenceReference

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceReference from a JSON string
v2reports_sequence_reference_instance = V2reportsSequenceReference.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceReference.to_json())

# convert the object into a dict
v2reports_sequence_reference_dict = v2reports_sequence_reference_instance.to_dict()
# create an instance of V2reportsSequenceReference from a dict
v2reports_sequence_reference_from_dict = V2reportsSequenceReference.from_dict(v2reports_sequence_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


