with

source as (
    select * from
    {{ source('projeto_jaffle_shop', 'stores')}}
),      -- Pegando todos os dados da nossa tabela items.

rename as (
    select

        ------------- ids
        id as store_id,

        ------------- text
        name as location,

        ------------- numerics
        tax_rate,

        ------------- timestamp
        {{ dbt.date_trunc('day', 'opened_at') }} as opened_date


    from source
)       -- Renomeando colunas desejadas assim melhorando estrutura para ánalises.

select * from rename
