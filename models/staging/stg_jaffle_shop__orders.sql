with

source as (
    select * from
    {{ source('projeto_jaffle_shop', 'orders')}}
),

rename as (
    select
        id as order_id
        customer as customer_id
        ordered_at,
        store_id,
        subtotal,
        tax_paid,
        order_total,
        {{ cents_to_dollar('subtotal') }} as subtotal,
        {{ cents_to_dollar('tax_paid') }} as tax_paid,
        {{ cents_to_dollar('order_total') }} as total_value

    from * source
)
