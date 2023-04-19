BEGIN;
--
-- Add field stream to student
--
ALTER TABLE "students_student" ADD COLUMN "stream_id" bigint NULL REFERENCES "stream_stream" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "students_student_stream_id_890b539a" ON "students_student" ("stream_id");
COMMIT;
