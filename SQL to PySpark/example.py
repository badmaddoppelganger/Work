

execute("SELECT house_area\
        FROM eda_sql\
        WHERE house_area < 9\
        GROUP BY house_area\
        ORDER BY house_area ASC\
        ")

execute("SELECT due_time\
        FROM eda_sql\
        GROUP BY due_time\
        ORDER BY due_time DESC\
        ")

execute("SELECT total_floors\
        FROM eda_sql\
        GROUP BY total_floors\
        ORDER BY total_floors ASC\
        ")

execute("SELECT object_type_str\
        FROM eda_sql\
        GROUP BY object_type_str\
        ORDER BY object_type_str DESC\
        ")

execute("SELECT metro\
        FROM eda_sql\
        GROUP BY metro\
        ORDER BY metro ASC\
        ")

execute("SELECT residential_complex_name, count(residential_complex_name)\
        FROM eda_sql\
        GROUP BY residential_complex_name\
        ORDER BY count(residential_complex_name) DESC\
        ")

execute("SELECT living_area, count(living_area)\
        FROM eda_sql\
        GROUP BY living_area\
        ORDER BY living_area DESC\
        ")

execute("SELECT land_category, count(land_category)\
        FROM eda_sql\
        GROUP BY land_category\
        ORDER BY count(land_category) DESC\
        ")

execute("SELECT ad_id, count(ad_id)\
        FROM eda_sql\
        GROUP BY ad_id\
        ORDER BY count(ad_id) DESC\
        ")

execute("SELECT id, area, description\
        FROM eda_sql\
        WHERE id = 13461558\
        ")

execute("SELECT location2, count(location2)\
        FROM eda_sql\
        GROUP BY location2\
        ORDER BY count(location2) DESC")

execute("SELECT id, location\
        FROM eda_sql\
        ORDER BY location")

execute("SELECT source, count(source)\
        FROM eda_sql\
        GROUP BY source\
        ORDER BY source ASC")

execute("SELECT source_id\
        FROM eda_sql\
        GROUP BY source_id\
        ORDER BY source_id ASC")

execute("SELECT source_id\
        FROM eda_sql\
        GROUP BY source_id\
        ORDER BY source_id DESC")

execute("SELECT type\
        FROM eda_sql\
        GROUP BY type\
        --WHERE type IS NOT NULL\
        --ORDER BY person DESC")

execute("SELECT id, description\
        FROM eda_sql\
        WHERE description LIKE 'x%'\
        --ORDER BY person DESC")

execute("SELECT id, description\
        FROM eda_sql\
        WHERE description LIKE '1'\
        --ORDER BY person DESC")

execute("SELECT id, person\
        FROM eda_sql\
        WHERE person LIKE '*%'\
        ORDER BY person DESC")

execute("SELECT id, person\
        FROM eda_sql\
        WHERE person LIKE '1%'\
        ORDER BY person DESC")

execute("SELECT id, phone\
        FROM eda_sql\
        WHERE phone >1\
        ORDER BY phone DESC")

execute("SELECT id, price\
        FROM eda_sql\
        WHERE price >30000000\
        ORDER BY price DESC")

execute("SELECT id, price\
        FROM eda_sql\
        WHERE price = 9 OR price = 99 OR price = 999\
        ORDER BY price asc")
execute("SELECT object_sub_type, count(object_sub_type)\
        FROM eda_sql\
        GROUP BY object_sub_type\
        --ORDER BY title DESC")

execute("SELECT id\
        , title\
        FROM eda_sql\
        WHERE title not like '1%'\
        ORDER BY title DESC")

execute("SELECT id\
        , title\
        FROM eda_sql\
        WHERE title not like ' %'\
        AND title IS NOT NULL\
        ORDER BY title ASC")

execute("SELECT id\
        , url\
        FROM eda_sql\
        WHERE url not like 'https%'\
        ORDER BY url DESC")

execute("SELECT id\
        , url\
        FROM eda_sql\
        WHERE url not like 'http%'\
        ORDER BY url DESC")

#for col in eda_df.columns:
#    execute("select count(distinct("+ col + ")) from eda_sql")

