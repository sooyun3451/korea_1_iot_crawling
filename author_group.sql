insert into author_group_tb
select 
	0,
    webtoon_id,
    author_id
from 
	webtoon_tb wt
    left outer join author_tb at on(wt.author like concat('%', at.author_name, '%'))