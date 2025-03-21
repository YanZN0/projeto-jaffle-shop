with

source as (
    select * from
    {{ source('projeto_jaffle_shop', 'orders')}}
),

rename as (
    select
        ------------- ids
        id as order_id,
        customer as customer_id,
        store_id,

        ------------- timestamp
        ordered_at,

        ------------- booleans
        {{ cents_to_dollars('subtotal') }} as subtotal,
        {{ cents_to_dollars('tax_paid') }} as tax_paid,
        {{ cents_to_dollars('order_total') }} as total_value

    from source
)       -- Renomeando colunas desejadas assim melhorando estrutura para ánalises.

select * from rename
