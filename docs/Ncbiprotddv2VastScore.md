# Ncbiprotddv2VastScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vast_score** | **float** |  | [optional] 
**align_length** | **int** |  | [optional] 
**pct_identity** | **float** |  | [optional] 
**rmsd** | **float** |  | [optional] 
**p_value** | **float** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_vast_score import Ncbiprotddv2VastScore

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2VastScore from a JSON string
ncbiprotddv2_vast_score_instance = Ncbiprotddv2VastScore.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2VastScore.to_json())

# convert the object into a dict
ncbiprotddv2_vast_score_dict = ncbiprotddv2_vast_score_instance.to_dict()
# create an instance of Ncbiprotddv2VastScore from a dict
ncbiprotddv2_vast_score_from_dict = Ncbiprotddv2VastScore.from_dict(ncbiprotddv2_vast_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


