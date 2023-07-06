#json_data={"name":"john","age":30,"city":"New York"}
#print(type(json_data))
#print(json_data["name"])
import json
json_data_str='{"name":"john","age":30,"city":"New York"}'
py_dict=json.loads(json_data_str)
print(type(py_dict))
print(py_dict["name"])
print(py_dict["age"])
print(py_dict.get("name"))
print(py_dict.keys())
print(py_dict.values)