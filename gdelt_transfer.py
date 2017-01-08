import csv
import MySQLdb
import datetime

##############################################
# READ EVENTS FROM LOCAL CSV AND ONLY        #
# KEEP PROTEST EVENTS                        #
##############################################
def getGDELTEvents():
    gdelt_events = []

    with open('/PATH/TO/latest_gdelt_events.csv', 'rb') as gdelt_events_csv:
        gdelt_reader = csv.reader(gdelt_events_csv, delimiter='\t')

        for event in gdelt_reader:
            #This is my own set of filters as I was interested in protest events
            if event[28] == "14":
                gdelt_events.append(event)

    return gdelt_events



##############################################
# COMMIT PROTEST EVENTS TO DB                #
##############################################
def commitGDELTEvents(my_gdelt_events):
    # Open database connection
    conn = MySQLdb.connect("HOST",
                           "USERNAME",
                           "PASSWORD",
                           "DATABASE")

    # prepare cursors
    cur = conn.cursor()

    # Iterate through events
    for event in my_gdelt_events:
        # Upload event
        add_event = ("INSERT INTO gdelt "
                        "(gdelt_id, published_date, insert_date, url, "
                        "actor1_code, actor1_name, actor1_country_code, actor1_known_group_code, actor1_ethnic_code, actor1_religion1_code, actor1_religion2_code, actor1_type1_code, actor1_type2_code, actor1_type3_code, "
                        "actor2_code, actor2_name, actor2_country_code, actor2_known_group_code, actor2_ethnic_code, actor2_religion1_code, actor2_religion2_code, actor2_type1_code, actor2_type2_code, actor2_type3_code, "
                        "is_root_event, event_code, event_base_code, event_root_code, quad_class, "
                        "goldstein_scale, num_mentions, num_sources, num_articles, avg_tone, "
                        "actor1_geo_type, actor1_geo_full_name, actor1_geo_country_code, actor1_geo_adm1_code, actor1_geo_adm2_code, actor1_geo_lat, actor1_geo_long, actor1_geo_feature_id, "
                        "actor2_geo_type, actor2_geo_full_name, actor2_geo_country_code, actor2_geo_adm1_code, actor2_geo_adm2_code, actor2_geo_lat, actor2_geo_long, actor2_geo_feature_id, "
                        "action_geo_type, action_geo_full_name, action_geo_country_code, action_geo_adm1_code, action_geo_adm2_code, action_geo_lat, action_geo_long, action_geo_feature_id) "
                        "VALUES (%s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s)")

        cur.execute(add_event, [event[0] if event[0] != "" else None, event[1] if event[1] != "" else None, datetime.datetime.now(), event[60] if event[60] != "" else None,
                                event[5] if event[5] != "" else None, event[6] if event[6] != "" else None, event[7] if event[7] != "" else None, event[8] if event[8] != "" else None, event[9] if event[9] != "" else None, event[10] if event[10] != "" else None, event[11] if event[11] != "" else None, event[12] if event[12] != "" else None, event[13] if event[13] != "" else None, event[14] if event[14] != "" else None,
                                event[15] if event[15] != "" else None, event[16] if event[16] != "" else None, event[17] if event[17] != "" else None, event[18] if event[18] != "" else None, event[19] if event[19] != "" else None, event[20] if event[20] != "" else None, event[21] if event[21] != "" else None, event[22] if event[22] != "" else None, event[23] if event[23] != "" else None, event[24] if event[24] != "" else None,
                                event[25] if event[25] != "" else None, event[26] if event[26] != "" else None, event[27] if event[27] != "" else None, event[28] if event[28] != "" else None, event[29] if event[29] != "" else None,
                                event[30] if event[30] != "" else None, event[31] if event[31] != "" else None, event[32] if event[32] != "" else None, event[33] if event[33] != "" else None, event[34] if event[34] != "" else None,
                                event[35] if event[35] != "" else None, event[36] if event[36] != "" else None, event[37] if event[37] != "" else None, event[38] if event[38] != "" else None, event[39] if event[39] != "" else None, event[40] if event[40] != "" else None, event[41] if event[41] != "" else None, event[42] if event[42] != "" else None,
                                event[43] if event[43] != "" else None, event[44] if event[44] != "" else None, event[45] if event[45] != "" else None, event[46] if event[46] != "" else None, event[47] if event[47] != "" else None, event[48] if event[48] != "" else None, event[49] if event[49] != "" else None, event[50] if event[50] != "" else None,
                                event[51] if event[51] != "" else None, event[52] if event[52] != "" else None, event[53] if event[53] != "" else None, event[54] if event[54] != "" else None, event[55] if event[55] != "" else None, event[56] if event[56] != "" else None, event[57] if event[57] != "" else None, event[58] if event[58] != "" else None])

        conn.commit()


    # disconnect from server
    conn.close()



if __name__ == "__main__":
    gdelt_events = getGDELTEvents()
    commitGDELTEvents(gdelt_events)