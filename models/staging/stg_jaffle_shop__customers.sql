
with

source as (
    select * from
    {{ source('projeto_jaffle_shop', 'customers')}}
),      -- Pegando todos os dados da nossa tabela customers.

rename as (
    select
        ------------- ids
        id as client_id,

        ------------- text
        name as client_name

    from source
)       -- Renomeando colunas desejadas assim melhorando estrutura para ánalises.


select * from rename
