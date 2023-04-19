BEGIN;
--
-- Add field slug to stream
--
CREATE TABLE "new__stream_stream" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "slug" varchar(50) NOT NULL UNIQUE, "name" varchar(255) NOT NULL);
INSERT INTO "new__stream_stream" ("id", "name", "slug") SELECT "id", "name", '11' FROM "stream_stream";
DROP TABLE "stream_stream";
ALTER TABLE "new__stream_stream" RENAME TO "stream_stream";
COMMIT;
