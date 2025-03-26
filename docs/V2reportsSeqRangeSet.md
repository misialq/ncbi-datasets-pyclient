# V2reportsSeqRangeSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession_version** | **str** |  | [optional] 
**range** | [**List[V2reportsRange]**](V2reportsRange.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_seq_range_set import V2reportsSeqRangeSet

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSeqRangeSet from a JSON string
v2reports_seq_range_set_instance = V2reportsSeqRangeSet.from_json(json)
# print the JSON string representation of the object
print(V2reportsSeqRangeSet.to_json())

# convert the object into a dict
v2reports_seq_range_set_dict = v2reports_seq_range_set_instance.to_dict()
# create an instance of V2reportsSeqRangeSet from a dict
v2reports_seq_range_set_from_dict = V2reportsSeqRangeSet.from_dict(v2reports_seq_range_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


