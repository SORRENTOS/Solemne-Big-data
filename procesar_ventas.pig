-- 1. Cargar las tres tablas desde la zona raw de HDFS
transactions = LOAD '/user/cloudera/solemne01/raw/transactions.csv' USING PigStorage(',') AS (
    transaction_id:int, 
    store_id:int, 
    product_id:int, 
    quantity:int, 
    date:chararray, 
    total:float
);

stores = LOAD '/user/cloudera/solemne01/raw/stores.csv' USING PigStorage(',') AS (
    store_id:int, 
    store_name:chararray, 
    city:chararray
);

products = LOAD '/user/cloudera/solemne01/raw/products.csv' USING PigStorage(',') AS (
    product_id:int, 
    product_name:chararray, 
    category:chararray, 
    unit_price:float
);

-- 2. CRUZAR Transacciones con Sucursales para obtener el nombre y ciudad
t_stores = JOIN transactions BY store_id, stores BY store_id;

-- Agrupar por tienda para calcular ingresos totales y transacciones por local
grouped_stores = GROUP t_stores BY (stores::store_id, stores::store_name, stores::city);
store_revenue = FOREACH grouped_stores GENERATE 
    group.store_id AS store_id,
    group.store_name AS store_name,
    group.city AS city,
    COUNT(t_stores) AS total_transacciones,
    ROUND(SUM(t_stores.transactions::total)*100)/100 AS ingreso_total;

-- Ordenar de mayor a menor ingreso (aquí identificas cuál tienda vende más)
ordered_stores = ORDER store_revenue BY ingreso_total DESC;
STORE ordered_stores INTO '/user/cloudera/solemne01/results/ingreso_por_tienda' USING PigStorage(',');


-- 3. CRUZAR Transacciones con Productos para ver las unidades vendidas de cada uno
t_prods = JOIN transactions BY product_id, products BY product_id;

grouped_prods = GROUP t_prods BY (products::product_id, products::product_name, products::category);
product_sales = FOREACH grouped_prods GENERATE 
    group.product_id AS product_id,
    group.product_name AS product_name,
    group.category AS category,
    SUM(t_prods.transactions::quantity) AS unidades_totales_vendidas,
    ROUND(SUM(t_prods.transactions::total)*100)/100 AS ingreso_total_producto;

-- Ordenar los productos más vendidos por cantidad de unidades
ordered_products = ORDER product_sales BY unidades_totales_vendidas DESC;
STORE ordered_products INTO '/user/cloudera/solemne01/results/unidades_por_producto' USING PigStorage(',');