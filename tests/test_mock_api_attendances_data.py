import json

json_string_attendance_rms = """
{
  "success": true,
  "data": [{
      "id": 33479712,
      "type": "AttendancePeriod",
      "attributes": {
        "employee": 2116366,
        "date": "1985-03-20",
        "start_time": "11:00",
        "end_time": "12:30",
        "break": 60,
        "comment": "release day! GNU Emacs Version 13 is available as free software now *yay*",
        "is_holiday": false,
        "is_on_time_off": false
      }
    }, {
      "id": 33479612,
      "type": "AttendancePeriod",
      "attributes": {
        "employee": 2116366,
        "date": "1985-03-19",
        "start_time": "10:30",
        "end_time": "22:00",
        "break": 120,
        "comment": "just a couple more parentheses...",
        "is_holiday": false,
        "is_on_time_off": false
      }
    }, {
      "id": 33479602,
      "type": "AttendancePeriod",
      "attributes": {
        "employee": 2116366,
        "date": "1985-03-18",
        "start_time": "10:00",
        "end_time": "20:00",
        "break": 90,
        "comment": "working on GNU Emacs",
        "is_holiday": false,
        "is_on_time_off": false
      }
    }
  ]
}
"""
json_dict_attendance_rms = json.loads(json_string_attendance_rms)
