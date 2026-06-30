# V2reportsJournal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 
**pmcid** | **str** |  | [optional] 
**doi** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**journal_name** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 
**issue** | **str** |  | [optional] 
**pages** | **str** |  | [optional] 
**authors** | [**List[V2reportsAuthor]**](V2reportsAuthor.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_journal import V2reportsJournal

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsJournal from a JSON string
v2reports_journal_instance = V2reportsJournal.from_json(json)
# print the JSON string representation of the object
print(V2reportsJournal.to_json())

# convert the object into a dict
v2reports_journal_dict = v2reports_journal_instance.to_dict()
# create an instance of V2reportsJournal from a dict
v2reports_journal_from_dict = V2reportsJournal.from_dict(v2reports_journal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


