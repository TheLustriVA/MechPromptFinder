create table if not exists identities(
	id UUID primary key not null,
	uuid UUID,
	user_oid character(24),
	author_id character(18),
	agent_id varchar(50)
	);

create table if not exists prompts(
	prompt_id integer primary key generated always as identity,
	prompt text,
	constraint id
		foreign key(id)
			references identities(id)
	);

create table if not exists files(
	files_id integer primary key generated always as identity,
	filename varchar(250),
	docarray varchar(250),
	picture varchar(200),
	jpg varchar(200),
	constraint id
		foreign key(id)
			references identities(id)
	);
	
create table if not exists dimensions(
	dimension_id integer primary key generated always as identity,
	width integer,
	height integer,
	thumbnail-sizes integer[],
	gif_size_ratio varchar(10),
	gif_fps integer,
	constraint id
		foreign key(id)
			references identities(id)
	);

create table if not exists colors(
	color_id integer primary key generated always as identity,
	dominant_color integer[],
	palette integer[][],
	constraint id 
		foreign key(id)
			references identities(id)
	);

create table if not exists loss(
	loss_id integer primary key generated always as identity,
	loss integer[],
	constraint id
		foreign key(id)
			references identities(id)  
	);

create table if not exists timing(
	timing_id integer primary key generated always as identity,
	fd_timestamp timestamp without time zone,
	last_preview timestamp without time zone,
	time_completed timestamp without time zone,
	dt_timestamp timestamp without time zone,
	str_timestamp timestamp without time zone,
	last_seen timestampe without time zone,
	constraint id
		foreign key(id)
			references identities(id)
	);