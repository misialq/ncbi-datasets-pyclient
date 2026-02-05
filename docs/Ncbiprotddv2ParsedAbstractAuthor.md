# Ncbiprotddv2ParsedAbstractAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surname** | **str** |  | [optional] 
**given_name_initials** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_parsed_abstract_author import Ncbiprotddv2ParsedAbstractAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2ParsedAbstractAuthor from a JSON string
ncbiprotddv2_parsed_abstract_author_instance = Ncbiprotddv2ParsedAbstractAuthor.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2ParsedAbstractAuthor.to_json())

# convert the object into a dict
ncbiprotddv2_parsed_abstract_author_dict = ncbiprotddv2_parsed_abstract_author_instance.to_dict()
# create an instance of Ncbiprotddv2ParsedAbstractAuthor from a dict
ncbiprotddv2_parsed_abstract_author_from_dict = Ncbiprotddv2ParsedAbstractAuthor.from_dict(ncbiprotddv2_parsed_abstract_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


