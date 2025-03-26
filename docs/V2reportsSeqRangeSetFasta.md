# V2reportsSeqRangeSetFasta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seq_id** | **str** |  | [optional] 
**accession_version** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**sequence_hash** | **str** |  | [optional] 
**range** | [**List[V2reportsRange]**](V2reportsRange.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_seq_range_set_fasta import V2reportsSeqRangeSetFasta

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSeqRangeSetFasta from a JSON string
v2reports_seq_range_set_fasta_instance = V2reportsSeqRangeSetFasta.from_json(json)
# print the JSON string representation of the object
print(V2reportsSeqRangeSetFasta.to_json())

# convert the object into a dict
v2reports_seq_range_set_fasta_dict = v2reports_seq_range_set_fasta_instance.to_dict()
# create an instance of V2reportsSeqRangeSetFasta from a dict
v2reports_seq_range_set_fasta_from_dict = V2reportsSeqRangeSetFasta.from_dict(v2reports_seq_range_set_fasta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


