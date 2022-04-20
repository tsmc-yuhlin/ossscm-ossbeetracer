import sqlalchemy as db
import pymysql
engine = db.create_engine("mysql+pymysql://name:password@ip:port/db_name")
get_resource_type = 'Nexus'
## get_count = engine.execute('select count(*) from table_name')
get_cpe_uri = engine.execute('select cpe_uri from table_name')
get_start_excl_ver = engine.execute('select start_excl_ver from table_name')
get_end_excl_ver = engine.execute('select end_excl_ver from table_name')
get_start_incl_ver = engine.execute('select start_incl_ver from table_name')
get_end_incl_ver = engine.execute('select end_incl_ver from table_name')
available_tables = get_cpe_uri.fetchall()
get_count = len(available_tables)
for i in range(get_count) :
##    print(available_tables[i])
    ans = str(available_tables[i]).split(':')
    get_resource_name = ans[4]
    if ans[6] == '*' :
        get_version = ans[5]
    else :
        get_version = ans[5]+"-"+ans[6]
