CREATE SCHEMA IF NOT EXISTS app_schema;

ALTER DATABASE mindspark SET search_path TO app_schema, public;

COMMENT ON DATABASE mindspark IS 'Main database for MindSpark'
