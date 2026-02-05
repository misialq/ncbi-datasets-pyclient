# Ncbiprotddv2ParsedAbstract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**authors** | [**List[Ncbiprotddv2ParsedAbstractAuthor]**](Ncbiprotddv2ParsedAbstractAuthor.md) |  | [optional] 
**epub** | [**Ncbiprotddv2ParsedAbstractEpub**](Ncbiprotddv2ParsedAbstractEpub.md) |  | [optional] 
**abstract_text** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_parsed_abstract import Ncbiprotddv2ParsedAbstract

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2ParsedAbstract from a JSON string
ncbiprotddv2_parsed_abstract_instance = Ncbiprotddv2ParsedAbstract.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2ParsedAbstract.to_json())

# convert the object into a dict
ncbiprotddv2_parsed_abstract_dict = ncbiprotddv2_parsed_abstract_instance.to_dict()
# create an instance of Ncbiprotddv2ParsedAbstract from a dict
ncbiprotddv2_parsed_abstract_from_dict = Ncbiprotddv2ParsedAbstract.from_dict(ncbiprotddv2_parsed_abstract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


