import sqlite3,time
SCHEMA="create table if not exists fact_sales(id integer primary key, sale_date text, product_id integer, amount real)"
def benchmark(rows=10000):
 db=sqlite3.connect(":memory:");db.execute(SCHEMA);db.executemany("insert into fact_sales(sale_date,product_id,amount) values(?,?,?)",((f"2026-01-{i%28+1:02d}",i%100,float(i%500)) for i in range(rows)));db.commit()
 start=time.perf_counter();db.execute("select product_id,sum(amount) from fact_sales where sale_date>=? group by product_id",("2026-01-15",)).fetchall();before=time.perf_counter()-start
 db.execute("create index ix_sales_date_product on fact_sales(sale_date,product_id)");start=time.perf_counter();db.execute("select product_id,sum(amount) from fact_sales where sale_date>=? group by product_id",("2026-01-15",)).fetchall();after=time.perf_counter()-start
 return {"without_index_ms":before*1000,"with_index_ms":after*1000}
if __name__=="__main__":print(benchmark())