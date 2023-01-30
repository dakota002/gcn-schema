from jsonschema import validate
import json

alert_info_file = open(".\\core-schema\\gcn.notices.core.AlertInfo.json")
alert_info_schema = json.load(alert_info_file)
alert_info_instance = {
    "alert_datetime":"test",
    "alert_tense":"current",
    "alert_type":"initial"
}

validate(instance=alert_info_instance,schema=alert_info_schema)


hardness_ratio_file = open(".\\core-schema\\gcn.notices.core.HardnessRatio.json")
hardness_ratio_schema = json.load(hardness_ratio_file)
hardness_ratio_instance = {
    "hardness_ratio":2
}
validate(hardness_ratio_instance, hardness_ratio_schema)