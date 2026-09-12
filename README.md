# Solemne-Big-data

Desarrollo del equipo MISH

## comandos para cambios de de archivos datasets

### 1. Subir y sobrescribir los archivos CSV actualizados en HDFS (reemplaza la ruta local según corresponda)

hadoop fs -put -f /home/cloudera/workspace/nuevos_datos/transactions.csv /user/cloudera/solemne01/raw/
hadoop fs -put -f /home/cloudera/workspace/nuevos_datos/stores.csv /user/cloudera/solemne01/raw/
hadoop fs -put -f /home/cloudera/workspace/nuevos_datos/products.csv /user/cloudera/solemne01/raw/

### 2. Eliminar las carpetas de resultados anteriores en HDFS (obligatorio para que Pig pueda sobrescribir)

hadoop fs -rm -r /user/cloudera/solemne01/results/ingreso_por_tienda
hadoop fs -rm -r /user/cloudera/solemne01/results/unidades_por_producto

### 3. Volver a ejecutar el script de Pig para procesar la nueva información con MapReduce

pig -x mapreduce analisis_avanzado.pig

## Como entrar a hue

1. ingresar a http://localhost:8888
2. el usuario es cloudera y cloudera
3. seleccionar hive o impala
4. jugar con sql
