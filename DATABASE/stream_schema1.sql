BEGIN;
--
-- Create model Stream
--
CREATE TABLE "stream_stream" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL);
CREATE TABLE "stream_stream_students" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "stream_id" bigint NOT NULL REFERENCES "stream_stream" ("id") DEFERRABLE INITIALLY DEFERRED, "student_id" bigint NOT NULL REFERENCES "students_student" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "stream_stream_students_stream_id_student_id_1fe310b7_uniq" ON "stream_stream_students" ("stream_id", "student_id");
CREATE INDEX "stream_stream_students_stream_id_8773bc48" ON "stream_stream_students" ("stream_id");
CREATE INDEX "stream_stream_students_student_id_570bc329" ON "stream_stream_students" ("student_id");
COMMIT;
