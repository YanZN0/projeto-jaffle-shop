with

order_last_mount as (
    select o.order_id, o.ordered_at


    from {{ ref('stg_jaffle_shop__orders') }} o
    where o.ordered_at >= '2017-08-01' and o.ordered_at < '2017-09-01'

),      -- SubQuery de filtro para pegar resultados com datas específicas, no nosso caso irei pegar datas do último mês de agosto de 2017.

order_last_mount_products as (
    select od.order_id, ol.ordered_at, od.product_id

    from order_last_mount ol
    left join {{ ref('stg_jaffle_shop__order_items')}} od ON od.order_id = ol.order_id
    order by ol.ordered_at

),      -- Subquery com objetivo de um LEFT JOIN entre as views para pegarmos só os pedidos da order_items do mês de agosto de 2017

jaffle_filter as (
    select ol.order_id, ol.ordered_at, ol.product_id, p.type_product, p.price_product

    from order_last_mount_products ol
    left join {{ ref('stg_jaffle_shop__products') }} p ON ol.product_id = p.product_id
    where p.type_product = 'jaffle'

),      -- Fazendo um filtro entre as datas para que, nos resulte em datas específicas com produtos jaffles.


most_requested_jaffle as (
    select
        jf.type_product,
        jf.product_id,
        jf.price_product,
        count(*) as most_requested,
        DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS ranking_most_requested
    from jaffle_filter jf
    group by jf.type_product, jf.product_id, jf.price_product
    order by ranking_most_requested

),      -- Contando as linhas iguais de (product_id), e fazendo um RANK para rankearmos os jaffles mais pedidos do mês de agosto.


jaffle_best_selling as (
    select jf.type_product, jf.product_id, p.product_name, p.product_description,
        sum(jf.price_product * jf.most_requested) total_value_of_all_orders

    from most_requested_jaffle jf
    left join {{ ref('stg_jaffle_shop__products') }} p ON jf.product_id = p.product_id
    group by jf.type_product, jf.product_id, p.product_name, p.product_description
    order by total_value_of_all_orders desc
    limit 1

)

select * from jaffle_best_selling

-- Essa KPI poderia ajudar a Jaffle Shop tomar decisões estratégicas mais certeiras tanto no négocio quanto no marketing. Essa KPI nos mostra o resultado do produto mais vendido no mês passado, é simples mas com ela poderiamos entender mais o que os clientes na loja.

-- Também com essa KPI tem uma informação importante no meio dela, no meio do código conseguimos ver os produtos que são mais pedidos, assim entendendo o que os clientes mais gostam assim podendo fazer promoções, propagandas gerando mais interesse em novos e antigos clientes.
