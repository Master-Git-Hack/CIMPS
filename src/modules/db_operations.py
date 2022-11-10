from src.config.bd_services import cnxn

def schemas(type = 'assistance'):
    match type:
        case 'assistance':
            return open('src/schemas/assistance.sql').read()
        case 'workshop':
            return open('src/schemas/workshop.sql').read()
        case 'committee':
            return open('src/schemas/committee.sql').read()
        case  _:
            print('Type not specified')
            return False

def get_assistance():
    query = open('src/schemas/assistance.sql').read()
    if cnxn != False and query != False:
        with cnxn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            data = []
            for row in rows:
                data.append({
                    'id_constancia':row['constancia'],
                    'id_evento':row['id_evento'],
                    'id_tipo_constancia':row['id_tipo_constancia'],
                    'texto1':row['texto1'],
                    'nombre':row['totexto2'],
                    'texto3':row['texto3'],
                    'genero':row['genero'],
                    'cimps_ed':row['texto4'],
                    'email':row['email'],
                })
            return data 

def get_workshops():
    query = open('src/schemas/workshops.sql').read()
    if cnxn != False and query != False:
        with cnxn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            data = []
            for row in rows:
                if row['id']!=1:
                    data.append({
                        'id_constancia':row['id'],
                        'nombre':row['name'],
                        'genero':row['gender'],
                        'email':row['email'],
                        'lugar':'taller',
                        'puesto':'Asistente',
                        'titulo':row['taller']
                    })
            return data 

def update(data,filename,url):
    if cnxn!=False:
        with cnxn.cursor() as cursor:
            query=f"""
                UPDATE 
                    constancia 
                SET 
                    nombre_archivo='{filename}.pdf',
                    url='{url}',
                    generado=1 
                WHERE 
                    id={data['id_constancia']}
                    AND
                    id_tipo_constancia={data['id_tipo_constancia']}
            """
            cursor.execute(query)
            cnxn.commit()
