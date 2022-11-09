import psycopg2
from config import host,user, password, db_name

connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

cursor = connection.cursor()
cursor.execute('''SELECT notebooks_brand.title ,COUNT (ALL brand_id)
FROM notebooks_notebook
JOIN notebooks_brand
ON notebooks_notebook.brand_id = notebooks_brand.id
GROUP BY notebooks_brand.title
ORDER BY count DESC''')
k = cursor.fetchall()
print(k)



