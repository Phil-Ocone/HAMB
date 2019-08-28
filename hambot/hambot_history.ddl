CREATE TABLE public.hambot_history
(
    manifest character varying(200) COLLATE pg_catalog."default" NOT NULL,
    test character varying(200) COLLATE pg_catalog."default" NOT NULL,
    status character varying(50) COLLATE pg_catalog."default" NOT NULL,
    source_connection character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "source count" bigint NOT NULL,
    target_connection character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "target count" bigint NOT NULL,
    diff numeric(500,2) NOT NULL,
    warning_threshold numeric(500,4) NOT NULL,
    failure_threshold numeric(500,4) NOT NULL,
    environment character varying(50) COLLATE pg_catalog."default" NOT NULL,
    created_time timestamp without time zone NOT NULL,
    uuid uuid NOT NULL,
    CONSTRAINT hambot_history_pkey PRIMARY KEY (uuid)
)