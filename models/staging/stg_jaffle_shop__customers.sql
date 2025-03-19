
with

source as (
    select * from
    {{ source('projeto_jaffle_shop', 'customers')}}
),      -- Pegando todos os dados da nossa tabela customers.

rename as (
    select
        id as client_id,
        name as client_name
    from source
)       -- Renomeando colunas desejadas.


select * from rename
