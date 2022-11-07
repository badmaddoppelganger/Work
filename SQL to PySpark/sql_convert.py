# !pip install moz_sql_parser
from moz_sql_parser import parse
from moz_sql_parser import format
import json

query = """select * from eda_sql
"""

v_parse = parse(query)
v_json = json.loads(json.dumps(v_parse, indent=4))


def fn_from(value):
    result_from = ""
    if type(value) is str:
        result_from = format({"from": value})
        result_from = result_from[5:]
    elif type(value) is dict:
        if "name" in value.keys():
            result_from = result_from + value['value'] + ".alias(\"" + value['name'] + "\")"
        else:
            result_from = result_from + value['value'] + ""
    elif type(value) is list:
        for item_from in value:
            if type(item_from) is dict:
                if "name" in item_from.keys():
                    result_from = result_from + item_from['value'] + ".alias(\"" + item_from['name'] + "\"),"
                else:
                    result_from = result_from + item_from['value'] + ","
            elif type(item_from) is str:
                result_from = result_from + item_from + ","
    return result_from


def fn_select(value):
    result_select = ""
    if type(value) is str:
        result_select = result_select + "\"" + value + "\","
    elif type(value) is dict:
        if "name" in value.keys():
            result_select = result_select + "\"" + value['value'] + "\".alias(\"" + value['name'] + "\")"
        else:
            result_select = result_select + "\"" + value['value'] + "\""
    elif type(value) is list:
        for item_select in value:
            if type(item_select) is dict:
                if type(item_select['value']) is dict:
                    if "name" in item_select.keys():
                        result_select = result_select + "\"" + item_select['name'] + "\","
                    else:
                        result_select = result_select + "\"" + item_select['value'] + "\".alias(\"" + item_select[
                            'name'] + "\"),"
                else:
                    result_select = result_select + "\"" + item_select['value'] + "\","
    return result_select[:-1]


def fn_where(value):
    result_where = ""
    result_where = format({"where": value})[6:]
    return result_where


def fn_groupby(value):
    result_groupby = ""
    result_groupby = format({"groupby": value})[9:]
    return result_groupby


def fn_agg(query):
    v_parse = parse(query)
    v_agg = ""
    for i in v_parse["select"]:
        if type(i["value"]) is dict:
            for key, value in i["value"].items():
                v_agg = v_agg + (key + "(" + "col(\"" + str(value) + "\")" + ").alias('" + i["name"] + "')") + ","
    v_agg = v_agg.replace("\n", "")
    return v_agg[:-1]


def fn_orderby(query):
    v_parse = parse(query)
    v_orderby_collist = ""
    v_orderby = v_parse["orderby"]
    for i in v_orderby:
        if i.get("sort", "asc") == "desc":
            v_sortorder = "desc()"
        else:
            v_sortorder = "asc()"
        v_orderby_collist = v_orderby_collist + "col(\"" + str(i.get("value", "")) + "\")." + v_sortorder + ","
    return v_orderby_collist[:-1]


def fn_limit(query):
    v_parse = parse(query)
    v_limit = v_parse["limit"]
    return v_limit


def fn_genSQL(data):
    v_fn_from = v_fn_where = v_fn_groupby = v_fn_agg = v_fn_select = v_fn_orderby = v_fn_limit = ""
    for key, value in data.items():
        # handle from
        if str(key) == "from":
            v_fn_from = fn_from(value)

        # handle where
        if str(key) == "where":
            v_fn_where = fn_where(value)

        # handle groupby
        if str(key) == "groupby":
            v_fn_groupby = fn_groupby(value)

        # handle agg
        if str(key) == "groupby":
            v_fn_agg = fn_agg(query)

        # handle select
        if str(key) == "select":
            v_fn_select = fn_select(value)

        # handle sort
        if str(key) == "orderby":
            v_fn_orderby = fn_orderby(query)

        # handle limit
        if str(key) == "limit":
            v_fn_limit = fn_limit(query)

    v_final_stmt = ""
    if v_fn_from:
        v_final_stmt = v_final_stmt + v_fn_from
    if v_fn_where:
        v_final_stmt = v_final_stmt + "\n.filter(\"" + v_fn_where + "\")"
    if v_fn_groupby:
        v_final_stmt = v_final_stmt + "\n.groupBy(\"" + v_fn_groupby + "\")"
    if v_fn_agg:
        v_final_stmt = v_final_stmt + "\n.agg(" + v_fn_agg + "\")"
    if v_fn_select:
        v_final_stmt = v_final_stmt + "\n.select(" + v_fn_select + ")"
    if v_fn_orderby:
        v_final_stmt = v_final_stmt + "\n.orderBy(" + v_fn_orderby + ")"
    if v_fn_limit:
        v_final_stmt = v_final_stmt + "\n.limit(" + str(v_fn_limit) + ")"

    return v_final_stmt


print(fn_genSQL(v_json))
