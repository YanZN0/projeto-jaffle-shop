with

source as (
    select * from
    {{ source('projeto_jaffle_shop', 'supplies')}}
),      -- Pegando todos os dados da nossa tabela items.

rename as (
    select

        ------------- ids
        id as supplies_id,
        sku as product_id,

        ------------- text
        name as product_name,
        perishable as product_available,

        ------------- booleans
        {{ cents_to_dollars('cost') }} as product_cost



    from source
)       -- Renomeando colunas desejadas assim melhorando estrutura para ánalises.

select * from rename
