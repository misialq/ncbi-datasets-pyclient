# V2reportsPatent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 
**patent_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**authors** | [**List[V2reportsAuthor]**](V2reportsAuthor.md) |  | [optional] 
**claim_no** | **int** |  | [optional] 
**issued_date** | **str** |  | [optional] 
**assignee** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_patent import V2reportsPatent

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsPatent from a JSON string
v2reports_patent_instance = V2reportsPatent.from_json(json)
# print the JSON string representation of the object
print(V2reportsPatent.to_json())

# convert the object into a dict
v2reports_patent_dict = v2reports_patent_instance.to_dict()
# create an instance of V2reportsPatent from a dict
v2reports_patent_from_dict = V2reportsPatent.from_dict(v2reports_patent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


