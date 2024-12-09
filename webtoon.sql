select 
	wt.webtoon_id,
    wt.title,
    group_concat(at.author_name separator ' / ') as author,
    wt.rating,
    wt.img_url,
    wt.category_id,
    ct.category_name
from 
	webtoon_tb wt
    left outer join author_group_tb agt on(agt.webtoon_id = wt.webtoon_id)
    left outer join author_tb at on(at.author_id = agt.author_id)
    left outer join category_tb ct on(ct.category_id = wt.category_id)
group by
	wt.webtoon_id,
    wt.title,
    wt.rating,
    wt.img_url,
    wt.category_id,
    ct.category_name