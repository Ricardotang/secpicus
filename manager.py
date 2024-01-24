import json


def load_all_info():
    with open("static/manager.json", "r") as f:
        return json.load(f)

def get_manager_info(manager_name: str, info_map: dict):
## 根据manager_name获取从数据库查询manager基础信息，
    info = info_map[manager_name]
    return info

def get_manager_by_id(id: str, info_map: dict):
    info = info_map[id]
    return info