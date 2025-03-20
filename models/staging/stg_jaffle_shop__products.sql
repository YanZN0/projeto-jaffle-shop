
with

source as (
    select * from
    {{ source('projeto_jaffle_shop', 'products')}}
),      -- Pegando todos os dados da nossa tabela customers.

rename as (
    select
        ------------- ids
        sku as product_id,

        ------------- text
        name as product_name,
        type as type_product,
        description as product_description,

        ------------- numerics
        {{ cents_to_dollars('price') }} as price_product

    from source
)       -- Renomeando colunas desejadas assim melhorando estrutura para ánalises.


select * from rename
