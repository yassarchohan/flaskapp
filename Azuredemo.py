import MySqlConnection


def searchemp(name):
    allnames = MySqlConnection.getMysqlData(name)
    return allnames