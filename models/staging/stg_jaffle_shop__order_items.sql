with

source as (
    select * from
    {{ source('projeto_jaffle_shop', 'items')}}
),      -- Pegando todos os dados da nossa tabela items.

rename as (
    select

        ------------- ids
        id as order_item_id,
        order_id,
        sku as product_id

    from source
)       -- Renomeando colunas desejadas assim melhorando estrutura para ánalises.

select * from rename
